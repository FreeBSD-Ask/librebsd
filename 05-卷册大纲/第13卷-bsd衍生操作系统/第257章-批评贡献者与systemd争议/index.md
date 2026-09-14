---
chapter: 第 257 章
id: CH257
volume: 第13卷-bsd衍生操作系统
---

# 第 257 章 批评贡献者与 systemd 争议

## 要点

- Linux 阵营对 BSD 治理的批评主要包括——其一，BSD Core Team 选举制效率低下（决策缓慢，如 CVS→SVN→Git 迁移迟缓）；其二，BSD 社区小团体化严重，外部贡献者难获认可；其三，BSD 许可证允许商业零回馈，使 BSD 成为“大公司的免费午餐”；其四，BSD 在桌面市场失败，反映 BSD 工程哲学不适合现代桌面需求。这些批评在 LKML、Reddit r/linux、Hacker News 等平台反复出现，构成 Linux 阵营对 BSD 的长期话语压力
- 商业 Unix 阵营（Oracle/Solaris、IBM/AIX、HP/HP-UX）对 BSD 治理的批评主要包括——其一，BSD 缺乏形式认证（UNIX 03/FIPS 140/Common Criteria），不适合企业合规需求；其二，BSD 商业支持薄弱（无与 Red Hat 同等级别的企业级支持）；其三，BSD 发布周期不稳定（FreeBSD 大版本间隔 2 年）。这些批评反映商业 Unix 阵营试图通过合规认证与企业支持门槛将 BSD 排除在企业市场之外的话语策略
- BSD 社区对 Linux 阵营也有反向批评——其一，Linux 内核由 Linus Torvalds 个人独裁，决策风险集中于个人；其二，Linux 生态被 Red Hat/IBM 控制垄断，开源独立性受质疑；其三，Linux 内核代码风格不一致，不同子系统差异大；其四，Linux 社区 LKML 毒性行为严重，对新人不友好。这些反向批评在 FreeBSD 邮件列表、OpenBSD 邮件列表、Theo de Raadt（西奥·德·若特） 公开发言中反复出现，构成 BSD 阵营对 Linux 的反向话语压力
- 学术界对 BSD/Linux 治理的批评相对中立——开源治理研究文献（如 O'Mahony 2007、Kelty 2008）对 BSD 与 Linux 治理模式均有批评，认为两者均存在小团体化、绩优主义形式主义、外部贡献者排斥等问题。学术批评的价值在于超越阵营立场，对开源治理的根本问题进行结构性分析。
- BSD/Linux 话语权争夺是开源运动内部的阵营对立，其形式主义呈现——BSD 阵营与 Linux 阵营各自以对方为“他者”建构自身认同，BSD 阵营以“许可证哲学纯粹性”建构认同，Linux 阵营以“市场份额与商业成功”建构认同。话语权争夺的形式主义化使双方均难以客观评价对方——BSD 阵营低估 Linux 的工程效率，Linux 阵营低估 BSD 的哲学价值。形式主义批评的史观辨析须保留双方的实质内容，同时警惕话语权运作的形式主义化

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4079] 卷“第13卷-bsd衍生操作系统”第 257 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4080] 卷“第13卷-bsd衍生操作系统”第 257 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4082] 卷“第13卷-bsd衍生操作系统”第 257 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:bsdnow_podcast:outline_mappings:om_10611] BSD Now 第 642 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10741] BSD Now 第 623 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10748] BSD Now 第 622 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10774] BSD Now 第 617 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10824] BSD Now 第 610 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10852] BSD Now 第 606 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10869] BSD Now 第 604 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10901] BSD Now 第 601 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11021] BSD Now 第 585 期，匹配 CH257 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11052] BSD Now 第 581 期，匹配 CH257 章，关联度 1.0

## 史观

- 总纲第 11 条——商品是形式主义：systemd 争议中的 systemd 作为商品的形式主义呈现
- 总纲第 15 条——文化即形式主义：systemd 争议中的文化即形式主义运作
- 总纲第 21 条——革命与改革是历史方法论的分歧：systemd 作为革命与 BSD rc.d 作为改革的方法论分歧，争议的不可调和性源于方法论分歧
- 总纲第 7 条——理论必须自反：本章对 systemd 争议的审视以自反姿态承认自身的形式主义化性质
- 总纲第 23 条——一切历史写作都是基于哲学设定的历史小说：本章对 systemd 争议的重构是基于项目统摄史观设定的历史小说
- 总纲第 2 条——历史是形式主义化的非存在：本章所写皆是当下主体的重构，从不宣称呈现 systemd 争议的历史本身

## 辨析

- Linux 阵营批评的具体来源须考据；“长期话语压力”的判断须有量化数据支持
- 商业 Unix 阵营批评的具体来源须考据；“排除竞争对手”的判断须有具体案例支持
- BSD 社区反向批评的具体来源须考据；Theo de Raadt 公开发言须以原文为准
- 学术批评的具体内容须以原文为准；“中立”的判断须警惕学术界自身的立场
- BSD/Linux 对立的具体案例须考据；用户文章的论断须按 0 信任原则考据

## 文献

- LKML；Reddit r/linux；Hacker News［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Oracle/IBM/HP 文档；企业 IT 咨询报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD/OpenBSD 邮件列表；Theo de Raadt 发言
- O'Mahony 2007；Kelty 2008；开源治理学术研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- BSD/Linux 对立档案；话语权研究文献；用户文章［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。
> 1985-2026 年间：1,474,340 次提交。
- 维护者/批评者自述；邮件列表；学术批评；用户史料
- iXsystems 公告与财务披露；PC-BSD/TrueOS 社区讨论存档；GhostBSD/MidnightBSD 捐赠页面 ［A］（2026-09-12 整改：行尾粘接的旧章号小节标题“## 256.14.7 社区治理中的利益冲突丑闻：Core Team 成员与企业利益的交织”系 256 章拆章残留（批次 C123 问题 6/7 剩余最后一处），已剥离留痕；该标题所指内容如须保留，应随 257.13-257.17 节号重排专项一并处置）
- FreeBSD Core Team 成员列表与雇主信息；FreeBSD Foundation IRS 990 表；Core Team 邮件列表；OpenBSD 邮件列表；Linux 内核 maintainer 统计

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。
> 1985-2026 年间：963,557 次提交。
- Ubuntu/Fedora/openSUSE 文档；Linux/BSD 桌面用户统计；硬件兼容性列表［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Juniper/NetApp/Sony 文档；Netflix/WhatsApp 文档；Android/Linux 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

