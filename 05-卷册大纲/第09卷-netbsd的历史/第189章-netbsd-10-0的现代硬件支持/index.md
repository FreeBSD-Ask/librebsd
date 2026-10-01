---
chapter: 第 189 章
id: CH189
volume: 第09卷-netbsd的历史
---

# 第 189 章 netbsd-10-0的现代硬件支持

## 要点

- NetBSD 10.0（**2024.3.31**）引入对 Apple Silicon M1/M2 的实验性支持，由 Jared McNeill（jmcneill）、Nick Hudson（skrll）、Ryo Shimizu（ryo）等共同推动；移植工作最早可追溯至 2021-08-30（jmcneill“Identify Apple M1 ‘Icestorm’ and ‘Firestorm’…”）
- NetBSD 10.0 硬件支持 commit 记录是研究现代硬件移植的核心史料；Jared McNeill、Taylor R Campbell 等是主要贡献者；考据需对照 CVS commit log 与硬件厂商文档
- pkgsrc 2010-2026 年间的 commit 记录与季度发布说明是研究 pkgsrc 现代演进的核心史料；Joerg Sonnenberger、Thomas Klausner（托马斯·克劳斯纳） 等是主要维护者；考据需对照 CVS commit log 与 pkgsrc-doc 邮件列表
- tainted code 政策公告与邮件列表讨论是研究政策出台过程的核心史料；公告由 Core Team 发布，邮件列表讨论涉及 committer、用户、外部观察者；考据需对照公告原文与邮件列表存档
- NetBSD Foundation 年报与 IRS 990 表是研究 Foundation 治理与财务的核心史料；年报记录 Foundation 治理、资金收支、项目进展；IRS 990 表是法律要求的非营利组织税务披露；考据需对照原始 PDF 与 IRS 数据库

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4003] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4004] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4005] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4006] 卷“第09卷-netbsd的历史”第 189 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲第 10 条——动手者创造历史：Apple Silicon M1/M2 的实验性支持由 jmcneill、skrll、ryo 等动手者在 CVS commit 层面接续完成，pkgsrc 的现代演进亦由 Sonnenberger、Klausner 等维护者的具体劳动推动，现代硬件支持史首先是这些动手者的历史
- 总纲第 9 条——经验优先：移植时间线、发布日期与政策出台过程均以 commit log、官方发布页面与公告原文为断代依据，二手转述（如先前叙事中的 “2024.5” 误传）一律回溯一手记录核验
- 总纲第 22 条——知识注定过时：硬件兼容性列表与内核支持范围随版本迭代迅速过时，本所述支持广度仅为 NetBSD 10.0 时点的快照

## 辨析

- 经 netbsd.duckdb netbsd-src 仓库 commits 表验证：Apple Silicon M1 移植最早可追溯至 2021-08-30（jmcneill），早于 10.0 发布 2024.3.31 约 2 年 7 个月；移植由 jmcneill（2021-2022）、skrll（2022）、ryo（2022）等人接续完成——jmcneill 于 2021-08-30 提交 Apple M1 初始支持（commit db7e12da2c51），skrll 于 2022 年 4-5 月补齐电源域控制器、GPIO、邮箱通信通道、I2C 与 RTKit SMC 等驱动，并自 OpenBSD 移植 Apple silicon NVME 支持（2022-05-07，commit e24a9df7237c），移植时间线延续至 10.0 发布前
- 先前叙事中称“NetBSD 10.0 发布日期 2024.5”系误传——NetBSD 官方发布页面（netbsd.org/releases/formal-10/NetBSD-10.0.html）明确为 2024.3.31；10.0 的实际硬件支持广度需对照硬件兼容性列表核验
- pkgsrc 软件包数量增长在不同来源中存在差异——2010Q1 与 2026Q4 的具体数字需对照原始 release tarball 核验；Sonnenberger 的 commit 量在统计工具中可能被低估
- 政策公告的具体发布日期在不同来源中可能略有差异——需对照 NetBSD 官方页面核验；外部媒体报道可能存在简化或误解
- NetBSD Foundation 年报的连续性在 2010-2026 年间可能存在缺口——部分年份的报告未公开发布；IRS 990 表的具体条目需对照 IRS 数据库核验

## 文献

