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

- 转写中“8 秒对 2.5 小时、1150 倍”为作者特定场景的实测数据，主持人亦提示学术上此类极端比值需谨慎看待。 [存疑脚注] 极端比值需结合具体场景理解（BSD Now EP354，[615.14-641.14]，L4）
- 当期开场为愚人节玩笑，若脱离日期语境可能被误当作对Richard Stallman与GPL v4的真实报道；同时主持人转述Matt Ahrens观点属二手转述，需以原始访谈或文字记录交叉核对。 [存疑脚注] 愚人节玩笑不可作为事实；Matt Ahrens关于ZFS与ECC的表述亦为节目主持人的口头转述。（BSD Now EP31，[3.3-18.0]，L4） [订正：原 [0.0-11.80]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP354] Pennington J. BSD Now: 354: ZFS safekeeps data[EB/OL]. (2020-06-11)[2026-08-15]. <https://www.bsdnow.tv/354>.
- [BSD Now EP31] Pennington J. BSD Now: 31: Edgy BSD Users[EB/OL]. (2014-04-01)[2026-08-15]. <https://www.bsdnow.tv/31>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-280 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-280`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者提到 OpenZFS 2.3 近期引入长文件名支持这一新特性。（YouTube EP9Si69u0mOV0，[790.8-796.68]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-279 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-279`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：OpenZFS 通过 cherry-picked 特性支持 illumos、FreeBSD、GNU Linux、Mac OS、Windows、NetBSD 与 Solaris 多个平台。（YouTube EP9Si69u0mOV0，[17.36-31.36]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-430 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-430`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：讲者 Imtiaz Mohammad 指出，其最新一次测试未启用压缩、仅使用 128k 写入（转写音作 without ... without compression just 128k rights），此时 ZFS 仍存在若干问题，表现不及 OpenZFS 2.0（转写音作 open gfs 2.0）（YouTube EPDmJ0uxF0wes，[926.24-941.43]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-429 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-429`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：讲者 Imtiaz Mohammad 表示，其团队约两年前开始从事该 ZFS on Windows 工作时，open gfs 2.0 版本尚未发布。（YouTube EPDmJ0uxF0wes，[639.76-644.949]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-479 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-479`；w172 YouTube 章节路由采纳）

据〔2019-02-26 OpenZFS Leadership Meeting〕讲者口述：illumos 的 NFS hook 参数不被 FreeBSD 的 NFS hook 所理解。（YouTube EPEXstK9ckcZQ，[3576-3585.29]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-484 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-484`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：OpenZFS 设计目的是把各社区汇入统一伞下，新 GitHub 仓库基于 Illumos gate，允许通过 pull request 将增强汇入主干。（YouTube EPF7af6_wb4PU，[155.8-185.8]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-857 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-857`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者 Tarkan Maner 口述：他约 2 年前加入 Nexenta，此前已了解 ZFS，并称扩大 ZFS 用户基数是首要目标。（YouTube EPPWS1TR8X4Fo，[71.96-80.19]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-898 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-898`；w172 YouTube 章节路由采纳）

据 Michael Dexter 与 Jorgen Lundman 讲者口述：FreeBSD 是 ZFS 移植的早期参与者之一，而 NetBSD 的移植起步相对滞后，两者形成明显的先后差距。（YouTube EPRc-9QmUlDXs，[114.32-118.95]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1328 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1328`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者自述其在 ZFS 上工作（转写讹作 'ZF'），并称这是其选择该课题的主要原因之一；转写标题逐字载明 'Scrub/Resilver Performance by Saso Kiselkov'。（YouTube EPSZFwv8BdBj4，[4.4-14.3]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-979 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-979`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者称其旧机器上运行 Lustre 2.5，下层为 ZFS 0.6.5（以 Lustre 承托 ZFS）。（YouTube EPTyA0EKhGRsE，[89.76-100.39]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-980 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-980`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者称其另有环境运行 Lustre 2.8，底层为 ZFS 0.7.9，且通常跟随最新发行版。（YouTube EPTyA0EKhGRsE，[103.2-110.35]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1013 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1013`；w172 YouTube 章节路由采纳）

据〔OpenZFS 开发者峰会 2014〕讲者 Prakash Surya 口述：OpenZFS 项目于 2013 年创建。（YouTube EPUtlGt3ag0o0，[49.8-53.7]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1216 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1216`；w172 YouTube 章节路由采纳）

