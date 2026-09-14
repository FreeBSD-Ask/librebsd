---
chapter: 第 105 章
id: CH105
volume: 第05卷-freebsd的工程化奠基
---

# 第 105 章 FreeBSD 7.x 同期的 DragonFly HAMMER 与 OS 比较

## 要点

- 比较史料疑点：（1）基准测试来源；（2）是否有选择性报告；（3）各 OS 版本对应
- 7.x 版本周期共 40 条 commit（29 CVE + 11 security fix），月均约 1.90 条/月，介于 6.x 的 1.07 条/月与 5.x 的 3.64 条/月之间。这一回升不能简单解读为“7.x 安全质量下降”，而是反映三重架构因素：其一，7.x 时期 ULE 在 7.1-RELEASE（官方公告 2009-01-04，tag 2008-12-31）成为 amd64 与 i386 GENERIC 内核默认；其二，Alpha 架构在 7.0-RELEASE 退役；其三，ip6fw 防火墙在 7.0-RELEASE 被移除。
- 路线趋同史料疑点：（1）DragonFly 选择 1:1 的时间；（2）Dillon 是否参考 FreeBSD libthr；（3）趋同是否偶然
- 7.0 发布前 ULE 2.0（Roberson 2007 重构）引发社区争论——部分开发者要求延迟发布。Core Team 最终保留 4BSD 为默认但保留 ULE 为备选。
- 批评史料疑点：（1）批评来源；（2）批评时间点；（3）是否有厂商背景

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3790] 卷“第05卷-freebsd的工程化奠基”第 105 章，匹配置信度 folder，原因：folder 第103章
- [DB:references_fulltext:chapter_matches:chmatch_3665] 卷“第05卷-freebsd的工程化奠基”第 105 章，匹配置信度 curated，原因：curated token rule

## 史观

- 〔待统一整改：本章七节史观字段的“总纲第 N 条”映射与权威 25 条总纲表主题均不匹配（如“终结与延续”“实践先于理论”“0 信任原则”“技术选择的代价”等），回填须待主代理统一映射后处置（DEFERRED）〕
- ULE 调度器从 5.0 引入到 7.1 成为默认，花了六年——当它终于成熟时，Linux 的 CFS 已经接替了 O(1)，性能竞赛的赛道又往前挪了一步。7.x 的基准测试数字确实漂亮，但“更快”不是“进步”——调度器的本质从 4BSD 的 O(n) 到 ULE 的 O(1)，变的是算法复杂度，不变的是“谁该在什么时候跑到哪个 CPU 上”这个永恒的调度问题

## 辨析

- 7.x 的 commit 月均（1.90）介于 5.x（3.64）与 6.x（1.07）之间，须谨慎解读——5.x 高位源于架构转型期的新代码密集审计，6.x 低位源于架构稳定后的低响应需求，7.x 回升主要源于 OpenSSL DTLS 漏洞群（4 条 CVE 同日修复）与 BIND 多分支回溯（CVE-2009-0696 的 4 条同日 commit）的统计放大；扣除 OpenSSL DTLS 漏洞群与 BIND 多分支回溯两组同日集中修复（合计 8 条 commit）后，7.x 的月度 commit 强度显著回落，故不宜将这一统计回升直接解读为 7.x 安全质量下降
- ULE 在 7.1 成为默认但 7.x 后续版本是否真“完全成熟”需查 8.0/9.0 release notes 与 EPFL 2018 USENIX ATC 批评；Alpha 退役是否加速 FreeBSD 在 RISC 工作站市场的衰落需对照 NetBSD/alpha 与 OpenBSD/alpha 状态；三类淘汰的相互独立性需评估

## 文献

- Phoronix FreeBSD 7.0 Benchmarks (2008)；freebsd-arch mailing list 2008 archives；LWN.net FreeBSD 7.0 review (2008) ［A］
- FreeBSD 社区论文：[FP-2008-005] An Independent H-TCP Implementation under FreeBSD 7.0 – Description and Observed Behaviour（Jeff Healy，2008）<https://papers.freebsd.org/2008/healy-cc_htcp/>

- freebsd.duckdb freebsd-src 仓库 5.x/6.x/7.x 版本周期 commit 统计对比；FreeBSD 7.x Release Notes；John Birrell DTrace 移植档案；freebsd-hackers 邮件列表 DTrace 讨论 ［A］

- Dillon, M. Kernel Native Threading (DragonFly BSD Digest, 2007)；freebsd-threads mailing list 2005-2008 archives；FreeBSD libthr commit log ［A］

- FreeBSD 邮件存档 ［A］

- freebsd-current mailing list 2008-2009 archives；freebsd-hackers ULE feedback threads (2008)；LWN.net FreeBSD ULE coverage (2008-2009) ［A］

- FreeBSD 7.0/7.1 src/sys/kern/sched_ule.c commit log；freebsd-hackers mailing list ULE contributors (2008)；FreeBSD Committer's Guide (freebsd.org) ［A］

- 7.0/7.1 Release Notes；freebsd-alpha/freebsd-ipfw 邮件；EPFL USENIX ATC 2018 论文；NetBSD/alpha 文档 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1996-2010 年间：482,545 次提交。

## 105.12 不同时期人员的采访录（详见 [采访录.md](采访录.md)）