- NetBSD 10.0 Release Notes；CVS commit log；tech-kern 邮件列表；NetBSD 官方发布历史页面（<https://www.netbsd.org/releases/formal.html>） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2024-2024 年间：29,047 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- pkgsrc CVS 仓库；pkgsrc 季度发布说明；pkgsrc-doc 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2010-2026 年间：892,617 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Core Team 公告；tech-kern 邮件列表；外部媒体报道 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：NetBSD 特性
- NetBSD Foundation 年报；IRS 990 表；members 邮件列表 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2010-2026 年间：892,617 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD core 邮件列表；Core Team 决议记录；NetBSD Foundation 年度报告 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2010-2026 年间：892,617 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- LWN 文章档案；Phoronix BSD 文章；OSNews NetBSD 评论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD CVS 仓库统计；邮件列表存档；BSDCan/AsiaBSDCon 演讲视频档案 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 10.0 Release Notes；CVS commit log；NetBSD/doc/PLATFORMS；rin. Add nvme(4) and raid(4). netbsd-src 仓库 [DB/OL]. 2020-11-10T08:52:36Z. commit: 571f6efb48f0；riastradh. nvme(4): Add suspend/resume, derived from OpenBSD. netbsd-src 仓库 [DB/OL]. 2021-05-29T08:46:38Z. commit: a6e80066045f；msaitoh. Add VMware AHCI and NVMe. netbsd-src 仓库 [DB/OL]. 2022-02-15T12:01:28Z. commit: 90fc9574253f；skrll. Add support for Apple silicon NVME. Ported from OpenBSD. netbsd-src 仓库 [DB/OL]. 2022-05-07T08:20:03Z. commit: e24a9df7237c；jmcneill. Add initial support for Apple M1. netbsd-src 仓库 [DB/OL]. 2021-08-30T23:26:26Z. commit: db7e12da2c51；skrll. Add support for the power domain controller found in Apple silicon machines. netbsd-src 仓库 [DB/OL]. 2022-04-27T07:55:42Z. commit: 4f480f1af932；skrll. Add a driver for the Apple GPIO controller found in Apple silicon. netbsd-src 仓库 [DB/OL]. 2022-04-27T07:59:18Z. commit: 4989e6f446f2；skrll. Add support for the mailbox that provides a communications channel with additional cores. netbsd-src 仓库 [DB/OL]. 2022-04-27T08:06:20Z. commit: 09966de28c10；skrll. Add a driver for the Apple M1 I2C controller. From OpenBSD. netbsd-src 仓库 [DB/OL]. 2022-05-10T08:05:32Z. commit: 33e6c36315e1；skrll. Add a driver for the Apple RTKit based System Management Controller found on M1 SoCs. netbsd-src 仓库 [DB/OL]. 2022-05-10T08:09:57Z. commit: 11f1e5f671ec；riastradh. Define pci_is_thunderbolt_attached (answer: no). netbsd-src 仓库 [DB/OL]. 2021-12-19T01:48:12Z. commit: edb5cae246b4 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP360（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 追查坏提交的文章介绍用 git bisect 二分定位引入回归的提交，并指出破坏可能来自非直观的依赖变更。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 完成 2020 年第十一届 Core 团队选举，Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Kyle Evans、Mark Johnston、Scott Long、Sean Chittenden、Warner Losh 当选。（BSD Now EP360，[460.69-614.65]，L2）
- NetBSD 在 Pinebook Pro 上以 NetBSD 9 用户态搭配 Current 内核运行，以兼顾二进制包与更好的硬件支持。（BSD Now EP360，[624.57-842.58]，L2）
- pf 状态表存在默认大小限制，FreeBSD 另有 `net.pf.request_maxcount` sysctl 控制单次 ioctl 载入表项数；DragonFly 侧限制为静态内核值。（BSD Now EP360，[1199.40-1404.41]，L2）

**史料**：

- 追查坏提交博文与 git bisect 说明。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 2020 年 Core 团队选举公告，由主持人转述当选名单。（BSD Now EP360，[460.69-614.65]，L2）

**史观**：

- 总纲10 动手者创造历史：FreeBSD 决策由“到场者”作出，主持人与提问者强调社区参与决定项目走向。（BSD Now EP360，[481.5-503.3]，L2）[订正：原 [2452.99-2456.55]（错挂片尾音乐段），2026-10-01 交叉核验订正——总纲10 内容真实出处为 481.5-503.3 段（core 团队九人自荐、社区九票多数当选），片尾 2443.1-2547.8 经两次转写均无语音产出判定为收播曲]
- 总纲4 分离聚合是永恒规律：Core 团队成员更替体现治理层的分离与再聚合。（BSD Now EP360，[460.69-614.65]，L2）

**辨析**：

- DragonFly 的 pf 表限制是静态内核值且未暴露为可调 sysctl，是否需要仿照 FreeBSD 改造仍待确认。　[存疑脚注] DragonFly 侧改造计划待核实（BSD Now EP360，[1360.80-1390.40]，L4）

**文献**：

- [BSD Now EP360] Pennington J. BSD Now: 360: Full circle[EB/OL]. (2020-07-23)[2026-08-15]. <https://www.bsdnow.tv/360>.

<!-- /PODCAST_REVIEW -->
