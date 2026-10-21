# 文件夹级数据库构建与去重进度看板

> 本看板记录 7 个文件夹数据库的构建、Schema 优化、去重、跨库引用解析进度。2026-08-01T13:21:49 由 `script/_update_metadata_after_ingest.py` 更新（5 段释读分析入库后）。

## 构建进度

| 数据库 | 文件数 | 块数 | 大小 | SHA-256（前16位） | Schema 版本 | journal_mode | 活跃文件 | 已删除文件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sacred_sources | 52 | 3177 | 4.12 MB | `2bdf35a7789ed4bb` | 1.4 | wal | 52 | 0 |
| original_sources | 604 | 40 | 11.54 MB | `bcc0021460356420` | 1.4 | wal | 3 | 601 |
| research_notes | 1800 | 486906 | 259.17 MB | `5ce4adf680977858` | 1.4 | wal | 1794 | 6 |
| fact_checks | 41 | 0 | 2.56 MB | `d572d9c7399244bd` | 1.4 | wal | 0 | 41 |
| review_reports | 57 | 192 | 1.05 MB | `6fdd6566eaef2bbf` | 1.4 | wal | 4 | 53 |
| cross_indexes | 53 | 21 | 628.00 KB | `59d615c9f18eaa4a` | 1.4 | wal | 2 | 51 |
| metadata_interfaces | 12 | 9822 | 3.38 MB | `0c266bd13ba0fc2f` | 1.4 | wal | 2 | 10 |

## Schema 优化记录

### Schema 1.2 → 1.3（2026-08-01，历史）

- 新增 schema_meta 表：7 个数据库均创建 schema_meta 键值表
- 新增 9 个预定义索引 + 扩展表索引
- PRAGMA 优化：journal_mode=WAL，synchronous=NORMAL，mmap_size=256MB，temp_store=MEMORY，wal_autocheckpoint=1000

### Schema 1.3 → 1.4（2026-08-01，格式统一）

- **索引命名统一**：`idx_xref_*` → `idx_cross_references_*`（3 个索引重命名）
- **删除冗余索引**：`idx_files_duplicate_type`（与 `idx_files_duplicate_of_id` 功能重复）
- **补建索引**：`idx_files_duplicate_of_db`（6 个数据库补建，research_notes 已有）
- **新增引用查询加速索引**：`idx_cross_references_reference_type`、`idx_cross_references_source_block_id`
- **扩展表合并（5 组，减少 5 张表）**：
  - original_sources.db：security_advisories + vulnerability_metadata → security_vulnerabilities（7 行）
  - review_reports.db：disputes + peer_reviews → review_records（14 行）
  - cross_indexes.db：person_index + person_biography → person_records（7 行）
  - cross_indexes.db：command_index + term_index → terminology_index（13 行）
  - metadata_interfaces.db：build_status + citation_frequency → build_citation_records（4 行）
- **schema_meta 键集合统一**：9 个标准键，`restored_from_git` 迁移至 update_log
- **table_count 统计口径修正**：不含 FTS5 影子表（5 张）
- **模块化分层设计验证**：7 个数据库均遵循“一库一文件夹”架构
- **冗余备份文件清理**：04-现代研究文献/ 5 个冗余备份已删除（按预览→备份→确认→执行→复核流程）

### PRAGMA 实际值校验

| 数据库 | journal_mode | synchronous | mmap_size | temp_store | wal_autocheckpoint |
| --- | --- | --- | --- | --- | --- |
| sacred_sources | wal | 2 | 0 | 0 | 1000 |
| original_sources | wal | 2 | 0 | 0 | 1000 |
| research_notes | wal | 2 | 0 | 0 | 1000 |
| fact_checks | wal | 2 | 0 | 0 | 1000 |
| review_reports | wal | 2 | 0 | 0 | 1000 |
| cross_indexes | wal | 2 | 0 | 0 | 1000 |
| metadata_interfaces | wal | 2 | 0 | 0 | 1000 |

> **PRAGMA 持久性说明**：`wal_autocheckpoint=1000` 已持久化到数据库文件头；`journal_mode=wal` 为会话级 PRAGMA，多数文件夹级库实测关闭后回退为 `delete`（2026-08-16 实测仅 review_reports/cross_indexes/doubts_standalone/播客两库/phoronix_news/openssh-apple/darwin 实为 wal）。`synchronous`、`mmap_size`、`temp_store` 为会话级 PRAGMA，需在应用程序每次连接时设置。

