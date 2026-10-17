---
chapter: 第 290 章
id: CH290
volume: 第15卷-许可证哲学与法律分析
---

# 第290章 bsd跨项目效应的批评与贡献者

## 史料

- [DB:research_notes:blocks:112095] 关键词“bsd跨项目效应”命中：编号：11aj
定位：第11卷-136.9.5 反批评层
缺口类型：辨析充分性
建议动作：补入 McKusick 或 d…
- [DB:research_notes:blocks:8] 关键词“贡献者”命中：史实考据：CSRG 于 1994 年 6 月发布的 4.4BSD-Lite 官方 Release Notes，是 4.4…
- [DB:research_notes:blocks:20] 关键词“贡献者”命中：史实考据：Mike Karels 于 1995 年 6 月发出的告别邮件，标题或正文包含“Berkeley CSRG i…
- [DB:research_notes:blocks:354] 关键词“贡献者”〔待核：原文截断，后文待回源〕

## 要点

- BSD 跨项目贡献者包括——Poul-Henning Kamp（FreeBSD + Varnish + Jails 设计）、Kirk McKusick（FreeBSD + POSIX + FFS 设计）、Robert Watson（FreeBSD + Capsicum + CHERI + Cambridge 学术）、Jordan Hubbard（FreeBSD + Apple Darwin）、Tim Kientzle（FreeBSD + libarchive）、Bob Beck（OpenBSD + OpenSSH + LibreSSL）、Theo de Raadt（西奥·德·若特）（OpenBSD + OpenSSH + LibreSSL）、Damien Miller（OpenSSH portable 维护者，非 OpenBSD 核心成员）、Luke Mewburn（NetBSD + rc.d 设计）、Jason Evans（FreeBSD + jemalloc）、Peter Grehan（彼得·格雷汉）/Neel Natu（尼尔·纳图）/Ed Maste（埃德·马斯特）（FreeBSD + bhyve）、Roman Divacky/Brooks Davis（FreeBSD + LLVM/Clang）；这些跨项目贡献者构成 BSD 阵营跨项目影响的核心节点
- BSD 跨项目贡献中存在大量被忽视的贡献——jemalloc 曾被 Rust 作为默认分配器（后随 RFC 1974 全局分配器机制在 Rust 1.28 中稳定化，默认分配器已切换为系统分配器，但 jemalloc 仍通过 tikv-jemallocator crate 被大量 Rust 项目采用）；socket API 进入 POSIX 后 BSD 贡献被“标准化”掩盖；FFS 对 ext2 的设计影响常被忽视；libarchive 被 macOS（bsdtar）、Debian/Ubuntu（bsdtar 包）、Homebrew 等广泛采用，但作为“看不见的基础设施”默默支撑全球归档工具，鲜少被归功于 FreeBSD；这些被忽视的贡献反映 BSD 跨项目影响的“基础设施性”特征——影响越基础越容易被忽视
- BSD 跨项目贡献中存在被遗忘的贡献者——Björn Grönvall（OSSH 创建者，OpenSSH fork 的源头，1999 年初重新发现 Tatu Ylönen 的 SSH 1.2.12 最后自由版本并修复漏洞，但 OpenBSD 项目成员在 OpenBSD 2.6 发布前不到两个月才发现其工作，随即 fork 为 OpenSSH，Grönvall 此后逐渐淡出，其 OSSH 仅支持 SSH 1.3 协议且“可能在 OpenSSH 成熟后停止了开发”）在 OpenSSH 历史中长期被边缘化；Anders Berg（Varnish 项目发起者，VG 系统管理员，2005 年撰写项目规格书，自述“我是一个思考者而非执行者——我想出了 Varnish Cache 的想法，但执行者是其他人”）在 Varnish 历史中被 PHK 名声掩盖；Anders Nordby（Aftenposten 系统管理员，Varnish 项目的关键连接者——Berg 通过 Nordby 认识 PHK，Nordby 建议“找一个内核开发者”并推荐了 PHK，Varnish Software 官方历史明确记载 Nordby 参与项目启动）在 Varnish 叙事中几乎完全被遗忘；Dag-Erling Smørgrav（FreeBSD 提交者与安全官，2005 年底在巴塞尔 EuroBSD 会议上将 PHK 拉到一旁提出了 Varnish 项目构想，当时任 Linpro 顾问，后担任 FreeBSD Varnish port 维护者）在 Varnish 历史中更多被视为“连接者”而非“开发者”；Luke Mewburn（NetBSD rc.d 设计者，Wasabi Systems 工程师，USENIX ATC 2001 FREENIX Track 论文作者）在 rc.d 跨项目扩散中较少被归功；这些被遗忘的贡献者反映 BSD 跨项目叙事中的“明星效应”——项目创始人被铭记，协助者、连接者与早期推动者被遗忘
- BSD 跨项目贡献中边缘贡献者的史料辨析需关注——贡献记录的完整性（部分贡献未留下 commit 记录）、来源的多样性（需通过 commit、邮件列表、会议记录、个人自述等多源交叉核查）、叙事的偏差（明星效应导致协助者被遗忘）；辨析需通过多源史料重建，避免单一来源（如官方历史）的偏差；需注意 0 信任原则——即使贡献者自述也需独立验证
- 对 BSD 跨项目叙事中“明星效应”（项目创始人被铭记，协助者、连接者与早期推动者被遗忘）的批评，BSD 阵营的再回应聚焦于四点：第一为 **“明星效应部分源于贡献可见度差异而非纯粹叙事偏差”**——PHK 作为 Varnish 首席架构师的设计笔记（varnish-cache.org/docs/trunk/phk/firstdesign.html）是公开可查的技术贡献，而 Anders Berg 的“发起者”角色（自述“thinker, not a doer”）与 Anders Nordby 的“连接者”角色（建议“找一个内核开发者”并推荐 PHK）虽经 Varnish Software 官方历史记载，但其贡献可见度低于 PHK 的技术产出——此“可见度差异”部分源于贡献性质（技术产出 vs 协调角色）而非纯粹叙事偏差。第二为 **“被遗忘的贡献者经考据可重新归位”**——Björn Grönvall（OSSH 创建者）经 OpenSSH 官方历史核实为 OpenSSH fork 的源头（“fork from the OSSH release”）；Anders Berg 与 Anders Nordby 经 Varnish Software 官方历史与 Berg 自述 Q&A 双重印证；Dag-Erling Smørgrav（DES）经 PHK 自述核实为 Varnish 项目构想者（“DES 在 EuroBSD 会议上把我拉到一旁”）；Luke Mewburn 经 NetBSD **rc.d(8)** 手册页与 USENIX 2001 论文双重印证为 rc.d 设计者——考据程序本身是对边缘者的重新归位，而非“永久遗忘”。第三为 **“freebsd.duckdb 的量化分析可部分修复边缘者被遗忘”**——freebsd.duckdb 查询 L7.2.1 显示衍生项目贡献者在 freebsd-src 的回馈前 10 位，其中 <behlendorf1@llnl.gov>（LLNL，OpenZFS 核心开发者）2,603 次、<ryan@iXsystems.com>（iXsystems）329 次、<mahrens@delphix.com>（Delphix）229 次等——这些量化数据使部分“看不见的贡献者”可见，修复了纯粹叙事中的边缘者遗忘。第四为 **“边缘者被遗忘是‘基础设施性’的代价而非道德失败”**——BSD 跨项目影响的“基础设施性”特征使贡献越基础越容易被忽视——libarchive 作为“看不见的基础设施”默默支撑 macOS/Debian/Homebrew，其贡献者 Tim Kientzle 与 Martin Matuska 的知名度低于 Varnish 的 PHK，此“知名度差异”是“基础设施性”的代价（影响越基础越容易被忽视）而非道德失败。

