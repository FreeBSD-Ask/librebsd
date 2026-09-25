### 宿主键 11210 = 节 112.10
节题：112.10 ZFS 在各版本 FreeBSD 中的演进——lz4 压缩、加密、克隆发送（zfs send -I）、书签、持久化 L2ARC、池检查点、池拆除（vdev removal）、特殊 vdev、克隆迁移
范围：**要点**：ZFS 早期版本仅支持 lzjb（Bonwick 自研的轻量压缩算法）和 gzip 压缩；lz4 压缩（由 Yann Collet 开发的高速压缩算法）于 2013 年前后在 illumos 中引入，随后同步到 FreeBSD 和 ZoL，lz4 压缩比 lzjb 压缩比更高但速度更快，成为 ZFS 默认推荐压缩算法；ZFS 原生加密（native encryption）在 OpenZFS 0.8（2019 年）中正式引入，支持 aes-128-ccm、aes-192-ccm、aes-256-ccm、aes-128-gcm、aes-192-gcm、aes-256-gcm 等加密套件，加密在数据集级别设置，加密元数据但不包括数据集名称、属性和快照结构；zstd 压缩（由 Yann Collet 开发，Facebook 支持）在 OpenZFS 2.0（2020 年）中引入，提供比 lz4 更高的压缩比和灵活的压缩级别选择

**史料**：illumos commit 记录（lz4 集成，约 2013 年）；OpenZFS 0.8 Release Notes（2019 年，原生加密）；OpenZFS 2.0 Release Notes（2020 年，zstd）；lz4 作者 Yann Collet 的 lz4 项目 GitHub（github.com/lz4/lz4）；zstd 项目 GitHub（github.com/facebook/zstd） ［A］

**史观**：总纲第 13 条——法律与道德是利益分配：lz4（BSD-2-Clause/GPLv2 双许可）和 zstd（BSD-3-Clause/GPLv2 双许可）都是宽松许可，可以自由合入 CDDL 许可的 ZFS 代码库，这体现了宽松许可对跨生态代码流动的重要性——如果 lz4/zstd 采用 GPLv2，合入 ZFS 同样会面临许可障碍

**辨析**：ZFS 加密历史需区分 “加密” 的不同形


### 宿主键 1214 = 节 121.4
节题：121.4 其他存储栈组件：devfs、mdconfig、tmpfs、sendfile、VFS
范围：**要点**：FreeBSD 5.0 之前，/dev 目录下的设备节点是静态创建的，通过 MAKEDEV 脚本手动运行创建必要的节点，主/次设备号静态分配，新设备驱动需要修改 MAKEDEV 脚本并分配主设备号；**devfs(5)** 由 phk 设计，随 FreeBSD 5.0（2003 年 1 月）正式引入，是一个内核态虚拟文件系统，设备节点由设备驱动自动创建和销毁，无需用户态脚本；devfs 支持规则（rule）机制，可通过 **devfs.conf(5)** 和 **devfs.rules(5)** 配置设备节点权限、所有者、掩码，支持 **jail(8)** 环境下的 /dev 隔离（每个 jail 有独立的 devfs 实例）；FreeBSD 5.0 之后，**mknod(8)** 命令仍保留但手动创建的设备节点不生效，所有设备节点必须由内核 devfs 管理；Linux 在同一时期也经历了 devfs→udev/devtmpfs 的演进，但 Linux 选择了用户态 udev 管理设备节点，FreeBSD（以及 DragonFly BSD、Darwin/macOS）选择内核态 devfs

**史料**：**devfs(5)**, **devfs.conf(5)**, **devfs.rules(5)** 手册页；phk 2002-2003 年 freebsd-arch@ devfs 设计讨论；FreeBSD 5.0 Release Notes devfs 章节；MAKEDEV 脚本历史（FreeBSD 4.x 源码） ［A］

**史观**：总纲第 10 条——边缘者贡献：phk 一个人完成了 devfs 的设计和实现——这不仅是技术工作，更是政治工作：它要求所有设备驱动开发者修改驱动以支持新的设备注册 API，废弃使用了十几年的 MAKEDEV 和静态主/次设备号分配；这种 “大爆炸式” 架构切换在保守的 BSD 项目中非常罕见，只有 phk 这样资历


