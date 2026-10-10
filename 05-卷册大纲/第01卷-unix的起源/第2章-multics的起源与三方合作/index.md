---
chapter: 第 2 章
id: CH2
volume: 第01卷-unix的起源
---

# 第 2 章 multics的起源与三方合作

## 要点

- 分析哲学与数学哲学为本书提供三重思想前提：其一，弗雷格—罗素的谓词逻辑与类型论直接构成下一节（2.2 数理逻辑核心概念）的内容主体；其二，希尔伯特判定问题在 1936 年引出图灵机模型（2.3），把“可机械执行的推理”从哲学理想变为数学对象；其三，从逻辑主义追求必然基础到哥德尔揭示形式系统内在限度，再到蒯因消解分析/综合的绝对二分，这条思想曲线与 UNIX 的工程经验主义、Multics 的理性主
- 为运行 Space Travel，Thompson 在 PDP-7 上构建了文件系统、进程调度、shell 雏形；这些基础设施演化为 UNIX 第一版（1969 年夏末）
- Multics 源代码、文档、运行日志由 MIT、Honeywell、Van Vleck 等保存；Multics.org 网站为最完整的在线档案；多项 Multics 概念（段式内存、动态链接、访问控制列表）影响后续操作系统
- Multics 是早期支持对称多处理（SMP）的操作系统之一——在 Honeywell 6180 上的多处理器配置中，允许多个 CPU 共享同一内存映像，由内核的锁机制协调。同时，Multics 实现了“在线重配置”——可在不停止系统运行的情况下添加/移除 CPU、内存模块与 I/O 控制器——这是现代云计算“热迁移”与“热插拔”的远古先例。
- 部分 Multics 工程师后来承认 UNIX 的简洁具有实用价值，但批评其安全模型粗糙、文件系统原始；Peter Neumann 持续批评 UNIX 安全缺陷至 21 世纪

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3604] 卷“第01卷-unix的起源”第 2 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1465] 卷“第01卷-unix的起源”第 2 章，匹配置信度 0.8，原因：关键词重合 2 项（file, finding, ports, clones, freebsd）
- [DB:references_fulltext:chapter_matches:chmatch_22] 卷“第01卷-unix的起源”第 2 章，匹配置信度 0.6，原因：路径启发：Thompson Trusting Trust 1984
- [DB:bsdnow_podcast:outline_mappings:om_11676] BSD Now 第 506 期，匹配 CH2 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12052] BSD Now 第 463 期，匹配 CH2 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12196] BSD Now 第 446 期，匹配 CH2 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12516] BSD Now 第 418 期，匹配 CH2 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12706] BSD Now 第 362 期，匹配 CH2 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12766] BSD Now 第 344 期，匹配 CH2 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12873] BSD Now 第 261 期，匹配 CH2 章，关联度 2.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 将 UNIX 哲学与实用主义/经验主义传统相联系的做法存在回溯性建构风险——Ritchie、Thompson 等人并无系统阅读分析哲学的文献证据，联系应止于“思想气候”层面
- UNIX 诞生日期 1969 年夏末是否准确——Thompson 与 Ritchie 的回忆略有出入；“第一版”的边界模糊
- Multics 对后续系统的影响程度存在争议——Plan 9、Java、Windows NT 的设计者均称受 Multics 启发，但影响路径难以精确追踪
- Multics SMP 使用“粗粒度锁”策略，在 2–4 个 CPU 配置下性能良好，但无法线性扩展至更多处理器。后续 Solaris、FreeBSD 与 Linux 的 SMP 演进（细粒度锁、RCU、NUMA 感知）暴露了 Multics 方法的局限，但这些局限在 1970 年代完全不可见。
- Neumann 的批评是否公平——需对比 Multics 与 UNIX 的实际安全记录；批评中是否夹杂项目失败的情绪

## 文献

