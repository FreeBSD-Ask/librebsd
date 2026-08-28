---
chapter: 第 69 章
id: CH69
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 69 章 openbsd的起源与de-raadt被netbsd逐出

## 要点

- OpenBSD 仓库共 491195 次提交（1995-10-18 至 2026-08-25），427 位贡献者，提交量虽少于 FreeBSD 和 NetBSD，但代码审计文化使其每行代码经过更严格审查

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3990] 卷""第 69 章，匹配置信度 0.9，原因：
- [DB:bsdnow_podcast:outline_mappings:om_10418] BSD Now 第 676 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10451] BSD Now 第 671 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10471] BSD Now 第 666 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10498] BSD Now 第 663 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10665] BSD Now 第 634 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10686] BSD Now 第 630 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10797] BSD Now 第 613 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11082] BSD Now 第 578 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11169] BSD Now 第 567 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11193] BSD Now 第 565 期，匹配 CH69 章，关联度 1.0

- [DB:code_repos:openbsd.duckdb] OpenBSD 仓库共 491195 次提交（1995-10-18 至 2026-08-25），427 位贡献者，提交量虽少于 FreeBSD 和 NetBSD，但代码审计文化使其每行代码经过更严格审查

## 史观

- 和解优于斗争：OpenBSD 的起源虽源于冲突（de Raadt 被逐），但最终走向安全至上，将分裂转化为建设性力量

## 辨析

- 通知的具体措辞在不同叙事中略有差异——需对照邮件列表原始存档核实；经[邮件列表库]核查：netbsd-users 列表 1994 年存档缺失，逐出通知原文两库无法验证；netbsd 库 port-sparc/port-m68k 列表存 Theo de Raadt（<deraadt@fsa.ca> / <deraadt@theos.com>）1994-1995 年多封技术邮件（如 port-sparc 19
- 通知邮件与 de Raadt 自述在事实细节上存在冲突——需对照多方公开声明交叉验证
- 后果的正负评估在不同叙事中差异较大——部分视为 BSD 阵营的损失，部分视为 OpenBSD 安全文化的契机；需对照多方公开声明核实
- 评价与 de Raadt 自述在事实细节上可能存在冲突——需对照多方公开声明交叉验证
- 合图层的撰写须警惕两种叙事陷阱——其一为“Core Team 正当、de Raadt 应受惩戒”的组织中心叙事，其二为“de Raadt 受害、Core Team 专断”的个人英雄叙事；两种叙事均以道德判断取代史观审视，违反“不偏袒叙事姿态”；本事件的不可调和性源于前理解的根本差异（总纲第 19 条）——Core Team 以“社区准则”为前理解，de Raadt 以“工程优先”为前理解，两种前理

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第69章-openbsd的起源与de-raadt被netbsd逐出 第 69 章 openbsd的起源与de-raadt被netbsd逐出（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：15966 条 -->

### 要点（播客口述史提取）
- was you know it's partway scrolled down but it says uh blah blah ported to openbsd and netbsd（BSD Now EP112 @ 394.7799）
- previous contributions to OpenBSD? Sure. So I am originally from San Francisco, California.（BSD Now EP1 @ 2959.639）
- This is the first security bug fix update of the NetBSD 6.1 release branch.（BSD Now EP1 @ 6405.640）
- NetBSD was formed, and I was one of the first four people involved in NetBSD.（BSD Now EP6 @ 522.29）
- And NetBSD, in the NetBSD tree, we started incorporating all the other architectures（BSD Now EP6 @ 533.45）

### 史料（播客当事人陈述）
- and an interview with Peter Hessler about his OpenBSD BGP SpamD project.（BSD Now EP1 @ 21.10000）
- Brower and Ray Flotter from OpenBSD are also giving talks. Very cool. Okay. So next event,（BSD Now EP6 @ 1901.51）
- So for this week's interview, we're joined by Theo DeRat, the founder of OpenBSD.（BSD Now EP6 @ 494.13）
- that it became time to create a new repository, and this was the genesis of OpenBSD.（BSD Now EP6 @ 584.33）

### 史观（播客当事人观点与总纲映射）
- because I remember hearing the original story of NetBSD was,（BSD Now EP99 @ 4575.119）
  → 史观映射：总纲23——一切历史写作都是基于哲学设定的历史小说
- aspect, I think, is what sets OpenBSD apart. I think it's rare to have a group of 100（BSD Now EP6 @ 821.42）

### 辨析（播客争议与存疑点）
- [存疑脚注] you get then you get like uh mere os which is a fork of of openbsd which has put their shell（BSD Now EP149 @ 5849.520）
- [存疑脚注] a change that's disputed it'll be backed up by the core team until the（BSD Now EP186 @ 2538.58）

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
