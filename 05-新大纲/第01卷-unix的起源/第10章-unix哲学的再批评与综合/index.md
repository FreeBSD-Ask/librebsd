---
chapter: 第 10 章
id: CH10
volume: 第01卷-unix的起源
---

# 第 10 章 UNIX 哲学的再批评与综合

## 要点

- 1973 年 UNIX V4 引入多用户分时后，root（UID 0）与普通用户的二元特权模型成为系统安全的核心结构；root 拥有绕过文件权限检查、绑定特权端口、执行关键系统调用等全部特权，普通用户权限受 9 位 rwx 权限位约束；该模型将 Multics 的环形保护（ring 0-7）与可信计算基（TCB）极简化为二元判定，符合 UNIX“做一件事并做好”的工程哲学
- UNIX 密码存储历经三阶段演化——V1-V3（1971-1973）存储于 `/etc/passwd`、V4-V6（1973-1975）尝试简单加密（ROT13 等被快速攻破）、V7（1979 年）引入基于 DES 25 轮迭代的 **crypt(3)** 与 12 位 salt 机制；1978-1979 年间 UNIX V6 密码文件被攻破事件直接触发 V7 密码散列升级；**crypt(3)** 由 Robert Morris（罗伯特·莫里斯）与 Ken Thompson 共同设计，使相同密码因不同 salt 产生不同散列，抵御预计算字典攻击
- Morris & Thompson 1979 年 CACM 论文《Password Security: A Case History》是密码散列演化的最权威学术记录，原作于 1978-1979 年间，描述了 UNIX V1 至 V7 密码存储方案的全部演化过程；该论文后被 4.4BSD 系统管理员手册第 17 章（SMM: 17）再版，成为 BSD 谱系密码安全的权威一手史料；论文记录了多种早期方案被攻破的过程，最终在 V7 引入 DES **crypt(3)** 与 12 位 salt
- root 二元特权模型与 DES **crypt(3)** 散列机制共同构成 Research UNIX 留给 BSD 的两大安全基因——root 模型延续至 4.4BSD-Lite 与 386BSD，**crypt(3)** 直接被 FreeBSD 1.0-4.x 继承直至 1990 年代末被 MD5-based **crypt(3)** 与 bcrypt 替代；root 模型的“全有或全无”缺陷催生 BSD 后世 **jail(8)**（4.4BSD-Lite2 后 FreeBSD 引入）、**securelevel(7)**、Capsicum（Watson et al. 2010）等细粒度特权机制；**crypt(3)** 的 salt 思想影响后续 bcrypt、scrypt、argon2 等现代密码散列设计
- UNIX 哲学（小工具 + 管道）与 Multics（统一抽象）、VMS（工程实用）、Lisp Machine（语言即系统）形成四路分野；UNIX 路线在 1980 年代后随 BSD/System V 扩散占据主流
- UNIX 哲学文本的塑造者包括 McIlroy、Pike、Kernighan、Raymond 等，但还包括 Bell Labs 内部通信参与者、USENIX 演讲者、邮件列表讨论者；多数边缘塑造者姓名未被记录

## 史观

- 实践先于理论：root 模型在缺乏形式化安全规格下演化定型，工程实践先于安全理论总结；哲学思潮：二元特权模型为 UNIX 极简化哲学在安全维度的工程转译
- 偶然性改写历史：1978-1979 年 V6 密码文件攻破事件偶然触发 V7 散列升级，重塑 UNIX 密码安全范式；软件工程：**crypt(3)** 的设计与 salt 机制为密码安全工程提供范本
- 实践先于理论：Morris & Thompson 论文是对 V1-V7 密码演化的事后理论总结，工程实践（攻破-升级循环）先于学术记录；边缘者贡献：Robert Morris 作为 Bell Labs 安全研究者，其贡献长期被 Ritchie/Thompson 的光环遮蔽
- 总纲第 4 条——分离聚合是永恒规律：root 模型与 **crypt(3)** 在 V7 定型后延续至 BSD 长达二十余年，是 Research UNIX 主导期终结后 BSD 分支延续的核心安全遗产；四路分野（UNIX/Multics/VMS/Lisp Machine）的分离在此时期完成，UNIX 路线聚合 BSD 与 System V 两条支流为下一时期奠基
- 边缘者贡献：UNIX 哲学非个人著作，而是集体讨论的结晶

## 辨析

