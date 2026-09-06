---
chapter: 第 34 章
id: CH34
volume: 第02卷-伯克利的岁月
---

# 第 34 章 4.2bsd时期的技术淘汰

## 要点

- **4.2BSD 发行公告**（即 4.2BSD Release Notes）的正式名称为 **"Bug fixes and changes in 4.2BSD"**，由 **Samuel J. Leffler** 编写，文档内部日期为 **1983 年 7 月 28 日**（标题页 `.TL` 行 "July 28, 1983"），文档归属 Computer Systems Research G
- 1983 年同期操作系统展现技术路线分化——4.2BSD（学术多用户网络）、XENIX（商业 UNIX）、PC DOS（PC 单用户）、Lisa（GUI），各自面向不同市场
- 现细节与 RFC 标准文本存在偏差；IETF 于 1989 年 10 月发布 **RFC 1122**《Requirements for Internet Hosts -- Communication Layers》（Editor: R. Braden，URL: <https://www.rfc-editor.org/rfc/rfc1122.txt>，Status: Internet Standard STD 3，Updates: RFC 793，Updated by: RFC 1349、RFC 4379、RFC 5884、RFC 6093、RFC 6298、RFC 6633、RFC 6864、RFC 8029、RFC 9293）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3815] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3921] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3922] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3923] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3924] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3925] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3926] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3927] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3928] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章
- [DB:references_fulltext:chapter_matches:chmatch_3929] 卷“第02卷-伯克利的岁月”第 34 章，匹配置信度 folder，原因：folder 第34章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 4.1BSD 在 TUHS utree 无独立条目，按 0 信任原则须明确标注为“TUHS utree 缺 4.1BSD 独立条目，发行公告以 TUHS Archive 重建版与 CSRG Archive CD-ROM 替代存证”——4.1BSD 的正式发行公告（若存在）在本次核查中未直接获取，仅通过 McKusick 1999 转述与 TUHS Archive 重建版间接确证 4.1BSD 19
- 4.2BSD 网络栈引入后的远程漏洞面在 Morris 蠕虫爆发前已为 BSD 社区知晓但未系统化修补，须区分“已知漏洞”与“系统化修补”——漏洞已知但修补机制缺失是 1980 年代 BSD 社区安全文化的真实状态；**sendmail(8)** DEBUG 命令、**fingerd(8)** 缓冲区溢出、`~/.rhosts` 信任链均为 Morris 蠕虫爆发前 BSD 与 Research
- [考据完成：2026-07-29 经联网考据 RFC 1122 原文与 4.2BSD 源代码交叉验证] 5 项偏差的辨析须注意：(1) 紧急指针口径问题在 RFC 793 原文与 RFC 1122 修正条款之间存在明确冲突，BSD 派生系统长期保留 RFC 793 原始口径是历史包袱而非主动选择；(2) MSL 30 秒虽偏离 RFC 793 建议值但符合 RFC 1122 “实现可配置”的容许条

## 文献

- Leffler, S. J. (1983) "Bug fixes and changes in 4.2BSD", 4.2BSD/usr/doc/uchanges/0.t—1.t, TUHS utree URL: <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/doc/uchanges/0.t>（标题页）与 <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/doc/uchanges/1.t>（Notable improvements）；McKusick, M. K., Bloom, J. M., Karels, M. J. (1986) "Bug Fixes and Changes in 4.3BSD", 4.3BSD/usr/doc/smm/12.uchanges/0.t, TUHS utree URL: <https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD/usr/doc/smm/12.uchanges/0.t>；4BSD/usr/doc/README（URL: <https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD/usr/doc/README>，1980-10-16，314 字节）；TUHS Archive 4.1BSD-19810901-reconstructed（URL: <https://www.tuhs.org/Archive/Distributions/UCB/4.1BSD-19810901-reconstructed/>）；CSRG Archive CD-ROM #1（URL: <http://www.mckusick.com/csrg/>，含 4.1.snap/4.1a/4.1c.1/4.1c.2）；McKusick, K. (1999) "Twenty Years of Berkeley Unix"（O'Reilly Open Sources 第 1 章，记载 4.2BSD 1983.8 发布与 Leffler 收尾工作） ［A］
- Datamation 1983 年市场报告；Salus, P. (1994) "A Quarter Century of UNIX"[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- 4.2BSD Release Notes (1983.8)；4.2BSD 网络源代码；Spafford E H. The Internet Worm Program: An Analysis [R]. Purdue University CSD-TR-823, 1988；CERT/CC CA-1988:01 公告；Bellovin S M. The Internet Worm and the FTP Security Workshop [R]. AT&T Bell Laboratories, 1989；Leffler S J, McKusick M K, Karels M J, Quarterman J S. The Design and Implementation of the 4.3BSD UNIX Operating System [M]. Reading: Addison-Wesley, 1989. ISBN 0-201-06196-1 ［A］## 33.9.3 4.2BSD TCP/IP 实现与 RFC 791/793 标准的具体偏差及 RFC 1122（1989）修正条款
- Postel J. RFC 791: Internet Protocol [EB/OL]. (1981-09)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc791>；Postel J. RFC 793: Transmission Control Protocol [EB/OL]. (1981-09)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc793>；Braden R. RFC 1122: Requirements for Internet Hosts -- Communication Layers [EB/OL]. (1989-10)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc1122>；Jacobson V. Congestion Avoidance and Control [C]//SIGCOMM '88. Stanford: ACM, 1988: 314-329；Larsen M, Gont F. RFC 6093: On the Implementation of the TCP Urgent Mechanism [EB/OL]. (2011-01)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc6093>；Paxson V, Allman M, Chu J, Henderson M. RFC 6298: Computing TCP's Retransmission Timer [EB/OL]. (2011-06)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc6298>；Leffler S J, McKusick M K, Karels M J, Quarterman J S. The Design and Implementation of the 4.3BSD UNIX Operating System [M]. Reading: Addison-Wesley, 1989. ISBN 0-201-06196-1 ［A］[^doubt-resolved-194]: 据 Accetta_Mach-New-Kernel-Foundation (未署名) 消解
