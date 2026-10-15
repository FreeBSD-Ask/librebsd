---
chapter: 第 130 章
id: CH130
volume: 第06卷-freebsd的核心技术革新
---

# 第 130 章 freebsd110的发布与arm64架构引入

## 要点

- 11.0 引入多个重要用户空间组件：① **libxo(3)**——由 Juniper Networks 赞助、Phil Shafer 开发的通用输出库，使系统工具可同时生成人类可读文本、XML、JSON、HTML 等多种格式输出，**netstat(1)**（r279122，Juniper 赞助；Glen Barber 于 2015-04-28T18:10:35Z 在 commit `d1e2507b7f2a645e09676d1c005713f39968e718` 完成切换〔截断据文献区 commit 著录补全；fstyp/devctl/uefisign/sesutil 等其余组件见文献区〕
- FreeBSD 11.4-RELEASE 于 2020 年 6 月 23 日发布，是 stable/11 分支第五个也是最后一个版本（“fifth and final release”）。核心更新：Clang/LLVM/LLD/LLDB/compiler-rt/libc++ 升级至 10.0.0；OpenSSL 1.0.2u（OpenSSL 1.0.2 系列最终版本）；Unbound 更新至 1.11〔截断据 11.4 Release Notes 组件清单补全，其余组件见要点前段〕
- 11.x 时期 Linux 兼容层（Linuxulator）持续改进：①CentOS 7 兼容层 ports（emulators/linux-c7）在 11.x 时期成熟（10.3 引入 64 位 Linux 支持后持续完善）；②1:1 线程模型与 **epoll(7)** 子集实现在 10.3 基础上持续改进，可运行更多 Linux 商业软件；③ **jail(8)** 内支持挂载 **linprocfs(5)**/``linpediafs`` 等 Linux 文件系统〔截断据 130.3 节 Linuxulator 叙事补全〕

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10423] BSD Now 第 676 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10510] BSD Now 第 661 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10526] BSD Now 第 656 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10533] BSD Now 第 655 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10540] BSD Now 第 654 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10556] BSD Now 第 652 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10566] BSD Now 第 651 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10589] BSD Now 第 645 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10606] BSD Now 第 642 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10630] BSD Now 第 638 期，匹配 CH130 章，关联度 1.0

## 史观

- 专题语（不设总纲条号）——工程扩展：11.0 是 10.x“大整合”之后的“架构扩展”版本，不再集中替换基础组件（见 130.1）。
- 总纲第 22 条——知识注定过时：Hyper-V Gen2 与 AWS ENA 支持的演进（见 130.2）体现云平台知识随基础设施代际更替。
- 社区治理：Security Officer 交接（Colin Percival→Dag-Erling Smørgrav）反映项目治理角色的制度化更替（见 130.2）。
- 总纲第 4 条——分离聚合是永恒规律：bhyve 独立路线（不采 KVM）体现 FreeBSD 在虚拟化领域的分离聚合抉择（见 130.3）。
- 总纲第 10 条——动手者创造历史：Netflix 对网络栈的持续贡献是商业动手者塑造内核的典型案例（见 130.3）。
〔本章级史观由 130.1-130.3 三节史观字段汇总回填，2026-09-13〕

## 辨析

