# 数据库拆分或合并评估报告

生成时间: 2026-08-01T14:01:20（第三次评估，确认结论不变）
历史评估: 2026-08-01T12:55:55（首次）→ 2026-08-01T13:55:46（第二次，Task 15-16 后）→ 2026-08-01T14:01:20（第三次）
评估范围: 7 个文件夹级数据库
评估目标: 清晰明白，方便调用，加速引用查询；保持模块化分层设计（一库一文件夹）


## 1. 数据库大小分布

| 数据库 | 文件大小 | table_count | active_files | blocks 数 | cross_references |
| --- | --- | --- | --- | --- | --- |
| sacred_sources | 4.12 MB | 5 | 52 | 3177 | 638 |
| original_sources | 15.19 MB | 7 | 602 | 7 | 0 |
| research_notes | 259.06 MB | 5 | 1792 | 486863 | 18441 |
| fact_checks | 2.56 MB | 5 | 41 | 0 | 17 |
| review_reports | 0.53 MB | 6 | 54 | 38 | 16 |
| cross_indexes | 0.61 MB | 8 | 53 | 21 | 15 |
| metadata_interfaces | 3.38 MB | 7 | 12 | 9822 | 0 |

**总大小**: 285.45 MB

**与上次评估（2026-08-01T13:55:46）的变化**:
- 全部 7 个数据库大小、表数量、行数、blocks 数、cross_references 数均无变化
- 第三次评估确认：sacred_sources 4.12 MB / files 52 / blocks 3177 / cross_references 638 保持稳定
- schema_version 全部为 1.4，journal_mode 全部为 wal，索引数与上次评估一致


## 2. blocks 分布

| 数据库 | blocks 总数 | file_id 唯一数 | 平均 blocks/file | 最大 blocks/file |
| --- | --- | --- | --- | --- |
| sacred_sources | 3177 | 52 | 61.1 | 315 |
| original_sources | 7 | 1 | 7.0 | 7 |
| research_notes | 486863 | 1792 | 271.7 | 285393 |
| fact_checks | 0 | 0 | 0.0 | 0 |
| review_reports | 38 | 4 | 9.5 | 11 |
| cross_indexes | 21 | 2 | 10.5 | 12 |
| metadata_interfaces | 9822 | 2 | 4911.0 | 9558 |

## 3. 跨库引用分析

| 数据库 | cross_references 总数 | target_path 跨库引用数 | 跨库占比 |
| --- | --- | --- | --- |
| sacred_sources | 638 | 573 | 89.8% |
| original_sources | 0 | 0 | 0.0% |
| research_notes | 18441 | 17304 | 93.8% |
| fact_checks | 17 | 0 | 0.0% |
| review_reports | 16 | 13 | 81.2% |
| cross_indexes | 15 | 2 | 13.3% |
| metadata_interfaces | 0 | 0 | 0.0% |

## 4. 扩展表使用率

### 4.1 已合并的低使用率扩展表（Task 5 完成，保持不变）

| 数据库 | 原表1（行数） | 原表2（行数） | 合并表 | 合并后行数 | 合并理由 |
| --- | --- | --- | --- | --- | --- |
| original_sources | security_advisories（6） | vulnerability_metadata（1） | security_vulnerabilities | 7 | 安全公告与漏洞元数据语义相近，合并后按 record_type 区分 |
| review_reports | disputes（9） | peer_reviews（5） | review_records | 14 | 历史争议与同行评议均为核查记录，合并后按 record_type 区分 |
| cross_indexes | person_index（1） | person_biography（6） | person_records | 7 | 人名索引与人物传记语义相近，合并后按 record_type 区分 |
| cross_indexes | command_index（1） | term_index（12） | terminology_index | 13 | 命令索引与术语索引均为索引记录，合并后按 record_type 区分 |
| metadata_interfaces | build_status（1） | citation_frequency（3） | build_citation_records | 4 | 构建状态与引文频次均为元数据记录，合并后按 record_type 区分 |

### 4.2 保留的扩展表

