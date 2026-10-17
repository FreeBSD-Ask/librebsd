---
chapter: 第 151 章
id: CH151
volume: 第07卷-freebsd的工程体系重构
---

# 第151章 freebsd14x发布与核心特性

## 史料

- [DB:research_notes:blocks:6] 关键词“核心特性”命中：史实考据：Marshall Kirk McKusick、Keith Bostic、Michael J. Karels、J…
- [DB:research_notes:blocks:8] 关键词“核心特性”命中：史实考据：CSRG 于 1994 年 6 月发布的 4.4BSD-Lite 官方 Release Notes，是 4.4…
- [DB:research_notes:blocks:1202] 关键词“核心特性”命中：史实考据：Michael W. Lucas 撰写的《Absolute FreeBSD》第三版，基于 FreeBSD 11…

## 要点

- FreeBSD 14.0-RELEASE 于 **2023 年 11 月 20 日** 由 Release Engineering Team 正式发布（Release Engineer 为 Colin Percival），是 stable/14 分支的首个版本，也是 2023 年 6 月 19 日 FreeBSD 1.0 发布三十周年之后的首个大版本；14.0 献词给 **Hans Petter Selasky**（hselasky@）——FreeBSD USB 子系统长期维护者与核心开发者，于 2023 年去世；14.0 开发周期跨越两年半（自 13.0 于 2021 年 4 月发布后），集成了超过 25,000 个 commit，代表 FreeBSD 进入现代化成熟期；14.0 支持架构包括 amd64、aarch64、i386、powerpc、powerpc64、powerpc64le、powerpcspe、armv7、riscv64（**注：powerpc64le 与 powerpcspe 在 14.2 起停止提供 RELEASE 镜像**）；amd64 与 arm64 平台支持高达 1024 个 CPU 核心
- 14.0 带来的核心技术变更包括但不限于：① 默认 MTA 从 sendmail 替换为 **dma(8)**（DragonFly Mail Agent），sendmail 仍保留在 base 中但不再默认启用；② OpenSSL 从 1.1.1t 升级至 **3.0.12**（许可证变更为 Apache 2.0，引入 provider 架构与 FIPS 模块支持）；③ ZFS 升级至 **OpenZFS 2.2**，支持 block cloning（块克隆，类似 reflinks 写时复制文件克隆）、zstd 压缩改进、scrub 性能优化、BLAKE3 校验算法；④ 默认编译器升级至 Clang/LLVM 16（14.0 后期跟进至 17）；⑤ **wg(4)** WireGuard VPN 驱动重新集成（由 Netgate/Rubicon Communications 与 FreeBSD Foundation 赞助重写，2021 年争议后的代码经过全面审查）；⑥ KTLS（内核 TLS）新增 TLS 1.3 接收端卸载支持（Netflix 赞助）；⑦ **netlink(4)**——Linux 兼容的 Netlink 协议实现（Alexander V. Chernikov 开发），为运行 Linux 网络管理工具（iproute2 等）提供协议基础；⑧ 64 位可执行文件默认启用 PIE（位置无关可执行文件）与 ASLR（地址空间布局随机化）；⑨ TCP 默认拥塞控制算法从 New Reno 改为 **CUBIC**；⑩ root 用户默认 shell 从 csh/tcsh 改为 **sh(1)**（BSD Bourne Shell，经大幅改进支持交互使用）；⑪ 新增 **fwget(8)** 工具自动获取 Intel/AMD GPU 等设备固件；⑫ bhyve 虚拟化支持 TPM 2.0 passthrough 与 GPU passthrough、解除 16 vCPU 限制；⑬ **boottrace(4)** 启动过程跟踪框架；⑭ 所有平台（包括 i386）启用 **64-bit time_t** 以解决 Y2038 问题；⑮ UFS 文件系统在启用 journaled soft updates 时支持后台文件系统检查（background filesystem checks）；⑯ AWS 与 Azure 提供实验性 ZFS 云镜像
- 相较 13.2-RELEASE（2023.4），14.0 的核心演进方向可归纳为“默认安全化、工具现代化、生态兼容化、64 位纯净化”四大主题：安全默认方面，PIE+ASLR 默认启用标志着 FreeBSD 加入现代操作系统安全基线行列；工具链方面，LLVM 16/17、OpenSSL 3.0、OpenZFS 2.2、OpenSSH 9.5p1 全面跟进上游；生态兼容方面，**netlink(4)**、**nproc(1)**、Linuxulator arm64 与 amd64 对等、NFS over TLS（rpc.tlsclntd/rpc.tlsservd）缩小与 Linux 的功能鸿沟；平台策略方面，i386 仍为 RELEASE 架构但被明确标注为“last major version with 32-bit platform support”；13.0-RELEASE 于 2021.4 发布时 WireGuard 因代码质量问题在 RC 阶段被临时移除，14.0 中 **wg(4)** 经过 Netgate 赞助 John Baldwin（约翰·鲍德温） 团队的完整重写与多轮安全审计后正式回归，这一过程历时约两年半
- 14.0 发布工程团队由 Colin Percival（Release Engineering Lead）、Glen Barber（Deputy Lead for 14.0）、Mike Karels 等组成；14.0 在发布前经历了多次 BETA/RC 迭代，原计划发布日期从 2023 年 10 月底推迟至 11 月 20 日；14.0 是 Mike Karels 参与发布工程工作的最后一个大版本之一——他于 2024 年 10 月去世（14.2 献词给他）；FreeBSD 30 周年（2023.6.19）恰在 14.0 发布前五个月，项目未举办大规模官方庆典，但 freebsd-announce 与社区邮件列表有纪念讨论；14.0 发布时同期操作系统生态为：Linux 6.1 LTS（2022.12，含初始 Rust 代码）、Windows 11 22H2（2022.9）、macOS 14 Sonoma（2023.9）、OpenBSD 7.4（2023.10）、NetBSD 10.0 RC 阶段、DragonFly BSD 6.4（2022.12）
- FreeBSD 14.0 采用 **dma(8)**（DragonFly Mail Agent）作为默认 MTA，取代自 FreeBSD 1.0（甚至可追溯至 4.2BSD）以来持续近四十年的 sendmail 默认地位；**dma(8)** 是 DragonFly BSD 项目开发的轻量级 MTA，设计目标不是替代完整功能的 sendmail/postfix/exim，而是满足桌面/简单服务器场景的本地邮件投递与上游 SMTP 转发需求——即 “接受本地 MUA 提交的邮件并递送到本地或远程智能主机（smarthost）”；sendmail 并未从 base system 中移除，仍可通过 **mailer.conf(5)** 配置切换回 sendmail 作为默认；这一决策最早由 Baptiste Daroussin（巴蒂斯特·达鲁桑）（bapt@）在 freebsd-current 邮件列表提出讨论（约 2022-2023 年），理由包括：sendmail 配置复杂度远超普通用户需求、绝大多数 FreeBSD 安装不运行公开邮件服务器、OpenBSD 早已使用 smtpd、NetBSD 使用 postfix、DragonFly 使用 dma——FreeBSD 是最后一个仍以 sendmail 为默认的主流 BSD；**dma(8)** 代码量约为 sendmail 的十分之一，攻击面显著减小

