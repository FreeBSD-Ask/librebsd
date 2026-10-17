---
chapter: 第 123 章
id: CH123
volume: 第06卷-freebsd的核心技术革新
---

# 第 123 章 freebsd9x版本基础与内核子系统


## 史料

- [DB:research_notes:blocks:534] 关键词“内核子系统”命中：史实考据：Antti Kantee 的 Aalto 大学 2012 年博士学位论文，系统阐述 anykernel 与 r…
- [DB:research_notes:blocks:1085] 关键词“内核子系统”命中：史实考据：DragonFly BSD 项目在 USENIX 2005 Annual Technical Conferen…
- [DB:research_notes:blocks:5483] 关键词“内核子系统”命中：史实考据：NetBSD 1.3 官方发布说明，确认发布日期为 1998 年 1 月 9 日；二进制发布支持 14 个平台…

## 要点

- FreeBSD 9.0 开发始于 stable/8 分支冻结后，历时近两年（2010 年中至 2012.1.12 正式发布），是 FreeBSD 历史上开发周期最长的大版本之一；9.x 系列包含四个 RELEASE：9.0（2012.1.12）、9.1（2012.12.30）、9.2（2013.9.30）、9.3（2014.7.16），无 9.4-RELEASE；9.3 作为 9.x 系列终章获得超长支持周期至 2017.1.1，是生产环境长期部署的 “企业级稳定版”
- Dennis M. Ritchie 于 2011 年 10 月 12 日逝世，距 9.0-RELEASE 发布恰好三个月；FreeBSD 项目在官方公告中明确将 9.0-RELEASE 献给 Ritchie："The FreeBSD Project dedicates the FreeBSD 9.0-RELEASE to the memory of Dennis M. Ritchie, one of the founding fathers of the UNIX operating system“；献辞指出 ”the fact that his work of so many years ago continues to influence new design decisions to this very day speaks for the brilliant engineer that he was"
- 2012 年 11 月 11 日，FreeBSD 基础设施中两台机器被检测到入侵——受影响的是旧版第三方包构建基础设施头节点（“pointyhat”）；入侵原因是某位开发者的 SSH 密钥泄露，而非 FreeBSD 代码本身存在漏洞；入侵者最早可能于 2012 年 9 月 19 日即获得访问权限；项目于 11 月 17 日公开通报，大量基础设施机器下线审计，导致 9.1-RELEASE 发布延迟且初始仅含 GNOME/KDE 最小包集，完整包集直至 2013 年 4 月 30 日才恢复；Subversion 源码仓库、base 系统均未被篡改
- 9.0-RELEASE 安全支持原计划至 2013.1.31，因 9.1 发布延迟顺延至 2013.3.31；9.1-RELEASE 作为延长支持版本 EOL 为 2014.12.31；9.2-RELEASE 支持至 2014.9.30；9.3-RELEASE 支持至 2017.1.1——这一超长支持周期使 9.3 成为 FreeBSD 历史上支持时间最长的 .0 大版本系列之一，被众多企业和托管服务商长期部署。9.x 系列版本发布与支持周期关键数据（tagger_date、target_commit_hash 经 **freebsd.duckdb** `tags` 表验证）汇总见下表。
- **bsdinstall(8)** 由 Nathan Whitehorn（nwhitehorn@）主导开发，在 9.0-RELEASE 中正式取代使用了近 20 年的 **sysinstall(8)**；bsdinstall 采用 shell 脚本与分布式模块化设计，而非 sysinstall 的单体 C 程序架构；核心设计目标是可扩展性——sysinstall 因硬编码逻辑难以支持新特性（如 ZFS、GPT、UEFI），bsdinstall 通过脚本化架构解决此问题；9.0-RELEASE 的 ISO 镜像默认使用 bsdinstall，但 sysinstall 仍存在于系统中以兼容旧脚本

## 史观

