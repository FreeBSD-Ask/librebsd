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
- Watson, R. N. M., & Zeeb, B. (2006-2016). *VNET Commit History*. svn.freebsd.org/cgit.freebsd.org; TrustedBSD Project. (2009). *VNET Technical Report*. trustedbsd.org; FreeBSD Release Engineering Team. (2016-10). *FreeBSD 11.0 Release Notes* (VNET production-ready). freebsd.org. ［A］**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=38）---**补充证据（基于全文数据库修订）**本次修订从全文数据库补充 8 篇新匹配文献的证据。**新增核心事实**文献 (06771908, 年份不详, p.4) 指出：UFS mentioned (4 times)。文献 (06771908, 年份不详, p.4) 指出：swap mentioned (6 times)。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详, p.34) 指出：Joy, Bill mentioned (3 times)。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详, p.34) 指出：McKusick, Marshall Kirk mentioned (2 times)。文献 (eurobsdcon2015-portroach, 年份不详, p.1) 指出：OpenBSD mentioned (10 times)。文献 (eurobsdcon2015-portroach, 年份不详, p.1) 指出：Ports Collection mentioned (6 times)。**新增人物**文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 提及 Joy, Bill，、格雷丝• 埃姆林（Grace Emlin）、马亚• 哈明（Maia Hamin）、 比尔• 乔伊（Bill Joy）、马克• 克尼汉（Mark Kernigh……。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 提及 McKusick, Marshall Kirk，尔实验室的主页被保留了下来，在其 上面有丹尼斯写的大部分论文和其他历史资料的链接。 柯克·麦库西克（Kirk McKusick）是BSD 的核心人物，他写了一 ……。**新增技术**文献 (06771908, 年份不详) 讨论 swap，as passed between processes only when an explicit swap took place. So, for examp……。文献 (06771908, 年份不详) 讨论 UFS，ing system we know today was born. III. THE PDP-7 UNIX FILE SYSTEM Structurally,……。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 讨论 TCP/IP，尔• 乔伊的 人为Unix 添加了vi 文本编辑器和C 语言的shell、csh，再加上改变世 界的TCP/IP 协议的socket 接口……这帮“超级英雄”编……。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 讨论 macOS，少的可选（也许并不必 要的）参数，修改了其操作行为，它仍然是Unix 核心命令之一。在 Linux、macOS 或Windows Subsystem for L……。文献 (eurobsdcon2015-portroach, 年份不详) 讨论 OpenBSD，Portroach, OpenBSD distﬁle scanner Jasper Lievisse Adriaanse。文献 (eurobsdcon2015-portroach, 年份不详) 讨论 Ports Collection，[Introduction] Who am I? ▶jasper@ since 2006 ▶ports ▶GNOME ▶Puppet ▶OpenBSD/octe……。**新增时间线事件**文献 (06771908, 年份不详) 记录 1980：ign and Programming Methodology, Springer-Verlag, 1980. I. INTRODUCTION During the past few years, t。文献 (06771908, 年份不详) 记录 1980：ign and Programming Methodology, Springer-Verlag, 1980. I. INTRODUCTION During the past few years, t。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 记录 1980：并不能真正满足他的需求。因此，他从最接近需求的 Simula a 中汲取养分，并将其与C 语言融合。1980 年，面向对象编程思想 与C 语言的效率和表现力相结合，结果得到了一种“带类的C 语言”。。文献 (UNIX 传奇：历史与回忆 ([美]布莱恩·W.克尼汉（BrianW.Kernighan）) (z-library.sk, 年份不详) 记录 1980：还在优先使用：这本书就是 用它写的。 人们对集成电路和VLSI（超大规模集成电路）也有持续的兴趣。 1980 年，1127 中心开设了为期3 周的集成电路设计速成课程，由加 利福尼亚理工学院的卡弗·米。文献 (eurobsdcon2015-portroach, 年份不详) 记录 2006：[Introduction] Who am I? ▶jasper@ since 2006 ▶ports ▶GNOME ▶Puppet ▶OpenBSD/octeon。文献 (eurobsdcon2015-portroach, 年份不详) 记录 2012：tt ▶portscout.freebsd.org ▶Jaleous looks at it in 2012。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
