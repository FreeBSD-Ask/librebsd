---
chapter: 第 166 章
id: CH166
volume: 第08卷-freebsd的范式转换
---

# 第 166 章 FreeBSD 16.x CURRENT 开发概览与版本定位

## 要点

- FreeBSD 主要版本发布周期自 10.0（2014 年 1 月）以来稳定在约 2 年左右：11.0（2016 年 10 月）、12.0（2018 年 12 月）、13.0（2021 年 4 月，因疫情等因素延迟约 4 个月）、14.0（2023 年 11 月）、15.0（2025 年 12 月）、16.0（预计 2027 年 12 月）；相邻两个大版本的间隔在 24—33 个月之间，“约两年”是统计意义上的节奏而非固定承诺，16.0 的目标日期已列入 FreeBSD 官方 Release Engineering 时间表（2027 年 12 月），届时 main 分支将从 16.0-CURRENT 转入新的 stable/16
- dialog 移除与 GPL 代码清零的合图不在“一方正确、一方错误”的二元判定中，而在 FreeBSD 选择的“base 纯洁化 + ports 多元化”双层架构中——base system 保持 BSD 许可证一致性满足工程原则与商业友好需求，Ports 集合保留 GPL 软件（含 GNU dialog）满足功能兼容与用户选择需求。这一双层架构使“BSD 纯洁化”与“GPL 软件可用”两个看似冲突的目标在同一系统内并行不悖：base 系统于 2026 年 7 月完成 GPL 代码清零，而 GNU dialog 等 GPL 软件在 Ports 集合中继续可安装、可使用

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3801] 卷“第08卷-freebsd的范式转换”第 166 章；该记录匹配置信度取值“folder”非法（系自动匹配把目录名误写入置信度字段），原因字段“folder 第164章”指向第 164 章属错位残留，本章归属以卷内路径为准，数据库侧记录待库侧治理修正

## 史观

- 总纲第 5 条——没有必然性，只有偶然性：FreeBSD 主要版本的发布节奏是统计规律而非必然规律——13.0 因疫情与 Clang/LLVM 工具链迁移延迟约 4 个月，stable/13 的 EOL 因部分基础设施仍在迁移而调整，16.0 的目标日期（2027 年 12 月）亦只是官方 Release Engineering 时间表上的目标；没有哪一次发布“必然按期”，每个具体日期都由具体的偶然条件凑成。
- 总纲第 18 条——时间是一种形式主义：版本号、release tag、发布时间表是 FreeBSD 项目对连续开发流的形式主义切分——“约两年”的周期、“五年支持”的承诺、目标日期的设定，都是把连续的时间组织为可管理单元的形式构造，而非开发过程本身内在的节律。
- 总纲第 4 条——分离聚合是永恒规律：base 系统与 Ports 集合的分立是 FreeBSD 许可证结构的基本形态——GPL 代码自 base 系统分离出去（2026 年 7 月清零），又在 Ports 集合中聚合存续（GNU dialog 及 dpv 三件仍可安装），“纯洁化”与“可用性”依托分离结构各得其所。
- 总纲第 25 条——逻辑是形式主义而非世界本身的结构：base 系统的 GPL 清零是许可证形式一致性的自我要求——被移除的 GPL 代码在功能上并无缺陷，清除它源于工程原则的逻辑自洽，而非技术结构本身的要求；dialog 的对话界面由 bsddialog 重建，形式替代形式。
- 总纲第 3 条——不存在进步，只有权力再分配：16.x 时期的 GPL 清零不应写成“更纯粹、更先进”的进步叙事——它是许可证权力边界的再划分：谁可进入 base、谁被移至 Ports，何种许可证在哪一层被允许，这是权力结构的重新分配，形式在流转，无高下之别。

## 辨析

