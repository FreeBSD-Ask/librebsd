## 第 36 章 不同时期人员的采访录

### CSRG 时期核心成员的采访（1978-1992 时期当事人）

#### 采访 1：麦库西克（Marshall Kirk McKusick）

**字段 1 采访元数据**

- 受访者：麦库西克（Kirk McKusick），时任加州大学伯克利分校 CSRG 核心成员
- 采访者：Will Backman，bsdtalk 播客主持人
- 采访时间：2006（bsdtalk 第 018 期发布）
- 采访形式：播客访谈
- 原始来源：bsdtalk Episode 018，互联网档案馆归档 **<https://archive.org/details/bsdtalk018>**
- 存档信息：互联网档案馆归档页经联网抓取可访问（访问日期 2026-07-24），未失效

**字段 2 采访摘要**

麦库西克在 bsdtalk 播客中回顾了 4.3BSD（1986 年发布）作为 CSRG 稳定维护版本的意义，详述了 4.3BSD 相对 4.2BSD 在性能与稳定性上的改进，以及 Mike Karels 在系统维护中的关键角色。访谈涉及 4.3BSD 时期 CSRG 与 Sun 的代码回流关系、虚拟内存改进工作，以及 4.3BSD 作为后续 Tahoe 与 Reno 版本基础的地位。

**字段 3 考据脚注**

本则采访的互联网档案馆归档页经联网抓取核实。麦库西克关于 4.3BSD 的陈述，经 Salus 1994 年《A Quarter Century of UNIX》中关于 4.3BSD 的章节交叉验证。自利偏差审查：麦库西克作为 CSRG 成员，对 4.3BSD 历史地位的叙述可能存在阵营立场偏向。完整考据过程见 [20260724_kirk-mckusick-bsdtalk-018-4.3bsd.md](../../../原材料/研究/考据记录/20260724_kirk-mckusick-bsdtalk-018-4.3bsd.md)。

**字段 4 与本章节内容的关联**

- 为子节 17.1（4.3BSD 的开发背景）提供 CSRG 核心成员的当事人回忆
- 为子节 17.3（4.3BSD 的性能改进）提供性能改进的当事人视角
- 为子节 17.5（4.3BSD 作为后续版本基础）提供从 2006 年回望 4.3BSD 地位的长时段反思

**字段 5 史观映射**

