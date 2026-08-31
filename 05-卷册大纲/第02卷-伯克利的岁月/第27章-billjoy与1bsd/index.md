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

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP362、BSD Now EP361、BSD Now EP278、BSDTalk EP18（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warner Losh 自述 2.11BSD 复原工程：因原始磁带由 Usenix 分发且早期母带重制，现仅存 patch level 195（约发布 18 个月后），他通过 2.10.1BSD、4.3BSD 等来源拼合出 patch level 0。（BSD Now EP362，[774.42-1103.02]，L1）
- 2.11BSD 的 patch 以 shell 脚本、uuencode 压缩 tar 等格式发布，部分指令破坏信息，无法简单用 patch -R 逆向。（BSD Now EP362，[884.78-912.34]，L1）
- Warner 自述曾因疫情失眠而以复原工程为消遣，最终重建出可启动的原始系统磁带，并计划把每个 patch 转为 git commit。（BSD Now EP362，[964.58-1472.50]，L1）
- 关于 sync：早期 Unix 没有 reboot 命令，靠 sync 后断电；连续三次 sync 是人为延时的误传，各 BSD 内核的 sync 只调度写盘而不等待完成。（BSD Now EP362，[2597.68-2885.24]，L1）
- Firecracker 由 AWS 于 2018 年开源，是依赖 KVM 的微虚拟机监控器；作者以 NetBSD 最小内核配置并绕过引导装载器构建“函数式微虚拟机”。（BSD Now EP361，[749.58-1016.66]，L2）
- Warner Losh 的 2.11BSD 复原工程公开，目标是以可复现方式重建 2.11BSD 发行磁带，并生成含全部 patch 点的 Git 仓库。（BSD Now EP361，[442.48-732.66]，L2）
- Warner Losh 的磁盘分区史文章梳理 Unix 第一至第七版从静态分区到多分区设备的演进，指出分区表曾编译进驱动而非写盘。（BSD Now EP361，[1266.82-1931.02]，L2）
- OpenBSD 发布首个 PowerPC64 快照，在 Raptor Blackbird 与 Talos II 上开发，并计划支持 Power8 系统。（BSD Now EP361，[1075.56-1141.02]，L2）
- McKusick 亲述伯克利早期四张桌四人同处一室、与 Bill Joy 为办公室同僚，办公室仅一部电话且十之八九是找 Bill Joy；他形容 Bill Joy 更像营销者，四处演讲、散发磁带、动员他人贡献。（BSD Now EP278，[176.66-198.66]，L1）
- McKusick 认为 FreeBSD 二十五年来最大的成就是形成一套能持续吸纳新人并让其上升的治理机制：文档 committer 与源码 committer 同样有权选举 core，营销背景者也能当选。（BSD Now EP278，[533.12-611.68]，L1）
- McKusick 援引 MIT 与法国南部高校的社会学研究，称多数开源项目约五年内沉寂，只有 Apache 与 FreeBSD 等项目完成三次以上成功的领导层更替，FreeBSD 已历约五代。（BSD Now EP278，[725.94-848.56]，L1）
- McKusick 亲述 FreeBSD 基金会起源：早期发行由 Walnut Creek CD-ROM 支撑，后依赖 Yahoo 提供基础设施十余年，Justin Gibbs 因担忧单一公司退出而发起基金会。（BSD Now EP278，[1883.72-1965.34]，L1）
- McKusick 亲述 UFS 三十年：其保存的 1982 年磁盘镜像在当代仍可读写，UFS 适合资源受限的嵌入式设备，ZFS 适合大资源环境，二者各解决不同问题。（BSD Now EP278，[1093.34-1174.26]，L1）
- McKusick 判断容器概念发明于 FreeBSD 却在他处获得成功，FreeBSD 常把项目推进到九成而缺最后一成产品化，恰如“先驱挨箭、定居者得地”。（BSD Now EP278，[2596.78-2625.54]，L1）
- McKusick 回忆早期 BSD 谱系：项目最初就是 Bill Joy 的一人工程，发布一些工具程序，首个发行物径称 BSD、后追认 1BSD，历经数个修订仍是工具集而非完整系统；约 1979 年的 3BSD 才是第一个带全部工具的完整系统；1979 年项目声望足以让 Bob Fabry 为系里争取到 DARPA 拨款，DARPA 想要一个所有承包商共用的操作系统基座，Joy 以 Unix 不绑定特定厂商说服对方，主要对手是只运行于 DEC 机器的 VMS——尽管当时 Unix 其实也只在 DEC 设备上运行，这一局面在 80 年代初随包括 Joy 赴创的 Sun 在内的工作站浪潮而迅速改变。（BSDTalk EP18，[77.45-211.79]，L1）
- 关于 TCP/IP 进入 BSD：ARPANET 原用 NCP 协议，仅运行于专用处理器且上限 256 台主机，扩张注定使其失效；伯克利的 DARPA 项目是让新协议 TCP/IP 落地，工作分工为 BBN 编写协议、伯克利定义并构建 API，今天尽人皆知的 socket 接口即伯克利的设计；BBN 交付的代码能打满一台 1 MIPS 处理器的 56 kbps，作为 ARPANET 速度尚称够用，但接上 3 M 以太网仍只有 56 kbps 吞吐，Joy 为使其跑满 3 M 乃至 10 M 以太网做了大量调优，期间与 BBN 产生分歧但最终解决；伯克利版的 API 与 TCP/IP 代码成为至少到 90 年代初几乎所有实现的共同基础。（BSDTalk EP18，[231.97-349.19]，L1）
- BSD 许可证诞生的完整链条：80 年代末以前获取 BSD 发行须先购 AT&T 源码许可证再另付一千美元，AT&T 许可费从两万至五万美元涨到 80 年代中期的二十五万至五十万，小公司无力承担，遂请伯克利单独发放明确属于伯克利的 TCP/IP 代码；伯克利律师想借此收取版税，团队以代码由政府资金开发、伯克利无权收费为由坚持开放；团队也评估过当时刚起步的 GNU 通用公共许可证，因其要求改动及关联代码全部开源——TCP/IP 运行于内核意味着交出整个内核——而否决；既不接受锁死权利的版权模式也不接受要求交出知识产权的 copyleft，他们自称 copy center，随取随拷、不要求回馈但予鼓励，许多厂商最终回赠大量代码，动因不是利他而是不堪每次新版发布后重新合并自有改动的负担；与大学律师反复争论后由律师定稿，即今日的 BSD 许可证，1988 年随 TCP/IP 代码及相关工具一并发布。（BSDTalk EP18，[371.17-547.37]，L1）
- 随后的代码释放与三团体分化：Keith Bostic 决心测试能解放多少代码，除内核外释放了全部有趣部分，CSRG 逐文件甄别内核归属并清除外来部分，尘埃落定时仅余约六个关键内核文件，1989 年发布后不久网络上的黑客便补齐了这六个文件，到 1990 年已出现可独立运行的 BSD；由此分出三支——坚持大学研究风格、保持系统小巧、追求多平台的 NetBSD，全力在 PC 架构上做到用户友好的 FreeBSD，两者目标分化迅速但都保持伯克利式许可证因而代码往来频繁；第三支是走向专有的 Berkeley Software Design Incorporated，整个 90 年代销售该系统，最终被 Wind River Systems 收购并将技术并入其产品。（BSDTalk EP18，[561.23-675.43]，L1）
- McKusick 当下的工作清单：近年持续增强文件系统——soft updates 以类似日志的机制让文件系统既快又稳且可恢复，snapshots 支持活动系统转储与后台文件系统检查；两年前出版 FreeBSD 操作系统设计与实现专著，其后围绕该书开发课件、授课并录像，即将开设一个读约八万行 FreeBSD 内核源码的代码阅读课；未来计划为 FFS 补上日志版本——对部分用户这只是采购清单上的勾选项——并完善 FreeBSD 中已有的 NFSv4 原型；他同时以教授身份厘清概念：UFS 是 Unix 文件系统的统称，FFS 是多数 BSD 系统采用的磁盘布局变体，此外还有日志式与内存式变体用于临时文件系统。（BSDTalk EP18，[683.77-834.79]，L1）

