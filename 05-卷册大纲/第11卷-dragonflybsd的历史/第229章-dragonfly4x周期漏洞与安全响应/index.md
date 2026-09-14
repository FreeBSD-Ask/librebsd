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
- DragonFly kernel@ 与 users@ 邮件列表存档（漏洞修复与安全响应讨论一手出处）[EB/OL]. **https://lists.dragonflybsd.org/**（2026-09-13 联网核验可访问，users、kernel 等 8 个列表 2003-2026 年归档）；**dragonfly.duckdb** dragonfly-src 仓库 tags 表（v4.0.0-v5.0.0 tagger_date 与 target_commit_date）

## 史观

- 总纲第 5 条——没有必然性，只有偶然性：4.x 周期 HAMMER 2 未见直接归因的 CVE 属偶然性事件而非设计优越性的必然证明，漏洞暴露与生产部署规模、使用时长相关，安全评估须避免以“无 CVE”反推“必然安全”
- 总纲第 8 条——本体论上各方平等：DragonFly 的 DRM 切换与 FreeBSD、Linux 的 DRM 子系统演化是各自独立演化的平等主体，Tigeot 的 DRM 移植不构成“追随者”式的等级定位（总纲第 5、8 条原文见 **原材料/哲学/项目统摄史观/第 25 章.md**）

## 辨析

- HAMMER 2 去重的信息泄露风险是跨用户存储系统的共同问题——ZFS 的去重同样存在此风险，解决方案为加密后去重（让相同明文加密为不同密文从而避免去重）；HAMMER 2 在 4.x 周期无 CVE 可能因部署规模有限而非设计优越性 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,207 次提交。

- dragonfly.duckdb dragonfly-src 仓库 tags 表（v4.0.0 tagger_date）；dragonfly.duckdb dragonfly-src 仓库 contributors 表（Tigeot 统计）；dragonfly.duckdb dragonfly-src 仓库 commit_files 表（sys/dev/drm/ 目录）；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 5 条） ［A］
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表（Tigeot 统计）；**dragonfly.duckdb** dragonfly-src 仓库 commits 表（DRM 关键词）；**freebsd.duckdb** freebsd-src 仓库 commits 表（DRM2 关键词）；Linux kernel git 仓库 DRM 子系统 commit [EB/OL]. <https://git.kernel.org/>；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 8 条与第 6 条） ［A］
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表与 commits 表（Tigeot DRM 移植统计）；DragonFly kernel@ 邮件列表档案 [EB/OL]. <https://www.dragonflybsd.org/mailinglists/>；Linux kernel DRM 文档 [EB/OL]. <https://www.kernel.org/doc/html/latest/gpu/>；**freebsd.duckdb** freebsd-src 仓库 sys/dev/drm2/ 目录；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 11 条、第 19 条与第 25 条） ［A］

- dragonfly.duckdb dragonfly-src 仓库 commits 表与 contributors 表（2014-2018 年活跃 committer 数与 Dillon/HAMMER2 统计）；dragonfly.duckdb commits 表（dragonfly-src 与 freebsd-src 对照）；dragonfly.duckdb dragonfly-src 仓库 tags 表（v4.6.0 tagger_date）；freebsd.duckdb freebsd-src 仓库 tags 表（release/11.0.0 tagger_date）；DragonFly 4.6 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release46/>**；DragonFly 4.8 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release48/>**；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/>**；FreeBSD 11.0 Release Notes [EB/OL]. freebsd.org/releases/；OpenBSD 5.9 Release Notes [EB/OL]. openbsd.org/59.html；OpenBSD 6.4 Release Notes [EB/OL]. openbsd.org/64.html；**dragonflybsd.org/foundation/** HTTP 404 ［A］
- dragonfly.duckdb dragonfly-src 仓库 commits 表（TOP 5 与 HAMMER2 统计）；dragonfly.duckdb dragonfly-src 仓库 tags 表（v5.0.0 tagger_date）；DragonFly 4.6 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release46/>**；DragonFly 5.0 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release50/>**；Dillon 2017-02-24 users@ 邮件列表“Update on status of master - NUMA and cache-line locality” [EB/OL]. **lists.dragonflybsd.org/pipermail/users/2017-February/313242.html**；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/>** ［A］
- dragonfly.duckdb dragonfly-src 仓库 commits 表与 contributors 表（TOP 5 集中度、Tigeot、HAMMER2、活跃 committer、NVMe 统计）；dragonfly.duckdb commits 表（dragonfly-src 与 freebsd-src 对照）；Dillon 2017-02-24 users@ 邮件列表“Update on status of master - NUMA and cache-line locality” [EB/OL]. **lists.dragonflybsd.org/pipermail/users/2017-February/313242.html**；DPorts 仓库［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ ［A］
- dragonfly.duckdb commits 表（dragonfly-src 与 freebsd-src/openbsd-src 2014-2018 年对照）；dragonfly.duckdb dragonfly-src 仓库 commits 表（HAMMER2 关键词统计）；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6 条、第 8 条与第 19 条） ［A］
- dragonfly.duckdb dragonfly-src 仓库 commits 表（HAMMER2 关键词 2014-2018 年统计）；dragonfly.duckdb dragonfly-src 仓库 tags 表（v5.0.0 tagger_date）；**dragonflybsd.org/foundation/** HTTP 404；FreeBSD Foundation [EB/OL]. **<https://freebsdfoundation.org/>**；OpenBSD Foundation [EB/OL]. **<https://www.openbsdfoundation.org/>**；原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13 条、第 19 条、第 21 条） ［A］

［存目·DEFERRED 登记：①原文献块内粘连第 228 章 6 处子节标题（228.3.2、228.3.3、228.4.2-228.4.5），系错章内容泄漏，经核查报告移除，其归位属跨文件迁移，登记 DEFERRED；②原三处重复 DB_REF:dragonfly.duckdb 块按报告保留单处，另两处删除，块内数据未作任何改动。］
