---
chapter: 第 222 章
id: CH222
volume: 第11卷-dragonflybsd的历史
---

# 第 222 章 dragonfly2x时代fork必要性的外部批评

## 要点

- 2.x 时代 fork 必要性争议的合图不是和解的实现，而是争议不可调和性的承认与独立主体性的完成。项目史观总纲第 6 条“和解优于斗争”在此审视：2.x 时代 HAMMER 1.0 默认切换（**2008.7.20**）是 fork 后技术分离的完成——**dragonfly.duckdb** 显示 2007 年 HAMMER 首引（commit `8750964d1997`）后 DragonFly 从 FreeBSD 的技术依附中独立出来，争议焦点由“是否应分叉”转向“独立路线能否自立”
- 通过对 Dillon、Hsu、Wildner、Tigeot 等贡献者的 commit 记录与邮件发言考据，量化个人贡献并梳理贡献轨迹
- 对 pkgsrc/DPorts 反批评的再审视可见 2.x 时代 DragonFly 软件包管理演化的双重面相——一方面，pkgsrc/DPorts 路径让 DragonFly 在软件包层面建立独立于 FreeBSD 的能力，与 HAMMER 默认切换、LWKT 共同构成 DragonFly 的完整技术身份，DPorts 雏形为后续完整化奠定基础；另一方面，**dragonfly.duckdb** dragonfly-src 仓库记录显示 2.x 时代 pkgsrc 采纳与 DPorts 雏形均处于起步阶段，独立包管理路线的成效须留待后续版本检验

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4045] 卷“第11卷-dragonflybsd的历史”第 222 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4046] 卷“第11卷-dragonflybsd的历史”第 222 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲第 6 条——和解优于斗争：2.x 时代 fork 必要性争议的合图不是和解的实现，而是争议不可调和性的承认——HAMMER 1.0 默认切换后 DragonFly 与 FreeBSD 各自独立演进，合图呈现张力而不强作调和
- 总纲第 8 条——本体论上各方平等：DragonFly 与 FreeBSD 在 2.x 时代的路线分歧是工程哲学预设的不同而非本体等级的高下，双方贡献者的 commit 记录与邮件发言在考据中同等对待（总纲第 6、8 条原文见 **原材料/哲学/项目统摄史观/第 25 章.md**）

## 辨析

- 考据过程留痕——【查证来源】项目史观总纲第 6、8 条经 **原材料/哲学/项目统摄史观/第 25 章.md** 一手核验；HAMMER 首引 commit `8750964d1997` 与 2007 年后回移停止的判定以 **dragonfly.duckdb** dragonfly-src 仓库 commits 表 parent_hashes 字段为依据，现有数据报告中 L7.1.1 系列未覆盖 dragonfly-src 仓库，回移停止时间节点暂无法以现有数据精确断定，正式撰写前须补跑覆盖 dragonfly-src 仓库的数据报告后再行确认
- commit 数量并非贡献唯一指标——部分贡献者 commit 少但单次 commit 影响大，需结合代码行数、子系统重要性等多维度辨析
- 考据过程留痕——【查证来源】项目史观总纲第 6、8 条经 **原材料/哲学/项目统摄史观/第 25 章.md** 一手核验；2.x 时代 DragonFly 社区规模（2008 年 36 位贡献者）以 **dragonfly.duckdb** dragonfly-src 仓库 contributors 表为依据，与 FreeBSD 数百 committer 的对比以 **freebsd.duckdb** freebsd-src 仓库 contributors 表为依据，两库统计口径与时间窗差异须在引用时注明

## 文献

- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6、8 条）；**dragonfly.duckdb** dragonfly-src 仓库 commits/contributors 表（2.x 时代客观数据） ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

- DragonFly commit log；kernel@ 邮件列表档案；贡献者个人简历 ［A］

## 史料考据补充（2026-08-04 任务3 联网核验）

> 主题：DragonFly 特性

- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6、8 条）；**dragonfly.duckdb** dragonfly-src 仓库 contributors 表；DragonFly pkgsrc 采纳公告；DragonFly 2.10 release notes ［A］

---

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

［存目·DEFERRED 登记：文末两枚 DB_REF:dragonfly.duckdb 块内容完全重复，系注入管线产物，登记 DEFERRED 待管线去重，块内数据未作任何改动。］
