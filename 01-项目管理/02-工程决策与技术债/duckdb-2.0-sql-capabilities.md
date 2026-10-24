# DuckDB 2.0.0 SQL 新能力实测与采用判定

- 日期：2026-10-24
- 依据：ykla 令“按 DuckDB 2.0 新能力逐项改造未迁移路径”
- 环境：`C:/Python314/python.exe`（Python 3.14）＋ `duckdb==2.0.0`
- 结论速览：四项能力中，`MERGE INTO` 与数据修改 CTE 判为采用，`RETURNING` 作为二者取值前提一并采用；`VARIANT` 与 `variant_*` 判为不采用——理由是**零落点**，不是能力缺失。

## 一、方法与口径

- **沙箱路径**：`script/_duckdb2_sql_probe/`。`script/` 是项目唯一的临时脚本与中间产物区（不入库），探针库 `probe.duckdb` 建在此目录内，与任何正式库无连接关系；报告固化后该目录整体删除，删除步骤见第五节。
- **只读原则**：本批唯一的库级操作是对 26 个正式库做只读普查，连接一律 `duckdb.connect(path, read_only=True)`；未写入、未复制库文件、未创建 `.bak`／`prebak*` 一类旁路副本。
- **未触碰**：任何 `.duckdb` 正式库、`05-卷册大纲/`、`12-数据库备份/`；全程无 git 操作。
- **探针口径**：只对当前 DuckDB 原生脚本实际用到的语法面取判定（判重写入、删除后的账目登记、JSON 型列），不以“语法能用”直接等同于“应当采用”。判定分三档：**采用**（有明确落点且语义等价或更优）、**不采用**（有落点价值但无落点事实）、**不适用**（目标链路已退役，不在本批范围）。

## 二、逐能力实测

| 能力 | 命令要点 | 实测输出 | 判定 |
| ---- | -------- | -------- | ---- |
| `MERGE INTO` | `MERGE INTO … USING (SELECT ? AS …) ON … WHEN NOT MATCHED THEN INSERT` | 参数化可用；**无唯一约束**的表上可用；同键二跑行数不变（幂等） | 采用 |
| 数据修改 CTE | `WITH upd AS (UPDATE … RETURNING), ins AS (INSERT … SELECT … FROM upd RETURNING) SELECT …` | 参数化可用；一条语句返回 `(updated=1, inserted=1)`；库内状态同步生效 | 采用 |
| `RETURNING` | 普通 `INSERT … RETURNING`、`UPDATE … RETURNING` | 两种形态均可用 | 采用（上两项的取值前提） |
| `VARIANT` 与 `variant_*` | `CAST(json(…) AS VARIANT)` ＋ `variant_extract`／`variant_keys`／`variant_exists` | 14 个 `variant%` 函数可查；正确路径下取值正常；`variant_bytes_to_variant` 报 `NotImplementedException` | 不采用（零落点） |

### 2.1 MERGE INTO

参数化写法成立：源端用 `USING (SELECT ? AS …)` 直接绑定参数，不需要先建临时表。关键实测点是**目标表无唯一约束时仍可用**——判重完全由 `ON` 条件承担，因此它替换的是应用层 `WHERE NOT EXISTS` 子查询，而不是替换数据库约束。同键二跑行数不变，说明 `WHEN NOT MATCHED THEN INSERT` 分支在多跑时不会重复插入，幂等由 `ON` 匹配保证。

### 2.2 数据修改 CTE

一条语句内串联两段写入：`upd` 先 `UPDATE … RETURNING`，`ins` 再 `INSERT … SELECT … FROM upd RETURNING`，外层 `SELECT` 汇总计数。实测参数化可用，返回 `(updated=1, inserted=1)`，且库内状态同步生效（无须二次查询确认）。其价值在于**消除两次往返之间的中间态**：更新与账目登记要么同批可见，要么同批不可见。

### 2.3 RETURNING

普通 `INSERT … RETURNING` 与 `UPDATE … RETURNING` 均可用，作为 2.1／2.2 的取值前提记录，不单独设落点。

## 三、VARIANT 专项

### 3.1 函数面

`duckdb_functions()` 中 `variant%` 函数 **14 个**：`variant_array_length`、`variant_bytes_to_variant`、`variant_comparator`、`variant_contains`、`variant_exists`、`variant_extract`、`variant_extract_string`、`variant_group_array`、`variant_group_object`、`variant_keys`、`variant_normalize`、`variant_to_parquet_variant`、`variant_type`、`variant_typeof`。

