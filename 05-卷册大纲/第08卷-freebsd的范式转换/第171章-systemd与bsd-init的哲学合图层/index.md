---
chapter: 第 171 章
id: CH171
volume: 第08卷-freebsd的范式转换
---

# 第 171 章 systemd与bsd-init的哲学合图层

## 要点

- **统计分析印证**——`bsd_commits.db` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；Pettitt 与 BUISHAND R 双变点检验一致判定 freebsd-src
- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），13,875 位贡献者
- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），13,875 位贡献者
- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），13,875 位贡献者

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3694] 卷“第09卷-netbsd的历史”第 171 章，匹配置信度 folder，原因：folder 第169章
- [DB:references_fulltext:chapter_matches:chmatch_3876] 卷“第09卷-netbsd的历史”第 171 章，匹配置信度 folder，原因：folder 第169章
- [DB:bsdnow_podcast:outline_mappings:om_10608] BSD Now 第 642 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10740] BSD Now 第 623 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10747] BSD Now 第 622 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10823] BSD Now 第 610 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10866] BSD Now 第 604 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10900] BSD Now 第 601 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11018] BSD Now 第 585 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11051] BSD Now 第 581 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11160] BSD Now 第 570 期，匹配 CH171 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11208] BSD Now 第 563 期，匹配 CH171 章，关联度 2.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- *统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 BSD init 子系统演进的实际工程意义须结合 init 相关 commit 比例综合判断——init 子系统 commit 仅占 freebsd-src 总量的一小部分，整体趋势不能等同于子系统趋势；(2) 变
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证

## 文献