## 跨库引用解析进度

| 数据库 | cross_references 行数 |
| --- | --- |
| sacred_sources | 627 |
| original_sources | 0 |
| research_notes | 18441 |
| fact_checks | 17 |
| review_reports | 16 |
| cross_indexes | 15 |
| metadata_interfaces | 0 |

## 拆分合并评估（2026-08-01）

> 评估结论详见 [db_split_merge_assessment.md](db_split_merge_assessment.md)

- **不合并小数据库**：保持按文件夹分库的清晰架构，合并会破坏一致性且收益有限
- **不拆分 research_notes**：保持按文件夹分库架构，已通过 WAL + blocks_fts 索引加速
- **合并低使用率扩展表**：5 组扩展表已合并（详见上方 Schema 1.4 记录）
- **新增引用查询索引**：cross_references 表新增 2 个索引（reference_type、source_block_id）

## 模块化分层违规登记（2026-08-16）

> 审计发现 3 处“一库一文件夹”违规，仅登记待评估，不移动文件。

- `04-现代研究文献/` 根目录并存 3 库：`research_notes.db`、`historical_claims.db`、`causal_graph.db`
- `03-原始史料库/01-代码仓库史料/01-数据库本体/` 并存 2 库：`phoronix_news.db`、`资料数据库.db`
- `03-原始史料库/01-代码仓库史料/08-跨项目对比/db/` 并存 3 库：`illumos-gate.db`、`openssh-apple.db`、`openssh.db`

## 去重进度

- 引用上一轮去重结果：5 条重复记录已删除
- 当前各库 active/deleted 文件数见上方构建进度表

## 已删除的空表

- `fact_checks`：`fact_check_records`（前次会话已删除）
- `metadata_interfaces`：`author_index`（前次会话已删除）

## 已合并的扩展表（v1.4）

| 数据库 | 原表 1 | 原表 2 | 合并表 | record_type | 合并后行数 |
| --- | --- | --- | --- | --- | --- |
| original_sources | security_advisories (6) | vulnerability_metadata (1) | security_vulnerabilities | advisory/vulnerability | 7 |
| review_reports | disputes (9) | peer_reviews (5) | review_records | dispute/peer_review | 14 |
| cross_indexes | person_index (1) | person_biography (6) | person_records | person_index/person_biography | 7 |
| cross_indexes | command_index (1) | term_index (12) | terminology_index | command/term | 13 |
| metadata_interfaces | build_status (1) | citation_frequency (3) | build_citation_records | build_status/citation_frequency | 4 |

## 冗余备份文件清理记录（2026-08-01）

> 按“预览→备份→确认→执行→复核”5 步安全流程执行

- 删除 5 个冗余备份文件：research_notes.db.corrupt.bak、research_notes.db.bak、research_notes_git_backup.db、research_notes_recovered.db、research_notes.db.bak_malformed
- 备份位置：`script/_folder_db_logs/deletion_backup_20260801_125804/`
- 删除后核验：04-现代研究文献/ 根目录只剩 research_notes.db 一个数据库文件
- research_notes.db integrity_check=ok，active_files=1789

## integrity_check 核验

| 数据库 | integrity_check |
| --- | --- |
| sacred_sources | ok |
| original_sources | ok |
| research_notes | ok |
| fact_checks | ok |
| review_reports | ok |
| cross_indexes | ok |
| metadata_interfaces | ok |

## 释读分析入库记录（2026-08-01）

> 入库 5 段哲学段落的释读分析到 sacred_sources.db

- **新增文件**：`02-sacred源材料/01-一刻哲学/附录-原始段落释读.md`（file_id=51，逻辑路径）
- **blocks 数**：105 个（heading/paragraph/list_item/quote）
- **cross_references**：10 个（5 个 file 级别 + 5 个 block 级别，关联原文 file_id=41,42）
- **active_files**：50 → 51
- **block_count**：3065 → 3170
- **分析对象**：
  - 论 LaTeX 与八股文（原文 file_id=42, block_id=3066-3067）
  - 经济学的本质是为了去分配（原文 file_id=42, block_id=3068-3069）
  - 论长生（原文 file_id=42, block_id=3070-3071）
  - 论物质与意识（原文 file_id=42, block_id=3072-3073）
  - 四版前言：和解与等待（草稿）（原文 file_id=41, block_id=1456）