**史料**：

- Warner Losh 本人口述及博客、Twitter 记录，涉及 Usenix 磁带分发、TUHS 档案与 patch 链。（BSD Now EP362，[774.42-1826.06]，L1）
- Unix Heritage Society（TUHS）由 William Toomey 创立，保存代码、二进制、论文扫描件与早期商业发行的私有档案。（BSD Now EP362，[2022.96-2260.64]，L1）
- “Fakecracker：NetBSD as function-based micro-VM”教程，含最小内核配置与 Sailor 工具说明。（BSD Now EP361，[749.58-1016.66]，L2）
- Warner Losh 的 2.11BSD 复原项目页面与早期 Unix 磁盘分区史博客。（BSD Now EP361，[442.48-732.66]，L2）
- McKusick 提及 FAST 大会关于文件系统三十年演进的 keynote、BSDCan 2018 的采访背景，以及 CSRG 重写 AT&T 程序时 Keith Bostic 主张将署名归于他人以自保的细节。（BSD Now EP278，[339.18-390.46]，L1）
- McKusick 提及 TeachBSD 项目，主张以真实操作系统而非玩具系统教授计算机科学，并认为 DTrace/DWatch 等工具是“玻璃制”可观测系统的重要组成部分。（BSD Now EP278，[2723.00-2781.38]，L1）

