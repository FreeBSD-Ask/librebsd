---
chapter: 第 72 章
id: CH72
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 72 章 openbsd起源的史观审视

## 要点

- 本事件的史观审视承认争议的不可调和性——这并非失败的叙事，而是项目统摄史观对历史诚实性的要求；和解优于斗争，但和解不等于消解分歧；本体论上各方平等，但平等不等于抹平差异；OpenBSD 的诞生既是分离的撕裂，也是新主体性的呈现——这一刻的 BSD 家族，因不可调和的争议而更加完整；史家呈现这一不可调和性，即是对 BSD 史作为 “各方主体性的呈现与和解之书” 的诚实书写；合图之下，Core Tea
- OpenBSD 2.0/2.1/2.2 时期（1996-1997）的漏洞响应模型呈现 “全代码审计主动识别 + errata 补丁被动发布” 的双层结构——全代码审计（1996 年夏天起）系统性识别 4.4BSD-Lite 遗留漏洞面（BIND/cron/IP 源路由/NFS/Kerberos V/procfs/rfork/vacation/lpd/tgetent/xterm），errata 机制

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3850] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3851] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3852] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3853] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3854] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3855] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3856] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章
- [DB:references_fulltext:chapter_matches:chmatch_3857] 卷“第04卷-大分裂与四大bsd的诞生”第 72 章，匹配置信度 folder，原因：folder 第70章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 5、6、8、19 条原文经原材料/哲学/项目统摄史观/第 25 章.md 一手核验；Adam Glass 通知邮件原文经 <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html> 一手核验；bsd_commits.duckdb commit 时间线经数据库查询一手核验；OpenBSD 官方
- 全代码审计与 errata 补丁的双层结构须严格区分——审计是主动识别（针对源码树），errata 是被动回溯（针对已发布版本），二者在时间维度与工程目标上不同；securelevel 在 OpenBSD 2.0 时期的实际默认启用状态须对照源码与 release notes 核实，概念雏形与默认启用为不同维度；r-commands 退役的精确版本与默认配置变更须对照 OpenBSD 2.0/2.

## 文献

- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 5、6、8、19 条原文）；Adam Glass 1994-12-23 通知邮件原文 [EB/OL]. <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html>；netbsd.duckdb netbsd-src 仓库 commits 表 deraadt 末次 commit（1994-12-17T23:12:41Z，commit `699d2a37b0e3c0c6ff29ea0d407c3feeba5642b4`）；openbsd.duckdb openbsd-src 仓库 commits 表最早 commit（1995-10-18T08:37:01Z，commit `df930be708d50e9715f173caa26ffe1b7599b157`）；OpenBSD 官方主页 index.html [EB/OL]. <https://www.openbsd.org/> ［A］## 第 28.16 不同时期人员的采访录（详见 [采访录.md](采访录.md)）> 第 28 章采访录子节，覆盖 1994-1996 年 OpenBSD 起源事件的当事人陈述，含 Theo de Raadt Slashdot 采访、Adam Glass NetBSD Core Team 通知邮件、Charles M. Hannum（查尔斯·汉纳姆） 治理陈述三则，每则采访按 5 字段深化，考据过程另见 原材料/研究/考据记录/ 下对应文件。## 第 28.17 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）
- OpenBSD security.html；OpenBSD 2.0/2.1/2.2 errata 页面；4.4BSD SMM: 16《On the Security of UNIX》；OpenBSD **securelevel(7)** 手册页；OpenBSD 早期 r-commands 退役 commit 序列；本项目。原材料/研究/bsd 漏洞史/版本周期/openbsd-2.x.md；本项目。bsd_commits.duckdb 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］