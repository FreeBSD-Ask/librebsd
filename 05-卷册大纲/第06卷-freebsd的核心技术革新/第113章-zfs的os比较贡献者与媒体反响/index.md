---
chapter: 第 113 章
id: CH113
volume: 06
---

# 第113章 zfs的os比较贡献者与媒体反响

## 要点

- Btrfs（B-tree file system，常读作"Butter FS"或"B-tree FS"）由 Chris Mason 于 2007 年在 Oracle 工作期间启动开发，设计目标是打造 Linux 原生的下一代 CoW 文件系统，提供与 ZFS 类似的功能（快照、校验、池化、RAID）；Btrfs 于 Linux 2.6.29（2009 年）合入主线内核，标记为 experimental；Btrfs 与 ZFS 的核心技术差异：（1）许可：Btrfs 采用 GPLv2（与 Linux 内核一致），可以直接进入 upstream；（2）设计：Btrfs 基于 B-tree 结构，ZFS 基于 Merkle 树 + 块指针；（3）成熟度：Btrfs 的 RAID 5/6 实现长期被标记为不稳定（存在 write hole 问题），直到 2020 年代仍有许多生产环境警告；（4）功能覆盖：Btrfs 缺少 ZFS 的一些企业级功能（如 send/recv 增量流虽然支持但不完整、无 ZIL/SLOG 分离等）；Red Hat 在 RHEL 中从 RHEL 6/7 开始将 Btrfs 列为 technology preview，但在 RHEL 8（2019 年）中移除了 Btrfs 支持，转而支持 Stratis（基于 XFS+LVM）
- 2005-2026 年间同期主要文件系统时间线：ext4 由 Theodore Ts'o（Ted Ts'o）开发，基于 ext3 扩展，Linux 2.6.28（2008 年 12 月）标记为稳定，是 RHEL 6/7/8/9 和多数 Linux 发行版的默认文件系统，采用日志而非 CoW 设计；XFS 最初由 SGI 为 IRIX 开发（1994 年），2001 年移植到 Linux，由 Red Hat 主导维护，是高性能 64 位日志文件系统，RHEL 7+ 默认文件系统；ReiserFS 由 Hans Reiser 开发（2001 年合入 Linux），但 Reiser 谋杀案后维护停滞，Reiser4 从未进入主线；Btrfs（2007 年启动，前述）；HAMMER（2008 年，DragonFly BSD）；HAMMER2（2018 年默认，DragonFly BSD）；ReFS（Resilient File System）由 Microsoft 于 Windows Server 2012 引入，是 Windows 的 CoW 文件系统，借鉴了 ZFS/Btrfs 的许多概念但仅限 Windows Server，不支持引导；APFS（Apple File System）由 Apple 于 2017 年发布（macOS 10.13/iOS 10.3），取代 HFS+，是 CoW 文件系统，支持快照、加密、空间共享，但不提供 ZFS 级别的池化/RAID；OpenZFS 成为跨平台统一代码库（2020 年 OpenZFS 2.0）
- FreeBSD ZFS 的法律确定性是其在所有平台中独有的优势：（1）BSD 许可与 CDDL 许可明确兼容——CDDL §3.5 允许与其他许可证的代码聚合，FreeBSD Foundation 和核心团队从未质疑 ZFS 在 FreeBSD base system 中的法律地位；（2）FreeBSD 将 ZFS 纳入 base system（2007 年起），不是作为可选模块或 DKMS 包，由 FreeBSD committer 直接维护，与内核同步更新；（3）FreeBSD 项目有统一的治理结构，核心团队明确支持 ZFS，没有 Linux 世界中“创始人 vs 发行版 vs 用户”的分裂；（4）相比之下：Linux 上 ZFS 始终是 out-of-tree 模块，受内核 API 变更影响，许可问题从未获得司法裁决，发行版支持差异大（Ubuntu 支持、Red Hat 不支持、Debian 在 main/contrib 之间反复）；macOS 上 ZFS（OpenZFS on OS X/macOS）是第三方移植，非 Apple 官方支持；Windows 上 OpenZFS 端口（2020 年代）同样是社区项目，非 Microsoft 支持；FreeBSD 成为 ZFS 法律和工程确定性最强的生产级平台
- 各文件系统关键史实汇总与交叉验证见下表，覆盖 ZFS、Btrfs、ext4、XFS、HAMMER/HAMMER2、ReFS、APFS 共 8 个 2005-2026 年间主流文件系统的启动时间、主要里程碑与当前状态。
- ZFS 在各平台的早期移植者：（1）Pawel Dawidek（pjd@）——FreeBSD ZFS 移植的核心开发者，波兰开发者，FreeBSD committer，2006-2007 年完成 ZFS 到 FreeBSD 的移植，包括 Solaris API 兼容层（solaris/ directory），commit r177621（2008 年 3 月）是关键里程碑；（2）Brian Behlendorf（布莱恩·贝伦多夫）——ZFS on Linux（ZoL）创始人，2008 年启动 Linux 移植，LLNL（Lawrence Livermore National Laboratory）雇员，其工作使 ZFS 在 Linux 上可用，ZoL 后来成为 OpenZFS 2.0 的基础代码库；（3）illumos 社区——2010 年 Oracle 关闭 OpenSolaris 后，Garrett D'Amore（加勒特·达莫尔） 等人发起 illumos fork，维护 OpenSolaris 代码继续发展，成为 ZFS 上游的重要来源；（4）Matt Ahrens——ZFS 联合设计者，Bonwick 离开 Sun/Oracle 后 Ahrens 成为 OpenZFS 社区技术领袖之一，Delphix 公司雇员，持续贡献 ZFS 代码至今；（5）其他重要移植者：Adam Leventhal（Delphix）、George Wilson（Delphix/Oracle）、Andriy Gapon（FreeBSD ZFS 维护者）、Martin Matuska（FreeBSD ZFS，后加入 OpenZFS 协调）

