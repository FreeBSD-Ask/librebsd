---
chapter: 第 77 章
id: CH77
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第77章 bsd项目的战略方向缺失与治理困境

## 要点

- 总纲第 5 条明示“没有必然性，只有偶然性。每一个关键人物、每一次 fork、每一个技术决定，都是不可替代的偶然。替代品的无限性不能否定事物的独特价值”。项目史观总纲第 5 章第 2 节“英雄人物的偶然性”进一步阐释“将英雄人物的出现必然化是一种机械的错误，没有认识到偶然性和自由的意义。那种认为‘张三不上李四也会上’的观点，无视了世界上没有必然性只有偶然性这一事实”。将这两重阐释应用于本章所述 BSD 三项目排外性与小团体文化争议，可揭示：FreeBSD、NetBSD、OpenBSD 三项目的分立本身是偶然事件——386BSD 中断、Theo de Raadt（西奥·德·若特） 与 NetBSD Core Team 的冲突、Jordan Hubbard 等人 fork 386BSD 的决定，皆是不可替代的偶然事件，不存在“BSD 必然分裂为三项目”的必然性。三项目的治理结构差异（Core Team 选举制、Foundation 董事会制、个体主导制）亦是偶然选择的产物，而非“最优治理结构”的必然结果。将 BSD 三项目的排外性归因于“BSD 哲学的必然产物”是机械的错误——排外性是三项目各自历史偶然路径上的具体呈现，而非 BSD 阵营共享的本质属性。Theo de Raadt 的独裁式排外是 de Raadt 个人风格与 NetBSD Core Team 冲突的偶然产物，并非 OpenBSD 安全定位的必然要求；Jordan Hubbard 2001 年辞职信揭示的 Core Team 封闭决策是 FreeBSD 选举制早期演化的偶然缺陷，并非 FreeBSD 治理结构的本质属性；NetBSD BSDCan 2011 仅 3 人到场的社区萎缩是 NetBSD 可移植定位与 Foundation 董事会制演化的偶然结果，并非 NetBSD 工程哲学的必然代价。项目统摄史观的审视在于：BSD 三项目排外性争议的史家书写须保留偶然性的维度，不将三项目的排外模式本质化为“BSD 阵营的共同特征”，亦不将任何一项目的排外模式正当化为“哲学必然”。
- 总纲第 8 条明示“本体论上各方平等。FreeBSD 相关记录（详情见存疑库）真正的斩杀线并非破产、失业或街头状态，而是：个体在一生中被制度性地安排为长期供养他人的角色，同时被灌输一种解释框架——将斩杀结果归因于个人能力不足或个人失败，从根本上否定对斩杀线本身进行质疑的合理性”。将这两重阐释应用于本章所述 BSD 三项目排外性与小团体文化争议，可揭示：BSD 三项目在本体论上地位平等——FreeBSD Core Team 选举制、NetBSD Foundation 董事会制、OpenBSD 个体主导制皆是 BSD 阵营治理结构的平等呈现，不存在“民主选举制优于独裁个体主导制”或“独裁个体主导制优于民主选举制”的本体论优劣。三种治理结构的差异仅是一刻状态的不同，各有其排外模式与合法性叙事，亦各有其工程成就与负资产——FreeBSD Core Team 选举制的负资产是封闭决策与“反应迟钝”（Jordan Hubbard 2001 辞职信、trasz@ 2025 年 12 月批评），OpenBSD 个体主导制的负资产是独裁式排外与新手敌意（LWN 2007 Corbet 报道、misc@ 邮件列表敌意），NetBSD Foundation 董事会制的负资产是社区萎缩与工具排外（BSDCan 2011 仅 3 人到场、pkgsrc 与 Ports 系统差异）。项目统摄史观“斩杀线”概念揭示：BSD 三项目的排外性本质是资源分配的具体行使——Core Team 选举制决定了谁获得 committer 权限、谁被排除在决策之外；Foundation 董事会制决定了谁获得资金与法律支持、谁被边缘化；个体主导制决定了谁获得 de Raadt 的认可、谁被排斥出 OpenBSD 生态。排外性不仅是社区文化现象，更是制度性的资源分配——“被排外者”被灌输一种解释框架（“个人能力不足”“风格不合”“贡献不达标”），从根本上否定对排外机制本身进行质疑的合理性。项目统摄史观的审视在于：BSD 三项目排外性争议的史家书写须保留本体论平等的维度，不将任何一项目的治理结构本质化为“最优”或“最劣”，亦须揭示排外性背后的资源分配逻辑，不将制度性排斥伪装为“个人能力问题”。