- FreeBSD Project. bsd_commits.db freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\bsd_commits.db`; Hibsd Project. 推断性统计.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md` Task 5-6; Hibsd Project. 时间序列分析.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\时间序列分析.md` Task 14-15; Hibsd Project. 卷章数据映射.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\卷章数据映射.md` 第五卷第 68B 章映射。［A］### 参考史料与文献清单> 按 GB/T 7714-2015 著录格式编排，与子节主题直接相关的参考文献已分散于各节“文献”字段，本节为整章汇总与补充。[1] Poettering L. Rethinking PID 1 [EB/OL]. (2010-03-30)[2026-07-22]. <https://0pointer.de/blog/projects/systemd.html>.[2] Poettering L. The Biggest Myths [EB/OL]. (2013)[2026-07-22]. <https://0pointer.de/blog/projects/the-biggest-myths.html>.[3] systemd 项目。systemd 上游仓库源码 [CP/OL]. HEAD commit `765dc96746d699229af60e912bac90b710ee5798`（2026-07-17）. <https://github.com/systemd/systemd>.[4] 本项目。systemd 上游仓库源码分析报告 [R/OL]. `script/systemd_analysis_report.md`. 2026-07-23.[5] 本项目。BSD init 数据库证据报告 [R/OL]. `script/bsd_init_db_report.md`. 2026-07-22.[6] 本项目。systemd 关键史实联网核查报告 [R/OL]. `script/systemd_fact_check_report.md`. 2026-07-22.[7] 本项目。BSD init 发展史与 BSD 阵营对 systemd 立场考据报告 [R/OL]. `script/bsd_init_fact_check_report.md`. 2026-07-22.[8] Fedora Project. Fedora 15 Release [EB/OL]. (2011-05-24)[2026-07-22]. <https://fedoraproject.org/wiki/Releases/15>.[9] Red Hat Inc. Red Hat Enterprise Linux 7 Release Notes [EB/OL]. (2014-06-10)[2026-07-22]. <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/release_notes/>.[10] Red Hat Inc. IBM to Acquire Red Hat, Completely Changing the Cloud Landscape and Becoming World's #1 Hybrid Cloud Provider [EB/OL]. (2018-10-28)[2026-07-22]. <https://www.redhat.com/en/about/press-releases/ibm-acquire-red-hat-completely-changing-cloud-landscape-and-becoming-worlds-1-hybrid-cloud-provider>.[11] Red Hat Inc. IBM Closes Landmark Acquisition of Red Hat for $34 Billion; Defines Open, Hybrid Cloud Future[EB/OL]. (2019-07-09)[2026-07-22]. <https://www.redhat.com/en/about/press-releases/ibm-closes-landmark-acquisition-red-hat-34-billion-defines-open-hybrid-cloud-future>.[12] Debian CTTE. Call for votes on default Linux init system for jessie [EB/OL]. (2014-02)[2026-07-22]. <https://lists.debian.org/debian-ctte/2014/02/msg00281.html>.[13] Gilbert M. Vote outcome analysis [EB/OL]. (2014-02)[2026-07-22]. <https://lists.debian.org/debian-ctte/2014/02/msg00338.html>.[14] Chamberlain S. sysvinit compatibility discussion [EB/OL]. (2014-02)[2026-07-22]. <https://lists.debian.org/debian-ctte/2014/02/msg00326.html>.[15] Debian Project. Debian 8 "Jessie" Release [EB/OL]. (2015-04-25)[2026-07-22]. <https://www.debian.org/releases/jessie/>.[16] Veteran Unix Admins. Don't panic and keep forking Debian [EB/OL]. (2014-11-27)[2026-07-22]. <https://www.devuan.org/os/announce/>.[17] NIST NVD. CVE-2013-4392 Detail [EB/OL]. (2013-10-28)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2013-4392>.[18] NIST NVD. CVE-2017-18078 Detail [EB/OL]. (2018-01-29)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2017-18078>.[19] NIST NVD. CVE-2018-15688 Detail [EB/OL]. (2018-10-26)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2018-15688>.[20] NIST NVD. CVE-2019-3842 Detail [EB/OL]. (2019-04-09)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2019-3842>.[21] NIST NVD. CVE-2021-33910 Detail [EB/OL]. [2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2021-33910>.[22] NIST NVD. CVE-2015-3407 Detail（证伪：实为 Perl Module:: Signature 漏洞）[EB/OL]. [2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2015-3407>.[23] FOSDEM. FOSDEM 2017 Main Schedule [EB/OL]. (2017-02-04~05)[2026-07-22]. <https://archive.fosdem.org/2017/schedule/>.[24] systemd-devel Mailing List Archive [EB/OL]. <https://lists.freedesktop.org/archives/systemd-devel/>.[25] The Unix Heritage Society. UNIX V6 /usr/source/s1/init.c [EB/OL]. (1975-05-14)[2026-07-22]. <https://www.tuhs.org/cgi-bin/utree.pl?file=V6/usr/source/s1/init.c>.[26] The Unix Heritage Society. 4BSD /etc/rc [EB/OL]. (1980-11-11)[2026-07-22]. <https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD/etc/rc>.[27] The Unix Heritage Society. 4.2BSD /etc/rc.local [EB/OL]. (1983-08-28)[2026-07-22]. <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/etc/rc.local>.[28] Mewburn L. The Design and Implementation of the NetBSD rc.d system [C]//USENIX Annual Technical Conference 2001, FREENIX Track. Berkeley: USENIX Association, 2001. 论文页 <https://www.usenix.org/legacy/publications/library/proceedings/usenix01/freenix01/mewburn.html>；PDF <http://www.mewburn.net/luke/papers/rc.d.pdf>.[29] NetBSD Project. NetBSD 1.5 Release Announcement [EB/OL]. (2000-12-06)[2026-07-22]. <https://www.netbsd.org/releases/formal-1.5/NetBSD-1.5.html>.[30] FreeBSD Project. FreeBSD 5.0 Release Announcement [EB/OL]. (2003-01-19)[2026-07-22]. <https://www.freebsd.org/releases/5.0R/announce/>.[31] FreeBSD Project. FreeBSD 5.0-RELEASE rc(8) Manual Page [EB/OL]. [2026-07-22]. <https://www.freebsd.org/cgi/man.cgi?query=rc&sektion=8&manpath=FreeBSD+5.0-RELEASE>.[32] OpenBSD Project. OpenBSD 4.9 Release [EB/OL]. (2011-05-01)[2026-07-22]. <https://www.openbsd.org/49.html>.[33] OpenBSD Project. OpenBSD 4.9 Changelog [EB/OL]. (2011-05-01)[2026-07-22]. <https://www.openbsd.org/plus49.html>.[34] OpenBSD Project. OpenBSD 5.6 Changelog [EB/OL]. (2014-11-01)[2026-07-22]. <https://www.openbsd.org/plus56.html>.[35] OpenBSD Project. OpenBSD 5.7 Changelog [EB/OL]. (2015-05-01)[2026-07-22]. <https://www.openbsd.org/plus57.html>.[36] OpenBSD Project. OpenBSD rc.d(8) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/rc.d.8>.[37] OpenBSD Project. OpenBSD rc.subr(8) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/rc.subr.8>.[38] FreeBSD Project. FreeBSD Hackers Mailing List Archive [EB/OL]. <https://lists.freebsd.org/pipermail/freebsd-hackers/>.[39] OpenBSD Project. OpenBSD misc Mailing List [EB/OL]. <https://marc.info/?laccopenbsd-misc>.[40] Apple Inc. Daemons and Services Programming Guide [EB/OL]. [2026-07-22]. <https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html>.[41] Oracle Corporation. Solaris 10 Service Management Facility Documentation [EB/OL]. [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]. <https://docs.oracle.com/cd/E19253-01/817-1985/6mhc1gblh/index.html>.[42] Robbins D, Marples R, Hubbs W, et al. OpenRC HISTORY [EB/OL]. [2026-07-22]. <https://raw.githubusercontent.com/OpenRC/openrc/master/HISTORY.md>.[43] Gentoo Wiki. OpenRC [EB/OL]. [2026-07-22]. <https://wiki.gentoo.org/wiki/OpenRC>.[44] Pape G. runit [EB/OL]. [2026-07-22]. <https://smarden.org/runit/>.[45] Bercot L. s6 [EB/OL]. [2026-07-22]. <https://skarnet.org/software/s6/>.[46] Bernstein D J. daemontools [EB/OL]. [2026-07-22]. <https://cr.yp.to/daemontools.html>.[47] Raymond E S. The Art of Unix Programming [M]. Boston: Addison-Wesley, 2003.[48] Kernighan B W, Pike R. The UNIX Programming Environment [M]. Englewood Cliffs: Prentice Hall, 1984.[49] Remnant S J. Upstart: A replacement for the init daemon [EB/OL]. (2006)[2026-07-22]. <https://wiki.ubuntu.com/ReplacementInitDaemon>.> ## 第 68B.12 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 68B.13 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）---**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=13）---**补充证据（基于全文数据库修订）**本次修订从全文数据库补充 4 篇新匹配文献的证据。**新增核心事实**文献 (45, 年份不详, p.3) 指出：ipfw，该文献的引用为该主题提供了相关学术背景。文献 (45, 年份不详, p.3) 指出：TCP/IP，该文献的引用为该主题提供了相关学术背景。文献 (standalone, 1997, p.1) 指出：UDP，该文献的引用为该主题提供了相关学术背景。文献 (standalone, 1997, p.1) 指出：NFS，该文献的引用为该主题提供了相关学术背景。文献 (asiabsdcon, 2015, p.5) 指出：FreeBSD 9.2-RELEASE，该文献的引用为该主题提供了相关学术背景。文献 (asiabsdcon, 2015, p.5) 指出：FreeBSD 10.1-RELEASE，该文献的引用为该主题提供了相关学术背景。**新增技术**：ipfw 防火墙（BSD 4.4 引入内核级包过滤，需启用 IPFIREWALL 选项）；TCP/IP 网络管理信息库（MIB-II）标准化；UDP 无连接数据报通信实现；AsiaBSDCon 2015 上 Go 语言内容过滤软件在 FreeBSD 的移植；top 命令 CPU 使用率报告改进。