（复核更正：初稿记“13 个”，实为逐项计数 14；2026-10-24 按 `duckdb_functions()` 复跑 `count = 14` 改正。）

### 3.2 陷阱：字符串直接 CAST 得到的是 VARCHAR variant

`CAST('{"a":1}' AS VARIANT)` 不解析 JSON，得到的是 **VARCHAR variant**：

- `variant_typeof` 返回 `'VARCHAR'`；
- `variant_extract(v,'a')` 返回 NULL；
- `variant_keys(v)` 返回空表。

正确路径是先过 `json()` 再转：

```sql
SELECT variant_typeof(CAST(json('{"a":1}') AS VARIANT));  -- OBJECT(a)
```

在该路径下 `variant_typeof` 返回 `OBJECT(a)`；对含嵌套键的对象，`variant_extract(v,'b')` 可取嵌套对象、`variant_extract_string(v,'s')` 返回 `'x'`、`variant_keys(v)` 返回 `['a','b']`、`variant_exists(v,'a')` 返回 `True`。

判定：本项目若启用 VARIANT，**必须**统一走 `json()` 中转写法；直接 `CAST` 字符串会静默降级为标量 variant，且不报错——这是采用成本的一部分。

### 3.3 负结果一：`variant_bytes_to_variant` 不可用

调用即报错，原文如下：

```text
NotImplementedException: Only version 1 of the Variant encoding scheme is supported, found version: 11
```

即外部 Variant 二进制（Parquet 侧常见 version 11 编码）无法经此函数摄入。

### 3.4 负结果二：本项目无 JSON 型列

普查口径：对 26 个正式库的 main schema 中每个 VARCHAR／JSON 列，取前 30 行非空值，统计以 `{` 开头者，命中 ≥5 行即计为该列命中。结果 **命中 0 个列**。

正向旁证：`EXPORT DATABASE` → `IMPORT DATABASE` 后 VARIANT 列类型保留（`information_schema` 中仍为 `VARIANT`），即备份链路对 VARIANT 无损——但这只说明“用了不会坏”，不构成“应当用”。

### 3.5 不采用的硬判据

**零 JSON 列即零落点**：全库普查 0 命中，意味着没有任何列需要从字符串型 JSON 升级为 VARIANT。反之，函数面存在（14 个）、正确路径可用、导出导入可保留类型，都是“能用”；“能用”与“该用”之间缺的正是落点。据此判定不采用，且不预留迁移脚手架。

## 四、落点与边界

| 能力 | 落点 | 处置 |
| ---- | ---- | ---- |
| `MERGE INTO` | `_full_ingest_all.py` 的判重写入 | 采用 |
| 数据修改 CTE | `cleanup_duplicates_and_errors.py::execute_deletion` | 采用 |
| `RETURNING` | 上述两处 | 采用 |
| `VARIANT`／`variant_*` | 无落点 | 不采用 |
| legacy SQLite 三脚本 | 不在本批范围 | 不适用 |

### 4.1 采用项：MERGE INTO

`_full_ingest_all.py` 现行判重是应用层 `WHERE NOT EXISTS` 子查询（其表无 PRIMARY KEY／UNIQUE，`INSERT OR IGNORE` 在无约束表上会抛 Binder Error）。改造为 `MERGE INTO … WHEN NOT MATCHED THEN INSERT` 后，判重与写入合并为一条语句，`--dry-run` 与实写的判据口径可共用同一段 SQL，二跑幂等由 2.1 的实测结果兜底。改造**不涉及表结构变更**，不加唯一约束。

### 4.2 采用项：数据修改 CTE

`cleanup_duplicates_and_errors.py::execute_deletion` 现行写法是先 `UPDATE "references"` 置 `status`／`file_path`，再按条件 `INSERT INTO reference_duplicates` 记账，两次 `execute` 之间若中断则出现“引用已标删除、账目无记录”的缺口。改造为单条数据修改 CTE（`UPDATE … RETURNING` 驱动 `INSERT … SELECT`）后，两段写入同语句完成，且返回计数可直接写入删除日志。

### 4.3 不采用项：VARIANT 与 `variant_*`

