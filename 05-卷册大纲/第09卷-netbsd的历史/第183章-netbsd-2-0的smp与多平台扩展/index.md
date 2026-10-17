---
chapter: 第 183 章
id: CH183
volume: 第09卷-netbsd的历史
---

# 第 183 章 NetBSD 2.0 的 SMP 与多平台扩展

## 要点

- NetBSD 2.0 分支（约 2003 年底切出）引入基于 FreeBSD SMPng 移植的细粒度锁机制，逐步替换 4.x 时代的 Giant Lock〔存疑：经 2026-09-12 联网复核，FreeBSD SMPng 系 FreeBSD 基于 BSD/OS 5.0 实现的自有项目（Lehey USENIX 论文），NetBSD 2.0 官方公告未提 SMPng 移植，2005 年官方演示材料仍载内核 Big lock 局限——2.0 是否引入细粒度锁并替换 Giant Lock 未能确证，须对照源码核验〕；2.0 正式发布于 2004.12，标志 NetBSD 进入真正的 SMP 时代
- NetBSD 2.x/3.x 时期 SMP 性能基准在 2-8 核机器上较 FreeBSD 5.x/6.x 落后，但在嵌入式 ARM/MIPS 多核场景占优；硬件支持广度（ports 数量）是同期 BSD 中最广；NetBSD 的跨平台能力不仅体现在 src 仓库的 ports 数量上，亦体现在 pkgsrc 跨平台包管理系统的规模上——pkgsrc 作为 NetBSD 的跨平台包管理系统，可独立于 NetBSD 引导并运行于 Solaris、Linux、macOS 等多个平台
- FreeBSD 5.x（2003-2005）推进 SMPng 与 Giant Lock 细化，5.2（2004）实验性引入 ULE 调度器；NetBSD 2.x/3.x 移植 SMPng 但调度器仍以 4BSD 为基础〔存疑：经 2026-09-12 联网复核，FreeBSD SMPng 系 FreeBSD 基于 BSD/OS 5.0 实现的自有项目（Lehey USENIX 论文），NetBSD 2.0 官方公告仅载为 i386、SPARC、PowerPC 新增 SMP 支持并改进 Alpha/VAX，未提 SMPng 移植，2005 年官方演示材料仍载内核 Big lock 局限——“移植 SMPng”未能确证，是否共享代码须对照 CVS 历史核验〕，反映两项目不同的工程节奏
- Linux 2.6（2003.12）引入 O(1) 调度器与抢占式内核，SMP 扩展性快速领先；Solaris 10（2005.1）引入 ZFS 与 DTrace，企业级 SMP 成熟度最高；NetBSD 2.x/3.x 在 SMP 上保守，但在可移植性上独树一帜

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3998] 卷“第09卷-netbsd的历史”第 183 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4009] 卷“第09卷-netbsd的历史”第 183 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_3989] 卷""第 183 章，匹配置信度 0.9，原因：〔存疑：经 2026-09-12 实查 references_fulltext.duckdb chapter_matches 表，id=3989 行的 primary_volume 字段确为空串、match_reasoning 为空，本行为库数据如实投影，须库侧修复生成逻辑后重灌，非本文件可改〕

## 史观

- 总纲第 5 条——没有必然性，只有偶然性：NetBSD 2.x/3.x 在 SMP 路线上以 4BSD 调度器为基础渐进推进，系具体工程条件下的偶然取舍，并非通向多核时代的必然进步序列
- 总纲第 8 条——本体论上各方平等：FreeBSD 5.x/6.x、Linux 2.6、Solaris 10 与 NetBSD 2.x/3.x 的同期 SMP 路线在本体论上平等并立，性能与功能差异系路线取舍与资源约束的表现，非先进与落后之分

## 辨析

- 经 netbsd.duckdb 验证，NetBSD 2.0 发布日期为 2004.12.09（commit message 明确记载 “NetBSD 2.0 was released on December 09, 2004”）；SMPng 移植的具体完成度需考据，2.0 是否已完全移除 Giant Lock 需对照源码核验。L1.1.1 查询的 commit 量数据存在 GitHub 镜像滞后风险——netbsd-src 为 GitHub 镜像（主仓为 Mercurial **hg.NetBSD.org**），2003-2004 年 commit 量可能不完整
- 基准测试的硬件配置差异需对照原始测试脚本核验，不得直接采信结论。L1.1.1 查询的 commit 量数据存在 GitHub 镜像滞后风险——netbsd-src 为 GitHub 镜像（主仓为 Mercurial **hg.NetBSD.org**），2004-2008 年 commit 量可能不完整；commit 量持续下降与 “性能落后” 叙事方向一致，但 commit 量下降不等于性能下降
- SMPng 是否为两项目共享代码需对照 CVS 历史核验，部分叙事夸大了共享程度
- 三项目同期 SMP 性能比较需在同一硬件上测试，跨硬件比较易误导

