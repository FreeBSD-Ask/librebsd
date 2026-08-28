---
chapter: 第 139 章
id: CH139
volume: 第07卷-freebsd的工程体系重构
---

# 第 139 章 freebsd网络栈的tcpip谱系与kame-ipv6

## 要点

- BSD TCP/IP 实现的一手史料包括 CSRG 发布的 4.2BSD（1983）、4.3BSD（1986）、4.4BSD-Lite（1994）磁带和源码光盘（部分可在 TUHS 档案馆获取）；FreeBSD 源码仓库（cgit.freebsd.org）完整记录了从 1994 年至今的每一次网络栈代码变更，是研究网络栈演进的一手史料；二手史料中 McKusick 等人的两版 *The Desig
- netgraph 早期设计史料包括 Julian Elischer 和 Archie Cobbs 在 freebsd-current 和 freebsd-net 邮件列表上的设计讨论（1997-1999 年）、初始 commit 日志、两人在 BSDCon 1999/2000 的演讲；netgraph 最初设计目的之一是替代当时繁琐的 PPP 和拨号网络配置，为 Whistle InterJet
- if_bridge 从 NetBSD 移植的精确时间——FreeBSD 5.2（2004 年 1 月）是首个包含 if_bridge 的版本，但代码导入时间约为 2003 年下半年；if_lagg 初始开发者——Mykola Dzham 完成了初始实现，Andrew Thompson 做了大量代码审查和 LACP 完善；早期 FreeBSD 网桥历史的一手资料较为分散——FreeBSD 2.x-4
- VNET 开发的一手史料包括 TrustedBSD 项目的技术报告（2006-2009）、罗伯特·N. M. 沃森 和 Bjoern Zeeb 在 freebsd-jail 和 freebsd-net 邮件列表的设计讨论、FreeBSD 源码仓库 sys/net/vnet.c 的提交历史；VNET 从实验性到稳定经历了约 7 年（2009-2016），核心挑战包括：① 将内核中数百个全局网络变量标

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1138] 卷“第07卷-freebsd的工程体系重构”第 139 章，匹配置信度 0.5，原因：关键词匹配: atlas shrugged
- [DB:bsdnow_podcast:outline_mappings:om_11515] BSD Now 第 528 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12363] BSD Now 第 435 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12614] BSD Now 第 404 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12635] BSD Now 第 401 期，匹配 CH139 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10424] BSD Now 第 676 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10441] BSD Now 第 674 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10631] BSD Now 第 638 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10690] BSD Now 第 630 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10729] BSD Now 第 624 期，匹配 CH139 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10763] BSD Now 第 618 期，匹配 CH139 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 需纠正几个常见史实错误：① “FreeBSD 网络栈来自 386BSD”——386BSD 0.1（1992）确实包含网络栈，但 FreeBSD 在 1994 年 2.0 版本就完整迁移到了 4.4BSD-Lite 代码基，此后网络栈直接演进自 CSRG 代码而非 Jolitz 的 386BSD 代码；② “**sendfile(2)** 是 Linux 发明”——错误，**sendfile(2)*
- netgraph 引入版本先前多处误写为 FreeBSD 3.0（1998-10），经 FreeBSD 3.4 Release Notes 一手核验，正确版本为 FreeBSD 3.4（1999-12）；先前误将 Archie Cobbs 记为唯一设计者，实际是 Julian Elischer 与 Archie Cobbs 两人共同设计，Elischer 是长期主要维护者；Cobbs 在 2000
- FreeBSD 网桥历史常被简化为“if_bridge 一直存在”——实际上在 5.2 之前 FreeBSD 缺少原生内核网桥，这是一个重要的史实修正；**brconfig(8)** 命令在 FreeBSD 8 之后被 ifconfig bridge 取代，成为历史遗留命令；部分文档提到的"if_trunk"是 OpenBSD 的链路聚合接口名，不是 FreeBSD 的
- VIMAGE 选项改名——VNET 框架在内核配置中最初名为 options VIMAGE，后来虽框架改名 VNET 但内核选项名保留为 VIMAGE 以避免破坏现有配置，这是一个“历史遗留命名”的小案例；Bjoern Zeeb 在 VNET 开发中的角色常被低估——Watson 是项目领导者，但 Zeeb 完成了大量实际代码实现和 vnet 化改造工作；VNET 第一个正式生产就绪声明是在 Fr

