-- 文件夹级数据库交叉引用查询模板
-- 用途：用于查询各文件夹数据库 cross_references 表中的引用关系
-- Schema 版本：1.0
-- 创建日期：2026-07-31
-- 关联 spec：convert-folders-to-databases-2026-07-31
-- 说明：本文件为查询模板参考，非自动执行脚本；使用时须替换 :db_name 等参数占位符
--
-- 标准 cross_references 表 Schema（本文件所有查询基于此结构）：
--   source_file_id      INTEGER  - 源文件 ID（关联 files 表 id）
--   source_block_id     INTEGER  - 源块 ID（关联 blocks 表 id，可为 NULL）
--   reference_type      TEXT     - 引用类型：wikilink/markdown_link/footnote/citation/chapter_ref/spec_ref/db_ref/external_url
--   reference_text      TEXT     - 引用原文（如 [[第5章]]、[fn:1] 等）
--   target_path         TEXT     - 目标路径（章节路径、文件路径或外部 URL）
--   target_db           TEXT     - 目标数据库名（references_fulltext/sacred_sources/...）
--   target_record_id    INTEGER  - 目标记录 ID（可为 NULL）
--   target_anchor       TEXT     - 目标锚点（如章节小节锚点，可为 NULL）
--   resolution_status   TEXT     - 解析状态：resolved/broken/external/pending
--   reference_context   TEXT     - 引用上下文片段（前后若干字符）
--   resolved_at         TEXT     - 解析时间戳（ISO8601，可为 NULL）
--
-- 关联表：
--   files(id, file_path, ...)         - 文件元数据表
--   blocks(id, file_id, block_content, ...) - 块级内容表


-- ============================================================
-- Section 1: 按引用类型统计 (By reference_type)
-- 统计 cross_references 表中各 reference_type 的数量与占比
-- 覆盖类型：wikilink, markdown_link, footnote, citation,
--           chapter_ref, spec_ref, db_ref, external_url
-- ============================================================

-- 1.1 各引用类型数量与百分比统计
SELECT
    reference_type,
    COUNT(*) AS ref_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM cross_references), 2) AS percentage
FROM cross_references
GROUP BY reference_type
ORDER BY ref_count DESC;

-- 示例用法：
--   sqlite3 :db_name -c "SELECT reference_type, COUNT(*) ... "
--   参数 :db_name 替换为具体文件夹数据库路径，如 03-原始史料库/01-代码仓库史料/db/freebsd.db


-- ============================================================
-- Section 2: 按目标数据库统计 (By target_db)
-- 统计 cross_references 表中各 target_db 的引用数量
-- 覆盖目标库：references_fulltext, sacred_sources, original_sources,
--             research_notes, fact_checks, review_reports,
--             cross_indexes, metadata_interfaces
-- ============================================================

-- 2.1 各目标数据库引用数量统计
SELECT
    target_db,
    COUNT(*) AS ref_count
FROM cross_references
WHERE target_db IS NOT NULL
GROUP BY target_db
ORDER BY ref_count DESC;

-- 2.2 指定目标数据库引用数量（参数化）
SELECT
    target_db,
    COUNT(*) AS ref_count
FROM cross_references
WHERE target_db = :target_db_name
GROUP BY target_db;

-- 示例用法：
--   参数 :target_db_name 替换为 ‘sacred_sources’ 或 ‘references_fulltext’ 等


-- ============================================================
-- Section 3: 按解析状态统计 (By resolution_status)
-- 统计 cross_references 表中各 resolution_status 的数量与占比
-- 覆盖状态：resolved, broken, external, pending
-- ============================================================

-- 3.1 各解析状态数量与百分比统计
SELECT
    resolution_status,
    COUNT(*) AS status_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM cross_references), 2) AS percentage
FROM cross_references
GROUP BY resolution_status
ORDER BY status_count DESC;

-- 3.2 单一状态数量查询（参数化）
SELECT
    resolution_status,
    COUNT(*) AS status_count
FROM cross_references
WHERE resolution_status = :status_name
GROUP BY resolution_status;

