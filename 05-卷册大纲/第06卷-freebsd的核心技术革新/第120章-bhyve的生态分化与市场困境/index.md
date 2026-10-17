---
chapter: 第 120 章
id: CH120
volume: 第06卷-freebsd的核心技术革新
---

# 第 120 章 bhyve的生态分化与市场困境

## 要点

- bhyve 被成功移植到 illumos 内核，形成了独立的 illumos bhyve 分支；Pluribus Networks 与 Joyent 是 illumos bhyve 移植的主要贡献者，Joyent 在 SmartOS 中使用 bhyve 作为其 Triton 云平台的核心 hypervisor 之一（与 Solaris Zones 并列）；illumos bhyve 添加了一些 F
- bhyve 项目的核心维护者 committer 状态：Neel Natu（尼尔·纳图）（nneul@）是 bhyve 初始代码作者，NetApp 员工，其 FreeBSD src committer 权限持续活跃至 2010 年代中后期，后逐渐减少活动；Peter Grehan（彼得·格雷汉）（grehan@）是 bhyve 长期主要维护者，FreeBSD Foundation 董事，持续活跃至
- 2011-2026 年间与 bhyve 同期发展的主要虚拟化技术见下表，覆盖 Linux KVM、Xen、VMware ESXi、Microsoft Hyper-V、QEMU、bhyve、Apple Hypervisor.framework 共 7 个主流 hypervisor 的发布年份、主导者、许可证与市场定位。

| 虚拟化技术 | 发布年份 | 主导者 | 许可证 | 市场定位 |
| --- | --- | --- | --- | --- |
| Linux KVM | 2007 年 | Avi Kivity/Red Hat | GPLv2 | 云虚拟化事实标准（AWS Nitro、GCE、Azure 部分） |
| Xen | 2003 年 | 剑桥大学 | GPLv2 | AWS 早期使用，后转向 KVM Nitro |
| VMware ESX/ESXi | 2001 年（ESX）/2007 年（ESXi） | VMware | 商业闭源 | 企业数据中心主流 |
| Microsoft Hyper-V | 2008 年 | Microsoft | 商业闭源 | Windows Server 内置，Azure 早期使用 |
| QEMU | 2003 年 | Fabrice Bellard | GPLv2 | KVM/Xen 的用户态设备模拟层 |
| bhyve | 2011-2014 年 | Neel Natu（尼尔·纳图）/Peter Grehan（彼得·格雷汉） | BSD 2-Clause | FreeBSD 原生 Type-2 hypervisor，随 FreeBSD 10.0 发布 |
| Apple Hypervisor.framework | 2014 年 | Apple | 专有 | OS X 10.10 用户态 hypervisor API |
- **统计分析印证**——`freebsd.duckdb` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；ARIMA(5,0,5) 模型拟合 AIC = 107.39（统计结论 C-29），预测精度
- bhyve ARM64 支持的探索始于 2015-2016 年，Mihai Carabaș 与 Peter Grehan（彼得·格雷汉） 在 BSDCan 2016 发表了 “Porting bhyve on ARM” 演讲，概述了将 bhyve 移植到 AArch64（ARM64）架构的工程计划；ARM64 虚拟化依赖 ARM Virtualization Extensions（VE），包括 E

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_635] 卷“第06卷-freebsd的核心技术革新”第 120 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_666] 卷“第06卷-freebsd的核心技术革新”第 120 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_701] 卷“第06卷-freebsd的核心技术革新”第 120 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_1058] 卷“第06卷-freebsd的核心技术革新”第 120 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1

## 史观

- 总纲第 5 条——没有必然性只有偶然性：bhyve 写出了 FreeBSD 自己的 hypervisor，却没有写出 KVM 身后那条庞大的产业链——这不是代码的失败，而是时机与生态的偶然判决。Neel Natu 在 NetApp 启动 BHyVe 项目时，KVM 已随 Linux 主线进入全球公有云，VMware 已统治企业数据中心十余年，hypervisor 市场的网络效应早已锁死。bhyve 的代码简洁、架构优雅、BSD 许可证自由，它在 FreeBSD/TrueNAS/illumos 生态中是一个成功的虚拟化方案，但它永远不会成为云时代的标准——这不是因为 bhyve 技术不好，而是因为当 2014 年 bhyve 随 FreeBSD 10.0 正式发布时，虚拟化战争早已结束。bhyve 的故事是 BSD 生态的缩影：技术优秀但资源有限，许可证自由但缺乏商业锁定，在大型厂商主导的基础设施市场中，它找到了属于自己的 niche，却无法打破既有格局。历史的判决不是 “bhyve 输给了 KVM”，而是 “在一个赢者通吃的网络效应市场中，晚到者即使做得更好，也很难改写格局”。bhyve 没有输，它只是生不逢时。

