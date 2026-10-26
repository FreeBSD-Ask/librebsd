-- =============================================================================
-- TUHS Wiki 史料库架构 SQL
-- =============================================================================
-- 文件用途：独立史料库 tuhs_wiki.duckdb 的完整架构定义（11 张表 + 1 个视图 + 5 个索引）
-- 目标库：03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb（DuckDB 运行时 2.0.0，存储版本 v2.0.0+）
-- 规格出处：.trae/specs/crawl-tuhs-wiki-20261025/spec.md（Requirement: 独立 DuckDB 2.0.0 库与 Schema）
-- 创建日期：2026-10-25
-- 架构版本：1.0
-- 类型口径：DuckDB 原生类型；正文列一律 VARCHAR，全库禁 BLOB（二进制正文不得入库）
-- 幂等性说明：所有 CREATE 语句均使用 IF NOT EXISTS，可重复执行
-- 编码：UTF-8 无 BOM，LF 换行
-- =============================================================================

-- =============================================================================
-- 第一部分：页面主表与全文
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 表 1：pages（页面与外链页统一主表，作用类比 references_fulltext 的 references）
-- source_kind：wiki（站点页面）／external（站外一跳抓取页）
-- status：active（成功）／failed（失败）／excluded（排除）／needs_ocr_deferred（待 OCR）等
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pages (
    id BIGINT PRIMARY KEY,
    page_key VARCHAR NOT NULL UNIQUE,
    source_kind VARCHAR NOT NULL,
    namespace VARCHAR,
    title VARCHAR,
    url VARCHAR NOT NULL,
    canonical_url VARCHAR NOT NULL,
    depth INTEGER NOT NULL DEFAULT 0,
    referrer_page_key VARCHAR,
    referrer_url VARCHAR,
    anchor_text VARCHAR,
    http_status INTEGER,
    content_type VARCHAR,
    fetched_at VARCHAR,
    fetch_mode VARCHAR,
    etag VARCHAR,
    last_modified VARCHAR,
    wikitext_path VARCHAR,
    md_path VARCHAR,
    source_bytes BIGINT,
    sha256_source VARCHAR,
    sha256_markdown VARCHAR,
    char_count BIGINT,
    extraction_method VARCHAR,
    converter VARCHAR,
    language VARCHAR,
    wiki_last_modified VARCHAR,
    wiki_last_author VARCHAR,
    status VARCHAR NOT NULL,
    notes VARCHAR
);

CREATE INDEX IF NOT EXISTS idx_pages_namespace ON pages(namespace);
CREATE INDEX IF NOT EXISTS idx_pages_source_kind ON pages(source_kind);
CREATE INDEX IF NOT EXISTS idx_pages_status ON pages(status);
CREATE INDEX IF NOT EXISTS idx_pages_canonical_url ON pages(canonical_url);

-- -----------------------------------------------------------------------------
-- 表 2：fulltext（Markdown 正文，每页恰 1 条）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS fulltext (
    id BIGINT PRIMARY KEY,
    page_key VARCHAR NOT NULL UNIQUE,
    content VARCHAR NOT NULL,
    char_count BIGINT NOT NULL,
    extraction_method VARCHAR,
    extracted_at VARCHAR,
    page_markers VARCHAR,
    extraction_notes VARCHAR,
    encoding VARCHAR DEFAULT 'utf-8',
    line_ending VARCHAR DEFAULT 'lf'
);

-- -----------------------------------------------------------------------------
-- 表 3：fulltext_blocks（Markdown 结构化块，段落级最小单元）
-- block_type：heading／paragraph／list_item／code_block／quote／table_row 等
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS fulltext_blocks (
    id BIGINT PRIMARY KEY,
    page_key VARCHAR NOT NULL,
    block_index BIGINT NOT NULL,
    block_type VARCHAR NOT NULL,
    block_level INTEGER,
    heading_path VARCHAR,
    block_content VARCHAR NOT NULL,
    block_page INTEGER,
    char_offset_start BIGINT,
    char_offset_end BIGINT,
    UNIQUE(page_key, block_index)
);

-- =============================================================================
-- 第二部分：链接图、排除台账与转换台账
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 表 4：links（链接图与抓取状态）
-- target_kind：internal／external／media／excluded_book／excluded_source／non_content
-- resolution_status：queued／fetched／broken_internal／excluded／failed 等
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS links (
    id BIGINT PRIMARY KEY,
    source_page_key VARCHAR NOT NULL,
    target_kind VARCHAR NOT NULL,
    target_url VARCHAR NOT NULL,
    target_page_key VARCHAR,
    anchor_text VARCHAR,
    link_context VARCHAR,
    depth INTEGER NOT NULL DEFAULT 1,
    resolution_status VARCHAR NOT NULL,
    discovered_at VARCHAR,
    UNIQUE(source_page_key, target_url, target_kind)
);

