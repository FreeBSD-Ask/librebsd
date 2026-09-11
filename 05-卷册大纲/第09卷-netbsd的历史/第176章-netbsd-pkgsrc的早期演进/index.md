---
chapter: 第 176 章
id: CH176
volume: 第09卷-netbsd的历史
---

# 第 176 章 netbsd-pkgsrc的早期演进

## 要点

- NetBSD 仓库构成：netbsd-pkgsrc(1225351)、netbsd-src(774061)。pkgsrc 提交量占比最大，与 FreeBSD Ports 形成镜像

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3994] 卷“第09卷-netbsd的历史”第 176 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_3995] 卷“第09卷-netbsd的历史”第 176 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:netbsd.duckdb] NetBSD 仓库构成：netbsd-pkgsrc(1225351)、netbsd-src(774061)。pkgsrc 提交量占比最大，与 FreeBSD Ports 形成镜像

## 史观

- 形式主义：pkgsrc 是‘跨平台软件包管理’的形式主义解决方案，与 FreeBSD Ports 形成镜像

## 辨析

- 移植的具体范围需考据——FreeBSD Ports 与 pkgsrc 的代码 diff 需对照源码核实。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：pkgsrc 早期发展实际涉及两位核心贡献者——agc（Alistair G. Crooks）1997-06-05 首次导入 FreeBSD packaging tool（pkg_install），1997-08-20
- commit 记录的完整性需考据——部分 commit 可能未完整记录；需对照多源档案核实。统计结论 [C-13] 局限性继承：netbsd-src 月度 commit 量 Pettitt 检验变点为 2012-04、BUISHAND R 检验变点为 2011-09（10,000 次 Monte Carlo），两检验变点年份均晚于本章覆盖时期（1997-2004）约 7-8 年，反映本章时期的 c
- OpenBSD Ports 与 pkgsrc 的分化时间需考据——OpenBSD 1996 年 7 月 fork 后软件包管理何时完全独立需对照 commit log 核验；OpenBSD 1.1 CVS 标签日期（1995.10.18）与 OpenBSD 1.2 首次正式发行日期（1996.7）在不同来源中混用，需对照 OpenBSD 官方发布档案进一步核验。经 netbsd.duckdb o
- 不可断言 pkgsrc “优于” RPM/DEB——二者服务不同生态（BSD 跨平台 vs Linux 发行版分发）。
- CVE-2002-0429 的 CVE 编号年份（2002）与修复 commit 日期（2004-03-11）相差近 2 年，反映该漏洞可能在 2002 年即被披露但修复延迟至 2004 年，或 CVE 编号系事后回溯分配——具体时序须对照 NetBSD-SA 公告与 NVD 条目核验；httpd 漏洞群（CVE-2006-2937/2940/3738/4343）由同一 commit `897b3

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 netbsd.duckdb