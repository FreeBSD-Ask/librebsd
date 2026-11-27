# Tasks — 重构2026 建议书与待执行待办任务合并总账

**Input**: Design documents from `/specs/004-refactor2026-backlog-merge/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

> change-id：`004-refactor2026-backlog-merge`
> 指令依据：主理人 2026-10-09 令“找出重构2026/index.html下的有关建议书和待执行的最近的spec。合并执行待办任务。”
> 认定：**最近的 spec ＝ `.trae/specs/converge-all-remaining-tasks/`**（唯一任务书）；次级＝`.trae/specs/finalize-refactor2026/`；建议书族＝`08-核查报告与多轮复核/重构2026/` 00–125 号文；唯一对账入口＝92 号文 §十一。
> 纪律：0 信任实测；UTF-8 无 BOM／LF；禁直角引号与“谱系”词；同一内容源不可并行编辑；只改内容源，`index.html` 由装配器生成。
> **边界**：Phase 1–4（T001–T019）为本 spec 自身的产出（文档级，可直接执行）；**Phase 5–7 之施工类任务（T020–T049）须经主理人批准后另批执行**，本 spec 不自行开工。

## Format: `[ID] [P?] [Story] Description`

- **[P]**：可并行（不同文件、无未完依赖）
- **[Story]**：归属用户故事（US1／US2／US3／US4）；Setup／Foundational／Polish 相无此标记
- 每条含**明确文件路径**；施工类任务含 `（映射 converge:T#.#）` 以对账唯一任务书

## Path Conventions

- 本 feature 文档：`specs/004-refactor2026-backlog-merge/`
- 唯一任务书：`.trae/specs/converge-all-remaining-tasks/tasks.md`
- 内容源（唯一）：`08-核查报告与多轮复核/重构2026/data/outline.txt`
- 装配产物（禁手改）：`08-核查报告与多轮复核/重构2026/index.html`

---

## Phase 1: Setup（本 spec 落点）

- [ ] T001 建立合并清单落点与来源索引，登记五源（A–E）之路径与权威性于 `specs/004-refactor2026-backlog-merge/research.md`
- [ ] T002 [P] 固化三契约（来源／映射／落账）与文本纪律于 `specs/004-refactor2026-backlog-merge/contracts/backlog-ledger-contract.md`
- [ ] T003 [P] 固化合并条目实体、来源/载体/落账实体、状态机与不变量于 `specs/004-refactor2026-backlog-merge/data-model.md`

---

## Phase 2: Foundational（阻塞性前置）

**⚠️ CRITICAL**: 本相完成前，任何用户故事任务不得开始。

- [ ] T004 冻结基线快照：记录现跑口径（`08-核查报告与多轮复核/重构2026/index.html` doc-metrics）与勾选状态（`.trae/specs/converge-all-remaining-tasks/tasks.md`），落 `specs/004-refactor2026-backlog-merge/research.md`
- [ ] T005 建立映射表：本 spec 任务 ↔ 唯一任务书 Task/SubTask（含未勾 Task 2–7 全覆盖），落 `specs/004-refactor2026-backlog-merge/research.md`

---

## Phase 3: User Story 1 — 定位“最近的 spec”与建议书待执行面（Priority: P1）🎯 MVP

**Goal**: 0 信任核定，产出可复核的来源清单与实测证据。
**Independent Test**: 每个被认定为“最近的 spec”的目录给出路径＋判据；每个待办项给出可定位证据锚点。

