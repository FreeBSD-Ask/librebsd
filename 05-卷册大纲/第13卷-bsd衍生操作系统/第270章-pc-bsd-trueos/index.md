---
chapter: 第 270 章
id: CH270
volume: 第13卷-bsd衍生操作系统
---

# 第 270 章 pc-bsd-trueos

## 要点

- PC-BSD（2005）由 Kris Moore（克里斯·摩尔） 发起，提供图形安装器、PBI 软件包系统、预配置桌面，目标是 “开箱即用 FreeBSD 桌面”；其存在反映社区对消费桌面的长期诉求。
- 2018 年 PC-BSD 更名为 TrueOS，转向服务端/嵌入式定位（延续 FreeBSD 基底），桌面努力由 Project Trident（基于 TrueOS）承接；2020 年前后 TrueOS/Trident 项目渐止，标志一轮桌面 BSD 实验的落幕。具体时间须以项目公告核实。
- PC-BSD/TrueOS 依赖 Kris Moore（美国）与小型志愿者团队；项目体现个人驱动力在 BSD 衍生中的关键作用。
- 对比 PC-BSD/TrueOS（FreeBSD）与 Linux 桌面（Ubuntu 等）、其他桌面 BSD（参见相关章节桌面 BSD 部分），分析桌面 BSD 实验的共性教训（生态/硬件/应用）。
- bsd_commits.duckdb 查询显示 trueos-src 仓库共 273 条 CVE 相关 commit、377 个去重 CVE，commit 数（273）低于去重 CVE 数（377），表明 TrueOS 存在单次 commit 合并多个 CVE 修复的批量化安全维护模式；trueos-src 的 CVE commit 跨越 2005 至 2020 年，2020 年后无新增 CVE comm

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3779] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3781] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3789] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3799] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3803] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3805] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3806] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3863] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章
- [DB:references_fulltext:chapter_matches:chmatch_3964] 卷“第14卷-商业生态与企业案例”第 270 章，匹配置信度 folder，原因：folder 第269章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- PC-BSD 各版本对应 FreeBSD 基底须以项目 Release Notes 核实；freebsd.duckdb 查询 L1.1.1 的 commit 量仅反映开发活跃度，须结合 commit 规模（additions/deletions）与 message 质量综合判断，且 GitHub 镜像仓库 commit 量可能滞后于主仓，trueos-src 仓库 2016 年的 commit 量峰值须与
- trueos-src 的 273 条 CVE commit 与 377 个去重 CVE 的数量差异（commit 数 < CVE 数）表明部分 commit 引用多个 CVE 编号，此批量化模式须以具体 commit message 核实，不得仅凭数量差异推断安全维护质量；2020 年后无新增 CVE commit 可能有多种原因——项目终止、仓库归档、镜像同步停止——须与 Project Tri
- PC-BSD 时期 “安全维护投入高于纯社区 fork” 的判断须以 iXsystems 员工 commit 量、安全公告频率等量化指标为据，不得仅凭定性判断；参照第 122 章 122.2.3 节已考据的 iXsystems 员工 freebsd-src 上游回馈 commit 前 4 名表——ryan@iXsystems.com 329 次、rob.norris@truenas.com 137

## 文献

