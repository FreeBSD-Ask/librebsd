# Feature Specification: login 数据库全量逐条判定入 claim 库与 05-大纲

**Feature Branch**: `003-login-claim-outline`

**Created**: 2026-10-06

**Status**: Draft

**Input**: User description: "对于login数据库，每条数据，即使是广告，也必须逐条遍历，根据本书既有规则。判断分析其历史意义，价值。从而是否应入本书claim数据库，如果是，必须同时按规则入05-大纲。应入本书而大纲不足以满足归类的，允许按规则新建大纲文件。过程中不得涉及任何重构2026文件夹（只读）。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - login 全量逐条判定（历史意义与价值的综合分析）(Priority: P1)

编纂者对 login 数据库（login-zazhi.duckdb）的**每一条文章记录**（6,604 篇，含广告、目录噪声、刊头启事等全部形态）**逐条遍历**，依据本书既有规则（《编纂原则清单》62 条、八项操作原则 R1-R12、十二项阈值标准、七类不写排查）对每条做**综合分析**——不限单一关键词匹配，而是综合其历史意义与价值（时代背景、当事人、技术/法律/社区/商业/文化五维关联、对本书各维度的证据价值），产出每条的**判定终态**：应入 claim 数据库 / 不应入（含理由与原则依据）。无史实价值的条目（如纯目录行）同样留痕判定过程，不得跳过；**禁止任何形式的抽查**。

**Why this priority**: 判定是后续一切入藏动作的前提；主理人指令明确"每条数据，即使是广告，也必须逐条遍历……逐条遍历，综合分析。禁止抽查"——全量无抽查＋综合分析是本任务的硬性起点。

**Independent Test**: 判定台账中每条 login 文章记录（含 kind='ad' 的广告行）各有一行判定终态；抽样任一篇（含一篇广告）能回溯到综合分析内容与所引原则编号。

**Acceptance Scenarios**:

1. **Given** login-zazhi.duckdb 的 6,604 篇文章记录（含 419 期全部形态），**When** 判定完成，**Then** 判定台账覆盖 6,604/6,604（100%），每条含综合分析内容、判定终态、理由与所引原则编号，禁抽查。
2. **Given** 一条 kind='ad' 的广告记录，**When** 判定处理它，**Then** 它获得与其他条目同等的逐条综合分析（不得因"是广告"而跳过；广告按 R11 利益分配分析等原则判定其史料价值，如 UNIX 商业化脉络中的广告证据）。
3. **Given** 判定为"不应入 claim 库"的条目，**When** 复核其台账行，**Then** 行内含综合分析与明确理由、所引原则编号（如七类不写排查判据），不臆造理由。

---

### User Story 2 - 判定应入者入 claim 数据库（historical_claims.duckdb）(Priority: P2)

对判定为"应入"的条目，按 claim 库既有 schema 与约定入藏：L1 raw_source 注册（source_id=`SRC-login:<article_id>`，坐标＋content_hash，不搬正文）、L2 evidence（quote 原文照录、fact_text、confidence）、L3 claim（claim_id 沿用 `CL-<卷>-<序号>` 命名空间续排；claim_type 十值枚举：FACT/ORIGIN_CLAIM/…/UNVERIFIED；evidence_level L1-L5；wording_gate 措辞门禁——L1 级禁写"继承/影响/源自/借鉴"；status 生命周期 proposed→supported/…）。全程遵循 0 信任原则与三次复查流程；被推翻/存疑的主张同样合法入库（refuted/UNVERIFIED 不物理删除）。

**Why this priority**: claim 库是本书五层体系（L1 史料→L2 证据→L3 主张→L4 解释→L5 叙事）的中枢；判定价值必须落为主张实体才算"入本书"。

**Independent Test**: 抽样任一入藏条目能按 `SRC-login:<id>` 定位 raw_source，沿 evidence 回溯原文 quote（与 login 库原文逐字一致），再沿 claim_evidence 到 claim 行；claim_id 在库内唯一。

**Acceptance Scenarios**:

1. **Given** 判定应入的一篇文章，**When** 入藏执行完成，**Then** raw_source 新增注册行（source_id 唯一、content_hash 存在）、evidence 行（quote 与 login 库原文逐字一致、未改写）、claim 行（claim_type/wording_gate/evidence_level 齐全）三层齐备。
2. **Given** 入藏的任一 claim，**When** 查其 wording_gate 字段，**Then** 措辞符合门禁规则（L1 级证据无"继承/影响/源自/借鉴"表述）。
3. **Given** 判定存疑的证据，**When** 入藏，**Then** claim 以 UNVERIFIED 类型或 status='contested' 合法入库并留反证/存疑处置记录，不默认为确证。