- 部分资料称“blacklistd 在 11.0 已集成到 OpenSSH”——经 11.0 与 11.1 Release Notes 交叉验证，11.0 仅导入 libblacklist 与 blacklistd 守护进程本身，OpenSSH 的 blacklistd 集成在 11.1-RELEASE 才完成（11.1 Announcement 明确列出“Support for blacklistd(8)”）〔截断据 11.1 Release Notes 补全〕
- 部分资料误称“11.4 是最后一个使用 GCC 4.2.1 的版本”——GCC 4.2.1 在 11.x 仍用于 powerpc/sparc64/mips 等非 x86 架构的构建，但 x86 早已默认 Clang；GCC 4.2.1 从 base 中完全移除发生在 FreeBSD 13.0 时期，非 11.4。11.4 携带的 OpenSSL 1.0.2u 是 OpenSSL 1.0.2 系列的最终版本〔截断据要点段补全〕
- Linux 兼容层在 11.x 仍不能运行 Docker——Docker 依赖大量 Linux 特定内核特性（cgroups v2、namespaces 完整集合、systemd socket 等），Linuxulator 实现的系统调用子集不足以支持 Docker；Docker on FreeBSD 在 11.x 时期需通过 bhyve 虚拟机运行 Linux 间接实现。WireGuard 在 11.x 未进入 base（内核实现自 13.0 起）〔截断据 13.x 迁移史补全〕

## 文献

