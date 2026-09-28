---
chapter: 第 141 章
id: CH141
volume: 第07卷-freebsd的工程体系重构
---

# 第141章 freebsd网络栈的tcp-sack漏洞与响应

## 史料

- [DB:research_notes:blocks:86198] 关键词“freebsd网络栈”命中：05-卷册大纲/第05卷-freebsd技术现代化/第55章-freebsd网络栈/第55.14节.md…
- [DB:research_notes:blocks:86216] 关键词“freebsd网络栈”命中：05-卷册大纲/第05卷-freebsd技术现代化/第55章-freebsd网络栈/第55.14节.md…
- [DB:research_notes:blocks:110807] 关键词“freebsd网络栈”命中：编号：5qg
定位：第5卷-55.7.4
缺口类型：文献字段完整性
建议动作：按扫描报告补全（文献字段完整性）
来源 U…

## 要点

- DragonFly BSD 是 Matt Dillon 于 2003 年从 FreeBSD 4.x 分叉的 BSD 操作系统，采用截然不同的 SMP 架构——不是细粒度锁，而是“每 CPU 线程模型”（per-CPU thread model）和消息传递；DragonFly 网络栈 MPSAFE 化路径与 FreeBSD 差异显著：FreeBSD 采用渐进式锁拆分（持续到 2010 年代中后期才完全移除 Giant 锁），DragonFly 则在 Matthew Dillon（马修·狄龙） 的带领下采用激进的架构重构：每个协议线程绑定到特定 CPU，使用异步消息（IPI，Inter-Processor Interrupt）在 CPU 核之间传递网络事件，而非传统的共享内存加锁；到 DragonFly 2.6（2009 年）左右网络栈核心协议实现了无锁或极少锁的并发处理，到 DragonFly 3.8（2014 年）左右包括 **pf(4)** 和 **ipfw(8)** 在内的所有网络子系统完成 MPSAFE 化
- DragonFly 网络栈并发模型的核心是用异步消息传递替代互斥锁——当某个 CPU 上的网络协议栈需要访问其他 CPU 管理的数据结构时，它不获取锁，而是发送一条 IPI 消息到目标 CPU，由目标 CPU 的协议线程在自己的上下文中访问数据并返回结果；这一设计类似于微内核的消息传递，但在单内核中实现；优点是：① 无死锁——消息传递天然避免了锁的死锁问题；② 优秀的多 CPU 扩展性——每个 CPU 独立运行协议线程，几乎不需要锁；③ 可预测的延迟——没有锁等待导致的延迟不确定性；缺点是：① 编程模型更复杂，需要将网络处理分解为消息驱动的状态机；② 某些工作负载下 IPI 本身成为开销；③ 代码与传统 BSD 网络栈差异大，难以从 FreeBSD 移植驱动
- FreeBSD 与 DragonFly 网络栈并行化路径对比：① 并发模型——FreeBSD 使用细粒度互斥锁（mutex/rwlock）保护共享数据结构，DragonFly 使用 per-CPU 线程+IPI 消息传递；② 代码演进——FreeBSD 在 CSRG 4.4BSD 代码基础上渐进式拆分锁，保留了绝大部分传统 BSD 网络栈代码结构；DragonFly 对网络栈做了更大规模的架构重构；③ 完成时间——FreeBSD 网络栈 Giant 锁移除持续了超过 10 年（2003-2014+），部分较新的网卡驱动（如 iflib 驱动）完全无 Giant 锁依赖但部分旧路径直到 11/12 才彻底移除；DragonFly 在 5 年左右（2009-2014）完成了核心网络栈的 MPSAFE 化；④ 生态兼容性——FreeBSD 的渐进式演进保留了与传统驱动和网络模块的兼容性，DragonFly 的重构导致网络驱动需要更多改动才能移植。FreeBSD 与 DragonFly 网络栈并行化路径关键维度对比见下表。
- DragonFly MPSAFE 网络栈的一手史料主要在 DragonFly 项目内部——Dillon 的内核提交日志非常详细（每个 commit 都有长篇解释），是研究其架构演进的极佳材料；但需要注意：DragonFly 社区规模小，大部分设计文档和讨论在 dragonflybsd.org 邮件列表和内核源码提交注释中，没有像 FreeBSD 那样多的第三方文档和会议论文；对比研究两个系统的网络栈需要注意：性能测试结果高度依赖硬件配置、网卡型号、测试工作负载、系统调优参数——看到“X 比 Y 快 50%”的说法时必须查看完整测试条件
- **ipfw(8)**（IP Firewall）是 FreeBSD 原生的防火墙和包过滤框架，最初由 Ugen J. S. Antsilevich 开发，随 FreeBSD 1.0（1993 年）即已存在，是 FreeBSD 历史最悠久的防火墙；**dummynet(4)** 流量整形系统由 Luigi Rizzo 于 1998 年设计并集成到 ipfw 框架，提供带宽限制、延迟模拟、丢包模拟、队列管理等功能，成为学术研究（TCP 协议研究）和网络仿真的标准工具；ipfw 采用经典的“规则列表匹配”模型——数据包按照规则编号顺序匹配，支持：IP/TCP/UDP/ICMP 层过滤、状态跟踪（keep-state、limit）、NAT（通过 **ipfw_nat(4)** 或 **ng_nat(4)**）、dummynet 流量整形、table 查找（高效 IP 集匹配）、fwd 规则（策略路由）；ipfw 的用户态工具是 **ipfw(8)** 命令；FreeBSD 10 之后 ipfw 还集成了 pfil 钩子和 VNET 支持

