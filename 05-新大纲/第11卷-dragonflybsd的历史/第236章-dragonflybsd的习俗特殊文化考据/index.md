---
chapter: 第 236 章
id: CH236
volume: 第11卷-dragonflybsd的历史
---

# 第 236 章 dragonflybsd的习俗特殊文化考据

## 要点

- 综合项目史观总纲审视，DragonFly BSD 习俗特殊文化呈现“fork 哲学”与“单一架构师传统”的双重结构——fork 哲学维度：2003 年 fork 周年纪念传统、Dillon 邮件长文传统皆是 Dillon 选择 fork（革命）而非留在 FreeBSD 推动改革的具体显现，与 FreeBSD 5.x 内部改革路线形成对照；单一架构师传统维度：Dillon 邮件长文传统、HAMMER/HAMMER2 设计讨论与“单开发者”定性皆是 Dillon 个人主导项目演进的习俗化显现。 [存疑脚注] 原文此处机械截断，截断后文本按辨析 1 所列互证案例回源补全。
- 4 条 DragonFly BSD 相关键传言自 2003-07 fork 事件起，至 2026 年 GitHub 仓库多开发者活动核验止，覆盖 fork 起因（与核心团队冲突）、技术生态（HAMMER 与 ZFS 关系、HAMMER2 高可用状态）、治理模式（单开发者项目定性）三大维度，构成 DragonFly BSD 传言生态从工程事实到社区叙事的形式主义化骨架；考证结论分布为真伪混杂 1 条

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3631] 卷“第12卷-macos的bsd遗产”第 236 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_4053] 卷“第12卷-macos的bsd遗产”第 236 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4059] 卷“第12卷-macos的bsd遗产”第 236 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4061] 卷“第12卷-macos的bsd遗产”第 236 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4062] 卷“第12卷-macos的bsd遗产”第 236 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4063] 卷“第12卷-macos的bsd遗产”第 236 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

总纲第 15 条——文化即形式主义：fork 周年纪念传统与邮件长文习惯是把工程实践形式化为社区认同仪式的习俗形态（据要点 1）；总纲第 4 条——分离聚合是永恒规律：Dillon 选择 fork（分离）而非留在 FreeBSD 推动内部改革（聚合），周年纪念传统即对这次分离的年度重述（据要点 1）；总纲第 10 条——动手者创造历史：单一架构师传统下 HAMMER/HAMMER2 设计与邮件长文皆系 Dillon 动手劳动的逐项累积（据要点 1）；总纲第 23 条——一切历史写作都是基于哲学设定的历史小说：4 条相关键传言的流传与真伪判定显示社区叙事对工程事实的建构性重组（据要点 2、辨析 2）；总纲第 19 条——解释学循环是历史认识的根本条件：传言考据须在邮件归档、源码比较与仓库活动记录间循环互证（据要点 2、辨析 1）。（2026-09-13 整改：史观字段按批次 C049 核查清单回填，映射依 25 条权威表）

## 辨析

- 考据过程留痕——【查证来源】综合审视史料综合 236.1-236.2 节所有引用的一手与二手史料；项目史观总纲第 4、5、7、8、9、10、21、22、23 条经 据原文第 25 章 一手核验；【交叉验证方法】“fork 哲学”论证须以 fork 周年纪念传统、Dillon 邮件长文传统二案例互证；“单一架构师传统”论证须以 Dillon 邮件长文传统、HAMMER/HAMMER2 设计讨论二案例互证。
- 4 条传言逐条考据最早可考源头、流传路径、考证结论、考证依据；考证结论分布为真伪混杂 1 条、史实失实 3 条；保留多处 0 信任原则考据留痕——FreeBSD Core Team 撤权公告原文未在公开归档中检索到、Dillon 自述存在 “为 fork 决策辩护” 的自利倾向、HAMMER 与 ZFS 算法渊源须经源码级比较方能定论、HAMMER2 私有分支原型未覆盖、“单开发者” 措辞存在定义歧义——须与 GitHub 仓库多开发者活动核验结果并读方可定论。

## 文献

- 上述 236.1-236.2 节所有文献综合；项目史观总纲第 4、5、7、8、9、10、21、22、23 条 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- Dillon M. Announcing DragonFly BSD [EB/OL]. (2003-07-16)[2026-07-27]. **<https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html>**; DragonFly BSD Project. DragonFly BSD History [EB/OL]. [2026-07-27]. **<https://www.dragonflybsd.org/history/>**; Dillon M. THE HAMMER FILESYSTEM [R/OL]. (2008-06-21)[2026-07-27]. **<https://www.dragonflybsd.org/hammer/hammer.pdf>**; DragonFly BSD Project. DragonFly BSD HAMMER Page [EB/OL]. [2026-07-27]. **<https://www.dragonflybsd.org/hammer/>**; DragonFly BSD Project. DragonFly BSD GitHub Repository [CP/OL]. [2026-07-27]. **<https://github.com/DragonFlyBSD/DragonFlyBSD>**; 本项目既有考据记录 `03-原始史料库/06-考据记录/20260727_rumors-dragonfly.md`

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