**史观**：

- 总纲19 解释学循环是历史认识的根本条件：复原工程通过现存 patch 链与早期二进制格式博客互相印证，构成解释学循环的认识过程。（BSD Now EP362，[1076.58-1268.54]，L2）
- 总纲22 知识注定过时：早期二进制格式与工具链需借助旧模拟器与二进制工件才能重建，说明工具知识会随代际过时。（BSD Now EP362，[678.42-758.62]，L1）
- 总纲10 动手者创造历史：Firecracker 微虚拟机与 2.11BSD 复原均由个体以工程实践填补生态空白。（BSD Now EP361，[749.58-1016.66]，L2）
- 总纲22 知识注定过时：早期 Unix 的分区表硬编码与设备号约定随存储工业演进而被淘汰。（BSD Now EP361，[1885.08-1931.02]，L2）
- 总纲10 动手者创造历史：McKusick 强调软件与项目的持续“养护”远非社区驱动项目所长，人们倾向做新奇有趣之事；文档与基础设施的默默维护恰是系统得以存活的关键。（BSD Now EP278，[451.46-489.68]，L1）
- 总纲3 不存在进步，只有权力再分配：McKusick 指出历史上 IBM、微软各自占据过绝对支配地位又相继让位，Linux 今日的支配地位同样不会永远持续，FreeBSD 甘居雷达之下反而得以延续。（BSD Now EP278，[2247.34-2342.26]，L1）
- 总纲5 没有必然性，只有偶然性：McKusick 以“容器发明于 FreeBSD 却成功于他处”为例，指出技术领先与市场成功之间并无必然因果，成功更多依赖偶然的产品化时机。（BSD Now EP278，[2596.78-2625.54]，L1）
- 总纲8 本体论上各方平等：McKusick 对竞争格局的判断建立在一个历史类比与一个生态学论证上：当年 PC 被讥为小、弱、难用，却因比大型机便宜十倍而被人找到用法，终至 PC 为王、大型机退居利基——开源相对专有软件正是同样的成本结构，IBM 弃自有操作系统拥抱 Linux、Oracle 访谈当周宣布收购 Sleepycat 并酝酿再购两家开源厂商皆是征兆，Linux 将取代 Windows 的主导地位而 Windows 不会消失；他又论证 Windows 的根本弱点在于它是横跨八成机器的单一一致目标，一个病毒即可通吃，计算生态需要遗传多样性，BSD 的价值恰在于既不是 Linux 也不是 Windows——小到病毒作者不感兴趣、久经岁月而足够防弹，装机数百万、缓慢增长，永不称王却是生态中不可替代的一极。（BSDTalk EP18，[847.61-1111.83]，L1）
- 总纲13 法律与道德是利益分配：McKusick 特别纠正了开源回馈的道德化叙事：厂商向伯克利回赠大量代码并非出于利他，而是每次新版发布都须重新合并自有改动的成本压力使然，把改动交回上游后改动随发行物一起维护反而省力——所谓社区美德话语之下运行的是赤裸裸的利益核算。（BSDTalk EP18，[509.95-525.89]，L1）

