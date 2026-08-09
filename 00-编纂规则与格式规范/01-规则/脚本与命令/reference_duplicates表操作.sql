-- reference_duplicates 表操作 SQL
-- 数据库：04-现代研究文献/05-参考文献全文数据库/references_fulltext.db
-- 表：reference_duplicates
-- 规则引用位置：流程规则.md “新增文献自动检测规则”、“重复与错误文档清理规则” 小节

-- 1. 写入 SHA-256 精确重复关系（INSERT OR IGNORE 避免唯一约束冲突）
INSERT OR IGNORE INTO reference_duplicates (
  primary_reference_id, duplicate_reference_id, duplicate_type, created_at
) VALUES (
  <主副本id>, <副本id>, 'exact', datetime('now')
);

-- 2. 写入标题+作者+年份模糊重复关系
INSERT OR IGNORE INTO reference_duplicates (
  primary_reference_id, duplicate_reference_id, duplicate_type, created_at
) VALUES (
  <主副本id>, <副本id>, 'fuzzy', datetime('now')
);

-- 3. 写入文件损坏标记
INSERT OR IGNORE INTO reference_duplicates (
  primary_reference_id, duplicate_reference_id, duplicate_type, created_at
) VALUES (
  <主副本id或NULL>, <损坏文件id>, 'corrupted', datetime('now')
);

-- 4. 写入文件无效标记
INSERT OR IGNORE INTO reference_duplicates (
  primary_reference_id, duplicate_reference_id, duplicate_type, created_at
) VALUES (
  <主副本id或NULL>, <无效文件id>, 'invalid', datetime('now')
);

-- 5. 查询所有精确重复
SELECT * FROM reference_duplicates WHERE duplicate_type = 'exact';

-- 6. 查询所有模糊重复
SELECT * FROM reference_duplicates WHERE duplicate_type = 'fuzzy';

-- 7. 查询所有损坏文件
SELECT * FROM reference_duplicates WHERE duplicate_type = 'corrupted';

-- 8. 查询主副本优先级（保留 id 最小即最早入库的记录为主副本）
SELECT rd.primary_reference_id, r1.title, r1.file_path AS primary_path,
       rd.duplicate_reference_id, r2.title, r2.file_path AS duplicate_path,
       rd.duplicate_type
FROM reference_duplicates rd
JOIN references r1 ON rd.primary_reference_id = r1.id
JOIN references r2 ON rd.duplicate_reference_id = r2.id
ORDER BY rd.primary_reference_id;