- 总纲第 21 条——革命与改革是历史方法论的分歧：9.x 是 8.x 时代的“终结”与 10.x 时代的“延续”之间的过渡——它既完成了 bsdinstall、SUJ、ZFS v28、Capsicum 等 10.x 时代核心特性的落地与验证，又保持了 GCC 4.2.1、pkg_install 等旧栈作为默认，为许可证纯洁化大迁移（GCC→Clang、pkg_install→pkg、BIND→Unbound）铺平了道路——以改革而非革命的节奏完成代际更替。
- 专题语（不设总纲条号）——支持周期与用户采用模式：9.3 获得超长支持，是因为 10.x 系列引入 Clang 默认、pkg 取代 pkg_install 等重大变化导致许多生产环境不愿升级，9.3 成为“旧世界”的最后堡垒；这种“LTS 式”社区自发延长支持的模式，与 Linux 发行版商业驱动的 LTS 形成对照
- 辨析：FreeBSD 官方从未使用 “LTS”
- 专题语（不设总纲条号）——安装器的工程范式迁移：sysinstall 到 bsdinstall 的更替体现了“单体 → 模块化”、“C 硬编码 → 脚本化组合”的迁移；sysinstall 是 1990 年代 BSD 安装器的典型（类 sysconfig 界面、静态菜单），bsdinstall 则面向 ZFS、虚拟化、云部署等 2010 年代新需求设计
- 总纲第 10 条——动手者创造历史：SUJ 是 McKusick 作为 UFS/FFS 原始设计者对其作品的“晚年修订”——soft updates 本身是 Ganger & Patt 于 1990 年代提出的元数据一致性方案，McKusick 在 FreeBSD 中实现并维护 15 年后，通过 SUJ 解决了其最后的痛点（崩溃后 fsck 时间）；这体现了核心系统软件“作者终身维护”的 BSD 传统（soft updates 自 1990 年代方案到 SUJ 的 15 年演进即此传统的实例）。
- 总纲第 13 条——法律与道德是利益分配：ZFS v28 成为 FreeBSD（以及后来整个开源社区）ZFS 演进的基础版本具有历史决定性——Oracle 闭源后，illumos 成为 ZFS 开源开发的主力，FreeBSD 从 illumos 持续移植改进；v28 作为 CDDL 许可的最后共同祖先版本，奠定了 BSD/Linux/macOS ZFS 生态的技术基础

## 辨析

- 9.x 常被叙事为 “新一代”（标题中 “新一代” 标签），但技术上多数核心特性在 8-CURRENT 已开始开发（如 USB 栈重写始于 8.0），9.0 是集成与稳定化而非全新革命；9.3 的超长支持周期（至 2017）与 10.x 系列较短的支持周期（10.0 至 2015.1.31）形成对比，表明生产用户对 9.x 稳定性的认可；**数据库验证结论**：9.x 四个 RELEASE 的 tagger_date 与 target_commit_hash 均经 tags 表逐项验证，与官方公告日期一致。
- FreeBSD 官方从未使用 “LTS” 术语，但 9.3 的实际支持周期（2014.7-2017.1，约 2.5 年）远超常规 RELEASE 支持周期（通常约 1 年）；这表明支持周期由用户需求与安全团队资源共同决定，而非硬性政策
- 文献：FreeBSD Security Team. FreeBSD Security Support [Z]. security.freebsd.org；各版本

- bsdinstall 的 “shell 脚本驱动” 常被误解为 “用 Lua 驱动”——bsdinstall 实际主要使用 POSIX shell 脚本配合 **dialog(1)** 提供文本界面，Lua 是在更晚版本（10.x 之后）才逐步引入部分组件；9.0 的 bsdinstall 尚不支持 ZFS root 自动安装（需手动配置），ZFS 引导的官方安装支持在 10.x 才完善

- SUJ 不是 “日志文件系统”（journaling filesystem）的完整实现——它仅对 soft updates 元数据更新增加意向日志以加速恢复，而非像 ext3/ext4、XFS 那样对元数据甚至数据进行完整日志记录；这一设计选择保持了 soft updates 的性能优势，同时消除了其最显著的运维缺陷（服务器异常断电后 fsck 时间与文件系统大小成正比）
  - 文献：McKus
- ZFS v28 在 FreeBSD 9.0 中状态为 “Production 但非默认根文件系统”——作为数据存储卷使用已相当稳定，但作为 root 文件系统仍需大量手动调整，不适合普通用户；10.0 时期 bsdinstall 才逐步加入自动 ZFS root 配置
  - 文献：svn commit r219089；FreeBSD 9.0-RELEASE Release Notes（ZFS 章节）。

## 文献

- FreeBSD Release Engineering Team. FreeBSD 9.0-RELEASE Announcement [Z]. 2012-01-12；FreeBSD Release Engineering Team. FreeBSD 9.3-RELEASE Announcement [Z]. 2014-07-16；Lucas M W. FreeBSD Mastery: Specialty Filesystems [M]. Tilton: Tilted Windmill Press, 2016；FreeBSD Project. release/9.0.0. freebsd-src
- FreeBSD Security Team. FreeBSD Security Support [Z]. security.freebsd.org；各版本 Release Announcement Support 章节［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD 9.0-RELEASE Release Notes [Z]. docs.freebsd.org；Whitehorn N. bsdinstall: A New Installation System for FreeBSD [C]//BSDCan 2011. Ottawa, 2011；**bsdinstall(8)** man page

## 存目（原 122.2.2/122.3.2/122.4.2/122.5.2/122.6.2 抢救残片）

- 上述五节为本 123 章主题（9.x 子系统史）的旧章号抢救残片，其正本体对应磁盘节文件 123.2（bsdinstall）、123.4（ZFS v28/TRIM/lz4）、123.5（CAM/ATA 与 USB 栈）、123.6（网络栈改进含 NFSv4）——残片均截断且含错位文献行，已按正本体删除；其中“122.3.2 UFS2 TRIM”题名与所引文献（实为 ZFS TRIM）错位，一并归档处理。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1230 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1230`；w172 YouTube 章节路由采纳）

据 BSDCan 2011 讲者口述：FreeBSD 的 daemon（转写音 demon）图形在 4.3BSD 中继续沿用。（YouTube EP0wIxny-n_Mg，[58.199-60.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1229 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1229`；w172 YouTube 章节路由采纳）

