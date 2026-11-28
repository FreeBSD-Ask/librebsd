---
spec_id: S03
title: 工具链归一化与并发
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 七、工具链归一化与并发（S03 的设计约束）
version: 1.0.1
status: closed
goals: [2]
owner: ykla
created: 2026-11-27
updated: 2026-11-28
binding_id: TB-20261127-S03
---

# S03 工具链归一化与并发

## 1. 意图确证（档 A 摘要）

- **用户原话（节录）**：对项目的数据库和工具链进行归一化，清洗，标准化，并发，多线程支持。
- **目标**：统一 139 件固定工具与 `script/` 一次性工具的 CLI、路径、配置、并发、锁、检查点与基准；设计阶段不改工具。
- **非目标**：
  - 不重写、不删除、不移动现有脚本。
  - 不做 Rust 化（S04）。
  - 不改门禁判据。
  - 不在本 spec 执行实际并发批。
- **验收判据**：
  - stable 工具 100% 映射到 CLI 契约。
  - 硬编码盘符清零方案可执行；真实代码路径仅 `audit_a11y.py:53` 等少数。
  - 并发模型覆盖 DuckDB 单写多读、Python 进程／线程／异步、锁、背压、检查点。
  - 基准方案可复跑；基准数据有环境与命令。
- **手段自由度**：
  - 只读源码扫描与 `--help` 试跑。
  - DuckDB 2.0 官方并发文档。
  - Python 3.15 官方文档与 PEP 703／734。
- **未知／[待验证]**：
  - 本机 Python 3.15 是否 free-threaded 构建。
  - 部分工具无 `--help`，需先补契约。
  - 并发批的实际瓶颈需基准确定。

## 2. 范围

### 2.1 范围内

- 工具分类与生命周期
- CLI 契约
- 路径与配置规范
- 并发模型
- 锁与检查点
- 背压与限速
- 基准方法
- 迁移与兼容

### 2.2 范围外

- 实际重写
- Rust 迁移
- 门禁判据修改
- 删除 one-shot

### 2.3 依赖

- S09 工具表 v0
- S01 的 DuckDB／Python 官方文档约束
- S04 消费本 spec 的并发判据

## 3. 用户故事与验收场景

### US-S03-1 工具可发现、可调用

**Why this priority**：维护者需要统一入口与退出码，不靠猜。

**Independent Test**：任取 10 个 stable 工具，`--help` 可跑、退出码语义一致。

**Acceptance Scenarios**：

1. Given 一个 stable 工具，When 跑 `--help`，Then 有用法、参数、退出码。
2. Given 一个写操作，When 跑 `--dry-run`，Then 不写盘并打印计划。

### US-S03-2 并发不撞库

**Why this priority**：多会话、多批、多进程同时写会损坏数据。

**Independent Test**：两个写同一库的批同时启动，只有一个获得锁。

**Acceptance Scenarios**：

1. Given 两个写批，When 同时启动，Then 一个 PASS、一个安全退出。
2. Given 锁超时，When 重试，Then 指数退避且有上限。

### US-S03-3 长任务可续跑

**Why this priority**：批中断后不能从头再来。

**Independent Test**：检查点能让任务从上一批继续，且幂等。

**Acceptance Scenarios**：

1. Given 一个长任务，When 中断后重启，Then 从 checkpoint 继续。
2. Given 同一批重跑，When 已完成，Then 新增 0。

## 4. 功能需求

| 编号 | 需求 | 验收判据 |
| ---- | ---- | -------- |
| S03-FR-01 | MUST 建立工具分类与生命周期映射，覆盖 139 件固定工具与 `script/` 顶层。 | 覆盖率 100%；分类字段非空。 |
| S03-FR-02 | stable 工具 MUST 支持 `--help`、`--root`、`--dry-run`；写操作支持 `--apply`／`--verify`；门禁支持 `--selftest`／`--check`。 | 契约矩阵；缺项列整改。 |
| S03-FR-03 | MUST 消除硬编码盘符；路径从 `Path(__file__)` 或 `--root` 派生。 | 扫描 0 真实代码路径；示例文本可保留但标明。 |
| S03-FR-04 | MUST 定义配置优先级：CLI > 环境变量 > 配置文件；禁止隐式主目录状态。 | 配置规范；示例可复跑。 |
| S03-FR-05 | MUST 定义 DuckDB 单写多读、写批串行化、读批并行边界。 | 并发规范；与官方文档一致。 |
| S03-FR-06 | MUST 定义锁协议：waterlock、文件锁、超时、死锁检测、释放。 | 锁测试用例；异常路径有处理。 |
| S03-FR-07 | MUST 定义检查点与幂等：输入哈希、完成项、失败项、下一站。 | checkpoint schema；重跑 +0。 |
| S03-FR-08 | MUST 定义背压、限速、重试与队列上界。 | 参数表；失败重试有上限。 |
| S03-FR-09 | MUST 定义基准方法：启动、吞吐、内存、I/O、查询 p50／p95；记录环境。 | 基准报告可复跑。 |
| S03-FR-10 | MUST 给出迁移与兼容方案：先影子、再灰度、保留回退入口。 | 迁移步骤；回退可执行。 |
| S03-FR-11 | MUST 评估共享库 `librebsd_toolkit` 的模块边界与入库可行性。 | 模块清单；依赖方向；入库决策点。 |

## 5. 非功能需求

- 可复现：命令、环境、输入、版本可追溯。
- 并发安全：单写多读、锁超时、幂等。
- 可维护：单一入口、路径派生、配置显式。
- 性能：基准有基线，不以“更快”替代正确性。

## 6. 关键实体

- Tool（tool_id、path、lifecycle、entrypoint）
- CLIContract（flags、exit_codes、outputs）
- Lock（scope、owner、timeout、state）
- Checkpoint（task、input_hash、done、failed、next）
- Benchmark（env、dataset、metric、value）

## 7. 标准与方法基线

- DuckDB 2.0 concurrency docs
- Python 3.15 docs（threading／multiprocessing／asyncio／concurrent.futures）
- PEP 703
- PEP 734
- ISO/IEC/IEEE 29119-1:2022（测试独立性）
- ISO/IEC 25010:2023（性能效率）

## 8. 交付物

- `工具分类与生命周期.tsv`
- `CLI契约.md`
- `路径与配置规范.md`
- `并发模型.md`
- `锁与检查点规范.md`
- `基准报告.tsv`
- `迁移与兼容方案.md`

## 9. 风险与未决

- 工具数量多、命名不统一；先分类后改造，不一次动全部。
- 无 `--help` 的工具需先补；补契约可能改变行为。
- free-threaded Python 兼容性未测；按有 GIL 设计，实测后再议。

## 10. 追溯

- **目标**：G2 工具链归一化／并发
- **任务**：T-S03-001、T-S03-002、T-S03-003、T-S03-004、T-S03-005、T-S03-006、T-S03-007、T-S03-008、T-S03-009、T-S03-010、T-S03-011
- **验收**：C-S03-001、C-S03-002、C-S03-003、C-S03-004、C-S03-005、C-S03-006、C-S03-007、C-S03-008、C-S03-009、C-S03-010、C-S03-011
- **依赖**：见 §2.3
- **被依赖**：见任务书 §3 追溯矩阵
- **绑定**：`BINDING.tsv` 对应行；任务书 §16
