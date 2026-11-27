# Tasks: login 数据库全量逐条判定入 claim 库与 05-大纲

**Input**: Design documents from `/specs/003-login-claim-outline/`

**Prerequisites**: plan.md（必读）、spec.md（用户故事）、research.md（决策 D1-D7）、data-model.md、contracts/、quickstart.md

**Tests**: 验证以只读 SQL 断言与门禁脚本为主（quickstart.md 场景），按任务内嵌而非独立 TDD 测试任务。

**Organization**: 任务按用户故事分组（US1 判定 → US2 claim 入藏 → US3 大纲同步 → US4 新建章 → US5 红线终检），每故事为可独立验收的增量。

## Format: `[ID] [P?] [Story] Description`

- **[P]**: 可并行（不同文件、无未完成依赖）
- **[Story]**: 所属用户故事（US1-US5）；Setup/Foundational/收尾阶段无 story 标签
- 描述含确切文件路径

## Path Conventions

- 引擎/写者/台账：`script/`（临时产物，CLAUDE.md 临时文件规则）
- 四件 spec 件：`specs/003-login-claim-outline/`
- 入藏目标：`historical_claims.duckdb`；判定回写：`login-zazhi.duckdb`（差量有痕）
- 大纲：`05-卷册大纲/第N卷/第XX章-slug/`（既有宿主章＋受控新建章）

## Phase 1: Setup

- [ ] T001 采集重构2026 只读基线：对 `08-核查报告与多轮复核/重构2026/` 全目录生成文件清单＋SHA-256 JSON 至 `script/_login_claim_baseline_20261006.json`（终检比对基线）
- [ ] T002 记录战役前行数基线：login-zazhi.duckdb（articles/issues/chunks/figures）与 historical_claims.duckdb（claim/raw_source/evidence/source_chapter）行数快照至 `script/_login_claim_rowbaseline_20261006.json`
- [ ] T003 [P] 建判定引擎骨架 `script/_login_claim_engine_20261006.py`：复用 `_glm_line_20261006.py`（KeyPool 轮替、线程池、断点续传、日志脱敏），CLI `--shard/--workers/--limit`——供滚动 40 路子代理按互斥分片运行
- [ ] T004 [P] 建入藏写者骨架 `script/_login_claim_writer_20261006.py`：单写者（唯一可写 claim 库进程）、事务批 200＋行数断言＋隔离文件＋游标（照 `_title_fix_writer_20261005.py` 与 `_fig_ocr_writer_20261006.py` 模式）
- [ ] T005 [P] 建大纲注入块写者骨架 `script/_login_claim_outline_20261006.py`：WO-007 幂等（import `00-编纂规则与格式规范/01-规则/脚本与命令/wo007_idempotency.py` 的 has_block/write_guard）

## Phase 2: Foundational（阻塞全部用户故事）

- [ ] T006 落判定 prompt 与判据集（引擎内嵌）：R1-R12 压缩集＋七类不写排查＋R11 广告价值判据＋十二阈值判定相关项（依据 research.md D3），输出结构化判定 JSON（verdict/significance/reasons[]/chapter_target）
- [ ] T007 落台账契约（ledger-contract.md）：台账 JSONL 读写函数＋幂等键（article_id）＋断点跳过逻辑（`script/_login_claim_engine_20261006.py`）
- [ ] T008 落 claim 入藏契约（claim-ingest-contract.md）：raw_source 注册（SRC-login:<id>＋content_hash）＋evidence（quote 原文照录）＋claim（CL-<卷>-<序号> 续排、claim_type 十值、wording_gate、evidence_level）＋claim_evidence＋source_chapter 的写库函数与校验（`script/_login_claim_writer_20261006.py`）
- [ ] T009 落大纲注入块契约（outline-inject-contract.md）：ROW_MINE 块体生成（证据等级从 claim 库读真值禁写死）＋WO-007 写入＋写后门禁调用（`script/_login_claim_outline_20261006.py`）
- [ ] T010 试点批（3 期 ≥30 篇，含至少 1 篇广告、1 篇目录噪声）：引擎判定→台账→（抽 3 条）入藏→（抽 3 条）大纲注入，全链跑通并人工检视；试点通过方开全量

## Phase 3: User Story 1 — login 全量逐条判定（P1）

**Story Goal**: 6,604 篇逐条综合分析、判定终态 100% 覆盖（含广告），理由与原则编号齐全；**滚动 40 路子代理（缺 1 补 1）执行，禁止抽查**。

**Independent Test**: 台账 6,604/6,604 唯一行；抽样含广告能回溯综合分析与原则编号；滚动派发无空转、失败子代理重派记录在案。

- [ ] T011 [US1] 滚动 40 路子代理派发（缺 1 补 1）：40 个并行子代理各领互斥分片运行 `script/_login_claim_engine_20261006.py --shard k`；分片完成即补领下一未完成分片直至 6,604 篇全量（`script/_login_claim_shards_20261006.jsonl` 分片清单＋派发记录；子代理失败/超时/零产出即重派；禁止抽查）至 `script/_login_claim_ledger_20261006.jsonl`
- [ ] T012 [US1] 台账覆盖率与唯一性断言：6,604/6,604、article_id 唯一、verdict 二值齐全、no_ingest 行 reasons 非空（只读 SQL）；失败清单按缺 1 补 1 重派
- [ ] T013 [US1] 全量二次复核（禁止抽查口径贯穿：6,604 逐条，非抽样）：对台账全部判定行做第二遍综合分析复核（滚动子代理或引擎，与首判独立提示词）——综合分析内容与原则编号回溯性、verdict 一致性、子代理产出回读核验（历史战役教训：子代理会臆造——按台账断言校验，不采信子代理自报）；两遍不一致行进入第三遍仲裁（三次复查流程）
- [ ] T014 [US1] 判定终态回写 login 库（差量 UPDATE 有痕，如需）：articles 增列或复用既有审计字段记录判定终态；update_log 登记

