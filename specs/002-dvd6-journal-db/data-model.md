# Data Model: dvd6 期刊四库建库 → 全文库入库 → 入大纲

**Feature**: specs/002-dvd6-journal-db | **Date**: 2026-10-05

四库统一 schema（每库同构，仅 `journal_meta` 不同）；Phase B/C 实体按既有库 schema 增量对接。主键自增 id 仅作库内主键，**业务判重一律用业务键**（见每表 `幂等键`）。

## 库 1–4：四库统一 schema（`ddj/` 下 ddj.duckdb / cuj.duckdb / sa.duckdb / tpj.duckdb）

### journal_meta（库级单行）

| 字段 | 类型 | 说明 |
|------|------|------|
| journal_code | VARCHAR | ddj / cuj / sa / tpj |
| journal_fullname | VARCHAR | Dr. Dobb's Journal / C/C++ Users Journal（C Users Journal）/ Sys Admin / The Perl Journal |
| source_root | VARCHAR | 来源树名（`dvd6/Website`；站点级而非文件路径） |
| years_covered | VARCHAR | 实测覆盖年段（建库完成后回填） |
| built_at | TIMESTAMP | 建库完成时间（UTC） |

### issues（期）

| 字段 | 类型 | 说明 |
|------|------|------|
| issue_id | BIGINT PK | 库内自增 |
| journal_code | VARCHAR | 刊号 |
| year | INTEGER | 年（如 1990；SA 用卷号换算的年份为准，卷号另存 issue_label） |
| month | INTEGER | 月 1–12（无法判定月份的期存 NULL 并在 issue_label 保留原文标识） |
| issue_label | VARCHAR | 原文期标识（`jan90` / `9001` / `v01i01` / `vol1_1` / `tpj0302`），照录不改 |
| toc_title | VARCHAR | 目录页标题原文（如 "January 1990 - REAL TIME AND EMBEDDED SYSTEMS PROGRAMMING"） |
| toc_text | VARCHAR | 目录页正文（栏目分节＋各文署名＋摘要文本） |
| 幂等键 | — | (journal_code, year, month, issue_label) |

### articles（文章）

| 字段 | 类型 | 说明 |
|------|------|------|
| article_id | BIGINT PK | 库内自增 |
| issue_id | BIGINT FK | → issues |
| title | VARCHAR | 题名照录 |
| subtitle | VARCHAR | 副题（DDJ h2；无则 NULL） |
| author | VARCHAR | 署名（多人以分号分隔） |
| author_bio | VARCHAR | 作者简介文本（无则 NULL） |
| section | VARCHAR | 栏目/类型（FEATURES/COLUMNS/EDITORIAL/LETTERS/NEW PRODUCTS/…，与 TOC 分节一致；TOC 未分节者按页面实测归类） |
| toc_abstract | VARCHAR | 目录页摘要（无则 NULL） |
| body_text | VARCHAR | 正文全文（HTML 转文本，标题层级→Markdown 标记，段落照录；文内提及的可执行文件名等随正文保留） |
| 幂等键 | — | (issue_id, title, author) |

### source_files（解压后文本代码/文档）

| 字段 | 类型 | 说明 |
|------|------|------|
| file_id | BIGINT PK | 库内自增 |
| issue_id | BIGINT FK | → issues（最小关联恒有） |
| article_id | BIGINT FK NULL | → articles（能建立映射时填；映射依据＝TOC/说明页/readme 提及、作者名吻合；不能建立则 NULL，不猜） |
| file_name | VARCHAR | 文本文件名照录（如 `zg_lwlvl.c`；内嵌包文件记 `saks.zip!bardavid.c` 形式的包层级，不算文件路径） |
| archive_layer | VARCHAR | 溯源标签（外层包＋内嵌包，如 `CUJ/1990/jan90.zip + saks.zip`；不含磁盘路径） |
| encoding | VARCHAR | 检出编码（utf-8/cp437/latin-1/…） |
| bytes | INTEGER | 解码前字节数（体量事实） |
| content_text | VARCHAR | 文本内容（UTF-8，照录不改字、不重排） |
| 幂等键 | — | (issue_id, archive_layer, file_name) |
| 约束 | — | **二进制禁入**：扩展名＋magic 头双判；命中即不入库并计入 `build_log` |

### ads（广告）

| 字段 | 类型 | 说明 |
|------|------|------|
| ad_id | BIGINT PK | 库内自增 |
| issue_id | BIGINT FK | → issues（广告必可归属到期） |
| article_id | BIGINT FK NULL | → articles（随文广告时填） |
| ad_text | VARCHAR | 文字广告全文（HTML 转文本） |
| figure_id | BIGINT FK NULL | → figures（整页/整幅图片广告时挂图） |
| ad_kind | VARCHAR | 侦察阶段定义的判别类目（文字栏/图片件/随文…，以侦察规则为准） |
| 幂等键 | — | (issue_id, ad_kind, coalesce(ad_text 首行, figure_id)) |

### figures（图片件处置台账）