- [ ] T006 [US1] 定位并留证“最近的 spec”，落 `specs/004-refactor2026-backlog-merge/research.md` §R1（路径／mtime／`change-id`／勾选状态）
- [ ] T007 [P] [US1] 排除主题不相关 spec 并留痕（比对 `specs/003-login-claim-outline/spec.md` 之“不得涉及重构2026”约束），落 `specs/004-refactor2026-backlog-merge/research.md` §R1
- [ ] T008 [P] [US1] 逐源取证·源 A：`.trae/specs/converge-all-remaining-tasks/tasks.md` 未勾 Task 2–7 及其 SubTask，落 `specs/004-refactor2026-backlog-merge/research.md` §R2-A
- [ ] T009 [P] [US1] 逐源取证·源 B：`.trae/specs/finalize-refactor2026/tasks.md` 剩余 Task 5／6／8／10 之并入关系，落 `specs/004-refactor2026-backlog-merge/research.md` §R2-B
- [ ] T010 [P] [US1] 逐源取证·源 C：`08-核查报告与多轮复核/重构2026/124-重构2026收官阶段建议书-20261008.md`／`125-重构2026收官总案-20261008.md`／`92-目录内容调整建议书-综合释疑库与未实施建议.md` §十一 未闭环项，落 `specs/004-refactor2026-backlog-merge/research.md` §R2-C
- [ ] T011 [P] [US1] 逐源取证·源 D：`08-核查报告与多轮复核/重构2026/review_logs/毕其功于一役-总任务账-20261009.md` 与 `08-核查报告与多轮复核/重构2026/review_logs/批5b总收官对账-20261009.md` §六 备核 6 项，落 `specs/004-refactor2026-backlog-merge/research.md` §R2-D
- [ ] T012 [P] [US1] 逐源取证·源 E：`01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md` 17 线（`_longline_status.py` 现跑），落 `specs/004-refactor2026-backlog-merge/research.md` §R2-E
- [ ] T013 [US1] 汇总来源清单与证据锚点，核 V1（锚点可定位、不指临时目录），落 `specs/004-refactor2026-backlog-merge/research.md`

**Checkpoint**: US1 完成——来源认定唯一、五源取证齐备，可独立交付。

---

## Phase 4: User Story 2 — 合并为单一可执行清单（Priority: P2）

**Goal**: 去重·定档·定序·可判定，并与唯一任务书一一映射。
**Independent Test**: 任一原分散待办项能定位到唯一一行；任一行能回溯来源；与总账一一映射。

- [ ] T014 [US2] 去重合并（同一事项只列一次、取范围最大者），落 `specs/004-refactor2026-backlog-merge/tasks.md`（承 D1）
- [ ] T015 [US2] 逐条定档（卷级／章级／节级／注级／零节变／非内容层）与定序，落 `specs/004-refactor2026-backlog-merge/tasks.md`（承 D2／D3）
- [ ] T016 [US2] 逐条标注前置（含“磁盘 156 章”待批注项），落 `specs/004-refactor2026-backlog-merge/tasks.md`（承 D4）
- [ ] T017 [US2] 验收措辞可判定化，核 V2（模糊词＝0），落 `specs/004-refactor2026-backlog-merge/tasks.md`
- [ ] T018 [US2] 双向追溯校验：spec 需求 ↔ tasks 条目 ↔ checklist 项互指（FR-006），落 `specs/004-refactor2026-backlog-merge/tasks.md` 与 `specs/004-refactor2026-backlog-merge/checklist.md`
- [ ] T019 [US2] 映射对账：与 `.trae/specs/converge-all-remaining-tasks/tasks.md` 一一映射、无新增施工面（核 V3、契约 §2），落 `specs/004-refactor2026-backlog-merge/contracts/backlog-ledger-contract.md` 附录

**Checkpoint**: US2 完成——合并清单成立，可独立交付。

---

## Phase 5: User Story 3 — 按序分批执行待办任务（Priority: P3）

> **⚠️ 须主理人批准后另批执行**；每批走收束铁律（改内容源 → 装配 → 字体子集 → 再装配 → 门禁全量 → 三套回归 → 落账 → 版本递增 → 提交）。
> 同一内容源 `08-核查报告与多轮复核/重构2026/data/outline.txt` 不可并行编辑；标 [P] 者指**不同载体**可并行。

