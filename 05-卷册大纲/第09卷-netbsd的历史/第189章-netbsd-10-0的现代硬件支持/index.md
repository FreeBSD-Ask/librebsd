---
chapter: 第 189 章
id: CH189
volume: 第09卷-netbsd的历史
---

# 第 189 章 netbsd-10-0的现代硬件支持

## 要点

- NetBSD 10.0（**2024.3.31**）引入对 Apple Silicon M1/M2 的实验性支持，由 Jared McNeill（jmcneill）、Nick Hudson（skrll）、Ryo Shimizu（ryo）等共同推动；移植工作最早可追溯至 2021-08-30（jmcneill“Identify Apple M1 ‘Icestorm’ and ‘Firestorm’…”）
- NetBSD 10.0 硬件支持 commit 记录是研究现代硬件移植的核心史料；Jared McNeill、Taylor R Campbell 等是主要贡献者；考据需对照 CVS commit log 与硬件厂商文档
- pkgsrc 2010-2026 年间的 commit 记录与季度发布说明是研究 pkgsrc 现代演进的核心史料；Joerg Sonnenberger、Thomas Klausner（托马斯·克劳斯纳） 等是主要维护者；考据需对照 CVS commit log 与 pkgsrc-doc 邮件列表
- tainted code 政策公告与邮件列表讨论是研究政策出台过程的核心史料；公告由 Core Team 发布，邮件列表讨论涉及 committer、用户、外部观察者；考据需对照公告原文与邮件列表存档
- NetBSD Foundation 年报与 IRS 990 表是研究 Foundation 治理与财务的核心史料；年报记录 Foundation 治理、资金收支、项目进展；IRS 990 表是法律要求的非营利组织税务披露；考据需对照原始 PDF 与 IRS 数据库

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4003] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4004] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4005] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4006] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲第 10 条——动手者创造历史：Apple Silicon M1/M2 的实验性支持由 jmcneill、skrll、ryo 等动手者在 CVS commit 层面接续完成，pkgsrc 的现代演进亦由 Sonnenberger、Klausner 等维护者的具体劳动推动，现代硬件支持史首先是这些动手者的历史
- 总纲第 9 条——经验优先：移植时间线、发布日期与政策出台过程均以 commit log、官方发布页面与公告原文为断代依据，二手转述（如先前叙事中的 “2024.5” 误传）一律回溯一手记录核验
- 总纲第 22 条——知识注定过时：硬件兼容性列表与内核支持范围随版本迭代迅速过时，本所述支持广度仅为 NetBSD 10.0 时点的快照

## 辨析

- 经 netbsd.duckdb netbsd-src 仓库 commits 表验证：Apple Silicon M1 移植最早可追溯至 2021-08-30（jmcneill），早于 10.0 发布 2024.3.31 约 2 年 7 个月；移植由 jmcneill（2021-2022）、skrll（2022）、ryo（2022）等人接续完成——jmcneill 于 2021-08-30 提交 Apple M1 初始支持（commit db7e12da2c51），skrll 于 2022 年 4-5 月补齐电源域控制器、GPIO、邮箱通信通道、I2C 与 RTKit SMC 等驱动，并自 OpenBSD 移植 Apple silicon NVME 支持（2022-05-07，commit e24a9df7237c），移植时间线延续至 10.0 发布前
- 先前叙事中称“NetBSD 10.0 发布日期 2024.5”系误传——NetBSD 官方发布页面（netbsd.org/releases/formal-10/NetBSD-10.0.html）明确为 2024.3.31；10.0 的实际硬件支持广度需对照硬件兼容性列表核验
- pkgsrc 软件包数量增长在不同来源中存在差异——2010Q1 与 2026Q4 的具体数字需对照原始 release tarball 核验；Sonnenberger 的 commit 量在统计工具中可能被低估
- 政策公告的具体发布日期在不同来源中可能略有差异——需对照 NetBSD 官方页面核验；外部媒体报道可能存在简化或误解
- NetBSD Foundation 年报的连续性在 2010-2026 年间可能存在缺口——部分年份的报告未公开发布；IRS 990 表的具体条目需对照 IRS 数据库核验