- PC-BSD 官方文档；freebsd.duckdb 查询 L1.1.1（trueos-src 仓库 2005-2020 年每年 commit 量时间序列）；原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1。 ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2018 年间：571,244 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 项目档案。［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 2018-2020 年间：126,447 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- 各桌面 OS 官方资料。［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- bsd_commits.duckdb 查询 trueos-src CVE commit（273 条，377 去重 CVE，2026-07-23）；bsd_commits.duckdb 查询 L7.1.1.trueos-src；`原材料/研究/bsd漏洞史/数据库提取/trueos-src-cve-commits.md`；`原材料/研究/bsd仓库分析/数据分析/衍生项目与跨项目对比分析.md` §L7.1。 ［B］## 269.4.2 PC-BSD 时期 CVE 处置与 iXsystems 商业安全维护投入
- freebsd.duckdb 查询 L1.1.1（trueos-src 每年 commit 量）；freebsd.duckdb 查询 L7.1.1.trueos-src；PC-BSD 官方文档；iXsystems 年度报告。 ［B］FreeBSD 社区论文：[FP-2018-035] The TrueOS Difference: Changing Methodologies for Changing Times（Ken Moore，2018）<https://papers.freebsd.org/2018/bsdcan/moore-the_trueos_difference/>

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1985-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP282、BSD Now EP225、BSD Now EP221、BSD Now EP193、BSD Now EP192、BSD Now EP185、BSD Now EP54、BSD Now EP19（共 8 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- openrsync 是对 rsync 的净室重实现，采用 BSD ISC 许可证而非 GPL，目标是兼容现代 rsync（以 3.1.3 为测试基准），从而可作为基础工具进入 BSD 系统。（BSD Now EP282，[1537.66-1615.38]，L2）
- openrsync 初期仅面向 OpenBSD 编译运行，安全机制依赖 pledge 与 unveil，移植到 FreeBSD 可用 Capsicum 实现，Linux 上则难以等效实现。（BSD Now EP282，[1600.22-1662.98]，L2）
- NetBSD 博客报告 LLD 链接器移植进展：LLD 相比 GNU ld 内存占用更低、链接更快，当前 8GB 内存不足以静态链接 LLVM，目标是从生成可用的 NetBSD 可执行文件逐步过渡到替换 userland 链接器。（BSD Now EP282，[1799.22-1950.22]，L2）
- TrueOS 17.12 稳定版发布，含 OpenRC 服务定义更新、Lumina 改进，并基于 FreeBSD current 以提前获取图形与 Wi-Fi 驱动。（BSD Now EP225，[73.68-83.2]，L2）
- PDP-11 回顾引述 C Gordon Bell 等人的论文，梳理 DEC 1957 年创立、以“Programmed Data Processor”避讳“计算机”一词，以及 PDP-11 在地址位、寄存器、栈、中断、字符处理上的设计取舍。（BSD Now EP225，[1844.12-1885.92]，L2）
- 该回顾点明 UNIX 1974 年由 Ken Thompson 携磁带抵达伯克利，演化出 BSD 与 Sun Microsystems；C 的 16 位 int 亦源自 PDP-11。（BSD Now EP225，[2883.82-2958.5]，L2）
- FreeBSD 2017 发布工程回顾：Glen Barber 全职工负责发布工程，11.1 于 7 月 21 日发布，10.4 由另一名发布工程师领衔并作为 stable 10 分支的最终版本。（BSD Now EP225，[3334.96-3475.08]，L2）
- 主持人 Alan 报告 BSD Taiwan 之行：会议约 120 余人报名、组织者被迫关闭注册，演讲含 FreeBSD 的 RISC-V 移植、Capsicum 沙箱化、FreeBSD 12 内存管理改进与 bhyve 图形支持史。（BSD Now EP221，[671.56-686.18]，L1）
- 该期报道 Lumina 1.4.0 发布（Ken Moore 团队），新增主题引擎与对 Qt5 应用换肤的支持。（BSD Now EP221，[1918.4-1955.88]，L2）
- 该期转述 OpenBSD p2k17 hackathon 报告（Bob Beck），回顾过去需拖运服务器与提前搭建基础设施，如今仅需最新快照与本地 CVS 仓库即可开发。（BSD Now EP221，[4912.02-5057.18]，L2）
- 该期转述 Matt Ahrens 对 ZFS 原生加密的回应：加密会先于 RAID-Z 扩容落地，已在 ZFS on Linux 主分支。（BSD Now EP221，[4712.78-4758.9]，L2）
- Adrian Chadd 在 FreeBSD 802.11 栈中启动 802.11ac 支持，先针对 Atheros QCA 10K 芯片，加入 VHT 通道与 20/40/80/160MHz 模式，并说明现有栈在多虚拟接入点上的局限。（BSD Now EP193，[147.78-631.0]，L2）
- Delphix 的 Matt Ahrens 等在 OpenZFS 开发者峰会原型基础上实现 zpool checkpoint，允许管理员在执行破坏性操作前为整个池建立可回滚检查点。（BSD Now EP193，[1810.2-2535.42]，L2）
- TrueOS（原 PC-BSD）改为基于 FreeBSD current 的滚动发布，默认 Lumina 桌面；DistroWatch 评测肯定其 ZFS 集成与安装流程，但指出硬件兼容与稳定更新方面的不足。（BSD Now EP193，[2605.18-3020.76]，L2）
- LibreSSL 2.5.4 修复证书验证回调一致性与 Linux getrandom 阻塞等问题；Michael Hendricks 因 Heartbleed 后 OpenBSD 分叉 LibreSSL 的经历由 macOS 转投 OpenBSD。（BSD Now EP193，[1277.66-1583.66]，L2）
- OpenSSH 彻底移除 SSHv1 全部代码，简化协议处理；此前该协议已默认禁用多年。（BSD Now EP192，[65.54-183.18]，L2）
- FreeBSD 基金会 4 月更新记录授予 Edward Napierala 项目资助，以 CTL 为后端开发 USB 大容量存储目标驱动，使 BeagleBone Black、Raspberry Pi Zero 等嵌入式平台可模拟 U 盘。（BSD Now EP192，[210.02-300.24]，L2）
- Patrick M. Hausen 回忆 1994 年与 Jordan Hubbard 会面，获 Walnut Creek 全套 CD-ROM 与 50 张 FreeBSD 1.1 光盘回德国推广，其后公司以 FreeBSD 3/4 运行服务器。（BSD Now EP192，[1270.68-1320.66]，L1）
- Rick Macklem 发布 pNFS 服务器首个测试征集，架构为单个元数据服务器加多个数据服务器，纯 FreeBSD 实现，当前尚不支持冗余。（BSD Now EP192，[5241.34-5535.38]，L2）
- Chris Moore 在主持 BSD Now 约四年、180 余期后卸任，Benedict Reuschling 接任共同主持。（BSD Now EP185，[61.44-101.44]，L1）
- Kris Moore 披露 FreeNAS 9.10.3 为首个基于 FreeBSD 11 stable 的 9 分支版本，并引入 MinIO S3 兼容对象存储。（BSD Now EP185，[657.68-869.02]，L1）
- TrueOS 移除 GRUB 安装选项，改用 EFI rEFInd 链加载 BSD loader；计划改进 GELI 密钥在 bootstrap、loader 与内核间的传递。（BSD Now EP185，[2829.24-2905.56]，L1）
- iocage 由 Brandon Schneider 以 Python 重写并引入 JSON API，插件采用 pkg 而非旧的 PBI 格式。（BSD Now EP185，[961.44-1046.98]，L2）
- Lumina 由 Ken Moore 开发，采用三条款 BSD 许可证，专为 FreeBSD 原生编写而非自 Linux 移植，依赖 Xorg、Qt 与 Fluxbox 窗口管理器。（BSD Now EP54，[3448.90-3497.98]，L1）
- Lumina 0.6.2 随 PC-BSD 10.0.3 发布，仍处 beta，但在轻量笔记本上 CPU 占用低于半个百分点、整机内存约 120 MB。（BSD Now EP54，[3491.66-3526.78]，L1）
- Lumina 附带 Insight 文件管理器，可浏览 ZFS 快照实现类似时光机的文件恢复，并集成书签、标签页与多媒体浏览。（BSD Now EP54，[4225.74-4268.26]，L1）
- Lumina 已提交进入 FreeBSD ports 树，PC-BSD 亦提供对应包，后续社区将其移植到 OpenBSD 与 DragonFly BSD。（BSD Now EP54，[3542.62-3548.58]，L1）
- 本期以 installfest 形式逐项演示 FreeBSD 10.0、OpenBSD 5.4、NetBSD 6.1.2、DragonFly BSD 3.6 与 PC-BSD 10.0 的安装流程，比较文本式、引导式与图形式安装器的交互差异。（BSD Now EP19，[1011.60-1046.72]，L2）
- FreeBSD 10 安装器新增键位测试、自动 root-on-ZFS、GELI 磁盘加密与 shell 安装模式，改进主要由 Devin Teske 与 Warren Block 等完成。（BSD Now EP19，[1069.32-1330.48]，L2）
- OpenBSD 在 5.4 前后提交 signify，用于签名基础发行集与第三方包，以解决此前 SHA256 校验在 X 集同步时因多机多时构建而出现的时序错配。（BSD Now EP19，[321.52-347.64]，L2）
- PC-BSD 使用 pc-sysinstall 脚本化安装器，图形安装可保存配置用于批量部署；TrueOS 为无 GUI 的服务器版本，内置 PEFS 与 Life Preserver 等命令行组件。（BSD Now EP19，[2244.04-2352.08]，L2）
- NetBSD 社区发布 pkgsrc 2013Q4；FreeBSD 侧由 Julio Merino 自 NetBSD 带入 Kyua 测试框架并搭建持续测试基础设施，以替代旧 Tinderbox 思路。（BSD Now EP19，[91.48-144.40]，L2）