---

### User Story 3 - 入 claim 者按规则同步 05-大纲 (Priority: P2)

凡入 claim 库的条目，必须**同时**按规则落 05-大纲：(a) claim 库侧 source_chapter 挂钩（vol/ch/sec + link_type used/mentioned/background）；(b) 05-卷册大纲磁盘侧按 ROW_MINE 块体格式规则写入注入块（块头结构、当事人自述抬头、证据等级标注真值来源、引用纪律句），写入走 WO-007 幂等防护（has_block 检查 + write_guard），写回带等级标注的块后跑证据等级门禁。大纲写入不得触碰重构2026 目录（该目录为装配产物体系，本任务只读）。

**Why this priority**: 主理人指令"如果是，必须同时按规则入05-大纲"——入 claim 与入大纲是同一动作的两面，缺一即未完成。

**Independent Test**: 抽样任一入藏条目：claim 库侧 source_chapter 有对应行；05-卷册大纲对应宿主章文件有符合 ROW_MINE 格式的注入块，块内证据等级标注与 claim 库 evidence_level 一致。

**Acceptance Scenarios**:

1. **Given** 入藏的一条主张（映射到既有 54 卷 454 章中某章），**When** 大纲同步完成，**Then** 该章宿主文件新增符合 ROW_MINE 块体格式规则的注入块，且写盘经 WO-007 幂等防护（无重复块）。
2. **Given** 写回的注入块，**When** 跑证据等级门禁（audit_evidence_level_labels），**Then** 块内等级标注与 claim 库 evidence_level 逐条一致（门禁 exit 0）。
3. **Given** 同一条目重复执行大纲同步，**When** 二次写入，**Then** has_block 检查拦截重复追加，宿主文件内容不漂移。

---

### User Story 4 - 大纲不足归类时按规则新建大纲文件 (Priority: P3)

应入本书而既有 54 卷 454 章大纲不足以满足归类的条目，允许按 CLAUDE.md“新增章节”扩展接口新建大纲文件：目录 `05-卷册大纲/第N卷/第XX章-slug/`（slug ≤40 字符）、先在卷 00-总览.md 登记章号与标题、再建章文件夹与 index.md、最后运行 sync_gitbook_summary.py --write 同步 SUMMARY.md；子节按五字段结构（要点/史料/史观/辨析/文献）与史观映射（≥5 条总纲）填写。新建章号插入时依次递归修改受影响章节序号，不记成本。

**Why this priority**: 依赖 User Story 1-2 的判定与入藏结果（只有实际遇到归类缺口才触发）；且触及全书结构（SUMMARY/序号），须最后执行。

**Independent Test**: 任一新建章：卷 00-总览.md 有登记、章文件夹与 index.md 存在、SUMMARY.md 含该条目、章内子节为五字段结构。

**Acceptance Scenarios**:

1. **Given** 一条判定应入但既有大纲无承载章的主张，**When** 新建大纲文件完成，**Then** 新章按扩展接口三步落位（卷头登记→章文件夹→SUMMARY 同步）。
2. **Given** 新建章的子节，**When** 检查字段结构，**Then** 每子节含五字段且史观映射 ≥5 条总纲。
3. **Given** 新建章导致章号插入，**When** 结构验证，**Then** 受影响章号已递归重排、无缺号重复（sync_gitbook_summary 与结构验证通过）。

---

### User Story 5 - 全程红线与终检 (Priority: P3)

全程三条红线贯穿并终检收口：(a) 重构2026 目录（`08-核查报告与多轮复核/重构2026/`）**只读**——零写入、零改动、零删除，终检以其文件清单与内容哈希零变更断言；(b) 执行架构按主理人最新指令（2026-10-06）——**滚动 40 路子代理（缺 1 补 1）**执行判定，判定/入藏的 LLM 调用经引擎旧线路客户端（key 轮替、日志脱敏）；(c) 收尾终检——判定台账 100% 覆盖、claim 入藏三层齐备、大纲挂钩/注入块齐备、写库经 update_log 登记、行数守恒、零二进制。

