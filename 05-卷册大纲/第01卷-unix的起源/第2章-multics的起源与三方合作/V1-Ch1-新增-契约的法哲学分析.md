# V1-Ch1-新增-契约的法哲学分析.md

## 契约的法哲学：MIT-GE-Bell Labs 三方协议作为利益分配工具

> **史观框架**：shigang §11 法哲学
> **核心命题**：“法律最大的作用不是公平正义，而是维稳。在实施过程中实现实施者的利益分配。”(shigang 11.1 节)

- 要点：MIT/GE/Bell Labs 1964-1969 年的三方合作不是“为了推动计算机科学发展”的理想主义联盟，而是三个不同利益主体在特定法律框架下的权宜联合。MIT 获取 ARPA 资助但需要工业合作伙伴提供硬件（GE）和系统软件人才（Bell Labs）；GE 需要 MIT 的学术声誉来推销其 GE-645 计算机；Bell Labs 需要在 AT&T 1956 Consent Decree 的约束下寻找“不违反反垄断条款的计算机研究方向”。三方协议中的退出条款（Bell Labs 1969 年 4 月援引退出）不是“意外事故”而是利益分配机制的必然结果——当 Multics 的成本超支使 Bell Labs 的投资回报率低于替代方案时，退出是理性的利益计算而非技术判断。shigang §11 的核心命题在此获得实证：三方协议的法律结构不是为了保障合作公平（Multics 对 MIT 和 GE 都“公平”但对 Bell Labs“不公平”），而是为了在合作可行时维系合作、在合作不可行时提供有序退出——“维稳”而非“正义”。

- 史料：MIT/GE/Bell Labs 三方合作协议（MIT 档案馆藏，部分条款见 multicians.org）；Bell Labs 1969 年退出通知函；AT&T 1956 Consent Decree (United States v. Western Electric, Civil Action No. 17-49, Final Judgment, January 24, 1956, Judge Thomas F. Meaney)；Ritchie 1984 BLTJ 对退出过程的回忆
- 史观：shigang §11 法哲学——“任何法律问题都是政治问题，任何政治问题都是利益分配问题。”(11.1 节) 三方协议的法律条款（退出机制、知识产权共享、成果发布自由）不是对“合作关系”的法律表述，而是对“利益分配关系”的法律制度化。shigang §12 经济哲学——“斩杀线是一种市场化资源分配标准”(8.2 节)。Bell Labs 1969 年的退出决策本质上是：Multics 的成本/进度越过了 Bell Labs 管理层的“斩杀线”——低于此线的项目不再获得资源分配。
- 辨析：三方协议的“失败”是否意味着契约本身的失败？——从 shigang §11 的视角，契约从来不是为了“成功”（各方均获益）而设计的，而是为了“管理失败”（各方有序退出）而设计的。Bell Labs 退出后 Multics 继续运行至 2000 年的事实证明，契约的退出机制是有效的——它没有阻止“失败”，但阻止了“失败的扩散”。这与 USL v. BSDi (1992-1994) 形成对照：后者之所以比其他 UNIX 诉讼“成功”，正是因为和解条款为各方提供了体面退出的路径——法律的形式主义在此不是障碍而是通道。
- 文献：AT&T 1956 Consent Decree (Final Judgment, Jan 24, 1956); Pinheiro, J. (1987). "AT&T Divestiture & the Telecommunications Market." Berkeley Technology Law Journal; Cole, R. (2018). "Unix: A View from the Field." USENIX ;login:; multicians.org/history.html; Salus, P. H. (1994). A Quarter Century of UNIX. Addison-Wesley. ISBN 0-201-54777-5. Ch3


<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.76`）

史学含义：本书所写的 BSD 史，并非某种与古代史有本质区别的"现代史"。从 UNIX 诞生到 FreeBSD、OpenBSD、NetBSD、DragonFly BSD 的分合，皆属古代史，皆属重复与循环。史家不应伪装自己呈现了"真实的历史"，而应坦承所写皆是形式主义化的非存在，是当下的重构。本书不宣称呈现"真实的 BSD 历史"，这一坦承本身，即是对形式主义最大的诚实。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.95`）

分离聚合是世界发展的规律。分久必合，合久必分，具有必然性。UNIX 分裂出各种 BSD，BSD 又分裂出 FreeBSD、NetBSD、OpenBSD、DragonFly BSD，此乃分离；而各分支间的代码共享、ports 互通、社区人员的流动，此乃聚合。分合循环，永无止息。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.97`）

否定是必然的，任何事情都要被否定。否定后必然会再次产生，这是社会发展的根本动力。形式主义的否定标志着社会文明的前进。任何理论本身的发展，最后都会变成八股文，变成最反动的，因为它没有勇气否定自己。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.99`）

