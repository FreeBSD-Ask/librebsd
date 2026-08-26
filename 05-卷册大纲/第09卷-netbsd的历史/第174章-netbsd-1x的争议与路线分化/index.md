---
chapter: 第 174 章
id: CH174
volume: 第09卷-netbsd的历史
---

# 第 174 章 netbsd-1x的争议与路线分化

## 要点

- 合图层从项目史观总纲第 13、19、21 条切入审视争议。批评方与反批评方的前理解不可通约——批评方以“桌面市场份额与 x86 性能”为前理解，反批评方以“可移植性与嵌入式定位”为前理解，两种前理解各成自洽的逻辑闭环，争议在解释学循环中不可避免地走向不可调和。合图层承认这一不可调和性而非以“折中”叙事消解分歧——NetBSD 与 FreeBSD 的路线分化是 BSD 家族“分离聚合律”的具象呈现，
- Theo de Raadt（西奥·德·若特） 作为 NetBSD 创始成员之一，1994.12.23 被 Core Team 以“沟通风格问题”为由通过投票撤销 commit 权限；de Raadt 此后无法继续贡献 NetBSD，1995 年下半年开始筹备 fork，1996 年 7 月正式发布 OpenBSD 1.2（首个正式发行版）；OpenBSD 从 NetBSD 1.0 代码基础 for

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3992] 卷“第09卷-netbsd的历史”第 174 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4011] 卷“第09卷-netbsd的历史”第 174 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 考据过程留痕——【查证来源】合图层的史观审视基于现有公开史料（NetBSD 官方文档、FreeBSD 4.0 公告、bsd_commits.db commit 量数据）与项目史观总纲第 13、19、21 条；【交叉验证方法】NetBSD 1.5/1.6 公告中的嵌入式平台支持（Dreamcast、Zaurus、Cobalt 等）与 NetBSD history.html 的"architectur
- 撤权的具体原因在不同叙事中差异较大——部分归因于沟通风格，部分归因于技术分歧，部分归因于项目治理分歧；OpenBSD 首次正式发布日期在不同叙事中存在分歧——部分早期资料误作 1996.5，部分资料区分 OpenBSD 1.1 CVS 标签（1995.10.18）与 OpenBSD 1.2 首次正式发行（1996.7），需对照 OpenBSD 官方档案进一步核验。经 bsd_commits.db 

## 文献

- NetBSD Project. About NetBSD [EB/OL]. <https://www.netbsd.org/about/>；NetBSD Project. History of the NetBSD Project [EB/OL]. <https://www.netbsd.org/about/history.html>；NetBSD Foundation. NetBSD 1.5 Release Announcement [EB/OL]. 2000-12-06. <https://www.netbsd.org/releases/formal-1.5/NetBSD-1.5.html>；NetBSD Foundation. NetBSD 1.6 Release Announcement [EB/OL]. 2002-09-14. <https://www.netbsd.org/releases/formal-1.6/NetBSD-1.6.html>；Jordan K. Hubbard. FreeBSD 4.0-RELEASE Announcement [EB/OL]. 2000-03-14. <https://www.freebsd.org/releases/4.0R/announce/>；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13、19、21 条）；原材料/哲学/项目统摄史观/第 11 章.md（法哲学与政治历史哲学）；原材料/哲学/项目统摄史观/第 19 章.md（历史解释学与权力）；原材料/哲学/项目统摄史观/第 21 章.md（革命与改革：历史方法论） ［A］<!-- foundation-writeback: NetBSD Foundation | NetBSD Foundation 政策文件 -->**NetBSD Foundation 史料**（NetBSD Foundation 政策文件，下载日期 2026-07-26）：
- de Raadt 撤权事件档案；OpenBSD 创建史料；BSD fork 史研究；OpenBSD 官方 changelog（<https://www.openbsd.org/plus.html>）；deraadt 在 netbsd-src 末条 commit. netbsd-src 仓库 [DB/OL]. 1994-12-17T23:12:41Z. commit: 699d2a37b0e3；deraadt 在 openbsd-src 首条 commit. openbsd-src 仓库 [DB/OL]. 1995-10-18T08:37:01Z. commit: df930be708d5；deraadt 在 openbsd-src 当日连续 commit. openbsd-src 仓库 [DB/OL]. 1995-10-18T08:37:01Z—12:22:00Z. commits: df930be708d5, 23993aedadda, 70e96dcb50e3 等 ［A］<!-- foundation-writeback: NetBSD Foundation | NetBSD Foundation 历年财务报告（2004-2025） -->**NetBSD Foundation 史料**（NetBSD Foundation 历年财务报告（2004-2025），下载日期 2026-07-26）：
