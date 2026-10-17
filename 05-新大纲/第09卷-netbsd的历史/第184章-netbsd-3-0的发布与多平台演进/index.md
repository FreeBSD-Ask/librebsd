---
chapter: 第 184 章
id: CH184
volume: 第09卷-netbsd的历史
---

# 第 184 章 netbsd-3-0的发布与多平台演进

## 要点

- NetBSD 2.1（2005.11）与 3.0（2005.12）以稳定化为主，扩展新平台支持（如 AMD64、ARM 多变体）；3.0 强化 SMPng 在嵌入式与服务器场景的可用性
- NetBSD 2.x/3.x 时期发布工程由 Jeff Rizzo、Soren Jacobsen 等推动；社区在 tech-kern、tech-userlevel 等邮件列表持续讨论架构方向；Foundation 在此时期逐步建立捐赠与企业合作机制

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4091] 卷“第09卷-netbsd的历史”第 184 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4092] 卷“第09卷-netbsd的历史”第 184 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 经 netbsd.duckdb 验证，NetBSD 3.0 发布日期为 2005.12.18（“Welcome to NetBSD 3.0 release.” commit author_date = 2005-12-18T14:11:21Z），原大纲误标为 2006 年已修正；2.1 与 3.0 的实质差异需对照 Release Notes 区分，部分叙事将二者混为一谈。L1.1.1 查询的 commi
- 发布工程的具体贡献者名单需对照 commit log 核验，部分叙事仅突出 Core Team 而忽略 release engineering 团队。L1.4.1 查询对 netbsd-src 不适用——netbsd-src 仓库 tags 表为空，无法通过 tag 提取发布版本信息，须依赖 branches 表的 netbsd-X-Y 命名约定识别发布分支；〔待核：原文截断，后文待回源〕

## 文献

- NetBSD 2.1 Release Notes [EB/OL]. (2005-11-14). <https://www.netbsd.org/releases/formal-2.1.html>（原始链接失效，互联网档案馆无存档）；NetBSD 3.0 Release Notes [EB/OL]. (2005-12-23). <https://www.netbsd.org/releases/formal-3.0.html>（原始链接失效，互联网档案馆无存档）；NetBSD Foundation 2005-2007 Annual Reports [EB/OL]. <https://www.NetBSD.org/foundation/reports/>；netbsd.duckdb netbsd-src 仓库（commits 表，repo_name =‘netbsd-src’，message_subject LIKE '%Welcome to NetBSD 3.0%’）；netbsd.duckdb 数据分析·宏观趋势统计.md §L1.1.1（netbsd-src 2005-2007 年度 commit 量）、§L2.3.1.smp（netbsd-src SMP 相关 commit 2005-2007） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2007 年间：289,144 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Foundation 2003-2007 Annual Reports [EB/OL]. <https://www.NetBSD.org/foundation/reports/>；release-engineering 邮件列表 [EB/OL]. <https://mail-index.netbsd.org/release-engineering/>；Jeff Rizzo、Soren Jacobsen releng commit 记录 [DB/OL]. netbsd.duckdb netbsd-src 仓库；netbsd.duckdb 数据分析·宏观趋势统计.md §L1.1.1（netbsd-src 2003-2007 年度 commit 量）、§L1.4.1（netbsd-src tags 表为空，分支命名约定差异） ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

