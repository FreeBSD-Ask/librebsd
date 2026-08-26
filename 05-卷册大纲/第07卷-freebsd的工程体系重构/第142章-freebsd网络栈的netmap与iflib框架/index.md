---
chapter: 第 142 章
id: CH142
volume: 07
---

## 要点

- **netmap(4)** 是 Luigi Rizzo（比萨大学，同时也是 FreeBSD 长期贡献者、dummynet 作者）设计的高速网络包 I/O 框架，论文发表于 SIGCOMM 2011；netmap 的核心思想是：通过将网卡环形缓冲区和内核包内存直接映射到用户态，绕过传统的 **mbuf(9)** 分配和协议栈处理，实现线速（wire speed）包处理——在 10Gbps 网卡上可以实现 14.88 Mpps（百万包每秒）的收发性能，仅占用单个 CPU 核的一小部分；VALE 是 netmap 附带的虚拟软件交换机，可作为虚拟机和 jail 之间的高速虚拟交换机；netmap pipes 实现高性能包管道；netmap 于 FreeBSD 10.0（2014 年 1 月）正式合入 FreeBSD 基础系统，Linux 也有 netmap 移植；与 DPDK（Intel 开发的用户态包处理框架）相比，netmap 更轻量、代码更小、与内核协议栈更好地集成（可以实现网卡拉分流——一部分流量走 netmap 用户态、一部分走内核协议栈），DPDK 生态更丰富但完全绕过内核
- **iflib(4)**（interface library）是 FreeBSD 的新一代网络接口驱动框架，由 John Baldwin（约翰·鲍德温） 和 Matt Macy 设计，于 FreeBSD 11.0（2016 年 10 月）引入，在 FreeBSD 12.0（2018 年）成为推荐的网卡驱动编写框架；iflib 出现之前，FreeBSD 网卡驱动直接与 **ifnet(9)** 层交互，每个驱动独立实现多队列、MSI-X 中断、校验和卸载、TSO/LRO 等功能，代码大量重复且容易出错；iflib 将这些通用功能抽象到公共框架中，驱动只需实现硬件相关操作（初始化、发送/接收队列操作、中断处理等），大大减少了代码重复并提升了多队列性能；FreeBSD 11/12/13 中越来越多网卡驱动迁移到 iflib，包括 Intel **ixl(4)**（10G/25G/40G/100G）、Mellanox **mlx5(4)**（10G-200G+）、Broadcom **bnxt(4)** 等现代高速网卡驱动；iflib 天然支持多队列分发、RSS（Receive Side Scaling）、硬件 offload、校验和、TSO/LRO、VLAN 卸载
- SCTP（Stream Control Transmission Protocol，RFC 4960）是一个现代传输层协议，支持多流（multi-streaming）、多宿主（multi-homing），最初为电信信令设计但也用于通用网络；FreeBSD SCTP 实现主要由 Randall Stewart 和 Michael Tuexen 维护，于 FreeBSD 7.0（2008 年）正式合入基础系统，是业界质量最高的 SCTP 实现之一；IPv6 支持来自日本 KAME 项目——KAME 是 1998-2006 年日本多家公司和研究机构（NEC、Toshiba、Hitachi、IIJ、Keio University、WIDE 项目）合作的 BSD IPv6/IPsec 参考实现项目；FreeBSD 4.0（2000 年）引入 KAME IPv6 栈，是最早原生支持 IPv6 的主流操作系统之一；无线驱动方面 FreeBSD 支持多种无线网卡：**ath(4)**（Atheros，Sam Leffler 维护，质量最好）、**iwn(4)**/**iwm(4)**（Intel Wireless）、**urtw(4)**/**rtwn(4)**（Realtek USB WiFi）、**wpi(4)**（Intel 3945）等；无线子系统和 **wlan(4)** 802.11 层主要由 Sam Leffler 开发和维护
- netmap、iflib、SCTP、KAME IPv6 这几个子系统有一个共同点：它们都是由特定领域专家长期维护的 “专业级” 代码——Rizzo 的 netmap/dummynet、Stewart/Tuexen 的 SCTP、Baldwin/Macy 的 iflib、KAME 团队的 IPv6、Leffler 的无线子系统；FreeBSD 网络栈不是由某个统一团队 “设计” 的，而是在 30 年间由不同领域的专家持续贡献和维护形成的有机整体；netmap 的一个常被忽视的特点：它的 API 设计同时支持内核模块和用户态程序，内核模块可以直接使用 netmap API 实现高速包处理（如软件交换机、防火墙）。FreeBSD 网络子系统关键技术演进汇总见下表。
- 本时期 FreeBSD 核心仓库的贡献高度依赖受雇于企业的核心开发者——iXsystems、Netflix、Intel、Isilon/EMC 等公司将工程资源投入 FreeBSD 的网络、存储与虚拟化子系统，以换取基础设施稳定；这种 “有组织贡献” 与志愿者个人贡献性质不同，二者共同构成 BSD 生态韧性之源（参见总纲第 7/10/22/25 条）。

## 史观

- 总纲第 1 条——项目统摄史观：netmap 在 SIGCOMM 2011 的发表是高速包处理的 “一刻”——在 netmap 和 DPDK 之前，软件包处理无法达到线速，10Gbps 网卡需要专用硬件；netmap 证明了通过正确的架构设计，通用 CPU 可以处理 10Gbps 甚至更高速率的包，这直接催生了软件定义网络（SDN）和网络功能虚拟化（NFV）的很多创新
  - 辨析：netmap
