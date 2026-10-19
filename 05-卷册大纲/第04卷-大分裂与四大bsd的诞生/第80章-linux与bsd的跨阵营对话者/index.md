---
chapter: 第 80 章
id: CH80
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第80章 linux与bsd的跨阵营对话者

## 要点

- 跨阵营对话者包括同时贡献 Linux 与 BSD 的开发者——如 Alan Cox 早期参与 NetBSD 的 USB 子系统讨论、Theodore Ts'o 在 Linux 与 BSD 文件系统层面的技术交流、Marshall Kirk McKusick（马歇尔·柯克·麦库西克） 跨阵营讲授 BSD 文件系统；跨阵营对话者构建技术交流桥梁
- 被忽视的 BSD 推广者包括——长期撰写 BSD 教程的社区成员（如 Dru Lavigne 在 FreeBSD 新闻网的教程）、组织 BSD 大会的志愿者、翻译 BSD 文档的非英语社区成员；推广者的贡献常被技术叙事忽视
- 被遗忘的贡献者辨析须识别两类——“技术贡献被低估”（如补丁作者、文档作者，其工作可经 bsd_commits.duckdb commit 数与邮件列表补丁提交记录量化）与“非技术贡献被忽视”（如组织者、翻译者、调解者，其工作须从 BSD 大会组织档案与非英语 BSD 社区档案挖掘）；两类贡献者的史料都须从原始档案主动挖掘，不得仅依赖主流叙事
- 边缘贡献者的史料辨析须经三类史料交叉验证——技术贡献（bsd_commits.duckdb 代码提交、BSD 邮件列表补丁提交记录）、文化贡献（BSD 教程存档如 Dru Lavigne FreeBSD 新闻网教程、BSD 文档如 Handbook 与 FAQ、BSDCon 演讲存档）、组织贡献（BSD 大会组织记录、非英语 BSD 文档翻译项目、社区调解邮件存档）；三类史料须交叉验证，不得仅依赖代码提交记录评估贡献
- 本节基于 79 项文化挪用案例（60 项 BSD 直接挪用 + 18 项非 BSD 系统挪用 + 1 项许可证概念挪用）的考据事实，从 31.1 至 31.6 的 “结构性对比” 向 “具体技术证据” 作纵深扩展，选取 18 项代表性案例归纳为 4 种模式——淡化源头模式、重写即归属模式、概念更名模式、发行版与社区文化重塑模式；4 种模式并非相互排斥而是经常在同一案例中相互渗透，形成 “叠加效应”；“平行演化与扩展超越” 作为 4 种模式的混合形态，在 BSD 与 Linux 同期演化的工具中尤为常见。4 种挪用模式归纳如下：

## 史观

- 总纲第 10 条——动手者创造历史：跨阵营对话者作为技术交流的边缘动手者，构建 Linux 与 BSD 阵营的桥梁
  - 辨析：跨阵营对话者的具体贡献在不同叙事中差异较大——部分强调技术交流（Alan Cox 早期参与 NetBSD USB 子系统讨论、Theodore Ts'o 在 Linux 与 BSD 文件系统层面的技术交流），部分强调社区调解（McKusick 跨阵营讲授 BSD 文件系统）；经原始邮件存档（NetBSD USB 邮件列表、Linux 内核邮件列表、BSDCon 演讲存档）核实，两类贡献均有据可循。
- 总纲第 11 条——商品是形式主义：4 种挪用模式本质上是 BSD 端技术经 Linux 端“形式主义化”后封装为“开源软件商品”的权力运作过程；总纲第 17 条——证明世界先于解释和改造世界：考据的首要任务是“证明 BSD 端的先验存在”；总纲第 22 条——知识注定过时：Linux 端主流叙事建构的“Linux 原生”知识“注定过时”，数字档案将持续证明 BSD 端的先验存在
- 总纲第 15 条——文化即形式主义：BSD 端的“ports 文化”“rc.d 文化”“man 文化”在 Linux 端“形式主义化”过程中被遮蔽与重构——“ports”被更名为“package manager”、“init script”被更名为“unit”、“man”被竞争为“man 与 GNU info”，传统在更名与重构中被遮蔽；“知音难觅”同样适用于技术社区——Coggeshall 与 Spencer、Terry 等 4 人、Watson 与 Anderson 等一手作者姓名在 Linux 端主流叙事中几近缺席。

