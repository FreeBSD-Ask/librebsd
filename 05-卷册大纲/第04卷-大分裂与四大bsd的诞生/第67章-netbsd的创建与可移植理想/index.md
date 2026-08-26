---
chapter: 第 67 章
id: CH67
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 67 章 netbsd的创建与可移植理想

## 要点

- NetBSD 仓库共 1999412 次提交（1992-07-13 至 2026-08-24），490 位贡献者，提交量在四大 BSD 中最高，反映其广谱移植策略的工程代价

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3670] 卷“第04卷-大分裂与四大bsd的诞生”第 67 章，匹配置信度 folder，原因：folder 第66章
- [DB:references_fulltext:chapter_matches:chmatch_3703] 卷“第04卷-大分裂与四大bsd的诞生”第 67 章，匹配置信度 folder，原因：folder 第66章
- [DB:references_fulltext:chapter_matches:chmatch_3961] 卷“第04卷-大分裂与四大bsd的诞生”第 67 章，匹配置信度 folder，原因：folder 第66章
- [DB:references_fulltext:chapter_matches:chmatch_3975] 卷“第04卷-大分裂与四大bsd的诞生”第 67 章，匹配置信度 folder，原因：folder 第66章

- [DB:code_repos:netbsd.duckdb] NetBSD 仓库共 1999412 次提交（1992-07-13 至 2026-08-24），490 位贡献者，提交量在四大 BSD 中最高，反映其广谱移植策略的工程代价

## 史观

- 经验优先：NetBSD 的可移植执念根植于对硬件多样性的经验性尊重，非抽象理念驱动

## 辨析

- MI/MD 架构并非在 0.8 时即完整建立——0.8 仅支持 i386 单平台，多平台支持与完整 MI/MD 分层在 0.9、1.0 及后续版本中逐步完善；4.4BSD-Lite 基础是 1.0 版本（1994.10）才引入的，0.8（1993.4）不基于 4.4BSD-Lite 也不基于 4.3BSD-Reno
- 1.0 正式二进制发布平台确认为 5 个架构（amiga、i386、mac68k、pc532、sparc），hp300 在源码中已有支持但二进制版尚未准备好；“6 个平台”说法包含了未就绪的 hp300；12/14/21 等数字为后续版本或混淆了平台与架构的计数
- 0.8 发布时多平台支持尚未实现，其吸引非 x86 用户是后续版本（0.9/1.0）的效应；用户反响规模需对照 Usenet 帖量核验
- FreeBSD Foundation 与 OpenBSD Foundation 注册的具体时间需对照官方文件核验
- Foundation 与 Core Team 的具体权力边界在不同时期叙事不一，需对照各年度 By-Laws 修订版本核实

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 netbsd.duckdb
