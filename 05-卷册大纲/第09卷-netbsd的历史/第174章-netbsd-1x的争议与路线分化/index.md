---
chapter: 第 174 章
id: CH174
volume: 第09卷-netbsd的历史
---

# 第 174 章 NetBSD 1.x 的争议与路线分化

## 要点

- 合图层从项目史观总纲第 13、19、21 条切入审视争议。批评方与反批评方的前理解不可通约——批评方以“桌面市场份额与 x86 性能”为前理解，反批评方以“可移植性与嵌入式定位”为前理解，两种前理解各成自洽的逻辑闭环，争议在解释学循环中不可避免地走向不可调和。合图层承认这一不可调和性而非以“折中”叙事消解分歧——NetBSD 与 FreeBSD 的路线分化是 BSD 家族“分离聚合律”的具象呈现。
- Theo de Raadt（西奥·德·若特）作为 NetBSD 创始成员之一，1994.12.23 被 Core Team 以“沟通风格问题”为由通过投票撤销 commit 权限；de Raadt 此后无法继续贡献 NetBSD，1995 年下半年开始筹备 fork，1996 年 7 月正式发布 OpenBSD 1.2（首个正式发行版）；OpenBSD 从 NetBSD 1.0 代码基础 fork 而来，此后沿可移植性与代码质量路线独立演进。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3992] 卷“第09卷-netbsd的历史”第 174 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4011] 卷“第09卷-netbsd的历史”第 174 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲映射：第 4 条（分离聚合是永恒规律）——NetBSD 与 FreeBSD 的路线分化及 OpenBSD 的 fork 是 BSD 家族分离聚合循环的具象；第 5 条（没有必然性，只有偶然性）——撤权决议与 fork 启动系治理冲突与具体人事交织的偶然条件，非技术演进的必然环节；第 8 条（本体论上各方平等）——NetBSD 与 OpenBSD 作为分支在本章平等呈现，不以胜负优劣论；第 13 条（法律与道德是利益分配）——commit 权限撤销与“沟通风格”叙事的背后是项目治理规则的权责分配；第 19 条（解释学循环是历史认识的根本条件）——批评方与反批评方前理解不可通约，争议在各自的解释学循环中自洽；第 21 条（革命与改革是历史方法论的分歧）——fork 出走与留在项目内改革构成路线方法论分歧的两种形态。各子节文件的史观/辨析字段为本章合图层提供分论支撑。

## 辨析

- 考据过程留痕——【查证来源】合图层的史观审视基于现有公开史料（NetBSD 官方文档、FreeBSD 4.0 公告、netbsd.duckdb commit 量数据）与项目史观总纲第 13、19、21 条；【交叉验证方法】NetBSD 1.5/1.6 公告中的嵌入式平台支持（Dreamcast、Zaurus、Cobalt 等）与 NetBSD history.html 的“quality and architecture independence”（质量与架构独立性）表述相互印证——该页明言“FreeBSD was formed later with a focus on the i386 PC platform”（FreeBSD 稍后成立，聚焦 i386 PC 平台），与本章 NetBSD、FreeBSD 两路线分化的叙事相合。
- 撤权的具体原因在不同叙事中差异较大——部分归因于沟通风格，部分归因于技术分歧，部分归因于项目治理分歧；OpenBSD 首次正式发布日期在不同叙事中存在分歧——部分早期资料误作 1996.5，部分资料区分 OpenBSD 1.1 CVS 标签（1995.10.18）与 OpenBSD 1.2 首次正式发行（1996.7），需对照 OpenBSD 官方档案进一步核验。经 **netbsd.duckdb** 提交记录核查，de Raadt 在 netbsd-src 仓库的末条 commit 为 1994-12-17T23:12:41Z（699d2a37b0e3），其在 openbsd-src 仓库的首条 commit 为 1995-10-18T08:37:01Z（df930be708d5），两条时间线与“撤权—筹备 fork—首次发行”的叙事相合。

## 文献

- NetBSD Project. About NetBSD [EB/OL]. <https://www.netbsd.org/about/>；NetBSD Project. History of the NetBSD Project [EB/OL]. <https://www.netbsd.org/about/history.html>；NetBSD Foundation. NetBSD 1.5 Release Announcement [EB/OL]. 2000-12-06. <https://www.netbsd.org/releases/formal-1.5/NetBSD-1.5.html>；NetBSD Foundation. NetBSD 1.6 Release Announcement [EB/OL]. 2002-09-14. <https://www.netbsd.org/releases/formal-1.6/NetBSD-1.6.html>；Jordan K. Hubbard. FreeBSD 4.0-RELEASE Announcement [EB/OL]. 2000-03-14. <https://www.freebsd.org/releases/4.0R/announce/>；**02-sacred源材料/sacred_sources.duckdb** 项目统摄史观第 25 章（总纲第 13、19、21 条）；**02-sacred源材料/sacred_sources.duckdb** 项目统摄史观第 11 章（法哲学与政治历史哲学）；**02-sacred源材料/sacred_sources.duckdb** 项目统摄史观第 19 章（历史解释学与权力）；**02-sacred源材料/sacred_sources.duckdb** 项目统摄史观第 21 章（革命与改革：历史方法论） ［A］<!-- foundation-writeback: NetBSD Foundation | NetBSD Foundation 政策文件 -->**NetBSD Foundation 史料**（NetBSD Foundation 政策文件，下载日期 2026-07-26）：
- de Raadt 撤权事件档案；OpenBSD 创建史料；BSD fork 史研究；OpenBSD 官方 changelog（<https://www.openbsd.org/plus.html>）；deraadt 在 netbsd-src 末条 commit. netbsd-src 仓库 [DB/OL]. 1994-12-17T23:12:41Z. commit: 699d2a37b0e3；deraadt 在 openbsd-src 首条 commit. openbsd-src 仓库 [DB/OL]. 1995-10-18T08:37:01Z. commit: df930be708d5；deraadt 在 openbsd-src 当日连续 commit. openbsd-src 仓库 [DB/OL]. 1995-10-18T08:37:01Z—12:22:00Z. commits: df930be708d5, 23993aedadda, 70e96dcb50e3 等 ［A］<!-- foundation-writeback: NetBSD Foundation | NetBSD Foundation 历年财务报告（2004-2025） -->**NetBSD Foundation 史料**（NetBSD Foundation 历年财务报告（2004-2025），下载日期 2026-07-26）：

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

