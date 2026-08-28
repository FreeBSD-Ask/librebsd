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

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第171章-systemd与bsd-init的哲学合图层 -->

## 要点（播客口述史提取）
- So there's a GitHub repo where you have a version of FreeBSD with the patches to work
- Which wrote an article about why they use open BSD. So first of all who they are
- And then I've seen the already started planning and holding polls on Twitter about VBSD con
- So first up, Ed Mass, over at the FreeBSD project,
- So in FreeBSD, they've had a BSD license version of DTC,
- Alan introduced me to BSD and tech snap a few months ago and I started listening to BSD
- Therefore, setting it to 1 is now ignored, and after the release of OpenBSD 6.0, we'll delete the CCTL entirely.
- be a downside for, especially since OpenBSD is the only version of X that doesn't require

## 史料（播客提及）
- [BSD Now EP151 @ 115.0199966430664] this on other BSDs as well. But it looks like some of the list in order of severity, I think is how
- [BSD Now EP151 @ 1763.3599853515625] gonzo at FreeBSD.org has a post up on the kernel Nomicon about actually
- [BSD Now EP151 @ 1768.4400634765625] getting it running FreeBSD so you can see it's actually connected up and he's
- [BSD Now EP151 @ 3147.9599609375] and I think Freeness turns it off as well, and PCBSD does.
- [BSD Now EP35 @ 1381.780029296875] And coming from IP tables and discovering actually my first OpenBSD firewall was with IPF,

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP151 @ 115.0199966430664] this on other BSDs as well. But it looks like some of the list in order of severity, I think is how
- [BSD Now EP151 @ 1763.3599853515625] gonzo at FreeBSD.org has a post up on the kernel Nomicon about actually
- [BSD Now EP151 @ 1768.4400634765625] getting it running FreeBSD so you can see it's actually connected up and he's
- [BSD Now EP151 @ 3147.9599609375] and I think Freeness turns it off as well, and PCBSD does.
- [BSD Now EP35 @ 1381.780029296875] And coming from IP tables and discovering actually my first OpenBSD firewall was with IPF,
- [BSD Now EP35 @ 1846.5599365234375] system. That's finally now in OpenBSD 5.5. The background for OpenBSD, I think all the
- [BSD Now EP35 @ 1954.5599365234375] Now FreeBSD doesn't have that yet, and I think that's a great shame.
- [BSD Now EP35 @ 2625.2998046875] And I think the other thing that contributed a lot to FreeBSD doing its own thing was that

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP253 @ 2262.7] So now we have a version of mere BSD's corn shell running on Jahane, which is a fork of plan 9.
- [存疑脚注] [BSD Now EP253 @ 5048.8] with FreeBSD. I guess that just the name itself could suggest it is in fact a big fork.
- [存疑脚注] [BSD Now EP92 @ 1562.5599365234375] Okay, imports started out as kind of a fork of the FreeBSD ports tree.
- [存疑脚注] [BSD Now EP92 @ 1696.5999755859375] Okay, so being a fork from a bit older version of free BSD. What's the harbor support like?
- [存疑脚注] [BSD Now EP92 @ 8.779999732971191] It's a slightly lesser known fork of free BSD with a focus on easy desktop use.
- [存疑脚注] [BSD Now EP252 @ 3267.52] Saying that macOS 10 is just FreeBSD with an Apple GUI is certainly false on face value,

