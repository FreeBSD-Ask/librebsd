---
chapter: 第 285 章
id: CH285
volume: 第15卷-许可证哲学与法律分析
---

# 第 285 章 bsdvsgpl哲学辩论与同期os比较

## 要点

- 许可哲学光谱：“义务自由（GPL）←→ 信任自由（BSD/宽松）←→ 闭源保护（Windows）”；BSD vs GPL 辩论的本质是“自由如何保障”的分歧，BSD 以信任、GPL 以约束，二者共同定义开源运动的哲学边界。
- Committer’s Big List of Rules 的沉默反映分层设计——治理程序处理“谁有权提交”，许可证哲学通过社区讨论与工程实践处理“提交什么”。BSD 化工程未通过修订 committer 规则实现，而是通过构建 BSD 许可证替代品逐步完成，证明规则的程序中立未阻碍许可证纯化，反而为工程替代争取了时间——若规则在早期强制禁绝 GPL 代码，FreeBSD 将因缺乏可用编译器而无法
- Committer’s Big List of Rules 争议映射出革命与改革的方法论分歧。革命路径主张直接修订规则——禁止 GPL 代码进入 base 系统、强制许可证审查、将 BSD 化写入治理章程；改革路径则在不修订规则的前提下，通过工程替代（Clang、LibreSSL、mandoc）逐步实现许可证纯化。FreeBSD 选择了改革路径，其困难远高于革命——须先构建功能对等的 BSD 替代
- 中文技术圈普遍以“病毒/传染”描述 GPL copyleft 机制，此隐喻**在法律意义上具有系统性误导**。词源可考：1990 年即出现 "General Public Virus"（GPV）贬称；2001 年 Microsoft 高管 Craig Mundie 称 GPL "viral aspect"，Steve Ballmer 更称 GPL 代码是 "a cancer that attach
- GPL 义务的触发条件是**分发（distribute，GPLv2）/传播（convey，GPLv3）**，而非“使用”或“修改”。中文圈“只要用了 GPL 代码就必须开源”的表述是核心误读之一。FSF GPL FAQ 明确：①**内部使用修改版不触发开源义务**——“GPL 不要求你发布修改版……你有自由修改并自用，而不必发布。这个规则也适用于机构（包括公司）”；②**运行修改版提供服务（Saa

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10483] BSD Now 第 665 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10547] BSD Now 第 654 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10584] BSD Now 第 646 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10645] BSD Now 第 637 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10778] BSD Now 第 617 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11152] BSD Now 第 571 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11215] BSD Now 第 563 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11366] BSD Now 第 546 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11444] BSD Now 第 536 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11544] BSD Now 第 526 期，匹配 CH285 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 辩论无终局——两种自由观各服务不同目标，BSD 的务实人文在光谱中独特定位。
- 【查证来源】FreeBSD Committer’s Guide 第 20 章经 docs.freebsd.org/en/articles/committers-guide/#rules WebFetch 一手核验目录条目存在；FreeBSD Core Bylaws 2000.8.28 版经 freebsd.org/internal/bylaws/ WebFetch 一手核验，规定 active c
- 【查证来源】项目史观总纲第 21 条原文经 据原文第 25 章 第 25 行 Read 一手核验：“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”；BSD 化工程时间线经 135.8 节史料（OpenBSD LibreSSL 公告、FreeBSD LLVM 迁移文档、openbsd.db L3.6.1 查询报告）交叉核验；FreeB
- 【查证来源】GPLv2 §5 原文：“如果可识别的作品部分不是派生自本程序，且可合理视为独立的分离作品，则本许可证及其条款不适用于那些部分”（WebFetch gnu.org/licenses/old-licenses/gpl-2.0.txt 一手核验）；GPLv3 §5 聚合定义"aggregate"（WebFetch gnu.org/licenses/gpl-3.0.txt 一手核验）；Sta
- 【查证来源】FSF GPL FAQ 中文版（gnu.org/licenses/old-licenses/gpl-2.0-faq.zh-cn.html）WebFetch 一手核验上述问答原文；GPLv3 §0 “传播”（to convey）定义（gnu.org/licenses/gpl-3.0.txt）一手核验  【交叉验证方法】（1）FSF FAQ 内部一致性核验：修改版自用问答与 SaaS 问答

## 文献

- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］------## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.2 劣币驱逐良币（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- Committer’s Big List of Rules（docs.freebsd.org/en/articles/committers-guide/#rules）；FreeBSD Core Bylaws 2000.8.28 版（freebsd.org/internal/bylaws/）；BSD 化 commit log；Core Team 选举记录（freebsd.org/administration/）［A］
- 项目史观总纲第 21 条（据原文第 25 章 第 25 行）；BSD 化工程时间线（详见 135.8 节）；FreeBSD Core Bylaws 2000.8.28 版第 9 条（freebsd.org/internal/bylaws/）［A］
- GPLv2/GPLv3 全文（gnu.org）；FSF GPL FAQ（gnu.org/licenses/gpl-faq.html）；Copyleft 词条（Wikimedia）；中文自媒体《开源许可证教程》（ref 2377，kaoju_unreliable 系列，被考据对象——仅作“个人观点”元引用，其史实断言须独立核验）## 284.13.2 传染触发条件的法律边界——“分发/传播”而非“使用”
- FSF GPL FAQ 中文版；GPLv2/GPLv3 全文；AGPL 文本［A］## 284.13.3 传染性边界：演绎作品 vs 聚合（aggregation）
- GPLv2/GPLv3 全文；FSF GPL FAQ；最高法（2021）最高法知民终51号判决；HBuilder 案判决；康达律师事务所开源协议分析文 ［A］## 284.13.4 GPL 的法律性质：许可条件（conditions）而非单纯合同承诺（covenants）
- Jacobsen v. Katzer（535 F.3d 1373, Fed. Cir. 2008）；Creative Commons 声明；Artifex v. Hancom（2017）；济宁网络科技案；广州知识产权法院典型案例；最高法（2021）最高法知民终51号 ［A］## 284.13.5 违约救济误读：从“最坏不过被起诉”到司法实践的多元救济
- 南京中院（2021）苏01民初3229号；FSF v. Cisco 记录；广州知识产权法院典型案例；济宁网络科技案（2021）；中文自媒体《开源许可证教程》（ref 2377，kaoju_unreliable 系列，被考据对象——其“GPL 病毒”与“法官只会判停止使用”断言已按判例逐条纠正，结论以 FSF 官方 + 判例原文为准）［A］## 284.13.6 中文圈 GPL 理解偏差总表（法律意义维度）| # | 中文圈常见表述 | 法律事实 | 偏差类型 ||---|---|---|---|| 1 | “GPL 是病毒，用了就传染” | 传染仅限演绎作品；聚合/独立程序豁免（GPLv2 §5/GPLv3 §5） | 隐喻误导 || 2 | “只要用了 GPL 代码就必须开源” | 义务触发条件是分发/传播，内部使用与 SaaS（GPLv2）不触发 | 触发条件误读 || 3 | “违反 GPL 只是违约，不构成侵权” | Jacobsen（2008）：许可条件是 copyright conditions，违反=侵权；中国广州案：合同性质+授权终止=侵权 | 法律性质误读 || 4 | “最坏情况就是被起诉、判停止使用” | 南京案 300 万惩罚性赔偿；济宁/广州案授权终止；FSF v. Cisco 合规导向 | 救济范围误读 || 5 | “GPL 是免费午餐/自由软件=免费” | GPL 允许商业收费（GPL FAQ：可销售拷贝赚钱）；"free" 指自由非价格 | 概念混淆（freedom vs gratis） || 6 | “GPL 软件不能商用” | GPL 明确允许商业使用/销售（FSF 商业例外策略） | 商用限制误读 || 7 | “GPLv3 与 GPLv2 区别不大” | v3 增加专利授权、反 Tivoization、与 Apache 2.0 兼容；Linux 内核固守 v2-only | 版本差异误读 || 8 | “违反 GPL 后权利人不享有著作权” | 最高法 51 号案：违反 GPL 与著作权独立——开发者基于独创贡献仍享有著作权（演绎作品保护） | 权利关联误读 |> 本表为法律意义维度的系统性梳理，供正文写作与编辑引用；每条均有判例/FSF 官方来源支撑（详见 284.13.1-284.13.5 各小节辨析字段）。---## 附录：判例一手原件清单（2026-08-04 依据“判例与法律文件一手原件入库规则”采集）> 全部一手原件已下载存档于 `04-现代研究文献/03-文献下载/01-判决书案例/`，并在 references_fulltext.db 入库（ref id），大纲概述以 `<!-- NEWREF:ID -->` 标记引用。案件总清单：`03-原始史料库/06-考据记录/20260804_gpl_cases_inventory.md`。| 案件 | 一手原件 | ref id | 本地存档 ||------|---------|--------|---------|| Jacobsen v. Katzer（CAFC 2008） | CAFC 判决书 PDF（535 F.3d 1373） | 2417 | `Jacobsen_v_Katzer/` || Jacobsen 上诉卷宗 | appellant/appellee brief、CC amicus brief（445KB）、oral argument order 等 10 份 | 2418 | `Jacobsen_v_Katzer/` || Artifex v. Hancom（N.D. Cal. 2017） | MSJ 裁定（govinfo 官方 PDF 491KB）、MTD 裁定（CMU 370KB）、Hancom 动议（archive.org 181KB） | 2423/2424/2425 | `Artifex_v_Hancom/` || FSF v. Cisco（S.D.N.Y. 2008） | 起诉状公告+背景说明（FSF 官方页，案号 08-CV-10764） | 2426/2427 | `FSF_v_Cisco/` || SCO v. Novell（10th Cir. 2011） | 上诉判决 PDF（62KB，确认 Novell 拥有 Unix 版权） | 2428 | `SCO_v_Novell/` || USL v. BSDi / USL v. UC（1993-1994） | 1993-03-03 判决、920420/920724 起诉状、**McKusick 法庭声明**（930119.mckusick.decl，证人证词一手）、1986 UC-AT&T 许可协议 | 2422 | `USL_v_BSDi_USL_v_UC/` || 最高法（2021）知民终51号（OpenWRT/GPLv2） | 判决书全文（官网 HTML 98KB + wikisource 149KB）；一审案号（2018）苏05民初845号 | 2419 | `最高法2021知民终51号_OpenWRT/` || 南京中院（2021）苏01民初3229号（GPL 抗辩） | **判决书全文（2022-09-19，华宇元典 2026-08-04 获取）**+“密切通信”传染规则+300 万惩罚性赔偿；汉坤律所技术+法律分析 | 2468/2420/2421 | `南京苏01民初3229号_GPL抗辩/` || 广州知产法院（2019）粤73知民初207号（GPLv3 合同性质） | 判决书全文（45K 字，2021-09-29） | 2429 | `广州粤73知民初207号_GPLv3罗盒/` || 深圳中院（2019）粤03民初3928号（罗盒 v. 风灵/腾讯） | 判决书全文（43K 字，2021-04-30） | 2430 | `深圳粤03民初3928号_GPLv3罗盒/` || 北京高院（2018）京民终471号（HBuilder 案二审） | **二审判决书全文（2019-11-06，知产宝 2026-08-04 获取）**——三插件独立文件夹无 GPL 协议不受约束；聚合体认定；改判 50 万 | 2476 | `北京HBuilder案_GPL第一案/` |**说明**：

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第285章-bsdvsgpl哲学辩论与同期os比较 第 285 章 bsdvsgpl哲学辩论与同期os比较（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：13665 条 -->

