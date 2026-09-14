---
chapter: 第 312 章
id: CH312
volume: 第16卷-开源运动与合规治理
---

# 第312章 管理学问题-治理历史演变

## 史料

- [WEB:freebsd.org/administration.html] FreeBSD Project Administration（官方一手）：Core Team/Doceng/portmgr/srcmgr/re/secteam 各团队 charter——治理演变的制度文本
- [WEB:vuink.com 2024 Developer Summit] 2024 FreeBSD Developer Summit 纪要（一手）：Rust 集成、pkgbase、发布周期缩短等治理议题的社区讨论记录

## 要点

- FreeBSD 项目管理从 1993 年首届 Core Team 纯志愿者治理起步，2000 年 FreeBSD Foundation 成立后逐步引入专职 staff（Executive Director Deb Goodkin（德布·古德金） 等）与合同制开发者，项目管理模式从纯志愿者演进为 “志愿者 + 基金会专职” 双轨制；Core Team 仍为技术决策最高机构，Foundation 负责资金筹募、法律保护与基础设施运营
- FreeBSD 外部贡献者指无 committer 权限但通过提交补丁、bug 报告、文档翻译参与项目的贡献者；外部贡献者的主要参与渠道包括 Bugzilla（后迁 GitHub Issues）、phabricator（代码审查，2020 年迁 Git 后逐步过渡到 GitHub PR）、邮件列表；企业外部贡献者（如 Netflix 工程师通过提交 kernel TLS offload 补丁、Juniper 工程师提交路由相关补丁）是 FreeBSD 高质量外部贡献的重要来源；外部贡献者转 committer 的 “mentor 担保” 机制是主要晋升路径但存在 mentor 数量瓶颈
- FreeBSD 管理学议题中的重要贡献者包括 Core Team 历届成员（如 McKusick、Hubbard、Baldwin 等在治理决策中的长期贡献）与 Foundation 专职 staff（如 Deb Goodkin（德布·古德金） 在筹款与外联中的贡献、Glen Barber（格伦·巴伯） 在 release engineering 中的贡献）；被边缘化的贡献者包括因行为准则争议离场的成员、因 committer 制度瓶颈未能晋升的长期外部贡献者、文档与翻译贡献者
- FreeBSD 项目治理与 Linux（Linus Torvalds 仁慈独裁者模式 + Linux Foundation 501(c)(6) 商业联盟）、OpenBSD（Theo de Raadt（西奥·德·若特） 事实独裁 + 简化 Foundation）、NetBSD（Core Team 共识 + Foundation）、Apache（ASF meritocracy + 共识）、Python（PEP 流程+BDFL 演变为指导委员会 2018 年起）、Rust（Rust Foundation 2021 年 + 社区选举领导委员会）等开源项目治理模式比较；FreeBSD 的共识模型在决策效率上低于 Linux 的独裁模式，但在社区参与度与决策合法性上具有优势；Apache meritocracy 强调 “功劳制” 晋升，与 FreeBSD mentor 担保制形成对比
- 批评者从五个维度对开源项目治理与挑战提出批评——其一，BDFL（Benevolent Dictator For Life，终身仁慈独裁者）模式的集中决策风险：Linux Torvalds 长期以 BDFL 模式主导 Linux 内核合并决策，2018 年 9 月因在 LKML（Linux Kernel Mailing List）中尖锐批评 contributor 引发社区反弹后公开道歉并宣布休假（break），同期 Linux 4.19-rc4 发布前引入 Code of Conduct（行为准则）取代先前的 Code of Conflict（冲突准则），CoC 基于 Contributor Covenant 1.4 版本；Python 的 Guido van Rossum（吉多·范罗苏姆） 自 1990 年代起任 BDFL，2018 年 7 月 12 日通过 Python-committers 邮件列表宣布卸任 BDFL，PEP 13（Python Language Governance，创建于 2018-12-16）确立 5 人 steering committee（指导委员会）治理模式，2024 任期委员会成员为 Brett Cannon、Gregory P. Smith、Pablo Galindo Salgado、Petr Viktorin、Thomas Wouters；Perl 的 Larry Wall 自 1987 年 12 月 18 日 Perl 1.0 发布起任 BDFL，Perl 6 项目（2019 年改名 Raku）长达近二十年的设计周期被认为反映 BDFL 模式在大型项目治理中的失效——BDFL 模式对个人决策者的依赖使其在项目规模扩张后难以维持有效治理；其二，Core Team 选举模式的代表性不足与决策效率困境：FreeBSD Core Team 9 名成员（2020 年代）的共识决策模型在社区 committer 数量增长至 400+ 人后决策效率下降，Core Team 选举制度长期遵循现行章程（2000-08-28 批准）的 committer 直选与两年任期制；2026-05-27 新批准章程改为年度选举并引入 Voting 与 Alternate 成员机制〔存疑：先前所记“先投票选出 2 名候选人再由 Core Team 内部补选”流程未见于 freebsd.org 章程文本，待一手来源核验〕；NetBSD Core Team 被批评“封闭性比 FreeBSD 更甚”，Core Team 成员长期稳定，新人进入极难；OpenBSD Theo de Raadt（西奥·德·若特） 事实独裁模式被批评“个人主导整个项目”；其三，商业公司对开源项目的过度影响：IBM 于 2018 年 10 月 28 日宣布以 340 亿美元（每股 190 美元现金）收购 Red Hat，Red Hat 作为 IBM 独立业务部门运营——Red Hat 是 Linux 内核贡献的最大企业雇主之一，收购引发关于企业资本对开源社区治理影响的担忧；Microsoft 维护 VS Code（基于 MIT 许可证）但同时掌控产品方向，VS Code 的核心开发与发布节奏由 Microsoft 决定，社区贡献者缺乏对项目方向的实质决策权；Apache Software Foundation（ASF，1999 年成立的 501(c)(3) 非营利组织）虽以 meritocracy（精英制）治理为标志但项目孵化与赞助仍受企业影响；其四，社区可持续性与 maintainer burnout（维护者倦怠）问题：Nadia Eghbal 2016 年发布的报告《Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure》揭示开源基础设施项目维护者长期承担不可见的劳动成本，资助与激励不足；FreeBSD committer 数量从 2000 年代高峰约 400 人逐步下降，新增 committer 速度低于退休速度；其五，贡献者流失与治理风险：2024 年 3 月 29 日 Andres Freund（微软工程师）发现 XZ Utils 后门（CVE-2024-3094，CVSS 评分 10），影响 xz/lzma 5.6.0 与 5.6.1 版本——后门通过 social engineering（社会工程学）方式使代号为 Jia Tan 的攻击者接管 XZ Utils 维护者身份，恶意代码仅植入 tarball 发行版而非 GitHub 上游源码，攻击者利用维护者身份将后门注入 SSH 认证链（sshd 依赖 liblzma）；XZ Utils 事件被视为开源治理失败的标志性案例——单一维护者倦怠后接受陌生人接管是治理机制缺位的直接显现，OpenSSF（Open Source Security Foundation）随后于 2024 年 4 月发布 Call to Action 呼吁加强开源基础设施治理