## 史观

- 总纲第 10 条——动手者创造历史：跨项目贡献者是 BSD 阵营跨项目影响的关键贡献者；考据规则（专题语，不设总纲条号）：贡献者名单需通过考据程序验证；统计结论印证：C-24/C-25/C-26/C-27 揭示 BSD 4 项目贡献者分布的高度集中——Gini 系数 0.82-0.92 意味着贡献极度不均，top 10% 贡献者承担约 90% commit 量，此量化结论为 “明星效应” 提供数据基础
- 总纲第 10 条（动手者创造历史）与考据规则（专题语，不设总纲条号）。BSD 阵营的再回应实质上是将“明星效应”与“边缘者被遗忘”的批评置于“贡献可见度差异”与“考据程序修复”的框架下重新审视——明星效应部分源于贡献性质差异而非纯粹叙事偏差，且考据程序本身是对边缘者的重新归位。项目统摄史观第十章“边缘者贡献”（源文本章节，非 25 条总纲条目）在此显现：边缘者非“被动的受害者”而是“主动的贡献者”，考据程序使其贡献被重新发现。
- 〔待核：史观段原文截断，后文待回源〕
- 总纲第 10 条（动手者创造历史）与项目统摄史观第六章（主体性与和解，源文本章节，非 25 条总纲条目）。BSD 跨项目贡献者的核心即“明星可见与边缘者被遗忘的辩证统一”——明星因技术产出可见度高而被铭记，边缘者因协调角色可见度低而被遗忘，二者是同一项目的两面。项目统摄史观第十章“边缘者贡献”（源文本章节）在此显现：边缘者非“被动的受害者”而是“主动的贡献者”，考据程序使其贡献被重新发现。
- **辨析**：考据过程留痕——【查证来源】Varnish Software 官方历史（varnish-software.com/varnish-history/）与 Berg 2016 年 Q&A〔待核：本行原文截断，详见辨析节同源条目；后文待回源补全〕
- 总纲第 13 条——法律与道德是利益分配：BSD 许可证的设计决定了回馈不足的结构性；总纲第 3 条——不存在进步只有权力再分配：商业采用与社区回馈的不对称
  - rvalds 批评的语境须查原访谈；0 信任原则局限标注：L3.2.1 查询基于 12 类商业邮箱域名（@netflix.com/@juniper.net/@netapp.com/@ixsystems.com 等）