历史是所有人的重复，重复着所有人的历史。人类社会是一个曲折回环的封闭道路。只有找出切点，人类才会摆脱这样的错误痛苦之路。所谓切点，即一种真正自反的、敢于否定自身的哲学。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.101`）

所谓否定之否定，实则不敢也不能否定主体自身，敢于改革却不敢推翻自己。这是一种忒修斯之船式的否定，不是真正的发展。真正的否定不在于否定，而在于接纳与和解。这与否定之否定有根本区别——后者否认实质上的自我消解，实则与庄子万物齐一无异。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.103`）

修仙小说设定古法强于今法，逻辑结果就是末法时代——功法最后都会消失，修仙界退化成地球。地球就是修仙界的最终结局。这一循环同样适用于技术世界：任何技术范式最终都会走向其自身的否定，被新的范式所取代，而新范式并不必然优于旧范式。传统的 UNIX 哲学在 Linux 的冲击下退潮，但 Linux 自身也面临着设计债务的累积与范式的僵化。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.105`）

计算机程序源代码中只有三个结构：循环、顺序、选择。放在现实世界，又有谁跳了出去呢？这不是一个比喻，而是一个本体论同构：历史的结构就是程序的结构。循环是历史的本质，顺序只是循环的假象，选择只是切线上的一个点。苦难的根源在于你知道圆上每一点都有一条切线，而你只能转圈。知道了切线的存在，并不意味着能脱离圆——恰恰相反，对切线的认知本身就是苦难的来源。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.107`）

命运是一个整体，将其拆分为"命"（既定）与"运"（流变）是形式主义的分析谬误。命与运在本体论上是一体的，正如存在与非存在是一体的。每个人都被安排好了属于自己的角色，但生命的预定并不意味宿命论的消极接受——预定只是框架，在框架之内，人的主体性仍然有其空间。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.108`）

史学含义：BSD 的历史中，Linux 的崛起、FreeBSD 的边缘化、OpenBSD 的安全转向、DragonFly 的 fork，皆非必然。不写"若没有某某也会有另一个人做同样的事"，因为世界上没有必然性只有偶然性。每一个关键节点都是不可替代的偶然。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.241`）

史学含义：BSD 史中不乏准宗教性的现象——对 UNIX 哲学的信仰、对开源精神的信奉、对特定人物的崇拜、对"稳定性"的坚守。这些不完全是理性选择或技术决策，而有深刻的信仰属性。信仰是人民为了活着而强加于自己的形式，BSD 社区的维系同样靠的是信仰而非利益。BSD 许可证之争本质上是不同信仰体系的冲突——BSD 承认人类的有限性，GPL 则用形式限制自由实则起了反作用。史家应识别技术决策背后的信仰结构，而非将其伪装为纯技术选择。道风的缺乏即是道风的道——BSD 社区的沉默与萎缩，本身也是一种道。



<!-- DEEP_ANALYSIS: sacred_sources.duckdb.blocks -->
**史家判断**（证据等级：L2，来源：`sacred_sources.duckdb.blocks.382`）

这世间种种的等待，就好像沥青在滴落。沥青滴落实验启示我们：历史的时间尺度远超个人的感知。BSD 项目从 UNIX 算起已有半个世纪，比大多数社区成员的年龄都大。在沥青滴落般缓慢的时间尺度中，技术的兴衰、社区的聚散、个人的来去，都不过是短暂的一瞬。史家应有此时间自觉。



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1049`）

1964
Timesharing systems started appearing in the
early 1960’s, with one of the ﬁrst being the Atlas
supervisor (designed by the Manchester Project
in England) for the Atlas brand computer. A timeshared system in that era meant that
two people would be sharing
the same system, many times setting up




<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_108`）

Motivation
Starting Position
Local Improvements
Remote Logging
Conclusion
Never Lose a Syslog Message
Alexander Bluhm
bluhm@openbsd.org
September 24, 2017 Motivation
Starting Position
Local Improvements
Remote Logging
Conclusion
Agenda
1
Motivation
2
Starting Position
3
Local Improvements
4
Remote L



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1083`）

27
FreeBSD Journal • September/October 2022
SSH
is a multipurpose tool used by pretty much anyone running and administering a
Unix machine, logging in from one to the next more often than not. Secure, en­
crypted logins as SSH’s core functionality are a great day-to-day help, but the daemon can
do m



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1137`）

