---
chapter: 第 33 章
id: CH33
volume: 第02卷-伯克利的岁月
---

# 第 33 章 4.2BSD 革命与三件套

## 要点

- 4.2BSD 引入的 socket API 由 Bill Joy 与 Sam Leffler 共同设计（BSD 端 socket 层作者与 TCP/IP 协议栈作者一致，McKusick 1999 记载 Joy 1981 年夏实现 IPC 原型、Leffler 后续完善），socket 作为 IPC 与网络通信的统一抽象支持 TCP/UDP/UNIX 域等多种协议族（AF_INET、AF_UNIX 等）〔2026-09-12 整改：截断补全并闭合括号——批次 B050 问题 2〕
- Joy 离开后 CSRG 失去核心开发者，Leffler、Karels、McKusick 接手 4.2BSD 完成工作，CSRG 从个人依赖转向团队化
- BSD daemon 成为 BSD 社区的文化符号，出现在手册、T 恤、会议海报等载体，与 Linux 的 Tux 企鹅形成文化对比
- Bill Joy 于 1982 年离开 Berkeley 加入 Sun Microsystems，将 4.2BSD 的集成工作移交给 Leffler 与 McKusick。这一交接是 BSD 历史上第一次核心开发者代际更替。
- 对 4.2BSD 的批评主要集中在发布后至 4.3BSD 发布前（1983.8-1986.6）约两年半时间，绝大多数性能问题在 4.3BSD 中得到解决；后续对“4.2BSD 过度膨胀”的叙事多为回溯性建构，需与当事人一手记载区分；4.2BSD 商业上极其成功——18 个月内颁发超过 1,000 份站点许可证，超过先前所有 BSD 版本总和，绝大多数 UNIX 厂商选择搭载 4.2BSD 而非 AT&T System V 原生版本〔2026-09-12 整改：截断按 33.5.4 语境补全——批次 B050 问题 3〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3716] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3717] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3718] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3725] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3727] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3816] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3883] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3886] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3944] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:references_fulltext:chapter_matches:chmatch_3947] 卷“第02卷-伯克利的岁月”第 33 章，匹配置信度 folder，原因：folder 第33章
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 33.7-关键词行级挖掘素材线索（2 条，CL-RM 段，见 33.7-关键词行级挖掘素材线索.md）

## 史观

总纲第 4 条——分离聚合是永恒规律：socket API 将网络与 IPC 聚合为统一抽象（AF_INET/AF_UNIX 多协议族），随后随 BSD 扩散聚合入各厂商系统；总纲第 10 条——动手者创造历史：socket 层由 Joy 与 Leffler 亲手设计实现（McKusick 1999 当事人记载），Joy 离开后的集成由 Leffler/Karels/McKusick 接续完成；总纲第 3 条——不存在进步，只有权力再分配：Joy 离开使 CSRG 从个人依赖转向团队化，是开发权的组织化再分配；总纲第 15 条——文化即形式主义：BSD daemon 作为文化符号在手册、T 恤、海报上的传播是社区文化的形式主义化承载；总纲第 5 条——没有必然性，只有偶然性：4.2BSD 的商业成功（18 个月 1000+ 许可证）系厂商选择与时机等偶然条件的聚合，非“革命”叙事的必然结果。（2026-09-12 整改：史观字段按批次 B050 回填，映射依 25 条权威表）

## 辨析

- socket IPC 的抽象与 NS 协议栈有结构相似性（2026-09-12 整改：句首主语补全——批次 B050 问题 6）；socket API 作者为 Joy 与 Leffler 共同设计，“由 Joy 设计”的不完整表述应改为“由 Joy 与 Leffler 共同设计”（McKusick 1999 记载 Joy 实现原型、Leffler 与 Joy 共同完善）
- CSRG 重组的具体过程在不同史料中描述详略不一，需核对内部备忘录
- daemon 与 Tux 的文化对比需谨慎，避免简化为 BSD vs Linux 的对立
- Bill Joy 1982 年离开 Berkeley 加入 Sun Microsystems 的时间节点需辨析——部分文献将 Joy 的离开记为 1982 年夏（完成 4.2BSD 集成前）或 1983 年（4.2BSD 发布后），“将集成工作移交给 Leffler 与 McKusick”的具体交接范围在不同叙事中有差异；此次交接是否构成“第一次核心开发者代际更替”，亦取决于对 1BSD→2BSD 时期人员变动的界定（2026-09-12 整改：截断按 33.4.2 语境补全——批次 B050 问题 4）
- 4.2BSD 的“革命性”地位不是事后赋予，而是由市场选择（1000+ 份许可证、厂商首选）确立的；性能问题真实存在但在后续版本中系统解决，这是研究型软件发布的正常工程周期

## 文献

