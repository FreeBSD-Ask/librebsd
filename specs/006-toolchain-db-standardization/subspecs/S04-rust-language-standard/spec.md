---
spec_id: S04
title: Rust 化评估与编程语言标准
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 八、Rust 化与编程语言标准（S04 的设计约束）
version: 1.0.0
status: draft
goals: [3]
owner: ykla
created: 2026-11-27
updated: 2026-11-27
binding_id: TB-20261127-S04
---

# S04 Rust 化评估与编程语言标准

## 1. 意图确证（档 A 摘要）

- **用户原话（节录）**：工具链能用rust改写的尽量用rust改写，建立编程语言标准，逐个评估。
- **目标**：对 121 个 Python 工具做逐工具 Rust 改写评估，建立 Python／Rust／JS／SQL／Shell 语言标准与 Rust 工程基线，给出生产改写、影子运行、灰度与回退方案；生产改写已获 ykla 2026-11-27 批准。
- **非目标**：
  - 不无基准地改写；每个改写批须有基准、影子比对与回退。
  - 不为 Rust 而 Rust；无收益不动。
  - 不把 Rust 引入 PDF／OCR 等生态薄弱环节。
  - 不立即删除 Python 入口；兼容期至少一个季度。
- **验收判据**：
  - 121 个 Python 工具 100% 有评估结论（改写／保留／观察）。
  - 每个“建议改写”有基准确认瓶颈、生态可行、回退可行。
  - 语言标准覆盖 Python／Rust／JS／SQL／Shell，三级（强制／推荐／禁止）。
  - Rust 基线含 edition、`rust-version`、clippy、fmt、deny、audit、lock、unsafe 政策。
  - 生产改写按影子、灰度、回退执行，每批有观测指标与任务审计准入。
- **手段自由度**：
  - 只读源码、依赖、运行基准。
  - Rust 官方规范（Reference、API Guidelines、Style Guide、Cargo Book、MSRV）。
  - DuckDB／Arrow／Polars／PDF／OCR 生态调研。
- **未知／[待验证]**：
  - Rust 改写后的真实性能收益需基准。
  - PDF／OCR 生态在 Rust 的成熟度。
  - 团队（单人＋AI）维护两语言的实际成本。

## 2. 范围

### 2.1 范围内

- 候选工具与评分矩阵
- 基准方法
- 生态可行性
- 决策规则
- 语言标准
- Rust 工程基线
- FFI／PyO3
- 生产改写与回退
- 供应链

### 2.2 范围外

- 立即删除 Python 实现
- 引入 nightly-only
- 更换 DuckDB 版本

### 2.3 依赖

- S03 的 CLI 契约与并发判据
- S01 的 Rust／供应链标准
- S09 的工具表

## 3. 用户故事与验收场景

### US-S04-1 逐个评估，不拍脑袋

**Why this priority**：改写需要数据与判据，不能以“Rust 更快”代替。

**Independent Test**：任取一个候选，矩阵有基准、生态、回退三项证据。

**Acceptance Scenarios**：

1. Given 一个 CPU 密集工具，When 查矩阵，Then 有基准与收益估计。
2. Given 一个 PDF 工具，When 查生态，Then 说明 Rust 生态可行性。

### US-S04-2 语言有标准

**Why this priority**：多语言混用需要统一规范，避免风格与依赖失控。

**Independent Test**：任取一种语言，标准有强制／推荐／禁止三级与判据。

**Acceptance Scenarios**：

1. Given Python 新代码，When 查标准，Then 有类型标注、ruff、`-I` 要求。
2. Given Rust crate，When 查基线，Then 有 edition、MSRV、clippy、deny。

### US-S04-3 生产改写可回退

**Why this priority**：改写失败不能影响生产。

**Independent Test**：生产改写有影子运行、逐字节比对、灰度与回退开关。

**Acceptance Scenarios**：

1. Given 一个改写批，When 影子运行，Then 输出与 Python 逐字节／逐记录比对。
2. Given 失败，When 回退，Then 恢复 Python 入口。

## 4. 功能需求