The Design and Implementation of the 4.4 BSD Operating System 由 CSRG 核心成员 McKusick、Bostic、Karels 和 Quarterman 合著，1996 年 Addison-Wesley 出版，共 736 页。全书系统记录 4.4 BSD 操作系统的设计与实现，涵盖内核架构、进程管理、内存管理、文件系统（FFS/LFS）、网络协议栈（TCP/IP）、进程间通信等核心子系统。该书是 CSRG 最后一份正式发布的 BSD 版本的权威技术文档，是 FreeBSD 4.x 分支的直接技术祖先，对理解 BSD UNIX 哲学的技术实现具有不可替代的价值。



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1163`）

文献《Plan_9_from_Bell_Labs》由 Pike（1993） 撰写。全文提取成功，共约 82566 字符。内容摘要：Plan 9 from Bell Labs Rob Pike Dave Presotto Sean Dorward Bob Flandrena Ken Thompson Howard Trickey Phil Winterbottom Bell Laboratories Murray Hill,New Jersey 07974 USA Motivation By the mid 1980s, the trend in computing was away from



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1189`）

将 Unix 从历史（1972 年约 5000 行内核）到 2016 年（约 2700 万行）的演进构建为 Git 版本库，涵盖 Bell Labs、BSD、386bsd、FreeBSD 等 24 个快照、49.6 万次提交、973 位贡献者，供软件工程经验研究使用。



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1200`）

文献《openbsd》由 Sadowski（2018） 撰写。全文提取成功，共约 6101 字符。内容摘要：OpenBSD Einblick, Überblick und Ausblick OpenRheinRuhr 2018 Rafael Sadowski <rsadowski@openbsd.org> whoami(1) ● Erste Aktivität auf ports@ ○ May 04, 2011; 1:18pm ○ NEW: graphics/opencv ● April 2017 ○ Invitation ○ CVS commit rights ● Night-Job ○ O



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1214`）

文献《Hot_cross_builds_Cross-compilation_in_pkgsrc》由 campbell（2024） 撰写。全文提取成功，共约 14282 字符。内容摘要：Hot cross builds Cross-compilation in pkgsrc Taylor R Campbell riastradh@NetBSD.org BSDCan 2024 Ottawa, Canada May 31, 2024 Hot cross builds: cross-compilation in pkgsrc https://www.NetBSD.org/gallery/present



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1216`）

文献《NetManager_NetBSD》由 Borrill（2025） 撰写。全文提取成功，共约 14519 字符。内容摘要：Building Products with NetBSD part 2: Stephen Borrill sborrill@precedence.co.uk sborrill@NetBSD.org @sborrill@justfollow.me.uk Why part 2? Building Products with NetBSD part 1: ThinIT presented at: EuroBSDCon 2007 (Copenhagen) BSDCan 20



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1260`）

1973 年 UNIX 用户组内部分享/讨论笔记的扫描件（TUHS 档案）。因 PDF 为纯图像、无可用 OCR 文本，无法逐段摘要；据标题应为早期 UNIX 用户交流与用法记录，属一手史料但不可全文检索。（源文件为图像扫描，摘要仅据题名与档案背景）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1266`）

BSTJ 1978 专刊中 S.R. Bourne《The UNIX Shell》的扫描件（图像无 OCR 文本）。该文系统描述 Bourne shell（sh）设计：作为用户可选常规进程、命令解释、I/O 重定向、管道、变量与环境、控制结构，奠定 POSIX shell 基础。（摘要基于该论文已知 canonical 内容，非全文 OCR）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1269`）

BSTJ 1978 专刊中 B.W. Kernighan 与 M.E. Mashey《UNIX Programming Environment》的扫描件（图像无 OCR 文本）。该文阐述 Unix 编程环境哲学：小而专的工具、管道组合、可脚本化、可移植，是“Unix 哲学”的经典表述之一。（摘要据 canonical 内容）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1274`）

S.C. Johnson 与 D.M. Ritchie 论述程序（尤其 Unix 系统与大部分软件）向 Interdata 8/32 等机器的可移植性：C 语言新扩展、pcc 等工具辅助检测不可移植结构，源语言表示在各环境基本一致。



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1279`）

BSTJ 1978 专刊头篇 D.M. Ritchie 与 K. Thompson《The UNIX Time-Sharing System》的扫描件（图像无 OCR 文本）。该文是 Unix 的权威总述：概述内核、文件系统、进程、shell、I/O 与系统调用接口，属必引史料。（摘要据 canonical 内容）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1280`）

D.M. Ritchie《UNIX Time-Sharing System: A Retrospective》的扫描件（图像无 OCR 文本）。该文对 Unix 设计作回顾性反思，评估早期决策得失。（摘要据 canonical 内容）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1282`）

