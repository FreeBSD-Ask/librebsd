---
chapter: 第 111 章
id: CH111
volume: 第06卷-freebsd的核心技术革新
---

# 第111章 oracle收购与openzfs社区分叉

## 要点

- Oracle 于 2009 年 4 月 20 日宣布以 74 亿美元收购 Sun Microsystems，交易于 2010 年 1 月 27 日完成；Oracle 收购 Sun 的核心商业动机包括：获得 Java 编程语言和平台的控制权、获得 Solaris 操作系统及 SPARC 处理器技术、获得 MySQL 数据库（后续引发 MySQL 开源社区 fork 为 MariaDB）、获得 Sun 的硬件产品线和专利组合；收购后 Oracle CEO Larry Ellison 明确表示将以 “专有软件” 模式运营 Solaris，逐步关闭 OpenSolaris 项目；OpenSolaris 治理委员会（OGB, OpenSolaris Governing Board）于 2010 年 8 月在 Oracle 任命的新领导层下解散；2010 年 8 月 13 日，一份内部 Oracle 备忘录泄露，显示 Oracle 将不再以开源方式发布 Solaris 后续版本，而是改为封闭开发、仅发布二进制更新
- OpenSolaris 关闭对 ZFS 社区的直接冲击是：ZFS 上游开发从 “Sun 主导的开源项目” 变为 “Oracle 封闭开发”，社区无法再从 Solaris 获得 ZFS 新功能的开源代码；Bonwick、Ahrens 等 Sun/ZFS 核心工程师大多留在 Oracle（至少短期留任），但 Oracle ZFS 团队与社区沟通几乎中断；已有的 OpenSolaris ZFS 代码（截至 2010 年 8 月的 ON build）因 CDDL 许可是永久自由的，社区有权在其基础上 fork 并继续开发；受影响的不仅是 ZFS——整个 OpenSolaris 生态（包括 DTrace、Zones、Crossbow、SMF 等）都面临同样的断供危机；FreeBSD 的 ZFS 移植在 2010 年前已相对独立维护，因此受冲击小于 illumos 社区
- OpenSolaris 关闭后 ZFS 生态的 fork 路径：Garrett D'Amore（前 Sun 工程师，Nexenta Systems 员工）于 2010 年 8 月 3 日发起 illumos 项目作为 OpenSolaris 的社区 fork，illumos 成为 ZFS 开源开发的事实上的上游；illumos 初期由 Nexenta 赞助，后发展为独立的社区治理项目；除 illumos 外，ZFS On Linux（ZoL，Brian Behlendorf（布莱恩·贝伦多夫） 2008 年在 LLNL 发起）在 2010-2013 年间也发展为独立的 ZFS 实现；2013 年，Matt Ahrens 联合各平台 ZFS 开发者在首届 OpenZFS Developer Summit 上正式宣布成立 OpenZFS 项目作为跨平台 ZFS 协作的 umbrella 组织
- Oracle 收购 Sun 及 OpenSolaris 关闭的关键日期交叉验证：Oracle 宣布收购 Sun：2009 年 4 月 20 日（Oracle/Sun 新闻稿、SEC filing 均确认）；欧盟反垄断审查通过：2010 年 1 月 21 日；收购完成：2010 年 1 月 27 日（SEC filing 确认）；illumos 项目启动：2010 年 8 月 3 日（Garrett D'Amore 邮件确认）；OpenSolaris Governing Board 解散：2010 年 8 月（OGB 会议纪要）；Oracle 内部备忘录泄露：2010 年 8 月 13 日（多个来源存档）；Oracle Solaris 11 发布：2011 年 11 月（首个完全闭源开发的 Solaris 版本）；需注意：OpenSolaris 从未被 Oracle “正式关闭”，而是通过停止更新开源代码仓库、解散治理委员会、撤回对社区版的支持等方式被 “实质终止”
- OpenZFS 项目于 2013 年正式成立，首届 OpenZFS Developer Summit 于 2013 年 11 月 18-19 日在旧金山举行；OpenZFS 由 Matt Ahrens（Delphix）发起，联合各平台 ZFS 开发者共同建立跨平台治理结构；OpenZFS Bylaws 规定了项目治理结构：选举产生的指导委员会（Governing Board）、各平台代表席位（FreeBSD、Linux、illumos、macOS/Windows 等）、代码贡献流程、发布流程；OpenZFS 商标最初由 Matt Ahrens 个人持有，后转让至 OpenZFS 组织；OpenZFS 的核心目标是建立跨平台的共享 ZFS 代码库，减少各平台移植之间的代码分叉

## 史观

- 总纲第 13 条——法律与道德是利益分配：Oracle 收购 Sun 是开源史上最具争议的商业事件之一，它直接证明了单一商业实体控制开源项目的风险——尽管 OpenSolaris 以 CDDL 开源，Oracle 作为版权持有者可以选择不再发布新版本的开源代码，社区无法强迫 Oracle 继续开源贡献；这是 CDDL/MPL 类文件级 copyleft 许可证相对于 GPL 的一个弱点〔订正注：原挂“总纲第 24 条——许可证”系伪标签，权威第 24 条为“美是消解性的体验”；许可证控制与利益结构语义依权威表改挂第 13 条〕
  - 辨析：Oracl
- 总纲第 4 条——分离聚合是永恒规律：OpenZFS 的成立标志着 ZFS 从 “Sun/Oracle 的项目” 彻底转变为 “社区拥有的项目”——这是一个历史终结与新生的节点：Sun 时代的 ZFS 终结了，社区自治的 ZFS 诞生了；Bylaws 这一形式化治理文件的制定，体现了开源项目从 “仁慈独裁者” 模式向制度化治理的转变〔订正注：原挂“总纲第 25 条——终结与延续”系伪标签，权威第 25 条为“逻辑是形式主义而非世界本身的结构”；项目归属转移语义依权威表改挂第 4 条〕
  - 辨析：OpenZFS 成立的精确时间：第一届 OpenZFS
- 总纲第 13 条——法律与道德是利益分配：ZoL 的模块加载策略是法律约束下的工程妥协——ZFS 无法进入主线内核，因此通过 DKMS/LKM 方式在主线外分发；这种 “核外生存” 模式虽然有性能和维护成本，但在法律灰区中开辟了一条可行路径〔订正注：原挂“总纲第 6 条——技术路线分化”系伪标签，权威第 6 条为“和解优于斗争”；许可证约束下的分发策略依权威表改挂第 13 条〕
  - 辨析：需澄清：Linux 内核的 GPL 许可范围问题——Linux 内核 COPYING 文件明确指出 "kernel modules are conside〔待核：原文截断〕

## 辨析

- Oracle 收购 Sun 的精确日期：宣布日为 2009 年 4 月 20 日，完成日（交易交割）为 2010 年 1 月 27 日，两者常被混淆；OpenSolaris 的 “关闭” 是一个渐进过程而非单一事件——2010 年 8 月的泄露备忘录确认了封闭政策，但 OpenSolaris 源代码在 2010 年 8 月后仍可访问一段时间，直到 Oracle 将其从公开仓库中移除
  - 文献：
- OpenZFS 成立的精确时间：第一届 OpenZFS Developer Summit 于 2013 年 11 月举行，但 OpenZFS 作为协作项目的筹备始于 2012-2013 年，Matt Ahrens 等人在多个会议上提出了跨平台 ZFS 统一的构想；OpenZFS 不是从零创建 ZFS 的 fork，而是一个协调已有 ZFS 实现（illumos ZFS、ZoL、FreeBSD ZF
- 需澄清：Linux 内核的 GPL 许可范围问题——Linux 内核 COPYING 文件明确指出 “kernel modules are considered derivative works”，但内核社区实际上长期容忍非 GPL 模块（NVIDIA、VMware 等闭源驱动，以及 OpenAFS 等 CDDL 模块），这形成了事实上的 “模块例外” 实践；ZoL 的法律地位在理论上有争议，但在

## 文献

