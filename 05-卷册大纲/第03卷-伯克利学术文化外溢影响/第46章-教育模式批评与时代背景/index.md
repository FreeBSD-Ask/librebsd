---
chapter: 第 46 章
id: CH46
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 46 章 教育模式批评与时代背景

## 要点

- CSRG 精英化与伯克利 1960-1980 年代左派教育语境的交叠呈现三重结构：（一）选拔机制的交叠——CSRG **1976 年** 正式成立时伯克利 EECS 系正处于后 FSM 时代的 “学术左派” 兴起阶段，CSRG 沿用 Fabry/McKusick 个人推荐加学术成绩的选拔机制，与伯克利左派学者圈子（如 Critical Legal Studies 运动、Feminist Scholars 团体，见文献行 Freeman 等条目）形成时代交叠
- 边缘贡献者的史料辨析包括：（1）BSD 源码贡献者记录（如 `CHANGELOG`、SCCS 日志）是辨识边缘贡献者的主要史料，但须注意记录的不完整性；（2）邮件列表存档（如 CSRG 内部邮件）可补充源码记录，但须注意存档的截取；（3）事后回忆（如 McKusick **1999 年** 文章）须警惕记忆偏差与自利偏差；（4）史料辨析须遵循 0 信任原则，对所有来源进行考据验证〔注：条目原以悬空表头片段「| 史料类型」结尾，系生成残片已删〕


- 1978-1992 年基础科学与计算机科学发展——Cook/Karp 的 NP 完全性理论、RSA 公钥密码学、Lamport 分布式系统理论、Codd 关系数据库理论；这些理论发展直接影响 BSD 的 TCP/IP 实现、密码学应用与数据库系统

| 理论 | 作者 | 时间 | 发表场所 | 对 BSD 影响 |
| --- | --- | --- | --- | --- |
| NP 完全性 | Cook；Karp | 1971；1972 | STOC '71；Miller & Thatcher 论文集 | 算法复杂度方法论背景 |
| 公钥密码学 | Rivest、Shamir、Adleman（Diffie 与 Hellman 1976 奠基） | 1978（1976） | CACM 21(2)（IEEE Trans. IT） | BSD 密码学应用的理论基础 |
| 分布式系统理论 | Lamport | 1978 | CACM | 分布式与并发设计思想 |
| 关系数据库理论 | Codd | 1970 | CACM | 数据库系统理论背景 |
| TCP/IP 协议理论 | Cerf 与 Kahn | 1974 | IEEE Trans. Comm. 22(5) | BSD TCP/IP 实现的直接基础 |


- 1978-1992 基础科学发展包括：（1）计算复杂度理论，Cook 1971 年证明 NP 完全性（“The Complexity of Theorem-Proving Procedures”），Karp 1972 年扩展 NP 完全问题类（“Reducibility Among Combinatorial Problems”）；（2）公钥密码学，Diffie 与 Hellman 1976 年提出公钥思想（“New Directions in Cryptography”，IEEE Trans. IT），Rivest、Shamir、Adleman 1978 年提出 RSA（CACM 21(2)）；（3）分布式系统理论，Lamport 1978 年在 CACM 发表分布式互斥与时序时钟研究；（4）关系数据库理论，Codd 1970 年在 CACM 提出关系模型
- 1978-1992 计算机科学发展包括：（1）TCP/IP 协议理论，Cerf 与 Kahn 1974 年发表 “A Protocol for Packet Network Intercommunication”（IEEE Trans. Comm.），奠定 TCP/IP 基础；（2）编程语言与系统，Stroustrup 1985 年发布 C++、Cox 1984 年发布 Objective-C（详见文献行）；（3）并发理论，Hoare 1978 年提出 CSP、Milner 1980 年提出 CCS

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3614] 卷“第03卷-伯克利学术文化外溢影响”第 46 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_4176] 卷“第03卷-伯克利学术文化外溢影响”第 46 章，匹配置信度 1.0，原因：4.3BSD 发布工程

## 史观

- 总纲第 15 条——文化即形式主义：CSRG 的选拔机制与伯克利左派教育语境的交叠，是学术文化形式对工程社群的塑造
- 总纲第 19 条——解释学循环是历史认识的根本条件：边缘贡献者辨析须警惕事后建构与记忆偏差，前理解差异决定史料取舍
- 总纲第 5 条——没有必然性，只有偶然性：Joy、McKusick 等核心成员与伯克利及 CSRG 的汇合属个体选择的偶然叠加
- 总纲第 2 条——历史是形式主义化的非存在：本章对教育模式与理论背景的梳理本身是形式主义化的重构
（编排说明：章级聚合随正文阶段逐章完成，子节级映射详见各节史观字段——2026-09-11 整改注）

## 辨析