- 总纲第 19 条明示“解释学循环是历史认识的根本条件。前理解的差异使分歧不可避免。权力与知识在历史书写中共谋——什么被记录、什么被遗忘，本身就是权力行使”。项目史观总纲第 19 章第 2 节“前理解与分歧的产生”进一步阐释“我们往往预设了读者与作者享有相同的‘前理解’与‘前意识’。因此，随着讨论深入，分歧只会越来越多”，第 19 章第 3 节“权力与知识的共谋”指出“什么是‘重要的’历史事件，什么被记录，什么被遗忘，什么被视为‘错误’，什么被视为‘进步’——这些判断背后都有权力的运作”。将这三重阐释应用于本章所述 BSD 三项目排外性争议，可揭示：BSD 阵营与批评方对“排外性”的解释受各自前理解支配而不可调和。批评方的前理解将“透明度与开放性”视为社区健康标准，故读出排外性是“治理缺陷”——Jordan Hubbard 2001 年辞职信、trasz@ 2025 年 12 月批评、LWN 2007 Corbet 报道、BSDCan 2011 仅 3 人到场，皆是先前理解框架下的“治理缺陷”证据。BSD 阵营的前理解将“工程质量与文化特异性”视为社区使命，故读出排外性是“必要代价”——OpenBSD 二十余年安全审计、FreeBSD Core Team 选举制的代码质量保证、NetBSD 可移植定位的工程专注，皆是先前理解框架下的“必要代价”证据。前理解的不可调和性决定了辩证链不会以一方说服另一方终结，而以各方在各自前理解框架内自洽地解释排外性而持续——这正是总纲第 19 条所揭示的历史认识的根本条件。项目统摄史观“权力与知识的共谋”进一步揭示：什么被记录为“排外性事件”、什么被遗忘为“日常社区运作”，本身就是权力行使——批评方记录 Jordan Hubbard 2001 年辞职信与 trasz@ 2025 年 12 月批评以建构“BSD 排外”叙事，BSD 阵营记录 OpenBSD 安全审计与 FreeBSD Foundation 年报以建构“BSD 工程”叙事，二者皆是权力与知识的共谋。史家须警惕：将“排外性事件”作为 BSD 阵营的核心特征记录，与将“工程成就”作为 BSD 阵营的核心特征记录，皆是形式主义化的选择，背后皆有权力运作。
- FreeBSD 近 **30 年** 无正式路线图——首份 Technology Roadmap 迟至 **2021 年 9 月** 由 FreeBSD Foundation 发布，涵盖终端用户、商用服务器、工具应用、虚拟化容器四个方向；先前 FreeBSD 无任何形式化的发展规划或优先级文档。BSD vs Linux 路线图对比对照如下：
- NetBSD“无截止日期”发布模式（Pronchery 2014 论文“Carve your NetBSD”）——“it is done when considered ready”；NetBSD 无公开的功能路线图或战略文档；OpenBSD 唯一可预测结构为六个月发布周期但无公开功能规划

## 史观

- 总纲第 5 条——没有必然性，只有偶然性；总纲第 2 条——历史是形式主义化的非存在；总纲第 8 条——本体论上各方平等
  - 辨析：考据过程留痕——【查证来源】项目史观总纲第 5 条原文经 据原文第 25 章 Read 一手核验（2026-07-23 复核），项目史观总纲第 5 章第 2 节“英雄人物的偶然性”原文经 据原文第 5 章 Read 一手核验（2026-07-23 复核）〔待核：原文截断，后文待回源〕
