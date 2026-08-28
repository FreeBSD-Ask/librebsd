---
chapter: 第 257 章
id: CH257
volume: 第13卷-bsd衍生操作系统
---

# 第 257 章 批评贡献者与systemd争议

## 要点

- Linux 阵营对 BSD 治理的批评主要包括——其一，BSD Core Team 选举制效率低下（决策缓慢，如 CVS→SVN→Git 迁移迟缓）；其二，BSD 社区小团体化严重，外部贡献者难获认可；其三，BSD 许可证允许商业零回馈，使 BSD 成为“大公司的免费午餐”；其四，BSD 在桌面市场失败，反映 BSD 工程哲学不适合现代桌面需求。这些批评在 LKML、Reddit r/linux、
- 商业 Unix 阵营（Oracle/Solaris、IBM/AIX、HP/HP-UX）对 BSD 治理的批评主要包括——其一，BSD 缺乏形式认证（UNIX 03/FIPS 140/Common Criteria），不适合企业合规需求；其二，BSD 商业支持薄弱（无与 Red Hat 同等级别的企业级支持）；其三，BSD 发布周期不稳定（FreeBSD 大版本间隔 2 年）。这些批评反映商业 Un
- BSD 社区对 Linux 阵营也有反向批评——其一，Linux 内核由 Linus Torvalds 个人独裁，决策风险集中于个人；其二，Linux 生态被 Red Hat/IBM 控制垄断，开源独立性受质疑；其三，Linux 内核代码风格不一致，不同子系统差异大；其四，Linux 社区 LKML 毒性行为严重，对新人不友好。这些反向批评在 FreeBSD 邮件列表、OpenBSD 邮件列表、T
- 学术界对 BSD/Linux 治理的批评相对中立——开源治理研究文献（如 O'Mahony 2007、Kelty 2008）对 BSD 与 Linux 治理模式均有批评，认为两者均存在小团体化、绩优主义形式主义、外部贡献者排斥等问题。学术批评的价值在于超越阵营立场，对开源治理的根本问题进行结构性分析。
- BSD/Linux 话语权争夺是开源运动内部的阵营对立，其形式主义呈现——BSD 阵营与 Linux 阵营各自以对方为“他者”建构自身认同，BSD 阵营以“许可证哲学纯粹性”建构认同，Linux 阵营以“市场份额与商业成功”建构认同。话语权争夺的形式主义化使双方均难以客观评价对方——BSD 阵营低估 Linux 的工程效率，Linux 阵营低估 BSD 的哲学价值。形式主义批评的史观辨析须保留双方

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

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Linux 阵营批评的具体来源须考据；“长期话语压力”的判断须有量化数据支持
- 商业 Unix 阵营批评的具体来源须考据；“排除竞争对手”的判断须有具体案例支持
- BSD 社区反向批评的具体来源须考据；Theo de Raadt 公开发言须以原文为准
- 学术批评的具体内容须以原文为准；“中立”的判断须警惕学术界自身的立场
- BSD/Linux 对立的具体案例须考据；用户文章的论断须按 0 信任原则考据

## 文献

- LKML；Reddit r/linux；Hacker News[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]## 256.13.2 商业 Unix 阵营对 BSD 治理的批评
- Oracle/IBM/HP 文档；企业 IT 咨询报告[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]## 256.13.3 BSD 社区对 Linux 阵营的反向批评
- FreeBSD/OpenBSD 邮件列表；Theo de Raadt 发言 ［A］## 256.13.4 学术界对 BSD/Linux 治理的批评
- O'Mahony 2007；Kelty 2008；开源治理学术研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]## 256.13.5 外部批评的史观辨析：BSD/Linux 话语权争夺的形式主义
- BSD/Linux 对立档案；话语权研究文献；用户文章[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:linux_kernel.duckdb -->> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1985-2026 年间：1,474,340 次提交。> 仓库总览：1,474,341 次提交，82,718 位贡献者，1970-01-01 至 2026-08-24。
- 维护者/批评者自述；邮件列表；学术批评；用户史料 ［A］## 256.14.6 BSD 衍生项目中的经费滥用案例：iXsystems 与 PC-BSD 的经费争议
- iXsystems 公告与财务披露；PC-BSD/TrueOS 社区讨论存档；GhostBSD/MidnightBSD 捐赠页面 ［A］## 256.14.7 社区治理中的利益冲突丑闻：Core Team 成员与企业利益的交织
- FreeBSD Core Team 成员列表与雇主信息；FreeBSD Foundation IRS 990 表；Core Team 邮件列表；OpenBSD 邮件列表；Linux 内核 maintainer 统计 ［A］<!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
- Ubuntu/Fedora/openSUSE 文档；Linux/BSD 桌面用户统计；硬件兼容性列表[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]## 256.15.2 BSD 与 Linux 在嵌入式与服务器市场的反向对比
- Juniper/NetApp/Sony 文档；Netflix/WhatsApp 文档；Android/Linux 文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]## 256.15.3 BSD 与商业 Unix（Solaris/AIX/HP-UX）的失败对比

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第257章-批评贡献者与systemd争议 第 257 章 批评贡献者与systemd争议（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：13139 条 -->

### 要点（播客口述史提取）
- But then I started to have some issues, I guess, most poignantly with SystemD when they did the whole upgrade from System5.（BSD Now EP71 @ 824.4000）
- and haven't introduced necessarily the feature creep that we have seen in SystemD.（BSD Now EP114 @ 397.1400）

### 史料（播客当事人陈述）
- With the growing adoption of SystemD, dissatisfaction with Linux has reached proportions not seen in recent years due to the extent that people are starting to talk of switching to FreeBSD.（BSD Now EP76 @ 785.5999）
- I know we've talked about SystemD's shim in OpenBSD or SystemBSD,（BSD Now EP106 @ 1034.299）
- some of the systemd daemons actually implement a lot more things than they document.（BSD Now EP106 @ 1180.739）

### 史观（播客当事人观点与总纲映射）
- But then I started to have some issues, I guess, most poignantly with SystemD when they did the whole upgrade from System5.（BSD Now EP71 @ 824.4000）
  → 史观映射：总纲10——动手者创造历史

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP35] Pennington J. BSD Now: 35: Puffy Firewall[EB/OL]. (2014-04-30)[2026-08-15]. https://www.bsdnow.tv/35.
- [BSD Now EP54] Pennington J. BSD Now: 54: Luminary Environment[EB/OL]. (2014-09-10)[2026-08-15]. https://www.bsdnow.tv/54.
- [BSD Now EP55] Pennington J. BSD Now: 55: The Promised WLAN[EB/OL]. (2014-09-17)[2026-08-15]. https://www.bsdnow.tv/55.
- [BSD Now EP60] Pennington J. BSD Now: 60: Don't Buy a Router[EB/OL]. (2014-10-22)[2026-08-15]. https://www.bsdnow.tv/60.
- [BSD Now EP67] Pennington J. BSD Now: 67: Must Be Rigged[EB/OL]. (2014-12-10)[2026-08-15]. https://www.bsdnow.tv/67.
- [BSD Now EP71] Pennington J. BSD Now: 71: System Disaster[EB/OL]. (2015-01-07)[2026-08-15]. https://www.bsdnow.tv/71.
- [BSD Now EP73] Pennington J. BSD Now: 73: Pipe Dreams[EB/OL]. (2015-01-21)[2026-08-15]. https://www.bsdnow.tv/73.
- [BSD Now EP76] Pennington J. BSD Now: 76: Time for a Change[EB/OL]. (2015-02-11)[2026-08-15]. https://www.bsdnow.tv/76.

<!-- /PODCAST_MINE -->