### 宿主键 1211 = 节 121.1
节题：121.1 FFS 与 UFS/UFS2——从 Berkeley FFS 到 64 位块指针的文件系统演进
范围：**要点**：Fast File System（FFS）由 麦库西克 在 Berkeley 读研期间设计，核心创新在于引入柱面组（cylinder group）概念，将磁盘划分为若干个柱面组，每个柱面组包含自己的超级块备份、inode、数据块，将相关数据和元数据局部化在同一柱面组，大幅减少磁头寻道时间；块大小从传统 UNIX 的 512 字节提升至 8KB，同时引入片段（fragment，1KB）机制减少小文件空间浪费；FFS 论文 “A Fast File System for UNIX” 于 1984 年 8 月发表于 ACM Transactions on Computer Systems（Vol.2 No.3），合作者包括 比尔·乔伊（Bill Joy）、Samuel Leffler、Robert Fabry；4.1b BSD（1983 年试验版）已包含 FFS 原型，正式随 4.2BSD 于 1983 年 8 月发布，而非 1984 年；FFS 是现代 BSD UFS 的直接前身

**史料**：McKusick et al. 1984 “A Fast File System for UNIX” ACM TOCS 论文；McKusick 1999 “Open Sources: Voices from the Open Source Revolution” 中 FFS 开发回忆；4.2BSD 发行手册（1983 年 8 月）；McKusick, Bostic, Karels, Quarterman 1996《The Design and Implementation of the 4.4BSD Operating System》第 7 章 ［A］

**史观**：总纲第 1 条——一切真历史都是古代史（原“项目统摄史观”系自创名目，按权威表正名；FFS“源头时刻”内容与第 1 条主旨相合）：FFS 的柱面组设计是 1980 年代初磁盘性能瓶颈下的 “源头时刻”——


### 宿主键 12210 = 节 122.10
节题：122.10 **与同时期操作系统的比较**：FreeBSD 非 ZFS 存储栈——GEOM/gvinum/UFS——与 Linux、Windows、illumos、其他 BSD 的对照
范围：**要点**：Linux 存储栈以 LVM（逻辑卷管理）提供卷抽象、ext4 为默认文件系统（含 delayed allocation、journal）、btrfs 提供写时复制与卷管理合一；与 FreeBSD 的 GEOM（模块化存储变换框架）+ UFS（soft updates/journal）形成对照，二者在 “卷管理 vs 文件系统” 的边界划分上思路不同。

**史料**：Linux LVM2/ext4/btrfs 文档；FreeBSD GEOM/UFS 手册（geom(4)、tunefs(8)）［A］

**史观**：总纲第 4 条——分离聚合是永恒规律：Linux 将卷管理（LVM）与文件系统（ext4/btrfs）分层，FreeBSD 以 GEOM 统一存储变换层，体现两种存储架构哲学。

**辨析**：btrfs 的 CoW 与 ZFS 思路相近而非与 UFS 对照；本章限非 ZFS 部分，故侧重 GEOM/UFS 与 LVM/ext4 的架构差异。

**文献**：Rodeh O et al. btrfs Design [EB/OL]；FreeBSD. GEOM Manual [Z]. ［B］

**要点**：Windows Server 2012 引入 Storage Spaces，以虚拟化存储池提供镜像/奇偶校验，理念类似软件 RAID；与 FreeBSD 的 gmirror/gstripe/graid 对应，但基于 NT 存储栈与 PowerShell 管理，闭源不可审计。

**史料**：Microsoft Storage Spaces 文档（2012）［A］

**史观**：总纲第 4 条——分离聚合是永恒规律：Storage Spaces 的 “存储池虚拟化” 与 GEOM/graid 的 “模块化 RAID” 目标相似但生态与可审计性不同。

**辨析**：Storage Spaces 与 gmirror 功能重叠，但 Windows 闭