据〔系统性能分析方法论主题演讲〕讲者 Brendan Gregg 口述：其旧图出自 Solaris，包含其编写的多个 DTrace 工具（YouTube EPZNkFDHLQnrA，[3305.019-3314.309]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-329 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-329`；w172 YouTube 章节路由采纳）

据〔2022年12月 OpenZFS 领导组会议〕讲者口述：FreeBSD 的 VFS 层已有名为 rctl 的类似机制（YouTube EPatbW3Ecqm5s，[1191.66-1195.909]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-339 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-339`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Richard Elling 口述：在 Solaris 与 Illumos（转写音作“Solaris alumina”）体系内，ZFS 的可观测性采用 DTrace（YouTube EPb5awF6SVNwI，[1796.8-1801.5]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-505 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-505`；w172 YouTube 章节路由采纳）

据〔August 2022 OpenZFS Leadership Meeting〕讲者口述：FreeBSD 上也有对应的 exports 文件，转写音作 Etc ZFS exports（读作 /etc/zfs/exports，确切文件名转写存疑）。（YouTube EPfi_ZKc_od54，[903.24-911.569]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-516 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-516`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Satabdi Das 口述：某些元数据密集型负载会使 ARC 大小远超所配置的 zfs_arc_max 值（YouTube EPfqQ95LlwOGg，[1029.48-1039.189]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-514 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-514`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Satabdi Das 口述：该 OpenZFS 之上的文件系统实现支持 NFS v3、v4.1 与 v4.2 协议（转写音作 V3 for 4.1 and 4.2）（YouTube EPfqQ95LlwOGg，[116.7-125.87]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-515 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-515`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Satabdi Das 口述：讲者称其团队于 2021 年 12 月推出 FSX for OpenZFS（转写音作“FSX for open CFS”；本条视频标题为 Operating OpenZFS at Scale）。（YouTube EPfqQ95LlwOGg，[69.18-77.149]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-584 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-584`；w172 YouTube 章节路由采纳）

据〔February 2022 OpenZFS Leadership Meeting〕讲者口述：讨论提到在 Linux 上实现类似 FreeBSD jail 或 illumos zone（转写音作 alumos）的隔离能力。（YouTube EPhij7PGGjevc，[3530.96-3537.51]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-585 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-585`；w172 YouTube 章节路由采纳）

据〔February 2022 OpenZFS Leadership Meeting〕讲者口述：zfs clone 这一文件功能最初位于 FreeBSD。（YouTube EPhij7PGGjevc，[262-266.95]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-810 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-810`；w172 YouTube 章节路由采纳）

据〔Sandboxing OpenZFS on Linux 报告（来源不详）〕讲者 Albert Lee 口述：该沙箱引入前，FreeBSD 已有同类设施 jails。（YouTube EPokF7D6lr2BI，[83.96-89.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-883 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-883`；w172 YouTube 章节路由采纳）