- 发布周期的“约两年”是统计规律而非硬性规定——13.0 因疫情、Clang/LLVM 工具链迁移等因素延迟约 4 个月；支持周期 5 年是一般规律，实际 EOL 日期可能根据用户需求和安全团队能力调整；stable/13 原计划 2026 年 4 月 EOL，部分基础设施仍在迁移中。**数据库交叉验证结论**：六个主要版本（10.0-15.0）的 release tag tagger_date 全部早于或接近该版本的官方公告日期——release/10.0.0 标记于 2014-01-16（公告 2014-01-20）、release/15.0.0 标记于 2025-11-28（公告 2025-12-02），tag 时序与发布时序一致，发布周期统计在此基础上成立
- 考据过程留痕——【查证来源】(1) FreeBSD Ports 中 misc/dialog port 经 freshports.org/misc/dialog/ 一手核验，确认 GNU dialog 仍可通过 Ports 安装，“base 纯洁化 + ports 多元化”双层架构在 Ports 层面成立；(2) FreeBSD FreshPorts 三个 ports 经一手核验，确认 dpv 三件（devel/libfigpar、devel/libdpv、sysutils/dpv）均在 Ports 集合中存在且可安装，dialog 前端依赖链在 Ports 层面完整

## 文献

- The FreeBSD Project. Release Information [EB/OL]. [2026-07-21]. <https://www.freebsd.org/releases/>; The FreeBSD Project. Supported Releases [EB/OL]. [2026-07-21]. <https://www.freebsd.org/security/#sup>; FreeBSD Release Engineering Team. FreeBSD Release Engineering Documentation [EB/OL]. [2026-07-21]. <https://docs.freebsd.org/en/articles/freebsd-releng/>; FreeBSD Project. release/10.0.0. freebsd-src 仓库 tag [DB/OL]. 2014-01-16T18:43:50Z. tag: release/10.0.0; commit: e3ff8788aa4381f45f5c39efd99c9cbf1b174b5a; FreeBSD Project. release/11.0.0. freebsd-src 仓库 tag [DB/OL]. 2016-09-23T22:37:05Z. tag: release/11.0.0; commit: 671fb7df97631020c42ce55527dc49fffe0656b7; FreeBSD Project. release/12.0.0. freebsd-src 仓库 tag [DB/OL]. 2018-12-07T21:40:35Z. tag: release/12.0.0; commit: 4ba619efbdd2476fb4ac075c6728e17ee02d6bcd; FreeBSD Project. release/13.0.0. freebsd-src 仓库 tag [DB/OL]. 2021-04-09T14:52:16-04:00. tag: release/13.0.0; commit: ea31abc261ffc01b6ff5671bffb15cf910a07f4b; FreeBSD Project. release/14.0.0. freebsd-src 仓库 tag [DB/OL]. 2023-11-17T18:23:38-05:00. tag: release/14.0.0; commit: f9716eee8ab45ad906d9b5c5233ca20c10226ca7; FreeBSD Project. release/15.0.0. freebsd-src 仓库 tag [DB/OL]. 2025-11-28T00:00:00Z. tag: release/15.0.0; commit: 7aedc8de6446ad5a10d553b926423c689f0a3363 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. FreeBSD Licensing Policy [EB/OL]. [2026-07-22]. <https://docs.freebsd.org/en/articles/license-guide/>; FreeBSD FreshPorts. misc/dialog [EB/OL]. [2026-07-22]. <https://www.freshports.org/misc/dialog/>; FreeBSD FreshPorts. devel/libfigpar, devel/libdpv, sysutils/dpv [EB/OL]. (2026-06-30)[2026-07-22]. <https://www.freshports.org/>; FreeBSD src repository cgit [EB/OL]. [2026-07-22]. <https://cgit.freebsd.org/src/>; FreeBSD Project. Code-Freeze Status [EB/OL]. (2026-07-02)[2026-07-22]. <https://www.freebsd.org/releng/>; Linuxiac. FreeBSD Base System No Longer Contains Any GPL-Licensed Software [EB/OL]. (2026-07-17)[2026-07-22]. <https://linuxiac.com/>; IT 之家。4 年成功收尾：FreeBSD 基本系统现已不再包含 GPL 许可的软件 [EB/OL]. (2026-07-18)[2026-07-22]. <https://www.ithome.com/0/978/444.htm>; Phoronix. FreeBSD 16 Goes GPL-Free [EB/OL]. (2026-07-15)[2026-07-22]. <https://www.phoronix.com/>; Siciliano A S. bsddialog Project [EB/OL]. (2021-03-27)[2026-07-22]. <https://gitlab.com/alfix/bsddialog> ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2026-2026 年间：44,266 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