- 同本节 2.1.1-2.1.4 所列；另参见 Turner F. From Counterculture to Cyberculture [M]. 2006（关于思想气候迁移的二手研究）
- Unix Heritage Society (TUHS) PDP-7 UNIX 重建项目；Ritchie 1984 BLTJ 63 No. 6 Part 2:1577-1593, DOI 10.1002/j.1538-7305.1984.tb00054.x；Kernighan 2019 回忆录 ［B］
- Multics.org；Organick“The Multics System” (1972)；Elliott Organick“Computer System Organization” (1973) [考据脚注：Organick 1972 为 Multics 研究经典一手文献，Multics 档案保存与概念遗产经 multicians.org 交叉验证确证。]
- Honeywell Info Systems, “Multics System Programmer's Manual,” 1977; Thomas W. Doeppner, “Operating Systems In Depth,” Wiley, 2011（第 6 章多处理器调度对 Multics 的回顾） ［B］
- Peter Neumann RISKS Forum (ACM)；Multics.org 社区评论；Neumann“Computer Security in Open Systems” (1995) ［B］
- Ritchie 1984 BLTJ 63 No. 6 Part 2:1577-1593, DOI 10.1002/j.1538-7305.1984.tb00054.x；Thompson 1979 BYTE；Kernighan 2019 回忆录 ［B］
- Ritchie & Thompson 1974 CACM“The UNIX Time-Sharing System”；Ritchie 1979/1984“The Evolution of the Unix Time-sharing System”（1979 年 AUUG 研讨会首次发表，1984 年 BLTJ 正式刊出）；US Patent 4,135,240“Protection of data file contents”；Morris 蠕虫 1988 事件报告；freebsd.duckdb：freebsd-src commit `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25，4.4BSD-Lite import）；freebsd.duckdb：freebsd-src commit `c2f46557264110fb353a0f512292db9330c09dc4`（1996-03-11，4.4BSD-Lite2 import） ［A］
- Shannon C E. A Symbolic Analysis of Relay and Switching Circuits [J]. Transactions of the AIEE, 1938, 57(12): 713-723；同本节 2.2.1-2.2.4 所列 [考据脚注：香农 1938 年硕士论文内容为逻辑史与信息论史学界公认，经信息论史文献与本章 2.15.13 节既有考据交叉验证确证。]
- 同本节 2.3.1-2.3.4 所列；另参见 Ceruzzi P. A History of Modern Computing [M]. 2003（模型—机器关系的二手研究）
- 同本节 2.4.1-2.4.4 所列；另参见 Ceruzzi 2003 第 1-3 章；Campbell-Kelly & Aspray“Computer”(1996) 相关章节

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：YouTube EPnwbqBdghh6E（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- McKusick 以当事人视角浓缩 BSD 全史：Ken Thompson 身为伯克利校友，1975 年学术休假时把 UNIX 带回校园，一年内吸引了一批研究生；1976 年他离开时 Bill Joy 已接管系统并继续开发，随后把伯克利开发的软件打包，以 Berkeley Software Distributions 之名发行，年度发行延续近十五年，先后由 Joy 与包括 McKusick 本人在内的后来者主持；1980 年代末自由再分发软件的兴趣渐起，伯克利同人着手把 AT&T 专有部分从 BSD 中剥离，到伯克利的最终发行版（转写作 1992 年）整个发行已可自由再分发；此后两支力量接续支撑 BSD——NetBSD 以支持尽可能多的硬件架构为目标，从微波炉到 Cray XMP 皆在其列，其口述时点已支持近六十种架构，FreeBSD 则以在 PC 架构上运行 BSD、支持尽可能广的设备并把系统做得尽量易装以吸引广大开发者为目标；他本人选择主要跟随 FreeBSD 群体，一面做软件，一面与 George Neville-Neil 合著 The Design and Implementation of the FreeBSD Operating System。（YouTube EPnwbqBdghh6E，[39.2-169.9]，L1）
- McKusick 叙述 UNIX 的诞生语境：UNIX 之前的主角是 Multics，由 Honeywell、AT&T 贝尔实验室与 MIT 三方合力建造分时系统，项目愈益宏伟却始终未能进入生产，每学会做一件事便又推倒重构去做下一件；贝尔实验室撤出后，已经习惯坐在 ASR33 电传终端前交互编程的 Ken Thompson 与 Dennis Ritchie 不愿退回打卡片的作业流，从角落里翻出一台废弃的小型机（转写作 PDP-8），写出一个极小的系统即 UNIX，其后迁往 PDP-11；鉴于 Multics 万事求全的教训，两人确立“找出做事的那一种方式”的极简哲学，标识符只保留进程号、用户号与组号寥寥数种，并让同一组标识符兼作计数、保护判定与调度决策之用。[订正：原区间终点 1994.2→1997.41，原终点止于转写“used for counting, used for making”段，“protection decisions, used for scheduling decisions”（保护判定与调度决策）落转写 [1994.2-1997.41] 段，内容复核]（YouTube EPnwbqBdghh6E，[1859.4-1998.3]，L1）[订正：原“（他按读音称 Multix）”——新转写该处为“a thing called Multics”，未见 Multix 读音变体，已删；重锚 [1864.49-1997.41]→[1859.4-1998.3]，内容核符]
- McKusick 把统一描述符空间列为 UNIX 的两大关键观念之一：给定一个描述符即可引用终端、文件、磁盘、管道或套接字等任何 I/O 通道，使用者无须知道它背后是什么便能读写且行为正确；此前各设备各配一套打开、读、写、关闭调用，像 cat 这样的程序必须自行判别输入类型并分派调用，统一之后程序只管读写，新增描述符类型亦不破坏既有程序；他称此后几乎每个操作系统都采纳了这一构造，唯太平洋西北岸一家大公司的系统至今未完全统一，并打趣说 Longhorn 会解决这个问题。（YouTube EPnwbqBdghh6E，[2019.4-2141.5]，L1）
- McKusick 把进程即商品列为另一关键观念：UNIX 之前的系统里进程是重型的贵重资源，IBM MVS 由系统管理员在引导时决定多重处理度数并预先创建定数进程，用户以 JCL 把编译各步写成一叠卡片作业——他称 JCL 是“六十年代的 sendmail 配置文件”，多一个空格或丢一个逗号整个作业即被吐回，且须经操作员换卡重交、等待数小时才能看到结果；UNIX 让这类记账性工作交给机器，按需即时创建进程、以管道相连、用毕即弃——一次编译即把预处理器、多趟编译器、优化器与装载器等七个进程经管道流水串联；他强调这并非进程创建变得廉价（以运行 ls 为例，九成以上成本仍在创建与销毁进程本身），而是省下的编程人力值得付出这份开销；早期内存不足时管道在底层实为文件，今则全在内存中流转。（YouTube EPnwbqBdghh6E，[2190.0-2537.5]，L1）

**史料**：

- 本期为 McKusick 内核课程宣传片与第一讲选段的一手口述：当事人自述其浓缩伯克利全史的三小时半录像与十二讲、约三十小时课程均发布于个人网站 www.mckusick.com，教科书为其与 George Neville-Neil 合著的 The Design and Implementation of the FreeBSD Operating System；讲义附录另载一篇约五年至八年前发表的 journalling 与 soft updates 比较论文，其结论为两种一致性方案性能相当，可作文件系统技术史线索。[订正：原考据脚注“本流转写被系统标记 severe_repetition，宣传片引言、第一讲开讲与第一讲正文三条音轨交错混排”之缺陷经滚动重叠重建后已不存在，新转写为单轨顺排]　[已核备注] 新转写已为单轨顺排，多音轨交错缺陷不再存在；人名与机器型号转写音变（如 PDP-8）仍见于自动转写，引用前仍须按通行记载核对。（YouTube EPnwbqBdghh6E，[103.4-966.4]，L3）[订正：原区间仅覆盖片首宣传段的录像与课程发布信息（[103.4-192.2]），未覆盖本条所述“讲义附录另载 journalling 与 soft updates 比较论文、两者性能相当”段（实位于第一讲文件系统提纲段 [930.7-966.4]）；重锚 [103.62-191.139]→[103.4-966.4]，扩；另“十二讲”新转写作“twelve chapters and thirty hours”，章节数与时长核符]

**史观**：

- 总纲4 分离聚合是永恒规律：McKusick 指出虚拟机并非新物：1960 年代计算机以冰箱大小的机柜与洗衣机大小的磁盘机组成，造价数百万美元的机器每秒仅约千万条指令，人人直接对裸硬件编程，IBM 以 VM 系统在一台十 MIPS 巨机上克隆出多台一模一样的裸机，各自引导数据库、工资单或分时作业；UNIX 借用其“独立可操作之物”的观念却把界面抬升到进程层，而授课时 VMware 一类产品又让用户回到引导原生操作系统——他称之为“关于正确层次为何的钟摆”往返摆动；抽象的聚拢与拆散在裸机、进程诸层之间循环往复，而非沿单一直线推进。（YouTube EPnwbqBdghh6E，[1477.6-2175.8]，L1）[订正：原区间仅覆盖 VMware 回落与“钟摆”结论段（[2149.5-2175.8]），未覆盖本条所述虚拟机起源、1960 年代裸机规格与 IBM VM 克隆段（[1477.6-1698.9]）；重锚 [2151.559-2178.89]→[1477.6-2175.8]，扩，内容核符]
- 总纲5 没有必然性，只有偶然性：McKusick 的 Multics—UNIX 叙事把操作系统的分野落在偶然条件而非必然规律上：三方合作的宏伟计划因不断加码而自我瓦解，UNIX 之所以存在，系于贝尔实验室一次撤出、两位研究者对交互式终端的眷恋，以及角落里恰好闲置的一台旧机器；课程亦以“一切从最顶层宽笔刷讲起、再逐层下探”的三遍式结构自反地承认听者知识水平参差，不预设任何单线的技术进步叙事。（YouTube EPnwbqBdghh6E，[319.1-1959.3]，L1）[订正：原区间仅覆盖“三遍式宽笔刷”教学结构段（[319.1-390.1]），未覆盖本条所述 Multics—UNIX 偶然条件叙事段（[1859.4-1959.3]）；重锚 [336.28-403.759]→[319.1-1959.3]，扩，内容核符]

**辨析**：

- 转写中 Thompson 与 Ritchie 起家所用机器记作 PDP-8（新转写逐字证实演讲原话即为 PDP-8），与通行记载的 PDP-7 不符，疑为口误或转写之误；片首宣传片另称伯克利“最终发行版”年份为 1992 年，而通行纪年为 4.4BSD 于 1993 年发布、4.4BSD-Lite 于 1994 年发布，McKusick 所述或指代码清理完成之时点；两处纪年均属单一来源口述，引用前须另行核验。[订正：原存疑脚注“本流转写为多音轨交错合并”之转写缺陷经滚动重叠重建后已不存在，新转写为单轨顺排]　[已核备注] 新转写已为单轨顺排；PDP-8 机型与 1992 年末版年份两处纪年仍系单一来源口述且与通行记载存在出入，未经与 McKusick 出版著作及 CSRG 发行记录交叉核对前不宜直接引用。（YouTube EPnwbqBdghh6E，[1931.0-1959.3]，L4）[订正：原“同段称伯克利最终发行版年份为 1992 年”不成立——PDP-8 原话位于第一讲正文，1992 年最终发行版陈述位于片首宣传片段 [94.9-103.0]，两处相隔逾 1800 秒，已改作“片首宣传片另称”；重锚 [1933.44-1946.549]→[1931.0-1959.3]，PDP-8 原话新转写逐字核符（“an old uh PDP eight”）]

**文献**：

- [YouTube EPnwbqBdghh6E] YouTube. YouTube: FreeBSD Kernel Internals, Dr. Marshall Kirk McKusick[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=nwbqBdghh6E>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- MIT. LCS RFC 37 (Voydock 1973, <https://people.csail.mit.edu/saltzer/Multics/MHP-Saltzer-060508/bookcases/RFCs/csr-rfc-037.pdf)>[EB/OL]. 1973. ［待核·needs_fix］［DKC-0981→fulltext:5751］
<!-- /dangan-20260908 -->
