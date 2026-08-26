---
chapter: 第 27 章
id: CH27
volume: 第02卷-伯克利的岁月
---

# 第 27 章 Bill Joy 与 1BSD

## 要点

- Bill Joy 于 1977 年作为伯克利研究生开始编译 1BSD，1978 年 3 月 9 日正式发布，约 30 份磁带拷贝
- 1BSD 是 UNIX 第六版的附加组件（Pascal 编译器和 ex 编辑器），非独立完整操作系统
- 1BSD 标志 BSD 软件发行版传统的开端，为后续 2BSD/3BSD/4BSD 系列奠定基础
- Joy 在 1BSD 时期的工作（vi、csh、Pascal 编译器）对后续 BSD 生态和 Sun Microsystems 的创立有深远影响

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_891] 卷“第01卷-unix的起源”第 21 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_1202] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 0.7，原因：无匹配
- [DB:references_fulltext:chapter_matches:chmatch_1541] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_4050] 卷“第11卷-dragonflybsd的历史”第 227 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4166] 卷“第18卷-全球社区地区bsd史”第 327 章，匹配置信度 1.0，原因：UNIX 社区第一手通讯；1975 首刊至 1978 v3n8
- [DB:references_fulltext:chapter_matches:chmatch_4185] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 1.0，原因：PSD:12 make 工具
- [DB:references_fulltext:chapter_matches:chmatch_4186] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 1.0，原因：PSD:13 RCS 版本控制
- [DB:references_fulltext:chapter_matches:chmatch_4187] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 1.0，原因：PSD:13 RCS 功能说明
- [DB:references_fulltext:chapter_matches:chmatch_4189] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 1.0，原因：PSD:19 curses 屏幕库
- [DB:references_fulltext:chapter_matches:chmatch_4212] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 1.0，原因：USD:4 C shell 入门
- [DB:references_fulltext:key_facts:kf_7314] 类别"origin"：C Shell（csh）由 Bill Joy 在伯克利开发，作为交互式命令行解释器随 BSD 发行。
- [DB:references_fulltext:key_facts:kf_8353] 类别"quote-kaoju"：Bill Joy 引述部分英文段落(如 Hubbard 对 Joy 的描述)疑为中文回译——已标注, 英文引述须谨慎
- [DB:references_fulltext:people_mentioned:p_34] 文献 ref 55 提及 Bill Joy，3 次
- [DB:references_fulltext:people_mentioned:p_109] 文献 ref 499 提及 Bill Joy，1 次
- [DB:references_fulltext:people_mentioned:p_126] 文献 ref 506 提及 Bill Joy，1 次
- [DB:references_fulltext:people_mentioned:p_249] 文献 ref 619 提及 Bill Joy，1 次
- [DB:references_fulltext:people_mentioned:p_348] 文献 ref 804 提及 William Joy（比尔·乔伊），1 次
- [DB:references_fulltext:people_mentioned:p_385] 文献 ref 890 提及 William Joy（比尔·乔伊），1 次
- [DB:references_fulltext:people_mentioned:p_387] 文献 ref 891 提及 William Joy（比尔·乔伊），1 次
- [DB:references_fulltext:people_mentioned:p_389] 文献 ref 899 提及 Bill Joy，1 次
- [DB:bsdnow_podcast:outline_mappings:om_10460] BSD Now 第 669 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10469] BSD Now 第 666 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10553] BSD Now 第 653 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10575] BSD Now 第 647 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10615] BSD Now 第 641 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10658] BSD Now 第 635 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10698] BSD Now 第 629 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10737] BSD Now 第 623 期，匹配第 26/27 章，关联度 1.0
- [DB:bsdnow_podcast:segments:seg_1475] BSD Now 第 672 期转写片段：And one of the other graduate students in my office was Bill Joy.
- [DB:bsdnow_podcast:segments:seg_1476] BSD Now 第 672 期转写片段：And Bill Joy, like myself, was working with Professor Susan Graham, getting a work reports at PhD in program languages.
- [DB:bsdnow_podcast:segments:seg_1561] BSD Now 第 672 期转写片段：Someone once asked me to compare myself to Bill Joy and I said,
- [DB:bsdnow_podcast:segments:seg_12602] BSD Now 第 613 期转写片段：bill joy wrote csh and decided he liked it um you know and you know when you write something you
- [DB:bsdnow_podcast:segments:seg_33048] BSD Now 第 535 期转写片段：But a great article it starts off by kind of detailing the humble origins of BSD you know starting with Bill Joy in the
- [DB:sacred_sources:blocks:blk_1583] sacred 文件 43（paragraph）：撰写 Bill Joy、Marshall McKusick、Mike Karels、Kirk McKusick、Rodney W. Grimes、Poul-Henning Kamp、Robert Watson、Theo de Raadt、M
- [DB:sacred_sources:blocks:blk_1604] sacred 文件 43（paragraph）：撰写 BSD 历史时，须回到原始史料（CSRG 邮件列表存档、FreeBSD commit log、Core Team 会议记录、Foundation 年报、原始公告），不得依赖二手转述。一手史料包括但不限于：Berkeley CSRG 技
- [DB:sacred_sources:blocks:blk_1606] sacred 文件 43（paragraph）：须特别注意：当事人自述也存在自利偏差、记忆偏差、事后修订等风险。Bill Joy 关于 vi 编辑器诞生的回忆、McKusick 关于 CSRG 解散的叙述、de Raadt 关于被逐出 NetBSD core 的解释——这些当事人自述都须
- [DB:sacred_sources:blocks:blk_1609] sacred 文件 43（paragraph）：撰写 BSD 关键人物的“主体性”时，须意识到主体性本身是一种预设，而非可证明的事实。我们无法证明 Bill Joy 在 1976 年的某个具体时刻“是”Bill Joy，也无法证明 Theo de Raadt 在 1996 年被逐出 Ne
- [DB:sacred_sources:blocks:blk_1669] sacred 文件 43（paragraph）：例如 Bill Joy 在 1970 年代伯克利就读时与 1980 年代 Sun 工作时与 2010 年代退休后的主体性是不同的；Theo de Raadt 在 1994 年 NetBSD core 时期与 1996 年 OpenBSD 创
- [DB:sacred_sources:blocks:blk_2401] sacred 文件 47（code_block）：```sh
FreeBSD 发展关键里程碑

1961 │ CTSS 分时系统
1969 │ UNIX 诞生
1973 │ UNIX 内核用 C 语言重写
1978 │ 1BSD 发布
1983 │ 4.2BSD 发布
1991 │ Net

- [DB:sacred_sources:blocks:blk_2412] sacred 文件 47（list_item）：- 1978 年 3 月 9 日：1BSD 发布
- [DB:sacred_sources:blocks:blk_2413] sacred 文件 47（paragraph）：基于 UNIX 创建的伯克利软件发行版（1BSD）是 UNIX 第六版的一种附加组件，而非独立完整的操作系统。此版本发行了大约 30 份。
- [DB:sacred_sources:blocks:blk_2415] sacred 文件 47（paragraph）：第二款伯克利软件发行版（2BSD）初版发布于 1978 年，经过增补后完整发布于 1979 年 5 月。涉及 1BSD 的软件更新，以及由 Bill Joy 新开发的两个至今仍在 UNIX 系统上使用的程序：vi 文本编辑器（ex 的可视化
- [DB:sacred_sources:blocks:blk_2419] sacred 文件 47（paragraph）：在 Bill Joy 离开伯克利并与他人创建 Sun Microsystems（太阳计算机系统公司）（1982 年）之后，4.2BSD 于 1983 年 8 月正式发布，这是 Bill Joy 离开后的第一个版本。1984 年，USENIX
- [DB:sacred_sources:blocks:blk_2889] sacred 文件 49（list_item）：- 容器技术的原型可追溯至 FreeBSD Jail 机制；
- 发行版（distribution）概念框架；
- sudo 工具最初面向 4.1BSD；
- Gentoo 采用的 Ports 包管理方法论，技术渊源可追溯至 BSD Por
- [DB:sacred_sources:blocks:blk_4186] sacred 文件 69（paragraph）：如果没有 Linux，这个世界会怎样？
 二十多年前，Linux 之父 Linus Torvalds 说："如果在我创造 Linux 之前 386BSD 已经可用，那么 Linux 可能不会出生。
" 后来，当人们回想反思时，也不乏有人 认
- [DB:ziliao:materials:mat_559] 类型“未分类”：1BSD cat 源代码
- [DB:ziliao:materials:mat_560] 类型“未分类”：Joy 1978 1BSD Release Notes
- [DB:ziliao:materials:mat_561] 类型“未分类”：TUHS 1BSD 档案 READ_ME（1977-11-23）
- [DB:ziliao:materials:mat_716] 类型“未分类”：1BSD/2BSD 发布说明
- [DB:ziliao:materials:mat_727] 类型“未分类”：1BSD 发布记录 ［B］
- [DB:ziliao:materials:mat_953] 类型“未分类”：1BSD Release Notes（1978-03-09）
- [DB:ziliao:materials:mat_1089] 类型“未分类”：4.1BSD/4.2BSD/4.3BSD/4.4BSD 内核源码（CSRG Archives
- [DB:ziliao:materials:mat_2662] 类型“未分类”：1BSD READ_ME 原始文件（1977-11-23，TUHS 归档）
- [DB:ziliao:materials:mat_2663] 类型“未分类”：1BSD 磁带标签原始照片
- [DB:ziliao:materials:mat_2673] 类型“未分类”：1BSD 原始磁带内容目录
- [DB:ziliao:materials:mat_2676] 类型“未分类”：1BSD READ_ME（1977-11-23）
- [DB:ziliao:materials:mat_2677] 类型“未分类”：1BSD 磁带源代码
- [DB:ziliao:materials:mat_2684] 类型“二手”：Computer History Museum Bill Joy Fellow 传记（2011） ［A］
- [DB:ziliao:materials:mat_2688] 类型“未分类”：1BSD READ_ME 原始文件（1977-11-23，TUHS 归档 minnie.tuhs.org）
- [DB:ziliao:materials:mat_2689] 类型“未分类”：1BSD/2BSD 的构建脚本原始文件
- [DB:ziliao:materials:mat_2720] 类型“未分类”：后世对 1BSD 的批评文献
- [DB:ziliao:materials:mat_2722] 类型“未分类”：1BSD 源代码的贡献者注释 ［A］
- [DB:ziliao:materials:mat_2727] 类型“未分类”：1BSD/2BSD/3BSD 贡献者清单
- [DB:ziliao:materials:mat_2737] 类型“未分类”：1BSD READ_ME 原始文件（1977-11-23，TUHS 归档，记载 ex-1.1）；Joy 与 Haley 在伯克利的开发笔记；Coulouris 在 Queen Mary College 的 em 源码（1975）；Bill
- [DB:ziliao:materials:mat_2738] 类型“一手”：Thompson 在伯克利 1975-1976 访问学者档案；Joy 的 Berkeley Pascal User's Manual（1977）；1BSD 磁带源码（Pascal 子目录）；CSRG 早期邮件存档；McKusick 1999
- [DB:ziliao:materials:mat_2741] 类型“未分类”：1BSD READ_ME 原始文件（1977-11-23，TUHS 归档）；1BSD 磁带目录结构（TUHS 归档）；McKusick, K. (1999) "Twenty Years of Berkeley Unix"；Salus, P.
- [DB:ziliao:materials:mat_2764] 类型“未分类”：1BSD 磁带清单（1978.3.9）
- [DB:ziliao:materials:mat_2966] 类型“未分类”：Joy 1BSD Release Notes ［A］
- [DB:ziliao:materials:mat_2968] 类型“未分类”：4.1BSD Release Notes (1981.6)
- [DB:ziliao:materials:mat_3084] 类型“未分类”：4.1BSD 发布说明
- [DB:ziliao:materials:mat_3087] 类型“未分类”：Joy "Changes in the Kernel in 4.1bsd" (1981.5.10) [存疑脚注]
- [DB:ziliao:materials:mat_3100] 类型“未分类”：4.1BSD 发布时间线
- [DB:ziliao:materials:mat_3120] 类型“未分类”：Kashtan, D. (1981?) "VMS vs UNIX Performance Benchmarks" SRI 报告；Joy, W. (1981) "Rebuttal to Kashtan Benchmarks"；4.1BSD R
- [DB:ziliao:materials:mat_3121] 类型“未分类”：4.1BSD 内核配置源代码；Elz, R. (1981) "Autoconfiguration for BSD"；4.1BSD Release Notes (1981.6)；McKusick, K. (1999) "Twenty Year
- [DB:ziliao:materials:mat_3126] 类型“未分类”：curses 源代码；Arnold, K. (1980s) "curses: Screen Optimization for UNIX"；4BSD/4.1BSD 发行磁带；rogue 游戏源代码 ［A］
- [DB:ziliao:materials:mat_3131] 类型“未分类”：4.1BSD Release Notes (1981.6)；4.2BSD Release Notes (1983.8)；McKusick, K. (1999) "Twenty Years of Berkeley Unix" ［B］
- [DB:ziliao:materials:mat_3136] 类型“一手”：4.1BSD Release Notes (1981.6)；4BSD Release Notes (1980.10)；4.4BSD SMM:1《Installing and Operating 4.4BSD》；McKusick et al.
- [DB:ziliao:materials:mat_3163] 类型“未分类”：CHM 2011 Bill Joy 口述史（X6073.2011）
- [DB:ziliao:materials:mat_3272] 类型“未分类”：4.1BSD 与 SunOS 1.0 源代码对比
- [DB:ziliao:materials:mat_3343] 类型“未分类”：MSST 2025 "NFS: Genesis" 主题演讲 PDF（Tom Lyon 2025 演讲稿，msstconference.org 一手档案，列示 NFS 团队 8 人名单："Bill Joy, Dave Goldberg, Bo
- [DB:ziliao:materials:mat_3381] 类型“未分类”：4.1BSD/4.2BSD 发布说明（学术开源分发）；SunOS 1.0/2.0/3.0/4.0 Release Notes（商业化专有产品）；BSD 许可证原文（1980
- [DB:ziliao:materials:mat_3824] 类型“未分类”：4.0BSD/4.1BSD delivermail 源代码
- [DB:ziliao:materials:mat_3898] 类型“一手”：4.0BSD/4.1BSD delivermail 源代码；4.1cBSD/4.2BSD Sendmail 源代码（1983.8）；RFC 780（MTP 邮件传输协议，1981 年 5 月）；RFC 821（SMTP 协议，1982 年
- [DB:ziliao:materials:mat_4337] 类型“未分类”：Bill Joy 1978-1982 年 BSD 开发记录（McKusick, K. (1999) "Twenty Years of Berkeley Unix"）；CSRG 1980 年 DARPA 合同档案；Joy 1982 年离开伯克
- [DB:ziliao:materials:mat_5639] 类型“未分类”：4.2BSD 源码中 chroot 实现（Bill Joy 提交记录）
- [DB:ziliao:materials:mat_5640] 类型“工具书”：jail(8) 手册页脚注（明确记载 1982 年 3 月 18 日 Bill Joy 加入 chroot）
- [DB:ziliao:references:ref_649] 1BSD Release Notes (1978)
- [DB:ziliao:references:ref_650] TUHS 1BSD 档案 READ_ME（1977-11-23）
- [DB:ziliao:references:ref_653] discoverbsd.blogspot.com 1BSD 历史记叙 ［C］
- [DB:ziliao:references:ref_1130] 1BSD 1978 公告
- [DB:ziliao:references:ref_3014] Joy, W. (1977) "1BSD READ_ME"（TUHS 归档） ［B］
- [DB:ziliao:references:ref_3017] Joy, W. (1977) "1BSD READ_ME"（TUHS 归档，1977-11-23）
- [DB:ziliao:references:ref_3018] Joy, W. (1978) "1BSD Release Notes"
- [DB:ziliao:references:ref_3022] Joy, W. (1977) "1BSD READ_ME"（TUHS 归档）
- [DB:ziliao:references:ref_3026] Computer History Museum (2011) "Bill Joy Fellow Biography" ［B］
- [DB:ziliao:references:ref_3053] 1BSD 原始源代码注释 ［A］
- [DB:ziliao:references:ref_3066] Joy, W. (1978) "ex Reference Manual" 1BSD
- [DB:ziliao:references:ref_3081] Joy, W. (1977) "1BSD READ_ME"（TUHS 归档，1977-11-23） ［B］
- [DB:ziliao:references:ref_3099] 1BSD 磁带清单（1978.3.9） ［B］
- [DB:ziliao:references:ref_3271] 4.1BSD Release Notes (1981.6)
- [DB:ziliao:references:ref_3334] Bostic, K. "2.11BSD Maintenance Records" ［B］
- [DB:ziliao:references:ref_3363] 4.1BSD Release Notes (1981)
- [DB:ziliao:references:ref_3364] Joy, W. (1981) "Changes in the Kernel in 4.1bsd"
- [DB:ziliao:references:ref_3391] 4.1BSD Release Notes (1981.6) ［B］
- [DB:ziliao:references:ref_3392] McKusick, K. (1999) "Twenty Years of Berkeley Unix"（当事人一手记载 Robert Elz autoconfig 随 4.1BSD 引入）
- [DB:ziliao:references:ref_3402] 4.1BSD Release Notes (1981.6) [存疑脚注]
- [DB:ziliao:references:ref_3407] McKusick, K. (1999) "Twenty Years of Berkeley Unix"（当事人一手明确区分 4.1BSD 正式版特性与 4.1a/b/c 开发线功能）
- [DB:ziliao:references:ref_3454] CHM (2011) "Oral History of Bill Joy"（X6073.2011，archive.computerhistory.org 全文 PDF）
- [DB:ziliao:references:ref_3662] 4.1BSD/4.2BSD Release Notes
- [DB:ziliao:references:ref_4231] 4.0BSD/4.1BSD delivermail 源代码
- [DB:ziliao:references:ref_4241] 4.1BSD BBN TCP/IP
- [DB:ziliao:references:ref_13962] McKusick M K. The Berkeley Software Distribution: From 1BSD to 4.4BSD-Lite2[C]//Proceedings of the 1995 USENIX Technical
- [DB:ziliao:references:ref_13966] Joy W N. 1BSD READ_ME[EB/OL]. (1977-11-23)[2026-07-19]. The Unix Heritage Society (TUHS) Archive. <https://www.tuhs.org/A>
- [DB:ziliao:references:ref_14632] Computer History Museum. Bill Joy Fellow Biography[EB/OL]. (2011)[2026-07-19]. <https://computerhistory.org/fellow/bill-j>
- [DB:ziliao:references:ref_14759] CSRG. 4.1BSD Release Notes[R]. 伯克利: 加州大学伯克利分校计算机系统研究小组, 1981-06.
- [DB:ziliao:references:ref_14760] Joy W N. Changes in the Kernel in 4.1bsd[R]. 伯克利: 加州大学伯克利分校, 1981-05-10 (1981-09-01修订).
- [DB:ziliao:references:ref_14831] TUHS Official Archive. 1BSD READ_ME[EB/OL]. (1977-11-23)[2026-07-19]. <https://www.tuhs.org/Archive/Distributions/UCB/1bs>
- [DB:ziliao:references:ref_14866] CSRG. CSRG 源代码归档（4.1BSD-4.4BSD-Lite）[Z]. 伯克利: 加州大学伯克利分校档案馆, 1980-1995.
- [DB:ziliao:references:ref_14913] Computer History Museum. CHM Oral History Collection: Bill Joy 口述史访谈[Z]. 山景城: 计算机历史博物馆.
- [DB:ziliao:references:ref_14992] Joy W N. An Introduction to the C Shell[J]. Berkeley: CSRG, University of California, Berkeley, 1979. 亦收录于 4.0BSD/4.1BSD
- [DB:ziliao:references:ref_16984] University of California, Berkeley. Computer Science Division. Hints on Configuring VAX Systems for UNIX [Z]. Berkeley:
- [DB:ziliao:references:ref_17007] University of California, Berkeley, Computer Systems Research Group. Bug Fixes and Changes in 4.1bsd[M]. Berkeley: CSRG.
- [DB:ziliao:references:ref_17012] University of California, Berkeley. Changes to the Kernel in 4.1bsd[M]. [存疑]

- [DB:references_fulltext:chapter_matches:chmatch_3721] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3722] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3734] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3766] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3768] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3770] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3822] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3824] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3881] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:references_fulltext:chapter_matches:chmatch_3884] 卷“第02卷-伯克利的岁月”第 27 章，匹配置信度 folder，原因：folder 第27章
- [DB:bsdnow_podcast:outline_mappings:om_11451] BSD Now 第 535 期，匹配 CH27 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12807] BSD Now 第 325 期，匹配 CH27 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10460] BSD Now 第 669 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10469] BSD Now 第 666 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10553] BSD Now 第 653 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10575] BSD Now 第 647 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10615] BSD Now 第 641 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10658] BSD Now 第 635 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10698] BSD Now 第 629 期，匹配 CH27 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10737] BSD Now 第 623 期，匹配 CH27 章，关联度 1.0

## 史观

- 多方视角并置：Joy 自述、Fabry 视角、Leffler 视角、McKusick 视角——同一事件呈现为四个不同的“历史小说”
- 分离聚合循环：1BSD 是 CSRG 团队化起点（聚合），Joy 离开去 Sun 是分离，Leffler 接手是再聚合
- 草台班子论：真正推动 BSD 的是动手者而非明星，Fabry/Haley/Standiford 等被 Joy 光环遮蔽的贡献者值得关注
- 自利偏差审查：当事人自述存在记忆偏差、事后修订等风险，需交叉验证
- 主体性预设反思：无法证明 Bill Joy 在 1976 年的某个具体时刻“是”Bill Joy——主体性是形式主义化的重构

## 辨析

- Joy 在 1BSD 中的实际贡献边界：编译整合 vs. 原创开发，需区分 Pascal 编译器的移植工作与全新代码编写
- 1BSD 的“约 30 份磁带拷贝”说法：多源记载一致，但具体分发名单缺乏完整一手记录
- 单人英雄叙事 vs. 团队协作：Joy 的知名度导致 1BSD 被过度归因于个人，实际存在 Fabry 的引入决策、Haley 的协作等
- 1BSD 与 2BSD 的边界：1BSD 发布于 1978 年 3 月，2BSD 初版同年发布，两者时间线交叉需明确
- 当事人自述的可信度：McKusick 作为史家-参与者双重视角，能否客观书写 BSD 史——元哲学的自指困境

## 文献

- Joy, W. (1977) "1BSD READ_ME"（TUHS 归档，1977-11-23）
- Joy, W. (1978) "1BSD Release Notes"
- Joy, W. (1978) "ex Reference Manual"1BSD
- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"，出自 O'Reilly《Open Sources》
- Joy, W. & McKusick, M. K. (1979) "Berkeley Pascal PX Implementation Notes"，第二版
- Computer History Museum (2011) "Bill Joy Fellow Biography"
- BSDTalk #170 (2009) Marshall Kirk McKusick at DCBSDCon 访谈
