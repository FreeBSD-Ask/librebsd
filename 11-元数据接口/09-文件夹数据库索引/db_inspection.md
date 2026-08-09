# 文件夹级数据库检查报告

> 生成时间：2026-08-01T13:07:02
> 数据库数量：7
> 反映 Schema 1.4 格式统一后的状态（索引命名统一 + 扩展表合并 + 引用查询加速索引）
>
> **2026-08-04 更新**：本报告覆盖范围为 7 个文件夹级数据库。本次数据库全面优化（详见 `dashboard.md`“数据库全面优化记录”）对 7 库无结构变更（编号/路径/索引核验通过）；独立库 `资料数据库.db` 已按 Schema v1.4 对齐（新增 5 通用表 + schema_meta，旧 cross_references 改名 material_cross_references），`references_fulltext.db` 删除 2 张零依赖空表并统一 schema_meta，详见 `folder_db_registry.csv`（已追加独立库行）。

## 概览

| 数据库 | 路径 | 业务表数 | 文件数 | 大小 |
| --- | --- | --- | --- | --- |
| sacred_sources | `02-sacred源材料/sacred_sources.db` | 7 | 50 | 3.97 MB |
| original_sources | `03-原始史料库/original_sources.db` | 9 | 602 | 15.19 MB |
| research_notes | `04-现代研究文献/research_notes.db` | 7 | 1792 | 259.06 MB |
| fact_checks | `07-事实核查记录/fact_checks.db` | 7 | 41 | 2.56 MB |
| review_reports | `08-核查报告与多轮复核/review_reports.db` | 8 | 54 | 540.00 KB |
| cross_indexes | `10-交叉索引/cross_indexes.db` | 10 | 53 | 628.00 KB |
| metadata_interfaces | `11-元数据接口/metadata_interfaces.db` | 10 | 12 | 3.38 MB |

## 各数据库表结构

### sacred_sources

路径：`02-sacred源材料/sacred_sources.db`
SHA-256：`5edac48f5e36df316b9132f86c9aefd1e5590e9f7674b77c33e526ec0f074d33`
大小：4165632 字节（3.97 MB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 50 |
| deleted_files | 0 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:08 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 7 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 3065 |
| blocks_fts | 3065 |
| cross_references | 627 |
| files | 50 |
| schema_meta | 9 |
| sqlite_sequence | 4 |
| update_log | 9 |

#### blocks (3065 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (3065 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### cross_references (627 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (50 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### sqlite_sequence (4 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### update_log (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`


### original_sources

路径：`03-原始史料库/original_sources.db`
SHA-256：`74d4791657620446c77568bb78d0a46a21be6bd76f6332f6868e278dbfb757a3`
大小：15929344 字节（15.19 MB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 1 |
| deleted_files | 601 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:09 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 9 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 7 |
| blocks_fts | 7 |
| cross_references | 0 |
| files | 602 |
| kaoju_records | 568 |
| schema_meta | 9 |
| security_vulnerabilities | 7 |
| sqlite_sequence | 6 |
| update_log | 10 |

#### blocks (7 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (7 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### cross_references (0 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (602 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### kaoju_records (568 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| source_verification | TEXT | 否 |  | 否 |
| cross_verification_method | TEXT | 否 |  | 否 |
| doubt_basis | TEXT | 否 |  | 否 |
| page_refs | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE kaoju_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    source_verification TEXT,
    cross_verification_method TEXT,
    doubt_basis TEXT,
    page_refs TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### security_vulnerabilities (7 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| record_type | TEXT | 否 |  | 否 |
| advisory_id | TEXT | 否 |  | 否 |
| project | TEXT | 否 |  | 否 |
| release_date | TEXT | 否 |  | 否 |
| affected_versions | TEXT | 否 |  | 否 |
| component | TEXT | 否 |  | 否 |
| severity | TEXT | 否 |  | 否 |
| cve_references | TEXT | 否 |  | 否 |
| cve_id | TEXT | 否 |  | 否 |
| published_date | TEXT | 否 |  | 否 |
| modified_date | TEXT | 否 |  | 否 |
| cvss_score | REAL | 否 |  | 否 |
| cvss_vector | TEXT | 否 |  | 否 |
| cwe | TEXT | 否 |  | 否 |
| affected_products | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE "security_vulnerabilities" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "file_id" INTEGER NOT NULL, "record_type" TEXT, "advisory_id" TEXT, "project" TEXT, "release_date" TEXT, "affected_versions" TEXT, "component" TEXT, "severity" TEXT, "cve_references" TEXT, "cve_id" TEXT, "published_date" TEXT, "modified_date" TEXT, "cvss_score" REAL, "cvss_vector" TEXT, "cwe" TEXT, "affected_products" TEXT)`

#### sqlite_sequence (6 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### update_log (10 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`


