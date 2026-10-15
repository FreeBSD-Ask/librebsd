---
chapter: 第 104 章
id: CH104
volume: 第05卷-freebsd的工程化奠基
---

# 第 104 章 freebsd7x的ule调度器成熟与性能飞跃

## 要点

- ULE 调度器由 Jeff Roberson 设计，2003 年 1 月 26 日首次提交（commit_hash = 35e6168fcdc76ba3ff2927279f9a48aa5ac3157d，committer_date = 2003-01-26T05:23:15Z，message_subject ="Add the ule scheduler. This is intended to be a general purpose process scheduler with many SMP benefits. It is still very experimental and should be used only in test environments."）并随 FreeBSD 5.0 引入作为实验性调度器，2008 年 12 月 31 日 7.1-RELEASE（release/7.1.0 tagger_date = 2008-12-31T22:57:14Z，tagger = Ken Smith，target_commit_hash = a1fc2b0c89a1dd2ca090ae990ab45b21363ab76e；官方公告日期为 2009 年 1 月 4 日）成为 amd64 与 i386 GENERIC 内核默认调度器，历时 6 年；演进包括 SMP 扩展优化、交互响应改进、公平性修复；7.0-RELEASE（release/7.0.0 tagger_date = 2008-02-24T05:45:17Z，tagger = cvs2svn，target_commit_hash = ba209d619d07461cc752dcdd596ab0d9b50e847a；官方公告日期为 2008 年 2 月 27 日）ULE 2.0 已大幅改进但 4BSD 仍为默认，7.0 公告明确"ULE scheduler is vastly improved...the 4BSD scheduler is still the default for 7.0 but ULE may become the default for 7.1"
- 7.1 将 ULE 设为默认调度器，影响包括：(1) SMP 性能提升；(2) 交互响应改善；(3) 4BSD 调度器保留为选项；(4) 部分工作负载需重新调优
- ULE 成熟辨析：(1) 是否真成熟（7.1 是否过早默认）；(2) 与 Linux O(1)/CFS 比较；(3) 6 年是否值得
- ULE 史料疑点：(1) 设计起始时间（2002 vs 2003）；(2) Roberson 的灵感来源（Solaris/Windows 调度器）；(3) 是否有学术背景
- FreeBSD 7.0 的 SMP 基准测试（如 Concurrent Users、SPECcpu）显示相比 6.x 有显著提升，特别是在多核环境下；ULE 调度器与 SMPng 细粒度锁的共同作用

## 史观

- 总纲第 9 条——经验优先：ULE 的 6 年演进是工程实践驱动的而非理论预设
  - 辨析：ULE 是否真比 4BSD 优越，需查基准测试；6 年成熟期是否过长；7.0 与 7.1 对 ULE 状态的表述差异；经 bsd_commits.duckdb tags 表验证，7.0-RELEASE 的 tagger_date 为 2008-02-24T05:45:17Z（cvs2svn 创建 tag），7.1-RELEASE 的 tagger_date 则为 2008-12-31T22:57:14Z（Ken Smith）——叙事中须区分“tag 创建时间”与“官方公告时间”（两者分别为 2008 年 2 月 27 日与 2009 年 1 月 4 日）。
