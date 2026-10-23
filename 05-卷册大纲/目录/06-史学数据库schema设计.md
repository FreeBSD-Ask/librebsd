# 06-史学数据库 schema 设计（历史主张数据库 historical_claims.db）

> **项目**：《给我自由——一部 BSD 史》编纂系统二次重构 · Phase 6-8
> **设计人**：数据工程师 · 洗澄明（实证研究团）· 2026-08-11
> **状态**：**设计文本，不建库、不执行**（与 07 号文档同一约束；DDL 已在临时库自测通过）
> **交付物**：本文档 + 配套 DDL 文件 `06a-史学数据库DDL.sql`（28 表 / 4 审计视图 / 4 触发器 / 预置数据）
> **演化备注**：上一行"28 表/4 审计视图/4 触发器"为设计稿口径；v0.1 实测口径为 33 表/8 视图/4 触发器，v0.2 补编再 +4 表（演化明细见本文档文末附录"表清单"）。
> **依赖**：Task #1（02-数据库盘点与史料字段差距分析）、Task #2（01-编纂原则清单）
> **对接**：07-因果链与影响分类体系（claim_id/evidence_id/L1-L5 门禁）、09-五系统（controversy_id/sources 层级编码）

---

## 第一部分：设计输入与硬约束

### 1.1 来自盘点（02 号文档）的三个事实

1. **字段缺口**：20 个史料分类字段中 🟢1 / 🟡12 / 🔴7。黄色字段的共性是"一手档案层有数据、素材/书目层缺挂载"（author 在邮件/提交中完备，在 24,129 条素材中只有 12 条）；红色 7 字段（organization、historical_period、involved_events、independence、contemporary、retrospective、relevant_claims）全仓无任何承载。
2. **层次现状**："两层半"——L1 原始史料充实（约 976 万条）、L2 抽取证据只有书目一条腿（4,163 篇）、L3/L4 完全不存在、L5 只有 348 章提纲；且主流路径是 L1 素材经 vol/ch/sec **直挂** L5 章节，跳过证据与主张层。
3. **结构缺口**：无主张实体 → doubts（1,987 条）无物可疑；无全局 ID → 跨库引用 13 条中 7 条悬空；一手档案层（占总量八成）与编纂体系零接触。

### 1.2 来自编纂原则（01 号文档）的硬约束

| 原则 | 对 schema 的强制要求 |
| ---- | -------------------- |
| P41 史料五层级 | `source_layer` 1-5 编码（1=代码产物最强 → 5=二手研究最弱）；`banned_source` 禁用标记（百科类/CSDN 类绝对禁用）；矛盾仲裁"低形式主义程度优先" |
| P42 邮件列表中心主义 | 邮件是一等史料载体（carrier='email'），引用须带时间戳与发件人；偏差自觉字段（选择性/代表性/幸存者偏差不在 schema 消除，在 `tier_basis`/`reliability_rationale` 中陈述） |
| P43 三重形式主义化 | 可靠性评级必须带**理由与人**（reliability_rationale/assessed_by）；争议裁决是"暂定判断"而非真相宣布（controversy.adjudication 语义） |
| P44 六期分期 | historical_period 六行预置，**年份交叠为设计特性**（一史料可属多期 → source_period 多值表）；禁线性"早/中/晚期"字段 |

### 1.3 来自下游文档的接口约定（必须兑现）

- **07 号**：`claim_id` 规范 `CL-<卷>-<序号>`、影响主张 `IC-<卷>-<序号>`；`evidence_id` 为跨库引用位；`evidence_level` L1-L5（**L5 最强**）；措辞门禁表（L1 禁写"继承/影响/源自/借鉴"是硬禁令）；十二类影响分类（impact_type 12 值）；07 §1.4 遗留问题（因果链表组独立成库还是并入主张库）**由本文档拍板：见 §8.2**。
- **09 号**：`controversy_id`（如 `openbsd_fork_motive`）；`sources_per_position` 每方观点的来源与层级（JSON）；五系统 `sources` 字段统一使用本库 L1-L5 编码。

### 1.4 设计红线

1. 本次**不建库、不执行、不迁移任何数据**；DDL 仅在临时库自测语法与约束。
2. 对遗留 29 库**只读**：新库采用"注册制"引用旧数据（坐标+哈希），不复制正文（34 GB 不可搬迁，也无必要）。
3. 禁止双写发散：事实性描述只允许存在于 evidence/claim 层；07 号 `node_summary` 式"描述性快照"原则（`summary_is_authoritative=0`）推广到全库。

---

## 第二部分：总体架构——五层隔离模型

### 2.1 层与表

