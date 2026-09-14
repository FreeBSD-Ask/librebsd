# 第 155 章 freebsd14x第三方软件与同期os比较

---
chapter: 第 155 章
id: CH155
volume: 第07卷-freebsd的工程体系重构
---

## 史料

- [WEB:freebsd.org/releases/14.0R/relnotes.html] FreeBSD 14.0-RELEASE Release Notes（官方一手）：第三方软件变更（OpenSSH 9.5p1、OpenSSL 3.0.12、OpenZFS 2.2）与同期 OS（Linux/NetBSD/OpenBSD）对照的官方文本基准
- [WEB:usenix.org BSDCon Proceedings] USENIX BSDCon 论文集（一手）：跨 BSD 项目技术对照的学术发表平台记录

## 要点

- FreeBSD 14.0-RELEASE（2023 年 11 月 20 日）将 DMA（DragonFly Mail Agent）设为 base system 的默认 MTA，替换自 4.1cBSD（1982 年）起服役 41 年的 sendmail。DMA 由 Matthias Schmidt 为 DragonFly BSD 项目开发，是一款轻量级 MTA，专为无需完整邮件服务器的桌面/客户端系统设计——仅负责本地邮件投递（如 cron 输出、系统通知）与通过外部 smarthost 转发，不具备 sendmail 的完整 MTA 功能（如邮件队列管理、反垃圾邮件、虚拟域等）。14.0 的默认 MTA 切换体现了 “默认情况下大部分 FreeBSD 系统不需要完整 MTA” 的设计哲学——需要完整邮件服务器功能的用户可从 ports 安装 sendmail、Postfix、Exim 等。sendmail 仍可通过 ports（mail/sendmail）安装，14.0 的 /etc/mail/mailer.conf 默认指向 dma 而非 sendmail。这是 FreeBSD 历史上最显著的 “上古组件退役” 事件之一，与 BIND 移除（10.0）、GCC 移除（13.0）并列。
- FreeBSD 14.0-RELEASE 搭载 OpenSSL 3.0.12（14.0）→ 3.0.13（14.1）→ 3.0.14（14.2）→ 3.0.16+（14.3-14.4），这是 FreeBSD 首次将 OpenSSL 从 1.1.1 系列升级至 3.0 系列。OpenSSL 3.0 的主要变化包括：将许可证从 OpenSSL License 改为 Apache 2.0（解决了 20 年的 GPL 兼容性争议）、引入 Provider 架构（模块化加密算法提供者）、FIPS 140-3 模块支持、改进的随机数生成器、新的 API 架构。OpenSSL 3.0 是 LTS 版本，支持至 2026 年 9 月 7 日。14.x 搭载的 OpenSSH 版本从 9.5p1（14.0）升级至 9.8p1（14.4），14.4 默认启用混合后量子密钥交换（<sntrup761x25519-sha512@openssh.com>）。
- 14.0 的第三方软件变更以 “默认配置现代化” 为主题——sendmail→DMA 默认 MTA 切换、root 默认 shell 从 csh 切换为 sh（/bin/sh）、telnetd 从 base 移除等，这些变更的共同特征是 “将 1980-1990 年代的默认配置替换为 2020 年代更安全、更简洁的默认配置”。14.0 的变更与 10.0 的 “集中换代” 不同——10.0 是 “一整批新组件的引入”，14.0 是 “一整批旧组件的退役或默认地位变更”。这体现了 FreeBSD 项目在 30 周年后对 “何为生产级 OS 的合理默认配置” 的重新审视。
- FreeBSD 14.x（2023.11-2028.11）同期的 Linux 生态以 Linux 6.1 LTS（2022.12，支持至 2026.12）与 Linux 6.6 LTS（2023.10，支持至 2026.11）、Linux 6.12 LTS（2025.11）为主；Linux 此时期的关键进展包括：① 初始 Rust 内核代码（Linux 6.1 引入，Google 赞助）；② Btrfs/XFS 持续改进（XFS 在线修复、Btrfs 性能优化）；③ BPF/eBPF 生态爆发式增长（可观测性、网络、安全）；④ io_uring 异步 IO 完善；⑤ 容器与 Kubernetes 生态主导云原生；⑥ 桌面硬件支持（特别是 GPU、WiFi）持续领先；⑦ AMD/Intel/NVIDIA GPU 驱动持续更新（NVIDIA 开源 GPU 驱动 Nouveau 改进、Intel Arc 显卡支持）；FreeBSD 14.x 与 Linux 的关键差异在于：FreeBSD 保留 BSD 整体内核设计、ZFS 原生、Jail/bhyve 虚拟化、BSD 许可证、完整的 base 系统；Linux 则在硬件支持、生态规模、企业级云原生支持方面占据市场主导地位
- FreeBSD 14.x 同期桌面 OS 市场：Windows 11（22H2 2022.9、23H2 2023.10、24H2 2024.10）持续演进，引入 Copilot AI 助手、改进 Android 应用兼容（Windows Subsystem for Android）、增强安全功能（TPM 2.0、Secure Boot、VBS/HVCI）；macOS 13 Ventura（2022.10）、14 Sonoma（2023.9）、15 Sequoia（2024.9）持续每年更新，Apple Silicon（M1/M2/M3/M4）Mac 完全转向 ARM64 架构；桌面 OS 市场由 Windows（约 70%）、macOS（约 15-20%）、Linux 桌面（约 2-3%）主导，FreeBSD 桌面用户占比极小（估计不到 0.1%）；FreeBSD 桌面体验在 14.x 中持续改进（Wayland 支持进展、GPU 驱动、WiFi 改进）但仍落后 Linux 桌面数年