K. Thompson《UNIX Implementation》的扫描件（图像无 OCR 文本）。该文描述 Unix 内核实现：以 C 而非汇编、文件系统（inode）、进程与 fork/exec、系统调用机制等底层结构。（摘要据 canonical 内容）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1284`）

D.L. Presotto 与 D.M. Ritchie 描述第八版 Unix 的进程间通信：在已有流（streams）机制上，提供以文件方式建立通信的低层机制——管道即交叉连接的流，新请求将流关联到命名文件，文件描述符可经流在进程间传递。



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1285`）

V. Jacobson 1987 年关于“调优 Unix lex”的笔记/文稿扫描件（图像无 OCR 文本）。据标题，内容应涉及对 Unix lex 词法分析生成器的性能调优经验。（摘要据题名与背景）



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1292`）

文献《openbsd_lteo-openbsd-carolinacon15-20190427》由 未知（未知） 撰写。全文提取成功，共约 26232 字符。内容摘要：Writing Exploit-Resistant Code with OpenBSD Lawrence Teo lteo openbsd.org @lteo Slides and references at: https://lteo.net/carolinacon15 CarolinaCon 15 - Charlotte, NC - April 27, 2019 A question Innovation’s Black Ho



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1303`）

文献《phk_malloc》由 未知（未知） 撰写。全文提取成功，共约 28591 字符。内容摘要：Malloc(3) revisited Poul-Henning Kamp 1 The FreeBSD Project ABSTRACT malloc (3) is one of the oldest parts of the C language environment and not surprisingly the world has changed a bit since it was ﬁrst conceived. The fact that most UNIX kernels hav



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1317`）

文献《netbsd_abc2009-P5A-paper》由 未知（2009） 撰写。全文提取成功，共约 37862 字符。内容摘要：Environmental Independence: BSD Kernel TCP/IP in Userspace Antti Kantee Helsinki University of Technology pooka@cs.hut.ﬁ Abstract Code is code. In the entire application stack only a very small fraction of code is special in the sense



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1331`）

文献《netbsd_apropos_replacement》由 未知（2012） 撰写。全文提取成功，共约 32820 字符。内容摘要：Apropos Replacement : Development of a full text search tool for man pages Abhinav Upadhyay <er.abhinav.upadhyay@gmail.com> J¨org Sonnenberger <joerg@NetBSD.org> Abstract Manual pages are a key component of Unix like oper- ating sys



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1337`）

文献《netbsd_AsiaBSDCon2017-basepkg》由 Yuuki Enomoto（2017） 撰写。全文提取成功，共约 6843 字符。内容摘要：Maintain the NetBSD Base System Using pkg_* Tools Yuuki Enomoto Ken’ichi Fukamachi Chitose Institute of Science and Technology Abstract • This presentation explains “basepkg.sh”. • Fine granular system can be easily upd



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1339`）

文献《netbsd_AsiaBSDCon2018-basepkg-paper》由 未知（2017） 撰写。全文提取成功，共约 30639 字符。内容摘要：Design, Implementation and Operation of NetBSD Base System Packaging Yuuki Enomoto∗ Ken’ichi Fukamachi† Abstract It is believed that UNIX operating system (OS) built on ﬁne granular small parts is preferable to one built on



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1340`）

文献《netbsd_AsiaBSDCon2018-basepkg》由 Yuuki Enomoto（2018） 撰写。全文提取成功，共约 12473 字符。内容摘要：Design, Implementation and Operation of NetBSD Base System Packaging Chitose Institute of Science and Technology Yuuki Enomoto Ken’ichi Fukamachi 1 Abstract • OS built on fine granular small parts is preferable to one 



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1342`）

