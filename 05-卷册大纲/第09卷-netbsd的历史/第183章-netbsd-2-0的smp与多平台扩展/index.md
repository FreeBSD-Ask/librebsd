---
chapter: 第 183 章
id: CH183
volume: 第09卷-netbsd的历史
---

# 第 183 章 netbsd-2-0的smp与多平台扩展

## 要点

- NetBSD 2.0 分支（约 2003 年底切出）引入基于 FreeBSD SMPng 移植的细粒度锁机制，逐步替换 4.x 时代的 Giant Lock；2.0 正式发布于 2004.12，标志 NetBSD 进入真正的 SMP 时代
- NetBSD 2.x/3.x 时期 SMP 性能基准在 2-8 核机器上较 FreeBSD 5.x/6.x 落后，但在嵌入式 ARM/MIPS 多核场景占优；硬件支持广度（ports 数量）是同期 BSD 中最广；NetBSD 的跨平台能力不仅体现在 src 仓库的 ports 数量上，亦体现在 pkgsrc 跨平台包管理系统的规模上——pkgsrc 作为 NetBSD 的跨平台包管理系统，可独立
- FreeBSD 5.x（2003-2005）推进 SMPng 与 Giant Lock 细化，5.2（2004）实验性引入 ULE 调度器；NetBSD 2.x/3.x 移植 SMPng 但调度器仍以 4BSD 为基础，反映两项目不同的工程节奏
- Linux 2.6（2003.12）引入 O(1) 调度器与抢占式内核，SMP 扩展性快速领先；Solaris 10（2005.1）引入 ZFS 与 DTrace，企业级 SMP 成熟度最高；NetBSD 2.x/3.x 在 SMP 上保守，但在可移植性上独树一帜

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3998] 卷“第09卷-netbsd的历史”第 183 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4009] 卷“第09卷-netbsd的历史”第 183 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_3989] 卷""第 183 章，匹配置信度 0.9，原因：

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 经 netbsd.db 验证，NetBSD 2.0 发布日期为 2004.12.09（commit message 明确记载 "NetBSD 2.0 was released on December 09, 2004"）；SMPng 移植的具体完成度需考据，2.0 是否已完全移除 Giant Lock 需对照源码核验。L1.1.1 查询的 commit 量数据存在 GitHub 镜像滞后风险——n
- 基准测试的硬件配置差异需对照原始测试脚本核验，不得直接采信结论。L1.1.1 查询的 commit 量数据存在 GitHub 镜像滞后风险——netbsd-src 为 GitHub 镜像（主仓为 Mercurial **hg.NetBSD.org**），2004-2008 年 commit 量可能不完整；commit 量持续下降与 “性能落后” 叙事方向一致，但 commit 量下降不等于性能下降
- SMPng 是否为两项目共享代码需对照 CVS 历史核验，部分叙事夸大了共享程度
- 三项目同期 SMP 性能比较需在同一硬件上测试，跨硬件比较易误导

## 文献

- NetBSD 2.0 Release Notes [EB/OL]. (2004-12-09). <https://www.netbsd.org/releases/formal-2.0.html>（原始链接失效，互联网档案馆无存档）；FreeBSD SMPng 设计文档 [EB/OL]. <https://docs.freebsd.org/en/books/arch-handbook/smp/>；Jason Thorpe、Frank van der Linden tech-smp 邮件列表帖 [EB/OL]. <https://mail-index.netbsd.org/tech-smp/>；bsd_commits.db 数据分析·宏观趋势统计.md §L1.1.1（netbsd-src 2003-2004 年度 commit 量）、§L2.3.1.smp（netbsd-src SMP 相关 commit 2005）、§SubTask 2.1（统计结论 C-04：netbsd-src 总 commit 数 773,683） ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2003-2004 年间：221,740 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- Phoronix NetBSD/FreeBSD 性能基准测试 [EB/OL]. <https://www.phoronix.com/>；NetBSD/doc/PLATFORMS 文件 [EB/OL]. <https://github.com/NetBSD/src/blob/trunk/doc/PLATFORMS>（原始链接失效，互联网档案馆无存档）；tech-perform 邮件列表 [EB/OL]. <https://mail-index.netbsd.org/tech-perform/>；bsd_commits.db 数据分析·宏观趋势统计.md §L1.1.1（netbsd-src 2004-2008 年度 commit 量）、§L2.3.1.smp（netbsd-src SMP 相关 commit 2005-2008）；外部基准-StackOverflow-PackageEcosystem.md 第 3.2 节（统计结论 E-15：netbsd-pkgsrc 总 commit 数 1,222,307） ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- FreeBSD 5.x Release Notes [EB/OL]. <https://www.freebsd.org/releases/>；NetBSD 2.x/3.x Release Notes [EB/OL]. <https://www.netbsd.org/releases/formal.html>；freebsd-arch 邮件列表存档 [EB/OL]. <https://lists.freebsd.org/archives/freebsd-arch/> ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Linux 2.6 Release Notes [EB/OL]. (2003-12-17). <https://kernelnewbies.org/LinuxVersions>；Solaris 10 Release Notes [EB/OL]. (2005-01-31). <https://www.oracle.com/solaris/solaris10/>；Molnar I. O(1) Scheduler [EB/OL]. <https://www.kernel.org/doc/Documentation/scheduler/sched-design-CFS.txt> ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
