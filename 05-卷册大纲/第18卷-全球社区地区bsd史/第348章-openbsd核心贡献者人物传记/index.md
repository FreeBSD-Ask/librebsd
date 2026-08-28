---
chapter: 第 348 章
id: CH348
volume: 第18卷-全球社区地区bsd史
---

# 第 348 章 openbsd核心贡献者人物传记

## 要点

OpenBSD 项目自 1995 年从 NetBSD 分叉以来，其核心贡献者群体形成了以 Theo de Raadt 为中心的独特技术社区。本章收录 OpenBSD 核心贡献者的人物传记，涵盖开发者（committer）、文档贡献者、发行工程与测试人员等角色。OpenBSD 的贡献者群体以安全至上哲学为共同纽带，在项目 30 年历史中维持了高度稳定的核心团队——与 FreeBSD 和 NetBSD 相比，OpenBSD 的核心贡献者更替率最低，反映出其 BDFL 治理模式下的社区凝聚力与潜在的单点故障风险。

## 史料

- OpenBSD 官方开发者列表（openbsd.org）—— 一手网络史料 ［A］
- OpenBSD 源代码仓库提交记录（openbsd.duckdb）—— 一手代码史料 ［A］
- OpenBSD 邮件列表 archives（marc.info）—— 一手网络史料 ［A］
- [DB:bsdnow_podcast:outline_mappings] BSD Now 播客多期涉及 OpenBSD 开发者访谈 —— 二手口述史料 ［B］
- [DB:references_fulltext:chapter_matches:chmatch_3633] 参考文献数据库匹配 —— 二手文献 ［B］
- OpenBSD 项目历史文档与 release announcements —— 一手网络史料 ［A］

## 史观

总纲第 15 条——安全至上哲学如何塑造贡献者群体的技术选择与社区文化；总纲第 7 条——动手者创造历史，OpenBSD 贡献者的技术实践（如代码审计、pledge/unveil 机制开发）是安全文化形成的物质基础；总纲第 5 条——经验优先，以提交记录与邮件列表为优先依据重建贡献者谱系；总纲第 12 条——BDFL 治理模式在开源社区中的权力集中与分散的辩证关系。

## 辨析

OpenBSD 的贡献者谱系研究面临若干方法论挑战：其一，OpenBSD 项目以代码审查严格著称，大量外部贡献者的 patch 经核心开发者修改后合入，原始作者身份在提交记录中可能被稀释——这要求区分"代码作者"与"提交者"两个层面；其二，Theo de Raadt 的 BDFL 角色使贡献者传记的叙事天然倾向于中心化，容易忽视边缘贡献者（如端口维护者、文档翻译者）的贡献；其三，OpenBSD 社区对"贡献者"的定义与其他 BSD 项目不同——OpenBSD 更强调代码质量而非贡献数量，这使得跨项目贡献者比较存在口径差异。本章在编纂时以提交记录为客观基准，辅以邮件列表讨论与公开访谈交叉验证，但须承认量化指标（如提交次数）不能完全反映贡献者的实际影响力。

## 文献

- OpenBSD 开发者列表（openbsd.org）
- OpenBSD 源代码仓库（cvsweb.openbsd.org）
- OpenBSD 邮件列表 archives
- BSD Now 播客相关期数（见史料字段 om_xxxxx 映射）
- 参考文献数据库匹配记录（chmatch_3633）

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第348章-openbsd核心贡献者人物传记 -->

## 要点（播客口述史提取）
- the OpenSend 23.1.1 release, how to clone a system with Ansible, FOSDEM 2023 trip reports from NetBSD,
- Crystal Colipay again created some patches for taking screenshots of the BSD console.
- developed sys trace but it turned out it was difficult to use the only user in open bsd base
- which was later renamed to pledge. Pledge was developed by studying all programs in OpenBSD
- So, next up in the news here, OS News has started a BSD family segment.
- So I guess it looks like an OS News reader decided to share some info about the BSDs,
- The system kind of like ports for net BSD has branched their 2013 Q3 version.
- first up, we got VBSDCon coming October 25th to the 27th. And the website's VBSDCon.com.

