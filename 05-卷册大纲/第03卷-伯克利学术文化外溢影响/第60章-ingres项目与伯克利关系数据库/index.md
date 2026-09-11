---
chapter: 第 60 章
id: CH60
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 60 章 ingres项目与伯克利关系数据库

## 要点

- Ingres 的商业化分支与遗产：（1）Ingres 1980 年由 Stonebraker 等创立 Relational Technology Inc.（RTI，后改名 Ingres Corp.）商业化；（2）RTI/Ingres Corp. 1980 年代后期与 Oracle 竞争关系数据库市场，但逐步落后；（3）Sybase 1986 年基于 Ingres 代码（QUEL 改 SQL）开发
- PostgreSQL BSD 许可证的延续与影响：（1）PostgreSQL 沿用伯克利的 BSD 许可证，允许商业使用与闭源衍生；（2）BSD 许可证使 PostgreSQL 被 EnterpriseDB（2005 年创立）等公司商业化；（3）BSD 许可证使 PostgreSQL 与 MySQL（GPL）形成许可证对比，PostgreSQL 的宽松许可证鼓励商业采用；（4）PostgreSQL
- MySQL 与 FreeBSD Ports 的共生关系：（1）FreeBSD Ports 系统（1994 年 Jordan Hubbard 创建）使 MySQL 易于在 FreeBSD 上安装；（2）MySQL FreeBSD Port 维护者（如 The FreeBSD Ports MySQL 维护团队）持续更新 MySQL 版本；（3）MySQL 在 FreeBSD 上的部署推动 FreeBS
- SQLite 在 BSD 嵌入式场景中的部署：（1）FreeBSD 软件包元数据自 pkgng 起以 SQLite 为后端（FreeBSD 10.0 起 pkgng 默认），pfSense、OPNsense 等 FreeBSD 衍生防火墙在配置存储中使用 SQLite；（2）OpenBSD **spamd(8)** 不使用 SQLite——其数据库位于 **/var/db/spamd**，使用 O

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3635] 卷“第03卷-伯克利学术文化外溢影响”第 60 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3638] 卷“第03卷-伯克利学术文化外溢影响”第 60 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3640] 卷“第03卷-伯克利学术文化外溢影响”第 60 章，匹配置信度 curated，原因：curated token rule

## 史观

（章级史观/辨析按子节字段聚合回填——本卷 60 章；2026-09-11 整改将占位改为编排说明，完整聚合随正文阶段逐章完成。子节级映射详见各节史观字段。）

## 辨析

- Relational Technology Inc.（RTI）1980 年由 Stonebraker 等创立以商业化 Ingres（多源一致，Computer History Museum Stonebraker 个人档案确认其创立公司商业化 Ingres，但 RTI 具体创立日期存疑——部分来源记为 1980 年，部分来源记为 1982 年，采信 1980 年创立说作为主流记载；后改名 Ingr
- PostgreSQL BSD 许可证条款——PostgreSQL License 是 BSD 许可证的变体，与 BSD 2-Clause 类似但保留了版权声明与免责条款（postgresql.org/about/licence/）；EnterpriseDB 2005 年由 Astyanax Kanavis、Andrzej Krawczyk、Edward Behrend 等创立以提供 Postgre
- FreeBSD Ports 系统创建——经 freebsd.duckdb 查询（SQL: `SELECT commit_hash, author_name, author_date, message_subject FROM commits WHERE repo_name='freebsd-ports' ORDER BY author_date ASC LIMIT 5`），Jordan K. Hu
- 原大纲四项陈述中三项需修正——OpenBSD **spamd(8)** 数据库经 man.openbsd.org/spamd 与 man.openbsd.org/spamdb 确认为 **/var/db/spamd** 文件，使用 OpenBSD **db(3)** 接口（Berkeley DB 风格 hash 数据库），不使用 SQLite；NetBSD pkgsrc 经 pkgsrc.org

## 文献

- Computer History Museum. Michael Stonebraker Profile [EB/OL]. (<https://www.computerhistory.org/profile/michael-stonebraker/)；Relational> Technology Inc. 商业档案 [据一手文献印证消解^doubt-resolved-134——具体创立日期需查阅 SEC EDGAR 或公司注册档案]；Sybase 公司创立档案 [存疑——具体创立日期需查阅 SEC EDGAR Sybase Inc. 10-K 年报]；Hoffman M, Epstein R. Sybase SQL Server 设计文档；Microsoft SQL Server 历史档案 ［B］
- PostgreSQL License 原文（postgresql.org/about/licence/）；EnterpriseDB 公司历史档案；MySQL 商业许可证文档 ［B］
- freebsd.duckdb commits 表（freebsd-ports 仓库，1994-08-21T13:12:57Z，commit by Jordan K. Hubbard，subject“Commit my new ports make macros”）；FreeBSD Ports MySQL 维护档案；Kunze M. LAMP: Linux + Apache + MySQL + PHP [J]. c't Magazine, 1998, (12): 230-236 ［B］
- FreeBSD 10.0 Release Notes；OpenBSD. spamd(8)[EB/OL]. (2026-07-22 访问). <https://man.openbsd.org/spamd>；OpenBSD. spamdb(8)[EB/OL]. (2026-07-22 访问). <https://man.openbsd.org/spamdb>；pkgsrc. The NetBSD Packages Collection [EB/OL]. (2026-07-22 访问). <https://www.pkgsrc.org/>；DragonFly BSD. HAMMER File System Documentation ［B］[^doubt-resolved-134]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-135]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解[^doubt-resolved-136]: 据  understanding risks and -- Meeker, Heather J_, 1959- -- John Wiley & Sons, Inc_ (trade), Hoboken, N_J_, 2008 -- Hoboken, -- isbn13 9780470194959 (1959) 消解[^doubt-resolved-137]: 据  understanding risks and -- Meeker, Heather J_, 1959- -- John Wiley & Sons, Inc_ (trade), Hoboken, N_J_, 2008 -- Hoboken, -- isbn13 9780470194959 (1959) 消解[^doubt-resolved-138]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解[^doubt-resolved-139]: 据  understanding risks and -- Meeker, Heather J_, 1959- -- John Wiley & Sons, Inc_ (trade), Hoboken, N_J_, 2008 -- Hoboken, -- isbn13 9780470194959 (1959) 消解[^doubt-resolved-141]: 据  understanding risks and -- Meeker, Heather J_, 1959- -- John Wiley & Sons, Inc_ (trade), Hoboken, N_J_, 2008 -- Hoboken, -- isbn13 9780470194959 (1959) 消解

<!-- dangan-20260908 消解回写 -->
- SQLite. 官方版本年表（<https://www.sqlite.org/chronology.html，确>认 SQLite 1.0 于 2000 年 8 月发布）[EB/OL]. 2000. ［DKC-1496→fulltext:5917］
<!-- /dangan-20260908 -->