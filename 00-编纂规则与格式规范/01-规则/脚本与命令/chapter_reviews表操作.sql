-- chapter_reviews 表操作 SQL
-- 数据库：04-现代研究文献/05-参考文献全文数据库/references_fulltext.db
-- 表：chapter_reviews
-- 规则引用位置：流程规则.md “新增文献自动检测规则” → “综述追加程序” 小节

-- 1. 追加新文献引用段落（自动入库，revised_by='auto_ingest'）
-- 注意：仅当 match_confidence ≥ 0.5 且对应章节在 chapter_reviews 表中存在记录时才执行追加
-- 追加后 revised_word_count 须在 300-5000 字范围内；超长（>5000 字）时不追加，日志标记“需人工精简”
UPDATE chapter_reviews
SET revised_review_text = revised_review_text || char(10) || char(10) || '<新增文献引用段落，含文献著录、与章节议题的关联说明（约100-300字）>',
    revised_word_count = <更新后的字数>,
    revised_at = datetime('now'),
    revised_by = 'auto_ingest'
WHERE chapter_id = <章节id>;

-- 2. 追加新文献引用段落（人工确认后，revised_by='manual'）
UPDATE chapter_reviews
SET revised_review_text = revised_review_text || char(10) || char(10) || '<人工确认后追加的新文献引用段落>',
    revised_word_count = <更新后的字数>,
    revised_at = datetime('now'),
    revised_by = 'manual'
WHERE chapter_id = <章节id>;

-- 3. 查询某章节的综述记录（含字数核验）
SELECT chapter_id, revised_word_count, revised_at, revised_by
FROM chapter_reviews
WHERE chapter_id = <章节id>;

-- 4. 查询字数超长（>5000 字）的综述记录（须人工精简）
SELECT chapter_id, revised_word_count, revised_at, revised_by
FROM chapter_reviews
WHERE revised_word_count > 5000;

-- 5. 查询字数不足（<300 字）的综述记录
SELECT chapter_id, revised_word_count, revised_at, revised_by
FROM chapter_reviews
WHERE revised_word_count < 300;

-- 6. 查询某章节是否已存在综述记录（用于判断是否可追加）
SELECT COUNT(*) AS review_count FROM chapter_reviews WHERE chapter_id = <章节id>;
