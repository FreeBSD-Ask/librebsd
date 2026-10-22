# DDJ（dvd6 期刊四库）任务书与交接书

> **迁入**：2026-10-17（主理人令“全部迁移”）｜**原址**：`script/_ddj_out/`。总登记与口径见 [`../任务书迁移登记.md`](../任务书迁移登记.md)。

**线状态：🟨 ACTIVE**（2026-10-22 22:33 本机只读实测，结论见文末“2026-10-22 实测进度块”；四库不在本机，库侧数值仍只能沿用 2026-10-19 w22 快照）：

- 🟩 **已完成**：T001–T025（US1 全链，侦察→骨架→issues/articles/sources/figures/ads→**T025 核验 26/26 PASS**）；T027 refs 著录四库 **10,068 条**（GB/T 7714，双向孤儿 0）；T004/T024 广告侦察（**ads 空表为证实结论**）；**T032 卷归属裁定**（2026-10-12 落定，四刊 10,068 篇宿主卷一律**第21卷**，claim 号段 `CL-21-00001`~`CL-21-03431` 连续无洞）；T028/T029 表实存（summaries 3,611／key_facts 19,422）；**T034 已落纲 3,431 条 bullet**（第21卷卷末书目述评）。
- 🟨 **部分完成**：判定 **3,611/10,068＝35.87%**，五方闭环 **3,431**（claims_ready＝raw_source＝evidence＝claim_evidence＝claim＝bullet）；w21 摘录污染清零（四库 9,491 段／0 非逐字）；T022 图片转写 TPJ 54/106 批已加载，CUJ／SA／DDJ 批次已生成未开工（⚠️ 续跑须先按 `kind` 字段判别桩文件再 load）。
- ⬜ **未做**：T033 `related_chapter`（列存在、非空 **0/19,422**；章级映射口径待裁定——考据记录已列为挂账存疑，**非被 T032 阻塞**）、T035 大纲门禁、T036 quickstart 终验、T037 `final_report.md`（文件不存在）、T038 四库推送、T039 本战役交接（`HANDOFF.md` 实存但停在 2026-10-05，仅为历史件；现行进度以任务书 2026-10-22 对盘块为准）；**余 6,457 篇待判**（ddj 3,416／cuj 1,800／sa 1,241／tpj 0）。

| 文件 | 角色 |
| ---- | ---- |
| `002-dvd6-journal-db-任务书-20260929.md` | **现行任务书**（Spec Kit 任务书＋w22 任务书逐项对盘快照；2026-10-19 由 `specs/002-dvd6-journal-db/tasks.md` 迁入，原址已换指针桩） |
| `_历史快照/002-dvd6-journal-db-任务书.pre_w22_20261019.md` | 批次史轮替分册（w11／w14／w15／w16＋w17／w18／w19／w20／w21 等 10 块快照；存档件，勿采信为现行） |
| `HANDOFF.md` | 历史件（2026-10-05 停更；四库现状表、已完成/未完成清单、坑位留痕；口径已过期，现行入口为任务书 2026-10-22 对盘块） |
| `ads_rules.md` | 广告判定规则 |
| `dispatch_templates.md` | 派单模板 |