- 总纲第 10 条——边缘者贡献：网络子系统的许多关键技术来自学术界（Rizzo 在比萨大学、KAME 在日本大学和研究机构）和专业领域公司（Netflix 做 CDN 优化），不是来自 “核心团队” 的规划；这体现了开源的力量——最好的代码可能来自意想不到的地方
- 辨析：netmap 是否被 FreeBSD 弃用——没有，netmap 仍在活跃维护，是 FreeBSD 高速包处理的主要方案；DP
- 总纲第 7 条——技术选择即政治选择：企业赞助方向直接塑造 FreeBSD 在该时期的子系统优先级（如 Netflix 推动内核 TLS 卸载与网络栈高性能化）。
  - 辨析：企业提交多属受雇工作期间的 “有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验。
  - 文献：bsd_commits.db（freebsd-src contri
- 总纲第 6 条——技术路线分化：Linux 以 eBPF 通用可编程数据面、FreeBSD 以 netmap/专用框架追求高性能，是网络栈演进的两条路线。
  - 辨析：eBPF 的“通用内核虚拟机”与 netmap 的“零拷贝用户态 IO”范式不同；将 XDP 等同于 netmap 会忽略架构差异。
  - 文献：Linux Kernel. eBPF/XDP Documentation [EB/
- 总纲第 7 条——BSD 谱系：三大 BSD 网络栈同源 4.4BSD-Lite，pf 的共享、VNET 思路的互鉴体现 BSD 家族“代码自由流动”的特征。
- 辨析：OpenBSD 主导 pf 开发，FreeBSD/NetBSD 移植并各自扩展，这一“上游在 OpenBSD、下游多 BSD 复用”的模式是 BSD 协作的典型样本。
- 文献：OpenBSD. pf(4) Manual [Z]；

## 辨析

- netmap 引入 FreeBSD 版本——netmap 代码在 FreeBSD 9.x 时代通过开发分支可获取，在 FreeBSD 10.0-RELEASE（2014）正式合入基础系统；数据库证据进一步精确化时间线：netmap 首次完整合入主线 commit 为 2011-11-17（`68b8534bdfeb...`），早于 FreeBSD 9.0-RELEASE（2012-01-12）约
- netmap 是否被 FreeBSD 弃用——没有，netmap 仍在活跃维护，是 FreeBSD 高速包处理的主要方案；DPDK 在 FreeBSD 上的支持——DPDK 有 FreeBSD 移植但不在基础系统中，需要从 ports 安装；KAME 项目的 IPv6 代码是否还存在于现代 FreeBSD 中——KAME 代码经过 20 年演进和重写，现代 FreeBSD IPv6 栈已不是原始
- 企业提交多属受雇工作期间的 “有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验。
  - 文献：bsd_commits.db（freebsd-src contributors 表，窗口 2010–2020，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<<https://docs.freebsd.org/en/arti>
- eBPF 的“通用内核虚拟机”与 netmap 的“零拷贝用户态 IO”范式不同；将 XDP 等同于 netmap 会忽略架构差异。
  - 文献：Linux Kernel. eBPF/XDP Documentation [EB/OL]；Rizzo L. netmap [A]. USENIX ATC 2012. ［B］
    FreeBSD 社区论文与演讲 [326]，[326] Christo
- OpenBSD 主导 pf 开发，FreeBSD/NetBSD 移植并各自扩展，这一“上游在 OpenBSD、下游多 BSD 复用”的模式是 BSD 协作的典型样本。
- 文献：OpenBSD. pf(4) Manual [Z]；DragonFly. Network Stack MPSAFE Notes [EB/OL]. ［B］

## 文献

- Rizzo, L. (2012). *netmap: A Novel Framework for Fast Packet I/O*. USENIX ATC '12 (SIGCOMM precursor); FreeBSD Project. (2014-01). *FreeBSD 10.0 Release Notes* (netmap). freebsd.org; Rizzo, L. (2012). *VALE: A Switched Ethernet for Virtual Machines*. ACM CoNEXT ’12; DPDK Project. (2010-2026). *DPDK
- FreeBSD Project. *Source Code History for netmap, SCTP, iflib, IPv6*. cgit.freebsd.org; Rizzo, L. (2011-2026). *netmap Project Page*. info.iet.unipi.it/~luigi/netmap/; Stewart, R., & Tuexen, M. (2007-2026). *SCTP for FreeBSD*. sctp.freebsd.org; KAME Project. (1998-2006). *KAME Project Archive*. web.
- bsd_commits.db（freebsd-src contributors 表，窗口 2010–2020，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<https://docs.freebsd.org/en/articles/contributing/>）［B］
    FreeBSD 社区论文与演讲 [329]，[329] Christos Margiolis. Re-decentralizing the Internet with BSD [C]//EuroBSDcon 2025. [S.l.]: [s.n.], 2025. 获取路径：<<https://pape>
- Linux Kernel. eBPF/XDP Documentation [EB/OL]；Rizzo L. netmap [A]. USENIX ATC 2012. ［B］
    FreeBSD 社区论文与演讲 [326]，[326] Christos Margiolis. Vox FreeBSD: How sound(4) works [C]//BSDCan 2025. [S.l.]: [s.n.], 2025. 获取路径：<https://papers.freebsd.org/2025/bsdcan/margiolis-vox-freebsd-how-sound4-works/> [访问
- OpenBSD. pf(4) Manual [Z]；DragonFly. Network Stack MPSAFE Notes [EB/OL]. ［B］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