```
L5 叙事层    chapter / narrative_unit / narrative_citation
                │ 只许引 claim / interpretation / evidence（CHECK 强制，raw_source 被拒）
L4 解释层    interpretation / interp_claim / interp_evidence
                │ 只许引 claim / evidence
L3 主张层    claim / claim_evidence / claim_entity / claim_period / claim_relation
                │ 只许引 evidence
L2 证据层    evidence / evidence_entity          （key_facts 结构升格为全仓通用）
                │ 只许引 raw_source
L1 史料层    raw_source / source_period / source_chapter / source_independence / provenance_history
                │ 注册制：坐标+哈希指向 29 个遗留库，不搬正文
横切        entity / entity_relation（图谱节点）· historical_period / controlled_vocab /
            wording_gate_rule（受控词表）· controversy / controversy_position（争议簿）·
            cross_ref（跨库引用）· schema_meta / update_log（三件套惯例）
```

### 2.2 隔离的三重强制机制

1. **列级 CHECK**：`narrative_citation.target_type IN ('claim','interpretation','evidence')`——L5 直引 L1 在 SQL 层即被拒绝（自测冒烟 PASS：插入 `target_type='raw_source'` 触发 IntegrityError）。
2. **审计视图**：`v_layer_violation`（双保险）、`v_claim_unsupported`（无证据主张扫描，UNVERIFIED 型与已否决者除外）、`v_banned_source`（P41 禁用来源）、`v_dangling_ref`（悬空跨库引用零容忍）。
3. **引用纪律**：层内引用用本库 TEXT 主键（FK 可校验）；跨库引用一律经 `cross_ref` 表，入库前校验目标存在，`validation_status='dangling'` 的记录禁止进入书稿流水线。

### 2.3 关键决策：L1 注册制而非迁移制

遗留一手档案（6 邮件库 + 11 仓库库，约 34 GB、976 万条记录）**留在原库**，raw_source 只登记 `(source_db, source_table, local_pk, content_hash)`：

- `source_id` 命名 `SRC-<namespace>:<本地键>`（如 `SRC-mail:<Message-ID>`、`SRC-commit:freebsd-src:a1b2c3`），**全局唯一 ID 一次解决**（02 报告缺口二）；
- `content_hash`（SHA-256）防正文漂移，审计时可抽样回验；
- 邮件/提交不必全量注册——按"章节需求清单"拉取（02 报告建议），`legacy_status` 跟踪 pending/migrated/verified 三态。

### 2.4 双轨编码警示（方向相反，全团队必须周知）

| 编码 | 定义 | 方向 | 出处 |
| ---- | ---- | ---- | ---- |
| `source_layer` INTEGER 1-5 | **史料五层级**（P41） | **1 最强**（代码产物）→ 5 最弱（二手研究） | 01 §P41 |
| `evidence_level` TEXT 'L1'-'L5' | **证据等级**（任务书第29阶段） | **L5 最强**（直接代码来源）→ L1 最弱（仅相关性） | 07 §2.3 |

两套编码方向相反且不可互相换算（一条第五层二手史料可以承载 L3 级文档证据；一条第一层代码可以只支撑 L1 级相关性主张）。DDL 已在 schema_meta 中分别登记约定；跨库快照字段（07 的 `source_layer`/`evidence_level` 并列）与此一致。

---

## 第三部分：20 个史料分类字段的落点（对 02 差距表的逐项兑现）