### 宿主键 1231 = 节 123.1
节题：123.1 9.x 系列总览与工程语境（2010-2014）
范围：**要点**：FreeBSD 9.0 开发始于 stable/8 分支冻结后，历时近两年（2010 年中至 2012.1.12 正式发布），是 FreeBSD 历史上开发周期最长的大版本之一；9.x 系列包含四个 RELEASE：9.0（2012.1.12）、9.1（2012.12.30）、9.2（2013.9.30）、9.3（2014.7.16），无 9.4-RELEASE；9.3 作为 9.x 系列终章获得超长支持周期至 2017.1.1，是生产环境长期部署的 “企业级稳定版”

**史料**：FreeBSD 9.0-RELEASE Announcement（2012.1.12）、9.1 Announcement（2012.12.30）、9.2 Announcement（2013.9.30）、9.3 Announcement（2014.7.16）、FreeBSD Release Engineering 日程邮件列表档案、FreeBSD Quarterly Status Reports 2010-2014；**freebsd.duckdb** `tags` 表 `freebsd-src` 仓库 release tag 数据库验证——`release/9.0.0` tagger_date = 2012-01-02T18:59:55Z，tagger_name = Ken Smith（原大纲误作 cvs2svn，已据数据库修正），target_commit_hash = `4e26149e5c0c0cd171a9ea428eafec0c80946c30`（原大纲误作 `9b5e2a67d39a...`，已据数据库修正），target_commit_date = 2012-01-02T18:59:55Z，与公开声明日期 2012-01-12 相差 10 日（在 9.x 系列 SVN 时代发布中偏差较大）；`release/9.1.0` tagger_date = 2012-12


### 宿主键 1013 = 节 101.3
节题：101.3 ARM 移植——FreeBSD/arm 的启动
范围：**要点**：FreeBSD/arm 由 Olivier Houchard、Sam Leffler 等 2004 启动移植，6.0(2005) 首次正式支持 ARMv4/v5；目标平台包括 ARM eval boards 与嵌入式设备
  
**史料**：FreeBSD/arm 项目页、Sam Leffler commit log、freebsd-arm 邮件 ［A］
  
**史观**：总纲第 7 条——BSD 与 UNIX 谱系的连续性
  
**辨析**：(1) ARM 移植是否受 NetBSD/arm 既有实现影响，需查 freebsd-arm 邮件早期讨论与 commit log 中的引用线索；(2) 2004 启动移植至 6.0(2005) 正式支持的时间窗是否合理，需对照 Sam Leffler commit log 与 FreeBSD 6.0 Release Notes 核实工程节奏；(3) Olivier Houchard 与 Sam Leffler 的具体分工需查 SVN commit log 按作者维度划分；(4) ARMv4/v5 起始与后续 ARMv6/v7 演进路径需对照 FreeBSD/arm 项目页版本演化记录
  
**文献**：freebsd-arm 邮件；项目页 ［A］

**要点**：FreeBSD/arm 对嵌入式的影响：(1) 为 ARM 设备提供 BSD 替代；(2) 用于路由器 (RouterBoard)、NAS(Buffalo Linkstation)、工业控制；(3) 与 NetBSD/arm 竞争
  
**史料**：嵌入式设备部署案例、RouterBoard 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 〔L3 官方文档；L5 二手研究〕
  
**史观**：总纲第 13 条——边缘者的作用，嵌入式是 BSD 边缘市场
  
**辨析**：


### 宿主键 1335 = 节 133.5
节题：133.5 架构支持变化——RISC-V 引入、sparc64 退役与 ARM64 成熟
范围：**要点**：FreeBSD/riscv64（64 位 RISC-V）移植工作主要由 Ruslan Bukin（br@）主导，在 FreeBSD 11.x 时期开始于 -CURRENT 分支，12.x 时期持续开发但未提供正式发布镜像直至 12.4-RELEASE（2022.12.5）。RISC-V 是 2010 年代兴起的开源指令集架构（ISA），由 UC Berkeley 发起、RISC-V International 标准化，以许可证自由（免授权费）、模块化扩展设计为特征，被视为 x86/ARM 之外的第三极。FreeBSD/riscv64 在 12.x 时期支持 SMP 多核、UART 控制台、virtio 设备（在 QEMU 中运行）、UEFI 引导等核心功能，但驱动支持有限，主要在 QEMU 虚拟机与少数开发板（如 SiFive HiFive Unmatched）上运行。RISC-V 在 FreeBSD 12.x 为 Tier 3 状态（实验性支持），FreeBSD Foundation 在 2020 年代持续资助 RISC-V 移植工作。