## 史观

- 总纲第 5 条——技术债务：sendmail 是 BSD 系统中资历最老的技术债务——其 sendmail.cf 配置语法以晦涩难懂著称，安全性历史上多次出现严重漏洞（如 1988 年 Morris 蠕虫利用 sendmail 漏洞），从社区讨论替换（2000 年代中期）到实际替换（2023 年）历时近 20 年；总纲第 25 条——终结与延续：sendmail 默认地位的终结是 BSD 传统 M
- 总纲第 6 条——技术路线分化：FreeBSD 与 Linux 在 2020 年代代表了两种不同的操作系统演进路径：Linux 走 “市场驱动、快速迭代、生态优先” 路线——内核每 2-3 个月一个大版本、支持尽可能多的硬件、围绕商业公司需求快速开发；FreeBSD 走 “工程质量优先、保守稳定、技术完整性” 路线——大版本约每 2-3 年、支持周期 5 年、重视架构一致性与长期稳定性；两者不是
- 总纲第 17 条——软件工程：80 个 SA 的分布不均（2026 年上半年 49 个，远超 2024 年全年 19 个）反映 FreeBSD Security Team 工作节奏的演进——Security Officer Team 在 Mark Johnston（马克·约翰斯顿）、Philip Paeps（菲利普·佩普斯） 主导下于 2026 年进入“主动审计 + 批量披露”阶段，这与 Open
- 总纲第 17 条——软件工程：regreSSHion 的“18 年回归”是复杂软件系统漏洞生命周期的典型样本——一个已被修复的漏洞在 19 年后因代码重构或补丁管理疏漏重新出现，这种现象在大型代码库中并不罕见（Linux 内核也曾多次出现类似回归）；OpenSSH 作为 base 系统中最敏感的网络服务（**sshd(8)** 默认监听 0.0.0.0:22，运行 root 权限，接受未认证连接）
- 总纲第 23 条——社区治理：OpenSSL 3.0 升级是 14.x 周期 FreeBSD 加密栈的“代际迁移”——OpenSSL 1.1.1 于 2023 年 9 月 EOL，FreeBSD 14.0（2023-11）恰在 EOL 后发布，选择 OpenSSL 3.0 作为新基础；这一迁移在 14.x 周期内引入了持续的安全债务——OpenSSL 3.0 系列在 2022-2024 年间持续发

## 辨析

