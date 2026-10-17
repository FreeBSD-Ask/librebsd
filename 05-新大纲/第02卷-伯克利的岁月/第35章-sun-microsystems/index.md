---
chapter: 第 35 章
id: CH35
volume: 第02卷-伯克利的岁月
---

# 第 35 章 sun-microsystems

## 要点

- Sun 早期战略为 “开放系统 + 高性价比工作站”，以 32 位 Motorola 68000 处理器为基础，配 BSD 操作系统与网络功能，主攻工程与科研市场，与 DEC VAX 工作站、Apollo Computer 工作站竞争，1982-1985 年实现营收从 0 到 1 亿美元增长
- AT&T 与 Sun 合作开发 SVR4 并非 “1988.6.13 联合公告” 的单日事件，而是 1985-1992 年的多阶段连续过程：1985 年 9 月 AT&T 与 Sun 首次达成合作意向，AT&T “enlisted Sun's efforts back in 1985”（techmonitor.ai 1988-01-18 一手报道）；1987 年 4 月 AT&T 与 Sun 签订正式合作协议（多阶段时间线的第二站，继 1985 年 9 月合作意向之后）
- 1980 年代工作站技术路线分化为：通用 BSD 路线（Sun、SGI、DEC）、专用 OS 路线（Apollo Aegis、Symbolics Genera）、专有 UNIX 路线（IBM AIX、HP-UX），BSD 路线在通用性上胜出，但 1990 年代被 Linux 路线取代

| 技术路线 | 代表厂商 | 硬件基础 | 操作系统 | 市场结局 |
| --- | --- | --- | --- | --- |
| 通用 BSD 路线 | Sun、SGI、DEC | 通用 Motorola 68000 / MIPS | SunOS/BSD、IRIX、Ultrix | 1985-1990 主导工作站市场 |
| 专用 OS 路线 | Apollo、Symbolics | Apollo 专有 / Symbolics 专用 Lisp | Aegis、Genera | 1989 Apollo 被 HP 收购，1996 Symbolics 关闭 |
| 专有 UNIX 路线 | IBM、HP | IBM POWER / HP PA-RISC | AIX、HP-UX（含 BSD 部分遗产） | 1990 年代延续至今 |
| Linux 路线 | 多厂商 | 通用 x86 / RISC | Linux（继承 BSD 部分遗产） | 1995 后逐步聚合所有路线 |
- SunOS 1.0 于 **1983 年** 随 Sun-100/Sun-1 工作站系列发布，基于 4.1BSD（1981 年 6 月发布）移植到 Motorola 68000 平台，同时包含 Joy 从 CSRG 带回的部分 4.2BSD 开发版（4.1a/4.1b）特性，包含 BSD 虚拟内存、文件系统、TCP/IP 网络栈，是首个大规模商业化的 BSD 衍生操作系统
- SunOS 4.0 于 1988 年 12 月发布，融合 System V Release 3、4.3BSD 与 SunOS 自有特性，引入新的虚拟内存系统、动态链接与 System V STREAMS I/O 架构，支持 Sun386i 平台，是 Sun 在 AT&T 合作前的过渡产品；1992 年 SunOS 5.0（Solaris 2）完全转向 SVR4，标志 Sun 与 BSD 主体血缘关系的基本终结（句尾原截断，按 SunOS 5.0 完全转向 SVR4 语境补全）

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3677] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3738] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3739] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3743] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3870] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3873] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3912] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3933] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3939] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:references_fulltext:chapter_matches:chmatch_3940] 卷“第02卷-伯克利的岁月”第 35 章，匹配置信度 folder，原因：folder 第35章
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 35.12-关键词行级挖掘素材线索（8 条，CL-RM 段，见 35.12-关键词行级挖掘素材线索.md）

## 史观

- 章级史观综述：Sun 是 BSD 学术成果经商业路径放大的枢纽案例——总纲第 11 条（商品是形式主义）：SunOS 将 BSD 的学术协作成果封装为商业商品，商业化逻辑塑造了工作站市场形态；总纲第 4 条（分离聚合是永恒规律）：Sun 从 BSD 主线分离出 SunOS 商业分支，又在 SVR4 阶段与 AT&T 聚合，1992 年 SunOS 5.0 完成再分离；总纲第 5 条（没有必然性，只有偶然性）：Joy 1982 年加入 Sun 与 AT&T-Sun 多阶段合作均非注定的路径；总纲第 3 条（不存在进步，只有权力再分配）：工作站市场 BSD 路线对专用 OS 路线的“胜出”与 1990 年代被 Linux 路线取代，是权力与资源的再分配而非单向进步。各子节 35.1-35.11 的史观/辨析字段为本综述的展开依据。