## 史观

- 总纲第 8 条——本体论上各方平等，志愿者、基金会专职 staff、企业贡献者等各方在治理结构中地位平等，从志愿者到基金会的演进体现社区规模扩张对治理结构的压力并重塑各方位置；统计结论印证：统计结论 [C-24] FreeBSD freebsd-src Gini 系数 0.9188（Bootstrap 95% CI [0.9093, 0.9270]）、统计结论 [C-25] DragonFly BSD dragonfly-src Gini 0.8972（[0.8517, 0.9187]）
- 总纲第 10 条——边缘者贡献，外部贡献者是社区 “动手者” 的典型代表，其贡献长期被 committer 叙事遮蔽
  - 辨析：外部贡献者的具体数量与贡献量需量化（以 Bugzilla/GitHub 统计为准）；企业外部贡献者与个人外部贡献者的动机差异需分析；mentor 瓶颈对外部贡献者转 committer 的具体影响需以 mentor 邮件列表讨论为据
  - 文献：Dahlander, L. & Magnusson, M. G. (2005). *Relationships Between Open Source Software Companies and Communities: Observations from Nordic Firms*. Research Policy, 34(4), 481-493
- 总纲第 10 条——边缘者贡献，管理学叙事中 “重要贡献者” 的定义常偏向决策层，忽视执行层与边缘层
  - 辨析：Core Team 成员的治理贡献需与代码贡献区分考据；离场成员的具体案例需逐一核查，避免事后叙事扭曲；Foundation 专职 staff 的具体贡献需以年度报告为据
  - 文献：FreeBSD Core Team Membership List (1993-2025). docs.freebsd.org
