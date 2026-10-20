---
chapter: 第 142 章
id: CH142
volume: 第07卷-freebsd的工程体系重构
---

# 第 142 章 FreeBSD 网络栈的 netmap 与 iflib 框架

## 要点

- **netmap(4)** 是 Luigi Rizzo（比萨大学，同时也是 FreeBSD 长期贡献者、dummynet 作者）设计的高速网络包 I/O 框架，论文发表于 USENIX ATC 2012；netmap 的核心思想是：通过将网卡环形缓冲区和内核包内存直接映射到用户态，绕过传统的 **mbuf(9)** 分配和协议栈处理，实现线速（wire speed）包处理——在 10Gbps 网卡上可以实现 14.88 Mpps（百万包每秒）的收发性能，仅占用单个 CPU 核的一小部分；VALE 是 netmap 附带的虚拟软件交换机，可作为虚拟机和 jail 之间的高速虚拟交换机；netmap pipes 实现高性能包管道；netmap 于 FreeBSD 10.0（2014 年 1 月）正式合入 FreeBSD 基本系统，Linux 也有 netmap 移植；与 DPDK（Intel 开发的用户态包处理框架）相比，netmap 更轻量、代码更小、与内核协议栈更好地集成（可以实现网卡拉分流——一部分流量走 netmap 用户态、一部分走内核协议栈），DPDK 生态更丰富但完全绕过内核
- **iflib(4)**（interface library）是 FreeBSD 的新一代网络接口驱动框架，由 John Baldwin（约翰·鲍德温） 和 Matt Macy 设计，于 FreeBSD 11.0（2016 年 10 月）引入，在 FreeBSD 12.0（2018 年）成为推荐的网卡驱动编写框架；iflib 出现之前，FreeBSD 网卡驱动直接与 **ifnet(9)** 层交互，每个驱动独立实现多队列、MSI-X 中断、校验和卸载、TSO/LRO 等功能，代码大量重复且容易出错；iflib 将这些通用功能抽象到公共框架中，驱动只需实现硬件相关操作（初始化、发送/接收队列操作、中断处理等），大大减少了代码重复并提升了多队列性能；FreeBSD 11/12/13 中越来越多网卡驱动迁移到 iflib，包括 Intel **ixl(4)**（10G/25G/40G/100G）、Mellanox **mlx5(4)**（10G-200G+）、Broadcom **bnxt(4)** 等现代高速网卡驱动；iflib 天然支持多队列分发、RSS（Receive Side Scaling）、硬件 offload、校验和、TSO/LRO、VLAN 卸载
- SCTP（Stream Control Transmission Protocol，RFC 4960）是一个现代传输层协议，支持多流（multi-streaming）、多宿主（multi-homing），最初为电信信令设计但也用于通用网络；FreeBSD SCTP 实现主要由 Randall Stewart 和 Michael Tuexen 维护，于 FreeBSD 7.0（2008 年）正式合入基本系统，是业界质量最高的 SCTP 实现之一；IPv6 支持来自日本 KAME 项目——KAME 是 1998-2006 年日本多家公司和研究机构（NEC、Toshiba、Hitachi、IIJ、Keio University、WIDE 项目）合作的 BSD IPv6/IPsec 参考实现项目；FreeBSD 4.0（2000 年）引入 KAME IPv6 栈，是最早原生支持 IPv6 的主流操作系统之一；无线驱动方面 FreeBSD 支持多种无线网卡：**ath(4)**（Atheros，Sam Leffler 维护，质量最好）、**iwn(4)**/**iwm(4)**（Intel Wireless）、**urtw(4)**/**rtwn(4)**（Realtek USB WiFi）、**wpi(4)**（Intel 3945）等；无线子系统和 **wlan(4)** 802.11 层主要由 Sam Leffler 开发和维护
- netmap、iflib、SCTP、KAME IPv6 这几个子系统有一个共同点：它们都是由特定领域专家长期维护的 “专业级” 代码——Rizzo 的 netmap/dummynet、Stewart/Tuexen 的 SCTP、Baldwin/Macy 的 iflib、KAME 团队的 IPv6、Leffler 的无线子系统；FreeBSD 网络栈不是由某个统一团队 “设计” 的，而是在 30 年间由不同领域的专家持续贡献和维护形成的有机整体；netmap 的一个常被忽视的特点：它的 API 设计同时支持内核模块和用户态程序，内核模块可以直接使用 netmap API 实现高速包处理（如软件交换机、防火墙）。FreeBSD 网络子系统关键技术演进汇总见下表。
- 本时期 FreeBSD 核心仓库的贡献高度依赖受雇于企业的核心开发者——iXsystems、Netflix、Intel、Isilon/EMC 等公司将工程资源投入 FreeBSD 的网络、存储与虚拟化子系统，以换取基础设施稳定；这种 “有组织贡献” 与志愿者个人贡献性质不同，二者共同构成 BSD 生态韧性之源（参见总纲第 7/10/22/25 条）。

