---
chapter: 第 57 章
id: CH57
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 57 章 arpanet到nsfnet的前bsd时代

## 要点

- 互联网前 BSD 时代（1969-1983）的协议生态包括：（1）NCP（Network Control Program，ARPANET 1971-1983 使用）；（2）X.25（CCITT 1976 标准的分组交换协议，用于 Tymnet、Telenet 等公共网络）；（3）SNA（IBM 1974 发布的系统网络架构）；（4）DECnet（DEC 1975 发布的网络架构）；（5）UUCP（
- BSD 开发者参与 IETF 的关键事件包括：（1）Joy 与 Leffler 的 4.2BSD TCP/IP 实现影响 IETF TCP/IP 标准化；（2）Paul Mockapetris（ISI）的 DNS 设计（RFC 882/883 1983）由伯克利四研究生实现为 BIND；（3）Jonathan Postel（USC ISI，RFC 编辑）与 CSRG 的合作；（4）Allman 的
- BIND 的全球统治：1990 年代 BIND 运行全球约 90% 的 DNS 服务器，BIND 的统治地位带来安全责任，BIND 安全漏洞史包括：（1）BIND 4.9.x 1990 年代后期多个远程漏洞；（2）BIND 8.2.x 1999 年 NXT 记录等多个漏洞（CERT Advisory CA-1999-14）；（3）BIND 9 的多次 CVE；BIND 的安全问题推动替代品（Pow
- Sendmail 的替代品：（1）Qmail 1995 年由 D. J. Bernstein 发布，强调安全性，Qmail 的安全设计（最小特权、沙箱）使 Sendmail 安全问题凸显，许可证：公有领域（Bernstein 本人于 cr.yp.to/qmail/dist.html 声明将 qmail 置于公有领域）[考据脚注：经 cr.yp.to/qmail/dist.html 一手来源确证。]

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3817] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3818] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3820] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3821] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3976] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3977] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 folder，原因：folder 第56章
- [DB:references_fulltext:chapter_matches:chmatch_3621] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3622] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3651] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3663] 卷“第03卷-伯克利学术文化外溢影响”第 57 章，匹配置信度 curated，原因：curated token rule

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NCP（Network Control Program）使用时间确认为 1971-1983 年（ARPANET 主机间通信协议，由 BBN 的 Steve Crocker 团队设计，1983.1.1 ARPANET 切换至 TCP/IP 后弃用）；X.25 为 CCITT 1976 年标准的分组交换协议（用于 Tymnet、Telenet 等公共数据网络，多源一致）；SNA（Systems Net
- Mockapetris DNS RFC 882/883 发布时间确认为 1983 年 11 月（RFC 882"Domain Names: Concepts and Facilities"与 RFC 883"Domain Names: Implementation and Specification"，作者 Paul Mockapetris，USC ISI）；SMTP RFC 821 发布时间确认
- BIND 1990 年代市场份额（约 90%）——多源引用但缺乏权威统计来源（Netcraft 等统计机构 1990 年代后期的 DNS 服务器市场份额数据保留 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]）；BIND 4.9.x 具体漏洞时间与版本——CERT/CC 安全公告档案为权威来源，具体漏洞编号与版本须以 CERT/CC 公告为准；BIND
- Qmail 发布时间确认为 1995 年（Daniel J. Bernstein 发布，强调安全性，许可证为公有领域——Bernstein 本人于 cr.yp.to/qmail/dist.html 声明将 qmail 置于公有领域）；Postfix 发布时间确认为 1998 年（原名 VMailer，IBM T.J. Watson 研究中心 Wietse Venema 开发，使用 IBM Publ

## 文献

- NCP 协议文档；CCITT X.25（1976）；IBM SNA 文档；DEC DECnet 文档；Lesk, M. (1978) UUCP[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- RFC 882/883（1983）；RFC 821（1982）；Mockapetris DNS 档案；Postel 与 CSRG 合作档案[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- BIND 安全漏洞档案；CVE 数据库；PowerDNS/Unbound/NSD 项目档案[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Bernstein, D. J. Qmail 档案；Venema, W. Postfix 档案；Hazel, P. Exim 档案；Sendmail 市场份额演变数据[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证][^doubt-resolved-121]: 据 en (1994) 消解
