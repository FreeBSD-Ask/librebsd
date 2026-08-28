---
chapter: 第 97 章
id: CH97
volume: 第05卷-freebsd的工程化奠基
---

# 第 97 章 freebsd-foundation

## 要点

- 成立史料疑点：(1) 创始人名单是否包括 McKusick 还是仅 Gibbs 等；(2) 注册动机是否仅为商标保护还是更广义的项目支持；(3) 早期资金来源
- 边界史料疑点：(1) Foundation 雇员名单是否公开；(2) 雇员是否参与 Core Team;(3) 雇员薪酬是否影响决策
- 生平史料疑点：(1) 各董事的 BSD 参与起点；(2) 董事提名过程是否透明；(3) 董事是否曾因争议离职
- 比较史料疑点：(1) 各基金会披露程度不同；(2) 治理结构的实际运作与文档差距；(3) 跨基金会对比是否公平
- 批评史料疑点：(1) 批评者是否客观；(2) 批评是否反映社区共识；(3) 批评是否促成治理改革

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3797] 卷“第05卷-freebsd的工程化奠基”第 97 章，匹配置信度 folder，原因：folder 第95章
- [DB:references_fulltext:chapter_matches:chmatch_1229] 卷“第05卷-freebsd的工程化奠基”第 97 章，匹配置信度 0.7，原因：无匹配
- [DB:bsdnow_podcast:outline_mappings:om_10420] BSD Now 第 676 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10440] BSD Now 第 674 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10477] BSD Now 第 665 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10490] BSD Now 第 664 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10509] BSD Now 第 661 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10520] BSD Now 第 659 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10539] BSD Now 第 654 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10588] BSD Now 第 645 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10598] BSD Now 第 644 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10616] BSD Now 第 641 期，匹配 CH97 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 创始人名单在基金会不同文档中是否一致，需逐份核对；**统计局限性标注**——统计显著 ≠ 实际显著，C-12 变点 p < 0.001 仅反映 commit 时序存在结构性断点，不等于 Foundation 的成立 “导致” 了变点，变点为工程节律切换的统计表征而非 Foundation 成立的工程因果；C-12 双检验一致性（Pettitt 与 BUISHAND）降低单一方法偏差但不可消除方法学
- 不应神化基金会——FreeBSD 的成功仍依赖核心开发者与社区；基金会是赋能工具而非替代。
- Determination Letter 是否曾在 IRS EO Select Check 中可查，需核实
- 州务卿备案是否包含完整 By-Laws，需查科罗拉多州备案规则
- McKusick 为亲历者，其"deadwood"表述带有当事人视角；首届民选核心团队（2000）与 Foundation 成立（2000）同年，二者是否同一治理改革的组成部分须对照 Core Team 档案核验

## 文献