## 辨析

- illumos bhyve 移植的时间线需精确——Pluribus Networks 于 2012-2013 年左右开始初始移植，Joyent 随后加入并将其集成到 SmartOS [存疑——精确日期需 Joyent/Pluribus 官方公告验证]；xhyve 对 macOS Hypervisor.framework 的利用是一个有趣的架构创新——将原本需要内核模块的 hypervisor 完全
- 原文中提到的 “Qing Huang” 作为主要维护者需要核实——该名字未在 bhyve 主要 commit 历史与演讲作者中显著出现 ［ 存疑脚注：此处事实待多源交叉验证 ］，bhyve 核心维护者应为 Neel Natu、Peter Grehan、John Baldwin 等人；bhyve 维护团队规模较小是事实，这直接导致了功能开发速度慢于 KVM，但也意味着代码审查严格、架构一致性保持较好
- bhyve 与各虚拟化技术的比较需避免简单的 “成败论” 叙事——bhyve 没有成为云标准并不意味着技术失败，它在其目标场景（FreeBSD 原生虚拟化、存储设备集成、BSD/illumos 生态）中是成功的；bhyve 与 KVM 的架构差异反映了不同的设计哲学：KVM 追求 “Linux 内核中的通用 hypervisor，支持一切场景”，bhyve 追求 “FreeBSD 内核中的简洁 h
- **统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 Sen's slope =+1.40/月 的实际工程意义须结合 FreeBSD 版本周期与 commit 粒度变化综合判断；(2) bhyve 贡献率未量化：commit 量统计不区分 bhyve 相关 commi
- bhyve ARM64 支持状态需精确区分：截至 FreeBSD 14.0（2023 年），arm64 bhyve 仍处于实验阶段，功能完整性落后于 x86 版本，不支持 PCI 直通、GPU 加速等高级功能；NetBSD 也开发了自己的 NVMM hypervisor 用于 ARM64，与 FreeBSD bhyve 独立；bhyve ARM64 支持并非从零开始，FreeBSD/arm64 架

## 文献

