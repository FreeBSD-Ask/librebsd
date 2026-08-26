---
chapter: 第 267 章
id: CH267
volume: 第13卷-bsd衍生操作系统
---

# 第 267 章 netflix-open-connect

## 要点

- Netflix 在扩展流媒体时选择 FreeBSD 构建 OCA 边缘设备，理由包括网络栈性能、ZFS 存储可靠性、`dtrace` 可观测性；Netflix 工程师在 BSDCan 等会议公开其 FreeBSD at scale 实践。Netflix 于 2011 年开始建设 Open Connect CDN，逐步从第三方 CDN（如 Akamai、Limelight）迁移至自建 OCA 边缘设
- Netflix 工程团队（含 Randall Stewart 等 FreeBSD 长期贡献者）向 FreeBSD 回馈大量网络/传输层补丁，是企业 →BSD 代码流动的典型。
- 对比 Netflix（FreeBSD）与 YouTube/Google（Linux）、AWS（Linux）的内容/云基础设施，分析 FreeBSD 在超大规模互联网的独特定位。Netflix 的基础设施架构呈现 “FreeBSD 数据面 + Linux 控制面” 的混合模式——OCA 边缘设备运行 FreeBSD 负责视频分发（数据面），而内容管理系统、推荐系统、编码转码等后端服务运行于 AWS

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4144] 卷“第13卷-bsd衍生操作系统”第 267 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Netflix 选用 FreeBSD 的具体技术理由（网络栈/存储）须以其工程博客核实；freebsd.db 查询 L3.2.1 与 L3.2.2 的 Netflix 占比须警惕邮箱域名识别不精确——Netflix 工程师（如 Randall Stewart）可能持有 @freebsd.org 邮箱并以该邮箱提交（被 L7.2.1 查询的 @freebsd.org 排除条件过滤），且占比为全 23
- Netflix 回馈的具体代码范围须以 commit 记录核实；kTLS 与 TLS 硬件卸载的上下游关系须区分——kTLS 是 FreeBSD 内核功能，TLS 硬件卸载依赖网卡硬件支持（如 Chelsio T6 与 Mellanox ConnectX-6），二者在 Netflix OCA 中的具体部署组合须以 Netflix 工程博客与 commit 记录核验；400Gb/s 到 800Gb/
- 具体贡献者须以 commit 记录核实；freebsd.db 查询 L7.2.1 的 “未出现 @netflix.com 邮箱贡献者” 不等于 Netflix 零回馈——Netflix 工程师（如 Randall Stewart）作为 FreeBSD Core Team 成员持有 @freebsd.org 邮箱，被 L7.2.1 查询的 @freebsd.org 排除条件过滤，须通过 L3.2.1
- Netflix 内部 Linux/FreeBSD 分工（控制面 vs 数据面）须以官方资料厘清——Netflix 工程博客与 BSDCan 演讲中提及的 “FreeBSD 用于 OCA 边缘设备” 与 “Linux 用于后端服务” 的分工边界须以具体服务组件核实，不可笼统概括；YouTube/Google 与 AWS 的 Linux 选型理由须以其工程文档核实，不得仅凭 “Linux 是主流” 推

## 文献

- Netflix 技术博客；BSDCan 存档；openbsd.db 查询 L3.2.1（商业实体 commit 占比随时间变化，含 Netflix @netflix.com）；openbsd.db 查询 L3.2.2（商业实体 commit 量按仓库分布）；原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.2.1、§L3.2.2。 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2011-2015 年间：216,147 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Netflix 技术文档；bsd_commits.db；FreeBSD 社区论文 [FP-2019-036]、[FP-2019-046]、[FP-2019-068]、[FP-2019-078]、[FP-2021-007]、[FP-2022-014]。 ［A］## 266.2.3 外部贡献者
- bsd_commits.db 查询 L7.2.1（衍生项目贡献者在 freebsd-src 的回馈 commit，≥5 次，前 30 名）；bsd_commits.db 查询 L3.2.1（商业实体 commit 占比随时间变化，含 Netflix @netflix.com）；原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md §L7.2；原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.2.1。 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2015-2026 年间：626,955 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 各公司官方资料；Netflix TechBlog；Google Research Blog；AWS 文档。[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]FreeBSD 社区论文：[FP-2022-014] The "other" FreeBSD optimizations used by Netflix to serve video at 800Gb/s from a single server（Drew Gallatin，2022）<https://papers.freebsd.org/2022/eurobsdcon/gallatin-the_other_freebsd_optimizations-netflix/>FreeBSD 社区论文：[FP-2021-007] Serving Netflix Video at 400Gb/s on FreeBSD（Drew Gallatin，2021）<https://papers.freebsd.org/2021/eurobsdcon/gallatin-netflix-freebsd-400gbps/>FreeBSD 社区论文：[FP-2019-046] Kernel TLS and TLS hardware offload（Slava Shwartsman, Drew Gallatin，2019）<https://papers.freebsd.org/2019/eurobsdcon/shwartsman_gallatin-kernel_tls_harware_offload/>FreeBSD 社区论文：[FP-2019-078] In-Kernel TLS Framing and Encryption for FreeBSD（John Baldwin（约翰·鲍德温），2019）<https://papers.freebsd.org/2019/vbsdcon/baldwin_in-kernel_tls_framing_and_encryption_for_freebsd/>FreeBSD 社区论文：[FP-2019-036] Netflix and FreeBSD: Reflections on Running FreeBSD Head in Production（Jonathan Looney，2019）<https://papers.freebsd.org/2019/bsdcan/looney-netflix_and_freebsd/>FreeBSD 社区论文：[FP-2019-068] Netflix and FreeBSD: Using Open Source to Deliver Streaming Video（Jonathan Looney，2019）<https://papers.freebsd.org/2019/fosdem/looney-netflix_and_freebsd/><!-- DB_REF:bsd_derivatives.duckdb -->> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，14,109 位贡献者，1985-06-13 至 2026-08-24。
