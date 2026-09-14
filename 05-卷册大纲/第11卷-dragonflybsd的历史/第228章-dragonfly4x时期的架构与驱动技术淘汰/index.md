---
chapter: 第 228 章
id: CH228
volume: 第11卷-dragonflybsd的历史
---

# 第 228 章 DragonFly 4.x 时期的架构与驱动技术淘汰

## 要点

- DragonFly v4.0.0（2014-11-23）完成从 FreeBSD DRM 到 Linux DRM 的切换后，BSD 阵营（尤以 FreeBSD GPU 驱动维护者与 NetBSD 用户为代表）对 DragonFly 的 DRM 路线提出三类批评。其一，“血缘背离”批评——**dragonfly.duckdb** 显示 sys/dev/drm/ 目录在 2014 年有 197 个 distinct commit、2015 年 310 个，这些 commit 的主体是 Tigeot 对 Linux DRM 的移植而非对 FreeBSD DRM 的维护，BSD 阵营认为 DragonFly 放弃了 BSD 家族共享的 GPU 驱动代码基础，削弱了 BSD 家族在 GPU 驱动上的代码互助传统
- DragonFly 阵营（以 Matt Dillon 与 François Tigeot 的工程实践为代表）对 BSD 阵营的三类批评提出三层回应。其一，“硬件支持现实”回应——**dragonfly.duckdb** 显示 2014-2015 年间 i915 关键词 commit 146 条、radeon 关键词 44 条，反映 DragonFly 在 FreeBSD DRM 框架下已无法跟上 Intel 与 AMD 的 GPU 硬件迭代速度，Linux DRM 作为上游拥有远超 FreeBSD DRM 的硬件支持覆盖率，DragonFly 选择 Linux DRM 移植是“让用户能用到现代 GPU”的工程现实选择
- BSD 阵营对 DragonFly 阵营的三层回应提出再反驳，并在合图阶段以项目史观总纲第 6 条与第 8 条为框架达成辩证综合。再反驳其一，“硬件支持不等于代码血缘”——BSD 阵营承认 Linux DRM 的硬件支持覆盖率确实高于 FreeBSD DRM，但指出 FreeBSD 通过 linuxkpi 兼容层同样支持现代 GPU，问题不在于“是否支持”而在于“以何种方式支持”，DragonFly 选择直接 Linux DRM 移植而非 linuxkpi 兼容层，是路线选择而非硬件支持的必然


- **bsd_commits.duckdb** 显示 2011-2018 年间四仓库年均 commit 量对照如下（2026-09-12 整改：netbsd-src 原作 16,669/6.9 倍，与 228.2 表内 8 年逐值合计 143,751/8≈17,969 不符，已按订正值统一，dragonfly-src 年均约 2,419 条为基准）：

| 仓库 | 年均 commit 量 | 与 dragonfly-src 比例 |
| --- | --- | --- |
| netbsd-src | 17,969 | 7.4 倍 |
| freebsd-src | 14,650 | 6.1 倍 |
| openbsd-src | 8,213 | 3.4 倍 |
| dragonfly-src | 2,419（基准） | 1.0 倍 |



## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4104] 卷“第11卷-dragonflybsd的历史”第 228 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4105] 卷“第11卷-dragonflybsd的历史”第 228 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4106] 卷“第11卷-dragonflybsd的历史”第 228 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

总纲第 6 条——和解优于斗争：BSD 阵营与 DragonFly 阵营围绕 DRM 路线的批评、回应与再反驳，最终在合图阶段达成辩证综合——DragonFly 的 DRM 切换既非对 BSD 血缘的“背叛”，亦非工程上的“必然”，而是 2014 年资源约束与硬件支持现实下的偶然工程选择，两条路线的争端以和解而非一方压倒收场；总纲第 8 条——本体论上各方平等：FreeBSD DRM 的独立适配与 Linux DRM 的直接移植在本体论上平等，各有代价与收益，技术路线的兴替不构成价值上的高下判分

## 辨析

