---
spec_id: M
title: 工具链与数据库标准化（总 spec）
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 一、意图确证（档 A 六字段）
version: 1.0.1
status: closed
goals: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
owner: ykla
created: 2026-11-27
updated: 2026-11-28
binding_id: TB-20261127-M
---

# Feature Specification: 工具链与数据库标准化

**Feature**: `specs/006-toolchain-db-standardization/`
**Created**: 2026-11-27
**Status**: Draft（G0 规划件；执行批未开工）
**Input**: ykla 2026-11-27 十二项目标（逐字见任务书 §1.1）

## 0. 意图确证（摘要）

- **用户原话**：见任务书 §1.1（逐字）。
- **目标**：建立任务书与多件套 spec；执行期完成标准调研、数据库与工具链归一化、Rust 逐个评估、公理化、数据质量评估、结构建议、软件工程理论复核、全局工具表、缓存清理机制、OCR／音频工具链，并给出不计成本且符合学术规范的最佳建议。
- **非目标**：不写正文、不写库、不改工具、不删缓存、不改结构、不设自动化；`specs/` 已获准入库，`.trae/specs/` 仍为工作区。
- **验收判据**：任务书 A-01—A-09；总 spec SC-01—SC-08；各子 spec checklist。
- **手段自由度**：Tavily／官方来源、只读勘察、工作区写 spec；禁止写库、删除、改规则、改门禁。
- **未知**：见任务书 §1.6 U-01—U-10。

## 1. 用户场景与测试（User Scenarios & Testing）

### US1 — 标准基线可引用（Priority: P0）

作为后续所有工作的前置，接手人需要一份**分级、现行、可定位**的标准清单：每条有标准号、版本、状态、适用条款、对本项目的约束、例外与冲突处置，并能回答“为什么引它”。

**Why this priority**：标准不清，则数据质量、工具契约、Rust 选型、公理化都失去外部锚点。

**Independent Test**：任取 10 条标准，复核者按 URL 与条款号可在官方页定位；四问抽取可复述；版本冲突表能解释 GB 与 ISO 的滞后关系。

**Acceptance Scenarios**：

1. **Given** 一条标准，**When** 复核者按清单 URL 打开官方页，**Then** 标准号、版本、状态与清单一致。
2. **Given** 一条“现行”标准，**When** 查其替代关系，**Then** 清单注明是否被代替、是否有修订计划。
3. **Given** 一条与项目规则冲突的标准，**When** 查冲突表，**Then** 有位阶处置与登记结论。

### US2 — 数据可归一、质量可度量（Priority: P0）

作为数据维护者，需要知道每个库的 schema、键、函数依赖、空值、重复、孤儿、时间戳与 provenance 覆盖，得到可比较的质量记分卡与改进建议。

**Why this priority**：数据库是项目的主要内容载体；不可归一、不可度量，则一切分析不可复现。

**Independent Test**：任取一个正式库，按记分卡复算 5 个指标，结果与报告一致；任取一条问题，能定位到表、列、行数与证据。

**Acceptance Scenarios**：

1. **Given** 一个正式库，**When** 跑只读剖析，**Then** 输出行数、列数、空值率、键重复、孤儿、时间范围。
2. **Given** 一个质量问题，**When** 查问题清单，**Then** 有严重级别、影响面、建议动作与证据路径。
3. **Given** 一个归一化建议，**When** 查迁移方案，**Then** 有 dry-run、行数对账与回退步骤。

### US3 — 工具可发现、可替换、可并发（Priority: P0）

作为维护者，需要一张全局工具表与统一 CLI 契约：知道每个工具的作用、创建／修改时间、生命周期、是否入库、被哪条规则引用；知道哪些工具可并行、如何加锁、如何检查点。

**Why this priority**：121 个脚本、多代实现、硬编码路径与无统一入口，是重复劳动与事故的主要来源。

**Independent Test**：任取 10 个稳定工具，工具表字段完整、路径存在、`--help` 可跑；任取一个并发批，锁与检查点行为符合规范。

