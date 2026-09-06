---
chapter: 第 166 章
id: CH166
volume: 第08卷-freebsd的范式转换
---

# 第 166 章 freebsd16xcurrent开发概览与版本定位

## 要点

- FreeBSD 主要版本发布周期自 10.0（2014 年 1 月）以来稳定在约 2 年左右：11.0（2016 年 10 月）、12.0（2018 年 12 月）、13.0（2021 年 4 月，因疫情等因素延迟约 4 个月）、14.0（2023 年 11 月）、15.0（2025 年 12 月）、16.0（预计 2027 年 12 月）；〔待核：原文截断，后文待回源〕
- dialog 移除与 GPL 代码清零的合图不在“一方正确、一方错误”的二元判定中，而在 FreeBSD 选择的“base 纯洁化 + ports 多元化”双层架构中——base system 保持 BSD 许可证一致性满足工程原则与商业友好需求，Ports 集合保留 GPL 软件（含 GNU dialog）满足功能兼容与用户选择需求。这一双层架构使“BSD 纯洁化”与“GPL 软件可用”两个看似

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3801] 卷“第08卷-freebsd的范式转换”第 166 章，匹配置信度 folder，原因：folder 第164章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 发布周期的“约两年”是统计规律而非硬性规定——13.0 因疫情、Clang/LLVM 工具链迁移等因素延迟约 4 个月；支持周期 5 年是一般规律，实际 EOL 日期可能根据用户需求和安全团队能力调整；stable/13 原计划 2026 年 4 月 EOL，部分基础设施仍在迁移中。**数据库交叉验证结论**：六个主要版本（10.0-15.0）的 release tag tagger_date 全
- 考据过程留痕——【查证来源】(1) FreeBSD Ports 中 misc/dialog port 经 freshports.org/misc/dialog/ 一手核验，确认 GNU dialog 仍可通过 Ports 安装，“base 纯洁化 + ports 多元化”双层架构在 Ports 层面成立；(2) FreeBSD FreshPorts 三个 ports 经一手核验，确认 dpv 三件

## 文献

- The FreeBSD Project. Release Information [EB/OL]. [2026-07-21]. <https://www.freebsd.org/releases/>; The FreeBSD Project. Supported Releases [EB/OL]. [2026-07-21]. <https://www.freebsd.org/security/#sup>; FreeBSD Release Engineering Team. FreeBSD Release Engineering Documentation [EB/OL]. [2026-07-21]. <https://docs.freebsd.org/en/articles/freebsd-releng/>; FreeBSD Project. release/10.0.0. freebsd-src 仓库 tag [DB/OL]. 2014-01-16T18:43:50Z. tag: release/10.0.0; commit: e3ff8788aa4381f45f5c39efd99c9cbf1b174b5a; FreeBSD Project. release/11.0.0. freebsd-src 仓库 tag [DB/OL]. 2016-09-23T22:37:05Z. tag: release/11.0.0; commit: 671fb7df97631020c42ce55527dc49fffe0656b7; FreeBSD Project. release/12.0.0. freebsd-src 仓库 tag [DB/OL]. 2018-12-07T21:40:35Z. tag: release/12.0.0; commit: 4ba619efbdd2476fb4ac075c6728e17ee02d6bcd; FreeBSD Project. release/13.0.0. freebsd-src 仓库 tag [DB/OL]. 2021-04-09T14:52:16-04:00. tag: release/13.0.0; commit: ea31abc261ffc01b6ff5671bffb15cf910a07f4b; FreeBSD Project. release/14.0.0. freebsd-src 仓库 tag [DB/OL]. 2023-11-17T18:23:38-05:00. tag: release/14.0.0; commit: f9716eee8ab45ad906d9b5c5233ca20c10226ca7; FreeBSD Project. release/15.0.0. freebsd-src 仓库 tag [DB/OL]. 2025-11-28T00:00:00Z. tag: release/15.0.0; commit: 7aedc8de6446ad5a10d553b926423c689f0a3363 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2024-2026 年间：168,386 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. FreeBSD Licensing Policy [EB/OL]. [2026-07-22]. <https://docs.freebsd.org/en/articles/license-guide/>; FreeBSD FreshPorts. misc/dialog [EB/OL]. [2026-07-22]. <https://www.freshports.org/misc/dialog/>; FreeBSD FreshPorts. devel/libfigpar, devel/libdpv, sysutils/dpv [EB/OL]. (2026-06-30)[2026-07-22]. <https://www.freshports.org/>; FreeBSD src repository cgit [EB/OL]. [2026-07-22]. <https://cgit.freebsd.org/src/>; FreeBSD Project. Code-Freeze Status [EB/OL]. (2026-07-02)[2026-07-22]. <https://www.freebsd.org/releng/>; Linuxiac. FreeBSD Base System No Longer Contains Any GPL-Licensed Software [EB/OL]. (2026-07-17)[2026-07-22]. <https://linuxiac.com/>; IT 之家。4 年成功收尾：FreeBSD 基础系统现已不再包含 GPL 许可的软件 [EB/OL]. (2026-07-18)[2026-07-22]. <https://www.ithome.com/0/978/444.htm>; Phoronix. FreeBSD 16 Goes GPL-Free [EB/OL]. (2026-07-15)[2026-07-22]. <https://www.phoronix.com/>; Siciliano A S. bsddialog Project [EB/OL]. (2021-03-27)[2026-07-22]. <https://gitlab.com/alfix/bsddialog> ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2026-2026 年间：44,266 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