- **入库脚本**：`script/_ingest_analysis.py`
- **验证脚本**：`script/_verify_analysis_ingest.py`
- **物理文件**：`script/_analysis_5_paragraphs.md`（按 AGENTS.md 规则保留在 script/）
- **integrity_check**：ok

## 存疑数据库迁移记录（2026-08-01）

> 将 `references_fulltext.db` 的存疑两表迁移至独立数据库 `doubts_standalone.db`，实现存疑内容的独立管理。

### 迁移来源

- **源数据库**：`04-现代研究文献/05-参考文献全文数据库/references_fulltext.db`
- **迁移表**：`doubts_to_resolve`（1707 行）、`non_doubt_markers`（1292 行）
- **源表处理**：迁移并校验通过后删除源表及 8 个相关索引，源数据库备份为 `references_fulltext.db.bak_before_doubt_migration`

### 目标数据库

- **数据库文件**：`04-现代研究文献/06-存疑数据库/doubts_standalone.db`
- **独立文件夹**：`04-现代研究文献/06-存疑数据库/`（遵循“一库一文件夹”模块化分层设计）
- **文档**：[04-现代研究文献/06-存疑数据库/index.md](../../04-现代研究文献/06-存疑数据库/index.md)
- **Schema 版本**：1.0.0
- **大小**：86.57 MB（88645632 bytes）
- **SHA-256（前16位）**：`1a7202de3fd31cf5`
- **journal_mode**：WAL
- **integrity_check**：ok

### 4 张表结构

| 表名 | 行数 | 说明 |
| --- | --- | --- |
| doubts_to_resolve | 1707 | 存疑主表（保留原 id） |
| non_doubt_markers | 1292 | 非存疑标记表 |
| doubt_review_log | 0 | 复核历史表（待后续填充） |
| schema_meta | 8 | 数据库元数据表 |

### 存疑状态分布

| resolution_status | 行数 |
| --- | --- |
| resolved | 1618 |
| open | 70 |
| unresolvable | 19 |

### 索引清单（12 个）

- `idx_doubts_outline_path`、`idx_doubts_line_number`、`idx_doubts_doubt_type`、`idx_doubts_resolution_status`、`idx_doubts_review_round`、`idx_doubts_source_db`、`idx_doubts_status_type`
- `idx_non_doubt_markers_outline_path`、`idx_non_doubt_markers_marker_type`、`idx_non_doubt_markers_source_db`
- `idx_doubt_review_log_doubt_id`、`idx_doubt_review_log_review_round`

### schema_meta 内容

| key | value |
| --- | --- |
| schema_version | 1.0.0 |
| schema_created_at | 2026-08-01 13:38:53 |
| last_migrated_at | 2026-08-01 13:38:53 |
| source_db | references_fulltext.db |
| source_path | 04-现代研究文献/05-参考文献全文数据库/references_fulltext.db |
| journal_mode | WAL |
| tables | doubts_to_resolve, non_doubt_markers, doubt_review_log, schema_meta |
| description | 存疑数据库：集中存放过去与未来所有存疑记录，独立于 references_fulltext.db |

### 迁移校验

- 行数一致性：doubts_to_resolve 1707/1707 ✓、non_doubt_markers 1292/1292 ✓
- 状态分布一致性：resolved 1618 + open 70 + unresolvable 19 = 1707 ✓
- 源表残留检查：references_fulltext.db 无 `doubt`/`non_doubt` 相关表 ✓
- 源数据库表总数：22 张（含 FTS5 影子表 5 张 + sqlite_sequence），业务表 16 张
- 备份文件：`references_fulltext.db.bak_before_doubt_migration`（437.69 MB）已保留

### folder_db_registry.csv 登记

- 新增一行：`doubts_standalone`（file_count=0, block_count=0, active_files=2999, deleted_files=0）
- **字段语义说明**：存疑数据库为功能数据库，无文件/块概念，`active_files` 字段记录总记录数（1707 + 1292 = 2999）

