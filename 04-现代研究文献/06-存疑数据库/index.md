# 存疑数据库

## 数据库概述

存疑数据库是《给我自由—一部 BSD 史》编纂项目中用于集中管理全部存疑记录的独立功能数据库。该数据库从 `references_fulltext.db` 迁移而来，承载过去与未来所有大纲存疑点、非存疑标记与复核历史，独立于参考文献全文数据库运行，遵循“一个数据库在一个文件夹内”的模块化分层设计规范。

- 数据库文件位置：**04-现代研究文献/06-存疑数据库/doubts_standalone.duckdb**
- 数据库类型：DuckDB（主存储层，自 SQLite 升格）
- Schema 版本：1.0.0
- 字符编码：UTF-8 无 BOM
- 换行符：LF
- 迁移来源：**04-现代研究文献/05-参考文献全文数据库/references_fulltext.db**（doubts_to_resolve 与 non_doubt_markers 两表已删除）

数据库遵循“单一来源真相”原则——所有存疑记录（迁移时 1707 条；截至 2026-09-28 共 **2496** 条）与未来新增记录均存放于本数据库，禁止在其他数据库（含 `references_fulltext.duckdb`）中重复存放存疑表。

## 4 张表结构说明

### 1. doubts_to_resolve（存疑主表）

存疑主表，每条记录对应一个从大纲审阅中抽取的存疑点，关联到具体大纲路径与行号，支持核查闭环。Schema 1.0.0 保留原 18 字段，新增 `source_db` 与 `migrated_at` 两字段标记迁移来源。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 主键（迁移自 references_fulltext.db，保留原 id） |
| outline_path | TEXT NOT NULL | 大纲路径 |
| line_number | INTEGER | 行号 |
| doubt_text | TEXT | 存疑描述 |
| doubt_context | TEXT | 存疑上下文 |
| doubt_type | TEXT | 存疑类型（date/authorship/attribution/number/citation/contradiction 等） |
| doubt_keywords | TEXT | 关键词（JSON 数组） |
| resolution_status | TEXT NOT NULL | 处理状态（resolved/open/unresolvable） |
| resolution_evidence | TEXT | 解决证据（JSON 数组，含 reference_id、block_id、quote、confidence 等字段） |
| resolution_summary | TEXT | 解决摘要 |
| resolved_by | TEXT | 解决者 |
| resolved_at | TEXT | 解决时间 |
| outline_revision_applied | INTEGER | 是否已应用到大纲（0/1） |
| outline_revision_diff | TEXT | 大纲修订 diff |
| outline_path_old | TEXT | 旧大纲路径（章号重构前的原始路径） |
| review_round | INTEGER | 复核轮次（0=未复核，1=第一轮，2=第二轮） |
| last_reviewed_at | TEXT | 最近复核时间 |
| reviewer_model | TEXT | 复核模型标识 |
| source_db | TEXT DEFAULT ‘references_fulltext’ | 迁移来源数据库（标记历史数据来源） |
| migrated_at | TEXT | 迁移时间戳 |

### 2. non_doubt_markers（非存疑标记表）

记录大纲中存在但不符合存疑登记条件的标记（如“考据完成”“已核实”等），避免误登记为存疑。Schema 1.0.0 保留原 7 字段，新增 `source_db` 与 `migrated_at` 两字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 主键（迁移自 references_fulltext.db，保留原 id） |
| outline_path | TEXT NOT NULL | 大纲路径 |
| line_number | INTEGER | 行号 |
| marker_text | TEXT | 标记原文 |
| marker_type | TEXT | 标记类型（methodology/descriptive/citation_reference/other_non_doubt） |
| context | TEXT | 上下文 |
| recorded_at | TEXT | 记录时间 |
| source_db | TEXT DEFAULT ‘references_fulltext’ | 迁移来源数据库 |
| migrated_at | TEXT | 迁移时间戳 |

### 3. doubt_review_log（复核历史表）

复核历史表，用于追踪未来对存疑记录的复核操作。Schema 1.0.0 新增，原 `references_fulltext.db` 未含此表。每次对存疑记录执行复核操作时须写入一条记录。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT | 主键自增 |
| doubt_id | INTEGER NOT NULL | 关联 doubts_to_resolve.id |
| review_round | INTEGER NOT NULL | 复核轮次 |
| reviewer_model | TEXT | 复核模型标识 |
| review_action | TEXT | 复核动作（verify/promote/demote/close/reopen） |
| review_notes | TEXT | 复核备注 |
| reviewed_at | TEXT NOT NULL | 复核时间 |
| FOREIGN KEY | - | doubt_id 引用 doubts_to_resolve(id) ON DELETE CASCADE |

### 4. schema_meta（数据库元数据表）

数据库元数据表，采用 key/value 结构存储 Schema 版本与迁移元数据。