- Shafer P. libxo: A Library for Generating Text, XML, JSON, and HTML Output [EB/OL]. juniper.github.io/libxo/；FreeBSD libxo(3)/blacklistd(8) Manual Pages [Z]；FreeBSD 11.0/11.1-RELEASE Release Notes [Z]. 2016/2017；Barber G. Document r279122, netstat(1) updated to use libxo(3). freebsd-src [DB/OL]. 2015-04-28T18:10:35Z. d1e2507b7f2a645e09676d1c005713f39968e718; Barber G. Document r275680, fstyp(8) addition. freebsd-src [DB/OL]. 2015-01-11T19:01:04Z. 7ddc205dac1e7b03d4a31b9496d9c263ac1c35b6; Barber G. Document r278320, devctl(3) and devctl(8) added. freebsd-src [DB/OL]. 2015-02-20T17:46:10Z. 742355ae61376053156d0875685c04f8cc7d59c3; Barber G. Document r279315, uefisign(8) addition. freebsd-src [DB/OL]. 2015-03-16T15:54:41Z. ac2456f1bd0ee0b03a7a7e7e2742f5fbed7b42ac; Barber G. Document r287473, sesutil(8) addition. Add Gandi.net to sponsor.ent. freebsd-src [DB/OL]. 2015-10-05T20:13:30Z. c4af256e4867cf90b7b1743a08cbb1cf8371f3ed ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2016-2016 年间：44,329 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Release Engineering Team. FreeBSD 11.4-RELEASE Announcement [Z]. 2020-06-23；FreeBSD Project. In Memoriam: Bruce Evans [Z]. 2020；FreeBSD 11.4-RELEASE Release Notes [Z]. 2020；FreeBSD Project. release/11.4.0. freebsd-src 仓库 tag [DB/OL]. 2020-06-16T13:59:51Z. tag: release/11.4.0; commit: 8c639945a44588f6cfdddfb057bb5aad88735da0 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD linux(4)/capsicum(4) Manual Pages [Z]；Watson R N M. Capsicum: Practical Capabilities for UNIX [C]//USENIX Security 2010；FreeBSD 11.x Release Notes Security chapters [Z].

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP290、BSD Now EP225、BSD Now EP162、BSD Now EP58（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 本期转述 FreeBSD 在 Cavium ThunderX ARM64（Gigabyte R120-T32）上的评估：FreeBSD 12 上 ARM64 为 Tier 2，ZFS 引导与二进制更新缺失、网卡受限，但 UFS 下稳定、49 线程源码构建与 ports 可用。（BSD Now EP290，[289.26-352.58]，L2）
- 一篇以 OpenBSD 用户看 NetBSD 8.0 的文章列出优缺点：NetBSD 可装 WAPBL 日志文件系统与 pkgin，但分区、网络配置、法式键盘与无 sudo 等体验不如 OpenBSD。（BSD Now EP290，[539.8-781.1]，L2）
- 本期介绍用 Vim 内建时间能力写 vimscript 插入相对时间戳（自会议开始计），并提及 John Baldwin 在 GitHub 仓库集中管理会议纪要。（BSD Now EP290，[790.32-1007.84]，L2）
- TrueOS 17.12 稳定版发布，含 OpenRC 服务定义更新、Lumina 改进，并基于 FreeBSD current 以提前获取图形与 Wi-Fi 驱动。（BSD Now EP225，[73.68-83.2]，L2）
- PDP-11 回顾引述 C Gordon Bell 等人的论文，梳理 DEC 1957 年创立、以“Programmed Data Processor”避讳“计算机”一词，以及 PDP-11 在地址位、寄存器、栈、中断、字符处理上的设计取舍。（BSD Now EP225，[1844.12-1885.92]，L2）
- 该回顾点明 UNIX 1974 年由 Ken Thompson 携磁带抵达伯克利，演化出 BSD 与 Sun Microsystems；C 的 16 位 int 亦源自 PDP-11。（BSD Now EP225，[2883.82-2958.5]，L2）
- FreeBSD 2017 发布工程回顾：Glen Barber 全职工负责发布工程，11.1 于 7 月 21 日发布，10.4 由另一名发布工程师领衔并作为 stable 10 分支的最终版本。（BSD Now EP225，[3334.96-3475.08]，L2）
- Petra Zeidler 自述经 Markus Wild 的 NetBSD/Amiga 移植在 1993 至 1994 年间接触 NetBSD，其 Amiga 在 NetBSD 1.0 发布约一个月后即运行至今，并长期承担邮件与 Usenet 服务。（BSD Now EP162，[1609.9-1697.9]，L1）[订正：原 [1616.56-1657.0]，2026-09-30 SenseAudio 重转核对]
- NetBSD 的治理与 FreeBSD 不同：core team 由任命而非选举产生、通常不更替，只处理技术事务；凡拥有 commit 权限者皆为 NetBSD Foundation 成员，享有董事会投票权，董事会负责委员会补员、财务与法律事务。（BSD Now EP162，[1914.7-2021.5]，L1）[订正：原 [1916.42-1981.16]，2026-09-30 SenseAudio 重转核对]
- Petra Zeidler 身兼 NetBSD 管理团队、pkgsrc 稳定分支、基金会董事会、安全团队与 EuroBSDCon 基金会 NetBSD 代表等多重角色。（BSD Now EP162，[1708.64-2171.24]，L1）
- NetBSD 借助 pkgsrc 稳定分支提供安全更新，使依赖链底部的包更新先沉淀，避免单个包更新导致半个依赖树失修。（BSD Now EP162，[1803.3-1913.68]，L1）
- FreeBSD 11.0 发布在即，Amazon EC2 实例从 10.3 经 freebsd-update 升级后挂起，原因被定位为 GELI 引导代码按 4K 对齐读取时越过盘尾；修复已提交并安排勘误。（BSD Now EP162，[574.0-1112.1]，L1）[订正：原 [596.0-1096.56]，2026-09-30 SenseAudio 重转核对]
- Voxer 联合创始人 Matt Ranney 自述迁移动机：创业早期流量激增时在 Linux 上遇到无法解决的棘手性能问题，Joyent 朋友建议换到有 DTrace 的平台并成功定位解决，由此认识 DTrace 的价值；自建基础设施、自有硬件时必须保留 DTrace 并想要 ZFS 的 L2ARC 以利用新出现的平价 SSD。在 Joyent 维护的 SmartOS 与 FreeBSD 之间抉择：FreeBSD 10 已为 ZFS 提供 SSD trim 支持而 illumos 仍无，且 FreeBSD 文档好得多、社区响应更快、被认为更稳定；ZFS trim 支持成为压倒性因素。（BSD Now EP58，[903.63-1103.11]，L1）
- 工程师 George Neville-Neil 补充入职时的境况：Voxer 原为全 SmartOS 部署，一次 arc cache bug 导致约 12 台服务器重启 panic；评估替代平台时 Linux 因缺 DTrace 而出局（仅 Oracle Enterprise Linux 有但不够好），最终在 FreeBSD 与 SmartOS 之间选择 FreeBSD。迁移后的部署形态：FreeBSD 10 release 承载全部后端——TLS 终止、全部 Node.js 进程、全部 Redis 缓存与 Riak 持久存储前端；全面 jails 化并从 SmartOS 的整机 zone 模型走向“每进程一 jail”，每个 jail 关联 ZFS 数据集以便进程跨基础设施迁移；用 Chef 自动化并自补 FreeBSD 支持缺口，计划开源相关项目；其 DTrace 内核补丁已被接受进入 10.1 并回移 9.x。（BSD Now EP58，[1015.23-1460.04]，L1）