## 史观

- 技术路线分化：DragonFly 与 FreeBSD 的网络栈并行化路径分歧是 2003 年分叉时就决定的——Dillon 认为 FreeBSD 的细粒度锁路线会导致不可接受的锁复杂度和性能扩展性问题，选择了更激进的消息传递/每 CPU 线程模型；两种路线各有优劣，是 BSD 生态中技术多样性的体现
  - 辨析：“DragonFly 网络栈比 FreeBSD 快”不能一概而论—
- 总纲第 6 条——技术路线分化：FreeBSD 与 DragonFly 的 SMP 网络栈路线选择再次证明：没有“唯一正确”的技术路线，架构选择必须考虑项目目标、开发资源、生态约束——FreeBSD 作为生产系统优先考虑兼容性和稳定性，选择渐进路线；DragonFly 作为研究/创新导向的系统，选择激进重构以实现更好的 SMP 扩展性
- 辨析：“DragonFly 路线更先进”是价值判断不是事实
- 项目统摄史观：ipfw 从 FreeBSD 1.0 起就存在，是极少数从项目成立延续至今仍在活跃维护的子系统——它见证了 FreeBSD 从 386BSD 后裔到现代操作系统的完整历史；dummynet 被全球网络研究者使用了 25 年，体现了好的工程设计的长久生命力
  - 辨析：ipfw 作者——Ugen Antsilevich 是 ipfw 最初作者（1993），Luigi
- 总纲第 6 条——技术路线分化：三个防火墙在 FreeBSD 中并存体现了 BSD 世界的“选择哲学”——不强制用户使用某个“官方答案”，而是提供多个经过验证的选项，让用户根据场景选择；这与 Linux 世界从 iptables 到 nftables 的强制迁移形成对比
- 辨析：“pf 是 FreeBSD 默认防火墙”——严格来说 FreeBSD 基础系统没有默认启用任何防火墙，用户需要自行配置
- 信息技术：SACK Panic 漏洞揭示了一个深刻的信息技术悖论——TCP/IP 协议在 1981 年（RFC 793）设计时几乎不考虑安全问题，SACK 作为 1996 年的扩展（RFC 2018）也主要关注性能，40 年后这些核心协议实现中的安全漏洞可以让整个互联网基础设施面临风险；这说明 “性能优化” 与 “安全保证” 之间存在永恒张力
  - 辨析：漏洞影响的 Free

## 辨析

