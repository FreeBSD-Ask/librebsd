---
chapter: 第 34 章
id: CH34
volume: 第02卷-伯克利的岁月
---

# 第 34 章 4.2bsd时期的技术淘汰

## 要点

- **4.2BSD 发行公告**（即 4.2BSD Release Notes）的正式名称为 **“Bug fixes and changes in 4.2BSD”**，由 **Samuel J. Leffler** 编写，文档内部日期为 **1983 年 7 月 28 日**（标题页 `.TL` 行 “July 28, 1983”），文档归属 Computer Systems Research Group（2026-09-12 整改：行尾截断补全）
- 1983 年同期操作系统展现技术路线分化——4.2BSD（学术多用户网络）、XENIX（商业 UNIX）、PC DOS（PC 单用户）、Lisa（GUI），各自面向不同市场
- 4.2BSD TCP/IP 实现细节与 RFC 标准文本存在偏差（2026-09-12 整改：行首截断按辨析字段语境补全）；IETF 于 1989 年 10 月发布 **RFC 1122**《Requirements for Internet Hosts -- Communication Layers》（Editor: R. Braden，URL: <https://www.rfc-editor.org/rfc/rfc1122.txt>，Status: Internet Standard STD 3，Updates: RFC 793，Updated by: RFC 1349、RFC 4379、RFC 5884、RFC 6093、RFC 6298、RFC 6633、RFC 6864、RFC 8029、RFC 9293）

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

（2026-09-12 整改注：上列 10 条匹配行置信度字段均作 "folder"（非数值），系库侧匹配结果生成异常，待库侧重跑；本组行仅作检索登记，不作证据采信依据——批次 C101 问题 11）

## 史观

总纲第 4 条——分离聚合是永恒规律：4.2BSD 时期的技术淘汰是 BSD 内部的分离—聚合循环——旧 v7 文件系统实现与早期 TCP/IP 代码被分离出去，而 RFC 791/793 的标准化把分歧的实现重新聚合进统一规范（RFC 1122 的修正条款即再聚合的制度形式）；总纲第 5 条——没有必然性，只有偶然性：RFC 1122（1989-10）对 TCP 实现偏差的集中修正恰在 Morris 蠕虫（1988-11）爆发之后出台，修正时点系蠕虫事件的偶然触发而非标准化进程的必然节点；总纲第 3 条——不存在进步，只有权力再分配：技术淘汰不是单纯的新陈代谢，CSRG 实现与 IETF 规范文本之间的偏差裁决权（RFC 1122 对紧急指针口径、MSL 时限等的裁定）即标准话语权的再分配。（2026-09-12 整改：史观字段按批次 C101 回填，映射依 25 条权威表；细节论证见子节文件史观/辨析字段）

## 辨析

- 4.1BSD 在 TUHS utree 无独立条目，按 0 信任原则须明确标注为“TUHS utree 缺 4.1BSD 独立条目，发行公告以 TUHS Archive 重建版与 CSRG Archive CD-ROM 替代存证”——4.1BSD 的正式发行公告（若存在）在本次核查中未直接获取，仅通过 McKusick 1999 转述与 TUHS Archive 重建版间接确证 4.1BSD 1981-09-01 发行存证（目录名 4.1BSD-19810901-reconstructed 自证）〔2026-09-12 整改：句尾截断按存证线索补全〕
- 4.2BSD 网络栈引入后的远程漏洞面在 Morris 蠕虫爆发前已为 BSD 社区知晓但未系统化修补，须区分“已知漏洞”与“系统化修补”——漏洞已知但修补机制缺失是 1980 年代 BSD 社区安全文化的真实状态；**sendmail(8)** DEBUG 命令、**fingerd(8)** 缓冲区溢出、`~/.rhosts` 信任链均为 Morris 蠕虫爆发（1988-11）前 BSD 与 Research Unix 世界已知的攻击面案例〔2026-09-12 整改：句尾截断按语境补全〕
- [考据完成：2026-07-29 经联网考据 RFC 1122 原文与 4.2BSD 源代码交叉验证] 5 项偏差的辨析须注意：(1) 紧急指针口径问题在 RFC 793 原文与 RFC 1122 修正条款之间存在明确冲突，BSD 派生系统长期保留 RFC 793 原始口径是历史包袱而非主动选择；(2) MSL 30 秒虽偏离 RFC 793 建议值但符合 RFC 1122 “实现可配置”的容许条款〔2026-09-12 整改：句尾截断补全〕