- root 模型定型的精确版本（V3 vs V4）需考据——按 Ritchie 1984 BLTJ 与 Salus 1994 两方独立来源交叉印证为 V4（1973 年）多用户分时引入后；“1972 年定型”的说法缺乏一手史料佐证[^doubt-resolved-55]；root 模型的优势在于实现简洁、性能开销低，缺陷在于 root 一旦失陷即全系统失陷，是 BSD 后世 **jail(8)**、**securelevel(7)**、Capsicum 等机制试图弥补的史源
- [考据脚注：经 Morris & Thompson 1979 CACM 论文一手表述确证，DES **crypt(3)** 引入于 1979 年 V7，而非 1976 年；V1-V3 明文存储的说法存在叙事分歧，部分来源指向 V4 起已有简单加密，穷尽考据后仍无法确证；salt 机制的设计灵感来源（是否受 IBM VM/370 密码机制影响）需进一步考据——已尝试多组关键词检索均未找到确证证据。]
- CACM 1979 论文与 4.4BSD SMM: 17 是否完全一致需对照——SMM: 17 可能含 4.4BSD 时期的补充说明；Morris & Thompson 1979 论文中描述的“V6 密码文件被攻破”事件的具体细节（攻破者身份、攻破方法）需考据；论文中提及的早期方案（ROT13 等）是否真在 V4-V6 中部署存在回忆差异风险
- root 模型与 **crypt(3)** 对 BSD 安全基因的“史源意义”是否被夸大需辨析——BSD 安全基因亦受 Multics 间接影响（详见本章对 Multics 统一抽象路径的比较）与 4.2BSD 网络栈引入后的安全扩展影响；**crypt(3)** 被 MD5/bcrypt 替代的确切时间需考据（FreeBSD 4.x 时期引入 MD5-based，OpenBSD 率先引入 bcrypt）
- Multics 统一抽象是否真的“过度”存在 Multics 阵营的辩护；UNIX 的简化是否真的“妥协”存在 UNIX 阵营的坚持
- VMS 工程实用主义是否在 1980 年代企业市场击败 UNIX 需考据；VMS 与 Windows NT 的承继需辨析；[考据脚注] VMS 发布日期经 HP OpenVMS 30 周年页面确证，另以 kiwix.kenryu.us VAX-11 条目〔禁引来源·仅作线索·不得直接采信〕作辅助线索对照——VMS 于 1977 年 10 月 25 日与 VAX-11/780 同期发布
- Lisp Machine 商业失败是技术原因还是商业原因需辨析——Symbolics 1982 年封闭软件后社区生态崩塌；Stallman 发起 GNU 运动与 Symbolics/LMI 之争的直接因果关系需考据；首台 3600 交付日期（1982.12）与 3600 系列正式发布（1983）两个时间节点需区分
- UNIX 哲学是否“胜出”存在争议——Windows NT（VMS 血统）、Lisp（函数式）在不同领域延续；**统计局限性标注**——references 表 16,867 条中仅 7,493 条（44.42%）成功提取年份，统计结论限于文献计量学层面，不可外推至代码活跃度；0 信任原则适用——`gbt7714` 字段为自由文本，年份正则可能误匹配 ISBN、页码、卷号中的数字
- 边缘塑造者的具体贡献难以量化；0 信任原则要求不臆测贡献归属
- Raymond 的运动化传播是否“代表”UNIX 哲学本身存在学术批评；McIlroy 对 Raymond 的态度需考据；经 freebsd.duckdb 查询未得明确证据（查询条件：`SELECT * FROM commits WHERE repo_name='freebsd-src' AND message_subject LIKE '%McIlroy%'`），freebsd.duckdb 不含 Bell Labs 内部哲学文献数据，暂保留存疑
- 每阶段“加入”了什么需逐阶段考据；叙事形成是否为线性存在争议
- 回忆的可靠性需与一手档案交叉验证；哪些 Bell Labs 档案已数字化公开需查 AT&T Archives 在线目录

## 文献

