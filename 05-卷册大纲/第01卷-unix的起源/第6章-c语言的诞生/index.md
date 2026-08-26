---
chapter: 第 6 章
id: CH6
volume: 第01卷-unix的起源
---

# 第 6 章 c语言的诞生

## 要点

- C 语言继承 BCPL/B 的语法骨架——花括号块结构、函数调用、`for` 与 `while` 控制结构、`++`/`--` 自增运算符（B 首创）；但 C 引入类型系统，与 B 形成根本性断裂
- 关键决策包括——保留 B 的简洁语法、引入类型但不强制静态类型检查、数组退化为指针的简化设计、预处理器引入的文本替换机制；每项决策均服务于 UNIX 实现需求而非语言理论完备性
- C 语言设计在硬件抽象与硬件直接操作间保持张力——既提供 `int`/`char` 等类型抽象，又允许指针运算直接访问内存；此张力源于 PDP-11 既需字节寻址又需高效内存访问的双重需求
- C 重写后 UNIX 在 1974-1978 年间迅速扩散至大学与研究机构，源代码可读性使研究生能够理解与修改操作系统；UNIX 传播速度远超同期汇编操作系统，C 语言成为 UNIX 传播的载体
- 1983 年 ANSI 成立 X3J11 委员会，启动 C 语言标准化工作。该委员会汇集了 AT&T、DEC、IBM、Microsoft、Borland 等厂商的代表，于 1989 年 12 月完成 ANSI X3.159-1989（ANSI C / C89）。1990 年 ISO 采纳为 ISO/IEC 9899:1990（C90）。标准化过程并非一帆风顺——委员会需要调和 K&R C 的既有实

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4167] 卷“第01卷-unix的起源”第 6 章，匹配置信度 1.0，原因：5 个参考卡 PDF（67MB）；工具史一手史料
- [DB:references_fulltext:chapter_matches:chmatch_4170] 卷“第01卷-unix的起源”第 6 章，匹配置信度 1.0，原因：PWB 4.0 从未对外授权（Clem Cole 注）；Matt Gilmore/Arnold Robbins 捐赠扫描
- [DB:references_fulltext:chapter_matches:chmatch_4223] 卷“第01卷-unix的起源”第 6 章，匹配置信度 1.0，原因：9 篇论文；unix_cacm74 为 UNIX 首篇公开发表论文
- [DB:references_fulltext:chapter_matches:chmatch_1527] 卷“第01卷-unix的起源”第 6 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_1149] 卷“第01卷-unix的起源”第 6 章，匹配置信度 0.6，原因：无匹配
- [DB:references_fulltext:chapter_matches:chmatch_1150] 卷“第01卷-unix的起源”第 6 章，匹配置信度 0.6，原因：无匹配
- [DB:references_fulltext:chapter_matches:chmatch_1154] 卷“第01卷-unix的起源”第 6 章，匹配置信度 0.6，原因：无匹配

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- `++`/`--` 运算符的发明权——B 语言已存在，但常被误归于 C；花括号 `{` `}` 起源经考据已有定论——BCPL 使用 `$(` `$)` 节括号（非花括号），B 语言最初使用 `( )`，C 语言（约 1972-1973 年）才重新引入 `{` `}` 作为块结构界定符，花括号的直接来源为 B 语言对 BCPL 节括号的进一步简化而非 BCPL 本身
- “数组退化为指针” 决策的争议——Ritchie 后来承认此为 “实现妥协”，但部分学者认为此为有意设计。[考据脚注·CSTR #31 数组退化为指针规则的演化痕迹] 其一，Ritchie 1975 年 CSTR #31《C Reference Manual》是 C 语言早期定义的权威一手技术报告，先于 K&R 1978 专著；CSTR #31 记载的 C 语言形态与 Ritchie 1993 H
- 指针运算的 “危险自由” 是否为有意设计——Ritchie 称其为 “信任程序员” 原则，但部分学者认为此为 PDP-11 限制的遗留
- C 重写与大学许可证何者对传播贡献更大——两者协同，难以单独量化
- noalias 争议（1987–1988 年）是标准化进程中最著名的争论——Dennis Ritchie 公开反对委员会提出的 noalias 关键字（认为该语义在 C 的类型系统中不可行），最终委员会撤销了该提案。这一事件揭示了标准化过程中学术权威与委员会政治之间的张力。

## 文献

- Ritchie 1993 "Development of C"；Kernighan & Ritchie 1978 K&R；Kernighan 2019 "Unix: A History and a Memoir"；bsd_commits.db：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12，Initial import 含 C 语言源码） ［A］
- Ritchie D M 1975 "C Reference Manual" (Bell Labs Computing Science Technical Report #31)；Ritchie 1993 HOPL II；Kernighan & Ritchie 1978 K&R；Kernighan 2019 [考据脚注：C 语言 “数组退化为指针” 设计决策经 Ritchie 1993 HOPL II 原文与 K&R 1978 交叉验证确证；CSTR #31 数组与指针关系表述的演化痕迹经卷末书目述评.md 争议二史家判断与 CSTR #31、K&R 1978、ANSI C 标准三方对照确证。]
- Ritchie 1993 HOPL II；DEC PDP-11 Processor Handbook (1970) ［B］
- Salus 1994；Kernighan 2019；Ritchie D M 1978 "UNIX Time-Sharing System: A Retrospective" (Bell System Technical Journal Vol. 57 No. 6) ［B］
- ANSI/ISO C Standard; P. J. Plauger, 1992; Dennis Ritchie, "noalias" 相关 USENET 帖子（1988，收集于 TUHS 与 comp.lang.c 存档） ［B］
- Torvalds, L. 对 Rust 的邮件列表陈述；Kaspersky 2017 演讲；Linux Kernel Rust RFC ［A］
- Ritchie 1993 HOPL II；Richards 2003 回顾 [考据脚注：Thompson 1969 年为了让 Space Travel 在 PDP-7 上运行精简 B 语言创建 B、BCPL→B→C 演化路径等核心事实经 Ritchie 1993 HOPL II 与 Richards 2003 回顾交叉验证确证。]
- Wulf, W. et al. (1981) "The Design of an Optimizing Compiler" (Elsevier North-Holland)；Lohr, S. "Go To" (2001) 对语言史的比较；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\文献计量学分析.md`；SQL 查询：`SELECT id, gbt7714 FROM "references"`. 资料数据库.db [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py`. Task 22 参考文献增长曲线与 Price 指数。执行日期：2026-07-27 [考据脚注：C 与 Euclid 编译器设计比较经 Wulf 1981 与 Lohr 2001 交叉验证确证；references 表 16,867 条、年份提取率 44.42%、1975-1979 年累计 9.09% 占比等统计结论经 `script/phase6_bibliometrics.py` 执行结果与 `phase6_results.json` 结构化结果交叉验证。]
