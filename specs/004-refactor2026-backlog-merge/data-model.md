# Phase 1 Data Model — 合并清单实体与映射

**Feature**: `004-refactor2026-backlog-merge` | **Date**: 2026-10-09

> 本件定义“合并清单”的实体、字段约束、关系与状态机。字段约束在 `tasks.md` 中**逐字引用**，不留实现期裁量。

## E1. 合并条目（Backlog Item）

合并清单的最小单位；对应 `tasks.md` 的一行。

| 字段 | 类型 | 约束 | 说明 |
| ---- | ---- | ---- | ---- |
| `id` | 字符串 | 形如 `T###`，全局唯一、按执行序递增 | 任务编号 |
| `parallel` | 布尔 | 仅当“不同文件、无未完依赖”时为真（渲染为 `[P]`） | 可并行标记 |
| `story` | 枚举 | `US1`／`US2`／`US3`／`US4`；Setup／Foundational／Polish 相**无**此字段 | 归属用户故事 |
| `source` | 字符串 | 非空；须为**可定位锚点**（绝对或仓库相对路径，可带行号／库名＋主键） | 来源契约（见 contract §1） |
| `ledger_map` | 字符串 | 非空；形如 `converge:T2.1` | 与唯一任务书的映射键 |
| `tier` | 枚举 | `卷级`／`章级`／`节级`／`注级`／`零节变`／`非内容层` | 档位（决定结构冻结前置） |
| `order` | 整数 | 非空；同序位内按 `id` 全序（保证可复现） | 序位 |
| `prereq` | 列表 | 可为空；元素须为已存在的 `id` 或显式外部前置描述 | 前置 |
| `accept` | 字符串 | 非空；须为**二值可判定事实**（含条件／数量／顺序／路径） | 验收判据 |
| `status` | 枚举 | 见 §状态机 | 状态 |

**校验规则**

- V1：`source` 若为文书路径，须能 `Test-Path` 命中；若为库锚点，须为“库名＋主键”形式，禁指向临时目录。
- V2：`accept` 含“正常／良好／可接受／合理”等模糊词即**不合格**。
- V3：`ledger_map` 须能在 `.trae/specs/converge-all-remaining-tasks/tasks.md` 中命中唯一 Task/SubTask。
- V4：`tier ∈ {卷级, 章级}` 且 `status = 待施工` 时，`prereq` 须包含“内容层收编完成”或“终校完成”。
- V5：同一 `ledger_map` 不得出现在两个 `status = 在途` 的条目上（防双写）。

## E2. 来源（Source）

| 字段 | 约束 |
| ---- | ---- |
| `kind` | 枚举：`spec`（最近/次级）／`proposal`（建议书族）／`ledger`（总账文书）／`longline`（长线登记表）／`review_logs`（执行记录与备核） |
| `path` | 仓库相对路径；须真实存在 |
| `evidence` | 该源中被采信的实测证据（行号／主键／勾选状态） |
| `authority` | 枚举：`唯一任务书`／`需求裁定`／`对账入口`／`登记监控`／`交叉核验` |

**已核定来源清单**（见 `research.md` R2）：

| # | kind | path | authority |
| - | ---- | ---- | ---- |
| A | spec | `.trae/specs/converge-all-remaining-tasks/tasks.md` | 唯一任务书 |
| B | spec | `.trae/specs/finalize-refactor2026/tasks.md` | 交叉核验 |
| C | proposal | `08-核查报告与多轮复核/重构2026/124-…md`／`125-…md`／`92-…md §十一` | 需求裁定／对账入口 |
| D | review_logs | `08-核查报告与多轮复核/重构2026/review_logs/毕其功于一役-总任务账-20261009.md` 等 | 登记监控 |
| E | longline | `01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md`（机读块） | 登记监控 |

## E3. 载体（Carrier）

| 字段 | 约束 |
| ---- | ---- |
| `name` | 如 `content_source`／`assembly_output`／`changelog`／`outline_gates`／`browser_regression` |
| `path` | 具体路径 |
| `writable` | 布尔；`assembly_output`（`index.html`）**恒为 false**（禁手改产物） |
| `role` | `唯一内容源`／`装配产物`／`台账`／`验收闸面` |

**已核定载体**：

| name | path | writable | role |
| ---- | ---- | ---- | ---- |
| content_source | `08-核查报告与多轮复核/重构2026/data/outline.txt` | true | 唯一内容源 |
| assembly_output | `08-核查报告与多轮复核/重构2026/index.html` | **false** | 装配产物 |
| changelog | `changelog.duckdb` | true（经 update_log） | 台账 |
| gates | `script/`＋`00-…/01-规则/脚本与命令/` 下 audit 系 | 只读运行 | 验收闸面 |
| regression | 三套浏览器回归 | 只读运行 | 验收闸面 |

## E4. 落账记录（Ledger Entry）

| 字段 | 约束 |
| ---- | ---- |
| `batch_id` | 施工批标识 |
| `changelog_id` | `changelog.duckdb` 行 id（整数，单调递增） |
| `version` | 页面版本号（如 `3.0.11`），内容层变更须递增；零内容层变更不递增 |
| `prebak` | 备份文件名（须存在） |
| `gates_result` | 门禁＋三套回归结果（须 FAILED=0） |
| `reconciled_in` | 92 号文 §十一 行号／98 号文 §十一 |

## 关系

```text
Source (E2) 1 ──* Backlog Item (E1)
Backlog Item (E1) * ──1 Carrier (E3)          # 每条目指明所改载体
Backlog Item (E1) 1 ──* Ledger Entry (E4)     # 每条目可有多批落账（分批施工）
Backlog Item (E1) 1 ──1 ledger_map → 唯一任务书 Task/SubTask
```

## 状态机

```text
待施工 ──(主理人批准 / 批次开动)──> 在途 ──(收束铁律全绿＋落账)──> 已落账
   │                                  │
   │                                  └──(失败)──> 回滚至 待施工（prebak 恢复）
   ├──(核定判为无必要)──> 销号（留痕理由）
   └──(判为不属本线)────> 另案（标注归属线与前置）
```

**不变量**

- I1：任一 `ledger_map` 在**同一时刻**至多一个条目处于 `在途`（防双写）。
- I2：`已落账` 条目须具备 `changelog_id` 与 `prebak`。
- I3：`销号`／`另案` 条目须有 `reason` 或 `owner_line` 非空。
- I4：`tier = 卷级` 的条目在结构冻结后**不得**由 `待施工` 转为 `在途`。