- 总纲 10“动手者创造历史”——据 据原文第 14 章 14.2 节“真正的问题不在于技术发展的程度，而在于是否动手。技术的发展使曾经需要数年完成的工作如今数日可成，但问题始终在于是否有人去做”，麦库西克与 Karels 在 4.3BSD 维护中的稳定性，是 14.2 节“无论什么时候街道总是需要人去扫”的具象——稳定性不是 4.3BSD 的内在属性，而是有人日复一日动手维护的结果。但据 14.1 节“决定世界的并非某个阶级，也不是什么经济”，此处“动手者”不可简化为“系统维护者”的固定身份——麦库西克与 Karels 作为 CSRG 核心成员维护 4.3BSD，是主体性未被理论遮蔽的状态。
- 总纲 22“知识注定过时”——据 据原文第 22 章 22.1 节“今天书写的技术史，可能在出版之日就已过时。但这不意味着史学写作无意义，而是要求史家有此自觉”，4.3BSD 的具体技术随时间过时，但作为基础的地位延续。22.2 节“技术债务是历史设计的代价。许多今天看来不合理的设计，源于其诞生年代的硬件与技术限制，但这一历史遗产至今仍由全球数百万用户承担”提示：4.3BSD 作为后续 Tahoe 与 Reno 的基础，既是技术遗产也是技术债务——后续版本继承 4.3BSD 的设计权衡，也继承其历史包袱。
- 总纲 4“分离聚合是永恒规律”——据 据原文第 4 章 4.1 节“分离聚合是世界发展的规律。分久必合，合久必分，具有必然性”，4.3BSD 作为聚合点，催生后续 Tahoe 与 Reno 的分离——4.3BSD 是 CSRG 多方工作的聚合，而 Tahoe 与 Reno 是从此聚合中分离出的新形态。但 4.2 节“否定后必然会再次产生，这是社会发展的根本动力”提示：Tahoe 与 Reno 的分离并非 4.3BSD 的否定，而是其形式主义的延续。
- 总纲 6“和解优于斗争”——据 据原文第 25 章 总纲 6“历史的动力不是对抗，而是各主体性的呈现与和解。和解是事物真正完整的一刻”，4.3BSD 时期 CSRG 与 Sun 的代码回流关系，是各主体性的呈现与和解——CSRG 与 Sun 在 4.3BSD 中通过代码回流实现了短暂的接纳。但第 6 章 6.7 节“真正的敌人是时间”提示：此和解是时间性的，Sun 转向 System V 是时间流变中的形式主义演化。
- 总纲 18“时间是一种形式主义”——据 据原文第 25 章 总纲 18“等待、记忆、历史的欣赏都具有时间性。沥青滴落般的时间尺度要求史家具备宏观的时间自觉”，4.3BSD 的稳定性是沥青滴落式的时间累积——第 27 章 27.4 节“和解往往取决于等待，或者说，取决于时间。这世间种种的等待，就好像沥青在滴落”提示：4.3BSD 作为后续版本基础的地位，是 BSD 长期主义的体现，但此长期主义非苦难哲学（见总纲 14）。
- 总纲 9“经验优先”——据 据原文第 25 章 总纲 9“优先呈现质朴的事实与当事人的直接经验，而非套用复杂框架”，麦库西克作为 CSRG 核心成员的当事人直接经验，优先于任何事后理论框架。但据第 2 章 2.3 节“记忆的东西从来都是不存在的——那天的偶然性都被转为了必然性，都是不存在的”，其 2006 年的回忆仍是一种形式主义化的重构。

**自反性声明**：本释读本身也是一种形式主义化的重构，不声称是对项目统摄史观的客观正确解读。释读中“麦库西克与 Karels 在 4.3BSD 维护中的稳定性是街道需要人去扫的具象”的判断本身也是一种形式主义化的隐喻归因，把内核维护简化为“扫街”类比，可能遮蔽 4.3BSD 维护中 Karels 对虚拟内存子系统的架构性重构无法被“扫街”涵盖的维度；释读中“4.3BSD 作为后续 Tahoe 与 Reno 基础既是技术遗产也是技术债务”的判断本身也参与遗产/债务二元对立的形式主义运作，可能遮蔽 4.3BSD 设计权衡在 Tahoe/Reno 时期被批判性重写而获得的非债务性延续；释读中“Tahoe 与 Reno 的分离是 4.3BSD 形式主义的延续而非否定”的判断本身也是一种形式主义化的连续性归类，可能遮蔽 Tahoe 在虚拟内存重写中对 4.3BSD 设计的实际否定；释读中“CSRG 与 Sun 在 4.3BSD 中通过代码回流实现短暂接纳”的判断本身也是一种形式主义化的和解浪漫化，可能遮蔽此回流中 Sun 对 CSRG 资源的实际汲取；释读中“4.3BSD 稳定性是沥青滴落式的时间累积”的判断本身也是一种形式主义化的时间浪漫化，可能遮蔽 4.3BSD 稳定性更源于 CSRG 内部代码评审制度的工程性建构；释读中“麦库西克 2006 年回忆仍是形式主义化的重构”的判断本身也是一种形式主义化的时间归因，可能遮蔽麦库西克作为长期参与者对 4.3BSD 维护细节的累积性认知，欢迎被更自反的释读所超越（见 据原文第 27 章 27.2 节）。

---

---

<!-- 附录还原合并：附录-采访录：Kirk McKusick.md -->

## 第 36 章 不同时期人员的采访录

### CSRG 时期核心成员的采访（1978-1992 时期当事人）

#### 采访 1：麦库西克（Kirk McKusick）