**Acceptance Scenarios**：

1. **Given** 一个工具，**When** 查工具表，**Then** 有 created_at、last_modified、purpose、lifecycle、tracked、rule_references。
2. **Given** 一个 `stable` 工具，**When** 跑 `--selftest`，**Then** 退出码 0 且有判据输出。
3. **Given** 两个写同一库的批，**When** 同时启动，**Then** 只有一个获得锁，另一个安全退出。

### US4 — Rust 化有判据、语言有标准（Priority: P1）

作为技术负责人，需要逐个工具的 Rust 改写评估矩阵与语言标准，避免“为改写而改写”，并保证改写可回退。

**Why this priority**：Rust 能带来性能与并发收益，但生态、维护、分发成本高；无判据即风险。

**Independent Test**：任取一个候选工具，评估矩阵有实测数据、结论有理由、回退方案可执行；语言标准覆盖 Python／Rust／JS／SQL／Shell。

**Acceptance Scenarios**：

1. **Given** 一个候选工具，**When** 查矩阵，**Then** 有 CPU／I/O、生态、并发、维护、分发、回退六类评分。
2. **Given** 一个“建议改写”结论，**When** 查生产改写方案，**Then** 有影子运行、灰度与逐字节比对。
3. **Given** 一个 Rust crate，**When** 查工程基线，**Then** 有 edition、MSRV、clippy、deny、audit、unsafe 政策。

### US5 — 公理化可检查、边界诚实（Priority: P1）

作为研究者，需要一套形式系统描述工具、库、标准、规则、spec 之间的实体与不变量，并证明相对一致、充分、完备；同时明确不可证事项。

**Why this priority**：目标 4 要求“公理化体系建立，证明，一致性，充分性，完备性”；没有形式定义与机器检查，就只是口号。

**Independent Test**：Alloy／TLC 模型可复跑；覆盖矩阵 100%；每个定理有证明或反例；限制文件列明不可证事项。

**Acceptance Scenarios**：

1. **Given** 公理集，**When** 跑 Alloy，**Then** 无矛盾模型或有反例解释。
2. **Given** 目标集，**When** 查覆盖矩阵，**Then** 每个目标至少一个 spec。
3. **Given** 一个“完备”主张，**When** 查限制文件，**Then** 明确“相对于声明范围”。

### US6 — 结构与清理有方案、不擅动（Priority: P2）

作为项目所有者，需要项目结构建议、缓存与垃圾识别机制、OCR／音频工具链任务书，但所有改动须经批准、可回退、不干扰在途工作。

**Why this priority**：结构与清理是高风险动作；先方案后施工，避免不可逆损失。

**Independent Test**：结构方案列明约束、选项、成本、风险、回退；缓存机制能扫描并分类；OCR／音频模板可被实际批次引用。

**Acceptance Scenarios**：

1. **Given** 一个结构建议，**When** 查约束表，**Then** 不新增根目录、不动 `05-卷册大纲/`。
2. **Given** 一个缓存候选，**When** 跑扫描，**Then** 有分类、体积、可再生产性、引用检查与建议动作。
3. **Given** 一个 OCR 批次，**When** 套模板，**Then** 有质量门、检查点、绑定与回退。

### Edge Cases

- **标准换版**：执行期发现新版发布，旧引用须改；已完成的 spec 须走变更流程。
- **数据库锁**：剖析时遇到写锁，须退避或复制后剖析，不得强杀。
- **specs 并发覆盖**：`specs/` 已入库，但并发会话仍可能覆盖未提交改动；以 Git diff＋BINDING 清单双查。
- **Rust 工具链不可用**：目标机无 cargo／MSRV 不符；评估可继续，生产改写须挂起。
- **OCR 多语言**：中英混排、古籍字形、扫描质量差；质量门须分级，不得一刀切。
- **音频版权**：转写产物与原文的许可；须按考据规则登记。

## 2. 需求（Requirements）

### 2.1 功能需求（总级）

