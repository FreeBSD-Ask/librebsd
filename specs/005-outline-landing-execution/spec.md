# Feature Specification: 05 大纲落地生产执行（Task 2 收尾／Task 4／Task 5，主代理形态）

**Feature Branch**: `005-outline-landing-execution`

**Created**: 2026-10-24

**Status**: Draft

**Input**: User description: “复核05-大纲落地Task1-2-4-5任务书-20261023.md任务书，确认任务内容，建立完整符合本项目软件工程理论的规划，不计成本代价，把子代理的任务转为主代理，不使用子代理”

## 缘起与范围界定

ykla 2026-10-24 令（三要件）：①**复核并确认**[05-大纲落地Task1-2-4-5任务书-20261023.md](../../01-项目管理/01-编纂规划与报告归档/05-大纲落地Task1-2-4-5任务书-20261023.md)的任务内容；②建立**完整符合本项目软件工程理论**（`00-编纂规则与格式规范/01-规则/工程实践规则.md`：需求基线／追溯链／L0–L5／任务审计 L1–L12／复核轮次／技术债／门禁接线）的执行规划，**不计成本代价**（项目最高规则：学术性与学术规范优先）；③**把子代理的任务转为主代理，不使用子代理**——原任务书 §4.5“可派独立复核子代理”的通道**就此关闭**，三路复核改由主代理串行执行（方案见 User Story 3 与 `contracts/three-pass-review.md`）。

**复核结论（2026-10-24 本会话逐件对账，作为本 spec 的需求事实基线）**：

- 输入真值三源互证一致：`outline.txt` 75 卷 523 章 3,705 节；`targets.tsv` 4,303 节点（C-0001…C-0523）；旧树 37,486 个 `.md`（37,484 子节＋2 个根级非子节）。
- Task 1（基线冻结）／Task 3（目标注册表）已完成；Task 2 完成 7/11——**剩 2.1a／2.1b／2.1c／2.1d＋2.4a 台账补录**；Task 4／Task 5 未开工（干执行“前置已核”）。spec 全景 34/104。
- 干执行实物：`mapping.sim.tsv` 实测 20.9 MB（16 列×37,484 行）；旧树反引号文件名 6,291 件；卷切分 26–9,454 条不均。
- 工程底盘已就绪：长线第 13 条 `landing05` 已立（真值 `映射/mapping.tsv`，探针在未生成期报 0/37,484）；批次排程件[05-大纲落地生产执行计划-20261024.md](../../01-项目管理/01-编纂规划与报告归档/05-大纲落地生产执行计划-20261024.md)已立（B1–B4／B5–B7／W1–W6）。

**防双账边界**：`.trae/specs/migrate-refactor2026-into-outline-20261023/tasks.md` 仍是施工勾选面的**唯一真身**；本 feature 的 `tasks.md` 与之**逐条映射**（每任务标注对应 SubTask 号），不另立并行台账。判据正文以 `.trae` spec 与 `01-规则/` 为准，冲突从后者。

**写入边界（全程）**：只写 `05-卷册大纲/映射/`、`script/` 临时区与 `01-项目管理/01-编纂规划与报告归档/`（台账文书）；禁写 `outline.txt`、`index.html`、卷／章／节目录、根级三件派生件。禁旁路备份；禁自动化；**禁用 Agent 工具派发子代理（ykla 2026-10-24 令）**。

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 旧树文件名合规可迁移（Task 2 收尾）(Priority: P1)

编纂者把旧树文件名整理到可迁移状态：2.1b 机械标准化（6,291 件反引号文件名，以 H1 为真值）＋2.4a 台账补录（约 160 行，由 outline 前置源 `c90a3c62b`→`d6853f29c` 题面差异重建）；2.1c 语义建议表（21,031 条只出表不自动改名，裁决权在 ykla）；2.1d 路径兼容复测；2.1a 派生件再生并冻结。

**Why this priority**: 2.1b 是 Task 4 开工的**硬前置**（任务书 §2.4 结论修正：反引号不修，迁移后文件名在 Windows 与 URL 两处出问题）；整条关键路径由此起步。

**Independent Test**: `映射/title-standardization.tsv` 落盘且每行 `sha256_before == sha256_after`；对旧树复扫六类机械违规计数全 0；`title-review.tsv` 覆盖 21,031 条且改名执行数 0；旧树派生三件再生后门禁 PASS 且宣告冻结。

**Acceptance Scenarios**:

1. **Given** 旧树 6,291 个反引号文件名，**When** 2.1b 执行完毕，**Then** 全库文件名反引号计数 0、每件改名前后 SHA-256 相等、新名保留 `编号-` 前缀连字符约定（dry-run F1 规则）、`title-standardization.tsv` 行数＝6,291＋168。
2. **Given** 21,031 条杂质名／短名，**When** 2.1c 出表，**Then** `title-review.tsv` 逐条含建议标题／风险级／理由，覆盖率 100%，且期间没有任何文件因“语义”被改名。
3. **Given** B1 改名完成后的旧树，**When** 2.1d 复测，**Then** 绝对路径 >260、保留名、尾点尾空格、大小写冲突四类命中为 0 或全数入 `path-overlong.tsv`（未裁决不得迁移）。
4. **Given** 2.1b 已完成，**When** 2.1a 再生派生三件，**Then** `audit_keyword_index.py`／`audit_mirror_ingest.py` PASS，`映射/README.md` 声明快照冻结。

### User Story 2 - 映射台账就绪（Task 4）(Priority: P1)

编纂者建立“旧子节→目标节”唯一映射台账：`mapping.tsv`（37,484 行×16 列全 `PENDING`，`S-%06d` 稳定 ID 按卷序→章序→节序→文件名升序，一经分配永不复用）、`target-catalog.md`（4,303 行与 `targets.tsv` 逐项相等）、`review/packs/<旧卷>.tsv` 24 卷工作包、`mapping.duckdb` 只读派生器。

**Why this priority**: 台账是 Task 5 判定的数据底盘；`landing05` 长线探针依赖它切换为逐状态计数。

**Independent Test**: 行数==37,484、列数==16、状态守恒（各状态和==37,484）；catalog 三元组 75/523/3,705 与 `targets.tsv` 逐项相等；生成器二跑 diff==0；`_longline_status.py --check` 18 条线仍一致且 `landing05` 进度串变为逐状态计数。

**Acceptance Scenarios**:

1. **Given** `inventory.tsv`（37,486 件），**When** 生成 `mapping.tsv`，**Then** 数据行==37,484（根级 2 个非子节不入）、16 列齐、全部 `PENDING`、SHA 分组重复组为 0（干执行预期）或每组恰 1 代表件余者 `DUPLICATE`。
2. **Given** `mapping.tsv`（20.9 MB，超 5 MB 门槛），**When** 入库提交，**Then** 提交说明带 `APPROVED-BIGFILE:`，且采用里程碑提交制（本批一次＋每卷收口各一次），不逐子批提交。
3. **Given** mapping 落盘，**When** 跑 `_longline_status.py --check`，**Then** `landing05` 探针自动由“0/37,484 未生成”切为逐状态计数且 18 线一致 PASS。

### User Story 3 - 每条旧子节有可信落点（Task 5 主代理三判复核）(Priority: P1)

**主代理**（本会话执行者，无子代理）对 37,484 条旧子节逐条判定落点：**同一子批做三趟串行独立判定（A／B／C）**，三趟输入包只读且相同（源文＋完整 3,705 节目录）、输出分文件密封（`映射/review/judgments/<子批>-{A,B,C}.tsv`）、三趟分别采用**差异化判定策略**（A＝题面语义优先／B＝内容主题词优先／C＝结构与编号线索优先，见 `contracts/three-pass-review.md`）；三趟齐后由合并器汇总：全同→`CONFIRMED`（review_a/b/c 全填），任一不同→`DISPUTED` 入 `disputes.tsv`；无法归入→`UNMAPPED`（须理由，禁硬塞）；目标节裁撤→`TARGET_LOST`；拆并→`REMAP` 登记后继 ID。六波推进（W1 旧卷 01–04 约 5,334 条优先；05 卷 9,454 拆 10 子批；09 卷拆 5；20 卷拆 6；余按卷）。

**Why this priority**: 这是全战役长尾主体与质量核心；三判一致性是 CONFIRMED 的唯一门。

**Independent Test**: 任一时刻 `PENDING + CONFIRMED + UNMAPPED + DISPUTED + DUPLICATE + DISCARDED + TARGET_LOST + REMAP == 37,484`；任一 `CONFIRMED` 行三路记录非空且三 `target_id` 全同；任一 `DISPUTED` 行在 `disputes.tsv` 有对应行。

**Acceptance Scenarios**:

1. **Given** 一个子批（≤1,000 条）的只读输入包，**When** 主代理先后做 A／B／C 三趟判定，**Then** 每趟只读输入包与该趟既有密封件、不读他趟输出；三份输出文件逐条含 `source_id`／`target_id`／理由／策略标记。
2. **Given** 三趟输出齐，**When** 合并器汇总，**Then** 三同→`CONFIRMED`；不同→`DISPUTED`（disputes.tsv 记三趟分歧详情）；子批行数守恒、checkpoint 落 `script/_landing_production_20261023/checkpoints/t5-<卷>-<子批>.json`、打印状态分布与分歧率。
3. **Given** 先导子批（W1 首两子批约 300–500 条）合并完毕，**When** 读其分歧率，**Then** 得到**真实分歧率实测值**；若 >50% 停批发起复盘修订判定指引，不得带病续波。
4. **Given** 任一条被拟判 `CONFIRMED`，**When** 校验其目标节，**Then** 目标节题面与源文主题有交集（禁硬塞判据）；`UNMAPPED` 行逐条有理由。

### User Story 4 - 复核与签收闭环（质量保障）(Priority: P1)

高风险任务的复核轮次与签收：每卷收口 1 轮独立复核（覆盖该卷全部 `CONFIRMED`／`DISPUTED`）＋全批 1 轮全量复核（状态守恒与跨卷一致性）＋整改后复验 1 轮，合计 ≥3 轮；任一轮 FAIL 即停批整改、整改后重跑该轮。**单代理语境的作者不复核自己**转译为：判定轮与复核轮须时间分离且轮次显式记录（不同会话或同会话声明冷却的独立轮），复核采用与三趟判定策略均不同的第四视角（抽样回放＋守恒断言＋禁硬塞抽查）。**收口签收由 ykla 本人，不得代签**。

**Why this priority**: L7 硬要求；无签收不得收口（`工程实践规则.md` §0.3）。

**Independent Test**: `01-项目管理/02-工程决策与技术债/任务复核台账.md` 有 ≥3 轮记录，每轮含轮次号／覆盖面／结论／复核视角；收口行有 ykla 签收标记；`任务审计台账.md` 回填收口证据。

**Acceptance Scenarios**:

1. **Given** 某卷全部子批合并完毕，**When** 卷级复核轮执行，**Then** 复核轮不复用判定轮的判定脚本现场（重算而非引用），输出逐项 PASS/FAIL 并写台账。
2. **Given** 任一复核轮 FAIL，**When** 处置，**Then** 停批整改→重跑该轮→FAIL 项清零，不得以“下一轮覆盖”代替。
3. **Given** 三轮齐且全 PASS，**When** 收口，**Then** ykla 签收行存在（缺签收不得收口），changelog 与 `.trae` spec 勾选面同批同步。

### User Story 5 - 全程可断点可审计（工程底盘）(Priority: P2)

每批可断点续跑（checkpoint 记批次号／source_id 区间／状态分布／输入哈希）、生成器幂等（二跑零增量）、门禁全绿（收口五命令＋常备四件）、L0–L5 按写入面完整循环、里程碑提交与长线刷新。

**Why this priority**: 37,484 条长尾跨多会话，断点与幂等是续航前提；审计链是工程实践规则的强制面。

**Independent Test**: 任一生成器二跑 diff==0；任一批收口五命令输出全 PASS；`audit_task_lifecycle.py` L1–L12 无本批新增 FAIL；每次里程碑提交后 `_longline_status.py --check` 18 线一致。

**Acceptance Scenarios**:

1. **Given** 任一子批中断，**When** 从 checkpoint 续跑，**Then** 已处理区间不重判（已 `CONFIRMED` 行不变）。
2. **Given** 有写入面的批（2.1b／B5／每子批回写），**When** 按 L0–L5 循环执行，**Then** L3 逐条回读留证、L4 二跑零增量、L5 坏件注入可见。
3. **Given** 全部批次收口，**When** 跑常备四件＋收口五命令，**Then** 全绿；`landing05` 进度串显示终态分布（PENDING=0）。

## Requirements

### Functional Requirements