- 总纲第 4 条——分离聚合是永恒规律，各开源项目治理模式在分离与聚合中演化，差异反映不同社区文化与历史路径
  - 辨析：治理模式比较须控制项目规模与社区文化变量；“效率” 与 “合法性” 的衡量标准须明确；Linux 的 “仁慈独裁者” 模式在 Linus Torvalds 2018 年暂休事件后是否发生实质变化需考据；Python 2018 年 BDFL（Guido van Rossum）卸任后转向指导委员会制度的转型
- 总纲第 13 条——法律与道德是利益分配：BDFL 模式、Core Team 选举、商业公司影响、社区可持续性、贡献者流失五个维度的治理问题本质上是利益分配机制的形式主义化；总纲第 5 条——偶然性改写历史：Torvalds 2018 年道歉、Guido 2018 年卸任、IBM 2018 年收购 Red Hat、XZ Utils 2024 年后门事件皆是偶然性事件，偶然地塑造了开源治理批评的具体

## 辨析

- Core Team 选举制度的具体演变时间节点需考据；Foundation 专职 staff 的引入是否改变 Core Team 技术决策权需分析；双轨制中 Core Team 与 Foundation 的权责边界需以 By-Laws 原文为准；【0 信任原则·author 字段可伪造】L1.2.2 与 L3.4.1.top10 基于 author_email 统计，git 的 author 字段可伪造，统计结论须多源交叉验证后方可采信
- 外部贡献者的具体数量与贡献量需量化（以 Bugzilla/GitHub 统计为准）；企业外部贡献者与个人外部贡献者的动机差异需分析；mentor 瓶颈对外部贡献者转 committer 的具体影响需以 mentor 邮件列表讨论为据
  - 文献：Dahlander, L. & Magnusson, M. G. (2005). *Relationships Between Open Source Software Companies and Communities: Observations from Nordic Firms*. Research Policy, 34(4), 481-493
- Core Team 成员的治理贡献需与代码贡献区分考据；离场成员的具体案例需逐一核查，避免事后叙事扭曲；Foundation 专职 staff 的具体贡献需以年度报告为据
  - 文献：FreeBSD Core Team Membership List (1993-2025). docs.freebsd.org; FreeBSD Contributors List. (1993-2025). freebsd.org/doc/en_US.ISO8859-1/articles/contributors/
- 治理模式比较须控制项目规模与社区文化变量；“效率” 与 “合法性” 的衡量标准须明确；Linux 的 “仁慈独裁者” 模式在 Linus Torvalds 2018 年暂休事件后是否发生实质变化需考据；Python 2018 年 BDFL（Guido van Rossum）卸任后转向指导委员会制度的转型过程需与 FreeBSD Core Team 模式比较
  - 文献：Linux Foundation 章程
