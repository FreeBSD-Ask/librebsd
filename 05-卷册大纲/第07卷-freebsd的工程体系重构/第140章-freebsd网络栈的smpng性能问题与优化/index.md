---
chapter: 第 140 章
id: CH140
volume: 07
---

## 要点

- SMPng（SMP Next Generation）项目始于 FreeBSD 5.0（2003 年 1 月），目标是将 FreeBSD 内核从传统的单 Giant 锁模型迁移到细粒度锁 SMP 架构；Giant 锁是一个全局内核互斥锁，早期 FreeBSD SMP 支持中所有内核操作都持有 Giant，导致多 CPU 时性能严重下降；网络子系统 SMP 化的核心挑战在于：① **mbuf(9)** 分配器需要 per-CPU 缓存；② 协议控制块（inpcb）需要独立锁而非全局锁；③ 网络接口输入/输出路径需要减少锁竞争；FreeBSD 5.x 采用了 “先粗粒度拆分，后逐步优化” 的策略——5.0-5.5 期间网络栈虽然引入了部分细粒度锁，但关键路径仍依赖 Giant 或存在严重锁竞争，导致在多 CPU 系统上网络性能相比 FreeBSD 4.x 出现显著倒退（部分测试显示倒退 30-50% 甚至更多）
- FreeBSD 5.x 网络性能倒退对用户群体产生了显著影响：① 许多 FreeBSD 4.x 生产用户拒绝升级到 5.x，继续停留在 4.x 系列直到 6.x 发布；② 防火墙/路由器用户（高度依赖网络性能）受影响最大，pfSense 等防火墙项目在 FreeBSD 5 时代曾面临是否升级的困境；③ 社区对 FreeBSD 项目产生了质疑——部分用户和开发者认为 5.x 在网络性能未就绪时不应标记为 STABLE；④ 这一事件直接导致 FreeBSD 发布工程团队调整发布策略——FreeBSD 6 开始更强调性能回归测试，且引入了 "one release for features, next for stabilization" 的模式
- FreeBSD 6.0（2005 年 11 月）引入了 Andre Oppermann 领导的重大网络栈重写和性能优化，核心改进包括：① 重写 TCP/IP 协议输入路径，减少锁竞争；② 引入 per-CPU 路由缓存，缓解 radix 锁竞争；③ 优化 mbuf 分配器，引入 UMA（Universal Memory Allocator）mbuf zone；④ 改进网络接口发送/接收路径的锁模型；⑤ 引入 TCP syncache 重写，提升 SYN flood 抵抗能力和性能；FreeBSD 6.x 系列（6.0、6.1、6.2、6.3）持续优化网络栈，到 FreeBSD 7.0（2008 年）时网络栈不仅恢复了 4.x 水平，而且在多 CPU 系统上实现了真正的 SMP 性能扩展；FreeBSD 7.0 还引入了 libpcap/bsd 改进的零拷贝 BPF（Berkeley Packet Filter）和 SCTP 支持
- SMPng 性能倒退事件的一手史料包括：FreeBSD SMPng 项目页面（2000-2006）、freebsd-current/freebsd-net/freebsd-stable 邮件列表档案、各版本 Release Notes、内核源码的锁定注释、Andre Oppermann 等人的 commit 日志；二手史料包括 Michael Lucas 的《Absolute FreeBSD》对 5.x 时代的描述、BSDCan 演讲；一个重要的历史背景：FreeBSD 5.x 不仅网络栈在 SMP 化，调度器、文件系统、VM 子系统都在经历 Giant 锁拆分——网络栈的性能倒退是整个内核 SMP 化阵痛的一部分，不是网络子系统的孤立问题。SMPng 网络栈性能倒退与恢复的关键节点汇总见下表。
- KTLS（Kernel TLS）是将 TLS 记录层加密/解密和封包/解包卸载到内核的框架，由 John Baldwin（约翰·鲍德温） 和 Netflix 团队开发，初始版本在 FreeBSD 12.0（2018 年）引入基础框架，在 FreeBSD 13.0（2021 年 4 月）完成完整的发送/接收和 TLS 1.3 支持；KTLS 的核心设计是零拷贝——TLS 记录层直接在 **mbuf(9)** 上进行加密/解密操作，避免用户态/内核态之间的数据拷贝；**sendfile(2)** 系统调用与 KTLS 深度集成——当从文件发送 TLS 加密数据时，文件页缓存中的页面可以直接加密发送，不需要拷贝到用户态；KTLS 支持将加密操作进一步卸载到支持 TLS 硬件加速的网卡（TLS offload），如 Chelsio T6/T7 和 NVIDIA ConnectX-6/7 系列网卡；KTLS 通过 **ktls(4)** 内核模块和 setsockopt 接口（`TCP_RXTLS` 和 `TCP_TXTLS` 选项）与用户态应用交互

## 史观

