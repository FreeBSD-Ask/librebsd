# DuckDB 2.0.0 单库迁移试验：导出／导入等价性与成本

> **2026-10-24 更正（存储版本号口径）**：本报告正文关于“2.0.0 新库文件头为 999”“2.0.0 没有可返回存储版本的 SQL 接口”
> 等表述系误读。DuckDB 2.0.0 的 `MainHeader.version_number` 已弃用、固定写 `StorageVersion::DEPRECATED = 999`
> （源码 `src/include/duckdb/storage/storage_info.hpp`），真实存储版本存于 `DatabaseHeader.storage_compatibility`，
> 官方编号为 **69（v2.0.0）**。正确读法是 `SELECT tags FROM duckdb_databases()` 取 `storage_version` 键；
> 实测复核 26 个正式库：25 个 `v2.0.0+`、`changelog` 为 `v1.0.0+`，与官方 64／69 完全吻合，无异常。
> **正文保留原始记录不作改写；与本节冲突处以本节为准。** 详见 `ADR-0017` §15 与 `流程规则.md`“存储版本的读取口径”。

- 执行日期：2026-10-24
- 依据：`.trae/specs/upgrade-duckdb-to-2-0-0-20261024/spec.md`（2.0.0 迁移试验批）
- 执行者：工程执行会话（AI）
- 纪律声明：全程未对任何现网库做写操作（`EXPORT DATABASE` 走 `read_only=True` 连接，逐表 `count(*)`／抽样亦为只读）；未复制任何 `.duckdb` 文件；未创建 `.bak`／`prebak*` 等旁路副本；未改动全局 duckdb（仍为 1.5.5）；未触碰 `05-卷册大纲/`；未做 git 操作。`IMPORT DATABASE` 目标全程在沙箱内。

## 一、结论摘要

1. **等价性成立**：最大 OFFICIAL 库 `netbsd.duckdb`（2 446 602 240 字节，9 表 29 273 016 行）经“1.5.5 导出 → 2.0.0 导入”后，表数／表清单／逐表行数／列定义／约束／索引／视图／元数据表全文／两张代表表前 100 行 sha256 **全部一致**，无一处 FAIL。
2. **成本很低**：本库（2.28 GiB）导出 13.18 秒、导入 37.45 秒，全流程含校验约 1 分钟。26 库（9.83 GiB）按实测吞吐线性外推约 5 分钟纯计算，留余量按 6—15 分钟计。
3. **新库更小**：2.0.0 写出的库 2 289 315 840 字节，较 1.5.5 原库 **−6.43%**；导出体 815 939 502 字节（约为原库 0.333 倍）。
4. **可量产**：脚本化后无人工判断点。唯一必须先办的工程动作是改 `duckdb-version-baseline.txt` 并经 ADR 变更基线——现行分析脚本的版本探测在 2.0.0 下按设计 FAIL（rc=2）。
5. **无数据级 API 断裂**：`analyze_all_databases.py` 的 `analyze_schema()`／`analyze_git_commits()` 核心逻辑在 2.0.0 下运行无异常，输出与 1.5.5 逐项相同。差异仅剩运行时内置宏集合与库文件体积两类非数据项（见 §七）。

## 二、试验对象

按 `duckdb-2.0-migration-inventory.tsv` 的 `category=OFFICIAL` 行按 `bytes` 降序，最大者为 `netbsd.duckdb`（2 446 602 240 字节）；次大 `linux-kernel.duckdb`（2 137 534 464 字节）未启用。该库只读连接未报 `LOCKED`，无占用问题。

| 项目 | 值 |
| ---- | -- |
| 试验库 | `03-原始史料库/01-代码仓库史料/03-NetBSD/db/duckdb/netbsd.duckdb` |
| 原库字节 | 2446602240（2.28 GiB） |
| 表数／总行数 | 9 表／29273016 行 |
| 最大表 | `main.commit_files` 27271149 行；`main.commits` 1999412 行 |
| 导出工具 | 全局 `C:/Python314/python.exe`，duckdb 1.5.5 |
| 导入工具 | 沙箱 venv `script/_duckdb2_trial/venv2`，duckdb 2.0.0（`duckdb-2.0.0-cp312-abi3-win_amd64.whl`，abi3 故可装于 Python 3.14.2） |
| 安装源 | 清华镜像＋`--proxy ""`（本机代理 `127.0.0.1:7890` 直连会 `ConnectionResetError(10054)`，与前批一致） |
| D 盘起始可用 | 291357425664 字节（271.35 GiB） |

## 三、方法与命令

