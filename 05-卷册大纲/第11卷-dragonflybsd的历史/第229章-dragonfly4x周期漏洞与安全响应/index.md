---
chapter: 第 229 章
id: CH229
volume: 第11卷-dragonflybsd的历史
---

# 第 229 章 dragonfly4x周期漏洞与安全响应

## 要点

- DragonFly 4.0（2015）正式发布 HAMMER 2 文件系统，4.x 周期是 HAMMER 2 进入生产部署的起点——HAMMER 2 支持 **多卷**、**快照**、**去重** 等特性；4.x 周期 dragonfly.duckdb 未见直接归因于 HAMMER 2 文件系统的 CVE——HAMMER 2 在 4.x 周期刚进入生产部署，漏洞尚未充分暴露。HAMMER 2 关键特性的安
- 项目史观总纲第 5 条“没有必然性，只有偶然性”为审视 DragonFly DRM 切换提供了根本框架。dragonfly.duckdb 显示 DRM 切换的关键节点——v4.0.0（2014-11-23）的 DRM 切换完成、Tigeot（<ftigeot@wolfpond.org>）2011-03-06 起的 1346 条 DRM 移植 commit、sys/dev/drm/ 目录 2014 年
- 项目史观总纲第 8 条“本体论上各方平等”为审视 DragonFly DRM 切换提供了去中心化视角。dragonfly.duckdb 显示 2014-2017 年间 DragonFly、FreeBSD、Linux 三方在 DRM 子系统上的关系不是“先进-落后”的等级关系，而是各自独立演化的本体论平等主体：DragonFly 的 DRM 移植（Tigeot 1346 条 commit）是 Drago
- Fly DRM 切换提供了双重透镜。形式主义层面：DRM 作为 GPU 驱动抽象层，其代码在 DragonFly、FreeBSD、Linux 三方间流动时被“形式主义化”——同一份 Linux DRM 代码在 DragonFly 中被重组为 DragonFly 内核子系统的一部分，其“商品形式”（可移植的 GPU 驱动代码）
- DragonFly 4.x 时代（2014-11-23 至 2017-08-01）dragonfly.duckdb dragonfly-src 仓库数据显示三类可持续性批评具有量化基础。其一，“社区规模持续缩小”批评——dragonfly.duckdb 显示活跃 committer 数从 2014 年 33 人降至 2018 年 24 人（降幅 27.3%），同期 freebsd-src 仓库 commi

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4107] 卷“第11卷-dragonflybsd的历史”第 229 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4108] 卷“第11卷-dragonflybsd的历史”第 229 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4109] 卷“第11卷-dragonflybsd的历史”第 229 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- HAMMER 2 去重的信息泄露风险是跨用户存储系统的共同问题——ZFS 的去重同样存在此风险，解决方案为加密后去重（让相同明文加密为不同密文从而避免去重）；HAMMER 2 在 4.x 周期无 CVE 可能因部署规模有限而非设计优越性 [考据完成：2026-07-28 HAMMER 2 在 4.x 周期无 CVE 可能因生产部署规模有限或安全研究社区审计关注较少，HAMMER 2 漏洞史须以 5
- 考据过程留痕——【查证来源】dragonfly.duckdb dragonfly-src 仓库 tags 表 v4.0.0 tagger_date = 2014-11-23T19:54:13-05:00（tagger = Justin C. Sherrill（贾斯廷·C·谢里尔），target_commit_hash = `b733ce3046bd`）经数据库查询核验，为 DRM 切换完成时间节点提供代码
- 考据过程留痕——【查证来源】dragonfly.duckdb dragonfly-src 仓库 contributors 表 Tigeot 1346 条 commit 2011-2020 经数据库查询核验，为 DragonFly 主体性的显现提供代码级证据；dragonfly.duckdb dragonfly-src 仓库 commits 表 DRM 关键词 2016-2018 年 332 条经数据库查询
- 考据过程留痕——【查证来源】dragonfly.duckdb dragonfly-src 仓库 contributors 表 Tigeot 1346 条 commit 经数据库查询核验，为“形式适配”性质提供代码级证据；dragonfly.duckdb dragonfly-src 仓库 commits 表 DRM 移植 commit message 含 Linux、port、adapt 关键词的统计经数据
- 考据过程留痕——【查证来源】dragonfly.duckdb dragonfly-src 仓库 commits 表 2014-2018 年活跃 committer 数 33/35/33/33/28/25/26/24 经数据库查询核验，为“社区规模持续缩小”批评提供量化证据；dragonfly.duckdb dragonfly-src 仓库 contributors 表 Dillon 2016-2018 年

## 文献

- dragonfly.duckdb dragonfly-src 仓库；DragonFly 4.0 Release Notes；Matt Dillon HAMMER 2 设计文档 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 tags 表（v4.0.0 tagger_date）；dragonfly.duckdb dragonfly-src 仓库 contributors 表（Tigeot 统计）；dragonfly.duckdb dragonfly-src 仓库 commit_files 表（sys/dev/drm/ 目录）；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 5 条） ［A］## 228.3.2 总纲第 8 条映射——DRM 切换中的本体论平等审视
- freebsd.duckdb dragonfly-src 仓库 contributors 表（Tigeot 统计）；freebsd.duckdb dragonfly-src 仓库 commits 表（DRM 关键词）；freebsd.duckdb freebsd-src 仓库 commits 表（DRM2 关键词）；Linux kernel git 仓库 DRM 子系统 commit [EB/OL]. <https://git.kernel.org/>；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 8 条与第 6 条） ［A］## 228.3.3 总纲第 11 条与第 19 条映射——DRM 作为商品形式主义与解释学循环
- freebsd.duckdb dragonfly-src 仓库 contributors 表与 commits 表（Tigeot DRM 移植统计）；DragonFly kernel@ 邮件列表档案 [EB/OL]. <https://www.dragonflybsd.org/mailinglists/>；Linux kernel DRM 文档 [EB/OL]. <https://www.kernel.org/doc/html/latest/gpu/>；freebsd.duckdb freebsd-src 仓库 sys/dev/drm2/ 目录；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 11 条、第 19 条与第 25 条） ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 commits 表与 contributors 表（2014-2018 年活跃 committer 数与 Dillon/HAMMER2 统计）；dragonfly.duckdb commits 表（dragonfly-src 与 freebsd-src 对照）；dragonfly.duckdb dragonfly-src 仓库 tags 表（v4.6.0 tagger_date）；freebsd.duckdb freebsd-src 仓库 tags 表（release/11.0.0 tagger_date）；DragonFly 4.6 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release46/**>；DragonFly 4.8 Release Notes [EB/OL].** <https://www.dragonflybsd.org/release48/**>；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/**>；FreeBSD 11.0 Release Notes [EB/OL]. freebsd.org/releases/；OpenBSD 5.9 Release Notes [EB/OL]. openbsd.org/59.html；OpenBSD 6.4 Release Notes [EB/OL]. openbsd.org/64.html；** dragonflybsd.org/foundation/** HTTP 404 ［A］## 228.4.2 反批评层——DragonFly 阵营的工程实用主义与多元路径回应（2014-2017）
- dragonfly.duckdb dragonfly-src 仓库 commits 表（TOP 5 与 HAMMER2 统计）；dragonfly.duckdb dragonfly-src 仓库 tags 表（v5.0.0 tagger_date）；DragonFly 4.6 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release46/**>；DragonFly 5.0 Release Notes [EB/OL].** <https://www.dragonflybsd.org/release50/**>；Dillon 2017-02-24 users@ 邮件列表"Update on status of master - NUMA and cache-line locality" [EB/OL]. **lists.dragonflybsd.org/pipermail/users/2017-February/313242.html**；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/>** ［A］## 228.4.3 再回应层——批评方对 DragonFly 阵营回应的再反驳（2014-2020）
- dragonfly.duckdb dragonfly-src 仓库 commits 表与 contributors 表（TOP 5 集中度、Tigeot、HAMMER2、活跃 committer、NVMe 统计）；dragonfly.duckdb commits 表（dragonfly-src 与 freebsd-src 对照）；Dillon 2017-02-24 users@ 邮件列表"Update on status of master - NUMA and cache-line locality" [EB/OL]. **lists.dragonflybsd.org/pipermail/users/2017-February/313242.html**；DPorts 仓库[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证] ［A］## 228.4.4 合图层——从项目统摄史观审视 DragonFly 4.x 时代可持续性争议（2014-2020）
- dragonfly.duckdb commits 表（dragonfly-src 与 freebsd-src/openbsd-src 2014-2018 年对照）；dragonfly.duckdb dragonfly-src 仓库 commits 表（HAMMER2 关键词统计）；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6 条、第 8 条与第 19 条） ［A］## 228.4.5 项目统摄史观审视子节——总纲第 13、19、21 条对可持续性争议的三重切入
- dragonfly.duckdb dragonfly-src 仓库 commits 表（HAMMER2 关键词 2014-2018 年统计）；dragonfly.duckdb dragonfly-src 仓库 tags 表（v5.0.0 tagger_date）；**dragonflybsd.org/foundation/** HTTP 404；FreeBSD Foundation [EB/OL]. **<https://freebsdfoundation.org/**>；OpenBSD Foundation [EB/OL].** <https://www.openbsdfoundation.org/**>；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13 条、第 19 条、第 21 条） ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。