## 文献

- The Unix Heritage Society. *BSD Source Archives*. tuhs.org; FreeBSD Project. *Source Repository*. cgit.freebsd.org; Greenman, D. (1997). *sendfile(2) System Call Commit*. svn.freebsd.org revision history; Salus, P. H. (1994). *A Quarter Century of UNIX*. Addison-Wesley. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Net Mailing List Archives. (1997-1999). *Netgraph Design Threads*. freebsd.org; Elischer, J., & Cobbs, A. L. (1999). *Netgraph: A Network Graphing Subsystem for FreeBSD*. BSDCon '99 Proceedings; FreeBSD Project. *sys/netgraph/ Source Code History*. cgit.freebsd.org. ［D］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1999-1999 年间：23,839 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. *sys/net/if_bridge.c, sys/net/if_lagg.c Commit History*. cgit.freebsd.org; Thompson, A. (2007). *if_lagg Link Aggregation Driver Commit*. svn.freebsd.org; FreeBSD Net Mailing List. (2003-2008). *Bridge and LAGG Discussions*. freebsd.org. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Watson, R. N. M., & Zeeb, B. (2006-2016). *VNET Commit History*. svn.freebsd.org/cgit.freebsd.org; TrustedBSD Project. (2009). *VNET Technical Report*. trustedbsd.org; FreeBSD 相关记录（详情见存疑库）。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 提及 McKusick, Marshall Kirk，作为 BSD 的核心人物，其撰写的 BSD 历史与 Unix 传奇是该领域的重要参考文献。**新增技术**文献 (06771908, 年份不详) 讨论 swap，该论文讨论了 Unix 早期进程间通过显式交换（swap）传递数据的机制，为理解 BSD 内存管理演进提供了历史背景。文献 (06771908, 年份不详) 讨论 UFS，该论文追溯了 PDP-7 Unix 文件系统的结构，为理解 BSD UFS 文件系统的设计起源提供了历史视角。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 讨论 TCP/IP，Bill Joy 为 Unix 添加了 vi 编辑器和 csh，并引入了改变世界的 TCP/IP 协议 socket 接口，这些贡献是 BSD 对互联网基础设施的奠基性工作。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 讨论 macOS，Unix 核心命令在 Linux、macOS 和 Windows Subsystem for Linux 中仍然广泛使用，体现了 BSD/Unix 技术的跨平台生命力。文献 (eurobsdcon2015-portroach, 年份不详) 讨论 OpenBSD，Jasper Lievisse Adriaanse 开发的 Portroach 是 OpenBSD 的 distfile 扫描工具，用于监控上游软件版本更新。文献 (eurobsdcon2015-portroach, 年份不详) 讨论 Ports Collection，Portroach 工具的设计灵感来自 FreeBSD 的 portscout，用于追踪 Ports Collection 中软件包的上游版本变化。**新增时间线事件**文献 (06771908, 年份不详) 记录 1980：Springer-Verlag 于 1980 年出版了关于设计与编程方法论的著作，为 Unix 系统设计提供了理论基础。文献 (06771908, 年份不详) 记录 1980：该文献引用了 1980 年关于 Unix 系统演进的学术出版物。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 记录 1980：Bjarne Stroustrup 于 1980 年将 Simula 的面向对象特性与 C 语言融合，诞生了"带类的 C 语言"，即 C++ 的前身。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 记录 1980：贝尔实验室 1127 中心于 1980 年开设了为期 3 周的集成电路设计速成课程，由加州理工学院的 Carver Mead 授课。文献 (eurobsdcon2015-portroach, 年份不详) 记录 2006：Jasper Lievisse Adriaanse 自 2006 年起成为 OpenBSD 开发者，专注于 GNOME 移植和 Puppet 配置管理。文献 (eurobsdcon2015-portroach, 年份不详) 记录 2012：FreeBSD 的 portscout 工具于 2012 年引起 OpenBSD 开发者的关注，启发了 Portroach 的开发。
<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第139章-freebsd网络栈的tcpip谱系与kame-ipv6 第 139 章 freebsd网络栈的tcpip谱系与kame-ipv6（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：13632 条 -->

