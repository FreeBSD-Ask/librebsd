# DuckDB 2.0 迁移 · 既有归档覆盖与回退演练（Task 5）

口径：**不为本迁移新建任何备份**（spec“回退保障”“磁盘预算约束”）。回退体一律取 `12-数据库备份/` 既有归档；归档体是 `EXPORT DATABASE (FORMAT PARQUET)` → tar → gzip 的逻辑导出，并非 DuckDB 单文件。

## 一、覆盖总览

- SCOPE 正式库：**26** 个；有归档 **26** 个；**NO_ARCHIVE 0** 个。
- 归档槽合计 **96** 份，压缩态合计 **5,996,738,253** 字节（5.58 GiB）。
- 每份归档均有同名 `.json` 清单（`json_pair_ok` 全 True）；清单 `integrity` 全为 `ok`、`archive_verified` 全为 True。

## 二、逐库归档覆盖表

| 库 | 源库字节 | 归档目录 | 槽数 | 最新归档 | 归档时间 | gz 字节 | manifest |
| -- | -------- | -------- | ---- | -------- | -------- | ------- | -------- |
| bsd-derivatives | 1,306,537,984 | 有 | 1 | 20261024_150928.duckdb.gz | 2026-10-24 15:09:28 | 318,170,524 | ok / True |
| causal_graph | 2,371,584 | 有 | 6 | 20261024_150559.duckdb.gz | 2026-10-24 15:05:59 | 6,751 | ok / True |
| changelog | 40,644,608 | 有 | 6 | 20261024_150555.duckdb.gz | 2026-10-24 15:05:55 | 19,927,807 | ok / True |
| cross_indexes | 9,449,472 | 有 | 6 | 20261024_150649.duckdb.gz | 2026-10-24 15:06:49 | 553,353 | ok / True |
| cross_source_identity | 1,323,008 | 有 | 1 | 20261024_151016.duckdb.gz | 2026-10-24 15:10:16 | 4,950 | ok / True |
| darwin | 16,003,072 | 有 | 1 | 20261024_151018.duckdb.gz | 2026-10-24 15:10:18 | 3,078,376 | ok / True |
| doubts_standalone | 349,974,528 | 有 | 6 | 20261024_150643.duckdb.gz | 2026-10-24 15:06:43 | 44,619,226 | ok / True |
| dragonfly | 300,167,168 | 有 | 1 | 20261024_150914.duckdb.gz | 2026-10-24 15:09:14 | 98,833,576 | ok / True |
| fact_checks | 1,847,296 | 有 | 6 | 20261024_150649.duckdb.gz | 2026-10-24 15:06:49 | 11,625 | ok / True |
| freebsd | 1,125,134,336 | 有 | 1 | 20261024_150650.duckdb.gz | 2026-10-24 15:06:50 | 303,084,099 | ok / True |
| historical_claims | 643,837,952 | 有 | 6 | 20261024_145133.duckdb.gz | 2026-10-24 14:51:33 | 230,655,042 | ok / True |
| illumos-gate | 35,926,016 | 有 | 1 | 20261024_151017.duckdb.gz | 2026-10-24 15:10:17 | 5,899,526 | ok / True |
| linux-kernel | 2,137,534,464 | 有 | 1 | 20261024_151019.duckdb.gz | 2026-10-24 15:10:19 | 528,944,086 | ok / True |
| metadata_interfaces | 2,633,728 | 有 | 6 | 20261024_150650.duckdb.gz | 2026-10-24 15:06:50 | 272,133 | ok / True |
| netbsd | 2,446,602,240 | 有 | 1 | 20261024_150728.duckdb.gz | 2026-10-24 15:07:28 | 561,881,206 | ok / True |
| openbsd | 321,662,976 | 有 | 1 | 20261024_150901.duckdb.gz | 2026-10-24 15:09:01 | 99,112,592 | ok / True |
| openssh | 12,857,344 | 有 | 1 | 20261024_151018.duckdb.gz | 2026-10-24 15:10:18 | 2,233,618 | ok / True |
| openssh-apple | 2,895,872 | 有 | 1 | 20261024_151018.duckdb.gz | 2026-10-24 15:10:18 | 55,736 | ok / True |
| openzfs | 51,916,800 | 有 | 1 | 20261024_150927.duckdb.gz | 2026-10-24 15:09:27 | 7,532,256 | ok / True |
| original_sources | 11,546,624 | 有 | 6 | 20261024_150557.duckdb.gz | 2026-10-24 15:05:57 | 1,463,602 | ok / True |
| phoronix_news | 1,847,296 | 有 | 6 | 20261024_150556.duckdb.gz | 2026-10-24 15:05:56 | 63,824 | ok / True |
| references_fulltext | 1,547,448,320 | 有 | 6 | 20261024_150600.duckdb.gz | 2026-10-24 15:06:00 | 353,644,297 | ok / True |
| research_notes | 156,774,400 | 有 | 6 | 20261024_150557.duckdb.gz | 2026-10-24 15:05:57 | 21,838,917 | ok / True |
| review_reports | 5,255,168 | 有 | 6 | 20261024_150649.duckdb.gz | 2026-10-24 15:06:49 | 342,314 | ok / True |
| sacred_sources | 4,730,880 | 有 | 6 | 20261024_150556.duckdb.gz | 2026-10-24 15:05:56 | 769,691 | ok / True |
| 资料数据库 | 16,789,504 | 有 | 6 | 20261024_150556.duckdb.gz | 2026-10-24 15:05:56 | 3,819,914 | ok / True |

