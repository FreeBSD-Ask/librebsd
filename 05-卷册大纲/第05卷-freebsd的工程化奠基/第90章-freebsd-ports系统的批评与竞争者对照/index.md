---
chapter: 第 90 章
id: CH90
volume: 第05卷-freebsd的工程化奠基
---

# 第 90 章 freebsd-ports系统的批评与竞争者对照

## 要点

- Ports 批评史料保存于邮件列表，但部分批评者存在“Linux 中心主义”偏见，需区分客观批评与立场批评
- 中文开源媒体（开源中国/知乎，2021）将 FreeBSD 的市场处境概括为“大败局”，核心论点为“成也 BSDL，败也 BSDL”——BSD 许可证允许大公司无偿使用代码而不回馈上游，FreeBSD 贡献者因此被调侃为“Apple 公司的无薪员工”；批评还指向 FreeBSD 缺乏 Red Hat 式的商业支持体系（“FreeBSD 几乎没有商业支持”）与“没有商业布局”（肖滢、lola, 20
- Port 边缘贡献者史料保存较差，因无 commit log，仅 PR 数据库与邮件列表可查，部分 PR 在 GNATS 迁移时丢失
- 四方比较存在“源码 vs 二进制”与“单平台 vs 多平台”两个维度，FreeBSD Ports 是源码 + 单平台，Debian apt 是二进制 + 单平台，pkgsrc 是源码 + 多平台，难以简单排名
- 本节的审视本身亦是形式主义化的非存在——史家通过项目史观总纲“重构”Ports 文化的遮蔽与重构、源码/二进制叙事的权力共谋、改革与革命的方法论分歧，但这一重构本身就是当下主体的形式主义建构，不宣称呈现“真实的 Ports 史”。本节对“Ports 文化被遮蔽”的论断本身亦是一种叙事权力行使——将源码编译派定位为“被遮蔽的传统”、将二进制软件包派定位为“遮蔽者的现代化叙事”，这一定位本身参与权力与

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3676] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 folder，原因：folder 第88章
- [DB:references_fulltext:chapter_matches:chmatch_3682] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 folder，原因：folder 第88章
- [DB:references_fulltext:chapter_matches:chmatch_3685] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 folder，原因：folder 第88章
- [DB:references_fulltext:chapter_matches:chmatch_3687] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 folder，原因：folder 第88章
- [DB:references_fulltext:chapter_matches:chmatch_3690] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 folder，原因：folder 第88章
- [DB:references_fulltext:chapter_matches:chmatch_3708] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 folder，原因：folder 第88章
- [DB:references_fulltext:chapter_matches:chmatch_1296] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 0.8，原因：关键词重合 2 项（oss2017, seccomp, pledge, openbsd）
- [DB:references_fulltext:chapter_matches:chmatch_1407] 卷“第05卷-freebsd的工程化奠基”第 90 章，匹配置信度 0.8，原因：关键词重合 2 项（2017, pledge, pkgsrccon, openbsd）

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 部分批评来自 Linux 用户而非 FreeBSD 用户，立场需考据
- 该文为自媒体二手叙事，其中“Dillon 是 1994 年加入 FreeBSD 的明星成员”等细节与 bsd_commits.db 核验结果冲突（Dillon 在 freebsd-src 的首 commit 为 1998-08-26），引用时须区分叙事价值与史实准确性，以 0 信任原则对待
- 按 0 信任原则考据。【查证来源】总纲第 1、2、7、19、23、25 条系经 Read 核实的项目统摄史观原文（原材料/哲学/项目统摄史观/第 25 章.md，2026-07-23 一手核验），其中总纲第 7 条“理论必须自反”与总纲第 2 条“历史是形式主义化的非存在”为本节自反审视的直接哲学依据；本节 35.9.1-35.9.4 的审视文本本身（经 Read 核实存在于 c:\Users\y

## 文献