## 文献

- NetBSD 10.0 Release Notes；CVS commit log；tech-kern 邮件列表；NetBSD 官方发布历史页面（<https://www.netbsd.org/releases/formal.html>） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2024-2024 年间：29,047 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- pkgsrc CVS 仓库；pkgsrc 季度发布说明；pkgsrc-doc 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2010-2026 年间：892,617 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Core Team 公告；tech-kern 邮件列表；外部媒体报道 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD 特性
- NetBSD Foundation 年报；IRS 990 表；members 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2010-2026 年间：892,617 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD core 邮件列表；Core Team 决议记录；NetBSD Foundation 年度报告 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2010-2026 年间：892,617 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- LWN 文章档案；Phoronix BSD 文章；OSNews NetBSD 评论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD CVS 仓库统计；邮件列表存档；BSDCan/AsiaBSDCon 演讲视频档案 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 10.0 Release Notes；CVS commit log；NetBSD/doc/PLATFORMS；rin. Add nvme(4) and raid(4). netbsd-src 仓库 [DB/OL]. 2020-11-10T08:52:36Z. commit: 571f6efb48f0；riastradh. nvme(4): Add suspend/resume, derived from OpenBSD. netbsd-src 仓库 [DB/OL]. 2021-05-29T08:46:38Z. commit: a6e80066045f；msaitoh. Add VMware AHCI and NVMe. netbsd-src 仓库 [DB/OL]. 2022-02-15T12:01:28Z. commit: 90fc9574253f；skrll. Add support for Apple silicon NVME. Ported from OpenBSD. netbsd-src 仓库 [DB/OL]. 2022-05-07T08:20:03Z. commit: e24a9df7237c；jmcneill. Add initial support for Apple M1. netbsd-src 仓库 [DB/OL]. 2021-08-30T23:26:26Z. commit: db7e12da2c51；skrll. Add support for the power domain controller found in Apple silicon machines. netbsd-src 仓库 [DB/OL]. 2022-04-27T07:55:42Z. commit: 4f480f1af932；skrll. Add a driver for the Apple GPIO controller found in Apple silicon. netbsd-src 仓库 [DB/OL]. 2022-04-27T07:59:18Z. commit: 4989e6f446f2；skrll. Add support for the mailbox that provides a communications channel with additional cores. netbsd-src 仓库 [DB/OL]. 2022-04-27T08:06:20Z. commit: 09966de28c10；skrll. Add a driver for the Apple M1 I2C controller. From OpenBSD. netbsd-src 仓库 [DB/OL]. 2022-05-10T08:05:32Z. commit: 33e6c36315e1；skrll. Add a driver for the Apple RTKit based System Management Controller found on M1 SoCs. netbsd-src 仓库 [DB/OL]. 2022-05-10T08:09:57Z. commit: 11f1e5f671ec；riastradh. Define pci_is_thunderbolt_attached (answer: no). netbsd-src 仓库 [DB/OL]. 2021-12-19T01:48:12Z. commit: edb5cae246b4 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP360（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 追查坏提交的文章介绍用 git bisect 二分定位引入回归的提交，并指出破坏可能来自非直观的依赖变更。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 完成 2020 年第十一届 Core 团队选举，Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Kyle Evans、Mark Johnston、Scott Long、Sean Chittenden、Warner Losh 当选。（BSD Now EP360，[460.69-614.65]，L2）
- NetBSD 在 Pinebook Pro 上以 NetBSD 9 用户态搭配 Current 内核运行，以兼顾二进制包与更好的硬件支持。（BSD Now EP360，[624.57-842.58]，L2）
- pf 状态表存在默认大小限制，FreeBSD 另有 `net.pf.request_maxcount` sysctl 控制单次 ioctl 载入表项数；DragonFly 侧限制为静态内核值。（BSD Now EP360，[1199.40-1404.41]，L2）