**Why this priority**: 红线是约束不是交付物，但终检失败则全部返工；故列为收口故事。

**Independent Test**: 终检脚本输出：重构2026 哈希清单零变更、判定台账行数=6,604、claim 库行数守恒断言、update_log 有本战役登记。

**Acceptance Scenarios**:

1. **Given** 战役全程执行完毕，**When** 对重构2026 目录做文件清单与内容哈希比对（对战役开始前基线），**Then** 零变更（exit 0）。
2. **Given** 全部写库动作，**When** 查 update_log，**Then** 本战役的每次批量写入均有登记行（含备份指针）。
3. **Given** 入藏的 evidence.quote，**When** 与 login 库原文逐字比对抽检，**Then** 零改写（含原件笔误照录）。

---

### Edge Cases

- 广告/目录噪声/刊头条目：仍逐条判定（R11 利益分配分析等原则可能判定其有价值，如 UNIX 商业化广告证据）；判定不入者留理由，不得静默跳过。
- 判定冲突：同一证据支撑的主张相互矛盾时，按多版本并置原则（P55）并存入库（claim_relation contradicts 边），不择一淘汰。
- 大纲归类边界：一条主张可属多章/多期时，source_chapter 多值挂钩（link_type 区分），claim_period 多值（六期交叠为设计特性）。
- login 库原文为 OCR 噪声（如大写乱码）：evidence.quote 照录噪声原文（不篡改原则），claim 措辞按门禁处理；无法支撑主张的以 UNVERIFIED 合法入库。
- 新建章号插入冲突：章号插入须递归重排受影响章节，SUMMARY 同步失败时回滚本次新建并留痕。
- 引擎/API 故障：断点续传（台账/断点文件），重跑不产生重复写（幂等键＝article id + 批次）。
- 子代理失败/超时/臆造：缺 1 补 1 立即重派（滚动 40 路）；子代理产出须回读核验（历史战役教训：子代理会臆造页/误报自身处置——判定行按台账断言校验，不采信子代理自报）；会话中断连子代理——断点续传从队首缺口补派。

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: 判定引擎 MUST 对 login-zazhi.duckdb articles 表全部 6,604 行逐条遍历（含 kind='ad'/'toc'/'frontmatter'/'unknown' 全部形态），覆盖率 100%，禁抽查；每条产出判定终态（应入/不入）、理由与所引原则编号（62 条原则/八项操作原则 R1-R12 编号）。
- **FR-002**: 判定 MUST 依据本书既有规则执行并留痕：0 信任原则、三次复查流程（查证→交叉验证→判定）、判定理由可回溯到所引原则条文；七类不写排查（BSD 版本列表项已放开、其余六类）作为判定判据之一。
- **FR-003**: 判定应入者 MUST 按既有 schema 入藏 claim 数据库（historical_claims.duckdb）：raw_source 注册行（source_id=`SRC-login:<article_id>`、坐标＋content_hash、不搬正文）；evidence 行（quote 原文照录零改写、fact_text、confidence）；claim 行（claim_id 沿用 `CL-<卷>-<序号>` 命名空间续排、claim_type 十值枚举、evidence_level L1-L5、wording_gate 措辞门禁、status 生命周期）。
- **FR-004**: 入藏 MUST 遵循证据纪律：claim_evidence 支撑/反证同表（role + disposition）；存疑主张以 UNVERIFIED/contested 合法入库不默认确证；反证检索留痕。
- **FR-005**: 入 claim 者必须同时按规则同步 05-大纲：claim 库侧 source_chapter 挂钩（vol/ch/sec、link_type used/mentioned/background、多值）；05-卷册大纲磁盘侧按 ROW_MINE 块体格式规则写入注入块，写盘走 WO-007 幂等防护（has_block + write_guard），写后跑证据等级门禁（audit_evidence_level_labels）并全绿。
- **FR-006**: 既有大纲不足以归类时 MUST 按 CLAUDE.md“新增章节”扩展接口新建大纲文件（卷 00-总览.md 登记→章文件夹与 index.md→sync_gitbook_summary.py --write；子节五字段、史观映射 ≥5 条总纲；插入章号递归重排）；仅在此条件下允许新建，禁止为省归类而滥建。
- **FR-007**: 全程 MUST 不涉及任何重构2026 文件夹（`08-核查报告与多轮复核/重构2026/` 只读：零写入/零改动/零删除），终检以其文件清单与内容哈希对战役前基线零变更断言。
- **FR-008**: 执行架构 MUST 遵循主理人最新指令（2026-10-06 新增要求，取代本战役此前“不派子代理”表述）：**滚动 40 路子代理（缺 1 补 1）**执行逐条判定与综合分析——每个子代理领取互斥分片运行 Python 判定引擎（引擎直调既有线路、key 轮替），分片完成即补领下一未完成分片直至全量；子代理失败/超时即重派（缺 1 补 1）；主会话只派发与排障。临时脚本只放 script/；全部落盘文件入库（sha256 去重）。
- **FR-009**: 全部写库/写大纲动作 MUST 经 update_log 登记（含批次、规模、备份指针）；行数守恒断言（login 库零改写或差量 UPDATE 有痕；claim 库纯增量）；零二进制入库。
- **FR-010**: 判定与入藏 MUST 支持断点续传与幂等重放（断点文件＋幂等键），中断后重跑不产生重复写或行数漂移。

