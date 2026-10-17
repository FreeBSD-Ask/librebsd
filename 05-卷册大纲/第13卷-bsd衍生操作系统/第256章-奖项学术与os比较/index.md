---
chapter: 第 256 章
id: CH256
volume: 第13卷-bsd衍生操作系统
---

# 第 256 章 奖项、学术与 OS 比较——BSD 荣誉史、学术引用与桌面 BSD 失败对比

## 要点

- FreeBSD 基金会与 FreeBSD 项目历年获得的奖项包括——2005 年 OSCON 开源奖项（Open Source Award）；2014 年 iXsystems 与 FreeBSD Foundation 获得的 InfoWorld Bossie Awards（最佳开源存储与服务器）；2019 年 FreeBSD Foundation 获得 Sovereign Tech Fund 资助
- NetBSD 项目获得的奖项包括——2006 年 NetBSD 3.0 获得 OSNews 评选的最佳开源操作系统提名；2010 年 NetBSD 5.1 获得 Slashdot 评选的最佳服务器操作系统提名；NetBSD 的可移植性纪录（运行于 50+ 硬件平台）曾获吉尼斯世界纪录认证。NetBSD 项目的奖项相对较少，反映其在主流市场的边缘地位。
- OpenBSD 项目获得的奖项包括——2004 年 OpenSSH 获得 USENIX STUG Award（Software Tools User Group Award）；OpenBSD 的安全审计方法论多次被信息安全社区表彰；OpenSSH 作为全球 SSH 事实标准，间接为 OpenBSD 项目带来声誉。OpenBSD 项目的奖项相对较少，Theo de Raadt（西奥·德·若特） 个人对奖项的公开态度须以原始声明为据（本节辨析层已列考据任务）〔2026-09-12 整改：句尾截断按批次 C092 指引收束〕
- CSRG 时期 BSD 获得的奖项（1980-1990 年代学术与工业界的若干提名与共享声誉）在 BSD 整体奖项谱系中具有承前启后的位置——承前于 CSRG 作为伯克利学术研究小组在系统研究社区的学术声誉，启后于 CSRG 解散后 FreeBSD/NetBSD/OpenBSD 各项目独立发展后的现代奖项谱系。CSRG 时期奖项的形式主义辨析须注意——奖项作为学术与工业界的认可形式，其“认可”在实质内容与形式仪式之间存在张力（见要点末条辨析）〔2026-09-12 整改：句尾截断收束〕
- BSD 奖项的辨析须避免两种极端——其一，以奖项数量判断项目价值（Linux 奖项多于 BSD 故 Linux 优于 BSD），其二，以反奖项姿态否定奖项价值（OpenBSD 反奖项故奖项无意义）。奖项作为形式主义操作，其“认可”在实质内容上既有真实成分（FreeBSD 获 Sovereign Tech Fund 资助反映其工程价值），也有形式主义成分（奖项的颁发常受政治与商业影响）。BSD 奖项谱系的书写本身即形式主义化的选择——入选与忽略均为编纂行为〔2026-09-12 整改：句尾截断收束〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4073] 卷“第13卷-bsd衍生操作系统”第 256 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4074] 卷“第13卷-bsd衍生操作系统”第 256 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

总纲第 15 条——文化即形式主义：奖项系开源社区认可机制的形式主义化仪式——奖牌、公告与典礼是社区价值的形式化载体，其与工程实质的关系正是本章辨析对象（据要点末条）；总纲第 3 条——不存在进步，只有权力再分配：奖项的授予与缺席反映社区内部与工业界话语权的再分配——获奖记录是权力地图而非价值排序（据要点 FreeBSD/OpenBSD 对照）；总纲第 7 条——理论必须自反：以奖项数量判定项目价值与以反奖项姿态否定奖项价值是同构的两极，均须自反（据要点辨析条）；总纲第 23 条——一切历史写作都是基于哲学设定的历史小说：奖项谱系的书写（入选/忽略/分期）本身是编纂者的叙事选择。（2026-09-12 整改：史观字段按批次 C092 回填，映射依 25 条权威表；细节见 256.10-256.12 各节）

