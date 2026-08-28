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
<!-- 章节主题过滤：第89章-freebsd-ports系统的起源与jordan-hubbard谱系 第 89 章 freebsd-ports系统的起源与jordan-hubbard谱系（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：8 期，扫描 segments：8079 条 -->

### 要点（播客口述史提取）
- So this is different from BSD Journal we mentioned earlier, which is being started in part by the FreeBSD Foundation.（BSD Now EP13 @ 2728.239）
- the same so you know i see huge difference so uh last friday he decided to download freebsd and（BSD Now EP13 @ 3354.539）
- and push new packages out ahead of maybe the original FreeBSD repo.（BSD Now EP13 @ 3734.899）
- so of course we released a new pcbsd 10.1 on monday so following freebsd 10.1 and of course it（BSD Now EP64 @ 1552.520）
- The original FreeBSD code disables and enables the keyboard port all the time（BSD Now EP64 @ 6695.359）

### 史料（播客当事人陈述）
- So we did mention last week about Jordan Hubbard giving a talk on some of the integrating different parts of Mac OS X into FreeBSD.（BSD Now EP105 @ 325.4400）
- We're working on getting interviews with both Kip Macy and Jordan Hubbard about this.（BSD Now EP105 @ 485.2200）
- coming up on this week's episode we have an interview with jordan hubbard about the new（BSD Now EP113 @ 0.0）
- Belied the size each of the three days of the conference featured a different keynote speaker in addition to Jordan Hubbard（BSD Now EP261 @ 1498.32）

### 史观（播客当事人观点与总纲映射）
- But he says, I've been trying to figure out what the reasoning is behind FreeBSD's selection of default shells.（BSD Now EP64 @ 5635.399）
- number which means a really old bug in freebsd um so i think the tool is still there to find（BSD Now EP64 @ 6149.879）
- But it's a very promising direction for FreeNAS, I think, and for FreeBSD-based appliances in general.（BSD Now EP113 @ 1891.619）
- And honestly, I spent more time on FreeBSD questions in those first three years than I did on almost any other day in the past.（BSD Now EP113 @ 5599.579）

### 辨析（播客争议与存疑点）
- [存疑脚注] Maintaining a fork of the FreeBSD ports tree is a non-trivial task. There are 30,000 packages in there.（BSD Now EP261 @ 460.98）
- [存疑脚注] Partly because, you know, FreeBSD project doesn't want to have to maintain a fork of X in order to maintain the ABI stability across, you know, the five-year life cycle of FreeBSD 10.（BSD Now EP105 @ 3315.979）
- [存疑脚注] And this, of course, is causing a little controversy in the FreeBSD community here as well.（BSD Now EP105 @ 341.3200）
- [存疑脚注] Yeah. So on a Lumos, in that ZFS directory under snapshots, you can create a new snapshot by doing mkdir, the name of the snapshot, and it will create a snapshot. That worked on FreeBSD until it was removed yesterday. What never worked on FreeBSD were the other bits of it, where on a Lumos, you can also delete a snapshot by removing the directory. And you can rename a snapshot by just renaming the（BSD Now EP184 @ 2136.919）

### 文献（播客参考条目）
- [BSD Now EP13] Pennington J. BSD Now: 13: Bridging the Gap[EB/OL]. (2013-11-27)[2026-08-15]. https://www.bsdnow.tv/13.
- [BSD Now EP64] Pennington J. BSD Now: 64: Rump Kernels Revisited[EB/OL]. (2014-11-19)[2026-08-15]. https://www.bsdnow.tv/64.
- [BSD Now EP74] Pennington J. BSD Now: 74: That Sly MINIX[EB/OL]. (2015-01-28)[2026-08-15]. https://www.bsdnow.tv/74.
- [BSD Now EP104] Pennington J. BSD Now: 104: Beverly Hills 25519[EB/OL]. (2015-08-26)[2026-08-15]. https://www.bsdnow.tv/104.
- [BSD Now EP105] Pennington J. BSD Now: 105: Virginia BSD Assembly[EB/OL]. (2015-09-02)[2026-08-15]. https://www.bsdnow.tv/105.
- [BSD Now EP113] Pennington J. BSD Now: 113: What’s Next for BSD?[EB/OL]. (2015-10-28)[2026-08-15]. https://www.bsdnow.tv/113.
- [BSD Now EP184] Pennington J. BSD Now: 184: Tokyo Dreaming[EB/OL]. (2017-03-08)[2026-08-15]. https://www.bsdnow.tv/184.
- [BSD Now EP261] Pennington J. BSD Now: Episode 261: FreeBSDcon Flashback | BSD Now 261[EB/OL]. (2018-08-30)[2026-08-15]. https://www.bsdnow.tv/261.

<!-- /PODCAST_MINE -->