**字段 1 采访元数据**

- 受访者：麦库西克（Kirk McKusick），时任加州大学伯克利分校 CSRG 核心成员
- 采访者：Will Backman，bsdtalk 播客主持人
- 采访时间：2006（bsdtalk 第 018 期发布）
- 采访形式：播客访谈
- 原始来源：bsdtalk Episode 018，互联网档案馆归档 **<https://archive.org/details/bsdtalk018>**
- 存档信息：互联网档案馆归档页经联网抓取可访问（访问日期 2026-07-24），未失效

**字段 2 采访摘要**

麦库西克在 bsdtalk 播客中回顾了 4.3BSD-Tahoe（1988 年发布）作为 CSRG 首个平台移植版本的意义，详述了 CCI（Chrysler Computer Corp.）Power 6 平台的移植工作，以及 Tahoe 版本如何引入了对非 VAX 平台的可移植性考量。访谈涉及 Tahoe 版本在 CSRG 内部的争议——是否应该投入资源支持非主流平台，以及这一决策对后续 Net/2 与 4.4BSD 可移植性设计的奠基作用。

**字段 3 考据脚注**

本则采访的互联网档案馆归档页经联网抓取核实。麦库西克关于 4.3BSD-Tahoe 的陈述，经 Salus 1994 年《A Quarter Century of UNIX》中关于 Tahoe 版本的章节与 4.3BSD-Tahoe 手册页交叉验证。自利偏差审查：麦库西克作为 CSRG 成员，对 Tahoe 历史地位的叙述可能存在阵营立场偏向，正文引用时须对照 CCI Power 6 平台档案。完整考据过程见 [20260724_kirk-mckusick-bsdtalk-018-tahoe.md](../../../原材料/研究/考据记录/20260724_kirk-mckusick-bsdtalk-018-tahoe.md)。

**字段 4 与本章节内容的关联**

- 为子节 18.1（4.3BSD-Tahoe 的开发背景）提供 CSRG 核心成员的当事人回忆
- 为子节 18.3（CCI Power 6 平台移植）提供平台移植的当事人视角
- 为子节 18.5（Tahoe 对后续可移植性的奠基作用）提供从 2006 年回望 Tahoe 地位的长时段反思

**字段 5 史观映射**

