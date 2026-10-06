---
chapter: 第 63 章
id: CH63
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 63 章 386bsd时代的法律诉讼与反向工程先例

## 要点

- Sega v. Accolade（1992）案的判决确立了反向工程目标代码以获取互操作性接口规范构成 fair use 的先例，对 1990 年代 PC 游戏兼容、Unix 工具开发、BSD 与 Linux 二进制兼容性等场景具有深远影响；判决成为后续 Sony v. Connectix 等案的基础
- USL 和解协议公开前，BSD 史学叙事中存在两种简化版本——BSD 一方叙事倾向于 “USL 完全败诉、BSD 完全胜诉”，USL 后继方叙事倾向于 “USL 通过和解保护了 UNIX 知识产权”；2004 年协议公开后，史学叙事得以重塑——和解实为 “复杂妥协”：Net/2 大部分代码保留（仅 3 文件移除）但同时 70 文件添加 USL 版权声明，双方均未承认对方主张，且关键事实（V32 版权瑕疵）被保密条款封存；该重塑使 BSD 起源叙事更接近历史复杂性，但仍受保密条款残留约束
- 386BSD 0.1（1992.7）发布后因 Jolitz 单人维护补丁积压，**1993 年 6 月 19 日** FreeBSD 项目 fork 386BSD 创建（Nate Williams、Rodney Grimes、Jordan Hubbard、David Greenman 4 人组），**FreeBSD 1.0**（1993.11）发布，主攻 Intel x86 PC 平台；**1993 年 4 月** NetBSD 0.8 发布（Chris Demetriou、Theo de Raadt、Adam Glass（亚当·格拉斯）、Charles Hannum 4 人组），主攻多平台移植（SPARC、Alpha、PowerPC、m68k 等），虽基于 386BSD 部分代码但更早脱离 386BSD 单人维护模式；**1995 年 10 月** OpenBSD 从 NetBSD 1.0 fork（Theo de Raadt 因与 NetBSD Core Team 冲突被驱逐后创建），主攻安全审查与代码质量；386BSD 单人维护模式在 1993-1995 年被 “淘汰” 为 FreeBSD/NetBSD/OpenBSD 三大 BSD fork 演化路径，386BSD 本身因 Jolitz 维护停滞而逐步衰落，1995 年后基本停止开发；FreeBSD/NetBSD/OpenBSD 三大 fork 形成 BSD 三大分支格局，分别主攻 PC 性能（FreeBSD）、多平台移植（NetBSD）、安全审查（OpenBSD），延续至 21 世纪；386BSD → 三大 fork 的演化路径是 BSD 从 “单一项目” 到 “多元分支” 的关键转型，后被 DragonFly BSD（2003 年从 FreeBSD 4.x fork，Matthew Dillon（马修·狄龙） 创建）等进一步分化
- Linux 1-2 月/版本、Minix 2-3 年/版本、Coherent 1-2 年/版本、386BSD 1-2 年后停滞；发行节奏的差异直接决定了开发者社区规模与生态增长速度。同期操作系统发行节奏对照如下：

| 项目 | 发行周期 | 维护模式 | 治理结构 |
| -- | ------ | ------ | ------ |
| Linux 0.01-0.99 | 1-2 月/版本 | 社区驱动 | 林纳斯·托瓦兹主导 |
| Minix 1.5 | 2-3 年/版本 | 单一维护者 | Tanenbaum 教学定位 |
| Coherent | 1-2 年/版本 | 商业公司 | Mark Williams Company |
| ISC UNIX | 受商业周期约束 | 商业公司 | Interactive Systems Corporation |
| 386BSD | 1-2 年后停滞 | 单一维护者 | Jolitz 夫妇 |
- 386BSD 0.1 是 OpenBSD 1.0（1996-07，从 NetBSD 1.0 fork）的间接前身——OpenBSD 通过 NetBSD 1.0 间接继承 386BSD 安全基线，但 OpenBSD 1.0 的直接基线是 NetBSD 1.0（1994，基于 4.4BSD-Lite），而非 386BSD 0.1；1994 年 6 月 4.4BSD-Lite 发布后，FreeBSD 2.0（1994-11）与 NetBSD 1.0（1994）均 rebase 至 4.4BSD-Lite，386BSD 作为直接安全基线的地位被 4.4BSD-Lite 取代；4.4BSD-Lite 引入 securelevel 内核安全等级机制（level 0/1/2 分级约束 root 用户运行时特权），是 386BSD 安全基线未包含的新机制；OpenBSD 1996 年 fork 后的全代码审计工程可视为对 386BSD 安全基线缺陷（4.3BSD 网络栈远程漏洞面、单 `/etc/passwd` 无 shadow password）的激进回应

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10562] BSD Now 第 651 期，匹配 CH63 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11009] BSD Now 第 586 期，匹配 CH63 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11400] BSD Now 第 541 期，匹配 CH63 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11618] BSD Now 第 514 期，匹配 CH63 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11660] BSD Now 第 507 期，匹配 CH63 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12201] BSD Now 第 446 期，匹配 CH63 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12520] BSD Now 第 418 期，匹配 CH63 章，关联度 1.0

## 史观

（章级史观/辨析按子节字段聚合回填——本卷 63 章；2026-09-11 整改将占位改为编排说明，完整聚合随正文阶段逐章完成。子节级映射详见各节史观字段。）

## 辨析