**史料**：

- openrsync 仓库为私有仓库的只读镜像，作者提示项目尚在快速变动、未完成，rsync 与 rsyncd 手册页可查协议细节。（BSD Now EP282，[1664.34-1695.70]，L2）
- NetBSD 达到 100% 可复现构建，主持人补充 FreeBSD 用户态长期基本可复现，仅 PMC stat 排序等偶发例外；这构成 BSD 系统构建可验证性的社区材料。（BSD Now EP282，[2409.80-2531.30]，L2）
- C Gordon Bell 等人论文（“What have we learned from the PDP-11?” 等四篇）的转述，含 1957 年 DEC 创立与 PDP-11 设计回顾。（BSD Now EP225，[1940.36-1968.48]，L2）
- 转述的 OpenBSD 工作站指南，含用户动作即时完成、极简工具、硬件隐私等设计目标。（BSD Now EP225，[542.34-652.4]，L2）
- FreeBSD 基金会 2017 发布工程回顾（Glen Barber 的 VBSDCon 演讲与问答）。（BSD Now EP225，[3334.96-3771.04]，L2）
- BSD Taiwan 会议议程与台湾用户 Scott Tsai 的逐演讲笔记（Google Doc）。（BSD Now EP221，[675.04-703.58]，L2）
- OpenBSD 6.2 唯一 CD 套装的 eBay 拍卖（Bob Beck，Theo de Raadt 手绘签名）。（BSD Now EP221，[4444.02-4527.38]，L2）
- Bob Beck 的 OpenBSD p2k17 hackathon 报告（undeadly.org）。（BSD Now EP221，[4912.02-4951.78]，L2）
- Matt Ahrens 关于 ZFS 原生加密的推文回复。（BSD Now EP221，[4717.92-4748.12]，L2）
- Adrian Chadd 关于 802.11ac bring-up 的博客（BSD Now EP193，[81.22-648.52]，L1）
- Delphix 关于 zpool checkpoint 的设计说明博客（BSD Now EP193，[1810.2-2600.06]，L1）
- DistroWatch 对 TrueOS 的评测文章（BSD Now EP193，[2605.18-3031.58]，L1）
- LibreSSL 2.5.4 发布说明（BSD Now EP193，[5057.4-5151.86]，L1）
- OpenBSD OpenSSH 删除 SSHv1 代码的提交记录（BSD Now EP192，[65.54-183.18]，L1）
- FreeBSD Foundation 2017 年 4 月开发者更新（BSD Now EP192，[210.02-300.24]，L1）
- Patrick M. Hausen 访谈自述（BSD Now EP192，[1066.4-2279.84]，L1）
- Rick Macklem 的 pNFS call for testing 邮件（BSD Now EP192，[5241.34-5535.38]，L1）
- Chris Moore 卸任自述（BSD Now EP185，[61.44-141.04]，L1）
- Kris Moore 访谈自述（BSD Now EP185，[628.1-1119.87]，L1）
- TrueOS 引导与 GELI 变更记录（BSD Now EP185，[2829.24-2905.56]，L1）
- Ken Moore 访谈兼 Lumina 界面走查（Lumina 作者当事人演示）。（BSD Now EP54，[3404.70-4697.20]，L1）
- 本期史料包括 Devin Teske 与 Warren Block 的安装器改动、OpenBSD signify 提交与测试密钥、Julio Merino 的 Kyua 测试框架、pc-sysinstall 脚本化安装器及 pkgsrc 2013Q4 分支。（BSD Now EP19，[91.48-1330.48]，L2）

