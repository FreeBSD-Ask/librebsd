---
chapter: 第 216 章
id: CH216
volume: 第11卷-dragonflybsd的历史
---

# 第 216 章 dragonflybsd早期演进现状与维护

## 要点

- DragonFly 仓库构成：dports（606,813 次提交）占主导，src（49,379 次提交），dports 提交量远超 src 反映 ports 移植工程规模

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4032] 卷“第11卷-dragonflybsd的历史”第 216 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:dragonfly.duckdb] DragonFly 仓库构成：dports（606,813 次提交）占主导，src（49,379 次提交），dports 提交量远超 src 反映 ports 移植工程规模

## 史观

- 动手者创造历史：DragonFly 的 dports 提交量远超 src，反映默默维护 ports 的动手者才是项目持续运转的基石

## 辨析

- release notes 与 git changelog 对照——**dragonfly.duckdb** tags 表显示 v6.4.0 tagger = Antonio Huete Jimenez（tuxillo@quantumachine.net），tagger_date = 2022-12-30T17:41:38+01:00，target_commit af5fb9a9e56f90cf51e48514d1874be61e9364e6 的 target_commit_date = 2022-12-21T21:35:22+01:00，tag 创建晚于目标 commit 约 9 天，反映发布 tag 在收尾 commit 后统一打点的时序；官方 cgit（**gitweb.dragonflybsd.org/dragonfly.git**）tag 页经联网一手核验一致 ［存疑脚注：本行原引 bsd_commits.duckdb 之 tagger_date 2022-12-30T22:34:52+01:00 与 target_commit_date 2022-12-29T03:03:14+01:00（相差约 43 小时），该库已于 2026-07-28 拆分并入 dragonfly.duckdb、现不在库内，且原数值与官方 cgit 及 dragonfly.duckdb tags 表不符，2026-09-13 联网核验后按一手来源改写］
- 从 commit message 与邮件讨论重构治理实践存在解读偏差风险——commit message 经常省略决策过程（如为何选择消息传递而非细粒度锁的论证），仅记录实现细节；邮件列表发言可能被截取脱离上下文，正式撰写时须以 lists.dragonflybsd.org 原始邮件 ID 与时间戳追溯完整讨论线程；Dillon 关于治理的系统性发言散见于多年线程，单条引用易以偏概全，须汇集同一议题的完整发言序列并标注时间线再作整体判断 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 参考文献全文数据库（4,077 篇全文，27,138 条时间线事件）—— 对应 dragonfly.duckdb