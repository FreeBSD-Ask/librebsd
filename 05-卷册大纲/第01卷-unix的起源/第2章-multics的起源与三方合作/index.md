---
chapter: 第 2 章
id: CH2
volume: 第01卷-unix的起源
---

# 第 2 章 multics的起源与三方合作

## 要点

- 分析哲学与数学哲学为本书提供三重思想前提：其一，弗雷格—罗素的谓词逻辑与类型论直接构成下一节（1.2 数理逻辑核心概念）的内容主体；其二，希尔伯特判定问题在 1936 年引出图灵机模型（1.3），把“可机械执行的推理”从哲学理想变为数学对象；其三，从逻辑主义追求必然基础到哥德尔揭示形式系统内在限度，再到蒯因消解分析/综合的绝对二分，这条思想曲线与 UNIX 的工程经验主义、Multics 的理性主
- 为运行 Space Travel，Thompson 在 PDP-7 上构建了文件系统、进程调度、shell 雏形；这些基础设施演化为 UNIX 第一版（1969 年夏末）
- Multics 源代码、文档、运行日志由 MIT、Honeywell、Van Vleck 等保存；Multics.org 网站为最完整的在线档案；多项 Multics 概念（段式内存、动态链接、访问控制列表）影响后续操作系统
- Multics 是早期支持对称多处理（SMP）的操作系统之一——在 Honeywell 6180 上的多处理器配置中，允许多个 CPU 共享同一内存映像，由内核的锁机制协调。同时，Multics 实现了“在线重配置”——可在不停止系统运行的情况下添加/移除 CPU、内存模块与 I/O 控制器——这是现代云计算“热迁移”与“热插拔”的远古先例。
- 部分 Multics 工程师后来承认 UNIX 的简洁具有实用价值，但批评其安全模型粗糙、文件系统原始；Peter Neumann 持续批评 UNIX 安全缺陷至 21 世纪

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3604] 卷“第01卷-unix的起源”第 2 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1465] 卷“第01卷-unix的起源”第 2 章，匹配置信度 0.8，原因：关键词重合 2 项（file, finding, ports, clones, freebsd）
- [DB:references_fulltext:chapter_matches:chmatch_22] 卷“第01卷-unix的起源”第 2 章，匹配置信度 0.6，原因：路径启发：Thompson Trusting Trust 1984
- [DB:bsdnow_podcast:outline_mappings:om_11676] BSD Now 第 506 期，匹配 CH2 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12052] BSD Now 第 463 期，匹配 CH2 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12196] BSD Now 第 446 期，匹配 CH2 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12516] BSD Now 第 418 期，匹配 CH2 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12706] BSD Now 第 362 期，匹配 CH2 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12766] BSD Now 第 344 期，匹配 CH2 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12873] BSD Now 第 261 期，匹配 CH2 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 将 UNIX 哲学与实用主义/经验主义传统相联系的做法存在回溯性建构风险——Ritchie、Thompson 等人并无系统阅读分析哲学的文献证据，联系应止于“思想气候”层面
- UNIX 诞生日期 1969 年夏末是否准确——Thompson 与 Ritchie 的回忆略有出入；“第一版”的边界模糊
- Multics 对后续系统的影响程度存在争议——Plan 9、Java、Windows NT 的设计者均称受 Multics 启发，但影响路径难以精确追踪
- Multics SMP 使用“粗粒度锁”策略，在 2–4 个 CPU 配置下性能良好，但无法线性扩展至更多处理器。后续 Solaris、FreeBSD 与 Linux 的 SMP 演进（细粒度锁、RCU、NUMA 感知）暴露了 Multics 方法的局限，但这些局限在 1970 年代完全不可见。
- Neumann 的批评是否公平——需对比 Multics 与 UNIX 的实际安全记录；批评中是否夹杂项目失败的情绪

## 文献

