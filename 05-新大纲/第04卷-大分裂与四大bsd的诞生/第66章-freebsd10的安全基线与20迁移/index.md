---
chapter: 第 66 章
id: CH66
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 66 章 freebsd10的安全基线与20迁移

## 要点

- FreeBSD 2.0（1994-11-22 网络公告，12 月 CD-ROM 分发）是首个完全基于 4.4BSD-Lite 的版本，消除 Net/2 争议代码的法律风险，同时引入 4.4BSD-Lite 的新安全机制——securelevel 内核安全等级机制（level 0 不安全模式、level 1 安全模式禁止 `/dev/mem` 访问与原始磁盘写入并强制 **chflags(2)**
- FreeBSD 1.x 版本周期内仅有的安全响应（2 条 isprint() 修复 commit）与回溯影响的栈溢出漏洞（FreeBSD-SA-96:20）共同反映 FreeBSD 1.x 安全基线的架构性缺陷——FreeBSD 1.0 基于 Net/2（4.3BSD 网络栈），未引入 securelevel 内核安全等级机制（securelevel 于 4.4BSD-Lite 引入，FreeBS
- 综合四层辩证，FreeBSD 从 386BSD patchkit fork 争议不能简化为 “窃取 vs 自救” 或 “合法 vs 不道德” 的二元结构——双方叙事都存在选择性记忆。Jolitz 夫妇 “全面窃取” 指控在事实层面部分不成立（用户流失是 386BSD 停滞的自然结果而非 “窃取”，代码继承基于 BSD 许可证合法），但在叙事层面有其合理性（FreeBSD 起源叙事确有简化，“被迫 fork” 叙事遮蔽了 patchkit 群体的主动选择与 Jolitz 夫妇的工程哲学）（据 66.13 节补全原截断）
- FreeBSD fork 既是“革命”又是“改革”——作为“革命”，FreeBSD 脱离 386BSD 单人维护模式，引入 Core Team 集体治理，是对 386BSD 治理结构的否定；作为“改革”，FreeBSD 继承 BSD 工程传统（基于 4.3BSD-Lite Net/2 + 386BSD 组件 + FSF 组件），延续 CSRG 的工程化路径，是对 BSD 工程传统的延续。项目史观总纲第 21 条“Linux 靠革命，BSD 靠改革”在此需要细化——FreeBSD fork 是“改革失败后的革命”：386BSD 单人维护模式在 1993 年初已无法维持社区贡献，patchkit 群体尝试通过“补丁包维护”改革 386BSD 维护模式但未获 Bill Jolitz 接受，fork 决策遂以“革命”方式重构治理结构（据 66.14 节补全原截断）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3683] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3698] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3764] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3874] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3875] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3878] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3960] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章
- [DB:references_fulltext:chapter_matches:chmatch_3970] 卷“第04卷-大分裂与四大bsd的诞生”第 66 章，匹配置信度 folder，原因：folder 第65章

## 史观

> 三个 patchkit 协调人不满意，然后他们动手了——没有宣言，没有请愿，只是把补丁包整理成一个可以独立安装的系统。Williams、Grimes、Hubbard 不是革命者，只是几个不愿意等别人修好东西的普通人。David Greenman 提议了 “FreeBSD” 这个名字，但重要的不是名字，而是有人选择不再等待。Walnut Creek CDROM 提供了开发机器和互联网连接，这笔交易后来被质疑为 “商业绑定”，但在 1993 年的现实中，没有商业支撑的开源项目连磁盘空间和带宽都付不起。自由从来不免费（原 “史观映射” 段自文献区错置迁入）

## 辨析

