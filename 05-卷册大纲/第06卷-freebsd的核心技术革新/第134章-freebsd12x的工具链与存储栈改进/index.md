---
chapter: 第 134 章
id: CH134
volume: 06
---

## 要点

- pkgbase 是将 FreeBSD base 系统拆分为可通过 **pkg(8)** 管理的软件包的实验性项目，主要由 Glen Barber（格伦·巴伯）（gjb@）与 Release Engineering Team 开发，在 12.x 时期引入实验性支持。传统上 FreeBSD base 系统通过 make buildworld/installworld 或 **freebsd-update(8)** 整体更新，pkgbase 目标是让 base 组件像 ports 编译的第三方软件一样可独立安装、更新、卸载。12.x 时期 pkgbase 处于“实验性技术预览”状态，提供基础包构建但不推荐生产使用。pkgbase 的长期目标是使系统更新更灵活（可只更新特定组件而不重启）、支持最小化系统安装（如仅安装内核+libc+SSH）。pkgbase 最终在 FreeBSD 14.x/15.x 逐步成熟。
- WireGuard（现代 VPN 协议）导入 FreeBSD base 系统的争议虽然发生在 FreeBSD 13.0 周期（2020 年 12 月 -2021 年 3 月）而非 12.x 周期，但其对社区治理的深远影响波及整个 12.x 后期维护时期。事件概要：2020 年 12 月，Netgate（Rubicon Communications，pfSense 母公司）雇员将 WireGuard 实现提交至 FreeBSD base，随后 WireGuard 作者 Jason Donenfeld 公开批评该代码存在严重安全漏洞与质量问题，引发激烈的社区争议；2021 年 3 月，该代码从 FreeBSD 13.0 中移除，由 John Baldwin（约翰·鲍德温） 等人重新基于 Jason Donenfeld 认可的实现重新移植。此事件暴露了企业商业利益与社区开源治理之间的张力，引发了关于 code review 流程、committer 责任、Core Team 治理能力的广泛讨论。12.x 分支未合入任何有争议的 WireGuard 代码。
- 12.x 时期跨越 2018 与 2020 两次 Core Team 选举：2018 年选举产生 2018-2020 届 Core Team，2020 年选举产生 2020-2022 届 Core Team。Security Officer Gordon Tetlow（戈登·泰特洛）（gordon@）自 11.2（2018.6）接任后在整个 12.x 周期（2018-2022）持续担任 Security Officer，Deputy 为 Ed Maste（埃德·马斯特）（emaste@）、Remko Lodder（remko@，至 12.1 后淡出）、Xin Li（delphij@，12.2 起任 Security Team Liaison）。Gordon Tetlow 任期内主导了 Meltdown/Spectre 等重大安全事件响应。FreeBSD Foundation 在 12.x 时期资助了大量项目：LLVM 工具链现代化、RISC-V 移植、可重现构建、WireGuard 重新实现、ZFS 改进、bhyve 改进、pkgbase 等。
- FreeBSD 12.0-RELEASE（2018 年 12 月 11 日）在 amd64 和 i386 架构上不再默认安装 GCC 4.2.1，commit r338562 由 Warner Losh（沃纳·洛什）（imp@）提交，这是 GCC 从 FreeBSD base system 逐步移除的关键里程碑。在此之前，10.0（2014）已将 GCC 从 x86/arm 的默认编译器位置移除但保留在 base 源码树中；12.0 进一步在 x86 架构上不再默认构建和安装 GCC 4.2.1 二进制文件，用户如需 GCC 可通过 ports（lang/gcc）安装现代 GCC 版本。GCC 4.2.1 仍保留在 base 源码树中用于 sparc64、powerpc、powerpc64、mips 等未完成 Clang 迁移的架构——这些架构在 12.0 中仍默认使用 GCC 构建。GCC 4.2.1 从所有架构完全移除发生在 FreeBSD 13.0（2021 年 4 月 13 日）。
- FreeBSD 12.0-RELEASE 将 LLD（LLVM Linker）设为 amd64 架构的默认系统链接器，替代 GNU ld（来自 GNU binutils）。LLD 是 LLVM 项目的子项目，由 Rui Ueyama 等开发，使用 Apache 2.0 with LLVM Exceptions 许可证，链接速度远快于 GNU ld（大型 C++ 项目可快 2-5 倍），且原生支持 LTO（Link Time Optimization）。12.0 中 LLD 为 amd64 默认链接器，i386 和 armv6/armv7 可选，arm64 也在 12.0 中默认使用 LLD。GNU ld 仍保留在 base 中用于其他架构（如 powerpc64、mips 等）。FreeBSD 13.0 将 LLD 设为所有架构的默认链接器。