**史料**：

- 追查坏提交博文与 git bisect 说明。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 2020 年 Core 团队选举公告，由主持人转述当选名单。（BSD Now EP360，[460.69-614.65]，L2）

**史观**：

- 总纲10 动手者创造历史：FreeBSD 决策由“到场者”作出，主持人与提问者强调社区参与决定项目走向。（BSD Now EP360，[481.5-503.3]，L2）[订正：原 [2452.99-2456.55]（错挂片尾音乐段），2026-10-01 交叉核验订正——总纲10 内容真实出处为 481.5-503.3 段（core 团队九人自荐、社区九票多数当选），片尾 2443.1-2547.8 经两次转写均无语音产出判定为收播曲]
- 总纲4 分离聚合是永恒规律：Core 团队成员更替体现治理层的分离与再聚合。（BSD Now EP360，[460.69-614.65]，L2）

**辨析**：

- DragonFly 的 pf 表限制是静态内核值且未暴露为可调 sysctl，是否需要仿照 FreeBSD 改造仍待确认。 [存疑脚注] DragonFly 侧改造计划待核实（BSD Now EP360，[1360.80-1390.40]，L4）

**文献**：

- [BSD Now EP360] Pennington J. BSD Now: 360: Full circle[EB/OL]. (2020-07-23)[2026-08-15]. <https://www.bsdnow.tv/360>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-912 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-912`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：讲者称 1993 年 4 月 NetBSD 0.8 问世，NetBSD 1.0 也在约 30 年前发布，其本人加入社群即在此时期。（YouTube EPRNHTYV4MI8Y，[80.52-87.87]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-913 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-913`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：NetBSD 的 RISC-V 移植始于 2014 年，讲者亦提及有说法称其始于 2015 年。（YouTube EPRNHTYV4MI8Y，[387.44-398.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1260 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1260`；w172 YouTube 章节路由采纳）

