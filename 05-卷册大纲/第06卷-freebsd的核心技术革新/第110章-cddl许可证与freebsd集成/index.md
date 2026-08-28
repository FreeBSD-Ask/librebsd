---
chapter: 第 110 章
id: CH110
volume: 第06卷-freebsd的核心技术革新
---

# 第110章 cddl许可证与freebsd集成

# 第 110 章 cddl许可证与freebsd集成

## 要点

- CDDL 与 GPL 不兼容争议从 2005 年 CDDL 发布持续至今（2025 年），核心事件时间线为：2004 年 12 月 CDDL 提交 OSI；2005 年 1 月 OSI 批准 CDDL；2005 年 6 月 OpenSolaris 发布；2005 年 11 月 ZFS 源码发布；2006 年 FSF 在许可证列表中标注 CDDL 为 GPL 不兼容；2007-2008 年 Pawe
- OpenSolaris 时期（2005-2010 年）的 ZFS 一手史料面临严重的访问性问题：OpenSolaris 源码仓库（hg.opensolaris.org）于 2010 年 Oracle 收购后逐渐下线；Sun 官方文档站点（docs.sun.com）在 Oracle 收购后多次迁移，大量 ZFS 文档链接失效；OpenSolaris 邮件列表（opensolaris.org/os/c
- Dawidek 的 ZFS 移植工作主要在 <freebsd-current@freebsd.org> 和 <freebsd-arch@freebsd.org> 邮件列表上公开讨论，关键邮件包括：2006 年末 Dawidek 宣布启动 ZFS 移植的邮件；2007 年 4 月 ZFS 代码导入 Perforce 仓库的通知；2007 年 4 月 6 日 ZFS 主干导入 commit（经 bsd

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_543] 卷“第06卷-freebsd的核心技术革新”第 110 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:bsdnow_podcast:outline_mappings:om_11222] BSD Now 第 562 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11357] BSD Now 第 546 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11944] BSD Now 第 474 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12219] BSD Now 第 445 期，匹配 CH110 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12237] BSD Now 第 444 期，匹配 CH110 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 需纠正一个常见误解：FreeBSD 之所以能集成 ZFS，并非因为 BSD 许可证 “比 GPL 更自由”，而是因为 BSD 许可证是 permissive（宽松许可）——它不对与之聚合分发的代码施加许可要求；GPL 是 copyleft 许可，要求衍生作品整体以 GPL 发布，因此与 CDDL 的文件级 copyleft 冲突；这不是 “自由程度” 的差异，而是 copyleft 边界设计的差异
- 原文 50.5 节标题写 “2007 年 ZFS 开源至 OpenSolaris” 有事实错误——ZFS 于 2005 年 11 月开源，OpenSolaris 本身于 2005 年 6 月发布，2007 年并非 ZFS 开源年份；Pawel Dawidek 的 FreeBSD ZFS 移植 commit hash 经 freebsd.db `commits` 表查询验证——FreeBSD src
- 经 freebsd.db `commits` 表与 `commit_files` 表交叉验证，Dawidek 的 ZFS 主干导入 commit 已确认为 `f0a75d274af375d15b97b830966b99a02b7db911`（author = committer = Pawel Jakub Dawidek，<pjd@FreeBSD.org>，author_date = commit

## 文献

