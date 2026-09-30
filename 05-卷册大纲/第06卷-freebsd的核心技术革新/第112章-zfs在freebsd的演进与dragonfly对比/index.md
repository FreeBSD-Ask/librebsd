---
chapter: 第 112 章
id: CH112
volume: 第06卷-freebsd的核心技术革新
---

# 第 112 章 zfs在freebsd的演进与dragonfly对比

## 要点

- **统计分析印证**——`freebsd.duckdb` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；Pettitt 与 BUISHAND R 双变点检验一致判定 freebsd-src 变点为
- 一个常见叙事是 “DragonFly BSD 自研 HAMMER/HAMMER2 是因为 CDDL 许可问题”——这一说法不准确；Matthew Dillon 从未将许可证列为不移植 ZFS 的原因，实际原因包括：（1）DragonFly BSD 的 VFS 和内存管理架构与 FreeBSD 差异较大，移植工作量大；（2）Dillon 认为 ZFS 过于复杂，不适合 DragonFly BSD 的
- 关于 Torvalds 2020 年 1 月 6 日 RealWorldTech 帖子的一手史料考证：（1）原帖位置：论坛主题讨论 “Spectre/Meltdown Fixes” 下的回复，讨论中一名用户抱怨内核 API 变更导致 ZFS 等 out-of-tree 模块无法工作，Torvalds 在该 thread 中回复；（2）精确时间：2020 年 1 月 6 日（UTC 时间）；（3）精

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1526] 卷“第06卷-freebsd的核心技术革新”第 112 章，匹配置信度 0.6，原因：无法匹配到具体章节（关键词重叠得分低于阈值）

## 史观

细目详见子节文件史观/辨析字段。

## 辨析

- **统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 Sen's slope =+1.40/月 的实际工程意义须结合 FreeBSD 版本周期与 commit 粒度变化综合判断；(2) 变点归因存疑：1999-08 变点距 2020-01 SVN-to-Git 迁移
- 纠正一个广泛传播的错误叙事：中文技术社区常称 “BSD 自研 HAMMER 是因为 CDDL 不兼容”——这是错的；经 CDDL 文本 §3.5 确认，CDDL 明确允许与其他许可（包括 BSD 和 GPL）的代码在更大作品中聚合，只是对 CDDL 代码本身的修改必须保持 CDDL；DragonFly 不移植 ZFS 是工程和哲学选择，非法律原因
- 常见误读包括：（1）误称 Torvalds 说 “ZFS 是邪恶的”——他从未用 “evil” 一词，原话是 “buzzword” 和 “non-starter”；（2）误将此言论解读为 Linux 项目的官方立场——Torvalds 是以个人身份发表观点，但他作为 Linux 创始人的地位使该言论具有官方效果；（3）忽略言论的上下文（out-of-tree 模块兼容性讨论）；Greg Kroah

## 文献

- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/freebsd.duckdb**; LibreBSD Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5-6; LibreBSD Project. phase3_inferential_stats.py Task 5-6 [CP/OL]. 2026-07-27. **script/phase3_inferential_stats.py**; LibreBSD Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第五卷第 50 章映射。［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Sun Microsystems (2004). *Common Development and Distribution License 1.0* §3.5 [EB/OL]. 获取路径：<https://opensource.org/licenses/cddl1.php> [访问日期 2026-07-30]; Dillon, M. DragonFly BSD Kernel Mailing List Posts [EB/OL] (2007-2008). 获取路径：<https://www.dragonflybsd.org/mailinglists/> [访问日期 2026-07-30].［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Torvalds, L. (2020-01-06). Real World Tech Forum Post [EB/OL] (archived via Wayback Machine). 获取路径：<https://www.realworldtech.com/forum/?threadid=189311> [访问日期 2026-07-30]; Phoronix (2020-01-07). *Linus Torvalds: Don't Use ZFS* [EB/OL]. 获取路径：<https://www.phoronix.com/news/Linux-5.6-ZFS-Oracle> [访问日期 2026-07-30]; LWN.net (2020-01). *Linus on ZFS* [EB/OL]. 获取路径：<https://lwn.net/Articles/809272/> [访问日期 2026-07-30].［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP651、BSD Now EP373、BSD Now EP354、BSD Now EP324、BSD Now EP308、BSD Now EP640、BSD Now EP300、BSD Now EP295、BSD Now EP633、BSD Now EP223、BSD Now EP219、BSD Now EP631、BSD Now EP200、BSD Now EP195、BSD Now EP193、BSD Now EP191、BSD Now EP190、BSD Now EP189、BSD Now EP170、BSD Now EP166、BSD Now EP149、BSD Now EP622、BSD Now EP81（共 23 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 邮件服务器作者以 PF 表加载 MaxMind GeoLite2 的约 27 万条 CIDR，对客户端端口按国家限制、仅 SMTP 保持全球可达，实现暴力破解日志下降约九成。（BSD Now EP651，[110.76-456.00]，L1）
- Alan Jude 的 ZFS 生产部署文章强调，ZFS 事故多为早期布局决策与运维漂移的延迟后果；数据集划分、VDEV 布局、快照策略与持续监控比依赖单一特性更重要。（BSD Now EP651，[782.30-1438.40]，L1）
- FreeBSD 的 Linuxulator 经 SSHD 环境变量引导 Linux bash，使 VS Code Remote SSH 透明运行 Linux 二进制，作者视为 Linux ABI 稳定性与 FreeBSD 兼容层实现质量的证明。（BSD Now EP651，[2152.32-2509.78]，L1）
- OpenBSD arm64 在 Apple Hypervisor 上以客户机运行的提交修复了 VIGPU 地址映射与 DMA 同步问题，并支持 virtio 网络 MTU 协商。（BSD Now EP651，[2838.30-2965.62]，L2）
- 访谈对象 Kyle Evans 因课程同学使用 FreeBSD 而入坑，从 bsdgrep 的 GSoC 项目开始参与 FreeBSD 开发，后当选 Core 团队成员。（BSD Now EP373，[163.48-233.53]，L1）
- bsdgrep 源自 2011 年前后的 GSoC 项目，旨在替换 base 中的 GNU grep；其难点在于需保持与 GNU 扩展及既有脚本依赖的 bug 兼容。（BSD Now EP373，[216.33-426.70]，L1）
- flua 是 base 中专用的 Lua 解释器，避免与 ports 中的 Lua 冲突；引导装载器由 Forth 转 Lua 后，boot 环境菜单等逻辑更易维护。（BSD Now EP373，[517.11-657.27]，L1）
- bectl 源自 GSoC 项目，用于管理 ZFS 引导环境；ZFS Boot CFG 进入上游 OpenZFS 后成为一等特性，可在 UEFI 下工作。（BSD Now EP373，[828.43-1009.87]，L1）
- certctl 将 Mozilla 根证书束纳入 base，使 FreeBSD 12.2 的新装系统默认具备 SSL 信任库，并可增删或拉黑证书。（BSD Now EP373，[1208.75-1317.09]，L1）
- FreeBSD 11.4 进入 RC2，camcontrol、freebsd-update、ZFS 书签重命名、certctl 等更新随 11.4 与 12.2 推出。（BSD Now EP354，[66.04-186.90]，L2）
- Jim Salter 的 Ars Technica 文章以 1.9TB 虚拟机镜像为例比较 ZFS 复制与 rsync：ZFS 靠块出生时间与快照可在 8 秒内完成，而 rsync 需约 2.5 小时。（BSD Now EP354，[474.62-667.52]，L2）
- Colin Percival 自 2008 年起主导 FreeBSD 移植至 Amazon EC2，并持续维护至今。（BSD Now EP354，[674.30-747.26]，L2）
- FreeBSD 项目发起 2020 年社区调查，以量化数据引导项目优先事项与努力方向。（BSD Now EP354，[756.54-846.94]，L2）
- Dan Langille 记录把 ZFS 池从 Dell R710 迁至 R720 的过程：停止应用、导出池、换盘、导入即可，且 ZFS 能跨端序（如 amd64 到 sparc64）处理，远超依赖同型 RAID 控制器的传统迁移。（BSD Now EP324，[261.86-321.34]，L2）
- 《OpenBSD in 2019》体验帖列举其优点（安全优先、base 与 /usr/local 分离、高质量 man page、clang 支持 C++17）与缺点（升级需手动清理、RAM 耗尽死机、find/du/tar 等工具差异），结论是仍愿继续使用。（BSD Now EP324，[501.72-909.04]，L2）
- Hammer2 增加紧急空间模式，允许在无空间写历史时继续磁盘操作，但会牺牲断电保护并可能损坏快照，与 ZFS 预留 slop 空间、UFS 超 100% 的策略形成对照。（BSD Now EP324，[1526.06-1671.52]，L2）
- ICCCM 选择机制的吐槽揭示 X11 规范以 atom 表达一切、缺少目标类型与属性类型的显式关联，实现者各自解读导致兼容性 creep 与增量传输的脆弱。（BSD Now EP324，[1304.40-1519.02]，L2）
- DragonFly BSD 更新 zlib 至 1.2.11、导入 dhcpcd 8.1.1，并把 PAM SSH/TacPlus/Radius 模块移出 base 改由 ports 提供，以换取更频繁的更新节奏。（BSD Now EP324，[923.76-987.80]，L2）
- 主持人以个人 FreeNAS 磁盘 AHCI 超时报错为例，演示用 smartctl 判断磁盘将坏、gpart backup/restore 复制分区表、zpool replace 建立临时镜像直至离线盘被自动移除的完整流程。（BSD Now EP308，[95.42-320.46]，L1）
- Warner Losh 通过 DEC 服务清单考据 PDP-7 序列号 34 为首台运行 Unix 的机器，并指出 99 台 PDP-7 中仅两台带硬盘，移植到 PDP-11 是 Unix 得以延续的关键。（BSD Now EP308，[1066.06-1305.06]，L2）
- 本期介绍在 OpenBSD 上以 umurmur/mumble 自建低延迟 VoIP，证书绑定昵称防止冒名，并提及 OpenBSD 默认禁用音频输入的安全设定。（BSD Now EP308，[710.98-889.42]，L2）
- FreeBSD 在 OCI Runtime Specification 1.3 中被列为官方支持平台，路径包括 Samuel Karp 的 RunJ、Doug Rabson 的 Buildah 与 Podman 移植以及官方镜像。（BSD Now EP640，[106.30-305.54]，L2）
- Jim Salter 的 ZFS 灾难恢复文章以 Sanoid 与 Syncoid 实现快照、销毁与复制的自动化，并强调 RAID 不是备份、备份机应主动拉取而非被动接收。（BSD Now EP640，[339.80-818.48]，L1）
- Chris Siebenmann 通过阅读 DSL 源码说明 ZFS 的 written 与 written@ 属性即时计算，written 需回加已释放空间以避免负值。（BSD Now EP640，[849.96-1060.68]，L1）
- Justin Sherrill 提醒间歇运行的 DragonFly BSD 虚拟机与笔记本因 cron 不触发而无法自动执行 HAMMER 清理，须手动运行 cleanup 以防空间耗尽。（BSD Now EP640，[1070.44-1192.64]，L1）
- CHM 2024 年发布的 Ken Thompson 与 Doug McIlroy 口述史含转录与约四个半小时视频，回顾贝尔实验室与早期 Unix。（BSD Now EP640，[1218.68-1264.24]，L2）
- 1966 年 Joseph Weizenbaum 发表 ELIZA 一文，ELIZA 被视为最早聊天机器人之一，其引发的拟人化反应即 Eliza 效应，并推动作者转向人工智能批评。（BSD Now EP640，[1272.40-1486.48]，L2）
- David Gwynne 在 OpenBSD 引入 source 与 state limiters，以单一限流器跨多端口限制状态数与创建速率，缓解规则重载带来的状态计数重置问题。（BSD Now EP640，[1581.78-1846.92]，L1）
- 本期回顾 BSDCan 2019：开发者峰会含 bhyvecon 与 ZFS 引导代码等工作小组；会议含 Matt Ahrens 的 ZFS 快照、Michael W. Lucas 的 Jails 二十年、CHERI、MQTT 与 NVMe 等演讲。（BSD Now EP300，[209.7-624.64]，L1）
- Allan Jude 的演讲说明 FreeBSD 将把 ZFS 上游从 illumos 仓库切到 OpenZFS（原 Linux 仓库将更名并含各 OS 子目录），以实现单一上游。（BSD Now EP300，[805.52-945.64]，L1）
- 本期转述 iXsystems 博客对 ZFS 池的讲解：磁盘组成 VDEV、VDEV 组成池，镜像可任意加深，RAIDZ2/3 提供双、三重校验。（BSD Now EP300，[1600.86-1821.46]，L2）
- Mariusz Zaborski 的博客解释 unlink/unlinkat 的 TOCTOU 竞态：检查与删除之间文件可能被替换；funlinkat() 通过目录 fd、文件名与已打开 fd 的 vnode 匹配，在内核锁定下消除竞态。（BSD Now EP295，[331.9-743.78]，L2）
- funlinkat() 允许以 FDNONE 回退为 unlinkat 行为，并为 Capsicum 沙箱（只持 fd、不知路径）与多线程删除提供安全保证。（BSD Now EP295，[583.62-743.78]，L2）
- Chris Siebenmann 提示 ZFS 原生加密在 0.8 测试期仍频繁改动磁盘格式，不建议用于关键数据，宜继续用 geli/LUKS 或等待官方发布。（BSD Now EP295，[1517.86-1839.74]，L2）
- Klara Systems 概述 OpenZFS 2.4 路线：标签区从 256 KB 扩至 256 MB 以容纳更多 uberblock 与更长回卷窗口，并规划 anyraidz 以混合容量磁盘提升可用空间。（BSD Now EP633，[379.98-706.22]，L2）
- Ed Brayden 的《Magical Systems Thinking》以 Forrester 的世界模型与啤酒游戏为例，论证复杂系统会反抗自上而下设计，成功来自从小处起步的简单可用系统。（BSD Now EP633，[897.06-1603.88]，L2）
- Broadcom 收购 VMware 后背负约 610 亿美元交易与债务，Bitnami 于 2025 年 8 月终止免费镜像并转向每年数万美元的付费服务，引发开发者迁移潮。（BSD Now EP633，[1612.96-2123.00]，L2）
- OpenSSH 10.1 于 2025 年 10 月 6 日发布，修复用户名控制字符注入问题，并新增 SIGINFO 通道日志、PKCS#11 ED25519 支持与 refuse connection 配置项。（BSD Now EP633，[2126.22-2590.12]，L2）
- Brian Kernighan 在 VCF East 2025 表示只写过一次 Rust 且体验不佳，认为其 crate 与编译链庞大缓慢，同时坦言对 NixOS 与多数发行版并不熟悉。（BSD Now EP633，[2757.82-3220.12]，L1）
- GhostBSD 25.02 基于 FreeBSD 14.3，新增以 GNUstep 组件与 XFCE 面板组合的 Gershwin 桌面，提供类 macOS 体验。（BSD Now EP633，[3371.86-3563.32]，L2）
- backtrace.io 文章比较 GCC 与 Clang 在优化下的 DWARF 调试信息质量，指出 Clang 对部分优化变量可能给出错误值而非“已优化”提示。（BSD Now EP223，[82.36-97.84]，L2）
- 该期讲解 Rust 应用移植到 FreeBSD ports 的流程：ports 以 Makefile 描述构建安装，portlint 检查顺序，make makepatch 生成补丁，约 30,000 个 ports 依赖 POSIX 可移植性。（BSD Now EP223，[916.48-1100.46]，L2）
- 该期辨析 Docker 在 FreeBSD/Solaris 的意义：Docker 是 Linux 与 Windows 隔离问题的解决方案，FreeBSD 以 jails 实现隔离，Docker 的移植依赖 Linux 模拟与 ZFS。（BSD Now EP223，[3109.0-3269.08]，L2）
- FreeBSD 基金会 11 月更新：Matt Ahrens 推进 RAID-Z 扩容（由 FreeBSD 基金会、Delphix、iXsystems 合办），预计 2018 年合入并赶上 FreeBSD 12。（BSD Now EP223，[5082.36-5176.8]，L2）
- Bryan Cantrill 在 Papers We Love 会议演讲中讲解自适应替换缓存（ARC）：ZFS 的实现并非单一最近最少使用缓存，而是划分为最近使用（MRU）、最常使用（MFU）与各自对应的幽灵缓存共四类，幽灵缓存记录刚被逐出的块，用于防止其被临时拉回时扰乱主缓存。（BSD Now EP219，[443.98-513.32]，L2）
- 该期新闻以法文博客的截图教程介绍 OpenBSD 6.2 全盘加密安装：用 bioctl 加密分区并让系统在启动时要求口令；同一博客亦提供 FreeBSD 的 ZFS 加密向导路径，两系统最终都实现无口令即无法读取磁盘的全盘加密。（BSD Now EP219，[5202.38-5547.70]，L2）
- Raymond Chen 复述复杂系统的基本失效模式定理：任何复杂系统都处于某种失效模式，局部补偿使问题潜伏，改变只会带来更复杂的反制。（BSD Now EP631，[138.14-224.48]，L1）
- Dr. Brian Robert Callahan 为 QBE 的 ARM64 后端编写窥孔优化，消除冗余寄存器拷贝与可即时数化的算术指令，说明 ARM64 定长指令下只能通过删除指令获利。（BSD Now EP631，[286.40-737.76]，L1）
- FreeBSD 笔记本作者发现 Nvidia 驱动会覆盖 Xorg 与 DRM 模块的文件，导致 GL 支持判定错乱，移除 Nvidia 驱动并重装 Intel 与 DRM 驱动后恢复正常。（BSD Now EP631，[765.84-908.32]，L1）
- 以 devd 规则按 USB 厂商与产品 ID 建立符号链接，并把链接置于 jail 根目录而非 /dev，可将设备以稳定名称传入 FreeBSD jail。（BSD Now EP631，[921.84-1316.76]，L1）
- Chris Siebenmann 澄清 ZFS 快照并非完全不可变，快照元数据会随独有空间统计、快照删除与重命名而更新，只有文件系统状态被冻结。（BSD Now EP631，[1321.58-1407.46]，L1）
- 将 PeerTube 从 Debian 迁移到 FreeBSD 的过程以 UFS 而非 ZFS 作为客户机文件系统，以避免在 OmniOS 的 ZFS 上嵌套 ZFS。（BSD Now EP631，[1417.28-1794.48]，L1）
- NetBSD announce 中 Soren Jacobsen 公告 netbsd-8 分支已创建，标志 NetBSD 8.0 发布流程启动；相比 7.0 的重大改进包括 USB 3.0 支持与含内核混音器的音频子系统重构。（BSD Now EP200，[154.14-195.94]，L2）
- 关于“scrub of death”的讨论指出：ZFS 校验和使其能发现镜像读到的坏数据，而普通 RAID 镜像无校验、无法察觉副本不同步；真正需担心的是“邪恶磁盘控制器”写错位置，ZFS 至少会检测而非返回错误数据。（BSD Now EP200，[3827.28-3924.82]，L2）
- 主持人援引 ZFS 联合创始人 Matt Ahrens 的说法：ZFS 并不比其他文件系统更需要或鼓励 ECC 内存，ECC 是可靠机器的通用要求；scrub of death 并非真实机制。（BSD Now EP200，[3933.54-4042.18]，L2）
- 该期还报道 FreeBSD 11.1 Beta 3 发布、OpenBSD 把 AMD64 汇编中的 NOP 填充改为 int3 以削弱 ROP gadget 的补丁，以及 ZFS 原生加密将先入 Linux、再经 illumos 进入 FreeBSD 的路线。（BSD Now EP200，[4148.72-5415.98]，L2）
- FreeBSD 的 ino64 项目合入 12-CURRENT：把内核 inode、dev_t、nlink、目录项偏移等从 32 位改为 64 位；项目源自 Gleb Kurtsou 的 PEFS，Kirk McKusick 接手推进，Ed Maste、John Baldwin 等参与，Konstantin Belousov 完成收尾，FreeBSD 基金会赞助。（BSD Now EP195，[63.72-500.34]，L2）
- Michael Dexter 与 iX Systems 的文章介绍用 OpenZFS 只读快照对抗 WannaCry 等勒索软件：感染后可克隆最近的未加密快照立即恢复，并能从未加密克隆中取回感染前刚保存的个别文件。（BSD Now EP195，[879.70-1164.32]，L2）
- 一篇“我为何爱 OpenBSD”的用户自述：从 MS-DOS、Red Hat、SUSE、Slackware 一路转向 OpenBSD，称其安全、文档完善、干净整洁，并作为日常桌面与服务器系统使用。（BSD Now EP195，[510.94-745.00]，L2）
- Adrian Chadd 在 FreeBSD 802.11 栈中启动 802.11ac 支持，先针对 Atheros QCA 10K 芯片，加入 VHT 通道与 20/40/80/160MHz 模式，并说明现有栈在多虚拟接入点上的局限。（BSD Now EP193，[147.78-631.0]，L2）
- Delphix 的 Matt Ahrens 等在 OpenZFS 开发者峰会原型基础上实现 zpool checkpoint，允许管理员在执行破坏性操作前为整个池建立可回滚检查点。（BSD Now EP193，[1810.2-2535.42]，L2）
- TrueOS（原 PC-BSD）改为基于 FreeBSD current 的滚动发布，默认 Lumina 桌面；DistroWatch 评测肯定其 ZFS 集成与安装流程，但指出硬件兼容与稳定更新方面的不足。（BSD Now EP193，[2605.18-3020.76]，L2）
- LibreSSL 2.5.4 修复证书验证回调一致性与 Linux getrandom 阻塞等问题；Michael Hendricks 因 Heartbleed 后 OpenBSD 分叉 LibreSSL 的经历由 macOS 转投 OpenBSD。（BSD Now EP193，[1277.66-1583.66]，L2）
- FreeBSD 长期使用 32 位 inode，单文件系统与 NFS 导出受约四十亿对象上限制约；ino64 分支源自 Gleb Kurtsou 的 GSoC 项目，后由 Kirk McKusick 接手，征集新旧内核与用户态混搭测试。（BSD Now EP191，[2826.6-3145.38]，L2）
- OpenBSD 在 amd64 与 i386 将 Clang 加入 base 作为非默认编译器，动因是 GCC 转向 GPLv3 以及支持 arm64 新硬件的需求。（BSD Now EP191，[5192.9-5287.82]，L2）
- Tatu Ylönen 于 1995 年向 IANA 申请端口 22，因 SSH 拟取代 FTP（20/21）与 Telnet（23），次日获 Joyce Reynolds 分配该端口。（BSD Now EP191，[5570.38-5905.62]，L2）
- 德国高校与 AV-TEST 合作研究扫描 64,415 个 GitHub PHP 代码库，发现 117 处与教程漏洞同源的安全缺陷，其中约八成是 SQL 注入。（BSD Now EP191，[4149.76-4709.4]，L2）
- OpenBSD 6.1 如期发布，为项目第 42 个版本；SSH 特权分离不再可配置关闭，并去除随机化与校验检查以支持 AFL fuzzing。（BSD Now EP190，[409.46-563.58]，L2）
- ZFS 压缩 send/receive 依赖压缩 ARC 特性，可跨网络直接传输压缩块，避免发送前解压、接收后再压缩的低效流程。（BSD Now EP190，[3892.42-4264.2]，L2）
- Kris Moore 披露 FreeNAS 11 将采用 jail 插件、从 GRUB 切换 BSD loader，并计划引入持久 L2ARC 等 ZFS 特性。（BSD Now EP190，[3280.58-3598.7]，L1）
- Mike Muuss 于 1983 年受 Dave Mills 言论启发，一夜写出 ping 并为 4.2a BSD 补充内核 ICMP 支持；ping 命名来自声呐回响，而非“Packet Internet Groper”缩写。（BSD Now EP190，[4653.46-4908.5]，L2）
- NetBSD 在其 wiki 列出 GSoC 内核级与用户态项目并标注难度；FreeBSD 的项目含 Lua bootloader、POSIX 合规测试框架、.NET Core CLR 移植等。（BSD Now EP189，[585.22-733.18]，L2）
- 受访者 Wendell 回忆 ZFS 可从多盘硬件故障且池满的状态恢复数据，并支持池在 SPARC 与 amd64 架构间跨字节序移植。（BSD Now EP189，[4340.92-4558.02]，L1）
- Wendell 用退役的 IBM NetApp 磁盘柜与 Google Search Appliance（Dell R710）搭建 10GbE 视频存储，ZFS 压缩使八百万文件遍历缩短到八分钟。（BSD Now EP189，[4702.86-5620.86]，L1）
- Ted Unangst 撰文记录在网站登录、系统登录等场景使用 YubiKey 的体验，以帮助他人少走弯路。（BSD Now EP189，[6182.44-6225.48]，L2）
- EuroBSDCon 2016 因视频团队两次均未到场而最终无录像，组织方收集了几乎全部讲者的幻灯片；Alan Jude 回顾了与 Rod Grimes、Jordan Hubbard、Kirk McKusick、Robert Watson 等人的现场交流。（BSD Now EP170，[72.16-122.12]，L1）
- 会议议题涵盖 Rod Grimes 的 FreeBSD 早期历史、Jordan Hubbard 的 FreeNAS 10、Intel netbooting、RISC-V、bhyve 六周年、PCI passthrough 与 Hyper-V 上的 FreeBSD 虚拟机。（BSD Now EP170，[213.42-243.24]，L1）
- Robert Watson、Benno Rice 与 John Baldwin 在会议期间讨论一种新的 IPC 或 RPC 机制，具体方案尚未公开。（BSD Now EP170，[496.7-518.6]，L1）
- Chris Staub 的文章梳理应用级沙箱谱系，从早期 systrace、Linux seccomp/libseccomp、FreeBSD Capsicum 到 macOS sandbox_init，认为其复杂度使开发者难以坚持使用。（BSD Now EP170，[1394.66-1424.68]，L2）
- pledge 以“使用画像”而非逐系统调用白名单表达权限，处于易用与能力的折中位置；其局限在于不能区分对具体文件的读写，且允许 exec 时可能启动未受沙箱约束的程序。（BSD Now EP170，[1497.66-1661.62]，L2）
- 与 pledge 相比，Capsicum 以文件描述符能力限制具体操作，沙箱内启动的子程序继承同一沙箱且权限只减不增；bsd patch 的 capsicum 化因文件角色清晰而十分容易。（BSD Now EP170，[1663.1-1819.74]，L2）
- 主持人认为 Capsicum 并非传闻中那样困难，已有团队推进 base system 工具的沙箱化，目标是覆盖 portsnap、freebsd-update 等所用的全部工具。（BSD Now EP170，[1717.96-1778.68]，L1）
- 一个 GitHub 仓库以自定义软件合成 24 个快照，将 Unix 自 1970 年 2500 行内核与 26 条命令到 2016 年 2700 万行系统的历史整理为约 50 万次提交、2000 余次合并的 1.1 GB 仓库，并识别约 1000 名贡献者。（BSD Now EP170，[1855.86-1934.38]，L2）
- FreeBSD 提交者 Sevan Janiyan 利用该历史仓库修正 man page 中工具首次出现时间的错误与缺失，并在 EuroBSDCon 前获得 commit bit。（BSD Now EP170，[1955.24-2035.46]，L2）
- Eric McCorkle 用 Grub 作引导器，在同一 ZFS 池上以 legacy mountpoint 分别挂载 FreeBSD 与 Gentoo Linux 数据集，实现两个系统的双启动。（BSD Now EP170，[653.26-839.66]，L2）
- ZFS 在磁盘前后各保留约 512K 的标签副本，共四份；即使磁盘被重新分区，只要任一标签完好，zpool 仍可被识别并导入。（BSD Now EP170，[3685.1-3733.14]，L1）
- 管道概念由 Doug McIlroy 在 Unix 早期提出，1969 年 Ritchie、Thompson 等人围绕文件系统设想时已在黑板讨论，但因当时被认为缺乏想象力而搁置，直到 1972 年才实际实现。（BSD Now EP166，[233.7-308.86]，L2）
- McIlroy 将管道与过滤器描述为连接程序与数据、消解组合程序时“意外困难”的概念结构，使可互相调用的程序在实践上能够真正连接。（BSD Now EP166，[398.14-414.98]，L2）
- NCC Group 以 AFL 加 QEMU 组成 TriforceAFL，并借助 flashrd 生成的 OpenBSD 系统对系统调用进行模糊测试，工具已开源，节目主持人提出可将同类方法转向 FreeBSD 系统调用。（BSD Now EP166，[122.62-224.46]，L2）
- Mark Schilder 的 FreeBSD MySQL 导入记录显示，通过关闭 sync_binlog、InnoDB flush log at commit 与 doublewrite，并将 ZFS sync 设为 disabled，导入速度从每分钟数十 MB 提升至数 GB。（BSD Now EP166，[566.72-824.56]，L2）
- MySQL 数据库在 ZFS 上宜将 record size 设为 16K 以匹配 InnoDB 页大小、减少写放大，并可设 redundant_metadata=most 与 logbias=throughput 降低元数据写与 ZIL 开销。（BSD Now EP166，[838.88-1004.52]，L2）
- OpenBSD VMM 的 vmctl 命令行与配置文件风格接近 bhyve 管理框架，配置可被 UCL 解析，但当时仅支持运行 OpenBSD 客户机，且只在 2016 年 10 月 22 日以后的最新 snapshot 中提供。（BSD Now EP166，[1128.68-1256.52]，L2）
- Adhoku 以 Ansible 和 FreeBSD Jails 复刻 Docker 式部署，每个应用创建独立 jail 并由宿主机 nginx 反向代理按域名分发，使单个 IP 可承载多站点，宣称无需 FreeBSD 专门知识。（BSD Now EP166，[1636.04-1775.64]，L2）
- FreeBSD Foundation 2016 年 10 月更新预告 developer summit 与 MeetBSD，并强调年末小额捐赠的数量关系到基金会维持公共慈善地位，而非仅依赖少数大额捐赠。（BSD Now EP166，[1259.92-1293.08]，L2）
- NetBSD 7.0.2 为小型安全更新，修复 mail.local 竞态、更新 OpenSSL 与 NTP/BIND，并修复 UFS1 外来文件系统、MIPS pmap 与 SPARC64 问题。（BSD Now EP166，[2064.56-2101.88]，L2）
- Matthew Dillon 修复 DragonFly 内核 MMC/SD 读写的 AB_RID 未清零导致的短读写，并将首次超时后的等待从 10 秒降为 1 秒，减少死端口引导延迟。（BSD Now EP166，[2108.32-2152.92]，L2）
- 本期核心为长期推动 bhyve 的 Michael Dexter 之当事人口述：MeetBSD 2010 圆桌认定 Xen 许可证与内核级复杂度不适于 FreeBSD，与会者得出“我们需要一个 hypervisor”（2641.42）的结论；2011 年 BSDCan 开发者峰会上 Neel Natu 与 Peter Grehan 展示尚属厂商内部项目的 bhyve，Dexter 随即以“零号用户”身份编写自动化脚本、暴露串口与 virtio 缺陷，促成其按期进入 FreeBSD 10 而非推迟到 11 或 12。（BSD Now EP149，[2585.26-2751.50]，L1）
- 新闻与动态部分构成 2016 年年中的 BSD 生态横截面：bhyve 的 UEFI/GOP 图形支持于录制前两日合入 FreeBSD CURRENT 并将随 11.0-BETA1 发布（7505.39-7554.56）；FreeBSD 基金会六月月报披露 Peter Holm 压力测试套件十年发现约 1400 个内核问题、Konstantin Belousov 复核其中 910 个；Solaris /proc 之父 Roger Faulkner 逝世，Bryan Cantrill 在 Hacker News 追忆其 pgrep 与师承轶事；RetroBSD 等项目将 BSD 2.11 与 4.4 移植至 PIC32 微控制器。（BSD Now EP149，[7505.39-7554.56]，L2）
- Mark Phillips 自述 2014 年入职仅约 18 个月的 Ansible，次年公司被 Red Hat 收购；此后在 Red Hat 与多家创业公司间辗转，2025 年初加入 FreeBSD Foundation 任技术营销经理。（BSD Now EP622，[407.42-944.24]，L1）
- Mark Phillips 主张营销的本质是对好产品讲好故事，把营销替换为讲故事即可理解其工作，并强调技术与营销互为表里、工程师需要被反馈其工作价值。（BSD Now EP622，[944.24-1506.38]，L1）
- Mark Phillips 认为 ZFS 是 FreeBSD 的杀手特性，Solaris 系统管理员因 ZFS 与 DTrace 的继承而转向 FreeBSD，FreeNAS 等产品也以此为基础。（BSD Now EP622，[1051.38-1238.66]，L1）
- Mark Phillips 曾帮助测试 Colin Percival 的 EC2 ZFS 根镜像工作，并从 Lightsail 迁往 EC2 以获得 ZFS 根文件系统。（BSD Now EP622，[1205.98-1244.40]，L1）
- Mark Phillips 建议开发者讲故事时不要试图改变他人想法，而是热情讲述自己相信并亲历的解决过程；他推荐 John York 的《Into the Woods》、Seth Godin、Kahneman 与 Nancy Duarte 等读物。（BSD Now EP622，[2825.06-3030.52]，L1）
- Lawrence Teo 的开发者入职路径浓缩了 OpenBSD 的贡献者遴选逻辑：遵“shut up and hack”（1800.24-1813.92）准则多年只发附带补丁的邮件（2004 年修改 MD5 工具、为 IBM 鼠标上报 USB ID），后因 libpcap 与主线脱节且无人认领而独自以约五个工作周完成同步，巨型 diff 一度无人跟进，直至数月后重提才获邀进入开发者私有频道并于 2012 年 5 月获得提交权——身份由持续产出与在任开发者接纳共同决定，而非自荐申请。（BSD Now EP81，[1792.90-1929.90]，L1）[订正：原 [1793.16-1861.10]，2026-09-30 SenseAudio 重转核对]
- Calyptix 的产品形态是 2015 年 OpenBSD 商用可行性的个案证据：面向无 UNIX 经验的微软系管理员提供基于 OpenBSD 的防火墙设备，尽量沿用 base 系统与通用内核（PF、IPsec/iked，LibreSSL 自 2014 年 12 月起生产环境使用，坚持 stock ksh 而不用 bash 使 Shellshock 几无影响），并以全自动更新应对中小机构无力运维的现实；客户覆盖律所、学校、医院、银行乃至 NASCAR 车队与路边广告牌，Teo 以“I'm living proof that it is”（2852.18-2857.62）回应 OpenBSD 是否已可商用。（BSD Now EP81，[2551.84-2857.62]，L1）
- OpenSSH 6.8 显示上游重构与下游发行版同步的摩擦成本：内部代码库化重构使 FreeBSD portable 版既有补丁全部失效、进入 ports 的时点推迟；同期新增 SHA-256 base64 主机指纹并设为默认、UseDNS 默认值由 yes 改为 no、实验性主机密钥轮换与多公钥认证，以及不依赖 OpenSSL/LibreSSL 的构建选项（仅保留 ED25519 与 ChaCha20 等新算法套件）——安全快速迭代与发行版移植节奏之间的张力在 2015 年已清晰可见。（BSD Now EP81，[1036.18-1192.06]，L2）

