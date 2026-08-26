---
chapter: 第 71 章
id: CH71
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 71 章 openbsd的首次发布与早期开发

## 要点

- IPFilter 许可证争议引发 OpenBSD 对全部依赖组件的许可证审计——审计结果导致多个组件被移除或重写；连锁反应强化 OpenBSD 对自由软件准则的严格执行
- OpenBSD 早期（1996-2003）技术淘汰具有 “安全驱动而非商业驱动” 的鲜明特征——淘汰决策主要基于安全论证而非市场份额或商业压力；这一特征使 OpenBSD 在 BSD 阵营中独树一帜，与 FreeBSD 的 “兼容优先” 形成对照；但需警惕将 OpenBSD 叙事为 “安全原教旨主义” 的回溯性建构——彼时 OpenBSD 的移除决策多基于具体工程权衡（如 telnetd 移除后
- Sun Solaris 2.5（1995）是基于 SVR4 的 UNIX，运行于 SPARC 与 x86，面向企业服务器与工作站台；作为商业 UNIX，Solaris 拥有成熟的企业安全特性但无 OpenBSD 式的公开代码审计文化。OpenBSD 在 1995-1996 以 “开源 + 主动安全” 开辟了一个商业 UNIX 与 Linux 都未占据的细分市场。
- OpenBSD 1.0/1.2 时期（1995-1996）de Raadt 与早期开发者对 NetBSD 1.0 源码进行全代码审计，逐行审查 386BSD 经 NetBSD 0.8/0.9 中转传递的安全相关代码——root/超级用户二元特权模型、文件权限 rwx、setuid/setgid 二进制清单、`/etc/passwd` 格式、4.3BSD 网络栈远程漏洞面（sendmail DEBU
- OpenBSD 1.2 在 BSD 社区引发关注——部分成员认可安全审计路径，部分成员质疑分叉的必要性；反响在 BSD 与 Linux 邮件列表持续讨论

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3842] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3843] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3844] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3845] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3846] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3847] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3848] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章
- [DB:references_fulltext:chapter_matches:chmatch_3849] 卷“第04卷-大分裂与四大bsd的诞生”第 71 章，匹配置信度 folder，原因：folder 第69章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- OpenBSD 移除决策是否完全基于安全需考据——sendmail 退役亦涉及配置复杂度与维护成本；r-commands 退役虽然安全论证为主，但 SSH 已成熟亦是工程前提
- Solaris 与 OpenBSD 目标用户重叠有限（企业 vs 高安全/研究）；OpenBSD 的价值不在企业特性丰富度，而在可验证的安全流程。
- OpenBSD 全代码审计的起始时间需考据——审计可能在 fork 后立即开始（1995 年 10 月起），亦可能在 OpenBSD 1.2 发布前集中进行（1996 年上半年），需对照 CVS 历史核实；【0 信任原则·commit 量不等于质量】L1.1.1 的 1995-1996 openbsd-src commit 量（770→5,240）反映开发活跃度但不等于代码质量，OpenBSD 1
- 反响的具体分布在不同叙事中差异较大——部分资料称多数认可，部分称多数质疑；需对照邮件列表存档统计核实
- 方法论的外部影响在不同叙事中评估不一——部分视为决定性，部分视为辅助性；需对照多 BSD/Linux 项目安全实践核实

## 文献

- OpenBSD 许可证审计文档；openbsd-cvs 邮件列表 2001-2003 年提交日志 ［A］
- OpenBSD 邮件列表 1996-2003 存档；de Raadt 公开演讲；OpenBSD Security FAQ ［A］### 史观映射> 第 28 章体现项目统摄史观中 “偶然性改写历史” 与 “分离与聚合” 的双重运作——de Raadt 被 NetBSD Core Team 逐出是具体的个人决定，但直接催生 OpenBSD 这一 BSD 家族的安全堡垒；fork 是 “分离” 的极端形式，但分离后的 “聚合”（加密代码集成、代码审计文化建立）才是 OpenBSD 真正的创造性贡献；“安全至上” 作为差异化定位是 “技术选择即政治选择” 的典型——de Raadt 选择安全而非可移植性或性能，这一选择反映了 OpenBSD 对 BSD 哲学的不同理解；Core Team 的驱逐决议则体现了 “组织结构塑造技术路径”——NetBSD 的精英决策结构直接改变了 BSD 家族的格局---<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1992-1995 年间：770 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- Sun Microsystems. Solaris 2.5 Documentation [Z]. 1995.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- OpenBSD CVS 历史早期记录；OpenBSD 1.2 Release Notes (1996.7)；OpenBSD 官方 FAQ；de Raadt 关于审计的公开声明；本项目。原材料/研究/bsd 漏洞史/bsd 前安全史/386bsd-security-1992-1994.md；本项目。原材料/研究/bsd 漏洞史/bsd 前安全史/4.4bsd-lite-security-1992-1995.md；本项目。bsd_commits.db 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］[^doubt-resolved-305]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1992-1995 年间：770 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- BSD 与 Linux 邮件列表 1996.7-1996 年存档；开源社区访谈录 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-1996 年间：6,236 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 官方 FAQ；BSD 与 Linux 安全实践对比研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- DARPA POSSE 项目公告；OpenBSD 关于 POSSE 的声明[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- OpenBSD 2003-2010 年度财务报告；OpenBSD Foundation 注册文件[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