## 辨析

- 跨阵营对话者的具体贡献在不同叙事中差异较大——部分强调技术交流（Alan Cox 早期参与 NetBSD USB 子系统讨论、Theodore Ts'o 在 Linux 与 BSD 文件系统层面的技术交流），部分强调社区调解（McKusick 跨阵营讲授 BSD 文件系统）；经原始邮件存档（NetBSD USB 邮件列表、Linux 内核邮件列表、BSDCon 演讲存档）核实，两类贡献均有据可循

- 本节遵循 0 信任原则与三次复查流程，所有事实以一手学术论文、CSRG 档案、设计者一手公告、**man7.org** / **freebsd.org** 一手手册页、互联网档案馆存档为交叉锚，禁用维基百科与百度百科；案例编号引用规则——BSD 直接案例以“BSD 案例 N”标注（编号 1-60），非 BSD 系统案例以“非 BSD 案例 N”标注（编号 1-18），许可证概念案例以“许可证案例 N”标注（编号 1）；本节不使用“Linux 是掠夺者”“Linux 盗窃 BSD”等道德判断性表述，以考据证据呈现文化挪用现象。
- 三重机制的“同时运作”非“依次发生”——在 BSD 案例 7（jail → Docker → OCI）中，来源淡化（PHK 1999 设计被“Solomon Hykes 2013 Docker 创新”叙事取代）、记忆抹除（Docker 重写为 libcontainer 与 runc，原作者被替换为重写者）、话语重塑（OCI 2015-12-08 加入 Linux Foundation 托管，以“开源通用遗产”包装具体的项目出身）三重机制在同一案例中同时运作而非依次发生。

## 文献

- 跨阵营对话者访谈；技术交流邮件存档 ［A］

## 80.10.2 被忽视的 BSD 推广者

- 要点：被忽视的 BSD 推广者包括——长期撰写 BSD 教程的社区成员（如 Dru Lavigne 在 FreeBSD 新闻网的教程）、组织 BSD 大会的志愿者、翻译 BSD 文档的非英语社区成员；推广者的贡献常被技术叙事忽视
- 史料：Dru Lavigne FreeBSD 教程存档；BSD 大会组织记录；非英语 BSD 文档翻译项目 ［A］
- 史观：总纲第 10 条——动手者创造历史：推广者作为社区文化的边缘动手者，其贡献常被技术叙事忽视但实际承载文化传承
- 辨析：被忽视的推广者须具体考据——部分推广者在小众社区贡献巨大（如 Dru Lavigne 在 FreeBSD 新闻网长期撰写 BSD 教程、非英语 BSD 社区翻译者将 BSD 文档译为中文、日文、俄文等），但因不在主流叙事中而被忽视；经小众社区记录（FreeBSD 新闻网存档、BSD 大会组织记录、非英语 BSD 文档翻译项目档案）核实，推广者贡献在文化传承维度有据可循。
- 原材料/研究/linux 文化挪用/ 全部案例文件与模式总结、史学映射、嵌入建议；一手学术论文与 CSRG 档案 ［A］

## 80.11.2 淡化源头模式典型案例

- 要点：淡化源头模式指 Linux 端主流叙事通过 man page、官方文档、培训教材、社区话语四个渠道，将 BSD 端的一手作者、起源日期、概念先验地位系统性隐去，使读者形成“该工具或概念起源于 Linux 端”的误判；本目选取 BSD 案例 1（sudo）、BSD 案例 14（Berkeley sockets）、BSD 案例 23（BIND）、BSD 案例 57（sysctl）、BSD 案例 56（Capsicum）、BSD 案例 16（MCS 锁）6 项典型案例。
- 原材料/研究/linux 文化挪用/模式总结.md；BSD 案例 1、23、7、22、59 案例文件；一手 man page 与培训教材档案；GPL 许可证原文；Linux Foundation 与 BSD Foundation 章程 ［A］