**史料**：

- 关于 Cavium ThunderX 与 FreeBSD Foundation 合作、Cavium 为 ARM64 参考平台的说明。（BSD Now EP290，[243.98-260.5]，L2）
- NetBSD Foundation 第 4 年（总计第 13 次）参与 GSOC 2019 的公告。（BSD Now EP290，[1066.32-1106.36]，L2）
- C Gordon Bell 等人论文（“What have we learned from the PDP-11?” 等四篇）的转述，含 1957 年 DEC 创立与 PDP-11 设计回顾。（BSD Now EP225，[1940.36-1968.48]，L2）
- 转述的 OpenBSD 工作站指南，含用户动作即时完成、极简工具、硬件隐私等设计目标。（BSD Now EP225，[542.34-652.4]，L2）
- FreeBSD 基金会 2017 发布工程回顾（Glen Barber 的 VBSDCon 演讲与问答）。（BSD Now EP225，[3334.96-3771.04]，L2）
- Petra Zeidler 访谈自述（BSD Now EP162，[1610.1-3220.96]，L1）
- FreeBSD News 1997 年夏季创刊号（David Filo 谈 Yahoo 早期运行于 FreeBSD、David Greenman 谈 CD-ROM.com FTP 服务器）（BSD Now EP162，[4100.78-4489.44]，L2）
- Colin Percival 博客与 FreeBSD 11.0 EC2 改进说明（128 CPU 支持、ENA 驱动、间接段 I/O）（BSD Now EP162，[84.7-406.4]，L2）[订正：原 [86.72-320.32]，2026-09-30 SenseAudio 重转核对]
- 本期新闻段涉及的一手发布材料：OpenSSH 6.7 发布公告（大规模内部重构使其可用作库、SFTP 断点续传、默认禁用 arcfour 等不安全密码、移除 TCP wrappers 支持、Unix 域套接字转发、portable 版支持对 LibreSSL portable 构建、ED25519 类型的 SSHFP 记录生成）；NetBSD 6.1.5 与 6.0.6 发布公告（OpenSSL 1.0.1i、modctl 用户控内存分配、setsockopt 内存泄漏、tap 驱动竞态、IPfilter mbuf 泄漏、PTYFS 两处溢出与内存损坏修复）；GhostBSD 4.0 发布（首个基于 FreeBSD 10，clang 取代 GCC、pkgng 默认、make 换为 bmake、桌面 MATE）；Cavium 与 FreeBSD Foundation 合作公告（捐赠 ThunderX 服务器、目标 ARMv8 tier-1、至多 48 核与 100 Gbps、包仓库逾 24000 应用）；OpenBSD 上线 portroach.openbsd.org 供认领无人维护的 ports。（BSD Now EP58，[482.38-2830.89]，L2）

**史观**：