- 项目统摄史观第五章（道与术的辩证，源文本章节，非 25 条总纲条目）与总纲第 13 条（法律与道德是利益分配）。BSD 阵营的反批评实质上是将“回馈不足”“话语权丧失”“资源分散”的批评置于“许可证设计意图”“标准化必然结果”“广泛孵化文化代价”的框架下重新审视——此三者非“失败”而是“设计代价”。项目统摄史观第五章“道与术的辩证”（源文本章节）在此显现：BSD 许可证作为“道”（哲学原则）允许“术”（具体采用）的无回馈，此“无回馈”非“道”的失败而是“道”〔待核：原文截断，后文待回源〕

## 辨析

- 每位贡献者的具体跨项目角色须逐个核实——如 Watson 在 CHERI 中的角色 vs FreeBSD 中的角色须区分；Damien Miller 在 OpenSSH portable 中的角色须查 openssh.com 治理文档；〔待核：原文截断，后文待回源〕
- 考据过程留痕——【查证来源】Varnish Software 官方历史（varnish-software.com/varnish-history/）经一手核验明确记载 Anders Nordby 参与项目启动；Anders Berg 2016 年 Q&A（varnish-software.com/blog）经一手核验自述“thinker, not a doer”与 Nordby 推荐 PHK 的细
- 考据过程留痕——【查证来源】Varnish Software 官方历史（Berg 发起、Nordby 连接、DES 构想、PHK 执行）经 varnish-software.com/varnish-history/ 一手核验；OpenSSH 官方历史（Grönvall 的 OSSH 为 fork 源头）经 openssh.org/history.html 一手核验；bsd_commits.duckdb 查
- 回馈“不足”的量化标准须明确——是 commit 数、代码行数还是资金量；OpenBSD 资金紧张的具体数据须查基金会年报；Torvalds 批评的语境须查原访谈；0 信任原则局限标注：L3.2.1 查询基于 12 类商业邮箱域名（@netflix.com/@juniper.net/@netapp.com/@ixsystems.com 等）匹配，企业员工若用个人邮箱（@gmail.com）或 @u
- 考据过程留痕——【查证来源】Torvalds 1998 年 LinuxFocus 访谈（linuxdoc.org/linuxfocus/English/March1998/article27.html）经一手核验明确表示“GPL 保证回馈”但“GPL 与 BSD 无本质优越性”；**OpenBSD Copyright Policy 官方文档**（openbsd.org/policy.html，经

## 文献

- 各项目 commit 历史；BSDCan 议程 ［A］；bsd_commits.duckdb L7.2.1 查询报告（衍生项目与跨项目对比分析.md §L7.2.1）；bsd_commits.duckdb C-24/C-25/C-26/C-27 查询报告（推断性统计.md Task 10 + 描述性统计.md SubTask 2.3）；外部基准 E-09 查询报告（外部基准-GitHub-CHAOSS.md 第 3 节）

