---
spec_id: S11
title: 缓存与垃圾识别清理机制
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 十二、缓存与垃圾识别清理（S11 的设计约束）
version: 1.0.1
status: closed
goals: [10]
owner: ykla
created: 2026-11-27
updated: 2026-11-28
binding_id: TB-20261127-S11
---

# S11 缓存与垃圾识别清理机制

## 1. 意图确证（档 A 摘要）

- **用户原话（节录）**：对既有缓存，垃圾建立清理识别机制。
- **目标**：建立缓存与垃圾的分类、检测、TTL、引用检查、清单、隔离、复扫机制；先解决 `cleanup_temp.py` 与 `audit_temp_residue.py` 缺失；设计阶段不删除。
- **非目标**：
  - 不在本 spec 删除任何文件。
  - 不做全仓清理；须 ykla 明示、另批。
  - 不改 `12-数据库备份/`。
  - 不设自动化定时清理。
- **验收判据**：
  - 分类覆盖 cache／temp／sidecar／orphan／snapshot／large／misnamed／empty。
  - 检测规则可机判；每条有正反例。
  - TTL 与保护清单明确；清单含 sha256 与引用检查。
  - 缺失执行器／门禁有处置结论（补实现或改规则）。
- **手段自由度**：
  - 复用 `audit_sidecar_backup.py`；`git ls-files`、mtime、grep 引用、du。
  - 清理清单沿用 §12 与既有 `cleanup_manifest.tsv` 字段。
  - D 路清点 2.13 GiB 初始池。
- **未知／[待验证]**：
  - `script/` 顶层 10k＋文件中哪些可删。
  - `_tmp/` 与 `dvd6/` 的保护边界。
  - 缺失执行器是补实现还是改规则。

## 2. 范围

### 2.1 范围内

- 分类
- 检测规则
- TTL
- 引用检查
- 清单
- plan／apply／verify
- 隔离
- 保护清单
- 缺失设施处置

### 2.2 范围外

- 实际删除
- 全仓清理
- 备份目录清理
- 自动化

### 2.3 依赖

- D 路清点
- S09 工具表（one-shot 识别）
- 工程实践规则 §12

## 3. 用户故事与验收场景

### US-S11-1 能识别

**Why this priority**：先知道哪些是缓存／垃圾，再谈清理。

**Independent Test**：任取一类，扫描能列出路径、体积、可再生产性。

**Acceptance Scenarios**：

1. Given `__pycache__`，When 扫描，Then 列出体积与文件数。
2. Given `.bak`，When 扫描，Then 标旁路备份并禁止新增。

### US-S11-2 不误删

**Why this priority**：删除不可逆；必须有清单、引用检查、隔离。

**Independent Test**：任取一个 delete 候选，有 sha256 与引用检查结果。

**Acceptance Scenarios**：

1. Given 一个被规则引用的文件，When 扫描，Then 标 keep。
2. Given 一个歧义项，When 计划，Then 进隔离而非删除。

### US-S11-3 可复扫

**Why this priority**：清理后要证明零残留。

**Independent Test**：`--verify` 复扫 allowlist，零残留。

**Acceptance Scenarios**：

1. Given 清理完成，When 复扫，Then 0 残留。
2. Given 隔离区超期，When 复扫，Then 进下一轮清单。

## 4. 功能需求

| 编号 | 需求 | 验收判据 |
| ---- | ---- | -------- |
| S11-FR-01 | MUST 定义分类：cache、temp、sidecar、orphan、snapshot、large、misnamed、empty。 | 分类表；每类判据。 |
| S11-FR-02 | MUST 定义检测规则：路径 glob、年龄、引用、tracked、哈希、保护清单。 | 规则表；正反例。 |
| S11-FR-03 | MUST 定义 TTL：缓存 7／30 天；one-shot 30 天；隔离 30 天；备份按 12 政策。 | TTL 表。 |
| S11-FR-04 | MUST 做引用检查：basename 在规则、报告、任务书、脚本中出现即 keep／archive。 | 引用检查脚本；结果。 |
| S11-FR-05 | MUST 产出清单：path、type、category、size、mtime、sha256、in_scope、referenced、regenerable、action、reason。 | 清单字段齐全。 |
| S11-FR-06 | MUST 定义 `scan→plan→apply→verify` 流程；apply 只删 allowlist 内 delete。 | 流程；权限边界。 |
| S11-FR-07 | MUST 定义保护清单：05、旧大纲、12-数据库备份、数据库、changelog、规则、历史报告。 | 保护清单；越界即 FAIL。 |
| S11-FR-08 | MUST 处置缺失设施：`cleanup_temp.py`、`audit_temp_residue.py` 补实现或改规则删引用。 | 决策记录；不假定可用。 |
| S11-FR-09 | MUST 记账：清单、删除计数、隔离计数、复扫结果入 changelog。 | 台账；可追溯。 |
| S11-FR-10 | MUST 不设自动化；清理由人在场按批执行。 | 无定时任务；批记录。 |

## 5. 非功能需求

- 安全：清单、sha256、隔离、复扫、保护清单。
- 可复现：扫描命令与口径。
- 可审计：每项有 reason。
- 克制：只清本任务产物与用户指定范围。

## 6. 关键实体

- CacheCandidate（path、category、size、action）
- Policy（TTL、protection、allowlist）
- Manifest（scan、plan、apply、verify）
- Quarantine（path、reason、expiry）

## 7. 标准与方法基线

- ISO 15489-1:2016（处置）
- GB/T 26162-2021
- ISO 14721:2025（信息包）
- 工程实践规则 §12

## 8. 交付物

- `缓存与垃圾识别机制.md`
- `cache_policy.tsv`
- `scan_report_template.tsv`
- `audit_cache_residue.py` 规格
- `缺失设施处置.md`

## 9. 风险与未决

- 误删不可逆；清单、隔离、复扫。
- `script/` 体量大；先扫顶层与已知缓存。
- 缺失执行器导致流程空转；先补或改规则。

## 10. 追溯

- **目标**：G10 缓存垃圾机制
- **任务**：T-S11-001、T-S11-002、T-S11-003、T-S11-004、T-S11-005、T-S11-006、T-S11-007、T-S11-008
- **验收**：C-S11-001、C-S11-002、C-S11-003、C-S11-004、C-S11-005、C-S11-006、C-S11-007、C-S11-008、C-S11-009、C-S11-010
- **依赖**：见 §2.3
- **被依赖**：见任务书 §3 追溯矩阵
- **绑定**：`BINDING.tsv` 对应行；任务书 §16
