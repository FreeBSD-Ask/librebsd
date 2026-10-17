---
chapter: 第 90 章
id: CH90
volume: 第05卷-freebsd的工程化奠基
---

# 第 90 章 freebsd-ports系统的批评与竞争者对照

## 要点

- Ports 批评史料保存于邮件列表，但部分批评者存在“Linux 中心主义”偏见，需区分客观批评与立场批评
- 中文开源媒体（开源中国/知乎，2021）将 FreeBSD 的市场处境概括为“大败局”，核心论点为“成也 BSDL，败也 BSDL”——BSD 许可证允许大公司无偿使用代码而不回馈上游，FreeBSD 贡献者因此被调侃为“Apple 公司的无薪员工”；批评还指向 FreeBSD 缺乏 Red Hat 式的商业支持体系（“FreeBSD 几乎没有商业支持”）〔待核：原文截断，后文待回源〕
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
- 该文为自媒体二手叙事，其中“Dillon 是 1994 年加入 FreeBSD 的明星成员”等细节与 freebsd.duckdb 核验结果冲突（Dillon 在 freebsd-src 的首 commit 为 1998-08-26），引用时须区分叙事价值与史实准确性，以 0 信任原则对待
- 按 0 信任原则考据。【查证来源】总纲第 1、2、7、19、23、25 条系经 Read 核实的项目统摄史观原文（原材料/哲学/项目统摄史观/第 25 章.md，2026-07-23 一手核验），其中总纲第 7 条“理论必须自反”与总纲第 2 条“历史是形式主义化的非存在”为本节自反审视的直接哲学依据；本节 35.9.1-35.9.4 的审视文本本身（经 Read 核实存在于 c:\Users\y

## 文献

