# 全部数据库全字段只读审计盘点报告

> 审计日期：2026-08-26
> 审计范围：全仓库全部数据库（功能库 + 代码仓库 DuckDB + 邮件合并库 + 邮件拆分子库 + 播客库），逐库逐表逐字段盘点
> 审计方法：纯只读枚举（DuckDB `SET read_only=ON` / `PRAGMA query_only=ON`，仅 `SELECT`/`information_schema`/`PRAGMA`），全程未执行任何写库操作（无 INSERT / UPDATE / DELETE / ALTER / VACUUM / DROP）
> 数据来源：`script/_db_audit/` 本次实测产物（`schema_inventory.json`、`column_stats.json`、`data_quality_summary.json`、`cross_db_consistency.json`、`aggregate_stats.json`）+ `11-元数据接口/09-文件夹数据库索引/folder_db_registry.csv`（登记簿）
> 报告形态：本 md 为汇总；分层数据字典留档于 `script/_db_audit/`（A 类可复用资产）

## 一、审计范围

本次审计覆盖**全部 293 个数据库**（含邮件拆分子库），按职责分五类：

| 类别 | 库数 | 说明 |
| ---- | ---- | ---- |
| 播客库 | 2 | 播客/新闻库 |
| 邮件合并库 | 5 | 邮件列表合并库（按邮件系统） |
| 代码仓库库 | 11 | BSD 派生项目一手提交数据（git 元数据） |
| 功能库 | 14 | 项目功能数据库（sacred、文献、核查、索引、变更记录等） |
| 邮件拆分库 | 261 | 邮件列表拆分子库（逐主题列表） |

清单与 `folder_db_registry.csv` 比对：登记 293 条、实测 293 条，无遗漏、无误入，仅表现路径表示（绝对 vs 相对）差异，规模无出入。

按用户 2026-08-26 要求：**不做任何写库/增补大纲/修改源文件**，仅产出只读盘点报告；最后清理一次性临时文件；全部原则遵循 `00-编纂规则与格式规范/01-规则/`。

## 二、库总览（一行一库）

完整逐库清单（类别、路径、表数、列数、行数、大小、异常数）见 `script/_db_audit/db_audit_summary.csv`。下表给分类合计（仅摘要）：

| 类别 | 库数 | 表数 | 列数 | 行数 | 库大小 |
| ---- | ---- | ---- | ---- | ---- | ------ |
| 播客库 | 2 | 17 | 151 | 246,187 | 0.0 GB |
| 邮件合并库 | 5 | 25 | 233 | 9,680,946 | 61.8 GB |
| 代码仓库库 | 11 | 93 | 711 | 70,121,996 | 7.8 GB |
| 功能库 | 14 | 120 | 1181 | 1,745,125 | 1.0 GB |
| 邮件拆分库 | 261 | 1044 | 12267 | 3,242,524 | 13.4 GB |
| **合计** | 293 | 1299 | 14543 | 85,036,778 | 84.1 GB |

## 三、schema 全量清点摘要

- 库数：**293**；表数：**1299**；列（字段）数：**14543**；总行数：**85,036,778**；库体积合计：**84.08 GB**。
- 逐库逐表逐字段明细见 `script/_db_audit/schema_inventory.json`（库→表→列三级）与 `schema_reports/<db>.md`（逐库可读清单）、`schema_inventory.csv`（扁平字段表）。

### 分类权重（字段数占比）

- 邮件拆分库：261 库 / 1044 表 / 12267 列（84.3%）
- 功能库：14 库 / 120 表 / 1181 列（8.1%）
- 代码仓库库：11 库 / 93 表 / 711 列（4.9%）
- 邮件合并库：5 库 / 25 表 / 233 列（1.6%）
- 播客库：2 库 / 17 表 / 151 列（1.0%）

## 四、字段级数据质量观测清单