- 总纲 3“不存在进步，只有权力再分配”——据 据原文第 25 章 总纲 3“技术演进不是从低级到高级的进步，而是形式主义的诡异曲线”，CCI Power 6 硬件平台直接塑造了 Tahoe 的可移植性设计空间——但这并非“可移植性进步”，而是第 9 章 9.3 节“不存在绝对的发展。修仙小说设定古法强于今法存在逻辑悖论，但反过来说今法绝对强于古法同样存在问题”所述的形式主义演化：Tahoe 针对 CCI Power 6 的移植工作，在后续非 VAX 平台的演化中既是基础也是技术债务。
- 总纲 10“动手者创造历史”——据 据原文第 14 章 14.2 节“真正的问题不在于技术发展的程度，而在于是否动手。技术的发展使曾经需要数年完成的工作如今数日可成，但问题始终在于是否有人去做”，CSRG 在 CCI Power 6 平台移植中的工作，是“动手去做”的具体显现——可移植性不是规划出来的设计目标，而是有人动手把代码移植到非主流平台上后才生出的属性。但据 14.1 节“决定世界的并非某个阶级，也不是什么经济”，此处“动手者”不可简化为“平台移植者”的固定身份——CSRG 成员移植代码到 CCI Power 6，是主体性未被理论遮蔽的状态。
- 总纲 4“分离聚合是永恒规律”——据 据原文第 4 章 4.1 节“分离聚合是世界发展的规律。分久必合，合久必分，具有必然性”，Tahoe 作为 VAX 与非 VAX 平台的分离点，催生后续可移植性聚合——Tahoe 是 VAX 平台与非 VAX 平台的分离，而后续 Net/2 与 4.4BSD 的可移植性设计是此分离产生的新聚合。但 4.2 节“否定后必然会再次产生，这是社会发展的根本动力”提示：Tahoe 的分离并非 VAX 平台的终结，而是通过此分离产生了新的可移植性形态。
- 总纲 5“没有必然性，只有偶然性”——据 据原文第 5 章 5.2 节“那种认为‘张三不上李四也会上’的观点，无视了世界上没有必然性只有偶然性这一事实”，CCI Power 6 平台的出现与 CSRG 选择移植到此平台，均为偶然条件交汇——若非 CCI 在 1980 年代后期提供 Power 6 平台与合同支持，Tahoe 不会以此时序诞生。但 5.3 节“记忆将许多偶然性认识为一种必然性，同时否定了这种偶然性的发生”提示：麦库西克 2006 年的回忆可能已将偶然转为必然。
- 总纲 22“知识注定过时”——据 据原文第 22 章 22.1 节“今天书写的技术史，可能在出版之日就已过时。但这不意味着史学写作无意义，而是要求史家有此自觉”，Tahoe 针对 CCI Power 6 的移植工作随 CCI 平台的消失而过时，但 22.2 节“技术债务是历史设计的代价。许多今天看来不合理的设计，源于其诞生年代的硬件与技术限制，但这一历史遗产至今仍由全球数百万用户承担”提示：Tahoe 的可移植性设计作为历史遗产，至今仍由后续 BSD 版本承担——既是基础也是包袱。
- 总纲 9“经验优先”——据 据原文第 25 章 总纲 9“优先呈现质朴的事实与当事人的直接经验，而非套用复杂框架”，麦库西克作为 CSRG 核心成员的当事人直接经验，优先于任何事后理论框架。但据第 2 章 2.3 节“记忆的东西从来都是不存在的——那天的偶然性都被转为了必然性，都是不存在的”，其 2006 年的回忆仍是一种形式主义化的重构。

**自反性声明**：本释读本身也是一种形式主义化的重构，不声称是对项目统摄史观的客观正确解读。释读中“Tahoe 针对 CCI Power 6 的可移植性设计是形式主义演化而非可移植性进步”的判断本身也是一种形式主义化的进步/非进步二元对立运作，可能遮蔽 Tahoe 在机器无关层抽象上相对 4.3BSD 的实际可度量进步；释读中“可移植性是动手移植后才生出的属性而非规划目标”的判断本身也参与动手/规划二元对立的形式主义运作，可能遮蔽 CSRG 在 Tahoe 立项前对可移植性战略价值的显式评估；释读中“Tahoe 作为 VAX 与非 VAX 分离点催生后续可移植性聚合”的判断本身也是一种形式主义化的循环论归因，可能遮蔽 Tahoe 移植决策中 CCI 合同金额与 DARPA 多平台战略的具体驱动而非抽象的“分离—聚合”；释读中“CCI Power 6 出现与 CSRG 选择移植是偶然条件交汇”的判断本身也参与偶然/必然二元的形式主义运作，可能遮蔽 CSRG 在 1986-1987 年间对多平台战略的主动追寻而非被动接受偶然；释读中“Tahoe 可移植性设计是历史遗产也是技术包袱”的判断本身也参与遗产/包袱二元对立的形式主义运作，可能遮蔽 Tahoe 机器无关层在 SPARC、i386 等后续平台移植中被批判性继承而获得的非包袱性延续；释读中“麦库西克 2006 年回忆已将偶然转为必然”的判断本身也是一种形式主义化的时间归因，可能遮蔽麦库西克对 CCI 合同执行流程的累积性认知，欢迎被更自反的释读所超越（见 据原文第 27 章 27.2 节）。

---


<!-- DEEP_ANALYSIS: cross_indexes.duckdb.concept_history -->
**史家判断**（证据等级：L2，来源：`cross_indexes.duckdb.concept_history.6`）

