---
chapter: 第 224 章
id: CH224
volume: 第11卷-dragonflybsd的历史
---

# 第 224 章 dragonfly3x的hammer2雏形设计

## 要点

- DragonFly 提交高峰期：2014年(98904次)，对应 3.x 时期 HAMMER 2 雏形设计

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4103] 卷“第11卷-dragonflybsd的历史”第 224 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

- [DB:code_repos:dragonfly.duckdb] DragonFly 提交高峰期：2014年(98904次)，对应 3.x 时期 HAMMER 2 雏形设计

## 史观

- 循环而非进步：HAMMER 2 的雏形设计是对 HAMMER 1 的循环性重构，非线性进步

## 辨析

- bsd_commits.duckdb 显示 v3.0.0 至 v3.2.0 间隔约 9 个月，但 v3.0.0 至 v3.0.1 仅 28 天、v3.0.1 至 v3.0.2 仅 31 天——反映 v3.0.x 系列为快速修正版，v3.2.0 为下一个主版本；HAMMER 2 设计讨论与 HAMMER 1 性能改进的具体 commit 须以 commit_files 表 sys/vfs/hammer/ 与
- dragonfly.duckdb 关键词搜索仅基于 message_subject，部分 SMP/LWKT commit 可能以具体函数名为关键词而未提及 ‘SMP’ 或 ‘LWKT’，实际 commit 量须以 commit_files 表 sys/kern/lwkt_* 路径核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；Wildner 2013
- 设计文档与源码可能有滞后——文档可能未及时反映源码最新变化，须对照 commit log 辨析；HAMMER 2 关键算法（如方框树 blockset tree、本地簇缓存）的作者归属须以 commit log 与 kernel@ 邮件列表核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；dragonfly.duckdb 显示 Dillon 2014 年
- 考据过程留痕——【查证来源】dragonfly.duckdb dragonfly-src 仓库 commits 表 MFC/From FreeBSD 关键词按年（2011 = 6、2012 = 34、2013 = 37、2014 = 34、2015 = 18）、活跃 committer 数按年（2011 = 33、2012 = 35、2013 = 33、2014 = 33、2015 = 28）、Dil

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 dragonfly.duckdb