| # | 字段 | 02判定 | 落点（historical_claims.db） | 迁移来源 |
| - | ---- | :----: | ---------------------------- | -------- |
| 1 | source_type | 🟡 | raw_source.source_type，受控词表 controlled_vocab（11 值，与 P41 五层+载体对齐） | mat_type 四值映射（一手→按载体细分；未分类→pending 待人工）；source_tier 七值映射；ref_type 四值映射 |
| 2 | source_level | 🟡 | raw_source.source_layer（结构化 INTEGER，取代 trust_basis 自由文本） | 解析 trust_basis 的 `level:` + mat_type 交叉校正 |
| 3 | source_date | 🟡 | raw_source.source_date + date_precision | 邮件 messages.date / 提交 author_date（先过项目生命周期窗口裁剪）；书目 year |
| 4 | author | 🟡 | raw_source.author（原文）+ author_entity（FK→entity） | messages.from_name / commits.author_name / 文献 frontmatter.作者；素材层待考据 |
| 5 | organization | 🔴 | raw_source.organization + org_entity（FK→entity） | 新建；entity_relation('employed_by'/'member_of') 承载人-机构关系 |
| 6 | historical_period | 🔴 | source_period 多值表 → historical_period（六期预置） | 新建；由 source_date 初筛 + 人工确认（交叠期允许多值） |
| 7 | involved_persons | 🟡 | evidence_entity(role) + claim_entity → entity('person') | people_mentioned.person_normalized_name（6,568）+ person_records（1,141）归并；legacy_refs 留溯源 |
| 8 | involved_projects | 🟡 | entity('project') + evidence_entity | repos（38 仓库）+ 素材标题中的项目名；多项目多值 |
| 9 | involved_technologies | 🟡 | entity('technology') + evidence_entity | technologies_mentioned（7,185）+ terminology_index（237）归并 |
| 10 | involved_events | 🔴 | entity('event') + evidence_entity + timeline 类 evidence | 新建事件主数据；timeline_events（42,307）经审核后升格 |
| 11 | provenance | 🟡 | provenance_url/commit/archive + acquired_at + acquisition_method + provenance_history（多跳流转链） | url 三字段 + archive_url + clone_url；转载链新建 |
| 12 | citation_chain | 🟡 | claim_evidence（主张↔证据）+ claim_relation（主张↔主张）+ source_independence（史料↔史料）三张关系表分工 | material_cross_references（667）迁入 source_independence/claim_relation |
| 13 | reliability | 🟡 | reliability_grade A/B/C/D/U + reliability_rationale | trust_basis.level 映射（0→U，1→B/C 视载体，2→C）；key_facts.confidence 作为证据层参考 |
| 14 | independence | 🔴 | source_independence 表（independent/dependent/repost/conflict/common_source 五值边） | 新建；doubts 的 source_conflict（141 条）迁为 conflict 边 |
| 15 | first_hand | 🟡 | raw_source.first_hand 布尔 + tier_basis 判定理由 | mat_type='一手' 初值；判定理由强制留痕 |
| 16 | contemporary | 🔴 | raw_source.contemporary 布尔（与 retrospective 互斥 CHECK） | 新建；由 source_date 与所指事件时间差推算 + 人工确认 |
| 17 | retrospective | 🔴 | raw_source.retrospective 布尔 | 新建；回忆录/访谈/口述自动预置 1 |
| 18 | controversy | 🟡 | controversy + controversy_position；raw_source.doubt_flag 保留 | doubts_to_resolve（1,987）迁入；doubt_flag（1,607）随素材迁入 |
| 19 | relevant_claims | 🔴 | claim_evidence 反向查询即"史料关联了哪些主张"；claim_relation 承载主张间网络 | 新建（本库存在本身即兑现） |
| 20 | relevant_chapters | 🟢 | source_chapter（vol/ch/sec + link_type used/mentioned/background）**无损保留** | 资料库 vol/ch/sec 全量迁移（全仓唯一成熟关联，迁移零语义损失） |

**覆盖结果**：20 字段全部有落点；🔴7 项全部新建；🟢1 项无损保留；🟡12 项全部给出迁移来源与映射规则。

---

## 第四部分：历史主张数据库 schema 核心

### 4.1 claim 主表与十类主张

`claim_type` 十值枚举（任务书约定）：`FACT`（事实断言）、`CAUSAL_CLAIM`（因果主张，对接 07 因果箭头）、`INTERPRETATION`（解释性主张，L4 的入口）、`COMPARISON`（比较主张）、`INFLUENCE_CLAIM`（影响主张，对接 07 十二分类）、`ORIGIN_CLAIM`（起源主张）、`FIRST_APPEARANCE`（首次出现主张）、`MOTIVATION`（动机主张）、`CONTROVERSY`（争议性主张）、`UNVERIFIED`（未证实线索，合法入库但受措辞门禁约束）。

生命周期 `status`：proposed → supported / contested / refuted / superseded。**refuted 不物理删除**（对齐 07 §1.1：被推翻的主张同样是编纂史的一部分）。

**影响主张的整合决策**：07 §2.4 的 `impact_claim` 不再单独建表，而是 `claim_type='INFLUENCE_CLAIM'` + `impact_subtype`（十二分类枚举）落同一张 claim 表。理由：(1) claim_id 命名空间统一（IC- 前缀同表共存，07 的 `IC-<卷>-<序号>` 约定不变）；(2) claim_evidence/claim_entity/claim_period/claim_relation 四张关系表免建第二套；(3) 措辞门禁、审计视图一次覆盖。07 的 impact_claim DDL 保留为过渡设计文本，字段已 1:1 映射（impact_type→impact_subtype、source_ref/target_ref→claim_entity 的 source/object 角色、carriers→attrs JSON、linked_arrow_id/parent_claim_id/segment_claim_ids 保留同名字段或 JSON）。