GEOM 由 Poul-Henning Kamp 提出构想（早期思想文《Geometry —— an idea》），最原始前身是作者对 Minix 1.2 所做的一个从未发布的 hack。2002 年 Kamp 在 NAI Labs 支持下，于 DARPA/SPAWAR 合同与 DARPA CHATS 研究计划框架内开发成形。2003 年 Kamp 在 BSDCon 发表 GEOM 教程。GEOM 自 FreeBSD 5.0（2003）起提供，明确定义 class/geom/provider/consumer/rank 等拓扑概念，提供分区（FDISK/MBR、GPT、BSD slice）、镜像（geom_mirror）、RAID、UFS 卷标、GBDE/geli 磁盘加密等类，并支持 ggate 用户态网关。至 FreeBSD 13.0，GEOM_BSD、GEOM_MBR、GEOM_SUNLABEL 等过时组件被移除，由 GEOM_PART_* 与 GEOM_LABEL 等替代，框架持续演化。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-121`）

TrustedBSD MAC 框架是用于 FreeBSD 平台的操作系统访问控制扩展的灵活模块化环境，由 Robert Watson 等人在 DARPA 信息生存能力项目会议论文中描述。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-012`）

4.4BSD 架构手册的作者署名为 William Joy、Robert Fabry、Samuel Leffler、M. Kirk McKusick、Michael Karels，隶属伯克利计算机系统研究组（CSRG）。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-013`）

4.2BSD 的 IPC 设施文档由计算机系统研究组（CSRG）成员 Samuel J. Leffler、Robert S. Fabry、William N. Joy、Phil Lapsley 署名。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-046`）

Ralph Campbell（CSRG，1986）撰写了 4.3BSD 行式打印机假脱机（lpd）手册。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-2-047`）

BIND 4.9 的一位作者在开发与发布 BIND 4.9 期间任职于 DEC 网络系统实验室，并曾被借调至 CSRG 完成相关工作。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-048`）

Graham、Kessler 与 McKusick（1982）描述了 gprof 调用图执行剖析器的设计：将被调例程的运行时间计入调用它们的例程。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-2-049`）

Sun Microsystems 与 CSRG（1988）的 rpcgen 编程指南说明 rpcgen(1) 用于帮助程序员简单直接地编写 RPC 应用。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-052`）

McKusick、Karels 与 Bostic（1989）描述了 CSRG 以小团队开发与集成 4.3BSD 的发布工程策略：每个发布周期分为开发阶段与发布工程阶段，发布工程分三步（alpha、beta、最终发布）。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-053`）

McKusick、Karels 与 Bostic（1989）记载伯克利的发布在“引入重大新设施”与“提供缺陷修复与效率改进”之间交替。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-054`）

McKusick、Karels 与 Bostic（1989）记载 CSRG 一直是一个小型软件开发团队，需协调 CSRG 成员与贡献代码的外部社区成员。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-055`）

McKusick、Karels 与 Bostic（1989）认为 BSD 开发的优势在于少数核心开发者能理解整个系统并协调工作，这是大型开发组织难以复制的。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-002`）

CSRG 使用 SCCS（首个源代码控制系统）管理 BSD 开发，1983 年设计 socket 接口并实现 TCP/IP，允许少数受信任外部贡献者经 ARPAnet 登录开发机直接更新源码。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-053`）

McKusick、Karels 与 Bostic 1990 年提出在可换页内存而非专用内存中构建 RAM 磁盘文件系统原型，以避免专用内存带来的性能损失。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-059`）

Macklem 1988 年记载 4.4BSD 的 NFS 实现可与 NFS Version 2 协议（RFC1094）实现互操作，并允许使用另一替代协议。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-3-061`）

Marshall Kirk McKusick（住址 1689 San Pablo Avenue, Berkeley）出现在 2017 年 5 月 30 日伯克利市议会会议记录的通信列表中，由议员 Worthington 提交。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-069`）

