---
spec_id: S02
title: 数据库归一化与清洗
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 六、数据库归一化与质量框架（S02／S06 的设计约束）
version: 1.0.1
status: closed
goals: [2]
owner: ykla
created: 2026-11-27
updated: 2026-11-28
binding_id: TB-20261127-S02
---

# S02 数据库归一化与清洗

## 1. 意图确证（档 A 摘要）

- **用户原话（节录）**：对项目的数据库和工具链进行归一化，清洗，标准化，并发，多线程支持。
- **目标**：对项目数据库做全量清点、数据字典、键与函数依赖分析、范式判定、清洗规则与迁移／回退设计；设计阶段只读，不写库。
- **非目标**：
  - 不在本 spec 执行 DDL／DML；迁移须另批授权。
  - 不删除任何库或表；不合并库。
  - 不把分析型宽表强行拆成 3NF；反规范化须有理由。
  - 不改变 `historical_claims.duckdb` 唯一真值路径。
- **验收判据**：
  - Tier A 28 库覆盖率 100%；Tier B/C 有清单与分层理由。
  - 每库有数据字典、键、函数依赖、范式判定与反规范化理由。
  - 清洗规则可机判；每条有正例／反例。
  - 迁移方案有 dry-run、行数对账、校验和与回退。
- **手段自由度**：
  - 只读 DuckDB 连接；`PRAGMA`、`information_schema`、`duckdb_databases()`。
  - 大库可复制到临时目录再剖析；复制件按临时件管理。
  - 函数依赖用 SQL 反例与闭包脚本复算。
- **未知／[待验证]**：
  - Tier B/C 的 50 件未登记库是否都属项目内容资产。
  - `folder_db_registry.csv` 字段错位的确切原因。
  - 部分库可能被其他会话锁定。

## 2. 范围

### 2.1 范围内

- 库人口与分层（磁盘 ∪ SCOPE ∪ 注册表）
- schema 清单与数据字典
- 键、函数依赖、范式判定
- 清洗规则（空值、重复、孤儿、编码、时间、路径）
- 迁移与回退设计
- 校验与对账方案

### 2.2 范围外

- 实际迁移
- 库合并
- 删除历史数据
- 改备份策略

### 2.3 依赖

- S06 的质量记分卡 v0 作为输入
- S01 的 11179／25012 约束
- 写批另批＋guard／waterlock

## 3. 用户故事与验收场景

### US-S02-1 知道每个库有什么

**Why this priority**：维护者需要一眼看到库、表、列、键、行数与来源。

**Independent Test**：任取一库，数据字典能回答表／列／键／行数／来源。

**Acceptance Scenarios**：

1. Given 一个正式库，When 查字典，Then 表、列、类型、键、行数齐全。
2. Given 一个字段，When 查来源，Then 有 source_snapshot 或 provenance。

### US-S02-2 知道该不该拆表

**Why this priority**：规范化不是目的；需要函数依赖与反例支撑。

**Independent Test**：任取一个 3NF 判定，能给出函数依赖与反例。

**Acceptance Scenarios**：

1. Given 一张宽表，When 查判定，Then 有 FD 列表与范式结论。
2. Given 一个反规范化，When 查理由，Then 有查询／更新异常权衡。

### US-S02-3 迁移可回退

**Why this priority**：任何结构变更都可能损坏数据；必须能回退。

**Independent Test**：迁移方案逐步可执行，回退后行数与校验和一致。

**Acceptance Scenarios**：

1. Given 迁移方案，When 跑 dry-run，Then 输出行数与差异。
2. Given 回退步骤，When 执行，Then 回到基线校验和。

## 4. 功能需求

| 编号 | 需求 | 验收判据 |
| ---- | ---- | -------- |
| S02-FR-01 | 库人口 MUST 由磁盘、备份 SCOPE、注册表三方并集确定，并分层（Tier A/B/C）。 | 三方对账表；差异逐条解释。 |
| S02-FR-02 | Tier A 每库 MUST 有 schema 清单：表、列、类型、可空、主键、外键、行数。 | 清单覆盖率 100%。 |
| S02-FR-03 | 每库 MUST 有 `schema_meta` 或等价元数据；缺者列入整改。 | 字段对照 §6.2；缺字段计数。 |
| S02-FR-04 | 每库 MUST 有数据字典：名称、定义、类型、值域、来源、责任。 | 字典覆盖率 100%（Tier A）。 |
| S02-FR-05 | MUST 识别候选键与函数依赖；用 Armstrong 公理求闭包并给反例。 | FD 表＋闭包输出＋反例查询。 |
| S02-FR-06 | MUST 判定 1NF—BCNF；反规范化须写理由与影响。 | 逐表判定；理由非空。 |
| S02-FR-07 | MUST 定义清洗规则：空值、重复、孤儿、枚举、编码、时间、路径。 | 规则表＋正反例。 |
| S02-FR-08 | MUST 给出迁移方案：步骤、dry-run、行数对账、校验和、回退。 | 方案可逐步执行；回退可复算。 |
| S02-FR-09 | MUST 给出迁移后验证：行数、键、孤儿、抽样逐字。 | 验证 SQL／脚本与预期结果。 |
| S02-FR-10 | 设计阶段 MUST 零写入；任何写操作另批并走 guard／waterlock。 | `read_only=True` 证据；无 DDL／DML。 |

## 5. 非功能需求

- 可复现：剖析脚本、输入、版本、命令可追溯。
- 可回退：迁移前有基线校验和与备份槽。
- 性能：大库分片剖析，不静默超时。
- 兼容：不改现有库路径与逻辑名。

## 6. 关键实体

- Database（db_name、path、tier、schema_version）
- Table（name、rows、columns、keys）
- Column（name、type、nullable、domain）
- FunctionalDependency（determinant、dependent、evidence）
- MigrationStep（order、sql、rollback、check）

## 7. 标准与方法基线

- ISO/IEC 25012:2008
- ISO/IEC 25024:2015
- ISO/IEC 11179-1:2023
- ISO/IEC 11179-3:2023/Amd 1:2026
- GB/T 25000.12-2017
- GB/T 36344-2018
- Armstrong 1974
- Codd 1970/1971/1972
- DuckDB 2.0 concurrency docs

## 8. 交付物

- `库人口与分层.tsv`
- `数据字典/`（按库）
- `键与函数依赖.tsv`
- `范式判定.md`
- `清洗规则.tsv`
- `迁移与回退方案.md`
- `验证方案.md`

## 9. 风险与未决

- 大库剖析耗时／锁冲突；分片与只读复制。
- 注册表字段错位导致人口误判；以磁盘与 SCOPE 为准。
- 迁移方案与在途写批冲突；写批另批、锁与窗口。

## 10. 追溯

- **目标**：G2 数据库归一化
- **任务**：T-S02-001、T-S02-002、T-S02-003、T-S02-004、T-S02-005、T-S02-006、T-S02-007、T-S02-008、T-S02-009、T-S02-010
- **验收**：C-S02-001、C-S02-002、C-S02-003、C-S02-004、C-S02-005、C-S02-006、C-S02-007、C-S02-008、C-S02-009、C-S02-010
- **依赖**：见 §2.3
- **被依赖**：见任务书 §3 追溯矩阵
- **绑定**：`BINDING.tsv` 对应行；任务书 §16
