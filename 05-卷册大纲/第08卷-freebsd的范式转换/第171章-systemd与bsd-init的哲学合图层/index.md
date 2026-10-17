---
chapter: 第 171 章
id: CH171
volume: 第08卷-freebsd的范式转换
---

# 第 171 章 systemd与bsd-init的哲学合图层

## 要点

- **统计分析印证**——`freebsd.duckdb` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；Pettitt 与 BUISHAND R 双变点检验一致判定 freebsd-src〔存疑：原文截断，待回源补全〕
- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），5,671 位贡献者（contributors 表行数）

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

- 章级史观：从项目史观总纲第 21 条（革命与改革是历史方法论的分歧）审视 systemd 与 BSD init 的哲学合图层——FreeBSD 以 rc.d/rcorder 渐进改良与兼容 shim 吸收 systemd 生态压力，走渐进改革路径而非跟随 Linux 的 init 革命路径；init 系统之争的表象是技术选型，深层是用户工作流、发行版治理与厂商利益的权力再分配（总纲第 3 条）；OpenBSD 拒绝 systemd 本体而以四组件兼容包装维持 GNOME 可用，体现各方平等前提下不同 init 路线的并存（总纲第 8 条）。细目详见子节文件史观/辨析字段。

## 辨析

- **统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 BSD init 子系统演进的实际工程意义须结合 init 相关 commit 比例综合判断——init 子系统 commit 仅占 freebsd-src 总量的一小部分，整体趋势不能等同于子系统趋势；(2) 变〔存疑：原文截断，待回源补全〕
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证

## 文献

- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/02-FreeBSD/db/duckdb/freebsd.duckdb**; LibreBSD Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5-6; LibreBSD Project. 时间序列分析.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/时间序列分析.md** Task 14-15; LibreBSD Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第八卷第 171 章映射。［A］
### 参考史料与文献清单
> 按 GB/T 7714-2015 著录格式编排，与子节主题直接相关的参考文献已分散于各节“文献”字段，本节为整章汇总与补充。
[] Poettering L. Rethinking PID 1 [EB/OL]. (2010-03-30)[2026-07-22]. <https://0pointer.de/blog/projects/systemd.html>.
[] Poettering L. The Biggest Myths [EB/OL]. (2013)[2026-07-22]. <https://0pointer.de/blog/projects/the-biggest-myths.html>.
[] systemd 项目。systemd 上游仓库源码 [CP/OL]. HEAD commit `765dc96746d699229af60e912bac90b710ee5798`（2026-07-17）. <https://github.com/systemd/systemd>.
[] 本项目。systemd 上游仓库源码分析报告 [R/OL]. `script/systemd_analysis_report.md`. 2026-07-23.
[] 本项目。BSD init 数据库证据报告 [R/OL]. `script/bsd_init_db_report.md`. 2026-07-22.
[] 本项目。systemd 关键史实联网核查报告 [R/OL]. `script/systemd_fact_check_report.md`. 2026-07-22.
[] 本项目。BSD init 发展史与 BSD 阵营对 systemd 立场考据报告 [R/OL]. `script/bsd_init_fact_check_report.md`. 2026-07-22.
[] Fedora Project. Fedora 15 Release [EB/OL]. (2011-05-24)[2026-07-22]. <https://fedoraproject.org/wiki/Releases/15>.
[] Red Hat Inc. Red Hat Enterprise Linux 7 Release Notes [EB/OL]. (2014-06-10)[2026-07-22]. <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/release_notes/>.
[] Red Hat Inc. IBM to Acquire Red Hat, Completely Changing the Cloud Landscape and Becoming World's #1 Hybrid Cloud Provider [EB/OL]. (2018-10-28)[2026-07-22]. <https://www.redhat.com/en/about/press-releases/ibm-acquire-red-hat-completely-changing-cloud-landscape-and-becoming-worlds-1-hybrid-cloud-provider>.
[] Red Hat Inc. IBM Closes Landmark Acquisition of Red Hat for $34 Billion; Defines Open, Hybrid Cloud Future[EB/OL]. (2019-07-09)[2026-07-22]. <https://www.redhat.com/en/about/press-releases/ibm-closes-landmark-acquisition-red-hat-34-billion-defines-open-hybrid-cloud-future>.
[] Debian CTTE. Call for votes on default Linux init system for jessie [EB/OL]. (2014-02)[2026-07-22]. <https://lists.debian.org/debian-ctte/2014/02/msg00281.html>.
[] Gilbert M. Vote outcome analysis [EB/OL]. (2014-02)[2026-07-22]. <https://lists.debian.org/debian-ctte/2014/02/msg00338.html>.
[] Chamberlain S. sysvinit compatibility discussion [EB/OL]. (2014-02)[2026-07-22]. <https://lists.debian.org/debian-ctte/2014/02/msg00326.html>.
[] Debian Project. Debian 8 “Jessie” Release [EB/OL]. (2015-04-25)[2026-07-22]. <https://www.debian.org/releases/jessie/>.
[] Veteran Unix Admins. Don't panic and keep forking Debian [EB/OL]. (2014-11-27)[2026-07-22]. <https://www.devuan.org/os/announce/>.
[] NIST NVD. CVE-2013-4392 Detail [EB/OL]. (2013-10-28)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2013-4392>.
[] NIST NVD. CVE-2017-18078 Detail [EB/OL]. (2018-01-29)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2017-18078>.
[] NIST NVD. CVE-2018-15688 Detail [EB/OL]. (2018-10-26)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2018-15688>.
[] NIST NVD. CVE-2019-3842 Detail [EB/OL]. (2019-04-09)[2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2019-3842>.
[] NIST NVD. CVE-2021-33910 Detail [EB/OL]. [2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2021-33910>.
[] NIST NVD. CVE-2015-3407 Detail（证伪：实为 Perl Module:: Signature 漏洞）[EB/OL]. [2026-07-22]. <https://nvd.nist.gov/vuln/detail/CVE-2015-3407>.
[] FOSDEM. FOSDEM 2017 Main Schedule [EB/OL]. (2017-02-04~05)[2026-07-22]. <https://archive.fosdem.org/2017/schedule/>.
[] systemd-devel Mailing List Archive [EB/OL]. <https://lists.freedesktop.org/archives/systemd-devel/>.
[] The Unix Heritage Society. UNIX V6 /usr/source/s1/init.c [EB/OL]. (1975-05-14)[2026-07-22]. <https://www.tuhs.org/cgi-bin/utree.pl?file=V6/usr/source/s1/init.c>.
[] The Unix Heritage Society. 4BSD /etc/rc [EB/OL]. (1980-11-11)[2026-07-22]. <https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD/etc/rc>.
[] The Unix Heritage Society. 4.2BSD /etc/rc.local [EB/OL]. (1983-08-28)[2026-07-22]. <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/etc/rc.local>.
[] Mewburn L. The Design and Implementation of the NetBSD rc.d system [C]//USENIX Annual Technical Conference 2001, FREENIX Track. Berkeley: USENIX Association, 2001. 论文页 <https://www.usenix.org/legacy/publications/library/proceedings/usenix01/freenix01/mewburn.html>；PDF <http://www.mewburn.net/luke/papers/rc.d.pdf>.
[] NetBSD Project. NetBSD 1.5 Release Announcement [EB/OL]. (2000-12-06)[2026-07-22]. <https://www.netbsd.org/releases/formal-1.5/NetBSD-1.5.html>.
[] FreeBSD Project. FreeBSD 5.0 Release Announcement [EB/OL]. (2003-01-19)[2026-07-22]. <https://www.freebsd.org/releases/5.0R/announce/>.
[] FreeBSD Project. FreeBSD 5.0-RELEASE rc(8) Manual Page [EB/OL]. [2026-07-22]. <https://www.freebsd.org/cgi/man.cgi?query=rc&sektion=8&manpath=FreeBSD+5.0-RELEASE>.
[] OpenBSD Project. OpenBSD 4.9 Release [EB/OL]. (2011-05-01)[2026-07-22]. <https://www.openbsd.org/49.html>.
[] OpenBSD Project. OpenBSD 4.9 Changelog [EB/OL]. (2011-05-01)[2026-07-22]. <https://www.openbsd.org/plus49.html>.
[] OpenBSD Project. OpenBSD 5.6 Changelog [EB/OL]. (2014-11-01)[2026-07-22]. <https://www.openbsd.org/plus56.html>.
[] OpenBSD Project. OpenBSD 5.7 Changelog [EB/OL]. (2015-05-01)[2026-07-22]. <https://www.openbsd.org/plus57.html>.
[] OpenBSD Project. OpenBSD rc.d(8) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/rc.d.8>.
[] OpenBSD Project. OpenBSD rc.subr(8) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/rc.subr.8>.
[] FreeBSD Project. FreeBSD Hackers Mailing List Archive [EB/OL]. <https://lists.freebsd.org/pipermail/freebsd-hackers/>.
[] OpenBSD Project. OpenBSD misc Mailing List [EB/OL]. <https://marc.info/?laccopenbsd-misc>.
[] Apple Inc. Daemons and Services Programming Guide [EB/OL]. [2026-07-22]. <https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html>.
[] Oracle Corporation. Solaris 10 Service Management Facility Documentation [EB/OL]. ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. <https://docs.oracle.com/cd/E19253-01/817-1985/6mhc1gblh/index.html>.
[] Robbins D, Marples R, Hubbs W, et al. OpenRC HISTORY [EB/OL]. [2026-07-22]. <https://raw.githubusercontent.com/OpenRC/openrc/master/HISTORY.md>.
[] Gentoo Wiki. OpenRC [EB/OL]. [2026-07-22]. <https://wiki.gentoo.org/wiki/OpenRC>.
[] Pape G. runit [EB/OL]. [2026-07-22]. <https://smarden.org/runit/>.
[] Bercot L. s6 [EB/OL]. [2026-07-22]. <https://skarnet.org/software/s6/>.
[] Bernstein D J. daemontools [EB/OL]. [2026-07-22]. <https://cr.yp.to/daemontools.html>.
[] Raymond E S. The Art of Unix Programming [M]. Boston: Addison-Wesley, 2003.
[] Kernighan B W, Pike R. The UNIX Programming Environment [M]. Englewood Cliffs: Prentice Hall, 1984.
[] Remnant S J. Upstart: A replacement for the init daemon [EB/OL]. (2006)[2026-07-22]. <https://wiki.ubuntu.com/ReplacementInitDaemon>.

## 不同时期人员的采访录（详见 [采访录.md](采访录.md)）

---

**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=13）

---

**补充证据（基于全文数据库修订）**

本次修订从全文数据库补充 4 篇新匹配文献的证据。**新增核心事实**文献 (asiabsdcon, 2015, p.5) 指出：FreeBSD 9.2-RELEASE，该文献的引用为该主题提供了相关学术背景。文献 (asiabsdcon, 2015, p.5) 指出：FreeBSD 10.1-RELEASE，该文献的引用为该主题提供了相关学术背景。**新增技术**：ipfw 防火墙（BSD 4.4 引入内核级包过滤，需启用 IPFIREWALL 选项）；TCP/IP 网络管理信息库（MIB-II）标准化；UDP 无连接数据报通信实现；AsiaBSDCon 2015 上 Go 语言内容过滤软件在 FreeBSD 的移植；top 命令 CPU 使用率报告改进。

**新增时间线事件**：〔订正：原“1991 年……王波《FreeBSD 使用大全》出版”句纪年疑讹已删〕2015 年 AsiaBSDCon 2015 展示 Go 语言内容过滤软件在 FreeBSD 上的实现。

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 2024-2026 年间：168,386 次提交。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP370、BSD Now EP71、BSD Now EP55（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warner Losh 分析 FreeBSD 从 Subversion 迁移 Git 的动因：SVN 生态萎缩、CI 与协作工具以 Git 为中心、新开发者更熟悉 Git；代价包括失去关键词展开与单调递增版本号。（BSD Now EP370，[248.97-1025.79]，L2）
- FreeBSD 已是最后一个大规模使用 Subversion 的开源项目，迁移中借鉴 Apache 与 LLVM 的迁移经验。（BSD Now EP370，[339.89-365.10]，L2）
- rcorder 自 NetBSD 约 1998 年引入，用于根据 rc.d 脚本依赖排序启动服务；FreeBSD 已有并行化尝试，D25389 提交为 rcorder 增加并行输出标志，可节省约 15 至 20 秒启动时间。（BSD Now EP370，[2060.52-2224.76]，L2）
- FuryBSD 2020 Q3 发布首个基于 OpenZFS 的 live 镜像，以只读或读写模式测试 FreeBSD 桌面，并保留系统完整性。（BSD Now EP370，[72.36-115.00]，L2）
- Ian Sutton 在 GSoC 期间为 OpenBSD 编写 systemd 四个非 init 组件的兼容包装器：GNOME 3 对 hostnamed、localed、timedated、logind 存在硬依赖，包装器经由 D-Bus 提供与 systemd 相同的接口使其透明可用；项目按操作系统无关设计，FreeBSD 提交者 Baptiste Daroussin 已着手移植，logind 因涉及 PAM 与 3D 加速设备权限传递而最为复杂，其余三个组件已基本成形。（BSD Now EP71，[879.16-934.98]，L1）
- 在 ISC NTPD 连串安全补丁与 NTP 反射攻击的背景下，长期无人维护的 portable OpenNTPD 由曾参与 LibreSSL 相关工作的 Brent Cook 等志愿者接手复活，产出 16 个补丁并重新发布至 GitHub 与 FreeBSD 包仓库，修复过程中还反哺了 OpenBSD 原生版代码。（BSD Now EP71，[602.16-686.20]，L2）
- pkg（pkgng）新增对 OS X 的支持并连发新版本，MacPorts 因 FreeBSD ports 树日益依赖 pkg 而考虑移植其完整功能，未来或为 Mac 引入二进制包；pkg 由此从 BSD 生态扩展为跨平台包管理方案，同期亦出现 Linux 移植迹象。（BSD Now EP71，[1842.70-1950.34]，L2）
- Adrian Chadd 自述 FreeBSD 无线栈在 AP 与 station 模式下工作良好，但仅有两名左右开发者，边界情况缺乏人手。（BSD Now EP55，[1430.5-1459.1]，L1）[订正：原 [1419.88-1458.76]，2026-09-30 SenseAudio 重转核对]
- Atheros 与 Intel 因开放源码与文档而成为 FreeBSD 无线的主要方向；Broadcom 与 Marvell 在 Sam Leffler 离开后未再更新，成为明显短板。（BSD Now EP55，[1459.3-1648.2]，L1）[订正：原 [1462.00-1544.32]，2026-09-30 SenseAudio 重转核对]
- Adrian Chadd 恢复因监管顾虑而停用的 monitor mode 注入，使 Kismet 与 Aircrack-NG 重新可用，同时承受实现监管域强制的压力。（BSD Now EP55，[1777.56-1881.62]，L1）
- OpenBSD 的 systemd 兼容层仅为 hostnamed、localed、timedated、logind 的 shim，以让 GNOME 运行，并非移植 systemd 本体或替换 init。（BSD Now EP55，[3505.2-3567.32]，L2）[订正：原 [3493.32-3567.32]，2026-09-30 SenseAudio 重转核对]

**史料**：

- Warner Losh 博客“FreeBSD Subversion to Git Migration, Part 1”及配套 YouTube 视频，逐条论证迁移理由。（BSD Now EP370，[248.97-1025.79]，L2）
- Dan Langille 关于 NUT 关机测试的博文，以及 `upsdrvctl -t` 测试模式与 `upsmon -c fsd` 命令的手册说明。（BSD Now EP370，[1174.02-1519.15]，L2）
- 本期涉及的一手史料包括：Ian Sutton 口述的 GSoC 项目经历及其导师 Landry Breuil、Antoine Jacoutot；freebsd-questions 邮件列表上 PGP 签名的 Protocol X97 恶作剧邮件；Theo de Raadt 对 shaman.c 未定义行为报告的邮件答复；oss-security 邮件列表的 FFmpeg 写后释放漏洞报告与漏洞样本视频；Sean Webb 博文《CodeRot and why I chose OpenBSD》；Baptiste 的“four years of pkg”大会演讲录像；FreeBSD 季度状态报告。（BSD Now EP71，[3539.10-3760.76]，L2）
- Adrian Chadd 访谈（FreeBSD 无线网络栈维护者当事人自述）。（BSD Now EP55，[1267.26-2874.88]，L1）

**史观**：

- 总纲10 动手者创造历史：迁移论证强调以 CI 与协作工具降低贡献者摩擦，推动力量来自开发者的实际工作流需求。（BSD Now EP370，[581.03-707.75]，L2）
- 总纲21 革命与改革是历史方法论的分歧：FreeBSD 迁移 Git 采取渐进改革而非激进重构，迁移团队试图保留旧用户熟悉的工作流。（BSD Now EP370，[984.63-1017.59]，L2）
- 总纲9 经验优先：全期叙事以当事人一手经验为骨架——Ian 自述因 Arch Linux 升级 systemd 时的目录冲突而转向 OpenBSD，CodeRot 作者自述删除死代码的体会，主持人强调开发者日常自用能在使用而非审查中发现问题；经验先于抽象论证的认识次序贯穿整期节目。（BSD Now EP71，[371.44-428.30]，L1）
- 总纲4 分离聚合是永恒规律：本期呈现的工具史并非线性进步，而是分离聚合的流转：pkg 从 FreeBSD 生态分离出去向 OS X 与 Linux 扩散又反向吸纳外部需求，portable OpenNTPD 先脱离 OpenBSD 独立维护、失修后再由志愿者重新聚合；各分支在分合中重构边界，而非简单的优胜劣汰。（BSD Now EP71，[1867.32-1931.22]，L2）
- 总纲20 历史地理塑造思想土壤：无线厂商是否开放文档、是否以 Linux 为主场，直接塑造了 FreeBSD 无线栈的可行范围。（BSD Now EP55，[1462.00-1603.66]，L1）
- 总纲9 经验优先：Adrian Chadd 以驱动开发与真机测试的一线经验陈述无线栈优劣，而非依赖纸面规格。（BSD Now EP55，[1430.5-1447.00]，L1）[订正：原 [1419.88-1447.00]，2026-09-30 SenseAudio 重转核对]
- 总纲4 分离聚合是永恒规律：各 BSD 共享 net80211 后各自分化，DragonFly BSD 又聚合 FreeBSD 更新栈，构成反复的分合。（BSD Now EP55，[1657.66-1722.12]，L1）

**辨析**：

- rcorder 并行化历史上多次尝试均遇到未声明依赖问题，主持人指出并行带来的启动加速与破坏风险并存。 [存疑脚注] 并行化风险范围待核实（BSD Now EP370，[2193.19-2299.69]，L4）
- 标题“System Disaster”与本期主体形成互文：2015 年初 systemd 争议已从 init 层蔓延至桌面依赖链（GNOME 3 硬依赖、Debian 用户请求反向移植、Arch 用户出走），但 Ian 澄清其项目并非把 systemd 移植到 OpenBSD，舆论“把 systemd 带上 BSD”的解读与工程事实有出入，引用时应区分依赖兼容与本体移植。（BSD Now EP71，[824.40-915.16]，L2）
- 该转写为双音轨交错且时间戳乱序，专名失真密集（bhyve 被转写为 Beehive、LibreSSL 为 Libra SSL、GSoC 为 G-Sog、Baptiste Daroussin 为 Baptiste Darosun、Antoine Jacoutot 为 Antoine Jacuto 等），语义虽可由语境恢复，但引用具体专名、数字与版本前须回查邮件列表原文、演讲录像与代码仓库记录。 [存疑脚注] 专名与数字均出自失真转写且未经原始史料核验；Beehive 疑为 bhyve，Libra SSL 疑为 LibreSSL，G-Sog 疑为 GSoC（BSD Now EP71，[3123.46-3135.96]，L4）
- 转录将 Ralink/Realtek 与 Atheros 的表述交错，主持人与嘉宾均存在口误修正，具体芯片归属需对照 FreeBSD 源码。 [存疑脚注] 无线芯片厂商归属存在口语转写歧义，未以代码仓库核验（BSD Now EP55，[1486.52-1493.84]，L4）

**文献**：

- [BSD Now EP370] Pennington J. BSD Now: 370: Testing shutdown[EB/OL]. (2020-10-01)[2026-08-15]. <https://www.bsdnow.tv/370>.
- [BSD Now EP71] Pennington J. BSD Now: 71: System Disaster[EB/OL]. (2015-01-07)[2026-08-15]. <https://www.bsdnow.tv/71>.
- [BSD Now EP55] Pennington J. BSD Now: 55: The Promised WLAN[EB/OL]. (2014-09-17)[2026-08-15]. <https://www.bsdnow.tv/55>.

<!-- /PODCAST_REVIEW -->