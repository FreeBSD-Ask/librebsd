# Tasks: OAA F1–F4 四组交接书与下一批任务书

**Input**: Design documents from `/specs/001-oaa-f1f4-next-batch/`

**Prerequisites**: plan.md（必需）、spec.md（必需）

**Tests**: 本特性不产生测试任务（纯文档产出）；以“复算一致性”检查点代替（见 checklist.md）。

**Organization**: 任务按用户故事分组，每个故事可独立完成与独立验收。

## Format: `[ID] [P?] [Story] Description`

- **[P]**: 可并行（不同文件，无依赖）
- **[Story]**: 所属用户故事（US1/US2/US3/US4）
- 描述含确切文件路径

## Path Conventions

- 勘测脚本：`script/_db_row_mining/audit_outline/work/`
- 交接书：`script/_db_row_mining/audit_outline/`
- 任务书：`01-项目管理/01-编纂规划与报告归档/`
- 规格件：`specs/001-oaa-f1f4-next-batch/`

---

## Phase 1: Setup (共享前置)

**Purpose**: 建立只读勘测能力，取得“合并台账 / 认领清单 / 分片判读盘面”三源的统一读入口

- [ ] T001 在 `script/_db_row_mining/audit_outline/work/_fclaims_scan.py` 建按认领清单逐宿主核 pending 的只读脚本（输入 `beacon/claims_FN.txt`，对每宿主做 ROW_MINE 差集，输出逐宿主块数）
- [ ] T002 [P] 在 `script/_db_row_mining/audit_outline/work/_fnext_scan.py` 建按卷 glob 的 pending 扫描脚本（辅助口径，用于交叉验证 T001）
- [ ] T003 冻结口径：以 `processed.jsonl` ∪ `processed_f1..f4.jsonl` 为合并台账唯一键集（实测 59,563 条），写进两脚本常量与注释

---

## Phase 2: Foundational (阻塞前置)

**Purpose**: 取得四组进度基线；此阶段完成前不得动笔写任何交接书/任务书

**⚠️ CRITICAL**: 本阶段数字是全部后续产出的唯一真值来源

- [ ] T004 运行 `python 00-编纂规则与格式规范/01-规则/脚本与命令/oaa_beacon.py --refresh`，记录刷新时点（2026-10-01T02:22:46）与四组 `done/pend`
- [ ] T005 用 T001 脚本实算四组待审块，与浮标逐组对账（要求 0 差）：F1 72,791／F2 88,722／F3 57,969／F4 71,545
- [ ] T006 [P] 聚合 `shards/` 与 `judgements/` 前缀计数，产出在途批清单：`f1_b03` 120/459 片、`f2_b01` 653/815 片、`f3_05` 8/255 片、`f4b04` 71/93 片
- [ ] T007 [P] 按卷汇总四组 pending 分布（写入交接书 §二 的输入），并核对卷目录名与磁盘一致（第12/17/18/20 卷为 `macos的bsd遗产`/`政治制度与社区治理`/`全球社区地区bsd史`/`linux社区史与比较研究`）
- [ ] T008 [P] 盘点四组挂账清单文件与条数：F1 `work/_f1_b01_guazhang.json`；F2 `beacon/_X1_ledger_f2.jsonl`；F3 `work/_f3_0{1,2,3,4}_x1_level.json`＋`_x2_remap.json`＋`_f3_04_x3_doubt.json`；F4 `work/_f4_fixdb_triage.json` 等
- [ ] T009 确认在途批宿主集，作为下一批任务书的**排除集**：F1 排除 `88.5`；F2 排除 `173.1`；F3 排除 `122.9`/`131.5`/`121.3`＋避让 `112.10`/`121.1`/`121.4`/`122.10`；F4 排除 `f4b04` 的 16 宿主

**Checkpoint**: 四组数字全部可复算、在途批宿主集已冻结 —— 可开始写交接书

---

## Phase 3: User Story 1 - 读盘取得 F1–F4 真实进度 (Priority: P1) 🎯 MVP

**Goal**: 产出可直接引用的“四组进度总表”，落盘到 `_HANDOFF_OAA.md` §七 数字快照与四份交接书 §二

**Independent Test**: 把总表四组待审块数与 `_BEACON.md` 比对，误差 ≤1%；在途批的“片数×片块数 vs 已判块数”与 `judgements/` 行数实测一致