| 数据库 | 保留表 | 行数 | 保留理由 |
| --- | --- | --- | --- |
| original_sources | kaoju_records | 568 | 考据记录，独立主题，行数较多 |
| cross_indexes | concept_history | 21 | 概念史与思想谱系，G2 缺口，独立主题 |
| metadata_interfaces | chapter_metadata | 346 | 章节元数据，独立主题，行数较多（注：此次评估未单独列出，因已合并入 files 表或作为 blocks 入库） |
| metadata_interfaces | timeline_records | 18 | 年代索引，G9 缺口，独立主题 |

### 4.3 当前各库扩展表清单

| 数据库 | 扩展表 | 行数 | 状态 |
| --- | --- | --- | --- |
| sacred_sources | 无 | — | 无扩展表 |
| original_sources | kaoju_records | 568 | 保留 |
| original_sources | security_vulnerabilities | 7 | 已合并（Task 5） |
| research_notes | 无 | — | 无扩展表 |
| fact_checks | 无 | — | 无扩展表 |
| review_reports | review_records | 14 | 已合并（Task 5） |
| cross_indexes | concept_history | 21 | 保留 |
| cross_indexes | person_records | 7 | 已合并（Task 5） |
| cross_indexes | terminology_index | 13 | 已合并（Task 5） |
| metadata_interfaces | timeline_records | 18 | 保留 |
| metadata_interfaces | build_citation_records | 4 | 已合并（Task 5） |

## 5. 评估结论

### 5.1 不合并小数据库

- **结论**: 7 个数据库保持独立，不合并

- **理由**:
  1. 模块化分层设计：每个数据库对应一个一级文件夹，承载该文件夹的内容，职责清晰
  2. 独立访问：按文件夹查询时只需打开对应数据库，避免跨库 JOIN 开销
  3. 独立备份恢复：单个数据库损坏不影响其他数据库
  4. 大小分布合理：最大 research_notes.db（约 259 MB）与最小 review_reports.db（约 0.53 MB）差异虽大，但各有独立职责
  5. 跨库引用通过 cross_references 表的 target_path 字段实现，无需合并即可查询

### 5.2 不拆分 research_notes.db

- **结论**: research_notes.db 不拆分

- **理由**:
  1. 内聚性：research_notes.db 承载 04-现代研究文献/ 文件夹的全部内容，主题内聚
  2. SQLite 性能：259 MB 对 SQLite 而言属中等规模，WAL 模式下读写性能良好
  3. 已有索引：blocks.file_id、blocks_fts 全文检索、cross_references 多字段索引已覆盖主要查询路径
  4. 拆分代价：拆分会破坏现有 cross_references 跨文件引用（18441 条），需重建引用网络，代价高于收益

### 5.3 已合并低使用率扩展表（保持不变）

- **结论**: 5 组扩展表已合并（详见 4.1 节），无需进一步合并

- **收益**:
  1. 减少表数量：4 个数据库共减少 5 张表（每组合并 2 表为 1 表）
  2. 简化查询：相关数据集中在一张表，通过 record_type 区分来源，避免跨表 JOIN
  3. 统一索引：合并表创建 file_id 与 record_type 索引，覆盖主要查询路径

### 5.4 新增引用查询加速索引（保持不变）

- **结论**: 7 个数据库的 cross_references 表已新增 2 个索引

- **索引清单**:
  1. idx_cross_references_reference_type（reference_type 字段）— 加速按引用类型过滤
  2. idx_cross_references_source_block_id（source_block_id 字段）— 加速按源块定位
- **收益**: EXPLAIN QUERY PLAN 核验显示 WHERE reference_type='wikilink' 与 WHERE source_block_id=123 均使用新索引

### 5.5 索引命名统一（保持不变）

- **结论**: 7 个数据库的冗余索引已清理

- **清理清单**:
  1. 删除 idx_xref_source、idx_xref_target_db、idx_xref_resolution_status（与 idx_cross_references_* 重复）
  2. 删除 idx_files_duplicate_type（与 idx_files_duplicate_of_id 功能重复）
  3. 补建 idx_files_duplicate_of_db（6 个数据库缺失）
- **收益**: 7 个数据库索引命名统一，避免冗余索引拖慢写入性能

### 5.6 schema_meta 键集合统一（保持不变）

- **结论**: 7 个数据库 schema_meta 键集合统一为 9 个标准键