- **FR-M-001**：任务书与 12 份子 spec MUST 双向可定位；每份 spec 的 frontmatter MUST 含 `task_book`、`task_book_anchor`、`spec_id`、`goals`、`version`、`status`。
- **FR-M-002**：`BINDING.tsv` MUST 记录每份 spec 三件套的 sha256、版本、状态与目标；任务书 MUST 内嵌摘要与 manifest 哈希。
- **FR-M-003**：目标 1—12 MUST 全部被至少一份 spec 覆盖；无孤儿 spec。
- **FR-M-004**：S01 MUST 产出一份分级标准清单，每条含标准号、版本、状态、适用条款、约束、例外、冲突、官方 URL、检索日期。
- **FR-M-005**：S02 MUST 产出全库 schema 清单、数据字典、函数依赖与规范化判定、迁移与回退方案。
- **FR-M-006**：S03 MUST 产出工具链 CLI 契约、并发模型、锁协议、检查点与基准方案。
- **FR-M-007**：S04 MUST 产出逐工具 Rust 评估矩阵、语言标准草案、Rust 工程基线与生产改写／回退方案。
- **FR-M-008**：S05 MUST 产出形式系统（排序、公理、定义、定理、证明）与机器检查模型，并明确相对一致／充分／完备的范围。
- **FR-M-009**：S06 MUST 产出 15 维数据质量记分卡、全库剖析、问题清单与不计成本的改进建议。
- **FR-M-010**：S07 MUST 产出项目结构评估、方案对比、迁移与回退、决策点；评估可立即执行，但不得直接改结构。
- **FR-M-011**：S08 MUST 产出软件工程理论对照、缺口登记（TG）、ADR 建议；不得直接改 `13-软件工程/` 正文。
- **FR-M-012**：S09 MUST 产出全局工具表 schema、生成器、校验器与生命周期规则；表为派生视图。
- **FR-M-013**：S10 MUST 产出组合式最佳建议、路线图、决策记录与学术规范声明。
- **FR-M-014**：S11 MUST 产出缓存与垃圾分类、判据、TTL、清单模板、隔离与复扫机制；不得在本批删除。
- **FR-M-015**：S12 MUST 产出 OCR／音频统一流水线、任务书模板、质量指标与绑定。
- **FR-M-016**：所有 spec MUST 含意图确证摘要、范围内／外、验收场景、FR、NFR、交付物、风险、追溯。
- **FR-M-017**：所有标准引用 MUST 可定位到官方来源；无法核实者 MUST 标 `[待核验]`，不得冒充已核。
- **FR-M-018**：所有数据库评估 MUST 只读；写操作设计与执行分离；写批 MUST 走 guard＋waterlock。
- **FR-M-019**：所有工具改动 MUST 有回退；Rust 生产改写 MUST 影子运行、灰度并逐字节／逐记录比对。
- **FR-M-020**：所有清理 MUST 有清单、sha256、隔离与复扫；不得 `rm -rf`、不得通配删除、不得删保护清单。

### 2.2 非功能需求（总级）

- **NFR-M-001 可复现**：关键数字与结论可由第二人按路径复算；脚本、输入、版本、命令可追溯。
- **NFR-M-002 可审计**：每份产物有作者、时间、版本、证据路径；变更走 changelog。
- **NFR-M-003 性能**：全库剖析与工具基准在可接受时间内完成；超时须分片，不得静默截断。
- **NFR-M-004 安全**：凭据不入库、不打印；外部依赖登记许可；SBOM 可生成。
- **NFR-M-005 可维护**：工具单一入口、路径派生、配置显式；禁止硬编码盘符。
- **NFR-M-006 学术规范**：引用可定位、限制与反例如实披露、不采纳强制标记 AI 生成内容的规范、无臆造。
- **NFR-M-007 兼容**：不破坏现有规则、门禁、数据库路径与在途批次；结构改动须回退方案。
- **NFR-M-008 并发安全**：单写多读、锁超时、幂等、背压、检查点。

## 3. 关键实体（Key Entities）