- [ ] T010 [US1] 生成进度总表 `script/_db_row_mining/audit_outline/_PROGRESS_SNAPSHOT_20261001.md`（含四组：认领宿主/已审/待审/在途批/进度/取量时点/口径说明）
- [ ] T011 [US1] 在总表中固化本特性的三条口径红线：①进度只认磁盘 ②在途批零触碰 ③避让清单不审不登记
- [ ] T012 [P] [US1] 复算 F2 台账口径差：`processed_f2.jsonl` 56 条 vs 浮标 done 56（b00 试点），确认 b01 的 15,013 块**未**入账
- [ ] T013 [P] [US1] 复算 F3 台账口径差：`processed_f3.jsonl` 22,581 条 vs 浮标 done 22,532（差 49 条为 remap-removed 后锚点已不存在者），在总表加脚注

**Checkpoint**: 进度总表落盘且可复算 —— MVP 达成

---

## Phase 4: User Story 2 - 每组一份组级交接书 (Priority: P2)

**Goal**: 四份 `_HANDOFF_F{1..4}.md`，固定五节（批次表／在途现场／挂账清单／坑／下一手）

**Independent Test**: 任取一份，其在途批三项数字（片数/块数/进度）与磁盘实测完全相等；挂账条目数与其 JSON 文件可复现

- [ ] T014 [P] [US2] 写 `script/_db_row_mining/audit_outline/_HANDOFF_F1.md`（已闭环 F1-01 4,640＋F1-02 11,247；在途 `f1_b03` 88.5 10,543 块 26.2%；挂账 X1 532／X2 80／X3 17；坑：重复日期前缀族幂等假跳、H2 键 1,150 排除）
- [ ] T015 [P] [US2] 写 `script/_db_row_mining/audit_outline/_HANDOFF_F2.md`（已闭环 `f2_b00` 试点 56＋工具链修复 `dc3557d85`；在途 `f2_b01` 173.1 18,725 块 80.2%；挂账 X1 3＋b01 203 待分流；坑：账户并发冻结三级降档、8 类判读件 JSON 污染、主代理可补判单块）
- [ ] T016 [P] [US2] 写 `script/_db_row_mining/audit_outline/_HANDOFF_F3.md`（已闭环 F3-01..04；在途 `f3_05` 5,858 块 3.1%；🔴**fix-db 54 条待 apply**（主库 PID 4 锁）＋X1 538／X2 191／X3 2；坑：避让清单已增至 9,110 块、垃圾邮件系统性混入、claim_text 截断族 780 条已修）
- [ ] T017 [P] [US2] 写 `script/_db_row_mining/audit_outline/_HANDOFF_F4.md`（已闭环 B5/B6/批次一/二/三；在途 `f4b04` 第34/35章 4,649 块 76.4%；挂账 X1 357／X2 353／X3 15；坑：36.4 现代帖跨时代错挂 103、deepseek 战线宿主须过滤、字数下限系统性宽松）
- [ ] T018 [US2] 四份交接书交叉核对：在途批宿主集互斥、挂账清单路径全部存在、每组“下一手”指向本次产出的对应任务书

**Checkpoint**: 四份交接书落盘且互不矛盾 —— US2 达成

---

## Phase 5: User Story 3 - 每组一份下一批任务书 (Priority: P3)

**Goal**: F1-04／F2-b02／F3-06／F4-b05 四份派发书

**Independent Test**: 按任务书的宿主清单跑一次差集，块数与标注一致（±5%）；清单与在途批宿主集交集为空

- [ ] T019 [US3] 写 `01-项目管理/01-编纂规划与报告归档/大纲邮件审计_F1-04-任务书-20261001.md`（范围：第05卷 `92.1-2000-2003-年-4-0-Jails.md` 9,509 块／414 片；排除在途 `88.5`）
- [ ] T20 [US3] 写 `01-项目管理/01-编纂规划与报告归档/大纲邮件审计_F2-b02-任务书-20261001.md`（范围：`184.1-netbsd2130多平台扩展与稳定化20052007.md` 12,919 块／562 片；与 `work/_f2_batchplan.json` 的 `f2_b02` 一致）
- [ ] T21 [US3] 写 `01-项目管理/01-编纂规划与报告归档/大纲邮件审计_F3-06-任务书-20261001.md`（范围：第06卷余下 26 宿主 4,249 块／≈185 片，清单落盘 `work/hosts_f3_06.txt`；含避让过滤与在途排除）
- [ ] T22 [US3] 写 `01-项目管理/01-编纂规划与报告归档/大纲邮件审计_F4-b05-任务书-20261001.md`（范围：第02卷余下 63 宿主 4,460 块／≈90 片，清单落盘 `work/hosts_f4_b05.txt`；含 36.4 并行新增 1,650）
- [ ] T23 [US3] 四份任务书统一小节：〇现场／一本批范围／二执行前置／三执行八步／四特有风险／五挂账口径／六验收／七收口序列；每份写明“取量时点 2026-10-01 02:22，开工以 `oaa_beacon.py --status` 实测为准”
- [ ] T24 [US3] 四份任务书均写入“不得触碰在途批的 shards/judgements/台账/大纲宿主”的排除声明（FR-004）

