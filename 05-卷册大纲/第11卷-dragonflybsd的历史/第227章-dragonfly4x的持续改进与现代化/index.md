---
chapter: 第 227 章
id: CH227
volume: 第11卷-dragonflybsd的历史
---

# 第 227 章 DragonFly 4.x 的持续改进与现代化

## 要点

- dragonfly.duckdb dragonfly-src 仓库 tags 表提供 v4.2.0（tagger_date = 2015-06-28T19:15:14-04:00）与 v4.4.0（tagger_date = 2015-12-03T18:58:35-05:00）的 tagger_date、tagger_name、target_commit_hash 字段。v4.2.0 target_commit_hash = `82c070747b09`，v4.4.0 target_commit_hash = `9ee45dd09766`——两 tag 间隔约 5 个月，反映 4.2 → 4.4 的开发周期约 5 个月
- dragonfly.duckdb dragonfly-src 仓库 commits 表提供 v4.6.0 与 v4.8.0 期间 NVMe 与 vkernel 改进的具体 commit。v4.6.0（2016-08-01）至 v4.8.0（2017-03-26）间隔约 8 个月，期间 NVMe 相关 commit 与 vkernel 相关 commit 须以 commit_files 表核验。dragonfly.duckdb 显示 2016-2018 年间 TOP 5 贡献者为 Wildner（<saw@online.de>，1447 条）、Dillon（<dillon@apollo.backplane.com>，1243 条）、zrj（772 条）、Kusumi（556 条）、Vadász（504 条）
- dragonfly.duckdb 不直接记录 commit 权限变动，权限授予与撤销须以 DragonFly 邮件列表（lists.dragonflybsd.org）中 Dillon 或 kernel@ 的公告为准。lists.dragonflybsd.org 完整归档 2003-2026 年间 kernel@、commits@、users@、bugs@ 等邮件列表，其归档连续性优于部分同期邮件列表〔存疑：原稿以“FreeBSD 2012 年迁移丢失事件”作对照，该事件的准确性质与其对邮件列表归档的实际影响未经权威一手来源核实，此处仅作对照线索〕。dragonfly.duckdb contributors 表中 first_commit_date 字段是权限授予时间的间接证据，须与邮件列表公告交叉验证
- dragonfly.duckdb 关键词搜索与 lists.dragonflybsd.org、lists.freebsd.org、LKML 邮件列表归档交叉对照是考据 DragonFly 批评原始发言的主要方法。dragonfly.duckdb 数据显示 DragonFly 2016-2018 年间 commit 量仅为 FreeBSD 同期 11-14%，为批评提供了量化证据；但批评发言的具体内容、时间、作者归属须以邮件列表原文核验，避免简化引用
- dragonfly.duckdb dragonfly-src 仓库 commits 表提供 2014-2018 年间 TOP 10 贡献者的 commit 量化数据：Wildner 2391 条、Dillon 1609 条、Kusumi 1151 条、Sepherosa 1105 条、Tigeot 641 条、Marino 587 条、zrj 575 条、Vadász 574 条、Huete Jimenez 210 条、Pfeiffer 150 条

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4050] 卷“第11卷-dragonflybsd的历史”第 227 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲第 4 条（分离聚合是永恒规律）——DragonFly 4.x 时期 DRM 移植从 FreeBSD DRM 转向 Linux DRM，与 FreeBSD 的代码共享减少、与 Linux 内核的同步增加，是 BSD 阵营内部聚合与分离规律的又一显现
- 总纲第 10 条（动手者创造历史）——本章各项改进由 Tigeot（DRM 移植）、Sepherosa Ziehau（网络栈）、Kusumi（HAMMER2）、Wildner（i386 移除与 release engineering）等长期动手者以数千条 commit 完成，commit 数据库是较零散叙事更可靠的贡献者数字遗产
- 总纲第 5 条（没有必然性，只有偶然性）——vkernel 在 4.x 时期持续改进（75 条相关 commit）却在 v6.0.0（2021 年）之后不再受支持，技术路线的演化非线性，不作“分叉必然发生”的目的论叙事
- 总纲第 19 条（解释学循环是历史认识的根本条件）——本章考据以 dragonfly.duckdb tags/commits/contributors 表与 kernel@ 邮件列表交叉验证，release notes 与 commit log 任一来源均不可单独采信，前理解差异决定史料取舍

