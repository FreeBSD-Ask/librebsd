---
chapter: 第 41 章
id: CH41
volume: 第02卷-伯克利的岁月
---

# 第 41 章 usl起诉bsdi与伯克利

## 要点

- USL v. BSDi 案件号为 Civil Action No. 92-1667（D. N.J.），起诉书要点包括：BSDi 基于 Net/2 商业化 BSD/OS 侵犯 USL 版权与商业秘密、伯克利校方未授权 BSDi 使用 Net/2 商业化、Net/2 中含 USL 衍生代码（约 6 个文件）、BSDi 须停止销售 BSD/OS 与赔偿

| 字段 | 内容 | 来源 |
| --- | --- | --- |
| 案件名 | Unix System Laboratories, Inc. v. Berkeley Software Design, Inc.; The Regents of the University of California | 判例抬头 |
| 案号 | Civ. No. 92-1667 | 判例 STATEMENT OF FACTS 节 |
| 法院 | United States District Court, D. New Jersey（D.N.J.） | 判例抬头 |
| 法官 | Dickinson R. Debevoise, District Judge | 判例抬头 |
| 起诉日期 | **1992 年 4 月 20 日**（原始诉状）；**1992 年 7 月 24 日**（第一次修正诉状追加 UC Regents 为共同被告） | 判例 PROCEDURAL HISTORY 节 |
| 公开判例 | 832 F. Supp. 790 (D.N.J. 1993)，意见书日期 **1993 年 9 月 8 日** | Justia 完整文本 |
- 经 Justia 832 F. Supp. 790 一手判例抬头确认，案件当事方与律师团队如下：原告 USL 为特拉华州公司、总部位于新泽西州 Summit（由 AT&T **1990 年** 成立、**1993 年** 出售给 Novell）；被告 BSDi 为特拉华州公司、总部位于弗吉尼亚州 Richmond Falls（由 CSRG 核心成员 Karels、McKusick、Bostic 等创立——判例原文称 “the CSRG programmers, at least those who founded BSDI (Karels, McKusick, and Bostic)”，2026-09-13 联网回源 832 F. Supp. 790 核验）
- BSDi 与伯克利的应对包括：BSDi 聘请律师团队应诉、伯克利校方法律顾问介入、CSRG 提供 Net/2 重写过程文件证据、社区组织支持 BSDi（如 USENIX 声明）、1993 年 3 月初（Debevoise 法官驳回初步禁令裁决后的下一个周一）伯克利在加州州法院反诉 USL（声称 USL 未按许可证要求为 System V 中使用的 BSD 代码提供署名）
- 经 McKusick 1999《Twenty Years of Berkeley Unix》当事人一手叙述确认，诉讼期间的 “代码清理” 须区分三个阶段：① **诉前清理（1989-1991）**——Karels、Bostic、McKusick 三人 "spent the next several months going over the entire distribution, file by
- **史料**：McKusick 1999《Twenty Years of Berkeley Unix》当事人一手原文（oreilly.com/openbook/opensources/book/kirkmck.html，**2026-07-28** 访问）；Novell-UC Berkeley 和解协议（**1994.1**，部分保密）；4.4BSD-Lite Release Notes（**1994.6**）；FreeBSD 2.0 Release Notes（freebsd.org/releases/2.0/notes/，**1994-1995**）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3711] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3731] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3736] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3865] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3893] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3935] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3956] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章

## 史观

- 章级史观综述：USL v. BSDi 诉讼是偶然与结构交织的转折——总纲第 5 条（没有必然性，只有偶然性）：诉讼爆发与和解走向均非注定，McKusick 转述的 Torvalds 回答（“诉讼本可能走向另一边，那样就什么都不会留下”）亦将 Linux 诞生窗口归因于诉讼的不确定性；总纲第 10 条（动手者创造历史）：Net/2 重写由 Bostic 张贴清单动员外围开发者逐一重写累积而成；总纲第 4 条（分离聚合是永恒规律）：4.4BSD-Lite 的强制清理使 BSD 从 AT&T 混合版权聚合体中彻底分离；总纲第 13 条（法律与道德是利益分配）：和解条款（约 70 个文件补加版权声明、删除 3 个文件、禁用 Net/2）实质是双方利益的再分配安排。各子节 41.1-41.4 的史观/辨析字段为本综述的展开依据。

## 辨析

