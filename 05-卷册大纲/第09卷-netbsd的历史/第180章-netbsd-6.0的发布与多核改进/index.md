---
chapter: 第 180 章
id: CH180
volume: 第09卷-netbsd的历史
---

# 第 180 章 netbsd-6.0的发布与多核改进

## 要点

- NetBSD 6.0（**2012.10.17**）继续由 Andrew Doran（安德鲁·多兰） 改进的线程调度器，引入更细粒度的优先级继承与多核负载均衡；6.0 的 SMP 改进特别针对 8 核以上机器优化；调度器设计延续 5.0 渐进式路径，未引入革命性重构
- NetBSD 6.0 Release Notes 与 CVS commit log 是研究 6.0 开发的核心史料；6.0 发布周期约 3 年 6 个月（5.0 于 2009.4.29 发布，6.0 于 2012.10.17 发布），commit 记录反映开发节奏；考据需对照多源档案交叉验证。经 netbsd.duckdb netbsd-src 仓库 commits 表 message_subject L〔存疑：本句于数据源截断，关键词查询结果待回源补全〕
- pkgsrc 2012Q3（2012.7）作为 6.0 同期发布版本，改进跨平台软件包管理；引入对 AIX、Solaris、HP-UX 等非 BSD 系统的更好支持；改进 二进制软件包构建基础设施；pkgsrc 跨平台能力让 NetBSD 工具链在非 NetBSD 系统上获得存在感，体现 BSD 反向影响线
- 2012 年操作系统围绕“多核扩展性”竞争：FreeBSD 9/10 与 Linux 3.x 在 x86 多核成熟，NetBSD 6.0 实现 SMP 性能跃升，OpenBSD 5.x 稳守安全，Windows 8/Server 2012 强化企业特性；NetBSD 6.0 以“多核 + 极致可移植”在 BSD 家族中独特定位。
- NetBSD 6.x 周期末期 OpenSSL 漏洞群持续积累，为 2014 年 Heartbleed（CVE-2014-0160）的爆发埋下伏笔——CVE-2013-0169（OpenSSL 1.0.1d 至 1.0.1e 升级中的多漏洞修复，christos 2013-02-12 commit `a79346cf8ad8cc6c7ff13916fedccb6b679da6ae`，commit〔存疑：本句于数据源截断，后续著录待回源补全〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3697] 卷“第09卷-netbsd的历史”第 180 章，匹配置信度 folder，原因：folder 第178章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 6.0 调度器相比 5.0 的具体改进幅度在不同来源中差异较大——部分基准显示显著提升，部分显示微小改进，需对照同硬件测试核验。经 netbsd.duckdb netbsd-src 仓库 branches 表验证：origin/netbsd-6-0 与 origin/netbsd-6-1 的 commit_date 均为 2018-07-02（前后相差仅 1 分钟），反映 6.x 系列分支在 2018.7〔存疑：本句于数据源截断，分支尾活动推断待回源补全〕
- 先前叙事中称 ~~“6.0 发布周期长达 3 年（2009.12 5.0 至 2012.10 6.0）”~~ 系误传——5.0 实际发布日期为 **2009.4.29**（非 2009.12），6.0 实际发布日期为 **2012.10.17**，实际间隔约 3 年 6 个月；发布说明的完整性需考据——部分细节可能滞后于实际代码；3 年 6 个月周期的具体里程碑（feature freeze 等）
- pkgsrc 2012Q3 的具体改进内容需对照发布说明核验；跨平台支持的“改进幅度”在不同来源中可能存在差异；pkgsrc 在 AIX/Solaris 上的实际采用率缺乏权威统计
- 不应以单维度性能评判——NetBSD 6.0 的可移植性价值在 ARM/MIPS 等平台凸显。
- NetBSD Heartbleed 修复 commit `ed81493569fefce792d08aa976144cfb15a2d23d` 的修复日期（2014-04-08）与 Heartbleed 公开披露日期（2014-04-07）相差 1 天，反映 NetBSD 的快速响应，但该修复是否同步至所有稳定分支（netbsd-6、netbsd-5）须对照 pullup commit 核验；CVE

## 文献