⚠️ 四库 DuckDB **活跃真值在 `C:\Users\ykla\Documents\libre\{ddj,cuj,sa,tpj}.duckdb`**（`C:\ddj_stage\` 为 10-09 建库原件、非续跑入口）；两者均**不在仓库**。最终推送目标 `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\`（T038 未做，该目录尚不存在）。机器可读产出（`articles_inventory.json`／`figures_inventory_*.json`／`verify_all_report.json` 等）仍留 `script/_ddj_out/`；判读工作区 `C:\Users\ykla\Documents\libre\ddj_claim_work\`。

## 2026-10-22 22:33 本机实测进度块（只读复核）

> 复核脚本 `script/_scan_ddj_truth_20261022.py`（纯只读）｜复核报告 `script/_review_chain_20261022/DDJ_REVIEW.md`｜本块**取代**上文“本机无四库副本／未复测”一类未经实测的表述。

**一、本机身份（本机实测）**

- `hostname`＝**`DESKTOP-M5P610N`**；主要 IPv4：`192.168.5.4`（以太网 2／DHCP），另有 `192.168.56.1`、`192.168.179.1`、`192.168.137.1`（虚拟或共享网卡）、若干 `169.254.*`（APIPA）。
- 与 T038 推送目标 `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\` **同名**；本机 `Get-Volume` 显示 C:／D: 均为 **Fixed 本地盘**（非网络映射），`Get-SmbShare` 有共享 `D`→`D:\`。故**本机即推送目标机**，推送目标实际落地为本机 `D:\librebsd\dvd6\Website\ddj\`。
- **本机不是四库真值机**：真值记录位置 `C:\ddj_stage\`、`C:\Users\ykla\Documents\libre\` 在本机均**不存在**；按任务书 10-11 实测记录，其宿主为作业机 `DESKTOP-RLOEIG9`（异机）。故四库属**在别处（异机）**，**不是**真值缺失或真值消失——任务书旧表述“本机无四库副本”易被误读为“副本已丢”，本块据实测改正。

**二、真值扫描（本机实测，89 秒／预算 180 秒／无截断）**

- 搜索面：`C:\Users\ykla\Documents`（深 5）、`C:\Users\ykla`（深 2）、`C:\`（深 3）、`D:\`（深 3）、`D:\librebsd`（深 3）、`D:\librebsd\dvd6`（深 6），`C:\ddj_stage`（根不存在）；累计访问 528,149 项。
- 目标 `{ddj,cuj,sa,tpj}.duckdb` 与 `ddj_claim_work`／`ddj_stage`／`libre`：**搜索面内 0 命中**。
- `C:\ddj_stage` 不存在；`C:\Users\ykla\Documents\libre` 不存在；`D:\librebsd\dvd6\Website\ddj` 不存在；`D:\librebsd` 与 `dvd6` 树内 `.duckdb` 0 件。
- `script/_ddj_out/` 实存：`articles_inventory.json`（943,520 B）、`figures_inventory_{ddj,cuj,sa,tpj}.json`、`verify_all_report.json`（2,673 B，T025 实证）、`issues_inventory.json`、`fulltext_schema.json`、`coverage_gap.md` 等；**缺** `final_report.md`（T037）、`rules_adopted.md`（T026）、`verify_rules_report.md`（T030）、`verify_outline_report.md`（T035）。
- 误建痕迹：`D:\librebsd\dvd6\Website\DESKTOP-M5P610N\d\librebsd\script\_ddj_out\transcribe_batches\batch_tpj_076.jsonl`（0 B，2026-10-06 14:37:48）——UNC 路径被当作相对路径落盘的产物，**非** T038 推送结果，不得误读。

**三、可离线复核的两项（不依赖四库）**

- **T034 实存**：`08-核查报告与多轮复核/12-重构大纲书目述评/第21卷-传播渠道与工具生态-卷末书目述评.md`（493,391 B）内 `ref (DDJ|CUJ|SA|TPJ)-` bullet **3,950 条**（DDJ 1,739／CUJ 1,254／SA 466／TPJ 491）；上文所记 3,431 为“五方闭环”旧值，磁盘实测已增至 3,950。旧路径 `05-卷册大纲/第21卷…/卷末书目述评.md` 已不存在（书评全文外迁制；卷内章号已重编为第 407–414 章）。
- **大纲口径**：`重构2026/index.html` 的 `doc-metrics` ＝ **75 卷 523 章 3705 节**；`sync_refactor2026_baseline.py --check` **exit 0／零未处置漂移**。任务书 2026-10-22 块内“74 卷／521 章／3,691 节”为过期时点值，以本块为准。

**四、阻塞项与解阻条件**

1. 四库与 `ddj_claim_work` 均在异机 `DESKTOP-RLOEIG9`；须在该机续跑，或把四库复制回本机——本机即推送目标机，此动作等价于执行 T038，**须先取得主理人明示**，不得默认开工。
2. T035／T036／T037／T038 全部以四库在场为前提，四库缺失下**根本不可执行**：T035 的 ref 悬空检查、T036 的 quickstart 场景 1–7、T038 的源侧字节级比对均无对象。
3. 下一批开工前，须按 `任务审计台账.md` §二 先在该表主表增行并填准入结论与证据（高风险、≥3 轮复核）；T035／T036 门禁未补齐前不得推新批（依 `工程实践规则.md` §0 及其不追溯条款，本线 2026-10-22 前已启动部分不补审、不重开）。