- FreeBSD 2.0 rebase 至 4.4BSD-Lite 的安全基线迁移须区分 “法律洁净” 与 “安全机制升级”——前者是 rebase 的直接动机（USL 诉讼和解要求），后者是 rebase 的附带收益（securelevel 等 4.4BSD-Lite 新机制进入 FreeBSD）；securelevel 的具体级别与约束须对照 4.4BSD SMM: 16 与 PSD: 5 核实
- FreeBSD 1.x 安全基线的架构性缺陷须区分“基线继承缺陷”（来自 Net/2 与 386BSD 0.1）与“FreeBSD 自身引入缺陷”（fork 后新代码中的缺陷）——26.12.1 的 isprint() 修复与 26.12.2 的栈溢出遗留均属基线继承缺陷，FreeBSD 自身引入缺陷在 1.x 时期因 commit 量有限（1993-11-01 至 1995-01-01 free
- 合图阶段不等于 “各打五十大板” 的折衷主义——须区分事实层面（代码继承、commit 记录、BSD 许可证条款可量化考据）与叙事层面（“被迫 fork” “全面窃取” 等价值判断）；事实层面须以一手史料（Release Notes、commit hash、邮件列表原始帖、BSD 许可证文本）为准，叙事层面须呈现双方立场而不予判定；本节不引入新的事实考据，仅综合既有辩证，新事实考据分散于 26.1
- “革命与改革”的二分是史观层面的形式主义化重构，事实层面 fork 决策同时具有革命与改革双重属性——脱离 386BSD 单人维护是革命，继承 BSD 工程传统是改革；“Linux 靠革命，BSD 靠改革”的总纲第 21 条原命题在 FreeBSD fork 案例中需要细化，FreeBSD fork 是“改革失败后的革命”，不能简单归入“BSD 靠改革”范畴；“破心中贼难”的“心中贼”指起源叙事争

## 文献