- freebsd-ports 邮件列表；BSDCon 辩论 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：对 Ports 系统的批评（Gentoo Portage 与 dpkg/rpm 对比）
- 肖滢、lola. FreeBSD 大败局 [EB/OL]. 2021. 知乎 ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- PR 数据库；邮件列表归档；开源史料保存研究 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 软件包管理系统比较论文；各系统官方文档；社区讨论归档 ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1998-1998 年间：18,134 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、19、23、25 条 ［A］FreeBSD 社区论文：[FP-2020-012] Unearthing the history of Unix（Warner Losh（沃纳·洛什），2020）<https://papers.freebsd.org/2020/bsdcan/losh-unearthing_the_history_of_unix/>FreeBSD 社区论文：[FP-2020-018] The hidden early history of Unix（Warner Losh，2020）<https://papers.freebsd.org/2020/fosdem/losh-hidden_early_history_of_unix/>FreeBSD 社区论文：[FP-2018-022] devmatch -- matching devices to modules: PNP plays matchmaker for kernel modules（Warner Losh，2018）<https://papers.freebsd.org/2018/bsdcan/losh-devmatch_matching_devices_to_modules/>FreeBSD 社区论文：[FP-2002-003] Problems updating FreeBSD's card system from ISA to PCI（M. Warner Losh，2002）<https://papers.freebsd.org/2002/bsdcon/imp-isa_to_pci/>### 史观映射> Ports 不需要宣言——三万多个 port 的维护者日复一日更新版本号、修复补丁、处理冲突，没有人在做英雄式的工作，但这座由琐碎劳动堆成的港口比任何架构蓝图都更持久。代码不撒谎，也不争辩：它只是在那里，每晚同步，每天编译，年复一年---## 第 35.10 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 35.11 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）---**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=10）---**补充证据（基于全文数据库修订）**本次修订从全文数据库补充 7 篇新匹配文献的证据。**新增核心事实**
文献 (2013spw-compartmentalisation, 年份不详, p.1) 指出：Watson, Robert N. M. 作为 TrustedBSD 和 Capsicum 的发起人，其应用隔离理论在该论文中被引用。
文献 (2013spw-compartmentalisation, 年份不详, p.1) 指出：Davis, Brooks 作为 CheriBSD 项目的核心开发者，在该论文中被列为致谢对象。
文献 (2015septupdate, 年份不详, p.1) 指出：Neville-Neil, George 作为 FreeBSD Foundation 董事会成员，在基金会月报中被提及。
文献 (2015septupdate, 年份不详, p.1) 指出：Belousov, Konstantin 作为 FreeBSD 内核开发者，在基金会月报中被提及。
文献 (37R5uB, 年份不详, p.2) 指出：FreeBSD 4.0 是该论文进行系统安全分析时引用的参照版本。
文献 (37R5uB, 年份不详, p.2) 指出：FreeBSD 8.0-RELEASE 是该论文进行系统安全分析时引用的参照版本。
**新增人物**
文献 (2013spw-compartmentalisation, 年份不详) 提及 Watson, Robert N. M.，其关于应用隔离理论的研究论文为该领域提供了理论基础。
文献 (2013spw-compartmentalisation, 年份不详) 提及 Davis, Brooks，作为 CheriBSD 和 FreeBSD 开发者，在该论文的致谢中被列为贡献者。
文献 (2015septupdate, 年份不详) 提及 Neville-Neil, George，作为 FreeBSD Foundation 董事会成员，与 Dru Lavigne 和 Glen Barber 等一同参与了基金会工作。
文献 (2015septupdate, 年份不详) 提及 Jude, Allan，作为 ScaleEngine 运营副总裁，对 FreeBSD 项目的持续发展表达了支持。
文献 (FreeBSD-and-Git, 年份不详) 提及 Maste, Ed，作为 FreeBSD Foundation 技术总监，在 2018 年 FreeBSD Vendor Summit 上发表了关于 FreeBSD 与 Git 迁移的演讲。
文献 (FreeBSD-and-Git, 年份不详) 提及 Kamp, Poul-Henning，其关于 Git 的批评性文章被该文献引用，讨论了版本控制系统的设计哲学。
**新增技术**
文献 (2013spw-compartmentalisation, 年份不详) 讨论 Capsicum，该论文将 Capsicum 能力模式作为应用隔离的理论基础，探讨了内核与用户态之间的安全边界。
文献 (2013spw-compartmentalisation, 年份不详) 讨论 Ports Collection，该论文以 Ports 系统的模块化设计为类比，讨论了分布式系统中节点间的连接模型。
文献 (2015septupdate, 年份不详) 讨论 FreeBSD，FreeBSD 基金会 2015 年 9 月更新报告涵盖了即将举行的社区活动。
文献 (37R5uB, 年份不详) 讨论 jails，该论文将 FreeBSD Jails 机制作为操作系统级资源隔离的参考实现进行了讨论。
文献 (Beckhoff-CASE-STUDY-5, 年份不详) 讨论 GPL，Beckhoff 公司因需要非 GPL 许可证的稳定安全平台而选择了 FreeBSD 作为其自动化系统的基础。
文献 (Contributing-to-FreeBSD-Ports-with-Git, 年份不详) 讨论 git，该文献记录了 FreeBSD Ports 从 Subversion 到 Git 的迁移过程，CVS 和 Subversion 现已被 Git 取代。
**新增时间线事件**
文献 (2013spw-compartmentalisation, 年份不详) 记录 1980：SRI International 计算机科学实验室于 1980 年 5 月发布了相关技术报告。
文献 (2013spw-compartmentalisation, 年份不详) 记录 1982：ACM Transactions on Programming Languages and Systems 于 1982 年 7 月发表了相关论文。
文献 (2015septupdate, 年份不详) 记录 2015：EuroBSDcon 2015 即将举行，FreeBSD 基金会发布了相关活动更新。
文献 (2015septupdate, 年份不详) 记录 2015：EuroBSDcon 2015 定于 2015 年 10 月 1 日至 4 日举行。
文献 (37R5uB, 年份不详) 记录 2010：2010 年 6 月相关技术文献发布。
文献 (Beckhoff-CASE-STUDY-5, 年份不详) 记录 1980：Beckhoff 公司成立于 1980 年，致力于开放式自动化系统的开发。
<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- ROW_MINE: login-zazhi.articles.CL-5-114 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-114`；login 逐条遍历判定采纳）

2000年春，Bob Gray 在科罗拉多大学本科操作系统课程中弃用基于 binary-only Windows NT 的 userland 作业，改用源码可得的 production UNIX（FreeBSD）让学生直接修改内核（如实现 undelete），95名三年级学生参与，作者主张真实内核实践优于模拟器教学。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-5-114 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-114`；login 逐条遍历判定采纳）

2000年春，Bob Gray 在科罗拉多大学本科操作系统课程中弃用基于 binary-only Windows NT 的 userland 作业，改用源码可得的 production UNIX（FreeBSD）让学生直接修改内核（如实现 undelete），95名三年级学生参与，作者主张真实内核实践优于模拟器教学。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2157 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2157`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie，EuroBSDcon 2022 演讲“Architectures vs the ports tree: a losing battle ?”〕讲者口述：OpenBSD 很早就采用了二进制软件包，主要原因是其领导者决定只发布二进制包——理由是开发者人数太少，无法支撑每台机器各自重新编译。（YouTube EPKw2_RWku-co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2158 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2158`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie，EuroBSDcon 2022 演讲“Architectures vs the ports tree: a losing battle ?”〕讲者口述：OpenBSD 为多数架构设有专用构建农场，但这些农场因其领导者的谨慎行事作风全部部署在自家地下室，对某些不够稳定的架构是个隐患。（YouTube EPKw2_RWku-co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2159 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2159`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie，EuroBSDcon 2022 演讲“Architectures vs the ports tree: a losing battle ?”〕讲者口述：32 位架构在主流通用系统上已不再有意义；团队早该在大型语言与放不下小机器的组件进入之前高声反对，但那是五到十年前的事，如今已无可挽回。（YouTube EPKw2_RWku-co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