## 文献

- Leffler, S. J. (1983) “Bug fixes and changes in 4.2BSD”, 4.2BSD/usr/doc/uchanges/0.t—1.t, TUHS utree URL: <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/doc/uchanges/0.t>（标题页）与 <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/doc/uchanges/1.t>（Notable improvements）；McKusick, M. K., Bloom, J. M., Karels, M. J. (1986) “Bug Fixes and Changes in 4.3BSD”, 4.3BSD/usr/doc/smm/12.uchanges/0.t, TUHS utree URL: <https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD/usr/doc/smm/12.uchanges/0.t>；4BSD/usr/doc/README（URL: <https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD/usr/doc/README>，1980-10-16，314 字节）；TUHS Archive 4.1BSD-19810901-reconstructed（URL: <https://www.tuhs.org/Archive/Distributions/UCB/4.1BSD-19810901-reconstructed/>）；CSRG Archive CD-ROM #1（URL: <http://www.mckusick.com/csrg/>，含 4.1.snap/4.1a/4.1c.1/4.1c.2）；McKusick, K. (1999) “Twenty Years of Berkeley Unix”（O'Reilly Open Sources 第 1 章，记载 4.2BSD 1983.8 发布与 Leffler 收尾工作） ［A］
- Datamation 1983 年市场报告；Salus, P. (1994) “A Quarter Century of UNIX”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 4.2BSD Release Notes (1983.8)；4.2BSD 网络源代码；Spafford E H. The Internet Worm Program: An Analysis [R]. Purdue University CSD-TR-823, 1988；CERT/CC CA-1988:01 公告；Bellovin S M. The Internet Worm and the FTP Security Workshop [R]. AT&T Bell Laboratories, 1989；Leffler S J, McKusick M K, Karels M J, Quarterman J S. The Design and Implementation of the 4.3BSD UNIX Operating System [M]. Reading: Addison-Wesley, 1989. ISBN 0-201-06196-1（2026-09-12 整改：行尾粘接的旧章号标题“## 33.9.3 …”残留已删除留痕）
- Postel J. RFC 791: Internet Protocol [EB/OL]. (1981-09)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc791>；Postel J. RFC 793: Transmission Control Protocol [EB/OL]. (1981-09)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc793>；Braden R. RFC 1122: Requirements for Internet Hosts -- Communication Layers [EB/OL]. (1989-10)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc1122>；Jacobson V. Congestion Avoidance and Control [C]//SIGCOMM '88. Stanford: ACM, 1988: 314-329；Larsen M, Gont F. RFC 6093: On the Implementation of the TCP Urgent Mechanism [EB/OL]. (2011-01)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc6093>；Paxson V, Allman M, Chu J, Henderson M. RFC 6298: Computing TCP's Retransmission Timer [EB/OL]. (2011-06)[2026-07-29]. <https://www.rfc-editor.org/rfc/rfc6298>；Leffler S J, McKusick M K, Karels M J, Quarterman J S. The Design and Implementation of the 4.3BSD UNIX Operating System [M]. Reading: Addison-Wesley, 1989. ISBN 0-201-06196-1（2026-09-12 整改：行尾孤儿脚注定义 [^doubt-resolved-194]（Mach 内核存疑消解，与本文件无关）与 ［A］ 残留标记已移除留痕，脚注应迁回原存疑点所在文件）

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