- FreeBSD 2.0 Release Announcement (22 Nov 1994)；FreeBSD 1.1.5.1 RELEASE Announcement (5 Jul 1994)；4.4BSD-Lite Release Notes (1994.6)；4.4BSD SMM: 16《On the Security of UNIX》；4.4BSD PSD: 5《Berkeley Software Architecture Manual (4.4 Edition)》；bsd_commits.duckdb `tags` 表与 `commits` 表 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1992-1995 年间：15,540 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd.duckdb `commits` 表（freebsd-src, 1993-11-01 至 1995-01-01）；FreeBSD-SA-96:20.stack-overflow 公告；4.4BSD SMM: 16《On the Security of UNIX》；FreeBSD 1.0/2.0 源代码 ［A］
- 综合前三层辩证所引文献；本节不引入新文献 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1992-1995 年间：15,540 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 综合 66.1-66.14 各节文献，无新增文献 ［A］
- 章内采访录指引：第 66 章采访录（详见 [采访录.md](采访录.md)），覆盖 1993-1994 年 FreeBSD 诞生时期的当事人自述与演讲，含 Jordan K. Hubbard BSDNow 278 采访、Rodney W. Grimes 邮件列表自述、David Greenman 命名由来自述三则，每则采访按 5 字段深化，考据过程另见 **原材料/研究/考据记录/** 下对应文件
- 章内媒体反响指引：第 66 章媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）
- **【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=8）

**补充证据（基于全文数据库修订）**

本次修订从全文数据库补充 7 篇新匹配文献的证据。

**新增核心事实**

文献 (021_Interprocess Communication in FreeBSD 11_ Performance An, 年份不详, p.3) 指出：FreeBSD 11.0.0 是该论文进行进程间通信性能分析的基准测试平台。
文献 (021_Interprocess Communication in FreeBSD 11_ Performance An, 年份不详, p.3) 指出：McKusick, Marshall Kirk 作为 FreeBSD 操作系统设计的核心人物，其著作被该论文引用为系统架构参考。
文献 (043_FreeBSD Mandatory Access Control Usage for Implementing , 年份不详, p.6) 指出：FreeBSD 5.0 是该论文研究强制访问控制框架实施的基础操作系统版本。
文献 (043_FreeBSD Mandatory Access Control Usage for Implementing , 年份不详, p.6) 指出：Watson, Robert N. M. 的 TrustedBSD 项目为该论文提供了 MAC 框架的理论与实践基础。
文献 (standalone, 1998, p.4) 指出：FreeBSD 2.2 是该论文进行内存分配器性能对比的参照版本。
文献 (standalone, 1998, p.4) 指出：Kamp, Poul-Henning 作为 FreeBSD malloc(3) 重写的作者，其内存分配器设计在该论文中被重点分析。

**新增人物**

文献 (021_Interprocess Communication in FreeBSD 11_ Performance An, 年份不详) 提及 McKusick, Marshall Kirk，其与 George Neville-Neil、Robert Watson 合著的《The Design and Implementation of the FreeBSD Operating System》是该论文的核心参考文献。
文献 (021_Interprocess Communication in FreeBSD 11_Performance An, 年份不详) 提及 Neville-Neil, George，作为 FreeBSD Core Team 长期成员，与 McKusick 合著了 FreeBSD 操作系统设计经典教材。
文献 (043_FreeBSD Mandatory Access Control Usage for Implementing , 年份不详) 提及 Watson, Robert N. M.，其发起的 TrustedBSD 项目为 FreeBSD 引入了强制访问控制框架，是 FreeBSD 安全子系统现代化的关键推动者。
文献 (standalone, 1998) 提及 Kamp, Poul-Henning，其重写的 malloc(3) 实现是 FreeBSD 内存管理子系统的重要工程贡献，显著提升了多线程环境下的分配性能。
文献 (standalone, 1998) 提及 Wemm, Peter，作为 FreeBSD 早期核心开发者，在内核基础设施与构建系统方面做出了重要贡献。
文献 (standalone, 2001) 提及 Bostic, Keith，作为 CSRG 核心成员，与 McKusick 等人合著了《The Design and Implementation of the 4.4BSD Operating System》，是 BSD 系统设计领域的奠基性文献。

**新增技术**

文献 (021_Interprocess Communication in FreeBSD 11_ Performance An, 年份不详) 讨论 DTrace，该论文使用 DTrace 动态追踪框架对 FreeBSD 11 的进程间通信机制进行了系统性能分析。
文献 (021_Interprocess Communication in FreeBSD 11_ Performance An, 年份不详) 讨论 FreeBSD，该论文以 FreeBSD 11 为平台，对管道、FIFO、Unix 域套接字等 IPC 机制的吞吐量与延迟进行了基准测试。
文献 (043_FreeBSD Mandatory Access Control Usage for Implementing , 年份不详) 讨论 MAC framework，该论文基于 FreeBSD TrustedBSD MAC 框架设计了强制访问控制实施方案，并对其安全策略模型进行了形式化分析。
文献 (standalone, 1998) 讨论 virtual memory，该论文指出 UNIX 内核已从交换/段式内存管理演进为虚拟内存/分页式内存管理，FreeBSD 的 VM 系统是这一演进的重要实例。
文献 (standalone, 2000) 讨论 jails，Poul-Henning Kamp 设计的 FreeBSD Jails 机制实现了操作系统级虚拟化，将 root 权限限制在隔离环境中。
文献 (standalone, 2001) 讨论 SMP，Greg Lehey 等人对 FreeBSD SMP 实现的改进工作，推动了 FreeBSD 在多处理器系统上的性能扩展。

**新增时间线事件**

文献 (021_Interprocess Communication in FreeBSD 11_Performance An, 年份不详) 记录 2008：该论文的 arXiv 预印本于 2020 年 8 月发布，其对 FreeBSD 11 进程间通信性能的实验结论为该领域提供了基准数据。
文献 (021_Interprocess Communication in FreeBSD 11_Performance An, 年份不详) 记录 2014：Addison-Wesley 于 2014 年出版了《The Design and Implementation of the FreeBSD Operating System》第二版（ISBN: 0321968972），是该论文引用的核心系统架构参考文献。
文献 (043_FreeBSD Mandatory Access Control Usage for Implementing , 年份不详) 记录 1985：美国国防部国家计算机安全中心于 1985 年发布可信计算机系统评估标准（TCSEC），为后续强制访问控制研究奠定了政策框架。
文献 (043_FreeBSD Mandatory Access Control Usage for Implementing , 年份不详) 记录 1989：R. S. Sandhu 于 1989 年在 IEEE 安全与隐私研讨会上发表基于格的访问控制模型论文，为 TrustedBSD MAC 框架提供了理论来源。
文献 (047_PEMBANGUNAN JARINGAN KOMPUTER NIRKABEL DENGAN FREEBSD, 年份不详) 记录 1980：Nakamura 等人于 1980 年发表无线传感器网络相关研究，该论文在讨论 FreeBSD 无线网络应用时作为早期文献引用。
文献 (047_PEMBANGUNAN JARINGAN KOMPUTER NIRKABEL DENGAN FREEBSD, 年份不详) 记录 1980：Nakamura、Bhown 与 Compans 于 1980 年发表流感病毒糖蛋白糖基化位点研究，与该论文 FreeBSD 无线网络主题关联薄弱，属数据库误匹配。