## 文献（播客参考条目）
- [BSD Now EP151] Pennington J. BSD Now: 151: Fuzzy Auditing[EB/OL]. (2016-07-20)[2026-08-15]. https://www.bsdnow.tv/151.
- [BSD Now EP35] Pennington J. BSD Now: 35: Puffy Firewall[EB/OL]. (2014-04-30)[2026-08-15]. https://www.bsdnow.tv/35.
- [BSD Now EP253] Pennington J. BSD Now: Episode 253: Silence of the Fans | BSD Now 253[EB/OL]. (2018-07-05)[2026-08-15]. https://www.bsdnow.tv/253.
- [BSD Now EP92] Pennington J. BSD Now: 92: BSD After Midnight[EB/OL]. (2015-06-03)[2026-08-15]. https://www.bsdnow.tv/92.
- [BSD Now EP252] Pennington J. BSD Now: Episode 252: Goes to 11.2 | BSD Now 252[EB/OL]. (2018-06-28)[2026-08-15]. https://www.bsdnow.tv/252.
- [BSD Now EP150] Pennington J. BSD Now: 150: Sprinkle a little BSD into your life.[EB/OL]. (2016-07-13)[2026-08-15]. https://www.bsdnow.tv/150.
- [BSD Now EP55] Pennington J. BSD Now: 55: The Promised WLAN[EB/OL]. (2014-09-17)[2026-08-15]. https://www.bsdnow.tv/55.
- [BSD Now EP96] Pennington J. BSD Now: 96: Lost Technology[EB/OL]. (2015-07-01)[2026-08-15]. https://www.bsdnow.tv/96.
- [BSD Now EP257] Pennington J. BSD Now: Episode 257: Great NetBSD 8 | BSD Now 257[EB/OL]. (2018-08-02)[2026-08-15]. https://www.bsdnow.tv/257.
- [BSD Now EP128] Pennington J. BSD Now: 128: The State of BSD[EB/OL]. (2016-02-10)[2026-08-15]. https://www.bsdnow.tv/128.
- [BSD Now EP158] Pennington J. BSD Now: 158: Ham, Radio and Pie (oh my)[EB/OL]. (2016-09-07)[2026-08-15]. https://www.bsdnow.tv/158.
- [BSD Now EP335] Pennington J. BSD Now: 335: FreeBSD Down Under[EB/OL]. (2020-01-30)[2026-08-15]. https://www.bsdnow.tv/335.
- [BSD Now EP276] Pennington J. BSD Now: Episode 276: Ho, Ho, Ho - 12.0 | BSD Now 276[EB/OL]. (2018-12-13)[2026-08-15]. https://www.bsdnow.tv/276.
- [BSD Now EP105] Pennington J. BSD Now: 105: Virginia BSD Assembly[EB/OL]. (2015-09-02)[2026-08-15]. https://www.bsdnow.tv/105.
- [BSD Now EP107] Pennington J. BSD Now: 107: In their midst[EB/OL]. (2015-09-16)[2026-08-15]. https://www.bsdnow.tv/107.
- [BSD Now EP217] Pennington J. BSD Now: 217: Your questions, part II[EB/OL]. (2017-10-25)[2026-08-15]. https://www.bsdnow.tv/217.
- [BSD Now EP15] Pennington J. BSD Now: 15: Kickin' NAS[EB/OL]. (2013-12-11)[2026-08-15]. https://www.bsdnow.tv/15.
- [BSD Now EP135] Pennington J. BSD Now: 135: Speciality MWL[EB/OL]. (2016-03-30)[2026-08-15]. https://www.bsdnow.tv/135.
- [BSD Now EP237] Pennington J. BSD Now: 237: AsiaBSDcon 2018[EB/OL]. (2018-03-14)[2026-08-15]. https://www.bsdnow.tv/237.
- [BSD Now EP76] Pennington J. BSD Now: 76: Time for a Change[EB/OL]. (2015-02-11)[2026-08-15]. https://www.bsdnow.tv/76.
- [BSD Now EP236] Pennington J. BSD Now: 236: How a cd works[EB/OL]. (2018-03-07)[2026-08-15]. https://www.bsdnow.tv/236.
- [BSD Now EP114] Pennington J. BSD Now: 114: BSD-Schooling[EB/OL]. (2015-11-04)[2026-08-15]. https://www.bsdnow.tv/114.
- [BSD Now EP73] Pennington J. BSD Now: 73: Pipe Dreams[EB/OL]. (2015-01-21)[2026-08-15]. https://www.bsdnow.tv/73.
- [BSD Now EP54] Pennington J. BSD Now: 54: Luminary Environment[EB/OL]. (2014-09-10)[2026-08-15]. https://www.bsdnow.tv/54.
- [BSD Now EP118] Pennington J. BSD Now: 118: BSD is go for Launch[EB/OL]. (2015-12-02)[2026-08-15]. https://www.bsdnow.tv/118.
- [BSD Now EP345] Pennington J. BSD Now: 345: Switchers to BSD[EB/OL]. (2020-04-09)[2026-08-15]. https://www.bsdnow.tv/345.
- [BSD Now EP337] Pennington J. BSD Now: 337: Kubernetes on bhyve[EB/OL]. (2020-02-13)[2026-08-15]. https://www.bsdnow.tv/337.
- [BSD Now EP67] Pennington J. BSD Now: 67: Must Be Rigged[EB/OL]. (2014-12-10)[2026-08-15]. https://www.bsdnow.tv/67.
- [BSD Now EP416] Pennington J. BSD Now: 416: netcat printing[EB/OL]. (2021-08-19)[2026-08-15]. https://www.bsdnow.tv/416.
- [BSD Now EP31] Pennington J. BSD Now: 31: Edgy BSD Users[EB/OL]. (2014-04-01)[2026-08-15]. https://www.bsdnow.tv/31.
- [BSD Now EP233] Pennington J. BSD Now: 233: High on ZFS[EB/OL]. (2018-02-14)[2026-08-15]. https://www.bsdnow.tv/233.
- [BSD Now EP318] Pennington J. BSD Now: 318: The TrueNAS Library[EB/OL]. (2019-10-03)[2026-08-15]. https://www.bsdnow.tv/318.
- [BSD Now EP62] Pennington J. BSD Now: 62: Gift from the Sun[EB/OL]. (2014-11-05)[2026-08-15]. https://www.bsdnow.tv/62.
- [BSD Now EP210] Pennington J. BSD Now: 210: Your questions, part I[EB/OL]. (2017-09-06)[2026-08-15]. https://www.bsdnow.tv/210.

<!-- /PODCAST_MINE -->