| 字段 | 类型 | 说明 |
|------|------|------|
| key | TEXT PRIMARY KEY | 元数据键 |
| value | TEXT | 元数据值 |

#### 当前 schema_meta 键值对

| key | value |
|-----|-------|
| schema_version | 1.0.0 |
| schema_created_at | 2026-08-01 13:38:53 |
| last_migrated_at | 2026-08-01 13:38:53 |
| source_db | references_fulltext.db |
| source_path | 04-现代研究文献/05-参考文献全文数据库/references_fulltext.db |
| description | 存疑数据库：集中存放过去与未来所有存疑记录，独立于 references_fulltext.db |
| tables | doubts_to_resolve, non_doubt_markers, doubt_review_log, schema_meta |
| journal_mode | WAL |

## 12 个索引说明

数据库为 4 张表共建立 12 个索引，覆盖以下查询场景：

- **doubts_to_resolve 表**（7 个索引）：
  - `idx_doubts_outline_path`：按大纲路径检索
  - `idx_doubts_resolution_status`：按处理状态筛选
  - `idx_doubts_doubt_type`：按存疑类型筛选
  - `idx_doubts_line_number`：按行号定位
  - `idx_doubts_review_round`：按复核轮次筛选
  - `idx_doubts_status_type`：(resolution_status, doubt_type) 复合索引
  - `idx_doubts_source_db`：按迁移来源筛选
- **non_doubt_markers 表**（3 个索引）：
  - `idx_non_doubt_markers_outline_path`：按大纲路径检索
  - `idx_non_doubt_markers_marker_type`：按标记类型筛选
  - `idx_non_doubt_markers_source_db`：按迁移来源筛选
- **doubt_review_log 表**（2 个索引）：
  - `idx_doubt_review_log_doubt_id`：按存疑 ID 检索复核历史
  - `idx_doubt_review_log_review_round`：按复核轮次筛选

全部索引使用 `IF NOT EXISTS` 保证幂等。

## 当前状态快照（截至 2026-09-28，第八轮：裁定落地后）

> 直接查询库内实数；与下方 2026-08-01 迁移时快照**不可混用**。

| resolution_status | 数量 | 说明 |
|-------------------|------|------|
| resolved | 2415 | 已解决存疑（含已应用大纲修订与未应用两类；后者全为 `[skipped] 行内无可明确替换的存疑标记` 哨兵，无隐藏改动池）。其中 **11 条**为 2026-09-28 第八轮“裁定落地”关条（`resolved_by='主理人批准-20260928'`） |
| open | 58 | 未解决存疑：第七轮入库后仍开 44 条＋第六轮遗留 14 条（含 **10 条可裁／4 条须取证**） |
| unresolvable | 23 | 无法解决存疑（穷尽考据仍不能确证） |
| 合计 | 2496 | 迁移时 1707 条 ＋ 后续核验新增与调整 |

- 复核轮次分布：`8` 69／`5` 10／`4` 7／`3` 14／`2` 289／`1` 1659／`0` 3／NULL 445；`doubt_review_log` 共 **2920** 条。
- 第七轮（2026-09-28 23:34）：55 条目录层处置判定入库（`reviewer_model='dir_review_92_20260928'`，日志 3485–3539）。
- 第八轮（2026-09-28 23:50）：69 条四层映射对齐（`MAP_ALIGN_20260928`）＋11 条关条（`close`），日志 **3540–3619**。记录见 `08-核查报告与多轮复核/重构2026/90-释疑内容入库入纲写回记录.md` §九／§十。
- 配套件（同目录）：`存疑R-O-磁盘-现行四层映射表.md`（治理映射表）、`存疑四层映射-20260928.csv`、`存疑写回delta-20260928.csv`（机器可读变更凭据）、`存疑卷级聚合台账.md`（卷级聚合）。
- 释疑结论已同步进 05 层：**30 个** `05-卷册大纲/**/概述.md` 追加“释疑结论同步”块（13 条有 R 锚点的条目；无锚点的 52 条按纪律不猜挂）。见 90 号文 §十一。
- ⚠️ 库内 `outline_path like '05-卷册大纲/%'` 的 1921 条路径中 **1917 条已悬空**（磁盘镜像为 21 卷／361 章，与现行 43 卷／412 章不同代）——库—盘自动核对前须先做路径重建，详见 `review_logs/磁盘层存疑标记抽样-60-20260928.md`。

## 存疑状态分布（截至 2026-08-01 迁移时；**历史快照，口径已过时**）

| resolution_status | 数量 | 说明 |
|-------------------|------|------|
| resolved | 1618 | 已解决存疑（含已应用大纲修订与未应用两类） |
| open | 70 | 未解决存疑（Task 9 新登记，待后续考据） |
| unresolvable | 19 | 无法解决存疑（含 methodology、historical_gap、literature_mismatch、privacy 四类） |
| 合计 | 1707 | 迁移自 references_fulltext.db |