**史观**：

- 总纲13 法律与道德是利益分配：以 BSD ISC 许可证对 GPL 工具做净室重实现，是许可证边界对工程行动的直接塑造：一个工具的许可证选择决定了它能否进入基础系统。（BSD Now EP282，[1554.64-1579.10]，L2）
- 总纲10 动手者创造历史：Spotifyd 以 Rust 重写后更容易跨平台，配合 NetBSD 的可移植性传统，把应用生态延伸到从大型机到嵌入式设备等非主流平台。（BSD Now EP282，[851.88-894.04]，L2）
- 总纲9 经验优先：贝尔的回顾强调计算机是“总体设计环境”的产物，成功在于为当下造出正确的机器，呼应经验优先的取向。（BSD Now EP225，[2066.0-2101.76]，L2）
- 总纲4 分离聚合是永恒规律：PDP-11 的开放架构使任何按规范实现者皆可称 PDP-11，DEC 内部形成快慢两条实现路线，体现分离聚合的规律。（BSD Now EP225，[2184.72-2209.84]，L2）
- 总纲10 动手者创造历史：发布工程回顾强调除 Glen Barber 外还有大量不在聚光灯下的人协作，凸显动手者叙事。（BSD Now EP225，[3746.94-3769.1]，L2）
- 总纲10 动手者创造历史：BSD Taiwan 会议以少数组织者承担大量工作、注册超预期，呈现社区由动手者维系。（BSD Now EP221，[1782.4-1824.5]，L2）
- 总纲9 经验优先：OpenBSD hackathon 从“提前数日搭建服务器”演变为“带上最新快照即可”，被叙述为工程工具简化带来的经验积累。（BSD Now EP221，[4962.9-5048.74]，L2）
- 总纲5 没有必然性，只有偶然性：ZFS 加密与 RAID-Z 扩容的时间线表明功能落地受社区贡献节奏约束，而非线性规划。（BSD Now EP221，[4755.94-4772.46]，L2）
- 总纲10 动手者创造历史：个人开发者因自身需要推进无线与存储特性，特性落地依赖具体动手者的持续投入。（BSD Now EP193，[147.78-648.52]，L2）
- 总纲5 没有必然性，只有偶然性：OpenBSD 停止发行 CD 与 LibreSSL 分叉均由 Heartbleed、GPLv3 等具体事件触发，而非抽象规划。（BSD Now EP193，[1277.66-1583.66]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 各发行版分叉后又聚合，zpool checkpoint 等特性先经 hackathon 快速原型，再逐步回上游。（BSD Now EP193，[1810.2-2535.42]，L2）
- 总纲10 动手者创造历史：Patrick Hausen 从组装 PC、接触 Xenix 到部署 FreeBSD 的历程表明，历史由持续动手运维的人塑造。（BSD Now EP192，[1068.62-1274.52]，L1）
- 总纲9 经验优先：主持人与其访谈对象依据长期实际部署经验判断 BSD 相对 Linux 的稳定性与文档质量，经验先于抽象理论。（BSD Now EP192，[1425.04-1488.94]，L1）
- 总纲4 分离聚合是永恒规律：pNFS 把单一 NFS 服务拆分为元数据节点与数据节点，再聚合为统一文件系统，体现分离聚合的循环。（BSD Now EP192，[5241.34-5535.38]，L2）
- 总纲10 动手者创造历史：主持人长期义务制作播客记录社区动态，节目史由持续动手的人维系。（BSD Now EP185，[61.44-141.04]，L1）
- 总纲5 没有必然性，只有偶然性：主持人更替源于个人职业压力等具体境遇，而非预先规划。（BSD Now EP185，[96.3-118.44]，L1）
- 总纲12 科学是形式主义：FreeNAS 坚持“尽早发布、频繁发布”，以迭代验证用户真实需求。（BSD Now EP185，[890.86-923.96]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Ken Moore 以个人开发并维护 Lumina 的方式为 FreeBSD 桌面生态提供原生工具。（BSD Now EP54，[3448.90-3526.78]，L1）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：Lumina 的轻量取向与 KDE、GNOME 等桌面被置于并置关系，强调按需求选择而非优劣评判。（BSD Now EP54，[3970.94-3977.02]，L1）
- 总纲24 美是消解性的体验：总纲24 美是消解性的体验：Lumina 以极简界面、壁纸与插件化桌面提供一种消解复杂性的日常使用体验。（BSD Now EP54，[3428.30-3436.06]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Devin Teske、Warren Block、Julio Merino 等以具体工程改进安装器与测试基础设施，推动发行流程演进。（BSD Now EP19，[1069.32-1300.48]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：sysinstall 被 bsdconfig 与脚本化安装器取代，旧安装方式随版本演进而淘汰。（BSD Now EP19，[2238.16-2399.96]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：installfest 将五大 BSD 并置演示，体现多分支在本体论上平等对待的叙述方式。（BSD Now EP19，[1011.60-1046.72]，L2）

