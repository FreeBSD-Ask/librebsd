---
chapter: 第 98 章
id: CH98
volume: 第05卷-freebsd的工程化奠基
---

# 第 98 章 freebsd50的开发挑战与工程困境

## 要点

- FreeBSD 5.0 开发时间线：2000.3 启动 5-CURRENT 分支，2002.4 首个 5.0-DP1 开发者预览，2002.10 5.0-DP2，2003.1.16 5.0-RELEASE 正式发布（release/5.0.0 tagger_date = 2003-01-16T16:56:23Z），从 4.0(2000.3.20) 到 5.0 历时近 3 年
- 3 年延期工程原因：(1) SMPng 细粒度锁改造规模超预期；(2) KSE M: N 线程模型反复重写；(3) GEOM 框架从零设计；(4) ULE 调度器从零设计；(5) MAC 框架引入
- 开发挑战辨析：(1) 多项重大改造并行导致相互依赖；(2) Giant Lock 拆分需触及所有子系统；(3) 性能倒退使测试困难；(4) 社区信心动摇
- 工程挑战史料疑点：(1) 延期是否曾被内部讨论缩短；(2) 是否曾考虑放弃部分改造；(3) Core Team 对延期的公开表态
- SMPng(SMP Next Generation) 由 John Baldwin（约翰·鲍德温） 等主导，目标是用细粒度锁替代 Giant Lock，支持多核 CPU 并行执行内核代码；架构包括 **mutex(2)**、**sx(9)**、**condvar(9)**、**witness(4)** 调试框架

## 史观

- 总纲第 17 条——证明世界先于解释和改造世界，3 年延期源于 SMPng 工程挑战而非计划
  - 辨析：经 bsd_commits.duckdb tags 表验证，5.0-RELEASE 的 tagger_date 为 2003-01-16（非旧叙事 2003.1.19，误差 3 天，可能为公告日期与 tag 日期差异），5.0 开发起始日期存在 2000.3 与 2000.1 两种说法，需查 SVN；0 信任原则适用说明：L1.1.1 年度 commit 量基于 author_date 聚合，FreeBSD SVN-to-Git 2020 迁移可能引入日期偏差但 author_date 应保持一致（2026-09-12 回源补全，据同章 98.1 子节辨析段）
- 总纲第 22 条——知识注定过时，4BSD 调度器是 1980s 设计的债务
  - 辨析：Roberson 批评是否公平，需独立验证 4BSD 调度器性能
  - 文献：Roberson BSDCon 2003 论文 ［B］

## 98.4 ULE 的双队列设计（2026-09-11 整改按磁盘实况 98.4 归位，三次重复合并为一节）

- 要点：ULE 调度器采用三个 per-CPU 队列 (current/next/idle) 设计，目标 O(1) 复杂度、CPU 亲和性、SMP 优化、交互式响应优先；算法基于时间片与交互性评分；ULE 首次 commit 于 2003-01-26T05:23:15Z（commit_hash = 35e6168fcdc76ba3ff2927279f9a48aa5ac3157d，freebsd.duckdb freebsd-src 仓库 commits 表 Jeff Roberson 提交，commit message 经 freebsd.duckdb commits 表验证为 “Add the ule scheduler. This is intended to be a general purpose process scheduler with many SMP benefits. It is still very experimental and should be used only in test environments.”（message_body 为空，主题行折叠空白已按规范合并；2026-09-11 回源补全））
- 总纲第 25 条——逻辑是形式主义而非世界本身的结构，ULE 设计相对克制
  - 辨析：经 bsd_commits.duckdb commits 表验证，ULE 首次 commit 为 2003-01-26T05:23:15Z（5.0-RELEASE 之后 10 天，属 5.1-CURRENT 开发周期）；ULE 是否真 O(1)，EPFL 2018 论文证明存在饥饿问题
  - 文献：Roberson 论文；EPFL USENIX ATC 2018 论文；Jeff Roberson. Add the ule scheduler. freebsd-src [DB/OL]. 2003-01-26T05:23:15Z. commit: 35e6168fcdc76ba3ff2927279f9a48aa5ac3157d ［A］
- 总纲第 9 条——经验优先，学术批评需独立验证
  - 辨析：ULE 移植是否准确反映原版，需查移植方法
  - 文献：Bouron et al. USENIX ATC 2018 论文 ［B］