据 BSDCan 2011 讲者口述：FreeBSD 系统里的 daemon 图形最早出现在 4.2BSD 手册中。（YouTube EP0wIxny-n_Mg，[48.84-52.349]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-275 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-275`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：syscaller 工具在 FreeBSD 内核中发现了数百个缺陷。（YouTube EP91lRj5Qwh1s，[668.32-670.31]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-276 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-276`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：Andy Turner 多年前曾从事 FreeBSD 的 arm64 相关工作。（YouTube EP91lRj5Qwh1s，[1040.16-1042.47]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-580 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-580`；w172 YouTube 章节路由采纳）

据〔Fall 2024 FreeBSD Summit〕讲者口述：FreeBSD 中有 60% 的代码属于设备驱动；若 ZFS 不再位于内核之中，这个比例会上升到 80%。（YouTube EPHBo8QiWpTWc，[64.199-72.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-747 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-747`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者 A. Rao 口述：FreeBSD 内核中存在与调度器直接关联的类，在其 FreeBSD 内核锁基础设施演讲中被当作既有事实单独点出。（YouTube EPMApy8-lN49A，[1008.28-1015.13]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1021 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1021`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Marshall Kirk 口述：瑞士联邦理工学院研究组曾对比 FreeBSD ULE 与 Linux CFS 调度器，所用 ULE 取自 FreeBSD 11.1。（YouTube EPV6AxdJ-jdUg，[2662.96-2685.51]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1020 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1020`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Marshall Kirk 口述：ULE 调度器首次出现在 FreeBSD 5。（YouTube EPV6AxdJ-jdUg，[453.12-460.95]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1146 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1146`；w172 YouTube 章节路由采纳）

据〔freebsd 与 gdb 演讲〕讲者口述：GDB 架构包括 FreeBSD amd64 ELF、NetBSD amd64 ELF 与 Linux i386（YouTube EPXVkOmFCQr9o，[29.759-39.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1125 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1125`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018〕讲者 Warner Losh 口述：FreeBSD 1.0 内核体积约 534K，被讲者作为 FreeBSD 内核体积逐年增长讨论的起点（现场有人估约每年 20%）。（YouTube EPXgnUWG5mAAQ，[135.31-152.37]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1124 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1124`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018〕讲者 Warner Losh 口述：图中绿色线代表 PDP-11 与 VAX 两代硬件，二者规模相当；红色数据来自 FreeBSD。（YouTube EPXgnUWG5mAAQ，[657.71-666.19]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-289 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-289`；w172 YouTube 章节路由采纳）