### research_notes

路径：`04-现代研究文献/research_notes.db`
SHA-256：`f0b2cfc3aa9be65f30218bf719d0f2aac8ce435d57a227b74757ea9f1829d2a6`
大小：271642624 字节（259.06 MB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 1789 |
| deleted_files | 0 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:11 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 7 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 486863 |
| blocks_fts | 486863 |
| cross_references | 18441 |
| files | 1792 |
| schema_meta | 9 |
| sqlite_sequence | 4 |
| update_log | 10 |

#### blocks (486863 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (486863 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### cross_references (18441 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (1792 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### sqlite_sequence (4 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### update_log (10 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`


### fact_checks

路径：`07-事实核查记录/fact_checks.db`
SHA-256：`d572d9c7399244bd621c4bc71a196b137d3a876d7d62b1bdbe833eb5a0398329`
大小：2686976 字节（2.56 MB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 0 |
| deleted_files | 41 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:11 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 7 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 0 |
| blocks_fts | 0 |
| cross_references | 17 |
| files | 41 |
| schema_meta | 9 |
| sqlite_sequence | 4 |
| update_log | 8 |

#### blocks (0 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (0 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### cross_references (17 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (41 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### sqlite_sequence (4 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### update_log (8 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`


### review_reports

路径：`08-核查报告与多轮复核/review_reports.db`
SHA-256：`c610c1aba857a1b79c98f5d10bd09fa090081d1df51e3e0ac121e7102631a5fc`
大小：552960 字节（540.00 KB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 4 |
| deleted_files | 50 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:11 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 8 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 38 |
| blocks_fts | 38 |
| cross_references | 16 |
| files | 54 |
| review_records | 14 |
| schema_meta | 9 |
| sqlite_sequence | 5 |
| update_log | 26 |

#### blocks (38 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (38 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### cross_references (16 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (54 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### review_records (14 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| record_type | TEXT | 否 |  | 否 |
| dispute_name | TEXT | 否 |  | 否 |
| parties | TEXT | 否 |  | 否 |
| period | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| positions | TEXT | 否 |  | 否 |
| evidence | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 否 |  | 否 |
| reviewer | TEXT | 否 |  | 否 |
| review_round | TEXT | 否 |  | 否 |
| submission_date | TEXT | 否 |  | 否 |
| verdict | TEXT | 否 |  | 否 |
| comments | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE "review_records" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "file_id" INTEGER NOT NULL, "record_type" TEXT, "dispute_name" TEXT, "parties" TEXT, "period" TEXT, "summary" TEXT, "positions" TEXT, "evidence" TEXT, "resolution_status" TEXT, "reviewer" TEXT, "review_round" TEXT, "submission_date" TEXT, "verdict" TEXT, "comments" TEXT)`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### sqlite_sequence (5 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### update_log (26 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`


### cross_indexes

路径：`10-交叉索引/cross_indexes.db`
SHA-256：`59d615c9f18eaa4a19398a5950bfb4ea2c5ff9436401a42d2cd134c6479155e1`
大小：643072 字节（628.00 KB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 2 |
| deleted_files | 51 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:11 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 10 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 21 |
| blocks_fts | 21 |
| concept_history | 21 |
| cross_references | 15 |
| files | 53 |
| person_records | 7 |
| schema_meta | 9 |
| sqlite_sequence | 7 |
| terminology_index | 13 |
| update_log | 10 |

#### blocks (21 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (21 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### concept_history (21 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| concept_name | TEXT | 否 |  | 否 |
| etymology | TEXT | 否 |  | 否 |
| history_summary | TEXT | 否 |  | 否 |
| related_concepts | TEXT | 否 |  | 否 |
| page_refs | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE concept_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    concept_name TEXT,
    etymology TEXT,
    history_summary TEXT,
    related_concepts TEXT,
    page_refs TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### cross_references (15 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (53 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### person_records (7 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| record_type | TEXT | 否 |  | 否 |
