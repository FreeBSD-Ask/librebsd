---
chapter: 第 114 章
id: CH114
volume: 第06卷-freebsd的核心技术革新
---

# 第 114 章 DTrace 的设计与 Solaris 起源

## 要点

- DTrace 设计的一手史料包括：Cantrill 在 dtrace.org/blogs/bmc/ 的个人博客（2006-2024 年，dtrace.org 域名仍可访问但部分旧文章存档需经互联网档案馆获取）；USENIX 2004 年论文全文（usenix.org 永久存档）；Solaris Dynamic Tracing Guide（docs.oracle.com 可访问）；Cantrill、
- D 语言最权威的设计文档是 Cantrill 等人 2004 年 USENIX 论文的第 3 节，该节完整描述了 D 语言的类型系统、变量种类（全局、线程局部、子句局部、聚合）、安全约束、执行模型；Solaris Dynamic Tracing Guide（Sun/illumos 出版）是最完整的参考手册，含 D 语言所有特性的逐章说明；FreeBSD 手册页 **dtrace(1)** 的 D
- Sun 选择 CDDL 许可 OpenSolaris（含 DTrace 和 ZFS）的历史背景是 Sun 2004-2005 年的开源战略转型：Sun CEO Scott McNealy 推动 OpenSolaris 以对抗 Linux 在服务器市场的崛起；CDDL 由 Simon Phipps（Sun 首席开源官）和 Sun 法务团队基于 MPL 1.1 起草，2004 年 12 月 1 日提交
- macOS DTrace 集成事件的一手史料包括：Apple 开源代码 opensource.apple.com/source/dtrace/（存档于互联网档案馆）；Leventhal 在 dtrace.org/blogs/ahl/ 的两篇博客（2008-01-18、2008-06-07）；Mac OS X 10.5 Leopard 发布新闻稿和技术文档；MacTech 2007 年 11 月《E
- FreeBSD DTrace 移植的一手史料包括：John Birrell 在 <freebsd-current@freebsd.org> 和 <freebsd-dtrace@freebsd.org> 邮件列表的移植进度帖子（2006-2008 年）；FreeBSD Perforce 仓库//depot/projects/dtrace/ 分支初始导入记录；FreeBSD Subversion 仓库

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_725] 卷“第06卷-freebsd的核心技术革新”第 114 章，匹配置信度 0.6，原因：关键词重合 2 项

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 原文将"Jolitz & Jolitz 1990s Dr. Dobb's Journal ‘Porting UNIX to the 386’"列为 DTrace 文献系明显错误——Jolitz 夫妇的 DDJ 文章是关于 386BSD 的，与 DTrace 无关；原文称论文作者为“Cantrill, Shapiro, Wiethels”系名字错误——第三作者是 Adam H. Leventhal，
- 原文称“D 语言与 BPF 程序比较”但引用 Jolitz DDJ 文章系无关文献错误已修正；D 语言不支持浮点运算是一个常被忽视的限制——DTrace 在内核态执行时默认不使用浮点寄存器以避免保存/恢复浮点上下文的开销，D 程序中不能使用 float/double 类型；D 语言的数组大小有静态上限（DTRACEOPT_MAXSIZE 等可调参数），这些限制都是安全模型的一部分
- 原文将“Sun 许可策略”与 Jolitz DDJ 文章相关联系错误；Sun 是否故意选择 CDDL 以阻止 ZFS/DTrace 进入 Linux 是一个长期争议——Sun 方（Phipps、Cooper）多次否认，称 CDDL 是基于 MPL 的合理许可证选择；GPL 阵营（FSF、Eben Moglen）则认为 CDDL 是故意设计为 GPL 不兼容；从技术史角度，这一争议无法在缺乏 Sun
- 原文标题称“2008 年 Mac OS X 集成 DTrace”系日期错误——Mac OS X 10.5 Leopard 于 2007 年 10 月 26 日发布，DTrace 争议始于 2008 年 1 月（Leventhal 博客发表），修复于 2008 年 6 月（10.5.3），应修正为“2007 年 Mac OS X 集成 DTrace”；〔待核：原文截断，后文待回源〕
- 原文 73.5 节（现行 114.5）标题称“George Neville-Neil 等完成 DTrace 移植”需修正——Neville-Neil 是重要维护者但非发起人；John Birrell 才是 DTrace FreeBSD 移植的发起者和核心实现者，这一事实在 FreeBSD 源码的 copyright 声明和早期 commit log 中均可查证；Birrell 去世的精确信息因公开讣告缺失而标注为 据

## 文献

