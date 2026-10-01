---
chapter: 第 169 章
id: CH169
volume: 第08卷-freebsd的范式转换
---

# 第 169 章 从 Subversion 到 Git 的迁移历程

## 要点

- FreeBSD 社区关于迁移到分布式版本控制系统的讨论始于 **2010 年代初期**，几乎与 Git 在 Linux 内核成功后开始流行同步；社区评估了多种分布式 VCS 选项，包括 Git、Mercurial（hg）、Bazaar（bzr）等；Git 之所以最终胜出而非 Mercurial 等其他 DVCS，原因包括：(1) Linux 内核采用 Git 产生的网络效应；(2) GitHub 官方只读镜像（github.com/freebsd/freebsd-src）降低浏览与克隆门槛〔存疑：原列举其后各项原文截断，待回源补录〕
- Git 工作组决策过程的一手史料主要包括：(1) freebsd-git@ 邮件列表的公开讨论存档（最完整、最权威）；(2) Git Transition Wiki 页面的历史版本（记录了方案演变）；(3) Ed Maste、Warner Losh 等人的会议演讲和博客文章；(4) Core Team 的公开状态报告；Core Team 内部讨论和投票细节未完全公开，部分决策理由只能从公开信息推断
- FreeBSD-doc Subversion to Git 迁移公告邮件经 freebsd-announce 邮件列表存档一手核验，发信人为 Warner Losh 与 Ed Maste（代表 git conversion working group），公告于 2020-12-02 发布：doc 仓库为首个由 Subversion 迁移至 Git 的 FreeBSD 仓库，迁移于 12 月 5 日前后启动、计划 12 月 8 日前后完成
- Git 迁移为 FreeBSD 带来的最显著长期变化是 CI/CD（持续集成/持续交付）能力的提升和外部贡献门槛的降低：(1) **CI/CD**：基于 GitLab CI 和 Cirrus CI 的自动化构建和测试管道在 Git 迁移后逐步建立，每次提交都会触发多架构构建和测试，这在 SVN 时代难以实现；(2) **外部贡献**：虽然 GitHub 不接受直接 PR，但开发者可以更容易地在 GitHub 上浏览与克隆源码、检视提交历史，并据此向邮件列表或代码评审流程提交补丁，参与门槛显著低于 SVN 时代
- Git 迁移争议相关一手史料的可靠性需分级评估：(1) **最高可信度**：官方 Wiki 时间表、freebsd-git 邮件列表原始帖子、版本控制系统中的 commit 记录——这些是当时形成的一手文档，可信度最高；(2) **高可信度**：Ed Maste（埃德·马斯特）、Warner Losh（沃纳·洛什） 等核心成员的会议演讲和博客文章——作者是亲历者，但事后回忆可能存在细节偏差；(3) **中等可信度**：事后整理的综述、媒体报道与社区回忆——距离事件现场较远，具体细节须与前两级史料交叉核验后方可采信

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_11886] BSD Now 第 481 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12157] BSD Now 第 452 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12260] BSD Now 第 443 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12823] BSD Now 第 307 期，匹配 CH169 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10435] BSD Now 第 675 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10576] BSD Now 第 647 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10599] BSD Now 第 644 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10632] BSD Now 第 638 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10708] BSD Now 第 627 期，匹配 CH169 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10745] BSD Now 第 622 期，匹配 CH169 章，关联度 1.0

## 史观

- 总纲3 不存在进步，只有权力再分配：版本控制工具的更替不是进步的阶梯——从 CVS 到 SVN 再到 Git，每一代工具都承诺永久保存，又在下一代到来时沦为需要迁移的遗产；Git 迁移既是数字档案的重建机遇，也是历史保存的潜在威胁，每一次格式转换都意味着某些沉默的上下文永远丢失
- 总纲4 分离聚合是永恒规律：从 CVS 到 SVN 再到 Git 的迁移链印证分离聚合的循环——工具不断分裂又不断聚合，而代码始终是那个被搬来搬去的客体；FreeBSD 28 年开发史在三次工具更替中完整保留，与子节史观字段（总纲3、4、9、10、21、22、25）互为印证

## 辨析

