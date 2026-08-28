---
chapter: 第 40 章
id: CH40
volume: 第02卷-伯克利的岁月
---

# 第 40 章 net2重写运动的贡献者与边缘者

## 要点

- Net/2（**1991.6**）是 BSD 首个完全自由完整代码发布，但 **1992-1994 年** USL 诉讼导致 Net/2 法律地位处于争议状态，CSRG 在诉讼期间继续 4.4BSD 开发；**1994 年 2 月** Novell-UC Berkeley 达成和解后，CSRG 于 **1994 年 6 月** **同时发布** 两个版本：4.4BSD-Lite（完全自由版，不含
- BSD 重写运动的独特性包括：基于成熟 BSD 代码基础（4.3BSD Reno）、社区志愿重写模式（早于现代开源协作 10 年）、法律风险预判与文件保留、BSD 许可证的宽松性（允许商业封闭）、与 USL 诉讼的法律博弈，这些独特性使 BSD 路线与 Linux 路线在 1990 年代分化
- shadow password（密码散列分离存储）在 BSD 与 System V 的分野源于 **1980 年代** 两者的安全哲学差异——System V **R3.2**（**1987 年**）引入 `/etc/shadow` 文件将密码散列从 `/etc/passwd` 移至仅 root 可读的 `/etc/shadow`，降低字典攻击风险，反映 System V 优先考虑商用客户的密码安
- 边缘贡献者的史料散见于源代码注释、邮件列表、新闻组与 CSRG 内部档案，缺乏系统化传记，需通过多源交叉核对恢复身份，特别是使用用户名的匿名贡献者与一次性补丁提交者
- Net/2 重写采用‘逐文件替换’策略：对每一个包含 AT&T 版权代码的文件，CSRG 安排独立程序员（未见过 AT&T 源码者）根据公开发布的文档与接口描述重写实现。这一‘洁净室’方法的法学依据是 Reverse Engineering 原则（Sony v. Connectix, 2000 年的判决确认，但 CSRG 在 1989 年即已实践）。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3715] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3765] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3767] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3769] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3814] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3936] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3942] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_3954] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 folder，原因：folder 第40章
- [DB:references_fulltext:chapter_matches:chmatch_1544] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_978] 卷“第02卷-伯克利的岁月”第 40 章，匹配置信度 0.8，原因：关键词重合 2 项 + 加分 1
- [DB:bsdnow_podcast:outline_mappings:om_11526] BSD Now 第 527 期，匹配 CH40 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11939] BSD Now 第 474 期，匹配 CH40 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12605] BSD Now 第 404 期，匹配 CH40 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12677] BSD Now 第 379 期，匹配 CH40 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 4.4BSD-Encumbered 与 4.4BSD-Lite 均于 1994 年 6 月同时发布（McKusick 当事人原文"Simultaneously, the complete system was released as 4.4BSD-Encumbered"），非 1993 年 11 月——1993 年仅发布过 4.4BSD-Alpha 测试版给 AT&T 许可持有者；4.4BSD-L
- BSD 与 Linux 的“独特性”对比需谨慎，避免事后判断，1991 年两者均处于早期阶段
- shadow password 分野的“安全哲学差异”叙述需避免简化为“BSD 不重视安全”——BSD 选择单文件格式是基于 NIS 工程约束的实践判断，而非忽视密码安全，须区分“安全哲学差异”与“安全意识差异”；BSD 直至 **4.4BSD-Lite** 仍坚持 `/etc/passwd` 单文件格式的判断需核对——4.4BSD-Lite Release Notes 与 4.4BSD 系统管理
- Net/2 历史意义的辨析须遵循 0 信任原则——即使 McKusick 1999 当事人叙述亦须与 Justia 法院意见书、FreeBSD Handbook、NetBSD 官方历史页面等独立来源交叉验证；CSRG 的发布意图（“完全自由 BSD”）与 USL 的诉讼视角（“盗用 AT&T 代码”）存在根本分歧，须区分双方视角而不预设一方正确；Net/2 的“历史意义”在不同史料中有不同表述，需

## 文献