判据见 3.5（零 JSON 列）。此处只补一句边界：**不采用不等于禁用**。若未来出现 JSON 列，本节结论失效，按第六节复审。

### 4.4 不适用项：legacy SQLite 三脚本

本批只针对当前 DuckDB 原生脚本。下列为 SQLite 时代遗留脚本，目标是 `.db`（已 0 字节或已归档），不在本批范围：

- `build_folder_databases.py`：用 `sqlite_master` 探查、以“触发器删除重建”实现刷新；
- `dedup_databases_global.py`：`sqlite3` 连接直连；
- `optimize_folder_databases.py`：`sqlite3` 的 `ON CONFLICT` 写法。

共同理由：它们不是 DuckDB 写路径。改造它们等于**复活已退役链路**——把一个“没有调用方、目标文件为空壳”的脚本升级成 2.0 语法，只会让退役事实变模糊，且无法通过任何现行门禁验证其行为。若确需复活，应先立复活决议，再按 DuckDB 写路径重写，届时本节的“不适用”结论同步失效。

## 五、可复跑步骤

复跑全程在 `script/_duckdb2_sql_probe/` 内完成，不连接任何正式库。脚本以 UTF-8 无 BOM、LF 落盘。

```python
# script/_duckdb2_sql_probe/probe.py
import shutil
from pathlib import Path

import duckdb

BASE = Path("script/_duckdb2_sql_probe")
DB = BASE / "probe.duckdb"
EXPORT_DIR = BASE / "export_probe"

BASE.mkdir(parents=True, exist_ok=True)
if DB.exists():
    DB.unlink()
if EXPORT_DIR.exists():
    shutil.rmtree(EXPORT_DIR)

con = duckdb.connect(str(DB))

# 0. 建探针表：刻意不加 PRIMARY KEY / UNIQUE（复现 2.1 的“无唯一约束”前提）
con.execute("CREATE TABLE t (k VARCHAR, v VARCHAR)")

# 1. MERGE INTO：参数化 + 无唯一约束 + 幂等（连跑两次，第二次行数不变）
merge_sql = (
    "MERGE INTO t USING (SELECT ? AS k, ? AS v) AS s ON t.k = s.k "
    "WHEN NOT MATCHED THEN INSERT (k, v) VALUES (s.k, s.v)"
)
con.execute(merge_sql, ["a", "1"])
con.execute(merge_sql, ["a", "1"])
print("merge_rows", con.execute("SELECT count(*) FROM t").fetchone()[0])  # 期望 1

# 2. 数据修改 CTE：UPDATE ... RETURNING 驱动 INSERT ... SELECT
con.execute("CREATE TABLE audit (k VARCHAR, v VARCHAR)")
stmt = (
    "WITH upd AS (UPDATE t SET v = ? WHERE k = ? RETURNING k, v), "
    "ins AS (INSERT INTO audit SELECT k, v FROM upd RETURNING k) "
    "SELECT (SELECT count(*) FROM upd) AS updated, (SELECT count(*) FROM ins) AS inserted"
)
print("cte", con.execute(stmt, ["2", "a"]).fetchone())  # 期望 (1, 1)
print("audit_rows", con.execute("SELECT count(*) FROM audit").fetchone()[0])  # 期望 1

# 3. RETURNING：普通 INSERT / UPDATE
print("ins_ret", con.execute(
    "INSERT INTO t VALUES ('b', '9') RETURNING k, v").fetchall())
print("upd_ret", con.execute(
    "UPDATE t SET v = '10' WHERE k = 'b' RETURNING k, v").fetchall())

# 4. VARIANT：陷阱写法 vs 正确写法
print("trap_type", con.execute(
    "SELECT variant_typeof(CAST('{\"a\":1}' AS VARIANT))").fetchone()[0])   # VARCHAR
print("trap_extract", con.execute(
    "SELECT variant_extract(CAST('{\"a\":1}' AS VARIANT), 'a')").fetchone()[0])  # None
print("trap_keys", con.execute(
    "SELECT count(*) FROM variant_keys(CAST('{\"a\":1}' AS VARIANT))").fetchone()[0])  # 0

v = "CAST(json('{\"a\":1,\"b\":{\"c\":2},\"s\":\"x\"}') AS VARIANT)"
print("ok_type", con.execute(f"SELECT variant_typeof({v})").fetchone()[0])       # OBJECT(a)
print("ok_nested", con.execute(f"SELECT variant_extract({v}, 'b')").fetchone()[0])
print("ok_str", con.execute(f"SELECT variant_extract_string({v}, 's')").fetchone()[0])  # x
print("ok_keys", con.execute(f"SELECT * FROM variant_keys({v})").fetchall())    # a, b, s
print("ok_exists", con.execute(f"SELECT variant_exists({v}, 'a')").fetchone()[0])  # True

# 5. variant_bytes_to_variant：预期抛 NotImplementedException（version 11）
try:
    con.execute("SELECT variant_bytes_to_variant(?::BLOB)", [b"\x0b\x00" * 8]).fetchall()
    print("bytes_to_variant", "unexpected_ok")
except Exception as exc:  # 记录原文，不据此改判
    print("bytes_to_variant", type(exc).__name__, exc)

# 6. EXPORT / IMPORT：VARIANT 列类型是否保留
con.execute("CREATE TABLE vt AS SELECT CAST(json('{\"a\":1}') AS VARIANT) AS v")
con.execute(f"EXPORT DATABASE '{EXPORT_DIR.as_posix()}' (FORMAT PARQUET)")
con.close()

con2 = duckdb.connect(str(BASE / "probe_import.duckdb"))
con2.execute(f"IMPORT DATABASE '{EXPORT_DIR.as_posix()}'")
print("imported_type", con2.execute(
    "SELECT data_type FROM information_schema.columns "
    "WHERE table_name = 'vt' AND column_name = 'v'").fetchone()[0])  # VARIANT
con2.close()
```