## 史料（播客提及）
- [BSD Now EP498 @ 784.739990234375] developed sys trace but it turned out it was difficult to use the only user in open bsd base
- [BSD Now EP6 @ 2563.59] it into mainline FreeBSD. Yeah, I think it's a good incubator for some of the cool stuff.
- [BSD Now EP6 @ 2894.54] I think free BSD could be at a tipping point. I'm glad you guys are leading the charge.
- [BSD Now EP6 @ 637.69] through to the SAP people, and also actually communicated with people in the BSD community
- [BSD Now EP6 @ 821.42] aspect, I think, is what sets OpenBSD apart. I think it's rare to have a group of 100

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP498 @ 784.739990234375] developed sys trace but it turned out it was difficult to use the only user in open bsd base
  → 史观映射：总纲14——苦难不值得被提倡
- [BSD Now EP6 @ 2563.59] it into mainline FreeBSD. Yeah, I think it's a good incubator for some of the cool stuff.
- [BSD Now EP6 @ 2894.54] I think free BSD could be at a tipping point. I'm glad you guys are leading the charge.
- [BSD Now EP6 @ 637.69] through to the SAP people, and also actually communicated with people in the BSD community
- [BSD Now EP6 @ 821.42] aspect, I think, is what sets OpenBSD apart. I think it's rare to have a group of 100
- [BSD Now EP1 @ 1427.760009765625] because it actually works on freebsd it's like a web hosting shared web hosting control panel
- [BSD Now EP1 @ 1785.93994140625] and actually just have them be put into as articles in not the handbook, but in the FreeBSD documentation tree.
- [BSD Now EP1 @ 2718.81982421875] thing they've always had bsd stuff there and this year the keynote is actually given by kirk mccusick

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP6 @ 2058.23] Sure. The big thing for free BSD 10 are much better Beehive and Zen. More GNU stuff removed.
- [存疑脚注] [BSD Now EP6 @ 2498.63] Not TrueOS specifically. The stats come in, they look the same for both. So I just see it as FreeBSD
- [存疑脚注] [BSD Now EP1 @ 2369.199951171875] quite some time i'm sure pcbsd in particular has got lots of complaints about this
- [存疑脚注] [BSD Now EP1 @ 432.5] back uh yeah so uh back to veris oh yeah yeah uh they said you know bsd is quite literally at the
- [存疑脚注] [BSD Now EP186 @ 30.0] This is BSD Now, episode 186, the Fast and the Firewall Tokyo Drift.

## 文献（播客参考条目）
- [BSD Now EP498] Pennington J. BSD Now: 498: Dropping Privileges[EB/OL]. (2023-03-16)[2026-08-15]. https://www.bsdnow.tv/498.
- [BSD Now EP6] Pennington J. BSD Now: 6: Doing It de Raadt Way[EB/OL]. (2013-10-09)[2026-08-15]. https://www.bsdnow.tv/6.
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.
- [BSD Now EP523] Pennington J. BSD Now: 523: Literally Unix[EB/OL]. (2023-09-07)[2026-08-15]. https://www.bsdnow.tv/523.
- [BSD Now EP203] Pennington J. BSD Now: 203: For the love of ZFS[EB/OL]. (2017-07-19)[2026-08-15]. https://www.bsdnow.tv/203.
- [BSD Now EP198] Pennington J. BSD Now: 198: BSDNorth or You can’t handle the libtruth[EB/OL]. (2017-06-14)[2026-08-15]. https://www.bsdnow.tv/198.
- [BSD Now EP258] Pennington J. BSD Now: Episode 258: OS Foundations | BSD Now 258[EB/OL]. (2018-08-08)[2026-08-15]. https://www.bsdnow.tv/258.
- [BSD Now EP238] Pennington J. BSD Now: 238: VLAN-Zezes-ki in Hardware[EB/OL]. (2018-03-21)[2026-08-15]. https://www.bsdnow.tv/238.
- [BSD Now EP186] Pennington J. BSD Now: 186: The Fast And the Firewall: Tokyo Drift[EB/OL]. (2017-03-22)[2026-08-15]. https://www.bsdnow.tv/186.
- [BSD Now EP112] Pennington J. BSD Now: 112: Tracing the source[EB/OL]. (2015-10-21)[2026-08-15]. https://www.bsdnow.tv/112.

<!-- /PODCAST_MINE -->