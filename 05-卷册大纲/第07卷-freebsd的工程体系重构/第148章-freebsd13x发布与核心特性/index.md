---
chapter: 第 148 章
id: CH148
volume: 第07卷-freebsd的工程体系重构
---

# 第148章 freebsd13x发布与核心特性

## 史料

- FreeBSD Release Engineering Team. FreeBSD 13.0/13.1/13.2-RELEASE Announcement 与对应 Release Notes（2021-04-13、2022-05-16、2023-04-11）：KTLS、arm64 Tier 1、GCC 4.2.1 完全移除、OpenZFS 2.x、wg(4) 缺席与加入等核心特性演进的一手官方记载
- [DB:code_repos:freebsd.duckdb] freebsd 仓库 13.x 时段（stable/13 分支 2021-04 起）commit 元数据：GCC 移除、LLVM/Clang 11.0.1 工具链统一、Git 迁移完成（2021-04-06）等关键事件的代码档案记录
- freebsd-announce / freebsd-current 邮件列表存档（2021-04）：13.0-RELEASE Now Available 公告（Message-ID 20210413185035.34DD1202D@nucleus，发件人 Glen Barber）与 Git 迁移完成公告的现场记录

## 要点

- FreeBSD 13.0-RELEASE 于 2021 年 4 月 13 日由发布工程团队正式公告，Glen Barber（格伦·巴伯） 担任 13.0 发布工程师，这是 stable/13 分支的首个版本；13.0 发布前 8 天（2021 年 4 月 5 日）美国最高法院就 Google LLC v. Oracle America, Inc.（593 U.S. 1, Docket No. 18-956）作出 6-2 判决，认定 Google 对 Java API 的重新实现构成 fair use，这一判决对 BSD 社区重新实现 UNIX API 的长期实践具有重大法律意义；13.0 发布时全球仍处于 COVID-19 疫情期间，FreeBSD 开发者会议已全面转为线上，BSDCan 2020-2021 连续两年取消线下会议
- FreeBSD 13.0-RELEASE 将最后残余的 GCC 4.2.1 从 base system 中完全移除——x86 架构（amd64/i386）在 FreeBSD 12.0 已完成向 Clang/LLVM 的迁移，但非 x86 架构（powerpc/powerpc64/arm/arm64/mips/riscv）在 12.x 期间仍保留 GCC 4.2.1 作为可选编译器；13.0 中所有支持架构均统一使用 LLVM/Clang 11.0.1 工具链，包含 clang、lld（LLVM 链接器，成为所有架构默认链接器）、lldb（LLVM 调试器）、compiler-rt、libunwind、libc++ 等组件；同时移除的还有过时的 binutils 2.17 和用于 **crashinfo(8)** 的旧 GDB，用户可通过 ports/packages 安装现代 GDB；LLD 作为默认链接器意味着 FreeBSD 彻底摆脱了对 GNU ld 的依赖，这是自 FreeBSD 10.0 引入 Clang 以来十年去 GNU 化工程的里程碑
- FreeBSD 13.0 将 64 位 ARM 架构（称为 arm64 或 AArch64）正式提升为 **Tier-1** 架构，与 amd64 并列成为 FreeBSD 最高支持级别的架构；Tier-1 地位意味着：发布工程团队为 aarch64 构建 RELEASE 镜像、提供安全更新和 errata、提供官方二进制软件包集、RELEASE 构建阻塞级别为 blocking（即 aarch64 构建失败会阻塞整个发布）；aarch64 支持最初由 Andrew Turner 等开发者于 FreeBSD 11.0（2016）引入，12.x 期间为 Tier-2，13.0 升 Tier-1 标志着 ARM 服务器市场（如 AWS Graviton、Ampere Altra、Apple M 系列芯片）成熟，FreeBSD 成为少数将 ARM64 列为一等公民的通用操作系统；13.0 同时为 aarch64 提供 AWS EC2 AMI、Google Compute Engine 镜像等云平台支持
- 13.0 相比 12.x 的核心特性跨越包括：(1) 工具链全架构 LLVM 化；(2) aarch64 升 Tier-1；(3) KTLS（内核 TLS 卸载）支持 TLS 1.0-1.3（详见 84.2）；(4) OpenZFS 取代原 FreeBSD ZFS 分支（详见 84.3 相关，ch72 详述）；(5) 64 位 inode 支持（UFS/UFS2），突破 2^32 inode 限制，支持超过 80 亿文件；(6) bsdgrep 成为默认 grep，移除 GNU grep；(7) iflib 网络驱动框架成为默认；(8) bhyve 虚拟化改进（AMD-V/VT-d 优化、更多 vCPU 支持，13.2 起支持 > 16 vCPU）；(9) Linux ABI 兼容层改进，引入基于 Debian/Ubuntu 的 Linux 用户态支持（不只是 CentOS）；(10) **fusefs(4)** 文件系统完善；(11) VMDk/VHD/VHDX 虚拟机镜像格式官方支持；(12) **makefs(8)** 支持 ZFS；(13) ASLR 在 13.2 起对 64 位可执行文件默认启用；(14) Capsicum/Casper 能力系统持续完善；(15) 移除 Beastie ASCII 启动菜单（新启动菜单不再包含 Beastie ASCII art）；(16) **syscons(4)** 从 GENERIC 内核移除，**vt(4)** 成为默认控制台
- FreeBSD 13.1-RELEASE 于 **2022 年 5 月 16 日** 由发布工程团队正式公告，Glen Barber 担任 13.1 Release Engineer（这是他最后一次担任 Release Engineer Lead）；13.1 是 stable/13 分支的第二个版本，核心特性包括：(1) OpenSSH 升级到 8.8p1，支持 FIDO/U2F 硬件认证密钥（ecdsa-sk、ed25519-sk 公钥类型）；(2) OpenSSL 升级到 1.1.1o；(3) ZFS 升级到 OpenZFS 2.1.4；(4) **ice(4)** 驱动更新到 1.34.2-k，添加固件日志和初始 DCB 支持；(5) 引入 **iwlwifi(4)** 驱动及 LinuxKPI 802.11 兼容层，补充 **iwm(4)** 以支持较新的 Intel WiFi 芯片；(6) EC2 镜像默认使用 UEFI 启动而非传统 BIOS；13.1 公告专门将此版本献给 386BSD 共同作者 **Bill Jolitz**——“We stand on the shoulders of giants”，Bill Jolitz 于 2022 年逝世；13.1 不包含 WireGuard **wg(4)** 驱动（重写工作仍在进行）

