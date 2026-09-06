---
chapter: 第 17 章
id: CH17
volume: 第01卷-unix的起源
---

# 第 17 章 rust与系统编程语言的未来

## 要点

- 1974 年 1 月 UC Berkeley 收到 Bell Labs Version 4 UNIX 磁带，由研究生 Keith Standiford 在新购 PDP-11/45 上安装，PDP-11/45 由 CS+Math+Stats 三系联合购买，Bob Fabry 教授主导从 AT&T 获取 UNIX source license；Thompson 离开后（1976 年春夏），研究生 Ch
- 从总纲第 3 条形式主义膨胀角度分析，批评本身亦可能陷入 “现代语言必然优于 C” 的形式主义；BSD 的保守或为对另一形式主义的抵抗
- 动手者的史料稀缺，多见于 Ports MAINTAINER 字段与提交日志，缺乏自述与访谈；需以提交记录、邮件列表、Ports 历史多重交叉还原其贡献；其姓名散逸非因其社会阶层 “边缘”，而是因事后叙事偏向 Core Team 与大幅 commit 的核心开发者
- Linux 与三大 BSD 在 1990 年代至 2020 年代遵循相似的内核语言策略——以 C 为唯一系统编程语言，但三者在执行严格性与演进路径上存在显著差异：(1) Linux 内核在 1992 年短暂尝试 C++ 后彻底放弃，Torvalds 以个人权威维持 C 单一语言政策直至 2022 年 Rust 入核，其决策模式为“仁慈独裁者”（BDFL）模式，个人偏好权重极大；(2) FreeBS
- Go 和 Rust 在 BSD 生态中的引入遵循不同路径：(1) Go 语言——由 Robert Griesemer、Rob Pike 与 Ken Thompson（UNIX 与 C 语言共同创造者）于 2007 年在 Google 开始设计，2009 年 11 月开源发布，2012 年 3 月发布 Go 1.0；Go 在 FreeBSD 上的移植始于 2009-2010 年间，通过 Ports（

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4227] 卷“第01卷-unix的起源”第 17 章，匹配置信度 1.0，原因：极早期分时系统完整技术文档；SNAP FSNAP 计算器等
- [DB:references_fulltext:chapter_matches:chmatch_1535] 卷“第01卷-unix的起源”第 17 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- [考据脚注] 1974 年 UNIX 引入伯克利的精确日期与责任人。McKusick 文章与 SNAC CSRG 档案条目两方独立来源一致确认：1974 年 1 月 V4 磁带送达，Bob Fabry 教授主导，研究生 Keith Standiford 安装；Thompson 1975 年 sabbatical 时伯克利已有 UNIX（1974 年 1 月安装），Thompson 的贡献是帮助安装
- 形式主义分析不消解具体工程争议——哲学层面的 “形式主义膨胀” 批评与工程层面的 “ABI 稳定性” “构建时间” 争议分属不同范畴，前者评估语言选择的哲学立场，后者评估具体技术约束，二者可并行不悖；将形式主义分析误用为工程决策的替代会消解工程争议的具体性，但形式主义分析本身作为哲学审视仍有价值
- 史料稀缺不等于贡献不重要——以工程影响反推贡献价值：Java 移植使 FreeBSD 在 2000 年代企业 Java 部署中保有一席之地，Perl/Python/Ruby Port 维护使 BSD 系统在 Web 时代保持可用，Rust 移植使 FreeBSD 在 2020 年代 Rust 生态中不缺席；以史料多寡论英雄会系统性低估维护者劳动；须自反地承认 “以工程影响反推贡献价值” 本身亦是一
- 四种 BSD/Linux 内核语言策略的差异是否实质大于形式——所有四者均以 C 为内核语言，差异仅在边缘政策与演进路径上，此相似性可能反映的是 C 语言在操作系统内核领域的客观技术优势而非治理结构的差异；OpenBSD 的“安全要求 C”是否经得起实证检验——OpenBSD 内核虽为纯 C 但仍有安全漏洞，Rust 的内存安全保证在理论上可减少特定类别的漏洞，但 OpenBSD 社区认为 Rus
- Go 语言未进入 FreeBSD 基础系统是否与 Ken Thompson 的 BSD 渊源有关——Thompson 是 Go 语言三位设计者之一，且是 UNIX 与 C 语言的共同创造者、Berkeley 访问教授（1975 年），但 FreeBSD 社区对 Go 入基础系统的决策并未因 Thompson 的个人影响而改变，说明 BSD 治理的“精英治理”模式优先于个人关系；Go 的垃圾回收（G

## 文献

- McKusick M K. Twenty Years of Berkeley Unix [C]//Open Sources. O'Reilly, 1999; SNAC CSRG 档案条目 (snaccooperative.org/view/30565669); Internet Archive 1BSD tarball metadata (archive.org/details/1bsd.tar_201503) ［A］
- 1.md 项目统摄史观；社区辩论存档；McKusick 著作 ［A］
- FreeBSD Ports 提交日志；freebsd-java、freebsd-rust 邮件存档；1.md 项目统摄史观 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：BSD 语言移植的动手者（Java/Perl/Python/Ruby 移植团队）
- Linux 内核 coding-style.rst；FreeBSD committer's guide（docs.freebsd.org/en/articles/committers-guide/）；NetBSD 项目文档（netbsd.org/docs/）；OpenBSD 项目文档（openbsd.org/）；McKusick et al. 1996"The Design and Implementation of the 4.4BSD Operating System"；de Raadt 公开演讲与 OpenBSD 邮件列表存档 ［A］<!-- DB_REF:linux_kernel.duckdb -->> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1962-1978 年间：1 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- Go 语言官方文档（go.dev）；Thompson、Pike、Griesemer 2009 Go 初始设计文档；FreeBSD Ports Tree（lang/go、lang/rust）；freebsd-hackers 2024-01 邮件线程（lists.freebsd.org/archives/freebsd-hackers/2024-January/thread.html#2823）；Somers 2024 FreeBSD FUSE Rust 重写工作；Linux 6.1 Rust 合并公告（LKML 2022-12-11） ［A］
- FreeBSD Source Tree；freebsd-arch 邮件存档；McKusick et al. "Design of 4.4BSD" (1996) ［A］<!-- DB_REF:linux_kernel.duckdb -->> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1962-1978 年间：1 次提交。> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。
- LWN.net "A first look at Rust in the 6.1 kernel" 2022-10-13；LWN.net "Rust in the 6.2 kernel"；InfoQ 2022-12-20；LKML 2022-12-11 公告（lkml.org/lkml/2022/12/11/206）；Kernelnewbies 6.1 changelog；Alan Somers. The Case for Rust (in the base system) [EB/OL]. 2024-01-20T16:51:25Z. <https://lists.freebsd.org/archives/freebsd-hackers/2024-January/002823.html>; Warner Losh. Re: The Case for Rust (in the base system) [EB/OL]. 2024-01-20T18:37:25Z. <https://lists.freebsd.org/archives/freebsd-hackers/2024-January/002830.html>; freebsd-hackers 邮件存档 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2010 年间：34,527 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