说明：`manifest` 列为清单内 `integrity` 与 `archive_verified` 两字段（备份时写入，本次未逐份重跑）。

## 三、抽样归档校验（调用原函数 verify_archive()）

校验方式：**直接 import 并调用** `00-编纂规则与格式规范/01-规则/脚本与命令/backup_databases.py` 中的 `verify_archive(gz_path, expect_tables)`，**非复刻**。三段判据：①解 gzip 到 EOF（CRC）②读 tar 成员并核 parquet 数 ≥ 表数 ③逐个 parquet 由 DuckDB 加载计数。`expect_tables` 取当前源库的 `information_schema` 表数（非清单值），以同时验证清单与现状一致。

| 库 | 抽样归档 | gz 字节 | 源库表数 | 清单表数 | 结果 | detail |
| -- | -------- | ------- | -------- | -------- | ---- | ------ |
| fact_checks | 20261024_150649.duckdb.gz | 11,625 | 5 | 5 | PASS | verified: 5 tables / 81 rows |
| cross_indexes | 20261024_150649.duckdb.gz | 553,353 | 10 | 10 | PASS | verified: 10 tables / 3840 rows |
| original_sources | 20261024_150557.duckdb.gz | 1,463,602 | 7 | 7 | PASS | verified: 7 tables / 1320 rows |

三个抽样分属三种样本：最小库（`fact_checks`）、索引库（`cross_indexes`）、史料库（`original_sources`）；**3/3 PASS**。

## 四、回退演练（从既有归档重灌，即删）

- 演练库：`fact_checks`（26 个正式库中体积最小，源库 1,847,296 字节 ≈ 1.76 MiB）。
- 归档：`12-数据库备份/fact_checks/20261024_150649.duckdb.gz`（11,625 字节）。
- 沙箱：`script/_duckdb2_drill/`（目录名不含被清扫模式；流程结束整目录删除）。
- 重灌方式：解 gzip → 解 tar → `IMPORT DATABASE`（DuckDB 恢复入口，内部执行 `schema.sql` 后 `load.sql` 并改写 parquet 路径）。

| 判据 | 结果 | 明细 |
| ---- | ---- | ---- |
| 表清单一致 | PASS | 源 5 表／演练 5 表 |
| 每表行数一致 | PASS | blocks=0、cross_references=17、files=41、schema_meta=11、update_log=12 |
| 抽样 100 行校验和一致 | PASS | 逐表 `SELECT * … ORDER BY ALL LIMIT 100` 序列化后 sha256 前 32 位逐表相等 |

- 演练体占用 1,345,631 字节；删除后沙箱存在＝False。
- 磁盘可用空间：演练前 **291,322,925,056** 字节，删除后 **291,322,925,056** 字节，差值 **0** 字节（回落至演练前）。

**实测发现（须在恢复手册中体现，本批不改规则）**：归档内 `load.sql` 的 `COPY` 语句带**导出机绝对路径**（`C:/Users/ykla/AppData/Local/Temp/duckdb_bak_*/…`），且 `load.sql` 本身只有 `COPY`、无 `CREATE TABLE`。因此**单跑 `load.sql` 会失败**：先报 `Table with name … does not exist`，即便先建表也因路径失效而失败。正确恢复入口是 `IMPORT DATABASE '<解档目录>'`（本次实测其内部完成建表、路径改写与装载）。AGENTS.md 现行表述“恢复须跑档内 `load.sql`”宜后续修订为“`IMPORT DATABASE` 或 `schema.sql` + 改写路径后的 `load.sql`”——待 ykla 裁定。

## 五、NO_ARCHIVE 清单

**无。** 26 个正式库全部有归档（覆盖 100%），不存在 `NO_ARCHIVE` 候选，故本迁移无需为任何库补建备份。

## 六、纪律留痕

- 未新建任何备份、未复制任何库文件、未生成 `.bak`／`prebak*`／`*~` 副本；演练体只为解档重灌产物，且已删除。
- 未修改任何 `.duckdb`：源库仅以 `read_only` 打开；演练体是归档重灌出的新文件，位于 `script/` 沙箱内并已删除。
- 未改动 `05-卷册大纲/`、未提交 git。