## 290.10.2 被忽视的跨项目贡献

- 要点：BSD 跨项目贡献中存在大量被忽视的贡献——jemalloc 曾被 Rust 作为默认分配器（后随 RFC 1974 全局分配器机制
- Varnish Software. Official History [EB/OL]. <https://varnish-software.com/varnish-history/>; Berg A. Q&A 2016 [EB/OL]. <https://varnish-software.com/blog>; OpenSSH. Official History [EB/OL]. <https://openssh.org/history.html>; Mewburn L. The Design and Implementation of the NetBSD rc.d System [R]. U
- Varnish Software. Official History [EB/OL]. <https://varnish-software.com/varnish-history/>; OpenSSH. Official History [EB/OL]. <https://openssh.org/history.html>; openbsd.duckdb L7.2.1 查询报告; 项目史观总纲第十章“边缘者贡献”[Z]. **sacred_sources.duckdb**（项目统摄史观第 10 章）.
- de Raadt 资金呼吁；Torvalds 评论；基金会年报 ［B］；bsd_commits.duckdb L3.2.1 查询报告（深层信息挖掘.md §L3.2.1）；bsd_commits.duckdb L7.2.1 查询报告（衍生项目与跨项目对比分析.md §L7.2.1）

## 290.9.2 BSD 效应力被 Linux 阵营抢占话语权的批评

- 要点：BSD 跨项目影响虽广但话语权长期被 Linux 阵营抢占——Jails 早于 Docker 13 年但 Docker 流行化后被广泛称为“容器革命”，Jails 的开创性贡献被忽视；socket API 进入 POSIX 后被普遍称为"POS
- Torvalds L. LinuxFocus Interview [EB/OL]. (1998-03). <https://linuxdoc.org/linuxfocus/English/March1998/article27.html>; de Raadt T. Request for Funding our Electricity [EB/OL]. openbsd-misc mailing list, 2014-01; bsd_commits.duckdb L3.2.1 查询报告; bsd_commits.duckdb L7.2.1 查询报告; 项目史观总纲第五章“道与术的辩证”[Z]. **sacred_sources.duckdb**（项目统摄史观第 5 章）〔待核：原文截断，后文待回源〕
- de Raadt T. Request for Funding our Electricity [EB/OL]. openbsd-misc mailing list, 2014-01; The Register. Bitcoin donation saves OpenBSD [EB/OL]. 2014-01-20; openbsd.duckdb L3.2.1 查询报告; Postel J. RFC 793: Transmission Control Protocol [S]. 1981; FreeBSD 4.0 release notes [EB/OL]. 2000-03; Docker offici
- openbsd.duckdb L3.2.1 查询报告； openbsd.duckdb L7.2.1 查询报告； 项目史观总纲第六章“主体性与和解”[Z]. **sacred_sources.duckdb**（项目统摄史观第 6 章）; 项目史观总纲第二十四章“许可证哲学”[Z]. **sacred_sources.duckdb**（项目统摄史观第 24 章）.
- 项目史观总纲第 13、19、21 条 [Z]. **sacred_sources.duckdb**（项目统摄史观第 25 章）; 项目史观总纲第十三章“文艺与审美历史哲学”[Z]. **sacred_sources.duckdb**（项目统摄史观第 13 章）; 项目史观总纲第十九章“历史解释学与权力”[Z]. **sacred_sources.duckdb**（项目统摄史观第 19 章）; 项目史观总纲第二十一章“革命与改革：历史方法论”[Z]. **sacred_sources.duckdb**（项目统摄史观第 21 章）; BSD 许可证文本 [EB/OL]. <https://www.freebsd.org/copyright/freebsd-license/>; GPL 文本 [EB/OL]. <https:

## 本章节索引

- [290.9 对 BSD 跨项目效应的批评：自由放任的代价与话语权丧失](290.9-对-BSD-跨项目效应的批评-自由放任的代价与话语权丧失.md)
- [290.10 重要贡献者与边缘者：跨项目贡献者与被边缘化者](290.10-重要贡献者与边缘者-跨项目贡献者与被边缘化者.md)

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。