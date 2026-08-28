---
chapter: 第 314 章
id: CH314
volume: 第17卷-政治制度与社区治理
---

# 第 314 章 bsd-daemon词源与名称溯源

## 要点

- 汉语将 BSD daemon 译为“小恶魔”“恶魔”是基督教化语义的延续，丢失了古希腊守护神与 MIT 工程术语两层意涵；“恶魔”在汉语民间语境中带强烈邪性，与 BSD 项目原本的幽默守护意图相悖；中国民间信仰中“保家仙”（东北地区以黄鼠狼、狐狸、蛇、刺猬、鼠为“五大家仙”[考据完成：2026-08-04 五大家仙（狐黄白柳灰）属东北动物崇拜，五通神为江南男性神灵，非同一概念；存疑 id 1761
- 伯克利市名源考据须交叉验证伯克利市官方档案、UC Berkeley 校史、Frederick Billings 书信、George Berkeley 诗作原文四个独立来源；贝克莱哲学引用须以斯坦福哲学百科（SEP）为权威二手来源，并以 Berkeley 原著为终极一手来源；《FreeBSD 从入门到跑路》中关于伯克利市与贝克莱哲学的论述（`原材料/教材/` 整理）须作为中文语境的叙事参照，但其中任
- BSD 推广失败的判断须基于多重市场数据交叉验证——服务器市场份额（Netcraft/W3Techs）、云镜像可用性（AWS/Azure/GCP）、容器基础镜像下载量（Docker Hub）、高校课程采用率、技术媒体提及频次；社区自省须参照 FreeBSD Core Team 与 Foundation 历年公开声明中关于推广的反思；用户文章关于 BSD 推广失败的论述须按 0 信任原则考据；须区分
- 反批评者认为，BSD 未申请 UNIX 03/FIPS 140/Common Criteria 等形式认证是工程理性而非战略失败——认证费用高昂（UNIX 03 认证每次数万美元、FIPS 140 认证动辄数十万美元），FreeBSD Foundation 年预算仅约 200 万美元，将有限资源投入技术开发比形式认证更具性价比；“实质合规未形式认证”策略在技术上是合理的——FreeBSD 的 PO
- 再批评指出，认证缺位的“工程理性”论回避了长期代价——缺乏形式认证导致 FreeBSD 在政府采购、军事合规、企业采购等需要认证的领域被排除在外，损失的潜在市场价值远超认证费用；“实质合规”在实际采购中往往不被接受——政府采购与军事合规通常要求形式认证而非自证合规；macOS 的 UNIX 03 认证恰恰说明商业公司认为认证有价值——Apple 愿意支付认证费用说明认证在市场中确有回报；认证的战略

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3987] 卷“第17卷-政治制度与社区治理”第 314 章，匹配置信度 folder，原因：folder 第312章
- [DB:bsdnow_podcast:outline_mappings:om_11561] BSD Now 第 522 期，匹配 CH314 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12101] BSD Now 第 458 期，匹配 CH314 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10445] BSD Now 第 674 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10612] BSD Now 第 642 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10627] BSD Now 第 639 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10705] BSD Now 第 629 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10725] BSD Now 第 625 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10733] BSD Now 第 624 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10753] BSD Now 第 620 期，匹配 CH314 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10838] BSD Now 第 609 期，匹配 CH314 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- “黄鼠狼保家仙类比”是用户文章提出的再语境化尝试，须明确标注为类比而非定论；保家仙信仰有强烈的地域性（东北为主）与民间宗教属性，不宜普世化；汉语 BSD 翻译中是否存在“守护神”“护法”等更贴近古希腊原意的译法，须考据；用户文章的论断须按 0 信任原则考据验证，不得因其来自用户即直接采信；考据过程留痕——【查证来源】乌丙安《中国民间信仰》（上海人民出版社 1995 年 11 月初版，孔夫子旧书网商
- 伯克利市命名年份（1866）与加州大学创立年份（1868）须明确区分；George Berkeley 主教身份与哲学家身份的叙述平衡须把握；`原材料/教材/` 与用户文章中可能存在的简化叙事须逐一核对；汉语“贝克莱/伯克利”双译名的语境区分须全书一致
- 服务器市场份额统计的方法论差异（按域名/按流量/按活跃站点）须明确；“BSD 推广失败”的判断须限定语境，避免普世化；社区自省声明须警惕自我美化的自利偏差
- 认证费用的具体数额须考据；“实质合规”在政府/军事采购中是否被接受须区分场景
- 损失的潜在市场价值如何量化——反事实推理的方法论困难；认证缺位与知名度下降的因果关系须谨慎判定

## 文献

- `原材料/教材/` BSD daemon 翻译章节；用户文章（BSD daemon 词源考察）；中国民间信仰研究（如乌丙安《中国民间信仰》）；东北保家仙田野调查档案 ［B］---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.1 少数与多数（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- 伯克利市档案；UC Berkeley 校史；SEP, "George Berkeley"；Berkeley, Principles；`原材料/教材/`；用户文章 ［B］
- Netcraft 调查；W3Techs 统计；FreeBSD Foundation 年报；用户文章 ［B］
- The Open Group 认证费用文档；NIST CMVP 数据库；FreeBSD Foundation 年报 ［B］
- 政府采购合规要求文献；FreeBSD 市场分析；认证的商业价值研究 ［A］
- doc 仓库 git 历史；口述历史档案；Foundation 声明；用户文章 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：BSD 项目/徽标相关
- 三大 BSD 邮件列表存档；外部贡献者访谈；用户文章；BSD 会议记录 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：BSD 名称溯源
- Foundation 年报；口述历史档案；用户文章；Foundation 声明 ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第314章-bsd-daemon词源与名称溯源 -->

