---
chapter: 第 121 章
id: CH121
volume: 第06卷-freebsd的核心技术革新
---

# 第 121 章 freebsd存储栈的ffs与ufs演进

## 要点

- 中文网络上关于 UFS/FFS 历史的常见错误包括：FFS 发布年份误作 1984 年（应为 1983 年 8 月随 4.2BSD 发布，论文 1984 年发表）、Soft Updates 引入 FreeBSD 版本误作 5.0（应为 3.x 时期集成，4.x 默认启用）、UFS2 设计者遗漏 Poul-Henning Kamp（McKusick 与 phk 共同设计）、SUJ 引入版本误作 Fr
- GEOM 引入 FreeBSD 的精确时间为 FreeBSD 5.0（2003 年 1 月），但开发工作从 2001-2002 年即已开始，在 FreeBSD 5.0-CURRENT 分支中逐步替换旧存储层；GEOM 与 Linux Device Mapper（2002 年 Red Hat 主导开发，随 Linux 2.6 引入）是同时代产物，但设计哲学存在关键差异：GEOM 是纯内核态框架，用户
- CAM 从仅支持并行 SCSI 到统一支持 SCSI/SAS/SATA/USB/NVMe 的演进历时 20 余年（1998-2020+），核心阶段包括：FreeBSD 3.0（1998）CAM 导入支持并行 SCSI；FreeBSD 5.x USB **umass(4)** 通过 CAM 接入；FreeBSD 8.x-9.x ATA/SATA 整合入 CAM 成为 **ada(4)**；FreeB
- FreeBSD NFS 支持历史：NFSv2 在 BSD 4.3 时代即已引入，NFSv3 在 FreeBSD 3.x/4.x 时期支持，NFSv4 由 Rick Macklem 主导重写，新的 NFSv4 客户端/服务器实现随 FreeBSD 8.2/9.0（2012 年前后）引入，支持 NFSv4.0、NFSv4.1（含 pNFS 部分特性），旧 NFS 实现仍保留为兼容；NFS 实现位于内核

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3827] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 folder，原因：folder 第119章
- [DB:references_fulltext:chapter_matches:chmatch_3967] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 folder，原因：folder 第119章
- [DB:references_fulltext:chapter_matches:chmatch_3661] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3662] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3664] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_348] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_351] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_352] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_359] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_363] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:bsdnow_podcast:outline_mappings:om_11314] BSD Now 第 552 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11691] BSD Now 第 505 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11841] BSD Now 第 484 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12067] BSD Now 第 461 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12108] BSD Now 第 456 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12136] BSD Now 第 454 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12534] BSD Now 第 417 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12634] BSD Now 第 401 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12678] BSD Now 第 379 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10637] BSD Now 第 637 期，匹配 CH121 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 需澄清一个常见误解：“UFS 是 FFS 的另一个名字”——在 BSD 术语中，UFS 指上层目录结构和元数据处理代码（src/sys/ufs/ufs/），FFS 指下层数据块分配和物理布局代码（src/sys/ufs/ffs/），两者共同构成完整的文件系统实现；Solaris UFS、macOS 旧版 UFS 均从 BSD UFS/FFS 衍生但各自有扩展（如 Solaris UFS Loggi
- 需纠正一个关于 GEOM 设计来源的说法：“GEOM 是 Netgraph 移植到存储”——phk 本人多次表示 GEOM 受 Netgraph 启发，但存储与网络有本质差异：存储 I/O 必须按请求顺序完成（生物序等价性），网络包可乱序、复制、丢弃，因此 GEOM 的实现与 Netgraph 完全独立；GEOM 是否 “未完成”——**geom_sched(8)**（I/O 调度器）模块长期处于
- 需澄清 “Linux SCSI midlayer 与 CAM 谁更先进” 的无意义比较——两者架构目标不同：CAM 是所有存储传输的统一抽象，Linux SCSI midlayer 仅处理 SCSI 协议类设备，ATA 走 libata、NVMe 走独立驱动，块层是另一层抽象；两种架构各有优劣：CAM 的统一带来工具和错误处理的一致性，但要让新协议适配 CAM 需要额外工作；Linux 的分层更灵
- 时间线错误：“NFSv4 在 FreeBSD 8.0 引入”——新 NFSv4 客户端/服务器代码在 FreeBSD 8.2（2011 年 7 月）和 9.0（2012 年 1 月）中正式发布，旧的 NFSv2/v3 实现继续可用，用户可通过 mount 选项选择使用新/旧实现；FreeBSD NFSv4.1/pNFS 支持在 FreeBSD 12/13 中持续完善；**aio(4)** 的一个误