- 案件号经 Justia 联邦判例汇编 832 F. Supp. 790 (D.N.J. 1993) 公开判例确认为 Civ. No. 92-1667，法院为 United States District Court, D. New Jersey（D.N.J.），法官为 Dickinson R. Debevoise；先前 “部分史料称 D. N.J. Newark” 的歧义已解决——D.N.J. 为
- [考据脚注：BSDi 总部地址] Justia 判例原文记载 BSDi 总部为 “Richmond Falls, Virginia”（2026-09-13 联网回源核验：意见书 832 F. Supp. 790 及 1992-04-20 原始诉状均印作 “Richmond Falls”，后者并注 [sic]，原文本身完整无截断），但弗吉尼亚州实际地名无 “Richmond Falls”——可能为 “Richmond”（弗吉尼亚州首府）或 “Falls Church”（弗吉尼亚州城市）〔存疑：判例原文地名疑点保留待核〕
- 反诉时间经 McKusick 1999 当事人一手叙述确认——法官裁决约六周后（1993 年 3 月）发布，伯克利 “following Monday morning” 即下周一在加州起诉；1992 年 6 月说法无一手来源支持，系时间线混淆
- [考据脚注：诉讼期间代码清理的辨析] 经 2026-07-28 联网核查 McKusick 1999 一手原文确认，诉讼期间的 “代码清理” 存在三个需辨析的误区——① **误区一：诉讼加速了代码清理**——实际相反，诉讼使 CSRG 成员被拘传作证、撰写数百页法律材料，代码工作停滞；真正的代码清理在 1989-1991 年诉前完成；② **误区二：和解协议要求大规模代码重写**——实际仅 3 个文件被要求完全删除，另有约 70 个文件仅须补加 USL 版权声明，Net/2 被禁用发行（见本章 PODCAST_REVIEW 和解条款当事人叙述）
- [考据脚注：FreeBSD 2.0 发布日期] FreeBSD 2.0 Release Notes 未在文档开头明确标注发布日期，但 freebsd.duckdb freebsd-src 仓库中 RELENG_2_0_5_ALPHA 标签创建于 1995-05-29、RELENG_2_0_5_RELEASE 标签创建于 1995-06-10，Jordan K. Hubbard 于 1995-01-04 提交的版本记录〔存疑：句尾原文截断，所指提交内容待回源〕

## 文献

- USL v. BSDi, Civil Action No. 92-1667（D. N.J. 1992）；Unix System Laboratories, Inc. v. Berkeley Software Design, Inc., 832 F. Supp. 790 (D.N.J. 1993)[Z/OL]. 美国新泽西联邦地区法院，1993-09-08. <https://law.justia.com/cases/federal/district-courts/FSupp/832/790/1428569/> [2026-07-28]；McKusick, K. (1999) “Twenty Years of Berkeley Unix”；Quinlan, D. (1992) “The USL v. BSDi Case” ［A］
- Unix System Laboratories, Inc. v. Berkeley Software Design, Inc., 832 F. Supp. 790 (D.N.J. 1993)[Z/OL]. 美国新泽西联邦地区法院，1993-09-08. <https://law.justia.com/cases/federal/district-courts/FSupp/832/790/1428569/> [2026-07-28]；Cal. Const. art. IX § 9（UC Regents 设立依据） ［A］
- BSDi 应诉文件；伯克利反诉状；McKusick, K. (1999) “Twenty Years of Berkeley Unix”（当事人一手叙述）；FreeBSD Project. “A Brief History of FreeBSD”（FreeBSD Handbook） ［B］

<!-- NEWREF:2475 --><!-- NEWREF:2520 --><!-- NEWREF:2521 --><!-- NEWREF:2522 --><!-- NEWREF:2523 --><!-- NEWREF:2524 --><!-- NEWREF:2538 -->

## 文献增补与辩证校准（2026-08-08 追加）