| 编号 | 需求 | 验收判据 |
| ---- | ---- | -------- |
| S04-FR-01 | MUST 对 121 个 Python 工具逐个评分：计算密度、瓶颈、生态、并发、维护、分发、供应链、回退。 | 矩阵 121 行；无空项。 |
| S04-FR-02 | MUST 用基准确认瓶颈；无基准不得下“值得改写”结论。 | 基准命令与数据；环境记录。 |
| S04-FR-03 | MUST 评估生态：duckdb-rs、arrow、polars、pdf、ocr、http、cli。 | 每类有可行／不可行结论与替代。 |
| S04-FR-04 | MUST 定义决策规则：收益／成本比、回退可行、生态可行三者同时满足。 | 规则可二值判定；反例。 |
| S04-FR-05 | MUST 建立语言标准：Python／Rust／JS／SQL／Shell，三级。 | 标准表；每条有判据。 |
| S04-FR-06 | Rust 基线 MUST 含 Edition 2024、`rust-version`、`Cargo.lock`、fmt、clippy `-D warnings`、deny、audit。 | 模板 `Cargo.toml`＋CI 命令。 |
| S04-FR-07 | MUST 定义 unsafe 政策：默认 `forbid`，例外 crate 白名单＋SAFETY 注释＋Miri。 | 政策与检查命令。 |
| S04-FR-08 | MUST 定义 FFI／PyO3 边界：`Send`／`Sync`、生命周期、错误映射、禁止共享可变引用。 | FFI 规范；示例。 |
| S04-FR-09 | MUST 给出生产改写方案：影子运行、逐字节／逐记录比对、灰度、回退、批准。 | 方案步骤；回退开关。 |
| S04-FR-10 | MUST 覆盖供应链：SLSA 1.2、SPDX 3.0.1／CycloneDX 1.7、ISO/IEC 5230、SSDF。 | SBOM 与 provenance 方案。 |
| S04-FR-11 | MUST 明确“不建议改写”的工具与理由，避免范围膨胀。 | 保留清单；理由可复述。 |
| S04-FR-12 | 生产改写 MUST 按批次执行：每批有基准、影子比对、灰度、回退点与任务审计准入。 | 批次记录；观测指标；回退演练。 |

## 5. 非功能需求

- 可复现：基准环境、输入、版本、命令。
- 可回退：Python 入口保留至少一个季度。
- 可维护：单仓库、单工具链、依赖锁定。
- 安全：unsafe 最少化、依赖审计、SBOM。

## 6. 关键实体

- Candidate（tool_id、score、decision）
- Benchmark（metric、value、env）
- LanguageRule（language、level、rule）
- RustCrate（name、edition、rust_version、unsafe_policy）
- Pilot（tool、shadow、compare、rollback）

## 7. 标准与方法基线

- Rust 2024 Edition（1.85.0）
- Rust 1.100.0（2026-11-12）
- Rust Reference
- Rust API Guidelines
- Rust Style Guide
- RFC 2495
- Cargo Book
- Clippy／rustfmt／cargo-deny／cargo-audit
- Miri
- SLSA 1.2
- SPDX 3.0.1／ISO/IEC 5962:2021
- CycloneDX 1.7／ECMA-424
- ISO/IEC 5230:2020
- NIST SP 800-218 v1.1
- SemVer 2.0.0
- RFC 2119／8174

## 8. 交付物

- `Rust评估矩阵.tsv`
- `语言标准.md`
- `Rust工程基线.md`
- `FFI规范.md`
- `生产改写方案.md`
- `保留清单.md`
- `供应链方案.md`

## 9. 风险与未决

- Rust 生产改写已批准；收益仍须基准与回退控制。
- PDF／OCR 生态弱；保留 Python。
- 双语言维护成本高；限定热路径与 CLI 层。

## 10. 追溯

- **目标**：G3 Rust 化与语言标准
- **任务**：T-S04-001、T-S04-002、T-S04-003、T-S04-004、T-S04-005、T-S04-006、T-S04-007、T-S04-008、T-S04-009、T-S04-010、T-S04-011
- **验收**：C-S04-001、C-S04-002、C-S04-003、C-S04-004、C-S04-005、C-S04-006、C-S04-007、C-S04-008、C-S04-009、C-S04-010、C-S04-011、C-S04-012
- **依赖**：见 §2.3
- **被依赖**：见任务书 §3 追溯矩阵
- **绑定**：`BINDING.tsv` 对应行；任务书 §16