- [ ] T020 [US3] 阶段 3 史料回填（承 Batch 2–6：V17／V10／V18／V15／V6 DVB 11 章＋29 待补块；旧卷号按现行结构重锚），改 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T2.1）
- [ ] T021 [US3] 阶段 4 章级改写（原 355→181／243 口径按现行 65 卷结构重推后执行），改 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T2.2）
- [ ] T022 [US3] 阶段 5 一致性核查（T5 系规则），改 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T2.3）
- [ ] T023 [US3] 阶段 6 总纲对接，改 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T2.4）
- [ ] T024 [US3] 46 处悬空分工注清结（第五／十四件零悬空、零重复），改 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T2.5）
- [ ] T025 [US3] SUMMARY／元数据三源回写（55 号文 T2.2／T7；`sync_gitbook_summary.py --check` PASS），改 `08-核查报告与多轮复核/重构2026/data/outline.txt` ＋ `SUMMARY.md`（映射 converge:T2.6）
- [ ] T026 [US3] Task 2 收束：门禁全量＋三套回归 FAILED=0＋落账（`01-项目管理/00-变更记录/changelog.duckdb` ＋ `08-核查报告与多轮复核/重构2026/92-目录内容调整建议书-综合释疑库与未实施建议.md` §十一）（映射 converge:T2.7）
- [ ] T027 [P] [US3] 【**本轮暂缓**·不迁移大纲目录（主理人 2026-10-09 令）】磁盘层·丁-2：347 条节级修订待办表（357 文件 REVIEW-ANNOT 批注块）逐条处置，改 `05-卷册大纲/`（映射 converge:T3.1）
- [ ] T028 [P] [US3] 【**本轮暂缓**·不迁移大纲目录】磁盘层·批量面：数词概括式 20 处＋`[存疑脚注]` 转换面（约 3267 处），改 `05-卷册大纲/`（映射 converge:T3.2）
- [ ] T029 [US3] 【**本轮暂缓**·不迁移大纲目录；另待裁定：磁盘 156 章维持搁置否】磁盘层·结构面：b 线第 22 卷 B3–B4／第 23 卷拆分对齐／73–74 号文磁盘判定／磁盘 156 章疑似未迁移，改 `05-卷册大纲/`（映射 converge:T3.3）
- [ ] T030 [P] [US3] 史料库层：存疑库 2415 条写回／编程之夏 S2–S4／播客库采集（83 号文），改 `04-现代研究文献/` 与 `12-数据库备份/`（映射 converge:T3.4）
- [ ] T031 [P] [US3] 载体层：84 号文体例残留复核／收尾，改 `08-核查报告与多轮复核/重构2026/assets/doc.css`（映射 converge:T3.5）
- [ ] T032 [US3] Task 3 收束：门禁全量＋三套回归 FAILED=0＋落账（`01-项目管理/00-变更记录/changelog.duckdb` ＋ `08-核查报告与多轮复核/重构2026/92-目录内容调整建议书-综合释疑库与未实施建议.md` §十一）（映射 converge:T3.6）
- [ ] T033 [P] [US3] ;login: 杂志线：标题治理全量（236 期，先修 2.6 阻塞）→ OCR 主战役（16,806 项）→ 双通道复核 → 入大纲流水线（5,510 篇）→ 收尾，改 `15-login杂志史料/` 与 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T4.1）
- [ ] T034 [P] [US3] 存疑标记“双轨同号”线：先导样本收尾＋全量推广，改 `05-卷册大纲/`（映射 converge:T4.2）
- [ ] T035 [P] [US3] 邮件库线挂起项：`digest-linux-mining-legacy-phase3` Task 6.2 等（前置：figures 库邮箱域拆分重灌），改 `03-原始史料库/11-邮件列表史料/`（映射 converge:T4.3）
- [ ] T036 [P] [US3] 播客线＋其余近线 spec 未勾项按 Task 0 核定处置，改 `03-原始史料库/` 播客库与 `.trae/specs/podcast-*/`（映射 converge:T4.4）
- [ ] T037 [US3] Task 4 收束：门禁全量＋三套回归 FAILED=0＋落账（`01-项目管理/00-变更记录/changelog.duckdb` ＋ `08-核查报告与多轮复核/重构2026/92-目录内容调整建议书-综合释疑库与未实施建议.md` §十一）（映射 converge:T4.5）
- [ ] T038 [US3] Task 5.1 历批备核 6 项全库普查（`08-核查报告与多轮复核/重构2026/review_logs/批5b总收官对账-20261009.md` §六）（映射 converge:T5.1）
- [ ] T039 [US3] Task 5.2 阶段二专项新登记清零（散落 14 处／待核 58 条／92 号文历史行引号／2 件旧 CRLF），据 `08-核查报告与多轮复核/重构2026/review_logs/阶段二专项Task5-散落项登记与未获一手待核清单-20261009.md`（映射 converge:T5.2）
- [ ] T040 [US3] Task 5.3 98 号文 §十一 总账刷新与全量对账，改 `08-核查报告与多轮复核/重构2026/98-建议书状态总账与最新建议-20260930.md`（映射 converge:T5.3）
- [ ] T041 [US3] Task 5.4 98 号文残项清零（9 小项），改 `08-核查报告与多轮复核/重构2026/98-建议书状态总账与最新建议-20260930.md` 与 `08-核查报告与多轮复核/重构2026/data/outline.txt`（映射 converge:T5.4）
- [ ] T042 [US3] Task 6 ★22 残留终校：映射表／卷引重指向／卷头 65 行／三表／全量验收，改 `08-核查报告与多轮复核/重构2026/data/outline.txt`【前置：T020–T041 完成】（映射 converge:T6）
- [ ] T043 [US3] Task 7 总收官冻结：三源交叉复核／长线刷新／冻结声明，改 `01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md`【前置：T042 完成】（映射 converge:T7）

