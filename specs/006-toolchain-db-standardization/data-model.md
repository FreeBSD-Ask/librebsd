---
spec_id: M
title: 工具链与数据库标准化（数据模型）
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 十一、全局工具表（S09 的设计约束）
version: 1.0.0
status: draft
goals: [2, 5, 8, 10, 12]
owner: ykla
created: 2026-11-27
updated: 2026-11-27
---

# Data Model: 工具链与数据库标准化

> 本件定义六张核心逻辑表。物理形态优先 TSV（可 diff、可入库）；需要 SQL 查询时由生成器导入 DuckDB 临时库，不另立真值。

## 1. 实体关系

```text
TaskBook 1 ─── N Spec 1 ─── N FR
                 │
                 └── N Binding (1:1 Spec)
Tool N ─── N Rule
Tool N ─── N Gate
Database 1 ─── N Table 1 ─── N Column
Database 1 ─── N QualityMetric
Database 1 ─── N Dataset
Standard N ─── N FR
CacheCandidate N ─── 1 PathPolicy
```

## 2. `tool_registry`（全局工具表）

**物理载体**：`01-项目管理/03-架构与技术文档/工具总表.tsv`（执行期建立；本批只定义）。
**生成器**：`build_tool_registry.py`；**校验器**：`audit_tool_registry.py`。

| 列 | 类型 | 必填 | 约束 | 说明 |
| -- | ---- | ---- | ---- | ---- |
| `tool_id` | string | 是 | 唯一，`T-<domain>-<seq>` | 稳定标识 |
| `name` | string | 是 | 非空 | 文件名／命令名 |
| `path` | string | 是 | 相对仓库根，存在 | 主入口路径 |
| `category` | enum | 是 | gate/writer/scanner/collector/converter/service/analysis/other | 类别 |
| `language` | enum | 是 | python/rust/sql/js/shell/other | 语言 |
| `entrypoint` | string | 是 | 可执行命令模板 | 调用方式 |
| `purpose` | string | 是 | ≤120 字 | 作用 |
| `owner` | string | 是 | ykla／线名 | 责任者 |
| `created_at` | date-time | 是 | ISO 8601 | 创建时间 |
| `last_modified` | date-time | 是 | ISO 8601 | 最后修改 |
| `lifecycle` | enum | 是 | stable/experimental/deprecated/one-shot/external | 生命周期 |
| `tracked` | boolean | 是 | 与 `git ls-files` 一致 | 是否入库 |
| `rule_references` | string | 否 | 分号分隔，路径存在 | 规则引用 |
| `gates` | string | 否 | 分号分隔编号 | 关联门禁 |
| `dependencies` | string | 否 | 名称＋版本 | 外部依赖 |
| `invocation` | string | 否 | 示例命令 | 调用示例 |
| `exit_codes` | string | 否 | `0=ok;1=fail;2=usage` | 退出码 |
| `last_verified` | date-time | 否 | ISO 8601 | 最近自检 |
| `verification_method` | string | 否 | selftest/manual/recompute | 验证方式 |
| `risk` | enum | 否 | low/medium/high | 风险 |
| `notes` | string | 否 | ≤240 字 | 例外与迁移指针 |

**不变量**：

- `lifecycle=stable → tracked=true ∧ has_selftest=true ∧ rule_references≠空`。
- `lifecycle=one-shot → tracked=false ∧ path 以 script/ 开头`。
- `tracked=true → path 在 `git ls-files` 中`。
- `created_at ≤ last_modified`。
- `last_verified` 为空时 `verification_method` 必须为空。

## 3. `schema_meta`（库元数据）

**物理载体**：每个正式 DuckDB 内的 `schema_meta` 表（执行期经 ADR 后建立）。

| 列 | 类型 | 必填 | 约束 |
| -- | ---- | ---- | ---- |
| `schema_name` | VARCHAR | 是 | 唯一 |
| `schema_version` | VARCHAR | 是 | SemVer |
| `built_at` | TIMESTAMPTZ | 是 | ISO 8601 |
| `source_snapshot` | VARCHAR | 是 | 源标识／commit |
| `generator` | VARCHAR | 是 | 脚本＋版本 |
| `git_commit` | VARCHAR | 否 | 生成时提交 |
| `row_count` | BIGINT | 是 | ≥0 |
| `checksum` | VARCHAR | 否 | 规范化摘要 |
| `quality_profile` | VARCHAR | 否 | 记分卡版本／路径 |
| `notes` | VARCHAR | 否 | 例外 |

**不变量**：

- 每个正式库恰有一行 `schema_name` 等于逻辑库名。
- `schema_version` 单调递增；迁移须旧→新映射。
- `row_count` 与 `COUNT(*)` 对账，差异 0 或有解释。

## 4. `quality_scorecard`（质量记分卡）

**物理载体**：`quality_scorecard.tsv`（执行期；落点待定）。