| person_name | TEXT | 否 |  | 否 |
| normalized_name | TEXT | 否 |  | 否 |
| aliases | TEXT | 否 |  | 否 |
| role | TEXT | 否 |  | 否 |
| biography_summary | TEXT | 否 |  | 否 |
| page_refs | TEXT | 否 |  | 否 |
| biography | TEXT | 否 |  | 否 |
| academic_genealogy | TEXT | 否 |  | 否 |
| affiliations | TEXT | 否 |  | 否 |
| works | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE "person_records" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "file_id" INTEGER NOT NULL, "record_type" TEXT, "person_name" TEXT, "normalized_name" TEXT, "aliases" TEXT, "role" TEXT, "biography_summary" TEXT, "page_refs" TEXT, "biography" TEXT, "academic_genealogy" TEXT, "affiliations" TEXT, "works" TEXT)`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### sqlite_sequence (7 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### terminology_index (13 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| record_type | TEXT | 否 |  | 否 |
| command_name | TEXT | 否 |  | 否 |
| manual_section | TEXT | 否 |  | 否 |
| category | TEXT | 否 |  | 否 |
| description | TEXT | 否 |  | 否 |
| page_refs | TEXT | 否 |  | 否 |
| term | TEXT | 否 |  | 否 |
| translation | TEXT | 否 |  | 否 |
| definition | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE "terminology_index" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "file_id" INTEGER NOT NULL, "record_type" TEXT, "command_name" TEXT, "manual_section" TEXT, "category" TEXT, "description" TEXT, "page_refs" TEXT, "term" TEXT, "translation" TEXT, "definition" TEXT)`

#### update_log (10 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`


### metadata_interfaces

路径：`11-元数据接口/metadata_interfaces.db`
SHA-256：`0c266bd13ba0fc2fb5a59e01fcdad08129f65b990da5cb089d380918404cc095`
大小：3543040 字节（3.38 MB）
Schema 版本：1.4
journal_mode：wal
integrity_check：ok

#### schema_meta 键值对

| key | value |
| --- | --- |
| active_files | 2 |
| deleted_files | 10 |
| ghost_blocks_cleaned | 0 |
| journal_mode | wal |
| last_optimize_at | 2026-08-01T13:06:50 |
| last_vacuum_at | 2026-08-01T11:11:12 |
| pragma_optimized_at | 2026-08-01T11:37:58 |
| schema_version | 1.4 |
| table_count | 10 |

#### 触发器

- `trigger_blocks_fts_ad`
- `trigger_blocks_fts_ai`
- `trigger_blocks_fts_au`

#### cross_references 索引（5 个，v1.4 命名统一 + 引用查询加速）

- `idx_cross_references_reference_type`
- `idx_cross_references_resolution_status`
- `idx_cross_references_source_block_id`
- `idx_cross_references_source_file_id`
- `idx_cross_references_target_path`

#### files 索引

- `idx_files_content_hash`
- `idx_files_duplicate_of_db`
- `idx_files_duplicate_of_id`
- `idx_files_sha256`
- `idx_files_status`
- `sqlite_autoindex_files_1`

#### 各业务表行数

| 表名 | 行数 |
| --- | --- |
| blocks | 9822 |
| blocks_fts | 9822 |
| build_citation_records | 4 |
| chapter_metadata | 346 |
| cross_references | 0 |
| files | 12 |
| schema_meta | 9 |
| sqlite_sequence | 6 |
| timeline_records | 18 |
| update_log | 14 |

#### blocks (9822 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| block_index | INTEGER | 是 |  | 否 |
| block_type | TEXT | 是 |  | 否 |
| block_level | INTEGER | 否 |  | 否 |
| block_content | TEXT | 是 |  | 否 |
| block_line_start | INTEGER | 否 |  | 否 |
| block_line_end | INTEGER | 否 |  | 否 |
| block_char_offset_start | INTEGER | 否 |  | 否 |
| block_char_offset_end | INTEGER | 否 |  | 否 |
| heading_anchor | TEXT | 否 |  | 否 |
| block_metadata | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### blocks_fts (9822 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| file_id |  | 否 |  | 否 |
| block_id |  | 否 |  | 否 |
| content |  | 否 |  | 否 |

CREATE 摘要：`CREATE VIRTUAL TABLE blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
)`

