---
chapter: 第 179 章
id: CH179
volume: 第09卷-netbsd的历史
---

# 第 179 章 netbsd-5.0架构重构与社区演进

## 要点

- NetBSD 5.0（**2009.4.29**）引入由 Andrew Doran（安德鲁·多兰） 设计的新 SMP 调度器，采用每 CPU 运行队列与工作窃取算法，取代 4.x 的全局锁机制；新调度器支持多核负载均衡与优先级继承，使 NetBSD 在 4 核至 32 核机器上获得显著性能提升
- NetBSD 5.0 的架构设计文档散布于 tech-kern 邮件列表、CVS commit 信息与 NetBSD Foundation 年度报告；Andrew Doran、YAMAMOTO Takashi、Joerg Sonnenberger 等开发者的设计帖是核心一手史料；源码考据需对照 CVS 历史与 commit log 的署名、时间戳
- pkgsrc commit 记录是研究 2005-2009 年 pkgsrc 演进的核心一手史料；Joerg Sonnenberger 作为 pkgsrc 长期维护者提交数千次 commit；季度发布说明（pkgsrc-2008Q1 等）记录每季度的软件包数量增长与重要变更
- NetBSD Foundation 2005-2009 年度报告记录了 Foundation 治理、资金收支、项目进展与 committer 变更；编程之夏导师分配、学生项目列表、最终评估是编程之夏史料核心；两类文档需对照原始 PDF 与邮件列表通知核验
- NetBSD Core Team 决议记录是研究 2005-2009 年社区治理的核心史料；core 邮件列表存档（部分公开，部分私密）；Core Team 决议涉及新 committer 加入、自动退休、技术路线争议等；考据需对照 core 邮件列表与公开宣布

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4086] 卷“第09卷-netbsd的历史”第 179 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4087] 卷“第09卷-netbsd的历史”第 179 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Doran 新调度器与 FreeBSD Jeff Roberson 的 ULE 2.0（2007.5 引入 FreeBSD 7.0）的关系存在叙事分歧——Doran 在邮件列表中提及参考 ULE 但强调独立性，需对照源码 diff 核验；新调度器的性能基准数据在第三方测试中差异较大，需查 Phoronix/BSD Insights 等早期基准。经 netbsd.duckdb netbsd-src 仓库 b
- CVS 与后续 Git 迁移过程中的元数据保真度问题——部分早期 commit 在迁移后丢失 author 字段；邮件列表存档在 mail-index.netbsd.org 与 MaraRepos 等多镜像中存在版本差异
- pkgsrc 软件包数量统计在不同来源中差异较大——2005Q1 与 2009Q4 的具体数字需对照原始 release tarball 核验；Sonnenberger 的 commit 量在统计工具中可能被低估（部分 commit 以 typos 或 docs 形式提交）
- NetBSD Foundation 2005-2009 年度报告的连续性存在缺口——部分年份的报告未公开发布，需对照邮件列表年度总结补全；编程之夏 2005 年首届的学生项目记录在 Google 官方档案中部分缺失
- Core Team 决议的私密性使考据困难——部分决议未公开宣布，需对照 CVS commit 的 author 变化推断；Core Team 成员名单在不同来源中可能略有出入

## 文献

- NetBSD CVS 仓库归档；mail-index.netbsd.org；NetBSD Foundation 年度报告 2008/2009 ［B］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2009-2009 年间：93,511 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- pkgsrc CVS 仓库；pkgsrc 季度发布说明；tech-pkg 邮件列表年度总结 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2009 年间：468,780 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Foundation 年度报告 2005-2009；Google 编程之夏 官方档案；NetBSD Foundation 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2009 年间：468,780 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD core 邮件列表；Core Team 决议记录；NetBSD Foundation 年度报告 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD Core Team 与 committer
- Linux Weekly News 档案；Slashdot BSD 相关帖；OSNews NetBSD 评论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD CVS 仓库统计；邮件列表存档；BSDCan 演讲视频档案 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD 发布工程（Manuel Bouyer 等）
- NetBSD 5.0 Release Notes；Kengo NAKAHARA MPLS 设计邮件；BSD MPLS 实现比较研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Netcraft Web Server Survey 2005-2009；IDC 服务器操作系统市场报告；Distrowatch 统计页面［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2009 年间：183,657 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- netbsd.duckdb netbsd-src 仓库 commits 表；CVE-2011-0014、CVE-2011-0539 NVD 条目 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP210（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 该期报道 NetBSD 微内核式重实现的进展：底层是仅约 1.3 万行代码的微内核，只处理中断、消息传递、低级调度与硬件细节；内存管理、文件系统、分页交换与设备驱动几乎全部作为用户态进程运行，并受 MMU 保护，被认为是一个可能真正可用的微内核。（BSD Now EP210，[136.60-353.82]，L2）
- 关于 Mac 快速联网的分析指出，Mac 通过记住已知网络、假设旧 IP 仍有效并先自行配置再后台完成 DHCP 握手，可在链路建立后约 10 毫秒开始联网，远快于依赖用户态 DHCP 客户端的 Android 设备。（BSD Now EP210，[379.94-963.36]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：NetBSD 微内核重实现把整块内核拆分为用户态进程并经由消息传递聚合，是分离与聚合在操作系统架构层面的体现。（BSD Now EP210，[136.60-353.82]，L2）

