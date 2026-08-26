---
chapter: 第 232 章
id: CH232
volume: 第11卷-dragonflybsd的历史
---

# 第 232 章 dragonfly6x时代的可持续性外部批评

## 要点

- bsd_commits.db 不记录邮件列表发言，批评原始发言须以 lists.dragonflybsd.org（DragonFly）、lists.freebsd.org（FreeBSD）、lkml.org（Linux 内核）等邮件列表归档为准。lists.dragonflybsd.org 完整归档 2003-2026 年间 kernel@/commits@/users@/bugs@ 邮件列表，l
- bsd_commits.db dragonfly-src 仓库 contributors 表提供 Dillon/Wildner/Aaron LI/Huete Jimenez 等贡献者的 commit 量、首末 commit 时间跨度，kernel@ 邮件列表档案提供其设计发言与决策参与记录。bsd_commits.db 显示 Dillon 合并多个邮箱（<<dillon@dragonflybsd.o>
- bsd_commits.db 显示 2022-2026 年间四仓库 commit 量对照：DragonFly 2024 年 277 条 vs FreeBSD 14541 条、OpenBSD 6512 条、NetBSD 5985 条——DragonFly 在资源约束下专注减法（vkernel 移除、HAMMER 1 维护化），FreeBSD 与 NetBSD 资源充足下兼顾减法与加法（FreeBSD
- bsd_commits.db 提供四仓库 2019-2026 年 commit 量对照量化数据：2019 年 freebsd-src = 14273、netbsd-src = 10227、openbsd-src = 7930、dragonfly-src = 1962；2024 年 freebsd-src = 14541、netbsd-src = 5985、openbsd-src = 6512、dr

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4115] 卷“第11卷-dragonflybsd的历史”第 232 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 批评发言可能被断章取义——须结合完整上下文辨析；OSNews/Slashdot 等技术媒体报道须经 archive.org 核验原始 URL，避免链接腐烂导致引述失真；DragonFly users@ 邮件列表中用户担忧发言的具体内容 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证] 须以 lists.dragonflybsd.org 归档为准
- commit 数量并非贡献唯一指标——bsd_commits.db 显示 Aaron LI 868 条 commit 多为 GPU 驱动回移与 HAMMER 2 维护性工作，Dillon 79 条 commit 多为重大架构决策的实现，单条 commit 影响力差异显著；贡献者邮箱合并须谨慎——bsd_commits.db 显示 Dillon 使用多个邮箱（<dillon@dragonflybsd
- 跨项目比较须结合项目目标——bsd_commits.db 显示 commit 量差距显著，但 DragonFly 与 OpenBSD 资源约束下专注减法，FreeBSD 与 NetBSD 资源充足下兼顾减法与加法；技术淘汰的节奏须结合具体项目辨析——DragonFly 6.x 的 vkernel 缺席（6.x 时期仅 13 条 commit）与 HAMMER 1 维护化（2022-2024 年 0
- 市场份额数据须谨慎采用——BSD 项目通常无商业销售数据，须结合镜像下载量、邮件列表活跃度、第三方调查等多源数据交叉验证；bsd_commits.db commit 量比较须考虑 commit 粒度差异——部分项目 commit 粒度大、部分项目 commit 粒度小，单纯 commit 数量比较可能误导；DragonFly 2026 年 commit 回升至 906 条反映项目仍有维护能力，与

## 文献

- lists.dragonflybsd.org 邮件列表归档；lists.freebsd.org 邮件列表归档；lkml.org Linux 内核邮件列表归档；archive.org 技术媒体报道存档 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db dragonfly-src 仓库 contributors 表（多邮箱合并统计）；bsd_commits.db dragonfly-src 仓库 commits 表（按 author_email 与 author_date 交叉统计）；kernel@ 邮件列表档案 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db commits 表（四仓库 2022-2026 年对照）；FreeBSD 14.x/15.x release notes [EB/OL]. freebsd.org/releases/；OpenBSD 7.x release notes [EB/OL]. openbsd.org/；NetBSD 10.x release notes [EB/OL]. netbsd.org/；DragonFly 6.x release notes [EB/OL]. dragonflybsd.org/release/ ［A］---**卷末**：书目述评（约 3,500 字）——讨论“BSD 大败局”叙事的形式主义性质，分析许可证哲学差异的历史后果。<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db commits 表（四仓库 2019-2026 年对照）；各项目 release notes；OpenBSD/NetBSD/FreeBSD Foundation 年报 ［A］FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/><!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2019-2026 年间：243,053 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
