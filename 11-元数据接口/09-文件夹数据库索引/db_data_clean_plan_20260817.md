# 全量数据库数据内容清洗与列级优化清单

> 生成日期：2026-08-17
> 数据来源：`script/_db_full_audit_20260817.json`（292 库只读实测）+ `script/_db_full_audit_summary_20260817.json`
> 审计方法：`SELECT` / `PRAGMA table_info` / `integrity_check` / 行数 / 全空列探测，零写库
> 状态：**待用户确认**（确认后进入备份→执行→复核→删除备份）

---

## 一、总览

| 类别 | 数量 | 完整性 |
| --- | --- | --- |
| 文件夹级数据库 | 7 | 全部 integrity=ok |
| 功能数据库 | 9 | 全部 integrity=ok |
| 代码仓库数据库（raw） | 11 | ok / SKIP(heavy) |
| 邮件列表数据库（raw） | 265 | 全部 integrity=ok |
| **合计** | **292** | 无损坏、无打开错误 |

292 库与 `folder_db_registry.csv` 逐行对齐，无遗漏、无多记、无路径漂移（分类统计 functional=9 / folder_level=7 / code_raw=11 / mail_raw=265）。

---

## 二、空表（0 行）分类

### 2.1 内容工程待导入（延后阶段 4，不删除）

| 库 | 空表数 | 表 |
| --- | --- | --- |
| causal_graph | 9 | causal_arrow / causal_arrow_alternative / causal_arrow_evidence / causal_arrow_status_log / causal_arrow_temporal / causal_chain / causal_counterfactual / causal_node / chain_cross_ref |
| historical_claims | 15 | claim_entity / claim_period / claim_relation / controversy_position / cross_ref / entity_relation / evidence_entity / interp_claim / interp_evidence / interpretation / narrative_citation / narrative_unit / provenance_history / source_independence / source_period |
| bsd_podcasts_external | 1 | outline_mappings（内容缺口，非结构问题） |

### 2.2 可退役

| 库 | 表 | 处置 |
| --- | --- | --- |
| fact_checks | blocks | 空壳库已退役（登记簿 `retired_deleted_41_active_0`），blocks 表为悬空残留，无需回填 |

**结论**：空表均属“待阶段 4 数据导入”或“已退役”，**本次不执行删除**（因果链/上层主张表结构为重构2026 预留，删除会破坏 schema 设计）。

---

## 三、全空列（删列候选）分类与处置

全量扫描识别出大量“100% 空值列”。经归类，绝大部分为 **schema 预留字段**（非冗余、非废弃），删除将破坏跨库 schema 一致性。分类处置如下：

### 3.1 文件夹级库通用 Schema v1.4 预留字段（**保留，不删除**）

7 个文件夹级库共享通用架构，以下空列是“去重 / 交叉引用”功能的预留字段，未来阶段 3/4 数据回填时启用：

- `files` 表：`frontmatter`、`duplicate_of_id`、`duplicate_type`、`duplicate_of_db`、`duplicate_of_global_file_id`
- `cross_references` 表：`source_block_id`、`target_db`、`target_record_id`、`target_anchor`、`resolved_at`
- `update_log` 表：`file_id`

**风险提示**：若删除某一库的上述列，将导致该库与其余 6 库 schema 不一致。**不建议删除**。

### 3.2 历史学库预留字段（**保留，延后阶段 4 填充**）

`historical_claims` 多张表的空列（`claim.parent_claim_id` / `controversy.adjudication` / `entity.merged_into` / `raw_source.author_entity` 等）是重构2026 史学库的字段预留，随 M4-M9 迁移填充，**不删除**。

### 3.3 邮件库采集字段空值（**保留，史料完整性优先**）

265 个邮件库的 `messages` 表存在因数据源差异而全空的列（`body_html`、`archive_url`、`from_email`、`to_text`、`cc_text`、`raw_headers`、`source_offset`、`in_reply_to`、`thread_refs` 等），`lists` 表的 `list_address` / `category` / `archive_url` / `note` / `first_year` / `last_year` 亦因列表而异。

**结论**：这些是采集 schema 的统一字段，删除会破坏 265 库 schema 一致性，且属史料索引字段，**不删除**。

### 3.4 代码仓库库空列（**保留**）

`org_contributions.contributors`、`repos.clone_duration_min`、`commit_files.additions/deletions`、`commits.signed_off_by` 等空列，是各仓库数据源差异所致（部分项目无 diff 统计 / 无 Signed-off-by / 无 clone 时长统计），属采集 schema 统一字段，**不删除**。