| ID | 需求 | 优先级 | 验收（二值） | 追溯 |
| -- | ---- | ---- | ---- | ---- |
| FR-001 | 2.1b 机械改名＋2.4a 台账：六类清零、SHA 相等、台账含补录行 | P0 | `title-standardization.tsv` 行数与计数精确相等；复扫六类==0 | US1；.trae 2.1b/2.4a |
| FR-002 | 2.1c 只出表：21,031 条建议全覆盖、执行改名数==0 | P0 | `title-review.tsv` 行数==21,031；git 无语义改名 | US1；.trae 2.1c |
| FR-003 | 2.1d 复测四类路径问题全入台账或为零 | P0 | `path-overlong.tsv` 与复扫输出一致 | US1；.trae 2.1d |
| FR-004 | 2.1a 派生件再生→门禁 PASS→冻结声明 | P1 | 两门禁 PASS 输出＋README 冻结段存在 | US1；.trae 2.1a |
| FR-005 | mapping.tsv 精确生成（37,484×16、S-ID 稳定、SHA 分组） | P0 | 行数/列数/守恒三断言 | US2；.trae 4.1 |
| FR-006 | catalog 与 packs：4,303 逐项相等、24 卷工作包 | P0 | 三元组断言＋packs 文件数==24 | US2；.trae 4.3 |
| FR-007 | mapping.duckdb 只读派生器（或 staging 方案） | P1 | 派生统计与 TSV 直数一致 | US2；.trae 4.4–4.6 |
| FR-008 | 主代理三判：三趟串行、输入密封、策略差异化、输出分文件 | P0 | 三文件齐且互无交叉引用；每条含策略标记 | US3；contracts |
| FR-009 | 合并判定：三同 CONFIRMED／分歧 DISPUTED／守恒断言／checkpoint | P0 | 状态守恒==37,484；checkpoint 可续跑 | US3；.trae 5.7 |
| FR-010 | 先导子批实测分歧率并设停盘阈（>50%） | P0 | 实测值落台账；超阈停盘记录在案 | US3 |
| FR-011 | 禁硬塞与 UNMAPPED 理由 | P0 | CONFIRMED 行主题交集抽查 0 违例 | US3 |
| FR-012 | 复核 ≥3 轮＋ykla 签收＋台账双登记 | P0 | 复核台账与审计台账行存在且含签收 | US4；L7 |
| FR-013 | 幂等与断点：生成器二跑零增量、续跑不重判 | P0 | 二跑 diff==0；续跑后 CONFIRMED 不变 | US5；NFR-T4/T5 |
| FR-014 | 门禁与长线：每批收口五命令＋常备四件＋landing05 探针一致 | P0 | 门禁输出全 PASS；18 线一致 | US5 |
| FR-015 | 里程碑提交制＋`APPROVED-BIGFILE:` | P1 | 提交清单与标记可查 | US2/US5 |

### Non-Functional Requirements

| ID | 需求 | 判定 |
| -- | ---- | ---- |
| NFR-001 | **零子代理**：全程不调用 Agent 工具派发子代理（ykla 2026-10-24 令） | 会话记录与批次日志无子代理派发 |
| NFR-002 | 写入边界：只落 `映射/`／`script/`／台账文书路径 | 每批 `git status --porcelain` 面合规 |
| NFR-003 | 内容保真：旧树只读（除 2.1b 已批准机械改名）；不改内容字节 | 改名件 SHA 前后相等 |
| NFR-004 | 幂等：一切生成器与合并器二跑零增量 | 二跑 diff==0 |
| NFR-005 | 可审计：每批证据可定位（文件路径＋行数＋哈希＋命令输出） | 审计台账行完整 |
| NFR-006 | L0–L5 完整循环按写入面适用（任务书 §七 表） | 循环记录在批日志 |

## Success Criteria

1. Task 2 全子项勾选、旧树文件名面合规可迁移（六类==0）。
2. `mapping.tsv` 就绪且 `landing05` 探针切为逐状态计数、18 线一致。
3. `PENDING==0` 且八状态守恒==37,484；`CONFIRMED` 三路记录俱全；`DISPUTED` 全数挂账。
4. 真实分歧率实测值落台账；先导子批结论（续跑/停盘）有据。
5. 复核 ≥3 轮＋ykla 签收行存在；审计双台账回填。
6. 全程零子代理；全部门禁绿；里程碑提交齐且大文件带放行标记。

## Key Entities

`mapping.tsv`（16 列）、`title-standardization.tsv`（6 列）、`title-review.tsv`、`path-overlong.tsv`、`target-catalog.md`、`review/packs/*.tsv`、`review/judgments/*-{A,B,C}.tsv`、`disputes.tsv`、`checkpoints/*.json`、`mapping.duckdb`（派生）。字段与状态机见 `data-model.md`。

## Assumptions

- 干执行数字复用为工作基线并以 2026-10-24 完整链路干执行实测修订（见 `dryrun-20261024.md`）：反引号 6,291（6,118 纯剥离＋173 模板名→H1 名）；2.4a 补录 **168 行**；mapping 20.9 MB；卷切分 26–9,454；**S-ID 规范序＝relpath 数值感知自然序、一经分配冻结**；先导分歧率基线 58.3%（12 件小样本）。
- 主代理串行三判的**方法学限制**如实披露：非盲独立（同一模型记忆连续），以策略差异化＋输出密封＋合并器硬判据缓解；该限制记入 `research.md`，不得宣称等同三独立评审员。
- 本 feature 不施工 Task 6+（挂账冻结／引擎／迁移），另批另 feature。