## 辨析

- FreeBSD 奖项的具体年份与颁发机构须以原始公告为准；OSCON 2005 年奖项的具体内容须考据；Sovereign Tech Fund 2024 年资助金额经联网核查确认为 €686,400（非任务描述的 €666,000），公告时间 2024-08-26，专项用于基础设施现代化（Zero Trust Builds、CI/CD Automation、Reduce Technical Debt）〔2026-09-12 整改：截断补全并闭合括号〕
- NetBSD 奖项的具体年份与颁发机构须以原始公告为准；吉尼斯世界纪录 NetBSD 条目须考据（可能不再活跃）
- USENIX STUG Award 2004 年公告须以原始公告为准；Theo de Raadt 对奖项的态度须以公开声明为据
- CSRG 时期奖项的具体列举与考据归入 CSRG 教育与文化章，本节仅做谱系位置辨析，避免重复；“形式与实质张力”的判断须以具体奖项案例为基础；“学术声誉转向社区认可”的判断须有 BSD 项目演化的事实支持
- 奖项数量与项目价值的关系须警惕简化判断；用户文章的论断须按 0 信任原则考据

## 文献

- FreeBSD Foundation 奖项公告；OSCON 档案；InfoWorld 档案；FreeBSD Foundation. Sovereign Tech Fund to Invest €686,400 in FreeBSD Infrastructure Modernization [EB/OL]. 2024-08-26. <https://freebsdfoundation.org/blog/sovereign-tech-fund-to-invest-e686400-in-freebsd-infrastructure-modernization/> （访问日期 2026-07-22）；Sovereign Tech Fund. FreeBSD Project [Z/OL]. <https://www.sovereigntechfund.de/projects/freebsd>（访问日期 2026-07-22，原始链接失效，互联网档案馆无存档） ［A］
- NetBSD 奖项公告；OSNews/Slashdot 档案；吉尼斯世界纪录档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- USENIX STUG Award 公告；OpenBSD 声明；信息安全社区表彰档案 ［B］
- CSRG 时期奖项档案；CSRG 解散后 BSD 各项目奖项档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- BSD/Linux 奖项档案；奖项研究文献；用户文章［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1993-2026 年间：1,294,851 次提交（2026-09-12 整改：原“1985”系注入纪元错误，仓库 commit 起始为 1993-06-12）。
- McKusick 1996；Capsicum 论文；CHERI 论文；HAMMER 文档；bhyve 论文 ［B］（2026-09-12 整改：原文献区粘接的旧章号子节标题 8 处（255.10.2-255.10.5、255.11.2-255.11.5）系旧章机械拼接残留，已清除留痕；对应内容现属 256.10/256.11 节文件）
- SOSP/OSDI/USENIX 论文档案 ［B］
- 4.2BSD TCP/IP 文档；Jacobson 1988 论文；BBR 论文 ［B］
- FFS/LFS/ZFS/HAMMER 论文与文档 ［B］
- 学术论文批评档案；BSD 前沿研究案例 ［B］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。
> 1985-2026 年间：963,557 次提交。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-13-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-13-043`；login 逐条遍历判定采纳）

2000 年第四届 Annual Linux Showcase & Conference 由 USENIX 与志愿者社区合办，设 Hack Linux、Use Linux、Extreme Linux（集群与高性能计算）三个技术轨道，超过 80 家厂商参展，反映 2000 年前后 Linux 会议生态与商业化规模。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-13-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-13-043`；login 逐条遍历判定采纳）

