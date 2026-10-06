---
chapter: 第 75 章
id: CH75
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 75 章 openbsd的加密与固件开放政策

## 要点

- OpenBSD 对固件许可证持严格立场——厂商为节省成本不再在芯片内固化固件、改由操作系统加载后，固件分发许可证冲突显现；OpenBSD 把可自由再分发的固件纳入 base 系统，许可证不兼容的固件经 `fw_update(8)` 从端口单独分发，多数为 WiFi、显卡与 Intel 芯片组（afresh1, 2024）。
- Linux、Windows NT 4.0、Solaris 2.5 与 OpenBSD 的安全比较需辨析——不同项目的安全目标、用户基数、商业模型差异较大；辨析需对照多方原始文档交叉验证；freebsd.duckdb 统计结论 C-05 显示：openbsd-src 总 commit 数 245,904（SQL 查询 `SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`，完整口径见本文件文献字段）
- OpenBSD 2.6/2.7/2.8/2.9 时期（1999-2001）的漏洞响应模型呈现 errata 机制成熟化特征——errata 条目从 2.0/2.1 时期的纯补丁发布演化为 2.7 时期的密集安全修复期（2000 年 10 月多条 SECURITY FIX 条目）与 2.9 时期的末条 errata（2002 年 6 月 25 日第 027 条）。〔订正注：原处“〔待核：原文截断〕”系截断占位，句意已完整，据本文件辨析字段 errata 成熟化路径收束〕
- 从项目史观总纲第 5 条 “没有必然性，只有偶然性”、第 6 条 “和解优于斗争”、第 21 条 “革命与改革是历史方法论的分歧” 三条切入审视，de Raadt 独裁模式、代码审计团队与被疏远贡献者并非 “独裁必然产生安全至上” 或 “独裁必然排斥贡献者” 的目的论结果，而是 1996 年夏天 OpenBSD 启动全代码审计（security.html 一手记载 “We have been a…”〔订正注：原处引文截断，完整原文待回源；审计自 1996 年夏启动之史实见本文件辨析字段〕）。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3826] 卷“第04卷-大分裂与四大bsd的诞生”第 75 章，匹配置信度 folder，原因：folder 第73章

## 史观

OpenBSD 加密与固件开放政策的章级史观——总纲第 4 条“分离聚合是永恒规律”：de Raadt 自 NetBSD 的被逐分离催生了以代码审计为旗帜的 OpenBSD 聚合（详见下方史观映射）；总纲第 10 条“动手者创造历史”：全代码审计（1996 年夏起）、errata 逐版成熟化与 `fw_update(8)`/rtwn(4) 固件许可证谈判均系一线开发者逐项推动的工程实践，而非顶层设计产物；总纲第 13 条“法律与道德是利益分配”（存疑）：固件许可证冲突的实质是厂商成本考量与再分发自由之间的利益分配——可自由再分发者纳入 base、许可证不兼容者经 `fw_update(8)` 单独分发，边界划定本身即利益结构的映射。〔订正注：原字段“(待人工回填)”系占位，按本章 75.11-75.14 各节史观/辨析字段主题回填〕

## 辨析

- OpenBSD 的严格许可证立场与硬件厂商的省钱考量构成持续冲突——rtwn(4)/urtwn(4) 固件经 kevlo 联系 Realtek 去除专利条款后移入 base，是许可证谈判成功的少数案例；多数不兼容固件仍须经 `fw_update(8)` 分发（afresh1, 2024）。
- 比较的具体维度在不同叙事中略有差异——需对照多方原始文档交叉验证；【0 信任原则·commit 量不等于质量】C-05 openbsd-src 245,904 与 C-03 freebsd-src 444,203 的量级差异不等于两项目代码质量或安全性的差异——OpenBSD 的安全审计文化（自 1996 年夏天起全代码审计）使单次 commit 可能包含更密集的审计修正，commit 量与安全质量不能直接互推。
- errata 机制从 2.0 至 2.9 的成熟化路径须逐版本对照 errata 页面核实——2.0 时期 errata 为纯补丁发布，2.7 时期出现密集安全修复期，2.9 末条 errata 为收尾，3.x 起引入架构性防御，各阶段边界须以 errata 条目数量与内容为据而非史家主观分期；hackathon 对漏洞响应的具体贡献须对照 hackathons.html 记录与 errata 时间线。
- 考据过程留痕——【查证来源】项目史观总纲第 5 条原文经 据原文第 25 章 第 11 行 Read 一手核验，第 6 条原文经第 13 行 Read 一手核验，第 21 条原文经第 25 行 Read 一手核验；OpenBSD security.html 经 <https://www.openbsd.org/security.html> WebFetch 一手核验，“We have been a…”（security.html 引文于原处截断，完整原文待回源）

