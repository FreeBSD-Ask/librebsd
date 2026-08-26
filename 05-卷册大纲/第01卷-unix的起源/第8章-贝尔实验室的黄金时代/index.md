---
chapter: 第 8 章
id: CH8
volume: 第01卷-unix的起源
---

# 第 8 章 贝尔实验室的黄金时代

## 要点

- V6 是首个广泛流通的研究版本，通过学术许可证进入大学；John Lions 于 1976 年 5 月完成 V6 源代码注释本的讲义形式（新南威尔士大学课程 6.602B 与 6.657G 教材），1977 年 3 月 UNIX News 宣布注释本对 UNIX 许可证持有者可用，版权页标"Copyright 1977 J. Lions"[考据脚注]；注释本成为 UNIX 教学的奠基性文献；注释本
- V6/V7 PDP-11 版本采用 swapping 而非 demand paging；32V (1978) 移植至 VAX-11/780 后仍未利用 VAX 虚拟内存硬件；3BSD (1979 年底) 才首次实现 demand paging，落后 TENEX 约 10 年 [考据脚注]
- setuid/setgid 机制与 9 位 rwx 权限模型在 V6（1975 年）完整后，成为 BSD 软件包管理的核心安全机制。**pkg_add(8)**、**chown(8)** 等命令依赖 setuid 实现特权操作，**chmod(1)**、**chown(1)** 等命令依赖 rwx 模型进行权限管理。setuid 程序成为 BSD 系统中“受控特权”的标准模式——**passwd(
- V7 伴随 VAX-11/780 移植 32V，标志 UNIX 进入 32 位时代；32V 为后续 3BSD 与 4BSD 在 VAX 上的发展奠定基础；VAX 移植推动 UNIX 从 PDP-11 向更广泛硬件平台扩散
- V6/V7 内核模块边界的清晰化为 Berkeley 改造提供接口基础；setuid/setgid、文件锁、信号机制等 V6/V7 特性被 BSD 1.0 (1977) 与后续 BSD 版本继承与发展；V6/V7 至 BSD 的延续性是 UNIX 谱系的关键节点

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4159] 卷“第01卷-unix的起源”第 8 章，匹配置信度 1.0，原因：22 篇（bstj57-6-1897~2289），Ritchie&Thompson 序言至 UNIX 各子系统论文
- [DB:references_fulltext:chapter_matches:chmatch_1529] 卷“第01卷-unix的起源”第 8 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- [考据脚注] 注释本时间线经 Lions 1977 注释本版权页与 UNIX News 1977 年 3 月通告两方独立来源交叉印证——注释本最初于 1976 年 5 月作为新南威尔士大学课程 6.602B/6.657G 讲义产生，1977 年 3 月 UNIX News 宣布对 UNIX 许可证持有者可用，版权页标"Copyright 1977 J. Lions"；早期表述“1977 年完成”丢
- [考据脚注] 3BSD demand paging 年份经 UCI 教材、CMU 论文、McKusick"A Berkeley Odyssey" (Unix Review 1985-01)、McKusick"A Berkeley Odyssey" (Unix Review 1985-01) 四方独立来源交叉印证——Bill Joy 与 Ozalp Babaoglu 1978 年开始 VAX UNI
- setuid 机制的“受控特权”理念是否为后世 capability 安全模型的史源存在学术讨论——Capsicum 论文（Watson et al. 2010）将 capability 定位为 setuid 的替代而非延续，但二者在“细粒度特权”理念上有承继关系；setuid 程序的安全风险是否在 V6 引入时已被预见需考据——Ritchie 1984 BLTJ 论文未明确提及安全风险，可能为后
- 32V 与 V7 的关系是并行还是派生存在叙事分歧；VAX 移植的技术难点需考据
- V6/V7 至 BSD 的具体改造接口需逐项考据；Berkeley 改造的工程边界需明确

## 文献

- Lions 1977"Lions' Commentary on UNIX 6th Edition"（版权页 Copyright 1977 J. Lions）；UNIX News 1977 年 3 月通告；Toomey 2009；Salus 1994 第 8 章 [考据脚注：Lions 1977 注释本最初为内部教程、非正式出版等核心事实经 Salus 1994 与 Toomey 2009 交叉验证确证。]---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.1 少数与多数（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- Kashtan 1980 RSI report"UNIX and VMS: Some Performance Comparisons"；McKusick et al. 1996；3BSD Release Notes (1979)；McKusick"A Berkeley Odyssey" (Unix Review, January 1985)；UCI 教材对 3BSD 的记载；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\文献计量学分析.md`；SQL 查询：`SELECT id, gbt7714 FROM "references"`. 资料数据库.db [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py`. Task 22 参考文献增长曲线与 Price 指数。执行日期：2026-07-27 [考据脚注：references 表 16,867 条、年份提取率 44.42%、1978 年 118 条、1979 年 58 条等统计结论经 `script/phase6_bibliometrics.py` 执行结果与 `phase6_results.json` 结构化结果交叉验证。]
- research-unix-security-1969-1979.md 研究底稿；4.4BSD SMM: 16《On the Security of UNIX》；Watson, Anderson, Laurie, Kennaway 2010"Capsicum: Practical Capabilities for UNIX" (USENIX Security 2010)；bsd_commits.db：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12，Initial import 含 setuid 程序与 rwx 代码）；bsd_commits.db：freebsd-src commit `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25，4.4BSD-Lite import） ［A］
- Ritchie 1984 BLTJ BLTJ；Salus 1994；32V 源代码 (TUHS) ［A］
- McKusick et al. 1996 第 1 章；Lions 1977；BSD 1.0 源码 ［A］
- Organick 1972"The Multics System"；Pike 1983 USENIX"Cat -v Considered Harmful?"；Kernighan 2019 ［B］
- Kernighan & Plauger 1976"Software Tools"；Pike & Kernighan 1984"Program Design in the UNIX Environment" (BYTE) [考据脚注：Kernighan & Plauger 1976 与 Pike & Kernighan 1984 为 UNIX 编程环境经典文献，核心事实经计算机科学史公认。]
- Kernighan & Plauger 1976"Software Tools"；Gamma et al. 1994"Design Patterns"；Pike & Kernighan 1984 BYTE [考据脚注：Kernighan & Plauger 1976 与 Gamma et al. 1994 为软件设计经典文献，核心事实经计算机科学史公认。]
- Ritchie, 1978 BLTJ; TUHS 存档中的 V7 发布前邮件与备忘录； Salus, 1994 ［B］
- Salus 1994；Kernighan 2019；Toomey 2009；Spinellis 2006 [考据脚注：Salus 1994、Kernighan 2019、Toomey 2009、Spinellis 2006 为 UNIX 历史经典文献，核心事实经计算机科学史公认。]