## 文献

- NetBSD 2.0 Release Notes [EB/OL]. (2004-12-09). <https://www.netbsd.org/releases/formal-2.0.html>（原始链接失效，互联网档案馆无存档）；FreeBSD SMPng 设计文档 [EB/OL]. <https://docs.freebsd.org/en/books/arch-handbook/smp/>；Jason Thorpe、Frank van der Linden tech-smp 邮件列表帖 [EB/OL]. <https://mail-index.netbsd.org/tech-smp/>；netbsd.duckdb 数据分析·宏观趋势统计.md §L1.1.1（netbsd-src 2003-2004 年度 commit 量）、§L2.3.1.smp（netbsd-src SMP 相关 commit 2005）、§SubTask 2.1（统计结论 C-04：netbsd-src 总 commit 数 773,683） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。
> 2003-2004 年间：221,740 次提交。

- Phoronix NetBSD/FreeBSD 性能基准测试 [EB/OL]. <https://www.phoronix.com/>；NetBSD/doc/PLATFORMS 文件 [EB/OL]. <https://github.com/NetBSD/src/blob/trunk/doc/PLATFORMS>（原始链接失效，互联网档案馆无存档）；tech-perform 邮件列表 [EB/OL]. <https://mail-index.netbsd.org/tech-perform/>；netbsd.duckdb 数据分析·宏观趋势统计.md §L1.1.1（netbsd-src 2004-2008 年度 commit 量）、§L2.3.1.smp（netbsd-src SMP 相关 commit 2005-2008）；外部基准-StackOverflow-PackageEcosystem.md 第 3.2 节（统计结论 E-15：netbsd-pkgsrc 总 commit 数 1,222,307） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。
> 1993-2026 年间：1,999,408 次提交。

- FreeBSD 5.x Release Notes [EB/OL]. <https://www.freebsd.org/releases/>；NetBSD 2.x/3.x Release Notes [EB/OL]. <https://www.netbsd.org/releases/formal.html>；freebsd-arch 邮件列表存档 [EB/OL]. <https://lists.freebsd.org/archives/freebsd-arch/> ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1993-2026 年间：1,294,851 次提交。

