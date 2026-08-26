---
chapter: 第 114 章
id: CH114
volume: 第06卷-freebsd的核心技术革新
---

# 第 114 章 dtrace的设计与solaris起源

## 要点

- DTrace 设计的一手史料包括：Cantrill 在 dtrace.org/blogs/bmc/ 的个人博客（2006-2024 年，dtrace.org 域名仍可访问但部分旧文章存档需经互联网档案馆获取）；USENIX 2004 年论文全文（usenix.org 永久存档）；Solaris Dynamic Tracing Guide（docs.oracle.com 可访问）；Cantrill、
- D 语言最权威的设计文档是 Cantrill 等人 2004 年 USENIX 论文的第 3 节，该节完整描述了 D 语言的类型系统、变量种类（全局、线程局部、子句局部、聚合）、安全约束、执行模型；Solaris Dynamic Tracing Guide（Sun/illumos 出版）是最完整的参考手册，含 D 语言所有特性的逐章说明；FreeBSD 手册页 **dtrace(1)** 的 D
- Sun 选择 CDDL 许可 OpenSolaris（含 DTrace 和 ZFS）的历史背景是 Sun 2004-2005 年的开源战略转型：Sun CEO Scott McNealy 推动 OpenSolaris 以对抗 Linux 在服务器市场的崛起；CDDL 由 Simon Phipps（Sun 首席开源官）和 Sun 法务团队基于 MPL 1.1 起草，2004 年 12 月 1 日提交
- macOS DTrace 集成事件的一手史料包括：Apple 开源代码 opensource.apple.com/source/dtrace/（存档于互联网档案馆）；Leventhal 在 dtrace.org/blogs/ahl/ 的两篇博客（2008-01-18、2008-06-07）；Mac OS X 10.5 Leopard 发布新闻稿和技术文档；MacTech 2007 年 11 月《E
- FreeBSD DTrace 移植的一手史料包括：John Birrell 在 <freebsd-current@freebsd.org> 和 <freebsd-dtrace@freebsd.org> 邮件列表的移植进度帖子（2006-2008 年）；FreeBSD Perforce 仓库//depot/projects/dtrace/ 分支初始导入记录；FreeBSD Subversion 仓库

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_725] 卷“第06卷-freebsd的核心技术革新”第 114 章，匹配置信度 0.6，原因：关键词重合 2 项

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 原文将"Jolitz & Jolitz 1990s Dr. Dobb's Journal ‘Porting UNIX to the 386’"列为 DTrace 文献系明显错误——Jolitz 夫妇的 DDJ 文章是关于 386BSD 的，与 DTrace 无关；原文称论文作者为"Cantrill, Shapiro, Wiethels"系名字错误——第三作者是 Adam H. Leventhal，
- 原文称“D 语言与 BPF 程序比较”但引用 Jolitz DDJ 文章系无关文献错误已修正；D 语言不支持浮点运算是一个常被忽视的限制——DTrace 在内核态执行时默认不使用浮点寄存器以避免保存/恢复浮点上下文的开销，D 程序中不能使用 float/double 类型；D 语言的数组大小有静态上限（DTRACEOPT_MAXSIZE 等可调参数），这些限制都是安全模型的一部分
- 原文将“Sun 许可策略”与 Jolitz DDJ 文章相关联系错误；Sun 是否故意选择 CDDL 以阻止 ZFS/DTrace 进入 Linux 是一个长期争议——Sun 方（Phipps、Cooper）多次否认，称 CDDL 是基于 MPL 的合理许可证选择；GPL 阵营（FSF、Eben Moglen）则认为 CDDL 是故意设计为 GPL 不兼容；从技术史角度，这一争议无法在缺乏 Sun
- 原文标题称“2008 年 Mac OS X 集成 DTrace”系日期错误——Mac OS X 10.5 Leopard 于 2007 年 10 月 26 日发布，DTrace 争议始于 2008 年 1 月（Leventhal 博客发表），修复于 2008 年 6 月（10.5.3），应修正为“2007 年 Mac OS X 集成 DTrace”；原文称“Apple 修改了部分探针以隐藏 iTu
- 原文 73.5 节标题称“George Neville-Neil 等完成 DTrace 移植”需修正——Neville-Neil 是重要维护者但非发起人；John Birrell 才是 DTrace FreeBSD 移植的发起者和核心实现者，这一事实在 FreeBSD 源码的 copyright 声明和早期 commit log 中均可查证；Birrell 去世的精确信息因公开讣告缺失而标注为 据

## 文献

- Cantrill, B. et al. (2008). Fishworks: Now it can be told. dtrace.org/blogs/bmc/; illumos Project. Dynamic Tracing Guide. illumos.org/books/dtrace/; Gregg, B. DTrace Tools and DTraceToolkit. brendangregg.com/dtrace.html; Leventhal, A. H. (2008). Mac OS X and the missing probes. dtrace.org/blogs/ahl/ ［C］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Cantrill, B. M. et al. (2004). Dynamic Instrumentation of Production Systems. USENIX ATC '04; illumos Project. Solaris Dynamic Tracing Guide. illumos.org/books/dtrace/; FreeBSD Project. **dtrace(1)** Manual Page (D Language Reference) ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Phipps, S. (2005). Why We Chose CDDL. webmink.com; Open Source Initiative. CDDL Approval Archives (2004-12/2005-01). opensource.org; Sun Microsystems. (2005-06-14). OpenSolaris Launches. Press Release[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2004-2004 年间：45,499 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Apple Inc. opensource.apple.com/source/dtrace/ (archived); Leventhal, A. H. dtrace.org/blogs/ahl/ (2008 posts); Apple Inc. Mac OS X 10.5 Technical Specifications (2007-10-26) ［C］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2007-2008 年间：65,762 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project Mailing List Archives. lists.freebsd.org (freebsd-current, freebsd-dtrace); FreeBSD Source Repository. cddl/ import history; FreeBSD Project. Release Notes 7.1-12.x (DTrace changelog entries) ［A］[^doubt-resolved-616]: 据 Handbook (未署名) 消解[^doubt-resolved-617]: 据 Handbook (未署名) 消解[^doubt-resolved-618]: 据 upper-saddle-river-prentice-hall (Gregg, 2011) 消解[^doubt-resolved-619]: 据 操作系统内核并发错误检测研究进展_期刊 (石剑君, 2021) 消解[^doubt-resolved-620]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解[^doubt-resolved-621]: 据 Arch_Handbook (未署名) 消解[^doubt-resolved-622]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-623]: 据 The Fall of the Bell System A Study in Prices and Politics (Peter Temin, Louis Galambos) (z-library.sk, 1lib.sk, z-lib.sk) (未署名) 消解<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