- NetBSD 6.0 史料分析；tech-release 邮件列表；NetBSD 官方发布历史页面（<https://www.netbsd.org/releases/formal.html>）；NetBSD Project. note NetBSD 6.0 release. netbsd-src [DB/OL]. 2012-10-17T18:30:33Z. ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2012-2012 年间：80,326 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- pkgsrc 2012Q3 发布说明；tech-pkg 邮件列表；pkgsrc 跨平台文档 ［A］
- FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-075] By the numbers: ZFS Performance Results from Six Operating Systems and Their Derivatives（Michael Dexter，2019）<https://papers.freebsd.org/2019/vbsdcon/dexter-zfs_performance_results/>FreeBSD 社区论文：[FP-2019-021] Cross Platform Parallel Regression and Performance Testing of, and with OpenZFS, FreeBSD and bhyve（Michael Dexter，2019）<https://papers.freebsd.org/2019/bsdcan/dexter-cross_platform_parallel_regression_and_performance_testing/>FreeBSD 社区论文：[FP-2019-039] Virtualization of BSD Using the QNX Hypervisor（Quentin Garnier，2019）<https://papers.freebsd.org/2019/bsdcan/garnier-virtualization_of_bsd_using_the_qnx_hypervisor/>FreeBSD 社区论文：[FP-2019-066] KLEAK - Practical Kernel Memory Disclosure Detection（Thomas Barabosch，2019）<https://papers.freebsd.org/2019/fosdem/barabosch-kleak/>FreeBSD 社区论文：[FP-2019-081] OpenZFS: Best Filesystem for every OS（Allan Jude（艾伦·裘德），2019）<https://papers.freebsd.org/2019/jude-openzfs-everyos/>FreeBSD 社区论文：[FP-2018-018] A Public-Key Trust Infrastructure for FreeBSD（Eric McCorkle，2018）<https://papers.freebsd.org/2018/bsdcan/mccorkle-a_public-key_trust_infrastructure_for_freebsd/>FreeBSD 社区论文：[FP-2018-019] Adding verification to FreeBSD loader（Simon Gerraty，2018）<https://papers.freebsd.org/2018/bsdcan/gerraty-adding_verification_to_freebsd_loader/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>

### 史观映射

