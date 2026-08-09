-- chapter_matches 表操作 SQL
-- 数据库：04-现代研究文献/05-参考文献全文数据库/references_fulltext.db
-- 表：chapter_matches
-- 规则引用位置：流程规则.md “新增文献自动检测规则” → “章节匹配置信度阈值” 小节

-- 1. 高置信度匹配写入（match_confidence ≥ 0.7，关键词重合 ≥ 2 项）
INSERT INTO chapter_matches (
  reference_id, primary_chapter, match_confidence, match_reason, created_at
) VALUES (
  <文献id>, <主匹配章号>, <置信度如0.85>, '<匹配命中的关键词清单>', datetime('now')
);

-- 2. 中置信度匹配写入（0.5 ≤ match_confidence < 0.7，关键词重合 1 项，须人工复核）
INSERT INTO chapter_matches (
  reference_id, primary_chapter, match_confidence, match_reason, created_at
) VALUES (
  <文献id>, <主匹配章号>, <置信度如0.6>, '<匹配命中的关键词清单>', datetime('now')
);

-- 3. 低置信度匹配写入（match_confidence < 0.5，primary_chapter=0，须人工确认）
INSERT INTO chapter_matches (
  reference_id, primary_chapter, match_confidence, match_reason, created_at
) VALUES (
  <文献id>, 0, <置信度如0.3>, '<匹配命中的关键词清单>', datetime('now')
);

-- 4. 人工确认后更新章节归属与匹配信息
UPDATE chapter_matches
SET primary_chapter = <人工确认章号>,
    match_confidence = <人工确认后置信度>,
    match_reason = '<人工确认后匹配依据>'
WHERE reference_id = <文献id> AND primary_chapter = 0;

-- 5. 查询所有需人工复核的中置信度匹配
SELECT * FROM chapter_matches WHERE match_confidence >= 0.5 AND match_confidence < 0.7;

-- 6. 查询所有需人工确认的低置信度匹配
SELECT * FROM chapter_matches WHERE match_confidence < 0.5;

-- 7. 查询某章节的所有匹配文献
SELECT cm.reference_id, r.title, r.author, r.year, cm.match_confidence, cm.match_reason
FROM chapter_matches cm
JOIN references r ON cm.reference_id = r.id
WHERE cm.primary_chapter = <章号>
ORDER BY cm.match_confidence DESC;