## 文献

- afresh1, 2024《Why rewrite fw_update(8)?》BSDCan 2024 演讲

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1992-1995 年间：770 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- 四个项目 1995-1996 年安全文档；安全对比研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；本项目。freebsd.duckdb 数据分析报告：描述性统计与推断性统计 [R/OL]. 2026.（统计结论 C-05 openbsd-src 总 commit 数 245,904，SQL 查询 `SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`；统计结论 C-03 freebsd-src 总 commit 数 444,203；统计结论 C-14 openbsd-src 变点 Pettitt 2001-01 / BUISHAND 2017-09，Python 脚本自实现 Pettitt + BUISHAND R 检验 10,000 次 Monte Carlo；统计结论 C-12 freebsd-src 变点 1999-08 双检验一致 p < 0.001） ［A］
- OpenBSD 2.6/2.7/2.8/2.9 errata 页面；OpenBSD hackathons.html；OpenBSD security.html；OpenBSD 3.x errata 页面；本项目。原材料/研究/bsd 漏洞史/版本周期/openbsd-2.x.md；本项目。bsd_commits.duckdb 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］
- 项目史观总纲第 5 条、第 6 条、第 21 条（据原文第 25 章）；OpenBSD security.html [EB/OL]. <https://www.openbsd.org/security.html>；OpenBSD hackathons.html [EB/OL]. <https://www.openbsd.org/hackathons.html>；OpenBSD goals.html [EB/OL]. <https://www.openbsd.org/goals.html>；openbsd.duckdb openbsd-src 仓库 deraadt 首 commit 与累计 commit 量 ［A］

### 史观映射

> de Raadt 被逐出 NetBSD——一封邮件通知，没有上诉，没有告别。分离从来不是和平的，但分离之后必有新的聚合：OpenBSD 从 NetBSD 的废墟中诞生，以代码审计为旗帜。de Raadt 的天才加速了 OpenBSD 的崛起——PF、OpenSSH、全代码审计方法论，每一项都是他驱动下的产物。但同一种不妥协的气质，既是他创造的动力，也是他冲突的根源：与 NetBSD 的决裂只是开始，此后与 FreeBSD 的隔阂、与 DARPA 的冲突、与社区新人的摩擦，都是同一种结构的反复。天才不总是灾厄，但天才的边界往往就是灾厄的起点

---

## 第 75.15 不同时期人员的采访录（详见 [采访录.md](采访录.md)）

> 第 75 章采访录子节，覆盖 1996-2001 年 OpenBSD 安全文化奠基的当事人陈述，含 Theo de Raadt（西奥·德·若特） OpenBSD 安全文化奠基演讲、Bob Beck OpenBSD 安全响应工程两则，每则采访按 5 字段深化，考据过程另见 `07-事实核查记录/`〔订正注：原 `原材料/研究/考据记录/` 路径全项目不存在，已改指实际考据目录〕。

## 第 75.16 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)；该节文件尚未落盘，待回源）

