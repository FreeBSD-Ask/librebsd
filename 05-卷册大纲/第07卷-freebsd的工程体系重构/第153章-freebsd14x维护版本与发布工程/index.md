---
chapter: 第 153 章
id: CH153
volume: 07
---

## 要点

- FreeBSD 14.1-RELEASE 于 **2024 年 6 月 4 日** 发布，是 stable/14 分支第二个版本，Release Engineer 为 Colin Percival；核心亮点：① C 库在 amd64 上增加 SIMD 实现的字符串/内存操作函数（memcpy、strlen、memset 等），性能提升明显；② 音效子系统改进，包括设备热插拔支持；③ 初始 native cloud-init（config drive）支持，兼容 OpenStack 与众多云服务商；④ OpenZFS 升级至 2.2.4（bug 修复与稳定性）；⑤ Clang/LLVM 升级至 18.1.5；⑥ OpenSSH 升级至 9.7p1；14.0-RELEASE 支持周期至 2024.9.30（14.1 发布后三个月）；14.1 支持架构：amd64、i386、powerpc、powerpc64、powerpc64le、powerpcspe、armv7、aarch64、riscv64（与 14.0 相同）
- FreeBSD 14.2-RELEASE 于 **2024 年 12 月 3 日** 发布，是 stable/14 分支第三个版本，Release Engineer 为 Colin Percival；**献词纪念 Mike Karels**——他是《The Design and Implementation of the 4.3BSD UNIX Operating System》等 BSD 经典著作的合著者、4.3BSD/4.4BSD 核心开发者、在 BSD 社区贡献超过 40 年，当时担任 Deputy Release Engineering Lead，于 2024 年 10 月去世；核心亮点：① OCI 容器镜像正式可用（从 14.2 开始发布官方 OCI 镜像）；② 安装程序支持在安装 base 后自动下载安装必要固件包；③ OpenZFS 升级至 2.2.6；④ OpenSSL 升级至 3.0.15；⑤ 新增 Oracle Cloud Infrastructure（OCI）官方支持（amd64 与 aarch64，UFS 与 ZFS 镜像）；14.2 支持架构从 14.0/14.1 的 9 个缩减为 7 个——**powerpc64le 与 powerpcspe 不再提供 RELEASE 镜像**；14.1 EOL 为 2025.3.31，14.2 支持至 2025.9.30；发布工程团队在 Mike Karels 去世后由 Ed Maste（埃德·马斯特） 接任 Deputy Lead，新增 Dave Cottlehuber、John Hixson、Mahdi Mokhtari、Muhammad Moinur Rahman 等成员，Glen Barber（格伦·巴伯）（gjb@，14.0 Deputy Lead）未出现在 14.2 re@ 名单中
- FreeBSD 14.3-RELEASE 于 **2025 年 6 月 10 日** 发布，是 stable/14 分支第四个版本，Release Engineer 为 Colin Percival；核心亮点：① **iwlwifi 驱动支持 802.11ac（WiFi 5）**——这是 FreeBSD WiFi 支持的重要里程碑，现代 Intel WiFi 芯片首次在 FreeBSD 上可用 802.11ac；② OCI 容器镜像正式发布至 Docker Hub 与 GitHub Container Registry；③ Clang/LLVM 升级至 19.1.7；④ OpenSSH 升级至 9.9p2；⑤ xz 升级至 5.8.1（xz-utils 后门事件后版本，5.6.x 系列含后门，FreeBSD 13.x/14.x 中未使用受影响版本但仍跟进更新）；⑥ expat 升级至 2.7.1；14.3 支持至 2026.6.30，14.2 EOL 为 2025.9.30；xz 后门事件（CVE-2024-3094，2024.3 发现）影响的是 xz 5.6.0-5.6.1，FreeBSD 14.x 使用较旧的 xz 版本，未受该后门直接影响
- FreeBSD 14.4-RELEASE 于 **2026 年 3 月 10 日** 发布，是 stable/14 分支第五个版本（截至 2026.7，14.5 在开发中），Release Engineer 为 Colin Percival；**献词纪念 Ken Smith**——他曾担任 FreeBSD Release Engineering Lead 长达 7 年（负责 FreeBSD 6 至 FreeBSD 10 的发布工程），于 2025 年底去世；核心亮点：① **OpenSSH 10.0p2 默认启用混合后量子密钥交换算法 mlkem768x25519-sha256**——这是 FreeBSD 首次默认启用抗量子计算密码学算法；② OpenZFS 升级至 2.2.9；③ nuageinit（FreeBSD 原生 cloud-init 实现）的 cloud-init 兼容性显著改进；④ bhyve 通过新的 **p9fs(4)** 支持 host-guest 文件系统共享（Plan 9 协议）；⑤ 手册页工具与内容的显著改进；14.4 是 re@ 团队变动最大的版本——新增 Sergio Carlavilla Delgado、Jake Freeland、Craig Leres、Vladlen Popolitov、Lexi Winter、Alexander Ziaee 等新成员，Konstantin Belousov（康斯坦丁·别洛乌索夫）、John Hixson、Doug Rabson（道格·拉布森）、Mahdi Mokhtari 等未再出现在名单中，Antoine Brodin 仍负责 Package Building、Ed Maste 任 Deputy Lead；14.4 支持至 2026.12.31，14.3 EOL 为 2026.6.30；Open Sats Initiative 新增进入赞助商名单
- stable/14 分支支持至 **2028 年 11 月 30 日**（约 5 年支持周期，自 2023.11 起），截至 2026.7 已发布 14.0-14.4 共 5 个 RELEASE 版本，14.5 在开发中；整个 14.x 周期的更新节奏体现了 FreeBSD 发布工程的成熟：约每 6 个月一个 .RELEASE（14.0:2023.11、14.1:2024.6、14.2:2024.12、14.3:2025.6、14.4:2026.3——整体接近 6 个月周期）；Colin Percival 自 FreeBSD 13.x 起担任 Release Engineering Lead，是 FreeBSD 历史上担任 re@ Lead 时间较长的成员之一；14.x 周期内 re@ 团队经历了 Glen Barber 离开、Mike Karels 去世等人事变动，但发布节奏基本保持稳定；14.x 也是最后一个包含 32 位 i386 RELEASE 镜像的稳定分支，15.0（2025 年底/2026 初发布）将只发布 64 位架构 RELEASE

