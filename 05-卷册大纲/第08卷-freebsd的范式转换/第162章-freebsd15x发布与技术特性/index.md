---
chapter: 第 162 章
id: CH162
volume: 第08卷-freebsd的范式转换
---

# 第162章 FreeBSD 15.0 发布与技术特性

## 史料

- [DB:research_notes:blocks:5350] 关键词“技术特性”命中：史实考据：Sun Microsystems 于 2005 年 11 月随 OpenSolaris build 27 以 …
- [DB:research_notes:blocks:5352] 关键词“技术特性”命中：史实考据：John Birrell 于 2008 年 12 月 3 日在 freebsd-current 邮件列表发布 …
- [DB:research_notes:blocks:5354] 关键词“技术特性”命中：史实考据：Robert N. M. Watson 与 Jonathan Anderson 主导的 Capsicum 论文…

- [WEB:freebsd.org/releases/15.0R/announce/] FreeBSD 15.0-RELEASE Announcement（官方一手，2025-12-02 发布）：pkgbase 打包 base 系统（技术预览，16 计划成为标准并移除 distribution sets/freebsd-update）；发行构件无需 root 生成；原生 inotify 实现；OpenZFS 2.4.0-rc4；OpenSSL 3.5.4 LTS（QUIC + ML-KEM/ML-DSA/SLH-DSA 后量子算法）；OpenSSH 10.0p2（默认后量子密钥交换）；MIT Kerberos 1.22.1 替代 Heimdal；amd64 LA57 支持 4TB+ 内存；32 位平台 i386/armv6/32-bit powerpc 退役（armv7 为最后 32 位平台）；OCI 容器镜像与 Oracle Cloud 镜像发布；EC2 启动较 14.0 快 76%；可复现构建（reproducible builds）里程碑

## 要点