- **标准键**: active_files, deleted_files, ghost_blocks_cleaned, journal_mode, last_optimize_at, last_vacuum_at, pragma_optimized_at, schema_version, table_count
- **迁移**: research_notes.db 的 restored_from_git 键已迁移至 update_log

### 5.7 模块化分层设计验证（保持不变）

- **结论**: 7 个数据库均遵循“一库一文件夹”架构

- **对应关系**:
  1. 02-sacred源材料/sacred_sources.db
  2. 03-原始史料库/original_sources.db
  3. 04-现代研究文献/research_notes.db
  4. 07-事实核查记录/fact_checks.db
  5. 08-核查报告与多轮复核/review_reports.db
  6. 10-交叉索引/cross_indexes.db
  7. 11-元数据接口/metadata_interfaces.db
- **核验**: 无跨文件夹存放的数据库文件，无一个文件夹含多个活动数据库

## 6. 总结

本次评估（第三次，2026-08-01T14:01:20）确认：
- 7 个数据库保持独立，不合并（模块化分层设计）
- research_notes.db 不拆分（SQLite WAL 性能良好）
- 5 组低使用率扩展表已合并（Task 5 完成，保持不变）
- 引用查询加速索引已创建（Task 6 完成，保持不变）
- 索引命名已统一（Task 1-2 完成，保持不变）
- schema_meta 键集合已统一（Task 3 完成，保持不变）
- 模块化分层设计已验证（Task 13 完成，保持不变）

与第二次评估（2026-08-01T13:55:46）相比，全部 7 个数据库大小、表数量、行数、blocks 数、
cross_references 数均无变化。评估结论与首次、第二次评估一致，无需进一步拆分或合并。

**最终评估结论**:
1. **数据库层面**：7 个数据库保持现状，不合并小库（模块化分层设计），不拆分 research_notes（WAL 性能良好）
2. **数据表层面**：5 组低使用率扩展表已合并完成，3 个独立主题扩展表（kaoju_records、concept_history、timeline_records）保留
3. **索引层面**：cross_references 表已新增 2 个加速索引，索引命名已统一，冗余索引已清理
4. **schema 层面**：7 个数据库 schema_version 统一为 1.4，schema_meta 键集合统一为 9 个标准键


**评估完成时间**: 2026-08-01T14:01:20（第三次评估，确认结论不变）

---

## 第四次评估补充（2026-08-04，数据库全面优化后）

> 本次评估范围扩展至独立库（资料数据库 v1.4 化 + references_fulltext 表重组）。

**独立库拆分合并决策**:

1. **资料数据库.db（v1.4 化）**：不拆分、不合并库文件；按 Schema v1.4 对齐结构——
   - 旧 `cross_references`（667 行，src_ch/dst_ch 整数章节引用）**改名 `material_cross_references`**：避免与 v1.4 通用 cross_references 同名冲突，数据完整保留（零脚本依赖，已 grep 全量确认）
   - 新增 5 张通用表（files/blocks/blocks_fts/cross_references/update_log）+ schema_meta（key-value，9 标准键）
   - `db_meta`（3 行）数据并入 schema_meta（db_meta 表保留兼容既有脚本）
   - 业务表（materials 15033 行 / references 16879 行 / freebsd_sa 713 行 / nvd_cve_metadata 1770 行 / fact_check_records 39 行）**保留为专属扩展表**，不改名（references 与 references_fulltext.references 同名异构，两库并存，语义不同：前者为章节引用清单，后者为文献元数据）
2. **references_fulltext.db（21 表）**：不合并 chapter_matches/chapter_reviews 进核心库（reference_id 外键血缘 + 99/25 次脚本依赖）；fulltext 与 fulltext_blocks **不冗余**（整篇 vs 块级，块级供 FTS）；删除 2 张零依赖空表（fulltext_assets/fulltext_tables）；schema_meta 统一为 v1.4 key-value
3. **核心 7 库**：维持第三次评估结论不变

**执行依据**：`script/_refactor_ziliao_db_20260804.py`、`script/_cleanup_phase1_20260804.py`；完整性：资料数据库 integrity=ok、行数零丢失（material_cross_references 667/667、materials 15033/15033、references 16879/16879）。

**评估完成时间**: 2026-08-04T00:30:00（第四次评估补充）
