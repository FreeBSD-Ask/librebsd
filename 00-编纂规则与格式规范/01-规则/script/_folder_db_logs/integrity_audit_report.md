# 文件夹级数据库完整性复核报告

> 生成时间：2026-10-06 12:09:45 BJT
> 模式：全量复核

## 汇总表

| db_name | dangling_db_records | unindexed_disk_files | sha256_mismatch |
|---|---|---|---|
| sacred_sources | 0 | 0 | 0 |
| original_sources | 0 | 0 | 0 |
| research_notes | 0 | 0 | 0 |
| fact_checks | 0 | 0 | 0 |
| review_reports | 0 | 0 | 0 |
| cross_indexes | 0 | 0 | 0 |
| metadata_interfaces | 0 | 0 | 0 |
| **合计** | **0** | **0** | **0** |

## 详情：dangling_db_records

无

## 详情：unindexed_disk_files

无

## 详情：sha256_mismatch

无

## 建议动作

### dangling_db_records

- 建议：从数据库删除记录（`python script/build_folder_databases.py --update-file <path>` 或手动 DELETE）
- 影响数量：0

### unindexed_disk_files

- 建议：使用 `python script/build_folder_databases.py --add-file <path>` 入库
- 影响数量：0

### sha256_mismatch

- 建议：使用 `python script/build_folder_databases.py --update-file <path>` 刷新
- 影响数量：0
