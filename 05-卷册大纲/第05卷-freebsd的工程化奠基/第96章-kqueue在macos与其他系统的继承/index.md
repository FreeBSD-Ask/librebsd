---
chapter: 第 96 章
id: CH96
volume: 第05卷-freebsd的工程化奠基
---

# 第 96 章 kqueue 在 macOS 与其他系统的继承

> 编号缺口登记（2026-09-12 整改补，批次 C067 旗标处置）：96.1-96.3 缺失系拆分沿革遗留——本子章由原第 39 章拆分而来，96.1-96.3 内容归属第 95 章 95.1-95.3（SUMMARY 第 833-836 行），非误删。

## 本章节索引

1. [96.4 kqueue 在 macOS/iOS 的继承——Apple 采纳](96.4-kqueue-在-macOS-iOS-的继承-Apple-采纳.md)
2. [96.5 外部批评与反对者 1——Ariadne Conill 2021-06-05 博客](96.5-外部批评与反对者-1-Ariadne-Conill-2021-6-5-博客-前.md)
3. [96.6 kqueue 开发者 Jonathan Lemon 的工程传记与设计演进](96.6-kqueue开发者jonathanlemon的工程传记与设计演进.md)
4. [96.7 对 kqueue 的批评——epoll/io_uring 竞争者与跨平台张力](96.7-对-kqueue-的批评-epoll-io_uring-竞争者与跨平台张力-对.md)
5. [96.8 重要贡献者与边缘者——kqueue 早期采用者与文档贡献者](96.8-重要贡献者与边缘者-kqueue-早期采用者与文档贡献者-kqueue.md)
6. [96.9 与同时期操作系统的比较——2000 年同期 Linux select/poll 等](96.9-与同时期操作系统的比较-2000-年同期-Linux-select-poll-W.md)
7. [96.10 项目统摄史观审视——偶然性、形式主义与权力-知识的共谋](96.10-项目统摄史观审视-偶然性-形式主义与权力-知识的共谋.md)
8. [采访录](采访录.md)

## 要点

- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），5,671 位贡献者（contributors 表行数）
- Apple 采纳史料的争议：（1）Apple 是在哪个 Mac OS X 版本首次集成 kqueue（有 10.3 与 10.4 两种说法）；（2）Apple 是否因 kqueue 早于 epoll 而选择；（3）iOS 1.0 是否已包含 kqueue
- 外部批评史料的疑点：（1）Conill 博客的技术细节是否准确（kqueue 是否真的 “每新增资源需改内核”）；（2）Hacker News 讨论的代表性是否被夸大；（3）FreeBSD 社区对批评的回应是否被记录
- kqueue 的引入与设计渊源（2000 年 FreeBSD 4.1、Jonathan Lemon 设计、VMS `QIO`/`AST` 模型灵感）详见第 95 章 95.1 节，本章只谈后续继承（2026-09-12 整改：原条与第 95 章叙述重复，改交叉引用——批次 C067 问题 9）。事件通知应为内核原语而非用户态轮询的哲学在后续 epoll（2002）中反复验证。
- 批评史料的疑点（与上条「外部批评史料的疑点」合并，2026-09-12 整改——批次 C067 问题 7）：（1）Conill 2021 批评是否预示 io_uring 时代的 kqueue 衰落；（2）FreeBSD 社区对 io_uring 的官方态度；（3）kqueue 在 2020 年代是否仍是合理选择

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3772] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3774] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3780] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3784] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章
- [DB:references_fulltext:chapter_matches:chmatch_3798] 卷“第05卷-freebsd的工程化奠基”第 96 章，匹配置信度 folder，原因：folder 第94章

（2026-09-12 整改注：上列 5 条章级匹配均指向第 94 章（"folder 第94章"），与本章 96 不符且置信度字段作 "folder" 非数值——系库侧 chapter_matches 的 folder 映射错锚，入库侧复核列 DEFERRED；本组行仅作检索登记不作证据采信——批次 C067 问题 13）

## 史观

总纲第 4 条——分离聚合是永恒规律：kqueue 自 FreeBSD 分离后被 Apple（macOS/iOS）、PostgreSQL 等异质系统聚合采用，事件通知机制的传播史即分合循环（与 96.4/96.8 映射一致）；总纲第 5 条——没有必然性，只有偶然性：Apple 采纳 kqueue 的版本断代（10.3/10.4 两说）与个人驱动采用（Munro）均系偶然条件（与 96.4/96.10 映射一致）；总纲第 10 条——动手者创造历史：Lemon 的设计演进与早期采用者、文档贡献者的劳动构成 kqueue 生态的实际主体（与 96.6/96.8 映射一致）；总纲第 3 条——不存在进步，只有权力再分配：Conill 批评与 io_uring 竞争折射异步 I/O 话语权的再分配，kqueue「衰落」叙事本身是权力位移的呈现（与 96.5/96.7 映射一致）；总纲第 8 条——本体论上各方平等：kqueue/epoll/io_uring 三种事件通知机制作为不同工程取舍在本体论上地位相等（与 96.7/96.9 映射一致）；总纲第 22 条——知识注定过时：2000 年的设计在 2020 年代的硬件与负载下须重新评估（与 96.7 映射一致）。（2026-09-12 整改：史观字段按批次 C067 自 96.4-96.10 各节归纳回填，映射依 25 条权威表）

## 辨析

- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- iOS 1.0 内核是否包含 kqueue 二进制证据来自越狱设备，需谨慎采信
- kqueue 的 filter 是否真的需要改内核，需查 FreeBSD 内核扩展机制
- FreeBSD 社区是否计划引入 io_uring，需查 commit log 与 roadmap
- Munro 同时为 PostgreSQL 与 FreeBSD 开发者（`tmunro@postgresql.org` 与 `tmunro@freebsd.org`），该采用属个人驱动还是社区共识须对照 PostgreSQL 13 release notes 核验；其报告中“大幅降低系统时间”为特定负载（hw.ncpu=88）下的观测，不得泛化为普遍结论

## 文献

- iPhone Dev Team 越狱档案；Apple Developer Release Notes［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1996-2010 年间：482,545 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD 内核文档；Conill 博客 ［C］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 2021 年间：60,852 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Lemon J. 2001（kqueue 论文）；**kqueue(2)** 手册页［A］（2026-09-12 整改：手册页引用改原始体例、半角分号改中文——批次 C067 问题 10）

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1996-2010 年间：482,545 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Foundation roadmap；freebsd-hackers 邮件 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1996-2010 年间：482,545 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Munro. PostgreSQL on FreeBSD: Some news, observations and speculation [C]//BSDCan 2020. Ottawa, 2020 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1996-2010 年间：482,545 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- BSDCon 2000 proceedings；DANCES 2002 proceedings［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 2000 年间：29,754 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
