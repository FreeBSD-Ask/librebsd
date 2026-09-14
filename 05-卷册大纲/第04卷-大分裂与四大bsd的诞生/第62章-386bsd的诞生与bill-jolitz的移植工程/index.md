---
chapter: 第 62 章
id: CH62
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 62 章 386BSD 的诞生与 Bill Jolitz 的移植工程

## 要点

- 386BSD 是首个能在普通 PC 上运行的免费 32 位 BSD 系统，证明 BSD 内核可在 commodity x86 硬件上稳定运行；其 MI/MD 分层设计为后续 FreeBSD/NetBSD 的多平台架构奠定了基础；Net/2 + 386BSD 的组合为 USL 诉讼后 BSD 重建提供了法律清白的代码基础
- DDJ 连载使 386BSD 在国际技术社区获得知名度，吸引荷兰、澳大利亚、日本等地开发者尝试；连载附带的源码磁盘与 ftp.cs.berkeley.edu 镜像共同构成早期 386BSD 的分发渠道
- 补丁维护者群体逐渐独立运作，形成 unofficial patchkit；用户群开始流失至 Linux 与其他 BSD 雏形；386BSD 的滞后直接催生了 1993.6 FreeBSD 与 1993.4 NetBSD 的 fork
- patchkit 维护者希望以 6 个月或更短周期发布，Jolitz 夫妇坚持 “ready when ready” 的长周期；386BSD 0.1（1992 年 7 月）到 1.0（1994 年末）间隔超过 2 年，期间无任何公开版本发布（**无 0.2 公开版本**），与 patchkit 群体的节奏预期差距巨大
- Salon 专访对 Jolitz 夫妇评价复杂——既承认其作为 BSD 在 386 平台先驱的历史地位，也暗示其在社区协作上的局限；专访引发 FreeBSD 社区对自身起源叙事的反思

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10561] BSD Now 第 651 期，匹配 CH62 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11008] BSD Now 第 586 期，匹配 CH62 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11399] BSD Now 第 541 期，匹配 CH62 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11617] BSD Now 第 514 期，匹配 CH62 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11659] BSD Now 第 507 期，匹配 CH62 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12200] BSD Now 第 446 期，匹配 CH62 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12519] BSD Now 第 418 期，匹配 CH62 章，关联度 1.0

## 史观

- 总纲第 10 条——动手者创造历史：Jolitz 夫妇的移植工程使 BSD 落地普通 PC，无名维护者群体以 patchkit 接力
- 总纲第 4 条——分离聚合是永恒规律：unofficial patchkit 自 386BSD 分离，聚合为 FreeBSD 与 NetBSD
- 总纲第 3 条——不存在进步，只有权力再分配：发布节奏之争实为维护权与起源叙事权的再分配
- 总纲第 7 条——理论必须自反：Salon 专访引发 FreeBSD 社区对自身起源叙事的反思

## 辨析

- 386BSD 与 FreeBSD 1.0 代码共享比例存在不同估计——FreeBSD Project 倾向强调自身独立性，Jolitz 夫妇则强调 FreeBSD 大量继承 386BSD 代码，需对照源码 diff 独立核验
- 386BSD 0.1 的 “250000 次下载” 或 “175000 张光盘” 数字在不同来源中差异巨大，需考据是 FTP 下载次数还是 CD-ROM 销量
- FreeBSD fork 的具体动机在不同叙事中权重不同——FreeBSD Project 强调 “社区驱动”，Jolitz 夫妇强调 “窃取用户群”，需对照原始邮件列表
- Jolitz 夫妇声称节奏放缓是为等待 4.4BSD-Lite 及应对 USL 诉讼法律风险，但 4.4BSD-Lite 1994 年 6 月发布后 386BSD 1.0 于 1994 年末才发布，且基于 0.1 而非 4.4BSD-Lite，需考据真实原因；原文献引用 “Lynne Jolitz Salon (1999)” 为错误信息
- 专访对 Jolitz 的评价是否 “中立” 存在争议——FreeBSD 社区认为专访偏向 Jolitz，Jolitz 夫妇认为专访仍不够充分；原引用 “Salon 1999 专访” 为错误信息，应为 2000 年 Rachel Chalmers 文章

## 文献

- Jolitz DDJ 连载；FreeBSD Project 官方历史文档；Marshall Kirk McKusick（马歇尔·柯克·麦库西克） “Design and Implementation of 4.4BSD” (Addison-Wesley 1996) ［B］

## 史料登记与辩证校准（2026-08-08 追加）

> **本卷命题**：历史非断裂而是循环——总纲第 4 条——分离聚合是永恒规律（原追加块编号“24.4”系旧卷册基准口径残留，2026-09-12 整改统一为总纲条目口径；详见本卷 00-总览“编纂指导思想叙事参照”）

### 史料文献

- DDJ 1992 年度报告；FreeBSD Project FAQ 历史；Marshall Kirk McKusick 个人回忆 ［B］
- Jordan Hubbard freebsd-announce (1993.6.19)；NetBSD Project 历史；Marshall Kirk McKusick（马歇尔·柯克·麦库西克） 回忆录 ［A］
- Chalmers, R. “The unknown hackers” Salon, 17 May 2000；386BSD 0.1 Release Notes (14 July 1992)［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Chalmers, R. “The unknown hackers” Salon, 17 May 2000；FreeBSD 邮件列表 2000 年讨论 ［A］
- Torvalds, L. & Diamond, D. “Just for Fun” (2001)；Linux 1.0 Release Announcement (14 March 1994)；Linksvayer, M. Meta Magazine interview, late 1993［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Torvalds 1991; Jolitz 1991-1992 ［A］

<!-- DB_REF:linux_kernel.duckdb -->
> **数据库引用（linux_kernel.duckdb）**：本子节对应 linux_kernel 代码仓库。
>
> 1991-1991 年间：0 次提交。
>
> 仓库总览：1,474,341 次提交，39,865 位贡献者（contributors 表行数，1970-01-01 至 2026-08-24）。

<!-- 取数窗口“1991-1991 年间：0 次提交”与 linux_kernel 仓库 1991 年起始的表述矛盾，系库侧取数条件所致，2026-09-12 整改留痕，待库侧核正取数条件 -->

- Chalmers, R. “The unknown hackers” Salon, 17 May 2000；FreeBSD Project “A Brief History of FreeBSD”［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Usenet 历史档案；FreeBSD 邮件列表档案 ［A］
<!-- 原 [^doubt-resolved-257/258/259] 三条悬空脚注引用（文件内无定义、来源 slug 乱码、Amit Singh 条目重复）于 2026-09-12 整改移除 -->
- Gödel, K. (1931); Jolitz & Jolitz DDJ (1991-1992); FreeBSD 1.0 Release Notes (1993); NetBSD 0.8 Release Notes (1993)