## 80.12.2 遮蔽不等于盗窃——形式主义权力运作的辨析

- 要点：文化挪用的遮蔽本质须与道德意义上的“盗窃”明确区分——遮蔽是形式主义的权力运作，指 Linux 端主流叙事通过 man page、官方文档、培训教材、社区话语等渠道，将 BSD 端的一手作者、起源日期、概念先验地位系统性隐去的形式主义过程；“盗窃”是道德判断，预设了“财产权”的明确边界与“窃取”的主观恶意；BSD 许可证本身允许自由使用、修改、再分发，Linux 端使用 BSD 代码在法律层面不构成“盗窃”；但法律层面的“允许使用”不等于叙事层面的“归属公正”。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP345、BSD Now EP335（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- NetBSD 8.2 作为 8.x 树的第三个点版本发布，聚合此前安全修复与旧硬件引导、Hyper-V、EFI 等改进。（BSD Now EP345，[81.96-118.92]，L2）
- 本期主体是 JT 征集的社区反馈：多位听众讲述从 Linux 转投 BSD 的经历，涉及 systemd 反感、PF 抗攻击、ZFS 回滚与 BSD 社区友好度。（BSD Now EP345，[1090.66-1183.78]，L2）
- 许可证争论在反馈中被表述为‘BSD 许可证是温和路径、GPL 是强制路径’的对立，主持人回应两者在自由目标上同路。（BSD Now EP345，[1188.74-1223.54]，L2）
- Deb Goodkin 与 FreeBSD Foundation 在 Linux Conf AU 内组织首个 FreeBSD mini-conf，Ben Woods、Peter Grehan 等演讲者出席。（BSD Now EP335，[1272.54-1399.32]，L2）
- Hyperbola 联合创始人 Andre 解释弃 Linux 内核的原因：HDCP 等 DRM、GRSecurity 停止公开补丁、Rust 商标限制，并计划 fork OpenBSD 内核。（BSD Now EP335，[419.28-605.24]，L2）
- JT 对‘从 Linux 迁移到 BSD’一文四个论点逐条反驳：Linux 碎片化被高估、商业介入非坏事、社区优劣是比例问题、许可证争论难有定论。（BSD Now EP335，[1941.52-2505.94]，L2）

**史料**：

- NetBSD 8.2 发布公告（Maya Rashish 撰写），列出安全修复与引导改进。（BSD Now EP345，[81.96-118.92]，L2）
- 听众来信中的亲身经历：Debian 防火墙受攻击、改用 OpenBSD 与 PF 后稳定、再以 FreeBSD 与 ZFS 搭存储。（BSD Now EP345，[1722.54-1828.54]，L1）
- FreeBSD 打包故事：陌生人在作者完成 Debian 打包前即已将其应用打包进 FreeBSD。（BSD Now EP345，[1257.9-1307.1]，L1）
- Ruben 撰写的澳大利亚 FreeBSD mini-conf 回顾，含演讲者名单与议题。（BSD Now EP335，[1272.54-1438.44]，L2）
- It's FOSS 的 John Paul 对 Hyperbola 联合创始人 Andre 的访谈。（BSD Now EP335，[419.28-426.72]，L2）
- Kamil Rytarowski 的 NetBSD 博客：改进 ptrace API 并为 LLVM 10 做准备。（BSD Now EP335，[935.22-964.18]，L2）

**史观**：