- 组织结构塑造技术路径（专题语，不设总纲条号；原挂“总纲第 5 条——组织结构塑造技术路径”系伪标签，权威第 5 条为“没有必然性，只有偶然性”，依 2026-09-14 核查报告去条号留论旨）：路线图缺失反映 FreeBSD 治理结构的长期问题
- 辨析：路线图缺失的具体影响在不同叙事中略有差异——需对照 FreeBSD Foundation 公告核实
- 文献：FreeBSD Foundation Technology Roadmap 2021.9；Hubbard 2001 辞职信［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 76.7.

- 总纲第 4 条——分离聚合是永恒规律（原挂“总纲第 2 条——分离与聚合”系伪标签，权威第 2 条为“历史是形式主义化的非存在”；依 2026-09-14 核查报告改挂第 4 条）：三项目的分立是分离后产生的新聚合；总纲第 5 条——没有必然性，只有偶然性：三项目的定位差异是偶然选择的产物；总纲第 13 条——法律与道德是利益分配：BSD 许可证允许 fork 是法律结构，分叉争议本质是社区资源分配的争议
- 辨析：考据过程留痕——【查证来源】FreeBSD 官方关于页面、NetBSD 官方关于页面与历史页面、OpenBSD 官方 FAQ 与 g
- 总纲第 4 条——分离聚合是永恒规律（原挂“总纲第 2 条——分离与聚合”系伪标签，权威第 2 条为“历史是形式主义化的非存在”；依 2026-09-14 核查报告改挂第 4 条）：协同失败是 BSD 阵营分离过程的负资产；技术选择即政治选择（专题语，不设总纲条号；原挂“总纲第 7 条——技术选择即政治选择”系伪标签，权威第 7 条为“理论必须自反”，依 2026-09-14 核查报告去条号留论旨）：衡量“技术多样性”价值的标准之争本身是技术选择的政治维度；总纲第 13 条——法律与道德是利益分配：BSD 许可证允许 fork 是法律结构，但 fork 代价的分配是社区资源分配的实质问题
- 辨析：考据过程留痕——【查证来源】Linux 内核 subsystem maintainer

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 5 条原文经 据原文第 25 章 Read 一手核验（2026-07-23 复核），项目史观总纲第 5 章第 2 节“英雄人物的偶然性”原文经 据原文第 5 章 Read 一手核验（2026-07-23 复核），“将英雄人物的出现必然化是一种机械的错误”原文确认存在；〔待核：原文截断，后文待回源〕
- 路线图缺失的具体影响在不同叙事中略有差异——需对照 FreeBSD Foundation 公告核实
- 文献：FreeBSD Foundation Technology Roadmap 2021.9；Hubbard 2001 辞职信［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

#

- 分裂代价的程度在不同叙事中差异较大——需对照多方公开声明核实
  - 文献：BSD 三项目发展史；BSD vs Linux 对比研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 76.7.2 协同失败的批评

- 要点：BSD 三项目协同失败被长期批评——代码共享减少、跨
- 考据过程留痕——【查证来源】FreeBSD 官方关于页面、NetBSD 官方关于页面与历史页面、OpenBSD 官方 FAQ 与 goals 页面经 WebFetch 一手核验（2026-07-24 复核），三项目定位声明的关键表述（“features, speed, and stability”“portability”"correctness, security, standardizatio
- 考据过程留痕——【查证来源】Linux 内核 subsystem maintainer 体系与 driver 子系统架构的官方文档经 WebSearch 检索，具体一手原文 URL 未取得，沿用既有公开技术资料 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；OpenBSD `pf` 跨项目移植与 OpenSSH 跨项目采用的具体 release not

## 文献

- 本项目内部哲学文献《项目统摄史观》第 5 章“偶然性与必然性”、第 25 章总纲第 5 条（sacred 哲学源材料）；本章 30.1.1〔待核实节号〕 节 bsd_commits.duckdb 数据库证据；Jordan Hubbard 2001 辞职信［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；LWN 2007 Corbet 报道 ［A］；jmmv 2013 EuroBSDCon 报道 ［A］


<!-- dangan-20260908 消解回写 -->
- OpenBSD. Project. OpenBSD Hackathons [EB/OL]. <https://www.openbsd.org/hackathons.html>（2026-07-24 复核）[EB/OL]. 2026. ［DKC-1569→fulltext:5931］
<!-- /dangan-20260908 -->
## 76.10.2 总纲第 8 条审视：三项目本体论平等与“斩杀线”的资源分配