- 总纲第 17 条——软件工程：SMPng 期间的性能倒退是 “架构迁移成本” 的教科书案例——从单 Giant 锁到细粒度锁不可能一步完成，必须经历一个 “锁拆分但优化尚未到位” 的中间状态，这个状态的性能必然不如旧架构；FreeBSD 核心团队选择在 5.x 系列承受性能倒退以换取架构现代化，这是一个有争议但有远见的工程决策
  - 辨析：“FreeBSD 5.x 完全不能用” 是夸张说法——F
- 总纲第 3 条——形式主义膨胀：SMPng 阵痛是 “形式化过程必须经历不完美” 的体现——从单锁到细粒度锁是架构形式化的必然步骤，但这个步骤本身会暂时降低系统性能；历史书写必须避免 “后见之明”，不能因为最终成功就否定阵痛时期的困难
- 辨析：性能倒退百分比的准确数字——不同硬件配置、不同工作负载下倒退幅度差异巨大，单 CPU 几乎无倒退，4 路 SMP 高网络负载下可能倒退 50% 以上，网上
- 总纲第 2 条——实践先于理论：KTLS 不是一个 “研究项目”，而是 Netflix 为解决其 CDN 实际吞吐量问题而开发的生产级解决方案——Open Connect CDN 服务器需要向数百万用户提供 TLS 加密视频流，纯用户态 TLS 终止（如 nginx+OpenSSL）在 100Gbps 网卡上成为 CPU 瓶颈；这又是一个 “生产需求驱动内核创新” 的典范
  - 辨析：KTLS
- 总纲第 6 条——技术路线分化：KTLS 在两个系统上并行发展，说明这是行业共同需求——随着 TLS 成为互联网默认（TLS 1.3、Let's Encrypt 普及），内核 TLS 卸载从 “小众优化” 变成 “必需品”；但两个系统的实现细节差异体现了各自网络栈架构的不同
- 辨析：“Linux KTLS 比 FreeBSD 早 4 年”——技术上 Linux 4.13（2017）有初始框架，但
- 总纲第 23 条——社区治理：WireGuard 事件暴露了 FreeBSD 项目治理中的一个张力——商业赞助商对项目开发有重大影响，代码审查流程是否对商业赞助代码有足够的约束力？这个问题没有简单答案，但事件后 FreeBSD 确实调整了安全敏感代码（如加密协议）的审查流程
  - 辨析：“丑闻” 一词是否准确——事件中没有发现后门或恶意代码，核心问题是代码质量和审查流程，“丑闻” 是媒体和社区的

## 辨析

- “FreeBSD 5.x 完全不能用” 是夸张说法——FreeBSD 5.x 在单 CPU 系统上性能与 4.x 接近，倒退主要发生在多 CPU 系统和高网络负载场景；锁竞争的主要来源：① 路由表锁（radix 锁）竞争；②inpcb（协议控制块）全局锁竞争；③ 网络接口 TX/RX 路径锁；Andre Oppermann 在 FreeBSD 6 周期的优化主要针对这些热点；部分网络文章称 “Fr
- 性能倒退百分比的准确数字——不同硬件配置、不同工作负载下倒退幅度差异巨大，单 CPU 几乎无倒退，4 路 SMP 高网络负载下可能倒退 50% 以上，网上常说的 “50% 倒退” 是特定测试场景数字，不是普遍情况；“FreeBSD 5.0 是失败的版本”——从工程角度看 5.0 是技术预览版，向 SMP 架构迁移的必要步骤，但项目在版本命名和用户预期管理上存在不足；FreeBSD 5.x 持续了约
- KTLS 引入版本——基础框架在 FreeBSD 12.0（2018）但只支持发送方向且功能有限，完整的双向 TLS 1.2/1.3 支持和硬件 offload 在 FreeBSD 13.0（2021）完成；KTLS 不是 “绕过加密”——它只是把记录层操作移到内核，加密本身仍使用相同的密码套件（AES-GCM、ChaCha20-Poly1305 等），安全性不变；Netflix 800 Gbps
- “Linux KTLS 比 FreeBSD 早 4 年”——技术上 Linux 4.13（2017）有初始框架，但生产可用的完整支持（包括 sendfile 零拷贝、TLS 1.3、硬件 offload）两者时间相近（2019-2021）；Nginx 在两个平台上都支持 KTLS，但是配置方式不同；KTLS 是否会取代用户态 TLS（如 OpenSSL）——不会完全取代——用户态 TLS 仍有灵活
- “丑闻” 一词是否准确——事件中没有发现后门或恶意代码，核心问题是代码质量和审查流程，“丑闻” 是媒体和社区的修辞，实际是工程流程争议；Matt Macy 的代码是否 “完全不合格”——代码可以运行，但存在多个安全和协议一致性问题，需要修复；Netgate 的角色——Netgate 赞助开发本身没有错，争议在于代码合并过程中社区审查不足；部分描述称 “未经任何审查”，这不准确——代码确实经过了 c