- 经邮件列表库验证通过（来源：freebsd-git 列表，Message-ID <CAPyFy2CKdHW_KkOOQozPW04jBDz8ZaNWSJLqFWAdzKcaDfSzcA@mail.gmail.com>，2017-02-21，Ed Maste 发起“Reconsider switching from svn to git?”，Warner Losh 回复）；经邮件列表库验证通过〔存疑：本条其后另有一条独立验证记录，原文截断待回源补录〕
- 部分评论称“Git 迁移是基金会强行推动的”——这一说法不准确：基金会提供了资金支持，但技术决策由 Git 工作组（由资深 committer 组成）做出，Core Team 保留最终批准权；基金会资助使迁移工作能够更快推进，但并未改变社区决策流程
- 考据过程留痕——【查证来源】(1) freebsd-announce 邮件列表 mailman 存档经 lists.freebsd.org/pipermail/freebsd-announce/2020-December/002002.html 一手核验，确认邮件标题“[FreeBSD-Announce] FreeBSD-doc Subversion to Git migration”、发信人为 Warner Losh 与 Ed Maste（代表 git conversion working group），公告于 2020-12-02 发布：doc 仓库为首个由 Subversion 迁移至 Git 的 FreeBSD 仓库，迁移于 12 月 5 日前后启动、计划 12 月 8 日前后完成
- “Git 迁移使 FreeBSD 开发速度大幅提升”这一说法需辩证看待——单个提交的合入速度不一定更快（因为审查流程可能更规范），但整体开发吞吐量确实因更好的工具链、更多外部贡献和 CI 自动化而提升；开发质量也因自动化测试而提高
- 部分争议点可能永远没有完全清晰的答案——例如 Core Team 内部讨论的细节、某些决策的真实考量、个别 committer 退役的真实原因等；史笔至此须存疑，不可为了叙事完整性而编造或推断

## 文献