- Ritchie D M 1984“The Evolution of the Unix Time-sharing System”（AT&T Bell Laboratories Technical Journal 63 No. 6 Part 2 pp. 1577-1593）；4.4BSD SMM: 16《On the Security of UNIX》；Salus 1994“A Quarter Century of UNIX”；freebsd.duckdb：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12，Initial import 含 root UID 0 特权判定代码）［A］
- Morris R, Thompson K 1979 CACM“Password Security: A Case History”Vol. 22 No. 11 pp. 594-597；4.4BSD SMM: 17《Password Security: A Case History》；UNIX V7 源代码 `usr/src/lib/crypt.c`；**docs.freebsd.org/44doc/smm/17.password/**；Salus 1994 ［A］
- Watson et al. 2010“Capsicum: Practical Capabilities for UNIX”（USENIX Security）；Poul-Henning Kamp 1998 MD5-crypt；Provos & Mazières 1999 bcrypt；freebsd.duckdb：freebsd-src commit `5b81b6b301437eb9a6df491c829475bd29ae5d6c`（1993-06-12）与 `26f9a76710a312a951848542b9ca1f44100450e2`（1994-05-25）［A］
- Organick 1972“The Multics System”；Corbató & Vyssotsky 1965 AFIPS；Multics MSPM；DEC VMS Manual (1977)；Kashtan 1980 RSI report；Cutler 1988 VMS to NT 演化记录；HP OpenVMS 30 周年页面（**h71000.www7.hp.com/openvms/30th/**）［B］
- Moon 1985 ISCA“The Architecture of the Symbolics 3600”pp. 76-83；Moon 1987 IEEE Computer“Symbolics Architecture”Vol. 20 No. 1；Stallman 1985 GNU Manifesto；Levy 1984“Hackers: Heroes of the Computer Revolution”［B］
- Ceruzzi 2003“A History of Modern Computing”；Campbell-Kelly & Aspray 1996；Raymond 2003；**资料数据库.duckdb** 文献计量学统计（C-41、C-42）；统计分析报告：`03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/文献计量学分析.md` Task 22（查询日期 2026-07-27）［A］
- TUHS 邮件列表早期帖；USENIX ; login: 期刊；Kernighan 2019 ［A］
- 同 10.8.1；Campbell-Kelly 2007 综述 ［C］
- Salus 1994；Campbell-Kelly 2007；Raymond 2003 附录 [考据脚注：经 Salus 1994“A Quarter Century of UNIX”与 Campbell-Kelly 2007 原著交叉验证确证。]
- TUHS 邮件列表；AT&T Archives 在线目录；USENIX ; login: 期刊早期卷期 ［A］

[^doubt-resolved-55]: 据 losh-hidden_early_history_of_unix-slides (fosdem, 2020) 消解

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP513、BSD Now EP485（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 新主持人 Jason Tubner 自述从业经历：约 2000 年经同事 Steve Nunez 赠予的 OpenBSD 2.8 光盘接触 BSD，此前学习 Solaris 并从事系统管理与存储咨询，此后成为 BSD 长期使用者与布道者。（BSD Now EP513，[315.3-418.6]，L1）[订正：原 [325.74-418.48]，2026-10-01 SenseAudio 重转核对]
- 其所在的澳大利亚非营利社区健康服务机构以 FreeBSD 与 OpenBSD 混合部署，用 bhyve 在通用硬件上承载 VPN 网关与 Windows 补丁分发设备，并通过生产使用向 BSD 项目反馈缺陷，形成使用、报错、修复、再使用的循环。（BSD Now EP513，[480.5-714.3]，L1）[订正：原 [480.56-712.56]，2026-09-30 SenseAudio 重转核对]
- 节目转述 su 降权文章，指出 su 的功能是提升而非降低权限，其被用于降权的误用源自 1986 年 Fielder 与 Hunter 著作及流传教程；自 1997 年 daemontools 的 setuidgid 起已有专用降权工具，PAM 的引入进一步改变其行为。（BSD Now EP513，[1574.8-1934.6]，L2）[订正：原 [1576.30-1933.64]，2026-09-30 SenseAudio 重转核对]
- 新闻部分报道 OpenBSD dt 动态追踪设备于 6.7 首次出现并逐步获得工具支持，以及 LibreSSL 3.6.3、3.7.3 与 3.8.0 开发版的发布，并介绍 FreeBSD 12 起的手工 jail 部署流程。（BSD Now EP513，[1947.4-2641.0]，L2）[订正：原 [1953.10-2632.10]，2026-10-01 SenseAudio 重转核对]
- 该期以技术新闻为载体，实质触及三条史学线索：awk 等脚本语言在 Unix 早期的设计逻辑、OpenBSD 以 mimmutable 为代表的系统调用级内存保护推进，以及对 Unix 技术史演进的年代学反思。（BSD Now EP485，[838.82-1430.78]，L2）
- 主持人转述 Dan Langille 的教程，指出 Home Assistant 默认面向容器或 pip 安装，在 FreeBSD jail 中按传统方式部署需补装 Rust、Pillow、SQLite 等依赖，折射出开源项目向容器化打包收敛的普遍趋势。（BSD Now EP485，[579.66-836.38]，L2）

**史料**：

- OpenBSD 2.8 光盘为当事人 Jason Tubner 的个人入门一手经历，经当期采访自述。（BSD Now EP513，[375.2-418.6]，L1）[订正：原 [389.32-404.68]，2026-10-01 SenseAudio 重转核对]
- Fielder 与 Hunter 1986 年著作被节目指为 su 降权误用的历史文本来源之一，属于经主持人转述的二手史料线索。（BSD Now EP513，[1574.8-1604.8]，L2）[订正：原 [1583.36-1600.52]，2026-10-01 SenseAudio 重转核对]
- setuidgid（daemontools，1997 年发布，最初称 setuser）及其克隆工具的谱系，作为 su 专用降权替代工具的历史证据，经节目转述。（BSD Now EP513，[1833.0-1898.1]，L2）[订正：原 [1858.80-1896.40]，2026-10-01 SenseAudio 重转核对]
- Brian Kernighan 接受 PLDB 访谈，自述 awk 的核心想法是关联数组，并强调 yacc 与 lex 降低了语言实验的语法与词法成本，属当事人一手史料。（BSD Now EP485，[900.9-960.12]，L1）
- Theo de Raadt 在 OpenBSD tech 邮件列表总结 mimmutable 内存保护工作，Otto Moerbeek 跟进 malloc 数据结构的只读与不可变改造，属一手邮件史料。（BSD Now EP485，[1051.28-1141.08]，L1）

**史观**：

- 总纲第 10 条——动手者创造历史：生产使用者通过报错与反馈参与 BSD 演进，默默做事的使用者同样是历史主体——Jason 及其机构以生产使用向 BSD 项目反馈缺陷，BSD 的完善来自使用者的动手反馈而非单向的官方规划。（BSD Now EP513，[602.8-714.3]，L1）[订正：原 [629.78-712.56]，2026-10-01 SenseAudio 重转核对]
- 总纲第 9 条——经验优先：以实机安装与生产使用的经验作为选择操作系统的依据——Jason 的个人路径由 Solaris、Linux 到 OpenBSD 光盘的实机经验驱动，其判断以实际使用而非抽象宣传为依据。（BSD Now EP513，[315.3-418.6]，L1）[订正：原 [325.74-418.48]，2026-10-01 SenseAudio 重转核对]
- 总纲第 8 条——本体论上各方平等：各 BSD 分支按工具适配性平等参与生产部署，不预设等级次序——机构同时使用 FreeBSD 与 OpenBSD 并按具体任务选型，而非只认同单一 BSD 分支。（BSD Now EP513，[180.2-225.0]，L1）[订正：原 [193.80-222.84]，2026-10-01 SenseAudio 重转核对]
- 总纲第 10 条——动手者创造历史：Brian Kernighan 等动手者通过小语言与工具设计塑造 Unix 生态，其访谈表明语言设计经验优先于既有参照，属动手者创造历史的直接例证。（BSD Now EP485，[929.9-962.12]，L1）
- 总纲第 18 条——时间是一种形式主义：Chris Siebenmann 判断 Unix 技术史大体定格于 1990 年代，用户层体验三十年间变化有限，恰与时间作为形式主义的史观呼应：技术演进并非线性进步，而是特定年代结构的沉淀。（BSD Now EP485，[1160.36-1293.24]，L2）

**辨析**：

- 关于 su 降权误用的历史叙述将 Fielder 与 Hunter 1986 年著作视为源头之一，但该书是否确实传播该误用、以及 su 语义演化的精确时间线，需结合 4.4BSD 手册与 PAM 引入记录核验。 [存疑脚注] su 语义演化时间线为单一文章转述，未给出原始手册或提交编号，须交叉验证。（BSD Now EP513，[1574.8-1800.0]，L4）[订正：原 [1583.36-1788.98]，2026-10-01 SenseAudio 重转核对]
- OpenBSD dt 设备在 6.7 中悄然进入源码树的说法为节目转述，其首次引入版本与功能范围需以 OpenBSD 发布说明与提交记录确认。 [存疑脚注] dt 的引入版本与早期功能缺乏当期节目的一手出处，须以官方发布说明核验。（BSD Now EP513，[1947.4-2003.8]，L4）[订正：原 [1963.84-1978.36]，2026-10-01 SenseAudio 重转核对]
- Siebenmann 对 1990 年代后 Unix 技术变化趋缓的判断系个人观察，未提供系统比较证据，属单一来源推断。 [存疑脚注] Unix 技术史年代学判断需与内核、文件系统、网络栈的量化演进对照验证。（BSD Now EP485，[1160.36-1293.24]，L4）
- 转写将 OpenBSD 的 mimmutable 系统调用描述为接近完成最后一步，但该机制当时的合入状态与后续实际发布版本需考据确认。 [考据脚注] mimmutable 具体合入版本与发布时间需查 OpenBSD 发行说明与源码提交记录。（BSD Now EP485，[1073.7-1151.56]，L4）

**文献**：

- [BSD Now EP513] Pennington J. BSD Now: 513: New Host Interview[EB/OL]. (2023-06-29)[2026-08-15]. <https://www.bsdnow.tv/513>.
- [BSD Now EP485] Pennington J. BSD Now: 485: FreeBSD Home Assistant[EB/OL]. (2022-12-15)[2026-08-15]. <https://www.bsdnow.tv/485>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

