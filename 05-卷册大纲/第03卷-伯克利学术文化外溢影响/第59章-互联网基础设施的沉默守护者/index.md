---
chapter: 第 59 章
id: CH59
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 59 章 互联网基础设施的沉默守护者

## 要点

- BIND（Berkeley Internet Name Domain，伯克利 CSRG 四名研究生 Terry/Painter/Riggle/Zhou 1984 年开发，DNS 协议 RFC 882/883 1983 年 11 月标准化）与 Sendmail（1983 年随 4.2BSD 正式发布）长期主导互联网 DNS 与邮件传输市场，但 1990 年代后期两者均面临严重安全挑战——BIND 4
- BSD 作为互联网沉默支柱的辨析：（1）BSD 的 BIND/Sendmail/TCP/IP 在 1980-1990 年代是互联网基础设施核心，但 BSD 系统的市场份额在 1990 年代后期被 Linux 超越；（2）BSD 的 “沉默” 源于其许可证宽松（无需署名）与基础设施性质（用户不直接接触）；（3）BSD 作为沉默支柱的具体辨析基于实际部署数据——BIND 1990 年代约 90% DN
- 互联网基础设施边缘贡献者的史料辨析：（1）BSD 源码贡献者记录（CHANGELOG、SCCS 日志）是辨识边缘贡献者的主要史料，但 CSRG 时期（1978-1992）记录不完整，4.4BSD-Lite 之后的 CVS/SVN/Git 记录较完整；（2）邮件列表存档（如 IETF 邮件列表、CSRG 内部邮件）可补充源码记录，但存档可能存在截取、邮件丢失、事后编辑，须通过多个独立存档交叉验证；（

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1548] 卷“第03卷-伯克利学术文化外溢影响”第 59 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- BIND/Sendmail 被 “淘汰” 指主导地位被多元替代方案挑战，而非完全弃用——BIND 9 与 Sendmail 在 BSD 与 Linux 中仍保留一定份额，须区分 “主导地位退场” 与 “完全弃用”；Dan Kaminsky 2008 年漏洞（CERT VU#800113）是 DNS 协议设计层缺陷（事务 ID 仅 16 位 + 源端口固定），影响所有未实现源端口随机化的 DNS 实
- BSD/Linux 市场份额演变——Netcraft 统计显示 1990 年代后期起 Linux Web 服务器部署份额逐步超越 BSD 系统的部署份额（定性趋势确认，定量数据保留 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]）；Linux 借鉴 BSD 代码的具体案例——Linux NET-2 借鉴 BSD 网络代码（含 BSD 版权声明，与 23.
- 源码贡献者记录的完整性——BSD 源码 CHANGELOG 与 SCCS 日志为辨识边缘贡献者的主要史料，但早期（CSRG 时期 1978-1992）记录不完整，4.4BSD-Lite 之后的 CVS/SVN/Git 记录较完整；邮件列表存档的截取情况——IETF 邮件列表与 CSRG 内部邮件存档可能存在截取、邮件丢失、事后编辑，须通过多个独立存档（如 marc.info、ietf.org 邮件

## 文献

- BIND/Sendmail 漏洞公告；BIND 9 发布记录；PowerDNS/Unbound/Postfix/qmail 发布记录；Dan Kaminsky 2008 DNS 漏洞披露；CVE 数据库[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- BSD/Linux 市场份额数据（Netcraft）；Linux 代码档案；Apache 档案；McKusick (1999) "Twenty Years of Berkeley Unix" ［A］### 史观映射> 互联网不是从硅谷的车库里诞生的，而是从伯克利的终端室里长出来的。BIND 让全球的域名得以解析，Sendmail 让全球的邮件得以送达，BSD TCP/IP 栈让全球的数据包得以路由——这些技术构成了互联网的神经系统，但写下它们的人从未出现在任何互联网创业的封面上。ARPANET 到 NSFNET 的二十年是互联网从军事实验到学术骨干再到公共基础设施的转型期，而 BSD 系统恰好站在了每一个转折点上——不是作为主角，而是作为那个沉默的、在后台运转的操作系统。当 IETF 说 "rough consensus and running code" 时，他们说的其实就是 BSD 的工程哲学：先跑起来，再谈标准。当万维网从 CERN 传遍全球时，跑着 Apache 的 BSD 服务器已经在为第一批网站提供服务——但它们从未被看见，因为真正的互联网基础设施本就不该被看见---## 第 23.12 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 23.13 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）
- BSD 源码 CHANGELOG/SCCS 日志；IETF/CSRG 邮件列表存档；Allman/Vixie 回忆录；0 信任原则方法论 ［A］