- BDFL 模式的“集中决策风险”在不同项目中表现不同——Linux 的 Torvalds 模式与 Python 的 Guido 模式、Perl 的 Larry Wall 模式各有差异，须分别考据不得普世化；【0 信任原则·多源交叉验证不可靠性规则】多个开源治理研究对 BDFL 模式的批评在多个独立来源中一致，但这一一致性可能源于对 BDFL 模式的共同前理解（个人主导即风险）而非独立验证。

## 文献

- FreeBSD Core Team. (2000-2025). *Core Team Reports*. lists.freebsd.org; McKusick, M. K., Neville-Neil, G. V., & Watson, R. N. M. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Addison-Wesley. (Chapter 1: History and Goals); FreeBSD Foundation. (2001-2025). *Annual Reports*
- Dahlander, L. & Magnusson, M. G. (2005). *Relationships Between Open Source Software Companies and Communities: Observations from Nordic Firms*. Research Policy, 34(4), 481-493; West, J. & O'Mahony, S. (2008). *The Role of Participation Architecture in Growing Sponsored Open Source Communities*. Ind
- FreeBSD Core Team Membership List (1993-2025). docs.freebsd.org; FreeBSD Contributors List. (1993-2025). freebsd.org/doc/en_US.ISO8859-1/articles/contributors/; Lakhani, K. R. & Wolf, R. G. (2005). *Why Hackers Do What They Do: Understanding Motivation and Effort in Free/Open Source Software Project
- Linux Foundation 章程； ASF Governance Documents; Python PEP 13; Rust Foundation Charter; O'Mahony, S. (2007). *The Governance of Open Source Projects: Does It Influence Innovation?* Journal of Management and Governance, 11(2), 123-146.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. <https://lkml.org/>；Linux Code of Conduct [EB/OL]. <https://www.kernel.org/doc/html/latest/process/code-of-conduct.html>；Python PEP 13 [EB/OL]. <https://www.python.org/dev/peps/pep-0013/>；IBM. IBM to Acquire Red Hat [EB/OL]. 2018-10-28. <https://www.ibm.com/>；Eghbal, N. (2016). *Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure*.
- FreeBSD Core Team. (2020-2025). *Core Team Reports*. lists.freebsd.org; Glass, R. L. (2002). *Facts and Fallacies of Software Engineering*. Addison-Wesley; O'Mahony, S. (2007). *The Governance of Open Source Projects: Does It Influence Innovation?* Journal of Management and Governance, 11(2), 123-146
- FreeBSD Release Engineering Team. (2003-2025). *Release Engineering Documentation*. docs.freebsd.org; McKusick, M. K. (2004). *The -CURRENT/-STABLE Branch Model*. USENIX BSDCon 2003; Erenkrantz, J. R. (2003). *Release Management Within Open Source Projects*. ICSE 2003 Workshop. ［B］
- Raymond, E. S. (1999). *The Cathedral and the Bazaar*. O'Reilly Media; von Krogh, G., Spaeth, S., & Lakhani, K. R. (2003). *Community, Joining, and Specialization in Open Source Software Innovation*. Research Policy, 32(7), 1217-1241; Shah, S. K. (2006). *Motivation, Governance, and the Viability of Hybrid Forms in Open Source Software Development*. Management Science, 52(7), 1000-1014


<!-- dangan-20260908 消解回写 -->
- Freund. A. (2024-03-29). *backdoor in upstream xz/liblzma leading to ssh server compromise* [EB/OL]. <https://www.openwall.com/lists/oss-security/2024/03/29/4>[EB/OL]. 2024.［DKC-0537→fulltext:5550］；Freund. A. (2024-03-29). *backdoor in upstream xz/liblzma* [EB/OL]. <https://www.openwall.com/lists/oss-security/2024/03/29/4>[EB/OL]. 2024.［DKC-0625→fulltext:5580］
<!-- /dangan-20260908 -->
## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
