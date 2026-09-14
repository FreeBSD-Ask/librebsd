---
chapter: 第 232 章
id: CH232
volume: 第11卷-dragonflybsd的历史
---

# 第 232 章 DragonFly 6.x 时代的可持续性外部批评

> 本章章入口。SUMMARY 以同章 概述.md 承载章入口与本节索引，本文件与其职责重叠；受 2026-09-11 整改权限所限未合并，待主代理按材料合并强制要求统一收口。

## 本章节索引

- 章入口与节索引：[概述.md](概述.md)
- [232.1 外部批评与反对者dragonfly可持续性批评](232.1-外部批评与反对者dragonfly可持续性批评.md)
- [232.2 重要贡献者与边缘者dragonfly5x6x时期的核心团队](232.2-重要贡献者与边缘者dragonfly5x6x时期的核心团队.md)
- [232.3 dragonflybsd6x时期的技术淘汰](232.3-dragonflybsd6x时期的技术淘汰.md)
- [232.4 与同时期操作系统的比较20192026年同期netbsd9x10x可移植性fre](232.4-与同时期操作系统的比较20192026年同期netbsd9x10x可移植性fre.md)
- [采访录.md](采访录.md)

## 要点

- **dragonfly.duckdb** 不记录邮件列表发言，批评原始发言须以 **lists.dragonflybsd.org**（DragonFly）、**lists.freebsd.org**（FreeBSD）、**lkml.org**（Linux 内核）等邮件列表归档为准。**lists.dragonflybsd.org** 完整归档 2003-2026 年间 `kernel@`/`commits@`/`users@`/`bugs@` 邮件列表，可直接检索本章涉及的全部原始发言与回应
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表提供 Dillon/Wildner/Aaron LI/Huete Jimenez 等贡献者的 commit 量、首末 commit 时间跨度，kernel@ 邮件列表档案提供其设计发言与决策参与记录。**dragonfly.duckdb** 显示 Dillon 合并多个邮箱（如 `dillon@apollo.backplane.com`、`dillon@dragonflybsd.org` 等，按合并规则计入同一贡献者）
- **dragonfly.duckdb** 显示 2022-2026 年间四仓库 commit 量对照：DragonFly 2024 年 277 条 vs FreeBSD 14,541 条、OpenBSD 6,512 条、NetBSD 5,985 条——DragonFly 在资源约束下专注减法（vkernel 移除、HAMMER 1 维护化），commit 量的下滑是资源约束下维护策略的显性化，而非项目停止开发的标志
- freebsd.duckdb 提供四仓库 2019-2026 年 commit 量对照量化数据：2019 年 freebsd-src = 14,273、netbsd-src = 10,227、openbsd-src = 7,930、dragonfly-src = 1,962；2024 年 freebsd-src = 14,541、netbsd-src = 5,985、openbsd-src = 6,512、dragonfly-src = 277

## 史料

- [DB:references_fulltext.duckdb:chapter_matches:chmatch_4115] 卷“第11卷-dragonflybsd的历史”第 232 章，匹配置信度 1.0

## 史观

- 总纲第 3 条（不存在进步，只有权力再分配）——6.x 时期 commit 量的下滑与回升不构成线性衰退或复兴叙事，而是开发权力向少数长期维护者再分配过程的显性化
- 总纲第 5 条（没有必然性，只有偶然性）——可持续性危机的成形由具体偶然事件与主体选择（vkernel 移除、维护策略收缩）构成，不作“项目必然衰落”的目的论叙事
- 总纲第 6 条（和解优于斗争）——对外部“BSD 大败局”式批评不以胜负裁决回应，呈现批评方、项目维护方与沉默用户多方立场的并存
- 总纲第 8 条（本体论上各方平等）——外部批评者、项目回应者与普通用户在本体论上地位平等，批评叙事不优先于项目自述，亦不相反
- 总纲第 10 条（动手者创造历史）——6.x 时代的项目延续由持续动手者（Aaron LI、Sascha Wildner 等长期贡献者的 commit 序列）支撑，而非仅由创始人陈述代表
- 总纲第 19 条（解释学循环是历史认识的根本条件）——批评方与项目方对“可持续性”的前理解差异使判断必然多元，本章以循环结构呈现 2022-2026 年的批评与回应

## 辨析

- 批评发言可能被断章取义——须结合完整上下文辨析；OSNews/Slashdot 等技术媒体报道须经 archive.org 核验原始 URL，避免链接腐烂导致引述失真；DragonFly users@ 邮件列表中用户担忧发言的具体内容 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 须以 **lists.dragonflybsd.org** 归档为准
- commit 数量并非贡献唯一指标——**dragonfly.duckdb** 显示 Aaron LI 868 条 commit 多为 GPU 驱动回移与 HAMMER 2 维护性工作，Dillon 79 条 commit 多为重大架构决策的实现，单条 commit 影响力差异显著；贡献者邮箱合并须谨慎——**dragonfly.duckdb** 显示 Dillon 使用多个邮箱，统计时须按邮箱合并规则归并为同一贡献者，避免重复计数
- 跨项目比较须结合项目目标——**dragonfly.duckdb** 显示 commit 量差距显著，但 DragonFly 与 OpenBSD 资源约束下专注减法，FreeBSD 与 NetBSD 资源充足下兼顾减法与加法；技术淘汰的节奏须结合具体项目辨析——DragonFly 6.x 的 vkernel 缺席（6.x 时期仅 13 条 commit）反映该子系统的维护优先级下调，属主体选择而非能力丧失
- 市场份额数据须谨慎采用——BSD 项目通常无商业销售数据，须结合镜像下载量、邮件列表活跃度、第三方调查等多源数据交叉验证；**dragonfly.duckdb** commit 量比较须考虑 commit 粒度差异——部分项目 commit 粒度大、部分项目 commit 粒度小，单纯 commit 数量比较可能误导；DragonFly 2026 年 commit 回升至 906 条反映项目仍有维护能力，与 2024 年 277 条的低谷相比明显回升，但绝对量仍远低于 FreeBSD 主线

## 文献

- lists.dragonflybsd.org 邮件列表归档；lists.freebsd.org 邮件列表归档；lkml.org Linux 内核邮件列表归档；archive.org 技术媒体报道存档 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表（多邮箱合并统计）；**dragonfly.duckdb** dragonfly-src 仓库 commits 表（按 author_email 与 author_date 交叉统计）；kernel@ 邮件列表档案 ［A］
- **dragonfly.duckdb** commits 表（四仓库 2022-2026 年对照）；FreeBSD 14.x/15.x release notes [EB/OL]. [2026-09-11]. **https://www.freebsd.org/releases/**；OpenBSD 7.x release notes [EB/OL]. [2026-09-11]. **https://www.openbsd.org/**；NetBSD 10.x release notes [EB/OL]. [2026-09-11]. **https://www.netbsd.org/**；DragonFly 6.x release notes [EB/OL]. [2026-09-11]. **https://www.dragonflybsd.org/release/** ［A］
- **bsd_commits.duckdb** commits 表（四仓库 2019-2026 年对照）；各项目 release notes；OpenBSD/NetBSD/FreeBSD Foundation 年报 ［A］
- FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。
> 2019-2026 年间：243,053 次提交。