| 列 | 类型 | 必填 | 说明 |
| -- | ---- | ---- | ---- |
| `db_name` | string | 是 | 逻辑库名 |
| `db_path` | string | 是 | 物理路径 |
| `schema_version` | string | 是 | 来自 schema_meta |
| `table_count` | integer | 是 | 表数 |
| `row_count` | bigint | 是 | 总行数 |
| `size_bytes` | bigint | 是 | 文件大小 |
| `last_modified` | date-time | 是 | mtime |
| `registry_match` | boolean | 是 | 与 folder_db_registry 一致 |
| `schema_meta_present` | boolean | 是 | 是否有元数据表 |
| `pk_fk_coverage` | float | 是 | 主键／外键覆盖率 0—1 |
| `orphan_count` | integer | 是 | 跨表孤儿总数 |
| `duplicate_rate` | float | 是 | 重复键率 |
| `null_rate` | float | 是 | 必填列空值率 |
| `provenance_coverage` | float | 是 | provenance 覆盖率 |
| `encoding_issues` | integer | 是 | U+FFFD／非法编码计数 |
| `timestamp_min` | date-time | 否 | 最早时间 |
| `timestamp_max` | date-time | 否 | 最晚时间 |
| `quality_score` | float | 是 | 加权总分 0—100 |
| `risk_level` | enum | 是 | low/medium/high/critical |
| `top_issues` | string | 否 | 前三条问题 |
| `evidence_path` | string | 是 | 剖析输出路径 |

**计分**：15 维各 0—100，按权重求和；权重由 S06 在 ADR 中定。缺数据的维度记 `null`，不得记 0 冒充低分。

## 5. `binding_manifest`（绑定清单）

**物理载体**：`BINDING.tsv`。

| 列 | 类型 | 必填 | 约束 |
| -- | ---- | ---- | ---- |
| `binding_id` | string | 是 | 唯一，`TB-20261127-<id>` |
| `spec_id` | string | 是 | M／S01—S12 |
| `goal_ids` | string | 是 | 逗号分隔 |
| `spec_path` | string | 是 | 存在 |
| `spec_sha256` | string | 是 | 64 hex |
| `tasks_sha256` | string | 是 | 64 hex |
| `checklist_sha256` | string | 是 | 64 hex |
| `task_book_path` | string | 是 | 存在 |
| `task_book_anchor` | string | 是 | 可定位 |
| `spec_version` | string | 是 | SemVer |
| `status` | enum | 是 | draft/active/closed/superseded |
| `updated_at` | date-time | 是 | ISO 8601 |

**不变量**：

- `binding_id` 唯一；`spec_id` 唯一。
- 三件套路径存在且哈希匹配。
- `goal_ids` 并集覆盖 1—12。
- `status` 与 spec frontmatter 一致。

## 6. `spec_frontmatter`（spec 元数据）

| 字段 | 类型 | 必填 | 约束 |
| ---- | ---- | ---- | ---- |
| `spec_id` | string | 是 | M／S01—S12 |
| `title` | string | 是 | 非空 |
| `task_book` | string | 是 | 路径存在 |
| `task_book_anchor` | string | 是 | 可定位 |
| `version` | string | 是 | SemVer |
| `status` | enum | 是 | draft/active/closed/superseded |
| `goals` | array[int] | 是 | 1—12 |
| `owner` | string | 是 | ykla |
| `created` | date | 是 | ISO 8601 |
| `updated` | date | 是 | ISO 8601 |
| `binding_id` | string | 是 | 与清单一致 |

## 7. `cache_candidate`（缓存候选）

**物理载体**：`script/_cleanup_<YYYYMMDD>/cleanup_manifest.tsv`（沿用既有清理格式）。

| 列 | 类型 | 说明 |
| -- | ---- | ---- |
| `path` | string | 相对路径 |
| `type` | enum | dir/file/glob |
| `category` | enum | cache/temp/sidecar/orphan/snapshot/large/misnamed/empty |
| `size_bytes` | bigint | 体积 |
| `mtime` | date-time | 最后修改 |
| `sha256` | string | 文件哈希（目录为空） |
| `in_scope` | boolean | 是否在 allowlist |
| `referenced` | boolean | 是否被引用 |
| `regenerable` | enum | yes/no/unknown |
| `action` | enum | keep/archive/quarantine/delete |
| `reason` | string | 判据 |

## 8. `standard_inventory`（标准清单）

| 列 | 类型 | 说明 |
| -- | ---- | ---- |
| `std_id` | string | 稳定编号 |
| `number` | string | 标准号 |
| `edition` | string | 年份／版本 |
| `title` | string | 名称 |
| `body` | enum | ISO/IEC/IEEE/ITU/W3C/GB/GB-T/DA-T/other |
| `status` | enum | current/replaced/revision/published/withdrawn |
| `clauses` | string | 适用条款 |
| `constraint` | string | 对本项目的约束 |
| `exception` | string | 例外 |
| `conflict` | string | 冲突处置 |
| `url` | string | 官方 URL |
| `retrieved_at` | date | 检索日期 |
| `evidence_level` | enum | primary/secondary/pending |
| `mapped_specs` | string | 映射到哪些 spec |

## 9. 物理与版本

- TSV：UTF-8 无 BOM、LF、制表符分隔；字段内不得含制表符／换行。
- 时间：ISO 8601 扩展格式，带时区（`2026-11-27T12:00:00+08:00`）。
- 哈希：sha256，小写 hex。
- 版本：SemVer 2.0.0。
- 变更：表结构变更须 minor 版本＋迁移说明；破坏性变更须 major＋ADR。