- CSRG 与伯克利左派传统的 “交叠” 程度须严格考据——CSRG 核心成员 Joy（1975 年入伯克利）、McKusick（1976 年入伯克利研究生）、Karels、Bostic 等均晚于 FSM（1964）与人民公园（1969），其 “亲历” 程度须核对成员本人自述，避免事后建构；交叠程度的判定须以 CSRG 成员本人同期记录为据，而非以时代氛围作宏观归因
- 源码贡献者记录的完整性需核对；邮件列表存档的截取情况需核对；事后回忆的记忆偏差需核对；0 信任原则的适用性需核对
- Cook 1971、Karp 1972、RSA 1978、Lamport 1978、Codd 1970 等理论的发表时间与刊物考据详见 22.20.13.1 辨析〔跨章小节引用待验〕；各理论与 BSD 实现的具体关联为史家阐释而非当事人自述——RSA 理论（1978）在 BSD 中的应用（SSH、SSL/TLS、IPsec）属 CSRG 解散（1995）前后及之后的后续发展〔注：句尾原文截断，按年代语境收束〕
- Cook 1971、Karp 1972、DES 1977、RSA 1978、Lamport 1978、Codd 1970 等论文的发表时间、刊物与卷期页码详见 22.20.13 表格；Cook 论文发表于 STOC '71（1971.5.3-5，Shaker Heights, Ohio）；Karp 论文后收入 Miller & Thatcher (1972) 论文集，扩展 NP 完全问题类至 21
- Cerf/Kahn 1974 论文发表于 IEEE Trans. Comm. 22(5)（1974.5），奠定 TCP/IP 协议基础；C++ 与 Objective-C 的发布时间考据详见 22.20.8 辨析〔跨章小节引用待验〕，其与 BSD 的关联属同期技术生态背景而非直接承继

## 文献

- McKusick, M. K. (1999) Twenty Years of Berkeley Unix // FreeBSD 官方网站；UC Berkeley Bancroft Library. CU-551 CSRG Records, 1974-2005；UC Berkeley Bancroft Library. Free Speech Movement Archives；Savio, M. Papers. San Francisco State University, Labor Archives & Research Center；Rorabaugh, W. J. (1989) Berkeley at War: The 1960s. New York: Oxford University Press；Cohen, R., & Zelnik, R. E. (2002) The Free Speech Movement: Reflections on Berkeley in the 1960s. Berkeley: University of California Press；Freeman, J. (1970) The Tyranny of Structurelessness // The Second Wave, 2(1): 2-11；Freeman, J. (2004) At Berkeley in the Sixties. Bloomington: Indiana University Press；UC Berkeley School of Law. Critical Legal Studies Archive；UC Berkeley, Department of Gender and Women's Studies Records ［B］
- BSD 源码 CHANGELOG/SCCS 日志；CSRG 邮件列表存档；McKusick (1999) “Twenty Years of Berkeley Unix”；0 信任原则方法论 ［A］
- Cook 1971 STOC；Karp 1972 “Reducibility Among Combinatorial Problems”；RSA 1978 CACM；Lamport 1978 CACM；Codd 1970 CACM ［B］
- Cook, S. (1971) “The Complexity of Theorem-Proving Procedures”, STOC；Karp, R. (1972) “Reducibility Among Combinatorial Problems”；FIPS PUB 46（1977）；Rivest, R., Shamir, A., Adleman, L. (1978) CACM；Lamport, L. (1978) CACM；Codd, E. (1970) CACM ［B］
- Cerf, V. & Kahn, R. (1974) IEEE Trans. Comm.；Stroustrup, B. (1985) “The C++ Programming Language”；Cox, B. (1984) Objective-C；Tanenbaum-Torvalds 1992 usenet 争论档案；Hoare, C. (1978) CSP；Milner, R. (1980) CCS［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- RSA 1978 CACM；DES FIPS PUB 46；Diffie-Hellman 1976 IEEE IT；PGP 1991 发布档案 ［B］
- Rivest, R., Shamir, A., Adleman, L. (1978) CACM 21(2)；US Patent 4,405,829（1983）；FIPS PUB 46（1977）；Diffie, W. & Hellman, M. (1976) IEEE Trans. IT；Zimmermann, P. (1991) PGP ［B］
- Koblitz, N. (1985) “Elliptic Curve Cryptosystems”, Math. Comp.；Miller, V. (1985) “Use of Elliptic Curves in Cryptography”, CRYPTO；Shamir, A. (1979) Comm. ACM；Rabin, M. (1979) MIT LCS ［B］
- Morris 蠕虫档案；CERT/CC 建立档案；Stoll, C. (1989) “The Cuckoo's Egg”；Computer Fraud and Abuse Act（1986）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Morris 蠕虫漏洞分析；4.3BSD-Reno/4.4BSD 安全审计档案；Morris, R. & Thompson, K. (1979) “Password Security: A Case History”；BSD Kerberos 集成档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- dangan-20260908 消解回写 -->
- Leslie. The Cold War and American Science[Z]. 1993. ［DKC-1304→fulltext:5860］
<!-- /dangan-20260908 -->