- Oracle Corporation. (2009-04-20). *Oracle to Buy Sun Microsystems*. Press Release; SEC. *Oracle-Sun Merger Filings*. sec.gov; OpenSolaris Governing Board. (2010-08). *Meeting Minutes and Resignation Letter*. opensolaris.org (archived); LWN.net (2010-08-16). *What's Next for OpenSolaris*. lwn.net.[考据
- OpenZFS Project. *Bylaws*. openzfs.org/wiki/Bylaws; Ahrens, M. (2013). *The OpenZFS Project*. LinuxCon North America 2013; OpenZFS Developer Summit 2013 Schedule. openzfs.org; Behlendorf B. zfs-0.4.1. openzfs-zfs 仓库 tag [DB/OL]. 2009-01-21T12:25:52-08:00. tag: zfs-0.4.1; commit: a66e5effd5c81f504fca
- Behlendorf, B. (2008). *ZFS on Linux Launch*. zfsonlinux.org; ZFS on Linux Project. *SPL: Solaris Porting Layer*. github.com/openzfs/spl; Linux Kernel Project. *COPYING File* (module licensing note). kernel.org.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
    Fr

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP491、BSD Now EP374、BSD Now EP232、BSD Now EP222、BSD Now EP203、BSD Now EP181、BSDTalk EP197、Nerding Out with Victor EPS01E25、YouTube EPpN7OLChclH8、YouTube EPhTbqEf9LRGE（共 10 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- DragonFly BSD 发布 6.4（2022 年 12 月 30 日），延续 6.x 系列：内核修复涉及 exec CVPE 环境传递、名称缓存膨胀与 vnode 回收、HAMMER2 的批量释放与内存分配，并引入来自 FreeBSD 的 GTaskQ API；默认编译器仍为 GCC 8，新增对 Type 2 hypervisor（NVMM）、AMD GPU 驱动与 HAMMER2 卷远程挂载的实验性支持。（BSD Now EP491，[188.06-530.00]，L2）
- 节目转述 Clara 关于 OpenZFS 在 FreeBSD 与 Linux 间取舍的文章，指出 2020 年 12 月 OpenZFS 统一了 FreeBSD 与 Linux 平台的代码库；FreeBSD 安装器原生默认支持 OpenZFS root，而 Ubuntu 依赖未完成的 ZSys 项目并遗留过多 dataset 与快照管理问题。（BSD Now EP491，[525.06-993.02]，L2）
- Peter 的博客回顾其约 15 年的 greytrapping 与灰名单实践：其 bsdly.net 兼作个人邮件服务与蜜罐，用于生成 IP 信誉数据；他讨论 71% 垃圾邮件捕获率的衡量问题，并指出在内容过滤前尽早丢弃垃圾流量可降低资源与能耗。（BSD Now EP491，[1134.30-1417.44]，L2）
- 节目报道第六届可复现构建峰会 2022 于威尼斯举行，NetBSD 基本系统自 8.0 起可复现构建，pkgsrc 也已迈出第一步，但包级可复现仍有待完善。（BSD Now EP491，[1922.36-2086.72]，L2）
- 其余内容涉及 Ubuntu 在 FreeBSD 的 Linux 二进制兼容搭建、疯狂 shell 提示符的 misc 邮件，以及用 Ansible 管理 FreeBSD jail 的问答。（BSD Now EP491，[1705.60-1922.36]，L2）
- OpenBSD 于 2020 年 10 月 18 日发布 6.8 版，正值项目创立二十五周年；该版引入由引导装载器向内核传递的随机种子置信度标记、在支持的 arm64 处理器上启用 PAN，并改进 FFS、安装镜像与多架构安装引导。（BSD Now EP374，[0.0-10.72]，L2）
- NetBSD 于 2020 年 10 月 18 日发布 9.1，新增并行磁盘加密、C.UTF-8 区域设置、ZFS 支持增强、NVMM 虚拟机监控器更新以及 PowerPC64 PowerNV 支持。（BSD Now EP374，[590.42-796.96]，L2）
- OpenZFS 开发者峰会 2020 因疫情改以 Zoom 举办，采用 webinar 演讲与虚拟走廊并行的组织方式；峰会自 2013 年起规模持续扩大，本年取消人数上限后允许更多人参加。（BSD Now EP374，[847.32-970.56]，L1）
- BastilleBSD 相关文章将容器技术谱系上溯至 1979 年 Unix 第七版 chroot，指出 jail 术语最早见于 1991 年 4.3BSD，FreeBSD 4.0 于 2000 年提供 jail 命令，Linux 迟至 2008 年才有 LXC、2013 年才有 Docker。（BSD Now EP374，[1848.72-2116.32]，L2）
- 该期记录了 FOSDEM 2018 期间的 FreeBSD 开发者峰会与 BSD Dev Room，主持人自述在比利时参会、与基金会人员当面交流并设摊分发资料的经历。（BSD Now EP232，[58.6-105.36]，L1）
- 宽容许可证与 copyleft 的对比重申：BSD 系许可证由四条款逐步缩减，GPL 则随版本增长；两阵营均自称捍卫自由，一者保护代码自由，一者保护使用者自由。（BSD Now EP232，[1754.46-1836.7]，L2）
- 该期辨析 ZFS 与 OpenZFS 术语：ZFS 为技术总称，OpenZFS 为 2010 年后由 illumos 延续的开源项目，Oracle ZFS 为其专有分支，二者应分别称呼。（BSD Now EP232，[3306.54-3592.66]，L2）
- FreeBSD 基金会 2018 年 1 月更新称 Kostik 负责 x86 内核的 PTI 缓解，retpoline 与 Clang 工具链缓解正在推进，并强调基金会使专职开发者能放下原计划集中应对漏洞。（BSD Now EP232，[2468.14-2777.78]，L2）
- 该期引述 2006 年 Larry Ellison 对《金融时报》的表态“若开源产品足够好，我们会直接采用”，并批评 Oracle 在政府游说中反对开源、在商业上拥抱开源的双面姿态。（BSD Now EP222，[390.9-398.1]，L2）
- 该期解释 Oracle 收购 Sun 后 ZFS/OpenSolaris 开发者仅停留数周便离开，OpenZFS 开发者峰会由留下的社区延续，呈现收购与分叉的因果。（BSD Now EP222，[435.98-454.76]，L2）
- Netflix 以约 700 个微服务控制服务，核心视频以 AWS 转码为多格式并加 DRM，同时以自建 Open Connect 盒子（运行 FreeBSD）在 ISP 端就近缓存分发。（BSD Now EP222，[1862.4-2110.86]，L2）
- FreeBSD 出现在 Netflix 的分发环节：Open Connect 盒子由 Netflix 提供给 ISP，按热度分级缓存内容以节省带宽。（BSD Now EP222，[2320.66-2487.94]，L2）
- 该期以“ZFS 是否还是最佳文件系统”为引，反驳一篇称 ZFS 陷于过去的博文：指出异步销毁、透明压缩、分配类、vdev 移除等大量特性均为近十年新增，ZFS 并未停滞。（BSD Now EP203，[377.50-720.00]，L2）
- 主持人梳理 ZFS 法律史：2007 年 NetApp 诉 Sun 侵犯 WAFL 专利，Sun 反诉，最终互不侵权；Oracle 收购 Sun 后关闭 OpenSolaris 源码，OpenZFS 项目从最后的开源版本分叉并延续至今。（BSD Now EP203，[148.62-241.44]，L2）
- 技术反驳包括：去重收益常被压缩抵消，Intel 的分配类（allocation classes）与元数据分层可实现混合存储；George Wilson 与 Matt Ahrens 的 2014/2016 空间分配改进缓解了大而碎池的性能悬崖。（BSD Now EP203，[522.88-800.00]，L2）
- Theo de Raadt 在 OpenBSD 技术邮件列表报告内核随机重链接（KARL）进展：安装、升级与每次开机都会以随机顺序与偏移重链接生成唯一内核，使单个指针泄露无法推断其他地址，并要求用户测试 6.2 快照。（BSD Now EP203，[4432.62-4690.58]，L2）
- Jörg Sonnenberg 公告 NetBSD 仓库 CVS→Fossil→Git 转换迁至新家，改用 SHA-512 校验；同期 LibreSSL 2.5.5 与 2.6.0 发布，后者将成为 OpenBSD 6.2 的一部分。（BSD Now EP203，[5080.48-5480.00]，L2）
- 作为 kqueue 与 illumos event ports 时代的当事工程师，Bryan Cantrill 系统复盘 1990 年代末事件通知机制的三条设计路线：Solaris devpoll 保留轮询语义、BSD kqueue 引入事件注册、event ports 强制事件在分发后与源自动解关联直至消费线程重新关联；他论证唯有解关联模型能避免多线程环境下同一文件描述符事件被重复分发，并批评 epoll 沿用 devpoll 模型且以描述符数值绑定事件，在 dup、close 与 fork 场景产生无法自洽的语义，如“the Epol man page is remarkably frank about all the design defects involved”（3915.12-3921.54），并进而解释 DTrace 与 ZFS 长期缺席 Linux 的文化根源。（BSD Now EP181，[3677.30-3928.32]，L1）[订正：原 [3889.76-3928.32]，2026-09-30 SenseAudio 重转核对]
- 访谈三给出 D-Trace 起源的完整口述：1996 年入职 Sun 后从事端到端调度器研究，1997 年 12 月参与 E10K 大型机 SAP 基准排障时发现系统在系统态长时间空转而无任何工具可以定位，最终查明为机器被误配置为路由器、叠加一台固件有缺陷的路由器周期性重启所致，由此确立“任何普通配置错误都可能造成不可观测系统”的问题意识；2001 年 11 月他与 Mike Shapiro、Adam Leventhal 启动动态内核插桩项目，2003 年 9 月随 Solaris 10 发布，2005 年 1 月成为 Sun 开源系统的首个组件，随后经 John Birrell 移植 FreeBSD、Apple 在 WWDC 宣布移植 macOS、QNX 亦采纳。（BSD Now EP181，[1469.20-3491.10]，L1）[订正：原 [2997.47-3180.90]，2026-09-30 SenseAudio 重转核对]
- illumos 团队对 rm -rf / 实现了在符合 POSIX 前提下的防护：起因是 Solaris patchadd 对非补丁输入执行未初始化变量的删除而清空整机的真实事故，团队细读标准后发现多处删除中任一失败即进入未定义行为、且删除当前目录恒为非法，遂令 rm 实现先尝试删除当前目录从而整体失败；Cantrill 以 Steam 客户端与 Red Hat 测试包的同型事故说明此类删除几乎均由脚本未初始化变量引起，防护具有普遍系统意义，该治理思路被视为值得 FreeBSD 借鉴的 illumos 惯例。（BSD Now EP181，[5053.3-5478.64]，L1）[订正：原 [5213.96-5478.64]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 核心团队成员 M. Warner Losh 自述 2007 年以来推动嵌入式 FreeBSD 议程并从事 MIPS 移植，2010 年出任 iXsystems 自由软件开发总监后主持 FreeNAS 8 重构：目标是从单一 NAS 设备转向可跨 FreeBSD 版本移植、可扩展至打印与媒体服务等用途的平台，并以 Alpha 快照形式向社区公开测试。（BSDTalk EP197，[62.72-117.12]，L1）
- FreeNAS 8 的工程基座由旧版沿用 m0n0wall 的 crunched binary 方案整体切换为 NanoBSD：该框架作为 FreeBSD 源树内的打包脚本随主线同步，天然继承全部架构与驱动支持，以约半 GB 镜像面向 CF 卡介质，并通过双分区交替写入实现更新失败即回滚；配置层则改为以 SQLite 数据库统一建模主机、接口、磁盘与卷，开机时由 Shell 与 Python 脚本生成配置文件，Django 提供 MVC 式 Web 界面，数据模式带版本化转换层以延续旧版免手工合并的升级体验。 [存疑脚注] 转写将 NanoBSD 作者记作 Paul Hennigkamp，按 FreeBSD 通行史料应为 Poul-Henning Kamp，属转写音误（BSDTalk EP197，[293.88-1041.86]，L1）
- Losh 从工程角度论证 ZFS 的必要性：磁盘容量增长快于错误率下降使完整性校验与自动纠错成为刚需，ZFS 的去重、压缩、池动态扩容与数据冗余构成对低端商用 NAS 盒的差异化优势；其成熟度随各版本导入 FreeBSD 持续改善，且已有公司围绕 FreeBSD 加 ZFS 开展开发，即便 Oracle 不再发布新代码，ZFS 在 FreeBSD 生态中也足以独立维持演化。（BSDTalk EP197，[1544.10-1681.78]，L1）
- Jude 将三大 BSD 与 Linux 发行版的根本差异概括为操作系统边界之争：BSD 把内核、基础工具与驱动同置单一源码树，系统本体与第三方包二分，Linux 则连内核在内一切皆包；FreeBSD 以 ports 树的 Makefile 描述取源、校验、打补丁、构建与卸载全流程，自 FreeBSD 8 起以集群工具每三四日全量重编二进制包，再叠加每三月才升大版本的季度分支兼顾新鲜与稳定，至 13.3 操作系统已可实现可复现构建。（Nerding Out with Victor EPS01E25，[837.0-1180.0]，L1）
- Netflix 案例构成 FreeBSD 工程优势的完整链条：其选型的决定性因素是变更数周即入 mainline 的上游速度而非许可证本身；sendfile 系统调用消除内核与用户态间文件发送的反复拷贝，HTTPS 普及后内核 TLS 让 sendfile 在加密时代复活并在 Spectre 与 Meltdown 加剧越界成本后愈发关键，Netflix 再将批量加密密钥下放网卡专用芯片实现硬件卸载，单路服务器由 100 Gbps 推至 800 Gbps；Comcast 全量切换 IPv6 后的流量规模暴露出四字节计数器回绕溢出，数小时一崩的规律使缺陷迅速定位并经 errata 通知全网上游修复。（Nerding Out with Victor EPS01E25，[1204.0-1702.0]，L2）
- Jude 以 OpenZFS 开发者身份拆解其数据模型：vdev 层承载镜像或 RAID-Z 变换并各自负责完整性，pool 汇聚全部可用容量，dataset 动态共享剩余空间并逐集设定压缩与加密；RAID-Z 借事务性写入从结构上消除 RAID-5 写洞，奇偶校验分布于全组盘而非专用盘，RAID-Z3 为硬件 RAID 所无；LZ4 每核压缩数 GB/s 使透明压缩自 OpenZFS 2.2 起默认开启，早停机制对不可压数据及时放弃，高层级 Zstandard 先以 LZ4 试探再决定是否重压；原生加密采用 AES-GCM 逐数据集加钥，校验和前半与消息认证码后半拆分存储，使加密数据可无密钥完成校验、修复与重建，密钥卸载后数据静态受保护。（Nerding Out with Victor EPS01E25，[2683.0-3597.0]，L1）
- Dan Langille 把 ZFS 概括为合并了文件系统与卷管理器功能的文件系统：zpool 是基本构件，由若干 vdev（虚拟设备，可为单盘、两盘以上镜像或 RAID Z）聚合而成；文件系统经 zfs create 在池内分层创建、自父级继承属性，并可挂载到与 ZFS 名无关的任意路径；他反复强调池的冗余与恢复能力位于 vdev 层而非池层——损失一个 vdev 即失去整个池，设计存储池时须时刻记住这一约束；相较 UFS 按分区划拨空间、/var 空间不足时将数据移入 /usr 并以符号链接指回的旧习，池把全部空间统一调度。（YouTube EPpN7OLChclH8，[357.12-936.2]，L1）[订正：原“/usr 满后以符号链接搬迁”→“/var 空间不足时将数据移入 /usr 并以符号链接指回”（依新转写 [671.4-706.6]：var db 空间不足时把数据移入 /usr 并建符号链接）；原[357.12-585.839]→[357.12-936.2]，内容复核（zfs create 分层创建/继承/挂载对应转写 [599.8-664.5]、UFS 对比对应 [671.4-706.6]、vdev 可为单盘/镜像/RAID Z 对应 [919.9-936.2]，均落原区间外）]
- 关于 RAID Z 的语义，讲者辨正流传误解：RAID Z 不是 RAID 5 或 RAID 6，也没有专用校验盘——RAID Z n 的含义是阵列中任意 n 块盘可失效而无数据丢失；原版文档把这些盘称作“校验盘”，曾令用户误以为只能丢那几块指定的盘；RAID Z 的真正意义是为你赢得更换故障盘的时间，越早更换越好；镜像则只要剩一块盘仍能工作。（YouTube EPpN7OLChclH8，[373.28-878.8]，L1）[订正：原“涂色标作”→“称作”（新转写 [850-867.9]：称校验盘者为原版文档，蓝色涂示系幻灯示意可失效盘数，非文档涂色）；原[373.28-434.639]→[373.28-878.8]，内容复核（“越早更换越好”对应转写 [452.7-462.8]、原版文档称校验盘对应 [851.9-864.5]、镜像剩一盘仍工作对应 [871.2-878.8]，均落原区间外）]
- 讲者把数据完整性列为 ZFS 的头号卖点：其元数据自上而下逐层校验，读盘结果与校验和不符即报告数据损坏，而无校验的文件系统无从得知；在镜像或 RAID Z 的冗余之内，ZFS 能从别处取得正确数据自动修复错误，系统照常运行而不为人所觉；scrub 读取全量数据核对校验和，属预防性手段，他每周运行并建议启用，可在磁盘隐患扩大成灾之前发现；另须监控池容量，尽量勿超八成、绝勿满盘。（YouTube EPpN7OLChclH8，[1342.72-2195.9]，L1）[订正：原[1342.72-1462.799]→[1342.72-2195.9]，内容复核（条目“监控池容量，尽量勿超八成、绝勿满盘”对应转写 [2153.9-2195.9]，落原区间外）]
- 讲者给出一整套运维准则：换盘先以 gpart 把序列号作卷标识别故障盘，旧盘若仅降级尚能工作应留在池内直至 zpool replace 完成，以免移除后另一块盘再失效而全池俱毁；勿用 RAID 卡——RAID 卡自行“修复”后向系统报告驱动器已死，剥夺 ZFS 自愈的机会，应使用 HBA（部分 RAID 卡可刷写成 IT 模式，FreeBSD 项目维护有兼容清单）；bectl 与 beadm 管理的引导环境把内核与系统装在独立 ZFS 文件系统中，升级或试新内核前先保存旧环境，故障时经引导装载器回切，被他称作“终会救你一命的安全网”，nextboot 则可只指定下一次启动所用内核；配额把后代数据集与快照一并计入，宜设在路径末端；可将 SSD 池挂载到 /var/db/postgres 一类路径实现挂载中嵌套挂载，对系统全然透明；快照只读且不可变，同一主机上的快照不是备份，发送到别处才成为备份，亦可用于取证；以“静止数据库快照加可写克隆”快速搭建开发测试库，用毕即弃；mkdir 之际不妨考虑 zfs create，让照片、项目各成文件系统以便快照、发送与配额。（YouTube EPpN7OLChclH8，[1060.16-2706.64]，L1）[订正：原[1060.16-2066.8]→[1060.16-2706.64]，内容复核（配额对应转写 [2073.4-2123.8]、快照备份与取证对应 [2461.5-2489.6]、快照加克隆搭测试库对应 [2548.4-2596.1]、mkdir 与照片项目各成文件系统对应 [2627.5-2706.6]，均落原区间外）]
- ZFS 诞生前 Sun 两次组建大型团队开发新文件系统皆因团队膨胀过快而中途夭折，Jeff Bonwick 遂亲自挑选一名刚毕业的 Brown 大学学生，两人闭门以白板从零设计，直指当时文件系统的容量上限、inode 硬性配额与单盘假设三大桎梏；ZFS 将卷管理器与文件系统合为一体，一切资源动态分配，存储池合并全部磁盘供多个数据集共享空闲空间。（YouTube EPhTbqEf9LRGE，[1871.92-2007.48]，L2）[订正：原[1871.92-1987.0]→[1871.92-2007.48]，内容复核（条目“将卷管理器与文件系统合为一体…合并全部磁盘”对应转写 1998.36-2007.48，落原区间外）]
- Oracle 收购 Sun 并关闭源码后，社区自最后一版开源 Solaris 分叉出 Illumos，FreeBSD 转以 Illumos 为上游；但各操作系统各自维护 ZFS 版本导致功能序列错位与来回搬运的延迟，最终赶在 FreeBSD 13.0 建成 OpenZFS 统一仓库——公共核心代码与 Linux、FreeBSD 的集成层同库存放，经 Solaris Porting Layer 翻译内核调用，使 FreeBSD 与 Linux 上的 ZFS 源自同一份代码并统一版本号。（YouTube EPhTbqEf9LRGE，[2066.159-2323.64]，L1）[订正：原[2066.159-2297.64]→[2066.159-2323.64]，内容复核（条目“统一版本号”对应转写 2312.8-2323.64，落原区间外）]
- OpenZFS 自 2.2 版起默认启用透明压缩：LZ4 每核压缩速度达数 GB/s、解压逾 10 GB/s；early abort 机制在预计节省不足 12% 时中止压缩直接存原文，高 Zstandard 级先以 LZ4 试压、不可压文件即放弃重压，使压缩在现代硬件上近乎零成本。（YouTube EPhTbqEf9LRGE，[3208.76-3382.08]，L1）[订正：原“写放大反而可能因压缩而降低”→删，全期转写（rev6/auto 两版）均无 write amplification 表述，内容复核]
- ZFS 原生加密以数据集为粒度采用 AES-GCM，并将校验和拆半——SHA-256 前半验证磁盘块完整性、后半充作加密消息认证码，故修复坏盘与重建阵列全程无需解密密钥；密钥可按数据集卸载实现静态加密，某律所客户即以按案件数据集销毁密钥的方式满足诉讼终结后的证据销毁义务。（YouTube EPhTbqEf9LRGE，[3395.56-3653.76]，L1）[订正：原“并将军验和拆半”→“并将校验和拆半”，内容复核]
- Netflix 因自身流量占比过高而弃用商业 CDN，将 Open Connect Appliance 部入 ISP 机房就近服务；选 FreeBSD 的关键是补丁数周内即可进入主线与跟随开发版运行约六周滞后，而非许可证——因其并无内嵌操作系统的专有改动；技术脉络自 sendfile 零拷贝系统调用，经 HTTPS 迫使数据往返内核的回退，到 kernel TLS 套接字选项，再到与 Mellanox、Chelsio 合作的网卡加密卸载，单 CPU 服务器吞吐自 100Gbps 提升至 800Gbps；Comcast 全量启用 IPv6 后流量放大了计数器约 40 亿回绕的溢出缺陷，Netflix 设备数小时一崩，Netflix 定位修复并回灌主线。（YouTube EPhTbqEf9LRGE，[1222.72-1702.64]，L2）

**史料**：

- DragonFly BSD 6.4 发布说明，涉及内核、HAMMER2、GCC 默认版本与 NVMM 支持，为官方发布线索，经节目转述。（BSD Now EP491，[188.06-530.00]，L2）
- Clara 关于 OpenZFS 在 FreeBSD 与 Linux 平台差异的文章，为二手技术文本，经节目转述。（BSD Now EP491，[525.06-993.02]，L2）
- Peter 关于 greytrapping 与垃圾邮件捕获衡量的博客及其 bsdly.net 数据，为当事人一手实践叙述，经节目转述。（BSD Now EP491，[1134.30-1417.44]，L1）
- NetBSD 可复现构建峰会报告由 Pierre Pronchery 撰写，为参会者一手叙述，经节目转述。（BSD Now EP491，[1922.36-2086.72]，L2）
- OpenBSD 6.8 官方变更日志与发行公告，涵盖 OpenSSH 8.4、LibreSSL 3.2.2、OpenSMTPD 与 VMM/VMD 更新，由主持人转述。（BSD Now EP374，[357.24-391.04]，L2）
- NetBSD 9.1 官方发布公告，涵盖 cgd 并行磁盘加密、ZFS、NVMM、NPF、X11 默认窗口管理器切换等内容，由主持人转述。（BSD Now EP374，[590.42-823.44]，L2）
- OpenZFS 开发者峰会 2020 议题，包括 Matt Ahrens 论 OpenZFS 状态与版本化、George Wilson 论 ARC 与操作系统内存协作、持久 L2ARC、ZIL 并行化、顺序重建与 send/recv 性能提升，由 Alan Jude 亲历转述。（BSD Now EP374，[974.72-1777.74]，L1）
- 主持人口述 FOSDEM 2018 现场，含 FreeBSD 基金会摊位、BSD Dev Room 与约 21 人参加的开发者峰会。（BSD Now EP232，[87.6-105.36]，L1）
- 转述博客文章对宽容许可证的辩护及对 GPL 四自由与复杂性的概括。（BSD Now EP232，[1493.02-1706.66]，L2）
- 转述 Michael Dexter 的“ZFS versus OpenZFS”博文，含 Sun 2005 年以 CDDL 发布 ZFS、2010 年 Oracle 停止公开开发与 illumos 分叉的线索。（BSD Now EP232，[3306.54-3480.74]，L2）
- 转述 FreeBSD 基金会 2018 年 1 月开发项目更新，含 Meltdown/Spectre 缓解与 Kostik、Dimitry Andric 等人的分工。（BSD Now EP232，[2468.14-2777.78]，L2）
- 2006 年 Larry Ellison 接受《金融时报》采访的表态（转述）。（BSD Now EP222，[390.9-398.1]，L2）
- Netflix 架构科普文章，含 700 微服务、AWS 转码、DRM 与 Open Connect 的描述。（BSD Now EP222，[2014.12-2054.92]，L2）
- 转述 EuroBSDCon 2017 参会者 Vincent 的游记，含 OpenBSD 包工具、Coreboot、DragonFly 图形栈等演讲。（BSD Now EP222，[4664.98-4934.78]，L2）
- OpenZFS wiki 公司列表与 Dev Summit 材料；OpenBSD 技术邮件列表 KARL 状态帖；NetBSD announce 仓库转换公告；LibreSSL 发布说明。（BSD Now EP203，[148.62-5480.00]，L2）
- 本期可依凭的一手材料包括：epoll 手册页对自身多线程与 fork 缺陷的自述、POSIX 标准中 rm 处理失败与删除当前目录的条款原文、illumos 对 rm 的防护实现、2015 年 8 月 FreeBSD patch 工具经 ed 注入命令的安全修复、Oracle 首席安全官 Mary Ann Davidson 2015 年 8 月反对逆向工程的博客及其被撤下的过程、Torvalds 2001 年前后反对让内核可调试的邮件言论、2016 年 11 月 Linux 将 BUG_ON 批量替换为 WARN_ON 的补丁讨论，以及受访者本人保存的 Sun 时代工程经历与访谈录音本身。（BSD Now EP181，[10743.66-10765.86]，L2）
- 该期一手史料以 Losh 口述为主：2007 年起的 FreeBSD MIPS 移植与嵌入式推广经历、FreeBSD 9 计划引入 soft updates journaling 以获得接近 ZFS 的快速重启、Oracle 承诺每个 Solaris 大版本后发布 ZFS 源码转储；开场主持人并提及通知工具 biff 最早见于 4.0BSD，属其固定片头考据。（BSDTalk EP197，[34.00-144.00]，L1）
- 访谈提供的一手史料线索：Kirk McKusick 关于 BSD 文件系统与 TCP/IP 发明的系列历史讲座（DVD 与会议版本可获取）；BSDI 采用 1-800-ITS-UNIX 订购电话引燃 AT&T 商标与版权主张，USL 诉讼和解据称涉及约七个文件重写且细节从未完全披露；Berkeley 早期以磁带寄送修改并回收补丁的协作形态先于许可证概念出现。（Nerding Out with Victor EPS01E25，[131.0-372.0]，L2）
- OpenZFS 侧一手工程记录：Jude 自述 2018 年创立 Klara 提供 FreeBSD 与 ZFS 开发支持服务，为客户在 Ubuntu 的 LXD 容器中委托 ZFS 数据集以运行非特权 Docker 的特性由其团队开发并上游 OpenZFS，随后随 Ubuntu 22.04 进入生产环境，体现商业委托开发经上游回馈转化为发行版默认能力的路径。（Nerding Out with Victor EPS01E25，[2530.0-2652.0]，L1）
- 本期为 FreeBSD Fridays 系列第五期（由尾段改期公告可断为 2020 年 8 月中旬）的一手口述：主持人 Deb Goodkin 介绍讲者 Dan Langille 自 1998 年用 FreeBSD，创办 FreshPorts、FreshSource 与 BSDCan、PGCon 会议，其经验长期连载于 FreeBSD Diary；Langille 回忆当年听 Pawel Jakub Dawidek（转写音变为 powell 的讲座 pal 即 pjd）关于把 ZFS 导入 FreeBSD 的首场讲座，当即信服并沿用至今，自述约 2010 年前后起以 ZFS 为主存放备份数据（更早或已开始使用）；Goodkin 宣布系列自 8 月 28 日起改为隔周五举行，次周为 FreeBSD 安全导论。[考据脚注] 本流转写为开场介绍与正段双声轨交错混排，speaker 标记均为“未知”，人名与术语存在系统性音变，日期仅可由尾段改期陈述间接推定，引用前须与 FreeBSD Fridays 官方日程核对。（YouTube EPpN7OLChclH8，[10.72-3145.68]，L3）[订正：原[2993.2-3015.68]→[10.72-3145.68]，内容复核（开场“第五期/Goodkin 介绍”对应转写 [10.7-117.8]、2010 年前后起用 ZFS 对应 [149.9-168.2]、尾段改期公告对应 [3106.2-3145.7]，均落原区间外）]
- 该期含多则 Klara 公司当事人一手案例：某大学高可用系统误将同一存储池导入两台服务器，双写约 25 分钟致数据严重损坏，Klara 为此发明新修复工具并借 ZFS send 饱和 10Gb 网络抢回大部分数据；某早期全闪存阵列固件舍入错误致写入错位，由 ZFS 校验和暴露规律后促成厂商修复固件；Allan Jude 亦自述 2018 年创立 Klara、为 Ubuntu LXD 容器开发 ZFS 数据集委托特性并上游纳入 22.04 默认。（YouTube EPhTbqEf9LRGE，[2530.92-4601.12]，L1）[订正：原[4425.32-4601.12]→[2530.92-4601.12]，内容复核（全闪存阵列案例对应转写 3916.0-3948.52、创立 Klara/LXD 案例对应 2530.92-2662.68，均落原区间外）]

**史观**：

- 总纲4 分离聚合是永恒规律：OpenZFS 跨平台实现先分离后统一，社区与代码在聚合中重新整合：OpenZFS 在 2020 年统一 FreeBSD 与 Linux 代码库，体现长期分离后的再次聚合。（BSD Now EP491，[562.70-573.74]，L2）
- 总纲10 动手者创造历史：版本演进由内核、文件系统与驱动的逐项修复累积而成：DragonFly 与 NetBSD 的维护者以持续提交累积系统改进，动手者的日常修复构成系统演进。（BSD Now EP491，[188.06-530.00]，L2）
- 总纲9 经验优先：以长期运行积累的实测数据评估垃圾邮件防护，而非仅凭厂商宣称：greytrapping 以十五年实测数据衡量防护效果，经验数据优先于营销性宣称。（BSD Now EP491，[1134.30-1417.44]，L1）
- 总纲10 动手者创造历史：OpenZFS 峰会的进展来自各平台维护者在 ARC 内存协作、持久 L2ARC、顺序重建等具体工程上的改进，而非单一权威的主导。（BSD Now EP374，[1024.98-1169.92]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 代码在 FreeBSD、Linux、illumos、macOS、Windows 之间聚合，jail 则在 chroot 基础上分离出独立的隔离模型，两者皆呈现分离聚合的循环。（BSD Now EP374，[1848.72-2116.32]，L2）
- 总纲6 和解优于斗争：宽容许可证与 copyleft 的争论被呈现为两种自由观的冲突而非孰优孰劣的线性胜负，与和解优于斗争的取向相合。（BSD Now EP232，[1805.46-1871.3]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 社区以开源性质获得远高于 Oracle 专有分支的流行度，体现分离聚合与技术路线选择的偶然性而非必然性。（BSD Now EP232，[3541.7-3562.18]，L2）
- 总纲10 动手者创造历史：节目强调基金会出资使专职开发者能放下原计划、集中应对漏洞，呈现动手者创造历史的工程逻辑。（BSD Now EP232，[2586.3-2615.26]，L2）
- 总纲13 法律与道德是利益分配：Oracle 的双面被概括为“开源足够好就直接采用”，呈现企业以利益而非理念对待开源。（BSD Now EP222，[390.9-405.0]，L2）
- 总纲9 经验优先：Netflix 的 Open Connect 以 FreeBSD 作为边缘分发设备，被呈现为企业选型中经验与工程实践优先于流行度。（BSD Now EP222，[2320.66-2377.7]，L2）
- 总纲5 没有必然性，只有偶然性：ZFS 从 Sun 内部项目到 OpenZFS 社区的转折由诉讼、收购等偶然事件驱动，社区分叉后反而延续了技术生命，体现分离聚合与偶然性在文件系统史中的塑造。（BSD Now EP203，[148.62-241.44]，L2）
- 总纲10 动手者创造历史：KARL 把安全机制落实为每次开机的具体重构，由 Theo 与协助者在 hackathon 上动手实现，显示安全演进来自动手者的直接推进而非抽象原则。（BSD Now EP203，[4432.62-4690.58]，L2）
- 总纲9 经验优先：Cantrill 明确期待“someday historians are going to go back and watch these interviews and stuff and start writing the history of all this stuff that happened in the 90s”（4168.38-4176.08），把当事人访谈视为未来书写 1990 年代操作系统史的一手根据；这与以口述、邮件列表与当事人一手材料优先构筑历史叙述的取径一致，即先有可考的经验材料，方有可复核的历史。（BSD Now EP181，[4168.38-4176.08]，L1）
- 总纲21 革命与改革是历史方法论的分歧：Cantrill 将 Linux 的路径概括为“Linux is not designed. This is the problem. It evolves.”（9555.08-9562.86），并断言 ZFS、DTrace、容器与安全这类问题无法靠渐进演化达成，必须允许有人重新思考并以一次整体设计整合大块工作；由此他把工程文化的差异上升为两种历史方法论的对立——革命式的整体设计与改革式的增量演化，且认为后者的社区会自发排斥前者的实践者。（BSD Now EP181，[9555.08-9666.18]，L1）
- 总纲8 本体论上各方平等：Cantrill 拒绝单一赢家叙事：容器领域不存在所谓“VMware of containers”，技术世界的未来更像编程语言与数据库的多选格局，让人为任务挑选合适的系统，而 1990 年代式的一统天下思维已被证伪；他以 OpenSSL 单一文化酿成 Heartbleed 一类系统性风险为例，主张在开源世界维护异质生态，并在本体论层面把 FreeBSD、illumos 与 Linux 视为平等并存、各有设计中心的技术选项。（BSD Now EP181，[13198.74-13282.6]，L1）[订正：原 [13198.74-13253.74]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：Losh 强调 iXsystems 在对外发布前做了九个月幕后基础工作以先达到稳定点， FreeNAS 的展示价值依赖具体动手者的持续工程投入而非营销叙事。（BSDTalk EP197，[244.32-272.88]，L1）
- 总纲3 不存在进步，只有权力再分配：iXsystems 接管 FreeNAS 引发社区对商业公司收编的普遍焦虑，Losh 以 FreeBSD 式治理回应——做实际工作的人拥有最大话语权、开发全部公开、基础产品永久免费而收入来自整机与服务——显示项目控制权在个人维护者与公司之间的再分配，而非单纯的技术进步叙事。（BSDTalk EP197，[1828.74-1925.56]，L1）
- 总纲4 分离聚合是永恒规律：Losh 判断 ZFS 即使在 Oracle 停止发布代码的情况下也已有足够多的公司与 FreeBSD 社区承托而将长期自持演化，呈现核心技术器物脱离其原属商业母体后经由开源社区聚合再生的轨迹。（BSDTalk EP197，[1650.34-1681.78]，L1）
- 总纲5 没有必然性，只有偶然性：Jude 复述并认同的历史反事实：USL 诉讼恰在 386 普及窗口冻结 BSD 采用，芬兰学生 Linus 因 BSD 不可用转而自写内核，Jude 以其口吻称“若非 AT&T 诉讼，我根本不会费劲去写 Linux”（397.0）——Linux 的诞生由法律时序的偶然而非技术优劣决定，许可证纠纷改写了其后数十年的操作系统格局。 [存疑脚注] 该归因系访谈内反事实因果推断，Linus Torvalds 本人对开发动机的一手自述（1991 年 comp.os.minix 发布帖及自传）未被引证，回写大纲时须与一手材料交叉验证。（Nerding Out with Victor EPS01E25，[373.0-413.0]，L2）
- 总纲3 不存在进步，只有权力再分配：治理结构被 Jude 呈现为权力组织方案而非演进等级：Linux 集中于 Linus 与十余名副官的合并权，FreeBSD 则由约 250 名直接提交者每两年选举九人 core team，选举日前 365 天有提交记录者方可投票——两种共同体契约之间不存在谁更先进叙事，只呈现同一开源生产在权力分配上的不同解法。（Nerding Out with Victor EPS01E25，[1727.0-1783.0]，L1）
- 总纲4 分离聚合是永恒规律：ZFS 谱系呈现典型的分离聚合循环：Sun 开源、Oracle 收购后闭源、Illumos 与 ZFS on Linux 分头演化为分离，OpenZFS 统一上游仓库是对分离的再聚合；当事人以同一份源码在 FreeBSD 与 Linux 上完全一致为聚合完成之标准，并称各系统仅需保留与各自内核对接的薄层。（YouTube EPhTbqEf9LRGE，[2066.159-2293.4]，L1）

**辨析**：

- DragonFly 6.4 的具体内核修复与特性为发布说明转述，其中 GCC 默认版本与 HAMMER2 远程挂载状态需以官方发布说明与提交核验。 [存疑脚注] 版本细节为节目转述，须以 DragonFly 官方发布说明与提交记录核验。（BSD Now EP491，[188.06-530.00]，L4）
- OpenZFS 统一时间为 2020 年 12 月的表述为节目转述，需以 OpenZFS 官方公告核验。 [存疑脚注] 代码库统一的具体时间需以 OpenZFS 项目公告与提交记录确认。（BSD Now EP491，[562.70-573.74]，L4）
- 转写中 OpenBSD 6.8 随机种子置信度标记被表述为“RB_GOODRANDOM”，其具体宏名与语义应以 OpenBSD 6.8 发布说明及源码为准。 [存疑脚注] 具体宏名待官方变更日志核对（BSD Now EP374，[397.32-447.44]，L4）
- 宽容许可证的讨论源自一篇德语科技网站争论的二手转述，博客作者身份与原始争论语境未能从转写确认，各阵营主张未经独立核验。 [存疑脚注] 博客原文语境与争论双方身份无法从转写核实（BSD Now EP232，[1493.02-1547.18]，L4）
- Netflix 架构细节（微服务数量、DRM 与缓存策略）系二手科普文章转述，且节目自身注明“地图不按比例”等不确定处，具体数字须以 Netflix 工程博客核实。 [存疑脚注] 架构数字系二手转述，须以 Netflix 官方资料核实（BSD Now EP222，[2631.92-2643.76]，L4）
- Cantrill 称 Linux MADV_DONTNEED 的破坏性语义源自 Digital UNIX 并由 Tru64 延续（9320.40-9324.60），另以 JemAlloc 对该行为清零保证的隐性依赖说明其危害之隐蔽；此溯源与 Tru64 语义谱系的论断均为访谈口述的单一来源推断，属于可辨识但未独立核证的细节。 [存疑脚注] MADV_DONTNEED 消极语义源自 Digital UNIX/Tru64 的谱系仅见本期口述，未核对 Tru64 手册页与 Linux man-pages 变更史，采信前需查证（BSD Now EP181，[9078.20-9338.74]，L4）[订正：原 [9320.40-9338.74]，2026-09-30 SenseAudio 重转核对]
- Losh 关于基础产品永久免费、不搞快照独占、按 FreeBSD 模式开放治理的表述属 2010 年 9 月当事人的意图性承诺，其兑现程度（尤其 FreeNAS 之后向 TrueNAS 的转型路径）须与后续项目实际演化交叉验证后方可作为史实引用。 [存疑脚注] 当期承诺性陈述，非既成史实；与 260.2 TrueNAS 企业化演进的后续记载互证后方可采信（BSDTalk EP197，[1828.74-1969.14]，L5）
- ZFS 入 Linux 的法律争议在访谈中被简化为实践事实：CDDL 与 GPL 的链接不兼容使 ZFS 长期被 mainline 拒之门外，而 Ubuntu 转为自行编译随发行版提供，Jude 称“结果证明没人起诉他们”（2428.0）——但未被起诉不等于合法性确认，软件自由保护组织等机构 2016 年前后的公开质疑并无司法结论，回写大纲时应作为未决争议点而非定论。 [存疑脚注] 无人起诉即安全的说法为访谈中的实践性推断，CDDL 模块与 GPL 内核合体发行的效力无判例支撑，须对照软件自由保护组织 2016 年公开信等一手文献核实。（Nerding Out with Victor EPS01E25，[2331.0-2428.0]，L2）
- 讲者专设破除传言一节，逐一回应 ZFS 社区流传的门槛之说：单盘系统用 ZFS 亦有价值——得校验与与快照之利，错误可察而不可纠，除非启用 extra copies 这类高级选项；没有 ECC 内存亦可运行 ZFS，有则更佳，“无 ECC 的 ZFS 胜过没有 ZFS”；无需高端硬件，家用市售盘即可，二手 HBA 约六十至一百美元，普通 PC 机箱足够；亦无需大内存，他一只仅 1GB 内存、余 250MB 的 DigitalOcean droplet 上运行 ZFS 承载 Nagios 监控，性能不高但够用。（YouTube EPpN7OLChclH8，[2197.04-2393.839]，L1）
- 讲者自承本讲面向新手“极端简化”，多处明言“这是过度简化，稍后再讲”，且对 RAID Z1 的最小盘数自记不清（“至少四块，也可能三块”）；幻灯示例还曾因照搬官方文档而误导读者，他自行加注后才敢出示。引用其数值与命令示例时不宜直接当作规范口径，须以 OpenZFS 文档复核。[已核备注] 本条所据转写经滚动重叠重建后已成线性单轨文本，段落次序与音轨归属已还原（rev6 逐字复核通过）；RAID Z1 最小盘数等参数仍系讲者现场追忆（“至少四块，也可能三块”），未经文档核验。（YouTube EPpN7OLChclH8，[352.8-796.9]，L4）[订正：原“[存疑脚注] 全部内容为单一讲者口述加现场演示，转写双声轨交错，细节精度有限。 [存疑脚注] RAID Z1 最小盘数等参数系讲者现场追忆，未经文档核验；转写交错导致段落次序与音轨归属需人工还原”→依重建后转写（[533.7-553.1] 段线性连贯、无交错）改写为已核备注，保留参数未经核验之提示；原[532.88-545.68]→[352.8-796.9]，内容复核（“面向新手简化”对应转写 [352.8-357.1] 与 [791.4-796.9]、RAID Z1 最小盘数对应 [533.7-553.1]、“这是过度简化，稍后再讲”对应 [706.6-712.2]、照搬文档误导并加注对应 [777.8-796.9]，均落原区间外）]
- CDDL 与 Mozilla MPL 基本等同，非病毒式许可且允许编译产物以任意许可发布，与 GPL 的真正冲突在于 GPL 要求链接进内核的代码一并转为 GPL 而 CDDL 禁止再授权，故 ZFS 至今未入 mainline Linux；Ubuntu 以 DKMS 为用户编译内核模块发行且无人起诉，遂成事实上的通行做法。 [存疑脚注] CDDL/GPL 冲突的这一定性系 Allan Jude 单方解释，未经法庭裁决，应与 FSF 及 Sun 各自发布的法律分析文本交叉验证（YouTube EPhTbqEf9LRGE，[2333.24-2450.96]，L4）[订正：原[2333.24-2447.0]→[2333.24-2450.96]，内容复核（条目明言 DKMS，对应转写 2447.0-2450.96，落原区间外）]

**文献**：

- [BSD Now EP491] Pennington J. BSD Now: 491: Catch the Spammers[EB/OL]. (2023-01-26)[2026-08-15]. <https://www.bsdnow.tv/491>.
- [BSD Now EP374] Pennington J. BSD Now: 374: OpenBSD’s 25th anniversary[EB/OL]. (2020-10-29)[2026-08-15]. <https://www.bsdnow.tv/374>.
- [BSD Now EP232] Pennington J. BSD Now: 232: FOSDEM 2018[EB/OL]. (2018-02-07)[2026-08-15]. <https://www.bsdnow.tv/232>.
- [BSD Now EP222] Pennington J. BSD Now: 222: How Netflix works[EB/OL]. (2017-11-29)[2026-08-15]. <https://www.bsdnow.tv/222>.
- [BSD Now EP203] Pennington J. BSD Now: 203: For the love of ZFS[EB/OL]. (2017-07-19)[2026-08-15]. <https://www.bsdnow.tv/203>.
- [BSD Now EP181] Pennington J. BSD Now: 181: The Cantrillogy (Not special edition)[EB/OL]. (2017-02-15)[2026-08-15]. <https://www.bsdnow.tv/181>.
- [BSDTalk EP197] Backman W. BSDTalk: 197: bsdtalk197 - FreeNAS 8 with M. Warner Losh[EB/OL]. (2010-09-19)[2026-08-27]. <https://bsdtalk.blogspot.com/2010/09/bsdtalk197-freenas-8-with-m-warner-losh.html>.
- [Nerding Out with Victor EPS01E25] Petersson V. Nerding out with Victor: All things ZFS and FreeBSD with Allan Jude[EB/OL]. (2024-12-02)[2026-08-15]. <https://vpetersson.com/podcast/s01e25/>.
- [YouTube EPpN7OLChclH8] YouTube. YouTube: FreeBSD Fridays: Introduction to ZFS[EB/OL]. (发布日期不详)[2026-08-15]. <https://www.youtube.com/watch?v=pN7OLChclH8>. [订正：原"()"→"(发布日期不详)"，内容复核（该集发布日期 DB episodes.publish_date 与转写均未载，对齐 112.10 行著录）]
- [YouTube EPhTbqEf9LRGE] YouTube. YouTube: All Things ZFS and FreeBSD with Allan Jude: Snapshots, Replication & Real-World Use[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=hTbqEf9LRGE>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-213 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-213`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting〕讲者口述：讲者提到 Paweł Dawidek（转写音作 paul doydek）在五年前曾为 FreeBSD 做过与 zfs list 相关的实现。（YouTube EP-WwwomHkAZg，[186.959-195.19]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-223 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-223`；w172 YouTube 章节路由采纳）

据〔July 2024 OpenZFS Leadership Meeting〕讲者口述：讲者将产品部署到 FreeBSD jail，最初打算用 ZFS clones 但很快遇到问题。（YouTube EP1BoXxarifw8，[2121.8-2131.03]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-227 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-227`；w172 YouTube 章节路由采纳）

据〔2018 年 10 月 OpenZFS 领导层会议〕讲者口述：Jurgen 完成 FreeBSD 平台 ZFS 移植并持续维护。（YouTube EP2Bi0ZicXEz0，[387.229-399.589]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-251 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-251`；w172 YouTube 章节路由采纳）

据〔QAT 硬件加速演讲〕讲者口述：讲者说明其测试用 zpool 由三块 NVMe 组成，并提到使用 FIO 工具。（YouTube EP4zWTU_hnGp0，[943.72-946.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-252 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-252`；w172 YouTube 章节路由采纳）

据〔QAT 硬件加速演讲〕讲者口述：ZFS 默认使用 Fletcher 校验和，讲者借向 zpool 写入文件来观察加速测试的结果。（YouTube EP4zWTU_hnGp0，[1263.88-1268.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-256 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-256`；w172 YouTube 章节路由采纳）

据〔State of OpenZFS 2019〕讲者口述：ZFS on Linux、ZFS on FreeBSD、ZFS on Mac OS 三个平台各有独立仓库。（YouTube EP5e8emXau64U，[232.18-238.83]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-257 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-257`；w172 YouTube 章节路由采纳）

据〔State of OpenZFS 2019〕讲者口述：下一大版本将命名为 OpenZFS 2.0 用于 Linux 与 FreeBSD，不会再叫 0.9。（YouTube EP5e8emXau64U，[929.8-943.02]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-274 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-274`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：ZFS 已移植到 FreeBSD 数年，2010 年发生了影响演进的重要事件。（YouTube EP8T9Rh-46jhI，[507.39-511.599]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-273 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-273`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：ZFS 与 OpenZFS 的缘起，其开发始于 2001 年的 Sun 公司。（YouTube EP8T9Rh-46jhI，[449.23-454.497]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-317 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-317`；w172 YouTube 章节路由采纳）

据〔April 2020 OpenZFS Leadership Meeting〕讲者口述：FreeBSD 已有一些被称作 live ZFS FS 的工作可资借鉴。（YouTube EPAfvBY8du8OE，[66.42-74.149]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-318 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-318`；w172 YouTube 章节路由采纳）

据〔April 2020 OpenZFS Leadership Meeting〕讲者口述：FreeBSD 尚无 SMB 组件，因此 illumos 移植 SMB 相对容易。（YouTube EPAfvBY8du8OE，[261.45-266.18]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-388 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-388`；w172 YouTube 章节路由采纳）

据〔OpenZFS Developer Summit 2016〕讲者口述：Matt Ahrens 回顾道，从 OpenZFS 发布至今大约只有三年时间。（YouTube EPCIJGUNDZ9yE，[460.039-463.16]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-407 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-407`；w172 YouTube 章节路由采纳）

据〔2023 年 1 月 OpenZFS 领导层会议〕讲者口述：FreeBSD 的 Mark Johnson 在 makefs 工具中创建了 ZFS 支持。（YouTube EPD6gOgkEG9X0，[2774.16-2779.73]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-422 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-422`；w172 YouTube 章节路由采纳）

据〔2018 OpenZFS Developer Summit〕讲者口述：OpenZFS 是 SPI（Software in the Public Interest，一家非营利组织）旗下的关联项目，起步于讲述时约两年前。（YouTube EPDearbVpOTro，[187.33-202.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-421 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-421`；w172 YouTube 章节路由采纳）

据〔2018 OpenZFS Developer Summit〕讲者口述：Matt Ahrens 是 ZFS 的联合创始人，同时被称作 OpenZFS 的“父亲”。（YouTube EPDearbVpOTro，[0.03-11.38]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-481 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-481`；w172 YouTube 章节路由采纳）

据〔2025 年 3 月 OpenZFS 领导组会议〕口述：议题 16967 内容为为 Linux 增加原生 NFSv4 风格的 ZFS ACL 支持。（YouTube EPEXyIqCP7bDI，[540.839-553.47]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-482 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-482`；w172 YouTube 章节路由采纳）

据〔2019-05-28 OpenZFS Leadership Meeting〕讲者口述：即便涉及 Linux 相关代码进入 FreeBSD，底层仍统一走既有 Solaris 移植层。（YouTube EPEzyPr3BuePo，[464.86-468.06]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-526 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-526`；w172 YouTube 章节路由采纳）

据〔March 2020 OpenZFS Leadership Meeting〕讲者口述：2020 年的分析发现，ZFS 能把少量 NVMe 盘打到接近其硬件性能的吞吐。（YouTube EPFVwYAwrKZCU，[484.389-498.309]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-525 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-525`；w172 YouTube 章节路由采纳）

据〔March 2020 OpenZFS Leadership Meeting〕讲者口述：2020 年 3 月该会议提到，ZFS 的 FreeBSD 移植仓库已迁到 OpenZFS 组织名下。（YouTube EPFVwYAwrKZCU，[21.84-36.53]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-553 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-553`；w172 YouTube 章节路由采纳）

据〔2022年7月 OpenZFS 领导层会议〕讲者口述：有实测数据显示，约 5000 万个文件的目录操作耗时约 2.3 毫秒，且该测试由极快的 NVMe 存储支撑。（YouTube EPGPgy9ATYeYY，[2586.96-2594.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-586 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-586`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting〕讲者口述：团队除在 Linux 上继续开发工具外，另有一个独立的示例内核模块 vfs-zfs 与之并行推进。（YouTube EPHjkV7vuKATM，[1474.08-1482.59]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-621 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-621`；w172 YouTube 章节路由采纳）

据〔2024 OpenZFS Developer Summit〕讲者口述：2024 年 OpenZFS 用户与开发者峰会的举办地已不再是旧金山。（YouTube EPIIj6LCSRTNA，[2.88-15.4]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-622 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-622`；w172 YouTube 章节路由采纳）

据〔2024 OpenZFS Developer Summit〕讲者口述：讲者称会议领导权已由 Michael Dexter 接手，并把大会带到俄勒冈州波特兰。（YouTube EPIIj6LCSRTNA，[89.32-100.76]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-707 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-707`；w172 YouTube 章节路由采纳）

据〔June 2025 OpenZFS Leadership Meeting〕讲者口述：2025 年 6 月的会议讨论到，FreeBSD 上 ZFS 只允许挂载，之后仍需用户态 VFS 挂载步骤。（YouTube EPKr_3FtJUvVU，[2996.24-3004.309]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-719 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-719`；w172 YouTube 章节路由采纳）

据〔2024 OpenZFS Developer Summit〕讲者口述（Rob Norris 被引用为相关改进者，非主张人）：讲者提出 ZIL 可置于特殊 vdev（转写 special vdev），因写入主 dRAID 需以 total syncs 穿过全部设备而不高效。（YouTube EPL81FeMEf2JE，[1863.559-1880.159]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-731 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-731`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting〕讲者口述：OpenZFS 的 mount daemon 会读取 /etc/exports 与 /etc/zfs/exports，后者即各数据集的 share-nfs 属性。（YouTube EPLi8Z08KZvg8，[557.44-565.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-938 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-938`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting 2025-10〕讲者口述：FreeBSD 一侧有一个改动，为把数据集委派给 jail 的场景新增了一个数据集属性。（YouTube EPSJb0QS-yMXU，[2118.64-2125.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-937 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-937`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting 2025-10〕讲者口述：有一个问题把文件的记录大小错误地报告成 512 字节，而不是其真实大小。（YouTube EPSJb0QS-yMXU，[603.36-610.949]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-962 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-962`；w172 YouTube 章节路由采纳）

据〔June 25, 2019 OpenZFS Leadership Meeting〕讲者口述：2019 年 6 月 25 日会议中，ZFS 模块新增 os 目录，下设 freebsd 与 linux 子目录，平台相关文件归入其中。（YouTube EPTJwykiJmH0M，[200.549-207.379]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1049 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1049`；w172 YouTube 章节路由采纳）

据〔OpenZFS 领导组会议 2021年2月〕讲者口述：FreeBSD 曾使用 OpenZFS 主干（转写音作 open cfs），后改为基于 OpenZFS 发布分支发行。（YouTube EPVmXoHO2PDP4，[1086.799-1098.47]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1048 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1048`；w172 YouTube 章节路由采纳）

据〔OpenZFS 领导组会议 2021年2月〕讲者口述：更现实的时间表是在 FreeBSD 13.1 中更新 OpenZFS。（YouTube EPVmXoHO2PDP4，[801.44-808.15]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1094 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1094`；w172 YouTube 章节路由采纳）

据〔2019年11月 OpenZFS 领导组会议〕讲者口述：讨论的变更需至 OpenZFS 2.0（转写音作 olicity opens the FS 2.0）才会正式发布（YouTube EPWKfS3lAmLGc，[295.55-303.61]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1107 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1107`；w172 YouTube 章节路由采纳）

据〔2024年6月 OpenZFS 领导层会议〕讲者口述：为使 ZFS 在 Linux 与 FreeBSD 上获得支持，两者都必须走一遍 Solaris 兼容层。（YouTube EPWXmcAFnjfWc，[654.04-662.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1149 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1149`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, March 2022〕讲者口述：OpenZFS 数据集如同在 illumos（转写音作“lumos”）委派给 zone、在 FreeBSD 委派给 jail 那样可被委派（YouTube EPXZ0a2Ctn38I，[2346.56-2353.19]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1223 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1223`；w172 YouTube 章节路由采纳）

据〔OpenZFS 领导组会议 2021年3月〕讲者口述：OpenZFS 3.0（转写音作 open vfs）与 2.0 兼容。（YouTube EPZXkSVkq0bgM，[203.44-208.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1206 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1206`；w172 YouTube 章节路由采纳）

据〔2021年1月 OpenZFS 领导组会议〕讲者口述：会议期待 openzfs 3.0（转写音作 open zfs 3.0）成为下一个主要版本（YouTube EPZhx17DyCWFo，[180.56-188.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1207 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1207`；w172 YouTube 章节路由采纳）

据〔2021年1月 OpenZFS 领导组会议〕讲者口述：其将 openzfs 3.0 描述为 zfs on linux 历史上最快的一次主要版本（YouTube EPZhx17DyCWFo，[192.56-198.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-292 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-292`；w172 YouTube 章节路由采纳）

据〔LISA 2013〕讲者 George Wilson 口述：ZFS 于 2005 至 2006 年首次面向客户出货，FreeBSD 集成则在 2008 年完成。（YouTube EP_cIZIy0E0ZA，[126.52-138.15]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-293 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-293`；w172 YouTube 章节路由采纳）

据〔LISA 2013〕讲者 George Wilson 口述：他称数月前宣布的 OpenZFS 是 ZFS 的首个真正开源后继项目（原文 just a few months ago we announced openzfs um as the first truly open source successor for ZFS）。（YouTube EP_cIZIy0E0ZA，[201.319-214.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-338 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-338`；w172 YouTube 章节路由采纳）

据〔2026年5月 OpenZFS 领导组会议〕讲者口述：会议正在评估更新或重写 ZFSd 的方案（YouTube EPb2KfBySYBRQ，[772.8-778.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-347 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-347`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, May 2023〕讲者口述：会议称团队已推进到希望在 FreeBSD 与另一平台上同时采用新版 ZFS 的阶段（YouTube EPbhsbBo4tnrs，[430.38-436.73]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-397 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-397`；w172 YouTube 章节路由采纳）

据〔DirectIO for ZFS 演讲〕讲者 Brian Atkinson 口述：其所在机构（转写音作 lanol，同转写前文作 lanl；无据称 Lenovo）在下一代并行文件系统方向关注 Luster-ZFS（转写音作 luster zfs）与其底层 NVMe 设备（YouTube EPcWI5_Kzlf3U，[279.52-288.15]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-398 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-398`；w172 YouTube 章节路由采纳）

据〔DirectIO for ZFS 演讲〕讲者 Brian Atkinson 口述：Matt Macy 完成了 DirectIO 的全部 FreeBSD 移植工作（YouTube EPcWI5_Kzlf3U，[1610.96-1616.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-426 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-426`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting 2019-04-23〕讲者口述：Chris Mo 团队完成 OpenZFS 在 FreeBSD 上的可测试移植（YouTube EPdIVGGJaZ7zk，[974.16-983.189]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-431 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-431`；w172 YouTube 章节路由采纳）

据〔January 2024 OpenZFS Leadership Meeting〕讲者口述：讲者称 FreeBSD main 分支与 zfs-master 保持同步（转写音作 FreeBSD Master main synit with ZFS Master）（YouTube EPdOhRPyQzTA0，[382.319-395.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-493 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-493`；w172 YouTube 章节路由采纳）

据〔Second January 2024 OpenZFS Leadership Meeting〕讲者口述：Solaris 在磁碟上存在 UFS 时就必须关闭写入缓存（转写音作 right caching）（YouTube EPfbvkgSFy5Oc，[3476.16-3484.15]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-497 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-497`；w172 YouTube 章节路由采纳）

据〔BSDCan〕讲者 Matt Ahrens 口述：ZFS 的贡献者来自 FreeBSD、Linux 与 macOS 等多个社区（YouTube EPfcTTNfSLhao，[2321.97-2334.5]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-540 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-540`；w172 YouTube 章节路由采纳）

据〔September 2025 OpenZFS Leadership Meeting〕讲者口述：讲者已为新的 ZFS 创建 vendor branch，用于拆分 ZFS 2.4 相关变更。（YouTube EPgAogrbmkbHw，[1357.52-1366.87]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-587 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-587`；w172 YouTube 章节路由采纳）

据〔October 2019 OpenZFS Leadership Meeting〕讲者口述：由于该仓库不只服务 Linux 也服务 FreeBSD，此后将不再以“ZFS on Linux”命名。（YouTube EPhL31yMN6Eq0，[645.28-655.65]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-579 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-579`；w172 YouTube 章节路由采纳）

据〔April 2024 OpenZFS Leadership Meeting〕讲者口述：早年曾试图在 Linux 与 FreeBSD 之间统一 sharenfs 属性（转写音作 share NFS）。（YouTube EPhabANXNHPWQ，[1774.48-1782.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-638 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-638`；w172 YouTube 章节路由采纳）

据〔2024 OpenZFS User Summit〕讲者口述：在 VFS 层获取文件名开销很大（YouTube EPiYAWcKeE8fA，[403.96-411.24]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-639 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-639`；w172 YouTube 章节路由采纳）

据〔2024 OpenZFS User Summit〕讲者口述：审计的一种做法是复用 zfs diff 所用的同一调用，阻塞一切活动直至其返回（转写音作 ZFS diff）（YouTube EPiYAWcKeE8fA，[411.24-428.44]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-640 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-640`；w172 YouTube 章节路由采纳）

据〔2024 OpenZFS User Summit〕讲者口述：ZFS 会重用 inode 号，讲者称约十万次删除后即回绕回收，以免无谓地递增到尽头（YouTube EPiYAWcKeE8fA，[513.92-526.12]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-697 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-697`；w172 YouTube 章节路由采纳）

据〔September 2019 OpenZFS Leadership Meeting〕讲者口述：ZFS on Linux 与 FreeBSD 的用户命名空间实现略有差异，ZFS on Linux 上呈现为带 user. 前缀（转写音作 user dot prefix）（YouTube EPkjBWhEE8tZ8，[675.87-688.16]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-756 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-756`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：libzfs 是支撑 zpool 与 zfs 命令行工具的内部库。（YouTube EPmJW6xz2gcF8，[527.92-536.31]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-757 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-757`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：解决该问题有同类做法——FreeBSD 把 libzfs 视作私有库，它只被 FreeBSD 内部工具使用，因此版本必然一致，不会出现版本不匹配。（YouTube EPmJW6xz2gcF8，[1465.52-1472.95]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-795 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-795`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, June 2021〕讲者口述：OpenZFS 讨论中将隔离实现与 Solaris 的 zones、BSD 的 jails 机制作类比（YouTube EPnVYeW48SxWk，[374.08-377.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-813 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-813`；w172 YouTube 章节路由采纳）

据〔October 2022 OpenZFS Leadership Meeting〕讲者口述：新增的重命名系统调用（转写音作 rename apps）可原子交换两个文件。（YouTube EPoNNTEIYX2zc，[173.76-178.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-814 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-814`；w172 YouTube 章节路由采纳）

据〔October 2022 OpenZFS Leadership Meeting〕讲者口述：FreeBSD 上 whiteout 可为常规文件，UFS 已有支持。（YouTube EPoNNTEIYX2zc，[425.52-430.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-834 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-834`；w172 YouTube 章节路由采纳）

据〔September 2024 OpenZFS Leadership Meeting〕讲者口述：他已把更多组件移入用户态，含 ZFS ioctl 与 ZFS VFS 操作。（YouTube EPpAI_Tb5ik3c，[3120.76-3131.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-858 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-858`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, September 2022〕讲者口述：本次为 2022 年 9 月的 OpenZFS 领导层会议（YouTube EPpWSXah94Tw0，[0.08-2.47]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-859 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-859`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, September 2022〕讲者口述：OpenZFS 相关项目早期曾有支持完整 NFSv4 的讨论（YouTube EPpWSXah94Tw0，[622.16-625.269]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-970 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-970`；w172 YouTube 章节路由采纳）

据〔ZFS idmapped mount 分享〕讲者 Youzhong Yang 口述：与 ext4、XFS（转写音作 est4 xfs）类似，ZFS 亦须实现 idmapped mount 到 NFS server 的通路，才能支持 SMB（转写音讹作 SMP）Windows 访问。（YouTube EPtTHUtegxfro，[820.32-832.35]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-971 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-971`；w172 YouTube 章节路由采纳）

据〔ZFS idmapped mount 分享〕讲者 Youzhong Yang 口述：Linux 内核 5.2 之后 ext4 与 XFS 已支持 idmapped mount（原句转写音作 X4 xfs），但 NFS server 尚未支持，因此 OpenZFS 亦未获得支持。（YouTube EPtTHUtegxfro，[788.399-798.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1018 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1018`；w172 YouTube 章节路由采纳）

据〔FreeBSD Day 2024〕讲者 Allan Jude 口述：讲者聚集人员创办 Klara（转写音作 Clara），提供 FreeBSD 与 OpenZFS 相关的开发与支持服务。（YouTube EPuXjTRaLRRYA，[164.48-171.509]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1017 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1017`；w172 YouTube 章节路由采纳）

据〔FreeBSD Day 2024〕讲者 Allan Jude 口述：Matt Ahrens（转写音作 Matt Erin's）是 ZFS 项目 2001 年的创始人之一，其缺席期间讲者承担相关 backup host 职责。（YouTube EPuXjTRaLRRYA，[660.92-669.269]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1058 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1058`；w172 YouTube 章节路由采纳）

据〔March 2023 OpenZFS Leadership Meeting〕讲者口述：讲者说明向容器委派数据集时，FreeBSD 侧使用 jail，另一侧使用 LXD 容器。（YouTube EPvrTSukIwQzQ，[3100.38-3109.309]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1108 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1108`；w172 YouTube 章节路由采纳）

据〔November 2023 OpenZFS Leadership Meeting〕讲者口述：为使 sendfile 在 ZFS 上正常工作，需在 FreeBSD 上处理系统 page cache（转写音作 send file）。（YouTube EPwy9M39Yb_7E，[2527.92-2538.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1116 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1116`；w172 YouTube 章节路由采纳）

据〔January 2020 OpenZFS Leadership Meeting〕讲者口述：据 Mozilla 等资料，OpenSSL 支持 TLS 1.3 的两种模式但仅启用 GCM。（YouTube EPx9-wua_mzt0，[2816.18-2826.4]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1117 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1117`；w172 YouTube 章节路由采纳）

据〔January 2020 OpenZFS Leadership Meeting〕讲者口述：Intel 处理器上 12 倍的加速来自移植 OpenSSL 的汇编例程。（YouTube EPx9-wua_mzt0，[2854.88-2863.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1340 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1340`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者自报姓名（转写讹作 'Paul de Leeuw'，与标题 'Paul Dagnelie' 不符）并自述其演讲主题为 ZFS；转写标题逐字载明 'Dedup Send Receive by Paul Dagnelie'。（YouTube EPyPObFI-QU0o，[5.3-9.8]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1194 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1194`；w172 YouTube 章节路由采纳）

据〔March 2024 OpenZFS Leadership Meeting〕讲者口述：讲者查阅 Solaris 旧补丁以推进 ZFS 更接近零拷贝（转写音作 closer to zero copy）的实现。（YouTube EPz7ond6CCLH0，[1806.08-1820.269]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1193 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1193`；w172 YouTube 章节路由采纳）

据〔March 2024 OpenZFS Leadership Meeting〕讲者口述：讲者向会议询问是否有人在 Linux 或 FreeBSD 上的 ZFS 中遇到过 sendfile 系统调用（转写音作 send file）特别有用的用例。（YouTube EPz7ond6CCLH0，[1783.44-1793.83]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1208 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1208`；w172 YouTube 章节路由采纳）

据〔Fault Management 分享〕讲者 Don Brady 与 Justin Gibbs 口述：ZFS 故障管理代码正再次向 OpenZFS 内部迁移。（YouTube EPzJbQiqdcpDg，[99.88-108.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1209 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1209`；w172 YouTube 章节路由采纳）

据〔Fault Management 分享〕讲者 Don Brady 与 Justin Gibbs 口述：讲者称这些变更多数已上游进入 FreeBSD，余下少数则多半经 illumos 上游后回流 FreeBSD。（YouTube EPzJbQiqdcpDg，[710.72-717.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1195 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1195`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, January 2025 (second)〕讲者口述：ZFS 很早就一贯支持 NFS 风格的 ACL，长期存在于 NAS 系统形态中（转写音作 solarus Lumas and 3bd，疑为 Solaris、illumos、BSD 讹字）（YouTube EPzcwyVgHqqH8，[1998.48-2009.669]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1196 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1196`；w172 YouTube 章节路由采纳）

据〔OpenZFS Leadership Meeting, January 2025 (second)〕讲者口述：FreeBSD 与 illumos 上的 NFS 直接支持这些 ACL；在 Samba（转写音作 samb）中同样支持，并把 Windows ACL 映射为 nfsv4 风格 ACL，使文件系统能按 Windows 的方式管理访问控制。（YouTube EPzcwyVgHqqH8，[2028.679-2038.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1451 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1451`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：本场报告为 ZFS 设备移除（device removal）功能的全长技术深潜；主持人口述该功能已在 Delphix 产品中使用了多年，近期才移植进 Linux 树。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1452 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1452`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：ZFS 设备移除功能是在 2012 年前后于 Delphix 公司设计开发的。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1453 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1453`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：开发初期设想的主要用例是回收超配的存储：客户往池中加入了过多磁盘，或只为一个月的临时项目临时扩容，之后希望把这部分空间移除。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1454 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1454`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：该“回收超配空间”设想后来被证明并不是真实的用例。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1455 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1455`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：实践中真正最主要的使用场景是存储迁移：把池中所有磁盘移除，并把存储数据迁到一批容量或数量都可能不同的新磁盘上。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1456 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1456`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：设备移除与 detach 的区别在于：它移除整个顶层镜像并实际缩减存储池总容量，而 detach 只能移除镜像的一侧、不减少池容量，自 ZFS 之初即可做到。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1457 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1457`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：当时该功能要求池中所有设备的 asize 一致，支持裸盘与镜像，不支持 RAID-Z；RAID-Z 组的移除被列为未来工作。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1458 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1458`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：设备移除单次映射的可分配空间上限在两树之间不同：Linux 上为 16MB，而 FreeBSD 与 illumos 上仅 1MB。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1459 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1459`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：最佳情况下单次映射可达 16MB，映射表每行占 24 字节，内存开销由此降为每移除 1TB 设备约 1.5MB。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1460 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1460`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：在讲者给出的最坏碎片形态下，映射内存开销理论可达每 TB 磁盘 600MB；而实践中观测到的最坏值约为每 TB 100MB。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1461 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1461`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：设备移除的映射允许跨越长度不超过 32K 的空闲片段，理论上可使映射内存开销降低一千倍。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1462 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1462`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：该跨越空闲片段的机制最初并未实现，早期表现明显更差；加入它之后，实践中观测到的最坏情况改善了约十倍。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1463 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1463`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：该功能自 2015 年起在 Delphix 产品中生产使用，并于当年早些时候合入全部上游仓库。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1464 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1464`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Device Removal by Matt Ahrens（Matt Ahrens 的 OpenZFS 大会全长技术报告）讲者口述：设备移除通过查看空间映射（space map）来定位待迁移的已分配空间，而不是像 zpool scrub 或 resilver 那样去找全部块指针、因而无须遍历整个存储池的间接块树。（YouTube EPKGnFhmG8gT0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1558 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1558`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 1 月第二次 OpenZFS 领导组会议〕讲者口述：2.2 版本能否切分支受制于零克隆（zero claim）这一前置项，在其实现之前跨数据集的块克隆无法放行，讲者自估还需约一个月返工。（YouTube EP94HaCotHBAA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1559 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1559`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 1 月第二次 OpenZFS 领导组会议〕讲者口述：ChaCha20 加密算法提案中，FreeBSD 侧直接调用既有的软件加密路径，Linux 侧另写模块实现，而 illumos 的代码树缺少相应算法；会议倾向信任外部参考实现，只由社区审阅 ZFS 相关改动与手册页措辞。（YouTube EP94HaCotHBAA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1560 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1560`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 1 月第二次 OpenZFS 领导组会议〕讲者口述：ARC 缓存驱逐的幽灵态逻辑因只先驱逐数据、后触及元数据而长期失衡，已废弃多年且部分算法早于 ARC；提交者抹除该段代码，重写为约两页的四个状态自适应平衡。（YouTube EP94HaCotHBAA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1561 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1561`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 1 月第二次 OpenZFS 领导组会议〕讲者口述：主张每年切一次发布、不为等长周期特性而推迟，并指出主分支已具备测试就绪状态、切维护分支亦便于回移。（YouTube EP94HaCotHBAA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1563 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1563`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2020 OpenZFS Leadership Meeting〕讲者口述：会议首项议题为废弃带去重的 ZFS 发送流，废弃提示已加入 master 并回移到 0.8 分支，下一版 0.8 将带出该提示。（YouTube EPhGTjxSypEKU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1564 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1564`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2020 OpenZFS Leadership Meeting〕讲者口述：另开 PR 新增 zstream-redo 工具，把去重发送流转成普通发送流，使老快照的去重发送流仍可被新软件长期接收，同时保留 zstream dump 作为别名。（YouTube EPhGTjxSypEKU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1565 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1565`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2020 OpenZFS Leadership Meeting〕讲者口述：讨论 o_direct 时决定，若启用校验和或相关特性，须在 I/O 期间把用户缓冲区在内存复制一份；理由是校验和必须对应真正写入磁盘的数据。（YouTube EPhGTjxSypEKU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1566 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1566`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2020 OpenZFS Leadership Meeting〕讲者口述：会议提议新增一层 ZFS 管理 API（会中作 live ZFS API），动机是简化应用的集成成本——当时所见各类集成都要调用 zpool、ZFS 命令行再解析其输出，讲者希望有一个可供这些集成直接改用的 API。（YouTube EPhGTjxSypEKU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1584 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1584`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2021 OpenZFS Leadership Meeting〕讲者口述：会上提出在 ztest 运行中启用 address sanitizer，理由是让它覆盖代码中潜在或随新改动引入的内存问题；随后有人提到 FreeBSD 项目的 Mark Johnston 另有一个 pull request 待并入，修的是他在 FreeBSD 内核中实际运行 ZFS、并用内核内存消毒器（kernel memory sanitizer）时发现的若干问题。（YouTube EP5Lby_Vl6H88，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1585 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1585`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2021 OpenZFS Leadership Meeting〕讲者口述：Ryan 说明扩展属性在不同平台上的命名规则不一致：Illumos 没有命名空间、属性名原样存放；FreeBSD 分若干命名空间，系统命名空间的名字会加“system:”前缀，用户名空间的名字不加前缀、与 Illumos 一致，因此两边可以互相读取对方的属性；而 Linux 在用户名空间上也给名字加前缀，跨平台读取时会被错认。为此他开了 PR，以 xattr_compat／xattr_fallback 属性做回落读取，并把 Linux 侧写成不带前缀，已准备随 TrueNAS 的 beta 版本发布并希望尽快上游。（YouTube EP5Lby_Vl6H88，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1586 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1586`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2021 OpenZFS Leadership Meeting〕讲者口述：他介绍 Linux 移植的命名空间支持 PR 已基本可用，新增的 zfs user ns 命令可把数据集委派给 Linux 的用户命名空间，做法类似把数据集委派给 Solaris 的 zone 或 BSD 的 jail；进入该命名空间后只能看到被授权的数据集。他补充该 PR 的第一个提交需先回退一处为兼容 linux 4.9 而改动的 uid 查找逻辑，因为 ZFS 在磁盘上始终按根命名空间存 uid，否则在命名空间内 stat 会报 EOVERFLOW。（YouTube EP5Lby_Vl6H88，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1587 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1587`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2021 OpenZFS Leadership Meeting〕讲者口述：Alexander 反对 8k 这一默认 recordsize：他称在 4k 物理扇区已成常态、乃至 SSD 上也常见的情况下，8k 的块大小几乎不允许有效压缩，压缩实际变成“要么开、要么关”，而 16k 的块能压缩得明显更好。（YouTube EP5Lby_Vl6H88，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1669 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1669`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2020 OpenZFS Leadership Meeting〕讲者口述：克隆文件时只需把原块指针的数据复制进新文件并在块引用表中登记，条目只在块真正被克隆时才建立；因此不使用该特性时不付出任何代价，使用它时读写路径也不付出代价——与原去重表每次写入都落一条条目形成对照。（YouTube EPY9HQ4RbqIEw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1670 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1670`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2020 OpenZFS Leadership Meeting〕讲者口述：去重表（DDT）条目当前每个 392 字节，而块引用表条目只约 80 字节、理论上还能更小；另一项优点是条目可按设备偏移排序落盘，使克隆文件的条目聚集、释放时可顺序读取而非随机读。（YouTube EPY9HQ4RbqIEw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1671 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1671`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2020 OpenZFS Leadership Meeting〕讲者口述：修复后若已用大写 L 传输大块、随后又改为不发送大块，zfs receive 直接拒绝而非继续写入错误数据；反向切换则由接收端保留已收小块的粒度并自行切分。讲者同时说明保留该开关的理由是防止对存量系统加剧原有问题。（YouTube EPY9HQ4RbqIEw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1672 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1672`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2020 OpenZFS Leadership Meeting〕讲者口述：作者新增 zfs send 流格式标志，为把大写 L 变成默认乃至唯一行为铺路——切换到新默认后，含大块的流只允许较新的系统接收，从而在不破坏旧系统的兼容前提下完成默认行为的迁移。（YouTube EPY9HQ4RbqIEw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1712 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1712`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 4 月 OpenZFS 领导层会议〕讲者口述：会中谈到校验和加速所受的许可约束：Linux 内核中几乎全部加密例程都按 GPL 方式导出，因而不宜调用；由于 OpenZFS 项目不使用任何 GPL-only 导出，取用 Linux 内核的加密例程并非好选择——讲者认为这正是校验和（ICP）代码取自 illumos 的原因。（YouTube EP6zb6AxL26d8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1713 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1713`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 4 月 OpenZFS 领导层会议〕讲者口述：会中进一步指出：若能找到许可适当可用的实现，便可将其引入——若 FreeBSD 一侧的代码属 BSD 许可，就有可能把它们复制进 ZFS 源树，替换取自 illumos 的校验和实现。（YouTube EP6zb6AxL26d8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1714 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1714`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 4 月 OpenZFS 领导层会议〕讲者口述：有与会者自陈着手推进了“纠接收取”（corrective receive）补丁：多数测试已通过，唯独一项 FreeBSD 专属测试——针对 redacted send 的那项——会导致、而且只会导致 FreeBSD 内核 panic，并且并非每次都能复现。（YouTube EP6zb6AxL26d8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1715 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1715`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 4 月 OpenZFS 领导层会议〕讲者口述：会上提请各方关注编号 11919 的提案，讨论的是扩展属性（extended attributes）在 FreeBSD 与 Linux 之间移植的兼容性问题——历史上门户系统（illumos）一侧本就已存在两种互不兼容的实现。（YouTube EP6zb6AxL26d8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1719 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1719`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年1月29日 OpenZFS 领导组纵例会〕讲者口述：针对 dedupe-ditto 属性他提出的方案是保留属性本身但让它不再生效——发送该属性的脚本仍归零退出，但不再创建任何新的去重锁。引文之外他强调存量数据块仍能被识别处理并正确释放，会上该项提案无人反对。（YouTube EPE6lvNOxCxOw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1720 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1720`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年1月29日 OpenZFS 领导组纵例会〕讲者口述：zfs remap（随设备移除功能一并入的命令）已在 ZFS on Linux 上剔除，而它曾随 FreeBSD 12 的版本释出，因此会上明确把 FreeBSD 列入与 illumos 并列的待处置平台。（YouTube EPE6lvNOxCxOw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1721 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1721`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年1月29日 OpenZFS 领导组纵例会〕讲者口述：讨论新增可启用特性默认值时，参与者回顾 FreeBSD 一直存在“开启某项特性会导致系统无法启动”的情形，并提出一个改进方向——将这类兼容性提醒正式化，在用户误开使系统无法启动的特性时显式告知。（YouTube EPE6lvNOxCxOw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1722 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1722`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年10月 OpenZFS 领导层会议〕讲者口述：讲者称距他上次汇报近一年后重提该工作，进展是“块引用表（block reference table）已可用”、并借一个“zfs write override”技巧达成目的；当前数据结构仍与去重表类似，需要换成更优的结构。（YouTube EPVsBNknvrAas，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1723 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1723`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年10月 OpenZFS 领导层会议〕讲者口述：讲者说明块引用表像去重表一样是全局表；它“克隆的不是文件而是块”，内部可对任意块做克隆，把块指针复制到同一文件、不同文件，甚至不同数据集。（YouTube EPVsBNknvrAas，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1724 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1724`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年10月 OpenZFS 领导层会议〕讲者口述：讲者说明成本模型：不使用块引用表时没有任何代价；一旦开始使用，每次释放都要付出代价，因为块指针里没有特殊标志位，必须去查块引用表。（YouTube EPVsBNknvrAas，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1725 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1725`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年10月 OpenZFS 领导层会议〕讲者口述：讲者述说 ZFS 加密的一处格式不兼容事故：dnode 中的哈希（转写音作 project d node）最初未被包含，而 macOS 与 illumos 接手该代码时尚未发现，于是野外已有不含该哈希的加密数据集，讲者据此判断这使其无法交换。（YouTube EPVsBNknvrAas，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1742 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1742`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 OpenZFS 领导会议〕讲者口述：ZFS direct I/O 写入在提交前校验失败时会中止、不提交块指针并向上返回错误码；讲者指出该情形在 FreeBSD 上不成问题——stable pages 机制可用、可写保护用户缓冲区，而 Linux 上做不到，只能依靠校验兜底。（YouTube EPWiyrHu6R8ow，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1743 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1743`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 OpenZFS 领导会议〕讲者口述：direct I/O 在 FreeBSD 侧仍有一个遗留读路径缺陷——连续发起多个 direct I/O 读请求时，第一个请求在执行 fault hold 页时常失败，失败从 FreeBSD 的 bm_fault_quick_hold 一路向上返回，讲者称自己也不明其因。（YouTube EPWiyrHu6R8ow，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1744 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1744`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 OpenZFS 领导会议〕讲者口述：ZFS 的 zio_taskq_batch 可调配额是按池各建一组任务队列的，因此在两个池之间做 zfs send/receive 时，仅压缩与解压缩就会占到 150% 的 CPU 核心配额。（YouTube EPWiyrHu6R8ow，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1745 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1745`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 6 月 OpenZFS 领导会议〕讲者口述：下一次领导会议定在四周后的 7 月 19 日；因 Delphix 方面当月有公司活动、部分成员可能无法出席，遂改请 Brian Behlendorf 主持该次会议，本人当场应准。（YouTube EPWiyrHu6R8ow，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1750 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1750`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2025 OpenZFS Leadership Meeting〕讲者口述：本次为 2025 年 7 月 OpenZFS 领导团队（leadership team）例会，可见该社区分叉设有常设的领导团队议事机制。（YouTube EP0KHUB97oFGY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1751 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1751`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2025 OpenZFS Leadership Meeting〕讲者口述：OpenZFS 侧原计划在 8 月中旬前切出 3.0／2.4 分支；此事曾在 FreeBSD 开发者峰会提出，但 FreeBSD 的发布工程师并不认可 OpenZFS 在 11 月初出包，因为 FreeBSD 的 RC 排在 11 月、正式版在 12 月 2 日。（YouTube EP0KHUB97oFGY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1752 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1752`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2025 OpenZFS Leadership Meeting〕讲者口述：OpenZFS 正在筹办开发者峰会，赞助情况良好、报名进行中，整体按既定计划推进。（YouTube EP0KHUB97oFGY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1753 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1753`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2025 OpenZFS Leadership Meeting〕讲者口述：空间型 metaslab 的权重重算路径，据其估计自 2010 年前后起便不调用常规的 metaslab 权重函数，而是在 range tree 中内联了段型算法。（YouTube EP0KHUB97oFGY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1788 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1788`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hackathon Presentations and Awards - OpenZFS Developer Summit 2014〕讲者口述：讲者所属队伍（其自报队名为“ghettosen”）当日实现了 ZFS 压缩包数据发送（send of compressed data）：直接取磁盘上已压缩的数据过网传输，接收端解压缩后再做评级、随后可能重新压缩；讲者自述“it basically works”。（YouTube EPgPbVPwScMGk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1789 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1789`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hackathon Presentations and Awards - OpenZFS Developer Summit 2014〕讲者口述：讲者团队发现 ZFS 在 zil 关闭、zfs 回滚与 spa_sync 之间存在竞态，据其描述该竞态有两种失效模式：一为 panic（在系统回滚衔接时触发），二为 hang（陷入任务队列析构的死循环）。（YouTube EPgPbVPwScMGk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1790 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1790`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hackathon Presentations and Awards - OpenZFS Developer Summit 2014〕讲者口述：该团队判定此处确为竞态后写出诊断脚本（转写音作 e-script／djs／descript，据语境应为 dtrace 脚本），并以此作为排查手段：当无法继续推进时至少先写出脚本记录假设，以便对故障情形做二分收敛。（YouTube EPgPbVPwScMGk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1791 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1791`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hackathon Presentations and Awards - OpenZFS Developer Summit 2014〕讲者口述：讲者当日把 zfs 中 snapshot ioctl 对应的 C 代码整段删除，改以约 30 行脚本实现，并自述尚未覆盖全部边界情形——例如因存储池系统版本不支持快照而无法取快照的情形。（YouTube EPgPbVPwScMGk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1831 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1831`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2020 OpenZFS 领导层会议〕讲者口述：该 pull request 为 zpool replace 新增一个命令行选项，用于请求串行重建(sequential rebuild)，且仅适用于镜像。（YouTube EPSyNn26YbRZY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1832 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1832`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2020 OpenZFS 领导层会议〕讲者口述：称 AIO 较常规 POSIX I/O 更具 性能优势，而 FreeBSD 的 AIO 当时是以特殊线程池实现的。（YouTube EPSyNn26YbRZY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1833 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1833`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2020 OpenZFS 领导层会议〕讲者口述：新增 zpool export -F，丢弃脏数据并完成清理，使系统与其他池可继续运行、挂起的池可日后导入。（YouTube EPSyNn26YbRZY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1834 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1834`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2020 OpenZFS 领导层会议 文档系统议题〕讲者口述：认为构建手册页须引入额外文档工具链将非常遗憾，因 FreeBSD 已将 man doc 纳入 base。（YouTube EPSyNn26YbRZY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1839 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1839`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年3月 OpenZFS Leadership Meeting 讲者口述〕讲者口述：提案（由 Josh 前一天发到邮件列表）主旨是，创建 pool 或升级 pool 时可以可选指定只启用 portable（可移植）的特性。（YouTube EPtVhf4ZxfB1Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1840 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1840`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年3月 OpenZFS Leadership Meeting 讲者口述〕讲者口述：portable 的定义是该特性在当前版本的所有 tier-one 平台可用，tier-one 平台口径为 FreeBSD 的编号发布版本、ZFS on Linux 的编号发布版本，以及 illumos gate 中已存在一年的代码；除滚动口径外另有按年固定的 portable 年份集，且选定的可移植性口径会记录在盘上。（YouTube EPtVhf4ZxfB1Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1841 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1841`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年3月 OpenZFS Leadership Meeting 讲者口述〕讲者口述：对 tier-one 平台中 Ubuntu LTS 的口径，讲者主张只纳入当前 LTS、不纳入所有仍在支持的 LTS，理由是拖得太远；这与更早讨论的取舍一致——选择可移植性往往意味着一段时间内不能启用新特性。（YouTube EPtVhf4ZxfB1Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1842 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1842`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2019年3月 OpenZFS Leadership Meeting 讲者口述〕讲者口述：做 ZFS 复制工具的讲者（Christian）发现 dataset 的 guid 属性已有 PR 改为公开并得到较广泛支持，用它做跨机器文件系统的差异判定，因为快照的 guid 在复制过程中保持不变；而文件系统自身在接收端会拿到不同 guid，因此设想把 guid 作为属性经 send/receive 通道带到接收侧并存储，以便源端重命名文件系统后仍能定位目标。（YouTube EPtVhf4ZxfB1Y，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1864 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1864`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2023 OpenZFS Leadership Meeting 会议〕讲者口述：会议中一位成员表示将承接赞助方的合同工作，把已经停滞了一段时间的 raidz 扩展（raidz expansion）工作做完；他说明这项工作最初主要由 FreeBSD 基金会出资赞助，2016 年前后启动，iX Systems（真纳斯／TrueNAS 的运营公司，Alexander Motesh 所在公司）早期也有少量参与或贡献人力，本次合同由 iX Systems 出钱、他计划本周提交 Pull Request，并表示愿意把早已过期的自己那份旧 PR 关闭掉。（YouTube EP2p32m-7FNpM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1865 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1865`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2023 OpenZFS Leadership Meeting 会议〕讲者口述：OpenZFS 会议上一位正在讲解去重（dedup）重构设计的成员指出，当前去重最大的问题是“写之前必须读”——每次写入若去重表（DDT，dedup table）未缓存在内存里，就必须先经过间接块再到叶块做一次随机读，才能判断这个哈希是否已经存在；另外去重表叶块被刻意存成 4K 小记录、间接块也限制在 4K（而非默认的 128K），原因是写入放大问题；再加上去重表按哈希排序，同一事务里新写入的 100 个块会散落到整张去重表的各处随机写，I/O 反而可能更多地花在更新去重表上而不是写数据本身。（YouTube EP2p32m-7FNpM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1866 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1866`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔June 2023 OpenZFS Leadership Meeting 会议〕讲者口述：会议中介绍正在推进的另一种去重实现思路，灵感取自 Matt（Matt Ahrens）早年的日志式去重（log dedup）构想，但目的是摆脱原方案的限制——原方案在压缩去重表时要把整张表作为一个事务组重写，导致整个系统原地等待该事务写完（若去重表有 100GB，等待时间可观），并且去重表必须一直常驻内存、无法淘汰；新方案采用分片＋日志的方式，让内存占用主要落在可淘汰的 ARC 中，使去重表可以整体换出到磁盘再按需换入，从而对去重表规模不设上限（例如把 2TB 的高速 NVMe 专门用于存放去重表）。（YouTube EP2p32m-7FNpM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1877 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1877`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 1 月 OpenZFS 领导层例会〕讲者口述：该项议程保留在名单上主要是一种提醒——不应忘记 OpenZFS 尚有一批加密相关缺陷悬而未决，且眼下无人有商业动机去处理它们；该主持人另收到来自某复制工具维护者的同类报告。（YouTube EPtyCk376bC9A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1878 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1878`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 1 月 OpenZFS 领导层例会〕讲者口述：OpenZFS 加密缺陷之一为编号 11679，基本情形是 debuf write 与 debuf read 被先后调用，debuf write 完成并在结束处临时释放缓冲。（YouTube EPtyCk376bC9A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1879 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1879`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 1 月 OpenZFS 领导层例会〕讲者口述：更换压缩算法后，若在 ARC 内的副本未压缩而块指针启用了压缩，则写入 L2ARC 前必须重压缩，读回时与块指针中的校验和匹配，从而误报 L2ARC 返回了损坏数据；后果仅限误报，不会使系统崩溃。（YouTube EPtyCk376bC9A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1880 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1880`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 1 月 OpenZFS 领导层例会〕讲者口述：Rich 发现 illumos 与 FreeBSD 自带的 gzip 实现输出与 Linux 内核中的 gzip 略有差异；而 LUKS 当年已先行只更新其解压器而不更新压缩器，构成同类变更的先例。（YouTube EPtyCk376bC9A，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1929 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1929`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2025 OpenZFS 领导会议〕讲者口述：会议介绍 anyRAID（转写音作 any raid／any vdeev）提案动因——既有 ZFS 镜像与 RAID-Z 要求各成员盘容量基本一致，容量有差异时只能取最小盘，限制了不同容量设备混装的可用性。（YouTube EPMifloJFCpLU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1930 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1930`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2025 OpenZFS 领导会议〕讲者口述：anyRAID 实现为单个顶层 vdev 挂载多个子设备，内部把写请求分发到不同区域，复用既有镜像逻辑处理写入，并继承全部修复等其余行为；‘rights’为 write 的 ASR 误写。（YouTube EPMifloJFCpLU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1931 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1931`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2025 OpenZFS 领导会议〕讲者口述：anyRAID 的区域映射表尚无存放位置，由此引出 DevSummit 上关于 ZFS 标签（label）可扩展性重构的讨论——预留更多空间，并按 Mav 提出的目录表思路依池类型动态分配空间。（YouTube EPMifloJFCpLU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1932 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1932`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔May 2025 OpenZFS 领导会议〕讲者口述：标签重构须考虑两年前 DevSummit 上 Brooks Davis 提出的旧问题——标签内 MV list 的用法破坏了 CHERI 硬件，因为存的是指针类数据，换到 64 位 CPU 以外的架构就会不同（‘cherry’为 CHERI 的 ASR 误写）。（YouTube EPMifloJFCpLU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1945 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1945`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2022 OpenZFS Leadership Meeting 会议〕讲者口述：主讲人 Rich 为其压缩早停启发式补丁所述，lz4 作为第一遍试探后若返回“不可压缩”而不给出压缩结果，便不再尝试更高压缩级别的 zstd，该做法对加速不可压缩数据“效果非常好”。（YouTube EP8ugj9V6hTR4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1946 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1946`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2022 OpenZFS Leadership Meeting 会议〕讲者口述：若只用 lz4 做首遍判定、放弃更高压缩级别，在高度可压缩的数据集上最多损失约 8% 的压缩率，主讲人当场判断“这不是一个可接受的数字”。（YouTube EP8ugj9V6hTR4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1947 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1947`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2022 OpenZFS Leadership Meeting 会议〕讲者口述：会上展示的图表显示，该启发式把在 Raspberry Pi 上以 zstd 15 压缩一个约 40 余 GB 的数据集所需时间从两小时降到约 15 分钟。（YouTube EP8ugj9V6hTR4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1948 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1948`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Second March 2022 OpenZFS Leadership Meeting 会议〕讲者口述：主讲人称曾考虑在 OpenZFS 中自带 zlib 而非调用系统自带版本，动机之一是避免 FreeBSD 与 Illumos 同 Linux 之间产生不同的压缩结果。（YouTube EP8ugj9V6hTR4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2012 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2012`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brian Behlendorf 演讲“Lustre ZFS & Supercomputers”〕讲者口述：ZFS 源码于 2005 年发布；Livermore 大约自 2008–2009 年前后开始评估把 ZFS 用作 Lustre 的后端，当时 ZFS 已在真实生产系统上得到验证。（YouTube EPRoyrIocAByU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2013 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2013`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brian Behlendorf 演讲“Lustre ZFS & Supercomputers”〕讲者口述：该站点的负载大量是写检查点，写入来自众多随机进程；ZFS 的写时复制把这些写入序列化为顺序写，讲者称性能因此表现良好。（YouTube EPRoyrIocAByU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2014 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2014`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brian Behlendorf 演讲“Lustre ZFS & Supercomputers”〕讲者口述：Lustre 并非叠在 ZFS 的 POSIX 层或卷管理器之上，而是直接对接 ZFS 的 DMU 层并作为其第一类消费者（first class consumer）；把 ZFS 移植到 Linux 的工作由 Livermore 完成。（YouTube EPRoyrIocAByU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2046 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2046`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年3月 OpenZFS 领导组会议〕ZFS 开发者口述：vdev 属性方案他本人首次提出是在 2018 年，在 2018 年 hackathon 上集中投入了相当一段时间，随后于 2019 年正式呈现基于那次成果的设想。（YouTube EPz5JoRoBbUmA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2047 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2047`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年3月 OpenZFS 领导组会议〕ZFS 开发者口述：Richard 在该方案的幻灯片批注中提出改进用法——面向多站点（转写音作 metro）部署中“有镜像但部分磁盘为远端”的场景，可表达“读优先偏向本地镜像”。（YouTube EPz5JoRoBbUmA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2048 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2048`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年3月 OpenZFS 领导组会议〕ZFS 开发者口述：他给 vdev 增加用户属性的动机之一是记不住已更换盘片的序列号——池内其余盘片的序列号都查得到，唯独被换掉的那块查不到；把序列号存入 vdev 属性后，机房值班人员拔盘时即可核对是否拔对了盘。（YouTube EPz5JoRoBbUmA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2049 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2049`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021年3月 OpenZFS 领导组会议〕ZFS 开发者口述：池用户属性刻意与 ZFS 数据集属性区分——把用户属性设在根数据集上会被池内每个数据集继承，而池属性只出现在 zpool 层面，故两者是相互独立的概念。（YouTube EPz5JoRoBbUmA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2055 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2055`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZettaLane Systems ZFS 技术演讲（ZettaLane 创办人 Supramani Samandanda）〕讲者口述：其 ZFS on Linux 移植最初始于 OpenZFS 的 Nevada 分支，此后改跟随 illumos 的源代码；因保留相同的树结构，从 illumos gate 引入补丁比当时从 ZFS on Linux 引入补丁更容易。（YouTube EP8htVeyHkQSM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2056 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2056`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZettaLane Systems ZFS 技术演讲（ZettaLane 创办人 Supramani Samandanda）〕讲者口述：在其 ZFS 移植中仍保留 Solaris 的 VFS 与 vop 接口层，因为 xattr 与快照挂载需要它们；正因这些层原封不动，才能直接把 illumos 的补丁套用过来。（YouTube EP8htVeyHkQSM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2057 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2057`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZettaLane Systems ZFS 技术演讲（ZettaLane 创办人 Supramani Samandanda）〕讲者口述：Solaris 里有 comstar，可与 zvol 直接自然集成；Linux 上没有对应机制，且已有 SCST、LIO target 等竞争者，因此无法在 Linux 上做出与 Solaris comstar 等价的存储虚拟化集成。（YouTube EP8htVeyHkQSM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2066 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2066`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 5 月 OpenZFS 领导层会议〕讲者口述：OpenZFS 上游的 pull request 与 issue 维护工作过去近十年几乎全部由 Brian Behlendorf 一人承担；随着项目贡献量增长，这已成为单人难以承受的工作负担。（YouTube EPGKusXS8T_KY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2067 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2067`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 5 月 OpenZFS 领导层会议〕讲者口述：会议宣布增补三位长期从事 ZFS 工作的新维护者 Tony Nguyen、Mark 与 John Kennedy，职责是护送 pull request 走完评审流程。（YouTube EPGKusXS8T_KY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2068 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2068`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 5 月 OpenZFS 领导层会议〕讲者口述：OpenBSD 侧讲者称其最初打算在内核中使用 ZFS，但内核态文件系统一旦发生 panic 就会拖垮整个系统并需要重启，这是该方案的顾虑。（YouTube EPGKusXS8T_KY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2069 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2069`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2021 年 5 月 OpenZFS 领导层会议〕讲者口述：有人报告 ZFS 的 zstd 压缩头在大端机（转写音作 spark 与 power pc，即 SPARC 与 PowerPC）上的存储方式存在问题，会上称已有 PR 但尚未有人评审。（YouTube EPGKusXS8T_KY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2107 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2107`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 9 月 OpenZFS 领导会议〕讲者口述：OpenZFS 2.2 至今已切出四个 RC，最后一个 RC 是上周切出的，希望这就是接近最终的版本，目前状况相当不错，可能还会再并入一些补丁。（YouTube EP0b6uAdtMgnc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2108 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2108`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 9 月 OpenZFS 领导会议〕讲者口述：他注意到 FreeBSD 的构建机器（freebsd-build）又出问题了，失败发生在配置阶段，与自己的改动无关；他还说明自己这次缩短了测试套件的运行时间，因为之前的测试套件在旧版本上会超时。（YouTube EP0b6uAdtMgnc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2109 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2109`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 9 月 OpenZFS 领导会议〕讲者口述：有人在 FreeBSD 上对 2.2 做了大规模软件包构建并反馈多个问题，其中块克隆也是一个被击中的痛点，补丁已提交、目前运转良好；此后仅又收到一条关于卸载文件系统的抱怨，难以判断是 2.2 的问题还是操作系统本身的问题。（YouTube EP0b6uAdtMgnc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2110 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2110`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2023 年 9 月 OpenZFS 领导会议〕讲者口述：他认为会上介绍的并行同步（在 spa_sync 下对多个数据集并行同步、互不串行等待）与自己几年前做的工作相近——后者是在单个数据集内部让数据节点成对并行同步，前者相当于把这件事扩展到跨多个数据集，并表示自己可能抽空看一下。（YouTube EP0b6uAdtMgnc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2312 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2312`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 11 月 OpenZFS 领导层例会〕讲者口述：为让 ZFS 在 FreeBSD 上正确支持 direct I/O，Mark Johnson 提交了一份在 zgetpages 全程持有 range lock的补丁，主持人称“right now we have directio blocked for FreeBSD”，希望该补丁完成最后一轮评审、赶得上 OpenZFS 2.3，届时两种操作系统上 direct I/O 均可用。（YouTube EPMmuEKvXwLfw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2313 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2313`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 11 月 OpenZFS 领导层例会〕讲者口述：ZFS on multiple pools 的补丁已从draft 转为 open 并自指派 Brian 评审，其做法是把 ZFS 原本存于“per process state”的单个 blob 扩展为按池数量生成的多个 blob（“instead of one blob it's end blobs because we have end pools”）。讲者提醒 ztest 代码阅读门槛高，靠附注补足评审所需信息。（YouTube EPMmuEKvXwLfw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2314 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2314`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 11 月 OpenZFS 领导层例会〕讲者口述：OpenZFS 社区当时约有 130 个开放 PR，维护者希望收敛到“一屏”而不是“六屏”，正在补打标签、关闭陈旧 PR；另有人提出给值得重做的旧想法打 revisit 之类标签，免得在八千多个已关闭 PR 里翻找（“you're not looking through all 8,000 closed ones”）。（YouTube EPMmuEKvXwLfw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2319 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2319`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZFS 开发者峰会演讲 Tom Caputi〕讲者口述：判断 ZFS 进程卡死时能否用 Ctrl-C 取消，是最重要的初步调试信息；若进程停在用户态（S 状态而非 D 状态）即可取消，而习惯 Unix 系统的人第一反应就是先按 Ctrl-C。（YouTube EPJoD_Kmqnkgg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2320 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2320`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZFS 开发者峰会演讲 Tom Caputi〕讲者口述：“core dumped”的信息并不可信，须先执行 ulimit -c unlimited；他明确称这是 Linux 的习惯做法，并不确定 FreeBSD 或其他平台上如何运作。（YouTube EPJoD_Kmqnkgg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2321 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2321`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZFS 开发者峰会演讲 Tom Caputi〕讲者口述：他自己与会中多数人日常写的代码面向 Linux 内核或 BSD 内核等在内核侧，一旦问题落在内核空间（进程卡在 D 状态、Ctrl-C 无法终止），几乎没有可用手段，只能去看 dmesg。（YouTube EPJoD_Kmqnkgg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2322 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2322`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ZFS 开发者峰会演讲 Tom Caputi〕讲者口述：ZFS 的调试消息通道在 Linux 上经由 /proc/spl 下的 zfs debug message 提供，是一份循环回收的虚拟文件，因此并非全量记录。（YouTube EPJoD_Kmqnkgg，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2334 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2334`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2025年1月OpenZFS领导层会议〕参与讨论者：会议通报 2.3 已出 rc5，其中包含 Don Brady 的若干收尾改动。（YouTube EP4CG76qFS3XA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2335 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2335`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2025年1月OpenZFS领导层会议〕参与讨论者：承接上文 Brian 已切出 rc5 一事，会上表示他承诺下周一发正式版，且认为没有其他已知问题，2.3 正式发布在望。（YouTube EP4CG76qFS3XA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2336 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2336`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2025年1月OpenZFS领导层会议〕参与讨论者：ZFS 测试套件近期做了若干修复使其可在 FreeBSD 15 上通过，但目前 CI 构建器存在问题，3b d 的 vdev 实现有回归，FreeBSD 15 上游已修，仍需更新 CI 才能干净通过。（YouTube EP4CG76qFS3XA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2337 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2337`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2025年1月OpenZFS领导层会议〕参与讨论者：ARC 淘汰调试与 dbuf 淘汰相关改动已推进相当一段时间，正逐步接近可合入状态。（YouTube EP4CG76qFS3XA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2338 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2338`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2019 OpenZFS Leadership Meeting 会议口述〕讲者口述：会议宣布 OpenZFS 开发者峰会定于当年 11 月 4 日、5 日举行，注册已经开放，演讲与报告征集（call for papers）同步开放，欢迎提交自己在 ZFS 上做的工作。（YouTube EPltIIDDq9qag，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2339 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2339`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2019 OpenZFS Leadership Meeting 会议口述〕讲者口述：讨论 Linux 5.0 内核中的 SISD 支持时，有与会者提到这段针对 Intel 平台的向量化汇编代码源自以 BSD 许可证交给 Intel 的代码，因此尽管它已在 Linux 内核之中，同一份代码也可以 BSD 许可证直接从 Intel 下载，在内核中也可能以 GPL/BSD 双重许可存在。（YouTube EPltIIDDq9qag，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2340 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2340`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2019 OpenZFS Leadership Meeting 会议口述〕讲者口述：有人问 FreeBSD 侧是否基本不应期待新特性被逐个移植、直到切换到 OpenZFS 为止；回答是现在难以确定，要看该切换的时间线，可能只有少量改动会被拉入，以维持旧版本可用，直至相关特性进入主线。（YouTube EPltIIDDq9qag，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2341 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2341`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔July 2019 OpenZFS Leadership Meeting 会议口述〕讲者口述：有开发者报告一个标准化相关工作数周前新近开了 PR，其性质是把 FreeBSD 的最新版本实现移植到 ZFS on Linux 一侧；目前它能通过 Linux 侧全部编译测试，却无法在所有测试构建中通过编译，尚需他人协助排查。（YouTube EPltIIDDq9qag，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2361 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2361`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenZFS 2020年7月领导层月会〕讲者口述：ZFS send 的一贯做法是新增特性由新的 feature flag 守护，使开始跑 0.8 的机器发出的流仍能被习惯于接收 0.7 快照的旧机器收下。（YouTube EPrKK1pfNt66g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2362 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2362`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenZFS 2020年7月领导层月会〕讲者口述：与会者指出 zpool 特性旗标若仅在数据集上设置 Zstd 压缩属性而未实际写入数据块，不会从 enabled 转 active，0.8／0.7 旧版仍可导入该池，列数据集时可能触发 panic。（YouTube EPrKK1pfNt66g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2363 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2363`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenZFS 2020年7月领导层月会〕讲者口述：OpenZFS 2.0 发布计划不同于以往——计划 8 月中旬自 master 顶端切出 2.0 分支转入稳定，master 分支继续保持开放以接纳后续新特性。（YouTube EPrKK1pfNt66g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2364 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2364`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔OpenZFS 2020年7月领导层月会〕讲者口述：2.0 发布前最要紧的是 FreeBSD 回归——凡 ZFS on FreeBSD 原先可用而改用 OpenZFS 后失效或集成不良之处，均须在发布前处理。（YouTube EPrKK1pfNt66g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2409 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2409`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 4 月 OpenZFS 领导层会议〕讲者口述：议程讨论下一次 OpenZFS 大会的筹办，按惯例应落在十月或十一月、距会议约六个月；就“是否办成线下会”，主持者请与会者以打勾（要）／打叉（不要）表态，见到多数打勾后决定启动线下活动的筹划，同时商定场地与日期、并考虑防疫措施的取舍。（YouTube EPfTIJgGpV3HE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2410 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2410`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 4 月 OpenZFS 领导层会议〕讲者口述：就“OpenZFS 原生加密能否放心用于单机系统”这一提问，会议归纳手上证据称：加密数据集的发送／接收（send and receive）环节问题成堆，而在不走发送接收的场景里至少已有人长期使用且未见严重故障；即当时对“生产可用”并无干脆的结论。另有发言者自述自 Solaris crypto 时代起长期使用加密文件系统，但只做本地加密、不做发送接收。（YouTube EPfTIJgGpV3HE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2411 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2411`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 4 月 OpenZFS 领导层会议〕讲者口述：TrueNAS 一侧的与会者自述，其用户正从此前使用的 FreeBSD GELI 磁盘加密迁移到 ZFS 原生加密，即将发布的 TrueNAS 版本只支持原生加密，因此使用原生加密的人数预计会继续增长；被问及有无工单时答称“有几个，但没什么大问题”。（YouTube EPfTIJgGpV3HE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2412 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2412`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 4 月 OpenZFS 领导层会议〕讲者口述：为支持廉价的整文件拷贝与文件区间拷贝（对应 Linux 的 copy_file_range 与 reflink 一类接口），由于 FreeBSD 内核尚无这类通用接口，他把接口随 ZFS 一起以内核模块方式加载，并新增两个系统调用；他判断终局方案应是在 FreeBSD 内核里做出对所有文件系统开放的通用接口，且表示愿做 FreeBSD 一侧而 Linux 一侧尚需他人认领。（YouTube EPfTIJgGpV3HE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2424 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2424`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 5 月 OpenZFS 领导层会议〕讲者（会中称 Alexander）口述：他把 TrueNAS（转写音作 tras scale）升级到 Linux 6.6 LTS、配 ZFS 2.2.3／2.2.4 并把 ARC 上限调到接近最大值之后出现的换页与用户态进程变慢，归因于内核中新引入、体量逐步增大的 multigen LRU 代码：他在 6.1 内核里只找到它的若干片段，而在 6.6 中它“变大并被默认启用”。同一发言称，该逻辑一次性算出内存压力、先丢弃大量 page cache 并激活 swap，之后才经 shrinker 通知 ZFS 释放 ARC，因此他们靠关闭该代码的内核开关并禁用 swap、调低 swappiness 规避。（YouTube EP8QtWEdRtBDY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2425 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2425`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 5 月 OpenZFS 领导层会议〕讲者口述：他自述注意到 FreeBSD 与 Linux 两点差异——在 FreeBSD 上 ZFS（转写音作 3bd DFS）总以 4 KB 粒度申请单个页，内核内存碎片化时会“收集最差的页”，把连续页留给别的使用者；而 Linux 上的 ZFS 显得贪婪，总想拿到最大 2 的幂尺寸的分配。他自称对此实验尚不充分，并问是否有人试过压低 ZFS 分配粒度以减轻整机碎片压力。（YouTube EP8QtWEdRtBDY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2426 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2426`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 5 月 OpenZFS 领导层会议〕与会者口述：其团队已有多线程 ARC 驱逐的补丁，且 Don 提交的“多池并行导出”应已合入；此外他们把一份源自 illumos（转写音作 Al lumos）的旧补丁“重新启用并完成”，使 ARC 的释放可以在池导出之后放到后台进行，从而在 HA 故障转移等场景不必等待。（YouTube EP8QtWEdRtBDY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2427 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2427`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2024 年 5 月 OpenZFS 领导层会议〕与会厂商代表口述：DDT 配额与 DDT 预载等一批 PR 自 2 月起挂起待评审，该厂商（转写作 ATX，所指存疑）要求按此前提议在第二季度末切出 2.3 分支以对齐自身发布周期，已在跑 ZFS master 的每夜构建（转写作 nightless）作准备；会议主持则称与 Brian 商议后认为 2.3 应能在 Q2 末完成分支，并提到上一年 2.2 的分支被过度延误。（YouTube EP8QtWEdRtBDY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2526 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2526`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔October 2024 OpenZFS Leadership Meeting〕讲者口述：某套模拟器（转写作“Q emu”）被部署到 openzfs 的构建机器人之后，现在有一批 FreeBSD 测试通常能够运行，并且捕获了此前从未见过的若干缺陷。（YouTube EPmN-UPaWmERs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2527 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2527`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔October 2024 OpenZFS Leadership Meeting〕讲者口述：OpenZFS 2.3 的首个候选发布版（转写作“230 rc1”）在该周切出，反响颇好，尤其受到那些“weird corners of the internet”中紧盯最新文件系统的用户关注；同段并提到关于重复数据删除旧行为仍存在大量误传，需反复向人澄清。（YouTube EPmN-UPaWmERs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2528 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2528`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔October 2024 OpenZFS Leadership Meeting〕与会者问答口述：被问及某项特性做了多少年，答者称“at least five years”，并回忆自己曾在 Google／GitHub 的一次峰会上就此讲过，如今又赶在另一场峰会之前落地。（YouTube EPmN-UPaWmERs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2529 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2529`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔October 2024 OpenZFS Leadership Meeting〕讲者口述：在讨论存储池冗余耗尽后的处置时，其明确表示 OpenZFS 当时并没有可让池降级为只读的模式，“it's only full suspension”，另有讲者自称做过让池转为只读的雏形实现但尚未落地。（YouTube EPmN-UPaWmERs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2530 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2530`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2026 年 1 月 OpenZFS 领导组会议〕讲者口述：大标签（large label）PR 在评审中修正了建池阶段的标签写入路径：写标签时走的是 null task queue，而该队列只有单一工作线程，因此无论多少块盘都是逐台串行写入；讲者称其测试中建池耗时“something like 50 seconds”，改为在池初始化／vdev 创建期间不派发到 null task queue 后建池时间显著缩短。（YouTube EPievah8K2LqI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2531 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2531`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2026 年 1 月 OpenZFS 领导组会议〕讲者口述：会议记录到一件来自 Seagate 的新 PR，为 RAID-Z 增加“failure domains”能力，让使用者声明硬件布局，使 RAID-Z 建立的分组跨设机箱分布，从而失去整机箱时不会使存储池故障；与会者称此前只能建多个独立 RAID-Z vdev，因而失去 RAID-Z 相对分立 raid Z vdev 的大多数优势。（YouTube EPievah8K2LqI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2532 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2532`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2026 年 1 月 OpenZFS 领导组会议〕讲者口述：有关 L2ARC 改进的 PR 已进入待合并状态：目标是提高 L2ARC 设备写入速度并使其长期稳定，同时不永久提速以免磨损 SSD，因此引入按“每天整盘写入次数”计的上限，默认设为每设备每日一轮。（YouTube EPievah8K2LqI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2533 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2533`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2026 年 1 月 OpenZFS 领导组会议〕讲者口述：关于 Python 版 libzfs 绑定的维护归属，与会者口述其团队仅维护 Linux 侧绑定、不维护 FreeBSD 侧，并说 FreeBSD 上“the free BSD one the core”那套已“out of date”；由此引出是否愿意为 FreeBSD 协助维护的讨论，另一人回应称跨平台维护无法承诺。（YouTube EPievah8K2LqI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2545 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2545`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 OpenZFS 开发者峰会黑客松〕讲者口述：讲者称当日晨间与 Paul、Richard 讨论 ZFS 与 cherry（转写音，实指 CHERI）议题后汇报：XDR 磁盘格式隐式编码了内存结构中随指针宽度而变的细节，此前一律以 64 位指针处理尚可工作，但在 cherry 上行不通；议定方案是格式保持不变，由 cherry 侧代码自行推算其在 64 位系统上本应占的尺寸，讲者称方案看似直接、但需要测试套件兜底。（YouTube EPS-0b0V07G2Q，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2546 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2546`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 OpenZFS 开发者峰会黑客松〕讲者口述：主持人收尾时称很高兴时隔已久重新线下相聚，希望明年再办，并称本届为第 10 届年度峰会（转写音作 we did a decade this is the 10th Annual）。（YouTube EPS-0b0V07G2Q，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2547 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2547`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 OpenZFS 开发者峰会黑客松〕讲者口述：讲者称与 Madden 讨论并检索网络后复现了问题，并复活了来自 illumos 的若干补丁请求（转写音作 multiple requests），使 Zap 条目被删除时逐步收缩 Zap（转写音作 this app），并以火焰图展示修补后明显提速。（YouTube EPS-0b0V07G2Q，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2714 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2714`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔November 2018 OpenZFS Leadership Meeting〕与会者口述：跨平台特性同步的策略，仍是选定一条大版本线后整体拉平，以此覆盖特性矩阵中未逐一认领的其余条目。（YouTube EPoV58X-z8xVU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2715 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2715`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔November 2018 OpenZFS Leadership Meeting〕与会者口述：只挑想要的特性而不跟进其依赖（含加密等连带），本质是标准的技术债问题——而多家公司各自投入，难以协调。（YouTube EPoV58X-z8xVU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2718 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2718`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔November 2020 OpenZFS Leadership Meeting〕与会者口述：OpenZFS 2.0 已切出五个 RC 候选，社区测试揪出几个小问题、无大碍，正准备打最终版 tag，希望当月早些时候发布。（YouTube EPS-SAfg1Awos，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2719 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2719`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔November 2020 OpenZFS Leadership Meeting〕与会者口述：2.0 发布冻结纪律——只从 master 最后 cherry-pick 低风险项（一些 FreeBSD 相关内容、文档清理之类），更大改动不再进。（YouTube EPS-SAfg1Awos，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