## 使用规范

### 新增存疑记录

发现新存疑时须按以下流程登记：

1. 在 `doubts_to_resolve` 表插入记录，必填 `outline_path`、`line_number`、`doubt_text`、`doubt_type`、`resolution_status`（默认 `open`）。
2. `doubt_keywords` 字段填写 JSON 数组格式的关键词清单，便于后续检索。
3. `source_db` 字段对新存疑填 `NULL` 或 `direct_entry`（非迁移数据标记）。
4. `migrated_at` 字段对新存疑填 `NULL`（仅迁移数据有值）。
5. 新增后须在 `doubt_review_log` 表写入首轮复核记录（`review_round=1`，`review_action='verify'`）。

### 复核存疑记录

对既有存疑执行复核时须按以下流程：

1. 按 0 信任原则 + 三次复查流程执行考据。
2. 更新 `doubts_to_resolve` 表的 `resolution_status`、`resolution_evidence`、`resolution_summary`、`resolved_by`、`resolved_at`、`review_round`、`last_reviewed_at`、`reviewer_model` 字段。
3. 在 `doubt_review_log` 表写入一条复核记录，含 `review_action`（verify/promote/demote/close/reopen）与 `review_notes`。
4. 若考据后确证，更新大纲对应位置的存疑标记为 `[考据完成：YYYY-MM-DD <结论简述>]` 格式。
5. 若穷尽考据仍无法确证，保留 `[存疑脚注]` 标注，并将 `resolution_status` 标为 `unresolvable`。

### 查询示例

```sql
-- 检索未解决存疑点
SELECT id, outline_path, line_number, doubt_text, doubt_type
FROM doubts_to_resolve
WHERE resolution_status = 'open'
ORDER BY outline_path, line_number;

-- 按大纲路径检索存疑
SELECT id, line_number, doubt_text, resolution_status
FROM doubts_to_resolve
WHERE outline_path LIKE '05-卷册大纲/第01卷-%'
ORDER BY line_number;

-- 按存疑类型统计
SELECT doubt_type, resolution_status, COUNT(*) AS cnt
FROM doubts_to_resolve
GROUP BY doubt_type, resolution_status
ORDER BY doubt_type, resolution_status;

-- 检索某存疑的复核历史
SELECT drl.review_round, drl.review_action, drl.review_notes, drl.reviewed_at
FROM doubt_review_log drl
WHERE drl.doubt_id = 1
ORDER BY drl.review_round;

-- 检索低置信度已解决存疑（需重新考据）
SELECT id, outline_path, doubt_text, resolution_evidence
FROM doubts_to_resolve
WHERE resolution_status = 'resolved'
  AND review_round < 2
ORDER BY id;

-- 检索非存疑标记（避免误登记）
SELECT outline_path, line_number, marker_text, marker_type
FROM non_doubt_markers
WHERE marker_type = 'methodology'
ORDER BY outline_path;
```

## 迁移历史

### 2026-08-01 从 references_fulltext.db 迁移

- **迁移时间**：2026-08-01 13:38:53
- **源数据库**：04-现代研究文献/05-参考文献全文数据库/references_fulltext.db
- **迁移表**：doubts_to_resolve（1707 行）、non_doubt_markers（1292 行）
- **源数据库备份**：references_fulltext.db.bak_before_doubt_migration
- **源表清理**：迁移校验通过后已从源数据库删除两表与 8 个相关索引
- **源数据库剩余表数**：22（原 24 表）
- **依据 spec**：doubt-zero-trust-review-2026-08-01
- **依据规则**：
  - 流程规则.md“模块化分层设计规范（一库一文件夹）”
  - 流程规则.md“源文件不可变性”（数据库表可修改，源 .md 文件不可修改）
  - 考据规则.md“禁止为消除存疑而强行采信”
  - 考据规则.md“0 信任原则”
- **迁移脚本**：script/_doubt_migrate_to_standalone.py
- **校验结果**：源/目标行数一致（1707/1707、1292/1292）、状态分布一致（resolved 1618 + open 70 + unresolvable 19）

## 关联文档

- 考据规则：[../../00-编纂规则与格式规范/01-规则/考据规则.md](../../00-编纂规则与格式规范/01-规则/考据规则.md)
- 流程规则：[../../00-编纂规则与格式规范/01-规则/流程规则.md](../../00-编纂规则与格式规范/01-规则/流程规则.md)
- 迁移脚本：[../../../script/_doubt_migrate_to_standalone.py](../../../script/_doubt_migrate_to_standalone.py)
- 源数据库文档：[../05-参考文献全文数据库/index.md](../05-参考文献全文数据库/index.md)
- Spec 文件：[../../../.trae/specs/doubt-zero-trust-review-2026-08-01/](../../../.trae/specs/doubt-zero-trust-review-2026-08-01/)