## 史观

- 总纲第 24 条——许可证：Btrfs 的诞生很大程度上是为了在 Linux 内核中“绕过”ZFS 的 CDDL 许可问题——Oracle 作为 ZFS 版权持有者，选择重新开发一个 GPL 许可的 CoW 文件系统，这本身就是 CDDL-GPL 不兼容如何塑造技术生态的最好例证
  - 辨析：Btrfs 稳定性的争议：Btrfs 在单盘场景下已经相当稳定（被 openSUSE/SUSE 作为默认
- 总纲第 3 条——形式主义膨胀：文件系统发展史的形式化记录（版本号、发布日期、commit hash）是历史书写的基础，没有精确的时间锚点，技术叙事就会退化为模糊的技术传奇
- 辨析：需注意各文件系统“稳定”的定义差异——ext4 在 2008 年即被标记为 stable 并被发行版大量采用；Btrfs 虽合入主线但 RAID 5/6 长期不稳定；ZFS 在 Solaris 中 2006 年即被视
- 总纲第 25 条——终结与延续：ZFS 的延续不是由 Sun/Oracle 决定的，而是由一群分散在不同公司和社区的开发者共同维系的——Dawidek 在波兰、Behlendorf 在 LLNL、Ahrens 在 Delphix、illumos 社区独立 fork，这些 “边缘者” 的努力使得 ZFS 在 Oracle 闭源后得以延续和发展
  - 辨析：ZFS 移植的历史常被简化为 “Pawel

## 辨析

- Btrfs 稳定性的争议：Btrfs 在单盘场景下已经相当稳定（被 openSUSE/SUSE 作为默认文件系统多年），但其多盘 RAID 功能的稳定性长期被质疑；这与 ZFS 在所有模式下（包括 RAID-Z）都以生产稳定著称形成对比；Btrfs 的 write hole 问题（RAID 5/6 模式下的原子性问题）直到 2023 年前后才通过新的日志机制部分解决
  - 文献：Mason, C
- 需注意各文件系统“稳定”的定义差异——ext4 在 2008 年即被标记为 stable 并被发行版大量采用；Btrfs 虽合入主线但 RAID 5/6 长期不稳定；ZFS 在 Solaris 中 2006 年即被视为 production ready，在 FreeBSD 中 7.0 标记为 experimental、8.0 production ready；HAMMER 在 DragonFly
- ZFS 移植的历史常被简化为 “Pawel Dawidek 移植到 FreeBSD”，但实际上早期 ZFS 移植是多人协作：Dawidek 是核心人物，但罗伯特·N. M. 沃森（Robert Watson）、Kip Macy 等人也参与了早期工作；ZoL 早期并非 “官方” 移植，而是 Behlendorf 的个人/LLNL 项目，直到 2010 年代中期才获得广泛认可
  - 文献：FreeB

## 文献

- Mason, C. (2007). *Btrfs: The Linux B-tree Filesystem*. LWN.net; Btrfs Wiki. btrfs.wiki.kernel.org; Red Hat (2019). *RHEL 8 Release Notes - Deprecated Functionality*. redhat.com. ［B］
    FreeBSD 社区论文与演讲 [327]，[327] Mateusz Piotrowski. ZFS Direct IO Benchmarking Pitfalls [C]//BSDCan 2025. [S.l.]: [s.
- USENIX Conference on File and Storage Technologies (FAST) Proceedings [C/OL]. 获取路径：<https://www.usenix.org/conferences/byname/925> [访问日期 2026-07-30]; 各文件系统项目官方文档。［D］
- FreeBSD Project. *SVN Commit History*. svnweb.freebsd.org; OpenZFS. *Contributor History*. openzfs.org; Behlendorf, B. (2013). *ZFS on Linux: Past, Present, and Future*. LinuxCon 2013. ［A］
    FreeBSD 社区论文与演讲 [327]，[327] Mateusz Piotrowski. ZFS Direct IO Benchmarking Pitfalls [C]//BSDCan 2025. [S.l.

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
