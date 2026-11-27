# 验收检查点：OAA F1–F4 四组交接书与下一批任务书

**Feature**: `specs/001-oaa-f1f4-next-batch/` ｜ **生成**: 2026-10-01
**语义**：每条为“通过／不通过”二值判定；生成时一律 `[ ]`，**勾选权归复核人**（`[x]`＝经复核通过，非生产者自勾）。
**分层**：一 实现完整性 → 二 需求覆盖 → 三 边界与异常 → 四 既有功能未回归。

## 一、实现完整性

- [ ] Check 1: `script/_db_row_mining/audit_outline/_HANDOFF_F1.md` 存在且行数 ≥60（来源：spec FR-002／Task T014）
- [ ] Check 2: `script/_db_row_mining/audit_outline/_HANDOFF_F2.md` 存在且行数 ≥60（来源：FR-002／T015）
- [ ] Check 3: `script/_db_row_mining/audit_outline/_HANDOFF_F3.md` 存在且行数 ≥60（来源：FR-002／T016）
- [ ] Check 4: `script/_db_row_mining/audit_outline/_HANDOFF_F4.md` 存在且行数 ≥60（来源：FR-002／T017）
- [ ] Check 5: `01-项目管理/01-编纂规划与报告归档/大纲邮件审计_F1-04-任务书-20261001.md` 存在且含七节（〇/一/二/三/四/五/六/七）（来源：FR-003／T019）
- [ ] Check 6: `…/大纲邮件审计_F2-b02-任务书-20261001.md` 同上（来源：FR-003／T20）
- [ ] Check 7: `…/大纲邮件审计_F3-06-任务书-20261001.md` 同上（来源：FR-003／T21）
- [ ] Check 8: `…/大纲邮件审计_F4-b05-任务书-20261001.md` 同上（来源：FR-003／T22）
- [ ] Check 9: `script/_db_row_mining/audit_outline/work/hosts_f3_06.txt` 与 `work/hosts_f4_b05.txt` 各含一行一宿主、无空行（来源：FR-003／T21・T22）
- [ ] Check 10: `_HANDOFF_OAA.md` 新增 §9.6 节，内含四份 `_HANDOFF_F*.md` 与四份任务书的路径，且四条路径逐一可打开（来源：FR-010／T025）

## 二、需求覆盖

- [ ] Check 11: 四份交接书均含且仅含约定的五节标题：已闭环批次表／在途批现场／挂账移交／特有坑／下一手与断点真值（来源：FR-002）
- [ ] Check 12: 四份交接书的“在途批现场”均给出 宿主名＋片数＋块数＋已判片数＋进度百分比＋续接起点共 6 项（来源：FR-002／SC-005）
- [ ] Check 13: 挂账清单条目数与文件可复现——F3 X1 合计 538（134+203+177+24）（来源：SC-006）
- [ ] Check 14: 四份任务书均含逐宿主路径＋块数的本批清单，条目数分别 = 1／1／26／63（来源：FR-003）
- [ ] Check 15: 四份任务书均含并发滚动路数、五门禁判据、验收标准、提交规范三节（来源：FR-003）
- [ ] Check 16: 四份任务书均含 `--gpg-sign -F` 与 `%G? ＝ G` 的提交要求（来源：FR-007）
- [ ] Check 17: 四份任务书均含 `oaa_register.py --ledger processed_fN.jsonl` 与收工 `oaa_beacon.py --refresh`（来源：FR-008）
- [ ] Check 18: 四份任务书均标注取量时点“2026-10-01 02:22”并写明“开工以 `--status` 实测为准”（来源：FR-009／SC-004）
- [ ] Check 19: F3-06 任务书含避让过滤说明，明确 4 个避让文件不审、不登记、不改动（来源：FR-006）
- [ ] Check 20: 四份任务书均含 fix-db 三情形分流表（①②当场修库／③挂账 X1）（来源：FR-005）
- [ ] Check 21: 交接书 §二 引用的每条批报告路径，在 `08-核查报告与多轮复核/07-目录审计/` 下真实存在（来源：spec US2 验收场景 2）

## 三、边界与异常

- [ ] Check 22: 四份任务书本批宿主集与同组在途批宿主集**交集为空**（来源：FR-004／T024）
- [ ] Check 23: 四份任务书本批宿主集 ∪ 同组在途批宿主集 ∪ 已审宿主 ⊆ `beacon/claims_FN.txt`（越界检查）（来源：FR-004）
- [ ] Check 24: F3-06 宿主清单不含 basename 以 `112.10`／`121.1`／`121.4`／`122.10` 开头者（来源：FR-006／T21）
- [ ] Check 25: F4-b05 宿主清单不含 `f4b04` 的 16 个在途宿主（来源：FR-004／T22）
- [ ] Check 26: F1-04 宿主清单不含 `88.5`（`f1_b03` 在途）；F2-b02 宿主 = `184.1`（`f2_b01`＝`173.1` 在途）（来源：FR-004）
- [ ] Check 27: 本特性执行期间 `05-卷册大纲/**` 无本会话写入——以 `git status --porcelain 05-卷册大纲/` 与抽查文件 mtime 证实（来源：SC-003）
- [ ] Check 28: 本特性执行期间 `audit_outline/shards/**` 与 `judgements/**` 无本会话写入（来源：SC-003）
- [ ] Check 29: 卷目录名与磁盘一致：交接书/任务书中出现的第12/17/18/20 卷名分别为 `macos的bsd遗产`／`政治制度与社区治理`／`全球社区地区bsd史`／`linux社区史与比较研究`（来源：plan Phase 0）
- [ ] Check 30: 避让清单块数记 9,110（＝浮标 57,969 − 实算 48,859），且交接书注明与原载 7,988 的差异原因（并行会话增写）（来源：spec Edge Cases）

## 四、既有功能未回归

- [ ] Check 31: `_HANDOFF_OAA.md` 原有 §一–§八、§9.1–9.5 内容**逐字保留**（仅新增 §9.6 与刷新 §九 数字表）——以 `git diff --numstat` 证实删除行仅在数字表内（来源：spec US4）
- [ ] Check 32: `beacon/claims_F*.txt` 与 `claims_UNCLAIMED.txt` 未被本特性改写（认领边界不变）（来源：plan Constraints）
- [ ] Check 33: `processed.jsonl` 与 `processed_f1..f4.jsonl` 行数未变（基线冻结＋分片台账由各组独占写）（来源：plan Constraints）
- [ ] Check 34: 四组组任务书（`大纲邮件审计任务组F{1,2,3,4}-任务书-20260929.md`）未被改动（来源：plan Structure Decision）
- [ ] Check 35: 新增的两个勘测脚本为**只读**——grep 确认其中无 `open(...,'w')`／`os.remove`／`shutil` 写入调用（来源：plan Constraints）
- [ ] Check 36: `specs/001-oaa-f1f4-next-batch/` 四件齐全（`spec.md`／`plan.md`／`tasks.md`／`checklist.md`）＋ `checklists/requirements.md`（来源：技能收尾报告）

## 缺口登记

- （无）—— 生成时未发现 spec 需求、验收场景或 tasks 任务无对应检查点者。