## 辨析

- “开放系统” 在 Sun 语境中指 “UNIX 标准 + 开放接口”，但 SunOS 本身是专有商业产品，需区分 Sun 的 “开放” 修辞与实际授权策略
- SunOS 4.x 与 Solaris 1.x 的命名关系需核对——Solaris 1 = SunOS 4.x（BSD 基础），Solaris 2 = SunOS 5.x（SVR4 基础），须严格区分命名与基础；SunOS 4.x 在 1992-1994 年作为兼容版本保留，须区分 “主线转换”（SunOS 5.0 1991 移植 / 1992 发布）与 “兼容版本保留”（SunOS 4.x 持续供给存量用户）两件事
- 技术路线 “胜出” 的判断需区分短期（1985-1990 BSD）与长期（1995- Linux），避免线性进步史观
- SunOS 4.x 与 Solaris 1.x 的命名关系常被混淆，需核对 Sun 命名规则（Solaris 1 = SunOS 4.x；Solaris 2 = SunOS 5.x）；SunOS 4.0 基于 SVR3 而非 SVR4，SVR4 融合在 SunOS 5.0 中完成
- 需精确区分 “协议兼容” 与 “代码贡献”——Sun 开发了 NFS 协议并公开（RFC 1094, 1989），但 BSD 中的 NFS 代码由 Rick Macklem 独立实现，并非 Sun 贡献；需精确区分 “协议开源” 与 “实现开源”——Sun 通过 RFC 公开 NFS 协议规范，但 Sun 的 NFS 参考实现并未开源贡献给 CSRG。

## 文献

- Sun Microsystems 年报（1984-1986）；Joy, B. (1985) “The Network Is the Computer” 演讲原稿；Salus, P. (1994) “A Quarter Century of UNIX” ［B］
- techmonitor.ai 1988-01-18 “THE UNIX YEAR IN REVIEW – PART TWO”（techmonitor.ai/analysis/the_unix_year_in_review_part_two）；techmonitor.ai 1988-09-29 “AT&T AND SUN HOLD TECHNICAL SESSIONS ON FORTHCOMING UNIX SYSTEM V.4”（techmonitor.ai/technology/att_and_sun_hold_technical_sessions_on_forthcoming_unix_system_v4）；TUHS 邮件列表 2017-01-11 “the guy who brought up SVr4 on Sun machines”（www.tuhs.org/pipermail/tuhs/2017-January/009512.html）；SVR4 设计文档（1988）；SunOS 4.0/5.0 Release Notes；McKusick, K. (1999) “Twenty Years of Berkeley Unix”；Salus, P. (1994) “A Quarter Century of UNIX” ［A］；文献计量学分析.md Task 22（参考文献增长曲线与历史分期分布）；卷章数据映射.md 第二卷第 16 章映射条目；SQL 与 Python 查询清单.md Phase 6 文献计量学查询清单
- Ceruzzi, P. (2003) “A History of Modern Computing”；Salus, P. (1994) “A Quarter Century of UNIX”；DiBona, C. (1999) “Open Sources”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- SunOS 4.0 Release Notes（1988.12）；Sun-AT&T 合作多阶段时间线（1985.9 合作意向、1987.4 协议、1988.10 SVR4 宣布、1989 Q3 SVR4 4.0 发布）；Bach, M. (1986) “The Design of the UNIX Operating System”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix” O'Reilly Open Sources；Sandberg, R. et al. (1985) “Design and Implementation of the Sun Network Filesystem” Sun Microsystems；RFC 1094 (1989) “NFS: Network File System Protocol Specification”；Macklem, R. (1990) “The 4.3BSD-Reno NFS Implementation” ［A］
- CSRG 档案（伯克利 Bancroft 图书馆）；McKusick, K. (1999) “Twenty Years of Berkeley Unix”；USENIX 会议论文集（1984-1985） ［B］
- McKusick, K. (1999) “Twenty Years of Berkeley Unix”；USL v. BSDi 案卷；DiBona, C. (1999) “Open Sources” ［B］
- USL 诉讼档案； Sun 技术文档 ［A］
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix” O'Reilly Open Sources；RFC 1094 (1989)；RFC 1057 (1988)；Sandberg, R. et al. (1985) “Design and Implementation of the Sun Network Filesystem”；Stanford University Libraries, Special Collections (Sun Microsystems Archives)；Internet Archive sun1.sunhelp.org 镜像 ［A］
- Sun 专利申请记录（USPTO）；SunOS 源代码注释；USENIX 会议论文集（1983-1990） ［A］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP552（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人转述 Liam Proven 在 The Register 的报道：iXsystems 将重心转向基于 Debian 的 TrueNAS SCALE，FreeBSD 基底的 TrueNAS CORE 进入维持工程阶段，计划推出基于 FreeBSD 13.3 的版本后不再规划 FreeBSD 14 基底。（BSD Now EP552，[806.14-1046.26]，L2）
- 文章追述 FreeNAS 与 iXsystems 的商业谱系：FreeNAS 始于 2005 年、基于 m0n0wall 与 PHP Web 界面；iXsystems 源自曾销售 BSD/386 的 Berkeley Software Design Inc.，经与 Walnut Creek CD-ROM 合并、向 Wind River 出售 OS 部门等转手后于 2007 年收购 FreeNAS。（BSD Now EP552，[919.74-1153.86]，L2）
- 主持人介绍 Jason Eckert 的博客：1997 年 Tadpole Technologies 的 SPARCbook 3000ST 搭载 Fujitsu TurboSPARC 170MHz 处理器、128MB 内存与 Solaris 2.5.1，售价约 21000 美元，是 1990 年代高端 Unix 笔记本电脑的代表。（BSD Now EP552，[1590.02-1751.82]，L2）
- 主持人转述 Hacker News 用户评论：Ford Aerospace 是早期商业 BSD Unix 站点之一，须先向 AT&T 购买 Unix 32V 许可，再从伯克利的 Bill Joy 处取得 BSD 磁带；BSD 当时无网络，站点购买 3Com 的 UNET（Greg Shaw 所写 TCP/IP）并处理 4.3BSD 与其他实现的互操作问题，最终与 Nagle 算法的出现相关。（BSD Now EP552，[2710.40-2874.60]，L2）

