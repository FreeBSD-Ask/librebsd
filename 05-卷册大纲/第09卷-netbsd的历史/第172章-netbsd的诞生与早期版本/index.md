---
chapter: 第 172 章
id: CH172
volume: 第09卷-netbsd的历史
---

# 第 172 章 netbsd的诞生与早期版本

## 要点

- NetBSD 时间跨度（1992-07-13 至 2026-08-24），始于 1992 年，早于 FreeBSD/OpenBSD 的代码仓库起点

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3695] 卷“第09卷-netbsd的历史”第 172 章，匹配置信度 folder，原因：folder 第170章
- [DB:references_fulltext:chapter_matches:chmatch_3696] 卷“第09卷-netbsd的历史”第 172 章，匹配置信度 folder，原因：folder 第170章
- [DB:references_fulltext:chapter_matches:chmatch_3877] 卷“第09卷-netbsd的历史”第 172 章，匹配置信度 folder，原因：folder 第170章
- [DB:references_fulltext:chapter_matches:chmatch_4007] 卷“第09卷-netbsd的历史”第 172 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:netbsd.duckdb] NetBSD 时间跨度（1992-07-13 至 2026-08-24），始于 1992 年，早于 FreeBSD/OpenBSD 的代码仓库起点

## 史观

- 形式主义：NetBSD 的历史是‘可移植性’这一形式主义概念在不同硬件平台上的物质化

## 辨析

- 分叉动机在不同叙事中差异较大——部分归因于技术分歧，部分归因于个人冲突；需对照原始邮件存档核实。经 netbsd.duckdb netbsd-src 仓库 commits 表验证，Chris Demetriou（cgd）与 Theo de Raadt（deraadt）的首批 commit 时间戳（1993-03-21 与 1993-04-02）与 NetBSD 1993.4 创建公告时间高度吻合，可作为分叉时间线的锚点证据，但分叉动机的定性仍须以原始邮件存档为准 [存疑脚注：分叉动机（技术分歧抑或个人冲突）缺乏当事人一致表述，须核验原始邮件存档后方可定谳]
- **history.html** 载明四位创始人（Demetriou、de Raadt、Glass、Hannum），与 171.1 节既有考据一致；**openbsd-faq1.html** 为简介页（不含分裂详述），分裂事件详述以 **netbsd-history.html** 与 171.3 节考据为准；**formal.html** 为版本历史列表（0.8 1993-04-20 起），与 171.1 节版本时间线表一致
- 文档与源码的一致性需考据——部分文档可能滞后于源码；需对照多源档案核实
- 撤权的具体日期与原因在不同叙事中差异较大——本节叙事采用 1994.12.23 决议日期（NetBSD Core Team 公开记录口径），但部分二手叙事误作 1995 年 12 月；撤权原因部分归因于沟通风格，部分归因于技术分歧，部分归因于项目治理分歧，需对照原始邮件存档核验。经 **netbsd.duckdb** netbsd-src 仓库 commits 表验证：deraadt 末条 commit 落于 1994-12-17（commit `699d2a37b0e3c0c6ff29ea0d407c3feeba5642b4`），早于 1994.12.23 撤权决议 6 天（对照 **bsd_commits.db** commit 时间线）[存疑脚注：撤权具体日期与原因在不同叙事中存在分歧，本处采 NetBSD Core Team 公开记录口径，二手叙事之 1995 年 12 月说待原始邮件存档定谳]
- 【交叉验证方法】OpenBSD fork 与 DragonFly fork 的比较以 **bsd_commits.duckdb** commits 表为代码级证据基础，结合两人 fork 前后 commit 时间线、fork 动机（人际冲突 vs 技术分歧）

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 netbsd.duckdb