- 要点：总纲
- FreeBSD Foundation Technology Roadmap 2021.9；Hubbard 2001 辞职信［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 76.6.2 NetBSD 与 OpenBSD 的无规划传统

- 要点：NetBSD“无截止日期”发布模式（Pronchery 2014 论文“Carve your NetBSD”）——“it is done when considered ready”；NetBSD 无公开的功能路线图或战略文档；O
- BSD 三项目发展史；BSD vs Linux 对比研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 76.7.2 协同失败的批评

- 要点：BSD 三项目协同失败被长期批评——代码共享减少、跨项目协作困难、文档与社区用语差异扩大；协同失败加剧 BSD 阵营与 Linux 阵营的竞争力差距
- 史料：三项目主线合并记录、跨项目 committer 名单统计、BSDCan/AsiaBSDCon 历年议题对比 ［A］
- 史观：总纲第 4 条——分离聚合是永恒规律（原挂“总纲第 2 条——分离与聚合”系伪标签，权威第 2 条为“历史是形式主义化的非存在”；依 2026-09-14 核查报告改挂第 4 条）：协同
- FreeBSD Project. About FreeBSD [EB/OL]. <https://www.freebsd.org/about/>（2026-07-24 复核）；NetBSD Project. About NetBSD [EB/OL]. <https://www.netbsd.org/about/>（2026-07-24 复核）；NetBSD Project. History of the NetBSD Project [EB/OL]. <https://www.netbsd.org/about/history.html>（2026-07-24 复核）；OpenBSD Proje
- Linux 内核开发模式文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；Linux 内核 eBPF、cgroups 等技术创新扩散案例 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；OpenBSD `pf` 跨项目移植记录 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；OpenSSH 跨项目采用记录 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. <https://www.freebsd.org/about/>（2026-07-24 复核）；NetBSD Project. About NetBSD [EB/OL]. <https://www.netbsd.org/about/>（2026-07-24 复核）；NetBSD Pro
- 本项目内部哲学文献《项目统摄史观》第 19 章“历史解释学与权力”、第 21 章“革命与改革：历史方法论”、第 25 章总纲第 13、19、21 条（sacred 哲学源材料）；本章 30.1 至 30.7 三足鼎立格局辩证链；本章 30.2 节 BSD 许可证条款对比；本章 30.9 节同期操作系统比较；FreeBSD Project. About FreeBSD [EB/OL]. <https://www.freebsd.org/about/>（2026-07-24 复核）；NetBSD Project. About NetBSD [EB/OL]. <<https://www.netbsd>.
- BSDDN 跨项目 committer 名单；跨项目 committer 自述 ［A］

## 76.8.2 被边缘化者

- 要点：BSD 三项目存在被边缘化者——部分贡献者因项目分裂、社区冲突、风格不合等原因被边缘化；被边缘化者反映 BSD 阵营治理结构的问题
- 史料：BSD 三项目邮件列表历年存档、被边缘化者个人自述、开源社区访谈录 ［A］
- 史观：总纲第 10 条——动手者创造历史（原挂“总纲第 10 条——边缘者贡献”系自撰名目，权威第 10 条为“动手者创造历史”，依 2026-09-14 核查报告统一权威名目）：被边缘化者反映 BSD 阵营治理结构的问题
- 辨析：被边缘化的具体诱因在不同贡献者叙事中差异较大——需逐案核实
- 文献：BSD 三项目邮件列表存档；被边缘化者自述 ［A］

