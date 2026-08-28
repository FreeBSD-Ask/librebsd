---
chapter: 第 89 章
id: CH89
volume: 第05卷-freebsd的工程化奠基
---

# 第 89 章 freebsd-ports系统的起源与jordan-hubbard谱系

## 要点

- FreeBSD 仓库构成（按提交量）：freebsd-ports(788411)、freebsd-src(445203)、freebsd-doc(61237)。Ports 树提交量占比最大，反映第三方软件生态的工程规模

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10489] BSD Now 第 664 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10799] BSD Now 第 613 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10875] BSD Now 第 603 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11125] BSD Now 第 573 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11132] BSD Now 第 572 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11198] BSD Now 第 564 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11752] BSD Now 第 493 期，匹配 CH89 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12548] BSD Now 第 416 期，匹配 CH89 章，关联度 1.0

- [DB:code_repos:freebsd.duckdb] FreeBSD 仓库构成（按提交量）：freebsd-ports(788411)、freebsd-src(445203)、freebsd-doc(61237)。Ports 树提交量占比最大，反映第三方软件生态的工程规模

## 史观

- 形式主义：Ports 系统是'软件包管理'这一形式主义概念在 FreeBSD 生态中的物质化

## 辨析

- 部分 bsd.port.mk 的大改未在 commit message 中标注版本号，需以功能为分界；**统计局限性标注**——统计显著 ≠ 实际显著，C-12 变点 p < 0.001 仅反映 freebsd-src commit 时序存在结构性断点，不直接等同于 Ports 系统同期发生同步变点；E-14 FreeBSD ports 784,191 commits 包含 Ports 系统全生命
- 40,000+（2022）与 34,000+（2024）两组数字可能分别对应“仓库中全部 port 条目数”与“可构建/活跃 port 数”，须在正文中明确标注口径，避免引用冲突；Mingrone 所载 SVN 接管日期（2012-07-15）与本卷 87.8 节 ports 仓库迁移首 commit 日期（2012-07-14）相差一日，须以 SVN 转换日志为准交叉核验
- CVSup 废弃的精确时间存在 2008(SVN 迁移) 与 2012(最后镜像关闭) 两种说法
- pkgng 是否“解决”了分歧存在争议，Ports 仍保留编译选项
- 考据过程留痕——【查证来源】pkg(8) 手册页经 FreeBSD 官方文档一手核验，pkg(8) 命令行工具与子命令集（install/upgrade/delete/query/info 等）在手册页中完整描述；freebsd-pkg 邮件列表 2011-2016 归档经 <https://lists.freebsd.org/archives/freebsd-pkg/> 一手核验，覆盖 pkgn

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 freebsd.duckdb

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第89章-freebsd-ports系统的起源与jordan-hubbard谱系 -->

## 要点（播客口述史提取）
- added to it since he presented it originally uh he said it was an exciting trip with an opportunity
- but he says he got started in OpenBSD back about the time when he started college,
- So he says, my first example is a bug in the original NetBSD FTP client,
- So he took the original NetBSD FTP client and they added one feature.
- So, Andrew Gapon re-implemented it in the FreeBSD native ZFS or VFS specific bits.
- Yeah. So on a Lumos, in that ZFS directory under snapshots, you can create a new snapshot by doing mkdir, the name of the snapshot, and it will create a snapshot. That worked on FreeBSD until it was removed yesterday. What never worked on FreeBSD were the other bits of it, where on a Lumos, you can also delete a snapshot by removing the directory. 
- in FreeBSD first, was there anything else that led you into working on encrypted crash dumps?
- developers I went to EuroBSD call in 2013 where I met Pavel so I could

## 史料（播客提及）
- [BSD Now EP184 @ 3610.33984375] And I think it's very important to have such technical support
- [BSD Now EP184 @ 3685.179931640625] you and actually even Thomas or Tras before you becoming developers in FreeBSD after going
- [BSD Now EP184 @ 4439.07958984375] So I think you'd need to read the book and then once you understand the concepts, apply the FreeBSD style guide to your code.
- [BSD Now EP184 @ 5301.60009765625] will be able to use free bsd update again i think that's the idea here he said should i post to a
- [BSD Now EP184 @ 5305.72021484375] particular mailing list file a bug report do both or something else well i think you're already

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP184 @ 3610.33984375] And I think it's very important to have such technical support
- [BSD Now EP184 @ 3685.179931640625] you and actually even Thomas or Tras before you becoming developers in FreeBSD after going
- [BSD Now EP184 @ 4439.07958984375] So I think you'd need to read the book and then once you understand the concepts, apply the FreeBSD style guide to your code.
- [BSD Now EP184 @ 5301.60009765625] will be able to use free bsd update again i think that's the idea here he said should i post to a
- [BSD Now EP184 @ 5305.72021484375] particular mailing list file a bug report do both or something else well i think you're already
- [BSD Now EP184 @ 5376.9599609375] that i found that list free bsd included just with unix and linux and they don't actually run it well
- [BSD Now EP184 @ 759.0399780273438] The point there is that you can actually build NetBSD on not NetBSD,
- [BSD Now EP74 @ 111.37999725341797] But Jordan Hubbard, I think, did the keynote for that,

## 辨析（播客争议与存疑点）
- [存疑脚注] [BSD Now EP184 @ 1677.199951171875] which is what OpenBSD would have inherited when they forked from NetBSD.
- [存疑脚注] [BSD Now EP184 @ 2136.919921875] Yeah. So on a Lumos, in that ZFS directory under snapshots, you can create a new snapshot by doing mkdir, the name of the snapshot, and it will create a snapshot. That worked on FreeBSD until it was removed yesterday. What never worked on FreeBSD wer

## 文献（播客参考条目）
- [BSD Now EP184] Pennington J. BSD Now: 184: Tokyo Dreaming[EB/OL]. (2017-03-08)[2026-08-15]. https://www.bsdnow.tv/184.
- [BSD Now EP74] Pennington J. BSD Now: 74: That Sly MINIX[EB/OL]. (2015-01-28)[2026-08-15]. https://www.bsdnow.tv/74.

<!-- /PODCAST_MINE -->