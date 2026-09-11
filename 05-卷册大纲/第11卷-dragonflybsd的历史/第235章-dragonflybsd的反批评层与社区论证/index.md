---
chapter: 第 235 章
id: CH235
volume: 第11卷-dragonflybsd的历史
---

# 第 235 章 dragonflybsd的反批评层与社区论证

## 要点

- DragonFly 阵营对社区规模萎缩批评的回应集中于 niche 价值与持续维护两点——其一，niche 价值：DragonFly 的 LWKT 消息传递架构、HAMMER/HAMMER2 写时复制文件系统、vkernel 用户态虚拟化三大创新在 BSD 阵营中具有不可替代性——dragonfly.duckdb 显示 sys/kern/lwkt_thread.c（commit `8ad65e0803
- **辩证合图**——DragonFly 哲学文化与社区的辩证综合：Dillon 个人主导模式既是 DragonFly 决策效率的保障（反批评层）也具有继承风险与法律实体缺位（批评层与再批评层），二者并非非此即彼；Dillon 个人主导模式在 Dillon 主导下具有历史合理性（小团队 + 激进创新哲学 + 23 年持续发布），但这一合理性以继承风险（无公开继任机制）〔待核：原文截断，后文待回源〕
- 从项目史观总纲第 19 条“解释学循环是历史认识的根本条件”与“权力与知识在历史书写中共谋”审视，DragonFly 哲学文化叙事的权力知识共谋体现在三个层次——其一，命名权的权力行使：Dillon 在 2003 年 fork 时选择“DragonFly BSD”作为项目名称（fork 公告原标题“Annoucning DragonFly BSD!”，原拼写错误保留），这一命名本身是权力行使——以

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4118] 卷“第11卷-dragonflybsd的历史”第 235 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- 实际史料条目：Dillon M. DragonFly BSD fork announcement（2003-07-16，freebsd-current 邮件列表）；**dragonfly.duckdb** dragonfly-src 仓库 commits/contributors/tags 表；DragonFly BSD Digest（dragonflydigest.com）长期跟踪报道；FreeBSD/NetBSD/OpenBSD 三方 Foundation 治理文件（对照 DragonFly 无 Foundation 模式）

## 史观

- 总纲第 4 条（分离聚合是永恒规律）——反批评层与批评层、再批评层的往复对话，是 fork 社区分离之后试图重新聚合理解的循环过程
- 总纲第 5 条（没有必然性，只有偶然性）——DragonFly 的存续与批评的成立均系具体偶然事件与主体选择，不作“项目必然萎缩”或“批评必然正确”的目的论叙事
- 总纲第 8 条（本体论上各方平等）——反批评方、批评方与再批评方在本体论上地位平等，反批评不因维护立场而低值，批评不因外部立场而高值
- 总纲第 10 条（动手者创造历史）——对“社区萎缩”批评的最有力回应是持续发布的 release 序列与 contributors 表中的长期动手者记录，而非修辞辩护
- 总纲第 19 条（解释学循环是历史认识的根本条件）——批评方与项目方的前理解差异使“可持续性”“利基价值”等判断必然多元，本章以合图层呈现循环而非终结争议
- 总纲第 6 条（和解优于斗争）——合图不寻求消除张力而寻求呈现张力，反批评与批评的并置本身即是和解的书写形态

## 辨析

- 反批评的合理性在不同叙事中评估不一——部分视为有效辩护，部分视为合理化；【0 信任原则·niche 价值的归因辨析】LWKT/HAMMER/HAMMER2/vkernel 的持续维护是 DragonFly 社区集体贡献，不得单一归因于“niche（利基）价值”——这些产出亦依赖 Matthew Dillon、Tomohiro Kusumi（HAMMER/HAMMER2 协作者）等核心贡献者的个人努力；单一归因与集体归因的张力须以 contributors 表 commit 统计与邮件列表讨论记录交叉核验
- 合图不寻求消除张力而寻求呈现张力——Dillon 个人主导模式的“效率”与“脆弱”、小团队模式的“凝聚力”与“代际更替风险”、无 Foundation 模式的“独立”与“脆弱”、社区规模萎缩的“niche（利基）价值”与“可持续性危机”是同一治理结构/团队结构/资金模式/技术路线选择的共生效应，不可分割；【0 信任原则·合图的非终结性】合图并非辩证链的终结而是阶段性综合，随 DragonFly 治理演进而可被再综合，不预设终局判断
- 权力知识共谋审视不意味着否定 DragonFly 官方叙事的真实性——Dillon 主导的官方叙事在工程事实层面（LWKT、HAMMER、HAMMER2、vkernel commit 时间序列、release 节奏、贡献者统计）经 **dragonfly.duckdb** 核验为真，但叙事的真实性不否定其作为权力行使的性质；【0 信任原则·叙事权力的对称呈现】本节试图呈现 DragonFly 阵营与批评者阵营各自的叙事建构过程，而非裁决任何一方的修辞胜负

## 文献

- **dragonfly.duckdb** dragonfly-src 仓库 commits 表与 commit_files 表与 tags 表与 contributors 表；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者（contributors 表行数），2003-06-17 至 2026-08-18。
- 综合原第 105 章全章文献；sacred_sources.duckdb 第 25 章（file_id=26，总纲第 6 条与第 8 条原文）；**dragonfly.duckdb** dragonfly-src 仓库 commits/contributors/tags/commit_files 表；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/>；dragonflybsd.org/foundation/ 页面 404；FreeBSD Core Team bylaws [EB/OL]. <https://www.freebsd.org/internal/core-team/>；NetBSD Foundation bylaws [EB/OL]. <https://www.netbsd.org/foundation/>；OpenBSD Foundation [EB/OL]. <https://www.openbsdfoundation.org/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者（contributors 表行数），2003-06-17 至 2026-08-18。
- 项目史观总纲第 19 条；Dillon M. DragonFly BSD fork announcement [EB/OL]. <https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/>；DragonFly BSD Digest [EB/OL]. <https://www.dragonflydigest.com/>；dragonflybsd.org/foundation/ 页面 404；**dragonfly.duckdb** dragonfly-src 仓库 contributors 表；FreeBSD Core Team bylaws [EB/OL]. <https://www.freebsd.org/internal/core-team/> ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者（contributors 表行数），2003-06-17 至 2026-08-18。