## 史观

- 项目统摄史观：14.0 是 FreeBSD 历史上承前启后的关键一刻——它既是 FreeBSD 项目创立三十周年后的首个大版本，也是最后一个正式支持 32 位平台作为 RELEASE 架构的大版本系列；三十年前（1993.6.19）FreeBSD 1.0 从 386BSD 补丁包中诞生，三十年后的 14.0 站在向 64 位纯现代化转型的门槛上
  - 辨析：[双库核查：2026
- 总纲第 10 条——边缘者贡献：**dma(8)** 来自 DragonFly BSD——一个核心开发者长期仅个位数的 “边缘 BSD 分支”，却为整个 BSD 生态贡献了一个解决实际问题的工具；这印证了 BSD 生态中 “小项目解决大问题” 的传统：pf 来自 OpenBSD、HAMMER/HAMMER2 来自 DragonFly、pkg 来自 FreeBSD 自身但最初为独立项目——每个 BS
- 许可证：OpenSSL 许可证问题是 BSD 与 GPL 生态长达二十年的法律灰区——旧 OpenSSL 许可证（原 SSLeay 许可证 + OpenSSL 许可证的 “advertising clause”）与 GPL 不兼容，导致所有链接 OpenSSL 的 GPL 程序都需要特殊例外条款；Apache 2.0 许可证的采用彻底解决了这一问题，这一变化对整个开源生态的影响
- 项目统摄史观：block cloning 是 ZFS 设计哲学的自然延伸——ZFS 从诞生起就是写时复制（CoW）文件系统，块克隆是 CoW 语义在文件级克隆上的直接应用，而不是 “追赶 Btrfs reflinks” 的模仿；Bonwick 在 2005 年设计 ZFS 时架构上就为此类扩展预留了空间，这印证了 “面向未来设计” 的工程价值——18 年前的设计决策在今天依然能承

## 辨析

- [双库核查：2026-08-15] 14.0-RELEASE 发布日期（2023-11-20）经邮件列表库验证通过——Message-ID <20231120210317.5DB0E473C@freefall.freebsd.org>（2023-11-20T21:03:17+00:00），发件人 Colin Percival，主题 FreeBSD 14.0-RELEASE Now Available，
- 需澄清 “sendmail 被移除” 的误解——sendmail 在 14.0 中仍完整保留在 base system 中（包括 sendmail.cf 配置、makemap 等工具），只是默认 mailer.conf 指向 dma；这与 telnetd 在 14.0 中被完全移除（见 85.13）性质不同；〔待核：原文截断，后文待回源〕
- OpenSSL 3.0 的 FIPS provider 并非默认启用——FIPS 模式需要显式配置与安全策略激活，FreeBSD base 系统本身不持有 FIPS 140-2/140-3 认证，认证由各商业发行版（如 TrueNAS、pfSense 等基于 FreeBSD 的产品）自行申请；“FreeBSD 不持有 FIPS 认证” 是一个必须明确区分的事实——FreeBSD 作为社区项目不进行
- block cloning 有严格使用限制：源文件与目标文件必须在同一存储池（不能跨池克隆）、不能跨不同 ashift vdev、部分 RAID-Z 配置下有性能或功能限制；与快照/克隆的区别：zfs clone 是数据集级（文件系统/卷）的克隆，block cloning 是文件级的轻量级克隆；〔待核：原文截断，后文待回源〕

## 文献

- FreeBSD Project. FreeBSD 14.0-RELEASE Announcement [EB/OL]. (2023-11-20)[2026-07-19]. <https://www.freebsd.org/releases/14.0R/announce/>; FreeBSD Project. FreeBSD 14.0-RELEASE Release Notes [EB/OL]. (2023-11-20)[2026-07-19]. <https://www.freebsd.org/releases/14.0R/relnotes/>; FreeBSD Foundation. 202
- DragonFly BSD Project. dma(8) — DragonFly Mail Agent [EB/OL]. [2026-07-19]. <https://www.dragonflybsd.org/>; FreeBSD Project. mailer.conf(5) Manual Page [EB/OL]. [2026-07-19]. <https://man.freebsd.org/mailer.conf/5>; Costales B, Allman E. sendmail (4th Edition)[M]. O'Reilly Media, 2007. ISBN 978-0-5
- OpenSSL Project. OpenSSL 3.0 Release Notes [EB/OL]. (2021-09-07)[2026-07-19]. <https://www.openssl.org/blog/blog/2021/09/07/OpenSSL300/>; OpenSSL Project. OpenSSL License Change [EB/OL]. [2026-07-19]. <https://www.openssl.org/blog/blog/2017/11/04/apache/>; NIST. Cryptographic Module Validation Progr
- OpenZFS Project. OpenZFS 2.2.0 Release Notes [EB/OL]. (2023-10-12)[2026-07-19]. <https://github.com/openzfs/zfs/releases/tag/zfs-2.2.0>; Ahrens M. OpenZFS Block Cloning Design [C]. OpenZFS Developer Summit 2022/2023; FreeBSD Project. cp(1) Manual Page [EB/OL]. [2026-07-19]. <<https://man.freebsd.org/>


<!-- dangan-20260908 消解回写 -->
- Venema. W. postfix Architecture Overview [EB/OL]. [2026-07-19]. <http://www.postfix.org/>[EB/OL]. 2026. ［待核·needs_fix］［DKC-2256→fulltext:6125］
<!-- /dangan-20260908 -->
## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-590 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-590`；w172 YouTube 章节路由采纳）

据〔June 2021 FreeBSD Developer Summit〕讲者口述：FreeBSD 部分由 FreeBSD 上游，ZFS 部分通过 OpenZFS 上游（YouTube EPhm_S0jInF6U，[662.16-668.389]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2005 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2005`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD 开发者峰会“14.0 规划”场〕讲者口述：主讲人参照 FreeBSD 12 与 13 之间的发布间隔，个人猜测 14.0 会在 2023 年某个时候发布，或许在 10 月前后；他同时强调 14.0 尚未在任何地方定下日期。（YouTube EP7LhcQDkUHN4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2006 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2006`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD 开发者峰会“14.0 规划”场〕讲者口述：有人私下回复主讲人称 14.0 或许在 7 月至 10 月之间发布，因此本次规划会以“2023 年年中”作为功能落地的目标时间范围。（YouTube EP7LhcQDkUHN4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2007 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2007`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD 开发者峰会“14.0 规划”场〕讲者口述：bhyve 的 arm64 支持由 Andy 同时为 FreeBSD 基金会与 cambridge 两条路径推进，其分支已放在 GitHub；主讲人确认该工作已存在，并预期会在 2023 年之前合入主线。（YouTube EP7LhcQDkUHN4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2008 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2008`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD 开发者峰会“14.0 规划”场〕讲者口述：FreeBSD 的 ZFS 硬件加速摘要方案基本是用 ocf 来做摘要；主讲人当时已看过相关进展，其中大部分改动是向 OpenZFS 上游提出的合并请求，内容只是修正 ocf 自身若干错误的断言。（YouTube EP7LhcQDkUHN4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2149 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2149`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD Developer Summit 14.0 Planning 第二场〕讲者口述：FireWire 支持被提议从 FreeBSD 淘汰——它有一批遗留问题，且已开始影响 CAM 层，使用人数不多，也没有人在维护，因此应当直接移除。（YouTube EPtpR0xyOPhpQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2150 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2150`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD Developer Summit 14.0 Planning 第二场〕讲者口述：非 EFI 的 x86 boot loader 有一个约 500K 的硬性容量上限，loader 里塞的东西越来越多，若要 PXE 引导往往得自行构建定制的 loader EFI。（YouTube EPtpR0xyOPhpQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2151 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2151`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD Developer Summit 14.0 Planning 第二场〕讲者口述：在讨论 FreeBSD base 是否移除 ftpd 时，转述称 Red Hat 已移除 ftpd 并且正在移除 FTP 客户端，Google 与 Mozilla 正把 FTP 协议从浏览器中移除、该协议已被弃用，至少在 Chrome 里已经没有了。（YouTube EPtpR0xyOPhpQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2152 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2152`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 FreeBSD Developer Summit 14.0 Planning 第二场〕讲者口述：telnetd 与 ftpd 的客户端、服务器版都已搬进 Ports，且 GitHub 仓库经压缩处理后仍保留完整提交历史、可回溯至 epoch，因此 FreeBSD 可以据需要把二者从 base 移走。（YouTube EPtpR0xyOPhpQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