**史料**：

- 本期史料包括 Liam Proven 的记者综述、Jason Eckert 的设备拆解记录，以及 Hacker News 上 Ford Aerospace 亲历者的自述评论；后两者经节目主持人口头转述。（BSD Now EP552，[806.14-2874.60]，L2）

**史观**：

- 总纲10 动手者创造历史：Ford Aerospace 工程师为网络互操作重写 UDP、ICMP 与 TCP，Nagle 算法源于一线工程实践而非纯理论推演，体现动手者创造历史。（BSD Now EP552，[2814.88-2857.92]，L2）
- 总纲3 不存在进步，只有权力再分配：iXsystems 从 BSDi 谱系转向 Linux 基底，是存储商业生态中资源与权力在平台间的重新分配。（BSD Now EP552，[806.14-1046.26]，L2）
- 总纲11 商品是形式主义：SPARCbook 以 21000 美元的高价与军事级镁合金机身成为小众商品，与廉价 PC 开放架构的对照呈现技术商品化的不同形态。（BSD Now EP552，[1647.86-1751.82]，L2）

**辨析**：

- Hacker News 评论为匿名用户自述，Ford Aerospace、3Com UNET 与 Nagle 算法的具体关联须以更多独立来源交叉验证。 [存疑脚注] 早期 TCP/IP 口述为匿名评论经节目转述，未经多源交叉验证。（BSD Now EP552，[2710.40-2874.60]，L4）
- iXsystems 转向 Linux 的时间线与版本计划来自记者报道与 Reddit 上 Chris Moore 的帖子，须以官方公告核实。 [存疑脚注] TrueNAS 路线信息来自记者报道与社区帖文，未经官方公告核实。（BSD Now EP552，[948.50-1000.66]，L4）

**文献**：

- [BSD Now EP552] Pennington J. BSD Now: 552: The Laptop Sparc[EB/OL]. (2024-03-28)[2026-08-15]. <https://www.bsdnow.tv/552>.

<!-- /PODCAST_REVIEW -->

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

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

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