## 要点（播客口述史提取）
- This week on the show, we have Dragonfly BSD release 5.2.1 available,
- So first, they explain the problem. It's basically, a few months ago, I tried porting the FreeBSD
- where at first it was just, hey, let's virtualize FreeBSD on FreeBSD.
- playstation 4 the bug could also potentially be exploited on unpatched versions of freebsd
- So like I think what exists in FreeBSD, we have a driver implemented to do VertIO net in the kernel.
- any FreeBSD-based version older or equal to the host.
- Wow. Here we go. That's how old mail is and where it all started, at least from the BSD side.
- yeah don't try to mess with the share smb option in zfs that's not actually implemented in freebsd

## 史料（播客提及）
- [BSD Now EP248 @ 2578.89990234375] I think from what I've read, its goals appear very similar to what OpenBSD is running,
- [BSD Now EP248 @ 3117.659912109375] So like I think what exists in FreeBSD, we have a driver implemented to do VertIO net in the kernel.
- [BSD Now EP248 @ 3144.659912109375] I think in FreeBSD, the define that sets the sizing for VMs in FreeBSD is, I think, 16 vCPUs.
- [BSD Now EP248 @ 4323.7998046875] ocean with uh our coupon code freebsd now which gives you a ten dollar credit and i think we
- [BSD Now EP248 @ 6090.8798828125] yeah don't try to mess with the share smb option in zfs that's not actually implemented in freebsd

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP248 @ 2578.89990234375] I think from what I've read, its goals appear very similar to what OpenBSD is running,
- [BSD Now EP248 @ 3117.659912109375] So like I think what exists in FreeBSD, we have a driver implemented to do VertIO net in the kernel.
- [BSD Now EP248 @ 3144.659912109375] I think in FreeBSD, the define that sets the sizing for VMs in FreeBSD is, I think, 16 vCPUs.
- [BSD Now EP248 @ 4323.7998046875] ocean with uh our coupon code freebsd now which gives you a ten dollar credit and i think we
- [BSD Now EP248 @ 6090.8798828125] yeah don't try to mess with the share smb option in zfs that's not actually implemented in freebsd
- [BSD Now EP94 @ 1255.760009765625] BSD for MIPS. And actually with that, because of the more strict checking and
- [BSD Now EP94 @ 1380.199951171875] I remember a little while back when FreeBSD had got the, you know, it says it stays for
  → 史观映射：总纲18——时间是一种形式主义
- [BSD Now EP94 @ 4151.7001953125] Yeah. And I haven't personally checked out CBSD but there was a lot of talk at BSD Can

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP248 @ 133.22000122070312] There were also some improvements to IPFW3, their fork of the FreeBSD firewall.
- [存疑脚注] [BSD Now EP94 @ 1144.9599609375] that we had forked the repo for a hard and BSD stable,
- [存疑脚注] [BSD Now EP94 @ 537.3199462890625] Brooks Davis did one on CherryBSD, which is a research fork of FreeBSD.
- [存疑脚注] [BSD Now EP57 @ 1505.699951171875] They removed buying from FreeBSD base, and so there they switched some of the DNS utilities,
- [存疑脚注] [BSD Now EP113 @ 2385.6201171875] So first off, NextBSD kind of got split off of the FreeNAS 10 project
- [存疑脚注] [BSD Now EP113 @ 7498.1796875] They said they didn't want to throw the hardenedBSD bits into current

## 文献（播客参考条目）
- [BSD Now EP248] Pennington J. BSD Now: Episode 248: Show Me The Mooney | BSD Now 248[EB/OL]. (2018-05-29)[2026-08-15]. https://www.bsdnow.tv/248.
- [BSD Now EP94] Pennington J. BSD Now: 94: Builder's Insurance[EB/OL]. (2015-06-17)[2026-08-15]. https://www.bsdnow.tv/94.
- [BSD Now EP95] Pennington J. BSD Now: 95: Bitrot Group Therapy[EB/OL]. (2015-06-24)[2026-08-15]. https://www.bsdnow.tv/95.
- [BSD Now EP57] Pennington J. BSD Now: 57: The Daemon's Apprentice[EB/OL]. (2014-10-01)[2026-08-15]. https://www.bsdnow.tv/57.
- [BSD Now EP113] Pennington J. BSD Now: 113: What’s Next for BSD?[EB/OL]. (2015-10-28)[2026-08-15]. https://www.bsdnow.tv/113.
- [BSD Now EP267] Pennington J. BSD Now: Episode 267: Absolute FreeBSD | BSD Now 267[EB/OL]. (2018-10-10)[2026-08-15]. https://www.bsdnow.tv/267.
- [BSD Now EP219] Pennington J. BSD Now: 219: We love the ARC[EB/OL]. (2017-11-08)[2026-08-15]. https://www.bsdnow.tv/219.
- [BSD Now EP124] Pennington J. BSD Now: 124: Get your engine(x) started![EB/OL]. (2016-01-13)[2026-08-15]. https://www.bsdnow.tv/124.
- [BSD Now EP155] Pennington J. BSD Now: 155: Cabling up FreeBSD[EB/OL]. (2016-08-17)[2026-08-15]. https://www.bsdnow.tv/155.
- [BSD Now EP161] Pennington J. BSD Now: 161: The BSD Bromance[EB/OL]. (2016-09-28)[2026-08-15]. https://www.bsdnow.tv/161.

<!-- /PODCAST_MINE -->