- Net/2 Release Notes (1991.6)；4.4BSD-Lite/4.4BSD-Encumbered Release Notes (1994.6)；4.4BSD-Lite 2 Release Notes (1995.6)；Novell-UC Berkeley 和解协议（1994.2）；FreeBSD/NetBSD/OpenBSD Release Notes；McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading: Addison-Wesley, 1996. ISBN: 0-201-54979-4 ［B］；资料数据库.db 文献计量学分析报告（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md` Task 22，2026-07-27）；外部基准报告（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/外部基准-Academic-CVE.md` 第 1.2 节，E-19，2026-07-27）；卷章数据映射表（`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md` 第二卷第 20 章）
- Bostic, K. (1991) "Net/2 Release Notes"；McKusick, K. (1999) "Twenty Years of Berkeley Unix"；Moody, G. (2001) "Rebel Code" ［B］<!-- DB_REF:linux_kernel.duckdb -->> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。> 1991-1991 年间：0 次提交。> 仓库总览：1,474,341 次提交，82,718 位贡献者，1970-01-01 至 2026-08-24。
- *4.2BSD** `/etc/passwd` 文件格式规范；System V **R3.2** `/etc/shadow` 文件规范 (**1987**)；**4.4BSD-Lite** Release Notes (**1994.6**)；4.4BSD 系统管理员手册（SMM）；**FreeBSD 4.0** Release Notes (**2000.3**)；Salus, P. H. (1994) "A Quarter Century of UNIX"；Leffler, S. J. et al. (1989) "The Design and Implementation of the 4.3BSD UNIX Operating System" ［A］[^doubt-resolved-235]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解[^doubt-resolved-238]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解
- Net/2 源代码注释；CSRG 邮件列表存档（伯克利 Bancroft 图书馆）；comp.unix.bsd 新闻组存档 ［A］---## 文献增补与辩证校准（2026-08-08 追加）> - **文献增补（ref 3778）**：McKusick《Twenty Years of Berkeley Unix》(1999) 确认“约一百个工具”18 个月内由社区志愿者完成——39.7 匿名贡献者考据的直接一手依据> - **文献增补（ref 3780）**：4.4BSD 设计书作者简介（Bostic GWU 背景/CSRG 400+ 工具管理）可补充 39.7 人物档案> - **辩证校准（总纲 24.1/20.5）**：39.7 “需主动恢复其历史可见性”的表述，应以“如实记录”替代“主动恢复”——边缘化是形式主义固有结构（20.5），匿名贡献者的价值按其实际贡献记录即可，不须以“被亏欠”姿态写作（24.1：少数≠错误；总纲5：无必然性）
- CSRG Net/2 档案； McKusick 1999 ［A］
- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix"；FreeBSD Handbook 第 1 章（docs.freebsd.org/en/books/handbook/introduction/#history）；NetBSD 官方历史页面（netbsd.org/about/history.html）；*Unix System Laboratories v. Berkeley Software*, 832 F. Supp. 790 (D.N.J. 1993) ［B］

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第40章-net2重写运动的贡献者与边缘者 第 40 章 net2重写运动的贡献者与边缘者（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：4 期，扫描 segments：3266 条 -->

### 要点（播客口述史提取）
- And apparently the same thing with Net2 showed up in 1993 as well.（BSD Now EP150 @ 3219.260）

### 史料（播客当事人陈述）
- （待人工提取）

### 史观（播客当事人观点与总纲映射）
- （该章节匹配播客中未提取到当事人观点性陈述）

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP150] Pennington J. BSD Now: 150: Sprinkle a little BSD into your life.[EB/OL]. (2016-07-13)[2026-08-15]. https://www.bsdnow.tv/150.
- [BSD Now EP203] Pennington J. BSD Now: 203: For the love of ZFS[EB/OL]. (2017-07-19)[2026-08-15]. https://www.bsdnow.tv/203.
- [BSD Now EP273] Pennington J. BSD Now: Episode 273: A Thoughtful Episode | BSD Now 273[EB/OL]. (2018-11-23)[2026-08-15]. https://www.bsdnow.tv/273.
- [BSD Now EP298] Pennington J. BSD Now: 298: BSD On The Road[EB/OL]. (2019-05-16)[2026-08-15]. https://www.bsdnow.tv/298.

<!-- /PODCAST_MINE -->
