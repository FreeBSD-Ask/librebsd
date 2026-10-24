# DuckDB 2.0 迁移 · 库清册汇总（Task 4）

扫描口径：`D:\librebsd` 全树 `*.duckdb`（含 `.git`／`node_modules`／`_tmp`／外部克隆／`12-数据库备份/`），共 **424** 个文件、**131,299,508,224** 字节（122.282 GiB）。

逐件明细见 `duckdb-2.0-migration-inventory.tsv`（UTF-8／LF，列：relpath、bytes、category、scope_match、note）。

## 三类计数与体量

| 类别 | 文件数 | 字节 | GiB | 判据 |
| ---- | ------ | ---- | --- | ---- |
| OFFICIAL | 26 | 10,553,712,640 | 9.829 | 路径与 `backup_databases.py` SCOPE 逐字命中 |
| EXTERNAL_CLONE | 0 | 0 | 0.000 | `03-原始史料库/02-man源与posix仓库/` 克隆树或 `.git` 内部 |
| TEMP_SANDBOX | 398 | 120,745,795,584 | 112.453 | 其余全部（非 SCOPE，不纳入迁移） |
| **合计** | **424** | **131,299,508,224** | **122.282** | 三类之和 == 实际清点数 |

判据自检（脚本内断言，全部通过）：OFFICIAL 计数 == SCOPE 计数（26）；三类之和 == 实际清点数（424）；SCOPE 26 条路径全部在磁盘命中（无缺失）。

## TEMP_SANDBOX 内部构成（按 note 前缀）

`category` 只有 spec 限定的三种取值；下表把非迁移面细分，避免把**内容库**误读为临时垃圾。

| 细分 | 文件数 | GiB | 说明 |
| ---- | ------ | --- | ---- |
| NON_SCOPE_CONTENT | 308 | 73.871 | 非 SCOPE 内容库（邮件列表分库 294、播客 10、login 1、ROW_MINE 派生 1、归档派生 2），有真实史料价值，**只是不迁移** |
| BACKUP_LAYER | 78 | 37.722 | `12-数据库备份/` 内的快照件（含 `historical_claims` 旧快照与 `tmp*` 残留目录），属备份层，不迁移 |
| TEMP | 12 | 0.860 | `_tmp`／`script` 内临时与试验件 |

## 与 spec 数字的差异（如实披露）

spec“Why”记 **346 个 `.duckdb`／86.6 GB**。本次实测全树 **424 个／122.28 GiB**；扣除 `12-数据库备份/` 内的 78 个快照件后恰为 **346** 个——即 spec 该数字不含备份层。体量差异另因邮件列表分库（294 个、72.9 GiB）已入库。

## 排除与边界说明

- `.git`／`node_modules` 已纳入遍历，命中 `*.duckdb` **0** 件（git 对象为打包压缩体，不以扩展名存在）。
- `03-原始史料库/02-man源与posix仓库/` 15 个克隆树内无 `*.duckdb`，故 EXTERNAL_CLONE 实为 **0** 件。
- `12-数据库备份/` 内发现既有旁路命名件（`*preb12fix2*`、`pre_*` 等），**本批不清扫**：删除该目录内容须 ykla 明示；按现状如实登记。
- 本批只读扫描，未打开任何库，未改动任何 `.duckdb`。

## NO_ARCHIVE 候选（衔接 Task 5）

**无。** 26 个 OFFICIAL 库在 `12-数据库备份/` 全部有归档，无 `NO_ARCHIVE` 候选；覆盖与抽样校验详见 `duckdb-2.0-archive-coverage.md`。