**Checkpoint**: 全部待执行项收束；结构冻结生效。

---

## Phase 6: User Story 4 — 双重台账防线与收官勾销（Priority: P3）

**Goal**: 守住唯一任务书边界，防双写，收官勾销。
**Independent Test**: 任一事项仅在一处处于在途；被并入 spec 均有标注。

- [ ] T044 [US4] 台账在途唯一性核验（核 V5、不变量 I1），落 `specs/004-refactor2026-backlog-merge/checklist.md`
- [ ] T045 [US4] 被并入 spec 统一勾销／标注并入（`finalize-refactor2026`／`execute-login-title-fix-and-figures-ocr`／`write-doubt-marker-taskbook-2026-09-30`／`mail2d-*`／`podcast-*`／`digest-linux-mining-legacy-phase3` 等），改 `.trae/specs/` 各件（映射 converge:T7.3）
- [ ] T046 [US4] 冻结声明落盘并刷新长线任务总登记表机读块（`_longline_status.py --write-block`），改 `01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md`（映射 converge:T7.2）

---

## Phase 7: Polish & Cross-Cutting Concerns

- [ ] T047 [P] 文本纪律全库扫描：直角引号＝0／“谱系”词＝0／BOM＝0／CRLF＝0（以现跑扫描为准），扫 `08-核查报告与多轮复核/重构2026/data/outline.txt`
- [ ] T048 [P] 跑 `specs/004-refactor2026-backlog-merge/quickstart.md` 四场景并留痕
- [ ] T049 本 spec 收束落账：`01-项目管理/00-变更记录/changelog.duckdb` ＋ `08-核查报告与多轮复核/重构2026/92-目录内容调整建议书-综合释疑库与未实施建议.md` §十一 ＋ `08-核查报告与多轮复核/重构2026/98-建议书状态总账与最新建议-20260930.md` §十一 ＋ `08-核查报告与多轮复核/重构2026/review_logs/` 收官记录（映射 converge:T7.4）

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup（Phase 1）**：无依赖，可立即开始。
- **Foundational（Phase 2）**：依赖 Setup 完成；**阻塞全部用户故事**。
- **US1（Phase 3）**：依赖 Phase 2 完成。
- **US2（Phase 4）**：依赖 US1（须先核定才能合并）。
- **US3（Phase 5）**：依赖 US2（须先有合并清单）；**须主理人批准**。
- **US4（Phase 6）**：与 US3 并行推进，收官段依赖 US3 之 T042／T043。
- **Polish（Phase 7）**：依赖全部期望故事完成。

