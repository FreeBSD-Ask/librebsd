---
chapter: 第 110 章
id: CH110
volume: 第06卷-freebsd的核心技术革新
---

# 第 110 章 cddl许可证与freebsd集成

## 要点

- CDDL 与 GPL 不兼容争议从 2005 年 CDDL 发布持续至今（2025 年），核心事件时间线为：2004 年 12 月 CDDL 提交 OSI；2005 年 1 月 OSI 批准 CDDL；2005 年 6 月 OpenSolaris 发布；2005 年 11 月 ZFS 源码发布；2006 年 FSF 在许可证列表中标注 CDDL 为 GPL 不兼容；2007-2008 年 Pawel Dawidek 完成 ZFS 向 FreeBSD 的移植（2007-04-06 导入 freebsd-src 主干，2008-02 随 FreeBSD 7.0 发布，详见辨析与文献段著录）
- OpenSolaris 时期（2005-2010 年）的 ZFS 一手史料面临严重的访问性问题：OpenSolaris 源码仓库（hg.opensolaris.org）于 2010 年 Oracle 收购后逐渐下线；Sun 官方文档站点（docs.sun.com）在 Oracle 收购后多次迁移，大量 ZFS 文档链接失效；OpenSolaris 邮件列表（opensolaris.org/os/community 等社区版面）档案亦随站点关闭而大量散佚，仅可经互联网档案馆等第三方存档部分回溯
- Dawidek 的 ZFS 移植工作主要在 <freebsd-current@freebsd.org> 和 <freebsd-arch@freebsd.org> 邮件列表上公开讨论，关键邮件包括：2006 年末 Dawidek 宣布启动 ZFS 移植的邮件；2007 年 4 月 ZFS 代码导入 Perforce 仓库的通知；2007-04-06 ZFS 主干导入 freebsd-src 的提交通知（commit `f0a75d274af375d15b97b830966b99a02b7db911`，“Please welcome ZFS - The last word in file systems”，2007-04-06T01:09:06Z，详见辨析与文献段完整著录）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_543] 卷“第06卷-freebsd的核心技术革新”第 110 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:bsdnow_podcast:outline_mappings:om_11222] BSD Now 第 562 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11357] BSD Now 第 546 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11944] BSD Now 第 474 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12219] BSD Now 第 445 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12237] BSD Now 第 444 期，匹配 CH110 章，关联度 1.0

## 史观

- 总纲第 13 条——法律与道德是利益分配（存疑）：CDDL 与 GPL 的互斥不是简单的“Sun 恶意”或“GPL 极端”，而是文件级 copyleft 与作品级 copyleft 两种设计哲学的根本冲突；FSF 的 GPL 不兼容分类虽非法院判决，却在社区中具有类似“准法律”的效力（详见 110.4 子节史观字段）〔订正注：原挂“总纲第 24 条——许可证”系伪标签，权威第 24 条为“美是消解性的体验”，25 条名目中无“许可证”；按论旨改挂第 13 条〕
- 总纲第 4 条——分离聚合是永恒规律（存疑）：OpenSolaris 开源是 Sun 向开源转型的关键节点，但转型未拯救 Sun——2010 年 Sun 被 Oracle 收购、OpenSolaris 被关闭；ZFS 是 OpenSolaris 遗产中生命力最持久的组件，后续发展（illumos/OpenZFS/FreeBSD ZFS）完全脱离了 Sun/Oracle 的控制，“创造者不必然是继承者”（详见 110.5/110.6 子节史观字段）〔订正注：原挂“总纲第 25 条——终结与延续”系伪标签，权威第 25 条为“逻辑是形式主义而非世界本身的结构”；按论旨改挂第 4 条〕
- 总纲第 9 条——经验优先（存疑）：Dawidek 以在 BSD 内核中模拟 Solaris API 的兼容层策略移植 ZFS 而非改写 ZFS 适配 BSD，使 FreeBSD 在其后 15 年持续从上游合并新功能而无需承担代码分叉维护成本，体现 BSD 内核工程文化的“最小侵入”原则（详见 110.6 子节史观字段）〔订正注：原挂“总纲第 6 条——技术路线分化”系伪标签，权威第 6 条为“和解优于斗争”；按论旨改挂第 9 条〕
- 总纲第 3 条——不存在进步，只有权力再分配（存疑）：长达 20 年的 CDDL-GPL 争议未产生任何法院判例，社区经由技术架构（DKMS、独立代码库、分离分发）而非诉讼化解冲突；OpenSolaris 史料随单一商业实体战略转变而系统性散佚，其历史能被重建全靠社区分叉（illumos）、第三方存档与 BSD 世界的独立导入（详见 110.4/110.5 子节史观字段）〔订正注：原挂“总纲第 3 条——形式主义膨胀”，名目“形式主义膨胀”不在权威 25 条之表，改标第 3 条权威全称〕