- 总纲5 没有必然性，只有偶然性：Spectre/Meltdown 后 ARM 服务器因多数 ARM 不受 Meltdown 影响而被重新评估，属偶然事件推动的硬件路线变化。（BSD Now EP290，[79.28-101.08]，L2）
- 总纲9 经验优先：以 OpenBSD 用户亲身试装 NetBSD 8.0 的经验比较二者，而非抽象优劣。（BSD Now EP290，[539.8-781.1]，L2）
- 总纲9 经验优先：贝尔的回顾强调计算机是“总体设计环境”的产物，成功在于为当下造出正确的机器，呼应经验优先的取向。（BSD Now EP225，[2066.0-2101.76]，L2）
- 总纲4 分离聚合是永恒规律：PDP-11 的开放架构使任何按规范实现者皆可称 PDP-11，DEC 内部形成快慢两条实现路线，体现分离聚合的规律。（BSD Now EP225，[2184.72-2209.84]，L2）
- 总纲10 动手者创造历史：发布工程回顾强调除 Glen Barber 外还有大量不在聚光灯下的人协作，凸显动手者叙事。（BSD Now EP225，[3746.94-3769.1]，L2）
- 总纲3 不存在进步，只有权力再分配：NetBSD 以任命制 core team 与基金会集中式权力分配运作，治理形态是具体权力安排而非线性进化。（BSD Now EP162，[1914.7-2021.5]，L1）[订正：原 [1916.42-1981.16]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：当事人以动手维护 Amiga 架构、邮件与 Usenet 服务，边缘平台因持续维护而存续。（BSD Now EP162，[1616.56-1697.7]，L1）
- 总纲4 分离聚合是永恒规律：pkgsrc 稳定分支与 head 分离，依赖整体以“协同的生态”方式聚合，再随安全更新周期性合流。（BSD Now EP162，[1852.94-1913.68]，L1）
- 总纲10 动手者创造历史：上游协作的动手者文化成为企业采纳的助推器：Voxer 工程师试用 Node 的 DTrace helper 失败后一周内自行解决并提交，下一周补丁即被接受，Ranney 感叹“无法想象这发生在其他操作系统上”；上游愿意接受补丁意味着企业不必维护自己的私有补丁集，向 10.1 升级因此变容易。生产者直接改写工具而非等待平台方，是动手者创造历史在 2014 年企业语境中的直接呈现。（BSD Now EP58，[1512.31-1576.90]，L1）
- 总纲9 经验优先：选型方法论的自述：迁移促使 Voxer 认真审视真实技术需求，按实际需要选择技术，“不是因为大家都在用”；平台决策由 Node 进程在 DTrace 下的可见性这一具体经验事实主导，若无该因素结局难料。经验优先于从众与阵营归属，构成该企业案例的方法论内核。（BSD Now EP58，[1281.64-1305.40]，L1）

**辨析**：

- [存疑脚注] 转写中 Cavium/ThunderX 与 Gigabyte 机型、NetBSD 版本号等专名存在 ASR 噪音，且 Tier 1/2 口径为节目转述，未与 FreeBSD 官方平台状态页核对。　[存疑脚注] 硬件专名与 Tier 口径未经官方状态页核对（BSD Now EP290，[240.06-260.5]，L4）
- PDP-11 回顾系博客作者对贝尔论文的二手转述，且转写将“Maria Strobel”等专名误转，人名与具体数字须核对原文。　[存疑脚注] 专名与数字须以贝尔论文原文核实（BSD Now EP225，[1927.8-1965.5]，L4）
- [存疑脚注] 转写对专名的识别可能失真，如董事会成员姓名、pkgsrc 被写作“Package Source”、GELI 被写作“Gelly”，引用时须以一手拼写为准。　[存疑脚注] 专名转写存疑，须核验一手拼写。（BSD Now EP162，[1746.36-2171.24]，L4）
- 当事人对 Linux 与 BSD 用户态差异的批评：这些差异多数无人能说明为何存在或是否重要，却每一个都构成迁移路障——wc 输出带前导空格而 GNU 版没有、make 与 GNU make 不兼容常使 Node 原生模块编译爆掉、GNU 工具新增旗标抢占 BSD 同字母旗标（sort 例）、cp -R 尾部斜杠语义差异曾使其从 Linux 转到 Mac 时脚本大面积失效。建议提供 GNU 工具优先的安装路径或易装的 Linux 用户态层以降低新用户门槛；bash 默认 shell 因 ports 不得触碰 base 的规则而受阻，与 illumos 社区拒绝适应导致采用度落后相对照；一切为平滑过渡做的投入都将换来更大的社区。（BSD Now EP58，[1617.26-2031.17]，L1）
- 社区文化比较的当事人评价：BSD 邮件列表上的讨论相较 Linux 界更像严肃技术专业人士之间的理性辩论；主持人引述某调查显示 BSD 开发者平均年龄比 Linux 开发者大十岁，并认为这与讨论形态相关。George 称其习惯的 illumos 世界信息更难寻，FreeBSD 的文档与 Google 可寻性远优于 illumos 文档，“能用 Google 解决问题在这个年代至关重要”。（BSD Now EP58，[2032.53-2160.41]，L1）
- 上游重构与下游维护成本的当期实例：OpenSSH 6.7 的代码重构破坏了 FreeBSD port 携带的大量补丁，port 维护者 Brian Drewery 表示需要数日逐一整理方可更新，宁可延迟也不发布行为不明的安全组件；同时移除 TCP wrappers 支持将波及依赖它的 denyhosts 类工具。这一案例具体呈现了大型上游重构向下游 port 体系传导的时滞与风险。（BSD Now EP58，[2691.64-2823.43]，L2）

**文献**：

- [BSD Now EP290] Pennington J. BSD Now: 290: Timestamped Notes[EB/OL]. (2019-03-21)[2026-08-15]. <https://www.bsdnow.tv/290>.
- [BSD Now EP225] Pennington J. BSD Now: 225: The one true OS[EB/OL]. (2017-12-20)[2026-08-15]. <https://www.bsdnow.tv/225>.
- [BSD Now EP162] Pennington J. BSD Now: 162: The Foundation of NetBSD[EB/OL]. (2016-10-05)[2026-08-15]. <https://www.bsdnow.tv/162>.
- [BSD Now EP58] Pennington J. BSD Now: 58: Behind the Masq[EB/OL]. (2014-10-08)[2026-08-15]. <https://www.bsdnow.tv/58>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1122 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1122`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon 2024〕讲者 Andrew Turner 口述：FreeBSD arm64 移植始于约 2014 年，距今将近十年。（YouTube EPXGfTCK4kFM0，[1331.08-1335.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1123 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1123`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon 2024〕讲者 Andrew Turner 口述：Mark Johnston（转写音作 Mark did Johnson）为 FreeBSD arm64（转写音作 m64）实现原子操作，arm64 上的原子操作对应纯 ARMv8.0（转写音作 pure RV 8.0）。（YouTube EPXGfTCK4kFM0，[2202.28-2211.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1170 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1170`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018 Emmanuel Vadot 演讲〕讲者 Emmanuel Vadot 口述：其为 Rockchip RK3288（转写音作 rockchip III 2002 8）完成了时钟支持工作（YouTube EPYoB5NknHWbk，[1439.95-1449.84]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-400 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-400`；w172 YouTube 章节路由采纳）

据〔FreeBSD Vendor Summit, 2021 年 11 月〕讲者口述：FreeBSD 11.0 是其 arm64 移植后首个纳入该支持的发行版。（YouTube EPczbF9wA10jY，[175.599-178.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-492 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-492`；w172 YouTube 章节路由采纳）

据〔June 2021 FreeBSD Developer Summit〕讲者口述：该方案支持手工安装 FreeBSD，并使用 ZFS 替代预制的 UFS 镜像（YouTube EPfanQQp2I_aw，[1024.799-1035.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-512 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-512`；w172 YouTube 章节路由采纳）

据〔2020 FreeBSD Vendor Summit〕讲者口述：讲者指出 GCC 9.4（转写音作 gcc and gc 9.4）已支持 outline atomics（轮廓原子操作）。（YouTube EPfmZ9o7CbIvU，[203.599-216.47]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
