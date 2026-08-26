---
chapter: 第 96 章
id: CH96
volume: 第05卷-freebsd的工程化奠基
---

# 第 96 章 kqueue在macos与其他系统的继承

## 要点

- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），13,875 位贡献者
- Apple 采纳史料的争议：(1) Apple 是在哪个 Mac OS X 版本首次集成 kqueue(有 10.3 与 10.4 两种说法)；(2) Apple 是否因 kqueue 早于 epoll 而选择；(3) iOS 1.0 是否已包含 kqueue
- 外部批评史料的疑点：(1) Conill 博客的技术细节是否准确 (kqueue 是否真的 “每新增资源需改内核”)；(2) Hacker News 讨论的代表性是否被夸大；(3) FreeBSD 社区对批评的回应是否被记录
- 2000 年在 FreeBSD 4.1 中引入 kqueue——灵感来自 VMS 的 $QIO/AST 模型。‘事件通知应为内核原语而非用户态轮询’的哲学在后续 epoll（2002）中反复验证。
- 批评史料的疑点：(1) Conill 2021 批评是否预示 io_uring 时代的 kqueue 衰落；(2) FreeBSD 社区对 io_uring 的官方态度；(3) kqueue 在 2020 年代是否仍是合理选择

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3772] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3774] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3780] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3784] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3798] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- iOS 1.0 内核是否包含 kqueue 二进制证据来自越狱设备，需谨慎采信
- kqueue 的 filter 是否真的需要改内核，需查 FreeBSD 内核扩展机制
- FreeBSD 社区是否计划引入 io_uring，需查 commit log 与 roadmap
- Munro 同时为 PostgreSQL 与 FreeBSD 开发者（tmunro@postgresql.org 与 tmunro@freebsd.org），该采用属个人驱动还是社区共识须对照 PostgreSQL 13 release notes 核验；其报告中“大幅降低系统时间”为特定负载（hw.ncpu=88）下的观测，不得泛化为普遍结论

## 文献

- iPhone Dev Team 越狱档案；Apple Developer Release Notes[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD 内核文档；Conill 博客 ［C］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2021-2021 年间：60,852 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Lemon 2001; kqueue 手册页 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Foundation roadmap；freebsd-hackers 邮件 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Munro. PostgreSQL on FreeBSD: Some news, observations and speculation [C]//BSDCan 2020. Ottawa, 2020 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- BSDCon 2000 proceedings；DANCES 2002 proceedings[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2000-2000 年间：29,754 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