## 辨析

- 需纠正一个常见误解：FreeBSD 之所以能集成 ZFS，并非因为 BSD 许可证 “比 GPL 更自由”，而是因为 BSD 许可证是 permissive（宽松许可）——它不对与之聚合分发的代码施加许可要求；GPL 是 copyleft 许可，要求衍生作品整体以 GPL 发布，因此与 CDDL 的文件级 copyleft 冲突；这不是 “自由程度” 的差异，而是 copyleft 边界设计的差异
- 原文 50.5 节标题写 “2007 年 ZFS 开源至 OpenSolaris” 有事实错误——ZFS 于 2005 年 11 月开源，OpenSolaris 本身于 2005 年 6 月发布，2007 年并非 ZFS 开源年份；Pawel Dawidek 的 FreeBSD ZFS 移植 commit hash 经 freebsd.duckdb `commits` 表查询验证——FreeBSD src 仓库中该 commit 为 `f0a75d274af375d15b97b830966b99a02b7db911`（2007-04-06T01:09:06Z，详见下行辨析与文献段著录）
- 经 freebsd.duckdb `commits` 表与 `commit_files` 表交叉验证，Dawidek 的 ZFS 主干导入 commit 已确认为 `f0a75d274af375d15b97b830966b99a02b7db911`（author = committer = Pawel Jakub Dawidek，<pjd@FreeBSD.org>，author_date = commit_date = 2007-04-06T01:09:06Z，与文献段两处完整著录一致）

## 文献