> 40.1-40.3 USL 诉讼进程：
> - **文献增补（ref 3778）**：McKusick 亲述诉讼始末（Net/2 分发→BSDi 起诉→USL 反诉），40.1 起诉书要点的一手背景
> - **文献增补（ref 3783）**：CSRG 时间线综述确认 1992 年诉讼与 1995 年 CSRG 解散的因果链
> - **辩证校准（第 24 章 24.4 节）**：诉讼不是 BSD 史的断裂而是循环——4.4BSD-Lite 的发布是“否定与再生”（第 24 章 24.4 节原文），本章叙事应呈现循环结构
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix” [Z/OL]. O'Reilly Open Sources, ISBN 1-56592-582-6. <https://www.oreilly.com/openbook/opensources/book/kirkmck.html> [2026-07-28]；USL v. BSDi, Civil Action No. 92-1667（D. N.J. 1992-1994）；1994 年和解协议；4.4BSD-Lite Release Notes（1994.6） ［A］
- FreeBSD 2.0 Release Notes [EB/OL]. The FreeBSD Project. <https://www.freebsd.org/releases/2.0/notes/> [2026-07-28]；McKusick, M. K. (1999) “Twenty Years of Berkeley Unix” [Z/OL]. O'Reilly Open Sources, ISBN 1-56592-582-6. <https://www.oreilly.com/openbook/opensources/book/kirkmck.html> [2026-07-28]；4.4BSD-Lite Release Notes（CSRG, 1994.6）；freebsd.duckdb freebsd-src 仓库 1994-1995 年 commit 历史；FreeBSD COPYRIGHT 文件 [EB/OL]. The FreeBSD Project. <https://raw.githubusercontent.com/freebsd/freebsd-src/main/COPYRIGHT> [2026-07-28]（含 4.4BSD-Lite 原始 4-clause BSD License 文本与 1999-07-22 William Hoskins 广告条款删除声明）；Rodney W. Grimes. This is the official 4.4 Lite copyright. freebsd-src [DB/OL]. 1994-09-11T07:53:28Z. 18bc25c1733fd8cd749502ec5ec9333e672c7397 ［A］[^doubt-resolved-241]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：YouTube EPbVSXXeiFLgk（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Unix 传入伯克利的路径由 Bob Fabry 一人促成：Thompson 与 Ritchie 于 1973 年在 SOSP 报告第四版后，这位伯克利教授主动接触 Thompson，Unix 遂进入伯克利；系里无力独占 PDP-11/45，与数学及统计系各出资三分之一合购，后者坚持运行 DEC 系统并将机器时间切为每日三班轮转，Unix 仅获午夜至八时的时段；这一不可持续的共享安排促使计算机系很快自购 PDP-11/70，Version 6 时期 Thompson 以伯克利校友身份亲自到场安装，并因该机罕见地配有两台 28MB 磁盘而暴露并发访问竞态，由其亲手调试。（YouTube EPbVSXXeiFLgk，[406.51-593.23]，L1）[订正：原 [461.03-557.03]→[406.51-593.23]，内容复核]
- 1978 年伯克利购入第七台 VAX 供运行 Lisp 的 VAXIMA 方程求解项目，而贝尔实验室的 32V 仅是 PDP-11 版的最低限度移植，不使用 VAX 分页硬件且只支持固定数量的进程；Bill Joy 找到以虚拟内存为博士论文方向的 Ozalp Babaoglu，将其分页原型并入 32V，并利用圣诞假期这一全年仅有的独占机时反复迭代，1979 年形成 3BSD——首个包含完整操作系统与库的 BSD 发行；因内嵌大量 AT&T 代码，获取 3BSD 必须持有 AT&T 源码许可，而彼时学生身份的 Joy 兼任发行协调员，许可核验仅凭电话口头询问完成。（YouTube EPbVSXXeiFLgk，[775.03-1071.55]，L1）[订正：原 [775.03-986.15]→[775.03-1071.55]，内容复核]
- 1980 年前后 DARPA 面对承包商在机器、操作系统与编程语言上的碎片化，决定统一硬件与软件平台，选定 VAX 并在 VMS 与 Unix 的长期辩论后选择 Unix；伯克利受资助构建基本系统，取代仅能容纳 256 台主机的 NCP 的 TCP/IP 协议实现被 DARPA 交予 BBN，伯克利名义上只负责设计 socket API；DARPA 资金同时使 Joy 首次领取薪水并得以雇用专人核验 AT&T 许可——要求对方寄送许可副本并致电 AT&T 核实，结束了学生口头问询的时代。（YouTube EPbVSXXeiFLgk，[1079.23-1209.39]，L1）

**史料**：