- Maste, E. (2018). *Git for FreeBSD*. MeetBSD 2018 presentation; BSD Now. (2019-09-18). *Episode 316: git commit FreeBSD*; OpenBSD Project. *Why OpenBSD Developers Use CVS*. openbsd.org/anoncvs.html; Torvalds, L. (2005). *Git initial release announcement*. Linux Kernel Mailing List. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-2008 年间：428,694 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. *freebsd-git Mailing List Archives*. lists.freebsd.org; FreeBSD Wiki. *GitTransition* (page history); FreeBSD Foundation. (2019-2021). *Quarterly Status Reports*. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2018-2019 年间：95,408 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Losh W, Maste E. [FreeBSD-Announce] FreeBSD-doc Subversion to Git migration [EB/OL]. (2020-12)[2026-07-23]. <https://lists.freebsd.org/pipermail/freebsd-announce/2020-December/002002.html>; Losh W. FreeBSD Git Docs — Doc Cutover Schedule [EB/OL]. [2026-07-23]. <https://github.com/bsdimp/freebsd-git-docs/blob/main/doc-cutover-schedule.md>; FreeBSD Project. freebsd-git Mailing List Archives [DB/OL]. [2026-07-23]. <https://lists.freebsd.org/pipermail/freebsd-git/> ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2021 年间：114,212 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. *CI/CD Documentation*. ci.freebsd.org; FreeBSD Foundation. (2021-2024). *Annual Reports* (contributor growth statistics); Cirrus CI. *FreeBSD CI Configuration*. github.com/freebsd/freebsd-src/tree/main/.cirrus.yml. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. *freebsd-git and freebsd-hackers mailing list archives*. lists.freebsd.org; Wayback Machine. *FreeBSD Wiki historical snapshots*. web.archive.org; FreeBSD Foundation. (2021). *Git Migration Retrospective*. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/freebsd.duckdb**; LibreBSD Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5-6; LibreBSD Project. 时间序列分析.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/时间序列分析.md** Task 14-15; LibreBSD Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第五卷第 66 章映射; LibreBSD Project. 外部基准-GitHub-CHAOSS.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/外部基准-GitHub-CHAOSS.md** 第 1.1 节（E-06、E-08 数据来源与三次复查留痕）; GitHub. Octoverse 2025: A new developer joins GitHub every second as AI leads TypeScript to #1 [R/OL]. 2025. URL: `https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/`（三次复查：2026-07-27）; Internet Archive. GitHub Octoverse 2014-2017 历年存档 [DB/OL]. `https://web.archive.org/web/2014-2017/https://octoverse.github.com/`（三次复查：2026-07-27）. ［A］
- [FP-2019-049] Poudriere for Port Maintenance（Matthew Seaman，2019）<https://papers.freebsd.org/2019/eurobsdcon/matthew-poudriere_for_port_maintenance/>
- [FP-2017-004] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2017）<https://papers.freebsd.org/2017/bsdcan/lwhsu-continuous_integration_of_the_freebsd_project/>
- [FP-2017-002] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2017）<https://papers.freebsd.org/2017/asiabsdcon/lwhsu-continuous_integration_of_the_freebsd_project/>
- [FP-2016-013] Continuous Integration of the FreeBSD Project（Li-Wen Hsu，2016）<https://papers.freebsd.org/2016/eurobsdcon/lwhsu-continuous_integration_of_the_freebsd_project/>
- [FP-2015-008] Supporting a BSD Project（Ed Maste，2015）<https://papers.freebsd.org/2015/vbsdcon/maste-supporting_a_bsd_project/>

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP370、BSD Now EP360、BSD Now EP164（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warner Losh 分析 FreeBSD 从 Subversion 迁移 Git 的动因：SVN 生态萎缩、CI 与协作工具以 Git 为中心、新开发者更熟悉 Git；代价包括失去关键词展开与单调递增版本号。（BSD Now EP370，[248.97-1025.79]，L2）
- FreeBSD 已是最后一个大规模使用 Subversion 的开源项目，迁移中借鉴 Apache 与 LLVM 的迁移经验。（BSD Now EP370，[339.89-365.10]，L2）
- rcorder 自 NetBSD 约 1998 年引入，用于根据 rc.d 脚本依赖排序启动服务；FreeBSD 已有并行化尝试，D25389 提交为 rcorder 增加并行输出标志，可节省约 15 至 20 秒启动时间。（BSD Now EP370，[2060.52-2224.76]，L2）
- FuryBSD 2020 Q3 发布首个基于 OpenZFS 的 live 镜像，以只读或读写模式测试 FreeBSD 桌面，并保留系统完整性。（BSD Now EP370，[72.36-115.00]，L2）
- 追查坏提交的文章介绍用 git bisect 二分定位引入回归的提交，并指出破坏可能来自非直观的依赖变更。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 完成 2020 年第十一届 Core 团队选举，Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Kyle Evans、Mark Johnston、Scott Long、Sean Chittenden、Warner Losh 当选。（BSD Now EP360，[460.69-614.65]，L2）
- NetBSD 在 Pinebook Pro 上以 NetBSD 9 用户态搭配 Current 内核运行，以兼顾二进制包与更好的硬件支持。（BSD Now EP360，[624.57-842.58]，L2）
- pf 状态表存在默认大小限制，FreeBSD 另有 `net.pf.request_maxcount` sysctl 控制单次 ioctl 载入表项数；DragonFly 侧限制为静态内核值。（BSD Now EP360，[1199.40-1404.41]，L2）
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

**史料**：

