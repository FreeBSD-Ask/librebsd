-- =============================================================================
-- 文件夹级数据库通用架构 SQL
-- =============================================================================
-- 文件用途：7 个文件夹级数据库的通用架构定义（5 张通用表 + schema_meta 表 + 文件夹专属扩展表）
-- 架构版本：1.4
-- 创建日期：2026-07-31
-- 修订日期：2026-08-04（v1.4 补充登记：资料数据库 v1.4 化对齐——旧 cross_references 改名 material_cross_references）
-- 修订日期：2026-08-01（v1.4：索引命名统一 + 扩展表合并 5 组 + 引用查询加速索引）
-- 修订历史：2026-08-01（v1.3：新增 schema_meta 元数据表 + 9 个预定义索引；由 optimize_folder_databases.py 执行）
-- 修订历史：2026-08-01（v1.2：files 表新增 duplicate_of_db、duplicate_of_global_file_id 字段，支持跨库去重）
-- 修订历史：2026-07-31（v1.1：按需建表，构建脚本按 db_name 过滤专属表）
-- 关联规范：convert-folders-to-databases-2026-07-31、optimize-databases-and-file-organization-2026-08-01、unify-database-format-2026-08-01
-- 2026-08-04 补充登记：`03-原始史料库/01-代码仓库史料/01-数据库本体/资料数据库.db`（独立库，非文件夹级 7 库）已按本 schema v1.4 对齐——
--   新增 5 张通用表（files/blocks/blocks_fts/cross_references/update_log）+ schema_meta（key-value，9 标准键）；
--   旧业务表（materials/references/freebsd_sa/nvd_cve_metadata/fact_check_records）保留为专属扩展表，不适用下方文件夹专属表清单；
--   旧 `cross_references` 表（src_ch/dst_ch 整数章节引用语义）已改名为 `material_cross_references`，避免与 v1.4 通用 cross_references 同名冲突。
--   执行脚本：script/_refactor_ziliao_db_20260804.py（2026-08-04）
-- v1.4 变更摘要：
--   1. 索引命名统一：idx_xref_* → idx_cross_references_*（3 个索引重命名）
--   2. 删除冗余索引：idx_files_duplicate_type（与 idx_files_duplicate_of_id 功能重复）
--   3. 补建索引：idx_files_duplicate_of_db（files.duplicate_of_db 字段）
--   4. 新增引用查询加速索引：idx_cross_references_reference_type、idx_cross_references_source_block_id
--   5. 扩展表合并（5 组，减少 5 张表）：
--      - security_advisories + vulnerability_metadata → security_vulnerabilities（original_sources.db）
--      - disputes + peer_reviews → review_records（review_reports.db）
--      - person_index + person_biography → person_records（cross_indexes.db）
--      - command_index + term_index → terminology_index（cross_indexes.db）
--      - build_status + citation_frequency → build_citation_records（metadata_interfaces.db）
--   6. 合并表均含 record_type 字段区分来源，并创建 file_id 与 record_type 索引
-- 适用数据库（7 个文件夹级数据库）：
--   1. 02-sacred源材料/sacred_sources.db（无专属表）
--   2. 03-原始史料库/original_sources.db（2 张专属表：kaoju_records/security_vulnerabilities）
--   3. 04-现代研究文献/research_notes.db（无专属表）
--   4. 07-事实核查记录/fact_checks.db（fact_check_records 已按需删除，无专属表）
--   5. 08-核查报告与多轮复核/review_reports.db（1 张专属表：review_records）
--   6. 10-交叉索引/cross_indexes.db（4 张专属表：person_records/terminology_index/concept_history，含合并表）
--   7. 11-元数据接口/metadata_interfaces.db（4 张专属表：chapter_metadata/timeline_records/build_citation_records，含合并表；author_index 已按需删除）
-- 按需建表规则：
--   - 构建脚本 apply_schema(conn, db_name) 按 “-- 数据库 X：<db_name>.db” 标记分割 SQL
--   - 通用表（5 张）：所有数据库始终创建
--   - 专属表：只有 db_name 匹配的分组才创建
--   - sacred_sources 与 research_notes 无专属表，只创建通用表
--   - 2026-07-31 精简：已删除各数据库中不属于它的空专属表（共删除 96 张）
--   - 2026-08-01 合并：5 组低使用率扩展表已合并（共减少 5 张表）
-- 编码：UTF-8 无 BOM，LF 换行
-- 规则引用位置：流程规则.md “规则引用脚本与命令独立存储规则” 小节
-- 幂等性说明：所有 CREATE 语句均使用 IF NOT EXISTS，可重复执行
-- =============================================================================