## 史观

- 总纲第 17 条——软件工程：pkgbase 反映了 FreeBSD 从"monolithic base"向"packageable components"的工程范式迁移。类 Unix 操作系统长期以来将基础系统与第三方软件严格分离（base vs ports/pkg），这种分离保证了 base 的纯净与一致性但也限制了灵活性。pkgbase 试图在保持 base 质量标准的同时引入更现代的软件管
- 总纲第 24 条——许可证：GCC 移除是 FreeBSD 许可证纯洁化工程的最终阶段——GCC 4.2.1 是最后一个 GPLv2 许可的 GCC 版本（GCC 4.3+ 转为 GPLv3），FreeBSD 项目拒绝引入 GPLv3 代码到 base，因此长期使用 2007 年发布的 GCC 4.2.1 作为“最后的 GPL 编译器”；总纲第 5 条——技术债务：GCC 4.2.1 在 2018
- 总纲第 13 条——法律与道德是利益分配：GPL 阵营的批评反映 copyleft 主义内部的逻辑自洽——若“自由”定义为“用户免于被锁定的自由”，则宽容许可证确为“较弱的保护”，BSD 阵营驱逐 GPL 工具实为削弱对用户自由的保护。但该批评同样遮蔽了 BSD 阵营对“自由”的不同定义（开发者任意处置代码的自由），双方在各自哲学框架内均自洽，争议的实质是“自由”定义权之争而非道德高下之分。
  
- 总纲第 13 条——法律与道德是利益分配：GCC 移除与 LLD 替代争议的法律文本（GPLv3 §5/§6/§11）与道德话语（“自由”“纯洁”）均为利益分配的形式主义工具。CDDL 许可的 ZFS/DTrace 被接受入 base 而 GPLv3 的 GCC 被驱逐，二者的法律差异（CDDL 是弱 copyleft 文件级，GPLv3 是强 copyleft 作品级）确为实质差异，但“接受”与
- 总纲第 17 条——软件工程：bectl 是典型的“将最佳实践工具内化到 base”案例——引导环境管理概念源自 Solaris 的 beadm，FreeBSD 社区长期通过 ports/sysutils/beadm 使用此功能，12.0 将其纳入 base 表明引导环境已被视为系统级核心功能而非附加工具。ZFS 引导环境配合 **freebsd-update(8)** 可实现安全可靠的系统更新，

## 辨析

- pkgbase 在 12.x 完全是实验性质，不适合生产环境；**freebsd-update(8)** 仍是 12.x 官方推荐的二进制更新工具；pkgbase 与传统 buildworld 并行存在而非替代。pkgbase 概念的最初发起者是 bapt@（Baptiste Daroussin），2015 年即已启动（Vadot, 2019），Glen Barber 与 Release Engi
- 12.0 的 GCC 移除是“amd64/i386 上不再默认安装”而非“从源码树删除”——GCC 4.2.1 源码仍存在于 base 中供非 x86 架构使用，且 x86 用户仍可通过 WITH_GCC 选项启用 GCC 构建；sparc64 在 12.0 已被移除为 Tier 2 并最终在 12.x 中停止发布镜像，但 GCC 4.2.1 仍保留用于 powerpc/powerpc64/mip
- 按 0 信任原则考据，“12.0 仅 amd64/i386 不默认安装 GCC 4.2.1”系经 FreeBSD 12.0-RELEASE Release Notes 核实的确证事实（61.9.1 已考据）。“sparc64 在 12.x 停止发布镜像”系经 61.5 架构支持变化节考据。“LLD 仅 amd64/arm64 默认”系经 61.9.2 考据。但“FSF 官方点名批评 FreeBSD
- 考据过程留痕——【查证来源】总纲第 13 条系经 Read 核实的项目统摄史观原文（第 25 章.md 第 17 行），引用确证；GPLv3 §11 与 Apache 2.0 §3 专利条款对照经 61.9.7 考据确证；FreeBSD base 中 CDDL 许可的 ZFS/DTrace 与 Apache 2.0 许可的 LLVM/Clang/LLD 共存事实经 FreeBSD base 源码确
- **bectl(8)** 在 12.0 为初始版本，功能相对基础；高级功能（如引导环境快照自动清理、与 pkg 集成的自动快照）在后续版本完善。bectl 仅管理 ZFS 引导环境——UFS 文件系统不支持引导环境。bectl 不替代 beadm——两者可共存但 bectl 为官方推荐工具。
  - 文献：FreeBSD **bectl(8)** Manual Page [Z]；FreeBSD 1

