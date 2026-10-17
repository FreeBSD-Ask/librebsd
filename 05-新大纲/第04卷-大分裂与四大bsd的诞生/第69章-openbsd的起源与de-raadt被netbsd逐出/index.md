---
chapter: 第 69 章
id: CH69
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 69 章 openbsd的起源与de-raadt被netbsd逐出

## 要点

- OpenBSD 仓库共 491195 次提交（1995-10-18 至 2026-08-25），427 位贡献者，提交量虽少于 FreeBSD 和 NetBSD，但代码审计文化使其每行代码经过更严格审查

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3990] 匹配第 69 章，匹配置信度 0.9，原因：匹配说明原文截断，待库侧重跑增补补全
- [DB:bsdnow_podcast:outline_mappings:om_10418] BSD Now 第 676 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10451] BSD Now 第 671 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10471] BSD Now 第 666 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10498] BSD Now 第 663 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10665] BSD Now 第 634 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10686] BSD Now 第 630 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10797] BSD Now 第 613 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11082] BSD Now 第 578 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11169] BSD Now 第 567 期，匹配 CH69 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11193] BSD Now 第 565 期，匹配 CH69 章，关联度 1.0

- [DB:code_repos:openbsd.duckdb] OpenBSD 仓库共 491195 次提交（1995-10-18 至 2026-08-25），427 位贡献者，提交量虽少于 FreeBSD 和 NetBSD，但代码审计文化使其每行代码经过更严格审查

## 史观

- 和解优于斗争：OpenBSD 的起源虽源于冲突（de Raadt 被逐），但最终走向安全至上，将分裂转化为建设性力量

## 辨析

- 通知的具体措辞在不同叙事中略有差异——需对照邮件列表原始存档核实；经[邮件列表库]核查：netbsd-users 列表 1994 年存档缺失，逐出通知原文两库无法验证；netbsd 库 port-sparc/port-m68k 列表存 Theo de Raadt（<deraadt@fsa.ca> / <deraadt@theos.com>）1994-1995 年多封技术邮件（如 port-sparc 1994-1995 年间各帖，具体邮件编号待库侧重查补全）
- 通知邮件与 de Raadt 自述在事实细节上存在冲突——需对照多方公开声明交叉验证
- 后果的正负评估在不同叙事中差异较大——部分视为 BSD 阵营的损失，部分视为 OpenBSD 安全文化的契机；需对照多方公开声明核实
- 评价与 de Raadt 自述在事实细节上可能存在冲突——需对照多方公开声明交叉验证
- 合图层的撰写须警惕两种叙事陷阱——其一为“Core Team 正当、de Raadt 应受惩戒”的组织中心叙事，其二为“de Raadt 受害、Core Team 专断”的个人英雄叙事；两种叙事均以道德判断取代史观审视，违反“不偏袒叙事姿态”；本事件的不可调和性源于前理解的根本差异（总纲第 19 条）——Core Team 以“社区准则”为前理解，de Raadt 以“工程优先”为前理解，两种前理解互不兼容且无法互相归约，史家须将二者并置呈现而不代作裁断。

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb

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