| 实体 | 关键属性 | 关系 |
| ---- | -------- | ---- |
| TaskBook | task_id、path、version、status | 1—N Spec |
| Spec | spec_id、goal_ids、version、status、sha256 | N—1 TaskBook；1—N FR |
| FR | fr_id、text、acceptance、priority | N—1 Spec |
| Tool | tool_id、path、language、lifecycle、tracked、created_at、last_modified | N—N Rule；N—N Gate |
| Database | db_name、path、schema_version、built_at、quality_score | 1—N Table |
| Dataset | dataset_id、source、provenance、license | N—1 Database |
| Standard | std_id、number、edition、status、url、retrieved_at | N—N FR／Tool／Database |
| QualityMetric | metric_id、dimension、formula、threshold、evidence | N—1 Database |
| Binding | binding_id、spec_id、sha256、task_book_anchor | 1—1 Spec |
| CacheCandidate | path、category、size、mtime、regenerable、action | — |

## 4. 成功判据（Success Criteria）

- **SC-01**：目标 1—12 覆盖率 100%，无孤儿 spec。
- **SC-02**：每份 spec 至少 5 条可测 FR、3 条验收场景、5 条 checklist。
- **SC-03**：标准清单每条有官方 URL＋检索日期；`[一手已核]` 比例 ≥80%，其余有复核路径。
- **SC-04**：正式库质量记分卡覆盖率 100%；关键指标可由第二脚本复算，差异 0。
- **SC-05**：稳定工具在全局工具表中覆盖率 100%；`tracked` 与 `git ls-files` 一致率 100%。
- **SC-06**：Rust 候选工具评估覆盖率 100%；每个“建议改写”有基准与回退；生产改写有影子、灰度与观测指标。
- **SC-07**：公理化覆盖矩阵 100%；Alloy／TLC 可复跑；限制文件列明不可证事项。
- **SC-08**：缓存扫描覆盖全部类别；保护清单零越界；清理方案不含未授权删除。

## 5. 假设与依赖（Assumptions）

- 项目继续以 DuckDB 2.0.0 为工作副本，SQLite 归档不回迁。
- Python 3.15 为当前解释器基线；Rust 生产改写已获 ykla 2026-11-27 批准，每批仍走任务审计准入。
- `05-卷册大纲/` 的 Task 8.2／8.3 在途工作优先；S07 评估可立即，结构施工冻结到其收口。
- `specs/` 已按 2026-11-27 ykla 令入库跟踪；`.trae/specs/` 仍为工作区。
- 子代理并发上限按 2026-11-27 实测 ≤4；失败即停，主会话兜底。

## 6. 范围外（Out of Scope）

- 正文写作、大纲改号、目录页装配。
- 数据库 DDL／DML、迁移执行、备份删除。
- 工具删除、移动；无基准的 Rust 重写。
- 规则与门禁修改；ADR 正式采纳。
- 缓存实际删除；全仓清理。
- 自动化任务与定时调度。

## 7. 追溯（Traceability）

| 目标 | 子 spec | 总 FR | 验收 |
| ---- | ------- | ----- | ---- |
| G1 | S01 | FR-M-004、FR-M-017 | SC-03 |
| G2 | S02、S03 | FR-M-005、FR-M-006、FR-M-018 | SC-04、SC-05 |
| G3 | S04 | FR-M-007、FR-M-019 | SC-06 |
| G4 | S05 | FR-M-008 | SC-07 |
| G5 | S06 | FR-M-009、FR-M-018 | SC-04 |
| G6 | S07 | FR-M-010 | SC-08 |
| G7 | S08 | FR-M-011 | SC-02 |
| G8 | S09 | FR-M-012 | SC-05 |
| G9 | S10 | FR-M-013 | SC-02 |
| G10 | S11 | FR-M-014、FR-M-020 | SC-08 |
| G11 | S12 | FR-M-015 | SC-02 |
| G12 | 任务书 §16＋binding.md | FR-M-001—003 | SC-01 |