2000 年第四届 Annual Linux Showcase & Conference 由 USENIX 与志愿者社区合办，设 Hack Linux、Use Linux、Extreme Linux（集群与高性能计算）三个技术轨道，超过 80 家厂商参展，反映 2000 年前后 Linux 会议生态与商业化规模。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-13-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-13-043`；login 逐条遍历判定采纳）

2000 年第四届 Annual Linux Showcase & Conference 由 USENIX 与志愿者社区合办，设 Hack Linux、Use Linux、Extreme Linux（集群与高性能计算）三个技术轨道，超过 80 家厂商参展，反映 2000 年前后 Linux 会议生态与商业化规模。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-13-043 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-13-043`；login 逐条遍历判定采纳）

2000 年第四届 Annual Linux Showcase & Conference 由 USENIX 与志愿者社区合办，设 Hack Linux、Use Linux、Extreme Linux（集群与高性能计算）三个技术轨道，超过 80 家厂商参展，反映 2000 年前后 Linux 会议生态与商业化规模。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1287 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1287`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：Kim McMahon 来自 FreeBSD 基金会，他与一位数字安全设计领域的获奖者共同出席。（YouTube EP8eNDkPFRKRc，[0.6-7.7]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-762 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-762`；w172 YouTube 章节路由采纳）

据讲者口述：FreeBSD 的功能来源颇为混合——packet filter（转写音作 pcket filter）源自 OpenBSD，DTrace 与 ZFS 则取自 Solaris，此外还包括 bhyve（转写音作 beehive）与 Zen 等自研组件。（YouTube EPMQaEUj9bDyU，[145.04-155.229]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-761 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-761`；w172 YouTube 章节路由采纳）

据讲者口述：Ted Mittelstaedt（转写音作 Ted middl sets）大约在 2000 年前后撰写的 FreeBSD Corporate Networker's Guide，正值 FreeBSD 的 jail 技术刚问世之初，讲者称不少听众仍记得这本书。（YouTube EPMQaEUj9bDyU，[79.72-88.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1360 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1360`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Michael Dexter《Lessons from the CFT Lab》欧洲 BSD 会议演讲〕讲者口述：BSD（与 illumos 一并讨论）是能够获得完整操作系统栈的路径：可以在任意层动手改动、与同层同事协作、修复并改进，把某处小改动做成一次会议报告乃至一份职业；讲者称这“是绝对关键的”，并称这些系统的一致性、文档以及“镜头背后的 Unix”（how the system works）就是计算机本来的工作方式。（YouTube EP03hwVHqGnsw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1361 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1361`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Michael Dexter《Lessons from the CFT Lab》欧洲 BSD 会议演讲〕讲者口述：讲者回顾：早在 2003 年他第一次接触 FreeBSD 的 jail 时，便想到把 sendmail 可执行文件连同少量依赖抛进 jail，即可得到一个只做一件事的邮件服务器。这是他自述以 jail 作为“单一职责”容器化用法的起点；同段口述另指出 FreeBSD 的 build options 可声明“纳入什么、不要什么”，可借此做减法。（YouTube EP03hwVHqGnsw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1362 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1362`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Michael Dexter《Lessons from the CFT Lab》欧洲 BSD 会议演讲〕讲者口述：讲者称 FreeBSD 13 在“显而易见与非显而易见的层面”都是里程碑：它汲取上游 OpenZFS、包含可重现构建（reproducible builds）、从 git 获取，并强调它“有可用的 build options”，还重复一遍以突出此前这一能力长期不可用。（YouTube EP03hwVHqGnsw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1363 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1363`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Michael Dexter《Lessons from the CFT Lab》欧洲 BSD 会议演讲〕讲者口述：讲者口述：zfs set readonly=on 可让数据集免费获得不可变（immutability）属性，取代过去“卸载文件系统、再重新挂载”的旧做法，而且“随时随处、免费”。讲者把不可变与勒索软件防护挂钩，称缓解建议的首要两条是保持系统更新与让数据不可变，因为读不了的东西难以被加密。（YouTube EP03hwVHqGnsw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