- Warner Losh 博客“FreeBSD Subversion to Git Migration, Part 1”及配套 YouTube 视频，逐条论证迁移理由。（BSD Now EP370，[248.97-1025.79]，L2）
- Dan Langille 关于 NUT 关机测试的博文，以及 `upsdrvctl -t` 测试模式与 `upsmon -c fsd` 命令的手册说明。（BSD Now EP370，[1174.02-1519.15]，L2）
- 追查坏提交博文与 git bisect 说明。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 2020 年 Core 团队选举公告，由主持人转述当选名单。（BSD Now EP360，[460.69-614.65]，L2）
- DragonFly vkernel copy-on-write 镜像模式的功能说明。（BSD Now EP164，[176.8-266.7]，L2）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 提交者关于 Raspberry Pi 3 支持的博客。　[存疑脚注] 博客作者全名须核验。（BSD Now EP164，[328.18-412.58]，L2）
- OpenBSD 官方只读 GitHub 镜像（github.com/openbsd）。（BSD Now EP164，[3828.2-3915.58]，L2）[订正：原 [3816.62-3915.58]，2026-09-30 SenseAudio 重转核对]
- Libreboot.org 关于以开源 BIOS 引导 OpenBSD/LibertyBSD 的文档。（BSD Now EP164，[3926.18-4004.28]，L2）
- Josh Paetzel 访谈自述（iXsystems，FreeNAS/TrueNAS 相关运维经验）。（BSD Now EP164，[985.8-2820.6]，L1）[订正：原 [1600.0-2610.0]，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲10 动手者创造历史：迁移论证强调以 CI 与协作工具降低贡献者摩擦，推动力量来自开发者的实际工作流需求。（BSD Now EP370，[581.03-707.75]，L2）
- 总纲21 革命与改革是历史方法论的分歧：FreeBSD 迁移 Git 采取渐进改革而非激进重构，迁移团队试图保留旧用户熟悉的工作流。（BSD Now EP370，[984.63-1017.59]，L2）
- 总纲10 动手者创造历史：FreeBSD 决策由“到场者”作出，主持人与提问者强调社区参与决定项目走向。（BSD Now EP360，[481.5-503.3]，L2）[订正：原 [2452.99-2456.55]（错挂片尾音乐段），2026-10-01 交叉核验订正——总纲10 内容真实出处为 481.5-503.3 段（core 团队九人自荐、社区九票多数当选），片尾 2443.1-2547.8 经两次转写均无语音产出判定为收播曲]
- 总纲4 分离聚合是永恒规律：Core 团队成员更替体现治理层的分离与再聚合。（BSD Now EP360，[460.69-614.65]，L2）
- 总纲4 分离聚合是永恒规律：vkernel 以只读镜像为基底、以 copy-on-write 层承载差异，多个实例分离运行又共享同一映像，呈现分离与聚合的结构。（BSD Now EP164，[176.8-266.7]，L3）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]
- 总纲3 不存在进步，只有权力再分配：Libreboot 试图把引导固件的控制权从闭源厂商转移给用户，是围绕系统控制权的权力再分配。（BSD Now EP164，[4007.8-4038.48]，L3）
- 总纲9 经验优先：ZFS 的可靠性来自 Sun 时期大量工程投入与后续商业资源，专业经验沉淀为可用的复杂系统。（BSD Now EP164，[2522.4-2603.72]，L3）
- 总纲25 逻辑是形式主义而非世界本身的结构：ZFS 以冗余与校验把故障可能性压到极低，但剩余风险以极端方式集中爆发，安全是形式化边界内的构造。（BSD Now EP164，[2434.64-2497.76]，L3）
- 总纲22 知识注定过时：OpenBSD 长期使用 CVS，在 Git 成为主流后以镜像方式补足浏览体验，旧工具随生态变化而需要新形式。（BSD Now EP164，[3816.62-3900.24]，L3）

**辨析**：

- rcorder 并行化历史上多次尝试均遇到未声明依赖问题，主持人指出并行带来的启动加速与破坏风险并存。　[存疑脚注] 并行化风险范围待核实（BSD Now EP370，[2193.19-2299.69]，L4）
- DragonFly 的 pf 表限制是静态内核值且未暴露为可调 sysctl，是否需要仿照 FreeBSD 改造仍待确认。　[存疑脚注] DragonFly 侧改造计划待核实（BSD Now EP360，[1360.80-1390.40]，L4）
- [存疑脚注] 转写未给出 DragonFly vkernel copy-on-write 功能的具体提交与作者，须核验 DragonFly 仓库与提交记录。　[存疑脚注] COW 功能提交与作者须核验。（BSD Now EP164，[176.8-266.7]，L4）[订正：原 [197.82-249.56]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP370] Pennington J. BSD Now: 370: Testing shutdown[EB/OL]. (2020-10-01)[2026-08-15]. <https://www.bsdnow.tv/370>.
- [BSD Now EP360] Pennington J. BSD Now: 360: Full circle[EB/OL]. (2020-07-23)[2026-08-15]. <https://www.bsdnow.tv/360>.
- [BSD Now EP164] Pennington J. BSD Now: 164: Virtualized COW / PI?[EB/OL]. (2016-10-19)[2026-08-15]. <https://www.bsdnow.tv/164>.

<!-- /PODCAST_REVIEW -->