**Checkpoint**: 四份任务书落盘、清单与在途批零交集 —— US3 达成

---

## Phase 6: User Story 4 - 主交接书回指 (Priority: P4)

**Goal**: `_HANDOFF_OAA.md` 登记四份交接书与四份任务书，刷新现场

**Independent Test**: 从 `_HANDOFF_OAA.md` 出发四份交接书均 1 跳可达

- [ ] T025 [US4] 在 `script/_db_row_mining/audit_outline/_HANDOFF_OAA.md` §九 增补“9.6 组级交接书索引（2026-10-01）”节，列出四份 `_HANDOFF_F*.md` 与四份任务书路径
- [ ] T026 [US4] 更新 `_HANDOFF_OAA.md` §九 的四组进度表（认领/块数/已审/在途），与 `_BEACON.md` 02:22 快照一致

---

## Phase 7: Polish & 交叉核验

- [ ] T027 [P] 运行 `checklist.md` 全部检查点并记录判定结果（不得由生产者自勾）
- [ ] T028 [P] 复核“零写盘”红线：确认本特性未新增/覆盖 `05-卷册大纲/**`、`shards/**`、`judgements/**`、`processed_fN.jsonl` 任一文件
- [ ] T029 提交：`git add` 仅限本次产出路径 ＋ `git add -f` 补 `script/` 下被 ignore 的交接书/脚本；`git commit --gpg-sign -F <msgfile>`；`git log -1 --format=%G?` 须为 `G`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**：无依赖，可立即开始
- **Foundational (Phase 2)**：依赖 Phase 1 的脚本；**阻塞全部用户故事**
- **User Stories (Phase 3–6)**：均依赖 Phase 2
- **Polish (Phase 7)**：依赖全部用户故事完成

### User Story Dependencies

- **US1 (P1)**：Phase 2 后即可开始，不依赖其他故事 —— **MVP**
- **US2 (P2)**：依赖 US1 的数字（T010 总表）
- **US3 (P3)**：依赖 US1 与 Phase 2 的 T009 排除集
- **US4 (P4)**：依赖 US2、US3 的文件路径

### Within Each User Story

- 先落盘正文，再做交叉核对（T018／T023／T024）
- 交接书与任务书之间的在途批宿主集必须**互斥且穷尽**（并集＝该组全部待审宿主）

### Parallel Opportunities

- T002／T007／T008 可并行（互不依赖）
- T014–T017 四份交接书可全并行（不同文件）
- T019–T022 四份任务书可全并行（不同文件）

---

## Parallel Example: Phase 4（四份交接书）

```text
Task: "写 script/_db_row_mining/audit_outline/_HANDOFF_F1.md"
Task: "写 script/_db_row_mining/audit_outline/_HANDOFF_F2.md"
Task: "写 script/_db_row_mining/audit_outline/_HANDOFF_F3.md"
Task: "写 script/_db_row_mining/audit_outline/_HANDOFF_F4.md"
```

---

## Implementation Strategy

### MVP First

1. Phase 1 Setup → 2. Phase 2 Foundational → 3. Phase 3（US1 进度总表）→ **STOP & VALIDATE**（对账浮标）→ 4. 余下故事。

### Incremental Delivery

1. Setup＋Foundational → 数字可信
2. US1 → 进度总表（MVP）
3. US2 → 四份交接书（接手入口可用）
4. US3 → 四份任务书（可续跑）
5. US4 → 主交接书回指（单一入口闭环）

### 预期产出计数

| 类 | 件数 | 路径 |
| --- | ---: | --- |
| 勘测脚本 | 2 | `work/_fclaims_scan.py`、`work/_fnext_scan.py` |
| 进度总表 | 1 | `script/_db_row_mining/audit_outline/_PROGRESS_SNAPSHOT_20261001.md` |
| 组级交接书 | 4 | `script/_db_row_mining/audit_outline/_HANDOFF_F{1..4}.md` |
| 下一批任务书 | 4 | `01-项目管理/01-编纂规划与报告归档/大纲邮件审计_F{1-04,2-b02,3-06,4-b05}-任务书-20261001.md` |
| 主交接书回指 | 1 | `script/_db_row_mining/audit_outline/_HANDOFF_OAA.md` §9.6 |
| 宿主清单 | 2 | `work/hosts_f3_06.txt`、`work/hosts_f4_b05.txt` |

---

## Notes

- [P] 任务＝不同文件、无依赖
- 本特性**不执行**判读/应用/修库 —— 这些属各批任务书的职责
- 每个检查点可停下独立验收
- 禁用语：任务书写“本批完成”前必须先有磁盘证据