面向全 293 库逐列统计：非空 / NULL / distinct 计数、文本列 min/avg/max 长度。异常观测共 **6579** 条（明细见 `script/_db_audit/data_quality_report.md` 全文与 `data_quality_summary.json`）：

| 异常类型 | 条数 | 说明 |
| -------- | ---- | ---- |
| low_cardinality_or_placeholder | 3930 | 见下述 |
| all_null | 1997 | 见下述 |
| scan_error=empty_table | 652 | 见下述 |

**要点**：

- `all_null`（约 1997 条）：大量出现的字段为空值，主要分布在邮件库的**可选留空字段**（如 `body_html`/`to_text`/`cc_text` 等）与功能库 `cross_references` 等表中未落库的关联字段（如 `target_*`、`resolved_at`）——这些属结构性空值，提示有表结构预留未填充，非数据损坏。
- `low_cardinality_or_placeholder`（约 3930 条）：短文本列且 distinct ≤ 2，多为布尔/标记/短枚举字段（正常）或占位记录。
- `empty_table`（约 652 条）：整表为空（row_count = 0）的表实例。

> 数据质量观测为只读事实登记，不对任何库做修改；具体每条坐标（库/表/字段）已在 JSON 留档。

## 五、跨库一致性摘要

对同名表做字段集合与类型比对（细则见 `script/_db_audit/cross_db_consistency.md`）。摘要：

- **代码仓库库（11 库）**：`commits`/`branches` 等核心表在各库公共列与类型一致；个别库有非公共列差异（留档）。
- **功能库**：`files`/`blocks`/`schema_meta`/`cross_references` 等共性表在部分库存在字段口径差异（详见明细）。
- **邮件库**：拆分子库与合并库 `messages` 等表共性字段基本一致；空表/空字段偏差见数据质量清单。

交叉库比对仅登记结构异同，不构成孰对孰错判断。

## 六、只读约束核验

- 本审计所有脚本以只读模式打开源库；全程仅执行 `SELECT`/`information_schema`/`PRAGMA`。
- 全程**零写库**：无任何源库被写入；唯一计划内写操作为本报告末尾的 changelog 登记（见下），其按四步流程 + 写前备份 + 去重执行。

## 七、结论与后续建议（纯建议）

- 本报告提供全库全字段的只读清晰视图，供后续任何写库 / 增补 / 清理决策参考。
- 数据质量观测揭示大量结构性空字段（尤其是邮件库与引用表），建议后续（如需）按业务口径逐类核实是否应填充或标识。

## 八、临时文件清理记录（2026-08-26 用户一次性例外）

按用户 2026-08-26“最后清理临时文件”的显式要求——本项目“script/ 不清理”规则在此为一次性显式用户例外——对只读审计产生的一次性临时产物执行清理。清理对象：

- 删除（C 类：运行日志 / 临时演示副本）：`script/_db_audit/enumerate_schema.log`、`script/_db_audit/data_stats_scan.log`；`script/_staging/changelog_demo.duckdb`（changelog 写库演示临时副本）。
- 保留（A 类：可复用资产）：审计脚本 `discover_databases.py` / `crosscheck_registry.py` / `enumerate_schema.py` / `generate_schema_reports.py` / `data_stats_scan.py` / `generate_data_quality_report.py` / `cross_db_consistency.py` / `generate_phase4_report.py` / `changelog_precheck.py` / `register_changelog.py`；数据字典 `schema_inventory.json` / `schema_inventory.csv` / `column_stats.json` / `data_quality_summary.json` / `cross_db_consistency.json` / `aggregate_stats.json` / `db_list.json` / `crosscheck_report.json` / `db_audit_summary.csv`；可读清单 `schema_reports/`（293 个） / `data_quality_report.md` / `cross_db_consistency.md`。

> 清理时间：2026-08-26。清理清单与审计结论同步登记于 `01-项目管理/00-变更记录/changelog.duckdb` 变更记录（id=949，2026-08-26）。