## 文献

- FreeBSD Project. *FreeBSD Release Notes Archive*. freebsd.org/releases; McKusick, M. K. *Soft Updates, Snapshots, and Background Fsck Resources*. mckusick.com/softdep/; Aurora, V. (2009-07-01). *Soft updates, hard problems*. LWN.net, lwn.net/Articles/339337/; McKusick, M. K., Neville-Neil, G. V., & Watson, R. N. M. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Addison-Wesley, Chapter 8. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Kamp, P.-H. (2004). *GEOM Tutorial*. BSDCan 2004; FreeBSD Project. **geom(4)**, **geom(8)** Manual Pages; Linux Kernel Documentation. *Device Mapper*. kernel.org/doc; Lucas, M. W. (2018). *FreeBSD Mastery: Storage Essentials*. Chapter 3-5.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. **camcontrol(8)** Manual Page; McKusick, M. K. et al. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Chapter 10; FreeBSD Project. *CAM Subsystem Source Tree*. src/sys/cam/. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. **nfs(5)**, **aio(4)**, **nfsstat(1)** Manual Pages; Macklem, R. (2009-2012). *New NFSv4 Client/Server Implementation Commits*; FreeBSD Project. *FreeBSD 9.0 Release Notes* NFSv4 section; McKusick, M. K. et al. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Chapter 9. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第121章-freebsd存储栈的ffs与ufs演进 -->

## 要点（播客口述史提取）
- we did release our PCBSD 10.1.2 quarterly update this last Monday.
- Okay, first up we have Dominic writes in about a BSD install fest.
- And he's looking forward to having lots of good BSD talk in 2015.
- vm so he asks will i be able to mount the zfs created under free nas under free bsd 10.1 how
- bsd 10.1 they've backported them all and those would be like the feature flags for your z yeah
- They are pleased to announce the release of GhostBSD 11.1 on 64-bit architecture with made an XFCE desktop on direct and torrent downloads.
- There are new versions of Lumina and Ghost BSD available for you to check out.
- Making your own ports is an easy and fun way to make your first contribution to a BSD project.

## 史料（播客提及）
- [BSD Now EP90 @ 1466.0799560546875] a lot of the information that's in there is actually not necessarily accurate for free BSD.
- [BSD Now EP90 @ 4054.33984375] nice okay well he does say here eventually i want to replace the free nas with free bsd without the
- [BSD Now EP221 @ 1697.43994140625] is interesting um there's also talk a short one about bsd miser which is actually from the company
- [BSD Now EP221 @ 2234.079833984375] laundry list of demands for his little pdf viewer program uh i think by the end of bsd can he had a
- [BSD Now EP221 @ 4884.1201171875] And I think if we just had a couple more people doing that for FreeBSD,

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP90 @ 1466.0799560546875] a lot of the information that's in there is actually not necessarily accurate for free BSD.
- [BSD Now EP90 @ 4054.33984375] nice okay well he does say here eventually i want to replace the free nas with free bsd without the
- [BSD Now EP221 @ 1697.43994140625] is interesting um there's also talk a short one about bsd miser which is actually from the company
- [BSD Now EP221 @ 2234.079833984375] laundry list of demands for his little pdf viewer program uh i think by the end of bsd can he had a
- [BSD Now EP221 @ 4884.1201171875] And I think if we just had a couple more people doing that for FreeBSD,
- [BSD Now EP298 @ 1864.699951171875] architecture support in free bsd ports well this is i think from his rss aggregator thing
- [BSD Now EP298 @ 1870.699951171875] but it's basically his comments on uh one of the papers from agbsdcon actually
- [BSD Now EP298 @ 1903.97998046875] work on the power processors on FreeBSD and how most of the problems can actually be solved.

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP298 @ 1749.3599853515625] So they said, now that OpenBSD 6.5 is out,
- [存疑脚注] [BSD Now EP298 @ 734.6199951171875] and they write, as a regular, it's false readers should know, I like diving into the world of BSDs.
- [存疑脚注] [BSD Now EP125 @ 5860.33984375] but they said pcbsd's default zfs file system was faster with its embedded sqlibrary
- [存疑脚注] [BSD Now EP125 @ 6034.72021484375] audio encoding they had uh dragonfly in about the middle and pcbsd last but they said that's uh
- [存疑脚注] [BSD Now EP388 @ 1650.62] bsd argument and with that you can then reload your pfrule set to apply these
- [存疑脚注] [BSD Now EP388 @ 2660.78] and also removed the UFSFoldDisk option from the installer.