## 史观

- 专题语（不设总纲条号）——项目统摄史观：netmap 在 SIGCOMM 2011 的发表是高速包处理的 “一刻”——在 netmap 和 DPDK 之前，软件包处理无法达到线速，10Gbps 网卡需要专用硬件；netmap 证明了通过正确的架构设计，通用 CPU 可以处理 10Gbps 甚至更高速率的包，这直接催生了软件定义网络（SDN）和网络功能虚拟化（NFV）的很多创新
  - 辨析：netmap
- 总纲第 10 条——动手者创造历史：网络子系统的许多关键技术来自学术界（Rizzo 在比萨大学、KAME 在日本大学和研究机构）和专业领域公司（Netflix 做 CDN 优化），不是来自 “核心团队” 的规划；这体现了开源的力量——最好的代码可能来自意想不到的地方
- 辨析：netmap 是否被 FreeBSD 弃用——没有，netmap 仍在活跃维护，是 FreeBSD 高速包处理的主要方案；DP
- 总纲第 3 条——不存在进步只有权力再分配：企业赞助方向直接塑造 FreeBSD 在该时期的子系统优先级（如 Netflix 推动内核 TLS 卸载与网络栈高性能化）。
  - 辨析：企业提交多属受雇工作期间的 “有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验。
  - 文献：freebsd.duckdb（freebsd-src contri