**史料**：FreeBSD 12.4-RELEASE Announcement（riscv64 加入发布架构列表）、Ruslan Bukin RISC-V 移植 commit log、FreeBSD Wiki RISC-V 页面（wiki.freebsd.org/riscv）、FreeBSD Foundation 年度报告（RISC-V 赞助记录）、FreeBSD Quarterly Status Reports RISC-V 章节。 ［A］

**史观**：总纲第 4 条——分离聚合是永恒规律：RISC-V 是计算架构领域的重要新变量，但在 12.x 时期（2018-2022）仍处于非常早期阶段。FreeBSD 对 RISC-V 的支持体现了操作系统项目对新兴架构的前瞻布局——等到 RISC-V 硬件生态成熟再移植将


### 宿主键 1792 = 节 179.2
节题：179.2 pkgsrc 2.0 与跨平台软件包管理（2005-2009）——pkgsrc 2.0 改进依赖管理、引入二进制软件包支持、扩展至 Linux/macOS/Solaris 等非 NetBSD 平台，成为真正意义上的跨平台软件包管理系统
范围：**要点**：pkgsrc 2.0（2005）引入 bootstrap 机制使 pkgsrc 可在非 NetBSD 平台构建；改进依赖解析与冲突处理，引入 buildlink 框架统一编译期依赖；pkg_view 与 pkg_install 工具更新支持多版本并存

**史料**：pkgsrc 2.0 Release Notes；tech-pkg 邮件列表设计帖；Alistair Crooks 与 Joerg Sonnenberger 的 commit 记录 ［A］

**史观**：总纲第 17 条——形式与内容：pkgsrc 作为“形式”（软件包管理框架），其脱离 NetBSD 内核独立运行的能力使其内容扩展至多平台

**辨析**：pkgsrc 2.0 的具体版本号与发布日期存在叙事分歧——部分资料称 2.0 于 2005.7 与 NetBSD 2.1 同步发布，但 tech-pkg 邮件列表暗示 2.0 标签更早；需对照 pkgsrc-dist 文件 RELEASE-NOTES 核验

**文献**：pkgsrc 2.0 Release Notes；tech-pkg 邮件列表 2004-2005；Alistair Crooks “pkgsrc: The NetBSD Package System” 文档 ［A］

**要点**：pkgsrc 2005-2009 年间扩展至 Linux（特别是 Slackware、Gentoo 等发行版）、macOS（通过 bootstrap）、Solaris、IRIX、AIX 等平台；pkgsrc 在 macOS 上的成功催生 MacPorts（2007）等项目借鉴其设计；跨平台能力使 pkgsrc 成为“系统无关的软件包管理框架”

**史料**：pkgsrc/doc/PLATFORMS 文件历年版本；macOS 上 pkgsrc bootstrap 文档；MacPorts 设计文档与 pkgsrc 对比［考据注：2026-07-


### 宿主键 1852 = 节 185.2
节题：185.2 社区治理结构：Core Team 与 Foundation
范围：**要点**：NetBSD Core Team 采用邀请制，与 FreeBSD 2000 年直选制不同；NetBSD Foundation 在特拉华州注册为非营利组织（**精确成立日期存疑**——NetBSD Foundation 主页与 Bylaws 均未直接给出成立日期，仅说明“incorporated in the State of Delaware”），于 **2004 年 1 月 22 日** 获得美国国税局 501(c)(3) 免税组织地位（来源：NetBSD Foundation 2003 年报"as of January 22nd 2004, the NetBSD Foundation is a 501(c)(3) tax-exempt organization"）；Foundation 承担法律实体与资产管理职责；Core Team 与 Foundation Board 的权力边界长期模糊；原叙事中“NetBSD Foundation 于 1995 年成立”的精确日期未获考据确认——考据记录 20260723_announcements-netbsd.md § 存疑判定依据-二 -4 显示，穷尽 NetBSD 官方公开文档（Foundation 主页、Bylaws、2003 年报）后未能取得精确成立日期，仅能确认成立日期介于 1993 年（项目起始）至 2004 年（获得 501(c)(3) 地位）之间［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