**新增时间线事件**：1991 年 IEEE Trans Communs 发表路由模型网络可靠性研究论文，王波《FreeBSD 使用大全》出版；2015 年 AsiaBSDCon 2015 展示 Go 语言内容过滤软件在 FreeBSD 上的实现。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP370、BSD Now EP55（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warner Losh 分析 FreeBSD 从 Subversion 迁移 Git 的动因：SVN 生态萎缩、CI 与协作工具以 Git 为中心、新开发者更熟悉 Git；代价包括失去关键词展开与单调递增版本号。（BSD Now EP370，[248.97-1025.79]，L2）
- FreeBSD 已是最后一个大规模使用 Subversion 的开源项目，迁移中借鉴 Apache 与 LLVM 的迁移经验。（BSD Now EP370，[339.89-365.10]，L2）
- rcorder 自 NetBSD 约 1998 年引入，用于根据 rc.d 脚本依赖排序启动服务；FreeBSD 已有并行化尝试，D25389 提交为 rcorder 增加并行输出标志，可节省约 15 至 20 秒启动时间。（BSD Now EP370，[2060.52-2224.76]，L2）
- FuryBSD 2020 Q3 发布首个基于 OpenZFS 的 live 镜像，以只读或读写模式测试 FreeBSD 桌面，并保留系统完整性。（BSD Now EP370，[72.36-115.00]，L2）
- Adrian Chadd 自述 FreeBSD 无线栈在 AP 与 station 模式下工作良好，但仅有两名左右开发者，边界情况缺乏人手。（BSD Now EP55，[1419.88-1458.76]，L1）
- Atheros 与 Intel 因开放源码与文档而成为 FreeBSD 无线的主要方向；Broadcom 与 Marvell 在 Sam Leffler 离开后未再更新，成为明显短板。（BSD Now EP55，[1462.00-1544.32]，L1）
- Adrian Chadd 恢复因监管顾虑而停用的 monitor mode 注入，使 Kismet 与 Aircrack-NG 重新可用，同时承受实现监管域强制的压力。（BSD Now EP55，[1777.56-1881.62]，L1）
- OpenBSD 的 systemd 兼容层仅为 hostnamed、localed、timedated、logind 的 shim，以让 GNOME 运行，并非移植 systemd 本体或替换 init。（BSD Now EP55，[3493.32-3567.32]，L2）

