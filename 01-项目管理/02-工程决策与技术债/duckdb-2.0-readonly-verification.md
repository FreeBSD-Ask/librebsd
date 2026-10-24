# DuckDB 2.0.0 只读兼容性与零改动验证

- 执行日期：2026-10-24
- 依据：`.trae/specs/upgrade-duckdb-to-2-0-0-20261024/spec.md` → `Requirement: 双版本只读验证`
- 执行者：工程执行会话（AI）
- 纪律声明：全程仅以 `duckdb.connect(path, read_only=True)` 打开正式库；未复制任何库文件、未创建 `.bak`／`prebak*` 副本、未改动全局 duckdb、未提交 git。

## 一、结论摘要

1. **可只读打开**：duckdb 2.0.0 对三个正式库（小／中／大三档，均在 `backup_databases.py` 的 SCOPE 之内）均只读连接成功并完成读查询，无 `LOCKED`。
2. **只读零改动**：三库字节数与 SHA-256 在连接前后完全相等，且未生成 `.wal` 文件；只读连接上的 `CREATE TABLE` 被内核拒绝。
3. **存储版本**：2.0.0 **没有**可返回“库文件存储版本号”的 SQL 接口（`duckdb_settings()` 的 `storage_compatibility_version` 只是会话设置 `latest`，`PRAGMA database_size` 只返回体积，`PRAGMA version` 只返回库引擎版本）。改用文件头实测：三个现有库的存储版本字段均为 **64**。
4. **与 spec 的口径差异（需核实）**：由 2.0.0 新建的空库，其存储版本字段实测为 **999**，而非 spec 记载的 69；1.5.5 读取该库时明确报“can only read versions between 64 and 68”。该差异按 0 信任原则挂出，不作为迁移判据采信，待以官方 storage 文档复核。

## 二、环境

- 隔离环境：`script/_duckdb2_verify/venv`（`C:/Python314/python.exe -m venv` 创建，Python 3.14.2，未使用系统 site-packages）。
- venv 内安装：`duckdb 2.0.0`（wheel `duckdb-2.0.0-cp312-abi3-win_amd64.whl`，abi3 故可在 3.14 装载）。
- 全局环境：`C:/Python314/python.exe` 仍为 `duckdb 1.5.5`，**未改动**。
- 网络说明：本机 `Internet Settings` 代理为 `127.0.0.1:7890`（`ProxyEnable=1`），直连该代理时 pip 报 `ProxyError ... ConnectionResetError(10054)`；改用 `--proxy ""` ＋ 清华镜像源后安装成功。此偏差已记录，安装源非官方 pypi。

## 三、方法与命令

```text
C:/Python314/python.exe -m venv script/_duckdb2_verify/venv
script/_duckdb2_verify/venv/Scripts/python.exe -m pip install --proxy "" -i https://pypi.tuna.tsinghua.edu.cn/simple duckdb==2.0.0
script/_duckdb2_verify/venv/Scripts/python.exe script/_duckdb2_verify/verify_ro.py
C:/Python314/python.exe script/_duckdb2_verify/header_probe.py
script/_duckdb2_verify/venv/Scripts/python.exe script/_duckdb2_verify/cross_version.py make
C:/Python314/python.exe script/_duckdb2_verify/cross_version.py open
```

每库的判定步骤：`sha256`＋字节数 → `connect(read_only=True)` → `SELECT count(*) FROM duckdb_tables()` → 存储版本探测 → `CREATE TABLE _ro_probe(x INT)` → 再算 `sha256`＋字节数。哈希按 8 MiB 分块流式计算，未整读入内存。

## 四、三库结果

| 库 | 角色 | 字节数 | 表数 | 只读打开 | 写入被拒 | SHA-256 前后一致 | 状态 |
| -- | ---- | ------ | ---- | -------- | -------- | ---------------- | ---- |
| `01-项目管理/00-变更记录/changelog.duckdb` | 小 | 40644608 | 2 | 是 | 是 | 是 | OK |
| `04-现代研究文献/historical_claims.duckdb` | 中（claim 唯一真值） | 643837952 | 34 | 是 | 是 | 是 | OK |
| `03-原始史料库/01-代码仓库史料/02-FreeBSD/db/duckdb/freebsd.duckdb` | 大 | 1125134336 | 11 | 是 | 是 | 是 | OK |

前后 SHA-256（相等即零改动）：

```text
changelog         1d7208bbeaad44187859c12fa9edc19d90bc4c48ae481fa5fe81f09837e6a6b7
historical_claims 4ff1b8806ab1a43d0977fd1a64e23c3d26a909664fd6cc9c9660a64250bfb412
freebsd           b48927c7cb21ed6200d6e6022dac43a0498ee297c1ffccbee2065d52c7381e4f
```

