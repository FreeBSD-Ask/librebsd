# 03-叙事参照 索引

> 本文件夹原承载 `一刻哲学-第24章-应用于bsd史编纂.md` 叙事参照文件，该文件内容已合并入 `sacred_sources.duckdb`，原文件已按“删除安全规范”（预览→备份→确认→执行→复核）删除。

## 数据库索引

| 字段 | 值 |
|------|-----|
| 数据库 | `sacred_sources.duckdb` |
| 数据表 | `files` / `blocks` / `cross_references` |
| 释读分析 file_id | 52 |
| 释读分析逻辑路径 | `02-sacred源材料/01-一刻哲学/附录-第24章叙事参照.md` |
| 原文 file_id | 25 |
| 原文逻辑路径 | `02-sacred源材料/01-一刻哲学/第24章.md` |
| 原文标题 | 二十四、应用于 BSD 史编纂 |
| cross_references | file_id=52 → file_id=25（reference_type=db_ref） |

## 备份位置

- 备份目录: `script/_folder_db_logs/deletion_backup_narrative_ref/`
- 备份文件: `一刻哲学-第24章-应用于bsd史编纂.md`
- 备份 SHA-256: `d6d6bd0fc93985ab3cb9ce1ae0c0743e00c9a52290f403db75eb495ba9eefda6`

## 查询方式

```sql
-- 查询叙事参照全文
SELECT block_content FROM blocks WHERE file_id=52 ORDER BY block_index;

-- 查询叙事参照与原文的关联
SELECT * FROM cross_references WHERE source_file_id=52;

-- 全文检索（DuckDB 主存储层无 FTS5，用 LIKE 扫描）
SELECT block_content FROM blocks WHERE block_content LIKE '%少数与多数%' ORDER BY block_index;
```

## 说明

- 叙事参照内容已合并到 `sacred_sources.duckdb`，不再以独立物理文件形式存在于 `00-编纂规则与格式规范/03-叙事参照/`
- 原文件内容亦曾在 `06-正式书稿/00-前后辅文/01-前辅文/introduction.md` 中作为段落完整追加（该目录已因禁止编纂正文而移除，备份于 `script/_backup_20260804_06正文归档/`）
- 本索引文件作为导航入口，指向数据库中对应的记录
