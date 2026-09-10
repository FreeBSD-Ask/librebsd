---
chapter: 第 216 章
id: CH216
volume: 第11卷-dragonflybsd的历史
---

# 第 216 章 dragonflybsd早期演进现状与维护

## 要点

- DragonFly 仓库构成：dports(606813次提交)占主导，src(49379次提交)，dports 提交量远超 src 反映 ports 移植工程规模

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4032] 卷“第11卷-dragonflybsd的历史”第 216 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:dragonfly.duckdb] DragonFly 仓库构成：dports(606813次提交)占主导，src(49379次提交)，dports 提交量远超 src 反映 ports 移植工程规模

## 史观

- 动手者创造历史：DragonFly 的 dports 提交量远超 src，反映默默维护 ports 的动手者才是项目持续运转的基石

## 辨析

- release notes 与 git changelog 对照——bsd_commits.db 显示 v6.4.0 tagger_date = 2022-12-30T22:34:52+01:00 而 target_commit_date = 2022-12-29T03:03:14+01:00，二者相差约 43 小时，反映 tag 创建与 commit 提交的时间差；v6.4.0 tagger =
- 从 commit message 与邮件讨论重构治理实践存在解读偏差风险——commit message 经常省略决策过程（如为何选择消息传递而非细粒度锁的论证），仅记录实现细节；邮件列表发言可能被截取脱离上下文，正式撰写时须以 lists.dragonflybsd.org 原始邮件 ID 与时间戳追溯完整讨论线程；Dillon 关于治理的系统性发言 [考据完成：2026-07-28 该处存疑标注
- 【0 信任原则·SMPng 性能判断的时点性】Dillon 2003 年"too heavily mutexed"的判断须以 2003 年硬件语境评估，不得以 2004-2006 年 SMPng 改善后的事后视角否定 2003 年判断的合理性——dragonfly.duckdb 显示 FreeBSD 5.0（2003-01）至 5.3（2004-11）期间 SMPng 仍处于性能调优期，Dillon

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 dragonfly.duckdb