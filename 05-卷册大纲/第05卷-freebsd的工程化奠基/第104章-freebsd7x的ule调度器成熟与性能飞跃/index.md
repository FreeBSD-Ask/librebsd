---
chapter: 第 104 章
id: CH104
volume: 05
---

## 要点

- ULE 调度器由 Jeff Roberson 设计，2003 年 1 月 26 日首次提交（commit_hash = 35e6168fcdc76ba3ff2927279f9a48aa5ac3157d，committer_date = 2003-01-26T05:23:15Z，message_subject ="Add the ule scheduler. This is intended to be a general purpose process scheduler with many SMP benefits. It is still very experimental and should be used only in test environments."）并随 FreeBSD 5.0 引入作为实验性调度器，2008 年 12 月 31 日 7.1-RELEASE（release/7.1.0 tagger_date = 2008-12-31T22:57:14Z，tagger = Ken Smith，target_commit_hash = a1fc2b0c89a1dd2ca090ae990ab45b21363ab76e；官方公告日期为 2009 年 1 月 4 日）成为 amd64 与 i386 GENERIC 内核默认调度器，历时 6 年；演进包括 SMP 扩展优化、交互响应改进、公平性修复；7.0-RELEASE（release/7.0.0 tagger_date = 2008-02-24T05:45:17Z，tagger = cvs2svn，target_commit_hash = ba209d619d07461cc752dcdd596ab0d9b50e847a；官方公告日期为 2008 年 2 月 27 日）ULE 2.0 已大幅改进但 4BSD 仍为默认，7.0 公告明确"ULE scheduler is vastly improved...the 4BSD scheduler is still the default for 7.0 but ULE may become the default for 7.1"
- 7.1 将 ULE 设为默认调度器，影响包括：(1) SMP 性能提升；(2) 交互响应改善；(3) 4BSD 调度器保留为选项；(4) 部分工作负载需重新调优
- ULE 成熟辨析：(1) 是否真成熟（7.1 是否过早默认）；(2) 与 Linux O(1)/CFS 比较；(3) 6 年是否值得
- ULE 史料疑点：(1) 设计起始时间（2002 vs 2003）；(2) Roberson 的灵感来源（Solaris/Windows 调度器）；(3) 是否有学术背景
- FreeBSD 7.0 的 SMP 基准测试（如 Concurrent Users、SPECcpu）显示相比 6.x 有显著提升，特别是在多核环境下；ULE 调度器与 SMPng 细粒度锁的共同作用

## 史观

- 总纲第 2 条——实践先于理论，ULE 的 6 年演进是工程实践驱动的而非理论预设
  - 辨析：ULE 是否真比 4BSD 优越，需查基准测试；6 年成熟期是否过长；7.0 与 7.1 对 ULE 状态的表述差异；经 bsd_commits.db tags 表验证，7.0-RELEASE 的 tagger_date 为 2008-02-24T05:45:17Z（cvs2svn 创建 tag），7