- 同本节 1.1.1-1.1.4 所列；另参见 Turner F. From Counterculture to Cyberculture [M]. 2006（关于思想气候迁移的二手研究）
- Unix Heritage Society (TUHS) PDP-7 UNIX 重建项目；Ritchie 1984 BLTJ 63 No. 6 Part 2:1577-1593, DOI 10.1002/j.1538-7305.1984.tb00054.x；Kernighan 2019 回忆录 ［B］
- Multics.org；Organick"The Multics System" (1972)；Elliott Organick"Computer System Organization" (1973) [考据脚注：Organick 1972 为 Multics 研究经典一手文献，Multics 档案保存与概念遗产经 multicians.org 交叉验证确证。]
- Honeywell Info Systems, "Multics System Programmer's Manual," 1977; Thomas W. Doeppner, "Operating Systems In Depth," Wiley, 2011（第 6 章多处理器调度对 Multics 的回顾） ［B］
- Peter Neumann RISKS Forum (ACM)；Multics.org 社区评论；Neumann"Computer Security in Open Systems" (1995) ［B］
- Ritchie 1984 BLTJ 63 No. 6 Part 2:1577-1593, DOI 10.1002/j.1538-7305.1984.tb00054.x；Thompson 1979 BYTE；Kernighan 2019 回忆录 ［B］
- Ritchie & Thompson 1974 CACM"The UNIX Time-Sharing System"；Ritchie 1979/1984"The Evolution of the Unix Time-sharing System"（1979 年 AUUG 研讨会首次发表，1984 年 BLTJ 正式刊出）；US Patent 4,135,240"Protection of data file contents"；Morris 蠕虫 1988 事件报告；freebsd.db：freebsd-src commit `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25，4.4BSD-Lite import）；freebsd.db：freebsd-src commit `c2f46557264110fb353a0f512292db9330c09dc4`（1996-03-11，4.4BSD-Lite2 import） ［A］
- Shannon C E. A Symbolic Analysis of Relay and Switching Circuits [J]. Transactions of the AIEE, 1938, 57(12): 713-723；同本节 1.2.1-1.2.4 所列 [考据脚注：香农 1938 年硕士论文内容为逻辑史与信息论史学界公认，经信息论史文献与本章 1.15.13 节既有考据交叉验证确证。]
- 同本节 1.3.1-1.3.4 所列；另参见 Ceruzzi P. A History of Modern Computing [M]. 2003（模型—机器关系的二手研究）
- 同本节 1.4.1-1.4.4 所列；另参见 Ceruzzi 2003 第 1-3 章；Campbell-Kelly & Aspray"Computer"(1996) 相关章节

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第2章-multics的起源与三方合作 第 2 章 multics的起源与三方合作（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：7 期，扫描 segments：5545 条 -->

### 要点（播客口述史提取）
- So by the end of the 1970s, Unix, which had started a decade earlier as a reaction against the loss of the comfortable programming environment of Multics, was growing like a weed through academic and IT industry.（BSD Now EP259 @ 1218.420）

### 史料（播客当事人陈述）
- （待人工提取）

### 史观（播客当事人观点与总纲映射）
- Oh, yes. But I think you shouldn't mention it to the authors because they're kind of aware of that and people are now, you know, getting expectant. Yeah. We'll leave you with that. And oh, the next thing is also a bit more for the historic historians, although people interested in the history of Unix, because we have the Multics history page over at multicians.org.（BSD Now EP333 @ 1805.159）
  → 史观映射：总纲23——一切历史写作都是基于哲学设定的历史小说

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP171] Pennington J. BSD Now: 171: The APU - BSD Style![EB/OL]. (2016-12-07)[2026-08-15]. https://www.bsdnow.tv/171.
- [BSD Now EP214] Pennington J. BSD Now: 214: The history of man, kind[EB/OL]. (2017-10-04)[2026-08-15]. https://www.bsdnow.tv/214.
- [BSD Now EP231] Pennington J. BSD Now: 231: Unix Architecture Evolution[EB/OL]. (2018-02-01)[2026-08-15]. https://www.bsdnow.tv/231.
- [BSD Now EP259] Pennington J. BSD Now: Episode 259: Long Live Unix | BSD Now 259[EB/OL]. (2018-08-16)[2026-08-15]. https://www.bsdnow.tv/259.
- [BSD Now EP315] Pennington J. BSD Now: 315: Recapping vBSDcon 2019[EB/OL]. (2019-09-12)[2026-08-15]. https://www.bsdnow.tv/315.
- [BSD Now EP333] Pennington J. BSD Now: 333: Unix Keyboard Joy[EB/OL]. (2020-01-16)[2026-08-15]. https://www.bsdnow.tv/333.
- [BSD Now EP416] Pennington J. BSD Now: 416: netcat printing[EB/OL]. (2021-08-19)[2026-08-15]. https://www.bsdnow.tv/416.

<!-- /PODCAST_MINE -->