- FreeBSD 15.0-RELEASE 于 **2025 年 12 月 2 日** 由 Release Engineering Team 正式发布（Release Engineer 为 Colin Percival），是 stable/15 分支的首个版本；15.0 是 FreeBSD 历史上首个 **不为 i386、armv6、32 位 powerpc 提供 RELEASE 安装镜像** 的大版本，标志着 FreeBSD 正式进入 64 位纯净时代；15.0 开发周期自 14.0 于 2023 年 11 月发布后历时约两年，集成了大量基础设施改进；15.0 支持架构为 **amd64、aarch64、armv7、powerpc64、powerpc64le、riscv64**（armv7 为最后保留的 32 位 Tier 2 平台）；15.0 的一项里程碑式工程成就是：**所有发布制品（安装镜像、VM 镜像等）均无需 root 权限构建**，这为可重现构建与 CI/CD 现代化奠定了基础；15.0-RELEASE 将支持至 **2026 年 9 月 30 日**，整个 15.x 稳定分支将支持至 **2029 年 12 月 31 日**
- 15.0 带来的核心技术变更包括但不限于：① **pkgbase（打包基本系统）** 作为技术预览引入——基本系统可通过 **pkg(8)** 软件包管理器安装与管理，**bsdinstall(8)** 提供 “Distribution Sets（传统方式）” 与 “Packages（pkgbase 新方式）” 两种安装选项，传统方式计划在 16.0 移除，pkgbase 是 VM 镜像与公有云镜像的默认方式；② **原生 inotify(7) 实现**——不再依赖 Linux 兼容层的 inotify 模拟，原生实现简化了 Linux 桌面应用移植与目录监控；③ OpenZFS 升级至 **2.4.0-rc4**（含 RAIDZ expansion 在线扩容、vdev initialization、fast dedup、zstd 快压缩改进、contiguous dirty dnodes 等长期需求特性）；④ OpenSSL 升级至 **3.5.4 LTS**——支持 QUIC 协议与已标准化的后量子算法（ML-KEM、ML-DSA、SLH-DSA）；⑤ OpenSSH 升级至 **10.0p2**——**默认启用后量子密钥交换**（ML-KEM-512 混合密钥交换），这是主流 OS 中首批默认启用抗量子计算密钥交换的系统之一；⑥ 默认工具链 Clang/LLVM 升级至 **19.x**（15.1 将跟进至更高版本）；⑦ 所有平台（包括 32 位兼容层）完成 **64-bit time_t** 转换，彻底解决 Y2038 问题；⑧ LinuxKPI（Linux Kernel API 兼容层）大幅改进，对齐 Linux 6.x API，以支持从 Linux 移植的现代 GPU 驱动（drm-kmod）与 WiFi 驱动（iwlwifi/rtw88/rtw89）；⑨ KTLS（内核 TLS）TLS 1.3 发送/接收双向卸载默认完善；⑩ **pf(4)** 防火墙改进（syncookie 默认、dummynet 集成等）；⑪ bhyve 虚拟化改进（Intel AMX 支持、更多设备模拟、**p9fs(4)** Plan 9 文件系统共享在 15.1 完善）；⑫ **makefs(8)** 成熟支持 ZFS 镜像无需 root 构建；⑬ **fwget(8)**/**fwctl(8)** 固件管理框架完善；⑭ Linux 兼容层（Linuxulator）改进，支持 Ubuntu 24.04/Debian 12 用户态，Wine/Proton 兼容性持续提升
- 15.0 中 LinuxKPI（Linux Kernel Programming Interface 兼容层）的大幅改进是 FreeBSD 硬件支持战略的关键转向——通过提供与 Linux 内核 API 兼容的头文件与封装层，FreeBSD 可以相对低成本地移植 Linux 中的现代硬件驱动；15.0/15.1 中基于 LinuxKPI 的驱动包括：① **WiFi 驱动**：**iwlwifi(4)**（Intel WiFi 6/6E）、**rtw88(4)**（Realtek 802.11ac）、**rtw89(4)**（Realtek WiFi 6）、**mt76(4)**（MediaTek WiFi 6）——15.1 中这些驱动已升级至基于 **Linux 7.0** 内核版本；② **GPU 驱动**：drm-kmod 系列包括基于 Linux 5.15 LTS 的 drm-515-kmod 与基于 Linux 6.1 LTS 的 drm-61-kmod，支持 Intel i915（12 代/13 代/14 代核显）、AMD AMDGPU（RDNA 2/RDNA 3 显卡）；③ **网络驱动**：部分现代 10G/25G/100G 网卡驱动通过 LinuxKPI 移植；LinuxKPI 战略使 FreeBSD 能够利用 Linux 生态中庞大的驱动开发资源，而不必为每款新硬件从零编写驱动——这是 FreeBSD 在 Linux 主导硬件驱动生态时代的务实工程选择
- 相较 14.4-RELEASE（2026.3；14.5-RELEASE 已于 2026-09-08 发布，14.x 分支至此收官），15.0 的核心演进方向可归纳为 “基本系统软件包管理化、64 位平台纯净化、加密后量子化、硬件支持 LinuxKPI 化、构建流程现代化” 五大主题；15.0 发布工程团队由 Colin Percival（Release Engineering Lead，15.0/15.1 Release Engineer）、Ed Maste（埃德·马斯特）（Deputy Lead）、Antoine Brodin（Package Building）、Lexi Winter（pkgbase wrangler）、Xin Li（Security Team Liaison）等组成；15.0 发布前经历了多个 ALPHA/BETA/RC 迭代周期；15.0 发布时同期操作系统生态为：Linux 6.12 LTS（2024.11，sched_ext BPF 调度器）、Linux 6.14（2025.3，Rust for Linux 标记可用于新驱动）、Windows 11 24H2、Windows Server 2025、macOS 15 Sequoia（2024.9）、macOS 26 Tahoe（2025.9；苹果自 2025 年起将版本号统一为 26）、OpenBSD 7.7（2025.4）、OpenBSD 7.8（2025.10，修复 27 年 TCP SACK 漏洞）［ 注：依 OpenBSD 半年发布节奏，2026.4 预估已出 7.9，成书前宜复核最新稳定版 ］、NetBSD 10.1（2024.12，现行稳定版）、NetBSD 11.0（截至 2026.7 处于 RC6 阶段未发布）、DragonFly BSD 6.4+
- FreeBSD 15.1-RELEASE 于 **2026 年 6 月 16 日** 由 Release Engineering Team 正式发布，是 stable/15 分支的第二个版本；15.1 献词给 **Peter G. Neumann**——长期与 FreeBSD 开发者在 capability-based security 领域合作的计算机安全先驱，Multics 项目的贡献者，现代 OS 安全中许多核心概念（最小权限、能力系统、形式化验证）的奠基人；15.1-RELEASE 将支持至 **2027 年 3 月 31 日**

## 史观

- 总纲第 1 条——一切真历史都是古代史：15.0 是 FreeBSD 历史上的关键一刻——它终结了自 1993 年 1.0 以来持续 32 年的 32 位 x86（i386）平台 RELEASE 构建传统；从 386BSD 补丁包中诞生的 FreeBSD，在 32 位 x86 上运行了整整一代人的时间后，正式将 i386 送入历史；这一刻不是 “抛弃传统”，而是承认硬件现实——AMD Opteron 于 2003 年发布后 amd64（x86-64）逐步成为服务器与桌面主流架构，i386 的边缘化是此后二十余年的长期趋势，FreeBSD 直至 15.0 才终止其 RELEASE 镜像，是对既有用户群长期承诺兑现之后的自然谢幕
- 专题语（不设总纲条号）——工程范式转型：pkgbase 的引入是 FreeBSD 基本系统软件包管理范式的根本转变——自 1993 年以来，FreeBSD 基本系统一直通过 “distribution sets”（tar 分发软件包）与 **freebsd-update(8)** 管理，pkgbase 将基本系统与第三方软件包统一到同一个软件包管理框架下；这是 ports/pkg 体系成熟以来 FreeBSD 用户态管理的最大结构性变革，为二进制更新、容器镜像与 CI 流水线提供了统一底座
- 总纲第 6 条——和解优于斗争：LinuxKPI 战略不是 “屈服于 Linux” 或 “变成 Linux”，而是在承认 Linux 已成为硬件驱动事实标准生态的前提下，保持 FreeBSD 内核独立性与 BSD 哲学的工程智慧；这与 **netlink(4)** 在 14.0 引入（兼容 Linux 网络配置协议）属于同一思路——不重新发明轮子，在非核心差异化领域兼容生态事实标准，将有限的开发者资源集中于内核核心与真正的差异化领域
- 总纲第 4 条——分离聚合是永恒规律：15.0 对 14.x 呈现延续与分离并存——稳定的 API/ABI 兼容性承诺（5 年支持周期至 2029.12）、lib32 对 32 位应用程序的运行时兼容、Jail/bhyve/ZFS/pf 等核心子系统的持续演进、BSD 许可证与 FreeBSD 开发模式的坚持，是聚合的一面；i386/armv6/powerpc RELEASE 镜像的终止与传统 distribution sets 的退出路径（16.0 移除），则是分离的一面
- 总纲第 10 条——动手者创造历史：Peter G. Neumann 从未是 FreeBSD 的核心 committer，但他在 capability-based security 领域数十年的理论工作（从 1960 年代 Multics 到 2000 年代 Capsicum）为 FreeBSD 的能力机制与安全设计提供了理论根基，15.1 的献词是对这类“边缘”理论贡献者影响力的承认

## 辨析

- **重要日期纠正**：中文媒体与部分二手来源将 15.0 发布日期误报为 ~~“2025 年 11 月 21 日”~~，经官方公告原文 “Date: December 2, 2025” 与 freebsd-announce 邮件列表原始时间戳交叉验证，确认为 **12 月 2 日**；i386 并非 “完全移除源码支持”——i386 内核源码与 lib32 兼容层仍保留在源码树中，用户可自行构建，仅 RELEASE 安装镜像不再提供；从源码构建 i386 的路径仍对遗留硬件与模拟器场景开放
- 关于 “默认 shell 从 tcsh 改为 sh” 的说法需精确澄清——14.0 已将 **root 用户默认 shell 从 csh/tcsh 改为 /bin/sh**（BSD Bourne Shell），15.0 延续了这一改变并进一步改进了 /bin/sh 的交互使用体验，但 **并非 15.0 新引入的变化**；**wg(4)** WireGuard 驱动状态——14.0 已集成 **wg(4)** WireGuard 内核驱动，15.0 延续随内核发布并持续完善其配套工具链
- LinuxKPI 驱动与 “原生 FreeBSD 驱动” 的区别需澄清——基于 LinuxKPI 的驱动在内核中运行，通过 LinuxKPI 兼容层调用 FreeBSD 原生内核功能，性能与稳定性接近原生驱动，但代码来自 Linux 上游；这与 Linuxulator（Linux 二进制兼容层，运行 Linux 用户态程序）性质不同——LinuxKPI 是内核态 API 兼容，Linuxulator 是用户态系统调用与执行环境兼容
- 关于 “FreeBSD 15.0 是 AI 时代的版本” 这一叙事需适度——15.0 本身不包含任何 AI/LLM 特定的内核特性，但 15.x 周期恰逢 AI 大爆发时代（ChatGPT 2022.11、GPT-4 2023.3、Claude 系列、Gemini 系列），社区中确实出现了使用 AI 辅助驱动开发（Varankin BCM4350 驱动）的案例，但 Core Team 截至 2025 年仍未就 AI 辅助开发出台正式的接受或禁令政策，相关讨论仍在进行〔存疑：政策最新进展待回源核验；同期 NetBSD 已宣布禁止 AI 生成代码入库，两项目取向不同〕
- **重要日期纠正**：部分二手来源将 15.1 发布日期误报为 ~~“2026 年 6 月 6 日”~~，经官方公告原文 “Date: June 16, 2026” 交叉验证，确认为 **6 月 16 日**；另一个值得注意的细节：15.1 公告提到 VM 镜像支持 i386——但这并不意味着 i386 重新成为 RELEASE 架构，仅表示提供实验性 i386 VM 镜像用于测试与兼容性目的，安装级 RELEASE 支持并未恢复

## 文献

- FreeBSD Project. FreeBSD 15.0-RELEASE Announcement [EB/OL]. (2025-12-02)[2026-07-19]. <https://www.freebsd.org/releases/15.0R/announce/>; FreeBSD Project. FreeBSD 15.0-RELEASE Release Notes [EB/OL]. (2025-12-02)[2026-07-19]. <https://www.freebsd.org/releases/15.0R/relnotes/>; FreeBSD Project. Supported Releases [EB/OL]. [2026-07-19]. <https://www.freebsd.org/releases/>
- OpenZFS Project. OpenZFS 2.4.0 Release Notes [EB/OL]. (2025)[2026-07-19]. <https://github.com/openzfs/zfs/releases>; OpenSSL Project. OpenSSL 3.5 Release Notes [EB/OL]. (2025-04-08)[2026-07-19]. <https://www.openssl.org/blog/blog/2025/04/08/OpenSSL35/>; OpenSSH Project. OpenSSH 10.0 Release Notes [EB/OL]. (2025-04)[2026-07-19]. <https://www.openssh.com/txt/release-10.0>
- FreeBSD Project. LinuxKPI Source Code [EB/OL]. [2026-07-19]. <https://cgit.freebsd.org/src/tree/sys/compat/linuxkpi>; FreeBSD DRM Graphics Drivers Project [EB/OL]. [2026-07-19]. <https://github.com/freebsd/drm-kmod>; FreeBSD Foundation. 2025 Sponsored Projects Update [EB/OL]. [2026-07-19]. <https://freebsdfoundation.org/blog/>［著录补全注：原 URL 截断，补至可核查的官方博客域名路径］
- FreeBSD Project. In Memoriam: Mike Karels [EB/OL]. (2024-12)[2026-07-19]. <https://www.freebsd.org/releases/14.2R/announce/> (Dedication section); FreeBSD Project. FreeBSD 15.1-RELEASE Announcement [EB/OL]. (2026-06-16)[2026-07-19]. <https://www.freebsd.org/releases/15.1R/announce/> (Dedication to Peter G. Neumann)
- FreeBSD Project. FreeBSD 15.1-RELEASE Announcement [EB/OL]. (2026-06-16)[2026-07-19]. <https://www.freebsd.org/releases/15.1R/announce/>; Neumann P G. Computer-Related Risks [M]. Addison-Wesley, 1995. ISBN 978-0-201-55805-9; FreeBSD Project. release/15.1.0. freebsd-src 仓库 tag [DB/OL]. 2026-06-12［著录补全注：原条目截断于时间戳半途，按 tag 日期补全至日级］
- FreeBSD Project. FreeBSD 15.1-RELEASE Release Notes [EB/OL]. (2026-06-16)[2026-07-19]. <https://www.freebsd.org/releases/15.1R/relnotes/>; Unicode Consortium. Unicode 17.0 Release [EB/OL]. (2025-09)[2026-07-19]. <https://home.unicode.org/announcing-unicode-17/>.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］; FreeBSD Project. FreeBSD Release Engineering [EB/OL]. [2026-07-19]. <https://www.freebsd.org/releng/>; Somers A. The Case for Rust (in the base system)[EB/OL]. (2024-01-20)[2026-07-19]. <https://lists.freebsd.org/archives/freebsd-hackers/2024-January/002823.html>. ［A］
- FreeBSD Project. FreeBSD Release Schedule Archive [EB/OL]. [2026-07-19]. <https://www.freebsd.org/releases/>; Percival C. FreeBSD Release Engineering Posts [EB/OL]. [2026-07-19]. <https://www.daemonology.net/blog/>. ［C］


<!-- dangan-20260908 消解回写 -->
- LWN.net.. NetBSD Bans AI-Generated Code?[EB/OL]. (2024-05)[2026-07-19]. <https://lwn.net/>[EB/OL]. 2024. ［待核·needs_fix］［DKC-2348→fulltext:6168］
<!-- /dangan-20260908 -->

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