- Gerdts M. bhyve zones in SmartOS [C]//bhyvecon 2018. 2018; Joyent. SmartOS Documentation: bhyve [EB/OL]. [2026-07-19]. <https://docs.smartos.org/>; machyve. xhyve: a lightweight OS X virtualization solution [EB/OL]. [2026-07-19]. <https://github.com/machyve/xhyve>; Moby Project. HyperKit: A toolkit for embedding hypervisor capabilities [EB/OL]. [2026-07-19]. <https://github.com/moby/hyperkit>.

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. FreeBSD src Repository Commit Log [EB/OL]. [2026-07-19]. <https://cgit.freebsd.org/src/>; FreeBSD Project. Committer's Guide [EB/OL]. [2026-07-19]. <https://www.freebsd.org/doc/en_US.ISO8859-1/articles/committers-guide/>; FreeBSD Core Team. Project Announcements [EB/OL]. [2026-07-19]. <https://lists.freebsd.org/archives/freebsd-announce/>. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Kivity A, Kamay Y, Laor D, et al. kvm: the Linux Virtual Machine Monitor [C]//Proceedings of the Linux Symposium. 2007, 1: 225-230; Barham P, Dragovic B, Fraser K, et al. Xen and the Art of Virtualization [C]//SOSP '03. 2003: 164-177; Bellard F. QEMU, a Fast and Portable Dynamic Translator [C]//USENIX ATC ’05. 2005: 41-46; VMware. ESXi Technical Documentation [EB/OL]. [2026-07-19]. <https://docs.vmware.com/>; Microsoft. Hyper-V Technical Documentation [EB/OL]. [2026-07-19]. <https://learn.microsoft.com/en-us/windows-server/virtualization/>; Apple. Hypervisor.framework Documentation [EB/OL]. [2026-07-19]. <https://developer.apple.com/documentation/hypervisor>; Grehan P, Natu N. bhyve - Past, Present, and Future [C]//AsiaBSDCon 2014. Tokyo, 2014.

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/freebsd.duckdb**; LibreBSD Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5; LibreBSD Project. 时间序列分析.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/时间序列分析.md** Task 14-15; LibreBSD Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第五卷第 53 章映射。［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Carabaș M, Grehan P. Porting bhyve on ARM [C]//BSDCan 2016. Ottawa, 2016; FreeBSD Project. FreeBSD 13.0-RELEASE Release Notes [EB/OL]. (2021-04-13)[2026-07-19]. <https://www.freebsd.org/releases/13.0R/relnotes/>; FreeBSD Project. **vmm(4)** arm64 Manual Page; FreeBSD arm64 mailing list archives. lists.freebsd.org/archives/freebsd-arm/.

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- iXsystems. Introducing TrueNAS SCALE [EB/OL]. (2020)[2026-07-19]. <https://www.truenas.com/>; iXsystems. TrueNAS CORE Release Notes [EB/OL]. [2026-07-19]. <https://www.truenas.com/docs/core/>; Kennedy C. Why We're Moving TrueNAS from FreeBSD to Debian [EB/OL]. Blocks & Files, 2024-04-08 [2026-07-19]. [考据脚注：该文章标题本身存在误导——“Moving TrueNAS from FreeBSD” 暗示 TrueNAS 整体从 FreeBSD 迁移，但文章实际讨论的是 SCALE 版本的 Linux 选择，并非 CORE 版本放弃 FreeBSD。经核查，该 URL 当前返回 404，但文章标题在互联网多个转载中可确认。]; Moore K. On the TrueNAS CORE Deprecation [EB/OL]. iXsystems Blog, 2024-04 [2026-07-19]. ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP337、BSD Now EP128（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- CBSD 作者以约四小时写出 K8CBSD 模块，用 bhyve 起 Ubuntu 云镜像虚拟机组成 Kubernetes 集群，展示 FreeBSD 与 Linux 技术的协作。（BSD Now EP337，[1720.78-1743.02]，L2）
- Drew DeVault 的文章坦诚全职自由软件工作的幸福与压力：能按自己方式写代码，但伴随技术债、过高期待与时间碎片化。（BSD Now EP337，[412.76-544.44]，L2）
- Warner Losh 在 FOSDEM 访谈中讲述恢复 Venix、接触 Unix Heritage Society（TUHS）与早期 Unix 被遗忘的首次实践。（BSD Now EP337，[2755.62-2889.14]，L2）
- NetBSD 9 RC1 发布，含 AArch64 支持、NVMM 硬件虚拟化、内核 ASLR 与 sanitizer 等。（BSD Now EP337，[1975.48-2102.14]，L2）
- 受访路由工程师自述：俄亥俄州教育科研网络以 FreeBSD 承载 DNS、堡垒机、监控后端与 Juniper 设备管理，基础设施自 4.x 时代积累、历经 6 与 8 两代停留后正向 10.x 迁移；其运维哲学是裸金属单用途部署以隔离故障级联，并以串口控制台、远程电源恢复与改造自 PC-BSD 的自动化安装器保障全州分散机房的可管理性，新机交付现场或制作安装 U 盘各仅需十分钟 [存疑脚注] 转写专名失真：受访机构作 Ornette 应为 OARnet，受访人拼写 Wolf/Wolfe 不定，以当期节目页为准（BSD Now EP128，[1456.6-1663.3]，L1）[订正：原 [1463.68-1650.74]，2026-09-30 SenseAudio 重转核对]
- 同一访谈揭示 ISP 场景对发布工程的特殊要求：只需安全更新的运维方长期不信任二进制包，季度包分支改善局面但仍不足以建立信任，因而期待 base 系统打包化并以 Poudriere 自管包源；主持方以冻结 ports 快照重建包源、必要时整机重装包清单的做法被引为可行先例，折射 2016 年前后 FreeBSD 包管理从源码构建向二进制包信任转移的过渡态（BSD Now EP128，[2149.6-2304.1]，L1）[订正：原 [2150.86-2296.64]，2026-09-30 SenseAudio 重转核对]
- 首届存储峰会与 USENIX FAST 会议联办并转向 hackathon 形态：CAM 工作组讨论多队列控制器与跨 CPU 争用，ZFS 工作组聚焦 OpenZFS 新增的 SHA-512 截断 256 位与 Skein 校验和；后者在 64 位 x86 上因字长匹配更快，但 FreeBSD 内核尚缺实现，且 block pointer 仅预留 256 位校验和空间，容纳更长摘要将迫使盘上格式自 V5000 升版，播客中甚至出现未来淘汰 Fletcher 4 的半玩笑预言，显示格式演进受制于设计时预留的约束（BSD Now EP128，[3099.2-3306.7]，L2）[订正：原 [3110.24-3306.50]，2026-09-30 SenseAudio 重转核对]

