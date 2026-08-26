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
