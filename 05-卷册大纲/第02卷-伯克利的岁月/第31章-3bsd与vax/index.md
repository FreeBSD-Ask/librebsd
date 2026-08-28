---
chapter: 第 31 章
id: CH31
volume: 第02卷-伯克利的岁月
---

# 第 31 章 3bsd与vax

## 要点

- 3BSD 的历史意义在于证明 BSD 可在 VAX 上运行，为 DARPA 招标提供了技术基础，是 BSD 从 PDP-11 时代迈向 VAX 时代的关键转折
- UNIX/32V（1978 年由 Bell Labs 的 John Reiser 和 Tom London 完成移植）作为 Bell Labs V7 UNIX 的 VAX 移植版，其内核结构与 V7 UNIX 基本一致——简单换页、无虚拟内存抽象、无网络支持；3BSD（1979.12）以 32V 内核为基础进行深度改造——加入由 Özalp Babaoğlu 实现的请求调页式虚拟内存、加入 2BS
- CDC NOS/VE 1984-1985 年间发布，运行于 Cyber 180 系列主机（CDC NOS/VE Product Documentation 记载 "1984 – Cyber 810, Cyber 830, Cyber 840, Cyber 850"），1985 年 NOS/VE 仍未达到生产就绪（60bits.net "NOS/VE Operating System" 原文 "In
- 3BSD 的虚拟内存实现为后续 4.xBSD 的 VAX 支持奠定基础，其设计影响了 FreeBSD 的虚拟内存子系统与现代化操作系统内存管理
- 1980 年代后期 VAX 逐渐被 RISC 工作站（Sun SPARC、MIPS）与 x86 PC 替代，BSD 在 VAX 上的开发逐步减少，1990 年代初 BSD 主力转向 386 与 SPARC

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3719] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3732] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3733] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3823] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3867] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3879] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3888] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3913] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_3931] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 folder，原因：folder 第31章
- [DB:references_fulltext:chapter_matches:chmatch_66] 卷“第02卷-伯克利的岁月”第 31 章，匹配置信度 0.6，原因：关键词重合 2 项
- [DB:bsdnow_podcast:outline_mappings:om_10651] BSD Now 第 636 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10677] BSD Now 第 631 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10738] BSD Now 第 623 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10839] BSD Now 第 607 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11258] BSD Now 第 558 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11378] BSD Now 第 543 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11549] BSD Now 第 525 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12153] BSD Now 第 452 期，匹配 CH31 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12808] BSD Now 第 325 期，匹配 CH31 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 3BSD 在 DARPA 招标中的具体权重在不同史料中评估不一，需核对 DARPA 评标记录
- 3BSD 是 “BSD 谱系首次以完整独立系统形式发布” 须严格区分——1BSD（1977 年初）、2BSD（1978 年中）虽为伯克利发布但本质为 Bell Labs UNIX 的附加组件（含 Pascal 系统、ex/vi 编辑器、termcap、csh 等用户工具），依赖 AT&T V6/V7 内核运行，不具独立内核；3BSD 内核改造程度在不同史料中描述详略不一，需核对 3BSD 与 32
- NOS/VE 的发布年份已确认为 1984（与 Cyber 180 同步），1985 年仍未生产就绪，1985.8 才在 TNO 的 Cyber 170-835 上首次实际安装（museumwaalsdorp.nl 原文 "In augustus 1985 werd NOS/VE op de CYBER 170-835 van TNO geïnstalleerd"）；先前叙述 “1979 年” 系
- 3BSD 虚拟内存对 FreeBSD 的具体影响程度在不同史料中评估不一，需核对代码谱系
- VAX 时代的终结时间节点（1989 还是 1992）在不同史料中不一致，需核对 DEC 退市记录

## 文献

- McKusick, K. (1999) "Twenty Years of Berkeley Unix"；Salus, P. (1994) "A Quarter Century of UNIX" ［B］
- UNIX/32V 源代码（1978）；3BSD 内核源代码；3BSD Release Notes (1979.12)；Joy, W. (1979) "3BSD Kernel Changes"；McKusick, K. (1999) "Twenty Years of Berkeley Unix" ［A］
- CDC (1984) "NOS/VE Reference Manual"；CDC Cyber 180 硬件文档；museumwaalsdorp.nl "NOS/VE operating system"（Cyber 170-835 TNO 1985.8 首次安装）；60bits.net "NOS/VE Operating System"（1985 NOS/VE not ready for prime time）[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- McKusick, K. et al. (1996) "The Design and Implementation of the 4.4BSD Operating System" ［B］
- DEC (1992) "VAX Product Strategy"；McKusick, K. (1999) "Twenty Years of Berkeley Unix" ［B］
- DEC VAX Handbook; Babaoglu & Joy 1981 ［A］
- CSRG 邮件列表存档；USENIX 1979-1980 年会议论文集 ［A］
- USENIX 会议论文集（1979-1980）；伯克利 CSRG 邮件列表存档 ［A］
- DEC VMS 手册； CSRG 技术报告 ［A］

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第31章-3bsd与vax 第 31 章 3bsd与vax（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：9 期，扫描 segments：9048 条 -->

### 要点（播客口述史提取）
- Berkeley Unix had been ported to the VAX by the start of the 1980s and was thriving as（BSD Now EP225 @ 2920.64）
- Just the talk about risk or reduced instruction set computers and how that was evolved out of the PDP, Unix, the Vax, BSD, Next,（BSD Now EP225 @ 2985.3）

### 史料（播客当事人陈述）
- but after a discussion on the Vax mailing list,（BSD Now EP41 @ 2923.039）
- I don't know about that Vax we talked about earlier（BSD Now EP54 @ 1954.560）
- So RFC893 enables zero copy networking on a Vax,（BSD Now EP119 @ 255.7799）
- Just the talk about risk or reduced instruction set computers and how that was evolved out of the PDP, Unix, the Vax, BSD, Next,（BSD Now EP225 @ 2985.3）

### 史观（播客当事人观点与总纲映射）
- I think there's somebody out there running a Vax or maybe an Alpha and somebody is actually（BSD Now EP119 @ 2618.139）

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP41] Pennington J. BSD Now: 41: Commit This Bit[EB/OL]. (2014-06-11)[2026-08-15]. https://www.bsdnow.tv/41.
- [BSD Now EP46] Pennington J. BSD Now: 46: Network Iodometry[EB/OL]. (2014-07-16)[2026-08-15]. https://www.bsdnow.tv/46.
- [BSD Now EP54] Pennington J. BSD Now: 54: Luminary Environment[EB/OL]. (2014-09-10)[2026-08-15]. https://www.bsdnow.tv/54.
- [BSD Now EP70] Pennington J. BSD Now: 70: Daemons in the North[EB/OL]. (2014-12-31)[2026-08-15]. https://www.bsdnow.tv/70.
- [BSD Now EP119] Pennington J. BSD Now: 119: There be Dragons, BSD Dragons anyway[EB/OL]. (2015-12-09)[2026-08-15]. https://www.bsdnow.tv/119.
- [BSD Now EP134] Pennington J. BSD Now: 134: Marking up the Ports tree[EB/OL]. (2016-03-24)[2026-08-15]. https://www.bsdnow.tv/134.
- [BSD Now EP152] Pennington J. BSD Now: 152: The Laporte has landed![EB/OL]. (2016-07-27)[2026-08-15]. https://www.bsdnow.tv/152.
- [BSD Now EP225] Pennington J. BSD Now: 225: The one true OS[EB/OL]. (2017-12-20)[2026-08-15]. https://www.bsdnow.tv/225.

<!-- /PODCAST_MINE -->