- freebsd-ports 邮件列表；BSDCon 辩论 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：对 Ports 系统的批评（Gentoo Portage 与 dpkg/rpm 对比）
- 肖滢、lola. FreeBSD 大败局 [EB/OL]. 2021. 知乎 ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- PR 数据库；邮件列表归档；开源史料保存研究 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 软件包管理系统比较论文；各系统官方文档；社区讨论归档 ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1998-1998 年间：18,134 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、19、23、25 条 ［A］FreeBSD 社区论文：[FP-2020-012] Unearthing the history of Unix（Warner Losh（沃纳·洛什），2020）<https://papers.freebsd.org/2020/bsdcan/losh-unearthing_the_history_of_unix/>FreeBSD 社区论文：[FP-2020-018] The hidden early history of Unix（Warner Losh，2020）<https://papers.freebsd.org/2020/fosdem/losh-hidden_early_history_of_unix/>FreeBSD 社区论文：[FP-2018-022] devmatch -- matching devices to modules: PNP plays matchmaker for kernel modules（Warner Losh，2018）<https://papers.freebsd.org/2018/bsdcan/losh-devmatch_matching_devices_to_modules/>FreeBSD 社区论文：[FP-2002-003] Problems updating FreeBSD's card system from ISA to PCI（M. Warner Losh，2002）<https://papers.freebsd.org/2002/bsdcon/imp-isa_to_pci/>### 史观映射> Ports 不需要宣言——三万多个 port 的维护者日复一日更新版本号、修复补丁、处理冲突，没有人在做英雄式的工作，但这座由琐碎劳动堆成的港口比任何架构蓝图都更持久。代码不撒谎，也不争辩：它只是在那里，每晚同步，每天编译，年复一年---## 第 35.10 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 35.11 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）---**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=10）---**补充证据（基于全文数据库修订）**本次修订从全文数据库补充 7 篇新匹配文献的证据。**新增核心事实**文献 (2013spw-compartmentalisation, 年份不详, p.1) 指出：Watson, Robert N. M. mentioned (1 times)。文献 (2013spw-compartmentalisation, 年份不详, p.1) 指出：Davis, Brooks mentioned (1 times)。文献 (2015septupdate, 年份不详, p.1) 指出：Neville-Neil, George mentioned (2 times)。文献 (2015septupdate, 年份不详, p.1) 指出：Belousov, Konstantin mentioned (1 times)。文献 (37R5uB, 年份不详, p.2) 指出：FreeBSD 4.0 mentioned。文献 (37R5uB, 年份不详, p.2) 指出：FreeBSD 8.0-RELEASE mentioned。**新增人物**文献 (2013spw-compartmentalisation, 年份不详) 提及 Watson, Robert N. M.，ards a Theory of Application Compartmentalisation Robert N. M. Watson（罗伯特·N·M·沃森）1, Steven J……。文献 (2013spw-compartmentalisation, 年份不详) 提及 Davis, Brooks，s paper, including Ross Anderson, David Chisnall（戴维·奇斯纳尔）, Brooks Davis, Pawel Dawidek, S……。文献 (2015septupdate, 年份不详) 提及 Neville-Neil, George，h Foundation board and staff members Dru Lavigne, George Neville-Neil and Glen B……。文献 (2015septupdate, 年份不详) 提及 Jude, Allan，project gets the support it needs to flourish." – Allan Jude（艾伦·裘德）, VP Operations, Sca……。文献 (FreeBSD-and-Git, 年份不详) 提及 Maste, Ed，FreeBSD and Git Ed Maste（埃德·马斯特） - FreeBSD Vendor Summit 2018。文献 (FreeBSD-and-Git, 年份不详) 提及 Kamp, Poul-Henning，"Git is not a Version Control System" phk@ missive, reproduced at <https://blog.f……。**新增技术**文献> (2013spw-compartmentalisation, 年份不详) 讨论 Capsicum，lopment. 3 Applications as Distributed Systems In Capsicum, the kernel and a sma……。文献 (2013spw-compartmentalisation, 年份不详) 讨论 Ports Collection，Instead each node can be modelled as a series of ports, and connectivity is from……。文献 (2015septupdate, 年份不详) 讨论 FreeBSD，FreeBSD Foundation September Update Upcoming Event。文献 (37R5uB, 年份不详) 讨论 jails，er than isolation of global re- sources, as e.g. "Jail" does. This permits the v……。文献 (Beckhoff-CASE-STUDY-5, 年份不详) 讨论 GPL，Windows CE on the horizon, Beckhoff needed a non-GPL, stable, secure, and high-p……。文献 (Contributing-to-FreeBSD-Ports-with-Git, 年份不详) 讨论 git，e source of truth was migrated from Subversion to Git. As both CVS and Sub- vers……。**新增时间线事件**文献 (2013spw-compartmentalisation, 年份不详) 记录 1980：mputer Science Laboratory, SRI International, May 1980.。文献 (2013spw-compartmentalisation, 年份不详) 记录 1982：s on Programming Languages and Systems 4, 3 (July 1982), 382– 401.。文献 (2015septupdate, 年份不详) 记录 2015：ation September Update Upcoming Events EuroBSDcon 2015。文献 (2015septupdate, 年份不详) 记录 2015：October 1-4, 2015。文献 (37R5uB, 年份不详) 记录 2010：06. June 2010。文献 (Beckhoff-CASE-STUDY-5, 年份不详) 记录 1980：solutions and cutting-edge technology. Founded in 1980, Beckhoff implements open automation systems。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