-- 启用外键约束（SQLite 默认关闭，须在每个连接中显式开启后方能使 ON DELETE CASCADE 生效）
PRAGMA foreign_keys = ON;

-- =============================================================================
-- 第一部分：通用表（5 张）
-- 所有 7 个文件夹级数据库均须创建以下 5 张通用表
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 表 1：files（主表）
-- 存储文件元数据、内容哈希、重复关系
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    filename TEXT NOT NULL,
    folder_path TEXT NOT NULL,
    file_extension TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    line_count INTEGER,
    char_count INTEGER,
    encoding TEXT NOT NULL DEFAULT 'utf-8',
    line_ending TEXT NOT NULL DEFAULT 'lf',
    mtime TEXT NOT NULL,
    ingested_at TEXT NOT NULL,
    title TEXT,
    summary TEXT,
    frontmatter TEXT,
    status TEXT NOT NULL DEFAULT 'active',
    duplicate_of_id INTEGER,
    duplicate_type TEXT,
    duplicate_of_db TEXT,
    duplicate_of_global_file_id INTEGER,
    FOREIGN KEY (duplicate_of_id) REFERENCES files(id)
);

CREATE INDEX IF NOT EXISTS idx_files_sha256 ON files(sha256);
CREATE INDEX IF NOT EXISTS idx_files_status ON files(status);
CREATE INDEX IF NOT EXISTS idx_files_duplicate_of_db ON files(duplicate_of_db);

-- -----------------------------------------------------------------------------
-- 表 2：blocks（结构化块表）
-- 存储文件解析后的结构化块（paragraph/heading/list_item/code_block/quote/table_row/frontmatter/csv_row/json_node/footnote）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    block_index INTEGER NOT NULL,
    block_type TEXT NOT NULL,
    block_level INTEGER,
    block_content TEXT NOT NULL,
    block_line_start INTEGER,
    block_line_end INTEGER,
    block_char_offset_start INTEGER,
    block_char_offset_end INTEGER,
    heading_anchor TEXT,
    block_metadata TEXT,
    UNIQUE(file_id, block_index),
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_blocks_file_id ON blocks(file_id);
CREATE INDEX IF NOT EXISTS idx_blocks_block_type ON blocks(block_type);
CREATE INDEX IF NOT EXISTS idx_blocks_heading_anchor ON blocks(heading_anchor);

-- -----------------------------------------------------------------------------
-- 表 3：blocks_fts（FTS5 全文检索虚拟表）
-- 基于 blocks.block_content 建立全文索引，unicode61 分词器支持中文与多语种
-- -----------------------------------------------------------------------------
CREATE VIRTUAL TABLE IF NOT EXISTS blocks_fts USING fts5(
    file_id UNINDEXED,
    block_id UNINDEXED,
    content,
    tokenize='unicode61 remove_diacritics 2'
);

-- 同步触发器：保持 blocks_fts 与 blocks 表一致
CREATE TRIGGER IF NOT EXISTS trigger_blocks_fts_ai AFTER INSERT ON blocks BEGIN
    INSERT INTO blocks_fts(file_id, block_id, content)
    VALUES (new.file_id, new.id, new.block_content);
END;

CREATE TRIGGER IF NOT EXISTS trigger_blocks_fts_ad AFTER DELETE ON blocks BEGIN
    DELETE FROM blocks_fts WHERE block_id = old.id;
END;

CREATE TRIGGER IF NOT EXISTS trigger_blocks_fts_au AFTER UPDATE ON blocks BEGIN
    DELETE FROM blocks_fts WHERE block_id = old.id;
    INSERT INTO blocks_fts(file_id, block_id, content)
    VALUES (new.file_id, new.id, new.block_content);