**辨析**：

- openrsync 的“净室重实现”表述来自作者与主持人转述，其兼容性目标（3.1.3 基准）与安全机制（pledge/unveil）在 2019 年初仍属进行时状态，须以项目仓库与后续发布记录核验完成度。　[存疑脚注] 项目完成度与最终进入基础系统的时点未经一手仓库核对。（BSD Now EP282，[1554.64-1695.70]，L4）
- PDP-11 回顾系博客作者对贝尔论文的二手转述，且转写将“Maria Strobel”等专名误转，人名与具体数字须核对原文。　[存疑脚注] 专名与数字须以贝尔论文原文核实（BSD Now EP225，[1927.8-1965.5]，L4）
- BSD Taiwan 报名人数（预期 80、注册 120 余）系主持人口述，无官方书面数字复核。　[存疑脚注] 报名数字系口述，须以会议官方记录核实（BSD Now EP221，[1772.4-1782.4]，L4）
- 转写将多个人名与机构名误转（如“Gambold”“Nanshiao”等），人物身份须核对会议议程。　[存疑脚注] 转写人名拼写不可靠（BSD Now EP221，[1146.76-1173.16]，L4）
- [存疑脚注] DistroWatch 评测中遇到的硬件问题可能由评测者特定的 AMD APU 环境所致，未必能推广为 TrueOS 的普遍缺陷。　[存疑脚注] 单一评测者的硬件结论，需多源交叉验证。（BSD Now EP193，[2963.24-3020.76]，L4）
- [存疑脚注] Patrick Hausen 所忆 1994 年与 Jordan Hubbard 会面、Walnut Creek 光盘数量等细节系当事人多年后回忆，需与 Walnut Creek 档案交叉核验。　[存疑脚注] 当事人回忆性细节，缺乏独立一手档案印证。（BSD Now EP192，[1279.84-1320.66]，L4）
- [存疑脚注] FreeNAS 9.10.3 的发布时间与 MinIO、iocage 等功能的落地范围在访谈时尚属计划，须以最终发布说明为准。　[存疑脚注] 计划性披露，需与正式发布记录核验。（BSD Now EP185，[668.32-869.02]，L4）
- Lumina 0.6.2 仍为 beta，转录中对其稳定性与未来形态的判断属开发者预期，最终演进需以 PC-BSD/TrueOS 历史为准。　[存疑脚注] 开发者对未来稳定性的判断为单方预期，未形成多源佐证（BSD Now EP54，[3513.38-3526.78]，L4）
- OpenBSD 5.4 时期 signify 仍为测试密钥，正式签名需待 5.5；各 BSD 安装器细节为主持人实操演示，与官方手册的一致性需逐项复核。　[存疑脚注] 安装器细节与 signify 状态以官方发布说明为准，需交叉验证。（BSD Now EP19，[321.52-347.64]，L4）

