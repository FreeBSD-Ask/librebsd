# Changelog 数据库

本目录存储 FreeBSD 历史书编纂项目的变更记录数据库。

- **数据库文件**：`changelog.db`（SQLite 3，1.77 MB）
- **数据库路径**：`01-项目管理/00-变更记录/changelog.db`
- **迁移日期**：2026-07-21
- **原格式**：纯文本 Markdown 文件（`changelog/2026-07/` 下按年月→日→条目三级嵌套存储，共 91 个 .md 文件、622 个条目），已全部迁移至 SQLite 并删除原文件
- **最近更新**：2026-08-17（id=915，新增 24 号文学术方法论锚定与外部谱系增补；修正 16/03/05 号文口径；登记一致性/学术性复核结论）

## 当前状态（截至 2026-08-17）

| 项目 | 数值 |
| --- | --- |
| 数据库大小 | 1.77 MB |
| 表数 | 3 |
| 显式索引数 | 0（仅 `entries` 表主键自动索引） |
| `entries` 表行数 | 888 |
| id 范围 | 1 - 915（含 27 处空号） |
| date 范围 | 2026-07-16 至 2026-08-17 |
| sqlite_stat1 | 已收集统计信息（1 行） |

### 最近 7 日条目分布

| 日期 | 条目数 |
| --- | --- |
| 2026-08-17 | 5 |
| 2026-08-16 | 14 |
| 2026-08-15 | 3 |
| 2026-08-14 | 8 |
| 2026-08-13 | 6 |
| 2026-08-12 | 4 |
| 2026-08-11 | 2 |

## 表结构

```sql
CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,           -- 日期，格式 YYYY-MM-DD
    entry_order INTEGER NOT NULL DEFAULT 0,  -- 同日内条目序号
    summary TEXT NOT NULL,        -- 条目摘要（内容前 80 字符）
    content TEXT NOT NULL,        -- 条目完整内容
    created_at TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);
```

字段列表：

| cid | name | type | notnull | pk | default |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | 0 | 1 | None |
| 1 | date | TEXT | 1 | 0 | None |
| 2 | entry_order | INTEGER | 1 | 0 | 0 |
| 3 | summary | TEXT | 1 | 0 | None |
| 4 | content | TEXT | 1 | 0 | None |
| 5 | created_at | TEXT | 1 | 0 | datetime('now','localtime') |

## 索引

`entries` 表仅依赖主键自动索引（`sqlite_autoindex_entries_1`，字段 `id`），无显式 INDEX。

如未来按 `date` 或 `summary` 高频查询，可考虑追加：

```sql
-- 可选：按日期查询的覆盖索引
CREATE INDEX idx_entries_date ON entries(date, entry_order);

-- 可选：按摘要前缀查询
CREATE INDEX idx_entries_summary ON entries(summary);
```

当前规模（888 条）下全表扫描耗时可忽略，暂无需追加索引。

## 基本查询示例

```sql
-- 查看某日全部变更
SELECT id, entry_order, summary FROM entries WHERE date = '2026-07-21' ORDER BY entry_order;

-- 全文搜索
SELECT id, date, summary FROM entries WHERE content LIKE '%关键词%';

-- 按日期统计条目数
SELECT date, COUNT(*) FROM entries GROUP BY date ORDER BY date;

-- 查看最新 10 条
SELECT id, date, summary FROM entries ORDER BY id DESC LIMIT 10;
```

## Python 访问示例

```python
import sqlite3
conn = sqlite3.connect("01-项目管理/00-变更记录/changelog.db")
cur = conn.execute("SELECT date, summary FROM entries WHERE date = '2026-07-22' ORDER BY entry_order")
for row in cur.fetchall():
    print(row[0], row[1])
conn.close()
```

## 去重规则

每次向数据库追加新条目时须触发去重检查，以 SQL 查询替代人工遍历：

```sql
-- 查找疑似重复条目（相同日期、摘要前 60 字符相同）
SELECT a.id, b.id, a.date, a.summary
FROM entries a JOIN entries b ON a.date = b.date AND a.id < b.id
WHERE SUBSTR(a.summary, 1, 60) = SUBSTR(b.summary, 1, 60);
```

2026-07-24 Task 18 已执行一次去重，删除 26 条内容完全相同的重复条目（15 组），id 范围内由此产生空号。

## 索引维护流程

每次大量追加条目后建议执行：

```sql
-- 更新统计信息（耗时 < 0.01s）
ANALYZE;
```

由于 `entries` 表仅依赖主键自动索引，无需 REINDEX。如未来添加显式索引，可在追加大量数据后用 `REINDEX <索引名>` 重建。

## 迁移脚本

迁移脚本存放于 `script/migrate_changelog_to_db.py`。

## 文件编码与标点

- 数据库文件编码：SQLite 默认 UTF-8
- 本说明文件编码：UTF-8 无 BOM，LF 换行符
- 标点规则：禁用中文方头括号「」与白双引号『』，使用中文弯引号“”或‘’