## 史观

- 项目统摄史观：2021 年 4 月是 FreeBSD 历史的关键一刻——Git 迁移完成（2021-04-06）、最高法院 API 版权判决（2021-04-05）、13.0 正式发布（2021-04-13），三件大事在八天内相继发生，共同标志着 FreeBSD 从 12.x 时代向 13.x 时代的过渡
  - 辨析：[双库核查：2026-08-15] 13.0-RELEASE 发布日期（2021-04-13）经邮件列表库验证通过——Message-ID 20210413185035.34DD1202D@nucleus，发件人 Glen Barber，主题 FreeBSD 13.0-RELEASE Now Available
- 总纲第 2 条——实践先于理论：KTLS 不是学术界设计的“完美方案”，而是 Netflix 生产环境中遇到 TLS 性能瓶颈后的工程解决方案——内容分发网络需要处理海量 TLS 连接，用户态 TLS 终止的上下文切换和数据拷贝开销过高，因此推动内核态 TLS 实现；这符合 FreeBSD“生产需求驱动开发”的传统
  - 辨析：常见误解称 13.0“默认启用 KTLS”，实际上需要重新编译 world 启用 WITH_OPENSSL_KTLS 选项，KTLS 在 13.0 是“可用但非默认”状态
- 总纲第 25 条——终结与延续：2021 年 4 月 6 日标志着 FreeBSD 使用了 20 年（2001-2021）的 CVS/SVN 时代终结，Git 时代开始；这不是简单的工具替换，而是开发工作流的深刻变革——Gerrit 代码审查、GitHub Pull Request 镜像、CI/CD 集成等现代开发实践成为可能
  - 辨析：“13.0 是 Git 迁移后第一个 RELEASE”是准确的——svn 在 2021 年 3 月冻结提交，13.0 构建在 Git 迁移完成后进行，而 13.1 才是完全在 Git 工作流下开发的第一个版本，二者以此为界
- 总纲第 4 条——分离与聚合：WireGuard 争议是开源社区“商业公司利益”“上游作者权威”“核心团队治理”“安全审计”多方力量分离后的剧烈冲突，也是 FreeBSD 治理模式成熟过程中必须经历的阵痛；争议最终促成代码重写和流程改进，体现了开源社区“在争论中进步”的特性
  - 辨析：**重大事实修正**：原大纲称“13.1 启用重构后版本”是 **错误** 的——经 13.1 和 13.2 官方 Release Notes 交叉验证，13.1（2022-05-16）不包含 **wg(4)** 驱动，**wg(4)** 在 **13.2（2023-04-11）** 才正式可用
- 总纲第 19 条——解释学循环是历史认识的根本条件：Scott Long 与 Kyle Evans 的邮件揭示了 WireGuard 争议中各方前理解的不可调和——Scott Long 的前理解以“Netgate 商业利益与安全披露伦理”为框架，将 Donenfeld 的公告解读为“协同抹黑行动”；Kyle Evans 的前理解以“FreeBSD 工程文化与技术准确性”为框架，既承认代码问题存在又

## 辨析

- [双库核查：2026-08-15] 13.0-RELEASE 发布日期（2021-04-13）经邮件列表库验证通过——Message-ID 20210413185035.34DD1202D@nucleus（2021-04-13T14:50:35-04:00），发件人 Glen Barber，主题 FreeBSD 13.0-RELEASE Now Available；13.0 发布日期存在 4 月
- 常见误解称 13.0“默认启用 KTLS”，实际上需要重新编译 world 启用 WITH_OPENSSL_KTLS 选项，KTLS 在 13.0 是“可用但非默认”状态；KTLS 并非“零拷贝”的银弹，它减少了用户态/内核态之间的数据拷贝次数，但仍需要正确的套接字选项和应用程序支持；KTLS 接收卸载在 13.0 中仅支持 TLS 1.2 AES-GCM，TLS 1.3 接收卸载在后续版本完善

