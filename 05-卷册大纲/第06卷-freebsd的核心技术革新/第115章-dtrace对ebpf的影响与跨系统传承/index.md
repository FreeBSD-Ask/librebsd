---
chapter: 第 115 章
id: CH115
volume: 第06卷-freebsd的核心技术革新
---

# 第 115 章 dtrace对ebpf的影响与跨系统传承

## 要点

- Cantrill 与 Shapiro、Leventhal 三人团队在 2002-2004 年秘密开发 DTrace——背景是 Solaris 10 的‘系统可观测性危机’。
- DTrace 贡献者记录的一手史料分布在多个地方：Sun/Oracle 时期的贡献记录主要在 Solaris 源码版权头和 USENIX 论文作者中；FreeBSD 移植者记录在 FreeBSD commit log（svn/freebsd.org 和 git）和邮件列表中；Brendan Gregg 的工具集贡献在 DTraceToolkit 和 GitHub 上；eBPF 贡献者记录在 Lin
- SystemTap、eBPF 与 DTrace 的关键技术差异对比如下表，三种追踪系统代表了三种设计哲学：DTrace 追求追踪专用与安全一体化，eBPF 追求通用可扩展多用途，SystemTap 追求 GPL 兼容与功能灵活。

| 系统 | 起始年份 | 主导者 | 编译/执行模型 | 安全模型 | 主要平台 | 主要局限 |
| --- | --- | --- | --- | --- | --- | --- |
| DTrace | 2004 年 | Sun（Cantrill 等） | D 语言 →DIF 字节码 → 内核 DIF 虚拟机 | DIF 验证器（无循环、无写、无跳转） | Solaris/FreeBSD/macOS/NetBSD/Windows | D 语言图灵不完备，无循环 |
| eBPF | 2014 年 | Starovoitov/Borkmann | C 语言 →LLVM/Clang→eBPF 字节码 | eBPF 验证器（支持有界循环、尾调用） | Linux（主） | 追踪专用原语需 helper 函数实现 |
| SystemTap | 2005 年 | Red Hat | 脚本 →C 代码 → 内核模块加载 | 早期无形式化验证，存在崩溃风险 | Linux | 安全性弱，云原生场景被 eBPF 盖过 |
- **统计分析印证**——`freebsd.duckdb` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；〔待核：原文截断，后文待回源〕
- DTrace 对 eBPF 影响的一手史料包括：Brendan Gregg 在 brendangregg.com 关于 DTrace 和 eBPF 的博客文章（2014-2024 年，数量众多）；Gregg 2014 LISA 演讲幻灯片和视频；USENIX ATC 等会议上关于 eBPF 和 DTrace 的学术论文；Alexei Starovoitov 和 Daniel Borkmann 在

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_12238] BSD Now 第 444 期，匹配 CH115 章，关联度 1.0

## 史观

总纲第 4 条——分离聚合是永恒规律：DTrace 自 Solaris 分离，经 FreeBSD 移植与 OpenDTrace 跨平台整理，再聚合入 macOS、Windows 与 illumos；其验证器、探针抽象与聚合模型又经 eBPF 在 Linux 生态重生——追踪技术的传承呈反复分离与聚合，不以许可证或阵营为边界。各子节逐条史观映射详见本章各子节文件的史观字段。

## 辨析

- John Birrell 的去世信息是 DTrace 历史中一个需要谨慎处理的点——他作为 FreeBSD DTrace 移植的发起者，其贡献值得记录，但公开可查的英文资料中关于他的去世信息有限（无法找到正式讣告或精确日期），在获得确切信息前标注为 [存疑脚注：2026-08-17 John Birrell 去世日期无正式讣告，无法确证] 是合适的做法；Mike Shapiro 在 DTrace
- *统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 Sen's slope =+1.40/月 的实际工程意义须结合 FreeBSD 版本周期与 commit 粒度变化综合判断；(2) 变点归因存疑：1999-08 变点距 DTrace 集成约 7 年，归因单一化风险
- 原文称“Gregg 宣告 bpftrace 为‘DTrace 2.0’”——这一表述经检索 Gregg 博客和演讲，“DTrace 2.0”更多是 Gregg 在描述 bpftrace 定位时使用的类比修辞，而非正式宣告；Gregg 在实际写作中更谨慎地区分了 DTrace 和 bpftrace/eBPF 的关系；bpftrace 创建者是 Alastair Robertson，Gregg 是重要
- 原文将 OpenDTrace 描述为“2018 年 FreeBSD 基金会资助”的项目，经核实存在两处错误：启动时间应为 2016 年 9 月（GitHub 仓库创建日期一手核验），FreeBSD 基金会资助未查到明确证据，已修正；OpenDTrace 不是对 DTrace 的重写，而是基于 OpenSolaris 原始代码的跨平台整理——这一点与某些报道所称“重写”不同
- Oracle 在 2010 年代后期向 eBPF 靠拢（Oracle Linux 同时支持 DTrace 和 eBPF）确实在工程话语权上标志着 DTrace 不再是 Oracle 的可观测性战略重心，但 Oracle 同时继续维护 Solaris DTrace 和 Oracle Linux DTrace；Cantrill 离开 Oracle 后（2010 年加入 Joyent，2019 年联合创