## 76.8

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP172（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Rod Grimes 自述 1970 年代初在 Oregon Museum of Science and Industry 的 PDP-11/45 上，利用夜间时段重新引导系统运行早期 AT&T Research Unix，白天机器则运行博物馆业务用的分时系统，并使用 Tektronix 4000 系列图形终端。（BSD Now EP172，[1331.76-1442.94]，L1）
- FreeBSD 创建时期，Rod Grimes 主要用 386BSD 做 SLIP 路由器以避开拨号 BBS 的 shell 上网方式，并借此获取 SPICE 等电子工程软件，时间约为 1992 年。（BSD Now EP172，[1487.16-1557.9]，L1）
- Rod Grimes 用 dd 反复读取坏块做磁盘数据恢复，指出 FreeBSD 在 ATA 或 SCSI 设备被卡住时不像其他系统那样锁死，因此长期用于路由器、LAMP 服务器与批量邮件系统。（BSD Now EP172，[1600.96-1667.48]，L1）
- FreeBSD 创始团队并未以竞争产品心态出发，只是出于必要与愿望；当时担心的并非被击垮，而是与 386BSD、BSDI、NetBSD 的关系，Linux 仅被视为另一份开源软件。（BSD Now EP172，[1807.66-1906.68]，L1）
- Rod Grimes 自认不适合仁慈独裁者角色，因自己观点强硬且无法掌握操作系统全部细节，并认为独裁模式长期会分裂团队，FreeBSD 实际采用接近 CSRG 伯克利团队的合作模式。（BSD Now EP172，[1900.99-2003.26]，L1）
- Rod Grimes 认为 FreeBSD 做得正确的包括系统性能、网络栈、ports collection，以及开源带来的可观察性，使系统状态易于查看。（BSD Now EP172，[2184.6-2295.72]，L1）
- Rod Grimes 认为项目早期过度锁定 x86 架构，使后来支持 MIPS 与 ARM 更困难；同时宣传不足，FreeBSD 虽很早运行于 Raspberry Pi 3，但快照未公开、网络与图形缺失，削弱了在 ARM64 嵌入式市场的影响。（BSD Now EP172，[2303.2-2494.7]，L1）
- Rod Grimes 希望 2017 年推进 GPL 代码移除（GPL clean release 为 12.0 目标）、ARM 与 MIPS 升至 Tier 1，并推进 bhyve 的 hypervisor 能力与 GPU passthrough。（BSD Now EP172，[2640.04-2725.56]，L1）
- Rod Grimes 与 Michael Dexter 合作推进 bhyve GPU passthrough，已能在 bhyve 内看到 PCI GPU 设备的 probe 与 I/O 映射，但内存块尚缺失，预期 2017 年初可见工作原型。（BSD Now EP172，[2726.62-2836.32]，L1）
- OpenSSH 7.4 由 Damien Miller 发起公开测试，移除 SSH v1 服务器支持与 3DES-CBC 默认密码，禁用预认证压缩与 UseLogin，并新增受 PuTTY 启发的 proxy multiplexing 与 curve25519-sha256 密钥交换。（BSD Now EP172，[94.39-364.48]，L2）
- Ingo Schwarze 在 Toulouse 的 LibreSSL hackathon 中完成 libcrypto 剩余 130 页手册的 pod2mdoc 转换，使全部文档可用 mdoc 检索，并回顾了 2014 年以来 Anthony Bentley 等人的转换史。（BSD Now EP172，[3495.94-3681.4]，L2）
- Matthew Garrett 批评 Canonical 的 IP 政策：若按政策理解，分发基于 Ubuntu 的作品即使不称 Ubuntu 也可能需向 Canonical 付费，这超出商标保护范围，故 Ubuntu 不是自由软件。（BSD Now EP172，[3872.04-4203.14]，L2）
- DEMOS 是 1982 年诞生于莫斯科原子能研究所的 Unix 类操作系统，源自 MNOS 对 Unix v6 的克隆，1986 至 1990 年各版本合并为 DEMOS 2，运行于 SM4、SM1600 及 VAX 克隆与 Motorola 6820 微机，后转向 Relcom。（BSD Now EP172，[4550.66-4645.46]，L2）

**史料**：

- Rod Grimes 访谈自述（FreeBSD 创始成员、BSD janitor），覆盖 1970 年代初 Unix 接触与 FreeBSD 创建史。（BSD Now EP172，[1315.96-3158.28]，L1）
- Damien Miller 发布的 OpenSSH 7.4 公开测试说明与变更清单。（BSD Now EP172，[94.39-393.72]，L2）
- Ingo Schwarze 的 LibreSSL 手册转换 hackathon 报告（含 pod2mdoc 转换时间线）。（BSD Now EP172，[3495.94-3681.4]，L2）
- Matthew Garrett 对 Canonical IP 政策的博客批评与 Mark Shuttleworth 的官方立场博客。（BSD Now EP172，[3872.04-4203.14]，L2）