- “13.0 是 Git 迁移后第一个 RELEASE”是准确的——svn 在 2021 年 3 月冻结提交，13.0 构建在 Git 迁移完成后进行；但 13.0 的开发周期大部分时间仍在 svn 上进行，13.1 才是完全在 Git 工作流下开发的第一个版本；迁移并非“所有人都满意”——部分老 committer 对 Git 工作流不适应，但社区整体接受了迁移
  - 文献：FreeBSD Project. (2021-04-06). *Git Migration Complete Announcement*. freebsd.org; FreeBSD Release Engineering Team. (2022-05-16). *FreeBSD 13.1-RELEASE Announcement*. freebsd.org
- **重大事实修正**：原大纲称“13.1 启用重构后版本”是 **错误** 的——经 13.1 和 13.2 官方 Release Notes 交叉验证，13.1（2022-05-16）不包含 **wg(4)** 驱动，**wg(4)** 在 **13.2（2023-04-11）** 才正式可用；争议双方的核心分歧不是“WireGuard 好不好”，而是“代码质量是否达到可进入 RELEASE 的
- **0 信任原则考据过程留痕**——(1) **Scott Long 邮件的真实性验证**：Scott Long 原邮件为私人邮件，非公开发布，但其全文经 Donenfeld 2021-03-16T01:18:19Z 在 wireguard 邮件列表公开回复中逐段引用而进入公开记录；邮件列表存档（lists.zx2c4.com）为 WireGuard 项目官方存档，邮件 ID 006499，时间戳

## 文献

- FreeBSD Release Engineering Team. (2021-04-13). *FreeBSD 13.0-RELEASE Announcement*. freebsd.org; Supreme Court of the United States. (2021-04-05). *Google LLC v. Oracle America, Inc., 593 U.S. 1*; FreeBSD Foundation. (2021). *2021 Annual Report*. freebsdfoundation.org; FreeBSD Project. release/13.0
- FreeBSD Project. **ktls(4)** Manual Page; Baldwin, J. (2019). *Kernel TLS Offload*. BSDCan 2019; Gallatin, D., & Baldwin, J. (2017-2021). KTLS Commits to FreeBSD src. ［A］


<!-- dangan-20260908 消解回写 -->
- Salter. J. In-kernel WireGuard is on its way to FreeBSD and the pfSense router [EB/OL]. (2021-03-16)[2026-07-22]. <https://arstechnica.com/gadgets/2021/03/in-kernel-wireguard-is-on-its-way-to-freebsd-and-the-pfsense-router/>[EB/OL]. 2021. ［DKC-2234→fulltext:6118］
- Solidot.. WireGuard 将进入 FreeBSD 内核 [EB/OL]. (2021-03-16)[2026-07-22]. <https://www.solidot.org/story?sid=67219>[EB/OL]. 2021. ［DKC-2235→fulltext:6119］
<!-- /dangan-20260908 -->
## 148.2.2 KTLS 的工程效应与生态

- 要点：KTLS 的引入对 FreeBSD 网络栈有深远工程影响：(1) 推动内核加密框架（OPCF，Open Crypto Framework）重构，支持异步加密操作；(2) 促进 **sendfile(2)** 与 KTLS 协同实现内核态加密零拷贝发送，Netflix 的规模化内容分发即是此路径的生产应用
- FreeBSD Project. (2021-04-06). *Git Migration Complete Announcement*. freebsd.org; Maste, E. (2020). *FreeBSD Git Migration*. EuroBSDCon 2020; FreeBSD Foundation. (2021). Git Migration Project Retrospective. ［A］

## 148.3.2 Git 迁移对开发模式的效应

- 要点：Git 迁移对 FreeBSD 开发模式产生多方面深远影响：(1) 代码审查：引入 Gerrit 代码审查系统
- Donenfeld, J. A. (2021-03-15). *WireGuard for FreeBSD*. wireguard mailing list (lists.zx2c4.com/pipermail/wireguard/2021-March/006494.html); Ars Technica. (2021-03). *Buffeted by bug reports, FreeBSD reverts WireGuard support before 13.0 release*. arstechnica.com; FreeBSD Release Engineering Team. (2021-04-13). *FreeBSD 13.0-RELEASE Announcement*. freebsd.org
- Donenfeld J A. Re: [ANNOUNCE] WireGuard for FreeBSD in development for 13.y – and a note of how we got here (公开回复 Scott Long 私人邮件)[EB/OL]. (2021-03-16T01:18:19Z)[2026-07-23]. <https://lists.zx2c4.com/pipermail/wireguard/2021-March/006499.html>; Evans K. Re: [ANNOUNCE] WireGuard for FreeBSD in development for 13.y（公开回复，lists.zx2c4.com 存档）〔存疑：存档邮件 ID 待核补〕

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