- Cantrill, B. et al. (2008). Fishworks: Now it can be told. dtrace.org/blogs/bmc/; illumos Project. Dynamic Tracing Guide. illumos.org/books/dtrace/; Gregg, B. DTrace Tools and DTraceToolkit. brendangregg.com/dtrace.html; Leventhal, A. H. (2008). Mac OS X and the missing probes. dtrace.org/blogs/ahl/ ［C］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Cantrill, B. M. et al. (2004). Dynamic Instrumentation of Production Systems. USENIX ATC '04; illumos Project. Solaris Dynamic Tracing Guide. illumos.org/books/dtrace/; FreeBSD Project. **dtrace(1)** Manual Page (D Language Reference) ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Phipps, S. (2005). Why We Chose CDDL. webmink.com; Open Source Initiative. CDDL Approval Archives (2004-12/2005-01). opensource.org; Sun Microsystems. (2005-06-14). OpenSolaris Launches. Press Release［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2004-2004 年间：45,499 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Apple Inc. opensource.apple.com/source/dtrace/ (archived); Leventhal, A. H. dtrace.org/blogs/ahl/ (2008 posts); Apple Inc. Mac OS X 10.5 Technical Specifications (2007-10-26) ［C］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2007-2008 年间：65,762 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project Mailing List Archives. lists.freebsd.org (freebsd-current, freebsd-dtrace); FreeBSD Source Repository. cddl/ import history; FreeBSD Project. Release Notes 7.1-12.x (DTrace changelog entries) ［A］[^doubt-resolved-616]: 据 Handbook (未署名) 消解[^doubt-resolved-617]: 据 Handbook (未署名) 消解[^doubt-resolved-618]: 据 upper-saddle-river-prentice-hall (Gregg, 2011) 消解[^doubt-resolved-619]: 据 操作系统内核并发错误检测研究进展_期刊 (石剑君, 2021) 消解[^doubt-resolved-620]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解[^doubt-resolved-621]: 据 Arch_Handbook (未署名) 消解[^doubt-resolved-622]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-623]: 据 The Fall of the Bell System A Study in Prices and Politics (Peter Temin, Louis Galambos)  (未署名) 消解

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP112（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 当事人 Adam Leventhal 自述其 UNIX 入门与职业轨迹：高中在 NeXT 机器上初识 UNIX，回家在旧 PowerPC 上装 NetBSD 却连 `ls` 都不会、误敲 `dir` 半小时；大学依赖 Solaris 2.6 至 8；2000 年实习于 Solaris 内核团队、2001 年全职，先做 MDB 与 ptools 等诊断工具，随后转入 DTrace；2006-2010 年与 Bryan Cantrill、Mike Shapiro 等在 Sun 内部创业式小组 Fishworks 研发存储设备（即后来的 Oracle ZFS Storage Appliance），恰逢闪存价格骤降与 iPhone 问世，做出 L2ARC 与 SLOG 的混合存储池；Oracle 收购 Sun 后转投 Delphix 历任工程师、经理至 CTO，专注 ZFS 性能。（BSD Now EP112，[744.32-996.62]，L1）
- ZFS 工程贡献的当事人复盘：第一项贡献是把 zlib 移植入内核实现 GZIP 压缩的周末黑客，代码沿用至今基本未改；继而在存储设备项目中把单校验 RAID 扩为双校验并再造三校验（RAID-Z2/Z3），自陈课堂抽象代数难以直接转化为可用的 RAID 数学；与 ZFS 创始工程师之一 Matt Ahrens 合作重写写节流与 I/O 调度器，称其“当然，那很显然——但只有在抛弃了其他更显而易见的答案之后，它才显得显然”（1124.00-1133.34）；send/receive 则源于 Ahrens 滞留中国、不满 rsync 的切肤之痛，Leventhal 明言欣赏这种由急迫痛点催生的创造叙事。（BSD Now EP112，[1013.62-1177.18]，L1）
- 可入册的 Apple 侧一手佐证：Leventhal 回忆 Apple 曾尝试将 ZFS 移植到 Mac OS X 并在某届 WWDC 现场发放演示 DVD，同一届 WWDC 发布了 Time Capsule 与 Time Machine；Sun 一方人员上前询问才发现 Time Machine 与 ZFS 无关，其实现被他称为“以最难看的方式对目录做硬链接”（1276.54-1280.76），而 zfs send/receive 本可优雅完成同样功能；主持人 Kris Moore 随即以 PC-BSD 的 Life Preserver（异地复制加本地快照滑块）作对照。此段为 Apple ZFS 移植夭折史的当事人旁证。（BSD Now EP112，[1242.18-1288.44]，L1）

**史料**：