- “DragonFly 网络栈比 FreeBSD 快”不能一概而论——DragonFly 在高包速、多 CPU 场景下有更好的扩展性（由于无锁设计），但 FreeBSD 有更丰富的网卡驱动和硬件支持；DragonFly 的每 CPU 模型在某些工作负载下（如跨 CPU 流）可能有更高的 IPI 开销；DragonFly 是相对小众的 BSD 发行版，硬件支持和生态规模不如 FreeBSD，这不是技术
- “DragonFly 路线更先进”是价值判断不是事实判断——两种路线在不同场景下各有优劣；FreeBSD 网络栈是否最终也会完全无锁——FreeBSD 12/13/14 持续减少锁竞争，但没有转向消息传递模型的计划；iflib 框架通过多队列和 per-CPU 数据结构实现了高并发，但仍使用互斥锁保护必要的共享状态
- 文献：Dillon, M., & Watson, R. N. M. (2013〔待核：原文截断〕
- ipfw 作者——Ugen Antsilevich 是 ipfw 最初作者（1993），Luigi Rizzo 设计了 dummynet（1997-1998），后来 Gleb Smirnoff 等人做了大量现代化改进（支持 SMP、IPv6、VNET）；ipfw 是“第一代防火墙”吗？从技术上 ipfw 是 stateless 防火墙起家，后来添加了 keep-state 状态跟踪，现在是有状态防
- “pf 是 FreeBSD 默认防火墙”——严格来说 FreeBSD 基础系统没有默认启用任何防火墙，用户需要自行配置和启用；但 pfSense/OPNsense 等防火墙发行版默认使用 pf，pf 也是目前最活跃开发的防火墙；ipfw 是否被弃用——没有，ipfw 和 dummynet 仍在活跃维护和使用，dummynet 在学术研究中地位不可替代；三大防火墙可以同时使用吗？技术上可以通过 pf
- 漏洞影响的 FreeBSD 版本——SA-19:08 显示受影响版本为 FreeBSD 11.2、11.3、12.0、12.1，使用 RACK TCP 栈的 FreeBSD 13-CURRENT 不受 CVE-2019-5599 影响；SACK Panic 不是 OpenBSD 2026 年发现的——SACK Panic 是 2019 年的漏洞，章节标题提到的 “OpenBSD TCP SACK

## 文献

- Dillon, M. (2003-2014). *DragonFly Kernel Design Posts*. dragonflybsd.org; DragonFly Project. (2009-2014). *Release Notes* (MPSAFE sections). dragonflybsd.org; Sherrill, J. (2014). *DragonFly Networking Performance*. BSDCan '14.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］


<!-- dangan-20260908 消解回写 -->
- IETF.. . *RFC 5925: TCP Authentication Option*. ietf.org[Z]. 2010. ［DKC-2201→fulltext:6104］
<!-- /dangan-20260908 -->
## 140.10.4 网络栈并行化史料辨析

- 要点：DragonFly MPSA
- FreeBSD Project. *ipfw(8), dummynet(4) Manual Pages*; Rizzo, L. (1997). *Dummynet: A Simple Approach to the Evaluation of Network Protocols*. ACM Computer Communication Review; FreeBSD Foundation. *FreeBSD Handbook: Firewalls*. freebsd.org; Rizzo, L. (2010s). *ipfw/dummynet Modernization*. freebsd-n
- FreeBSD Foundation. *FreeBSD Handbook: Firewall Choices*. freebsd.org; Lucas, M. W. (2014). *FreeBSD Mastery: PF*. Tilted Windmill Press; PfSense Project. *Why PF? Documentation*. pfsense.org; Biancuzzi, F. (2005). *Interview with Daniel Hartmeier*. onlamp.com. ［B］
- FreeBSD Security Team. (2019-06-17). *FreeBSD-SA-19:08.tcp_sack: TCP SACK Denial of Service Vulnerabilities*. freebsd.org; Looney, J. (2019-06-17). *SACK Panic: Remote Denial of Service Vulnerabilities in Linux and FreeBSD*. Netflix Security Advisory; CVE Program. CVE-2019-5599, CVE-2019-11477/8/9.
- FreeBSD Project. *Active Committers List*. freebsd.org; FreeBSD Core Team. *Public Announcements Archive*. freebsd.org/news; FreeBSD Project. *Commit History*. cgit.freebsd.org. ［A］

## 140.9.2 2010-2026 年间网络栈贡献者动态记录

- 要点：2010-2026 年间 FreeBSD 网络栈贡献者呈现 “核心稳定、持续有新贡献者加入” 的态势：①2010-2015——Gleb Smirnoff

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