### 要点（播客口述史提取）
- And wow, they announced, let's see, FreeBSD5 with the jail commands, the management commands.（BSD Now EP149 @ 2064.819）
- And then they've also got a new project started, Getting Started with FreeBSD, which is the foundation hired an intern for the summer.（BSD Now EP149 @ 6788.140）
- At IX, we made the conscious decision to base FreeNAS and TrueOS on the FreeBSD operating（BSD Now EP242 @ 1258.4）
- FreeBSD network stack ported to userland on FreeBSD and allows you to use it as a library.（BSD Now EP242 @ 821.36）
- According to Wikipedia, Apple began using FreeBSD instead of NetBSD for macOS 10.3.（BSD Now EP273 @ 1951.94）

### 史料（播客当事人陈述）
- Today, Alan sits as a FreeBSD project committer and core member.（BSD Now EP149 @ 1014.319）
- If you do, you need to use that coupon code freeBSDnow, which is going to give you that $10 credit, which is good for running basically two months of their lower-end VM, which for a low-end VM still kicks a lot of butt because we're talking SSD-backed, terabyte of transfer a month, access to all the nice control panels and UI utilities they have in their HTML5 interface.（BSD Now EP149 @ 1574.079）
- Ed and Konstantin Belisov wrote about the FreeBSD virtual memory system.（BSD Now EP149 @ 6537.519）
- And they talk a bit about BSDCAN was also where the FreeBSD Foundation（BSD Now EP149 @ 6654.199）

### 史观（播客当事人观点与总纲映射）
- （该章节匹配播客中未提取到当事人观点性陈述）

### 辨析（播客争议与存疑点）
- [存疑脚注] And if you're using FreeBSD secure levels, you can actually make it so the flag can't be removed（BSD Now EP39 @ 3676.899）

### 文献（播客参考条目）
- [BSD Now EP149] Pennington J. BSD Now: 149: The bhyve has been disturbed, and a wild Dexter appears![EB/OL]. (2016-07-06)[2026-08-15]. https://www.bsdnow.tv/149.
- [BSD Now EP242] Pennington J. BSD Now: Episode 242: Linux Takes The Fastpath | BSD Now 242[EB/OL]. (2018-04-18)[2026-08-15]. https://www.bsdnow.tv/242.
- [BSD Now EP273] Pennington J. BSD Now: Episode 273: A Thoughtful Episode | BSD Now 273[EB/OL]. (2018-11-23)[2026-08-15]. https://www.bsdnow.tv/273.
- [BSD Now EP276] Pennington J. BSD Now: Episode 276: Ho, Ho, Ho - 12.0 | BSD Now 276[EB/OL]. (2018-12-13)[2026-08-15]. https://www.bsdnow.tv/276.
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.
- [BSD Now EP3] Pennington J. BSD Now: 3: MX with TTX[EB/OL]. (2013-09-18)[2026-08-15]. https://www.bsdnow.tv/3.
- [BSD Now EP39] Pennington J. BSD Now: 39: The Friendly Sandbox[EB/OL]. (2014-05-28)[2026-08-15]. https://www.bsdnow.tv/39.
- [BSD Now EP47] Pennington J. BSD Now: 47: DES Challenge IV[EB/OL]. (2014-07-23)[2026-08-15]. https://www.bsdnow.tv/47.

<!-- /PODCAST_MINE -->