### 3.5 真正“不需要”的列（**本次可删，需逐条确认**）

审计未发现“冗余列”（内容与另一列完全重复）或“废弃 legacy 列”（本次扫描 `legacy_tables` 为空，说明 `historical_claims.chapter_backup_313` 旧口径备份表已在前期瘦身中移除）。

**删列结论：本次不执行任何 DDL 删列操作。** 理由：292 库的“全空列”均为跨库共享 schema 的预留/统一字段，删除将破坏一致性且无收益；真正的冗余列、废弃列不存在。

---

## 四、日期/时间字段（UTC + 本地时间）状态

### 4.1 邮件库（已满足双轨要求 ✓）

全部 265 个邮件库 + 4 个合并库的 `messages` 表均已含 `date`（UTC）与 `date_local`（本地时间）双列，满足“时间用 UTC + 保留作者本地时间”要求，**无需规范化**。

### 4.2 代码仓库库（UTC 已满足，本地时区偏移待确认）

11 个代码仓库库的 `commits.author_date` / `committer_date` 为 git 时间戳（UTC 语义）。**待确认项**：git 提交的原始时区偏移（`author_tz_offset` / `committer_tz_offset`）是否在采集时保留。若未保留，且用户要求“保留作者本地时间”，需在阶段 3 史料回填时补充 tz_offset 列（**非本次删列范畴**）。

### 4.3 结构化库内部时间字段

`created_at` / `updated_at` / `timestamp` / `mtime` 等为库内元数据时间，多为 ISO 字符串（本地或 UTC），属系统内部时间，不涉及史料“作者本地时间”问题，**不在本次规范化范围**。

---

## 五、待清洗数据内容（占位/模板记录）

审计已确认的占位/模板记录（此前 `db_consistency_audit_20260816.md` 已登记）：

| 库 | 表 | 问题 | 处置 |
| --- | --- | --- | --- |
| review_reports | review_records | 14 条未填充模板（`parties`/`period`/`evidence`/`resolution_status`/`review_round`/`submission_date`/`verdict` 全空） | 属内容工程，延后阶段 4 补实 |
| cross_indexes | concept_history | 43 行 `history_summary` 为“总纲衍生”占位文本 | 属内容研究，延后阶段 4 补实 |

**结论**：占位/模板记录的“清洗”本质是内容补全（非删除），属阶段 4 内容工程，**本次不执行**（本次聚焦结构性清理，不触碰内容创作）。

---

## 六、汇总：本次可执行动作

| 序号 | 动作 | 对象 | 是否执行 |
| --- | --- | --- | --- |
| A | 空表删除 | causal_graph / historical_claims 空表 | 否（延后阶段 4） |
| B | 空壳退役收尾 | fact_checks.blocks | 否（已退役，无需动作） |
| C | 全空列删除 | 292 库各全空列 | **否**（均为 schema 预留/统一字段） |
| D | 冗余列/废弃列删除 | 无 | 无对象 |
| E | 占位/模板记录清洗 | review_reports / cross_indexes | 否（内容工程） |
| F | 时间规范化 | 邮件库已双轨 / 代码仓库待确认 tz_offset | 邮件库无需动作；代码仓库属阶段 3 |
| G | 登记簿口径同步 | folder_db_registry.csv | 本次无变化，无需更新 |

---

## 七、审计结论

1. **完整性**：292 库无损坏、无打开错误、integrity 全部 ok（raw 大库此前已核验 ok）。
2. **数据内容**：占位/模板记录已定位（review_reports 14 条、cross_indexes 43 行），但“清洗”本质是内容补全，属阶段 4，非本次结构清理范围。
3. **列级优化**：292 库存在大量“全空列”，但经归类均为跨库共享 schema 的**预留/统一字段**，删除将破坏 7 文件夹级库 / 265 邮件库 / 11 代码仓库库的 schema 一致性，且无收益；**真正的冗余列、废弃列不存在**。
4. **时间规范化**：邮件库已满足“UTC + 本地时间”双轨；代码仓库库 UTC 已满足，本地时区偏移是否保留属阶段 3 史料回填范畴。
5. **结论**：本次“复核”已完成，“清洗 / 调整 / 删列”无结构性可执行对象——所有发现均归入“延后阶段 4 内容工程”或“无需动作”。建议**不进入备份/执行/删除备份阶段**（无可执行变更）。

> 若用户仍希望对某些“全空列”执行 DDL 删除（如邮件库 `body_html`、代码仓库库 `additions/deletions`），需逐库明确授权，因该操作会破坏跨库 schema 一致性，需评估下游脚本依赖后单独执行。
