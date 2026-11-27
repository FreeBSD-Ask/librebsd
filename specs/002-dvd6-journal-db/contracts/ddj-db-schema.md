# Contract: 四库 schema（Phase A 建库 ↔ Phase B 入库的接口）

四库（`ddj/` 下 `ddj.duckdb` / `cuj.duckdb` / `sa.duckdb` / `tpj.duckdb`）同构，表名与列名固定如下；Phase B 唯一允许的读取面。建库脚本与入库脚本分别独立进程，只经本契约耦合。

## DDL（每库执行一次；已存在则跳过并校验兼容）

```sql
CREATE TABLE IF NOT EXISTS journal_meta (
  journal_code    VARCHAR NOT NULL,
  journal_fullname VARCHAR NOT NULL,
  source_root     VARCHAR NOT NULL,
  years_covered   VARCHAR,
  built_at        TIMESTAMP
);
CREATE TABLE IF NOT EXISTS issues (
  issue_id    BIGINT PRIMARY KEY,
  journal_code VARCHAR NOT NULL,
  year        INTEGER,
  month       INTEGER,
  issue_label VARCHAR NOT NULL,
  toc_title   VARCHAR,
  toc_text    VARCHAR
);
CREATE TABLE IF NOT EXISTS articles (
  article_id   BIGINT PRIMARY KEY,
  issue_id     BIGINT NOT NULL REFERENCES issues(issue_id),
  title        VARCHAR NOT NULL,
  subtitle     VARCHAR,
  author       VARCHAR,
  author_bio   VARCHAR,
  section      VARCHAR,
  toc_abstract VARCHAR,
  body_text    VARCHAR
);
CREATE TABLE IF NOT EXISTS source_files (
  file_id       BIGINT PRIMARY KEY,
  issue_id      BIGINT NOT NULL REFERENCES issues(issue_id),
  article_id    BIGINT REFERENCES articles(article_id),
  file_name     VARCHAR NOT NULL,
  archive_layer VARCHAR NOT NULL,
  encoding      VARCHAR,
  bytes         INTEGER,
  content_text  VARCHAR NOT NULL
);
CREATE TABLE IF NOT EXISTS ads (
  ad_id      BIGINT PRIMARY KEY,
  issue_id   BIGINT NOT NULL REFERENCES issues(issue_id),
  article_id BIGINT REFERENCES articles(article_id),
  ad_text    VARCHAR,
  figure_id  BIGINT REFERENCES figures(figure_id),
  ad_kind    VARCHAR
);
CREATE TABLE IF NOT EXISTS figures (
  figure_id          BIGINT PRIMARY KEY,
  issue_id           BIGINT NOT NULL REFERENCES issues(issue_id),
  article_id         BIGINT REFERENCES articles(article_id),
  image_name         VARCHAR NOT NULL,
  disposition        VARCHAR NOT NULL,  -- transcribed / base64 / skipped / uncertain
  disposition_reason VARCHAR,
  transcription_text VARCHAR,
  base64_data        VARCHAR,
  image_format       VARCHAR
);
CREATE TABLE IF NOT EXISTS build_log (
  log_id    BIGINT PRIMARY KEY,
  phase     VARCHAR NOT NULL,
  batch     VARCHAR NOT NULL,
  note      VARCHAR,
  logged_at TIMESTAMP NOT NULL
);
```

## 接口不变量（Phase B 读取前提，Phase A 收口断言）

1. `figures.disposition` ∈ {transcribed, base64, skipped, uncertain}，且 transcribed ⇒ `transcription_text` 非空、base64 ⇒ `base64_data` 非空，二者互斥；uncertain 收口时必须为 0 行。
2. `source_files.content_text` 无 NUL 字节、无压缩包原始字节（二进制禁入）。
3. `issues` 幂等键 (journal_code, year, month, issue_label) 唯一；`articles` (issue_id, title, author) 唯一；`source_files` (issue_id, archive_layer, file_name) 唯一；`figures` (issue_id, image_name) 唯一。
4. 所有文本列 UTF-8、无 BOM 字符前置；`issues.toc_text` 与 `articles.body_text` 为转文本产物（Markdown 标题标记＋段落），不含 HTML 标签残留（`<` 标签残留抽检为 0）。
5. 路径纪律：任何表不得存完整磁盘路径；溯源仅用 `archive_layer`/`image_name`/`file_name`。
6. DuckDB 保留字（如 `at`、`year` 视版本）在 SQL 中加引号；写入以显式事务包裹，脚本可安全重跑（幂等：先查幂等键存在则跳过）。

## 消费方（Phase B）最低读取契约

- 入库以 `(journal_code, year, month, issue_label)` 定位期、以 `articles` 行为单位取 `title/author/section/body_text`、以 `source_files.content_text` 取代码、以 `ads`/`figures` 取广告与图片处置产物。
- Phase B 不得回写四库；四库为只读源。