- FreeBSD Project. *FreeBSD 7.0 Release Notes* (2008-02-27). freebsd.org; OpenZFS Project. *OpenZFS 2.0.0 Release Notes* (2020-11-30). github.com/openzfs/zfs/releases; Ubuntu Technical Board (2016-02). *Meeting Minutes*. lists.ubuntu.com; LWN.net. *ZFS Coverage Timeline*. lwn.net.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Internet Archive. *opensolaris.org Archive*. web.archive.org/web/*/<https://opensolaris.org>; illumos Project.* illumos-gate Repository *. github.com/illumos/illumos-gate; FreeBSD Project.* Vendor Import of OpenSolaris Code *. svn.freebsd.org/base/vendor/opensolaris/; genunix.org. * OpenSolaris Community Archive*. genunix.org; Dawidek P J. Please welcome ZFS - The last word in file systems. freebsd-src [DB/OL]. 2007-04-06T01:09:06Z. f0a75d274af375d15b97b830966b99a02b7db911. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2005-2005 年间：42,570 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. *Mailing List Archives*. lists.freebsd.org/pipermail/; FreeBSD Project. *Git Repository*. git.freebsd.org/src.git; Dawidek, P. J. (2007). *Porting ZFS to FreeBSD*. BSDCan 2007; FreeBSD Project. *Subversion to Git Migration Notes* (2020); Dawidek P J. Please welcome ZFS - The last word in file systems. freebsd-src [DB/OL]. 2007-04-06T01:09:06Z. f0a75d274af375d15b97b830966b99a02b7db911. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第110章-cddl许可证与freebsd集成 第110章 cddl许可证与freebsd集成（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：5 期，扫描 segments：5253 条 -->

### 要点（播客口述史提取）
- collation thing, he decided it was time that FreeBSD got its proper string（BSD Now EP115 @ 1492.659）
- So he started working with John and importing the Dragonfly code into FreeBSD.（BSD Now EP115 @ 1503.619）
- had started that John extended and brought it back into FreeBSD. So now as a result of（BSD Now EP115 @ 1553.739）
- thing that got me started into actually working on FreeBSD related things. And then,（BSD Now EP115 @ 1955.079）
- But basically, when the cam target layer was originally introduced by a company in the FreeBSD,（BSD Now EP115 @ 687.2600）

### 史料（播客当事人陈述）
- Okay, so lastly here we got an article about switching from OS X to FreeBSD.（BSD Now EP115 @ 4176.520）
- Certainly the FreeBSD 2.0 source code, which he has handy access to via the GitHub repo,（BSD Now EP131 @ 1491.479）
- You know, buy the FreeBSD Mastery ZFS book.（BSD Now EP131 @ 3742.899）
- utini has a nice blog post slash tutorial on how to get started with it on freebsd so first of all（BSD Now EP131 @ 4193.199）

### 史观（播客当事人观点与总纲映射）
- in FreeBSD so that will be uh I think I will have to go to that one and learn a bit more about it（BSD Now EP131 @ 430.6600）
- Well, I think this is just an exporter similar to how FreeBSD does GitHub.（BSD Now EP203 @ 5152.779）
- I think the FreeBSD port enabled SSL by default, I think, is what happened.（BSD Now EP203 @ 6702.379）
- FreeBSD and I think OpenBSD for quite a long time. This is moving it out of the OS into the firewall.（BSD Now EP233 @ 2531.339）

### 辨析（播客争议与存疑点）
- [存疑脚注] Well, it has been forked to run on FreeBSD Open and NetBSD now as well.（BSD Now EP115 @ 1269.559）
- [存疑脚注] So we fired up my laptop running FreeBSD beside it and attempted to recreate the problem there（BSD Now EP232 @ 186.02）

### 文献（播客参考条目）
- [BSD Now EP115] Pennington J. BSD Now: 115: Controlling the Transmissions[EB/OL]. (2015-11-11)[2026-08-15]. https://www.bsdnow.tv/115.
- [BSD Now EP131] Pennington J. BSD Now: 131: BSD behind the chalkboard[EB/OL]. (2016-03-02)[2026-08-15]. https://www.bsdnow.tv/131.
- [BSD Now EP203] Pennington J. BSD Now: 203: For the love of ZFS[EB/OL]. (2017-07-19)[2026-08-15]. https://www.bsdnow.tv/203.
- [BSD Now EP232] Pennington J. BSD Now: 232: FOSDEM 2018[EB/OL]. (2018-02-07)[2026-08-15]. https://www.bsdnow.tv/232.
- [BSD Now EP233] Pennington J. BSD Now: 233: High on ZFS[EB/OL]. (2018-02-14)[2026-08-15]. https://www.bsdnow.tv/233.

<!-- /PODCAST_MINE -->
