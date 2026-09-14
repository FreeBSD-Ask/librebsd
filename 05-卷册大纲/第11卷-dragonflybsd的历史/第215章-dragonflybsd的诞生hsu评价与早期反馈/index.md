---
chapter: 第 215 章
id: CH215
volume: 第11卷-dragonflybsd的历史
---

# 第 215 章 dragonflybsd的诞生hsu评价与早期反馈

## 要点

- Hsu 的关键发言主要存于 dragonfly.kernel 邮件列表（lists.dragonflybsd.org 完整归档，2003-2007 年），部分早期发言在 freebsd-hackers（2002-2003 年）。Hsu 无公开个人 GitHub 主页，其发言须以邮件列表归档为准
- Core Team 撤权决议的原文存于 freebsd-hackers 邮件列表 2003 年归档，但完整投票记录未在 freebsd.org/administration/ 公开。Dillon 的回应邮件在 freebsd-current 与 freebsd-hackers 均有存档。dragonfly.duckdb 不记录邮件内容，但 commit message 中 Dillon 的表述可作治理
- HAMMER 的设计文档主要存于 DragonFly 官方网站（dragonflybsd.org/docs/hammer/）与源码树 sys/vfs/hammer/ 目录下的 README 文件。dragonfly.duckdb 显示 sys/vfs/hammer/ 目录首引 commit 为 `8750964d1997`（2007-10-10T19:37:25Z，Dillon），sys/vfs/ha
- DragonFly 的 LICENSE/COPYRIGHT 文件位于源码根目录，内容与 FreeBSD 的 COPYRIGHT 文件基本一致，仅版权持有者信息不同。dragonfly.duckdb 显示 DragonFly 首 commit `984263bcb83a`（2003-06-17）即包含 COPYRIGHT 文件的 Initial import


- 比萨饼隐喻存在多个版本，涉及 “10 个” 或 “3 个” 开发者、不同食物（比萨饼/蛋糕）、不同结局（“开发者死了”/“开发者打起来”/“11 个新变种”/“12 个新变种”）。版本变体反映社区传说的口头传统特征。已知主要版本变体对照如下：

| 变体维度 | 版本 A | 版本 B | 版本 C |
| --- | --- | --- | --- |
| 开发者数量 | 10 个 | 3 个 |  |



## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4031] 卷“第11卷-dragonflybsd的历史”第 215 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 部分引述的 Hsu 发言缺乏原始邮件 ID，正式撰写时须以 lists.dragonflybsd.org 邮件列表时间戳与 Message-ID 追溯完整讨论线程
- 决议的完整文本是否已公开——freebsd.org/administration/ 公开 Core Team 决议摘要但未公开完整投票记录，Dillon 在 dragonfly.kernel 邮件列表称程序不透明；正式撰写时须以 freebsd-hackers 邮件列表原始公告与 Core Team 公开声明交叉核对 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；lists.freebsd.org 邮件列表归档 [EB/OL]；marc.info 归档 [EB/OL]. marc.info/?l = freebsd-hackers ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- freebsd-hackers 2003 年归档 [EB/OL]；FreeBSD Core Team. 公开声明 [EB/OL]. freebsd.org/administration/；dragonfly.duckdb dragonfly-src 仓库 commits 表（Dillon commit message） ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- dragonfly.duckdb dragonfly-src 仓库 commit_files 表（sys/vfs/hammer/ 与 sys/vfs/hammer2/ 首引 commit）；DragonFly HAMMER 源码 [EB/OL]. github.com/DragonFlyBSD/DragonFlyBSD/tree/master/sys/vfs/hammer；Dillon M. HAMMER 设计文档 [EB/OL]. dragonflybsd.org/docs/hammer/ ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly BSD. COPYRIGHT 原文 [EB/OL]. github.com/DragonFlyBSD/DragonFlyBSD/blob/master/COPYRIGHT；FreeBSD. COPYRIGHT 原文 [EB/OL]. github.com/freebsd/freebsd-src/blob/main/COPYRIGHT；dragonfly.duckdb dragonfly-src 仓库 commit_files 表（COPYRIGHT 文件首引与修订历史） ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Usenet comp.unix.bsd.* 归档 [EB/OL]. groups.google.com/forum/#! comp.unix.bsd；DragonFly BSD 邮件列表存档 [EB/OL]. lists.dragonflybsd.org；社区口述史记录（散见各 BSD 项目 wiki 与博客） ［A］FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>### 史观映射> 第 102 章承载项目统摄史观中 “技术选择即政治选择” 与 “分离与聚合” 在 DragonFly BSD 诞生中的运作——Dillon 从 FreeBSD 5.x 分叉的直接原因是 SMPng 细粒度锁路线与 LWKT 消息传递路线的哲学分歧，这一分歧是 “技术选择即政治选择” 的典型：选择锁还是消息传递不仅是技术问题，更是项目治理哲学的政治化表达；fork 本身是 “分离” 的行为，但分离后的 “聚合”（LWKT、HAMMER、vkernels 等创新）才是 DragonFly BSD 的创造性贡献；比萨饼隐喻作为社区传说则承载 “社区文化即技术资产”——传说虽非史实，但构成了 DragonFly BSD 社区身份认同的文化资产；Dillon 的单一决策核心模式与 FreeBSD Core Team 的集体治理形成对照，“组织结构塑造技术路径”——不同的治理结构直接塑造了不同的技术路线选择---

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015；dragonfly.duckdb commits 表（BSD 家族 fork 首 commit 时间序列与 2003-2007 年代码流动）；衍生项目与跨项目对比分析.md §L7.1.1（数据缺口标注） ［B］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2004 年间：4,373 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 contributors 表（Dillon 合并 commit 10666 条，2003-06-17 至 2026-06-10）；统计分析报告：推断性统计.md Task 10 Bootstrap 重抽样 [R/OL]. 2026-07-27（dragonfly-src Gini 0.8972, 95% CI [0.8517, 0.9187]）；Dillon M. DragonFly BSD fork announcement [EB/OL]. <https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>, 2003-07；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/>, last edited 2019-01-17 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- dangan-20260908 消解回写 -->
- Phoronix.. DragonFly BSD HAMMER Performance Benchmarks [EB/OL]. 2008-2015[EB/OL]. 2008. ［DKC-0099→fulltext:5466］
<!-- /dangan-20260908 -->