- 本讲提供 Net-2 重写运动的第一手方法论：McKusick 与 Karels 先以 C beautifier（cb）将自有内核与 32V 源码统一为规范格式，再对 32V 建立逐行倒排数据库，将自有代码逐行比对，凡出现连续两三行匹配即判定为需要处理的 AT&T 代码残留；多数残留以更优算法（如以哈希替换进程表线性搜索）顺手重写而消除，尘埃落定时仅余约六个文件仍含实质性 AT&T 代码。（YouTube EPbVSXXeiFLgk，[2379.31-2433.63]，L1）
- 诉讼转折的一手细节：AT&T 在自身系统源码中使用了伯克利的 TCP/IP 代码却移除了版权声明，经手者已离职以致公司自身并不知情；其与 BSDi 比对源码时发现的大量共同代码，实为其取自 BSD 而未留声明的部分，该事实曝光约两年后 AT&T 意识到案件不成立，诉讼走向和解。（YouTube EPbVSXXeiFLgk，[2651.07-2684.95]，L1）[订正：原 [2651.07-2679.19]→[2651.07-2684.95]，内容复核]

**史观**：

- 总纲5 没有必然性，只有偶然性：McKusick 回忆在 Torvalds 首次公开演示 Linux（时为约一万行、刚超出终端模拟器阶段）的场合当面发问：伯克利已有 BSD，为何另起炉灶；Torvalds 答称 BSD 当时尽数卷入诉讼，“诉讼本可能走向另一边，那样就什么都不会留下，所以必须做点什么”——口述证据将 Linux 的诞生窗口归因于 USL 诉讼不确定性这一偶然条件，而非技术必然或路线优劣。（YouTube EPbVSXXeiFLgk，[2870.35-2908.43]，L1）[订正：原 [2889.43-2902.12]→[2870.35-2908.43]，内容复核]
- 总纲10 动手者创造历史：重写运动的动力机制不在 CSRG 内部而在外围无名参与者：Bostic 在 USENIX 会议张贴待重写的工具与库清单，以“贡献即可在 BSD 中留名”动员外部开发者，自 ls、cat 等简单工具做起，直至社区交付三分之二工具与近乎全部函数库，才迫使核心成员正面处理 AT&T 代码定位问题——系统摆脱专有代码依赖的进程，系由动员起来的动手者逐一重写累积而成。（YouTube EPbVSXXeiFLgk，[2303.76-2360.27]，L1）[订正：原 [2303.76-2343.27]→[2303.76-2360.27]，内容复核]

**辨析**：

- 和解条款的当事人口述版本与公开文本可互勘：条件包括在 70 个文件上补加 USL 版权声明（多为已被认定近乎公有领域的公共头文件）、删除三个文件并禁用 Net/2；McKusick 自述被删的 System V IPC、共享内存与信号量仿真实为有用代码，选择删除它们纯属让对方保留颜面——律师明言只需挑出任何三个文件以成全文义；此叙述提示和解的法律实质弱于其象征姿态，而 4.4BSD-Lite 正是以此法律清白版本的形式发行。（YouTube EPbVSXXeiFLgk，[2684.95-2774.58]，L1）

**文献**：

- [YouTube EPbVSXXeiFLgk] YouTube. YouTube: A Narrative History of BSD[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=bVSXXeiFLgk>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- PACER. Public Access to Court Electronic Records [EB/OL]. 美国联邦法院行政办公室。<https://pacer.uscourts.gov/>[EB/OL]. 2026. ［待核·needs_fix］［DKC-1287→fulltext:5856］
<!-- /dangan-20260908 -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3329 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3329`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The Making of BSD: The ACTUAL World's First Open-Source Operating System?〕讲者口述：讲者称 1992 年 USL 诉 BSDI 的诉讼提起，导致对 Net 2 发行的禁令，直至 USL 对源代码版权主张的有效性得以判定为止。（YouTube EPtuI2wX3ol2o，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3330 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3330`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The Making of BSD: The ACTUAL World's First Open-Source Operating System?〕讲者口述：讲者称该诉讼因法律地位的不确定性，使 BSD 自由软件后代的发展意外放缓了近两年；在此间歇中，不受此类法律纠纷困扰、基于 Linux 内核的系统获得了更广用户群的认同。（YouTube EPtuI2wX3ol2o，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3331 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3331`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The Making of BSD: The ACTUAL World's First Open-Source Operating System?〕讲者口述：讲者称诉讼最终于 1994 年 1 月和解、大体偏向伯克利：伯克利发行版的 18,000 个文件中仅 3 个须移除，另有 70 个经修改以加入 USL 版权注记。（YouTube EPtuI2wX3ol2o，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3332 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3332`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔The Making of BSD: The ACTUAL World's First Open-Source Operating System?〕讲者口述：讲者称和解的一个关键条款确保 USL 不得再对伯克利自有代码的用户或发行方提起诉讼，尤其涉及即将推出的 4.4BSD。（YouTube EPtuI2wX3ol2o，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
