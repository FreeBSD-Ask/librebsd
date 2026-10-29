# 功能库第二批行级遍历考据：references_fulltext

日期：2026-08-31
Spec：db-row-traversal-mining-2026-08-29（Phase 2A 收官）

## 查证来源

- references_fulltext.duckdb 13 表（key_facts 2325 / timeline_events 27138 / chapter_reviews 355 / summaries 1809 / chapter_matches 2569 / fulltext 4077 / fulltext_blocks 992226 / references 4803 / people_mentioned 7785 / technologies_mentioned 13371 / reference_duplicates 826 / reference_update_log 1545 / schema_meta 9）
- 核心事实类目导出 _dump_rf_keyfacts_core.jsonl（387 行）逐行过目
- 去重查证：historical_claims 只读查询（92-1667/USL 已覆盖去重；chroot 1982-03-18、90% committers、阮一峰、copycenter、Forbes 引语均零命中）
- 产物：claims_to_write_references_fulltext.jsonl（5 条，CL-RM-002001~002005），已逐条写入并回读校验

## 交叉验证方法

1. key_facts 按类分层：核心事实类目（architecture/design/origin/legal/lineage/event/culture/criticism/governance/interpretation/quote-kaoju/timeline，387 行）逐行精读；person（139 行 `X mentioned (N times)` 提及计数）、version（178 行版本提及）、technology（1418 行提及计数）、bibliographic（492 行著录）为登记型。
2. quote-kaoju 17 行（fid=2350/2354）为项目既有引语考据成果：无源引文判定（穷尽检索 2019 bsdcn/AxialCorps 2013/FOSDEM 2019）、不可信文献判定（阮一峰 2010，6 处硬性错误 + 引用链污染）与一手引语定位（Forbes 2005-06-16、sendmail.net 1999/BSDCon 1999、Meta Magazine 1993）——本次采纳其防错与定位结论，quote 取源行 source_quote 同串。
3. timeline_events 27138 行 event_type 全量为 mention（年份提及 + 上下文片段，抽样 6 行确认为文献出版/引用信息而非独立事件），与人名/技术提及同构，判登记型。
4. 大表（fulltext_blocks 99.2 万等）按 research_notes 先例抽样核验判登记型（文献原文切块/OCR 全文/著录登记）。

## 存疑判定依据

- pk=8341（Apple 上游回馈精确数字）与 pk=8348/8351~8353（出处待核实引语）：源行已标存疑，按宁缺毋滥不入主张，留在大纲引语考据层。
- USL v. BSDi 案号（92-1667）：historical_claims 已有同事实主张与证据（claim=1/evidence=2），按跨源去重跳过。
- timeline_events 中少量具体日期行（如 FreeBSD 3.0-RELEASE 1998-10-16）为 source_quote 携带信息，fact_text 为提及型，且相应版本日期已由既有主张或标准史实覆盖，不单独入库。
- 本批无新增 unresolvable 项。
