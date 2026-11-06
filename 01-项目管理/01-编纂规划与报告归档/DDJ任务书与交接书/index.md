# DDJ（dvd6 期刊四库）任务书与交接书

> **迁入**：2026-10-17（主理人令“全部迁移”）｜**原址**：`script/_ddj_out/`。总登记与口径见 [`../任务书迁移登记.md`](../任务书迁移登记.md)。

**线状态：⬛ CANCELLED／收官（2026-11-07 主理人令）**——**放弃“入 claim 库＋入 05-大纲”两层、判定全线停止；存量原样保留，只停增量**。终态口径见任务书“收官状态（2026-11-07）”节；下文 2026-10-22 实测块与三行状态为收官前的历史对盘记录，保留不回改。

- 🟩 **已完成（保留为成果）**：T001–T025（US1 全链，侦察→骨架→issues/articles/sources/figures/ads→**T025 核验 26/26 PASS**）；T027 refs 著录四库 **10,068 条**（GB/T 7714，双向孤儿 0）；T004/T024 广告侦察（**ads 空表为证实结论**）；**T032 卷归属裁定**（2026-10-12 落定，四刊 10,068 篇一律**第21卷**）；T028 summaries **4,171**／T029 key_facts **22,415**（2026-11-07 本机实测终态，随收官停止追加）。
- ⏹ **收官终态（2026-11-07 本机只读实测；w23 旧值已被推翻）**：判定 **4,171/10,068＝41.43%**（ddj 1,856／cuj 1,346／sa 469／tpj 500）——cuj 库 mtime 10-21 07:08，比 w23 记录多 360 篇且未载于任何波次记录；未判 **5,897 篇** 随收官作废。claim 存量 **3,950 条** `CL-21-00001`~`CL-21-03950`（2026-11-07 运行时升至 2.0.0 后实测，与 bullet 3,950 一一对应；此前记 3,619 为陈旧值）、大纲第21卷 bullet 存量 **3,950 条**（DDJ 1,739／CUJ 1,254／SA 466／TPJ 491，11-07 磁盘实测）——两者均**保留不追加**；T022 图片转写 TPJ 54/106 批已加载，其余按 10-11 令①豁免挂账。
- 📦 **DDJ 库完整性（11-07 实测）**：issues 343 期 1988–2009 逐年无缺、articles 5,272、refs 5,272 双向孤儿 0，与源快照年度包 100% 对齐；**建库完整成立、内容全量不成立**（图片 uncertain 4,565 豁免、概述/原料 1,856／9,823 冻结、1988 年前刊期不在源快照）。详见任务书“收官状态”节§五。
- ⬛ **撤销与终止（2026-11-07 收官令）**：**入 claim 库与入大纲两层放弃**（原 10-11 调整令第 3 条撤销）——T033 章级映射、T035 大纲门禁收口、claim ROW_MINE 章块全部取消；T036 quickstart 终验／T037 `final_report.md`／T038 四库推送随线终止；T039 交接以任务书“收官状态”节接续完成。**存量不删库、不改大纲、不回溯。**
- 🟨 **2026-11-07 第二令重开（仅 US2 两层）**：质量复核全绿（逐字 0 违规）→ 四库合并为 `dvd6_journals.duckdb`（**207.51 MB，`v2.0.0+`**，schema `ddj`／`cuj`／`sa`／`tpj`＋`main.journal_registry`，全表 md5 与源库一致，**合并库为唯一工作真值**）→ 概述／原料补全流水线上线（`ddj_fill_work/` 1,374 批／6,048 篇，装载器五道判据整篇拒收）。**进度 4,243/10,068＝42.14%，余 5,825 篇，约 130 波跨会话推进**；续跑入口 `_ddj_fill_status.py`。详见任务书“六、2026-11-07 第二令”节。

| 文件 | 角色 |
| ---- | ---- |
| `002-dvd6-journal-db-任务书-20260929.md` | **现行任务书**（Spec Kit 任务书＋w22 任务书逐项对盘快照；2026-10-19 由 `specs/002-dvd6-journal-db/tasks.md` 迁入，原址已换指针桩）；**2026-11-07 收官**，文首收官令与“收官状态”节为唯一现行口径 |
| `_历史快照/002-dvd6-journal-db-任务书.pre_w22_20261019.md` | 批次史轮替分册（w11／w14／w15／w16＋w17／w18／w19／w20／w21 等 10 块快照；存档件，勿采信为现行） |
| `HANDOFF.md` | 历史件（2026-10-05 停更；四库现状表、已完成/未完成清单、坑位留痕；口径已过期，现行入口为任务书 2026-10-22 对盘块） |
| `ads_rules.md` | 广告判定规则 |
| `dispatch_templates.md` | 派单模板 |

⚠️ 四库 DuckDB **活跃真值在 `C:\Users\ykla\Documents\libre\{ddj,cuj,sa,tpj}.duckdb`**（`C:\ddj_stage\` 10-09 建库原件**已于 2026-11-07 按主理人令删除**）；四库**不在仓库**。最终推送目标 `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\`——**T038 已随 2026-11-07 收官终止，该目录不建，四库为仓外资产**。机器可读产出（`articles_inventory.json`／`figures_inventory_*.json`／`verify_all_report.json` 等）仍留 `script/_ddj_out/`；判读工作区 `C:\Users\ykla\Documents\libre\ddj_claim_work\`（判读件证据链，保留）。

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