**文献**：

- [BSD Now EP210] Pennington J. BSD Now: 210: Your questions, part I[EB/OL]. (2017-09-06)[2026-08-15]. <https://www.bsdnow.tv/210>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-259 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-259`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者提到曾在考虑把 Rump Kernel 移植到 MINIX 3（quote‘MINIX 3's we've been thinking about maybe porting’，语气为‘maybe’）。（YouTube EP5GdP84VqKyk，[2838.57-2844.44]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-258 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-258`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：NetBSD Rump Kernel 当时能在 DragonFly 与 Solaris 上运行。（YouTube EP5GdP84VqKyk，[820.49-828.519]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1364 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1364`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kristaps Dzonsons《Process Isolation for NetBSD and OpenBSD》演讲〕讲者口述：实现例（instance）隔离的核心思路是取消内核里唯一的全局进程表，改为每个实例各持一张进程表；进程结构体中保存一张所属表的手柄，做进程查找时先经该手柄取得本实例的表，再按 pid 定位进程结构，从而在数据结构层面保证不同实例之间无从看见彼此的进程。（YouTube EPJaVnNllZxn4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1365 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1365`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kristaps Dzonsons《Process Isolation for NetBSD and OpenBSD》演讲〕讲者口述：把 FreeBSD jail 一类做法称为功能性隔离（functional isolation）——每遇到一处进程可见性冲突点就要施加一次“我能否看见它”的检查，而检查点是否被穷尽无从确知；讲者举 compat Linux 走不同路径、以及未来版本 FreeBSD 直接读进程哈希表为例，说明遗漏一处即可被绕过。（YouTube EPJaVnNllZxn4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1366 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1366`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kristaps Dzonsons《Process Isolation for NetBSD and OpenBSD》演讲〕讲者口述：按实例拆分进程表在承载数千实例时性能急剧下降；把进程表尺寸固定变小仍未能解决，于是讲者退而只维护一张进程表、以全局哈希开关在“每实例分表”与“单表”之间取舍，自称这是权宜做法。（YouTube EPJaVnNllZxn4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1367 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1367`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kristaps Dzonsons《Process Isolation for NetBSD and OpenBSD》演讲〕讲者口述：该项目的首次公开发布在 2007 年，基于讲者本地分支上 fork 出的整个 NetBSD 3.1 内核，原型体量庞大。（YouTube EPJaVnNllZxn4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1738 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1738`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDcon 2008 Kristaps Džonsons 演讲《Logical Resource Isolation in the NetBSD Kernel》〕讲者口述：讲者介绍的项目名为 MOL，自述已开发数月（称三到六个月左右，且不确定），其做法是把用户态“复数化”——在同一台主机内并存多个用户环境。（YouTube EPc63VneyQI-k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1739 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1739`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDcon 2008 Kristaps Džonsons 演讲《Logical Resource Isolation in the NetBSD Kernel》〕讲者口述：讲者定义“操作系统实例复数化系统”（operating instance multiplicity system）的“策略”即冲突区域的处理方式；MOL 的策略是特意设计为可以证明隔离成立，而不是仅凭巧妙技巧假装存在。（YouTube EPc63VneyQI-k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1740 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1740`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDcon 2008 Kristaps Džonsons 演讲《Logical Resource Isolation in the NetBSD Kernel》〕讲者口述：讲者称 FreeBSD jail 是最知名的此类实现，并称 OpenBSD 的 zones 与之极为类似、Linux VServer 亦属此类。（YouTube EPc63VneyQI-k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1741 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1741`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDcon 2008 Kristaps Džonsons 演讲《Logical Resource Isolation in the NetBSD Kernel》〕讲者口述：讲者称 Xen 不在其讨论范围，因 Xen 复数化的是内核而非操作系统实例；而 DragonFly BSD 的 vkernel 与 Kimu 同为操作系统实例复数化。（YouTube EPc63VneyQI-k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1985 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1985`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The pivot_root system call for BSD systems (NetBSD) / Adrian Steinmann 于 EuroBSDcon 2012〕讲者口述：讲者描述 FreeBSD 实现中的差异点：FreeBSD 2 的 /dev 是 devfs，pivot 后它会随之下移，须在这个系统调用内部把 /dev 重新挂回新 root，否则紧随其后的访问都会找不到 /dev 而失败；NetBSD 因无 devfs 无需此步，但 NetBSD 另有 current dot root 只读变量需另行更新（讲者称这部分尚未做完）。（YouTube EP6itw0i2OHwM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1986 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1986`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The pivot_root system call for BSD systems (NetBSD) / Adrian Steinmann 于 EuroBSDcon 2012〕讲者口述：讲者说明 pivot_root 源自 Linux，这或许是 FreeBSD 一直没有它的部分原因；同时长期内也确实没有实际需求，因为既有 init 阶段的切换机制已足够。（YouTube EP6itw0i2OHwM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1987 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1987`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The pivot_root system call for BSD systems (NetBSD) / Adrian Steinmann 于 EuroBSDcon 2012〕讲者口述：讲者提出 FreeBSD jails 场景下 pivot_root 的可行性问题：jail 内无法直接对整个系统做 pivot_root（会把世界颠倒地让他人落到自己 root 之下），但 jail 可以在自己的小天地里做自己那份 pivot_root——这是他视为有吸引力的方向。（YouTube EP6itw0i2OHwM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1988 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1988`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The pivot_root system call for BSD systems (NetBSD) / Adrian Steinmann 于 EuroBSDcon 2012〕讲者口述：讲者说明其在 NetBSD 的实现取向：新增一个与 Linux 兼容的系统调用，并将其放入内核可加载模块（而非改动 mount 系统调用），这也是他借机学习内核可加载模块的过程。（YouTube EP6itw0i2OHwM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2707 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2707`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔How to break long term compatibility in NetBSD（Joerg Sonnenberger）讲者口述：NetBSD 在兼容性上迄今只有一次有意的 ABI 破坏——废除调度器激活（scheduler activation，曾用于线程实现）；因问题太多且修不完而退役并给程序提供了替代。（YouTube EPQ7QhD8XryKY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2708 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2708`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔How to break long term compatibility in NetBSD（Joerg Sonnenberger）讲者口述：最后一次 libc 大版本跳变发生在 NetBSD 1.4，距今已逾十年；此后的 ABI 变更持续累积，好在可以显式定义——头文件里有各版结构体与原型。（YouTube EPQ7QhD8XryKY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2709 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2709`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔How to break long term compatibility in NetBSD（Joerg Sonnenberger）讲者口述：为直接创建带版本的符号，需扩展链接器使其能直接指定符号可见性，而不必借 assembler 名与宏间接命名。（YouTube EPQ7QhD8XryKY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3005 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3005`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔NFS scripting with Lua（Lourival Viera Neto）〕讲者口述：让操作系统可脚本化的动机：给操作系统更多灵活性、帮助用户满足新需求并配置内核子系统、允许非内核开发者改变内核行为，还能用脚本语言原型化新特性。（YouTube EPLoJ4Bg2P0nc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3006 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3006`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔NFS scripting with Lua（Lourival Viera Neto）〕讲者口述：讲者自 2008 年起做内核脚本环境（先在 Linux 上，后经 Google Summer of Code 项目移植到 NetBSD），其后由（转写音作 mark Palmer）者在 Lua 之上为 NetBSD 建了新基础设施；今年开始做 NPF Lua。（YouTube EPLoJ4Bg2P0nc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3007 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3007`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔NFS scripting with Lua（Lourival Viera Neto）〕讲者口述：选 Lua 作内核脚本语言：它生来既是可嵌入又是可扩展语言，只是一个 ISO C 库、几乎 freestanding、极易移植、不依赖操作系统，内核内占用极小。（YouTube EPLoJ4Bg2P0nc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3008 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3008`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔NFS scripting with Lua（Lourival Viera Neto）〕讲者口述：SSH 版本检测示例只有 12 行 Lua 代码，在 100 兆网络接口上实测开与不开脚本吞吐都约 96 兆，无可感开销。（YouTube EPLoJ4Bg2P0nc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
