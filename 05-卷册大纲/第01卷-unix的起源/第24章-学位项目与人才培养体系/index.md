---
chapter: 第 24 章
id: CH24
volume: 第01卷-unix的起源
---

# 第 24 章 学位项目与人才培养体系

## 要点

BSD 的历史与加州大学伯克利分校的计算机科学学位项目密不可分：CSRG（Computer Systems Research Group）作为 DARPA 资助的研究合同执行机构，同时承担了研究生培养职能，产出了 Bill Joy、Kirk McKusick、Mike Karels 等核心开发者。硕士与博士论文直接贡献了 BSD 的虚拟内存（Babaoglu & Joy 1981）、快速文件系统（McKusick 1984）、TCP/IP 协议栈等关键子系统。伯克利之外，CMU（Mach 微内核）、斯坦福（SUNDR/V Kernel）、MIT（X Window System）的学位项目也构成了 BSD 人才与技术的多中心来源。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3629] 卷“第01卷-unix的起源”第 24 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3643] 卷“第01卷-unix的起源”第 24 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3648] 卷“第01卷-unix的起源”第 24 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1539] 卷“第01卷-unix的起源”第 24 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_1145] 卷“第01卷-unix的起源”第 24 章，匹配置信度 0.8，原因：关键词匹配: sequel
- [DB:references_fulltext:chapter_matches:chmatch_1161] 卷“第01卷-unix的起源”第 24 章，匹配置信度 0.8，原因：关键词匹配: postgres
- McKusick M K, Joy W N, Leffler S J, Fabry R S. A Fast File System for UNIX[J]. ACM Transactions on Computer Systems, 1984, 2(3)（FFS 出自 McKusick 1984 年度论文，系本卷学位论文成果的当事人一手文献）
- CSRG Technical Reports 与 Berkeley Software Distribution 磁带归档（ tapes 目录，UCB EECS 系藏）
## 史观

总纲第 8 条——本体论上各方平等：BSD 的人才培养不仅依赖伯克利，还包括 CMU、斯坦福、MIT 等多中心的学术贡献，每个机构以不同的形式主义路径参与 BSD 生态的构建。总纲第 6 条——和解优于斗争：BSD 许可证的宽松条款本身就是学术成果向工业界平滑转移的制度设计，伯克利将研究生论文成果以 BSD 许可证发布，实现了学术自由与商业应用的制度性和解。总纲第 20 条——历史地理塑造思想土壤：伯克利的地理位置（旧金山湾区）与 DARPA 资助的研究合同共同构成了 BSD 人才培养的物质与制度土壤，这不是“地理决定论”而是形式主义条件制约。

## 辨析

学术机构的学位项目与 BSD 开发之间的因果关系需要审慎描述：CSRG 首先是 DARPA 资助的研究合同执行者，学位论文是其副产品而非其设计目标，将 BSD 简化为“学生项目”低估了 Bill Joy、Sam Leffler 等人在学期间的全职研究贡献。伯克利之后 BSD 人才向工业界（Sun Microsystems、Silicon Graphics、Apple、Google）的流动模式需要精确的群体传记学数据支撑，目前缺乏系统性的追踪研究。BSD 人才与 Linux 人才的学术背景差异（前者以伯克利为中心、后者以赫尔辛基大学与全球分散式贡献为特征）是否构成两者社区文化的结构性差异，仍有待比较史研究。

## 文献

- McKusick M K, Neville-Neil G V, Watson R N M. The Design and Implementation of the FreeBSD Operating System[M]. 2nd ed. Addison-Wesley, 2014.
- Babaoglu O, Joy W. Converting a Swap-Based System to do Paging in an Architecture Lacking Page-Reference Bits[C]//Proceedings of the Fourth ACM Symposium on Operating System Principles (SOSP). ACM, 1981.
- McKusick M K, Joy W N, Leffler S J, Fabry R S. A Fast File System for UNIX[J]. ACM Transactions on Computer Systems, 1984, 2(3).
- [DB:references_fulltext:chapter_matches:chmatch_3629]
- [DB:references_fulltext:chapter_matches:chmatch_1539]

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