### 规则与文档同步

- [考据规则.md](../../00-编纂规则与格式规范/01-规则/考据规则.md) 新增“存疑数据库位置与使用规范”小节
- [流程规则.md](../../00-编纂规则与格式规范/01-规则/流程规则.md) “模块化分层设计规范”登记存疑数据库
- [AGENTS.md](../../AGENTS.md) 项目布局登记 `06-存疑数据库/` 文件夹
- [04-现代研究文献/05-参考文献全文数据库/index.md](../../04-现代研究文献/05-参考文献全文数据库/index.md) 表数声明从 18 张更正为 16 张
- [04-现代研究文献/06-存疑数据库/index.md](../../04-现代研究文献/06-存疑数据库/index.md) 新建数据库结构说明文档

### 迁移脚本

- `script/_doubt_migrate_to_standalone.py`（迁移主脚本）
- `script/_doubt_check_current_state.py`（源数据库状态检查）
- `script/_doubt_check_schema_meta.py`（schema_meta 表检查）
- `script/_doubt_verify_final.py`（最终状态核验）
- 上述脚本按 AGENTS.md 规则保留在 script/ 目录

## 交叉引用同步记录（2026-08-01）

> 本小节记录阶段二任务 25-35 的交叉引用与元数据同步更新结果。

### chapter_index.json 更新

- **任务 25（volume_label 系统性更新）**：303 章 volume_label 字段重新计算，覆盖 18 个卷标识
- **任务 26（卷拆分字段更新）**：67 条卷拆分变更
  - 第 280-296 章：V14 → V15（许可证哲学与法律分析）
  - 第 297-310 章：V15 → V16（开源运动与合规治理）
  - 第 311-324 章：V15 → V17（政治制度与社区治理）
  - 第 325-346 章：V16 → V18（全球社区地区 BSD 史）
- **任务 27（第 180 章迁移）**：1 章从 V9 迁至 V2，volume/volume_number/volume_label/chapter_folder/title/slug/path/outline_path 字段同步更新
- **任务 28（第 243-244 章合并）**：删除第 244 章（1 章），其 sections 合并至第 243 章；第 243 章 title/slug/id/chapter_folder/path 同步更新
- **任务 29（第 273.16 节迁移）**：1 个子节从第 273 章迁移至第 43 章 43.17 节，section_number/section_file/section_title 同步更新
- **总章数**：346 → 345（删除第 244 章）

### cross_reference_map.csv 更新

- **任务 30 全面更新**：原 263 条 → 261 条
  - 删除 4 条（V9 内第 180 章相关链接）
  - 新增 2 条（V2 内第 180 章相关链接）
  - V16 → V18 侧变更：62 条
  - V14/V15 拆分变更：33 条
  - dragonflybsd → dragonfly-bsd 术语统一：8 条侧变更
  - V12-CH244 合并至 V12-CH243：0 条（无引用 V12-CH244 的记录）
  - 跨卷 next/prev 引用 reference_type 自动改为 cross_volume

### folder_db_registry.csv 补全

- **任务 31**：从 1 行（仅 doubts_standalone）补全至 8 行
  - 7 个文件夹数据库：sacred_sources、original_sources、research_notes、fact_checks、review_reports、cross_indexes、metadata_interfaces
  - 1 个功能数据库：doubts_standalone
  - 所有 db_path 经核验存在

### cross_db_references.csv 扫描

- **任务 32**：13 条跨库引用，0 条受影响
  - 跨库引用主要涉及数据库名（bsd_commits、资料数据库、changelog、original_sources）与文件路径（03-原始史料库/...、01-项目管理/...），均未受章节 id/卷路径变更影响

### 5 个数据库 cross_references 表同步

- **任务 33**：扫描 5 个数据库共 19127 条 cross_references 记录
  - sacred_sources：638 行，1 条含 dragonflybsd.org 域名 URL（外部 URL 不修改），0 条更新
  - research_notes：18441 行，0 条受影响
  - fact_checks：17 行，0 条受影响
  - review_reports：16 行，0 条受影响
  - cross_indexes：15 行，0 条受影响
  - 5 个数据库 PRAGMA integrity_check 全部 = ok

### 同步脚本