### 4.2 证据挂接与反证纪律

`claim_evidence` 支撑/反证同表（role），每条反证必须走处置流程：`disposition`（NULL=未处置 → '已排除'/'并存'/'已采信推翻'）+ `search_log_ref`（**反证检索留痕**："找了没找到"的记录，对齐 07 §1.5 与任务书标准 1）。`strength` 四档（decisive/strong/weak/contextual）供措辞门禁与章节评分（Task #17）消费。

### 4.3 主张网络与实体、时期挂接

- `claim_relation` 六值边：supports/contradicts/supersedes/decomposes_from/presupposes/related——relevant_claims 字段（02 🔴 之一）在此兑现为可查询网络；
- `claim_entity` 带角色（subject/object/agent/location），使 07 的 source_ref/target_ref 结构化；
- `claim_period` 多值（六期交叠），研究定位可查"某期某相位的未决主张清单"。

### 4.4 争议簿（controversy）

`controversy_id` 文本主键（对齐 09 约定如 `openbsd_fork_motive`）；`controversy_position` 记录每方立场与 `sources_per_position`（JSON：`[{"source_id":"SRC-...","source_layer":2}]`，09 §争议系统原样承接）；立场可主张化（`claim_id` 回指）。doubts_standalone 1,987 条按 doubt_type 分流：source_conflict→争议簿；date/version/name/fact→对应主张的 contradicting 证据或争议；unresolvable 11 条→`status='irresolvable'`（诚实呈现，P43）。

### 4.5 解释层（interpretation）

`paradigm` 标注解释框架（如"权力再分配观（总纲13）""分离聚合循环（总纲14）"），`coexists_with` 显式登记并存解释——**多解释并存是本体论要求（P10）而非待消除的缺陷**；解释只许引 claim 与 evidence，不得越过证据直引原始史料。

---

## 第五部分：叙事层

`chapter` 迁移 metadata_interfaces.chapter_metadata 348 章骨架（vol/ch/sec 三级主键与现状完全兼容）；`narrative_unit` 是成书文本单元（节/边栏/脚注块/附录）；`narrative_citation` 是五层隔离的**硬闸门**——target_type CHECK 不含 'raw_source'，书稿引用必须经过主张/解释/证据。这直接落实 02 报告的核心诊断：终结"L1 素材直挂 L5 章节"的跨层路径。

---

## 第六部分：迁移映射（遗留 29 库 → 新库，不执行）

| 批次 | 目标表 | 来源 | 规模 | 关键规则 |
| ---- | ------ | ---- | ---- | -------- |
| M1 | historical_period / controlled_vocab / wording_gate_rule | 静态预置（DDL 已含） | 6/11/5 行 | 无需迁移 |
| M2 | entity('person') | cross_indexes.person_records（1,141）+ fulltext.people_mentioned 归一名（6,568）+ person_bio_research（158） | 归并后估计 3-5 千 | 归一表由人名对齐任务产出；legacy_refs 留三源 ID |
| M3 | entity('technology'/'project'/'org') | technologies_mentioned（7,185）+ repos（38）+ 组织机构索引残档 | 千级 | org 为🔴新建，需人工建档 |
| M4 | raw_source（素材批次） | 资料库.materials 24,129 | 24,129 | mat_type/trust_basis 映射见 §3；vol/ch/sec 随迁 source_chapter；**先裁日期脏区**（02 §2.3） |
| M5 | raw_source（书目批次） | fulltext.references 4,163 | 4,163 | source_tier 映射；author/year 缺口沿用 FULL_AUDIT_REPORT 结论（29.4%/20.7% 待补） |
| M6 | raw_source（一手档案批次） | 6 邮件库按章节需求拉取；11 仓库库按 commits 关联拉取 | 增量、不全量 | 只注册坐标+哈希；日期窗口硬裁剪 |
| M7 | evidence | fulltext.key_facts（8,354）+ timeline_events（42,307，需 event_date 校验） | 约 5 万 | source_block_id→anchor 'block:<db>:<id>'；confidence 原样 |
| M8 | controversy | doubts_standalone.doubts_to_resolve 1,987 | 1,987 | 分流规则见 §4.4 |
| M9 | chapter | metadata_interfaces.chapter_metadata 348 | 348 | status='outline' 原样 |

**同名异构消歧**（02 §4.2）：旧 `references` 素材级→namespace 'mat'，书目级→namespace 'ref'；旧 `blocks` 各库独立编号→anchor 一律写 `block:<库名>:<id>`。

**执行顺序约束**：M2/M3（实体）→ M4/M5/M6（史料注册）→ M7（证据）→ M8/M9（争议/章节）→ 主张层由研究流程逐步建立（不批量迁移，主张是研究产物不是迁移产物）。