〔订正注：本段原与史观映射散文连排为巨行塌陷，旧章号 29.15/29.16 已按现行第 75 章重挂为 75.15/75.16，并恢复换行〕

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP428、BSD Now EP164、BSD Now EP16、BSDTalk EP82（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- OpenBSD 于 1995 年 10 月作为 NetBSD 分叉起步，其默认安装长期仅报告两个远程漏洞，被描述为默认安全的系统。（BSD Now EP428，[135.74-145.1]，L2）
- OpenBSD 率先随系统搭载 IPsec 等强密码学，并因此卷入美国出口管制，这是其基地设于加拿大的原因之一。（BSD Now EP428，[145.1-160.3]，L2）
- OpenBSD 形成发现漏洞后不再单点修补，而是在全树范围内寻找并修复同类模式的代码审计文化。（BSD Now EP428，[164.94-184.78]，L2）
- OpenBSD 是 OpenSSH、OpenBGPD、PF、OpenNTPD、IKED、Mandoc 与 LibreSSL 等广泛使用组件的上游来源。（BSD Now EP428，[247.2-262.74]，L2）[订正：原 OpenSMTPD、IKE，2026-09-30 SenseAudio 重转核对]
- DragonFly vkernel 类似 jail 但虚拟化整个内核，新支持 copy-on-write 镜像模式，使多个 vkernel 可从同一镜像启动，运行时变更保留在各自层而不写回原镜像文件，近似 UnionFS。（BSD Now EP164，[176.8-266.7]，L2）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]
- 若将镜像设为只读，多个 vkernel 共享同一镜像且互不修改；对镜像的改动被保留在分离的变更层中。（BSD Now EP164，[226.9-266.7]，L2）[订正：原 [226.9-239.82]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 在 Raspberry Pi 3 上的有限支持已提交 head，多数驱动可用上游，但 RNG 的 call-out 模式失效、SMP 尚未完成、VCHIQ 驱动存在仅对 ARM 成立的假设，且尚无 HDMI 支持。（BSD Now EP164，[328.18-412.58]，L2）
- OpenBSD 自成立起一直使用 CVS，与 NetBSD 及早期 FreeBSD 相同；本期公布位于 github.com/openbsd 的官方只读镜像，含源码与 ports 等仓库。（BSD Now EP164，[3816.62-3848.04]，L2）
- OpenBSD GitHub 镜像的 exporter 稳定性尚无保证，若基于该分支做 fork，数据可能以不同哈希重新导出而使 rebase 困难。（BSD Now EP164，[3902.24-3915.58]，L2）
- Libreboot.org 发布以开源 BIOS 引导 OpenBSD 或 LibertyBSD 的文档，含 USB 镜像制作、Grub 配置与排障，但 Libreboot 加 Grub 尚不支持全盘加密。（BSD Now EP164，[3926.18-4004.28]，L2）
- 主持人评论认为随着 EFI 增长，开源系统越发依赖闭源固件甚至迷你操作系统来引导，Libreboot 针对的正是最后一块不受控制的区域。（BSD Now EP164，[4007.8-4038.48]，L1）
- Josh Paetzel 亲述协助 FreeBSD Foundation 调试 Supermicro 服务器的 PXE 引导：串口看似故障，实为系统启动停止，改为静态 DHCP 预留后正常引导，根因仍未完全查明。（BSD Now EP164，[1637.4-1860.0]，L1）[订正：原 [1641.44-1928.76]，2026-09-30 SenseAudio 重转核对]
- Josh Paetzel 认为 ZFS 中延迟敏感负载宜用 RAID10，容量优先与非延迟敏感负载宜用 RAIDZ/RAIDZ2；其团队运行过 200 至 300 盘的 RAIDZ2 与 RAID10 池且未因硬件故障丢失池。（BSD Now EP164，[2049.82-2168.1]，L1）[订正：原 [2049.82-2203.34]，2026-09-30 SenseAudio 重转核对]
- Josh Paetzel 以客机比喻 ZFS：非常安全，多数故障被冗余吸收，但一旦突破临界即彻底崩溃，且没有理解 RAID-Z 布局的数据恢复工具。（BSD Now EP164，[2434.64-2497.76]，L1）
- Josh Paetzel 指出 ZFS 自 2011 年开源后五年间约 45% 的代码为新写，并认为文件系统需要商业实体与专业工程资源支撑。（BSD Now EP164，[2522.4-2603.72]，L1）
- 教程演示在 FreeBSD 与 OpenBSD 上执行全盘加密安装；FreeBSD 侧以脚本化方式处理 GELI 与 ZFS 根文件系统，OpenBSD 侧则结合加密根分区与引导加载器。（BSD Now EP16，[4289.6-4418.6]，L2）
- 新闻讨论 FreeBSD Ports 将引入季度稳定分支（2014Q1），快照维护三个月，期间仅接受安全修复、构建与运行时修复及基础设施变更。（BSD Now EP16，[4690.7-4766.9]，L2）
- PackageNG 社区讨论类似 pkgsrc acceptable licenses 的许可证过滤，使用户可按许可证决定是否允许安装软件包，并考虑提供查看已装包许可证的命令。（BSD Now EP16，[4496.2-4585.9]，L2）
- 入门史与驱动者画像：OpenBSD 开发者约八年，自 1997 或 1998 年底起；入伙缘于 OpenBSD 2.3 在其老 Sun 4/300——25 MHz、32 MB 内存、9U VME 机箱——上无法启动而 2.2 正常，他定位出致病补丁并提交，随后收到素未谋面的 Theo de Raadt 主动给账号的邮件；此后写遍各类设备驱动，刻意回避磁盘设备以求存储稳定，多涉串口、网卡、网络层、显示与 USB。（BSDTalk EP82，[63.64-117.92]，L1）
- Theo de Raadt 的通才角色：其早期专注 SPARC port——尤以尚为 NetBSD 核心开发者时期为甚——但真正价值在于对树中各处皆有深入了解的通才能力，随兴趣转向树的其余部分；如今仍非常活跃，正不断催促 Jason 支持众多 SPARC64 机器与部分企业系统内置的 Cassini 以太网芯片——凡不带 Broadcom、HME 或 Gem 的机器皆有之，目前尚不支持。（BSDTalk EP82，[157.92-228.78]，L1）
- SPARC64 port 维护实况：过去五年 Jason 任该 port 维护者——覆盖自 Ultra 1 起步到当代 Enterprise 机器的 64 位产品线，甚至有人尝试在 Enterprise 15000 上运行、接近启动而未竟，是其须回归的项目；Sun 每台新机都藏着 quirk 或需要新驱动，必须在新机问世时尽早取得实机；他的名字出现在大量版权声明中，只因某种怪异设备仅存于约两台机器——沮丧与乐趣并存的 port 经历。（BSDTalk EP82，[139.92-476.98]，L1）
- 当前硬件缺口与调试现实：手头一台 Ultra 3 至为关键——该机指令缓存已支持而数据缓存未支持；缓存调试几乎必须物理接触机器，因为电源键使用频繁，上次 hackathon 的受害机五天内经历约六十次上电循环，机器会进入拒绝关机的状态。（BSDTalk EP82，[519.42-558.18]，L1）
- 厂商文档的混合图景：Intel 存储部门的 RAID 卡态度优秀、曾多次向 OpenBSD 开发者寄送实卡；Intel 网络组三年前连 FXP 十兆百兆网卡都不给文档——那并非新技术，人们要文档主要是为研究其 bug——如今才终于开始放文档；Broadcom 从未向任何人放过文档，除非签下卖身式 NDA；台湾以太网芯片厂商乐于发布他们所谓的文档——洋泾浜英语、质量欠佳但足以起步；再辅以 Linux、FreeBSD 甚至 OpenSolaris 的源码找线索；Sun 内部亦不一致——UltraSPARC III 处理器文档易得，而 PCI 主桥（Schizo、Tomatillo）文档近乎不可能获取，形成处理器可跑代码却碰不到设备的断裂。（BSDTalk EP82，[242.52-356.66]，L1）
- Cassini 文档与 NDA 立场：Cassini 以太网的文档同样不可得，Linux 阵营能支持它只因 David Miller 等人签下 NDA 让渡了权利——这既不是 Jason 个人也不是 OpenBSD 项目整体愿意接受的选项。（BSDTalk EP82，[359.18-376.70]，L1）
- Sun 硬件收藏与平台迁移：工作站曾为装有三块帧缓冲的 UltraSPARC 2——不算最快但够用——约八个月前转向 Macintosh；家中实验室散落大量 Sun 机器（因搬家仍处拆箱状态）：Ultra 1、2、5、30、60、80，Enterprise 220 与极为沉重的 Enterprise 4500，Blade 1000 与 2000——Ultra 10 不过是竖立机箱里的 Ultra 5。（BSDTalk EP82，[388.86-447.94]，L1）
- 业余无线电与 APRS 实践：新近参与分组无线电以支持自动位置报告系统 APRS——业余无线电社区周期性广播设备或电台位置，兼作带确认机制的慢速消息系统（半可靠、丢包可知），常用 1200 波特且收发切换须等待电台循环；UNIX 下主要应用 Xastir 接收他台位置、配合 GPS 显示相对位置与地图，华盛顿海军陆战队马拉松曾用于医疗站间传递选手信息；另涉数字模式无线电——RTTY 以 45.45 波特运行 Baudot 五位编码、以移位序列切换字母与数字符号档，PSK31 与 GMFSK 则面向键盘对键盘对话，类比是没有可靠性的 AIM 加上信号衰落；相关应用已移植 OpenBSD、待修整入 ports，Xastir 因几何、地图与 GPS 依赖成为可怕工程。（BSDTalk EP82，[576.54-807.30]，L1）
- 编辑器与桌面哲学：编辑器无宗派——长坐同一处迭代用 Emacs、在树中飞检索用 vi，而用得最多的是 OpenBSD 树中的 Emacs 克隆 MG；曾在 NFR 工作时为求各平台统一编辑器而把 MG 移植到 Linux on PowerPC、FreeBSD 4.8、macOS 等，其中 FreeBSD 反而是较难的移植目标而 Linux 尚好；图形环境不用桌面管理器——那只会浪费屏幕空间——用 TWM 且懒于安装他物；shell 用系统自带的 ksh，bash 中他喜欢的特性已并入其中；尽量使用每个发行版自带的工具。（BSDTalk EP82，[809.18-923.28]，L1）
- AMD64 IOMMU 未竟项目：IOMMU 概念源自 SPARCstation 1 与 2 时代——让地址空间受限的设备经由窗口访问全部主存，Sun 系统因所用以太网芯片只能寻址二十或二十四位而发明页映射表；AMD64 平台亦内置同类表；他一年前开始的工作已躺在 OpenBSD 树中未完成——不缺硬件只缺时间——该机制可让 32 位 PCI 设备经小窗口窥见 64 位地址空间，并公开征集协助。（BSDTalk EP82，[927.78-1010.32]，L1）

**史料**：

- Peter Hansteen 的 What every IT person needs to know about OpenBSD 系列文章，作为本期 OpenBSD 历史叙述的主要二手来源。（BSD Now EP428，[70.74-76.44]，L2）
- DragonFly vkernel copy-on-write 镜像模式的功能说明。（BSD Now EP164，[176.8-266.7]，L2）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 提交者关于 Raspberry Pi 3 支持的博客。　[存疑脚注] 博客作者全名须核验。（BSD Now EP164，[328.18-412.58]，L2）
- OpenBSD 官方只读 GitHub 镜像（github.com/openbsd）。（BSD Now EP164，[3828.2-3915.58]，L2）[订正：原 [3816.62-3915.58]，2026-09-30 SenseAudio 重转核对]
- Libreboot.org 关于以开源 BIOS 引导 OpenBSD/LibertyBSD 的文档。（BSD Now EP164，[3926.18-4004.28]，L2）
- Josh Paetzel 访谈自述（iXsystems，FreeNAS/TrueNAS 相关运维经验）。（BSD Now EP164，[985.8-2820.6]，L1）[订正：原 [1600.0-2610.0]，2026-09-30 SenseAudio 重转核对]
- 本期提及 NetBSD 在 Marvell Kirkwood 平台（插头式迷你服务器）上的使用文章，以及 FreeBSD Foundation 年终募款与开发者差旅资助。（BSD Now EP16，[548.6-570.2]，L2）
- 该期留存的一手史料线索：OpenBSD 2.3 的 Sun 4/300 启动 bug 及其定位补丁；SPARC64 port 对 Ultra 系至 Enterprise 系的覆盖与 E15K 尝试记录；Ultra 3 数据缓存与 Cassini 支持的树内缺口；MG 编辑器的多平台移植（Linux on PowerPC、FreeBSD 4.8、macOS）；Xastir、GMFSK、gPSK31 等业余无线电应用的 OpenBSD 移植；厂商向开发者寄送的 Intel RAID 实卡。（BSDTalk EP82，[811.46-878.34]，L1）

**史观**：

- 总纲10 动手者创造历史：OpenBSD 以代码审计与全树范围修复确立安全实践，体现动手者在具体工程中塑造项目文化。（BSD Now EP428，[164.94-191.78]，L2）
- 总纲13 法律与道德是利益分配：美国出口管制把加密技术纳入法律约束，迫使 OpenBSD 调整基地布局，体现法律与道德作为利益分配工具的现实效应。（BSD Now EP428，[145.1-160.3]，L2）
- 总纲4 分离聚合是永恒规律：vkernel 以只读镜像为基底、以 copy-on-write 层承载差异，多个实例分离运行又共享同一映像，呈现分离与聚合的结构。（BSD Now EP164，[176.8-266.7]，L3）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]
- 总纲3 不存在进步，只有权力再分配：Libreboot 试图把引导固件的控制权从闭源厂商转移给用户，是围绕系统控制权的权力再分配。（BSD Now EP164，[4007.8-4038.48]，L3）
- 总纲9 经验优先：ZFS 的可靠性来自 Sun 时期大量工程投入与后续商业资源，专业经验沉淀为可用的复杂系统。（BSD Now EP164，[2522.4-2603.72]，L3）
- 总纲25 逻辑是形式主义而非世界本身的结构：ZFS 以冗余与校验把故障可能性压到极低，但剩余风险以极端方式集中爆发，安全是形式化边界内的构造。（BSD Now EP164，[2434.64-2497.76]，L3）
- 总纲22 知识注定过时：OpenBSD 长期使用 CVS，在 Git 成为主流后以镜像方式补足浏览体验，旧工具随生态变化而需要新形式。（BSD Now EP164，[3816.62-3900.24]，L3）
- 总纲10 动手者创造历史：全盘加密教程把复杂的 GELI/ZFS 流程固化为可重复脚本，使普通用户得以动手部署并复现。（BSD Now EP16，[4331.5-4418.6]，L2）
- 总纲13 法律与道德是利益分配：NDA 是个人利益与项目原则之间的分配选择：David Miller 等人以让渡权利换取 Cassini 文档，从而 Linux 获得支持；Jason 与 OpenBSD 项目整体拒绝同一交易，宁缺驱动不签卖身契约——文档的开放与否由此不是技术可得性问题，而是不同主体间利益分配格局的产物。（BSDTalk EP82，[359.18-376.70]，L1）
- 总纲9 经验优先：SPARC64 port 的推进方法是把每台新机器尽快拿到手——quirk 与驱动缺口只能来自实机经验，文档缺失之下经验成为唯一路径；从 Sun 4/300 的启动 bug 定位到 Ultra 3 缓存调试的六十次上电循环，技术史在这一 port 上由反复上电的双手写成。（BSDTalk EP82，[450.54-466.46]，L1）