- FreeBSD Project. *FreeBSD 7.0 Release Notes* (2008-02-27). freebsd.org; OpenZFS Project. *OpenZFS 2.0.0 Release Notes* (2020-11-30). github.com/openzfs/zfs/releases; Ubuntu Technical Board (2016-02). *Meeting Minutes*. lists.ubuntu.com; LWN.net. *ZFS Coverage Timeline*. lwn.net.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Internet Archive. *opensolaris.org Archive*. web.archive.org/web/*/<https://opensolaris.org>; illumos Project.* illumos-gate Repository *. github.com/illumos/illumos-gate; FreeBSD Project.* Vendor Import of OpenSolaris Code *. svn.freebsd.org/base/vendor/opensolaris/; genunix.org. * OpenSolaris Community Archive*. genunix.org; Dawidek P J. Please welcome ZFS - The last word in file systems. freebsd-src [DB/OL]. 2007-04-06T01:09:06Z. f0a75d274af375d15b97b830966b99a02b7db911. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2005 年间：42,570 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. *Mailing List Archives*. lists.freebsd.org/pipermail/; FreeBSD Project. *Git Repository*. git.freebsd.org/src.git; Dawidek, P. J. (2007). *Porting ZFS to FreeBSD*. BSDCan 2007; FreeBSD Project. *Subversion to Git Migration Notes* (2020); Dawidek P J. Please welcome ZFS - The last word in file systems. freebsd-src [DB/OL]. 2007-04-06T01:09:06Z. f0a75d274af375d15b97b830966b99a02b7db911. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP30、Nerding Out with Victor EPS01E25（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 受访者转述 DTrace 的技术特性：可对系统中任意函数（库或可执行文件内）单独画像、聚合函数调用次数与耗时、语言支持线程局部存储以设条件变量；与 FreeBSD 的 ktrace、truss 等须持续读取内核内存并拖慢全局的工具不同，DTrace 关闭时零开销——它在内核中内置反汇编器、启用时改写指令、只影响被跟踪程序的运行性能；并转述 Bryan Cantrill 的演示：GNOME Terminal 打开一个新窗口竟发起约两千次系统调用。（BSDTalk EP30，[944.34-1076.12]，L1）
- 2006 年 BSD 阵营对脱离 GCC 的可能路径已有零星讨论：受访者借 OpenBSD 3.9 发布与 Theo 不妥协立场的调侃承认当下编译仍离不开 GPL 编译器这一妥协，随即列举替代选项——TinyCC、Intel C 编译器、以 MIT 许可开源的 Plan 9 C 编译器（Ken Thompson 作品，DragonFly 开发者一度关注但须改动内核以支持其目标格式）、以及在研的 TenDRA——结论是未来存在希望。（BSDTalk EP30，[1156.1-1245.58]，L1）
- LinuxWorld 2006 波士顿展会的 BSD 生态见闻：参观者普遍认知匮乏，有人径直询问“这是哪个版本的 Linux”，同时也有大量老用户与挑战者；BitDefender 起初称支持 OpenBSD 随即改口只有 FreeBSD；Coyote Point 为其网络负载均衡设备招募 FreeBSD 开发者；Cluster Resources 的开源自动部署软件希望支持 BSD；嵌入式方向对 NetBSD 兴趣可观。（BSDTalk EP30，[195.34-395.6]，L1）
- 受访者回忆在 Skycache（卫星 Usenet 服务商）的生产部署史：公司先以 NetBSD on SPARC 为上游，经由卫星每日吞吐约 250GB Usenet 流量，其后迁移到 Alpha DS10 上的 FreeBSD，原因是其 TCP 栈在当时表现卓越；受访者本人由此接触 BSD，并因转向安全领域而自然迁移至 OpenBSD。 [存疑脚注] 该段说话人因转写混叠难以确定归属 Dixon 或 O'Dell，公司部署事实本身为受访者一手自述（BSDTalk EP30，[778.04-815.88]，L1）
- Jude 将三大 BSD 与 Linux 发行版的根本差异概括为操作系统边界之争：BSD 把内核、基础工具与驱动同置单一源码树，系统本体与第三方包二分，Linux 则连内核在内一切皆包；FreeBSD 以 ports 树的 Makefile 描述取源、校验、打补丁、构建与卸载全流程，自 FreeBSD 8 起以集群工具每三四日全量重编二进制包，再叠加每三月才升大版本的季度分支兼顾新鲜与稳定，至 13.3 操作系统已可实现可复现构建。（Nerding Out with Victor EPS01E25，[837.0-1180.0]，L1）
- Netflix 案例构成 FreeBSD 工程优势的完整链条：其选型的决定性因素是变更数周即入 mainline 的上游速度而非许可证本身；sendfile 系统调用消除内核与用户态间文件发送的反复拷贝，HTTPS 普及后内核 TLS 让 sendfile 在加密时代复活并在 Spectre 与 Meltdown 加剧越界成本后愈发关键，Netflix 再将批量加密密钥下放网卡专用芯片实现硬件卸载，单路服务器由 100 Gbps 推至 800 Gbps；Comcast 全量切换 IPv6 后的流量规模暴露出四字节计数器回绕溢出，数小时一崩的规律使缺陷迅速定位并经 errata 通知全网上游修复。（Nerding Out with Victor EPS01E25，[1204.0-1702.0]，L2）
- Jude 以 OpenZFS 开发者身份拆解其数据模型：vdev 层承载镜像或 RAID-Z 变换并各自负责完整性，pool 汇聚全部可用容量，dataset 动态共享剩余空间并逐集设定压缩与加密；RAID-Z 借事务性写入从结构上消除 RAID-5 写洞，奇偶校验分布于全组盘而非专用盘，RAID-Z3 为硬件 RAID 所无；LZ4 每核压缩数 GB/s 使透明压缩自 OpenZFS 2.2 起默认开启，早停机制对不可压数据及时放弃，高层级 Zstandard 先以 LZ4 试探再决定是否重压；原生加密采用 AES-GCM 逐数据集加钥，校验和前半与消息认证码后半拆分存储，使加密数据可无密钥完成校验、修复与重建，密钥卸载后数据静态受保护。（Nerding Out with Victor EPS01E25，[2683.0-3597.0]，L1）

**史料**：

- Devon O'Dell 一手自述 DTrace 移植 FreeBSD 的缘起：2005 年 OSCON 上经 Santa Clara OpenSolaris 用户组结识的 Sun 内核工程师 Bryan Cantrill 与 Keith Wesolowski 午餐相劝，他先以移植步骤复杂为由拒绝，后于会后聚会上见到 DTrace 经 PHP 扩展挂钩 PHP 脚本、从函数调用一路追踪进内核再返回的演示，遂动心启动移植；此为 FreeBSD 集成 DTrace 之前最早的移植意向口述之一。（BSDTalk EP30，[851.38-920.82]，L1）
- Jason Dixon 一手自述 OSCON 演示与 Jordan Hubbard 轶事：其防火墙故障切换演讲配三台 Dell 与大屏液晶做 PF 加 CARP 拔线演示，观众惊讶、有风险投资人当场递名片，Astaro 等 iptables 方案因无对应故障切换能力无可竞争；交谈 CARP 与 PF 时发现听众多为 Jordan Hubbard 本人，后者透露 Apple 正尝试将 CARP 集成进 OS X，此后未见后续结果。 [存疑脚注] Apple 集成 CARP 一说系 Dixon 转述 Hubbard 口述，仅此一处，须与 Apple/FreeBSD 邮件档案交叉验证（BSDTalk EP30，[420.8-572.88]，L1）
- 主持人开场转述的新闻：FreeBSD 已与 Sun Microsystems 达成协议获准再分发 Java 1.5，此前用户须到 Sun 网站接受许可条款后另行下载安装，此后可如常规软件包一样直接安装，降低 FreeBSD 用户使用门槛。（BSDTalk EP30，[88.5-115.3]，L2）
- 访谈提供的一手史料线索：Kirk McKusick 关于 BSD 文件系统与 TCP/IP 发明的系列历史讲座（DVD 与会议版本可获取）；BSDI 采用 1-800-ITS-UNIX 订购电话引燃 AT&T 商标与版权主张，USL 诉讼和解据称涉及约七个文件重写且细节从未完全披露；Berkeley 早期以磁带寄送修改并回收补丁的协作形态先于许可证概念出现。（Nerding Out with Victor EPS01E25，[131.0-372.0]，L2）
- OpenZFS 侧一手工程记录：Jude 自述 2018 年创立 Klara 提供 FreeBSD 与 ZFS 开发支持服务，为客户在 Ubuntu 的 LXD 容器中委托 ZFS 数据集以运行非特权 Docker 的特性由其团队开发并上游 OpenZFS，随后随 Ubuntu 22.04 进入生产环境，体现商业委托开发经上游回馈转化为发行版默认能力的路径。（Nerding Out with Victor EPS01E25，[2530.0-2652.0]，L1）

**史观**：

- 总纲5 没有必然性，只有偶然性：Jude 复述并认同的历史反事实：USL 诉讼恰在 386 普及窗口冻结 BSD 采用，芬兰学生 Linus 因 BSD 不可用转而自写内核，Jude 以其口吻称“若非 AT&T 诉讼，我根本不会费劲去写 Linux”（397.0）——Linux 的诞生由法律时序的偶然而非技术优劣决定，许可证纠纷改写了其后数十年的操作系统格局。 [存疑脚注] 该归因系访谈内反事实因果推断，Linus Torvalds 本人对开发动机的一手自述（1991 年 comp.os.minix 发布帖及自传）未被引证，回写大纲时须与一手材料交叉验证。（Nerding Out with Victor EPS01E25，[373.0-413.0]，L2）
- 总纲3 不存在进步，只有权力再分配：治理结构被 Jude 呈现为权力组织方案而非演进等级：Linux 集中于 Linus 与十余名副官的合并权，FreeBSD 则由约 250 名直接提交者每两年选举九人 core team，选举日前 365 天有提交记录者方可投票——两种共同体契约之间不存在谁更先进叙事，只呈现同一开源生产在权力分配上的不同解法。（Nerding Out with Victor EPS01E25，[1727.0-1783.0]，L1）

**辨析**：

- 受访者对 CDDL 的专利条款作三层风险评估：顶层是两名贡献代码的开发者，中层是接受 CDDL 并对部分代码主张专利的厂商，底层是运行该厂商 OpenSolaris 的客户；一旦厂商起诉贡献者，贡献者有六十天通知期撤销其许可，厂商客户随即陷入危险；由此判断 CDDL 从 BSD 许可证立场并不友好，DTrace 不会进入 FreeBSD base 系统，只能作为后启用组件。 [存疑脚注] 对 CDDL 专利终止机制的六十天期限与后果系受访者口头解读，须对照 CDDL 原文条文核验（BSDTalk EP30，[1078.7-1156.1]，L1）
- ZFS 入 Linux 的法律争议在访谈中被简化为实践事实：CDDL 与 GPL 的链接不兼容使 ZFS 长期被 mainline 拒之门外，而 Ubuntu 转为自行编译随发行版提供，Jude 称“结果证明没人起诉他们”（2428.0）——但未被起诉不等于合法性确认，软件自由保护组织等机构 2016 年前后的公开质疑并无司法结论，回写大纲时应作为未决争议点而非定论。 [存疑脚注] 无人起诉即安全的说法为访谈中的实践性推断，CDDL 模块与 GPL 内核合体发行的效力无判例支撑，须对照软件自由保护组织 2016 年公开信等一手文献核实。（Nerding Out with Victor EPS01E25，[2331.0-2428.0]，L2）

**文献**：

- [BSDTalk EP30] Backman W. BSDTalk: 30: bsdtalk030 - Interview with Devon O'Dell and Jason Dixon[EB/OL]. (2006-04-07)[2026-08-27]. <https://archive.org/details/bsdtalk030>.
- [Nerding Out with Victor EPS01E25] Petersson V. Nerding out with Victor: All things ZFS and FreeBSD with Allan Jude[EB/OL]. (2024-12-02)[2026-08-15]. <https://vpetersson.com/podcast/s01e25/>.

<!-- /PODCAST_REVIEW -->