据〔So you want to add a system call 演讲〕讲者 Brooks Davis 口述：其十五年前或更早曾尝试向 FreeBSD 添加系统调用（YouTube EP_5LF_0GIpi8，[26.08-33.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-290 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-290`；w172 YouTube 章节路由采纳）

据〔So you want to add a system call 演讲〕讲者 Brooks Davis 口述：FreeBSD 与几乎每一个系统调用保持兼容可回溯至 FreeBSD 1.0（YouTube EP_5LF_0GIpi8，[175.68-182.149]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-312 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-312`；w172 YouTube 章节路由采纳）

据〔FreeBSD 内核锁基础设施演讲〕讲者 A. Rao 口述：FreeBSD 5.x 时期开展 SMP 新世代计划以推进锁基础设施改进。（YouTube EPa3XLROUjXic，[263.199-268.109]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-406 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-406`；w172 YouTube 章节路由采纳）

据〔FreeBSD Summit, Fall 2024〕讲者口述：该内核能导入 ZFS 存储池，并可在写入 UFS 的场景下工作（YouTube EPd66YD7ypM6A，[914.839-920.87]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-405 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-405`；w172 YouTube 章节路由采纳）

据〔FreeBSD Summit, Fall 2024〕讲者口述：为缩小救援内核体积，其排除了 SMP、WITNESS 等大量内核选项（另有转写音作“CIS CLE”的项）（YouTube EPd66YD7ypM6A，[317.16-325.23]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1012 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1012`；w172 YouTube 章节路由采纳）

据〔Fall 2024 FreeBSD Summit〕讲者口述：并发套件提供宏，用于在链表和队列上执行原子操作（转写音作 cues）。（YouTube EPuS4i6iobXAk，[566-577.91]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1182 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1182`；w172 YouTube 章节路由采纳）

据〔内核 Fuzzing 分享〕讲者 Andrew Turner 口述：本次谈内核 fuzzing 状态覆盖 FreeBSD、NetBSD、OpenBSD 三个项目。（YouTube EPyyQFdWJDmh0，[34.96-46.58]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1183 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1183`；w172 YouTube 章节路由采纳）

据〔内核 Fuzzing 分享〕讲者 Andrew Turner 口述：FreeBSD 与 NetBSD 已具备相关 evidence support，后续演示具体原因。（YouTube EPyyQFdWJDmh0，[511.26-520.88]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1430 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1430`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Kernel Internals, Dr. Marshall Kirk McKusick〕讲者口述：伯克利 UNIX 上开发出来的软件由 Bill Joy 开始打包并以“Berkeley Software Distributions”之名分发，这个名称很快被缩短为 BSD，此后 BSD 以每年一次的发行持续了将近十五年。（YouTube EPnwbqBdghh6E，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1431 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1431`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Kernel Internals, Dr. Marshall Kirk McKusick〕讲者口述：伯克利最后一次发行之后，出现了两个组织继续维护 BSD，其一是 NetBSD，首要目标是为尽可能多的架构提供支持，从微波炉一直到 Cray XMP，他称到讲座当时已接近六十种架构。（YouTube EPnwbqBdghh6E，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1432 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1432`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Kernel Internals, Dr. Marshall Kirk McKusick〕讲者口述：另一个组织是 FreeBSD，目标是把 BSD 跑起来并在 PC 架构上支持尽可能广的设备集合，同时希望让系统尽量容易安装，以吸引更广泛的开发者群体。（YouTube EPnwbqBdghh6E，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1433 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1433`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Kernel Internals, Dr. Marshall Kirk McKusick〕讲者口述：他归纳 UNIX 区别于前代系统的关键想法之一是统一的描述符空间——一个描述符可以引用任意一种 I/O 设备乃至任意 I/O 通道，终端、文件、磁盘各有各的描述符，程序无需知道其类型即可对其读写。（YouTube EPnwbqBdghh6E，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1469 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1469`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kirk McKusick 在 EuroBSDcon 2012 题为《An Overview of Locking in the FreeBSD Kernel》的演讲〕讲者口述：在多线程内核出现之前的旧式 FreeBSD 内核同步方式中，被保护的资源上定义有若干标志：其中锁标志置位即表示该资源正在被使用、清除则表示可用，据此可判断是否有其他进程正在对该资源做读或写；一旦判定他人正在占用，请求者便无法取得该资源，转而设置等待标志，随后去睡眠等待。（YouTube EPUfiTV9QWhM4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1470 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1470`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kirk McKusick 在 EuroBSDcon 2012 题为《An Overview of Locking in the FreeBSD Kernel》的演讲〕讲者口述：FreeBSD 内核锁对硬件的最低要求是 test and set，而在现代硬件上则是比较交换指令（compare and swap），FreeBSD 采用的正是后者；讲者提醒必须留意这些指令的实际使用方式，并指出多数架构上存在轻量与重量两类 test and set 或 compare and swap。（YouTube EPUfiTV9QWhM4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1471 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1471`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kirk McKusick 在 EuroBSDcon 2012 题为《An Overview of Locking in the FreeBSD Kernel》的演讲〕讲者口述：讲者介绍 FreeBSD 为避免死锁而引入的见证代码（witnessing code）：它记录各锁的类别及其次序层级，并监视每一次锁的分配、获取与释放，以确保加锁规则得到遵守。（YouTube EPUfiTV9QWhM4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1472 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1472`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Kirk McKusick 在 EuroBSDcon 2012 题为《An Overview of Locking in the FreeBSD Kernel》的演讲〕讲者口述：讲者指出，读多锁的最优实现方案被 IBM 持有专利：IBM 允许 GPL 代码免费使用该受专利保护的实现，但非 GPL 软件则不得使用这一专利。（YouTube EPUfiTV9QWhM4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1498 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1498`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis《Address space reservations: Re-thinking address space management for pointer provenance》演讲〕讲者口述：CheriBSD 是一个由讲者所在团队长期维护的 FreeBSD 分叉，Cheri ABI 是其默认进程 ABI；在该 ABI 下内核为进程的全部映射提供有界指针（能力），程序虽有一段地址空间基址，但在内核授予特定比特的访问能力之前无法访问其中任何部分。（YouTube EP1VVVgOIZMp8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1499 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1499`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis《Address space reservations: Re-thinking address space management for pointer provenance》演讲〕讲者口述：CheriBSD 的做法是预留（reservation）失效后被完全取消映射后不立即回收复用，而是放入隔离区（quarantine）：其中既不能被重新映射、也不能被访问，讲者称之为一种能力撤销（revocation）机制。（YouTube EP1VVVgOIZMp8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1500 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1500`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis《Address space reservations: Re-thinking address space management for pointer provenance》演讲〕讲者口述：为在预留时表达一个映射允许的最大页保护上限，讲者新增了一个标志并把它引入了 FreeBSD，即 prop_max（转写音 prop Max／Max prot）一组标志，讲者自陈其在 FreeBSD 中不过算是一种较弱的缓解措施。（YouTube EP1VVVgOIZMp8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1501 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1501`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis《Address space reservations: Re-thinking address space management for pointer provenance》演讲〕讲者口述：CheriBSD 没有原生 CHERI 硬件时只能靠模拟器运行（QEMU，转写音 qimo／kuu）；在有 Cheri 硬件的情形下，讲者表示 morello（转写音 Mel）硬件上已有 bhyve（转写音 beehive）支持，并且在 RISC-V（转写音 risk five／risk 5）上已做到“first light”级别的 bhyve 支持。（YouTube EP1VVVgOIZMp8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1571 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1571`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔John Baldwin 讲《Advanced ptrace() usage on FreeBSD》〕讲者口述：FreeBSD 在 FreeBSD 5 引入内核线程后，多线程进程里任一线程在内核遇到事件、要向调试器上报时，内核会对其余所有线程做同步、强制全体停住暂挂在内核中。（YouTube EPQDjkj-URxrM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1572 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1572`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔John Baldwin 讲《Advanced ptrace() usage on FreeBSD》〕讲者口述：讲者称 FreeBSD 11.0 加回的 LWP 事件留有一处属于自己写下的内核 bug：新增“线程出生”事件时，detach 路径未清除该标志，脱离调试后醒来、带着出生事件的新线程会给自己发一个真正的 SIGTRAP 而 core dump；修复当时仍在评审、尚未提交。（YouTube EPQDjkj-URxrM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1573 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1573`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔John Baldwin 讲《Advanced ptrace() usage on FreeBSD》〕讲者口述：FreeBSD 以 ptrace 操作 PT_FOLLOW_FORK 实现 GDB 所称的 fork following，开启后内核会自动附加到被调试进程 fork 出的新子进程。（YouTube EPQDjkj-URxrM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1574 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1574`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Colin Percival 讲《Profiling the FreeBSD kernel boot》〕讲者口述：启动进入内核后，amd64 上先运行机器相关初始化函数，随后进入 machine-independent 启动函数 mi_startup，完成内核初始化的绝大部分工作；其后转入 into init。（YouTube EPHMywejyXB9k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1575 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1575`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Colin Percival 讲《Profiling the FreeBSD kernel boot》〕讲者口述：其中挂载根文件系统，因为没有根文件系统就无法从它运行程序。（YouTube EPHMywejyXB9k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1576 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1576`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Colin Percival 讲《Profiling the FreeBSD kernel boot》〕讲者口述：DTrace 在 FreeBSD 上固然强大，但它依赖 traps、内存分配与线程调度等机制，而他想剖析的阶段发生在这些机制存在之前，因此 DTrace 无法处理整个内核启动过程。（YouTube EPHMywejyXB9k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1577 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1577`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2018 Colin Percival 讲《Profiling the FreeBSD kernel boot》〕讲者口述：他最终为启动剖析新增了一个日志系统：两个文件合计约 150 行代码，内核以 options TS_log 编译，缓冲区分量在编译期指定，默认 256,000 条记录。（YouTube EPHMywejyXB9k，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1658 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1658`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，John Baldwin《Managing Resources in FreeBSD Bus Drivers》〕讲者口述：FreeBSD 中的设备以对象树构建，树中任何带有子节点者即为总线设备（bus device）——一棵树只分叶设备与内部节点两类，而所有内部节点在 FreeBSD 的术语中都是总线设备。（YouTube EPBCM0QSfrog8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1659 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1659`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，John Baldwin《Managing Resources in FreeBSD Bus Drivers》〕讲者口述：内核里的资源管理器在 newbus 最初写成时是专为内核内存场景单独编写的特化实现，因此带有一些历史特性，例如它会保存那些申请了资源的设备引用。（YouTube EPBCM0QSfrog8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1660 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1660`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，John Baldwin《Managing Resources in FreeBSD Bus Drivers》〕讲者口述：bus_generic_rman 一族助手函数由讲者本人编写，虽早在数年前就已写好，直到本次演讲之年（2024 年）才最终并入主干树。（YouTube EPBCM0QSfrog8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1661 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1661`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDCon 2024，John Baldwin《Managing Resources in FreeBSD Bus Drivers》〕讲者口述：讲者自述其在最初为 PCI 驱动引入资源管理器时的做法是一个粗陋的层级越界——把已在低层分配得到的资源一路向上传回设备树的根部去构造映射。（YouTube EPBCM0QSfrog8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1800 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1800`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Writing Custom Command in FreeBSD's DDB Kernel Debugger, John Baldwin, EuroBSDcon 2022〕讲者口述：据讲者所知，DDB 最早是随 386BSD 移植进入 BSD 阵营的，但 386BSD 的详细历史并不清楚，他只能判断它出现在那条时间线的某个时点，随后才辗转进入 FreeBSD。（YouTube EPsZMcVZjFW4g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1801 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1801`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Writing Custom Command in FreeBSD's DDB Kernel Debugger, John Baldwin, EuroBSDcon 2022〕讲者口述：若自定义命令在 DDB 中执行时发生 fault，DDB 会恢复并回到其主解析循环；实现上是在调用命令函数之前先 setjump（转写音作 set jump），一旦出错便 longjmp 跳回，其直接后果是 DDB 中不存在清理（cleanup）的概念。（YouTube EPsZMcVZjFW4g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1802 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1802`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Writing Custom Command in FreeBSD's DDB Kernel Debugger, John Baldwin, EuroBSDcon 2022〕讲者口述：John Baldwin 自认 db_pager_quit 这个全局变量的作者，添加时间大约在 20 年前；有听众反馈某些 DDB 命令并未正确遵循 pager 的行为。（YouTube EPsZMcVZjFW4g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1803 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1803`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Writing Custom Command in FreeBSD's DDB Kernel Debugger, John Baldwin, EuroBSDcon 2022〕讲者口述：讲者称近一两年间由 ISILON 回馈给 FreeBSD 团队的一项贡献，是加入一个类似底层控制台那样的 debug 网络栈，从而可以真正通过网络连接使用 GDB。（YouTube EPsZMcVZjFW4g，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1860 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1860`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2022 线上会议“Speeding up the FreeBSD boot”Colin Percival〕讲者口述：2017 年他在 FreeBSD 内核加入了 ts_log 框架，本质上是一组 C 宏，除非在内核配置里设置 options ts_log，否则编译后完全空转，对性能没有影响；启用后由 ts_enter／ts_exit 两枚宏记录进入与退出函数的时间戳和函数名，纯 C 宏实现、不依赖编译器魔法插桩。他用它打点了 hammer_time、mi_startup、start_init、delay 例程、向控制台输出的 vprintf、所有 CIS 例程（CIS init 本身是宏，因此加几行代码即可让内核全部 CIS 例程被打点）、设备 probe／attach 与 vfs_mount，并据此生成了 FreeBSD 11.0 发布版的内核启动火焰图。（YouTube EP10XRCiBtyhA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1861 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1861`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2022 线上会议“Speeding up the FreeBSD boot”Colin Percival〕讲者口述：FreeBSD 当时使用 BIOS 传统引导（该模式可追溯到 1980 年代 IBM PC），它的问题是仍运行在 16 位模式下完成磁盘 I/O，因此必须在 1 兆字节寻址边界之下使用弹跳缓冲，引导加载程序每次只能做 16 千字节大小的 I/O，比 64 千字节以上的顺序读慢；加之 EC2 实例的 VGA 文本模式极慢，每次触碰都会陷入并切换 CPU 模式去渲染字形，约每次 6 万时钟周期，所以他建议这些实例类型改用 UEFI 引导。（YouTube EP10XRCiBtyhA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1862 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1862`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2022 线上会议“Speeding up the FreeBSD boot”Colin Percival〕讲者口述：他展示的自由BSD 11.1 发布版引导火焰图整个启动过程约 28 秒；同一台 EC2 c5.xlarge 实例运行 FreeBSD 13.1 发布版时，整个引导过程约 9 秒半，引导加载段明显缩短，内核段时间从约 10 秒降到约 1 秒；若对该实例做重启而非冷启动，因磁盘已部分缓存，引导加载与用户态段都更快，降到约 4 秒半。（YouTube EP10XRCiBtyhA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1863 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1863`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2022 线上会议“Speeding up the FreeBSD boot”Colin Percival〕讲者口述：FreeBSD 内核随机数生成器的设备驱动里有一条注释说为了阻止写请求压垮它而引入一段恼人的延迟，实际是每次向该设备写入时延迟 100 毫秒；启动时用户态要往 /entropy/entropy 与 /var/db/entropy 等文件写入随机启动脚本抛下的熵位，讲者推测这条延迟源于一种没有根据的担忧，即大量非随机输入会削弱随机数生成器的输出，但他指出这在二十三十年前的老式随机数生成器上成立，现代密码学级随机数生成器不受影响。他直接删掉这 100 毫秒延迟，引导时间随即快了 900 毫秒。（YouTube EP10XRCiBtyhA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1913 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1913`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis，EuroBSDcon 2022 演讲《So you want to add a system call?》〕讲者口述：FreeBSD 支持自其起源以来的几乎每一个系统调用（讲者口报为 four three uh vsd，即 4.3BSD），因此系统调用基本上永远都在，FreeBSD 几乎能运行任何曾在 FreeBSD 系统上运行过的二进制；正因如此他告诫不要无端添加系统调用，以免累积维护负担与攻击面。（YouTube EP4h0GCzFUyU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1914 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1914`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis，EuroBSDcon 2022 演讲《So you want to add a system call?》〕讲者口述：他说 FreeBSD 相对 Linux 的一大优点是每个系统调用在所有架构上编号相同；Linux 则沿用该移植创建时主流 UNIX 平台的编号，他举了 Solaris 与 hpux 两个例子。（YouTube EP4h0GCzFUyU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1915 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1915`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis，EuroBSDcon 2022 演讲《So you want to add a system call?》〕讲者口述：他在把 FreeBSD32 兼容处理自动化的过程中发现，实际上有两个系统调用一直是坏的、从未真正可用过；他自承记不清是哪两个，只说他想起来是 P read V 与 P right V（即 preadv、pwritev），推测其末参 offset 一向为零且使用者体量又小，才偶然碰巧能用。（YouTube EP4h0GCzFUyU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1916 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1916`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis，EuroBSDcon 2022 演讲《So you want to add a system call?》〕讲者口述：为在 CherryBSD 上运行混合代码，他们新增了一层基于 FreeBSD32 的 32 freebsd32 compound layer 兼容层——既有代码可在 Cherry 处理器上无收益也无代价地运行，部署风险很小，随逐步采用而收益递增。（YouTube EP4h0GCzFUyU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1917 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1917`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Colin Percival，讲座 P05A《Profiling the FreeBSD kernel boot》〕讲者口述：他剖析 FreeBSD 启动时发现 vm_page 数组（转写音作 vm page array）约耗 20 毫秒；他自己新买的笔记本有 32GB 内存，而朋友的一台机器有两 TB 内存，此处耗时就要长得多。（YouTube EPNeJ2ztPasso，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1918 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1918`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Colin Percival，讲座 P05A《Profiling the FreeBSD kernel boot》〕讲者口述：他在 FreeBSD 系统启动非常靠前的位置量到一次约一秒的停顿，原因是内核等的是 1.19Hz 的基本 PC 定时器走完节拍，他口报为 one point one something nine Hertz。（YouTube EPNeJ2ztPasso，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1919 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1919`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Colin Percival，讲座 P05A《Profiling the FreeBSD kernel boot》〕讲者口述：为覆盖整个 FreeBSD 内核初始化过程，他自写了一套名为 PS log x half log 2（转写音，应为 pslogx／halflog2）的日志设施，在源码树中只占很小的几个文件——头文件提供宏接口，C 文件里一个函数负责反向遍历、另一个负责写入记录。（YouTube EPNeJ2ztPasso，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1920 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1920`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Colin Percival，讲座 P05A《Profiling the FreeBSD kernel boot》〕讲者口述：该缓冲区编入 256000 条记录，其中他这台笔记本的启动约产出 90000 条；他引 Bill Gates（比尔·盖茨）一句这应该够所有人用了，并自承这话也许并非盖茨所说。（YouTube EPNeJ2ztPasso，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2001 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2001`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Fuzzing the kernel - Porting the Clang Sanitizers to FreeBSD 演讲〕讲者口述：三大 BSD 都已各自提交了一个覆盖率 sanitizer 的版本，并认为是各家独立实现的。（YouTube EP1tYtT8Jk21c，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2002 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2002`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Fuzzing the kernel - Porting the Clang Sanitizers to FreeBSD 演讲〕讲者口述：该内核模糊测试器支持 FreeBSD、NetBSD 与 OpenBSD，并且非常擅长在内核里找出 panic（内核崩溃）。（YouTube EP1tYtT8Jk21c，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2003 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2003`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Fuzzing the kernel - Porting the Clang Sanitizers to FreeBSD 演讲〕讲者口述：三大 BSD 之间确实共享未定义行为（UB）sanitizer 的代码库，因为据他所知它完全基于 micro UB 那一套（在 user space 下同样可用）；而 K-COV 则是有三套完全独立的实现。（YouTube EP1tYtT8Jk21c，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2004 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2004`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Fuzzing the kernel - Porting the Clang Sanitizers to FreeBSD 演讲〕讲者口述：freebsd 例如已有查找 use after free（释放后使用）问题的工具；但他指出问题在于：你察觉到发生了解放后使用，是在尝试进行下一次分配的那一刻，而不是在释放发生的那一刻。（YouTube EP1tYtT8Jk21c，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2015 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2015`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Christos Margiolis 演讲“How sound4 works”〕讲者口述：本人自述为 FreeBSD committer，年份自述记不清（转写为 2023），目前以承包（contract）方式与 Foundation 合作从事音频开发。（YouTube EP77STLO_9h14，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2016 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2016`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Christos Margiolis 演讲“How sound4 works”〕讲者口述：FreeBSD 音频内核代码常被称作 PCM，主要是出于历史原因，也因存放代码的目录就叫 PCM；该层是为设备驱动接入而设的通用层。（YouTube EP77STLO_9h14，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2017 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2017`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Christos Margiolis 演讲“How sound4 works”〕讲者口述：FreeBSD 用户态经由 Open Sound System（OSS）API 访问音频，这是一套较老的 API，但稳定、可用，虽有问题，讲者称与另一套或 Windows 的 API 相比更显优雅。（YouTube EP77STLO_9h14，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2018 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2018`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Christos Margiolis 演讲“How sound4 works”〕讲者口述：音频内核模块此前没有任何测试，讲者向测试套件写入了简单测试；另新增浮点采样格式支持，动因之一是 Wine 移植的部分功能因缺少浮点支持而无法工作。（YouTube EP77STLO_9h14，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2160 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2160`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔剑桥大学博士生 Suain Jani（转写音，据标题应为 Zhuo Ying Jiang），演讲“Improvements to FreeBSD KASAN”〕讲者口述：要在 FreeBSD 内核中实现 KASan，须在内核分配器的分配与释放函数里插入投毒例程，因为编译器无法得知这些内核分配器的语义；讲者并说明 FreeBSD 以 KASan mark 函数对内存区间投毒与解毒，并自定义了 FreeBSD 的毒码。（YouTube EPpwwSdQi0NUI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2161 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2161`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔剑桥大学博士生 Suain Jani（转写音，据标题应为 Zhuo Ying Jiang），演讲“Improvements to FreeBSD KASAN”〕讲者口述：FreeBSD 内核分配器（含通用 malloc 分配器）不对已释放内存做隔离：释放某块后立刻分配同尺寸新块，会复用其底层内存，此后通过失效指针访问不再触发故障，导致 use-after-free 漏检。（YouTube EPpwwSdQi0NUI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2162 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2162`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔剑桥大学博士生 Suain Jani（转写音，据标题应为 Zhuo Ying Jiang），演讲“Improvements to FreeBSD KASAN”〕讲者口述：讲者为 FreeBSD 的内核分配器加入红区填充以捕获越界，并以函数 optimal_red_zone_size 按对象大小动态确定红区尺寸，明确该做法与 Linux 相近；其假设是分配越大越可能溢出更远，小分配则较少溢出成倍空间。（YouTube EPpwwSdQi0NUI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2163 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2163`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔剑桥大学博士生 Suain Jani（转写音，据标题应为 Zhuo Ying Jiang），演讲“Improvements to FreeBSD KASAN”〕讲者口述：讲者称本项 FreeBSD KASan 改进受到一项在 CherryBSD 上开展的模糊测试工作启发，并介绍 Cherry 是一种硬件内存安全方案，以不可伪造的能力指针替代普通指针。（YouTube EPpwwSdQi0NUI，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2277 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2277`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sysunit Unit Testing for the FreeBSD Kernel（讲者 Ryan Stone 自述）〕讲者口述：自述为 FreeBSD committer 逾 10 年；本报告介绍其从事的 sysunit 工作，即 FreeBSD 内核单元测试的基础设施。（YouTube EPBVbJ9JDc18c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2278 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2278`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sysunit Unit Testing for the FreeBSD Kernel（讲者 Ryan Stone 自述）〕讲者口述：该方法把一小段内核代码编译为用户态目标并链接进用户态可执行文件，由该可执行文件对其执行测试；被该内核代码依赖的内核编程接口（KPI）由测试替身（test doubles）替换。（YouTube EPBVbJ9JDc18c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2279 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2279`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sysunit Unit Testing for the FreeBSD Kernel（讲者 Ryan Stone 自述）〕讲者口述：选 GTest 的第二条理由是该框架已在 FreeBSD 源码树内——他称树中至少已有两套测试框架，故不必再引入新的。（YouTube EPBVbJ9JDc18c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2354 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2354`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Aymeric Wibo 谈 FreeBSD S0ix 的演讲〕讲者口述：Intel 的工程师（转写音作 Ben Wowski）早在 2018 年就以两个补丁初步做了 FreeBSD S0ix 方面的工作，但要让它真正可用还需要大量后续工作。（YouTube EPRCjPc4X2Edc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2355 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2355`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Aymeric Wibo 谈 FreeBSD S0ix 的演讲〕讲者口述：ACPI S3 进入与退出都很慢且不灵活，较新的 AMD 与 Intel 机架笔记本（Framework）已不再提供 S3，因而无法睡眠，这正是 FreeBSD 需要转向 S0ax/S0i3 的硬件背景。（YouTube EPRCjPc4X2Edc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2356 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2356`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Aymeric Wibo 谈 FreeBSD S0ix 的演讲〕讲者口述：他所用的 USB4 代码继承自 FreeBSD 开发者 Scott Long 早前编写的骨架；本人删去了固件实现的 ICM（内部连接管理器），改为完全由操作系统侧的 host connection manager 处理。（YouTube EPRCjPc4X2Edc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2357 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2357`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Aymeric Wibo 谈 FreeBSD S0ix 的演讲〕讲者口述：他当年度指导一个谷歌编程之夏项目，把 Linux 工具 Powertop 移植到 FreeBSD，这是 FreeBSD 基金会笔记本项目的一部分。（YouTube EPRCjPc4X2Edc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2574 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2574`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Daniel Lovasko〕讲者口述：其目标是让现有分析工具能够检查来自其他架构的内核转储，例如拿到一台 MIPS 机器也能读出当时内核里运行过哪些进程。（YouTube EP4-zPra5hK3E，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2575 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2575`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Daniel Lovasko〕讲者口述：用同一框架可以很快写出 jailstat 之类的工具，在内核的 jail 列表里查出某个 jail 的 IPv4 地址或 jail ID。（YouTube EP4-zPra5hK3E，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2576 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2576`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Daniel Lovasko〕讲者口述：这套方法并不限于 FreeBSD——按 CTF 数据对照，OS X 内核里也有非常相似的对应物，只是 CTF 目前看来更像 FreeBSD 特有的东西。（YouTube EP4-zPra5hK3E，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
