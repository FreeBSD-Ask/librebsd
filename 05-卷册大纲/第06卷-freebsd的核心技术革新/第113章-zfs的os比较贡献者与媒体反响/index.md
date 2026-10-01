---
chapter: 第 113 章
id: CH113
volume: 第06卷-freebsd的核心技术革新
---

# 第113章 zfs的os比较贡献者与媒体反响

## 要点

- Btrfs（B-tree file system，常读作“Butter FS”或“B-tree FS”）由 Chris Mason 于 2007 年在 Oracle 工作期间启动开发，设计目标是打造 Linux 原生的下一代 CoW 文件系统，提供与 ZFS 类似的功能（快照、校验、池化、RAID）；Btrfs 于 Linux 2.6.29（2009 年）合入主线内核，标记为 experimental；Btrfs 与 ZFS 的核心技术差异：（1）许可：Btrfs 采用 GPLv2（与 Linux 内核一致），可以直接进入 upstream；（2）设计：Btrfs 基于 B-tree 结构，ZFS 基于 Merkle 树 + 块指针；（3）成熟度：Btrfs 的 RAID 5/6 实现长期被标记为不稳定（存在 write hole 问题），直到 2020 年代仍有许多生产环境警告；（4）功能覆盖：Btrfs 缺少 ZFS 的一些企业级功能（如 send/recv 增量流虽然支持但不完整、无 ZIL/SLOG 分离等）；Red Hat 在 RHEL 中从 RHEL 6/7 开始将 Btrfs 列为 technology preview，但在 RHEL 8（2019 年）中移除了 Btrfs 支持，转而支持 Stratis（基于 XFS+LVM）
- 2005-2026 年间同期主要文件系统时间线：ext4 由 Theodore Ts’o（Ted Ts’o）开发，基于 ext3 扩展，Linux 2.6.28（2008 年 12 月）标记为稳定，是 RHEL 6/7/8/9 和多数 Linux 发行版的默认文件系统，采用日志而非 CoW 设计；XFS 最初由 SGI 为 IRIX 开发（1994 年），2001 年移植到 Linux，由 Red Hat 主导维护，是高性能 64 位日志文件系统，RHEL 7+ 默认文件系统；ReiserFS 由 Hans Reiser 开发（2001 年合入 Linux），但 Reiser 谋杀案后维护停滞，Reiser4 从未进入主线；Btrfs（2007 年启动，前述）；HAMMER（2008 年，DragonFly BSD）；HAMMER2（2018 年默认，DragonFly BSD）；ReFS（Resilient File System）由 Microsoft 于 Windows Server 2012 引入，是 Windows 的 CoW 文件系统，借鉴了 ZFS/Btrfs 的许多概念但仅限 Windows Server，不支持引导；APFS（Apple File System）由 Apple 于 2017 年发布（macOS 10.13/iOS 10.3），取代 HFS+，是 CoW 文件系统，支持快照、加密、空间共享，但不提供 ZFS 级别的池化/RAID；OpenZFS 成为跨平台统一代码库（2020 年 OpenZFS 2.0）
- FreeBSD ZFS 的法律确定性是其在所有平台中独有的优势：（1）BSD 许可与 CDDL 许可明确兼容——CDDL §3.5 允许与其他许可证的代码聚合，FreeBSD Foundation 和核心团队从未质疑 ZFS 在 FreeBSD base system 中的法律地位；（2）FreeBSD 将 ZFS 纳入 base system（2007 年起），不是作为可选模块或 DKMS 包，由 FreeBSD committer 直接维护，与内核同步更新；（3）FreeBSD 项目有统一的治理结构，核心团队明确支持 ZFS，没有 Linux 世界中“创始人 vs 发行版 vs 用户”的分裂；（4）相比之下：Linux 上 ZFS 始终是 out-of-tree 模块，受内核 API 变更影响，许可问题从未获得司法裁决，发行版支持差异大（Ubuntu 支持、Red Hat 不支持、Debian 在 main/contrib 之间反复）；macOS 上 ZFS（OpenZFS on OS X/macOS）是第三方移植，非 Apple 官方支持；Windows 上 OpenZFS 端口（2020 年代）同样是社区项目，非 Microsoft 支持；FreeBSD 成为 ZFS 法律和工程确定性最强的生产级平台
- 各文件系统关键史实与交叉验证以要点条目分散呈现：ext4、XFS、ReiserFS、HAMMER/HAMMER2、ReFS、APFS 见时间线要点，Btrfs 与 ZFS 的许可、设计、成熟度差异见专条要点，不设汇总对照表。
- ZFS 在各平台的早期移植者：（1）Pawel Dawidek（pjd@）——FreeBSD ZFS 移植的核心开发者，波兰开发者，FreeBSD committer，2006-2007 年完成 ZFS 到 FreeBSD 的移植，包括 Solaris API 兼容层（solaris/ directory），commit r177621（2008 年 3 月）是关键里程碑；（2）Brian Behlendorf（布莱恩·贝伦多夫）——ZFS on Linux（ZoL）创始人，2008 年启动 Linux 移植，LLNL（Lawrence Livermore National Laboratory）雇员，其工作使 ZFS 在 Linux 上可用，ZoL 后来成为 OpenZFS 2.0 的基础代码库；（3）illumos 社区——2010 年 Oracle 关闭 OpenSolaris 后，Garrett D’Amore（加勒特·达莫尔） 等人发起 illumos fork，维护 OpenSolaris 代码继续发展，成为 ZFS 上游的重要来源；（4）Matt Ahrens——ZFS 联合设计者，Bonwick 离开 Sun/Oracle 后 Ahrens 成为 OpenZFS 社区技术领袖之一，Delphix 公司雇员，持续贡献 ZFS 代码至今；（5）其他重要移植者：Adam Leventhal（Delphix）、George Wilson（Delphix/Oracle）、Andriy Gapon（FreeBSD ZFS 维护者）、Martin Matuska（FreeBSD ZFS，后加入 OpenZFS 协调）