-- -----------------------------------------------------------------------------
-- 表 5：excluded_items（书籍／源码／媒体排除台账，排除项一律不下载）
-- item_kind：book／source_code／binary_media／out_of_scope
-- review_flag=1 表示待人工复核（如 >50 MB 的 PDF）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS excluded_items (
    id BIGINT PRIMARY KEY,
    url VARCHAR NOT NULL,
    item_kind VARCHAR NOT NULL,
    reason VARCHAR,
    evidence_page_key VARCHAR,
    evidence_text VARCHAR,
    http_content_type VARCHAR,
    content_length BIGINT,
    review_flag INTEGER NOT NULL DEFAULT 0,
    recorded_at VARCHAR,
    UNIQUE(url, item_kind)
);

-- -----------------------------------------------------------------------------
-- 表 6：conversions（转换台账：源哈希／md 哈希／警告）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS conversions (
    id BIGINT PRIMARY KEY,
    page_key VARCHAR NOT NULL,
    converter VARCHAR NOT NULL,
    converter_version VARCHAR,
    source_kind VARCHAR,
    source_sha256 VARCHAR,
    md_sha256 VARCHAR,
    converted_at VARCHAR,
    warnings VARCHAR,
    UNIQUE(page_key, converter)
);

-- =============================================================================
-- 第三部分：批次、请求留痕与验证
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 表 7：crawl_runs（批次基线与计数；scope_json 存页面集合排序 SHA-256 与逐命名空间计数）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS crawl_runs (
    run_id VARCHAR PRIMARY KEY,
    started_at VARCHAR,
    finished_at VARCHAR,
    scope_json VARCHAR,
    page_baseline INTEGER,
    page_fetched INTEGER,
    external_fetched INTEGER,
    excluded INTEGER,
    failed INTEGER,
    status VARCHAR,
    tool_version VARCHAR
);

-- -----------------------------------------------------------------------------
-- 表 8：crawl_log（逐请求留痕：重试、状态、错误）
-- url_kind：wiki_raw／wiki_xhtml／index／external／wayback 等
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS crawl_log (
    id BIGINT PRIMARY KEY,
    run_id VARCHAR,
    url VARCHAR,
    url_kind VARCHAR,
    attempt INTEGER,
    http_status INTEGER,
    bytes BIGINT,
    error_type VARCHAR,
    error_detail VARCHAR,
    started_at VARCHAR,
    finished_at VARCHAR,
    duration_ms BIGINT
);

CREATE INDEX IF NOT EXISTS idx_crawl_log_run_id ON crawl_log(run_id);

-- -----------------------------------------------------------------------------
-- 表 9：verification（每轮验证的判据与期望／实测）
-- round：第一轮（主验证器）／第二轮（独立 SQL 复核）／第三轮（人工抽样）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS verification (
    id BIGINT PRIMARY KEY,
    run_id VARCHAR,
    round VARCHAR,
    check_id VARCHAR,
    check_name VARCHAR,
    expected VARCHAR,
    actual VARCHAR,
    passed BOOLEAN,
    detail VARCHAR,
    verified_at VARCHAR
);

-- =============================================================================
-- 第四部分：元数据与变更留痕
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 表 10：schema_meta（key-value 元数据：9 个标准键 + 语料键）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS schema_meta (
    key VARCHAR PRIMARY KEY,
    value VARCHAR
);

-- -----------------------------------------------------------------------------
-- 表 11：update_log（字段级变更留痕）
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS update_log (
    id BIGINT PRIMARY KEY,
    page_key VARCHAR,
    operation VARCHAR NOT NULL,
    field_changed VARCHAR NOT NULL,
    old_value VARCHAR,
    new_value VARCHAR,
    timestamp VARCHAR NOT NULL,
    operated_by VARCHAR NOT NULL,
    notes VARCHAR
);

-- =============================================================================
-- 第五部分：遍历视图
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 视图 v_page_documents：pages 左连 fulltext，供后续项目按 namespace 顺序快速遍历
-- -----------------------------------------------------------------------------
CREATE VIEW IF NOT EXISTS v_page_documents AS
SELECT
    p.page_key,
    p.source_kind,
    p.namespace,
    p.title,
    p.url,
    p.fetched_at,
    p.sha256_source,
    p.sha256_markdown,
    f.content,
    f.char_count,
    f.extraction_method
FROM pages p
LEFT JOIN fulltext f USING (page_key);

-- =============================================================================
-- 文件结束
-- 共 11 张表：pages、fulltext、fulltext_blocks、links、excluded_items、conversions、
--             crawl_runs、crawl_log、verification、schema_meta、update_log
-- 共 1 个视图：v_page_documents
-- 共 5 个索引：pages（namespace／source_kind／status／canonical_url）、crawl_log（run_id）
-- =============================================================================