## 文献

- Cantrill 2008; dtrace.org ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Source Repository. cddl/ commit history and copyright notices; Linux kernel MAINTAINERS and git history; Cantrill, B., Shapiro, M., & Leventhal, A. (2004). Dynamic Instrumentation of Production Systems (author credits); Gregg, B. brendangregg.com ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/freebsd.duckdb**; LibreBSD Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5-6; LibreBSD Project. 时间序列分析.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/时间序列分析.md** Task 14-15; LibreBSD Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第五卷第 51 章映射。［A］

### 史观映射

> DTrace 的“零开销”许诺是一种消解性的美——在生产环境中做到观测而不扰动，本身就是对复杂性最安静的否定。但这份安静没能传到 Linux 那一侧：CDDL 让 DTrace 成为 Linux 社区口中“嫉妒的对象”而非“技术的同行”，Corbet 勾勒的“嫉妒”话语框架将 DTrace 定位为可望不可即的彼岸而非可对话的伙伴；但 DTrace 的设计思想并未因许可证壁垒而消亡——安全验证器、探针抽象、聚合模型通过 eBPF 在 Linux 生态中获得了新生，Brendan Gregg 从 DTrace 布道者到 eBPF 核心贡献者的转变本身就是这一技术谱系的最佳证明；Oracle 以 GPLv2+ 重新许可 DTrace Linux 代码的那一天，CDDL 路线在 Linux 上的工程话语权败局已写定——不是 DTrace 的探针失效了，而是许可证的边界比探针划得更深；然而 DTrace 在 FreeBSD、macOS、illumos 上继续安静地运行着，Netflix Open Connect CDN 每天用它分析 TB 级流量，这本身就是对“被击败”叙事最沉默的反驳——好的技术不需要赢下所有平台，只要在它存在的地方可靠地工作。

本章不同时期人员的采访录详见 [采访录.md](采访录.md)。

[^doubt-resolved-624]: 据 piotrowski-benchmarking-performance-overhead-of-dtrace-on-freebsd-and-ebpf-on-linux-paper (asiabsdcon, 2024) 消解
[^doubt-resolved-625]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解
[^doubt-resolved-626]: 据 Handbook (未署名) 消解
[^doubt-resolved-627]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解
[^doubt-resolved-628]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解
[^doubt-resolved-629]: 据 JavaScriptFirst20Years (WirfsBrockEich, 2020) 消解
[^doubt-resolved-630]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Gregg, B. brendangregg.com (DTrace/eBPF blog series); Robertson, A. bpftrace. github.com/iovisor/bpftrace; iovisor Project. iovisor.org; Starovoitov, A. & Borkmann, D. LKML eBPF patch submissions ［C］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- OpenDTrace GitHub. github.com/opendtrace (created September 2016); dtrace.org official website［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Gregg, B. brendangregg.com; Cantrill, B. dtrace.org/blogs/bmc/ (post-Oracle posts); eBPF Summit proceedings (2020-2025); USENIX LISA proceedings ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Corbet, J. LWN.net archive; Gregg, B. brendangregg.com; Linux Kernel Mailing List. lkml.org; SystemTap mailing lists. sourceware.org/systemtap/［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2007-2007 年间：33,007 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP269、BSD Now EP622（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 基金会 2018 年 9 月更新报告全年筹款目标为 125 万美元，Verisign 成为银级赞助商，基金会资助 CI 系统、发布工程与安全团队以支持 12.0 发布。（BSD Now EP269，[435.64-528.72]，L2）
- 文章介绍 daemonize 微型 C 库：System V 式守护进程初始化步骤繁多，而 BSD 自 4.4BSD 起提供的 daemon() 函数不完整遵循这些步骤，作者遂编写仅两个文件的小型库。（BSD Now EP269，[1440.68-1771.96]，L2）
- 微软将 DTrace 从 FreeBSD 移植到 Windows 10，D 脚本基本一致，仅系统调用名改为 NT 前缀的驼峰形式；DTrace 谱系为 illumos 发明、移植 FreeBSD、再传 macOS 与 Windows。（BSD Now EP269，[3414.48-3586.48]，L2）
- 波兰 BSD 用户组由 Mariusz Zaborski 等人在访问湾区 FreeBSD 用户组后创立，定位为促进波兰全部 BSD 的社区，会议以网络交流为主、演讲不超过十五分钟。（BSD Now EP269，[2943.52-3137.00]，L2）
- Mark Phillips 自述 2014 年入职仅约 18 个月的 Ansible，次年公司被 Red Hat 收购；此后在 Red Hat 与多家创业公司间辗转，2025 年初加入 FreeBSD Foundation 任技术营销经理。（BSD Now EP622，[407.42-944.24]，L1）
- Mark Phillips 主张营销的本质是对好产品讲好故事，把营销替换为讲故事即可理解其工作，并强调技术与营销互为表里、工程师需要被反馈其工作价值。（BSD Now EP622，[944.24-1506.38]，L1）
- Mark Phillips 认为 ZFS 是 FreeBSD 的杀手特性，Solaris 系统管理员因 ZFS 与 DTrace 的继承而转向 FreeBSD，FreeNAS 等产品也以此为基础。（BSD Now EP622，[1051.38-1238.66]，L1）
- Mark Phillips 曾帮助测试 Colin Percival 的 EC2 ZFS 根镜像工作，并从 Lightsail 迁往 EC2 以获得 ZFS 根文件系统。（BSD Now EP622，[1205.98-1244.40]，L1）
- Mark Phillips 建议开发者讲故事时不要试图改变他人想法，而是热情讲述自己相信并亲历的解决过程；他推荐 John York 的《Into the Woods》、Seth Godin、Kahneman 与 Nancy Duarte 等读物。（BSD Now EP622，[2825.06-3030.52]，L1）