## 文献

- FreeBSD Project. *SMPng Project Documentation*. freebsd.org/smp; McKusick, M. K., Neville-Neil, G. V., & Watson, R. N. M. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.), Chapter 4; Oppermann, A. (2004-2006). *Network Stack Locking and Performance Posts*. freebsd-ne
- Internet Archive. *FreeBSD SMPng Project Pages* (2003-2006 snapshots). web.archive.org; Lucas, M. W. (2007). *Absolute FreeBSD* (2nd ed.). No Starch Press; FreeBSD Project. *Release Notes for FreeBSD 5.0 through 7.0*. freebsd.org.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始
- FreeBSD Project. *ktls(4) Manual Page*; Baldwin, J. (2019). *Kernel TLS offload*. BSDCan '19; Netflix Technology Blog. (2018-2022). *KTLS and Open Connect CDN Posts*. netflixtechblog.com; FreeBSD Project. (2021-04). *FreeBSD 13.0 Release Notes* (KTLS section). freebsd.org. ［C］
    FreeBSD 社区论文与演讲 [3
- Linux Kernel Documentation. *Kernel TLS (kTLS)*. kernel.org; Watson, D. (2017). *Linux kTLS Patches*. lkml.org; Baldwin, J. (2019). *Cross-Platform KTLS Comparison*. freebsd-net@; Chelsio Communications. (2020-2026). *TLS Offload Documentation*. chelsio.com. ［A］
    FreeBSD 社区论文与演讲 [313]，[313] Mateu
- FreeBSD Project. *if_wg(4) Initial Commit*. cgit.freebsd.org (2020-11); Netgate Inc. (2020-2021). *WireGuard for FreeBSD Statements*. netgate.com; Donenfeld, J. A. (2020-12). *WireGuard for FreeBSD Review*. <freebsd-net@freebsd.org> mailing list. ［A］

## 139.7.2 Donenfeld 批评与从头重构过程

- 要点：2020 年 12 月
- FreeBSD Net Mailing List Archives. (2020-11 to 2021-06). *WireGuard Implementation Thread*[Z/OL]. freebsd.org. 获取路径：<https://lists.freebsd.org/archives/freebsd-net/> [访问日期 2026-07-30]; FreeBSD Project. *wg(4) and if_wg(4) Commit History*[Z/OL]. cgit.freebsd.org. 获取路径：<<https://cgit.freebsd.org/src/lo>

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP55（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Adrian Chadd 自述 FreeBSD 无线栈在 AP 与 station 模式下工作良好，但仅有两名左右开发者，边界情况缺乏人手。（BSD Now EP55，[1419.88-1458.76]，L1）
- Atheros 与 Intel 因开放源码与文档而成为 FreeBSD 无线的主要方向；Broadcom 与 Marvell 在 Sam Leffler 离开后未再更新，成为明显短板。（BSD Now EP55，[1462.00-1544.32]，L1）
- Adrian Chadd 恢复因监管顾虑而停用的 monitor mode 注入，使 Kismet 与 Aircrack-NG 重新可用，同时承受实现监管域强制的压力。（BSD Now EP55，[1777.56-1881.62]，L1）
- OpenBSD 的 systemd 兼容层仅为 hostnamed、localed、timedated、logind 的 shim，以让 GNOME 运行，并非移植 systemd 本体或替换 init。（BSD Now EP55，[3493.32-3567.32]，L2）

**史料**：

- Adrian Chadd 访谈（FreeBSD 无线网络栈维护者当事人自述）。（BSD Now EP55，[1267.26-2874.88]，L1）

**史观**：

- 总纲20 历史地理塑造思想土壤：总纲20 历史地理塑造思想土壤：无线厂商是否开放文档、是否以 Linux 为主场，直接塑造了 FreeBSD 无线栈的可行范围。（BSD Now EP55，[1462.00-1603.66]，L1）
- 总纲9 经验优先：总纲9 经验优先：Adrian Chadd 以驱动开发与真机测试的一线经验陈述无线栈优劣，而非依赖纸面规格。（BSD Now EP55，[1419.88-1447.00]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：各 BSD 共享 net80211 后各自分化，DragonFly BSD 又聚合 FreeBSD 更新栈，构成反复的分合。（BSD Now EP55，[1657.66-1722.12]，L1）

**辨析**：

- 转录将 Ralink/Realtek 与 Atheros 的表述交错，主持人与嘉宾均存在口误修正，具体芯片归属需对照 FreeBSD 源码。　[存疑脚注] 无线芯片厂商归属存在口语转写歧义，未以代码仓库核验（BSD Now EP55，[1486.52-1493.84]，L4）

**文献**：

- [BSD Now EP55] Pennington J. BSD Now: 55: The Promised WLAN[EB/OL]. (2014-09-17)[2026-08-15]. https://www.bsdnow.tv/55.

<!-- /PODCAST_REVIEW -->