```text
C:/Python314/python.exe -m venv script/_duckdb2_trial/venv2
script/_duckdb2_trial/venv2/Scripts/python.exe -m pip install --proxy "" -i https://pypi.tuna.tsinghua.edu.cn/simple duckdb==2.0.0
C:/Python314/python.exe script/_duckdb2_trial/probe_schema.py <原库> script/_duckdb2_trial/probe_old.json
C:/Python314/python.exe script/_duckdb2_trial/export_step.py <原库> script/_duckdb2_trial/export script/_duckdb2_trial/export_log.json
script/_duckdb2_trial/venv2/Scripts/python.exe script/_duckdb2_trial/import_step.py script/_duckdb2_trial/export script/_duckdb2_trial/migrated.duckdb script/_duckdb2_trial/import_log.json
C:/Python314/python.exe script/_duckdb2_trial/equiv_dump.py <原库> script/_duckdb2_trial/equiv_old.json
script/_duckdb2_trial/venv2/Scripts/python.exe script/_duckdb2_trial/equiv_dump.py script/_duckdb2_trial/migrated.duckdb script/_duckdb2_trial/equiv_new.json
C:/Python314/python.exe script/_duckdb2_trial/compare_equiv.py <两侧 JSON> script/_duckdb2_trial/equiv_table.md
script/_duckdb2_trial/venv2/Scripts/python.exe script/_duckdb2_trial/run_analysis_check.py script/_duckdb2_trial/migrated.duckdb
C:/Python314/python.exe script/_duckdb2_trial/run_analysis_check.py <原库>
```

等价取证的固定口径：同一份 `equiv_dump.py` 由两个版本各自执行，输出结构完全对称的 JSON，再由不依赖 duckdb 的 `compare_equiv.py` 比对。抽样哈希取 `SELECT * FROM <表> ORDER BY ALL LIMIT 100`（排序稳定后再逐行以 `\x1f` 连接、`\x1e` 分界喂 sha256；`NULL` 记为专有记号、`BLOB` 转 hex），代表表选 `main.commits`（核心大表，1 999 412 行）与 `main.db_meta`（元数据表全 7 行）。

## 四、耗时与体积

| 阶段 | 工具版本 | 耗时（秒） | 产物字节 |
| ---- | -------- | ---------- | -------- |
| `EXPORT DATABASE ... (FORMAT PARQUET)` | 1.5.5 | 13.18 | 815939502 |
| `IMPORT DATABASE ...` | 2.0.0 | 37.45 | 2289315840 |
| 等价取证（原库侧） | 1.5.5 | 4.1 | — |
| 等价取证（迁移库侧） | 2.0.0 | 0.8 | — |
| 分析脚本核心校验（每侧一次） | 1.5.5／2.0.0 | 各 0.5 | — |

导出体构成：9 个 `.parquet` ＋ `schema.sql` ＋ `load.sql`，共 11 个文件；`schema.sql` 内含 9 条 `CREATE TABLE` 与 2 条 `CREATE INDEX`，**无** `CREATE MACRO`（本库无用户宏）。

实测吞吐：导出约 185.6 MB/s（按原库字节／导出耗时），导入约 61.1 MB/s（按新库字节／导入耗时）。

## 五、等价对照表

| 校验项 | 结果 | 说明 |
| ------ | ---- | ---- |
| 表数 `duckdb_tables()` | PASS | 1.5.5=9／2.0.0=9 |
| 表清单 | PASS | 9 表逐一相同 |
| 逐表行数 | PASS | 9 表全部一致，合计 29273016 行 |
| 列定义（名称／类型／可空） | PASS | 9 表逐列相同（`duckdb_columns()`，按 `column_index` 排序） |
| 约束 `duckdb_constraints()` | PASS | 0 条，两侧相同 |
| 索引 `duckdb_indexes()` | PASS | 2 条，两侧相同 |
| 视图 `duckdb_views()`（非 internal） | PASS | 0 个，两侧相同 |
| `db_meta` 全文（`schema_meta` 等价物） | PASS | 7 行；`sha256=453bcddc19d01fbf…` 两侧一致（本库无 `schema_meta` 表，改以 `db_meta` 作等价物） |
| 抽样 `main.commits` 前 100 行 sha256 | PASS | 100 行；`sha256=b833e4c595a2fa4a…` 一致 |
| 抽样 `main.db_meta` 前 100 行 sha256 | PASS | 7 行；`sha256=453bcddc19d01fbf…` 一致 |
| 宏名集（运行时内置宏） | 信息项 | 1.5.5=131／2.0.0=140，差异全属运行时内置宏，非库内对象，见 §七 |
| 库文件体积 | 信息项 | 2446602240 → 2289315840（−6.43%） |

FAIL 项：**0**。`宏名集` 在机读比对中标记为 FAIL，经复核判定为运行时口径差异而非数据丢失：`schema.sql` 无任何 `CREATE MACRO`，导出体不含宏，差集为 2.0.0 新增的 `assert_true`／`if`／`json_copy_strftime_if_date`／`json_copy_strftime_if_timestamp`／`variant_group_array` 与移除的 `round_even`／`roundbankers`。

## 六、2.0.0 下的门禁／分析脚本结果

`analyze_all_databases.py` 无单库参数（整跑会扫描全部 26 库与邮件子库），故按其原函数对迁移库单库复刻：`require_duckdb_version()`、`analyze_schema()`、`analyze_git_commits()`。

