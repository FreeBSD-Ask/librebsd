---
spec_id: S09
title: 全局工具表
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 十一、全局工具表（S09 的设计约束）
version: 1.0.1
status: closed
goals: [8]
owner: ykla
created: 2026-11-27
updated: 2026-11-28
binding_id: TB-20261127-S09
---

# S09 全局工具表

## 1. 意图确证（档 A 摘要）

- **用户原话（节录）**：建立全局工具表，稳定调用应入git跟踪的，临时的，要及时清理的，表格字段起码要有创建时间，最后修改时间，作用，生命周期等。
- **目标**：建立机器可读、可校验、由脚本生成的全局工具表：覆盖 139 件固定工具与 `script/` 顶层一次性工具，字段含创建时间、最后修改时间、作用、生命周期、是否入库、规则引用；稳定工具入库，临时工具按 TTL 清理。
- **非目标**：
  - 不手写大表；表由生成器产出。
  - 不在本 spec 删除 one-shot；只标清理候选。
  - 不改工具行为。
  - 不把外部二进制纳入 git。
- **验收判据**：
  - 工具表覆盖 100% 固定工具与 `script/` 顶层；stable 覆盖 100%。
  - 字段含 created_at、last_modified、purpose、lifecycle、tracked、rule_references。
  - 生成器与校验器可复跑；`tracked` 与 `git ls-files` 一致。
  - one-shot 超期有清单；不自动删除。
- **手段自由度**：
  - `git ls-files`、文件 mtime、规则 grep、`folder_db_registry.csv`、备份 SCOPE。
  - TSV 为主，Markdown 为派生视图。
  - 生成器与校验器放 `01-规则/脚本与命令/`，执行期登记。
- **未知／[待验证]**：
  - 139 件工具中哪些是 stable 的最终名单（D 路初判 96 件，需复核）。
  - `script/` 顶层 10k＋文件的 one-shot 识别规则。
  - 工具表是否入库（建议入库）。

## 2. 范围

### 2.1 范围内

- 工具总表 schema
- 数据源与合并规则
- 生成器
- 校验器
- 生命周期规则
- stable／temporary 判定
- tracked 一致性
- TTL 与清理候选
- 例外覆盖

### 2.2 范围外

- 删除工具
- 改工具
- Rust 化
- 外部依赖安装

### 2.3 依赖

- S03 的工具分类
- S11 的清理机制
- D 路清点

## 3. 用户故事与验收场景

### US-S09-1 一表看全

**Why this priority**：维护者需要知道有哪些工具、做什么、是否还在用。

**Independent Test**：任取一个工具，表中有路径、作用、生命周期、创建／修改时间。

**Acceptance Scenarios**：

1. Given 一个固定工具，When 查表，Then 字段齐全。
2. Given 一个 one-shot，When 查表，Then 标临时与 TTL。

### US-S09-2 稳定与临时分开

**Why this priority**：稳定工具应入库；临时工具应清理。

**Independent Test**：stable 全部 tracked；one-shot 全部 untracked 且有到期日。

**Acceptance Scenarios**：

1. Given stable 工具，When 查 tracked，Then true。
2. Given one-shot 超过 30 天，When 查清单，Then 标清理候选。

### US-S09-3 表可复算

**Why this priority**：手写表会漂移；必须由脚本生成。

**Independent Test**：生成器重跑输出一致；校验器能发现漂移。

**Acceptance Scenarios**：

1. Given 生成器，When 重跑，Then 表不变或差异可解释。
2. Given 手工改表，When 跑校验，Then FAIL。

## 4. 功能需求

| 编号 | 需求 | 验收判据 |
| ---- | ---- | -------- |
| S09-FR-01 | MUST 定义工具表 schema：tool_id、name、path、category、language、entrypoint、purpose、owner、created_at、last_modified、lifecycle、tracked、rule_references、gates、dependencies、invocation、exit_codes、last_verified、verification_method、risk、notes。 | schema 文件；字段与 data-model 一致。 |
| S09-FR-02 | MUST 合并四源：`git ls-files`、规则 grep、`folder_db_registry.csv`、备份 SCOPE。 | 合并规则；冲突处置。 |
| S09-FR-03 | MUST 提供生成器 `build_tool_registry.py`；输出 TSV＋MD。 | 生成器可跑；输出可 diff。 |
| S09-FR-04 | MUST 提供校验器 `audit_tool_registry.py`；检查必填、路径、tracked、stable 条件、one-shot 超期、孤儿。 | 校验器 `--selftest`＋`--check`。 |
| S09-FR-05 | MUST 定义生命周期规则：stable／experimental／deprecated／one-shot／external。 | 规则表；判据二值。 |
| S09-FR-06 | stable MUST 满足：tracked、规则引用、`--selftest`、90 天调用证据；缺一降级。 | stable 清单；缺项说明。 |
| S09-FR-07 | one-shot MUST 满足：untracked、`script/` 路径、30 天 TTL；超期进清理候选。 | 到期清单；不自动删。 |
| S09-FR-08 | `tracked` MUST 与 `git ls-files` 一致；不一致即 FAIL。 | 校验器输出。 |
| S09-FR-09 | MUST 支持人工例外覆盖（只改备注／风险，不改生成字段）。 | 覆盖文件；冲突规则。 |
| S09-FR-10 | MUST 提供 dashboard 摘要：按生命周期、语言、类别、tracked 计数。 | 摘要节；数字可复算。 |

## 5. 非功能需求

- 可复算：生成器＋校验器。
- 可 diff：TSV 排序稳定。
- 可审计：字段有来源。
- 可维护：例外覆盖不污染主表。

## 6. 关键实体

- Tool（21 字段）
- Source（git、rules、registry、SCOPE）
- Lifecycle（状态、判据、TTL）
- Override（tool_id、field、value、reason）

## 7. 标准与方法基线

- ISO/IEC 19770-2:2015（SWID 结构参照）
- SPDX 3.0.1／CycloneDX 1.7（组件清单参照）
- SemVer 2.0.0
- ISO 8601-1:2019/Amd 1:2022

## 8. 交付物

- `工具总表.tsv`
- `工具总表.md`
- `build_tool_registry.py`
- `audit_tool_registry.py`
- `生命周期规则.md`
- `例外覆盖.tsv`

## 9. 风险与未决

- stable 判定依赖规则引用，而规则引用本身可能陈旧；需人工复核。
- `script/` 顶层 10k＋文件，one-shot 识别成本高；先按扩展名／日期／引用筛。
- 工具表入库需规则引用与门禁登记；执行期走 E1—E13。

## 10. 追溯

- **目标**：G8 全局工具表
- **任务**：T-S09-001、T-S09-002、T-S09-003、T-S09-004、T-S09-005、T-S09-006、T-S09-007、T-S09-008
- **验收**：C-S09-001、C-S09-002、C-S09-003、C-S09-004、C-S09-005、C-S09-006、C-S09-007、C-S09-008、C-S09-009、C-S09-010
- **依赖**：见 §2.3
- **被依赖**：见任务书 §3 追溯矩阵
- **绑定**：`BINDING.tsv` 对应行；任务书 §16