- 总纲第 9 条——经验优先：SMP 性能是工程迭代的结果
  - 辨析：测试方法是否公平，需查测试环境（硬件、内核配置）
  - 文献：FreeBSD 7.0 SMP Performance Benchmarks (freebsd.org 2008)；Phoronix“FreeBSD 7.0 Performance” (2008.3)；Roberson (2003) BSDCon paper[
- 总纲第 9 条——经验优先：选择性报告的检验须回到原始数据
  - 文献：Phoronix“FreeBSD 7.0 SMP Performance” (2008.3)；OpenBenchmarking.org FreeBSD 7.0 test results；McKusick & Neville-Neil (2014), Chapter 4 ［B］
- 总纲第 13 条——法律与道德是利益分配：厂商赞助关系影响基准报告的立场与取舍
  - 辨析：厂商赞助，需查利益关系
  - 文献：FreeBSD 7.0-RELEASE/7.1-RELEASE Release Notes；McKusick & Neville-Neil (2014)；The FreeBSD Foundation 2007-2009 Annual Reports；BSDCan 2007-2009 Conference Proce
- 专题语（不设总纲条号）——复杂度与性能的工程权衡：大页增加管理复杂度但减少 TLB miss
  - 辨析：大页是否真提升性能，需查基准测试
  - 文献：Cox, A. et al. “Practical Transparent Superpage Support for FreeBSD” (FreeBSD Project, 2007)；FreeBSD 7.0 Release Notes；Navarro, J.

## 辨析

- ULE 是否真比 4BSD 优越，须以基准测试回答；6 年成熟期是否过长；7.0 与 7.1 对 ULE 状态的表述差异——经 bsd_commits.duckdb tags 表验证，7.0-RELEASE 的 tagger_date 为 2008-02-24T05:45:17Z（cvs2svn 创建 tag），7.1-RELEASE 的 tagger_date 则为 2008-12-31T22:57:14Z（Ken Smith），官方公告日期分别为 2008 年 2 月 27 日与 2009 年 1 月 4 日，叙事须区分 tag 创建与公告发布两个时点。
- 测试方法是否公平，需查测试环境（硬件、内核配置）
  - 文献：FreeBSD 7.0 SMP Performance Benchmarks (freebsd.org 2008)；Phoronix“FreeBSD 7.0 Performance” (2008.3)；Roberson (2003) BSDCon paper［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 〔L3 官方文档〕
- 厂商赞助，需查利益关系
  - 文献：FreeBSD 7.0-RELEASE/7.1-RELEASE Release Notes；McKusick & Neville-Neil (2014)；The FreeBSD Foundation 2007-2009 Annual Reports；BSDCan 2007-2009 Conference Proceedings；Phoronix FreeBSD
- 大页是否真提升性能，需查基准测试
  - 文献：Cox, A. et al. “Practical Transparent Superpage Support for FreeBSD” (FreeBSD Project, 2007)；FreeBSD 7.0 Release Notes；Navarro, J. et al. "Practical, Transparent Operating Syst

## 文献

- Roberson, J. ULE: A Modern Scheduler For Threaded SMP Applications in FreeBSD[C]//Proceedings of BSDCon 2003 (USENIX, 2003)；McKusick, M. K. & Neville-Neil, G. V. The Design and Implementation of the FreeBSD Operating System, 2nd ed. (Addison-Wesley, 2014), Chapter 4；FreeBSD 7.0/7.1 Release Notes
- FreeBSD 7.0 SMP Performance Benchmarks (freebsd.org 2008)；Phoronix“FreeBSD 7.0 Performance” (2008.3)；Roberson (2003) BSDCon paper［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 104.3 大页支持的工程实现（存目）

- 本节正文见磁盘节文件 104.3-SUPERPAGE-大页支持.md；原 103.3.2 抢救残片（要点截断）已按正本体删除。

## 附：Sony 开放策略的效应（原 103.4.2，迁移处置 DEFERRED）

- 要点：Sony 的 OtherOS 功能（PS3 初始固件支持）允许用户安装第三方 OS，影响包括：（1）推动 BSD/Linux 在游戏机上运行；（2）2010 年 Sony 通过固件更新移除 OtherOS 引发社区抗议。
- 史料：Sony PS3 固件更新说明、新闻 ［C］
- 迁移说明：本节属第 13 卷 PlayStation 叙事（跨文件内容迁移），按整改规程登记 DEFERRED 交专项回迁，此处保留原 103.4.2 残片并改挂非节号标题。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP231（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 访谈嘉宾以 PDP-7 汇编起步的 UNIX 到 2017 年 FreeBSD 的半世纪架构演化为题，将两个关键里程碑定为 1970 年代末研究重心从 AT&T 贝尔实验室转向伯克利 CSRG，以及 1980 年代末至 1990 年代初开放源码化催生 386BSD 与三大 BSD。（BSD Now EP231，[311.72-365.52]，L1）
- 访谈强调从 1970 年代架构图到当代系统，进程、文件、管道等初始架构块仍存续，部分系统调用与 C 库函数近四十年几乎未变。（BSD Now EP231，[413.28-450.68]，L1）
- VBSDCon 2017 报告转述关于社区动力的演讲：许多 FreeBSD 开发者来自拨号 ISP 或 IRC 时代，这些进入路径如今已消失，项目需要寻找新的吸纳路径。（BSD Now EP231，[837.46-1004.6]，L2）
- FreeBSD current 邮件列表宣布由 Jeff Roberson 合入基于 cpuset 策略的 NUMA 支持，受 Dell EMC Isilon 与 Netflix 支持。（BSD Now EP231，[1885.86-1917.16]，L2）

**史料**：

- FOSDEM 前的访谈对象为软件工程教授、IEEE Software 主编、《Effective Debugging》作者。（BSD Now EP231，[100.48-120.24]，L1）
- 转述 VBSDCon 2017 参会报告，含对社区动力演讲的感想与 George Neville-Neil、Paul Vixie 等人演讲的提及。（BSD Now EP231，[666.34-991.88]，L2）
- FreeBSD current 邮件列表的 NUMA 合入公告（Jeff Roberson，提及 ULE 调度器作者身份）。（BSD Now EP231，[1885.86-2027.74]，L2）
- OpenBSD tech 邮件列表的栈指针检查 diff（Stefan），在每次陷阱与系统调用时校验栈指针所在页的 map_stack 标记。（BSD Now EP231，[2325.78-2402.74]，L2）

**史观**：

- 总纲9 经验优先：访谈以“形式解放”与经验优先解释 UNIX 架构的延续性，强调成熟形式使后来者得以在关键处创新而非重复造轮子。（BSD Now EP231，[468.68-483.88]，L1）
- 总纲5 没有必然性，只有偶然性：VBSDCon 报告呈现社区进入路径（拨号 ISP、IRC）随时代消失，开发者群体的再生产依赖偶然的历史条件而非必然机制。（BSD Now EP231，[896.12-947.68]，L2）

**辨析**：

- 访谈嘉宾姓名在转写中为“Diomedes Spinalis”的语音转写，具体拼写须核对 FOSDEM 演讲者名单；转写亦出现“Thomas Zoom”等疑似误转的人名。　[存疑脚注] 嘉宾姓名及若干人名拼写须以会议议程核实（BSD Now EP231，[90.64-97.48]，L4）

**文献**：

- [BSD Now EP231] Pennington J. BSD Now: 231: Unix Architecture Evolution[EB/OL]. (2018-02-01)[2026-08-15]. <https://www.bsdnow.tv/231>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-474 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-474`；w172 YouTube 章节路由采纳）

据〔EuroBSDcon 2024〕讲者 Olivier Certner 口述：FreeBSD 有两种实时优先级类型：RT_PR 是先出现的、更原生的一种，另一种为 POSIX 风格。（YouTube EPeUr4qI0nlKM，[183.84-192.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