## 史观

- 总纲第 13 条——法律与道德是利益分配：Btrfs 的诞生很大程度上是为了在 Linux 内核中“绕过”ZFS 的 CDDL 许可问题——Oracle 作为 ZFS 版权持有者，选择重新开发一个 GPL 许可的 CoW 文件系统，这本身就是 CDDL-GPL 不兼容如何塑造技术生态的最好例证
- 总纲第 18 条——时间是一种形式主义：文件系统发展史的形式化记录（版本号、发布日期、commit hash）是历史书写的基础，没有精确的时间锚点，技术叙事就会退化为模糊的技术传奇
- 总纲第 10 条——动手者创造历史：ZFS 的延续不是由 Sun/Oracle 决定的，而是由一群分散在不同公司和社区的开发者共同维系的——Dawidek 在波兰、Behlendorf 在 LLNL、Ahrens 在 Delphix、illumos 社区独立 fork，这些 “边缘者” 的努力使得 ZFS 在 Oracle 闭源后得以延续和发展

## 辨析

- Btrfs 稳定性的争议：Btrfs 在单盘场景下已经相当稳定（被 openSUSE/SUSE 作为默认文件系统多年），但其多盘 RAID 功能的稳定性长期被质疑；这与 ZFS 在所有模式下（包括 RAID-Z）都以生产稳定著称形成对比；Btrfs 的 write hole 问题（RAID 5/6 模式下的原子性问题）直到 2023 年前后才通过新的日志机制部分解决
- 需注意各文件系统“稳定”的定义差异——ext4 在 2008 年即被标记为 stable 并被发行版大量采用；Btrfs 虽合入主线但 RAID 5/6 长期不稳定；ZFS 在 Solaris 中 2006 年即被视为 production ready，在 FreeBSD 中 7.0 标记为 experimental、8.0 production ready；HAMMER 在 DragonFly
- ZFS 移植的历史常被简化为 “Pawel Dawidek 移植到 FreeBSD”，但实际上早期 ZFS 移植是多人协作：Dawidek 是核心人物，但罗伯特·N. M. 沃森（Robert Watson）、Kip Macy 等人也参与了早期工作；ZoL 早期并非 “官方” 移植，而是 Behlendorf 的个人/LLNL 项目，直到 2010 年代中期才获得广泛认可

## 文献