**史料**：

- Warner Losh 博客“FreeBSD Subversion to Git Migration, Part 1”及配套 YouTube 视频，逐条论证迁移理由。（BSD Now EP370，[248.97-1025.79]，L2）
- Dan Langille 关于 NUT 关机测试的博文，以及 `upsdrvctl -t` 测试模式与 `upsmon -c fsd` 命令的手册说明。（BSD Now EP370，[1174.02-1519.15]，L2）
- Adrian Chadd 访谈（FreeBSD 无线网络栈维护者当事人自述）。（BSD Now EP55，[1267.26-2874.88]，L1）

**史观**：

- 总纲10 动手者创造历史：迁移论证强调以 CI 与协作工具降低贡献者摩擦，推动力量来自开发者的实际工作流需求。（BSD Now EP370，[581.03-707.75]，L2）
- 总纲21 革命与改革是历史方法论的分歧：FreeBSD 迁移 Git 采取渐进改革而非激进重构，迁移团队试图保留旧用户熟悉的工作流。（BSD Now EP370，[984.63-1017.59]，L2）
- 总纲20 历史地理塑造思想土壤：总纲20 历史地理塑造思想土壤：无线厂商是否开放文档、是否以 Linux 为主场，直接塑造了 FreeBSD 无线栈的可行范围。（BSD Now EP55，[1462.00-1603.66]，L1）
- 总纲9 经验优先：总纲9 经验优先：Adrian Chadd 以驱动开发与真机测试的一线经验陈述无线栈优劣，而非依赖纸面规格。（BSD Now EP55，[1419.88-1447.00]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：各 BSD 共享 net80211 后各自分化，DragonFly BSD 又聚合 FreeBSD 更新栈，构成反复的分合。（BSD Now EP55，[1657.66-1722.12]，L1）

**辨析**：

- rcorder 并行化历史上多次尝试均遇到未声明依赖问题，主持人指出并行带来的启动加速与破坏风险并存。　[存疑脚注] 并行化风险范围待核实（BSD Now EP370，[2193.19-2299.69]，L4）
- 转录将 Ralink/Realtek 与 Atheros 的表述交错，主持人与嘉宾均存在口误修正，具体芯片归属需对照 FreeBSD 源码。　[存疑脚注] 无线芯片厂商归属存在口语转写歧义，未以代码仓库核验（BSD Now EP55，[1486.52-1493.84]，L4）

**文献**：

- [BSD Now EP370] Pennington J. BSD Now: 370: Testing shutdown[EB/OL]. (2020-10-01)[2026-08-15]. https://www.bsdnow.tv/370.
- [BSD Now EP55] Pennington J. BSD Now: 55: The Promised WLAN[EB/OL]. (2014-09-17)[2026-08-15]. https://www.bsdnow.tv/55.

<!-- /PODCAST_REVIEW -->