-- 示例用法：
--   参数 :status_name 替换为 ‘broken’ 或 ‘pending’ 等状态值


-- ============================================================
-- Section 4: 失效链接查询 (Broken links)
-- 查询所有 resolution_status='broken' 的交叉引用
-- 关联 files 表获取源文件路径
-- ============================================================

-- 4.1 失效链接清单（含源文件路径、引用原文、目标路径、上下文）
SELECT
    f.file_path       AS source_file_path,
    cr.source_block_id,
    cr.reference_type,
    cr.reference_text,
    cr.target_path,
    cr.target_db,
    cr.reference_context
FROM cross_references cr
JOIN files f ON cr.source_file_id = f.id
WHERE cr.resolution_status = 'broken'
ORDER BY f.file_path;

-- 示例用法：
--   sqlite3 :db_name < 此段 SQL
--   参数 :db_name 替换为待检查的文件夹数据库路径


-- ============================================================
-- Section 5: 跨库引用反查 (Cross-database reverse lookup)
-- 反查所有指向指定目标数据库的引用记录
-- 参数：:target_db_name
-- ============================================================

-- 5.1 反查指向指定目标数据库的所有引用（含源文件路径）
SELECT
    f.file_path       AS source_file_path,
    cr.reference_type,
    cr.reference_text,
    cr.target_path,
    cr.target_record_id,
    cr.target_anchor,
    cr.resolution_status,
    cr.reference_context
FROM cross_references cr
JOIN files f ON cr.source_file_id = f.id
WHERE cr.target_db = :target_db_name
ORDER BY f.file_path;

-- 5.2 反查并按解析状态分组统计
SELECT
    cr.resolution_status,
    COUNT(*) AS ref_count
FROM cross_references cr
WHERE cr.target_db = :target_db_name
GROUP BY cr.resolution_status
ORDER BY ref_count DESC;

-- 示例用法：
--   参数 :target_db_name 替换为 ‘original_sources’ 或 ‘fact_checks’ 等


-- ============================================================
-- Section 6: 文件级引用统计 (File-level reference statistics)
-- 统计每个源文件的引用数量、已解析数、失效数
-- 按总引用数降序，取前 50（LIMIT 可参数化）
-- ============================================================

-- 6.1 文件级引用统计（Top N）
SELECT
    f.file_path AS source_file_path,
    COUNT(cr.id) AS total_references,
    SUM(CASE WHEN cr.resolution_status = 'resolved' THEN 1 ELSE 0 END) AS resolved_count,
    SUM(CASE WHEN cr.resolution_status = 'broken' THEN 1 ELSE 0 END) AS broken_count,
    SUM(CASE WHEN cr.resolution_status = 'pending' THEN 1 ELSE 0 END) AS pending_count,
    SUM(CASE WHEN cr.resolution_status = 'external' THEN 1 ELSE 0 END) AS external_count
FROM files f
LEFT JOIN cross_references cr ON cr.source_file_id = f.id
GROUP BY f.id, f.file_path
HAVING COUNT(cr.id) > 0
ORDER BY total_references DESC
LIMIT :limit_count;

-- 示例用法：
--   参数 :limit_count 替换为 50（默认）或其他数值
--   sqlite3 :db_name -cmd ".mode column" < 此段 SQL


-- ============================================================
-- Section 7: 块级引用查询 (Block-level reference query)
-- 查询指定源块发出的所有引用
-- 参数：:block_id
-- 关联 blocks 表获取块内容片段
-- ============================================================

-- 7.1 指定块的所有引用（含块内容片段）
SELECT
    b.id              AS block_id,
    SUBSTR(b.block_content, 1, 200) AS block_content_snippet,
    cr.reference_type,
    cr.reference_text,
    cr.target_path,
    cr.target_db,
    cr.target_anchor,
    cr.resolution_status,
    cr.reference_context
FROM cross_references cr
JOIN blocks b ON cr.source_block_id = b.id
WHERE cr.source_block_id = :block_id
ORDER BY cr.id;