BIND 运维指南脚注记载作者 Kevin J. Dunlap 是 DEC ULTRIX 工程高级开发组成员，完成该工作时借调至 CSRG。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-003`）

FreeBSD 于 1993 年 6 月 19 日命名，由 Bill Jolitz 面向 Intel 386 的 4.4BSD-Lite 移植版本派生而来。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-105`）

CSRG 用 SCCS 管理源码，1983 年设计 socket 接口并在其下实现 TCP/IP，允许少数受信任外部贡献者经 ARPAnet 直接更新源码。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-113`）

McKusick 2018 年演讲称 FreeBSD 于 1993 年 6 月 19 日命名，源自 Bill Jolitz 面向 Intel 386 的 4.4BSD-Lite 移植版本。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-119`）

和解协议规定 UNIX 衍生文件包含 4.4BSD-Lite 中的 23 个文件，USL 在协议签署前已审阅并批准其纳入 4.4BSD-Lite。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-010`）

McKusick 与 Benno Rice 在《The Evolution of FreeBSD Governance》（FreeBSD Journal, 2017）中记载：BSDi 于 2000 年收购 Walnut Creek CDROM，使受雇开发者可接触 BSD/OS 源码；内核多线程化中 John Baldwin 的方案借鉴 BSD/OS 与 Solaris，Matthew Dillon 偏好类似 Amiga 内核的架构，两人冲突因核心团队不愿在技术争论中选边而加剧，最终 Dillon 的 commit 权限被移除并离开创立 DragonFly BSD。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-015`）

McKusick 在 BSDCan 2018 演讲中记载：Yahoo 完全基于 FreeBSD 运行并同意托管 CVS 仓库与发行版，Justin Gibbs 创立 FreeBSD Foundation 旨在提供 FreeBSD 项目基础设施——基金会成立的直接背景是项目基础设施对单一公司（Yahoo）的依赖。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-016`）

McKusick 在 BSDCan 2018 演讲中记载：FreeBSD 核心团队最初为终身制（约 20 名成员），僵化与冷漠促使起草章程建立 9 名成员、由 committer 选举的核心团队，首届民选核心团队于 2000 年产生且几乎无旧成员留任。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-113`）

关于 FreeBSD 迁移到 Subversion 的时间存在矛盾：McKusick 称经辩论后于 2000 年迁到 Subversion，而 Ed Maste 的版本控制历史显示 src/ 仓库直到 2008-05-31 才迁至 Subversion。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-6-002`）

Pawel Jakub Dawidek 与 Marshall Kirk McKusick 合作撰写将 Solaris ZFS 移植到 FreeBSD 的论文。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-6-107`）

4.2BSD 与 4.3BSD 引入可靠信号（reliable signals）与快速文件系统（fast filesystem），这是 FFS/UFS 进入 Berkeley 系统发行版的开端。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L2，来源：`historical_claims.duckdb.claim.CL-8-008`）

参考文献全文数据库收录《Berkeley city charter en》（Berkeley，1908），作为本章主题的候选史料。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-018`）

计算机系统研究组（CSRG）一直是小型软件开发团队，资源限制要求精细的软件工程管理以及对 CSRG 成员与社区贡献者的协调。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-052`）

McKusick 与 Karels 1988 年记载 4.3BSD 内核拥有至少十种不同的内存分配器，并提出通用目的动态内存分配器以统一接口。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L2，来源：`historical_claims.duckdb.claim.CL-8-003`）

参考文献全文数据库收录《McKusick design impl 44bsd en》（McKusick，1996），作为本章主题的候选史料。

## 文献

- eurobsdcon2014-mandoc-slides[M].
- eurobsdcon2015-mandoc[M].
- FreeBSD-Foundation-October-2016-Update[M]. 2016.
- FreeBSD-Foundation-September-2016-Update[M]. 2016.
- ONODERA R. NetBSD on Google Compute Engine -- Step by Step Guide（幻灯片）[EB/OL]. AsiaBSDCon 2016 NetBSD BoF.
- Martin Husemann. netbsd arm be8 asiabsdcon2015[M]. 2015.