- Leffler, S. J., Fabry, R. S., Joy, W. N., Lapsley, P., Miller, S. (1983) “4.2BSD Networking Implementation Notes”, SRI International CSRG, University of California, Berkeley（第 6.1 节“Socket layer”）；McKusick, K. (1999) “Twenty Years of Berkeley Unix”（Open Sources 第 1 章）；Stevens, W. R. (1990) “UNIX Network Programming”, Prentice Hall, ISBN 0-13-949876-1（经多源交叉验证：Open Library 书目记录（OL2203754M）明确记载 1990 年 UNIX Network Programming ISBN 0-139-49876-1，与多个引文一致，（消解说明 2026-09-12 整改：原“据一手文献印证消解^doubt-resolved-193…］已解除”破碎记录改写为通顺表述——Stevens 1990 ISBN 经 Open Library OL2203754M 与多源引文交叉验证通过，消解有效——批次 B050 问题 7））；CSRG (1983) “4.2BSD Unix Programmer's Manual”
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”；CSRG 内部档案 ［B］
- BSD conferences 历年海报档案；Raymond, E. S. (1996) “The New Hacker's Dictionary” ［B］
- McKusick 1999; Salus 1994 ［B］
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”；Salus, P. H. (1994) “A Quarter Century of UNIX”, Addison-Wesley, ISBN 0-201-54777-5；Leffler et al. (1989) 4.3BSD 设计书（ISBN 0-201-06196-1）；CSRG 发行统计 ［B］
- USENIX 会议论文集（1983-1985）；伯克利 CSRG 邮件列表存档 ［A］（2026-09-12 整改：行内拼接的脚注定义 [^doubt-resolved-193]“据 Handbook (未署名) 消解”删除留痕——该定义系幻觉来源（Handbook 无文献可指）且无正文引用点，Stevens 1990 的 ISBN 消解已由 Open Library 佐证独立成立——批次 B050 问题 8）

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

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-222 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-222`；w172 YouTube 章节路由采纳）

据〔BSD 快文件系统简史演讲〕讲者口述：快文件系统于 2003 年加入多 TB 容量支持，这一改动即形成 UFS2。（YouTube EP1BbMBdGPoHM，[3244.6-3250.51]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-997 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-997`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Kirk McKusick 口述：讲者将 BSD Fast Filesystem 的起点置于约 1982 年。（YouTube EPuF_J-itJDwM，[34.989-39.329]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2172 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2172`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A Brief History of the BSD Fast Filesystem, Kirk McKusick 演讲〕讲者口述：伯克利快文件系统（FFS）诞生于 1982 年，创意出自时任伯克利项目主持人的 Bill Joy；讲者自述自己因暑期需要一笔额外收入被 Joy 拉到一边，Joy 提议付其当暑薪资、请他为自己的文件系统构想做出原型。（YouTube EPtzieR5MM06M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2173 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2173`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A Brief History of the BSD Fast Filesystem, Kirk McKusick 演讲〕讲者口述：FFS 的基本构思是混合块大小：大文件用大块、小文件用小碎片；首次部署时大块为 1 千字节、小块为 512，分配方式从原先的自由链表改为位图（bitmap），以便在已分配块附近查找相邻块。（YouTube EPtzieR5MM06M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2174 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2174`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A Brief History of the BSD Fast Filesystem, Kirk McKusick 演讲〕讲者口述：面对崩溃后 fsck 需半小时至一个半小时的问题，在 ext3 与 Solaris 版 UFS 所采的日志式（journaling）之外，BSD 选择另一种方案软更新（soft updates）：不写日志，而维持一组导入数据结构跟踪文件系统状态，确保写入顺序使文件系统始终保持正确，虽可落后至多约两分钟，但从不处于不可直接使用的状态。（YouTube EPtzieR5MM06M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2175 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2175`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔A Brief History of the BSD Fast Filesystem, Kirk McKusick 演讲〕讲者口述：伯克利引入文件系统状态（fs_stat）层叠概念：多个文件系统可按层插件式挂载，不再把全部功能放在单一模块内，可分模块构建，且仅在实际使用该模块时才付出其开销；讲者举例以不支持操作的空实现置于底层，其上放 UFS，导出时再叠加 NFS 服务器模块，跨 UID/GID 不一致的导出场景再叠加 UID GID 映射模块。（YouTube EPtzieR5MM06M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2503 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2503`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marshall “A Narrative History of BSD” 演讲〕讲者口述：为查明内核中残留的 AT&T 代码，团队的做法是先把整个内核跑一遍 CB（C beautifier），再对 32V 作同样处理，然后逐行比对；凡有两三行连续与 32V 吻合，即认定可疑、需进一步追查。（YouTube EPbVSXXeiFLgk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2504 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2504`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marshall “A Narrative History of BSD” 演讲〕讲者口述：逐行比对做完之后，内核里只剩六个文件仍以 AT&T 代码为主；讲者称按其意见这六个文件不如重写，而全系统发布风险大，于是考虑像 Net/1 那样只发布部分内核加若干工具。（YouTube EPbVSXXeiFLgk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2505 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2505`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marshall “A Narrative History of BSD” 演讲〕讲者口述：和解的最终安排是：给 70 个文件加上 USL 版权声明并声明这些并非 USL 独有；讲者称这些都是公共头文件、后来证明属公有领域，另外还须移除三个文件，而内核中其实并没有那三个文件可删。（YouTube EPbVSXXeiFLgk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2506 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2506`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marshall “A Narrative History of BSD” 演讲〕讲者口述：今天可用的各种 BSD，其源头是 4.4BSD。（YouTube EPbVSXXeiFLgk，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