## 史观

- 总纲第 17 条——软件工程：.1 维护版本的定位是“稳定性、bug 修复、小功能增强”而非大的架构变更——SIMD string 函数、音效热插拔、cloud-init 支持都是不破坏 ABI 的渐进改进；这种“大版本创新 + 小版本稳定”的发布节奏是 FreeBSD 工程可靠性的基础
  - 辨析：libc SIMD 优化最初由 David C Lawrence（tale@）与其他贡献者开发，
- 总纲第 22 条——开源运动：此漏洞是典型的 “UNIX 工具组合哲学” 安全缺陷——rtsold 作为网络配置守护进程调用 resolvconf shell 脚本更新 DNS 配置，而 shell 脚本的字符串拼接与引号处理是传统 UNIX 工具中常见的安全隐患；这一漏洞提醒我们：即使是设计简洁、代码量小的 BSD 系统，在不同组件的交互边界仍可能出现严重安全问题；与 C 语言内存漏洞不同，sh
- 总纲第 23 条——社区治理：FreeBSD Core Team 选举制度是开源社区 “代议民主” 治理模式的典范——9 名核心成员由 committer 民主选举产生，任期两年，可连任；这一制度既避免了 BDFL（仁慈独裁者）模式的个人依赖风险，也避免了完全开放投票的民粹化倾向（只有具有代码提交记录的活跃开发者才有投票权）；Core Team 权力受项目章程约束，具体技术决策交由各领域团队（re

## 辨析

- libc SIMD 优化最初由 David C Lawrence（tale@）与其他贡献者开发，针对现代 x86-64 处理器的 SSE/AVX 指令集优化；这些优化在微基准测试中显著提升字符串操作性能（某些场景达数倍），对真实工作负载的影响因应用而异；音效热插拔改进解决了 USB 音频设备在系统运行中插入/拔出时的稳定性问题。**数据库验证结论**：`release/14.1.0` tagger
- 漏洞影响范围需精确说明：仅运行 rtsold/rtsol 且接口启用 ACCEPT_RTADV 的系统受影响；不使用 IPv6 或静态配置 IPv6 的系统不受影响；RA 报文是二层本地网段报文，路由器不应转发 RA 报文（否则违反 IPv6 规范），因此攻击无法跨越路由器实施远程攻击——这限制了漏洞的实际危害范围，但同一网络段（如公共 WiFi、企业局域网）的攻击者仍可利用；14.3-RELEA
- Hiroki Sato（hrs@）在 FreeBSD 社区地位崇高——他是文档项目负责人、亚洲 BSD 社区（特别是日本 BSD 用户组）的核心组织者、担任 Core Team 成员多年；原 ch85 草稿称他于 2022 年逝世且 13.1-RELEASE 献词给他，**经核实 13.1-RELEASE 实际献词给 Bill Jolitz**（386BSD 共同创建者），而非 Hiroki Sa

## 文献

- FreeBSD Project. FreeBSD 14.1-RELEASE Announcement [EB/OL]. (2024-06-04)[2026-07-19]. <https://www.freebsd.org/releases/14.1R/announce/>; FreeBSD Project. release/14.1.0. freebsd-src 仓库 tag [DB/OL]. 2024-05-30T17:34:21-07:00. tag: release/14.1.0; commit: 10e31f0946d820d53adc58b7d013b969e4a9a8ed ［A］