**史料**：NetBSD Foundation bylaws（**<https://www.netbsd.org/foundation/bylaws.html>**，访问日期 2026-07-23，含"non-profit organisation as per section 501(c)(3) of the Internal Re


### 宿主键 1853 = 节 185.3
节题：185.3 邮件列表、IRC 与通讯渠道文化
范围：**要点**：NetBSD 的主要通讯渠道包括 tech-kern、tech-userlevel、current-users、source-changes 等邮件列表，以及 #netbsd IRC 频道；邮件列表文化以技术深度著称，但也存在排外现象

**史料**：mail-index.netbsd.org 邮件列表存档；IRC 频道日志〔存疑：#netbsd 频道尚无公开、可确证的完整日志存档，本次考据未获取，留待查证〕；NetBSD 社区调查报告

**史观**：总纲第 14 条——商业与社区的张力，通讯渠道的迁移反映社区代际更替

**辨析**：邮件列表文化的“排外”标签需考据，需区分严格技术标准与排外行为

**文献**：mail-index.netbsd.org 邮件列表存档 [EB/OL]. <https://mail-index.netbsd.org/>；#netbsd IRC 频道（Libera Chat）；NetBSD 社区调查报告 [EB/OL]. <https://www.NetBSD.org/community/> ［A］

NetBSD 提交量最高的贡献者：wiz(222791), adam(71900), taca(66560), christos(58421), joerg(57785)

1993 年 12 月 17 日，cgd 在 tech 与 install 列表上提醒众人这些列表的张贴并非毫无限制，希望看到更多切题讨论，尤以 install 列表为甚，并要求发言保持理性，否则列表将再度被收紧管制。引用时按 L4 纪律：以上为邮件列表当事人一手自述，属过程性证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

1994 年 11 月 14 日，gwr 就 sun-lamp CVS 上 christos 修改 cons.c 与 vn.c、给 vn_open 增加参数一事发问，追问此事是否曾在 tech-kern 之类的地方


### 宿主键 1873 = 节 187.3
节题：187.3 与 Linux 的生态对照
范围：**BSD 四仓库合计 vs Linux commit 量对照（netbsd.duckdb 数据分析 §L7.3.1，四库合计口径）**：

注：倍数列数值为 Linux commit ÷ BSD 四仓库合计 commit（口径不对等，Linux 为单仓库全子系统，见辨析）。

**要点**：Linux 凭借 GPLv2 强制回馈机制与企业投入（Red Hat、IBM、Intel 等）在 2000 年代快速扩张生态；NetBSD 的 BSDL 允许商业闭源 fork 但缺乏企业回馈机制，生态扩张缓慢；（原要点尾部混入的参考文献计量统计 C-41/C-42/C-44 与本节 OS 对照主题无关，已移除，详见**文献计量学分析.md**）

**史料**：Linux Foundation 年度报告；NetBSD Foundation 年度报告；GPL vs BSDL 对比研究；技术新闻媒体的市场份额统计；netbsd.duckdb 数据分析 §L7.3.1 显示：2008 年 BSD（freebsd-src+netbsd-src+openbsd-src+dragonflybsd-src 合计）commit_count = 48,242，Linux（linux-stable 仓库）commit_count = 48,825，BSD/Linux 比例 = 1.01（基本持平）；2020 年 BSD commit_count = 36,392（较 2008 年下降 24.6%），Linux commit_count = 90,911（较 2008 年增长 86.2%），BSD/Linux 比例 = 2.50（Linux 已达 BSD 的 2.5 倍）；2026 年 BSD/Linux 比例 = 2.67，反映 Linux 生态在 2008-2026 年间相对 BSD 持续扩张；［A］

**史观**：总纲第 13 条——法律与道德是利益分配：许可证哲学直接塑造了生态扩张速度——GP