## 文献

- FreeBSD pkgbase Wiki page [EB/OL]. wiki.freebsd.org/PkgBase；Barber G. pkgbase status updates [EB/OL]. freebsd-announce mailing list, 2018-2022；Vadot E. pkgbase: Are We There Yet? [C]//EuroBSDCon 2019. Lillehammer, 2019. ［A］

## 133.10.2 WireGuard 争议与社区治理（13.x 语境事件）

- 要点：WireGuard（现代 VPN 协议）导入 FreeB
- FreeBSD 12.0-RELEASE Release Notes [Z]. 2018-12-11；FreeBSD 13.0-RELEASE Release Notes [Z]. 2021-04-13；commit r338562 [Z]. svn.freebsd.org ［A］

## 133.11.2 LLD 成为 amd64 默认链接器

- 要点：FreeBSD 12.0-RELEASE 将 LLD（LLVM Linker）设为 amd64 架构的默认系统链接器，替代 GNU ld（来自 GNU binutils）。LLD 是 LLVM 项目的子项目，由 Rui Ueyama 等开发
- FreeBSD 12.0-RELEASE Release Notes [Z]. 2018-12-11；FreeBSD 13.0-RELEASE Release Notes [Z]. 2021-04-13；Free Software Foundation. Various Licenses and Comments about Them [EB/OL]. gnu.org/licenses/license-list.html（#ModifiedBSD、#FreeBSD 条目，2026-07-22 核实）.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13 条，第 17 行）；Free Software Foundation. GNU General Public License Version 3 [Z]. 2007-06-29（§5c、§6、§11）；Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01（§3）；Free Software Foundation. 各类许可证及其评论 [EB/OL]. **<<https://www.gnu.org/licenses/license-list.html>*
- FreeBSD **bectl(8)** Manual Page [Z]；FreeBSD 12.0-RELEASE Release Notes Userland section [Z]. 2018；commit r337663 [Z]. svn.freebsd.org. ［A］

## 133.6.2 **iflib(4)** 网络驱动框架与驱动迁移

- 要点：iflib（Interface Framework，网络驱动框架）在 FreeBSD 11.x 引入原型，12.x 时期大量网卡驱动迁移到 iflib 框架上。iflib 由 Matt Macy（mmacy@）、John Baldwi
- FreeBSD 12.0-RELEASE Announcement/Release Notes Storage sections [Z]. 2018；McKusick M K, et al. The Design and Implementation of the FreeBSD Operating System (2nd ed.)[M]. Addison-Wesley, 2014. ［B］

## 133.7.2 NFSv4.1 服务端与 pNFS 支持

- 要点：FreeBSD 12.0 的 NFSv4.1 服务器实现更新，包含 pNFS（Parallel NFS）服务器支持（"The
- Watson R N M, et al. Capsicum: Practical Capabilities for UNIX [C]//USENIX Security 2010；FreeBSD **capsicum(4)**/**casper(3)** Manual Pages [Z]；FreeBSD 12.0-RELEASE Announcement [Z]. 2018.

## 133.8.2 Linux 兼容层——CentOS 7 与 Ubuntu 用户态

- 要点：FreeBSD 12.x 时期 Linux 二进制兼容层（Linuxulator）持续改进：①CentOS 7 用户态兼
- Pédron J-S. FreeBSD Graphics Status Reports [EB/OL]. freebsd-x11 mailing list, 2018-2022；FreeBSD Quarterly Status Reports Graphics chapters [R]；graphics/drm-kmod ports entry [Z]. ［A］

## 133.9.2 LinuxKPI 兼容层的工程效应

- 要点：LinuxKPI（Linux Kernel Programming Interface）兼容层是使 Linux DRM 驱动能在 FreeBSD 内核上运行的关键

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