#### build_citation_records (4 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| record_type | TEXT | 否 |  | 否 |
| target | TEXT | 否 |  | 否 |
| last_build | TEXT | 否 |  | 否 |
| last_success | TEXT | 否 |  | 否 |
| last_failure | TEXT | 否 |  | 否 |
| status | TEXT | 否 |  | 否 |
| reference_id | TEXT | 否 |  | 否 |
| citation_count | INTEGER | 否 |  | 否 |
| cited_in_chapters | TEXT | 否 |  | 否 |
| last_cited | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE "build_citation_records" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "file_id" INTEGER NOT NULL, "record_type" TEXT, "target" TEXT, "last_build" TEXT, "last_success" TEXT, "last_failure" TEXT, "status" TEXT, "reference_id" TEXT, "citation_count" INTEGER, "cited_in_chapters" TEXT, "last_cited" TEXT)`

#### chapter_metadata (346 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| chapter_id | TEXT | 否 |  | 否 |
| volume | TEXT | 否 |  | 否 |
| chapter | TEXT | 否 |  | 否 |
| title | TEXT | 否 |  | 否 |
| word_count | INTEGER | 否 |  | 否 |
| main_thread | TEXT | 否 |  | 否 |
| status | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE chapter_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    chapter_id TEXT,
    volume TEXT,
    chapter TEXT,
    title TEXT,
    word_count INTEGER,
    main_thread TEXT,
    status TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### cross_references (0 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| source_file_id | INTEGER | 是 |  | 否 |
| source_block_id | INTEGER | 否 |  | 否 |
| reference_type | TEXT | 是 |  | 否 |
| reference_text | TEXT | 是 |  | 否 |
| target_path | TEXT | 否 |  | 否 |
| target_db | TEXT | 否 |  | 否 |
| target_record_id | INTEGER | 否 |  | 否 |
| target_anchor | TEXT | 否 |  | 否 |
| resolution_status | TEXT | 是 | 'pending' | 否 |
| reference_context | TEXT | 否 |  | 否 |
| resolved_at | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (s ...`

#### files (12 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_path | TEXT | 是 |  | 否 |
| filename | TEXT | 是 |  | 否 |
| folder_path | TEXT | 是 |  | 否 |
| file_extension | TEXT | 是 |  | 否 |
| file_size | INTEGER | 是 |  | 否 |
| sha256 | TEXT | 是 |  | 否 |
| content_hash | TEXT | 是 |  | 否 |
| line_count | INTEGER | 否 |  | 否 |
| char_count | INTEGER | 否 |  | 否 |
| encoding | TEXT | 是 | 'utf-8' | 否 |
| line_ending | TEXT | 是 | 'lf' | 否 |
| mtime | TEXT | 是 |  | 否 |
| ingested_at | TEXT | 是 |  | 否 |
| title | TEXT | 否 |  | 否 |
| summary | TEXT | 否 |  | 否 |
| frontmatter | TEXT | 否 |  | 否 |
| status | TEXT | 是 | 'active' | 否 |
| duplicate_of_id | INTEGER | 否 |  | 否 |
| duplicate_type | TEXT | 否 |  | 否 |
| duplicate_of_db | TEXT | 否 |  | 否 |
| duplicate_of_global_file_id | INTEGER | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summar ...`

#### schema_meta (9 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| key | TEXT | 否 |  | 是 |
| value | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT)`

#### sqlite_sequence (6 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| name |  | 否 |  | 否 |
| seq |  | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE sqlite_sequence(name,seq)`

#### timeline_records (18 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 是 |  | 否 |
| event_date | TEXT | 否 |  | 否 |
| event_description | TEXT | 否 |  | 否 |
| event_type | TEXT | 否 |  | 否 |
| source_chapter | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE timeline_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    event_date TEXT,
    event_description TEXT,
    event_type TEXT,
    source_chapter TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
)`

#### update_log (14 行)

| 列名 | 类型 | 非空 | 默认值 | 主键 |
| --- | --- | --- | --- | --- |
| id | INTEGER | 否 |  | 是 |
| file_id | INTEGER | 否 |  | 否 |
| operation | TEXT | 是 |  | 否 |
| field_changed | TEXT | 是 |  | 否 |
| old_value | TEXT | 否 |  | 否 |
| new_value | TEXT | 否 |  | 否 |
| timestamp | TEXT | 是 |  | 否 |
| operated_by | TEXT | 是 |  | 否 |
| notes | TEXT | 否 |  | 否 |

CREATE 摘要：`CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
)`

