---
chapter: 第 115 章
id: CH115
volume: 第06卷-freebsd的核心技术革新
---

# 第 115 章 dtrace对ebpf的影响与跨系统传承

## 要点

- Cantrill 与 Shapiro、Leventhal 三人团队在 2002-2004 年秘密开发 DTrace——背景是 Solaris 10 的‘系统可观测性危机’。
- DTrace 贡献者记录的一手史料分布在多个地方：Sun/Oracle 时期的贡献记录主要在 Solaris 源码版权头和 USENIX 论文作者中；FreeBSD 移植者记录在 FreeBSD commit log（svn/freebsd.org 和 git）和邮件列表中；Brendan Gregg 的工具集贡献在 DTraceToolkit 和 GitHub 上；eBPF 贡献者记录在 Lin
- SystemTap、eBPF 与 DTrace 的关键技术差异对比如下表，三种追踪系统代表了三种设计哲学：DTrace 追求追踪专用与安全一体化，eBPF 追求通用可扩展多用途，SystemTap 追求 GPL 兼容与功能灵活。| 系统 | 起始年份 | 主导者 | 编译/执行模型 | 安全模型 | 主要平台 | 主要局限 || --- | --- | --- | --- | --- | ---
- **统计分析印证**——`freebsd.db` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；Pettitt 与 BUISHAND R 双变点检验一致判定变点为 1999-08（p < 0
- DTrace 对 eBPF 影响的一手史料包括：Brendan Gregg 在 brendangregg.com 关于 DTrace 和 eBPF 的博客文章（2014-2024 年，数量众多）；Gregg 2014 LISA 演讲幻灯片和视频；USENIX ATC 等会议上关于 eBPF 和 DTrace 的学术论文；Alexei Starovoitov 和 Daniel Borkmann 在

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_12238] BSD Now 第 444 期，匹配 CH115 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- John Birrell 的去世信息是 DTrace 历史中一个需要谨慎处理的点——他作为 FreeBSD DTrace 移植的发起者，其贡献值得记录，但公开可查的英文资料中关于他的去世信息有限（无法找到正式讣告或精确日期），在获得确切信息前标注为 [存疑脚注：2026-08-17 John Birrell 去世日期无正式讣告，无法确证] 是合适的做法；Mike Shapiro 在 DTrace 
- *统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 Sen's slope =+1.40/月 的实际工程意义须结合 FreeBSD 版本周期与 commit 粒度变化综合判断；(2) 变点归因存疑：1999-08 变点距 DTrace 集成约 7 年，归因单一化风险
- 原文称“Gregg 宣告 bpftrace 为‘DTrace 2.0’”——这一表述经检索 Gregg 博客和演讲，"DTrace 2.0"更多是 Gregg 在描述 bpftrace 定位时使用的类比修辞，而非正式宣告；Gregg 在实际写作中更谨慎地区分了 DTrace 和 bpftrace/eBPF 的关系；bpftrace 创建者是 Alastair Robertson，Gregg 是重要
- 原文将 OpenDTrace 描述为“2018 年 FreeBSD 基金会资助”的项目，经核实存在两处错误：启动时间应为 2016 年 9 月（GitHub 仓库创建日期一手核验），FreeBSD 基金会资助未查到明确证据，已修正；OpenDTrace 不是对 DTrace 的重写，而是基于 OpenSolaris 原始代码的跨平台整理——这一点与某些报道所称“重写”不同
- Oracle 在 2010 年代后期向 eBPF 靠拢（Oracle Linux 同时支持 DTrace 和 eBPF）确实在工程话语权上标志着 DTrace 不再是 Oracle 的可观测性战略重心，但 Oracle 同时继续维护 Solaris DTrace 和 Oracle Linux DTrace；Cantrill 离开 Oracle 后（2010 年加入 Joyent，2019 年联合创

## 文献

- Cantrill 2008; dtrace.org ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Source Repository. cddl/ commit history and copyright notices; Linux kernel MAINTAINERS and git history; Cantrill, B., Shapiro, M., & Leventhal, A. (2004). Dynamic Instrumentation of Production Systems (author credits); Gregg, B. brendangregg.com ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. freebsd.db freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\freebsd.db`; Hibsd Project. 推断性统计.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md` Task 5-6; Hibsd Project. 时间序列分析.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\时间序列分析.md` Task 14-15; Hibsd Project. 卷章数据映射.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\卷章数据映射.md` 第五卷第 51 章映射。［A］### 史观映射> DTrace 的“零开销”许诺是一种消解性的美——在生产环境中做到观测而不扰动，本身就是对复杂性最安静的否定。但这份安静没能传到 Linux 那一侧：CDDL 让 DTrace 成为 Linux 社区口中“嫉妒的对象”而非“技术的同行”，Corbet 勾勒的“嫉妒”话语框架将 DTrace 定位为可望不可即的彼岸而非可对话的伙伴；但 DTrace 的设计思想并未因许可证壁垒而消亡——安全验证器、探针抽象、聚合模型通过 eBPF 在 Linux 生态中获得了新生，Brendan Gregg 从 DTrace 布道者到 eBPF 核心贡献者的转变本身就是这一技术谱系的最佳证明；Oracle 以 GPLv2+ 重新许可 DTrace Linux 代码的那一天，CDDL 路线在 Linux 上的工程话语权败局已写定——不是 DTrace 的探针失效了，而是许可证的边界比探针划得更深；然而 DTrace 在 FreeBSD、macOS、illumos 上继续安静地运行着，Netflix Open Connect CDN 每天用它分析 TB 级流量，这本身就是对“被击败”叙事最沉默的反驳——好的技术不需要赢下所有平台，只要在它存在的地方可靠地工作---> ## 第 51.13 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 51.14 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）[^doubt-resolved-624]: 据 piotrowski-benchmarking-performance-overhead-of-dtrace-on-freebsd-and-ebpf-on-linux-paper (asiabsdcon, 2024) 消解[^doubt-resolved-625]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-626]: 据 Handbook (未署名) 消解[^doubt-resolved-627]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解[^doubt-resolved-628]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解[^doubt-resolved-629]: 据 JavaScriptFirst20Years (WirfsBrockEich, 2020) 消解[^doubt-resolved-630]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Gregg, B. brendangregg.com (DTrace/eBPF blog series); Robertson, A. bpftrace. github.com/iovisor/bpftrace; iovisor Project. iovisor.org; Starovoitov, A. & Borkmann, D. LKML eBPF patch submissions ［C］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- OpenDTrace GitHub. github.com/opendtrace (created September 2016); dtrace.org official website[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Gregg, B. brendangregg.com; Cantrill, B. dtrace.org/blogs/bmc/ (post-Oracle posts); eBPF Summit proceedings (2020-2025); USENIX LISA proceedings ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Corbet, J. LWN.net archive; Gregg, B. brendangregg.com; Linux Kernel Mailing List. lkml.org; SystemTap mailing lists. sourceware.org/systemtap/[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2007-2007 年间：33,007 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