- 总纲第 4 条——分离聚合是永恒规律：Linux 以 eBPF 通用可编程数据面、FreeBSD 以 netmap/专用框架追求高性能，是网络栈演进的两条路线。
  - 辨析：eBPF 的“通用内核虚拟机”与 netmap 的“零拷贝用户态 IO”范式不同；将 XDP 等同于 netmap 会忽略架构差异。
  - 文献：Linux Kernel. eBPF/XDP Documentation [EB/
- 总纲第 4 条——分离聚合是永恒规律：三大 BSD 网络栈同源 4.4BSD-Lite，pf 的共享、VNET 思路的互鉴体现 BSD 家族“代码自由流动”的特征。
- 辨析：OpenBSD 主导 pf 开发，FreeBSD/NetBSD 移植并各自扩展，这一“上游在 OpenBSD、下游多 BSD 复用”的模式是 BSD 协作的典型样本。
- 文献：OpenBSD. pf(4) Manual [Z]；

## 辨析

- netmap 引入 FreeBSD 版本——netmap 代码在 FreeBSD 9.x 时代通过开发分支可获取，在 FreeBSD 10.0-RELEASE（2014）正式合入基本系统；数据库证据进一步精确化时间线：netmap 首次完整合入主线 commit 为 2011-11-17（`68b8534bdfeb...`），早于 FreeBSD 9.0-RELEASE（2012-01-12）约
- netmap 是否被 FreeBSD 弃用——没有，netmap 仍在活跃维护，是 FreeBSD 高速包处理的主要方案；DPDK 在 FreeBSD 上的支持——DPDK 有 FreeBSD 移植但不在基本系统中，需要从 ports 安装；KAME 项目的 IPv6 代码是否还存在于现代 FreeBSD 中——KAME 代码经过 20 年演进和重写，现代 FreeBSD IPv6 栈已不是原始
- 企业提交多属受雇工作期间的 “有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验。
  - 文献：freebsd.duckdb（freebsd-src contributors 表，窗口 2010–2020，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<<https://docs.freebsd.org/en/arti>
- eBPF 的“通用内核虚拟机”与 netmap 的“零拷贝用户态 IO”范式不同；将 XDP 等同于 netmap 会忽略架构差异。
  - 文献：Linux Kernel. eBPF/XDP Documentation [EB/OL]；Rizzo L. netmap [A]. USENIX ATC 2012. ［B］
    FreeBSD 社区论文与演讲 [326]，[326] Christo
- OpenBSD 主导 pf 开发，FreeBSD/NetBSD 移植并各自扩展，这一“上游在 OpenBSD、下游多 BSD 复用”的模式是 BSD 协作的典型样本。
- 文献：OpenBSD. pf(4) Manual [Z]；DragonFly. Network Stack MPSAFE Notes [EB/OL]. ［B］

## 文献

- Rizzo, L. (2012). *netmap: A Novel Framework for Fast Packet I/O*. USENIX ATC '12; FreeBSD Project. (2014-01). *FreeBSD 10.0 Release Notes* (netmap). freebsd.org; Rizzo, L. (2012). *VALE: A Switched Ethernet for Virtual Machines*. ACM CoNEXT ’12; DPDK Project. (2010-2026). *DPDK
- FreeBSD Project. *Source Code History for netmap, SCTP, iflib, IPv6*. cgit.freebsd.org; Rizzo, L. (2011-2026). *netmap Project Page*. info.iet.unipi.it/~luigi/netmap/; Stewart, R., & Tuexen, M. (2007-2026). *SCTP for FreeBSD*. sctp.freebsd.org; KAME Project. (1998-2006). *KAME Project Archive*. web.
- freebsd.duckdb（freebsd-src contributors 表，窗口 2010–2020，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<https://docs.freebsd.org/en/articles/contributing/>）［B］
    FreeBSD 社区论文与演讲 [329]. Christos Margiolis. Re-decentralizing the Internet with BSD [C]//EuroBSDcon 2025. [S.l.]: [s.n.], 2025. 获取路径：<https://papers.freebsd.org/2025/eurobsdcon/margiolis-re-de-centralizing-the-internet-with-bsd/>［B］>
- Linux Kernel. eBPF/XDP Documentation [EB/OL]；Rizzo L. netmap [A]. USENIX ATC 2012. ［B］

- OpenBSD. pf(4) Manual [Z]；DragonFly. Network Stack MPSAFE Notes [EB/OL]. ［B］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP111（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Cloudflare 为 netmap 引入单队列绑定能力：服务器型网卡的多队列中仅将一条队列直通用户态，其余照常进内核，只需在 netmap 接口名后附加队列号即可绑定；借此可将目的端口 53 的 UDP 流量导入用户态过滤层以拦截 DNS 放大攻击，再回注内核。讲解人指出 FreeBSD 尚无 Linux ethtool 那样的流导向工具，netmap 作者 Luigi Rizzo 已在 FreeBSD 邮件列表发帖呼吁开发同类工具，并进一步设想以 IPFW netmap 构建有状态过滤路径。（BSD Now EP111，[451.84-605.34]，L2）
- BSD Router Project 的 Olivier 发布长文实测 FreeBSD 高性能路由：在八核至强与万兆网卡平台上，routing 分支相比发布版显著抬升转发曲线；再禁用网卡随机数收割后，八队列下逼近每秒一千万包。接入 IPFW 或 PF 状态过滤后吞吐回落，但按互联网典型包长折算仍可达约 15 Gb/s，作者另发布 USB 镜像以供复现基准环境。（BSD Now EP111，[858.32-1134.26]，L2）
- 据当事人描述，美国医疗行业信息系统仍普遍以 Windows XP 与 Windows 2000 承载生产流程，小众业务软件因需求规模不足而长期失修；其所在机构以 OpenBSD 承载医疗后台的 EDI 理赔、药品与资格数据处理、数据库持久化、Web 应用与调度自动化，并认为该平台在性能与可管理性上足以胜任。（BSD Now EP111，[1847.66-2050.56]，L1）

**史料**：

- 本期一手史料包括：Brandon Mercer 关于 OpenBSD 医疗部署与 PandaBoard ARM 移植的当事人访谈；Olivier 的 BSD Router Project 基准博文及配套 USB 镜像；The Register 的 OpenBSD 5.7 邮件服务器三部曲教程与 UEFI 引导教程；netmap 作者 Luigi Rizzo 在 FreeBSD 邮件列表关于流导向工具的发言；OpenSMTPD 审计方在邮件列表与 OpenBSD Journal 的复盘；ACM 女性勇气大会开源职业面板录像与 Dan Langille 的首次贡献工作坊。 [存疑脚注] 转写人名失真：Giles Shahad 应为 OpenSMTPD 开发者 Gilles Chehade，Dan and Jill 应为 Dan Langille，Xenuous 应为 Xinuos，均据上下文与同期语境辨识，著录前须回查原链接核实（BSD Now EP111，[1240.94-3394.98]，L1）

**史观**：

- 总纲10 动手者创造历史：Mercer 从桌面支持自学起步，在几乎无内核与硬件经验的条件下靠阅读 boot blocks 代码与反复实验把 PandaBoard 带入 userland，期间经 Dale Rahn 邮件指点、社区统一 ARM 引导块的工作与 Peter Hessler 的 hackathon 邀请而获得开发者账号——BSD 开发者身份由动手实践与社区协作生成，而非科班晋升管道。（BSD Now EP111，[1610.92-1806.00]，L1）
- 总纲22 知识注定过时：当事人以一台七年未升级的生产安装自证版本冻结的实际代价，将长期支持比作“不清理的冰箱”（2127.62-2133.42），并以 Linux LTS 照旧高频打补丁的经历断言它只是“不愿写好软件者的假面具”（2266.06-2267.66）：升级冲击无法靠冻结版本消除，OpenBSD 的常规发布周期与快照跟踪反而是更可预期的演进方式。（BSD Now EP111，[2064.92-2198.16]，L1）

**辨析**：

- “OpenBSD 用于医疗行业”目前仅有 Mercer 单一当事人自述：涉事机构未具名，访谈只笼统提及后台敏感数据与 EDI 流程，未直接出现 HIPAA 表述；该案例与 HIPAA 合规法规语境之间尚缺文档级互证，采信前应视为单一来源推断。 [存疑脚注] 单一来源：机构匿名且无书面证据支撑，须以监管备案或行业案例文献交叉验证后方可提升证据等级（BSD Now EP111，[1956.47-2050.56]，L4）
- 学生问及开源项目为何仍用邮件列表与 IRC 而非 Slack，Dan Langille 的回答——若 Slack 更好，把它搭起来，新人自会用——将工具更迭交由可用性检验而非权威裁决；但讲解人旋即承认自己内部恰以 Slack 协作并看重其与 GitHub、Jenkins 的集成，显示社区通信形式的选择是多重实用权衡而非身份教条。（BSD Now EP111，[2787.92-2832.62]，L2）

**文献**：

- [BSD Now EP111] Pennington J. BSD Now: 111: Xenocratic Oath[EB/OL]. (2015-10-14)[2026-08-15]. <https://www.bsdnow.tv/111>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-307 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-307`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：讲者给出的最后一张图对比了 QUIC（转写音作 quick）与 TCP 搭配 TLS 1.2 或 TLS 1.3 的表现，QUIC 居中。（YouTube EPA2gmtkLMPf8，[2278-2286.87]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-308 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-308`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：讲者提到本年有 dummynet 相关支持落地 FreeBSD，并点名 Kristof Provost（转写音作 kristoff provost）完成了 v-net 支持。（YouTube EPA2gmtkLMPf8，[2360.88-2365.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-862 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-862`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：讲者推荐 FreeBSD 上一个好用的小工具（转写音作 packag gen），称它由 Luigi Rizzo 加入。（YouTube EPPxnmk_h7CyI，[1175.44-1181.43]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-861 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-861`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：加密框架 OCF（转写音作 ocf）源自 OpenBSD，NetBSD 与 FreeBSD 也都实现了它；John Mark Gurney（转写音作 gurnie）为 OCF 加入转写音作 asni 的指令支持（原句未明确指令集名）。（YouTube EPPxnmk_h7CyI，[2237.64-2253.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-300 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-300`；w172 YouTube 章节路由采纳）

据〔Netflix 400Gbps FreeBSD 演讲〕讲者 Drew Gallatin 口述：Mellanox ConnectX-6 Dx（转写音作 melon ox connect x6 dx）可卸载 TLS 1.2 与 1.3 的 AES-GCM，为其最常用密码。（YouTube EP_o-HcG8QxPc，[1141.36-1147.909]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-301 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-301`；w172 YouTube 章节路由采纳）

据〔Netflix 400Gbps FreeBSD 演讲〕讲者 Drew Gallatin 口述：KTLS 已向上游合入 FreeBSD。（YouTube EP_o-HcG8QxPc，[2423.28-2429.109]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-375 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-375`；w172 YouTube 章节路由采纳）

据〔netmap-fwd 演讲〕讲者口述：Netmap 可在 Linux、FreeBSD 与 Windows 上运行。（YouTube EPcAVgvzivzII，[129.819-138.173]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-374 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-374`；w172 YouTube 章节路由采纳）

据〔netmap-fwd 演讲〕讲者口述：在 FreeBSD 上使用 netmap-forward 可显著提升转发速率。（YouTube EPcAVgvzivzII，[893.956-898.305]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-725 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-725`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：NetMap 提供体积很小的 pcap 仿真库，只需替换动态库即可让使用 pcap 的应用直接运行于 NetMap 之上。（YouTube EPla5kzNhqhGs，[1145.6-1161.2]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-724 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-724`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：经改造后，其用户态实现使用标准 libpcap 可达约八十万包每秒，仅把 pcap 库换成 NetMap 即再提速四倍。（YouTube EPla5kzNhqhGs，[1355.5-1385.2]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-723 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-723`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：作为参照，free/vs（转写音作 free v s，非 Free vSwitch）深度桥接约七十万包每秒；改用 libpcap 仿真做接口间转发可达约七百五十万包每秒。（YouTube EPla5kzNhqhGs，[1319.8-1349.8]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-796 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-796`；w172 YouTube 章节路由采纳）

据〔AsiaBSDCon 2014 (P3B)〕讲者 Luigi Rizzo 口述：英特尔的 DPDK 设有两层 Netmap 兼容层，一层在 DPDK 之上模拟 Netmap，另一层在 Netmap 之上模拟 DPDK。（YouTube EPnW8iHgOL9y4，[903.4-919.4]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-797 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-797`；w172 YouTube 章节路由采纳）

据〔AsiaBSDCon 2014 (P3B)〕讲者 Luigi Rizzo 口述：其学生 Vincenzo Maffione 于二月做出该网络后端（转写音作 BI，转写未能辨明所指）在 Netmap 上的首个原型，讲者随后补上事件支持（转写音作 TQK，转写未能辨明所指）。（YouTube EPnW8iHgOL9y4，[927.7-965]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1155 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1155`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018〕讲者 Michio Honda 口述：PASTE 的 netmap 扩展最初在 Linux 上实现，如今正在移植到 FreeBSD（YouTube EPy_F-8HijfOA，[1476.32-1483.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1543 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1543`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Userland TCP Transport for NVME 演讲（John Baldwin）〕讲者口述：他为 FreeBSD 实现的 NVMe over Fabrics 已近期合入；该项工作他做了约一年半，本期讲其中的用户态实现部分。（YouTube EPjJn4N6AJ-9o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1544 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1544`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Userland TCP Transport for NVME 演讲（John Baldwin）〕讲者口述：他给库的中间层命名为传输抽象层，职责是把 TCP、RDMA 等具体传输的细节从库的使用者那里屏蔽掉，使用者只需面对发送命令、收到响应的抽象。（YouTube EPjJn4N6AJ-9o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1545 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1545`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Userland TCP Transport for NVME 演讲（John Baldwin）〕讲者口述：讲者称此前工作仍只留在 GitHub 分支上、内核部分尚未完成，如今已合入 FreeBSD 主干，距演讲约一个月，将进入 15.0，不会进入已发布的 14.1。（YouTube EPjJn4N6AJ-9o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1546 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1546`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Userland TCP Transport for NVME 演讲（John Baldwin）〕讲者口述：以用户态守护进程方式运行时，可创建并导出一个或多个命名空间，其底层存储可为磁盘上的普通文件、磁盘设备（如 ZFS）或内存盘——可造出合成 RAM 盘导出；讲者称此做法与 codal 的做法相似。（YouTube EPjJn4N6AJ-9o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2168 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2168`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Tuning FreeBSD for routing and firewalling 讲者 Olivier Cochard Labbe〕讲者口述：他介绍自己的转发性能基准测试办法——最少只需两台设备，一台用支持 netmap 的网络接口，另一台用 netmap 系列的报文注入工具发包，这些工具能以线速（line rate）数量级的报文压测被测设备。（YouTube EPSLlzep0IxVY，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2169 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2169`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Tuning FreeBSD for routing and firewalling 讲者 Olivier Cochard Labbe〕讲者口述：他在剖析转发性能时发现，FreeBSD 的随机数生成器会读取所有以太网报文并从中取若干字节，这略微拖累了转发性能；于是他要求随机数生成器不再使用这种采集方式，重新生成剖析数据，并在两套配置上全部硬件复测。（YouTube EPSLlzep0IxVY，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2170 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2170`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Tuning FreeBSD for routing and firewalling 讲者 Olivier Cochard Labbe〕讲者口述：他在对比 FreeBSD 的 ipfw 与 PF 状态机制时指出，两者行为相近，但 PF 对每个入向连接要消耗两个状态，因为它会为回程方向（return transition）额外创建一个第二个状态。（YouTube EPSLlzep0IxVY，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2171 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2171`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Tuning FreeBSD for routing and firewalling 讲者 Olivier Cochard Labbe〕讲者口述：他把 ipfw 随状态数增多而性能线性退化的结果发给 Yandex 的 Andrei Rusu，一周之后 Rusu 回了一个补丁，改用并发工具集（concurrency kit）来处理状态相关的问题。（YouTube EPSLlzep0IxVY，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2187 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2187`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Sam Gwydir 演讲 Improving netdump hardware support and performance with iflib〕讲者口述：截至 2018 年 6 月，Mark Johnson 已为 FreeBSD 的 netdump 加入 iflib 支持，使原先须逐个驱动实现的 netdump 能力可由 iflib 统一覆盖一批网络驱动。（YouTube EPFuNgy8Ag4DE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2188 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2188`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Sam Gwydir 演讲 Improving netdump hardware support and performance with iflib〕讲者口述：netdump 客户端代码运行于 panic 上下文，没有中断、不能做动态内存分配、也接不到常规 TCP/IP 协议栈，因此须改用预留内存段承载转储数据、并轮询网卡发送。（YouTube EPFuNgy8Ag4DE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2189 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2189`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Sam Gwydir 演讲 Improving netdump hardware support and performance with iflib〕讲者口述：性能改进前，两台虚拟机经 Dummynet 网关注送 2 GB 转储需约 9 秒（0% 丢包）；丢包率升至 0.1% 时延至 131 秒，1% 丢包即无法完成，故曾把重试次数上调到 100 才能测出结果。（YouTube EPFuNgy8Ag4DE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2190 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2190`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Sam Gwydir 演讲 Improving netdump hardware support and performance with iflib〕讲者口述：经网关转储的吞吐由 1773 兆比特每秒提升到 3022 兆比特每秒，约 1.7 倍，收益主要来自发送侧缓冲对小段的合并；抗丢包能力尚未改善，须待滑动窗口实现。（YouTube EPFuNgy8Ag4DE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2436 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2436`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Patrick M. Hausen，FreeBSD 会议线上演讲〕讲者口述：其托管产品建立在带 VIMAGE 特性的 FreeBSD jail 上，他把该特性描述为“完全虚拟化的网络栈”，使 jail 内可拥有私有接口、私有防火墙与“一切私有”，在单机上构成虚拟机的幻觉；并说相较 hypervisor，jail 的启动、销毁与供给都很轻快。（YouTube EPTqg2UH6Mvoc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2437 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2437`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Patrick M. Hausen〕讲者口述：这套 jail 桥接方案当时在 FreeBSD 12 上撞到性能上限，他们所用的 bridge 接口原先只有单线程、曾是瓶颈；他当场点名感谢 Christoph 把它改成多线程，使吞吐提升“一个数量级”，他记得是五倍甚至更多。（YouTube EPTqg2UH6Mvoc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2438 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2438`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Patrick M. Hausen〕讲者口述：他们遇到只在自家数据中心生产环境复现的故障——epair 接口与真实硬件网卡一样有收发队列，队列一旦被填满，该接口就停止转发；成因是 bridge 把广播包同时泛洪给桥上所有 epair；处置上有人告知可用一个文档不多的 sysctl 参数加大队列长度，他还说 epair 的整段重构是否已进源码树自己并不确定。（YouTube EPTqg2UH6Mvoc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2439 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2439`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Patrick M. Hausen〕讲者口述：他向 FreeBSD 开发社区提出可否提供“点对点”式的 VNET 接口——理由是 VNET 与 jail 本身已是完全虚拟化的环境，用以太网（ethernet）语义去仿真连接 jail 并无根本必要；若能得到一条与 epair 相当的点对点链路，就可以去掉 bridge、把一切放在三层路由上做。（YouTube EPTqg2UH6Mvoc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2440 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2440`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Zec 演讲：Network emulation using the virtualized network stack in FreeBSD〕讲者口述：网络栈虚拟化技术当时已并入 FreeBSD 主干（转写音作 main freebsd iii，按上下文疑指 -current），但仍被标记为实验特性，尚有若干已知缺陷。（YouTube EPwh09MirPd5Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2441 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2441`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Zec 同一演讲〕讲者口述：虚拟化网络栈的最早雏形是他本人在 2002 年“出于纯粹好奇”做的一个概念验证，做法是把与网络相关的全局变量集中搬进一个大结构体。（YouTube EPwh09MirPd5Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2442 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2442`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Zec 同一演讲〕讲者口述：在“虚拟化单个操作系统内核”这条路线上，他认为 FreeBSD 借 jails 率先开创，Solaris zones（转写音作 solari zones）与 Linux 的类似做法晚出；此系讲者当场口述的谱系判断，并非经源码与提交记录验证的技术结论。（YouTube EPwh09MirPd5Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2443 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2443`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marko Zec 同一演讲〕讲者口述：他用 FreeBSD 做网络仿真时更依赖 netgraph，并称 netgraph 是 FreeBSD 中用于任意操纵网络流量的子系统；他还说 FreeBSD 里的蓝牙相关内容重度依赖 netgraph。（YouTube EPwh09MirPd5Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2834 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2834`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08A: Improving netdump hardware support and performance with iflib（Sam Gwydir）讲者口述：讲者为解决无小分区场景下的 core dump 问题而系统考察各种做法，发现彼时 FreeBSD 二者皆无：既无简单做法，也无 netdump（转写音作 net them）。（YouTube EPbBLSvTQY7xw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2835 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2835`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08A: Improving netdump hardware support and performance with iflib（Sam Gwydir）讲者口述：早期 netdump 补丁太旧，须移植到 FreeBSD 11（转写音作 previously 11）才能跟上；Isilon 的 Mark Johnson 基于更新的补丁集放出一套补丁供讲者使用。（YouTube EPbBLSvTQY7xw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2836 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2836`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08A: Improving netdump hardware support and performance with iflib（Sam Gwydir）讲者口述：截至 2017 年 4 月，netdump 所支持的驱动数量有限，且每一种驱动都要单独编写支持代码。（YouTube EPbBLSvTQY7xw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2837 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2837`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P08A: Improving netdump hardware support and performance with iflib（Sam Gwydir）讲者口述：把既有驱动移植到 iflib 大致不难——iflib 的函数名与接口大体与既有驱动相对应、易于逐一对译；但文档不完整，讲者须与人协作才弄清，其中一度因某个函数缺失而白查约一至两周。（YouTube EPbBLSvTQY7xw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2933 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2933`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：ClickOS 一言以蔽之是极小的专用虚拟机（转写音作 tiny design based，疑为 MiniOS-based），其上运行 Click 模块化路由器软件；目标是既灵活又高性能的虚拟化软件平台。（YouTube EP0HDxmLaW9EU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2934 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2934`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：ClickOS 剔除常规操作系统的累赘，改用 MiniOS（转写音作 minoas）——单地址空间操作系统、无抢占式调度器、只跑在单核上且只跑单个应用（即 Click 模块化路由器），本质上是一台只为处理包而生的虚拟机。（YouTube EP0HDxmLaW9EU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2935 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2935`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：Xen 默认 I/O 路径的瓶颈实测：Open vSwitch（转写音作 opened the switch）单独转发不超过 30 万 pps，只留 netback 也不超过 35 万 pps，整条管线合起来对最大尺寸包只能转发 22.5 万 pps。（YouTube EP0HDxmLaW9EU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2936 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2936`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔会议不详〕讲者口述：优化之一：以 VALE 交换机（转写音作 valid switch／value switch）替换 Open vSwitch——它是两年前于 CoNEXT（转写音作 connex，存疑）推出的高速软件交换机，可在虚拟端口间转发 1800 万 pps；因其基于 netmap，还顺带免除了包元数据结构的开销。（YouTube EP0HDxmLaW9EU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3069 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3069`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2021 FreeBSD Developer Summit: IFLIB（NetApp 讲者 Sai）〕讲者口述：iflib 是 FreeBSD 所有网络驱动的框架，把驱动中大量样板代码集中到一处，使驱动只需处理或关注硬件本身。（YouTube EPOyHxs_EAc6A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3070 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3070`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2021 FreeBSD Developer Summit: IFLIB（NetApp 讲者 Sai）〕讲者口述：NetApp 原有驱动功能完备且稳定，服务了约六到七个版本；切到该 iflib 修订时只剩基本功能集，须额外追赶才能恢复特性与稳定性。（YouTube EPOyHxs_EAc6A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3071 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3071`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2021 FreeBSD Developer Summit: IFLIB（NetApp 讲者 Sai）〕讲者口述：采用 iflib 后，一项软件数据路径性能测试出现相对基线的巨大延迟尖峰；团队由此开始追查原因。（YouTube EPOyHxs_EAc6A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3072 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3072`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2021 FreeBSD Developer Summit: IFLIB（NetApp 讲者 Sai）〕讲者口述：改动后，从 if_transmit 入队到 iflib 完成 TX 回收，mbuf 生命周期落在 10–100 微秒，最迟约 1 毫秒。（YouTube EPOyHxs_EAc6A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3333 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3333`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Nanako Momiyama: IP Forwarding Fastpath - BSDCan 2017〕讲者口述：讲者称其转发快速路径补丁原为 FreeBSD 8 编写、已过于陈旧，故将原补丁移植进 FreeBSD 12，并以转写音作 Excel v lookup 的函数取代转写音作 IP found 的查找调用。（YouTube EPFigtcfcTGRI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3334 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3334`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Nanako Momiyama: IP Forwarding Fastpath - BSDCan 2017〕讲者口述：讲者称吞吐随转写音作 bad side 的增大而上升，在 256 或 512 处达到峰值后不再变化，其曲线形状与转写音作 MCS 论文中所展示的几乎相同。（YouTube EPFigtcfcTGRI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3335 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3335`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Nanako Momiyama: IP Forwarding Fastpath - BSDCan 2017〕讲者口述：讲者称新实现把 L2 输入与 L2 输出例程的开销削减了八成以上，并使 FreeBSD 的 IPv4 转发提速约 3.8 倍。（YouTube EPFigtcfcTGRI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3336 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3336`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Nanako Momiyama: IP Forwarding Fastpath - BSDCan 2017〕讲者口述：回答 IPv6 提问时，讲者称该实现只针对 IPv4：所提的数据包 I/O 方案即便对 IPv6 也能提升速率，但查找部分对 IPv6 并不高效。（YouTube EPFigtcfcTGRI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