- 总纲第 2 条——实践先于理论，SMP 性能是工程迭代的结果
  - 辨析：测试方法是否公平，需查测试环境（硬件、内核配置）
  - 文献：FreeBSD 7.0 SMP Performance Benchmarks (freebsd.org 2008)；Phoronix"FreeBSD 7.0 Performance" (2008.3)；Roberson (2003) BSDCon paper[
- 总纲第 4 条——0 信任原则
  - 辨析：选择性报告，需查原始数据
  - 文献：Phoronix"FreeBSD 7.0 SMP Performance" (2008.3)；OpenBenchmarking.org FreeBSD 7.0 test results；McKusick & Neville-Neil (2014), Chapter 4 ［B］
- 总纲第 4 条——0 信任原则
  - 辨析：厂商赞助，需查利益关系
  - 文献：FreeBSD 7.0-RELEASE/7.1-RELEASE Release Notes；McKusick & Neville-Neil (2014)；The FreeBSD Foundation 2007-2009 Annual Reports；BSDCan 2007-2009 Conference Proce
- 总纲第 9 条——简洁与复杂的辩证，大页增加复杂度但减少 TLB miss
  - 辨析：大页是否真提升性能，需查基准测试
  - 文献：Cox, A. et al. "Practical Transparent Superpage Support for FreeBSD" (FreeBSD Project, 2007)；FreeBSD 7.0 Release Notes；Navarro, J. 

## 辨析

- ULE 是否真比 4BSD 优越，需查基准测试；6 年成熟期是否过长；7.0 与 7.1 对 ULE 状态的表述差异；经 bsd_commits.db tags 表验证，7.0-RELEASE 的 tagger_date 为 2008-02-24T05:45:17Z（cvs2svn 创建 tag），7.1-RELEASE 的 tagger_date 为 2008-12-31T22:57:14Z（K
- 测试方法是否公平，需查测试环境（硬件、内核配置）
  - 文献：FreeBSD 7.0 SMP Performance Benchmarks (freebsd.org 2008)；Phoronix"FreeBSD 7.0 Performance" (2008.3)；Roberson (2003) BSDCon paper[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇
- (1) 测试是否全面（仅测特定负载）；(2) 是否有选择性报告；(3) 与 Linux/Solaris 比较是否公平
  - 史料：基准测试报告[考据完成：2026-07-28 经穷尽联网考据，上述史料清单为已知公开来源汇总，部分原始档案未公开数字化或须档案馆藏地现场核验，属史料缺口，须待原始档案公开后方可补充确证] 〔L3 官方文档〕
  - 史观：总纲第 4 条——0 信任原则
  - 辨析：
- 厂商赞助，需查利益关系
  - 文献：FreeBSD 7.0-RELEASE/7.1-RELEASE Release Notes；McKusick & Neville-Neil (2014)；The FreeBSD Foundation 2007-2009 Annual Reports；BSDCan 2007-2009 Conference Proceedings；Phoronix FreeBSD
- 大页是否真提升性能，需查基准测试
  - 文献：Cox, A. et al. "Practical Transparent Superpage Support for FreeBSD" (FreeBSD Project, 2007)；FreeBSD 7.0 Release Notes；Navarro, J. et al. "Practical, Transparent Operating Syst

## 文献

- Roberson, J. "ULE: A Modern Scheduler for FreeBSD"Proceedings of BSDCon 2003 (USENIX, 2003)；McKusick, M. K. & Neville-Neil, G. V. The Design and Implementation of the FreeBSD Operating System, 2nd ed. (Addison-Wesley, 2014), Chapter 4；FreeBSD 7.0/7.1 Release Notes；Jeff Roberson. Add the ule schedule
- FreeBSD 7.0 SMP Performance Benchmarks (freebsd.org 2008)；Phoronix"FreeBSD 7.0 Performance" (2008.3)；Roberson (2003) BSDCon paper[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
## 103.2.2 性能提升的工程意义
  - 要点：性能提升的工程意义：(1) FreeBSD 重新成为高性能服务器选择；(2) SMPng 项目终于见效；(3) 为后续 
- Phoronix"FreeBSD 7.0 SMP Performance" (2008.3)；OpenBenchmarking.org FreeBSD 7.0 test results；McKusick & Neville-Neil (2014), Chapter 4 ［B］
- FreeBSD 7.0-RELEASE/7.1-RELEASE Release Notes；McKusick & Neville-Neil (2014)；The FreeBSD Foundation 2007-2009 Annual Reports；BSDCan 2007-2009 Conference Proceedings；Phoronix FreeBSD Benchmarks 2008；freebsd-hackers 邮件列表 2008 年归档 ［A］
- Cox, A. et al. "Practical Transparent Superpage Support for FreeBSD" (FreeBSD Project, 2007)；FreeBSD 7.0 Release Notes；Navarro, J. et al. "Practical, Transparent Operating System Support for Superpages"ACM SIGOPS 2002 ［B］
## 103.3.2 大页支持的工程实现
  - 要点：大页支持的工程实现：(1) 修改 pmap 层；(2) 支持 reservation 机制；(3) 
- FreeBSD 7.0-RELEASE hardware notes (powerpc)；Hachmann, U. FreeBSD on PS3 (2008)；freebsd-ppc mailing list 2007-2008 archives ［A］
## 103.4.2 Sony 开放策略的效应
  - 要点：Sony 的 OtherOS 功能（PS3 初始固件支持）允许用户安装第三方 OS，影响包括：(1) 推动 BSD/Linux 在游戏机上运行；(2) 2010 年 Sony 通过固件更新移除 OtherOS 引发社区抗议
  - 史料：Sony PS3 固件更新说明、新闻 ［C］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。