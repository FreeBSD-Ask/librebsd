---
chapter: 第 127 章
id: CH127
volume: 第06卷-freebsd的核心技术革新
---

# 第 127 章 freebsd100的发布与大整合开端

## 要点

- FreeBSD 提交高峰期：2024年(63750次)，对应 10.x 大整合与 pkg 迁移时期

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3699] 卷“第06卷-freebsd的核心技术革新”第 127 章，匹配置信度 folder，原因：folder 第125章

- [DB:code_repos:freebsd.duckdb] FreeBSD 提交高峰期：2024年(63750次)，对应 10.x 大整合与 pkg 迁移时期

## 史观

- 偶然性优先：FreeBSD 10.0 的大整合是多项技术路线偶然交汇的结果

## 辨析

- 10.0 支持周期（原计划至 2015.1.31）实际因后续 10.1/10.2 等版本发布而延长——单个 RELEASE 版本支持周期通常为至下一个次版本发布后一个月，stable/10 分支整体支持至 2018.10.31。
- bhyve 在 10.1 仍不支持 SMP 客户机（多 vCPU）——SMP 客户机支持在 10.3 才加入（10.1 中 bhyve 客户机仅限单 vCPU）；bhyve 在 10.1 仍无 UEFI 固件支持——uefi-edk2-bhyve 端口在 10.x 后期才成熟。
- 原文件提到 “pkg 1.10.1 升级后整个 pkg 环境无法使用、从 1.x 升级到 2.10 时大量包被意外安装、jail 环境中 pkg 命令陷入无限循环”——这些问题发生在 pkg 1.x 早期版本（约 2014-2015 年），属迁移期真实问题但多数在 10.2 时期已修复；pkg 2.x 系列实际是在更晚版本中出现，10.x 携带的是 pkg 1.x 系列。
- 10.3 中 Hyper-V 集成持续改进但 Azure 镜像在 10.3 Announcement 中仍链接 VMDepot 而非 Azure Marketplace（10.4 才正式进入 Azure Marketplace）。
- 不应将 10.x 神化为 “最好的 FreeBSD 版本”——10.0-10.2 时期存在大量迁移期 bug，10.3/10.4 才趋于稳定；但 10.x 时期完成的基础架构转型规模与深度在 FreeBSD 历史上前所未有，其工程价值在后续版本中得到充分体现。

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 freebsd.duckdb
