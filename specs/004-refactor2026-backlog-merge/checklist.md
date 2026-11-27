# 验收检查点 Checklist: 重构2026 建议书与待执行待办任务合并总账

**Purpose**: 对本 feature 的交付与施工逐项做“通过／不通过”二值判定。生成时一律 `[ ]`；勾选权归复核人——`[x]` 表示该判据经复核通过。
**Created**: 2026-10-09
**Feature**: [spec.md](./spec.md) ｜ [tasks.md](./tasks.md)

> 分层：一 实现完整性 → 二 需求覆盖 → 三 边界与异常 → 四 既有功能未回归。

## 一、实现完整性（交付物齐备）

- [ ] Check 1: `specs/004-refactor2026-backlog-merge/` 下 `spec.md`／`plan.md`／`tasks.md`／`checklist.md` 四件均存在且非空（来源：Task 1 交付边界）
- [ ] Check 2: 同目录下 `research.md`／`data-model.md`／`quickstart.md`／`contracts/backlog-ledger-contract.md`／`checklists/requirements.md` 五件均存在且非空（来源：plan.md Project Structure）
- [ ] Check 3: `spec.md` 含 User Scenarios & Testing／Requirements／Success Criteria／Assumptions 四个强制节（来源：spec 模板）
- [ ] Check 4: `tasks.md` 中每条任务均以 `- [ ]` 起始，且形如 `T### [P?] [US?] 描述＋路径`；缺 ID、缺路径者计数＝0（来源：tasks 格式规则）
- [ ] Check 5: `plan.md` 之 Constitution Check 表列出宪法 I–VII 条与 Execution Constraints，结论全为 PASS（来源：宪法）
- [ ] Check 6: `research.md` §R1 给出“最近的 spec”唯一认定＝`.trae/specs/converge-all-remaining-tasks/`，并列出判定证据（路径／mtime／`change-id`／勾选状态）（来源：FR-001／Task T006）
- [ ] Check 7: `research.md` §R2 含 A–E 五源小节，每节给出绝对路径与实测证据（行号／勾选状态）（来源：FR-002／Task T008–T012）
- [ ] Check 8: `data-model.md` 定义合并条目（E1）字段表，且含校验规则 V1–V5 与不变量 I1–I4（来源：Task T003）

## 二、需求覆盖（spec ↔ tasks ↔ checklist 互指）

- [ ] Check 9: 每条 Functional Requirement（FR-001～FR-014）至少被一条 tasks 任务覆盖；无覆盖的 FR 计数＝0（来源：FR-006／Task T018）
- [ ] Check 10: 每条 tasks 任务可回溯到至少一条 FR 或一条 US；孤立任务计数＝0（来源：FR-006／Task T018）
- [ ] Check 11: 四个用户故事（US1–US4）各在 `tasks.md` 中形成独立相，且每相含 Goal 与 Independent Test（来源：spec US1–US4）
- [ ] Check 12: `tasks.md` 中全部施工类任务均带 `（映射 converge:T#.#）`，映射键计数＝施工类任务数（来源：FR-004／Task T019）
- [ ] Check 13: 本 spec 的映射键集合 ⊆ `.trae/specs/converge-all-remaining-tasks/tasks.md` 之 Task/SubTask 编号集合（来源：FR-012／契约 §2）
- [ ] Check 14: 唯一任务书中未勾的 Task 2／3／4／5／6／7 在本 spec 中均有对应条目；遗漏计数＝0（来源：FR-004／Task T019）
- [ ] Check 15: `tasks.md` 中“不可判定措辞”计数＝0（扫描词：正常／良好／可接受／合理／较好）（来源：FR-005／Task T017）
- [ ] Check 16: `spec.md` 之 Success Criteria（SC-001～SC-010）每条均可在不依赖实现细节的前提下判定（来源：spec 模板）
- [ ] Check 17: `spec.md` 无 `[NEEDS CLARIFICATION]` 标记残留（来源：checklists/requirements.md）

## 三、边界与异常