- FreeBSD Security Team. FreeBSD-SA-25:12.rtsold — Remote Code Execution via ND6 Router Advertisements [EB/OL]. (2025-12-16)[2026-07-19]. <https://security.FreeBSD.org/advisories/FreeBSD-SA-25:12.rtsold.asc>; MITRE. CVE-2025-14558 [EB/OL]. (2025-12)[2026-07-19]. <<https://cve.mitre.org/cgi-bin/cvename>.
- FreeBSD Project. FreeBSD Administration and Management [EB/OL]. [2026-07-19]. <https://www.freebsd.org/administration/>; FreeBSD Core Team. Core Team Charter [EB/OL]. [2026-07-19]. <https://www.freebsd.org/internal/core-charter/>（原始链接失效，互联网档案馆无存档）. ［A］

## 152.12.2 Security Officer 任期与安全团队演进

- 要点：截

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP580（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Colin Percival 自述 FreeBSD 发布工程长期处于由发布工程师即兴决定的临时状态，他接任后引入按季度排布、覆盖未来五年的发布日历，使 minor 版本节奏可预期。（BSD Now EP580，[476.24-547.40]，L1）
- Colin 将 FreeBSD 主版本支持期由五年缩减为四年，以对齐每两年一次的主版本节奏，避免同时维护三个稳定分支带来的上游 OpenSSL、编译器与 ports 兼容负担。（BSD Now EP580，[630.52-756.16]，L1）
- Colin 回顾 freebsd-update 工具源于 2003 年他为简化系统补丁更新而编写，并为此创造了 bsdiff 二进制差分工具，后者后来被广泛用于各处的增量更新。（BSD Now EP580，[210.06-229.42]，L1）
- Andrew Hewus 自述约 2003 年在亚利桑那州一家小型 ISP 从 OpenBSD 3.5 或 3.6 开始，将 DNS、邮件与路由逐步替换为 OpenBSD，后经邮件列表接手 OpenBSD 基础系统中的 Perl 维护。（BSD Now EP580，[1455.12-1565.32]，L1）
- Liam Proven 梳理商业 Unix 的当代存续：Xinuos 继承 SCO 的 Xenix 与 UnixWare 业务并提供基于 FreeBSD 的清理版本；AIX 开发团队迁往印度；Solaris 不再出新版本但仍获安全修复；illumos 与 Oxide Computer 延续 OpenSolaris 谱系。（BSD Now EP580，[2915.18-3022.62]，L2）
- Liam Proven 以其亲历的 FreeBSD 13 升级 14 后桌面环境损坏为例，指出 BSD 桌面在升级平滑度与新手进入门槛上的短板，并批评 systemd 及其安全启动方向正在收窄用户对系统的控制。（BSD Now EP580，[3043.30-3344.86]，L1）

**史料**：

- 本期为 EuroBSDcon 2024 现场采访；Colin Percival 与 Andrew Hewus 为一手自述，Liam Proven 为 The Register 记者的一手见闻与二手综述。（BSD Now EP580，[59.28-1293.58]，L1）

**史观**：

- 总纲10 动手者创造历史：Colin 因自身补丁更新需求编写 freebsd-update 与 bsdiff，其工具后来成为 FreeBSD 更新基础设施的一部分，体现动手者为解决具体问题而塑造系统历史。（BSD Now EP580，[210.06-229.42]，L1）
- 总纲3 不存在进步，只有权力再分配：FreeBSD 发布工程从即兴决策到日历化、支持期从五年缩为四年的过程，是工程与治理权力在项目内部的重新配置。（BSD Now EP580，[630.52-756.16]，L1）
- 总纲21 革命与改革是历史方法论的分歧：Liam 对 systemd 与安全启动方向的批评，呈现开源生态中激进变革与保守续存两种方法论之间的持续张力。（BSD Now EP580，[3043.30-3164.96]，L2）

**辨析**：

- Liam Proven 关于 Xinuos 产品形态、AIX 团队迁移地等描述属记者二手综述，具体时点与细节须以厂商公告核实。　[存疑脚注] 商业 Unix 厂商现状为记者综述，未逐一核对厂商一手公告。（BSD Now EP580，[2915.18-3022.62]，L4）
- FreeBSD 桌面升级损坏为 Liam Proven 的个案经验，不能据以推断该升级路径具有普遍失败率。　[存疑脚注] 桌面升级问题为单一用户个案经验，未经系统复现或统计验证。（BSD Now EP580，[3252.54-3318.12]，L4）

**文献**：

- [BSD Now EP580] Pennington J. BSD Now: 580: EuroBSDcon 2024 - Part 2[EB/OL]. (2024-10-10)[2026-08-15]. https://www.bsdnow.tv/580.

<!-- /PODCAST_REVIEW -->
