# data-model.md — Phase 1 数据模型（login 判定入藏战役）

**Feature**: specs/003-login-claim-outline | **Date**: 2026-10-06

## 1. 判定台账行（新实体；JSONL，script/ 下）

| 字段 | 类型 | 约束/校验 |
| ---- | ---- | --------- |
| article_id | INT | 主键（幂等键）；∈ articles.article_id |
| identifier | VARCHAR | 期标识（溯源） |
| kind | VARCHAR | ∈ {article,column,news,ad,toc,frontmatter,unknown} |
| verdict | VARCHAR | ∈ {claim_ingest, no_ingest}（判定终态） |
| significance | VARCHAR | 历史意义/价值摘要（≤200 字） |
| reasons | VARCHAR[] | 所引原则编号（R1-R12/P 编号/七类不写判据） |
| chapter_target | VARCHAR | 拟挂大纲章（vol/ch；claim_ingest 必填） |
| claim_ids | VARCHAR[] | 入藏生成的 claim_id（回填） |
| judged_by | VARCHAR | 引擎标识（llm:agent-login） |
| judged_at | TIMESTAMP | |

**校验规则**: 覆盖 6,604/6,604 唯一；verdict 非 claim_ingest 时 reasons 非空且非臆造。

## 2. raw_source（L1；historical_claims.duckdb，既有表）

| 字段 | 类型 | 约束/校验 |
| ---- | ---- | --------- |
| source_id | VARCHAR | 主键；`SRC-login:<article_id>` 全库唯一 |
| source_db | VARCHAR | = 'login-zazhi' |
| source_table | VARCHAR | = 'articles' |
| local_pk | VARCHAR | = article_id |
| content_hash | VARCHAR | SHA-256（body_text 或 title+body 拼接，入藏时计算） |
| source_type | VARCHAR | 受控词表（magazine-article/magazine-ad/magazine-department…） |
| source_layer | INT | ∈ 1-5（P41 五层级；login 印刷期刊＝2 一手印刷档案层） |
| source_date / date_precision | VARCHAR | 期年月（issues 表） |
| author | VARCHAR | 文章作者（原文） |
| organization | VARCHAR | （如 USENIX） |

## 3. evidence（L2；既有表）

| 字段 | 类型 | 约束/校验 |
| ---- | ---- | --------- |
| evidence_id | VARCHAR | 主键；`EV-login:<article_id>:<seq>` 唯一 |
| source_id | VARCHAR | FK→raw_source.source_id |
| anchor | VARCHAR | `login-zazhi:articles:<article_id>` |
| quote | TEXT | **body_text 原文照录零改写**（噪声/原件笔误照录） |
| fact_text | TEXT | 判定引擎提炼的事实性要点（支撑拟议 claim） |
| evidence_kind | VARCHAR | ∈ 既有受控值 |
| confidence | VARCHAR | 0 信任评级 |
| extracted_by | VARCHAR | 引擎标识 |

## 4. claim（L3；既有表）

| 字段 | 类型 | 约束/校验 |
| ---- | ---- | --------- |
| claim_id | VARCHAR | 主键；`CL-<卷>-<序号>` 续排全库唯一 |
| claim_text | VARCHAR | 主张文本（措辞过门禁） |
| claim_type | VARCHAR | ∈ 十值枚举（FACT/CAUSAL_CLAIM/INTERPRETATION/COMPARISON/INFLUENCE_CLAIM/ORIGIN_CLAIM/FIRST_APPEARANCE/MOTIVATION/CONTROVERSY/UNVERIFIED） |
| evidence_level | VARCHAR | ∈ L1-L5（L5 最强） |
| wording_gate | VARCHAR | 措辞门禁标注（L1 级禁写"继承/影响/源自/借鉴"） |
| status | VARCHAR | ∈ proposed/supported/contested/refuted/superseded |
| created_by | VARCHAR | 'llm:agent-login' |

## 5. source_chapter（既有表）

| 字段 | 类型 | 约束/校验 |
| ---- | ---- | --------- |
| source_id | VARCHAR | FK→raw_source |
| vol / ch / sec | VARCHAR | 既有 54 卷 454 章口径的章节坐标 |
| link_type | VARCHAR | ∈ {used, mentioned, background}；多值多行 |

## 6. ROW_MINE 注入块（05-卷册大纲磁盘侧；非 DB 实体）

按 ROW_MINE 块体格式规则（2026-09-17 立规）：块头结构（`<!-- ROW_MINE: … -->` 定界）、当事人自述抬头、证据等级标注（真值＝claim 库 evidence_level，禁写死字面）、引用纪律句；写入经 WO-007（has_block 检查＋write_guard：库名规范化＋UTF-8 无 BOM＋LF）。

## 7. 新建大纲章文件（仅触发时）

卷 00-总览.md 登记 → `第XX章-slug/index.md` + 子节文件（五字段：要点/史料/史观/辨析/文献；史观映射 ≥5 条总纲）→ sync_gitbook_summary.py --write。

## 状态转换

- 判定台账：pending → judged（终态二值）→ ingested（claim_ids 回填）/ skipped（no_ingest 终态）。
- claim 生命周期：proposed → supported/contested/refuted/superseded（refuted 不物理删除）。

## 关系

- 判定台账 1 — N evidence（一篇多证据）；evidence N — 1 raw_source；claim N — N evidence（claim_evidence，role 区分支撑/反证）；raw_source 1 — N source_chapter（多章挂钩）。