> NetBSD 6.x 时代是“在虚假中寻找仅存的真实”的工程实践——当 Linux 以 cgroups/Docker/Kubernetes 席卷数据中心，NetBSD 在 ARM 嵌入式与 Apple Silicon 移植中寻找自己的生态位；tainted code 政策是 NetBSD 对 AI 时代“真实性困境”的率先回应——在 AI 生成代码模糊了“作者”与“真实性”的边界时，NetBSD 以最保守的姿态守护代码的“真”；然而 NetBSD 社区规模的持续萎缩与硬件支持的滞后，让“寻找仅存的真实”本身成为一种会者定离的修行——开发者在不被看见的角落维护着数十种平台的移植；39.2 **rump kernel 与 anykernel 创新（2010-2026）**——rump kernel 的设计理念：将 NetBSD 内核子系统作为用户态库运行；anykernel 架构的工程实现：内核代码无需修改即可在用户态运行；rump kernel 在云原生时代的应用：unikernel、用户态文件系统、网络栈测试；与 Linux unikernel（MirageOS、OSv）的对比；rump kernel 对 NetBSD 工程哲学的形式主义化：可移植性的极致延伸 ｜ **子-子节**：39.2.1 rump kernel 的设计理念与 anykernel 架构；39.2.2 rump kernel 的工程实现与核心技术；39.2.3 rump kernel 在云原生时代的应用（unikernel、用户态文件系统）；39.2.4 与 Linux unikernel（MirageOS、OSv）的对比及哲学反思 ｜ **子-子-子节**：39.2.1.1 Antti Kantee 的 rump kernel 概念提出与设计哲学考据；39.2.1.2 anykernel 架构：内核代码无需修改即可在用户态运行的工程实现；39.2.1.3 rump kernel 与微内核/宏内核之争的第三条路径辨析；39.2.1.4 anykernel 对 NetBSD 可移植性哲学的形式主义化延伸；39.2.2.1 rump kernel 的 hypercall 接口与 POSIX 调用转换机制；39.2.2.2 buildrumpsh.sh 等工具链设计与 rumpctrl 控制工具；39.2.2.3 rump kernel 内核子系统分解：VFS、网络栈、设备驱动；39.2.2.4 工程实现 commit 记录与设计文档考据；39.2.3.1 rump kernel 作为 unikernel 在云原生场景的部署探索；39.2.3.2 用户态文件系统（fuse-rump）与网络栈测试应用；39.2.3.3 rump kernel 在嵌入式开发与硬件模拟中的应用；39.2.3.4 rump kernel 应用的实际部署案例与社区反馈考据；39.2.4.1 MirageOS（OCaml）与 OSv 的 unikernel 哲学对比；39.2.4.2 rump kernel 复用 NetBSD 内核代码与 MirageOS 重新实现的路径差异；39.2.4.3 Linux unikernel 生态对 rump kernel 项目的边缘化影响；39.2.4.4 rump kernel 对 NetBSD 工程哲学的形式主义化反思；39.3 **NetBSD 与日本社区关系史（2010-2026）**——日本 NetBSD 用户组（Japan NetBSD Users’Group）的历史与活动；Ryo Shimizu、Jun Ebihara（海老原純） 等日本核心贡献者的长期贡献；日本学术机构（东京大学、京都大学）与 NetBSD 的合作；日本社区对 NetBSD 国际化的贡献：文档翻译、会议组织、ARM 移植；日本是 NetBSD 最活跃的区域社区之一 ｜ **子-子节**：39.3.1 日本 NetBSD 用户组的历史与活动；39.3.2 Ryo Shimizu、Jun Ebihara 等日本核心贡献者；39.3.3 日本学术机构与 NetBSD 的合作；39.3.4 日本社区对 NetBSD 国际化的贡献 ｜ **子-子-子节**：39.3.1.1 Japan NetBSD Users’Group（JNUG）的成立与组织结构考据；39.3.1.2 JNUG 年度会议与 NetBSD BoF 历届活动；39.3.1.3 日本 NetBSD 用户组邮件列表与文档资源；39.3.1.4 JNUG 与 NetBSD Foundation 的正式关系辨析；39.3.2.1 Ryo Shimizu 的 ARM 移植贡献与长期维护角色；39.3.2.2 Jun Ebihara 的 NetBSD/evbarm 与嵌入式贡献；39.3.2.3 日本核心贡献者的代际更替与会者定离；39.3.2.4 日本贡献者 commit 记录与邮件列表考据；39.3.3.1 东京大学与 NetBSD ARM 移植的学术合作；39.3.3.2 京都大学、东京工业大学等机构的 NetBSD 研究项目；39.3.3.3 日本学术机构对 NetBSD 嵌入式应用的贡献；39.3.3.4 学术合作史料与论文档案考据；39.3.4.1 日文文档翻译与 NetBSD 国际化（i18n）基础设施；39.3.4.2 AsiaBSDCon 与日本 BSD 会议的组织角色；39.3.4.3 日本社区对 NetBSD 源码注释与 man 页面翻译的贡献；39.3.4.4 日本作为 NetBSD 最活跃区域社区的史学定位辨析；39.4 **NetBSD 资金危机与 Foundation 现代化（2010-2026）**——2010 年代 NetBSD Foundation 多次资金紧张事件；Foundation 资金来源多样化尝试：个人捐赠、企业赞助、Google 编程之夏；与 FreeBSD Foundation（资金充裕）/OpenBSD Foundation（2014 危机）的对比；资金问题对项目可持续性的影响：开发者流失、基础设施维护困难；NetBSD Foundation 现代化改革：理事会结构调整、透明度提升 ｜ **子-子节**：39.4.1 2010 年代 NetBSD Foundation 资金紧张事件；39.4.2 Foundation 资金来源多样化尝试；39.4.3 与 FreeBSD/OpenBSD Foundation 资金状况的对比；39.4.4 资金问题对项目可持续性的影响及现代化改革 ｜ **子-子-子节**：39.4.1.1 2010 年代 NetBSD Foundation 资金紧张的标志性事件考据；39.4.1.2 基础设施维护成本（镜像、构建集群、源码仓库）的压力；39.4.1.3 开发者个人志愿投入的不可持续性辨析；39.4.1.4 资金紧张事件邮件列表与 Foundation 公告考据；39.4.2.1 个人捐赠计划与 PayPal/Stripe 捐赠通道；39.4.2.2 企业赞助计划的建立与早期赞助商考据；39.4.2.3 编程之夏资金对 NetBSD 项目的影响；39.4.2.4 资金来源多样化的效果评估与局限；39.4.3.1 FreeBSD Foundation 企业赞助模式（Netflix、Juniper、NetApp 等）；39.4.3.2 OpenBSD Foundation 2014 年资金危机与社区响应；39.4.3.3 三大 BSD Foundation 资金结构的横向对比；39.4.3.4 资金差异对项目可持续性的影响分析；39.4.4.1 资金不足对开发者留存与硬件支持广度的限制；39.4.4.2 Foundation 理事会结构调整与透明度提升改革；39.4.4.3 现代化改革对 NetBSD 项目长期可持续性的影响；39.4.4.4 Foundation 年报、IRS 990 表与现代化改革文档考据；39.5 **NetBSD 与 Darwin/macOS 关系史（2010-2026）**——Apple 早期借用 NetBSD 网络栈与用户态工具的历史；macOS XNU 内核与 NetBSD 代码共享的演变；Apple 商业成功与 NetBSD 贡献的失衡：Apple 未回馈或回馈有限；BSD 许可证下的“被白嫖”困境：法律允许但道德存疑；Darwin/macOS 关系的哲学反思：可移植性的意外受益者 ｜ **子-子节**：39.5.1 Apple 早期借用 NetBSD 网络栈与用户态工具的历史；39.5.2 macOS XNU 内核与 NetBSD 代码共享的演变；39.5.3 Apple 商业成功与 NetBSD 贡献的失衡及“被白嫖”困境；39.5.4 Darwin/macOS 关系的哲学反思 ｜ **子-子-子节**：39.5.1.1 NeXTSTEP/OpenStep 时期对 NetBSD 用户态工具的借用；39.5.1.2 Mac OS X 10.0（2001）的 BSD 用户空间与 NetBSD 关系；39.5.1.3 Apple 对 NetBSD 网络栈与套接字实现的采用；39.5.1.4 Apple 早期 BSD 借用的源码考据与版本对应；39.5.2.1 XNU 内核的 BSD 子系统与 NetBSD 代码共享范围；39.5.2.2 Apple libkern、libproc 等 NetBSD 衍生组件的演变；39.5.2.3 macOS 用户态工具（如 ping、netstat）的 NetBSD 起源；39.5.2.4 XNU 与 NetBSD 代码共享演变的源码对照；39.5.3.1 Apple macOS 商业成功与 NetBSD 项目未获回馈的失衡；39.5.3.2 BSD 许可证下 Apple 合规但不回馈的法律与道德张力；39.5.3.3 NetBSD 社区对 Apple“白嫖”的回应与态度演变；39.5.3.4 与 FreeBSD-Apple 关系（FreeBSD 5.x 借用）的对比；39.5.4.1 BSD 许可证“允许但不要求回馈”的哲学代价；39.5.4.2 可移植性的意外受益者：NetBSD 跨平台代码的全球扩散；39.5.4.3 Apple 作为 NetBSD 代码“形式主义化”载体的悖论；39.5.4.4 Darwin/macOS 关系对 BSD 商业化路径的启示 | NetBSD 6.x-10.x 时代体现了项目统摄史观中“在虚假中寻找仅存的真实”与“会者定离”的双重运作：tainted code 政策是对 AI 时代真实性困境的哲学回应（在虚假中寻找真实），而社区规模的萎缩与硬件支持的滞后则是会者定离的宿命——开发者在不被看见的角落守护着“可移植性”的理想