文献《netbsd_asiabsdcon_2017_modern_spell》由 未知（2017） 撰写。全文提取成功，共约 3947 字符。内容摘要：A modern replacement for spell(1) Abhinav Upadhyay <abhinav@NetBSD.org> AsiaBSDCon 2017 Problems with old spell Problems with old spell Very ancient - dates back to Unix version 7 Problems with old spell Very ancient - dates



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1343`）

文献《netbsd_a_modern_spell》由 未知（未知） 撰写。全文提取成功，共约 8065 字符。内容摘要：A Modern spell(1) Abhinav Upadhyay <abhinav@NetBSD.org> EuroBSDCon 2017, Paris Outline ➢ Shortcomings in the old spell(1) ➢ Feature Requirements of a modern spell(1) ➢ Implementation Details of new spell(1) ➢ Performance comparison with oth



<!-- DEEP_ANALYSIS: cross_indexes.duckdb.concept_history -->
**史家判断**（证据等级：L2，来源：`cross_indexes.duckdb.concept_history.14`）

分时思想出现于 1950 年代末：1959 年 Strachey 与 McCarthy 各自提出 time-sharing。1961 年 11 月，Fernando Corbató 与 Robert Daley 等在 MIT 建成并演示 Compatible Time-Sharing System（CTSS），成为首个可运行的分时系统，1963 年发展为稳定大规模系统；其后 CTSS 在 ARPA 支持下演进为 Project MAC（1963 年上线）。1965 年 CMOS 分时设计更上层楼，MIT Project MAC、贝尔电话实验室与通用电气联合启动 Multics（由 Corbató 领导），引入分页、分段存储与树状文件系统；贝尔实验室 1969 年退出，1970 年 GE 计算机业务转售 Honeywell 将其商业化，1985 年被取消。1990 年 Corbató 因在 CTSS 与 Multics 上的开创性工作获 ACM 图灵奖。



<!-- DEEP_ANALYSIS: cross_indexes.duckdb.concept_history -->
**史家判断**（证据等级：L2，来源：`cross_indexes.duckdb.concept_history.17`）

文件系统概念演化大体历经：①顺序/平坦期（1950–1960s）：磁带顺序访问与早期磁盘平面目录；②层次化突破（1960s–1970s）：Multics（始于 1965）首创树状文件目录与路径名，Unix（1970s）以 inode 架构、挂载点、“一切皆文件”简明化并推广层次文件系统；③性能重构期（1980s）：Marshall Kirk McKusick 等为 4.2BSD 设计 Fast File System（FFS/现称 UFS1，1982 年写出、随 4.2BSD 发行），引入柱面组、碎片、软更新，UFS2（2002–2003）改用 64 位块指针扩展至多 TB；④网络化期：Sun Microsystems 1984 年推出网络文件系统 NFS，确立 VFS/vnode 接口；⑤存储与纠错集成期：如 ZFS（2001–2006）将文件系统与卷管理、写时拷贝、校验和集成。



<!-- DEEP_ANALYSIS: cross_indexes.duckdb.concept_history -->
**史家判断**（证据等级：L2，来源：`cross_indexes.duckdb.concept_history.20`）

思想土壤为 1960–1970 年代大学与黑客社区的“软件共享”传统（如 MIT AI 实验室的 ITS 系统）。1984 年 1 月斯托曼正式启动 GNU 项目，回应专有软件扩散下的分享禁令；1985 年成立 FSF、发布《GNU 宣言》；1986 年阐明自由软件四项自由；1989 年发布 GNU GPL v1，1991 年 v2。1980 年代末至 90 年代初因 Linux 内核（Linus Torvalds）与 GNU 工具合并成 GNU/Linux，达成完全自由操作系统目标。1998 年 Raymond 的《大教堂与集市》、Netscape 开源其浏览器、Raymond 与 Perens 创立开放源代码促进会（OSI）与《开源定义》，自由软件运动与开源运动正式分野。



<!-- DEEP_ANALYSIS: cross_indexes.duckdb.concept_history -->
**史家判断**（证据等级：L2，来源：`cross_indexes.duckdb.concept_history.3`）

Capsicum 源自剑桥大学计算机实验室 Robert N.M. Watson 与 Jonathan Anderson 的 TrustedBSD 研究项目，受 Google、FreeBSD 基金会与 DARPA 资助。2010 年 12 月 USENIX ;login 刊发《introducing Capsicum: practical capabilities for UNIX》正式公开。原型在 FreeBSD 8.x 开发，2011 年起作为实验特性随 FreeBSD 9.0 提供。其思想可上溯至 Dennis 与 Van Horn 1966 年的 capability 理论。2013 年 Google 与 FreeBSD 基金会联合资助 Pawel Jakub Dawidek 整合改进 API 并开发 Casper 后台服务，Casper 自 FreeBSD 10.1 起提供并用于 tcpdump、kdump 等组件。此后持续移植到 Linux、DragonFlyBSD 等。



<!-- DEEP_ANALYSIS: cross_indexes.duckdb.concept_history -->
**史家判断**（证据等级：L2，来源：`cross_indexes.duckdb.concept_history.4`）

1979 年前后（一说 2BSD 时期）引入 chroot(2)，本为构建与测试设计而非安全机制，因可再次 chroot 逃逸而存在已知缺陷。1990 年代末，FreeBSD 开发者 Poul-Henning Kamp 应托管商 Derrick T. Woolworth 付费需求，开发出比 chroot 更强的内核级进程隔离：使每个 jail 拥有独立根文件系统、网络地址与进程空间。jail 随 FreeBSD 4.0（2000-03-14）正式发布，jail(2)/jail(8) API 沿用至今；同月于 SANE 2000 会议发表论文《Jails: Confining the omnipotent root》（Kamp 与 Robert Watson）。后续演进包括 VNET 虚拟网络栈、分层 jail、RCTL 资源限制、ZFS 深度集成，以及 ezjail/iocage/cbsd/Bastille 等管理工具。2013 年 Docker 容器热潮被视为 jail 早已具备的理念。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-002`）

