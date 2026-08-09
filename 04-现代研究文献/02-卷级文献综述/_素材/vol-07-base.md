# 第 7 卷综述素材（T1 三源合一，2026-08-04 自动生成）

> 卷目录：第07卷-freebsd的工程体系重构｜章范围：ch135-ch154

## ① 现有研究（references_fulltext，2 条）

- [887] acm-sigplan-notices（Ritchie，1993）
- [1138] Atlas Shrugged（Rand A，1957）

## ② 研究缺口（doubts_to_resolve，78 条）

- id=477 [resolved] - 辨析：原大纲本节列入的 "CVE-2002-0639 ISS X-Force 披露" 和 "CVE-2024-6387 Qualys regreSSHion
- id=478 [resolved] - 要点：FreeBSD 的内存保护机制演进：(1) 栈保护（SSP/ProPolice）——由 Erez Zadok 等人引入，FreeBSD 7.x/8.x
- id=479 [resolved] - 辨析："FreeBSD 不支持 W^X/ASLR" 说法错误——FreeBSD 10.x 起即支持这些机制，只是默认启用时间较晚；"内存保护机制可以完全阻止
- id=480 [resolved] - 要点：FreeBSD Security Team 由 Security Officer 领导，是负责接收安全漏洞报告、协调修复、发布安全公告的专门志愿者团队
- id=481 [resolved] - 辨析：历任 Security Officer 的完整名单和精确任期在公开资料中并不完整——早期 Security Officer 记录分散在邮件列表公告中，
- id=482 [resolved] - 要点：**freebsd-update(8)** 由 Colin Percival 开发，是 FreeBSD 的二进制安全更新工具，支持 fetch/ins
- id=483 [resolved] - 辨析：“freebsd-update 在 FreeBSD 6.0 引入 base”——经手册页和 Release Notes 核实，freebsd-upda
- id=484 [resolved] - 要点：FreeBSD VuXML（Vulnerability XML）是 FreeBSD Ports Collection 的软件漏洞数据库，记录 port
- id=485 [resolved] - 辨析：原大纲本节列入的 "Anthropic Claude Mythos 2026.4 AI 发现 OpenBSD TCP SACK 27 年漏洞" 事件—
- id=486 [resolved] - 要点：OpenBSD 安全机制与 FreeBSD 对比：(1) W^X（Write XOR Execute）——OpenBSD 在 2003 年（OpenB
- id=487 [resolved] - 要点：FreeBSD Security Team 由 Security Officer 领导，是负责接收安全漏洞报告、协调修复、发布安全公告的专门志愿者团队
- id=488 [resolved] - 辨析："Security Team 成员就是所有 src committer"——不是，Security Team 是专门处理安全事件、协调安全公告的特定团
- id=489 [resolved] - 辨析：SMPng 期间网络性能倒退的程度常被夸张化——FreeBSD 5.x 在单 CPU 上性能接近 4.x，但在多 CPU 上由于锁竞争严重性能下降明显
- id=490 [resolved] - 辨析："Linux 网络栈比 FreeBSD 快" 是不严谨的概括——在 Netflix CDN 的 TLS 终止场景下，带 kTLS 的 FreeBSD 
- id=491 [resolved] - 辨析：netgraph 引入版本经 FreeBSD 3.4 Release Notes 一手核验为 FreeBSD 3.4（1999 年），而非先前误写的 
- id=492 [resolved] - 辨析：FreeBSD 网桥实现的历史有三个阶段：① 早期 FreeBSD 2.x-4.x 时代使用用户态 `bridge' 程序或 dummynet 网桥，
- id=493 [resolved] - 辨析：功能对比常见误区：“Linux bridge 可以做交换机而 FreeBSD 不行”——两者都可以用作二层交换机，功能对等；“FreeBSD lagg
- id=494 [resolved] - 辨析：epair 引入精确版本——epair 代码出现在 FreeBSD 7.1 前后，但真正稳定和可用是在 FreeBSD 8.0 与 VNET 一起完成
- id=495 [resolved] - 辨析："VNET 是模仿 Linux network namespace"——从时间线看两者几乎并行开发（2006-2009），VNET 设计源于 Trus
- id=496 [resolved] - 辨析：KTLS 作者问题——John Baldwin 是 KTLS 框架的主要设计者和实现者，Andrew Gallatin（Netflix）做了大量性能优
- id=497 [resolved] - 辨析：漏洞影响的 FreeBSD 版本——SA-19:08 显示受影响版本为 FreeBSD 11.2、11.3、12.0、12.1，使用 RACK TCP
- id=498 [resolved] - 辨析：Dillon 对 FreeBSD SMPng 的批评——Dillon 在 2003 年分叉时公开批评 FreeBSD 的细粒度锁路线太复杂，认为会导致
- id=499 [resolved] - 辨析：地域仅以邮箱 ccTLD 作弱推断，个人/免费邮箱志愿者（1,998 次）地域难定，相关占比一律标 ［ 存疑脚注：此处事实待多源交叉验证 ］；绝不按姓
- id=500 [resolved] - 辨析：任何具体国别/族裔占比均不得外推为群体结论；非提交贡献者（文档、ports、翻译、漏洞上报者）的记录缺口标注 ［ 存疑脚注：此处事实待多源交叉验证 ］
- id=501 [resolved] - 辨析：按 0 信任原则考据，FSF 许可证列表将 BSD 列为“GPL 兼容”系经联网核实的 FSF 官方一手立场（gnu.org/licenses/lic
- id=502 [resolved] - 辨析：按 0 信任原则考据，“BSDL 兼容 GPLv3 但反向不成立”系经 FSF GPL FAQ（#WhatDoesCompatMean）与 GPLv3
- id=503 [resolved] - 辨析：按 0 信任原则考据，“Apache 2.0 含专利报复条款而 FreeBSD 接受”系经 Apache 2.0 §3 文本与 LLVM LICENS
- id=504 [resolved] - 文献：同上节。 ［ 存疑：Hubbard 1990 年代言论与 Baldwin 等当代开发者言论的对比系基于邮件列表通览的概括性归纳，未逐条引用具体邮件 I
- id=505 [resolved] | powerpc/powerpc64 | 是 | FreeBSD 11/12 逐步完善 | 较晚版本 | powerpc64le 在较新版本 Tier 2 [
- id=506 [resolved] - 辨析：按 0 信任原则考据，总纲第 13 条系经 Read 核实的项目统摄史观原文（第 25 章.md 第 17 行），引用确证。“CDDL 被接受而 GP
- id=507 [resolved] - 辨析：按 0 信任原则考据，总纲第 19 条与第 19 章 19.2/19.3 节系经 Read 核实的项目统摄史观原文，引用确证。“FreeBSD 叙事工
- id=508 [resolved] - 辨析：按 0 信任原则考据，总纲第 21 条与第 21 章 21.1/21.2 节系经 Read 核实的项目统摄史观原文，引用确证。“FreeBSD 改革方
- id=509 [resolved] - 辨析：考据过程留痕——【查证来源】FSF 许可证评论页面经 **<https://www.gnu.org/licenses/license-list.htm
- id=510 [resolved] - 辨析：考据过程留痕——【查证来源】FSF 许可证评论页面经 WebFetch 一手核验（2026-07-23），确认“BSD 许可证兼容 GNU GPL”表
- id=511 [resolved] - 辨析：按 0 信任原则考据，GPL 阵营批评层的核心法理论点须区分三层：①FSF 官方确认“BSD 许可证兼容 GNU GPL”——此为确证一手史料，但“兼
- id=512 [resolved] - 辨析：考据过程留痕——【查证来源】GPLv3 官方文本经 gnu.org 一手核验，§5c“作品”定义与 copyleft 传染条款、§6“用户产品”与安装
- id=513 [resolved] - 辨析：考据过程留痕——【查证来源】FreeBSD Foundation 2007 年公开信经 **<https://www.freebsdfoundatio
- id=514 [resolved] - 辨析：考据过程留痕——【查证来源】FreeBSD Foundation 2007 公开信经 **<https://www.freebsdfoundation
- id=515 [resolved] - 辨析：按 0 信任原则考据，反批评层的核心法律论证须区分三层：①GPLv3 §5c copyleft 传染——此为 GPLv3 法律文本确证条款，但“bas
- id=516 [resolved] - 辨析：考据过程留痕——【查证来源】GPLv3 §6“用户产品”定义与 §11 专利报复条款经 gnu.org 一手核验，FSF 许可证评论页面经 WebFe
- id=517 [resolved] - 辨析：考据过程留痕——【查证来源】总纲第 13 条系经 Read 核实的项目统摄史观原文（第 25 章.md 第 17 行），引用确证；GPLv3 §11 
- id=518 [resolved] - 要点：GPL 阵营再回应层与合图层的一手史料包括 GPLv3 官方法律文本（§6“用户产品”定义、§11 专利报复条款）、Apache 2.0 官方法律文本
- id=519 [resolved] - 辨析：按 0 信任原则考据，再回应层与合图层的核心论证须区分三层：①GPLv3 §6“用户产品”定义的法律争议——此为 GPLv3 法律文本确证条款，但“用
- id=520 [resolved] - 辨析：考据过程留痕——【查证来源】总纲第 13 条系经 Read 核实的项目统摄史观原文（第 25 章.md 第 17 行），引用确证；本章四层辩证链史料构
- id=521 [resolved] - 要点：总纲第 19 条断言“解释学循环是历史认识的根本条件。前理解的差异使分歧不可避免。权力与知识在历史书写中共谋——什么被记录、什么被遗忘，本身就是权力行
- id=522 [resolved] - 辨析：考据过程留痕——【查证来源】总纲第 19 条系经 Read 核实的项目统摄史观原文（第 25 章.md 第 23 行），引用确证；项目史观总纲第 19
- id=523 [resolved] - 要点：总纲第 21 条断言“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”。以此审视 GP
- id=524 [resolved] - 辨析：考据过程留痕——【查证来源】总纲第 21 条系经 Read 核实的项目统摄史观原文（第 25 章.md 第 25 行），引用确证；项目史观总纲第 21
- id=525 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com
- id=526 [resolved] - 辨析：**makefs(8)** 最初由 NetBSD 的 Christos Zoulas 于 2000 年代初开发，FreeBSD 从 NetBSD 导入
- id=527 [resolved] - 辨析：AI 辅助开发在 FreeBSD 社区的接受度存在差异——部分老派开发者对 AI 生成代码持怀疑态度（内核代码必须精确理解才能写入），部分年轻开发者积
- id=528 [resolved] - 辨析：Mike Karels 在 BSD 历史上的地位经常被低估——他是 4.3BSD/4.4BSD 与 McKusick、Bostic、Quarterma
- id=529 [resolved] - 辨析：**cvs2svn tagger_name 的特殊性**：1995-2008 年间 tagger_name 显示为 `cvs2svn`，是 SVN 迁
- id=530 [resolved] | FreeBSD 1.0 | 1993-11-19［ 存疑脚注 ］ | 1993-11-01T00:00:00-08:00 | svn2git | -18 |
- id=531 [resolved] | FreeBSD 3.0 | 1999-01-21［ 存疑脚注 ］ | 1999-01-21T00:55:32Z | cvs2svn | 0 | `76b53
- id=532 [resolved] | FreeBSD 4.0 | 2000-03-20［ 存疑脚注 ］ | 2000-03-20T08:47:53Z | cvs2svn | 0 | `172a0
- id=533 [resolved] | FreeBSD 5.0 | 2003-01-16［ 存疑脚注 ］ | 2003-01-16T16:56:23Z | cvs2svn | 0 | `47227
- id=534 [resolved] | FreeBSD 6.0 | 2005-11-03［ 存疑脚注 ］ | 2005-11-03T00:35:26Z | cvs2svn | 0 | `3d215
- id=535 [resolved] | FreeBSD 7.0 | 2008-02-24［ 存疑脚注 ］ | 2008-02-24T05:45:17Z | cvs2svn | 0 | `ba209
- id=536 [resolved] | FreeBSD 8.0 | 2009-11-21［ 存疑脚注 ］ | 2009-11-21T06:13:29Z | Ken Smith | 0 | `59d
- id=537 [resolved] | FreeBSD 9.0 | 2012-01-02［ 存疑脚注 ］ | 2012-01-02T18:59:55Z | Ken Smith | 0 | `4e2
- id=538 [resolved] | FreeBSD 10.0 | 2014-01-20［ 存疑脚注 ］ | 2014-01-16T18:43:50Z | Glen Barber | -4 | 
- id=539 [resolved] | FreeBSD 11.0 | 2016-09-23［ 存疑脚注 ］ | 2016-09-23T22:37:05Z | Glen Barber | 0 | `
- id=540 [resolved] | FreeBSD 12.0 | 2018-12-07［ 存疑脚注 ］ | 2018-12-07T21:40:35Z | Glen Barber | 0 | `
- id=541 [resolved] | FreeBSD 13.0 | 2021-04-13［ 存疑脚注 ］ | 2021-04-09T14:52:16-04:00 | Glen Barber | 
- id=542 [resolved] | FreeBSD 14.1 | 2024-06-04［ 存疑脚注 ］ | 2024-05-30T17:34:21-07:00 | Colin Percival
- id=543 [resolved] | FreeBSD 14.2 | 2024-12-03［ 存疑脚注 ］ | 2024-11-29T00:00:00Z | Colin Percival | -4
- id=544 [resolved] | FreeBSD 13.5 | 2025-03-11［ 存疑脚注 ］ | 2025-03-07T00:00:00Z | Colin Percival | -4
- id=545 [resolved] **Release Engineer 交接考据**：① Jordan K. Hubbard（1994-11-22 至 1995-06-10）：FreeBSD 2
- id=546 [resolved] - 要点：FreeBSD Core Team 每两年由活跃 committer 选举产生，是项目的 "董事会"，负责项目整体方向与重大决策；截至 2026 年 
- id=547 [resolved] - 辨析：Hiroki Sato（hrs@）在 FreeBSD 社区地位崇高——他是文档项目负责人、亚洲 BSD 社区（特别是日本 BSD 用户组）的核心组织者
- id=548 [resolved] - 辨析：地域仅以邮箱 ccTLD 作弱推断，个人/免费邮箱志愿者（1,932 次）地域难定，相关占比一律标 ［ 存疑脚注：此处事实待多源交叉验证 ］；绝不按姓
- id=549 [resolved] - 辨析：任何具体国别/族裔占比均不得外推为群体结论；非提交贡献者（文档、ports、翻译、漏洞上报者）的记录缺口标注 ［ 存疑脚注：此处事实待多源交叉验证 ］
- id=550 [resolved] - 要点：**Hiroki Sato**（hrs@）是 FreeBSD 社区最受尊敬的核心成员之一，担任 Documentation Engineering T
- id=551 [resolved] - 辨析：**关键事实修正**：① 原 ch85 草稿称 "13.1 献词给 Hiroki Sato" 是错误信息——13.1 实际献词给 Bill Jolit
- id=552 [resolved] - 要点：FreeBSD 14.x 上的 AI/ML 工作负载支持仍处于早期阶段：① GPU 计算：NVIDIA CUDA 不正式支持 FreeBSD，但 NV
- id=553 [resolved] - 辨析：**早期 SA 的考据盲点**：freebsd.org/security/advisories/ 页面仅列出从 FreeBSD-SA-08:05.op
- id=554 [resolved] - 辨析：**统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src com

## ③ 一手史料（original_sources.kaoju_records，0 条）

（无）
