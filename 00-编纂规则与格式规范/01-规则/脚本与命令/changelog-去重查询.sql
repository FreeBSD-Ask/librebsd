-- changelog 去重查询 SQL
-- 数据库：01-项目管理/00-变更记录/changelog.db
-- 表：entries
-- 规则引用位置：流程规则.md “changelog 去重规则” 小节

-- 1. 查找疑似重复条目（相同日期、摘要前 60 字符相同）
SELECT a.id, b.id, a.date, a.summary
FROM entries a JOIN entries b ON a.date = b.date AND a.id < b.id
WHERE SUBSTR(a.summary, 1, 60) = SUBSTR(b.summary, 1, 60);

-- 2. 时间顺序复核（按日期分组统计条目数）
SELECT date, COUNT(*) FROM entries GROUP BY date ORDER BY date;

-- 3. 条目数一致性复核
SELECT COUNT(*) FROM entries;

-- 4. 合并条目时删除冗余条目（须逐个核对后执行，禁批量禁脚本）
-- DELETE FROM entries WHERE id = <待删除条目id>;

-- 5. 删除无效条目（须逐个核对后执行）
-- DELETE FROM entries WHERE id = <无效条目id>;
