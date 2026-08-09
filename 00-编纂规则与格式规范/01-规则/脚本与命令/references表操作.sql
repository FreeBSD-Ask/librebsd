-- references 表操作 SQL
-- 数据库：04-现代研究文献/05-参考文献全文数据库/references_fulltext.db
-- 表：references
-- 规则引用位置：流程规则.md “新增文献自动检测规则”、“重复与错误文档清理规则” 小节

-- 1. SHA-256 精确去重查询（待入库文件 SHA-256 与既有记录比对）
SELECT id, title, author, year, file_path, sha256
FROM references
WHERE sha256 = '<待入库文件SHA-256>';

-- 2. 标题+作者+年份模糊去重查询（归一化标题 + 第一作者姓氏 + 年份三元组比对）
SELECT id, title, author, year, file_path
FROM references
WHERE year = '<年份>'
  AND author LIKE '<第一作者姓氏>%'
  AND REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(title, ' ', ''), ',', ''), '.', ''), ':', ''), '-', '') = '<归一化标题>';

-- 3. 新增文献入库 INSERT 示例（字段：title, author, year, format, file_path, filename, sha256, file_size 等）
INSERT INTO references (
  title, author, year, format, file_path, filename,
  sha256, file_size, status, created_at
) VALUES (
  '<题名>', '<作者>', '<年份>', '<格式>', '<文件路径>', '<文件名>',
  '<SHA-256>', <文件大小字节>, 'active', datetime('now')
);

-- 4. 标记错误文件（status='rejected'）
UPDATE references
SET status = 'rejected'
WHERE id = <错误文件id>;

-- 5. 标记已删除文件（status='deleted'，file_path 字段保留但追加 [DELETED YYYY-MM-DD] 前缀）
UPDATE references
SET status = 'deleted',
    file_path = '[DELETED ' || date('now') || '] ' || file_path
WHERE id = <被删除文件id>;

-- 6. 查询所有已删除条目（核验数据库一致性）
SELECT id, file_path, status FROM references WHERE status = 'deleted';