UNIX 的名称源于对 Multics（Multiplexed Information and Computing System）的类比；Brian Kernighan 命名时意在对比 Multics 的“多选项、多命令”哲学与 UNIX 的“小而统一”哲学



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L5，来源：`historical_claims.duckdb.claim.CL-1-004`）

rc 命令名源于 MIT CTSS 系统的 RUNCOM（run commands），CTSS 的 RUNCOM 相当于 Unix 的 shell 脚本



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L5，来源：`historical_claims.duckdb.claim.CL-1-005`）

Dennis Ritchie 本人持“Unix 是 CTSS 的现代版本”的论点，约 1973 年首次提出，1981 年仍坚持此论



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-006`）

“Unix 是阉割版 Multics（castrated Multics）”是同时使用过两套系统者之间的戏称，并非 Unix 命名的起源；Dennis Ritchie 在 1981 年 USENIX 会议上明确否认此说法



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-007`）

1981 年时 Multics 上已有读写 Unix tar 磁带格式的实用工具（PL/1 实现），Bill Jolitz 提及



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-1-008`）

Dijkstra 1968 年描述的 THE 多道程序系统明确声明不作为多访问系统、无公共数据库供独立用户间通信，与 Multics 的多访问分时设计形成同时期路径对照



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-012`）

Thompson 认为 UNIX 的流行是时机与机缘的结果，与计算机行业从中央大型机向自主小型机的转变相伴发生。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-013`）

C 语言与 UNIX 系统紧密关联——C 在 UNIX 系统上被开发，系统本身与运行其上的大部分程序均用 C 书写。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-017`）

运行于 PDP-11 的原 UNIX 系统采用简单优雅的文件系统，所有磁盘传输均为 512 字节块。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-1-019`）

第一个向 AT&T 索取 UNIX 的人是哥伦比亚大学的 Lou Katz 教授，Ken Thompson 将后来被称为第四版的内容复制给他。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-020`）

新南威尔士大学 John Lions 教授编写的《Lions 的 UNIX 第六版注释》收录了内核源码，作为盗版影印件被广泛传阅。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-022`）

第一个伯克利软件发行版（1BSD）是作为 UNIX 第六版的更新发布的，随后是用于第七版/PDP-11 的 2BSD，以及用于 VAX 的 3BSD 和 4BSD。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-051`）

Pike 与 Kernighan 1984 年论文中称 UNIX 的大部分力量来自一种使程序易于使用且更易于组合的程序设计风格，该风格以软件工具（software tools）的使用为特征，依赖程序如何融入编程环境——如何与其他程序协作——而非程序内部设计。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-1-052`）

Spinellis 2017 年实证研究手工标注了 Research Unix 各版本的个人贡献分配表（Table 3），例如 Eric Schmidt 贡献 lex、Stephen C. Johnson 贡献 cc/lint/mip/pcc/porttour/yacc、S. I. Feldman 贡献 f77/make、S. R. Bourne 贡献 adb/sh/shell。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-1-053`）

Spinellis 2017 年实证研究手工标注了 BSD Unix 版本的个人贡献分配表（Table 4），例如 Ken Arnold 贡献 curses/fortune/libcurses、Eric Allman 贡献 sendmail/syslog 相关工具。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-100`）

Salus 1994《A Quarter Century of UNIX》引录了 UNIX V6 内核中著名的注释 “/* You are not expected to understand this */”，该注释位于进程上下文切换相关代码段（lines 2240-2243 处，注释本身在第 2238 行），出自第六版内核源码。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-016`）

McKusick 等人在 1984 年快速文件系统论文中明确称，UNIX 操作系统从 Multics 这一大型高性能操作系统借鉴了许多思想。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-101`）

Bell 等人 1970 年在 DEC 发表 PDP-11 小型机架构论文，作者包括 DEC 的 G. Bell、R. Cady、H. McFarland、B. Delagi、J. O’Laughlin、R. Noonan 与卡内基梅隆大学的 W. Wulf。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-103`）