- 总纲6 和解优于斗争：总纲6 和解优于斗争：听众与主持人共同主张 Linux 与 BSD 目标相同、应减少阵营内耗，以展示各自优势代替互相贬低。（BSD Now EP345，[1151.7-1183.78]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：对 Linux 与 BSD 的许可证、社区规模比较被归结为不同哲学路径，而非优劣高下。（BSD Now EP345，[1188.74-1223.54]，L2）
- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：Hyperbola 的 fork 决策围绕 GPL、四条款 BSD 与 CDDL 的兼容性展开，许可证成为利益与自由的分配工具。（BSD Now EP335，[672.14-806.78]，L2）
- 总纲6 和解优于斗争：总纲6 和解优于斗争：JT 主张以正面理由论证 BSD 而非贬低 Linux，正面论证优于负面论证。（BSD Now EP335，[1971.68-1991.92]，L2）

**辨析**：

- 转写中多名写信人姓名与内容混杂（如‘Jason’ 与‘Jamie’ 指代可能互换），引用社区反馈时须以原邮件为准。 [存疑脚注] 转写写信人姓名存疑（BSD Now EP345，[1113.94-1225.54]，L4）
- Hyperbola 拟 fork OpenBSD 内核的计划被主持人质疑为工作量巨大、可持续性存疑，属开放性争议而非定论。 [存疑脚注] Hyperbola BSD 计划可行性存疑（BSD Now EP335，[829.34-903.78]，L3）

**文献**：

- [BSD Now EP345] Pennington J. BSD Now: 345: Switchers to BSD[EB/OL]. (2020-04-09)[2026-08-15]. <https://www.bsdnow.tv/345>.
- [BSD Now EP335] Pennington J. BSD Now: 335: FreeBSD Down Under[EB/OL]. (2020-01-30)[2026-08-15]. <https://www.bsdnow.tv/335>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1008 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1008`；w172 YouTube 章节路由采纳）

据〔服务器迁移讲座〕讲者 Stefan 口述：BSD 常用特性含 ZFS、Bhyve（转写音作 Behive）与 jail；DragonFly BSD 另有 Hammer 2 文件系统。（YouTube EPUnVp25-6Qao，[2028.08-2038.95]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1129 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1129`；w172 YouTube 章节路由采纳）

据〔BSD 4 Linux Users (October 2009)〕讲者口述：BSD 各发行版均提供 binary emulation，可在 BSD 上直接运行 Linux、Solaris、SCO 二进制文件。（YouTube EPxk6ouxX51NI，[1177.2-1191.6]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1130 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1130`；w172 YouTube 章节路由采纳）

据〔BSD 4 Linux Users (October 2009)〕讲者口述：ZFS 与 DTrace 已内建 FreeBSD；OpenBSD 提出了开放冗余协议 CARP。（YouTube EPxk6ouxX51NI，[1194.1-1209.9]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2729 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2729`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD from a Linux developer's perspective（D Scott Phillips，Intel）讲者口述：其笔电上 FreeBSD 的空闲功耗比 Linux 高 50–100%，等于损失四分之一到一半的电池续航；元凶是若干设备始终停在最高功耗状态。（YouTube EPml8vo1FWT1I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2730 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2730`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD from a Linux developer's perspective（D Scott Phillips）讲者口述：Wi-Fi 稳定性很好、吞吐却低；他把差异归因于 Linux 得到厂商第一方驱动（自启自家芯片），而 FreeBSD 没有同等待遇。（YouTube EPml8vo1FWT1I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2731 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2731`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD from a Linux developer's perspective（D Scott Phillips）讲者口述：文档上 FreeBSD 领先 Linux——一处集中生长的文档使内容更一致、更有信息量；对照 Linux 侧只有企业发行版零散的手册。（YouTube EPml8vo1FWT1I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2732 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2732`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD from a Linux developer's perspective（D Scott Phillips）讲者口述：补丁尺寸分布上两个项目几乎一样——一半的改动约六行、四分之三在约 25 行内；差别全在顶部 1% 的大改动上。（YouTube EPml8vo1FWT1I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2826 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2826`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD coming from a Linux user（Toshaan Bharvani，EuroBSDcon 2022）讲者口述：其作为 Linux 用户进入 BSD 社区时受到相当容易的接纳，讲题意在点出差异与可改进之处。（YouTube EPs1FLwHpiufA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