- **openbsd.duckdb** 显示 OpenBSD 移除 i386 的精确时间须以 openbsd-src 仓库 tag 核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］——**openbsd.duckdb** openbsd-src 仓库 tag 列表为空（可能因仓库镜像未抓取 tag），OpenBSD 5.7 release date 2015-05-01 须以 openbsd.org/57.html 核验
- 考据过程留痕——【查证来源】DragonFly BSD 4.0 Release Notes（**<https://www.dragonflybsd.org/release40/>**）经 WebFetch 一手核验，原文记载“DragonFly 4.0 now supports GPUs from the Haswell family, and OpenGL acceleration is now available out of the box”与“The drm/i915 driver is now mostly based on the Linux 3.8.13 implementation and is no longer similar to the FreeBSD driver”，确认 DragonFly 选择 Linux DRM 移植后获得了 Haswell GPU 支持与 OpenGL 加速
- 考据过程留痕——【查证来源】**dragonfly.duckdb** dragonfly-src 仓库 contributors 表 Tigeot first = 2011-03-06 last = 2020-12-19 total = 1346 经数据库查询核验，末次 commit 2020-12-19 为“维护负担的双向性”再反驳提供代码级证据——Tigeot 停止贡献后 DragonFly 的 DRM 维护进入低活跃期
- **dragonfly.duckdb** 显示 commit 量与项目实际影响力无简单线性关系——NetBSD 年均 commit 量最高（16669 条）但其市场份额未必高于 FreeBSD；**dragonfly.duckdb** 显示 DragonFly TOP 5 集中度 70.6% 反映巴士因子风险——若 TOP 5 贡献者中任何一人退出，DragonFly 维护能力将受严重影响；市场份额数据需谨慎采用——BSD 项目通常无商业销售数据，需结合镜像下载量、邮件列表活跃度、第三方调查等多源数据交叉验证

## 文献

- **dragonfly.duckdb** commits 表（四仓库 2014-2018 年对照）；**dragonfly.duckdb** dragonfly-src 仓库 tags 表（v4.0.0 tagger_date）；**freebsd.duckdb** freebsd-src 仓库 tags 表（release/11.0.0 tagger_date）；FreeBSD 11.0/14.0 release notes [EB/OL]. **<https://www.freebsd.org/releases/>**；OpenBSD 5.7 release notes [EB/OL]. **<https://www.openbsd.org/57.html>**；NetBSD 7.x/8.x release notes [EB/OL]. **<https://www.netbsd.org/releases/>** ［A］
- **dragonfly.duckdb** dragonfly-src 仓库 commit_files 表（sys/dev/drm/ 目录）；**dragonfly.duckdb** dragonfly-src 仓库 contributors 表（Tigeot 统计）；**dragonfly.duckdb** dragonfly-src 仓库 commits 表（DRM 切换关键 commit）；DragonFly BSD 4.0 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release40/>**；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/>**；dragonflybsd.org/kernel/ LWKT 文档 [EB/OL]；freebsd.org/cgi/man.cgi FreeBSD DRM 手册页 [EB/OL]；kernel@ 邮件列表档案 ［A］
- **dragonfly.duckdb** dragonfly-src 仓库 commits 表（i915/radeon 关键词统计）；**dragonfly.duckdb** commits 表（四仓库对照）；**dragonfly.duckdb** dragonfly-src 仓库 contributors 表（Tigeot 统计）；DragonFly BSD 4.0 Release Notes [EB/OL]. **<https://www.dragonflybsd.org/release40/>**；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/>**；dragonflybsd.org/community/ BSD 许可证声明 [EB/OL] ［A］
- **dragonfly.duckdb** dragonfly-src 仓库 contributors 表（Tigeot 统计）；**dragonfly.duckdb** dragonfly-src 仓库 commits 表（Tigeot 活跃度趋势）；**freebsd.duckdb** freebsd-src 仓库 commits 表（linuxkpi 相关 commit）；DragonFly BSD 官方历史页面 [EB/OL]. **<https://www.dragonflybsd.org/history/>**；**原材料/哲学/项目统摄史观/第 25 章.md**（总纲第 5、6、8 条）；dragonflybsd.org 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。
> 2003-2026 年间：656,206 次提交。
> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- **dragonfly.duckdb** commits 表（四仓库 2011-2018 年对照与 DragonFly 活跃 committer 数）；**dragonfly.duckdb** dragonfly-src 仓库 commits 表（2014-2017 年 TOP 5）；各项目 release notes 与官网；BSD 相关市场调研报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。
> 2011-2018 年间：568,339 次提交。
> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