### 内部依赖（关键序位）

- T020 → T021 → T022 → T023 → T024 → T025 → T026（同一内容源，**串行**）
- T027／T028／T030／T031 为不同载体，**可与 T020–T026 并行**
- T029 **阻塞于主理人裁定**（磁盘 156 章）
- T033／T034／T035／T036 为不同线，**互相可并行**
- **T042（★22 终校）依赖 T020–T041**；**T043（总收官）依赖 T042**
- T044 可与 T020–T043 并行；T045／T046 依赖 T043

### Parallel Opportunities

- Phase 1：T002 与 T003 可并行
- Phase 3：T007–T012 六项可并行
- Phase 5：T027／T028／T030／T031 并行；T033–T036 并行（不同线）
- Phase 7：T047 与 T048 可并行

---

## Parallel Example: User Story 1

```bash
# 六源取证可同时开动（不同文件、无依赖）：
Task: "T008 逐源取证·源 A：未勾 Task 2–7 → research.md §R2-A"
Task: "T009 逐源取证·源 B：finalize-refactor2026 剩余 → research.md §R2-B"
Task: "T010 逐源取证·源 C：建议书族 124／125／92§十一 → research.md §R2-C"
Task: "T011 逐源取证·源 D：review_logs 总账与备核 → research.md §R2-D"
Task: "T012 逐源取证·源 E：长线 17 线 → research.md §R2-E"
```

## Parallel Example: User Story 3（不同载体）

```bash
# 磁盘层与史料库层／载体层为不同载体，可并行：
Task: "T027 磁盘层·丁-2 347 条 → 05-卷册大纲/"
Task: "T030 史料库层：存疑库 2415 条／编程之夏 S2–S4 → 04-现代研究文献/"
Task: "T031 载体层：84 号文体例残留复核 → 重构2026/assets/doc.css"
```

---

## Implementation Strategy

### MVP First（仅 User Story 1）

1. 完成 Phase 1：Setup
2. 完成 Phase 2：Foundational（**阻塞全部故事**）
3. 完成 Phase 3：US1（定位与核定）
4. **STOP and VALIDATE**：独立验证“最近的 spec”认定唯一、五源取证齐备
5. 交付 US1 结论

### Incremental Delivery

1. Setup ＋ Foundational → 落点与映射就绪
2. ＋US1 → 来源认定与核定（**MVP**）
3. ＋US2 → 合并清单成立（本 spec 的完整交付）
4. ＋US3（经主理人批准，逐批）→ 待执行项收束
5. ＋US4 → 双重台账防线与收官勾销

### 交付边界

- **本 spec 的完整交付＝Phase 1–4（T001–T019）**：产出四件（spec／plan／tasks／checklist）＋研究／设计件。
- **Phase 5–7（T020–T049）为施工面**，须经主理人批准后另批执行；执行台账唯一真身为 `.trae/specs/converge-all-remaining-tasks/tasks.md`。

---

## Notes

- [P] 任务＝不同文件／不同载体，无依赖
- [Story] 标记用于追溯
- 每批施工须 prebak 备份先行；收束铁律全绿方算完成
- 施工类任务一律附 `（映射 converge:T#.#）`，便于与唯一任务书对账
