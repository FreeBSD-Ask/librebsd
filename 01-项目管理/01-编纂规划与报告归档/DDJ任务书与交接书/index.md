# DDJ（dvd6 期刊四库）任务书与交接书

> **迁入**：2026-10-17（主理人令“全部迁移”）｜**原址**：`script/_ddj_out/`。总登记与口径见 [`../任务书迁移登记.md`](../任务书迁移登记.md)。

**线状态：🟨 部分完成**（依 2026-10-05 会话末台账 `HANDOFF.md`）：

- 🟩 **已完成**：T001–T025（US1 全链，侦察→骨架→issues/articles/sources/figures/ads→**T025 核验 26/26 PASS**）；T027 refs 著录四库 **10,068 条**（GB/T 7714，0 孤儿）；T004/T024 广告侦察（**ads 空表为证实结论**）。
- 🟨 **部分完成**：T022 图片 LLM 转写 —— TPJ 54/106 批已加载（301 transcribed＋28 base64，余 327 uncertain）；CUJ／SA／DDJ 批次已生成未开工；⚠️ 续跑须先按 `kind` 字段判别桩文件再 load。
- ⬜ **未做**：US3（根阻塞＝T032 考据文件不存在）、T038 推送。

| 文件 | 角色 |
| ---- | ---- |
| `HANDOFF.md` | 战役交接台账（四库现状表、已完成/未完成清单、坑位留痕） |
| `ads_rules.md` | 广告判定规则 |
| `dispatch_templates.md` | 派单模板 |

⚠️ 四库 DuckDB 在本地暂存 `C:\ddj_stage\{ddj,cuj,sa,tpj}.duckdb`（**不在仓库**）；最终推送目标 `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\`（T038 未做）。机器可读产出（`articles_inventory.json`／`figures_inventory_*.json`／`verify_all_report.json` 等）仍留 `script/_ddj_out/`。
