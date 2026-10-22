# checklist.md — td022-crossvol-review-20261022

## 准入与证据

- [x] `任务审计台账.md` 有本任务准入行，结论 PASS，理论适用性引 TG-003／004／008
- [x] 77 项裁定表 `script/_td022_cv_verdict_20261022.csv` 行数 = 79（77 项登记＋2 条补出），`FALSE-POSITIVE` = 75，`REAL` = 4（其中 2 条为 CSV 漏登记、本批补出）
- [x] 每行含错位成因（字典序 `.10` < `.9`）或真实形态说明

## 处置正确性

- [x] `130.0.20-GAPAYTBEGIN20261020缺口A662期战役注入.md` 已删，删除前全文 sha256 `ba3f7318a59bf595…` 在案
- [x] `130.0.21-GAPAYTBEGIN20261020缺口A662期战役注入-2.md` 已删，删除前全文 sha256 `514d511a9fdedd3c…` 在案
- [x] 删除前断言：两文件除标题与空行外仅一条 BEGIN，无其他内容
- [x] `130.0.18` 首个 `ROW_MINE` 行之前有且仅有一条同形 BEGIN（第 3 行，首个 ROW_MINE 第 4 行）
- [x] `130.0.19` 首个 `ROW_MINE` 行之前有且仅有一条同形 BEGIN（同上）
- [x] `130.0` 目录现存 19 个 .md（原 21 减 2）

## 守恒断言

- [x] BEGIN/END 全树总数：GAP-A-YT 294/294、W172-YT-ROUTE 130/130、REVIEW-ANNOT 729/729（英文）＋1080/1080（含中文 开始／结束 各 351）不变
- [x] 按章＋节号数值序配对：全树残余 0
- [x] 非标记行逐字不变（逐文件反向复原比对）
- [x] `ROW_MINE`／`DEEP_ANALYSIS` 锚在两文件 24／14 与 5,810 未变
- [x] 全树 UTF-8 无 BOM、LF 无 CRLF
- [x] 目录内 `git diff --numstat` 仅 2 改 2 删；整树另含 3 处派生件联动（已在 changelog 与 §十 说明）

## 判据与门禁接线

- [x] `audit_anchor_pair_order.py --selftest` 正负样本全过（10 项）
- [x] `audit_anchor_pair_order.py --check` exit 0
- [x] `audit_gate_registry.py` 登记第三十四件、`STAGE_MAP` 合法、R1–R8 全 PASS
- [x] `脚本与命令/README.md` 有该脚本行（用途、触发条件、自检命令）
- [x] `TD-022-成对锚处置判据书.md` D4 已补“作用域＝章、排序键＝节号数值序、75 项伪报教训”（§四、§十）
- [x] `AGENTS.md` 门禁表与件次索引已补第三十四件

## 台账与收口

- [x] `changelog.duckdb` 有 159 批缺行补记（id=2484）
- [x] 去重线批号解释歧义句已写入 changelog（id=2484 附注：目录线 150–157 批 vs 清理线 去重 P1 批 1／2、TD-022 D1）
- [x] 本批 changelog 一行（id=2485，含门禁退出码、断言结论、删文件清单、prebak）
- [x] `任务复核台账.md` 三轮记录齐（RV-20261022-011／012／013），角色与作者分离
- [x] `任务审计台账.md` 收口行四段齐：`prebak=`、`已知限制=`、`轮替=`、`归档=`
- [x] `sync_outline_mirror.py --check` 零漂移；`audit_mirror_ingest.py` PASS
- [x] 常备三件 PASS：`sync_refactor2026_baseline --check`、`_longline_status --check`、`audit_gate_registry`

## 负向自检

- [x] 临时夹具中故意留一条未配 BEGIN，`audit_anchor_pair_order --check` 报 FAIL（`--selftest` P2 用例）
- [x] 临时夹具改回字典序，脚本报 2 条伪报（`--selftest` 负向对照用例），证明判据非空

## 收口备注

- 归档：`01-项目管理/01-编纂规划与报告归档/长线任务归档总登记表/12-工程批次规格归档/003-td022-crossvol-review-20261022/`
- 提交：`c63f1a323`（树＋派生件）、`9c6b086d7`（脚本＋规则与台账）
- 已知限制：`chapter_keywords.json` 的 `085.6.14` 键序差异；`ROW_MINE` 全树旧值 502,298 → 实测 501,415