## Phase 4: User Story 2 — claim 库三层入藏（P2）

**Story Goal**: 判定 claim_ingest 者三层齐备（raw_source/evidence/claim），claim_id 唯一、quote 零改写。

**Independent Test**: 抽样任一 SRC-login 三层链回溯；quote 与 body_text 逐字一致。

- [ ] T015 [US2] 入藏写者全量跑：台账 claim_ingest 行按批 200 入 claim 库（raw_source→evidence→claim→claim_evidence→source_chapter），事务断言＋隔离＋游标（`script/_login_claim_writer_20261006.py`）
- [ ] T016 [US2] 三层齐备断言：每条 claim_ingest 台账行有 raw_source＋≥1 evidence＋≥1 claim＋≥1 source_chapter（只读 SQL）；缺口清单重派
- [ ] T017 [US2] quote 原文一致性抽检（≥100 条）：evidence.quote 与 login 库 body_text 逐字比对，零改写（噪声照录）；不一致行隔离重藏
- [ ] T018 [US2] 措辞门禁抽检：L1 级证据的 claim 无"继承/影响/源自/借鉴"表述；claim_id 全库唯一性断言
- [ ] T019 [US2] update_log 登记与备份指针（入藏批次/规模）；行数守恒（claim 库纯增量：基线+增量=现值）

## Phase 5: User Story 3 — 05-大纲同步（P2）

**Story Goal**: claim_ingest 者 source_chapter 挂钩＋宿主章 ROW_MINE 注入块，门禁全绿。

**Independent Test**: 抽样任一 SRC-login：source_chapter 行＋宿主章注入块，块头等级＝claim 库 evidence_level。

- [ ] T020 [US3] 大纲注入块写者全量跑（`script/_login_claim_outline_20261006.py`）：按 chapter_target 写宿主章注入块（WO-007 幂等＋证据等级真值），同批推进 claim 入藏
- [ ] T021 [US3] 证据等级门禁全绿：跑 `00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py`（exit 0）；失败行修正块头等级后重跑
- [ ] T022 [US3] 挂钩与注入块齐备断言：source_chapter 行数≥claim_ingest 台账行数（多值挂钩）、抽样宿主章文件 has_block 命中且无重复块（WO-007 幂等验证）
- [ ] T023 [US3] 触及时跑文档格式门禁 `audit_markdown_lint.py`（宿主章文件如入闸面）

## Phase 6: User Story 4 — 大纲不足时新建章（P3，条件触发）

**Story Goal**: 归类缺口主张按扩展接口新建章文件（数量留档）。

**Independent Test**: 新建章三步落位齐备（卷头登记/章文件夹/SUMMARY 同步），子节五字段。

- [ ] T024 [US4] 归类缺口清单：统计 chapter_target 无法命中既有 54 卷 454 章的 claim（只读 SQL），按主题聚类提出新建章提案（章题/位置/依据原则）——仅判定应入且确无承载章者
- [ ] T025 [US4] 按扩展接口新建章：卷 00-总览.md 登记章号标题→`第XX章-slug/index.md`＋子节文件（五字段、史观映射 ≥5 条总纲）→`sync_gitbook_summary.py --write` 同步 SUMMARY.md；插入章号递归重排
- [ ] T026 [US4] 新建章验证：结构验证脚本＋SUMMARY 含条目＋该章纳入注入块写入范围（回补 T020 漏挂钩条目）

## Phase 7: 收尾 — 红线终检（US5）

- [ ] T027 重构2026 零涉及终检：重采哈希清单与 T001 基线比对（`script/_login_claim_baseline_20261006.json`），零变更 exit 0
- [ ] T028 全量终检（quickstart.md 场景 1-6）：覆盖率 100%、三层齐备、门禁全绿、update_log 登记、行数守恒、零二进制
- [ ] T029 收尾文档：本战役报告（台账统计/入藏统计/新建章清单/门禁结果）落 `specs/003-login-claim-outline/`；login 库侧判定统计回写台账机读块；按波提交（pathspec 单独提，禁 add -f 除非主理人明示）

## Task Dependencies

- T003-T005 可并行；T006-T009 阻塞 T010；T010 阻塞 T011（试点门禁）
- US1（T011-T014）阻塞 US2（T015-T019）；US2 阻塞 US3（T020-T023）；US3 与 US4 的 T024 并行可行（T024 只读统计）
- US4（T025-T026）依赖 T024 且须在 T020 之后（新建章纳入注入块范围）
- US5（T027-T029）最后执行，阻塞于全部故事

## Parallel Execution Examples

- Setup：T003/T004/T005 三写者骨架并行搭建（不同文件）
- US2/US3 交叉推进：入藏批 N 完成后即可对批 N 跑大纲注入（同批两写者并行，互斥目标：claim 库 vs 大纲文件）
- US1 判定引擎分片：`--shard 0,1,2…`（互斥分片）与 writer 并行（判定只读 login 库，写者写 claim 库）

## Implementation Strategy

- **MVP = US1 全量判定**（台账 100% 即可交付主理人审阅判定质量；后续故事独立追加）
- 试点门禁（T010）先于全量；每阶段断言失败即停重派，不带病推进
- 全程红线：重构2026 只读（T001/T027 基线闭环）、Python 直跑不派子代理、密钥脱敏、禁二进制
