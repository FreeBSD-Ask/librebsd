---
chapter: 第 175 章
id: CH175
volume: 第09卷-netbsd的历史
---

# 第 175 章 NetBSD 1.x 与同时期操作系统的比较

## 要点

- 1993-2004 是 BSD 复兴与 Linux 崛起的重叠期：NetBSD 1.x 以多平台 + 社区治理（NetBSD Foundation 1995）立身，FreeBSD 以 x86 性能 + Ports 领先，OpenBSD 以安全分叉，Linux 以 GPL 社区规模爆发；四者在此期既竞争又互鉴，奠定 2000 年后开源格局。
- OpenSSL 集成引入的加密库漏洞群在 NetBSD 1.x 后期集中显现——NetBSD-SA2001-013（OpenSSL PRNG 实现弱点，熵池初始化不充分导致会话密钥可预测）、NetBSD-SA2002-009（CVE-2002-0655，OpenSSL ASN.1 解析器缓冲区溢出与 SSL v2 弱密钥协商，远程攻击者可利用恶意证书或 SSL 握手触发任意代码执行）、NetBSD-SA2003-017（CVE-2003-0543/0544/0545，OpenSSL ASN.1 解析器三条缺陷路径合并公告）
- netbsd 代码仓库共 1,999,412 次提交（1992-07-13 至 2026-08-24），1,545 位贡献者（contributors 表行数）
- 本节史观审视的史料基础包括三类——其一，NetBSD 官方文档（About、portability、system、history 页面）作为 NetBSD 自我定位的一手史料；其二，NetBSD 1.5/1.6/2.0/5.0 发布公告作为 NetBSD 1.x 时代性能改进与后续重写的代码级证据；其三，项目史观总纲第 13、19、21 条与第 11、19、21 章原文作为史观审视的哲学基础。考据过程与验证留痕详见辨析字段

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3993] 卷“第09卷-netbsd的历史”第 175 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲第 13 条——法律与道德是利益分配：NetBSD 1.x 时期与同时期系统在许可证与治理安排上的竞争，呈现为利益分配框架的选择而非善恶对立
- 总纲第 19 条——解释学循环是历史认识的根本条件：对官方自我表述的解读须置于官方文档与社区叙事的循环中往返核验
- 总纲第 21 条——革命与改革是历史方法论的分歧：OpenBSD 自 NetBSD 分叉与 Linux 崛起的路径差异，呈现渐进改良与断裂重构两种方法论的分野
- 总纲第 8 条——本体论上各方平等：NetBSD、FreeBSD、OpenBSD 与 Linux 在比较框架中并置考察，不以任何一方路线为叙事中心
- 总纲第 9 条——经验优先：比较结论以官方发布公告、安全公告与 netbsd.duckdb commits 表为据，优先采用当事人一手材料

## 辨析

- 将此期视为“BSD vs Linux”零和竞争是误读——代码互鉴（如 VM、网络栈）与社区流动持续发生。
- CVE-2002-0655 在 NVD 中对应 OpenSSL 多漏洞，NetBSD-SA2002-009 将其与 SSL v2 弱密钥协商合并公告，但 NVD 记录的子漏洞编号须逐一核验；CVE-2003-0543/0544/0545 三个 CVE 编号对应 OpenSSL ASN.1 解析器的不同缺陷路径，NetBSD-SA2003-017 将三者合并于同一公告，反映“同组件多漏洞合并公告”的公告模式，合并口径与 NVD 逐条对应关系须对照公告原文核验
- 贡献者高度集中——Top 1 贡献者 wiz 占比 33.4%，需考量‘个人主导’与‘社区协作’的叙事张力
- 考据过程留痕——【查证来源】NetBSD 官方 About、portability、system、history 四个页面经 netbsd.org 一手核验，措辞“Of course it runs NetBSD”“Microoptimizations can play a part in any system, but design is even more important”等已录入 [存疑脚注：第三个以 NetBSD 起句的官方措辞在原稿中截断残缺，未能回源确证，暂不收录]

## 文献

- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-2004 年间：279,901 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数），1993-06-12 至 2026-08-25。
- NetBSD-SA2001-013、NetBSD-SA2002-009、NetBSD-SA2003-017 公告原文；netbsd.duckdb netbsd-src 仓库 itojun OpenSSL commit 记录 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数），1992-07-13 至 2026-08-24。
- NetBSD Project. About NetBSD [EB/OL]. <https://www.netbsd.org/about/>；NetBSD Project. Portability [EB/OL]. <https://www.netbsd.org/about/portability.html>；NetBSD Project. The NetBSD system [EB/OL]. <https://www.netbsd.org/about/system.html>；NetBSD Project. History of the NetBSD Project [EB/OL]. <https://www.netbsd.org/about/history.html>；NetBSD Foundation. NetBSD 1.5 Release Announcement [EB/OL]. 2000-12-06. <https://www.netbsd.org/releases/formal-1.5/NetBSD-1.5.html>；NetBSD Foundation. NetBSD 1.6 Release Announcement [EB/OL]. 2002-09-14. <https://www.netbsd.org/releases/formal-1.6/NetBSD-1.6.html>；NetBSD Foundation. NetBSD 2.0 Release Announcement [EB/OL]. 2004-12-09. <https://www.netbsd.org/releases/formal-2.0/NetBSD-2.0.html>；NetBSD Foundation. NetBSD 5.0 Release Announcement [EB/OL]. 2009-04-29. <https://www.netbsd.org/releases/formal-5/NetBSD-5.0.html>；**sacred_sources.duckdb**（项目统摄史观原文已入库：第 11 章——法哲学与政治历史哲学；第 19 章——历史解释学与权力；第 21 章——革命与改革：历史方法论；第 25 章——总纲第 13、19、21 条） ［A］<!-- foundation-writeback: NetBSD Foundation | NetBSD Foundation 执行委员会 -->**NetBSD Foundation 史料**（NetBSD Foundation 执行委员会，下载日期 2026-07-26）：[存疑脚注：本回写块内容缺失，执行委员会史料待回源补全]