**史观**：

- 总纲5 没有必然性，只有偶然性：Rod Grimes 强调 FreeBSD 的诞生出于必要与愿望而非与对手竞争，具体起点由当时的人和需求决定，而非历史必然。（BSD Now EP172，[1807.66-1906.68]，L3）
- 总纲6 和解优于斗争：Rod Grimes 认为独裁会分裂团队，合作环境更能避免分裂，治理选择倾向于和解而非斗争。（BSD Now EP172，[1945.54-2003.26]，L3）
- 总纲9 经验优先：ports collection 让“别人已完成的移植”成为可复用经验，使个体不必重复劳动，工程效率建立在经验累积之上。（BSD Now EP172，[2210.38-2247.96]，L3）
- 总纲10 动手者创造历史：Rod Grimes 以修复旧物、做数据恢复与移植为乐，历史由具体动手者而非抽象方案推进。（BSD Now EP172，[1600.96-1667.48]，L3）
- 总纲4 分离聚合是永恒规律：早期聚焦单一 x86 架构导致机独立代码不够架构中立，后期向 ARM/MIPS 迁移困难，单点聚焦与多架构分散之间存在结构张力。（BSD Now EP172，[2321.18-2399.88]，L3）

**辨析**：

- [存疑脚注] 转写将 OMSI 白天运行的分时系统记作“RISC-C”，疑为 DEC RSTS/E 的误转；Rod Grimes 首次接触 Unix 的具体年份与机型须以一手采访或档案复核。 [存疑脚注] 分时系统名与年份须核验一手资料。（BSD Now EP172，[1452.7-1463.98]，L4）
- [存疑脚注] OpenBSD Foundation 首笔铱金捐赠方转写为“smartizan/smartian”，疑指 Smartisan（锤子科技），280,000 加元金额与币种须核验官方公告。 [存疑脚注] 捐赠方名称与金额须核验。（BSD Now EP172，[4417.12-4457.48]，L4）
- [考据脚注] DEMOS 全称在转写中变形严重，应为俄语“Диалоговая Единая Мобильная Операционная Система”的英译，引用时须以俄文一手资料核验。 [考据脚注] 俄文全称须核验一手资料。（BSD Now EP172，[4557.02-4586.12]，L4）

**文献**：

- [BSD Now EP172] Pennington J. BSD Now: 172: A tale of BSD from yore[EB/OL]. (2016-12-14)[2026-08-15]. <https://www.bsdnow.tv/172>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1184 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1184`；w172 YouTube 章节路由采纳）

据〔DCBSDCon〕讲者 Jason Dixon 口述：DragonFly BSD 项目起于 FreeBSD 4.8 的延续，创始者因其对 SMP 线程模型的愿景而分叉。（YouTube EPYzXLwhkBe80，[994.5-998.78]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1185 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1185`；w172 YouTube 章节路由采纳）

据〔DCBSDCon〕讲者 Jason Dixon 口述：BSD 开发一度延续向 POSIX 合规推进；讲者称 AT&T 代码已成累赘（'the AT&T code was a hassle'），故引出 CSRG 的 Keith Bostic。（YouTube EPYzXLwhkBe80，[637.03-644.98]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-534 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-534`；w172 YouTube 章节路由采纳）

据〔NYCBSDCon 2007〕讲者 Jason Dixon 口述：1986 年 4.3BSD 相对 4.2BSD 引入性能改进；1988 年发布 4.3BSD-Tahoe（YouTube EPg7tvI6JCXD0，[404.1-413.299]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-533 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-533`；w172 YouTube 章节路由采纳）

据〔NYCBSDCon 2007〕讲者 Jason Dixon 口述：1983 年 4.2BSD 使用来自 BBN 的 TCP/IP（YouTube EPg7tvI6JCXD0，[390.539-394.159]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