### 要点（播客口述史提取）
- （该章节匹配播客中未提取到高置信度核心史实，需人工深挖）

### 史料（播客当事人陈述）
- （待人工提取）

### 史观（播客当事人观点与总纲映射）
- （该章节匹配播客中未提取到当事人观点性陈述）

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP12] Pennington J. BSD Now: 12: Collecting SSHells[EB/OL]. (2013-11-20)[2026-08-15]. https://www.bsdnow.tv/12.
- [BSD Now EP23] Pennington J. BSD Now: 23: Time Signatures[EB/OL]. (2014-02-05)[2026-08-15]. https://www.bsdnow.tv/23.
- [BSD Now EP31] Pennington J. BSD Now: 31: Edgy BSD Users[EB/OL]. (2014-04-01)[2026-08-15]. https://www.bsdnow.tv/31.
- [BSD Now EP40] Pennington J. BSD Now: 40: AirPorts & Packages[EB/OL]. (2014-06-04)[2026-08-15]. https://www.bsdnow.tv/40.
- [BSD Now EP60] Pennington J. BSD Now: 60: Don't Buy a Router[EB/OL]. (2014-10-22)[2026-08-15]. https://www.bsdnow.tv/60.
- [BSD Now EP106] Pennington J. BSD Now: 106: Multipath TCP[EB/OL]. (2015-09-09)[2026-08-15]. https://www.bsdnow.tv/106.
- [BSD Now EP114] Pennington J. BSD Now: 114: BSD-Schooling[EB/OL]. (2015-11-04)[2026-08-15]. https://www.bsdnow.tv/114.
- [BSD Now EP131] Pennington J. BSD Now: 131: BSD behind the chalkboard[EB/OL]. (2016-03-02)[2026-08-15]. https://www.bsdnow.tv/131.

<!-- /PODCAST_MINE -->