- Foundation 官方文档；Gibbs BSDCon 2001 演讲 ［B］；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md`；统计分析报告：推断性统计.md Task 6 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md`；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. bsd_commits.db [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase2_inferential.py`. Task 6 变点检测（Pettitt + BUISHAND）. 执行日期：2026-07-27 [考据脚注：C-03 freebsd-src 444,203 commits 与 C-12 变点 1999-08 经 `script/phase2_inferential.py` 执行结果与 `phase2_results.json` 结构化结果交叉验证；变点判定非迁移伪变点已通过距 2020-01 SVN-to-Git 迁移 245 个月的时间间距排除。]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2000-2000 年间：29,754 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Foundation 990 表；Core Team 名单 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：staff developer 与志愿者的张力
- 作者不详. FreeBSD Foundation 董事会名单[Z]. 年份不详；作者不详. freebsd-hackers 邮件列表[EB/OL]. 年份不详 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 各基金会 990 表[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 作者不详. 批评博客[EB/OL]. 年份不详；作者不详. FreeBSD Foundation 改革记录[Z]. 年份不详 ［C］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Foundation 档案[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]FreeBSD 社区论文：[FP-2020-014] FreeBSD Around the World!（Deb Goodkin（德布·古德金），2020）<https://papers.freebsd.org/2020/fosdem/goodkin-freebsd_around_the_world/>FreeBSD 社区论文：[FP-2018-002] Flexible Disk Use in OpenZFS（Matt Ahrens，2018）<https://papers.freebsd.org/2018/bsdcan/ahrens-flexible_disk_use_in_openzfs/>FreeBSD 社区论文：[FP-2018-043] The FreeBSD Foundation and How We Are Changing the World（Deb Goodkin，2018）<https://papers.freebsd.org/2018/fosdem/deb-the_freebsd_foundation_and_how-we_are_changing_the_world/>FreeBSD 社区论文：[FP-2015-008] Supporting a BSD Project（Ed Maste（埃德·马斯特），2015）<https://papers.freebsd.org/2015/vbsdcon/maste-supporting_a_bsd_project/>FreeBSD 社区论文：[FP-2010-002] Software Tools - Mission Accomplished or Mission Failure ?（Poul-Henning Kamp（波尔-亨宁·坎普），2010）<https://papers.freebsd.org/2010/phk-software-tools/>FreeBSD 社区论文：[FP-2007-003] Lousy virtualization, Happy users: FreeBSD's jail(2) facility（Poul-Henning Kamp，2007）<https://papers.freebsd.org/2007/euug/phk-jail/>FreeBSD 社区论文：[FP-2005-001] Building a FreeBSD Appliance With NanoBSD（Poul-Henning Kamp，2005）<https://papers.freebsd.org/2005/phk-nanobsd/>FreeBSD 社区论文：[FP-2005-004] Ioctl(2) is so 1980ies（Poul-Henning Kamp，2005）<https://papers.freebsd.org/2005/phk-ioctl/>FreeBSD 社区论文：[FP-2004-003] GEOM（Poul-Henning Kamp，2004）<https://papers.freebsd.org/2004/phk-geom/>FreeBSD 社区论文：[FP-2004-004] GEOM Tutorial（Poul-Henning Kamp，2004）<https://papers.freebsd.org/2004/phk-geom-tutorial/>FreeBSD 社区论文：[FP-2004-005] Making sure data is lost（Poul-Henning Kamp，2004）<https://papers.freebsd.org/2004/phk-gbde/>FreeBSD 社区论文：[FP-2003-001] GBDE - GEOM Based Disk Encryption（Poul-Henning Kamp，2003）<https://papers.freebsd.org/2003/bsdcon/phk-gbde-paper/>FreeBSD 社区论文：[FP-2003-002] GEOM tutorial（Poul-Henning Kamp，2003）<https://papers.freebsd.org/2003/bsdcon/phk-geom-tutorial/>FreeBSD 社区论文：[FP-2003-003] Making sure data is lost（Poul-Henning Kamp，2003）<https://papers.freebsd.org/2003/bsdcon/phk-gbde-slides/>FreeBSD 社区论文：[FP-2002-004] Rethinking /dev and devices in the UNIX kernel（Poul-Henning Kamp，2002）<https://papers.freebsd.org/2002/bsdcon/phk-devfs/>FreeBSD 社区论文：[FP-2002-009] Timecounters: Efficient and precise timekeeping in SMP kernels（Poul-Henning Kamp，2002）<https://papers.freebsd.org/2002/phk-timecounters/>FreeBSD 社区论文：[FP-2000-001] Jails: Confining the omnipotent root（Poul-Henning Kamp; Robert N. M. Watson（罗伯特·N·M·沃森），2000）<https://papers.freebsd.org/2000/phk-jails/>FreeBSD 社区论文：[FP-2000-003] The Nanokernel（Dave L. Mills; Poul-Henning Kamp，2000）<https://papers.freebsd.org/2000/phk-nanokernel/>FreeBSD 社区论文：[FP-1998-001] Raw data: Interrupt latency measurements（Poul-Henning Kamp，1998）<https://papers.freebsd.org/1998/phk-interrupts/>FreeBSD 社区论文：[FP-1998-002] Malloc(3) revisited（Poul-Henning Kamp，1998）<https://papers.freebsd.org/1998/phk-malloc/>### 史观映射> 基金会的诞生把一个松散的黑客共同体推入了法律实体的模具——科罗拉多州注册、IRS 501(c)(3) 裁定、By-Laws 条款、officer 职责分工，每一份表格都在把 “谁有权做什么” 从默契变成条文。形式主义化不一定是堕落——没有基金会，Jan Koum（简·库姆） 的支票无处可签；但形式主义化也不一定是进步——当执行总监与董事会争夺日常运营权，当技术派与商业派在预算表上对峙，当员工开发者因有薪酬而比志愿者更有话语权，治理就不再是服务社区的工具，而是社区必须服从的结构---<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD 相关记录（详情见存疑库）。文献 (Code, 2024) 提及 Tetlow, Gordon，作为 FreeBSD Foundation 执行董事，在基金会治理和项目战略规划中发挥关键作用。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 提及 Neville-Neil, George，作为 FreeBSD Core Team 成员，在存储系统方面做出了重要贡献。文献 (FreeBSD-Foundation-August-2016-Update, 2016) 提及 Baldwin, John，作为 FreeBSD 核心开发者，在内核修复和架构支持方面做出了重要贡献。文献 (FreeBSD-Foundation-December-2016-Update, 2016) 提及 Watson, Robert N. M.，以基金会董事会成员身份在上海 BSD 聚会中发表了演讲。文献 (FreeBSD-Foundation-January-2018-Update, 2018) 提及 Percival, Colin，作为 Tarsnap 总裁，对 FreeBSD 安全更新基础设施做出了重要贡献。**新增技术**文献 (Code, 2024) 讨论 bhyve，该安全审计报告对 Capsicum 和 bhyve 子系统进行了全面的安全审查。文献 (Code, 2024) 讨论 FreeBSD，该报告由 FreeBSD Foundation 于 2024 年 11 月发布。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 讨论 Ports Collection，FreeBSD 社区贡献者持续将改进和错误修复贡献回上游项目。文献 (FreeBSD-Foundation-December-2016-Update, 2016) 讨论 DTrace，社区成员对 Jails、DTrace 和 ZFS 等主题表现出浓厚兴趣。文献 (FreeBSD-Foundation-February-2018-Update, 2018) 讨论 lld，FreeBSD 工具链现代化项目将 LLVM 的 LLD 链接器引入基础系统。文献 (FreeBSD-Foundation-January-2018-Update, 2018) 讨论 clang，FreeBSD 在基础系统中采用 Clang 编译器作为默认编译器。**新增时间线事件**文献 (Code, 2024) 记录 2019：FreeBSD 安全公告涉及 CVE-2019-5607 漏洞。文献 (Code, 2024) 记录 2019：该安全公告涉及的漏洞模式分析。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 记录 2012：FreeBSD 项目在 NYI 数据中心部署了东海岸镜像站点。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 记录 2015：FreeBSD 测试集群在 2015 年底进行了重大升级。文献 (FreeBSD-Foundation-April-2018-Update, 2018) 记录 2018：FreeBSD 基金会参加了 Rootconf 2018 和 BSDCan 2018 等社区活动。文献 (FreeBSD-Foundation-April-2018-Update, 2018) 记录 2018：FreeBSD 基金会 2018 年 4 月更新，涵盖 Rootconf 2018 和 BSDCan 2018 
<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2000-2000 年间：29,754 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。


- IRS EO Select Check；Foundation 历年 990 表[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 科罗拉多州务卿档案；Foundation By-Laws ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- McKusick & Rice. The Evolution of FreeBSD Governance [J]. FreeBSD Journal, 2017, 4(5): 26-31 ［A］；McKusick. The Evolution of FreeBSD Governance [C]//BSDCan 2018. Ottawa, 2018 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第97章-freebsd-foundation -->

## 要点（播客口述史提取）
- And I can't remember when I first discovered FreeBSD,
- Yeah, I mean Sonos is the BSD-derived version from Son.
- So yes, I think it was probably then by early 2000s when I first experienced BSD, and it
- been the first time that i've been to a an in-person bsd event as well oh even there yeah
- yet another great BSD can this year. Dan already announced that BSD can 2020 will be from June
- So the first event or the official event of BSD can was on Tuesday, beehive con, I guess
- Uh, imported a port of WireGuard into the OpenBSD port
- although recently both RMV7 and RM64 for NetBSD have been moved over to the EFI boot using the

## 史料（播客提及）
- [BSD Now EP622 @ 1063.199951171875] That's actually what a lot of sysadmins who were coming from Solaris were also coming to FreeBSD
- [BSD Now EP622 @ 1086.4600830078125] driver for people to use FreeBSD. I think it's that's
- [BSD Now EP622 @ 244.95999145507812] So yes, I think it was probably then by early 2000s when I first experienced BSD, and it
- [BSD Now EP300 @ 3355.52] Interesting one was at BSD can somebody came who had just bought a new I think
- [BSD Now EP300 @ 3663.92] And I know like Gavin was working on getting free BSD working well on the, I think it

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP622 @ 1063.199951171875] That's actually what a lot of sysadmins who were coming from Solaris were also coming to FreeBSD
- [BSD Now EP622 @ 1086.4600830078125] driver for people to use FreeBSD. I think it's that's
- [BSD Now EP622 @ 244.95999145507812] So yes, I think it was probably then by early 2000s when I first experienced BSD, and it
  → 史观映射：总纲9——经验优先; 总纲18——时间是一种形式主义
- [BSD Now EP300 @ 3355.52] Interesting one was at BSD can somebody came who had just bought a new I think
- [BSD Now EP300 @ 3663.92] And I know like Gavin was working on getting free BSD working well on the, I think it
- [BSD Now EP300 @ 857.4] and FreeBSD is using that, that repo will actually be renamed.
- [BSD Now EP156 @ 1140.419921875] the Raspberry Pi. So this is actually something over at the FreeBSD Foundation site. And of course,
- [BSD Now EP156 @ 1293.9599609375] Well, in particular, the reason it does the FreeBSD, FreeBSD one

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP129 @ 1495.6199951171875] the NetBSD, they said, hey, you know, you're doing some good work. Would you like a
- [存疑脚注] [BSD Now EP197 @ 2454.97998046875] there was an interesting argument between uh developers of two different bsds
- [存疑脚注] [BSD Now EP70 @ 2876.860107421875] tools that are all started as a part of open bsd uh they have another started as open bsd fork of

## 文献（播客参考条目）
- [BSD Now EP622] Pennington J. BSD Now: 622: Interview with Mark Phillips - Technical Marketing Manager at the FreeBSD Foundation[EB/OL]. (2025-07-31)[2026-08-15]. https://www.bsdnow.tv/622.
- [BSD Now EP300] Pennington J. BSD Now: 300: The Big Three[EB/OL]. (2019-05-30)[2026-08-15]. https://www.bsdnow.tv/300.
- [BSD Now EP156] Pennington J. BSD Now: 156: The Fresh BSD experience[EB/OL]. (2016-08-24)[2026-08-15]. https://www.bsdnow.tv/156.
- [BSD Now EP256] Pennington J. BSD Now: Episode 256: Because Computers | BSD Now 2^8[EB/OL]. (2018-07-25)[2026-08-15]. https://www.bsdnow.tv/256.
- [BSD Now EP129] Pennington J. BSD Now: 129: Synthesize all the Things![EB/OL]. (2016-02-17)[2026-08-15]. https://www.bsdnow.tv/129.
- [BSD Now EP42] Pennington J. BSD Now: 42: Devious Methods[EB/OL]. (2014-06-18)[2026-08-15]. https://www.bsdnow.tv/42.
- [BSD Now EP80] Pennington J. BSD Now: 80: The PC-BSD Tour II[EB/OL]. (2015-03-11)[2026-08-15]. https://www.bsdnow.tv/80.
- [BSD Now EP197] Pennington J. BSD Now: 197: Relaying the good news[EB/OL]. (2017-06-07)[2026-08-15]. https://www.bsdnow.tv/197.
- [BSD Now EP70] Pennington J. BSD Now: 70: Daemons in the North[EB/OL]. (2014-12-31)[2026-08-15]. https://www.bsdnow.tv/70.

<!-- /PODCAST_MINE -->