- 默认禁用辨析：ULE 在 5.x 默认禁用 (4BSD 仍为默认)，因稳定性问题；6.0 起部分版本默认 ULE；7.1 起 ULE 成为默认（release/7.1.0 tagger_date = 2008-12-31T22:57:14Z，经 freebsd.duckdb tags 表验证：freebsd-src 仓库，tagger Ken Smith，tag_message “Copy releng/7.1 to release/7.1.0 for the 7.1-RELEASE.”；2026-09-11 回源补全）
  - 文献：Bouron et al. USENIX ATC 2018 论文 ［B］

## 98.10 Torvalds 对 VM 的辱骂性批评——四层辩证（批评—反批评—再批评—合图）（2026-09-11 整改按磁盘实况 98.10 归位，三次重复合并为一节）

- 要点：【批评层】Linus Torvalds 曾在 Linux 内核邮件列表（LKML）中辱骂 FreeBSD VM 开发者为 “incompetent idiots”（不胜任的白痴），反映 BSD 与 Linux 社区在虚拟内存子系统设计哲学上的长期张力；该辱骂被 FreeBSD 社区长期记忆，成为 BSD 与 Linux 关系史中的标志性话语事件。需特别辨析：任务描述中提及的 “Alan Cox” 实〔存疑：原文截断，待考；2026-09-11 联网核验：语录一手出处为 Torvalds 2006-04-20 致 LKML 邮件 “Re: Linux 2.6.17-rc2”（针对 FreeBSD zero-copy COW 页表方案的批评），帖内未见 Alan Cox 参与〕 [存疑脚注] “incompetent idiots” 语录原文经 comp.unix.bsd.freebsd.misc 新闻组存档转载（含邮件头 From: Linus Torvalds, Subject: Re: Linux 2.6.17-rc2, Date: 2006-04-20）与 LWN 2008-02-12 报道转引双重核验，LKML 官方存档原始链接待补。（2026-09-11 整改补标）
- 总纲第 3 条——不存在进步，只有权力再分配，性能回撤为可扩展性的代价。
  - 文献：SMPng 文档 ［A］；KSE 文档；7.0 发行说明 ［A］；Roberson 2003; 基准测试 ［A］

## 98.5 MAC 的策略架构（2026-09-11 整改按磁盘实况 98.5 归位，两次重复合并为一节）

- 要点：MAC 策略架构：(1) 策略模块通过 MAC Framework 钩子介入内核；(2) 内核对象关联 label；(3) 策略检查在客体访问时执行；(4) 支持策略组合 (多策略并行)
- 史料：**mac(4)** 手册页、Watson PhD 论文 ［A］
- 史观：总纲第 4 条——分离聚合是永恒规律，多策略组合增加复杂性
- 辨析：多策略组合是否真可用，需查测试；MAC 是否真被广泛使用，需查部署案例
- 文献：**mac(4)** 手册页；Watson BSDCon 2001 演讲；FreeBSD 5.0 Release Notes ［A］

## 文献

- FreeBSD 5.0 Release Notes；BSDCon 2003 5.0 演讲；release/5.0.0. freebsd-src 仓库 tag [DB/OL]. 2003-01-16T16:56:23Z. tag: release/5.0.0; commit: 47227ef0ef663b7abb81ab5a60a450da9a93d24b；freebsd.duckdb L1.1.1 查询结果（freebsd-src 年度 commit 量 2002-2003）[DB/OL]；freebsd.duckdb L1.4.1 查询结果（freebsd-src release tag 间隔）（2026-09-12 回源补全，据同章 98.1 子节文献段）
- Roberson BSDCon 2003 论文 ［B］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

## 史料

- [DB:historical_claims:claim] 关键词行级挖掘素材线索 98.11-关键词行级挖掘素材线索（1 条，CL-RM 段，见 98.11-关键词行级挖掘素材线索.md）

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2739 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2739`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Dev Summit: NetApp: Testing and CI〕讲者口述：其内建看板（转写音作 glance）里每个方块代表一次 CI 运行，顶端绿色的表示已通过、已生成 nightly；把光标悬停还能看到该问题牵连的所有 bug。（YouTube EPnQhhA9bnGJU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2740 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2740`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Dev Summit: NetApp: Testing and CI〕讲者口述：他们把 Jenkins 当作信息集散地（clearinghouse）来用，与多数人的用法不同——中间充当胶水，把既有流程跑出来的作业与结果汇进来并做分诊。（YouTube EPnQhhA9bnGJU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