**文献**：

- [BSD Now EP282] Pennington J. BSD Now: 282: Open the Rsync[EB/OL]. (2019-01-24)[2026-08-15]. <https://www.bsdnow.tv/282>.
- [BSD Now EP225] Pennington J. BSD Now: 225: The one true OS[EB/OL]. (2017-12-20)[2026-08-15]. <https://www.bsdnow.tv/225>.
- [BSD Now EP221] Pennington J. BSD Now: 221: BSD in Taiwan[EB/OL]. (2017-11-22)[2026-08-15]. <https://www.bsdnow.tv/221>.
- [BSD Now EP193] Pennington J. BSD Now: 193: Fire up the 802.11 AC[EB/OL]. (2017-05-10)[2026-08-15]. <https://www.bsdnow.tv/193>.
- [BSD Now EP192] Pennington J. BSD Now: 192: SSHv1 Be Gone[EB/OL]. (2017-05-03)[2026-08-15]. <https://www.bsdnow.tv/192>.
- [BSD Now EP185] Pennington J. BSD Now: 185: Exit Interview[EB/OL]. (2017-03-16)[2026-08-15]. <https://www.bsdnow.tv/185>.
- [BSD Now EP54] Pennington J. BSD Now: 54: Luminary Environment[EB/OL]. (2014-09-10)[2026-08-15]. <https://www.bsdnow.tv/54>.
- [BSD Now EP19] Pennington J. BSD Now: 19: The Installfest[EB/OL]. (2014-01-08)[2026-08-15]. <https://www.bsdnow.tv/19>.

<!-- /PODCAST_REVIEW -->