据〔December 2024 OpenZFS Leadership Meeting〕讲者口述：FreeBSD 另有一种 unlink（转写音作 you unlink）标志，文件属主可设置与清除它，而 ZFS 目前不支持。（YouTube EPqQcSXScRo6s，[866.199-875.949]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-996 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-996`；w172 YouTube 章节路由采纳）

据讲者口述：讲者来自 Delphix，分享在 illumos 与 Linux 上调试 ZFS 的经验。（YouTube EPuDDJnzSb-2w，[11.889-20.099]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1491 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1491`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Cross Platform Parallel Regression and Performance Testing of, and with OpenZFS, FreeBSD and bhyve〕讲者口述：讲者在“ZFS 这一维度”上列出的被测对象是——跑 ZFS 的 FreeBSD 变体如今有“出人意料地多”种，而且每个 FreeBSD 版本线（上一个版本、当前版本、开发版本）都要覆盖，此外还有 ZFS on Linux 这一支，共同构成他的跨平台回归与性能比较矩阵。（YouTube EPQmNko8GrUxA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1492 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1492`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Cross Platform Parallel Regression and Performance Testing of, and with OpenZFS, FreeBSD and bhyve〕讲者口述：讲者把自由BSD（FreeBSD）上的 bhyve（转写音作 beehive）作为底层虚拟基础设施，称理论上 bhyve 可以把阵列存储经控制器直通（pass-through）到“完全同一份存储”上，从而使各平台的 OpenZFS 能在同一份介质上被同条件测试。（YouTube EPQmNko8GrUxA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1493 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1493`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Cross Platform Parallel Regression and Performance Testing of, and with OpenZFS, FreeBSD and bhyve〕讲者口述：讲者讲述为做早期版本回归而回溯自由BSD 历史时的遭遇——若干关键发行版本干脆缺失（flat-out missing），还存在 md5 校验和文件与实际文件对不上的情况，他认为这不可能是正常做法。（YouTube EPQmNko8GrUxA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1506 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1506`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2018 年 12 月 OpenZFS 领导层会议，ZFS on Linux 方面发言者（转写称 Brian Behlendorf，主持人称其为该平台事实上的领导）〕讲者口述：ZFS on Linux 曾长期落后于其他平台，追上它的好办法虽是“逐个提交地系统梳理”，但代价是工作量巨大、进度缓慢，且每个提交都必须另做平台特定修改。（YouTube EPTwCc9zjhRw4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1507 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1507`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2018 年 12 月 OpenZFS 领导层会议，illumos 方面发言者〕讲者口述：illumos/Joyent 的做法不是逐提交跟进，而是“diff 最小化”工程——取某一版 ZFS on Linux 状态与 illumos 的 guide 状态做一次大 diff，把相关片段挑出移植，目标是把差异缩小到还讲得通的范围。（YouTube EPTwCc9zjhRw4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1508 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1508`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2018 年 12 月 OpenZFS 领导层会议〕讲者口述：为让各平台尽早看见变更，讲者提出一种最低成本的做法是——新增命令行选项或改动用户界面时，在 open-zfs-dev 邮件列表发一条消息供各平台相关者审查；不是每个 bug 修复都要如此，但影响用户界面或磁盘格式（on-disk format）的改动应有最广泛的讨论可见性。（YouTube EPTwCc9zjhRw4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1509 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1509`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2018 年 12 月 OpenZFS 领导层会议〕讲者口述：在讨论“建池默认启用哪些特性”时，讲者反对一律默认关闭的特性集，理由是那样绝大多数人将用不上 LZ4 压缩——它是一项需手动启用的附加特性，默认压缩仍会退回旧算法；另有与会者主张默认启用全部特性，并为需跨平台迁移的池另设可移植（portable）模式。（YouTube EPTwCc9zjhRw4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2125 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2125`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2023 OpenZFS Leadership Meeting〕讲者口述：在实现面向 Linux 的 ZFS 挂载相关支持时，曾加入若干仅在 Linux 上实现、而 FreeBSD 未实现的新日志记录；当时决定不为实现而分叉，而是保持二者兼容，即允许某些操作系统（此处指 FreeBSD）出现尚未实现、不存在的日志记录。（YouTube EPLcHmXy34seA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2126 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2126`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2023 OpenZFS Leadership Meeting〕讲者口述：由于上述兼容策略，日志重放只会推进到第一条未知记录处便停止。（YouTube EPLcHmXy34seA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2127 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2127`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2023 OpenZFS Leadership Meeting〕讲者口述：若把在 Linux 上写入的池直接导入 FreeBSD，用户没有任何办法阻止该过程，被跳过的日志条目会被静默丢弃——系统只在日志里打印提示，但数据已经丢失。（YouTube EPLcHmXy34seA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2128 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2128`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2023 OpenZFS Leadership Meeting 共享 slog 提案发言〕讲者口述：其提出共享 slog（把多个池的日志写入一个独立池）的动因之一，是 ZFS 最初即通过把卷管理与文件系统集成来解决此类问题；共享 slog 相当于把卷管理思路与 slog 概念再做一层集成。（YouTube EPLcHmXy34seA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2552 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2552`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Jorgen Lundman《Porting OpenZFS to OSX and Windows》演讲〕讲者口述：OS X/Windows 版 OpenZFS 移植的讲述者自名 Jorgen Lundman（转写音作 Jurgen Ludemann），任职于东京的 GMO Internet；该公司 90 年代中期以 ISP 起家，先后称 Internet Quest（转写音作 inter queue）与 Global Media Online。（YouTube EP6_8jQnJf418，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2553 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2553`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Jorgen Lundman《Porting OpenZFS to OSX and Windows》演讲〕讲者口述：其 OS X 移植不允许调用苹果内核内存管理器的一半函数，故 SPL 改为直接向内核申请全部页，自带 slab 分配器、magazines 与 kmem 缓存（转写音作 came in）；既然借移植 ZFS 已引入半个 Illumos（转写音作 Loomis），索性把 kmem 也一并移植，由其团队开发者 Brendan 完成，并称这部分代码干净、移植相当容易。（YouTube EP6_8jQnJf418，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2554 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2554`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Jorgen Lundman《Porting OpenZFS to OSX and Windows》演讲〕讲者口述：OpenZFS on OS X 直接与 OpenZFS 主仓库保持上游同步——只要 Matt 批准新特性、PR 或 commit，几小时后即以 cherry-pick 方式拉入，并自嘲“多亏时区，技术上我们总是最先拿到所有特性”。（YouTube EP6_8jQnJf418，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2555 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2555`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Jorgen Lundman《Porting OpenZFS to OSX and Windows》演讲〕讲者口述：答问时对比两次移植耗时——OS X 移植约一年才做到第一次存储池导入，Windows 移植 2 月开始、7 月完成（转写未给出年份）；他自述 Windows 阶段之所以更快，是因为彼时已熟悉 SPL 与 ZFS，只剩 Windows 内核这块未知。（YouTube EP6_8jQnJf418，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2564 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2564`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sam Atkinson 演讲〕讲者口述：其团队在争取更多 AWS 工程师工时投入 OpenZFS 代码，跟进与自身相关的 issue 报告并上游化更多缺陷修复与改进；他坦言此事有挑战但正在推进。（YouTube EP6Jt9LQcobXM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2565 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2565`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sam Atkinson 演讲〕讲者口述：其体感 OpenZFS 上游发布速度很高、节奏快，并称 AWS 所提供的许多其他文件系统的上游发布速度远不及此。（YouTube EP6Jt9LQcobXM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2698 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2698`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2020 OpenZFS Leadership Meeting〕与会者口述：illumos 与 Linux 上 ZFS send 相关线程都以最低可用优先级创建，但 illumos 上所有内核线程优先级都高于所有用户态线程，Linux 则共享同一优先级空间——同一代码在 Linux 上实际优先级低得多。（YouTube EPupUOXBhx-us，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2699 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2699`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2020 OpenZFS Leadership Meeting〕与会者口述：就线程优先级行为而言，三大平台中 Linux 是异类； FreeBSD（转写音含混）更接近 illumos——内核线程不走分时、实际上是固定优先级。（YouTube EPupUOXBhx-us，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2700 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2700`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔February 2020 OpenZFS Leadership Meeting〕与会者口述：对旧版写入、新版不认识的属性值，新版 ZFS 可以逐类消化——见到不认识的属性值时显示 unknown 并回落默认值，避免属性集合把新版搞糊涂。（YouTube EPupUOXBhx-us，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
