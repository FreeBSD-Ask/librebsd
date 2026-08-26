---
chapter: 第 112 章
id: CH112
volume: 第06卷-freebsd的核心技术革新
---

# 第 112 章 zfs在freebsd的演进与dragonfly对比

## 要点

- **统计分析印证**——`freebsd.db` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；Pettitt 与 BUISHAND R 双变点检验一致判定 freebsd-src 变点为
- 一个常见叙事是 “DragonFly BSD 自研 HAMMER/HAMMER2 是因为 CDDL 许可问题”——这一说法不准确；Matthew Dillon 从未将许可证列为不移植 ZFS 的原因，实际原因包括：（1）DragonFly BSD 的 VFS 和内存管理架构与 FreeBSD 差异较大，移植工作量大；（2）Dillon 认为 ZFS 过于复杂，不适合 DragonFly BSD 的
- 关于 Torvalds 2020 年 1 月 6 日 RealWorldTech 帖子的一手史料考证：（1）原帖位置：论坛主题讨论 "Spectre/Meltdown Fixes" 下的回复，讨论中一名用户抱怨内核 API 变更导致 ZFS 等 out-of-tree 模块无法工作，Torvalds 在该 thread 中回复；（2）精确时间：2020 年 1 月 6 日（UTC 时间）；（3）精

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1526] 卷“第06卷-freebsd的核心技术革新”第 112 章，匹配置信度 0.6，原因：无法匹配到具体章节（关键词重叠得分低于阈值）

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- *统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 Sen's slope =+1.40/月 的实际工程意义须结合 FreeBSD 版本周期与 commit 粒度变化综合判断；(2) 变点归因存疑：1999-08 变点距 2020-01 SVN-to-Git 迁移
- 纠正一个广泛传播的错误叙事：中文技术社区常称 “BSD 自研 HAMMER 是因为 CDDL 不兼容”——这是错的；经 CDDL 文本 §3.5 确认，CDDL 明确允许与其他许可（包括 BSD 和 GPL）的代码在更大作品中聚合，只是对 CDDL 代码本身的修改必须保持 CDDL；DragonFly 不移植 ZFS 是工程和哲学选择，非法律原因
- 常见误读包括：（1）误称 Torvalds 说 “ZFS 是邪恶的”——他从未用 "evil" 一词，原话是 "buzzword" 和 "non-starter"；（2）误将此言论解读为 Linux 项目的官方立场——Torvalds 是以个人身份发表观点，但他作为 Linux 创始人的地位使该言论具有官方效果；（3）忽略言论的上下文（out-of-tree 模块兼容性讨论）；Greg Kroah

## 文献

- FreeBSD Project. bsd_commits.db freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\bsd_commits.db`; Hibsd Project. 推断性统计.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md` Task 5-6; Hibsd Project. phase3_inferential_stats.py Task 5-6 [CP/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\script\phase3_inferential_stats.py`; Hibsd Project. 卷章数据映射.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\卷章数据映射.md` 第五卷第 50 章映射。［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Sun Microsystems (2004). *Common Development and Distribution License 1.0* §3.5 [EB/OL]. 获取路径：<https://opensource.org/licenses/cddl1.php> [访问日期 2026-07-30]; Dillon, M. DragonFly BSD Kernel Mailing List Posts [EB/OL] (2007-2008). 获取路径：<https://www.dragonflybsd.org/mailinglists/> [访问日期 2026-07-30].[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Torvalds, L. (2020-01-06). Real World Tech Forum Post [EB/OL] (archived via Wayback Machine). 获取路径：<https://www.realworldtech.com/forum/?threadid=189311> [访问日期 2026-07-30]; Phoronix (2020-01-07). *Linus Torvalds: Don't Use ZFS* [EB/OL]. 获取路径：<https://www.phoronix.com/news/Linux-5.6-ZFS-Oracle> [访问日期 2026-07-30]; LWN.net (2020-01). *Linus on ZFS* [EB/OL]. 获取路径：<https://lwn.net/Articles/809272/> [访问日期 2026-07-30].[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