Pike 等人 1995 年在《Plan 9 from Bell Labs》论文中称，1980 年代中期计算趋势正从大型集中式分时计算机转向由较小个人机器组成的网络，这是 Plan 9 的设计动机。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-001`）

Berkeley Pascal PX 实现说明（1979 年 1 月）由 PDP-11/70 原始版本更新，以反映运行于 VAX-11/780 上的解释器。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-002`）

Berkeley Pascal 的 px 解释器是 Ken Thompson 原始实现的 PDP-11/70 到 VAX-11/780 操作码映射，经 William Joy 与 Charles Haley 大量修改扩充。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-003`）

Kridle 与 McKusick（1983）在运行 4.2BSD 的 VAX-11/780 与 VAX-11/750 上测量了多种 I/O 操作下的 UNIX 文件系统吞吐量。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-108`）

1969 年，贝尔实验室团队（主要是 Ossanna、Thompson、Ritchie）开始为 Multics 寻找替代方案，并游说购买中型机器（DEC PDP-10 或 SDS Sigma 7）。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-114`）

C 语言于 1970 年代初被设计为新兴 Unix 操作系统的系统实现语言，源自无类型的 BCPL 语言并演化出类型结构。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-118`）

1974 年 7 月，Dennis Ritchie 与 Ken Thompson 在《Communications of the ACM》第 17 卷发表《The UNIX Time-Sharing System》，将 UNIX 描述为面向 DEC PDP-11/40 与 11/45 计算机的通用多用户交互式操作系统。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-125`）

Poul-Henning Kamp 在 2010 年演讲中质疑“软件工具”范式（1970-2010，约 40 年）作为 UNIX 哲学核心范式是否仍然相关。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-005`）

C Shell（csh）是伯克利为 UNIX 开发的新命令语言解释器，综合了其他 shell 的优良特性与类似 INTERLISP redo 的历史机制，其独有特性主要面向交互式用户。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-008`）

Bill Joy 编写了 vi 的版本 1 与 2.0 至 2.7 并创建了编辑器框架，Mark Horton 添加宏与其他特性使 ex/vi 在大量终端与 Unix 系统上工作。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-010`）

PDP-11 的 16 位虚拟地址空间到 1975 年已成为应用的真实限制，DEC 因而设计 32 位虚拟地址的 VAX 作为其继任者。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-011`）

VAX-11/780 于 1978 年推出，是 VAX 架构的首个实现；VAX 设计始于 1975 年，目标是成为 PDP-11 的兼容扩展以解决其虚拟地址空间限制，名称 VAX-11 源自“PDP-11 的虚拟地址扩展”。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-041`）

McKusick、Joy、Leffler 与 Fabry（1984）描述了从原始 512 字节 UNIX 文件系统到 4.2BSD 发布的新文件系统（快速文件系统 FFS）的变更。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-051`）

Pike 与 Kernighan（1984）提出 UNIX 操作系统的力量来自易于与其他程序组合的程序设计风格，其关键在于软件工具的使用。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-008`）

1973 年 11 月 Ken Thompson 与 Dennis Ritchie 在普渡大学 SOSP 发表首篇 Unix 论文，伯克利 Bob Fabry 出席后推动在伯克利获取 Unix。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-3-012`）

1986 年 2 月 18 日伯克利市议会批准决议，拨款 11,058 美元为卫生与公众服务部购置 UNIX 计算机及 System Development Corporation 软件。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-014`）

伯克利 UNIX 性能改进工作由 NSF 资助（MCS80-05144）与 DARPA（ARPA Order No. 4031，合同 N00039-82-C-0235）资助。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-050`）

McKusick 与 Karels 1986 年提出伯克利 UNIX 新虚拟内存实现方案：虚拟内存上限应为物理内存与交换空间之和，而非受预分配交换区大小限制。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-054`）

Leffler 等 1983 年记载进程间通信与网络是 4.2BSD 对 UNIX 最重要的新增之一，是两年以上讨论与研究的成果。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-055`）

Leffler 等 1983 年记载 BSD 进程间通信设施已成为 UNIX 的事实标准。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-056`）

McKusick、Joy、Leffler 与 Fabry 1984 年记载快速文件系统（FFS）的文件访问速率可达传统 UNIX 文件系统的十倍。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-3-070`）

Stonebraker、Wong、Kreps 与 Held 1976 年记载当时已运行的 INGRES 数据库管理系统给出关系数据视图，作为用户进程集合运行于 UNIX 之上（DEC PDP-11）。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-001`）