-- 7.2 指定块引用数量与状态汇总
SELECT
    COUNT(*) AS total_refs,
    SUM(CASE WHEN cr.resolution_status = 'resolved' THEN 1 ELSE 0 END) AS resolved_count,
    SUM(CASE WHEN cr.resolution_status = 'broken' THEN 1 ELSE 0 END) AS broken_count,
    SUM(CASE WHEN cr.resolution_status = 'pending' THEN 1 ELSE 0 END) AS pending_count
FROM cross_references cr
WHERE cr.source_block_id = :block_id;

-- 示例用法：
--   参数 :block_id 替换为具体块 ID（整数）


-- ============================================================
-- Section 8: 章节引用汇总 (Chapter reference summary)
-- 查询所有 reference_type='chapter_ref' 的引用
-- 按 target_path（章节）分组统计被引用次数
-- ============================================================

-- 8.1 各章节被引用次数汇总（降序）
SELECT
    cr.target_path   AS chapter_path,
    COUNT(*)         AS ref_count
FROM cross_references cr
WHERE cr.reference_type = 'chapter_ref'
GROUP BY cr.target_path
ORDER BY ref_count DESC;

-- 8.2 指定章节的所有引用来源（参数化）
SELECT
    f.file_path       AS source_file_path,
    cr.reference_text,
    cr.target_anchor,
    cr.resolution_status,
    cr.reference_context
FROM cross_references cr
JOIN files f ON cr.source_file_id = f.id
WHERE cr.reference_type = 'chapter_ref'
  AND cr.target_path = :chapter_path
ORDER BY f.file_path;

-- 示例用法：
--   参数 :chapter_path 替换为章节路径，如 ‘05-卷册大纲/第01卷-unix的起源/第01章-...’


-- ============================================================
-- Section 9: 数据库引用密度 (Database reference density)
-- 计算各数据库的引用密度（每文件平均引用数）
-- 参数：:db_name（单库密度查询）
-- ============================================================

-- 9.1 单库引用密度查询（参数化）
SELECT
    (SELECT COUNT(*) FROM files) AS total_files,
    (SELECT COUNT(*) FROM cross_references) AS total_references,
    ROUND(
        CAST((SELECT COUNT(*) FROM cross_references) AS REAL)
        / NULLIF((SELECT COUNT(*) FROM files), 0),
        4
    ) AS refs_per_file_ratio
FROM (SELECT 1) AS one;

-- 9.2 单库按引用类型的密度分布
SELECT
    cr.reference_type,
    COUNT(*) AS ref_count,
    ROUND(COUNT(*) * 1.0 / NULLIF((SELECT COUNT(*) FROM files), 0), 4) AS refs_per_file
FROM cross_references cr
GROUP BY cr.reference_type
ORDER BY ref_count DESC;

-- 示例用法：
--   参数 :db_name 替换为待计算密度的文件夹数据库路径
--   密度比值 = 总引用数 / 总文件数；NULLIF 防止除零


-- ============================================================
-- Section 10: 未解析引用清单 (Unresolved references)
-- 查询所有 resolution_status='pending' 的引用
-- 按源文件 ID 排序，便于逐文件处理
-- ============================================================

-- 10.1 未解析引用清单（含源文件路径）
SELECT
    f.file_path       AS source_file_path,
    cr.source_file_id,
    cr.source_block_id,
    cr.reference_type,
    cr.reference_text,
    cr.target_path,
    cr.target_db,
    cr.reference_context
FROM cross_references cr
JOIN files f ON cr.source_file_id = f.id
WHERE cr.resolution_status = 'pending'
ORDER BY cr.source_file_id;

-- 10.2 未解析引用按引用类型分组统计
SELECT
    cr.reference_type,
    COUNT(*) AS pending_count
FROM cross_references cr
WHERE cr.resolution_status = 'pending'
GROUP BY cr.reference_type
ORDER BY pending_count DESC;

-- 示例用法：
--   sqlite3 :db_name < 此段 SQL
--   参数 :db_name 替换为待排查的文件夹数据库路径