- 该期提示的一手与近一手材料：Leventhal 本人口述（Sun 内部 DTrace 立项、Fishworks、Delphix）；QNX 官方第三方版权声明 PDF（数百页，丰田 Highlander 车机即 QNX，其中含 OpenCrypto xforms.c 许可文本、NetBSD Foundation 与 NASA Ames 的版权转让、TrustedBSD、OpenSSH、tcpdump 许可等条目）；Chad Dougherty 发往 openbsd-misc 的车机软件信息屏帖；Theo de Raadt 的 pledge(2) 说明文章及全树铺开、征集快照 dmesg 反馈的社区动员；波兰站 Leonardo Taccari 的 NetBSD 7.0 访谈（附英译）；Brian Kernighan 谈 C 语言演化的访谈视频；OpenZFS 开发者峰会议程（Jeff Bonwick 讲 ZFS 诞生史、George Wilson 讲压缩 ARC、Nexenta 讲持久 L2ARC、OVH 讲基于 ZFS 的在线迁移等）；听众整理的 EuroBSDCon 2015 视频时间戳索引。　[存疑脚注] 以上条目名与人名经 ASR 失真（如 Theo Duratt、Christos Zalos），引用前须回查 QNX 版权 PDF、openbsd-misc 原帖与峰会日程原件（BSD Now EP112，[350.78-549.92]，L2）

**史观**：

- 总纲5 没有必然性，只有偶然性：DTrace 的诞生在当事人复盘中处处是偶然而非必然：Cantrill 向论文导师提出改写内核文本作追踪的设想，得到的回答是“我相信如果这可行，早就有人做过了”（1575.18-1580.06）；多年间“DTrace 将解决一切问题、DTrace 知晓一切探针”只是内核组内部“传奇蒸汽件”（1634.54-1649.40）；而 Leventhal 的加入仅因路过办公室时凭 SPARC 架构的一个怪癖想到用户态追踪方案，换来一句“去做吧”。技术史由具体的人在偶然机缘下的日常劳动推进，先于任何总体规划。（BSD Now EP112，[1538.56-1691.96]，L1）
- 总纲13 法律与道德是利益分配：Leventhal 对开源的论证本质是利益结构分析而非道德宣示：开源的价值在于软件不归属某一家公司，公司消失或“变坏”时用户仍有退路；他引 Stephen O'Grady《The Software Paradox》说明软件总利润上升而单一专有软件价值下降，并将开源概括为社区参与、招聘与入市路径；其闭源反事实尤为锋利——“如果 ZFS 或 DTrace 是闭源专有的，它们只会存在于某个垂死的、越来越少人关心的操作系统里”（2272.68-2287.40），即便免费发放二进制也只会加速社区重写兼容实现。许可证与社区规则在此显现为利益分配机制。（BSD Now EP112，[2149.92-2327.12]，L1）

**辨析**：

- 题名考据点：音频内报号自称“episode 112 Tracing the Source, recorded October 21st 2015”，而本卡片沿用库内元数据题名“112: Simple and Functional”，两者不一致；就全期内容（DTrace/ZFS 追踪与源码史）而言，音轨自报题名反而更贴合，入册引用前须核对节目官方存档与播客库期数元数据以定孰是。　[存疑脚注] 音轨自报题名与库内元数据冲突，属单一来源推断，须交叉验证官方存档后方可定题（BSD Now EP112，[34.14-61.26]，L4）
- 转写为双音轨交错、时间戳乱序，但各段语义完整可读；专名 ASR 失真普遍但可辨：“chris moore”应为 Kris Moore（PC-BSD 创始人、Lumina 作者 Ken Moore 之兄，节目中自称撰写 BSD Magazine 的 PC-BSD 10.2 文章），“alan juke”应为 Allan Jude，“Brian Cantrell”应为 Bryan Cantrill，“Matt Arons”应为 Matt Ahrens，“Theo Duratt”应为 Theo de Raadt，“Christos Zalos”应为 Christos Zoulas，“Henning Brouwer”应为 Henning Brauer；唯“Patrick Folstrom”与 BSD Magazine 访谈名单（Drew Levine、Luca Fiera、Alexander Roblacco 之音）无法由上下文确证，引用前须回查原链。　[存疑脚注] 上述人名与名单为转写失真或不可确证项，须逐条回查原始节目页与 BSD Magazine 2015 年 10 月号目录（BSD Now EP112，[485.70-521.80]，L4）

**文献**：

- [BSD Now EP112] Pennington J. BSD Now: 112: Tracing the source[EB/OL]. (2015-10-21)[2026-08-15]. <https://www.bsdnow.tv/112>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Corbet. J. (2007-08-07). On DTrace envy. LWN.net. lwn.net/Articles/244536/[Z]. 2007. ［DKC-1901→fulltext:6001］
<!-- /dangan-20260908 -->
