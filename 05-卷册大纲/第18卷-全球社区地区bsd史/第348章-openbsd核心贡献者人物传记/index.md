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
<!-- 章节主题过滤：第348章-openbsd核心贡献者人物传记 第 348 章 openbsd核心贡献者人物传记（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：15966 条 -->

### 要点（播客口述史提取）
- previous contributions to OpenBSD? Sure. So I am originally from San Francisco, California.（BSD Now EP1 @ 2959.639）
- that it became time to create a new repository, and this was the genesis of OpenBSD.（BSD Now EP6 @ 584.33）
- Yeah, so I guess first up we have stuff from the OpenBSD guys.（BSD Now EP14 @ 327.2999）
- So first up, looks like OpenBSD had a hackathon in Slovenia.（BSD Now EP47 @ 68.19999）
- so they've ported the OpenBSD one over and now they're cleaning up and improving it（BSD Now EP99 @ 1121.880）

### 史料（播客当事人陈述）
- and an interview with Peter Hessler about his OpenBSD BGP SpamD project.（BSD Now EP1 @ 21.10000）
- Brower and Ray Flotter from OpenBSD are also giving talks. Very cool. Okay. So next event,（BSD Now EP6 @ 1901.51）
- So for this week's interview, we're joined by Theo DeRat, the founder of OpenBSD.（BSD Now EP6 @ 494.13）
- that it became time to create a new repository, and this was the genesis of OpenBSD.（BSD Now EP6 @ 584.33）

### 史观（播客当事人观点与总纲映射）
- aspect, I think, is what sets OpenBSD apart. I think it's rare to have a group of 100（BSD Now EP6 @ 821.42）

### 辨析（播客争议与存疑点）
- [存疑脚注] you get then you get like uh mere os which is a fork of of openbsd which has put their shell（BSD Now EP149 @ 5849.520）

### 文献（播客参考条目）
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.
- [BSD Now EP6] Pennington J. BSD Now: 6: Doing It de Raadt Way[EB/OL]. (2013-10-09)[2026-08-15]. https://www.bsdnow.tv/6.
- [BSD Now EP11] Pennington J. BSD Now: 11: The Gateway Drug[EB/OL]. (2013-11-13)[2026-08-15]. https://www.bsdnow.tv/11.
- [BSD Now EP14] Pennington J. BSD Now: 14: Zettabytes for Days[EB/OL]. (2013-12-04)[2026-08-15]. https://www.bsdnow.tv/14.
- [BSD Now EP43] Pennington J. BSD Now: 43: Package Design[EB/OL]. (2014-06-25)[2026-08-15]. https://www.bsdnow.tv/43.
- [BSD Now EP47] Pennington J. BSD Now: 47: DES Challenge IV[EB/OL]. (2014-07-23)[2026-08-15]. https://www.bsdnow.tv/47.
- [BSD Now EP64] Pennington J. BSD Now: 64: Rump Kernels Revisited[EB/OL]. (2014-11-19)[2026-08-15]. https://www.bsdnow.tv/64.
- [BSD Now EP99] Pennington J. BSD Now: 99: BSD Gnow[EB/OL]. (2015-07-22)[2026-08-15]. https://www.bsdnow.tv/99.

<!-- /PODCAST_MINE -->
