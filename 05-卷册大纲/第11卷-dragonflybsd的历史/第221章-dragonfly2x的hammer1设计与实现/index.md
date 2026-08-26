---
chapter: 第 221 章
id: CH221
volume: 第11卷-dragonflybsd的历史
---

# 第 221 章 dragonfly2x的hammer1设计与实现

## 要点

- 以项目史观总纲第 13 条 “法律与道德是利益分配”、第 19 条 “解释学循环是历史认识的根本条件”、第 21 条 “革命与改革是历史方法论的分歧” 审视 HAMMER 文件系统设计争议，可见争议的更深维度。**总纲第 13 条审视**：HAMMER 与 ZFS 的设计争议背后是许可证哲学与利益分配的差异——HAMMER 采用 BSD 许可证（与 DragonFly 整体许可证一致），ZFS 采
- DragonFly 2.4/2.6 的发布说明、commit log 与邮件列表讨论的交叉考据，确认关键特性的实际引入时间与作者归属
- 通过对 DragonFly 邮件列表中权限相关发言的考据，梳理权限授予、撤销、争议的实际过程

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4043] 卷“第11卷-dragonflybsd的历史”第 221 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4044] 卷“第11卷-dragonflybsd的历史”第 221 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 13、19、21 条经 据原文第 25 章 一手核验；DragonFly BSD 采用 BSD 许可证经 **dragonflybsd.org** 官方页面核验；ZFS 采用 CDDL 经 OpenSolaris ZFS 设计文档核验；【交叉验证方法】CDDL 与 BSD 许可证的兼容性须以法律文本而非社区陈述为依据——CDDL 与 BSD 许可证在文件
- release notes 与 commit log 偶有不一致——release notes 可能为宣传目的省略部分变更或夸大某些特性，commit log 是更可靠的事实依据
- 邮件记录可能不完整——部分权限决策可能在私下邮件或 IRC 中进行，需结合 commit log 交叉验证

## 文献

- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13、19、21 条）；DragonFly BSD 官方页面（**dragonflybsd.org**，BSD 许可证）；OpenSolaris ZFS 设计文档（CDDL 1.0）；FreeBSD 8.x release notes（ZFS 集成许可证兼容性）；Phoronix、OSNews 等技术媒体存档（ZFS 与 HAMMER 报道频率对比）[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证] ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2008-2022 年间：570,543 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly 2.4/2.6 release notes；DragonFly git 仓库；kernel@ 邮件列表档案 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2009-2010 年间：6,829 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly 邮件列表档案；DragonFly commit log；committer 个人邮件 ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：DragonFly committer