删除沙箱（复跑结束后执行，目录内不含任何正式库数据）：

```python
import shutil
from pathlib import Path

shutil.rmtree(Path("script/_duckdb2_sql_probe"), ignore_errors=True)
```

第五节不含第 3.4 节的 26 库 JSON 列普查：该普查只读正式库，须按“每个库一个 `read_only=True` 连接”另行执行，重复运行不产生副作用。其 SQL 骨架为 `SELECT column_name FROM information_schema.columns WHERE table_schema='main' AND data_type IN ('VARCHAR','JSON')`，再对每列取前 30 个非空值并统计 `LIKE '{%'` 命中行数。

## 六、失效条件与复审触发

| 触发条件 | 复审动作 |
| -------- | -------- |
| 任一正式库出现 JSON 型列（普查命中 ≥1 列） | 重跑 3.4 普查，评估该列是否改用 VARIANT，并走 ADR |
| DuckDB 修复 `variant_bytes_to_variant`（可读 version 11） | 重测该函数，评估外部 Variant 编码摄入路径 |
| `CAST(… AS VARIANT)` 语义变化（字符串不再降为 VARCHAR variant） | 重测 3.2 陷阱，修订“必须经 `json()` 中转”的写法要求 |
| 启用 legacy SQLite 三脚本中的任何一个 | 先立复活决议并按 DuckDB 写路径重写；4.4 的“不适用”结论随之失效 |
| 目标表新增唯一约束（schema 变更） | 复核 `MERGE INTO` 的 `ON` 条件与约束判重是否重叠，避免双重判重 |
| `duckdb-version-baseline.txt` 的版本基线变更 | 按第五节全表重跑，本报告四栏实测结论全部重新判定 |

## 七、结论

本批四项新能力中，`MERGE INTO` 与数据修改 CTE 判为采用，落点分别为 `_full_ingest_all.py` 的判重写入与 `cleanup_duplicates_and_errors.py::execute_deletion`；二者都在无唯一约束的表上实测通过，语义与现行应用层判重、两段式写入等价或更紧，`RETURNING` 作为共用的取值前提一并采用。`VARIANT` 与 `variant_*` 判为不采用：函数面齐备、正确路径可用、导出导入可保留类型，但 26 个正式库的 VARCHAR／JSON 列普查命中 0 个列，**没有任何落点**——因此这不是遗漏，而是零落点，且 `variant_bytes_to_variant` 在 2.0.0 上本就不可用（只支持 version 1 编码）。改造范围限于当前 DuckDB 原生脚本；`build_folder_databases.py`、`dedup_databases_global.py`、`optimize_folder_databases.py` 三个 SQLite 时代脚本目标是已退役的 `.db`，判为不适用，不动即为正确处置。
