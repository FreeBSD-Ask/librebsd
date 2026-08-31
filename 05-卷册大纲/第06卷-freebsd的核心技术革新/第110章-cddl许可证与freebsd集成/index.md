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

