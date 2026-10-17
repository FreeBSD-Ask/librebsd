---
chapter: 第 22 章
id: CH22
volume: 第01卷-unix的起源
---

# 第 22 章 编程语言史

## 要点

C语言的诞生（1972年，Dennis Ritchie）与UNIX的共生关系构成了BSD史的技术语法基础：C语言为UNIX从汇编向高级语言移植提供了工具，UNIX则为C语言提供了实际验证场域。Fortran、ALGOL 60、CPL、BCPL、B等语言构成了C语言的谱系前身，而C++、Objective-C、Go等语言则是C的后继分支。BSD系统自身的工具链（cc、make、lex/yacc）与脚本语言（sh、awk、sed、perl）共同塑造了UNIX“小工具组合”的编程文化，这一文化在BSD社区中持续至今。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3598] 卷“第01卷-unix的起源”第 22 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3601] 卷“第01卷-unix的起源”第 22 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3632] 卷“第01卷-unix的起源”第 22 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1538] 卷“第01卷-unix的起源”第 22 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第 10 条——动手者创造历史：C语言是Ritchie为满足系统编程的实际需求而创造的，而非学院派语言设计的产物，其“信任程序员”的设计哲学体现了“没有多余形式主义的老实人”精神。总纲第9条——经验优先：C语言的成功源于其在UNIX内核与工具移植中的实用性验证，而非理论完备性——其类型系统的宽松与指针的自由度，在实践中被证明是系统编程不可或缺的灵活性来源。总纲第 5 条——没有必然性，只有偶然性：C语言成为“系统编程的通用语”并非必然，ALGOL 68的过度复杂、Pascal的过度约束、PL/I的过度庞大，都构成了C语言胜出的偶然条件。

## 辨析

C语言的设计哲学（信任程序员、不隐藏底层细节）既是其灵活性的来源，也是缓冲区溢出等安全漏洞的根源。BSD社区对lint、bounds-checking等静态分析工具的早期采纳，构成了对C语言固有风险的工程化应对。将C语言等同于“不安全语言”的当代批评需要放置于历史语境中理解：1970年代的内存与CPU资源约束使得运行时检查的成本不可接受。BSD向Rust等内存安全语言的渐进迁移（如FreeBSD对Rust的探索性引入）构成了对C语言遗产的辩证继承。

## 文献

- Ritchie D M. The Development of the C Language[C]//HOPL-II. ACM, 1993；Kernighan B W, Ritchie D M. The C Programming Language[M]. 2nd ed. Prentice Hall, 1988；Bergin T J, Gibson R G. History of Programming Languages II[M]. ACM Press/Addison-Wesley, 1996；[DB:references_fulltext:chapter_matches:chmatch_3598]；[DB:references_fulltext:chapter_matches:chmatch_1538]

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2655 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2655`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis〕讲者口述：C 语言教材首页那个 hello world 例程看似平凡，讲者要顺着它一路追到程序真正跑起来所牵涉的全部环节。（YouTube EPyWCMy5EiNkQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2656 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2656`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis〕讲者口述：在传统的 UNIX 操作系统里进程不是凭空出现的，而是先 fork 复制出一份完整副本、再调用 execve 替换掉整份程序内容，所以讲者从内核里的 execve 开始讲。（YouTube EPyWCMy5EiNkQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2657 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2657`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis〕讲者口述：链接时看到的 crt1 目标文件负责取到 _start，那是程序真正的入口，它设置运行环境、初始化各种结构，然后才去调用 main。（YouTube EPyWCMy5EiNkQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2658 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2658`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Brooks Davis〕讲者口述：在 FreeBSD 10 上设置与获取 TLS（线程局部存储）都要走系统调用，讲者说这套办法从一开始性能就差得惊人，每次访问都得付这笔开销。（YouTube EPyWCMy5EiNkQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