只读连接上写入被拒的原始报错（三库同型，仅库名不同）：

```text
InvalidInputException: Invalid Input Error: Cannot execute statement of type "CREATE"
on database "changelog" which is attached in read-only mode!
```

连接前后均无同名 `.wal` 文件（`wal_present_before=false`、`wal_present_after=false`）。

## 五、存储版本探测

### 5.1 官方接口：取不到明确版本号

| 探测语句 | 返回 | 是否给出存储版本 |
| -------- | ---- | ---------------- |
| `SELECT name, value FROM duckdb_settings() WHERE name ILIKE '%storage%'` | `default_secret_storage=local_file`、`logging_storage=memory`、`storage_block_prefetch=REMOTE_ONLY`、`storage_compatibility_version=latest` | 否（会话设置，非文件版本） |
| `SELECT current_setting('storage_compatibility_version')` | `latest` | 否 |
| `PRAGMA database_size` | 库名、`614.7 MiB`（historical_claims）等体积字段 | 否 |
| `PRAGMA version` | `v2.0.0`、`d54cbbe3df`、`Cyanoptera` | 否（引擎版本） |

结论：2.0.0 未向外暴露“该库文件存储版本 = N”的查询入口。此项**取不到**，不做猜测。

### 5.2 文件头经验比对（推定依据，非官方 API）

文档化的公开入口缺位，故以文件头字节做经验比对：字节 8–11 恒为 ASCII `DUCK`，字节 12 起的 `uint32`（小端）随写入引擎版本变化。为标定该字段位置，同一脚本先后用两个版本各新建一个空库（均落在 `script/_duckdb2_verify/tmp/`，探测后即删）。

| 样本 | 文件头前 16 字节（hex） | `DUCK` | `u32 @ 偏移 12` | 推定含义 |
| ---- | ----------------------- | ------ | --------------- | -------- |
| 现有 changelog / historical_claims / freebsd | `06d76f27c2dab3b94455434b40000000` | 是 | 64 | 存储版本 64 |
| 1.5.5 新建空库 | `06d76f27c2dab3b94455434b40000000` | 是 | 64 | 存储版本 64 |
| 2.0.0 新建空库 | `715b1fdc061e3d6c4455434be7030000` | 是 | 999 | 存储版本 999 |

三库前 16 字节与 1.5.5 新建库逐字节相同，故“现有库为版本 64”有直接比对支撑。

### 5.3 跨版本反向探测

以 2.0.0 建库（含 `CREATE TABLE probe AS SELECT 42 AS x`，274432 字节），再用全局 1.5.5 只读打开：

```text
IOException: IO Error: Trying to read a database file with version number 999, but we can only read
versions between 64 and 68.
The database file was created with an newer version of DuckDB.
```

该报错同时坐实两点：偏移 12 处确为存储版本字段；1.5.5 的可读区间为 64–68。由此，**spec 所记“2.0.0 用 storage version 69”与实测 999 不一致**，且由于 1.5.5 能读 64–68，若真有库落在 69，1.5.5 仍可读——“2.0 写出的库在 1.5.5 下不可读”这一表述本身仍成立，但成立原因是 999 超出 64–68，而非 69。两处均须在迁移前以官方 storage 文档复核。

## 六、结论

- **能否安全只读打开**：能。2.0.0 对三个 1.5.5 正式库（含 643 MB 与 1.07 GB 两档）只读打开并完成元数据与表计数查询，无异常、无锁冲突；官方“向后兼容读取”在此得到实测支持。
- **只读是否零改动**：是。三库 SHA-256 与字节数前后完全相等，无 WAL 生成，写操作被内核拒绝。故“只读打开不改变存储版本”这一 spec 场景在本批样本上成立，现行库仍为版本 64。
- **不可据此推广的部分**：本批只验证了连接、元数据查询与简单写拒绝；未验证扩展装载、大结果集查询、并发读写、`.wal` 存在时的恢复路径，也未验证 2.0.0 在 v64 库上执行 DDL／DML（那属写操作，本批明令禁止）。迁移仍应走“旧版导出 → 新版导入”，不得原地写入。

## 七、产物与清理

- 报告：本文件。
- 临时环境：`script/_duckdb2_verify/`（venv、验证脚本、`result.json`、临时库）在报告固化后整体删除，删除后复扫为空。
- 未触碰：任何 `.duckdb` 库文件、`05-卷册大纲/`、`12-数据库备份/`；未做任何 git 操作。