---

## 第七部分：验收清单（未来建库时逐条核验）

1. DDL 在空库 executescript 通过，28 表/4 视图/4 触发器齐全（**本次已在临时库自测通过**，见 qa_tmp/_ddl_selftest_out4.json）；
2. 冒烟三测通过：L5 直引 L1 被 CHECK 拦截；contemporary/retrospective 互斥生效；v_claim_unsupported 对已举证主张返回 0 行；
3. 预置数据核验：六期年份与 01 §P44 原文一致；措辞门禁五行与 07 §2.3 原文一致；
4. 迁移后：v_dangling_ref = 0 行；v_banned_source 全部有 reliability_rationale；source_chapter 行数 ≥ 资料库现有挂钩数（无损）；
5. 双轨编码抽查 20 条：source_layer 与 evidence_level 无混用。

---

## 第八部分：遗留问题拍板与风险

### 8.1 主张库不采用 files/blocks 三件套

三件套（files/blocks/cross_references + FTS5）面向**文档块检索**；主张库是**强类型实体关系库**，全文检索需求由遗留各库 FTS 继续承担（经 cross_ref 回跳），跨库引用由 cross_ref 表统一治理。schema_meta/update_log 惯例保留。

### 8.2 拍板：因果链表组独立成库 causal_graph.db（回应 07 §1.4 的二选一）

07 号表组（causal_chain/causal_node/causal_arrow/causal_arrow_evidence/…）与本库的耦合点全部是 TEXT 引用位（claim_id/evidence_id/object_ref），无 SQL 级 FK 依赖。独立成库的理由：(1) 因果链是**高频迭代的审计过程库**，主张库是主数据性质，分离便于独立备份与回滚；(2) 07 表组自带完整 schema_meta/update_log，天然成库；(3) 与"注册制"哲学一致——过程产物与主数据分治。约束：causal_graph.db 的 `causal_arrow_evidence.evidence_id` 与本库 `claim_evidence.evidence_id` 必须同为 EV- 命名空间，建库时以 cross_ref 登记互指。两新库（historical_claims.db 与 causal_graph.db）的落盘目录（均置于 `04-现代研究文献/`）、folder_db_registry.csv 登记与备份要求，见 00 号文阶段 2 落位决策。

### 8.3 风险与缓解

| 风险 | 缓解 |
| ---- | ---- |
| 素材层 source_date/author 大面积缺失（🟡→实为待考据） | legacy_status='pending' + 研究问题清单驱动补考（Task #9 问题树消费），不阻塞建库 |
| 日期脏区污染时间轴 | M4/M6 前置窗口裁剪（02 §2.3 已点名 2085/1973/1960 三类） |
| 人名/机构归并产生新歧义 | M2/M3 产出归一映射表并留 legacy_refs 三源 ID，可回滚 |
| 双轨编码混用 | schema_meta 登记约定 + 验收第 5 条抽查 + 本文档 §2.4 周知 |
| L1 注册制下正文不可离线 | content_hash 抽样回验 + 原库只读纪律（本团队既有铁律） |

---

## 附录：表清单（v0.2 · 32 表）

> v0.1（本文档主体）28 表；v0.2 补编（Task #19，详见 `15-知识图谱与一致性检查.md`）新增 4 表 + 4 视图 + entity.time_start/time_end 两列，DDL 位于 06a 文件文末，自测 `qa_tmp/_ddl_selftest_out5.json`。

**横切**：schema_meta、update_log、historical_period、controlled_vocab、wording_gate_rule、entity、entity_relation、cross_ref
**L1**：raw_source、source_period、source_chapter、source_independence、provenance_history
**L2**：evidence、evidence_entity
**L3**：claim、claim_evidence、claim_entity、claim_period、claim_relation、controversy、controversy_position
**L4**：interpretation、interp_claim、interp_evidence
**L5**：chapter、narrative_unit、narrative_citation
**v0.2 知识图谱**：entity_type_class（18 细分）、entity_relation_type（24 关系）、consistency_rule（T1-T5/N1-N6）、consistency_check（审计留痕）

视图（8）：v_layer_violation、v_claim_unsupported、v_banned_source、v_dangling_ref、v_entity_alias_conflict、v_temporal_gap、v_relation_unsupported、v_unresolved_conflict。触发器：trg_claim_touch、trg_evidence_touch、trg_raw_source_touch、trg_interp_touch。

*设计文本，不建库不执行；DDL 自测产物存 qa_tmp/_ddl_selftest*。—— 洗澄明，2026-08-11
