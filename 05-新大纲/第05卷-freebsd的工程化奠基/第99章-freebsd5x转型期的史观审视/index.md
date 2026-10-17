---
chapter: 第 99 章
id: CH99
volume: 第05卷-freebsd的工程化奠基
---

# 第 99 章 freebsd5x转型期的史观审视

## 要点

- FreeBSD 5.x SMPng 架构重构争议呈现四层辩证结构。【批评层】对 FreeBSD 5.x 的批评集中于三个层面：其一，5.0-RELEASE 耗时近 3 年开发（2000.3 启动 5-CURRENT 至 2003.1.16 `release/5.0.0` tagger_date 为 2003-01-16T16:56:23Z），延期源于 SMPng、KSE、GEOM、ULE、MAC
- 2003-2006 同期 Linux 2.6(2003.12, O(1) 调度器成熟、NPTL 1:1 线程模型、抢占式内核、FUSE、ext3 默认、SELinux 集成、cgroups 雏形) 与 Solaris 10(2005.1, ZFS、DTrace、Zones、SMF、Predictive Self-Healing、FMA)；FreeBSD 5.x 在 SMP 转型上落后约 2-3 年
- 技术路线分化辨析：(1) FreeBSD 渐进改造 vs Linux 渐进改造；(2) Solaris 完全重写 vs FreeBSD 部分重写；(3) 路线选择是否影响命运
- 比较形式主义分析：(1) 比较维度是否公平；(2) 比较时间点是否对齐；(3) 比较是否考虑市场份额
- 比较史料疑点：(1) Linux 2.6 与 Solaris 10 数据来源；(2) FreeBSD 5.x 是否真落后；(3) 落后是否真影响市场份额

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_264] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_271] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_272] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_274] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_334] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_338] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_339] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_813] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_869] 卷“第05卷-freebsd的工程化奠基”第 99 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1

## 史观

总纲第 3 条——不存在进步，只有权力再分配：5.x SMPng 转型的争议是架构改造权与发布节奏优先权之间的权力再分配；总纲第 5 条——没有必然性，只有偶然性：5.x 延期与同期 Linux 2.6/Solaris 10 的发布节点均为偶然条件叠加，非“FreeBSD 必然衰落”的叙事起点；总纲第 10 条——动手者创造历史：SMPng/KSE/GEOM/ULE/MAC 五大子系统由具体动手者逐 commit 推进；总纲第 4 条——分离聚合是永恒规律：5.x 将老旧ATA 驱动分离、GEOM/VFS/XEN 新层聚合，是架构大清理的长周期工程；总纲第 9 条——经验优先：5.x 成败以 commit 数据、Release Notes 与用户反馈的经验证据为准。（2026-09-12 整改：史观字段按批次 C101 回填 5 条，映射依 25 条权威表）

## 辨析

- 考据过程留痕——【查证来源】FreeBSD 5.0-RELEASE Announcement 经 **<https://www.freebsd.org/releases/5.0R/announce/>** 一手核验，邮件 Date 为 Sun, 19 Jan 2003 10:03:42 -0700，<scottl@FreeBSD.org>，原文 "Although FreeBSD 5.0 contains many new features and architectural changes, it is not the best choice for production environments at this time."（2026-09-12 整改：引文截断按 FreeBSD 5.0-RELEASE Announcement 官方公告补全——批次 C101 问题 4）
- SCO 是否真持有 UNIX 版权，需查 Novell v. SCO

## 文献

- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 5、6、8 条）；freebsd.duckdb freebsd-src/dragonfly-src 仓库 commits 表；Matthew Dillon（马修·狄龙）. Annoucning DragonFly BSD! [EB/OL]. 2003-07-16. <https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>；FreeBSD 5.0-RELEASE Release Notes；Bouron et al. The Battle of the Schedulers: FreeBSD ULE vs. Linux CFS [C]//USENIX ATC 2018.（2026-09-12 整改：著录尾部［A］残留清除——批次 C101 问题 5）
- FreeBSD 5.0-RELEASE Announcement [EB/OL]. 2003-01-19. **<https://www.freebsd.org/releases/5.0R/announce/>** ；FreeBSD 5.3-RELEASE Announcement [EB/OL]. 2004-11-06. **<https://www.freebsd.org/releases/5.3R/announce/>** ；freebsd.duckdb freebsd-src 仓库 tags 表（`release/5.0.0`、`release/5.3.0`、`release/7.1.0`）；Matthew Dillon. Annoucning DragonFly BSD! [EB/OL]. 2003-07-16. **<https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>** ；Roberson, J. ULE: A Modern Scheduler for FreeBSD [C]//BSDCon 2003；Bouron et al. The Battle of the Schedulers: FreeBSD ULE vs. Linux CFS [C]//USENIX ATC 2018；Phoronix FreeBSD 5.x 基准测试；freebsd-performance/freebsd-hackers 邮件列表 2003-2005 存档 ［A］
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13、19、21 条）；FreeBSD 5.0-RELEASE Announcement [EB/OL]. 2003-01-19. **<https://www.freebsd.org/releases/5.0R/announce/>** ；FreeBSD 5.3-RELEASE Announcement [EB/OL]. 2004-11-06. **<https://www.freebsd.org/releases/5.3R/announce/>** ；freebsd.duckdb freebsd-src 仓库 tags 表；Matthew Dillon. Annoucning DragonFly BSD! [EB/OL]. 2003-07-16. **<https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>** ；DragonFly BSD Project. History [EB/OL]. **<https://www.dragonflybsd.org/history/>** ；DragonFly BSD 2.0 Release Notes [Z]. 2008 ［A］
- 各操作系统 Release Notes［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 操作系统历史研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 市场份额数据［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 市场份额调查［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 基准测试；Distrowatch［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- DragonFly 历史；决议［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 决议；邮件［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］