据来源不详讲者口述：OpenBSD 一直在变更 Go 1.4，因为他们在添加特性时不保持向后兼容。（YouTube EPbrhzfN80LzE，[1778.1-1797.1]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-513 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-513`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon 2022〕讲者 Nia Alarie 口述：可在 x86 机器上交叉编译 NetBSD 的 mips 与 arm 目标（YouTube EPfNlxFh43V-w，[128.58-136.49]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1512 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1512`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sleeping Beauty - NetBSD on Modern Laptops, Jörg Sonnenberger〕讲者口述：改造的首要问题是原有的 ACPI 组件架构——他说该版本自“2006 版”以来一直沿用，在新的笔电上遇到不少问题，因为那些机器的固件开始实际使用 ACPI 特性，因而必须更换 ACPI。他紧接着说明他们真正需要的是让 ACPI 在 AMD 64 与 SMP 系统上跑起来。（YouTube EPv9ygBFjGR50，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1513 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1513`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sleeping Beauty - NetBSD on Modern Laptops, Jörg Sonnenberger〕讲者口述：PMF（电源管理框架）是该系统的一枚核心组件之一，由两部分构成——设备接口与事件接口；设备电源管理在设备特定逻辑、总线特定逻辑、设备类别逻辑三层组合上完成，挂起时按类别、设备、总线依次调用。（YouTube EPv9ygBFjGR50，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1514 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1514`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sleeping Beauty - NetBSD on Modern Laptops, Jörg Sonnenberger〕讲者口述：PMF 的系统挂起函数会先检查设备树中是否存在不支持 PMF 的设备，一旦发现就报错并立刻中止整次挂起；换言之，若想拥有 ACPI 挂起，所有驱动都必须实现 PMF，否则只会被抱怨。他说明这是有意为之——宁可报设备名让人禁用，也不要系统因为某个驱动没实现必要钩子而随机崩溃。（YouTube EPv9ygBFjGR50，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1515 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1515`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sleeping Beauty - NetBSD on Modern Laptops, Jörg Sonnenberger〕讲者口述：为了在挂起后仍能取得可用的显示与紧急控制台，他改用软模拟 VESA BIOS 的做法——取自“V2”、而该代码本身又出自“XP86”的模拟代码，数年前被人捐入，可以在内核一侧完成原本需要在用户空间用普通虚拟化能力（仅 86/86 有、64 位没有）才做得到的事。（YouTube EPv9ygBFjGR50，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1696 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1696`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD 会议讲座 BSD ARM Kernel Internals，讲者 Arun Thomas〕讲者口述：他以 BeagleBone Black 作为演示平台，称该平台便利、廉价、性能足够，“所有的 BSD”都支持它，唯独 DragonFly 彼时还没有 ARM 移植。（YouTube EP4gRKA7xoGJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1697 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1697`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD 会议讲座 BSD ARM Kernel Internals，讲者 Arun Thomas〕讲者口述：NetBSD 的 build.sh 允许跨操作系统构建，可在 Linux 或 macOS 等主机上构建系统；FreeBSD 则用 clang 构建系统本体，在 ARM 上亦如此。（YouTube EP4gRKA7xoGJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1698 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1698`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD 会议讲座 BSD ARM Kernel Internals，讲者 Arun Thomas〕讲者口述：FreeBSD 用设备树描述硬件配置，NetBSD 使用自动配置框架；FreeBSD 在 ARM 上另有一个额外的启动加载阶段——u-boot loader，NetBSD 没有这一阶段。（YouTube EP4gRKA7xoGJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1699 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1699`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD 会议讲座 BSD ARM Kernel Internals，讲者 Arun Thomas〕讲者口述：现场问答中他提到 BSD 无法直接沿用 Linux 设备树的障碍在于后者是 GPL 许可；他转述自己多年前与 Linux 内核开发者 Grant Likely 交谈时，对方似乎有意把该部分改为 BSD 许可，但他明言此事“也许可能”、自己并不确定，仍需 FreeBSD 官方出面与 Linux 方面商谈。（YouTube EP4gRKA7xoGJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1885 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1885`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Pierre Pronchery，EuroBSDcon 2012〕讲者口述：自述 NetBSD 此前仅在 Sharp Zaurus 等少数机型上受支持，且现代硬件无驱动，故由其本人自行编写触摸屏驱动；讲者后续说明该触屏连在 USB HID 总线上，并主张用 HID 控制把设备强制切到只发送绝对坐标中断的 mode 2，以优于鼠标模拟模式下的相对坐标。（YouTube EPhsS6MLCMjAI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1886 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1886`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Pierre Pronchery，EuroBSDcon 2012〕讲者口述：指出触屏校准相关的 wscons 校准工具尚未进入 NetBSD 基本系统，其做法是扩展 wscons 以暴露内核中原本已存在的校准值，让使用者可输入一系列采样点参与校准；他同时表示更希望有四点校准并在首次开机时自动完成。（YouTube EPhsS6MLCMjAI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1887 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1887`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Pierre Pronchery，EuroBSDcon 2012〕讲者口述：盘点该 NetBSD 平板的硬件支持现状：摄像头支持、触屏支持但硬件为多点触控而驱动仅单点、调制解调器经 u3g 驱动提供 3G 但存在问题（自述诊断结果为 UDP 可过而 TCP 不通）。（YouTube EPhsS6MLCMjAI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1888 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1888`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Pierre Pronchery，EuroBSDcon 2012〕讲者口述：自述其借该平板项目（含触摸屏驱动与 X11 鼠标驱动的若干补丁）的贡献成为 NetBSD 开发者，并称自己的首个提交曾短暂破坏 USB 键盘驱动、因此此后一律先询问他人。（YouTube EPhsS6MLCMjAI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1925 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1925`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Zachary McGrew 关于将 NetBSD 移植到 RISC-V 的演讲〕讲者口述：在他制作这批幻灯片的两个月前核实，NetBSD 可运行在 57 个不同平台与 16 种不同 CPU 类型之上。（YouTube EP2vQXGomKoxA，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1926 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1926`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Zachary McGrew 关于将 NetBSD 移植到 RISC-V 的演讲〕讲者口述：NetBSD 并不持有 Unix 许可，也未通过 Unix 认证，故他坚持只称其为 Unix-like，以免招致 Unix 工作组诉讼。（YouTube EP2vQXGomKoxA，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1927 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1927`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Zachary McGrew 关于将 NetBSD 移植到 RISC-V 的演讲〕讲者口述：NetBSD 的 RISC-V 移植并非由他起头，而是 Matt Thomas 于 2013 年发起的，他决定接手收拾后续工作，本以为大多已完成、只需清理收尾。（YouTube EP2vQXGomKoxA，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1928 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1928`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Zachary McGrew 关于将 NetBSD 移植到 RISC-V 的演讲〕讲者口述：NetBSD 在 RISC-V 上最终选定 Sv39，这也正是 FreeBSD 与 Linux 当时使用的模式，对应三级页表：512 个 1G 项、512 个 2M 项、512 个 4K 项。（YouTube EP2vQXGomKoxA，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2683 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2683`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Advances in Embedded ARM processors（Dmitri Epshtein，Marvell 软件团队）讲者口述：Marvell 每年出货逾两百万颗跑着 FreeBSD/NetBSD 的芯片，供 Apple、Cisco 等公司使用。（YouTube EPJ-FLykTaHRo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2684 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2684`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Advances in Embedded ARM processors（Dmitri Epshtein，Marvell）讲者口述：Marvell 的开发套件与参考设计板支持若干流行操作系统——FreeBSD、NetBSD、Linux 与 VxWorks，并支持大端与小端。（YouTube EPJ-FLykTaHRo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2685 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2685`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Advances in Embedded ARM processors（Dmitri Epshtein，Marvell）讲者口述：Marvell 不打算只把 plug computer 卖给大客户，而想把它提供给开放社区——Linux 与 NetBSD 开发者，由他们去发现这台机器上能跑什么应用。（YouTube EPJ-FLykTaHRo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2686 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2686`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Advances in Embedded ARM processors（Dmitri Epshtein，Marvell）讲者口述：近年很多公司从 VxWorks 这类老操作系统迁到 BSD 或 Linux；讲者自述五六年前自己的活多在 VxWorks，如今多在 Linux 或 BSD 上。（YouTube EPJ-FLykTaHRo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3001 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3001`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P05C Peripheral side USB support for NetBSD（Hiroyuki Bessho）〕讲者口述：设备可不经重启变换 USB 形态——如手机先作 USB 摄像头连到 PC，再变成 USB 大容量存储乃至打印机；USB 规范并未定义这类转变，故需要为此设计的框架。（YouTube EPlleYSD3defE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3002 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3002`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P05C Peripheral side USB support for NetBSD（Hiroyuki Bessho）〕讲者口述：OpenBSD 多年前即有 USB 外设侧支持，但只有一个单一接口的设备接口（转写音作 XI D，疑为 HID），系 OpenBSD 开发者为特定用途所写。（YouTube EPlleYSD3defE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3003 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3003`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P05C Peripheral side USB support for NetBSD（Hiroyuki Bessho）〕讲者口述：另一系统（疑为 Linux）多年前已有 USB 外设侧支持，其框架提供的特性与讲者的设计目标非常相似。（YouTube EPlleYSD3defE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3004 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3004`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P05C Peripheral side USB support for NetBSD（Hiroyuki Bessho）〕讲者口述：框架按“控制管道能否共享”约束接口组合：FTDI 模拟驱动要独占控制管道，导致 CDC 驱动无法与之组合进同一设备。（YouTube EPlleYSD3defE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
