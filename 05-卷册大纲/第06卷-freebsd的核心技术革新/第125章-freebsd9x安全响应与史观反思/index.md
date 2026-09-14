---
chapter: 第 125 章
id: CH125
volume: 第06卷-freebsd的核心技术革新
---

# 第 125 章 freebsd9x安全响应与史观反思

## 史料

- [WEB:freebsd.org/administration.html] FreeBSD Security Team 架构（官方一手）：安全通告（FreeBSD-SA）
- [WEB:freebsd.org/security/advisories/] FreeBSD Security Advisories Archive（官方一手）：SA-12:03.bind、SA-12:04.sysret、SA-13:03.openssl 等 9.x 周期安全通告原文
- [DB:freebsd.duckdb] freebsd-src 仓库 commits 表（本项目自建，0 信任）：9.x 周期 CVE commit 与 security fix commit 元数据（93 条 CVE commit／28 个 CVE／33 条无 CVE 编号 commit）
- [WEB:dblp.uni-trier.de MKMcKusick] dblp 书目（一手）：FreeBSD 9.x 时期相关安全/文件系统研究的学术发表链（Soft Updates/FFS 系列论文）

## 要点

- 9.x 版本周期文件覆盖窗口（**2012-01-01** 至 **2014-01-01**，对应 9.0-9.2-RELEASE 开发与维护期）freebsd-src 仓库共 **93 条 CVE 相关 commit**、去重后 **28 个 CVE**，另有 **33 条无 CVE 编号的 security fix commit**；将窗口扩展至 9.x 全支持周期（2012.1 至 2017.1，9.3-RELEASE 支持至 2017.1.1）则 CVE commit 增至 **312 条**；28 个 CVE 全部 “无 CVSS v3 评分”——这一元数据缺失反映 NVD 对 2012-2014 年 FreeBSD CVE 的覆盖长期滞后于 Linux 主流发行版；9.x 周期 BIND/**named(8)** 与 OpenSSL 是两个主要 CVE 来源，**sendmail(8)**、**sshd(8)**、Linuxulator 等子系统次之；9.x 时期 base 系统仍包含 BIND（10.0 才移除）与 sendmail（10.0 才换为 **dma(8)**），是 9.x 周期安全债务的两大结构性来源。9.x 周期关键安全事件时间线汇总见下表。
- **2012 年 5 月 3 日** Bjoern A. Zeeb（bz@）在 freebsd-src 仓库单日提交 **9 个 OpenSSL 修复 commit**（hash `63a04068615b`、`8b21581b6026`、`09a865e4fb3a`、`34e8deeed81e`、`51b069ec20bf`、`2ba20502898f`、`b5b482d053f2`、`a8ec49085f69`、`a95abaf17347`），一次性处理 **5 个 CVE**：CVE-2011-4109（OpenSSL 0.9.8s 之前版本 double free）、CVE-2011-4576（SSL 3.0 实现缺陷）、CVE-2011-4619（Server Gated Cryptography 实现）、CVE-2012-0884（CMS/PKCS #7 实现问题）、CVE-2012-2110（`asn1_d2i_read_bio` 函数堆缓冲区溢出）；**2013 年 4 月 2 日** Xin LI（delphij@）修复 CVE-2013-0166（OpenSSL CBC Lucky 13）与 CVE-2013-0169（TLS/DTLS 时序攻击），后者即业界著名的 “Lucky 13” 时序攻击；**SA-13:03.openssl**（2013-04-02 发布）是这两组 CVE 的官方公告——但 SA-13:03 发布时间晚于 2012-05-03 修复 commit 近一年，反映 9.x 时期 SA 流程中 commit 与 SA 发布的时间差通常较大
- 9.x 周期 BIND/**named(8)** 相关 SA 共 **6 个**——SA-12:03.bind、SA-12:05.bind、SA-12:06.bind、SA-13:01.bind、SA-13:04.bind、SA-13:07.bind，是 9.x 周期最密集的单一组件 CVE 来源；2012-06-12 Bjoern Zeeb 单日 **9 个 commit** 修复 CVE-2012-0217、CVE-2012-1667（**named(8)** 零长度 RDATA 字段崩溃）；2012-11-22 Simon L. B. Nielsen 单日 **7 个 commit** 修复 CVE-2012-4244、CVE-2012-4445、CVE-2012-4576、CVE-2012-5166（**named(8)** 多重 DoS）；2013-07-26 Xin LI 修复 CVE-2013-4851、CVE-2013-4854（**named(8)** RFC 5011 与 DNSSEC DoS）；9.x 是 BIND 在 base 的最后岁月——**10.0-RELEASE（2014-01-20）才将 BIND 从 base 移除**，转由 ports/dns/bind9 维护；9.x 时期 BIND 在 base 的存在使 **named(8)** CVE 必须通过 SA 流程修复，工作量巨大
- CVE-2012-4576 是 9.x 周期罕见的 FreeBSD base 系统特有 CVE——“Input Validation Flaw allows local users to gain elevated privileges”（输入验证缺陷允许本地用户获取提升权限）；**2012-11-23** Colin Percival 通过 MFS（Merge From Stable）补丁将该修复回溯至 HEAD（commit `43f13bea3529`），commit_subject 明确 “MFS security patches which seem to have accidentally not reached HEAD”——反映 9.x 时期安全补丁的双向回溯工作流（stable→HEAD 与 HEAD→stable 并存）；与同期 OpenSSL/BIND 第三方 CVE 不同，这是 FreeBSD base 自身代码的输入验证缺陷——本地用户可通过特定输入触发权限提升
- **SA-12:04.sysret**（**2012 年 6 月 12 日** 发布）修复 CVE-2012-0217——Xen 4.1.2 及更早版本 x86-64 内核系统调用功能中的权限提升漏洞；该漏洞允许 64 位 PV guest 用户模式在异常情况下获得内核权限，影响所有运行 Xen hypervisor 的系统；**2012-06-12** Bjoern Zeeb 单日提交多个 commit 修复 sysret 漏洞，与同日 SA-12:03.bind 修复同步发布——这是 9.0-RELEASE 发布后第一个月内的密集安全响应；这一 SA 反映 9.x 时期虚拟化安全的早期认知——bhyve 尚未发布（10.0 才正式），FreeBSD 主要作为 Xen guest 受影响，而非 hypervisor

## 史观

- 专题语（不设条号）：9.x 周期 28 个 CVE 全部无 CVSS v3 评分反映两个事实——其一，NVD 对 BSD 系 CVE 的元数据覆盖长期滞后于 Linux 主流发行版；其二，CVSS v3.0 于 2015 年发布，2012-2014 年 CVE 多以 CVSS v2 标注或不评分，9.x 周期安全态势的横向对比存在天然困难，任何 “9.x 比 14.x 更安全” 的结论都难以成立（原挂「总纲第 17 条——软件工程」，基线第 17 条为“证明世界先于解释和改造世界”，主题对不上基线，按 R2140 先例改不设条号专题语——2026-09-12 整改）。
- 总纲第 13 条——法律与道德是利益分配：许可证争议的法律文本（GPLv3 §5/§6/§11）与道德话语（“自由” “纯洁”）均为利益分配的形式主义工具。BSD patch 替换中，“接受” BSD 许可版本与 “驱逐” GPLv3 增强版本的边界划定本身反映 FreeBSD 商业生态的利益取舍——BSD 许可不威胁专利组合与商业分发自由，GPLv3 §11 威胁专利组合，故 “反 GPLv3” 非 “意识形态反 copyleft” 而是 “利益反专利风险与商业义务”。
- 总纲第 22 条——知识注定过时：CVSS v3.0 迟至 2015 年才发布，9.x 周期（2012-2014）CVE 的评分知识以旧版标准或不评分状态记载，安全评级方法本身随知识演进而过时，故对 9.x 安全态势的历史评价须回到一手 commit 数据重新考据，而非沿用当年缺失的评分。
- 总纲第 9 条——经验优先：NVD 元数据的系统性缺失使二手评分不可依赖，本小节以 freebsd-src 仓库 commit 级经验数据（93 条 CVE commit、全支持周期 312 条 CVE commit）为优先证据，而非以缺失的 CVSS 评分推演结论。
- 总纲第 18 条——时间是一种形式主义：同一“9.x 周期”在版本周期窗口（2012.1-2014.1，93 条）与全支持周期窗口（2012.1-2017.1，312 条）下得出两个不同数字，说明时间窗口是人为切分的形式主义框架，而非客体固有的时间尺度。

## 辨析

- **数据窗口辨析**：版本周期文件覆盖 2012.1-2014.1（开发与 9.0-9.2-RELEASE 维护期），但 9.3-RELEASE 支持至 2017.1.1——故 “9.x 周期” 在安全响应语境下有两个不同时间窗口：① 版本周期文件窗口（2012.1-2014.1，93 条 CVE commit）；② 全支持周期窗口（2012.1-2017.1，312 条 CVE commit）；
- 按 0 信任原则考据。【查证来源】总纲第 13 条系经 Read 核实的项目统摄史观原文（**02-sacred源材料/sacred_sources.duckdb（第 25 章）** 第 17 行，“13. **法律与道德是利益分配**。任何道德问题本质上是利益问题，社区治理亦是形式主义的政治产物”，2026-07-23 一手核验），引用确证；项目史观总纲第 11 章 11.5 节 “任何道德问题本质上是利益问题” 系总纲第 13 条的章节级阐述，经 Read 核实（**02-sacred源材料/sacred_sources.duckdb（第 11 章）** 第 27 行）。

## 文献

- FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2012-2017)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; FreeBSD Project. **freebsd.duckdb** — freebsd-src commits table [DB/OL]. 2026-07-22. SQL: `SELECT count(*) FROM commits WHERE repo_name = ‘freebsd-src’ AND author_da`〔存疑：著录原文中 SQL 语句于 `author_da` 处截断，完整查询条件与结果未能回源，待补〕
- **02-sacred源材料/sacred_sources.duckdb（第 25 章）**（总纲第 13 条）；**02-sacred源材料/sacred_sources.duckdb（第 11 章）**（11.1、11.5 节）；Free Software Foundation. GNU General Public License Version 3 [Z]. 2007-06-29（§11）；Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01（§3）. ［A］

## 125.20.2 总纲第 15 条审视——文化即形式主义

- 要点：总纲第 15 条断言 “文化即形式主义。传统在形式主义化过程中被遮蔽与重构。知音难觅同样适用于技术社区”。（小节完整内容见同章“125.20-项目统摄史观审视-BSD-patch-替代-GNU-patch-争议的方法论反思.md”）

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。