- Mason, C. (2007). *Btrfs: The Linux B-tree Filesystem*. LWN.net; Btrfs Wiki. btrfs.wiki.kernel.org; Red Hat (2019). *RHEL 8 Release Notes - Deprecated Functionality*. redhat.com. ［B］
- FreeBSD 社区论文与演讲：Piotrowski M. ZFS Direct IO Benchmarking Pitfalls[C]//BSDCan 2025. Ottawa, 2025.
- USENIX Conference on File and Storage Technologies (FAST) Proceedings [C/OL]. 获取路径：<https://www.usenix.org/conferences/byname/925> [访问日期 2026-07-30]; 各文件系统项目官方文档。［D］
- FreeBSD Project. *SVN Commit History*. svnweb.freebsd.org; OpenZFS. *Contributor History*. openzfs.org; Behlendorf, B. (2013). *ZFS on Linux: Past, Present, and Future*. LinuxCon 2013. ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP354、BSD Now EP31（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 11.4 进入 RC2，camcontrol、freebsd-update、ZFS 书签重命名、certctl 等更新随 11.4 与 12.2 推出。（BSD Now EP354，[66.04-186.90]，L2）
- Jim Salter 的 Ars Technica 文章以 1.9TB 虚拟机镜像为例比较 ZFS 复制与 rsync：ZFS 靠块出生时间与快照可在 8 秒内完成，而 rsync 需约 2.5 小时。（BSD Now EP354，[474.62-667.52]，L2）
- Colin Percival 自 2008 年起主导 FreeBSD 移植至 Amazon EC2，并持续维护至今。（BSD Now EP354，[674.30-747.26]，L2）
- FreeBSD 项目发起 2020 年社区调查，以量化数据引导项目优先事项与努力方向。（BSD Now EP354，[756.54-846.94]，L2）
- 本期发布于2014年4月1日，开场以采访Richard Stallman谈论GPL v4为愚人节玩笑，随后转入常规新闻与问答，玩笑部分不应作为事实采信。（BSD Now EP31，[3.3-18.0]，L2） [订正：原 [0.0-11.80]，2026-09-30 SenseAudio 重转核对]
- 主持人 Alan Jude 表示曾就此问题询问 ZFS 创建者 Matt Ahrens，得到的回答是：即便无法负担 ECC 内存，ZFS 仍是较好选择，因为磁盘校验与冗余能检测并修正由内存错误导致的不匹配。（BSD Now EP31，[510.88-548.24]，L2）
- 讨论指出ZFS scrub是只读操作，内存错误通常只影响极小比例读取，ZFS会把问题归因于磁盘并以冗余副本覆盖，而不会主动破坏数据。（BSD Now EP31，[566.52-594.32]，L2）
- ECC内存的主要价值在于减少随机内核panic，而ZFS的copy-on-write设计使意外中断不致像原地覆写文件系统那样产生撕裂写，最多回退到最近一次flush的状态。（BSD Now EP31，[599.12-662.56]，L2）
- 主持人指出 Btrfs 阵营以 ZFS 必须使用企业级硬件为由的论调没有根据，两人均表示在笔记本电脑等无 ECC 硬件上长期运行 ZFS。（BSD Now EP31，[706.32-739.06]，L2）
- 当期新闻提及 BSD Mag 2014 年 3 月刊内容，包括以 NetBSD 部署 AWS EC2、NetBSD 多功能文件服务器、DragonFly BSD 备份服务器、Wireshark 网络分析与安全文章。（BSD Now EP31，[450.68-488.92]，L2）
- 当期提及《FreeBSD 操作系统设计与实现》（第二版）出版，旧版第一版面向 FreeBSD 5，凸显 BSD 经典技术图书的版本跨度。（BSD Now EP31，[85.28-126.32]，L2）

**史料**：

- Jim Salter 在 Ars Technica 的 OpenZFS 指南及 syncoid 工具说明。（BSD Now EP354，[474.62-597.86]，L2）
- 关于 Colin Percival 的播客访谈，介绍其 Tarsnap 创立、AWS 使用经验与 FreeBSD 安全官经历。（BSD Now EP354，[674.30-747.26]，L2）
- 主持人转述其向Matt Ahrens当面询问ZFS与ECC问题的经过，构成ZFS创建者观点的一手转述来源。（BSD Now EP31，[510.88-548.24]，L2）
- 当期引用的文章包括一篇关于非ECC内存下使用FreeNAS/ZFS的博客，以及BSD Mag 2014年3月刊目录与FreeBSD设计实现第二版信息。（BSD Now EP31，[85.28-518.46]，L2）

**史观**：

- 总纲9 经验优先：ZFS 复制对 rsync 的优势来自块级快照的实际经验，而非理论推断。（BSD Now EP354，[560.26-667.52]，L2）
- 总纲3 不存在进步，只有权力再分配：社区调查旨在重新分配开发优先级，体现技术方向由使用数据而非线性进步主导。（BSD Now EP354，[756.54-846.94]，L2）
- 总纲9 经验优先：讨论以当事人与非ECC硬件上长期运行ZFS的实际经验，反驳ZFS必须使用企业级硬件的抽象论断。（BSD Now EP31，[678.44-739.06]，L3）
- 总纲5 没有必然性，只有偶然性：内存错误的发生与影响被描述为小概率、局部的偶然事件，而非必然导致数据灾难。（BSD Now EP31，[577.86-594.32]，L3）
- 总纲8 本体论上各方平等：对 Btrfs 阵营论调的回应不以贬低竞争者建立结论，而是以校验与copy-on-write机制说明ZFS在不同硬件条件下的行为。（BSD Now EP31，[706.32-750.48]，L3）

**辨析**：

- 转写中“8 秒对 2.5 小时、1150 倍”为作者特定场景的实测数据，主持人亦提示学术上此类极端比值需谨慎看待。　[存疑脚注] 极端比值需结合具体场景理解（BSD Now EP354，[615.14-641.14]，L4）
- 当期开场为愚人节玩笑，若脱离日期语境可能被误当作对Richard Stallman与GPL v4的真实报道；同时主持人转述Matt Ahrens观点属二手转述，需以原始访谈或文字记录交叉核对。　[存疑脚注] 愚人节玩笑不可作为事实；Matt Ahrens关于ZFS与ECC的表述亦为节目主持人的口头转述。（BSD Now EP31，[3.3-18.0]，L4） [订正：原 [0.0-11.80]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP354] Pennington J. BSD Now: 354: ZFS safekeeps data[EB/OL]. (2020-06-11)[2026-08-15]. <https://www.bsdnow.tv/354>.
- [BSD Now EP31] Pennington J. BSD Now: 31: Edgy BSD Users[EB/OL]. (2014-04-01)[2026-08-15]. <https://www.bsdnow.tv/31>.

<!-- /PODCAST_REVIEW -->