| 检查项 | 结果 | 说明 |
| ------ | ---- | ---- |
| 版本基线探测 | 按预期拦截 | 1.5.5 → rc=0；2.0.0 → rc=2（`[FAIL] duckdb 版本不一致：实际 2.0.0／期望 1.5.5`），基线文件 `duckdb-version-baseline.txt` 与 ADR-0017 设计如此 |
| `analyze_schema()` | PASS | 9 表结构／行数／列与 1.5.5 侧逐一相同，无异常 |
| `analyze_git_commits()` | PASS | `total_commits=1999412`、`total_authors=490`、`top_authors` 前十、`date_range=None` 均与 1.5.5 侧相同，无异常 |

## 七、峰值磁盘占用与总耗时

- **峰值占用**（导出体与新库同时存在时）：815939502 ＋ 2289315840 ＝ **3 105 255 342 字节（2.89 GiB）**；计入 venv（57 550 002 字节）为 3 162 805 344 字节（2.95 GiB）。即单库迁移需临时空间 ≈ 原库的 **1.27 倍**（导出 0.333×＋新库 0.936×）。
- **试验总耗时**：venv 创建＋安装约 1 分钟；迁移与校验实测合计约 56 秒（13.18＋37.45＋4.1＋0.8＋1.0）；含脚本调试与报告约 25 分钟。**结论用的量产耗时只取迁移与校验实测段。**

## 八、结论

### 8.1 是否可量产

可以。单库迁移链路为“只读导出 → 新版导入 → 等价取证”，全部为确定性脚本动作，无人工判断点；本次在最大库上零 FAIL，小库只会更快。量产前置条件两条：

1. 按 ADR 变更 `duckdb-version-baseline.txt` 至 2.0.0（否则所有分析脚本一律 rc=2 拒跑）；
2. 保留 1.5.5 导出的 `export` 体或既有 `12-数据库备份/` 归档作为回滚路径——1.5.5 无法读取 2.0.0 写出的库（前批实测：存储版本 999 超出 1.5.5 可读区间 64—68）。

### 8.2 耗时估算

- 单库（2.28 GiB，本批实测）：导出 13.18 s ＋ 导入 37.45 s ＋ 校验约 5 s ≈ **56 秒**。
- 26 库串行（OFFICIAL 合计 9.83 GiB）：按吞吐线性外推，导出约 57 s、导入约 173 s、校验约 40 s，合计约 **4.5—5 分钟**纯计算；计入 26 次进程启动、IO 抖动与最大库（`netbsd`）占主导的偏斜，实际按 **6—15 分钟** 预留。磁盘临时峰值以最大单库为准（约 3.1 GB），271 GiB 余量充裕，可串行亦可逐库清理后滚动。

### 8.3 需注意的 API／行为差异

1. **版本基线门禁**：2.0.0 下 `analyze_all_databases.py` 等一律 rc=2（设计如此，非缺陷）；量产须先改基线并经 ADR 记录。
2. **`EXPORT/IMPORT DATABASE` 不吃参数绑定**：`IMPORT DATABASE ?`／`EXPORT DATABASE ?` 在两个版本下均报 `ParserException: syntax error at or near "?"`（本次脚本初版即因此报错一次）；路径须内联字面量并转义单引号，建议统一转正斜杠。
3. **目录函数列名**：`duckdb_tables()`／`duckdb_views()` 的 schema 列是 `schema_name`（而 `information_schema.tables` 是 `table_schema`）；误用报 `BinderException`，两版一致。
4. **内置宏集合随运行时变化**（131 → 140）：新增 `assert_true`／`if`／`json_copy_strftime_if_date`／`json_copy_strftime_if_timestamp`／`variant_group_array`，移除 `round_even`／`roundbankers`。与库数据无关；但**若项目脚本按宏名做存在性判断（如依赖 `roundbankers`）需同批排查**。
5. **库文件体积 −6.43%**：迁移后备份归档体积亦可按同量级下降，但压缩档收益需另批实测，不能直接套用。
6. **未覆盖面**：本批只验证了数据等价与单库分析函数；未验证扩展（`json`／`icu` 等）装载差异、并发读写、`.wal` 存在时的导入路径，亦未验证 26 库全量串行的失败回滚编排。

## 九、产物与清理

- 报告：本文件。
- 临时环境：`script/_duckdb2_trial/`（venv、导出体、`migrated.duckdb`、脚本与日志）已整体删除，`Test-Path` 复测为空。D 盘可用空间：删除前 286396084224 字节，删除后 289546104832 字节，回收 3150020608 字节（与实测峰值 2.95 GiB 吻合）。
- 门禁：第十件 `audit_markdown_lint.py` PASS（闸面 149 文件 0 问题）、第二十四件 `audit_md_quote_glyphs.py` PASS（直角引号 0 处）、第三十六件 `audit_sidecar_backup.py` PASS（违规 0 件）。
- 未触碰：任何现网 `.duckdb`（含本次只读打开的 `netbsd.duckdb`）、`05-卷册大纲/`、`12-数据库备份/`；全局 duckdb 未升级；无 git 操作。
