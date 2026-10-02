---
chapter: 第 30 章
id: CH30
volume: 第02卷-伯克利的岁月
---

# 第 30 章 DARPA 的选择

## 要点

- DARPA 与伯克利的合同于 1980 年 4 月开始，为期 18 个月；Bob Fabry 于 1979 年秋撰写提案，1979 年 12 月 3BSD 发布打消 DARPA 疑虑；初始合同覆盖 4BSD（1980 年 10 月）至 4.1BSD（1981 年 6 月）开发，后续由 N00039-82-C-0235 接续（2026-09-12 整改：截断按合同序列收束——批次 45 问题 1）
- UNIX V6/V7 早期信号机制（signals）为 “不可靠信号”——信号处理后系统会重置信号处理函数为默认值（SIG_DFL），导致应用程序若需重复捕获同一信号须在处理函数内重新调用 **signal(2)** 安装处理函数，存在竞争窗口（race condition）：信号可能在处理函数重置与重新安装之间到达而被默认处理（通常为终止进程）；4BSD（1980 年 10 月）起引入 reliable signals（sigblock(2)/sigvec(2)），信号处理函数不再被自动重置，竞争窗口消除——但 signal(2) 接口为兼容而保留（2026-09-12 整改：截断按 reliable signals 语境收束——批次 45 问题 2）
- BSD 在 DARPA 资助项目中占据基础性地位——Mach 基于 BSD 代码、Athena 使用 BSD 工作站，BSD 成为 DARPA 操作系统研究的公共基础设施
- DARPA 对伯克利 BSD 的评审过程并非单一时点的评标，而是贯穿 1979 年至 1985 年的多阶段过程，涉及 DARPA IPTO、伯克利 CSRG、BBN 三方的立场差异与利益博弈；评审过程可划分为五个阶段——(1) **1979 年秋招标语境评审**：DARPA 决定统一操作系统并选择 UNIX，基于其 “proven portability”（已验证的可移植性），此决策由 DARPA
- CSRG 作为 BSD 的核心组织，从 1980 年代至 1990 年代初推动了 4BSD 到 4.4BSD 的全部主要版本，是开源软件史上最成功的学术研究小组之一

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3869] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 folder，原因：folder 第30章
- [DB:references_fulltext:chapter_matches:chmatch_3885] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 folder，原因：folder 第30章
- [DB:references_fulltext:chapter_matches:chmatch_3955] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 folder，原因：folder 第30章
- [DB:references_fulltext:chapter_matches:chmatch_4162] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：Leffler 61MB（BSD C 编译器奠基）+ Shannon 47.5MB（请求分页 UNIX）；清单#32 论文源头
- [DB:references_fulltext:chapter_matches:chmatch_4164] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：Berkeley_Unix_History.pdf(2.2MB)+unixreview 1984dec(24.8MB)/1985jan(34.5MB)
- [DB:references_fulltext:chapter_matches:chmatch_4168] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：22.5MB 整期杂志
- [DB:references_fulltext:chapter_matches:chmatch_4169] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：top_level_names 显示 disk1 含 1BSD 至 4.3BSD 全部源码；Bancroft CSRG Records(#100) 数字化索引线索；非 ISO
- [DB:references_fulltext:chapter_matches:chmatch_4184] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：PSD:5 伯克利软件架构手册
- [DB:references_fulltext:chapter_matches:chmatch_4188] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：PSD:18 gprof 性能剖析
- [DB:references_fulltext:chapter_matches:chmatch_4199] 卷“第02卷-伯克利的岁月”第 30 章，匹配置信度 1.0，原因：SMM:1 系统安装
- [DB:bsdnow_podcast:outline_mappings:om_11801] BSD Now 第 487 期，匹配 CH30 章，关联度 1.0

## 史观

总纲第 3 条——不存在进步，只有权力再分配：DARPA 选择 UNIX 并资助伯克利是承包商格局与操作系统的权力再分配——BSD 由学术边缘项目跃升为 DARPA 公共基础设施；总纲第 5 条——没有必然性，只有偶然性：3BSD 发布打消 DARPA 疑虑、Joy 恰好找到 Babaoglu 分页原型等偶然节点串成资助链条；总纲第 10 条——动手者创造历史：Fabry 撰写提案、Joy 兼任发行协调并核验许可，DARPA 资助经由具体动手者的劳动转化为 BSD 产出；总纲第 13 条——法律与道德是利益分配：AT&T 许可核验、BBN 与伯克利的 TCP/IP 分工均是资助框架下的利益分配安排；总纲第 4 条——分离聚合是永恒规律：BSD 在 DARPA 框架下从 AT&T UNIX 分离而出（Net/1 起完成自由分发聚合）——与 PODCAST_REVIEW 块总纲 5/10 两条映射互证。（2026-09-12 整改：史观字段按批次 45 回填，映射依 25 条权威表）

## 辨析

- 合同开始日期确认为 1980 年 4 月（McKusick 1999 明确记载）；初始合同期限为 18 个月；4.1BSD 发布于 1981 年 6 月而非 1981 年 4 月；初始合同号 F19628-80-C-0002 与后续合同 N00039-82-C-0235（1981-1983）需区分，初始合同号 F19628-80-C-0002 经 Fabry 1980 年提案文件（DTIC ADA094691）与 McKusick 1999 记载双源印证（2026-09-12 整改：原“据一手文献印证消解^doubt-resolved-174…］”残缺矛盾标记改写为确定表述——批次 45 问题 4）
- reliable signals 并未立即 “淘汰” unreliable signals——**signal(2)** 接口在 BSD 中长期保留作为兼容层，调用 **signal(2)** 内部转换为 **sigaction(2)**，须区分 “API 接口淘汰” 与 “实现机制淘汰”；System V 采纳 reliable signals 的时间为 SVR3（1987 年前后），非 SVR
- BSD 在 DARPA 项目中的 “基础” 地位是否被高估存在争议，需核对各项目实际代码依赖
- ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 本节缺口建议中提及 “DARPA IPTO（如 Saal 视角）”，但 McKusick 1999 一手原文中未提及名为 “Saal” 的 DARPA IPTO 项目经理——McKusick 1999 明确记载的 DARPA 代表为 Duane Adams（合同监督人，contract monitor，负责 DARPA IPTO 与 CSRG 之间的合同监督联络）〔2026-09-12 整改：句末截断补全并闭合括号——批次 45 问题 7〕
- CSRG 解散时间确认为 1995 年 6 月（4.4BSD-Lite Release 2 发布后解散，McKusick 1999 明确记载），非 1992 年

## 文献

- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable", in Open Sources: Voices from the Open Source Revolution, O'Reilly, ISBN 978-1-56592-582-3；Fabry, R. S. (1980) "Proposal for Configuration Control for the ARPA Standard Version of the UNIX Operating System", DTIC ADA094691（<https://apps.dtic.mil/sti/tr/pdf/ADA094691.pdf>，元数据页面 <https://apps.dtic.mil/sti/citations/ADA094691>，访问日期 2026-07-28） ［B］
- 4BSD Release Notes (1980.10)；4BSD sigblock(2) 手册页；POSIX.1 (1988) IEEE Std 1003.1；Bach, M. J. (1986) “The Design of the UNIX Operating System”, Prentice-Hall, ISBN 0-13-201799-7；Stevens, W. R. (1992) “Advanced Programming in the UNIX Environment”, Addison-Wesley, ISBN 0-201-56317-7；McKusick, M. K. et al. (1996) “The Design and Implementation of the 4.4BSD Operating System”, Addison-Wesley, ISBN 0-201-54979-4 ［A］
- Rashid, R. et al. (1988) “Mach Architecture”；MIT Athena 项目技术报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix”；CSRG (1995) “4.4BSD-Lite Release 2 Final Report” ［B］
- Cerf, V. & Kahn, R. (1974) “A Protocol for Packet Network Intercommunication”；4.2BSD Networking Manual［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- TUHS 存档； McKusick 1999 ‘Twenty Years of Berkeley Unix’ ［B］
- FOIA 申请获取的 DARPA 档案；学术界对 DARPA 决策的二手研究［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FOIA 请求档案；BBN 历史档案（部分公开）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- BSD License (1988) 原文；McKusick, M. K. (1999) “Twenty Years of Berkeley Unix” ［B］
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix”；Quarterman, J. S. et al. (1985) “4.2BSD and 4.3BSD as examples of the Unix system”, ACM Computing Surveys 17(4): 379-418, DOI: 10.1145/6041.6043；统计分析报告：文献计量学分析.md Task 22 [R/OL]. 2026-07-27. 文件路径：**c:\Users\ykla\Documents\LibreBSD\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\文献计量学分析.md**；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**c:\Users\ykla\Documents\LibreBSD\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md**；SQL 查询：`SELECT id, gbt7714 FROM "references"` 与 `SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. 资料数据库.duckdb 与 freebsd.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase6_bibliometrics.py` Task 22 与 `script/phase1_descriptive.py` SubTask 2.1. 执行日期：2026-07-27 ［B］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：YouTube EPbVSXXeiFLgk（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Unix 传入伯克利的路径由 Bob Fabry 一人促成：Thompson 与 Ritchie 于 1973 年在 SOSP 报告第四版后，这位伯克利教授主动接触 Thompson，Unix 遂进入伯克利；系里无力独占 PDP-11/45，与数学及统计系各出资三分之一合购，后者坚持运行 DEC 系统并将机器时间切为每日三班轮转，Unix 仅获午夜至八时的时段；这一不可持续的共享安排促使计算机系很快自购 PDP-11/70，Version 6 时期 Thompson 以伯克利校友身份亲自到场安装，并因该机罕见地配有两台 28MB 磁盘而暴露并发访问竞态，由其亲手调试。（YouTube EPbVSXXeiFLgk，[461.03-557.03]，L1）
- 1978 年伯克利购入第七台 VAX 供运行 Lisp 的 VAXIMA 方程求解项目，而贝尔实验室的 32V 仅是 PDP-11 版的最低限度移植，不使用 VAX 分页硬件且只支持固定数量的进程；Bill Joy 找到以虚拟内存为博士论文方向的 Ozalp Babaoglu，将其分页原型并入 32V，并利用圣诞假期这一全年仅有的独占机时反复迭代，1979 年形成 3BSD——首个包含完整操作系统与库的 BSD 发行；因内嵌大量 AT&T 代码，获取 3BSD 必须持有 AT&T 源码许可，而彼时学生身份的 Joy 兼任发行协调员，许可核验仅凭电话口头询问完成。（YouTube EPbVSXXeiFLgk，[775.03-986.15]，L1）
- 1980 年前后 DARPA 面对承包商在机器、操作系统与编程语言上的碎片化，决定统一硬件与软件平台，选定 VAX 并在 VMS 与 Unix 的长期辩论后选择 Unix；伯克利受资助构建基本系统，取代仅能容纳 256 台主机的 NCP 的 TCP/IP 协议实现被 DARPA 交予 BBN，伯克利名义上只负责设计 socket API；DARPA 资金同时使 Joy 首次领取薪水并得以雇用专人核验 AT&T 许可——要求对方寄送许可副本并致电 AT&T 核实，结束了学生口头问询的时代。（YouTube EPbVSXXeiFLgk，[1079.23-1209.39]，L1）

**史料**：

- 本讲提供 Net-2 重写运动的第一手方法论：McKusick 与 Karels 先以 C beautifier（cb）将自有内核与 32V 源码统一为规范格式，再对 32V 建立逐行倒排数据库，将自有代码逐行比对，凡出现连续两三行匹配即判定为需要处理的 AT&T 代码残留；多数残留以更优算法（如以哈希替换进程表线性搜索）顺手重写而消除，尘埃落定时仅余约六个文件仍含实质性 AT&T 代码。（YouTube EPbVSXXeiFLgk，[2379.31-2433.63]，L1）
- 诉讼转折的一手细节：AT&T 在自身系统源码中使用了伯克利的 TCP/IP 代码却移除了版权声明，经手者已离职以致公司自身并不知情；其与 BSDi 比对源码时发现的大量共同代码，实为其取自 BSD 而未留声明的部分，该事实曝光约两年后 AT&T 意识到案件不成立，诉讼走向和解。（YouTube EPbVSXXeiFLgk，[2651.07-2679.19]，L1）

**史观**：

- 总纲5 没有必然性，只有偶然性：McKusick 回忆在 Torvalds 首次公开演示 Linux（时为约一万行、刚超出终端模拟器阶段）的场合当面发问：伯克利已有 BSD，为何另起炉灶；Torvalds 答称 BSD 当时尽数卷入诉讼，“诉讼本可能走向另一边，那样就什么都不会留下，所以必须做点什么”——口述证据将 Linux 的诞生窗口归因于 USL 诉讼不确定性这一偶然条件，而非技术必然或路线优劣。（YouTube EPbVSXXeiFLgk，[2889.43-2902.12]，L1）
- 总纲10 动手者创造历史：重写运动的动力机制不在 CSRG 内部而在外围无名参与者：Bostic 在 USENIX 会议张贴待重写的工具与库清单，以“贡献即可在 BSD 中留名”动员外部开发者，自 ls、cat 等简单工具做起，直至社区交付三分之二工具与近乎全部函数库，才迫使核心成员正面处理 AT&T 代码定位问题——系统摆脱专有代码依赖的进程，系由动员起来的动手者逐一重写累积而成。（YouTube EPbVSXXeiFLgk，[2303.76-2343.27]，L1）

**辨析**：

- 和解条款的当事人口述版本与公开文本可互勘：条件包括在 70 个文件上补加 USL 版权声明（多为已被认定近乎公有领域的公共头文件）、删除三个文件并禁用 Net/2；McKusick 自述被删的 System V IPC、共享内存与信号量仿真实为有用代码，选择删除它们纯属让对方保留颜面——律师明言只需挑出任何三个文件以成全文义；此叙述提示和解的法律实质弱于其象征姿态，而 4.4BSD-Lite 正是以此法律清白版本的形式发行。（YouTube EPbVSXXeiFLgk，[2684.95-2774.58]，L1）

**文献**：

- [YouTube EPbVSXXeiFLgk] YouTube. YouTube: A Narrative History of BSD[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=bVSXXeiFLgk>.

<!-- /PODCAST_REVIEW -->