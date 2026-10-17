---
chapter: 第 72 章
id: CH72
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 72 章 OpenBSD 起源的史观审视

## 要点

- 本事件的史观审视承认争议的不可调和性——这并非失败的叙事，而是项目统摄史观对历史诚实性的要求；和解优于斗争，但和解不等于消解分歧；本体论上各方平等，但平等不等于抹平差异；OpenBSD 的诞生既是分离的撕裂，也是新主体性的呈现——这一刻的 BSD 家族，因不可调和的争议而更加完整；史家呈现这一不可调和性，即是对 BSD 史作为“各方主体性的呈现与和解之书”的诚实书写；合图之下，Core Team 的程序性沉默与 de Raadt 的行动性再回应共同构成辩证链的合图——双方均未选择公开论战，但分歧并未因此消解，而是以“分离”的形式凝固为 BSD 阵营的永久结构性事实。
- OpenBSD 2.0/2.1/2.2 时期（1996-1997）的漏洞响应模型呈现“全代码审计主动识别 + errata 补丁被动发布”的双层结构——全代码审计（1996 年夏天起）系统性识别 4.4BSD-Lite 遗留漏洞面（BIND/cron/IP 源路由/NFS/Kerberos V/procfs/rfork/vacation/lpd/tgetent/xterm），errata 机制以补丁形式向已发布版本回溯修复；该模型与同期 FreeBSD 2.1/2.2（以 Security Advisory 被动响应为主，无系统全代码审计）与 NetBSD 1.1/1.2（以 pullup 模型回溯修复为主，无系统全代码审计）形成鲜明对照。

## 史料

- 本章章级史料著录暂缺：原自动匹配的 8 条数据库锚点经查 references_fulltext.duckdb 均为 UNKNOWN REFERENCE（id=1862-1869，主库无可用题名/作者信息），不具可考据性。 [存疑脚注] 章级史料清单待依 72.14-72.15 节史料字段与考据留痕按 GB/T 7714 复核回填

## 史观

- 总纲第 5 条——没有必然性，只有偶然性：de Raadt 被要求辞职是 1994 年 12 月 NetBSD Core Team 中具体的人的具体决定，但直接催生 OpenBSD，替代品的无限性不能否定事物的独特价值（据 72.14）。
- 总纲第 8 条——本体论上各方平等：NetBSD Core Team 的委员会模式与 OpenBSD de Raadt 的 BDFL 模式在本体论上平等，各有其代价与收益，无优劣之分（据 72.14）。
- 总纲第 19 条——解释学循环是历史认识的根本条件：前理解的差异使分歧不可避免，权力与知识在历史书写中共谋——什么被记录、什么被遗忘本身就是权力行使（据 72.14）。
- 总纲第 6 条——和解优于斗争：本事件的合图并非和解的实现，而是和解的失败，双方以分离取代对话，争议在分离中凝固（据 72.14）。
- 总纲第 21 条——革命与改革是历史方法论的分歧：全代码审计安全响应模型是 OpenBSD 从被动 errata 到主动审计的改革式工程路径转折（据 72.15）。
- 总纲第 4 条——分离聚合是永恒规律：OpenBSD 从 4.4BSD-Lite 基线分离后主动加固，是 BSD 安全文化从继承到重构的转折（据 72.15）。
- 总纲第 10 条——动手者创造历史：de Raadt 与早期开发者以逐行审计的工程实践识别 4.4BSD-Lite 遗留的深层漏洞（据 72.15）。

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 5、6、8、19 条原文经 sacred_sources.duckdb（file_id=26，第 25 章总纲原文）一手核验；Adam Glass 通知邮件原文经 <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html> 一手核验；bsd_commits.duckdb commit 时间线经数据库查询一手核验；OpenBSD 官方主页 index.html 经 <https://www.openbsd.org/> 一手核验。
- 全代码审计与 errata 补丁的双层结构须严格区分——审计是主动识别（针对源码树），errata 是被动回溯（针对已发布版本），二者在时间维度与工程目标上不同；securelevel 在 OpenBSD 2.0 时期的实际默认启用状态须对照源码与 release notes 核实，概念雏形与默认启用为不同维度；r-commands 退役的精确版本与默认配置变更须对照 OpenBSD 2.0/2.1/2.2 release notes 核实。

## 文献

- sacred_sources.duckdb（file_id=26，第 25 章总纲原文：第 5、6、8、19 条）；Adam Glass 1994-12-23 通知邮件原文 [EB/OL]. <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html>；netbsd.duckdb netbsd-src 仓库 commits 表 deraadt 末次 commit（1994-12-17T23:12:41Z，commit `699d2a37b0e3c0c6ff29ea0d407c3feeba5642b4`）；openbsd.duckdb openbsd-src 仓库 commits 表最早 commit（1995-10-18T08:37:01Z，commit `df930be708d50e9715f173caa26ffe1b7599b157`）；OpenBSD 官方主页 index.html [EB/OL]. <https://www.openbsd.org/> ［A］
- OpenBSD security.html；OpenBSD 2.0/2.1/2.2 errata 页面；4.4BSD SMM: 16《On the Security of UNIX》；OpenBSD **securelevel(7)** 手册页；OpenBSD 早期 r-commands 退役 commit 序列；research_notes.duckdb（原“bsd 漏洞史”研究材料，源文件已清理入库）；bsd_commits.duckdb 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］

## 不同时期人员的采访录

> 采访录子节覆盖 1994-1996 年 OpenBSD 起源事件的当事人陈述，含 Theo de Raadt Slashdot 采访、Adam Glass NetBSD Core Team 通知邮件、Charles M. Hannum（查尔斯·汉纳姆）治理陈述三则，每则采访按 5 字段深化，考据过程另见 **03-原始史料库/06-考据记录/** 下对应文件。详见 [采访录.md](采访录.md)。（媒体反响与社区舆论子节原属旧第 28 章，本章未建立对应文件，2026-09-11 整改移除其虚空链接）