## 辨析

- release notes 与 commit log 偶有不一致——dragonfly.duckdb 显示 v4.2.0 与 v4.4.0 间隔约 5 个月，须以 commit log 核验实际开发投入；GPU 与网络栈改进的具体 commit 须以 commit_files 表核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；Dillon 在 v4.2 → v4.4 期间的 commit 量按 5/12 月比例估算约 137 条，精确值须以 author_date BETWEEN ‘2015-06-28’ AND ‘2015-12-03’ 单独统计 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- commit log 可能不完整反映改进全貌——部分改进可能分散在多个 commit 中，须结合邮件讨论辨析；Wildner 邮箱须注意——dragonfly.duckdb 显示其 2016-2018 年使用 <saw@online.de> 而非 <swildner@dragonflybsd.org>（后者 2004-2008 年使用），两邮箱合计 3517 条 commit；NVMe 与 vkernel 改进的具体作者归属须以 commit_files 表核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 邮件记录可能不完整——部分权限决策可能在私下邮件或 IRC 中进行；dragonfly.duckdb 显示 Aaron LI 首 commit = 2017-09-27，但其在 kernel@ 邮件列表的首次发言 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 须单独核验；权限撤销记录在 DragonFly 中罕见——dragonfly.duckdb contributors 表显示贡献者停止贡献是自然淡出而非被撤销权限
- 批评发言可能被断章取义——须结合完整上下文辨析，避免简化引用；bsd_commits.duckdb 关键词搜索可能低估批评相关讨论——部分讨论可能以 ‘community size’/‘project health’ 等术语进行；私人邮件与 IRC 讨论不可考，仅以公开邮件列表为准
- bsd_commits.duckdb 关键词搜索可能低估个人贡献——Tigeot 的 DRM 移植 commit 可能以 ‘i915’/‘radeon’ 等具体驱动名为关键词而未提及 ‘DRM’，须以 commit_files 表 sys/dev/drm/ 目录核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；commit 量与代码行数无简单线性关系——部分 commit 量大的贡献者（如 Wildner）多负责代码集成与维护，部分 commit 量小的贡献者（如 Pfeiffer）多负责关键修复；bsd_commits.duckdb contributors 表须按 author_email 合并邮箱变更（如 Wildner 的两邮箱、Vadász 的 ‘Vadász’ 与 ‘Vadasz’ 拼写差异）

## 文献

- dragonfly.duckdb dragonfly-src 仓库 tags 表（v4.2.0/v4.4.0 完整字段）；dragonfly.duckdb dragonfly-src 仓库 commits 表（Dillon 2014-2016 年按年统计）；DragonFly 4.2/4.4 release notes [EB/OL]. dragonflybsd.org/release/；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2015-2016 年间：90,164 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- /DB_REF -->

- dragonfly.duckdb dragonfly-src 仓库 commits 表（v4.6.0/v4.8.0 期间 commit 与 TOP 10 贡献者）；kernel@ 邮件列表档案；NVMe/虚拟化性能 benchmark 报告 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2016-2017 年间：88,853 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- /DB_REF -->

- lists.dragonflybsd.org 邮件列表归档；dragonfly.duckdb dragonfly-src 仓库 contributors 表（first_commit_date 序列）；marc.info DragonFly 备份 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2014-2017 年间：227,047 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- /DB_REF -->

- dragonfly.duckdb commits 表（两仓库对照）；lists.dragonflybsd.org 邮件列表归档；lists.freebsd.org 邮件列表归档；LKML 档案；技术媒体报道 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- /DB_REF -->

- dragonfly.duckdb dragonfly-src 仓库 commits 表与 contributors 表（2014-2017 年 TOP 10）；kernel@ 邮件列表档案；贡献者个人简历［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- /DB_REF -->