- [ ] Check 18: “最近的 spec”认定**排除** `specs/003-login-claim-outline`，排除理由已留痕（该 spec 明定不得涉及重构2026 文件夹）（来源：FR-001／Task T007）
- [ ] Check 19: 每条待执行项均带**可定位证据锚点**（文书路径可 `Test-Path` 命中，或“库名＋主键”形式）；指向临时目录（`_tmp/`／`_audit_tmp/`）的锚点计数＝0（来源：FR-003／契约 §1／Task T013）
- [ ] Check 20: 同一事项在两份台账**同时处于“在途”**的情形计数＝0（来源：FR-012／不变量 I1／Task T044）
- [ ] Check 21: “磁盘 156 章疑似未迁移”条目已标注“前置：主理人裁定——如维持搁置请批注”，未被静默开工（来源：FR-014／Task T029）
- [ ] Check 22: 源缺失线（H3／aline／bline／tri／podcast）在合并清单中标注“不可执行·保持登记”，未被列为施工项（来源：FR-014／research.md §R4）
- [ ] Check 23: 长线运行项（mail2d 族 8 件＋基建 1 件）标注为“登记监控·不重复排程”，未被并入关键路径（来源：spec Assumptions／Task T012）
- [ ] Check 24: 涉及卷级／章级（`tier ∈ {卷级, 章级}`）且 `待施工` 的条目，其前置均含“内容层收编完成”或“终校完成”（来源：不变量 I4／Task T016）
- [ ] Check 25: 涉及考据的条目（阶段 3 史料回填）附“证据锚点可定位”判据（库名＋主键或路径＋行号），且明定“未获一手不落卷”（来源：FR-011／Task T020）
- [ ] Check 26: 史料回填类条目明定“原文照录未改写”（含原件笔误照录）之纪律（来源：宪法 §III／Task T020）
- [ ] Check 27: “两套 spec 落点并存”情形已在 `plan.md` Complexity Tracking 与 `research.md` §R1 显式说明，且未合并／移动他人目录（来源：plan.md／Task T006）
- [ ] Check 28: 口径数字未硬编码——`spec.md`／`plan.md` 中所引卷／章／节／注数均标“来源文书历史时点值，施工以现跑为准”（来源：FR-008／spec Assumptions）
- [ ] Check 29: 门禁“件数”未硬编码，均表述为“以 `audit_gate_registry.py` 现跑为准”（来源：plan.md Technical Context）
- [ ] Check 30: 结构冻结前置已明定（内容层收编＋终校完成）且“冻结后禁再动结构”已写入（来源：FR-013／契约 §5）

## 四、既有功能未回归（纪律与载体）

- [ ] Check 31: 施工类任务全部只指向 `08-核查报告与多轮复核/重构2026/data/outline.txt` 或其派生件；指向 `index.html` 的**写**操作计数＝0（来源：FR-008／Task T020–T026）
- [ ] Check 32: 每批收束序列含全部八步（改内容源→装配→字体子集→再装配→门禁全量→三套回归→落账→版本递增），缺步计数＝0（来源：FR-007／契约 §3）
- [ ] Check 33: 每批落账字段（`batch_id`／`changelog_id`／`version`／`prebak`／`gates_result`／`reconciled_in`）齐备；缺字段计数＝0（来源：契约 §3／Task T026）
- [ ] Check 34: 每批均要求 prebak 备份先行，且回退路径明确（来源：FR-007／契约 §3）
- [ ] Check 35: 文本纪律判据已写入（UTF-8 无 BOM／LF／禁直角引号 U+300C·U+300D／禁制表符／禁“谱系”词），并有对应扫描任务（来源：FR-010／Task T047）
- [ ] Check 36: 提交纪律已写入（路径限定 `git commit -m <msg> -- <paths>`；不 commit 他人改动、不 rebase、不 `--force`）（来源：FR-009／契约 §3）
- [ ] Check 37: 同一内容源不可并行编辑已明定，且 `tasks.md` 中同改 `outline.txt` 的 T020–T026 标为串行（来源：FR-009／Task Dependencies）
- [ ] Check 38: 被并入 spec 的清单已列出（`finalize-refactor2026` 等 6+ 项），并含“统一勾销／标注并入”动作（来源：FR-012／Task T045）
- [ ] Check 39: 收官动作含冻结声明落盘与长线机读块刷新（`_longline_status.py --write-block`）（来源：FR-013／Task T046）
- [ ] Check 40: `quickstart.md` 四场景均可运行且各给出预期结果；场景与 checklist 层有索引对应（来源：Task T048）
- [ ] Check 41: 本 spec 收束落账覆盖 `changelog.duckdb`＋92 号文 §十一＋98 号文 §十一＋`review_logs/` 收官记录（来源：FR-013／Task T049）
- [ ] Check 42: 全程未新增根目录路径；临时脚本只落 `script/`（来源：宪法 §VI／Task T047）

## Notes

- 生成时一律 `[ ]`；`[x]` 表示该判据经复核通过。
- Check 1–8 判“交付物是否齐备”；Check 9–17 判“需求覆盖”；Check 18–30 判“边界与异常”；Check 31–42 判“既有功能与纪律未回归”。
- 任一项不通过，须在 `tasks.md` 新增修复任务后重跑。
- 本 spec 只交付 Phase 1–4；Phase 5–7 之施工判据（Check 20／25／26／31–42 中施工侧）在**主理人批准另批执行**后生效。