**辨析**：

- “默认安装仅两个远程漏洞”为 OpenBSD 项目长期自述口径，其统计口径与时间范围需与官方安全公告逐条核对。　[存疑脚注] 远程漏洞计数为项目自述，统计边界需对照 OpenBSD 官方安全公告确认。（BSD Now EP428，[138.94-145.1]，L4）
- [存疑脚注] 转写未给出 DragonFly vkernel copy-on-write 功能的具体提交与作者，须核验 DragonFly 仓库与提交记录。　[存疑脚注] COW 功能提交与作者须核验。（BSD Now EP164，[176.8-266.7]，L4）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]
- 教程中的加密安装步骤由主持人演示并录制，涉及 FreeBSD 9.2/10 与 OpenBSD 特定版本的实现细节，属于演示与转述而非当事人一手史料。（BSD Now EP16，[3.7-27.0]，L2）[订正：原 [0.0-10.2]，2026-09-30 SenseAudio 重转核对]
- E15K 接近启动、受害机五天六十次上电循环、Intel 网络组前后行为等细节均为当事人口述、无独立佐证；Cassini 所在的具体机型他本人亦不能确指，仅以 Solaris 下的 CE 网卡机型圈定范围；转写术语与人名多处失真（UltraSPARC、Schizo、Tomatillo、IOMMU、Xastir、Baudot 等按通行拼写校正）。[存疑脚注] 硬件细节与厂商行为均为单一来源陈述。　[存疑脚注] 机型与厂商行为细节无第三方佐证（BSDTalk EP82，[481.06-514.18]，L4）

**文献**：

- [BSD Now EP428] Pennington J. BSD Now: 428: Cult of BSD[EB/OL]. (2021-11-11)[2026-08-15]. <https://www.bsdnow.tv/428>.
- [BSD Now EP164] Pennington J. BSD Now: 164: Virtualized COW / PI?[EB/OL]. (2016-10-19)[2026-08-15]. <https://www.bsdnow.tv/164>.
- [BSD Now EP16] Pennington J. BSD Now: 16: Cryptocrystalline[EB/OL]. (2013-12-18)[2026-08-15]. <https://www.bsdnow.tv/16>.
- [BSDTalk EP82] Backman W. BSDTalk: 82: bsdtalk082 - OpenBSD Developer Jason Wright[EB/OL]. (2006-11-08)[2026-08-27]. <https://archive.org/details/bsdtalk082>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

