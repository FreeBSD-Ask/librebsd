---
chapter: 第 92 章
id: CH92
volume: 第05卷-freebsd的工程化奠基
---

# 第 92 章 freebsd4x的jails与黄金时代开端

## 要点

- Kamp 与 Watson 合著的 Jails 论文（SANE 2000，荷兰马斯特里赫特）记载，jails 工作由 servetheweb.com 赞助并捐赠给 FreeBSD 项目，FreeBSD 4.0-RELEASE 是首个包含该代码的发布，后续工作由 Safeport Network Services 赞助（Kamp & Watson, 2000）——为 4.0 引入 jails 提供了赞助与法律归属条件（jails 代码以捐赠形式进入 FreeBSD，4.0-RELEASE 起随基系统分发）〔2026-09-12 整改：句尾截断按 Kamp & Watson 2000 论文语境收束——批次 C105 问题 1〕
- kqueue 史料保存较好，Lemon 的 BSDCon 论文与手册页完整，但设计决策的演化散落在 commit log 中
- KAME 项目史料保存较好，但 KAME 与 FreeBSD 集成的具体决策过程散落在邮件列表中
- OpenSSH 集成史料保存较好，但 FreeBSD 与 OpenBSD 之间的代码同步机制缺乏系统文档
- Yahoo!/Hotmail 部署史料部分来自企业内部报告，部分未公开，需对照公开演讲与媒体报导

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_87] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_96] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_104] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_105] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_124] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_138] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_245] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 2
- [DB:references_fulltext:chapter_matches:chmatch_246] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 2
- [DB:references_fulltext:chapter_matches:chmatch_247] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 2
- [DB:references_fulltext:chapter_matches:chmatch_248] 卷“第05卷-freebsd的工程化奠基”第 92 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 2

## 史观

总纲第 4 条——分离聚合是永恒规律：jails 自 chroot 分离演进为独立内核隔离机制，kqueue/KAME/OpenSSH 自各自上游分离后与 FreeBSD 集成聚合——4.x 时期的黄金时代是技术组件分离—聚合循环的密集期；总纲第 10 条——动手者创造历史：jails 由 Kamp 与 Watson 亲手设计实现（SANE 2000 论文当事人），kqueue 由 Lemon 以论文与手册页留痕——组件集成由动手者的论文、commit 与邮件讨论逐项完成；总纲第 5 条——没有必然性，只有偶然性：jails 的赞助来源（servetheweb.com → Safeport）与集成节奏均系偶然条件，非“4.0 必然纳入 jails”的进步叙事；总纲第 9 条——经验优先：设计决策的演化散落在 commit log 与邮件列表中，须以一手工程经验记录重建而非事后概括。（2026-09-12 整改：史观字段按批次 C105 回填，映射依 25 条权威表；细节见子节文件）

## 辨析

- servetheweb.com 与 Safeport Network Services 的商业模式与 jails 设计的因果方向（是隔离需求催生赞助还是赞助催生需求）须对照 phk 个人陈述核验
- Dillon 的自述与 Core Team 的记述存在差异，需交叉验证
- 考据过程留痕——【查证来源】本节史料综合 37.9.1-37.9.3 节（旧编号体系，对应现行第 92 章 92.x 节，具体映射待核——2026-09-12 整改注）一手与二手史料：Dillon 2003-07-16 DragonFly BSD 公告（freebsd-current 邮件列表，<https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>，经 WebFetch 一手核验）、DragonFly 2003-07-16 fork 公告等一手与二手史料〔2026-09-12 整改：句尾截断按所列来源收束——批次 C105 问题 4〕

## 文献

- Kamp & Watson. Jails: Confining the omnipotent root [C]//Proceedings of SANE 2000. Maastricht, 2000 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2000-2003 年间：149,144 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Lemon 论文；commit log；kqueue(2) 手册页 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- KAME 档案；commit log；邮件列表 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- OpenBSD/FreeBSD commit log；邮件列表 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- BSDCon 演讲；媒体报导；企业公开报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Core Team 记录；邮件列表归档 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Foundation 档案；USPTO 数据库；邮件列表 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD/DragonFly commit log；Dillon 个人网站；邮件列表 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1998-1998 年间：18,134 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 综合 37.9.1-37.9.3 节文献（旧编号体系，对应现行第 92 章 92.x 节，映射待核——2026-09-12 整改注）；DragonFly BSD Project. History [EB/OL]. <https://www.dragonflybsd.org/history/>；FreeBSD 5.x/6.x/7.x Release Notes；freebsd.duckdb freebsd-src 仓库 commits 与 tags 表（Dillon 末次 commit、release/5.0.0、release/7.1.0）；dragonfly.duckdb dragonfly-src 仓库 commits 表（首条 commit 984263bcb83ad82313113c6ac840d99124d8f90c）；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 4 条、第 5 条）［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