END;

-- -----------------------------------------------------------------------------
-- 表 4：cross_references（交叉引用表）
-- 存储文件内/文件间/数据库间引用关系（wikilink/markdown_link/footnote/citation/chapter_ref/spec_ref/db_ref/external_url）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS cross_references (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    source_block_id INTEGER,
    reference_type TEXT NOT NULL,
    reference_text TEXT NOT NULL,
    target_path TEXT,
    target_db TEXT,
    target_record_id INTEGER,
    target_anchor TEXT,
    resolution_status TEXT NOT NULL DEFAULT 'pending',
    reference_context TEXT,
    resolved_at TEXT,
    FOREIGN KEY (source_file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (source_block_id) REFERENCES blocks(id) ON DELETE SET NULL
);

-- 引用查询加速索引（v1.4 命名统一 + 新增 2 个索引）
CREATE INDEX IF NOT EXISTS idx_cross_references_source_file_id ON cross_references(source_file_id);
CREATE INDEX IF NOT EXISTS idx_cross_references_target_path ON cross_references(target_path);
CREATE INDEX IF NOT EXISTS idx_cross_references_resolution_status ON cross_references(resolution_status);
CREATE INDEX IF NOT EXISTS idx_cross_references_reference_type ON cross_references(reference_type);
CREATE INDEX IF NOT EXISTS idx_cross_references_source_block_id ON cross_references(source_block_id);

-- -----------------------------------------------------------------------------
-- 表 5：update_log（更新日志表）
-- 记录文件级与数据库级操作日志（add/update/delete/merge/rebuild/migrate/fix/optimize）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    operation TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    timestamp TEXT NOT NULL,
    operated_by TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_update_log_file_id ON update_log(file_id);
CREATE INDEX IF NOT EXISTS idx_update_log_operation ON update_log(operation);
CREATE INDEX IF NOT EXISTS idx_update_log_timestamp ON update_log(timestamp);

-- =============================================================================
-- 第二部分：文件夹专属扩展表（v1.4 合并后 10 张，原 15 张 - 5 组合并 = 10 张）
-- 按数据库分组，仅对应文件夹级数据库须创建相应扩展表
-- 所有扩展表均含 file_id 外键（ON DELETE CASCADE），与 files 主表联动
-- 合并表均含 record_type 字段区分来源，并创建 file_id 与 record_type 索引
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 数据库 A：07-事实核查记录/fact_checks.db
-- -----------------------------------------------------------------------------
-- 注：fact_check_records 表已按需删除（空表），不再定义

-- -----------------------------------------------------------------------------
-- 数据库 B：08-核查报告与多轮复核/review_reports.db
-- -----------------------------------------------------------------------------

-- 表 6：review_records（核查记录合并表，v1.4 合并 disputes + peer_reviews）
-- record_type: dispute（历史争议）/ peer_review（同行评议）
CREATE TABLE IF NOT EXISTS review_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    record_type TEXT,
    dispute_name TEXT,
    parties TEXT,
    period TEXT,
    summary TEXT,
    positions TEXT,
    evidence TEXT,
    resolution_status TEXT,
    reviewer TEXT,
    review_round TEXT,
    submission_date TEXT,
    verdict TEXT,
    comments TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_review_records_file_id ON review_records(file_id);
CREATE INDEX IF NOT EXISTS idx_review_records_record_type ON review_records(record_type);

-- -----------------------------------------------------------------------------
-- 数据库 C：10-交叉索引/cross_indexes.db
-- -----------------------------------------------------------------------------

-- 表 7：person_records（人物记录合并表，v1.4 合并 person_index + person_biography）
-- record_type: person_index（人名索引）/ person_biography（人物传记）
CREATE TABLE IF NOT EXISTS person_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    record_type TEXT,
    person_name TEXT,
    normalized_name TEXT,
    aliases TEXT,
    role TEXT,
    biography_summary TEXT,
    page_refs TEXT,
    biography TEXT,
    academic_genealogy TEXT,
    affiliations TEXT,
    works TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_person_records_file_id ON person_records(file_id);
CREATE INDEX IF NOT EXISTS idx_person_records_record_type ON person_records(record_type);

-- 表 8：terminology_index（术语索引合并表，v1.4 合并 command_index + term_index）
-- record_type: command（命令索引）/ term（术语索引）
CREATE TABLE IF NOT EXISTS terminology_index (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    record_type TEXT,
    command_name TEXT,
    manual_section TEXT,
    category TEXT,
    description TEXT,
    page_refs TEXT,
    term TEXT,
    translation TEXT,
    definition TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_terminology_index_file_id ON terminology_index(file_id);
CREATE INDEX IF NOT EXISTS idx_terminology_index_record_type ON terminology_index(record_type);

-- 表 9：concept_history（概念史与思想谱系表，保留未合并）
CREATE TABLE IF NOT EXISTS concept_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    concept_name TEXT,
    etymology TEXT,
    history_summary TEXT,
    related_concepts TEXT,
    page_refs TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

-- 表 9b：organization_index（组织机构索引分表，2026-10-06 119j 批 119d ★10 新增）
-- category: 法人（基金会）/ 团队 / 职位；subject 取值＝四类历史主体（法人→基金会；团队·职位→团队与职位）
CREATE TABLE IF NOT EXISTS organization_index (
    id VARCHAR,
    file_id VARCHAR,
    category VARCHAR,
    entry VARCHAR,
    subject VARCHAR,
    anchor VARCHAR,
    aliases VARCHAR,
    note VARCHAR
);

CREATE INDEX IF NOT EXISTS idx_organization_index_file_id ON organization_index(file_id);
CREATE INDEX IF NOT EXISTS idx_organization_index_subject ON organization_index(subject);

-- -----------------------------------------------------------------------------
-- 数据库 D：03-原始史料库/original_sources.db
-- -----------------------------------------------------------------------------

-- 表 10：kaoju_records（考据记录表，保留未合并）
CREATE TABLE IF NOT EXISTS kaoju_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    source_verification TEXT,
    cross_verification_method TEXT,
    doubt_basis TEXT,
    page_refs TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

-- 表 11：security_vulnerabilities（安全漏洞合并表，v1.4 合并 security_advisories + vulnerability_metadata）
-- record_type: advisory（安全公告）/ vulnerability（漏洞元数据）
CREATE TABLE IF NOT EXISTS security_vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    record_type TEXT,
    advisory_id TEXT,
    project TEXT,
    release_date TEXT,
    affected_versions TEXT,
    component TEXT,
    severity TEXT,
    cve_references TEXT,
    cve_id TEXT,
    published_date TEXT,
    modified_date TEXT,
    cvss_score REAL,
    cvss_vector TEXT,
    cwe TEXT,
    affected_products TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_security_vulnerabilities_file_id ON security_vulnerabilities(file_id);
CREATE INDEX IF NOT EXISTS idx_security_vulnerabilities_record_type ON security_vulnerabilities(record_type);

-- -----------------------------------------------------------------------------
-- 数据库 E：11-元数据接口/metadata_interfaces.db
-- -----------------------------------------------------------------------------

-- 表 12：chapter_metadata（章节元数据表，保留未合并）
CREATE TABLE IF NOT EXISTS chapter_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    chapter_id TEXT,
    volume TEXT,
    chapter TEXT,
    title TEXT,
    word_count INTEGER,
    main_thread TEXT,
    status TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

-- 注：author_index 表已按需删除（空表），不再定义

-- 表 13：timeline_records（年代时间线记录表，保留未合并）
CREATE TABLE IF NOT EXISTS timeline_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    event_date TEXT,
    event_description TEXT,
    event_type TEXT,
    source_chapter TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

-- 表 14：build_citation_records（构建与引文记录合并表，v1.4 合并 build_status + citation_frequency）
-- record_type: build_status（构建状态）/ citation_frequency（引文频次）
CREATE TABLE IF NOT EXISTS build_citation_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    record_type TEXT,
    target TEXT,
    last_build TEXT,
    last_success TEXT,
    last_failure TEXT,
    status TEXT,
    reference_id TEXT,
    citation_count INTEGER,
    cited_in_chapters TEXT,
    last_cited TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_build_citation_records_file_id ON build_citation_records(file_id);
CREATE INDEX IF NOT EXISTS idx_build_citation_records_record_type ON build_citation_records(record_type);

-- =============================================================================
-- 第三部分：schema_meta 元数据表（v1.3 新增）
-- 由 optimize_folder_databases.py --schema 模式创建
-- 存储 schema_version、last_optimize_at、last_vacuum_at、table_count、active_files、
-- deleted_files、ghost_blocks_cleaned、journal_mode、pragma_optimized_at 等元数据键值对
-- v1.4 标准键集合（9 个）：active_files/deleted_files/ghost_blocks_cleaned/journal_mode/
--   last_optimize_at/last_vacuum_at/pragma_optimized_at/schema_version/table_count
-- =============================================================================
CREATE TABLE IF NOT EXISTS schema_meta (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- =============================================================================
-- 第四部分：预定义索引（v1.4 更新，由 optimize_folder_databases.py --schema 模式创建）
-- files 表 5 索引 + blocks 表 1 索引 + cross_references 表 5 索引 + 扩展表 file_id 索引
-- v1.4 变更：
--   - 删除 idx_files_duplicate_type（冗余）
--   - 新增 idx_files_duplicate_of_db
--   - cross_references 新增 idx_cross_references_reference_type、idx_cross_references_source_block_id
-- =============================================================================
CREATE INDEX IF NOT EXISTS idx_files_status ON files(status);
CREATE INDEX IF NOT EXISTS idx_files_sha256 ON files(sha256);
CREATE INDEX IF NOT EXISTS idx_files_content_hash ON files(content_hash);
CREATE INDEX IF NOT EXISTS idx_files_duplicate_of_id ON files(duplicate_of_id);
CREATE INDEX IF NOT EXISTS idx_files_duplicate_of_db ON files(duplicate_of_db);

CREATE INDEX IF NOT EXISTS idx_blocks_file_id ON blocks(file_id);

CREATE INDEX IF NOT EXISTS idx_cross_references_source_file_id ON cross_references(source_file_id);
CREATE INDEX IF NOT EXISTS idx_cross_references_target_path ON cross_references(target_path);
CREATE INDEX IF NOT EXISTS idx_cross_references_resolution_status ON cross_references(resolution_status);
CREATE INDEX IF NOT EXISTS idx_cross_references_reference_type ON cross_references(reference_type);
CREATE INDEX IF NOT EXISTS idx_cross_references_source_block_id ON cross_references(source_block_id);

-- =============================================================================
-- 文件结束
-- 共定义 15 张表：5 张通用表 + schema_meta 元数据表 + 9 张文件夹专属扩展表（v1.4 合并后）
-- 通用表（所有数据库创建）：files、blocks、blocks_fts、cross_references、update_log
-- 元数据表（所有数据库创建）：schema_meta
-- 扩展表（按 db_name 过滤创建）：
--   review_reports.db：review_records（1 张，合并自 disputes + peer_reviews）
--   cross_indexes.db：person_records、terminology_index、concept_history（3 张，person_records 合并自 person_index + person_biography，terminology_index 合并自 command_index + term_index）
--   original_sources.db：kaoju_records、security_vulnerabilities（2 张，security_vulnerabilities 合并自 security_advisories + vulnerability_metadata）
--   metadata_interfaces.db：chapter_metadata、timeline_records、build_citation_records（3 张，build_citation_records 合并自 build_status + citation_frequency）
--   sacred_sources.db、research_notes.db、fact_checks.db：无专属表（只创建通用表 + schema_meta）
-- 按需建表规则：构建脚本 apply_schema(conn, db_name) 按 “-- 数据库 X：<db_name>.db” 标记分割
-- v1.4 索引：由 optimize_folder_databases.py --schema 模式创建，不在构建脚本中执行
-- v1.4 合并表：均含 record_type 字段区分来源，并创建 file_id 与 record_type 索引
-- =============================================================================