- 判决先例的适用范围在不同司法管辖区（第九巡回 vs 其他）需对照后续判例核验
- ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ “BSD 一方叙事” 与 “USL 后继方叙事” 的代表性作品需对照具体史学文献核验，避免稻草人化；2004 年协议公开后史学叙事的 “重塑” 程度需通过 2004 年前后史学作品的文本对照量化评估；保密条款残留约束的具体范围（哪些事实仍被法律约束）需法律专家持续跟踪
- 386BSD 被 “淘汰” 为三大 fork 指 386BSD 单人维护模式主导地位退场，386BSD 代码本身部分被 FreeBSD 1.0 继承（基于 386BSD 0.1 + 4.4BSD-Lite），须区分 “维护模式退场” 与 “代码继承”；NetBSD 0.8（1993.4）与 FreeBSD 1.0（1993.11）的关系需核对——两者均基于 386BSD 但 NetBSD 更早脱离
- 发行节奏快是否必然导致生态增长需谨慎归因，Linux 1.0 后的商业化支持也是关键因素
- 386BSD 安全基线对 OpenBSD 的传承须区分 “直接继承” 与 “间接继承”——OpenBSD 1.0 通过 NetBSD 1.0 fork 间接继承 386BSD 安全基线，但 OpenBSD 1.0 的直接基线是 NetBSD 1.0（基于 4.4BSD-Lite），而非 386BSD 0.1；386BSD 作为直接安全基线的地位被 4.4BSD-Lite 取代的考据基于 FreeBSD 2.0（1994-11）与 NetBSD 1.0（1994）均 rebase 至 4.4BSD-Lite 的事实

## 文献

- Sega v. Accolade 977 F.2d 1510；Sony v. Connectix 203 F.3d 596；Maureen O'Rourke “Drawing the Boundary Between Copyright and Contract”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］<!-- NEWREF:2432 -->
- McKusick, M. K. (1999) “Twenty Years of Berkeley Unix”（in Open Sources, O'Reilly）；2004 年后 BSD 史学论文（如 Ceruzzi, Campell-Kelly 等修订版作品）；Groklaw 2004 年公开文件；BSD 史学评论文献 ［B］
- 386BSD Release Notes；FreeBSD/NetBSD/OpenBSD/DragonFly BSD fork 公告；Jolitz 单人维护记录；FreeBSD/NetBSD/OpenBSD Core Team 档案；Rodney W. Grimes. Initial import, 0.1 + pk 0.2.4-B1. freebsd-src [DB/OL]. 1993-06-12T14:49:13Z. 9002c02abc587664acb357c6879d8ca08664dd0b；cgd. initial import of 386bsd-0.1 sources. netbsd-src [DB/OL]. 1993-03-21T09:45:37Z. 0d110d127c41d7aeb2b1bfdc71964c5a496eabf9；deraadt. initial import of NetBSD tree. openbsd-src [DB/OL]. 1995-10-18T08:37:01Z. df930be708d50e9715f173caa26ffe1b7599b157；Jordan K. Hubbard 在 freebsd-src 的首次 commit. freebsd-src [DB/OL]. 1993-06-18T04:22:21Z. （netbsd.duckdb contributors 表）；deraadt 在 netbsd-src 的末次 commit. netbsd-src [DB/OL]. 1994-12-17T23:12:41Z. 699d2a37b0e3c0c6ff29ea0d407c3feeba5642b4；本项目。netbsd.duckdb 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］
- 各项目 release notes；Eric S. Raymond “The Cathedral and the Bazaar” (1997)［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- OpenBSD 1.0 Release Notes (1996.7)；NetBSD 1.0 Release Notes (1994.10)；4.4BSD-Lite Release Notes (1994.6)；4.4BSD SMM: 16《On the Security of UNIX》；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading, MA: Addison-Wesley, 1996. ISBN 0-201-54979-4 ［A］[^doubt-resolved-264][^doubt-resolved-265]
- Lotus Dev. Corp. v. Borland Int'l, Inc., 49 F.3d 807 (1st Cir. 1995) & 516 U.S. 233 (1996)；Oracle Am., Inc. v. Google Inc., 750 F.3d 1339 (Fed. Cir. 2014)；Google LLC v. Oracle America, Inc., 593 U.S. 1 (2021)；Sega Enterprises, Ltd. v. Accolade, Inc., 977 F.2d 1510 (9th Cir. 1992)；CSRG Net/2 重写工程记录 ［A］<!-- NEWREF:2362 --><!-- NEWREF:2363 --><!-- NEWREF:2364 --><!-- NEWREF:2365 --><!-- NEWREF:2366 --><!-- NEWREF:2367 --><!-- NEWREF:2368 --><!-- NEWREF:2369 -->
- ORACLE USA, Inc. v. SAP AG, No. 4:07-cv-01658 (N.D. Cal.)[Z/OL]. 美国加州北区联邦地区法院，2007-2014. <https://www.courtlistener.com/docket/>；Oracle Corp. v. SAP AG, 2011 WL 3861945 (N.D. Cal. 2011)（Hamilton 法官减赔令）；Oracle America, Inc. v. SAP AG, 765 F.3d 1080 (9th Cir. 2014)（第九巡回 3.567 亿美元裁定） ［A］<!-- NEWREF:2389 --><!-- NEWREF:2390 --><!-- NEWREF:2391 --><!-- NEWREF:2437 -->

[^doubt-resolved-264]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解
[^doubt-resolved-265]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

