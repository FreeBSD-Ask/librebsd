# DDJ（dvd6 期刊四库）任务书与交接书

> **迁入**：2026-10-17（主理人令“全部迁移”）｜**原址**：`script/_ddj_out/`。总登记与口径见 [`../任务书迁移登记.md`](../任务书迁移登记.md)。

**线状态：🟨 ACTIVE**（依 2026-10-19 w22 对盘实测；w20–w22 三波已把 10-05 台账全面推进）：

- 🟩 **已完成**：T001–T025（US1 全链，侦察→骨架→issues/articles/sources/figures/ads→**T025 核验 26/26 PASS**）；T027 refs 著录四库 **10,068 条**（GB/T 7714，双向孤儿 0）；T004/T024 广告侦察（**ads 空表为证实结论**）；**T032 卷归属裁定**（2026-10-12 落定，四刊 10,068 篇宿主卷一律**第21卷**，claim 号段 `CL-21-00001`~`CL-21-03431` 连续无洞）；T028/T029 表实存（summaries 3,611／key_facts 19,422）；**T034 已落纲 3,431 条 bullet**（第21卷卷末书目述评）。
- 🟨 **部分完成**：判定 **3,611/10,068＝35.87%**，五方闭环 **3,431**（claims_ready＝raw_source＝evidence＝claim_evidence＝claim＝bullet）；w21 摘录污染清零（四库 9,491 段／0 非逐字）；T022 图片转写 TPJ 54/106 批已加载，CUJ／SA／DDJ 批次已生成未开工（⚠️ 续跑须先按 `kind` 字段判别桩文件再 load）。
- ⬜ **未做**：T033 `related_chapter`（列存在、非空 **0/19,422**；章级映射口径待裁定——考据记录已列为挂账存疑，**非被 T032 阻塞**）、T035 大纲门禁、T036 quickstart 终验、T037 `final_report.md`（文件不存在）、T038 四库推送、T039 本战役 `HANDOFF.md`（文件不存在）；**余 6,457 篇待判**（ddj 3,416／cuj 1,800／sa 1,241／tpj 0）。

| 文件 | 角色 |
| ---- | ---- |
| `002-dvd6-journal-db-任务书-20260929.md` | **现行任务书**（Spec Kit 任务书＋w22 任务书逐项对盘快照；2026-10-19 由 `specs/002-dvd6-journal-db/tasks.md` 迁入，原址已换指针桩） |
| `_历史快照/002-dvd6-journal-db-任务书.pre_w22_20261019.md` | 批次史轮替分册（w11／w14／w15／w16＋w17／w18／w19／w20／w21 等 10 块快照；存档件，勿采信为现行） |
| `HANDOFF.md` | 战役交接台账（四库现状表、已完成/未完成清单、坑位留痕；2026-10-05 会话末台账，口径已过期，以本表线状态为准） |
| `ads_rules.md` | 广告判定规则 |
| `dispatch_templates.md` | 派单模板 |

⚠️ 四库 DuckDB **活跃真值在 `C:\Users\ykla\Documents\libre\{ddj,cuj,sa,tpj}.duckdb`**（`C:\ddj_stage\` 为 10-09 建库原件、非续跑入口）；两者均**不在仓库**。最终推送目标 `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\`（T038 未做，该目录尚不存在）。机器可读产出（`articles_inventory.json`／`figures_inventory_*.json`／`verify_all_report.json` 等）仍留 `script/_ddj_out/`；判读工作区在本机 `C:\Users\ykla\Documents\libre\ddj_claim_work\`。