### Key Entities *(include if feature involves data)*

- **login 文章记录**（articles 6,604 行）：遍历与判定对象；含 title/authors/body_text/kind（article/column/news/ad/toc/frontmatter）/seg_review_status；判定终态挂其上。
- **判定台账**：每条文章一行的判定记录（终态/理由/原则编号/证据指针），断点与幂等键载体。
- **raw_source**（L1）：login 史料的注册制坐标（SRC-login:<id> + content_hash）。
- **evidence**（L2）：quote（原文照录）+ fact_text + confidence；支撑/反证。
- **claim**（L3）：历史主张（claim_type 十值、evidence_level、wording_gate、status）；393,153 行既有库续排。
- **source_chapter**：L1→L5 挂钩（vol/ch/sec/link_type）。
- **05-卷册大纲**（54 卷 454 章 3683 节现行口径）：宿主章文件与注入块；新建章文件（若有）。
- **重构2026 目录**：只读对象，零变更基线。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 判定台账覆盖 6,604/6,604 篇（100%），含全部广告与噪声条目，每条有终态＋理由＋原则编号。
- **SC-002**: 判定应入者 100% 完成 claim 库三层入藏（raw_source/evidence/claim 齐备），claim_id 全库唯一，quote 与原文逐字一致（抽检零改写）。
- **SC-003**: 判定应入者 100% 完成 05-大纲同步（source_chapter 挂钩＋宿主章注入块），证据等级门禁 exit 0，WO-007 幂等零重复块。
- **SC-004**: 新建大纲文件（若触发）100% 按扩展接口落位（卷头登记＋SUMMARY 同步＋五字段结构），数量与理由留档。
- **SC-005**: 重构2026 目录对战役前基线零变更（文件清单与内容哈希比对 exit 0）。
- **SC-006**: 全部批量写库经 update_log 登记（含备份指针），行数守恒断言通过，零二进制列。
- **SC-007**: 断点续传验证：任一中断点重跑后行数无漂移、无重复写。
- **SC-008**: 滚动子代理验证：40 路滚动派发全程无空转（缺 1 补 1），失败子代理重派记录在案，最终分片覆盖率 100%。

## Assumptions

- “每条数据”以 **articles 表 6,604 篇为遍历主对象**（含广告/目录/刊头全部形态）；figures 12,403 项已有独立的图文映射与 review 体系（此前战役闭环），chunks 42,445 为分块派生物——二者本轮不并入逐条判定范围（如主理人另有指令可增量扩展）。
- claim_id 沿用既有 `CL-<卷>-<序号>` 命名空间按卷续排；login 为横向素材，其主张归属所映射的大纲卷。
- “按规则入05-大纲”＝claim 库侧 source_chapter 挂钩＋05-卷册大纲磁盘侧 ROW_MINE 注入块双面（与既有邮件挖掘战役同构）。
- 判定引擎的模型与执行架构：**滚动 40 路子代理（缺 1 补 1）＋Python 判定引擎**（主理人 2026-10-06 新增要求，取代本战役此前“不派子代理”表述；子代理运行互斥分片的判定引擎，引擎直调旧线路 glm-5.3-flash、key 轮替）。
- 新建大纲文件的触发条件从严：仅当既有 54 卷 454 章确无承载章且判定应入时；触发即按扩展接口三步落位。
- 六期分期（P44）与六期交叠为 claim_period 多值设计特性；判定时按六期表定位。