- Linux 2.6 Release Notes [EB/OL]. (2003-12-17). <https://kernelnewbies.org/LinuxVersions>；Solaris 10 Release Notes [EB/OL]. (2005-01-31). <https://www.oracle.com/solaris/solaris10/>；Molnar I. O(1) Scheduler [EB/OL]. <https://www.kernel.org/doc/Documentation/scheduler/sched-design-CFS.txt> ［A］

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1555 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1555`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Adventures in porting a Wayland Compositor to NetBSD and OpenBSD by Jeff Frasca 演讲〕讲者口述：把其 C 代码在 OpenBSD 上编译测试是极有价值的——若维护 C 项目，OpenBSD 会对一切内存管理失误毫不姑息，直接让程序崩溃，从而暴露出大量缺陷。（YouTube EPoo_8gnWQ4xo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1556 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1556`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Adventures in porting a Wayland Compositor to NetBSD and OpenBSD by Jeff Frasca 演讲〕讲者口述：BSD 使用 wscons——它为PC 启动到命令行模式时的基础命令行终端（视频／终端仿真）系统而建，仅处理显示器、键盘与鼠标三类设备。（YouTube EPoo_8gnWQ4xo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1557 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1557`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Adventures in porting a Wayland Compositor to NetBSD and OpenBSD by Jeff Frasca 演讲〕讲者口述：在混合键盘布局场景下，NetBSD 完全不做键位翻译——控制台上一个键盘可用、另一个键盘输出乱码，至少是“一致地坏”，而 OpenBSD 的对应行为在他处才出问题。（YouTube EPoo_8gnWQ4xo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2062 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2062`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Portable Hotplugging: NetBSD 的 uvm hotplug(9) API 开发 演讲（讲者 Cherry G. Mathew）〕讲者口述：目前所有 BSD 都沿用一套非常简单的实现来登记机器上的 RAM，本质上是一个静态数组——即著名的 vm_phys_max；当大量 RAM 出现、或 x86 的物理地址映射高度碎片化时，这个定义便成了被反复讨论的对象（YouTube EPK0Sry5laFvs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2063 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2063`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Portable Hotplugging: NetBSD 的 uvm hotplug(9) API 开发 演讲（讲者 Cherry G. Mathew）〕讲者口述：该项目的构想源于虚拟机需要在运行时动态增删内存——当下只有一个气球驱动（balloon driver）充当从虚拟机取走内存的权宜之计，而至少 NetBSD 上不存在把内存加回来的途径（YouTube EPK0Sry5laFvs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2064 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2064`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Portable Hotplugging: NetBSD 的 uvm hotplug(9) API 开发 演讲（讲者 Cherry G. Mathew）〕讲者口述：改用红黑树之后，维护内存段不再有多套并存策略，代码杂乱也随之下降；候选方案中曾有一类队列做法，但因兼有两种方案的缺点被排除，讲者遂倾向采用本就现成可用的 RB tree（YouTube EPK0Sry5laFvs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2065 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2065`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Portable Hotplugging: NetBSD 的 uvm hotplug(9) API 开发 演讲（讲者 Cherry G. Mathew）〕讲者口述：集成阶段主要由 Nick Hudson 与 Amaya 协助完成大部分代码，这场本可能失控的移植实际上只花约两周就完成大部分平台——70 个架构的规模令讲者印象深刻（YouTube EPK0Sry5laFvs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2230 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2230`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Porting NetBSD to the LatticeMico32 open source CPU 演讲，讲者 Yann Sionneau〕讲者口述：他为该软核 CPU 增加了内存管理单元，使流水线内只管理虚拟地址、经翻译后以物理地址访问主存，从而让 BSD 得以在该 CPU 上运行。（YouTube EPnpmbdZRLHJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2231 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2231`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Porting NetBSD to the LatticeMico32 open source CPU 演讲，讲者 Yann Sionneau〕讲者口述：该 MMU 的设计是出于实现简便与简单的考量：TLB 不会直接去取页表，硬件内不做页表遍历，即所谓无硬页表遍历的实现。（YouTube EPnpmbdZRLHJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2232 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2232`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Porting NetBSD to the LatticeMico32 open source CPU 演讲，讲者 Yann Sionneau〕讲者口述：该 CPU 没有原子指令，讲者读 NetBSD 内核源码后采用“可重启原子序列”技术实现基本 compare-and-swap，而后者正是互斥锁与自旋锁等实现的核心。（YouTube EPnpmbdZRLHJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2233 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2233`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Porting NetBSD to the LatticeMico32 open source CPU 演讲，讲者 Yann Sionneau〕讲者口述：因该 CPU 的 TLB 是软件管理的，NetBSD 中已有现成代码，讲者只取用 src/uvm 下的 pmap 文件即可，pmap 子系统只需补写入口函数 pmap_bootstrap，其余部分直接可用——讲者将其列为本次移植中最令人意外的省事之处。（YouTube EPnpmbdZRLHJ8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2472 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2472`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alistair Crooks 讲可移植 iSCSI initiator〕讲者口述：NetBSD 世界自 2006 年初起就有一个 iSCSI target，它可移植到 POSIX 系统，讲者本人还在业余时间把它移植到了 Windows XP。（YouTube EPMiZY7PMu7Ic，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2473 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2473`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alistair Crooks 讲可移植 iSCSI initiator〕讲者口述：他为 NetBSD 向制定 SCSI 标准的 T10 注册了厂商资格，因而可以在 target 与 initiator 中使用 netbsd 字符串，用于 iSCSI 的 IQN（internet qualified name）内部命名。（YouTube EPMiZY7PMu7Ic，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2474 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2474`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alistair Crooks 讲可移植 iSCSI initiator〕讲者口述：他们的第一次测试是在这个 initiator 之上跑 NetBSD 的构建脚本（转写音作 buildup shell，指构建编译器、全部工具与用户态库的那套 build 脚本），测试成功完成，性能令他惊讶；测试机是 8 GB、8 路的 amd64，最终性能与本地原生性能的差距在百分之一以内（转写作 within five of a%，并在上下文中给出 4750 对 4725 的耗时），他自承可能有缓存效应（转写作 cash effects）。（YouTube EPMiZY7PMu7Ic，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2475 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2475`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Alistair Crooks 讲可移植 iSCSI initiator〕讲者口述：RumpFS（转写音作 refuse）构建在 puffs 之上，提供与 FUSE 相同的用户态文件系统 API，且自 2007 年起与 FUSE 编译兼容，任何 FUSE 文件系统重新编译后都可在 RumpFS 下运行。（YouTube EPMiZY7PMu7Ic，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