**辨析**：

- 2BSD 系列早期版本号（2.8 至 2.11）与缺失版本（如 2.6/2.7）的编号逻辑，Warner 亦无法确证，仅推测与磁带编号相关。　[存疑脚注] 版本号缺口原因待原始档案确认（BSD Now EP362，[802.42-826.70]，L4）
- NetBSD 微虚拟机引导需 multiboot 内核选项，目前仅 i386 支持、AMD64 尚缺，作者假设其为近期限制。　[存疑脚注] AMD64 multiboot 支持状态待核实（BSD Now EP361，[863.18-887.58]，L4）
- McKusick 关于“文档 committer 与源码 committer 同等投票”的叙述属当事人视角，须与 FreeBSD 选举规则文件与历届 core 名单交叉核验；其对自己“不再关键”的自评也属谦辞。　[存疑脚注] 选举资格细节须以 FreeBSD Core Team 规则文件核实。（BSD Now EP278，[533.12-611.68]，L3）
- McKusick 提及的研究（MIT 与法国高校基于 commit log 分析领导层）未给出具体出处，其“只有 Apache 与 FreeBSD 等少数项目完成多次更替”的结论需核对原始研究。　[存疑脚注] 所援引研究未具名，结论无法直接追溯。（BSD Now EP278，[725.94-799.70]，L4）
- 转写专名失真须全面校核：BBN 被记作 Bermick and Nguyen，应为 Bolt Beranek and Newman；DSP FAST file system 应为 BSD Fast File System；TreeBSD 应为 FreeBSD；PreBSD 应为 FreeBSD；microstation 应为 workstations；Sleepy Cat 应为 Sleepycat。另有一处年代压缩风险：1989 年发布、黑客补齐六文件、1990 年出现独立 BSD 的叙述把 Net/1、Net/2 与 386BSD 的序列压成约数，精确版本学须对照发行物原件。　[存疑脚注] 年代压缩系当事人约数记忆，须以 Networking Release 1（1989）、Release 2（1991）与 386BSD（1992）的原始发行记录复核。（BSDTalk EP18，[267.67-349.19]，L1）

**文献**：

- [BSD Now EP362] Pennington J. BSD Now: 362: 2.11-BSD restoration[EB/OL]. (2020-08-06)[2026-08-15]. https://www.bsdnow.tv/362.
- [BSD Now EP361] Pennington J. BSD Now: 361: Function-based MicroVM[EB/OL]. (2020-07-30)[2026-08-15]. https://www.bsdnow.tv/361.
- [BSD Now EP278] Pennington J. BSD Now: Episode 278: The Real McCoy | BSD Now 278[EB/OL]. (2018-12-27)[2026-08-15]. https://www.bsdnow.tv/278.
- [BSDTalk EP18] Backman W. BSDTalk: Interview with Kirk McKusick[EB/OL]. (2006-02-17)[2026-08-15]. https://archive.org/download/bsdtalk018/bsdtalk018.ogg.

<!-- /PODCAST_REVIEW -->