**史料**：

- CBSD 项目的 K8CBSD 模块说明及其公开仓库与演示视频。（BSD Now EP337，[1728.62-1744.86]，L2）
- Warner Losh 的 FOSDEM 访谈与其 Unix 早期史演讲。（BSD Now EP337，[2577.96-2992.62]，L2）
- NetBSD 9 RC1 发布博客与 OPNsense 20.1 Keen Kingfisher 发布公告。（BSD Now EP337，[1969.8-2340.46]，L2）
- RISC-V 初始移植的一手线索：FreeBSD 基金会博客详述初始支持细节，剑桥研究工程师提交使 FreeBSD 于 Spike 模拟器可引导的系列提交，后续目标为多核与用户态支持，受英国高等教育创新基金与 DARPA CTSRD 项目资助，并被定位为免于 ARM 授权模式的低风险新指令集选项 [存疑脚注] 转写作 Ruslan Vukin，当为剑桥大学 Ruslan Bukin；基金名称与 CTSRD 展开须以基金会博客原文核验（BSD Now EP128，[299.9-398.6]，L2）[订正：原 [323.66-396.94]，2026-09-30 SenseAudio 重转核对]
- 纽约 Papers We Love 聚会预告构成容器史一手节点：Cantrill 借纽约容器峰会之便留驻一晚，重讲 Poul-Henning Kamp 与 Robert Watson 的论文 Jails: Confining the Omnipotent Root，以及 Dan Price 与 Andy Tucker 的 Solaris Zones 论文，主持人强调 jails 先于容器概念出现；预告附时间地点与录像计划，可回溯为 2016 年容器谱系论争的现场材料（BSD Now EP128，[2872.3-2945.2]，L2）[订正：原 [2893.92-2944.04]，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲10 动手者创造历史：CBSD 作者以几小时工程实践搭起 K8s 集群，体现工具链由动手者驱动。（BSD Now EP337，[1728.62-1743.02]，L2）
- 总纲19 解释学循环是历史认识的根本条件：Warner 借助重放的 Venix 源码与 TUHS 社群重新理解 Unix 早期史，史料与解释互为前提。（BSD Now EP337，[2838.34-2889.14]，L2）
- 总纲10 动手者创造历史：本期叙事重心不在发布与机构而在动手者：独力接管全州 FreeBSD 基础设施的年轻工程师、照标准把 SHA-512/256 写进 FreeBSD 内核的播客主持人、把 Tor 客户端移植到 OpenBSD 的志愿团队，均以具体修补而非宣言推动系统演进；主持人点出私有 workaround 只有被个别人推进主干才能惠及众人（2684.98-2688.86），正是动手者创造历史的注脚（BSD Now EP128，[2678.40-2688.86]，L2）

**辨析**：

- 转写中‘K8CBSD’ 等专名与 CBSD 版本信息需以 CBSD 官方文档核验；‘Wild Nenon truce’ 等表述为语音转写噪声。 [存疑脚注] 转写专名与习语存疑（BSD Now EP337，[1540.18-1554.58]，L4）
- bhyve 的 UEFI/CSM 客户机支持据称已进入 Current 并回移至 10.3 分支，Windows Server 与桌面各版本经测试可引导，无人值守安装依赖定制 ISO 与 Nahanni 预置脚本；上述论断均系口述，转写将 Peter 的人名主页、引导 ROM 改进与 userboot 路径选项混叙，具体提交号与支持矩阵须回到 commit 与移植文档复核，转写中 Beehive 通体为 bhyve 之误（BSD Now EP128，[474.7-594.1]，L2）[订正：原 [484.70-589.86]，2026-09-30 SenseAudio 重转核对]
- 新闻段提及一款聚合多物理机为单一巨型虚拟机的商用 hyperkernel 产品，转写作 TitleScale 并称其构建于 bhyve 之上，与 2016 年 2 月 Joyent 发布 Triton 弹性计算的时间与特征近似，但产品全名、虚拟化基座与 FreeBSD 支持细节在转写中均失真，映射与引用前须以官方新闻稿核验 [存疑脚注] 转写作 TitleScale，疑为 Joyent Triton；其是否基于 bhyve 聚合多机为单一虚拟机的表述与公开史实待官方新闻稿验证（BSD Now EP128，[699.4-784.0]，L4）[订正：原 [702.44-762.26]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP337] Pennington J. BSD Now: 337: Kubernetes on bhyve[EB/OL]. (2020-02-13)[2026-08-15]. <https://www.bsdnow.tv/337>.
- [BSD Now EP128] Pennington J. BSD Now: 128: The State of BSD[EB/OL]. (2016-02-10)[2026-08-15]. <https://www.bsdnow.tv/128>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-385 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-385`；w172 YouTube 章节路由采纳）

据〔User Friendly bhyve 演讲〕讲者 Michael Dexter 口述：FreeBSD 安装程序使用 UFS。（YouTube EPcF-qS7FQNPo，[1399.36-1403.11]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-384 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-384`；w172 YouTube 章节路由采纳）

据〔User Friendly bhyve 演讲〕讲者 Michael Dexter 口述：bhyve 可运行 Solaris zone 或 Linux 品牌 zone，类似 compat-linux jail。（YouTube EPcF-qS7FQNPo，[1231.679-1240.549]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-702 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-702`；w172 YouTube 章节路由采纳）

据〔EuroBSDCon 2024〕讲者口述：OpenBSD 技术包含 sec0（音作 SEC zero）、sect4、ospf、BGP（YouTube EPko8-nbDRiBQ，[2520.252-2525.522]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1420 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1420`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔bhyvecon Tokyo 2018 讨论环节〕讲者口述：一位为大学硕士学生提供大数据/NoSQL 课程实验机器的用户表示，bhyve 起步快、易上手，整个学期几乎无需运维管理；其负载为三个月左右的教学用途、非生产规模，并认为若要评估 bhyve 相对裸机的性能损失，可以借助 DTrace去定位瓶颈。（YouTube EP3pXFn23T2HM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1421 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1421`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔bhyvecon Tokyo 2018 讨论环节〕讲者口述：bhyve 网络性能测试称，采用 PT-netmap 后同一宿主机上宿主机到虚拟机的封装流量可达约 21 Gbit/s，跨网线虚拟机到虚拟机流量约 15 Gbit/s；该方案取自意大利比萨大学的 Luigi，但讲者随后表示它无法有效扩展，劝人不要走这条路。（YouTube EP3pXFn23T2HM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1422 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1422`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔bhyvecon Tokyo 2018 讨论环节〕讲者口述：有用户只在开发场景使用 bhyve，称若像 KVM/QEMU 那样拥有合适的接口与主流框架集成就愿意投入生产；另有讲者指出，各家云实现各不相同，要为它们提供统一语义的抽象层“credibly difficult”，这正是 bhyve 难以在生产落地的生态性障碍。（YouTube EP3pXFn23T2HM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1423 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1423`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔bhyvecon Tokyo 2018 讨论环节〕讲者口述：关于 bhyve 的在线迁移（live migration）实现，讲者介绍其做法是把虚拟机状态存到磁盘（说法与 OpenBSD 上保存虚拟机状态的方式类似），再把该状态存放在另一个虚拟机中。（YouTube EP3pXFn23T2HM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1535 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1535`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 P01A、Michael Dexter 演讲〕讲者口述：FreeBSD 自 2000 年起具备 jails、约 2014 年起具备 bhyve，二者在操作系统及其周边工具中已扮演重要角色，但尚未与操作系统充分整合以支持无摩擦使用。（YouTube EPe1B_6iGY2lU，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1536 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1536`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 P01A、Michael Dexter 演讲〕讲者口述：一例 FreeBSD 开发分支上的回归缺陷于 2017 年 6 月引入、10 月 1 日修复，暴露约三个月，历经 3710 次提交方修复；该变更本为新增功能，回归表现为内存泄漏。（YouTube EPe1B_6iGY2lU，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1537 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1537`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 P01A、Michael Dexter 演讲〕讲者口述：该回归随 FreeNAS 11.1 发布（12 月 13 日），远晚于缺陷已被发现与修复之时，其后于 36 天后的 18 日方在 FreeNAS 侧修正。（YouTube EPe1B_6iGY2lU，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1538 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1538`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 P01A、Michael Dexter 演讲〕讲者口述：当前 boot/kernel 目录布局自 FreeBSD 5 引入，而 FreeBSD 5 所引导的内核内置虚拟机监视器（bhyve）长期鲜有人尝试使用。（YouTube EPe1B_6iGY2lU，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