**史料**：

- Klara Systems（Alan Jude）博客文章 ZFS in Production: Real-World Deployments, Patterns, and Pitfalls。（BSD Now EP651，[782.30-1438.40]，L1）
- Rubenerd 博客关于 XFCE 桌面与 FreeBSD Linuxulator 远程开发的两篇文章。（BSD Now EP651，[1500.36-1745.60]，L1）
- Undeadly.org 关于 OpenBSD arm64 支持 Apple Hypervisor 的提交报道。（BSD Now EP651，[2838.30-2965.62]，L2）
- Kyle Evans 本人口述其参与 bsdgrep、flua、bectl、certctl 与 Core 团队的经过。（BSD Now EP373，[163.48-1933.73]，L1）
- 访谈提及 Warner Losh 引入 Lua 脚本、Alan Jude 作为 GSoC 导师等当事人协作细节。（BSD Now EP373，[522.88-867.89]，L1）
- Jim Salter 在 Ars Technica 的 OpenZFS 指南及 syncoid 工具说明。（BSD Now EP354，[474.62-597.86]，L2）
- 关于 Colin Percival 的播客访谈，介绍其 Tarsnap 创立、AWS 使用经验与 FreeBSD 安全官经历。（BSD Now EP354，[674.30-747.26]，L2）
- Dan Langille 博客的 ZFS 迁移记录，含 zpool status 快照、驱动托盘与 ICY Dock 适配器换装细节。（BSD Now EP324，[133.60-235.80]，L2）
- 用户体验帖《OpenBSD in 2019》及其对 GNU cpio 1994 年遗留 bug 的对照检查。（BSD Now EP324，[388.92-402.52]，L2）
- DragonFly BSD 关于 Hammer2 emergency mode 的提交说明，及 zlib、dhcpcd、PAM 模块调整的维护记录。（BSD Now EP324，[937.08-993.00]，L2）
- Brian Kernighan《Unix: A History and a Memoir》由 Princeton 于 2019 年 10 月出版的信息。（BSD Now EP324，[1938.08-1996.44]，L2）
- Warner Losh 博客关于 PDP-7 序列号 34 的考据，引 DEC 服务清单与 Bob Supnik 提供的 18 位服务列表。（BSD Now EP308，[1066.06-1305.06]，L2）
- OpenBSD Foundation 2019 年度个人捐款突破 5 万加元、社区成白金捐赠者的公告。（BSD Now EP308，[1900.42-2027.46]，L2）
- FreeBSD Foundation 博客 FreeBSD Officially Supported in the OCI Runtime Specification 1.3。（BSD Now EP640，[106.30-305.54]，L2）
- Jim Salter 于 Klara Systems 的 ZFS 灾难恢复文章。（BSD Now EP640，[339.80-818.48]，L1）
- Chris Siebenmann 关于 OpenZFS written 与 written@ 属性的博客。（BSD Now EP640，[849.96-1060.68]，L1）
- Justin Sherrill 的 DragonFly BSD Digest。（BSD Now EP640，[1070.44-1192.64]，L1）
- David Gwynne 的 Undeadly 文章 source and state limiters in PF。（BSD Now EP640，[1581.78-1846.92]，L1）
- BSDCan 2019 开发者峰会与会议，ScaleEngine 负责直播，视频发布于 FreeBSD YouTube 频道，笔记存于 FreeBSD Wiki。（BSD Now EP300，[574.74-627.28]，L1）
- Allan Jude 与 Matt Ahrens 主持的 OpenZFS BoF，及可公开参加并录制的 ZFS 领导力电话会议。（BSD Now EP300，[726.24-945.64]，L1）
- Jess Frazelle 关于开源固件重要性的博客，涉及 Nerf、ME cleaner、root of trust 及 Cerberus、Titan、Nitro 对比。（BSD Now EP300，[2051.0-2471.74]，L2）
- Mariusz Zaborski 的 funlinkat 博客，说明 unlink 为 syscall 10 的历史与 vnode 语义。（BSD Now EP295，[57.0-85.64]，L2）
- Josh Rastin 的 AT&T U-Verse OpenBSD 路由器博客，用 eap_parrot 代理 802.1X EAP。（BSD Now EP295，[785.02-1092.9]，L2）
- Klara Systems 的 OpenZFS 2.4 路线图文章。（BSD Now EP633，[379.98-706.22]，L2）
- Ed Brayden 于 worksinprogress 的《Magical Systems Thinking》。（BSD Now EP633，[897.06-1603.88]，L2）
- fastcode.io 关于 VMware 收购与 Bitnami 收费的报道。（BSD Now EP633，[1612.96-2123.00]，L2）
- OpenSSH 10.1 官方发布说明。（BSD Now EP633，[2126.22-2590.12]，L2）
- The New Stack 对 Brian Kernighan 在 VCF East 2025 问答的报道。（BSD Now EP633，[2749.04-3342.34]，L2）
- backtrace.io 的编译器可调试性文章，以 DWARF 状态机解释优化后变量的取值恢复。（BSD Now EP223，[72.32-97.84]，L2）
- Andrew Cherkashin 的 Rust 移植 Medium 文章（以 fd 工具为例说明 port 的 Makefile 结构）。（BSD Now EP223，[923.72-1010.84]，L2）
- FreeBSD 基金会 2017 年 11 月开发项目更新，含 RAID-Z 扩容、Broadcom Wi-Fi、ARM bhyve 与 LLD。（BSD Now EP223，[5033.72-5513.96]，L2）
- Bryan Cantrill 的 ARC 相关论文与 Papers We Love 会议演讲录像；OpenBSD 6.2 全盘加密法文教程博客（同一作者另写 FreeBSD 版本）。（BSD Now EP219，[56.18-608.32]，L3）
- 访谈中 Allan Jude 自述 BSD Now 的创立：TJ（blackheim）提出每周 BSD 播客设想并试写三期节目笔记，后由 Chris Moore 与 Allan Jude 主持，Jupiter Broadcasting 提供制作、网站与赞助基础设施。（BSD Now EP219，[4392.52-4801.32]，L1）
- Raymond Chen 于 devblogs.microsoft.com 的《The fundamental failure mode theorem》。（BSD Now EP631，[138.14-224.48]，L1）
- Dr. Brian Robert Callahan 博客 QBE ARM64 窥孔优化系列。（BSD Now EP631，[286.40-737.76]，L1）
- Chris Siebenmann 博客 ZFS snapshots aren't as immutable as I thought。（BSD Now EP631，[1321.58-1407.46]，L1）
- 关于 FreeBSD jail 设备稳定名称与 PeerTube 迁移的两篇博客。（BSD Now EP631，[921.84-1794.48]，L1）
- NetBSD announce 邮件列表 Soren Jacobsen 公告；Matt Ahrens 在 Ars Technica 评论及《ZFS 书》中的引语；OpenBSD trap sled 提交说明。（BSD Now EP200，[154.14-4042.18]，L3）
- ino64 合入 FreeBSD 12-CURRENT 的公告；iX Systems 与 Michael Dexter 的反勒索软件文章；OpenBSD 用户自述文章。（BSD Now EP195，[63.72-1164.32]，L2）
- Adrian Chadd 关于 802.11ac bring-up 的博客（BSD Now EP193，[81.22-648.52]，L1）
- Delphix 关于 zpool checkpoint 的设计说明博客（BSD Now EP193，[1810.2-2600.06]，L1）
- DistroWatch 对 TrueOS 的评测文章（BSD Now EP193，[2605.18-3031.58]，L1）
- LibreSSL 2.5.4 发布说明（BSD Now EP193，[5057.4-5151.86]，L1）
- Constantine Belousov 的 ino64 测试征集邮件（BSD Now EP191，[2826.6-3145.38]，L1）
- OpenBSD Clang 使用 FAQ（BSD Now EP191，[5192.9-5287.82]，L1）
- SSH.com 发表的“How SSH got port 22”历史文章（BSD Now EP191，[5570.38-5905.62]，L1）
- TU Berlin、Saarland University、TU Braunschweig 与 AV-TEST 合作的教程安全缺陷论文（BSD Now EP191，[4149.76-4709.4]，L1）
- OpenBSD 6.1 发布公告（BSD Now EP190，[72.92-87.54]，L1）
- FreeBSD ZFS vendor 分支导入提交（BSD Now EP190，[3892.42-4264.2]，L1）
- Kris Moore 访谈自述（BSD Now EP190，[3280.58-3714.9]，L1）
- Mike Muuss 的 ping 主页自述（BSD Now EP190，[4653.46-4908.5]，L1）
- Dennis Ritchie《The Evolution of the Unix Time-sharing System》（BSD Now EP190，[8.0-13.36]，L1）
- NetBSD GSoC wiki 项目列表（BSD Now EP189，[670.66-741.64]，L1）
- FreeBSD GSoC 项目列表（BSD Now EP189，[585.22-667.7]，L1）
- Wendell 访谈自述（BSD Now EP189，[4340.92-6064.62]，L1）
- Ted Unangst 的 YubiKey 使用博客（BSD Now EP189，[6182.44-6225.48]，L1）
- Chris Staub 关于以 pledge 做 Web 应用沙箱的专题文章，含 seccomp、Capsicum、sandbox_init 的比较。（BSD Now EP170，[1380.06-1709.34]，L2）
- Unix 完整提交历史 GitHub 仓库及其 README，覆盖 1970 至 2016 年的 24 个快照合成。（BSD Now EP170，[1855.86-1934.38]，L2）
- Eric McCorkle 的 FreeBSD 与 Gentoo Linux 同一 ZFS 池双启动教程。（BSD Now EP170，[653.26-839.66]，L2）
- Rhonda Hauben 撰写的 Unix 管道历史文章，引用 Doug McIlroy、Dennis Ritchie 与 Ken Thompson 的记述，主持人逐段转述。（BSD Now EP166，[233.7-422.96]，L2）
- NCC Group 开源的 TriforceAFL 与 flashrd 工具链（GitHub 仓库），用于 OpenBSD 系统调用模糊测试。（BSD Now EP166，[122.62-224.46]，L2）
- Mark Schilder 关于在 FreeBSD 上加速 MySQL 导入的博客文章，列出 InnoDB 与 ZFS 调优清单。（BSD Now EP166，[566.72-1010.56]，L2）
- Keith Burnett 的 OpenBSD 6.0 笔记本安装教程（ThinkPad X60 上配置 XFCE、doas 与 USB 挂载）。（BSD Now EP166，[1802.96-1947.44]，L2）
- 访谈内嵌多条可回溯的一手史料：Dexter 保存的旧式 Unix 光盘与 CSRG 档案实物（1795.82-1806.61）、其维护于 multiplicity.bsd.lv 的 Xen/NetBSD 文档与 multiplicity 脚本、投向 AsiaBSDCon 与 BSDCan 的 SMART 工具设计论文，以及他转述的 Robert Watson 关于系统调用包装器并发缺陷的 WOOT 论文（2220.21-2227.67），可供 bhyve 与 jails 相关章节的口述史与文献双轨考据。（BSD Now EP149，[1795.82-1806.61]，L1）
- Mark Phillips 访谈（2025 年 7 月柏林 Hackathon 现场）。（BSD Now EP622，[66.14-3216.34]，L1）
- FreeBSD Foundation 关于页面与 YouTube 频道内容。（BSD Now EP622，[2688.00-2695.60]，L2）
- 本期可入档的一手与准一手材料包括：AsiaBSDCon 2015 现场见闻（Dev Summit 与 vendor Summit、NetBSD Developer Summit、运行 NetBSD 的 Dreamcast 展台）；Lawrence Teo 专访（Calyptix 自 2006 年起每周向客户设备自动推送升级，含 LibreSSL 替换与 OpenBSD 本体整版升级）；Miod Vallat 将 OpenBSD versions 文件改回 -current 的提交日志（附仿《回到未来》的提交信息）；OpenSSH 6.8 发布公告；FreeBSD Foundation“FreeBSD from the Trenches”系列 AutoFS 博文；OpenBSD 澳洲 hackathon 报告（Jonathan Gray 的 AMD GPU 与图形工作、Ted Unangst 的虚拟内存层 SMP 工作）；OpenBSD 邮件列表经 SNDIO 与 SSH 端口转发跨网络播放音频 CD 的帖子；openBGPD 分发 PF 表更新的操作文章；GNU IceCat 31.5.0（Firefox 自由软件版）缺 BSD 移植的邮件列表问询帖；以及 Glenn Barber 关于 ZFS 旧池残留致启动挂起的博文。（BSD Now EP81，[4728.66-5006.99]，L2）　[订正：原 “Tor Browser Bundle 缺 BSD 版本的移植笔记”（新转写为 GNU IceCat 31.5.0 移植问询帖），2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲9 经验优先：总纲9 经验优先：邮件服务器作者以实际运维数据评估地理过滤的收益与代价，而非依赖纸面推断。（BSD Now EP651，[449.80-530.32]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Alan Jude 记录的 ZFS 事故源于接错线缆、换错盘等一线操作，运维纪律而非技术神话决定成败。（BSD Now EP651，[1336.04-1395.14]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：OpenBSD 与 FreeBSD 在虚拟化与兼容层上各自吸收上游技术又保持分化，构成分合循环。（BSD Now EP651，[2852.22-2965.62]，L2）
- 总纲10 动手者创造历史：Kyle 以“找让自己不舒服的问题”为切入点，从具体缺陷入手参与系统开发，体现动手者以具体工程推动项目。（BSD Now EP373，[1604.00-1770.17]，L1）
- 总纲9 经验优先：访谈强调通过实际项目学习并建立人际网络以获取经验，而非单纯阅读文档。（BSD Now EP373，[1639.55-1710.47]，L1）
- 总纲9 经验优先：ZFS 复制对 rsync 的优势来自块级快照的实际经验，而非理论推断。（BSD Now EP354，[560.26-667.52]，L2）
- 总纲3 不存在进步，只有权力再分配：社区调查旨在重新分配开发优先级，体现技术方向由使用数据而非线性进步主导。（BSD Now EP354，[756.54-846.94]，L2）
- 总纲9 经验优先：总纲9 经验优先：ZFS 迁移与 OpenBSD 评估都来自动手记录与亲身使用，而非厂商宣传或抽象判断。（BSD Now EP324，[106.52-115.00]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：OpenBSD 的优点被承认、缺点被具体列出，不神话也不贬低任何一方。（BSD Now EP324，[501.72-909.04]，L2）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：ZFS 数据可从一台机器分离、在另一台聚合，硬件代际更替体现分离聚合的循环。（BSD Now EP324，[263.66-301.54]，L2）
- 总纲12 科学是形式主义：总纲12 科学是形式主义：写时复制、紧急模式、slop 空间是文件系统对空间与安全的形式化约定。（BSD Now EP324，[1542.42-1671.52]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：OpenBSD 体验帖中列出的坏项可能已被修复，工具行为随版本变化，知识需持续更新。（BSD Now EP324，[898.80-921.40]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：能否顺利迁移取决于托盘规格、热插拔适配等偶然硬件条件，而非抽象必然。（BSD Now EP324，[142.44-153.60]，L2）
- 总纲5 没有必然性，只有偶然性：Unix 在 99 台 PDP-7 中仅两台带硬盘的偶然条件下诞生，并因 PDP-11 移植而延续。（BSD Now EP308，[1236.88-1271.3]，L2）
- 总纲9 经验优先：主持人以亲身动手替换故障磁盘的经验记录运维史，而非停留在理论推演。（BSD Now EP308，[95.42-320.46]，L1）
- 总纲10 动手者创造历史：Warner Losh 以逐台机器核对服务清单的动手考据方式确证首台 Unix 机器。（BSD Now EP308，[1066.06-1305.06]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：OCI 支持由 Samuel Karp、Doug Rabson 等志愿者的多年内核与工具链工作累积而成。（BSD Now EP640，[227.38-305.54]，L2）
- 总纲9 经验优先：总纲9 经验优先：Jim Salter 以亲身经历过的断电、火灾、失窃等故障说明为何 RAID 不等于备份。（BSD Now EP640，[630.76-692.68]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：HAMMER 清理依赖 cron 定时触发的假设在笔记本关机场景下失效，反映旧运维假设随硬件使用方式变化而过时。（BSD Now EP640，[1081.24-1215.64]，L1）
- 总纲4 分离聚合是永恒规律：OpenZFS 从各平台分叉走向单一上游仓库的再聚合。（BSD Now EP300，[817.88-916.16]，L1）
- 总纲9 经验优先：BSDCan 以 hallway track 与动手 hackathon 为经验交流主渠道。（BSD Now EP300，[939.76-960.68]，L1）
- 总纲9 经验优先：从实际删除文件的经验提炼出竞态，并以文件描述符保证同一 inode。（BSD Now EP295，[423.5-430.06]，L2）
- 总纲10 动手者创造历史：funlinkat 由 FreeBSD 开发者动手设计实现并写成博客讲解。（BSD Now EP295，[612.78-697.7]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：Ed Brayden 论证世界模型与预测的失败，强调复杂系统走向并非规划者所能必然掌控。（BSD Now EP633，[1084.22-1603.88]，L2）
- 总纲11 商品是形式主义：总纲11 商品是形式主义：Broadcom 将 Bitnami 免费镜像改造为定价商品，展示开源资产在资本收购后的形式主义化。（BSD Now EP633，[1645.84-2123.00]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：Brian Kernighan 以 C 语言长期推广者身份面对 Rust 崛起，反映技术知识随生态更替而过时的处境。（BSD Now EP633，[2863.88-2966.64]，L1）
- 总纲10 动手者创造历史：ports 生态以“志愿者为主、任何人均可提交 port”的机制让无数贡献者入门，节目强调 25 人以上因写 port 进入 FreeBSD。（BSD Now EP223，[1699.6-1719.64]，L2）
- 总纲5 没有必然性，只有偶然性：对 Docker 的辨析指出便利性常战胜效率，技术采纳受偶然性与习惯支配而非纯理性。（BSD Now EP223，[3344.12-3346.44]，L2）
- 总纲10 动手者创造历史：Cantrill 逐层讲解缓存算法与工程取舍，TJ 试写三期节目笔记促成播客落地，均体现动手者以具体实践而非宣言推动 BSD 生态。（BSD Now EP219，[4392.52-4801.32]，L2）
- 总纲9 经验优先：ARC 的四缓存与幽灵缓存设计来自对实际负载逐出模式的观察，展示工程经验先于理论说明。（BSD Now EP219，[443.98-513.32]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：基本失效模式定理强调复杂系统运行状态由具体故障与补偿关系决定，而非设计意图的必然实现。（BSD Now EP631，[138.14-224.48]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：笔记本作者通过动手排查定位 Nvidia 与 DRM 驱动文件覆盖问题，而非依赖文档结论。（BSD Now EP631，[874.40-908.32]，L1）
- 总纲25 逻辑是形式主义而非世界本身的结构：总纲25 逻辑是形式主义而非世界本身的结构：ZFS 快照的不可变是概念化标签，其元数据实现仍随操作可变，说明概念与实现之间的形式主义距离。（BSD Now EP631，[1324.62-1407.46]，L1）
- 总纲9 经验优先：“scrub of death”被澄清为对 ZFS 数据完整性机制的误解，当事人 Matt Ahrens 的一手说明优先于流传的恐惧叙事，体现经验与考据对传闻的修正。（BSD Now EP200，[3933.54-4042.18]，L2）
- 总纲10 动手者创造历史：ino64 从个人 PEFS 项目到基金会赞助、多人接力完成，显示大型基础设施改进由动手者接力实现，而非单一英雄或抽象计划。（BSD Now EP195，[63.72-500.34]，L2）
- 总纲10 动手者创造历史：个人开发者因自身需要推进无线与存储特性，特性落地依赖具体动手者的持续投入。（BSD Now EP193，[147.78-648.52]，L2）
- 总纲5 没有必然性，只有偶然性：OpenBSD 停止发行 CD 与 LibreSSL 分叉均由 Heartbleed、GPLv3 等具体事件触发，而非抽象规划。（BSD Now EP193，[1277.66-1583.66]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 各发行版分叉后又聚合，zpool checkpoint 等特性先经 hackathon 快速原型，再逐步回上游。（BSD Now EP193，[1810.2-2535.42]，L2）
- 总纲22 知识注定过时：32 位 inode 等既有设计随时间成为瓶颈，知识注定在演进中过时。（BSD Now EP191，[2826.6-3145.38]，L2）
- 总纲13 法律与道德是利益分配：OpenBSD 弃 GCC 选 Clang 是许可证约束与架构支持之间的利益权衡。（BSD Now EP191，[5234.94-5283.66]，L2）
- 总纲10 动手者创造历史：ino64 从 GSoC 学生项目经多人接力维护到主线，体现动手者持续积累的历史过程。（BSD Now EP191，[2993.42-3046.66]，L2）
- 总纲10 动手者创造历史：Mike Muuss 一夜写就 ping 并补齐内核支持，说明关键工具常由具体动手者直接造就。（BSD Now EP190，[4653.46-4908.5]，L2）
- 总纲9 经验优先：OpenZFS 以特性在生产环境运行六个月作为接纳前提，经验验证先于理论采纳。（BSD Now EP190，[3415.94-3437.3]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 特性先在 FreeBSD、illumos 等系统落地测试，再聚合回上游，体现分离聚合循环。（BSD Now EP190，[3396.02-3430.0]，L2）
- 总纲10 动手者创造历史：受访者以退役硬件自建存储系统并迁移海量文件，历史由动手实践者推动。（BSD Now EP189，[4702.86-5620.86]，L1）
- 总纲9 经验优先：对 ZFS 健壮性的判断来自亲身数据恢复与迁移经历，经验先于宣传。（BSD Now EP189，[4462.78-4558.02]，L1）
- 总纲12 科学是形式主义：存储性能与可靠性认知源于可复现的实验、工具与度量，而非主观印象。（BSD Now EP189，[5085.26-5282.2]，L1）
- 总纲25 逻辑是形式主义而非世界本身的结构：pledge 以“使用画像”替代逐系统调用白名单，是把具体操作抽象为形式化类别，再以此约束程序行为。（BSD Now EP170，[1607.48-1642.68]，L3）
- 总纲4 分离聚合是永恒规律：Capsicum 以文件描述符能力把权限拆分为最小单元，子进程只能继承更少能力，体现分离与受限聚合的设计。（BSD Now EP170，[1663.1-1819.74]，L3）
- 总纲10 动手者创造历史：沙箱机制若过于复杂便无人使用，工具的实际采纳取决于动手者的易用体验而非抽象能力高低。（BSD Now EP170，[1709.34-1717.96]，L3）
- 总纲2 历史是形式主义化的非存在：把 46 年 Unix 历史合成为单一 git 仓库，是以后来的版本管理形式重构过去的非存在，历史呈现为形式主义化的构造。（BSD Now EP170，[1855.86-1958.56]，L3）
- 总纲9 经验优先：源码考古修正了 man page 中长期错误的首次出现时间，考据以一手代码与历史经验校正既有知识。（BSD Now EP170，[1955.24-2035.46]，L3）
- 总纲5 没有必然性，只有偶然性：管道从 1969 年提议到 1972 年实现，其间经历了被质疑“缺乏想象”的搁置，具体技术路径由当时的人与偶然条件决定，而非线性必然。（BSD Now EP166，[233.7-308.86]，L3）
- 总纲9 经验优先：McIlroy 以“简单管线连接程序与数据”的经验表述总结工程实践，Unix 的哲学原则从具体动手经验中凝结而成。（BSD Now EP166，[398.14-414.98]，L3）
- 总纲1 一切真历史都是古代史：主持人感叹管道今日被当作理所当然，而忽略其曾有“没有管道的时代”，历史书写把建构产物自然化为恒常存在。（BSD Now EP166，[239.06-247.66]，L3）
- 总纲4 分离聚合是永恒规律：Adhoku 以 jail 做应用级分离、以反向代理做流量聚合，呈现分离与聚合的交替结构，而非单一集中或单一分散。（BSD Now EP166，[1636.04-1775.64]，L3）
- 总纲10 动手者创造历史：MySQL 与 ZFS 的优化均来自动手部署者的具体记录，性能改进由实际操作者而非抽象方案推动。（BSD Now EP166，[566.72-1010.56]，L3）
- 总纲10 动手者创造历史：Dexter 反复把项目史还原为具体的动手者时间：bhyve 得以按期进入 FreeBSD 10 靠的是“有人够笨、肯反复弄坏它并连日执行 build world”（2897.41-2906.52），其本人的贡献是孩子入睡后深夜 11 点至凌晨 2 点的志愿者工时；ZFS 重建工具、SMART 工具与用户组运营同样寄身于无名个人的业余时间，而非机构化的台前叙事。（BSD Now EP149，[3102.92-3113.45]，L1）
- 总纲5 没有必然性，只有偶然性：当事人把个人史与项目史的关键节点全部系于偶发事件：入坑源于 CS101 机房恰好是一台 BSD 4.3 系统的“绝对的偶然”（1704.83-1735.29），Rod Grimes 重返 Release Engineering 则起于大雪改期使其恰好顶替 Dexter 登上 BSDCan 讲台；此处没有必然规律，只有具体人物在具体条件下的相遇与后续的持续经营。（BSD Now EP149，[1704.83-1735.29]，L1）
- 总纲15 文化即形式主义：总纲15 文化即形式主义：Mark Phillips 把营销还原为讲故事的形式，提示技术传播中的品牌叙事同样是形式化构造。（BSD Now EP622，[2702.70-2727.46]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：他以工程师背景亲手测试 ZFS 根镜像并反馈给 Colin Percival，体现使用者参与塑造云镜像。（BSD Now EP622，[1215.20-1244.40]，L1）
- 总纲9 经验优先：总纲9 经验优先：其讲故事方法论基于多年创业与营销一线经验，而非抽象理论推演。（BSD Now EP622，[2553.94-2822.94]，L1）
- 总纲10 动手者创造历史：主持人转述的 OpenBSD 六个月发布节奏（三个月开发、三个月稳定化）与大锁拆解进度（约 220 个系统调用中仅 20 余个脱离 giant lock）呈现技术系统演进的累积形态：SMP 化不依赖一次性蓝图跃进，而由动手者在周期约束下一次次局部解锁累积而成，外界可见的只是每期数十个调用的渐进增量与 long-term 的隐性重排。（BSD Now EP81，[5010.00-5072.28]，L2）

**辨析**：

- 转录将 Klara Systems 误记为 Clara Systems，将 Rubenerd 误记为 Rubinerd 或 Ruben Nerd，正文按业界通行名处理。　[考据脚注] 机构与博客名存在语音转写偏差，须以原文链接核验（BSD Now EP651，[782.30-782.70]，L4）
- 转录中 OpenBSD PA-RISC 移植者被记作 Michael Shaliff，实为 Michael Shalayeff；因语音转写歧义，人名须以代码仓库与邮件列表核验。　[存疑脚注] 人名拼写存在转写歧义，未以 OpenBSD 代码仓库核验（BSD Now EP651，[2700.56-2735.66]，L4）
- bsdgrep 尚未完整支持 GNU 扩展，替换 base 中 GNU grep 的时机与兼容性范围仍待评估。　[存疑脚注] GNU 扩展兼容范围待核实（BSD Now EP373，[394.32-426.70]，L4）
- 转写中“8 秒对 2.5 小时、1150 倍”为作者特定场景的实测数据，主持人亦提示学术上此类极端比值需谨慎看待。　[存疑脚注] 极端比值需结合具体场景理解（BSD Now EP354，[615.14-641.14]，L4）
- Hammer2 紧急模式的“损坏快照”风险与 ZFS 预留空间对比为二手转述，未读 DragonFly 源码验证其具体实现边界。　[存疑脚注] 需对照 DragonFly 提交与手册核实危险程度（BSD Now EP324，[1557.86-1562.90]，L4）
- OpenBSD 体验帖的 RAM 耗尽死机成因不确定是 OpenBSD 本身还是 Vultr 虚拟化环境，作者本人未下定论。　[考据脚注] 环境变量未隔离，因果归属存疑（BSD Now EP324，[691.12-706.72]，L4）
- [存疑脚注] 转写中上一期引述与若干人名拼写（如 Kurt Mojic 等）存在 ASR 噪音，未与 Undeadly 原文核对。　[存疑脚注] 人名拼写与上一期引述未经原文核对（BSD Now EP308，[704.02-710.98]，L4）
- 转录将 Doug Rabson 记作 Doug Rapson、将 Dave Cottlehuber 记作 Dave Cossel-Huber，人名拼写存在转写歧义。　[存疑脚注] 贡献者姓名存在语音转写偏差，须以 FreeBSD Foundation 公告核验（BSD Now EP640，[227.38-290.18]，L4）
- ELIZA 作者名在转录中拼作 Weisenbaum 或 Weisenbalm，通行写法为 Joseph Weizenbaum，须以原始论文核验。　[考据脚注] 人名拼写存在转写偏差，以 Communications of the ACM 1966 年原文为准（BSD Now EP640，[1279.84-1342.08]，L4）
- [存疑脚注] 转写中会议演讲归属与人名拼写（如 Jan Piet Mens、Chuck Tuffli 等）存在 ASR 噪音，未逐一与 BSDCan 议程核对。　[存疑脚注] 演讲归属与人名未经议程核对（BSD Now EP300，[965.4-1043.32]，L4）
- [存疑脚注] 转写将 unlink 描述为最早的系统调用之一、FreeBSD syscall 10，并与 Linux 架构相关编号并列，未逐一核对各平台编号表。　[存疑脚注] 系统调用编号未经各平台编号表核对（BSD Now EP295，[71.12-90.44]，L4）
- 转录将 Klara Systems 记作 Clara、将 Brian Kernighan 记作 Koenigan 或 Kernigan，人名与机构名存在语音转写偏差。　[存疑脚注] 机构与人物名称存在转写偏差，须以原文核验（BSD Now EP633，[2753.12-2784.64]，L4）
- Bitnami 定价在转录中出现 600 亿、60 万与 7.2 万等不一致数字，具体金额须以 AWS Marketplace 与官方公告核验。　[存疑脚注] 价格数字存在转写歧义，未与官方定价页核验（BSD Now EP633，[1666.68-2041.44]，L4）
- 编译器的可调试性结论基于特定版本（GCC 5.2、Clang 3.6 等）的示例，随版本演进可能改变，且文章作者所属公司售卖崩溃报告产品，存在利益关联。　[存疑脚注] 结论依赖具体编译器版本且作者存在商业利益关联（BSD Now EP223，[803.04-822.92]，L4）
- 转录将 Raymond Chen 所属微软博客名称与若干命令参数出现错词，具体规则与命令须以原文核验。　[存疑脚注] 命令与规则细节存在转写歧义，须以原文核验（BSD Now EP631，[132.46-143.76]，L4）
- PeerTube 迁移文章作者在转录中记作 Tom Fatigue，疑为主持人 Tom Jones 或他人，署名须以原文核验。　[存疑脚注] 作者署名存在转写歧义（BSD Now EP631，[1417.28-1432.32]，L4）
- [存疑脚注] DistroWatch 评测中遇到的硬件问题可能由评测者特定的 AMD APU 环境所致，未必能推广为 TrueOS 的普遍缺陷。　[存疑脚注] 单一评测者的硬件结论，需多源交叉验证。（BSD Now EP193，[2963.24-3020.76]，L4）
- [存疑脚注] ino64 的 2007 年起始点与十年开发时长系播客转述，需对照 FreeBSD 提交历史核验。　[存疑脚注] 单一来源转述的时间线，缺提交记录印证。（BSD Now EP191，[2889.64-2908.0]，L4）
- [存疑脚注] 教程安全缺陷研究数据为 2017 年快照，117 处漏洞发现不能代表当时 PHP 生态全貌。　[存疑脚注] 研究样本受 GitHub API 限制，覆盖范围有限。（BSD Now EP191，[4334.74-4354.04]，L4）
- [存疑脚注] ping“一晚写成”与 4.2a BSD 内核 ICMP 支持的时间线系作者自述，需与 4.2BSD 源码与 DARPA 会议记录交叉核验。　[存疑脚注] 单一来源自述，缺少独立档案印证。（BSD Now EP190，[4708.38-4780.22]，L4）
- [存疑脚注] GSoC 项目名单为 2017 年计划，最终是否全部完成须以后续项目报告为准。　[存疑脚注] 计划性名单，验收结果待后续报告。（BSD Now EP189，[585.22-733.18]，L4）
- [存疑脚注] 转写将文章作者记作“Chris Stapps/Christoph”，实际姓名须核验原文署名。　[存疑脚注] 作者姓名须核验。（BSD Now EP170，[1385.34-1497.66]，L4）
- [存疑脚注] 转写将 man page 历史项目作者记作“Seven Johnian”，应为 FreeBSD 提交者 Sevan Janiyan 的误转，须核验。　[存疑脚注] 人名须核验。（BSD Now EP170，[1955.24-2015.8]，L4）
- [存疑脚注] 转写将管道历史中的参与者记作“Thompson and Kennedy”，疑为 Ritchie、Thompson 与 Rudd Canaday 的误转；管道提议与实现时间线须以 McIlroy 原文及 Unix 一手文献复核。　[存疑脚注] 人名与时间线须核验一手文献。（BSD Now EP166，[279.9-308.86]，L4）
- [存疑脚注] 转写将 Hauben 文章托管地记作“farther dot edu”，实际域名无法据此确认，引用时须核验文章来源。　[存疑脚注] 文章来源域名存疑。（BSD Now EP166，[417.88-422.96]，L4）
- fork 的利益结构辨析：八十至九十年代 NetApp、Juniper、Nokia、Isilon 等商业 fork 曾坐享 BSD 红利，十年后却陷入缺 SMP、缺 64 位与新驱动的维护赤字；社区侧则呈现单点悖论——做得差无人可用，做得好反使用户系于可能消失的维护者，Dexter 以 Brexit 喻 fork 的隐性代价，并主张以分支或 branch 而非整体分叉承载实验性工作。　[存疑脚注] 商业 fork 现状、Miros 与 HardenedBSD 定性等均系 Dexter 单一口述，无独立文件佐证；专名在转写中多处失真，引用前须核校。（BSD Now EP149，[5844.31-5948.60]，L4）
- 转写质量辨析：全篇为双音轨交错、时间戳乱序，专名系统性失真——bhyve 一律转作 “Beehive”（2703.93-2712.87），Xen 作 “Zen”，NetBSD 作 “NetVSD”，Kristaps Dzonsons 作 “Christoph Johnson”，Matt Ahrens 作 “Matt Aaron”；各段语义仍完整可辨，但任何人名、项目名与命令名在引用前必须回校原音频与当期节目笔记。　[存疑脚注] 全部专名系转写音译误差，需对照原节目音频与节目 shownotes 逐项核校后方可进入考据链。（BSD Now EP149，[2703.93-2712.87]，L5）
- 访谈为 Mark Phillips 单方自述，其职业时间线与 FreeBSD Foundation 任职细节为单一来源，关键节点须以基金会公告交叉验证。　[存疑脚注] 职业履历为当事人单一来源自述，未与其他公开资料交叉验证（BSD Now EP622，[407.42-944.24]，L4）
- 安全叙事存在单源与转写双重风险：Teo 以 Michal Zalewski 对各操作系统随机性的可视化研究作为其选择 OpenBSD 的关键论据，属当事人回忆中的单一二手引用（1693.70-1715.22）；HardenedBSD 的完整性强制机制仅有主持人转述，其与 NetBSD Veriexec 的类比、SHA-1/SHA-256 哈希清单机制及未来 X.509 ELF 签名计划均未经他源核证，细节可信度有限。　[存疑脚注] 本次转写专名拼写正确（IntegriForce、Veriexec、Michal Zalewski），但机制描述均为主持人单一转述，待与 HardenedBSD 官方公告核证（BSD Now EP81，[3070.24-3159.92]，L4）　[订正：原 失真对照“IntegraForce/VeraExec/Zalewski 姓名拼写存疑”，2026-09-30 SenseAudio 重转核对]
- 听众 Robert 的迁移个案为 2015 年 BSD 桌面生态提供正反两面当事人证词：因 PulseAudio 整合混乱与对 systemd 缺乏信心而离开 Linux，PC-BSD 10.1.1 实现硬件即插即用并带来“回到有理智 shell 的类 UNIX 环境”的体验（3817.50-3847.50）；但无线网卡仅 a/b/g 模式、可查文档仅有三年前 wiki 清单，以及大文件拷贝时的内存占用观感问题（后被澄清为 inactive memory 误读），暴露无线驱动支持与内存统计认知层面的生态短板。（BSD Now EP81，[3772.80-3856.78]，L1）　[订正：原 引文段（3793.64-3835.46）及范围起点 [3793.64]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP651] Pennington J. BSD Now: 651: Spatially aware ZFS[EB/OL]. (2026-02-19)[2026-08-15]. <https://www.bsdnow.tv/651>.
- [BSD Now EP373] Pennington J. BSD Now: 373: Kyle Evans Interview[EB/OL]. (2020-10-22)[2026-08-15]. <https://www.bsdnow.tv/373>.
- [BSD Now EP354] Pennington J. BSD Now: 354: ZFS safekeeps data[EB/OL]. (2020-06-11)[2026-08-15]. <https://www.bsdnow.tv/354>.
- [BSD Now EP324] Pennington J. BSD Now: 324: Emergency Space Mode[EB/OL]. (2019-11-14)[2026-08-15]. <https://www.bsdnow.tv/324>.
- [BSD Now EP308] Pennington J. BSD Now: 308: Mumbling with OpenBSD[EB/OL]. (2019-07-25)[2026-08-15]. <https://www.bsdnow.tv/308>.
- [BSD Now EP640] Pennington J. BSD Now: 640: Cleaning up Hammer[EB/OL]. (2025-12-04)[2026-08-15]. <https://www.bsdnow.tv/640>.
- [BSD Now EP300] Pennington J. BSD Now: 300: The Big Three[EB/OL]. (2019-05-30)[2026-08-15]. <https://www.bsdnow.tv/300>.
- [BSD Now EP295] Pennington J. BSD Now: 295: Fun with funlinkat()[EB/OL]. (2019-04-25)[2026-08-15]. <https://www.bsdnow.tv/295>.
- [BSD Now EP633] Pennington J. BSD Now: 633: Magical Systems Thinking[EB/OL]. (2025-10-16)[2026-08-15]. <https://www.bsdnow.tv/633>.
- [BSD Now EP223] Pennington J. BSD Now: 223: Compile once, debug twice[EB/OL]. (2017-12-06)[2026-08-15]. <https://www.bsdnow.tv/223>.
- [BSD Now EP219] Pennington J. BSD Now: 219: We love the ARC[EB/OL]. (2017-11-08)[2026-08-15]. <https://www.bsdnow.tv/219>.
- [BSD Now EP631] Pennington J. BSD Now: 631: Endorphin Rush[EB/OL]. (2025-09-25)[2026-08-15]. <https://www.bsdnow.tv/631>.
- [BSD Now EP200] Pennington J. BSD Now: 200: Getting Scrubbed to Death[EB/OL]. (2017-06-28)[2026-08-15]. <https://www.bsdnow.tv/200>.
- [BSD Now EP195] Pennington J. BSD Now: 195: I don’t WannaCry[EB/OL]. (2017-05-24)[2026-08-15]. <https://www.bsdnow.tv/195>.
- [BSD Now EP193] Pennington J. BSD Now: 193: Fire up the 802.11 AC[EB/OL]. (2017-05-10)[2026-08-15]. <https://www.bsdnow.tv/193>.
- [BSD Now EP191] Pennington J. BSD Now: 191: I Know 64 & A Bunch More[EB/OL]. (2017-04-26)[2026-08-15]. <https://www.bsdnow.tv/191>.
- [BSD Now EP190] Pennington J. BSD Now: 190: The Moore You Know[EB/OL]. (2017-04-19)[2026-08-15]. <https://www.bsdnow.tv/190>.
- [BSD Now EP189] Pennington J. BSD Now: 189: Codified Summer[EB/OL]. (2017-04-12)[2026-08-15]. <https://www.bsdnow.tv/189>.
- [BSD Now EP170] Pennington J. BSD Now: 170: Sandboxing Cohabitation[EB/OL]. (2016-11-30)[2026-08-15]. <https://www.bsdnow.tv/170>.
- [BSD Now EP166] Pennington J. BSD Now: 166: Pass that UNIX Pipe[EB/OL]. (2016-11-02)[2026-08-15]. <https://www.bsdnow.tv/166>.
- [BSD Now EP149] Pennington J. BSD Now: 149: The bhyve has been disturbed, and a wild Dexter appears![EB/OL]. (2016-07-06)[2026-08-15]. <https://www.bsdnow.tv/149>.
- [BSD Now EP622] Pennington J. BSD Now: 622: Interview with Mark Phillips - Technical Marketing Manager at the FreeBSD Foundation[EB/OL]. (2025-07-31)[2026-08-15]. <https://www.bsdnow.tv/622>.
- [BSD Now EP81] Pennington J. BSD Now: 81: Puffy in a Box[EB/OL]. (2015-03-18)[2026-08-15]. <https://www.bsdnow.tv/81>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- OpenZFS. Project. *Feature Flags Documentation* [EB/OL]. 获取路径：<https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Feature%20Flags>[EB/OL]. 2026. ［DKC-1987→fulltext:6029］
<!-- /dangan-20260908 -->