（整理留痕：上文 39.2-39.5 三级大纲系章号平移前旧第 39 章的他章大纲错装粘连（含子-子-子节全量条目），待跨文件迁移并按新号重编，暂 DEFERRED 留痕；FP 论文著录与史观映射已在本节内拆分独立）

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2012-2012 年间：37,493 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- netbsd.duckdb netbsd-src 仓库 christos commit 记录；Heartbleed 官方披露公告（heartbleed.com）；CVE-2013-0169、CVE-2014-0160 NVD 条目 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2909 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2909`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔S.P.Zeidler: NPF in NetBSD 6（P2B, AsiaBSDCon 2013）讲者口述：NPF 的全部目的在于设计并验证能在多个 CPU 上同时做包过滤的方案；讲者称 IP Filter 与 PF 都不做多处理器处理（原话带“若我说错请纠正”的保留，转写音作 to our budget processing）。（YouTube EPl9i016yBwxU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2910 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2910`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔S.P.Zeidler: NPF in NetBSD 6（P2B, AsiaBSDCon 2013）讲者口述：为使状态存储利于按 CPU 扩展，NPF 采用多棵红黑树：树数当前硬编码为 1024（计划改为可配置），每树各有一把锁（转写音作 retried lock），并按源／目的地址、接口与协议哈希选树。（YouTube EPl9i016yBwxU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2911 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2911`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔S.P.Zeidler: NPF in NetBSD 6（P2B, AsiaBSDCon 2013）讲者口述：NPF 核心在 6.0 与 6.1 之间有重大改动：其 SMP 处理路径在 6.0 中尚属未经测试，到 6.1 团队认为已足够稳定，遂启用该部分。（YouTube EPl9i016yBwxU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2912 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2912`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔S.P.Zeidler: NPF in NetBSD 6（P2B, AsiaBSDCon 2013）讲者口述：讲者解释 NetBSD 已有 IP Filter 与 PF 仍另建 NPF 的理由：要试验新算法与新基础设计，从零开始更容易，不必顾及既有配置、既有用户与既有框架（转写音作 IP to，疑指 IPF）。（YouTube EPl9i016yBwxU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
