# CVS 手册“What is CVS?”页（新 ref）引用卡

- **性质**：gnu.org 上《CVS—Concurrent Versions System v1.11.23》手册 1.1 节 “What is CVS?”（Cederqvist 等）；本机 Chrome UA curl 200
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b002；source_url 四键查重无重合，库内 cvs 手册零命中）
- **source_url**：https://www.gnu.org/software/trans-coord/manual/cvs/html_node/What-is-CVS_003f.html
- **quote（逐字，两处）**：
  1. CVS stores all the versions of a file in a single file in a clever way that only stores the differences between versions.
  2. CVS solves this problem by insulating the different developers from each other. Every developer works in his own directory, and CVS merges the work when each developer is done.
- **考据注**：第 1 句给存储形态（单个文件＋只存版本间差异），第 2 句给协作模型（隔离＋完成时合并）。**同页另有一段沿革**（Dick Grune 1986 年发表到 comp.sources.unix 的 shell 脚本；1989 年 4 月 Brian Berliner 设计并实现 CVS），本批未取——2.7.3 题面只问“集中式协作模型”，沿革留给 2.7.2／2.7.3 需要时再取，且同一 ref 同页可另引不同句。**注意**：第 2 句原文作 “his own directory”，为原文本用词，照录不改写为中性表述
- **本批落点**：V34.2.7.3 第 1、2 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b002；official_doc／L3）
