# Changelog 数据库

本目录存储 FreeBSD 历史书编纂项目的变更记录数据库。

- **数据库文件**：`changelog.duckdb`（DuckDB，主存储层）
- **数据库路径**：`01-项目管理/00-变更记录/changelog.duckdb`
- **原格式**：纯文本 Markdown 文件（`changelog/2026-07/` 下按年月→日→条目三级嵌套存储），先迁移至 SQLite（`changelog.db`），后随全库 DuckDB 化升格为 `changelog.duckdb`，原 SQLite 库以 `ARCHIVE_FINAL_*.db.gz` 归档于 `12-数据库备份/changelog/`

本文件为数据库使用说明。条目规模、id 范围、日期范围等随编纂持续变动，不在此固化快照计数；需要实时数值时按下文查询示例直接对库执行。

## 表结构

`entries` 单表，字段如下：

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| id | BIGINT | 条目主键（应用层以 `max(id)+1` 生成，DuckDB 无 AUTOINCREMENT 约束） |
| date | VARCHAR | 日期，格式 YYYY-MM-DD |
| entry_order | BIGINT | 同日内条目序号 |
| summary | VARCHAR | 条目摘要 |
| content | VARCHAR | 条目完整内容 |
| created_at | VARCHAR | 写入时间戳（应用层 `datetime.now().isoformat()` 填充） |

建表语句：

```sql
CREATE TABLE entries(
    id BIGINT,
    date VARCHAR,
    entry_order BIGINT,
    summary VARCHAR,
    "content" VARCHAR,
    created_at VARCHAR
);
```

## 索引

`entries` 表无显式索引。DuckDB 为列式存储，当前规模下按 `date`/`summary` 的过滤与全文 `LIKE` 扫描性能可接受，暂无需追加索引。

## 基本查询示例

```sql
-- 查看某日全部变更
SELECT id, entry_order, summary FROM entries WHERE date = '2026-09-08' ORDER BY entry_order;

-- 全文搜索
SELECT id, date, summary FROM entries WHERE content LIKE '%关键词%';

-- 按日期统计条目数
SELECT date, COUNT(*) FROM entries GROUP BY date ORDER BY date;

-- 查看最新 10 条
SELECT id, date, summary FROM entries ORDER BY id DESC LIMIT 10;
```

## Python 访问示例

```python
import duckdb

con = duckdb.connect("01-项目管理/00-变更记录/changelog.duckdb")
for row in con.execute(
    "SELECT date, summary FROM entries WHERE date = '2026-09-08' ORDER BY entry_order"
).fetchall():
    print(row[0], row[1])
con.close()
```

追加条目（含主键生成与同日序号）：

```python
import duckdb
from datetime import datetime

con = duckdb.connect("01-项目管理/00-变更记录/changelog.duckdb")
next_id = con.execute("SELECT max(id) + 1 FROM entries").fetchone()[0]
order = con.execute(
    "SELECT coalesce(max(entry_order), 0) + 1 FROM entries WHERE date = ?", [date_str]
).fetchone()[0]
con.execute(
    "INSERT INTO entries (id, date, entry_order, summary, content, created_at) "
    "VALUES (?, ?, ?, ?, ?, ?)",
    [next_id, date_str, order, summary, content, datetime.now().isoformat(timespec="seconds")],
)
con.close()
```

## 去重规则

每次向数据库追加新条目时须触发去重检查，以 SQL 查询替代人工遍历：

```sql
-- 查找疑似重复条目（相同日期、摘要前 60 字符相同）
SELECT a.id, b.id, a.date, a.summary
FROM entries a JOIN entries b ON a.date = b.date AND a.id < b.id
WHERE SUBSTR(a.summary, 1, 60) = SUBSTR(b.summary, 1, 60);
```

去重操作规范详见 [00-编纂规则与格式规范/01-规则/流程规则.md](../../00-编纂规则与格式规范/01-规则/流程规则.md) “changelog 去重规则”小节。

## 索引维护流程

大量追加条目后可更新查询统计信息：

```sql
ANALYZE;
```

## 文件编码与标点

- 数据库文件编码：DuckDB 默认 UTF-8
- 本说明文件编码：UTF-8 无 BOM，LF 换行符
- 标点规则：禁用中文方头括号（U+300C/U+300D）与白双引号（U+300E/U+300F），使用中文弯引号“”或‘’