**史料**：

- 基金会更新提及 OpenSSL 基础版本由 1.0.2 升级至 1.1.1 长期支持版，以及为 12.0 清理内核 bug 报告、修复 Unix 域套接字与 ZFS 回归的进展。（BSD Now EP269，[721.88-822.54]，L2）
- 提及 Doug Engelbart 1968 年“所有演示之母”五十周年，以及 EuroBSDCon 2018 在布加勒斯特举行的游记与 Kamil Rytarowski 的 NetBSD sanitizers 演讲。（BSD Now EP269，[2603.40-2648.68]，L2）
- Mark Phillips 访谈（2025 年 7 月柏林 Hackathon 现场）。（BSD Now EP622，[66.14-3216.34]，L1）
- FreeBSD Foundation 关于页面与 YouTube 频道内容。（BSD Now EP622，[2688.00-2695.60]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：DTrace 从 Solaris 发明、经 FreeBSD 移植、再由微软带入 Windows，追踪工具的跨系统传承显示技术思想的流动并不以许可证或阵营为边界。（BSD Now EP269，[3441.20-3510.40]，L2）
- 总纲10 动手者创造历史：波兰 BSD 用户组以“先做起来、控制在十五分钟演讲、保持低成本”的方式维系社区，说明地方社区依靠组织者的持续投入而非宏大规划得以存续。（BSD Now EP269，[3019.68-3177.30]，L2）
- 总纲15 文化即形式主义：Mark Phillips 把营销还原为讲故事的形式，提示技术传播中的品牌叙事同样是形式化构造。（BSD Now EP622，[2702.70-2727.46]，L1）
- 总纲10 动手者创造历史：他以工程师背景亲手测试 ZFS 根镜像并反馈给 Colin Percival，体现使用者参与塑造云镜像。（BSD Now EP622，[1215.20-1244.40]，L1）
- 总纲9 经验优先：其讲故事方法论基于多年创业与营销一线经验，而非抽象理论推演。（BSD Now EP622，[2553.94-2822.94]，L1）

**辨析**：

- 主持人称微软的 DTrace 移植“未从 illumos 上游起步而是自 FreeBSD 版本开始”，此谱系判断须以微软官方实现与代码署名核实。　[存疑脚注] DTrace Windows 移植的具体代码来源未经一手仓库核对。（BSD Now EP269，[3451.40-3460.96]，L4）
- 访谈为 Mark Phillips 单方自述，其职业时间线与 FreeBSD Foundation 任职细节为单一来源，关键节点须以基金会公告交叉验证。　[存疑脚注] 职业履历为当事人单一来源自述，未与其他公开资料交叉验证（BSD Now EP622，[407.42-944.24]，L4）

**文献**：

- [BSD Now EP269] Pennington J. BSD Now: Episode 269: Tiny Daemon Lib | BSD Now 269[EB/OL]. (2018-10-24)[2026-08-15]. <https://www.bsdnow.tv/269>.
- [BSD Now EP622] Pennington J. BSD Now: 622: Interview with Mark Phillips - Technical Marketing Manager at the FreeBSD Foundation[EB/OL]. (2025-07-31)[2026-08-15]. <https://www.bsdnow.tv/622>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Corbet. J. (2007-08-07). On DTrace envy. LWN.net. lwn.net/Articles/244536/[Z]. 2007. ［DKC-1901→fulltext:6001］
<!-- /dangan-20260908 -->
