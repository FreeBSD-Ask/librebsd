---
chapter: 第 22 章
id: CH22
volume: 第01卷-unix的起源
---

# 第 22 章 编程语言史

## 要点

C语言的诞生（1972年，Dennis Ritchie）与UNIX的共生关系构成了BSD史的技术语法基础：C语言为UNIX从汇编向高级语言移植提供了工具，UNIX则为C语言提供了实际验证场域。Fortran、ALGOL 60、CPL、BCPL、B等语言构成了C语言的谱系前身，而C++、Objective-C、Go等语言则是C的后继分支。BSD系统自身的工具链（cc、make、lex/yacc）与脚本语言（sh、awk、sed、perl）共同塑造了UNIX"小工具组合"的编程文化，这一文化在BSD社区中持续至今。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3598] 卷“第01卷-unix的起源”第 22 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3601] 卷“第01卷-unix的起源”第 22 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3632] 卷“第01卷-unix的起源”第 22 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1538] 卷“第01卷-unix的起源”第 22 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第6条——动手者创造历史：C语言是Ritchie为满足系统编程的实际需求而创造的，而非学院派语言设计的产物，其"信任程序员"的设计哲学体现了"没有多余形式主义的老实人"精神。总纲第9条——经验优先：C语言的成功源于其在UNIX内核与工具移植中的实用性验证，而非理论完备性——其类型系统的宽松与指针的自由度，在实践中被证明是系统编程不可或缺的灵活性来源。总纲第3条——偶然性优先：C语言成为"系统编程的通用语"并非必然，ALGOL 68的过度复杂、Pascal的过度约束、PL/I的过度庞大，都构成了C语言胜出的偶然条件。

## 辨析

C语言的设计哲学（信任程序员、不隐藏底层细节）既是其灵活性的来源，也是缓冲区溢出等安全漏洞的根源。BSD社区对lint、bounds-checking等静态分析工具的早期采纳，构成了对C语言固有风险的工程化应对。将C语言等同于"不安全语言"的当代批评需要放置于历史语境中理解：1970年代的内存与CPU资源约束使得运行时检查的成本不可接受。BSD向Rust等内存安全语言的渐进迁移（如FreeBSD对Rust的探索性引入）构成了对C语言遗产的辩证继承。

## 文献

（待补：Ritchie D M. The Development of the C Language[C]//HOPL-II. ACM, 1993；Kernighan B W, Ritchie D M. The C Programming Language[M]. 2nd ed. Prentice Hall, 1988；Bergin T J, Gibson R G. History of Programming Languages II[M]. ACM Press/Addison-Wesley, 1996；[DB:references_fulltext:chapter_matches:chmatch_3598]；[DB:references_fulltext:chapter_matches:chmatch_1538]）