| 字段 | 类型 | 说明 |
|------|------|------|
| figure_id | BIGINT PK | 库内自增 |
| issue_id | BIGINT FK | → issues |
| article_id | BIGINT FK NULL | → articles |
| image_name | VARCHAR | 图片名照录（如 `kanji-10pt.gif`；不含磁盘路径） |
| disposition | VARCHAR | transcribed / base64 / skipped / uncertain |
| disposition_reason | VARCHAR | 判别理由一句话（壳件、艺术照、含代码截图…） |
| transcription_text | VARCHAR | LLM 直转的图片内文字/代码（disposition=transcribed 时非空；LLM＝会话子代理读图，非本地模型） |
| base64_data | VARCHAR | 艺术图 base64 正文（disposition=base64 时非空） |
| image_format | VARCHAR | gif/jpg/png…（按 magic 头判，不信扩展名） |
| 幂等键 | — | (issue_id, image_name) |
| 约束 | — | transcribed 与 base64 互斥且必居其一（skipped/uncertain 除外）；`uncertain` 必须清零才算收口（SC-004） |

### build_log（建库留痕）

| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | BIGINT PK | 自增 |
| phase | VARCHAR | recon / extract / transcribe / ads / verify |
| batch | VARCHAR | 批次标识（如 `CUJ-1990-jan`） |
| note | VARCHAR | 追加式记账流水（处理数、跳过数、二进制命中数、异常） |
| logged_at | TIMESTAMP | UTC |

### refs（著录／文献综述原料；2026-10-05 修正新增）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR PK | 稳定号（如 `DDJ-1027`；按 article 建库顺序序生成） |
| article_id | BIGINT FK | → articles（每 article 恰一条） |
| bibliography_entry | VARCHAR | GB/T 7714 期刊著录：作者. 题名[J]. 刊名, 年(期). |
| journal_code | VARCHAR | ddj/cuj/sa/tpj |
| year | INTEGER | 出版年 |
| issue_label | VARCHAR | 期标识 |
| created_at | TIMESTAMP | UTC |
| 幂等键 | — | (article_id) |

### summaries（概述；schema 同 references_fulltext.summaries）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR PK | `sum-<db>-<seq>` |
| reference_id | VARCHAR | 指向本库 refs.id |
| summary | VARCHAR | 中文概述 3–6 句 |
| topic_keywords | VARCHAR | 顿号分隔关键词 |
| important_excerpts | VARCHAR | 原文摘引（照录） |
| processing_status | VARCHAR | success / pending |
| processed_at | VARCHAR | 处理日期 |
| 幂等键 | — | (reference_id) |

### key_facts（原料层；schema 同 references_fulltext.key_facts 12 列）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR PK | `kf-<db>-<ref>-<seq>` |
| reference_id | VARCHAR | 指向本库 refs.id（0 悬空硬约束） |
| fact_text | VARCHAR | 原子事实（中文） |
| fact_category | VARCHAR | 沿用既有类目（periodical_primary/core_claim/…） |
| source_quote | VARCHAR | 原文引文（照录） |
| source_block_id | VARCHAR NULL | 本库内定位（article_id 冗余可查） |
| related_people_ids / related_technology_ids / related_event_ids | VARCHAR NULL | 沿用既有 |
| confidence | VARCHAR | 0 信任评级 |
| related_chapter | VARCHAR NULL | 大纲归属（Phase C 写回，跟新不跟旧） |
| extracted_at | VARCHAR | 真实时间戳 |
| 幂等键 | — | (id)；(reference_id, fact_text) 查重 |

## Phase B 实体（2026-10-05 修正后）

原“入 references_fulltext.duckdb”阶段已删除——四库本身即全文库。Phase B＝按 references_fulltext 规则补齐上列 refs/summaries/key_facts 三表（构建规则见 research.md R7）。

## Phase C 实体（大纲两层）

| 实体 | 说明 |
|------|------|
| 卷末书目述评 bullet | `- **ref NNNN**｜…` 形式，追加宿主卷 `卷末书目述评.md`；has_block 幂等 |
| key_facts 行 | ref 关联＋关键事实文本；写后独立回读断言 |

## 实体关系

```text
journal_meta 1──* issues 1──* articles 1──* source_files（可空关联）
                  │            │
                  │            ├──* figures（图片处置台账）
                  │            └──* ads（figure_id 可空挂图）
                  └──* figures / ads（期级图片与广告）

四库 issues/articles/source_files/figures/ads
   ──Phase B──> references 著录 + fulltext_blocks + reference_update_log
   ──Phase C──> key_facts + 卷末书目述评 bullet（ref 回指著录，0 悬空）
```

## 校验规则（建库门禁）

1. 期覆盖：每刊库内 (year, issue_label) 集合＝磁盘实测集合（零遗漏零多出）。
2. 文章覆盖：抽样期库内 articles 数＝articles 树实测文章数。
3. 正文保真：抽样文 body_text 与源页转文本逐字一致。
4. 代码保真：抽样期 source_files 与解压文件逐字一致。
5. 二进制零命中：全库文本列无二进制特征（magic 头、NUL 字节）。
6. 图片台账：figures 无悬空（transcribed/base64 二选一），uncertain=0。
7. 幂等：全链重跑 0 新增 0 重复。