## 文献（播客参考条目）
- [BSD Now EP90] Pennington J. BSD Now: 90: ZFS Armistice[EB/OL]. (2015-05-20)[2026-08-15]. https://www.bsdnow.tv/90.
- [BSD Now EP221] Pennington J. BSD Now: 221: BSD in Taiwan[EB/OL]. (2017-11-22)[2026-08-15]. https://www.bsdnow.tv/221.
- [BSD Now EP298] Pennington J. BSD Now: 298: BSD On The Road[EB/OL]. (2019-05-16)[2026-08-15]. https://www.bsdnow.tv/298.
- [BSD Now EP125] Pennington J. BSD Now: 125: DevSummits, Core and the Baldwin[EB/OL]. (2016-01-20)[2026-08-15]. https://www.bsdnow.tv/125.
- [BSD Now EP388] Pennington J. BSD Now: 388: Must-have security tool[EB/OL]. (2021-02-04)[2026-08-15]. https://www.bsdnow.tv/388.
- [BSD Now EP216] Pennington J. BSD Now: 216: Software is storytelling[EB/OL]. (2017-10-18)[2026-08-15]. https://www.bsdnow.tv/216.
- [BSD Now EP172] Pennington J. BSD Now: 172: A tale of BSD from yore[EB/OL]. (2016-12-14)[2026-08-15]. https://www.bsdnow.tv/172.
- [BSD Now EP278] Pennington J. BSD Now: Episode 278: The Real McCoy | BSD Now 278[EB/OL]. (2018-12-27)[2026-08-15]. https://www.bsdnow.tv/278.
- [BSD Now EP193] Pennington J. BSD Now: 193: Fire up the 802.11 AC[EB/OL]. (2017-05-10)[2026-08-15]. https://www.bsdnow.tv/193.
- [BSD Now EP100] Pennington J. BSD Now: 100: Straight from the Src[EB/OL]. (2015-07-29)[2026-08-15]. https://www.bsdnow.tv/100.
- [BSD Now EP195] Pennington J. BSD Now: 195: I don’t WannaCry[EB/OL]. (2017-05-24)[2026-08-15]. https://www.bsdnow.tv/195.
- [BSD Now EP120] Pennington J. BSD Now: 120: I’m talking about the man in the middle[EB/OL]. (2015-12-16)[2026-08-15]. https://www.bsdnow.tv/120.
- [BSD Now EP223] Pennington J. BSD Now: 223: Compile once, debug twice[EB/OL]. (2017-12-06)[2026-08-15]. https://www.bsdnow.tv/223.
- [BSD Now EP241] Pennington J. BSD Now: Episode 241: Bowling in the LimeLight | BSD Now 241[EB/OL]. (2018-04-12)[2026-08-15]. https://www.bsdnow.tv/241.
- [BSD Now EP566] Pennington J. BSD Now: 566: Open Source Excellence[EB/OL]. (2024-07-04)[2026-08-15]. https://www.bsdnow.tv/566.
- [BSD Now EP157] Pennington J. BSD Now: 157: ZFS, The “Universal” File-system[EB/OL]. (2016-08-31)[2026-08-15]. https://www.bsdnow.tv/157.
- [BSD Now EP260] Pennington J. BSD Now: Episode 260: Hacking Tour of Europe | BSD Now 260[EB/OL]. (2018-08-23)[2026-08-15]. https://www.bsdnow.tv/260.

<!-- /PODCAST_MINE -->