- `script/_xref_sync_01_to_04_chapter_index.py`（任务 25-29 综合脚本）
- `script/_xref_sync_04_cross_reference_map.py`（任务 30）
- `script/_xref_sync_05_folder_db_registry.py`（任务 31）
- `script/_xref_sync_06_cross_db_references.py`（任务 32）
- `script/_xref_sync_07_db_cross_references.py`（任务 33）
- 上述脚本按 AGENTS.md 规则保留在 script/ 目录

## 数据库全面优化记录（2026-08-04）

> 执行依据：`script/_backup_all_dbs_20260804.py`（阶段0 全量备份）→ `_cleanup_phase1_20260804.py`（阶段1 清理）→ `_fix_db_renumber_20260804.py`（阶段2 编号迁移）→ `_cleanup_paths_20260804.py`（阶段2b 路径清理）→ `_refactor_ziliao_db_20260804.py`（阶段3 资料库 v1.4 化）→ `_optimize_indexes_20260804.py`（阶段4 索引）→ `optimize_folder_databases.py --all`（阶段5 核验）。

### 阶段 0：全量备份

- 33 个 .db 全部复制至 `script/_backup_20260804_full/`，生成 SHA256SUMS.txt（33 条）
- 逐库 integrity_check 全部 ok（唯一异常为旧备份 `research_notes_git_backup.db` 非数据库文件，非活动库）
- 报告：`script/_folder_db_logs/backup_report_20260804.md`

### 阶段 1：清理与 schema_meta 统一（references_fulltext.db）

- 删除空表：`fulltext_assets`、`fulltext_tables`（0 行、零脚本依赖、功能未启用）
- `schema_meta` 单行结构 → v1.4 key-value（9 标准键，schema_version=1.4）
- 表数 22 → 20，integrity_check=ok

### 阶段 2：旧编号 → 新 348 章体系迁移

- **chapter_reviews（71 行）**：67 行经人工核实映射表迁移至新章号（移除 legacy-expired）；4 行（id=2/30/31/60）无法可靠定位，标记 `renumber-unmapped-20260804` 保留旧编号
- **chapter_matches（1660 行）**：match_reasoning 旧引用替换 102 行（346→348 等）；vol=0 的 276 行为卷级参考保持设计状态
- **资料数据库**：materials ch 迁移 15008 行（ch 0-346 → 新体系，vol 按新 ch 反推）、references ch 迁移 13963 行（2916 行为 NULL 卷级记录）、fact_check_records ch 迁移 11 行、cross_references src_ch 迁移 667 行
- **timeline_records（18 行）**：全部映射成功（旧60→新61 等）
- **路径清理**：references.file_path 452 行绝对路径 → 相对路径（0 残留）；fact_check_records.file_path 39 行旧 hibsd 绝对路径 → 相对路径形式

### 阶段 3：资料数据库 v1.4 化重构

- 旧 `cross_references`（667 行，src_ch/dst_ch 整数引用）→ 改名 `material_cross_references`（零脚本依赖，已 grep 全量确认）
- 新增 5 张通用表（files/blocks/blocks_fts/cross_references/update_log）+ schema_meta（key-value）
- `db_meta` 数据并入 schema_meta（db_meta 表保留兼容）
- 业务表（materials/references/freebsd_sa/nvd_cve_metadata/fact_check_records）保留为专属扩展表
- 表数 9 → 20，索引 15 → 35，integrity_check=ok

### 阶段 4：索引优化

- references_fulltext：删冗余索引 `idx_chapter_matches_primary_volume`（与组合索引重复）；chapter_reviews 增 `outline_path` 索引
- 资料数据库：补 v1.4 通用索引 14 个 + materials(doubt_flag)/(vol,ch) + references(vol,ch)；删冗余 `idx_refs_vol_ch`
- EXPLAIN QUERY PLAN 验证全部命中索引

### 阶段 5：核验与优化

- `optimize_folder_databases.py --all`：7 库 schema/ghost-blocks/reindex/pragma 正常，VACUUM 回收约 5MB（original_sources 省 4.7MB）
- 规则同步：流程规则.md 346→348（5 处 + 卷数 16→18）
- folder_db_registry.csv 追加 references_fulltext/资料数据库/phoronix_news 3 行独立库注册
- changelog.duckdb 新增迁移记录（见 01-项目管理）