386BSD 移植工程由 William Frederick Jolitz 与 Lynne Greer Jolitz 夫妇合著，1991 年以《Porting UNIX to the 386: A Practical Approach》系列文章发表。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-4-004`）

Spinellis 构建的 Unix 历史仓库将 386BSD 0.0 与 0.1 的源码发行列为数据源。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-4-005`）

Spinellis 构建的 Unix 历史仓库将 386BSD 0.1 的 patchkit 补丁集列为数据源，存档于 tuhs.org。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-008`）

Dennis M. Ritchie 的论文《The Evolution of the Unix Time-sharing System》(1984) 概述 UNIX 早期发展史，聚焦文件系统、进程控制机制与管道命令思想的演进。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-112`）

USL 起诉加州大学董事会与 BSDi，指控其分发计算机软件侵犯 USL 对 UNIX 操作系统的专有权利。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L3，来源：`historical_claims.duckdb.claim.CL-4-117`）

《UNIX-HATERS Handbook》（1994）封面题词将伯克利最著名的两个产物称为 LSD 与 Unix，并称二者非巧合。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-118`）

USL 与加州大学和解协议记载，USL 已对新泽西联邦地区法院对大学、董事会个人成员与 BSDi 提起案号 92-1667 的诉讼，指控 Net2 侵犯 UNIX 版权。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-119`）

和解协议规定 UNIX 衍生文件包含 4.4BSD-Lite 中的 23 个文件，USL 在协议签署前已审阅并批准其纳入 4.4BSD-Lite。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-121`）

William Jolitz 1992 年 7 月 19 日在 comp.unix.bsd 发布 386BSD Release 0.1 公告，以“Cut the Tape”“14 July 1992 (Bastille Day)”“Vive la Revolution”渲染法国大革命修辞。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-122`）

McKusick《Twenty Years of Berkeley Unix》记载，Thompson 与 Ritchie 1973 年 11 月在普渡大学 SOSP 发表首篇 Unix 论文，伯克利 Fabry 教授与会后即着手在伯克利获取该系统。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-001`）

FreeBSD 核心开发者 Poul-Henning Kamp（phk）1996 年撰文指出，大多数 UNIX 内核已从 swap/segment 转向虚拟内存/页式内存管理，但 malloc/free API 的实现并未充分反映这一转变，为其面向现代虚拟内存环境重写 malloc 提供了动机背景。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-5-011`）

Kamp 与 Watson 在 Jails 论文（SANE 2000）摘要中陈述：FreeBSD“Jail”机制在保持 UNIX“root”模型简洁性的同时提供操作系统环境分区能力，允许系统管理员为每个虚拟化环境委托管理能力；截至论文发表时最流行的用途是 ISP 环境中的虚拟主机服务。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-6-015`）

Capsicum 是由 Robert N. M. Watson、Jonathan Anderson、Ben Laurie 与 Kris Kennaway 提出的面向 UNIX 的实用 capability 框架。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L2，来源：`historical_claims.duckdb.claim.CL-7-024`）

参考文献全文数据库收录《1984 McKusick A Fast File System for UNIX en》（unknown，1984），作为本章主题的候选史料。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L2，来源：`historical_claims.duckdb.claim.CL-7-048`）

参考文献全文数据库收录《A.2.1_The_UNIX_Time-Sharing_System》（D.M.Ritchie; K.Thompson，1969），作为本章主题的候选史料。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L2，来源：`historical_claims.duckdb.claim.CL-8-002`）

参考文献全文数据库收录《Pgs 01-38 Unix Programmer's Manual for MERT》（Bell Telephone Laboratories，1977），作为本章主题的候选史料。



<!-- DEEP_ANALYSIS: references_fulltext.duckdb.summaries -->
**史家判断**（证据等级：L2，来源：`references_fulltext.duckdb.summaries.sum_1146`）

以 Multics 为案例系统研究信息保护的机制设计，提出五项设计原则（最小特权、机制经济性、开放设计、权限完整、心理可接受），并描述访问控制列表、分级访问控制规范、用户认证与主存保护等核心机制，结尾讨论已知弱点。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-003`）

Unix 的诞生是对 Multics 在贝尔实验室默里山（BTL-MH）开发拖期、无法提供交互能力的直接反应——默里山团队被迫退回到运行 GECOS 的状态



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-011`）

Thompson 在 1984 年图灵奖演讲中称，特洛伊木马攻击的构想最早见于一份对 Multics 早期实现安全性的空军批判报告。



<!-- DEEP_ANALYSIS: historical_claims.duckdb.claim -->
**史家判断**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-116`）

Salus（1994）在《A Quarter Century of UNIX》前言中称，1992 年前所见的约二十余种 Unix 历史叙述无一完全准确，遂决定撰写一部真正历史。