- 再是默认 MTA，DMA 成为默认；DMA 的功能范围远小于 sendmail——DMA 不支持监听外部 SMTP 连接、不支持邮件队列管理、不支持反垃圾邮件，仅适用于 “本地投递 + 外部 smarthost 转发” 场景，需要完整邮件服务器的用户必须从 ports 自行安装 MTA；
- 关于 “FreeBSD 与 Linux 性能” 的比较需谨慎——不同工作负载下结果差异很大：网络转发（特别是小包处理）场景 FreeBSD 往往有优势、ZFS 文件服务器场景 FreeBSD/ZFS 是业界标杆、Web 服务器场景两者接近、AI/ML/GPU 计算场景 Linux 占据绝对优势（框架与驱动支持完善）；性能比较永远依赖具体工作负载、硬件配置与调优参数，不存在通用的 “X 比 Y 快”
- 80 个 SA 的“数量”本身不是安全态势好坏的直接指标——SA 数量多既可解读为“代码质量差、漏洞频发”，也可解读为“安全审计积极、漏洞主动清理”；14.x 周期 SA 数量增长同时伴随 base 系统架构现代化（Capsicum、bhyve、Jail、ktls 等），表明这是审计覆盖面扩大而非代码质量下降；2026 年 SA 数量激增与 SA-26 系列中“audit”主题（SA-26:45.
- Qualys 同时指出实际利用难度极高——需要绕过 ASLR 并在极窄的时间窗口内赢得竞争，但理论上可实施；一个月后 **FreeBSD-SA-24:08.openssh**（**2024 年 8 月 7 日**）修复 CVE-2024-7589——这是 regreSSHion 修复后发现的“同一问题的另一实例”，由 FreeBSD 特有的 blacklistd 集成引入，是 base 系统特定的
- **需精确说明 CVE 来源**：14.x 周期 OpenSSL CVE 中，部分是 OpenSSL 上游漏洞（如 CVE-2024-6119 证书名称检查拒绝服务），FreeBSD 通过 vendor import 同步修复；部分是 OpenSSL 3.0 引入的新漏洞（如 CVE-2024-5535 SSL_select_next_proto 空指针解引用，是 OpenSSL 3.0 重构 A

## 文献

- FreeBSD 14.0-RELEASE Announcement [Z]. 2023-11-20；FreeBSD 14.0 Release Notes [Z]. 2023；DragonFly BSD. dma - DragonFly Mail Agent [EB/OL]. dragonflybsd.org［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］


<!-- dangan-20260908 消解回写 -->
- Red. Hat. RHSA-2024:1644: Critical security update for xz [EB/OL]. (2024-03-29)[2026-07-22]. <https://access.redhat.com/errata/RHSA-2024:1644>[EB/OL]. 2024. ［待核·needs_fix］［DKC-2286→fulltext:6141］
<!-- /dangan-20260908 -->
## 154.18.2 OpenSSL 3.0 引入与许可证变更

- 要点：FreeBSD 14.0-RELEASE 搭载
- Linux Kernel Archives. Linux Kernel Releases [EB/OL]. [2026-07-19]. <https://www.kernel.org/>; Corbet J, Kroah-Hartman G, McPherson A. Linux Kernel Development Report [R]. The Linux Foundation, 2024; Larabel M. FreeBSD vs. Linux Benchmarks [EB/OL]. (2023-2026)[2026-07-19]. <<https://www.phoronix.com/>
- FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2024-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; MITRE. CVE Project cvelistV5 Repository [Z]. (2026-07). <https://github.com/CVEProject/cvelistV5>; FreeBSD Project. freebsd.duckdb — freebsd-src commits table [DB/
- FreeBSD Security Team. FreeBSD-SA-24:04.openssh: OpenSSH pre-authentication remote code execution [EB/OL]. (2024-07-01)[2026-07-22]. <https://security.freebsd.org/advisories/FreeBSD-SA-24:04.openssh.asc>; FreeBSD Security Team. FreeBSD-SA-24:08.openssh: OpenSSH pre-authentication async signal safety
- FreeBSD Security Team. FreeBSD-SA-24:13.openssl [EB/OL]. (2024-09-04)[2026-07-22]. <https://security.freebsd.org/advisories/FreeBSD-SA-24:13.openssl.asc>; OpenSSL Project. OpenSSL 3.0 Release Notes [EB/OL]. [2026-07-22]. <https://www.openssl.org/source/>; FreeBSD Project. freebsd.duckdb — freebsd-src Op
- MITRE. CVE-2024-3094: Malicious Code in xz-utils 5.6.0/5.6.1 [EB/OL]. (2024-03-29)[2026-07-22]. <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3094>; Freund A. oss-security: backdoor in upstream xz/liblzma leading to ssh server compromise [EB/OL]. (2024-03-29)[2026-07-22]. <<https://www.ope>
- FreeBSD Security Team. FreeBSD Security Information — Disclosure Policy [EB/OL]. [2026-07-22]. <https://www.freebsd.org/security/>; FreeBSD Security Team. FreeBSD-SA-26:28.capsicum [EB/OL]. (2026-06-09)[2026-07-22]. <https://security.freebsd.org/advisories/FreeBSD-SA-26:28.capsicum.asc>; FreeBSD Sec
- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/freebsd.duckdb**; FreeBSD Security Team. FreeBSD Security Advisories [EB/OL]. (2024-2026)[2026-07-27]. <https://www.freebsd.org/security/advisories/>; FreeBSD Security Tea

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
