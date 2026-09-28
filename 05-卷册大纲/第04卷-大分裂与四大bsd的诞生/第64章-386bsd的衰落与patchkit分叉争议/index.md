---
chapter: 第 64 章
id: CH64
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 64 章 386BSD 的衰落与 patchkit 分叉争议

## 要点

- 综合前述七层辩证，386BSD 停滞与分叉争议不能简化为“个人英雄主义 vs 社区协作”或“个人过失 vs 系统困境”的二元结构——双方叙事都存在选择性记忆与形式主义化重构。批评方的“单点故障”“个人维护导致停滞”“阻碍 BSD 在 x86 上的发展”三主线在事实层面成立（commit 量、版本发布时间、市场窗口可量化考据），但“个人英雄主义”标签遮蔽了 Jolitz 夫妇面临的个人精力、商业支持、法律风险三重困境。
- 386BSD patchkit fork 争议是“革命与改革”方法论分歧在 BSD 内部的具体呈现——Linux 靠革命，BSD 靠改革，而 386BSD 的停滞与 patchkit fork 恰恰是 BSD 改革路径内部的张力爆发。Jolitz 夫妇坚持“高质量门槛 + 单一维护者决策”的工程哲学，是 BSD 改革传统的延续——CSRG 在 4.xBSD 系列中亦是 small team 主导、长周期发布、质量优先。

## 史料

- 注：以下 BSD Now 条目已按 bsd-now.duckdb 人工著录，期号、标题与发布日期以该库 episodes 表为准（原自动注入行所标“第 651 期”等数字为库内 episode_id 而非实际期号）。
- [DB:bsd-now.duckdb:outline_mappings:om_10563] BSD Now 第 259 期《Long Live Unix》（2018-08-16），匹配 CH64 章，关联度 1.0
- [DB:bsd-now.duckdb:outline_mappings:om_11010] BSD Now 第 231 期《Unix Architecture Evolution》（2018-02-01），匹配 CH64 章，关联度 1.0
- [DB:bsd-now.duckdb:outline_mappings:om_11401] BSD Now 第 170 期《Sandboxing Cohabitation》（2016-11-30），匹配 CH64 章，关联度 1.0
- [DB:bsd-now.duckdb:outline_mappings:om_11619] BSD Now 第 163 期《Return of the Cantrill》（2016-10-12），匹配 CH64 章，关联度 1.0
- [DB:bsd-now.duckdb:outline_mappings:om_11661] BSD Now 第 136 期《This is GNN》（2016-04-06），匹配 CH64 章，关联度 1.0
- [DB:bsd-now.duckdb:outline_mappings:om_12202] BSD Now 第 91 期《Vox Populi》（2015-05-27），匹配 CH64 章，关联度 1.0
- [DB:bsd-now.duckdb:outline_mappings:om_12521] BSD Now 第 26 期《Port Authority》（2014-02-26），匹配 CH64 章，关联度 1.0

## 史观

- 偶然性（总纲第 5 条）：Jolitz 停滞、USL 诉讼、patchkit fork 都是偶然事件，没有必然性，但此偶然叠加使 BSD 错失窗口成为既成事实（据 64.16.1、64.15.8）。
- 本体论上各方平等（总纲第 8 条）：Jolitz 夫妇与 patchkit 群体在本体论上地位相等，无谁更“正统”，差异仅是一刻状态的不同；386BSD 不是“失败的先驱”，而是 BSD 在 386 平台的特定一刻状态（据 64.16.2、64.15.8）。
- 解释学循环与权力-知识共谋（总纲第 19 条）：双方叙事都基于前理解，分歧不可避免，权力与知识在历史书写中共谋——什么被记录、什么被遗忘本身就是权力行使；历史是形式主义化的非存在，本章所写皆是当下主体的重构（据 64.16.3）。
- 法律与道德是利益分配（总纲第 13 条）：“忽视”“窃取”“被迫 fork”等道德叙事，实质是 AT&T、加州大学、BSDi、Jolitz 夫妇、patchkit 群体五方主体对 BSD 代码归属与维护权利益分配冲突的形式主义化呈现（据 64.16.4）。
- 革命与改革是历史方法论的分歧（总纲第 21 条）：Linux 靠革命，BSD 靠改革，386BSD 的停滞与 patchkit fork 恰是 BSD 改革路径内部的张力爆发；改革的困难远高于革命——破山中贼易，破心中贼难（据 64.16.5）。
- 和解优于斗争：和解在工程层面已通过代码继承实际发生——386BSD 0.1 作为 FreeBSD 与 NetBSD 共同基线在早期 import commit 中有显式记录，叙事层面的不可调和性不阻碍代码层面的延续（据 64.15.8）。
- 理论必须自反：本章承认自身的形式主义性质，以自反姿态打开裂缝（据 64.16.3、64.16.5）。

## 辨析

- 考据过程留痕——【查证来源】合图层不引入新的事实考据，仅综合前述七层辩证，新事实考据分散于 64.15 各层辩证；本节所引史料均为前述辩证已核验的一手史料；【交叉验证方法】合图层的事实判断（如“386BSD 1.0 仍基于 0.1 而非 4.4BSD-Lite”“FreeBSD 在 USL 诉讼期间以约 2-6 个月周期持续发布”“Linux 1.0 发布于 1994 年 3 月 14 日”）均经前述辩证交叉验证，本节不重复考据过程，仅综合事实判断。
- 考据过程留痕——【查证来源】项目史观总纲第 21 条原文“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”经一手核验；Eric Raymond《A Brief History of Hackerdom》第 7 节“release every week”对照经 catb.org 一手核验；Linux 1.0 发布日期（1994.3.14）经 Linux Kernel Archive 一手核验。

## 文献

- 综合前述七层辩证所引文献；本节不引入新文献 ［A］
- 综合 64.15、64.16 各层辩证文献；项目史观总纲第 21 条原文；Raymond, E. S.《A Brief History of Hackerdom》in Open Sources (O'Reilly 1999)；Linux 1.0 Release Announcement (14 March 1994)；FreeBSD 1.0 RELEASE Announcement (1 Nov 1993)；NetBSD 0.8 Release Notes (April 1993) ［A］

## 史观映射

> Jolitz 停下了——没有宏大的理由，只是一个人在某个时刻选择了不再继续。这个“不再继续”是偶然的：如果他的补丁来得及发布，如果社区的需求没有超过他一个人能承载的限度——FreeBSD 也许永远不会诞生。386BSD 的停滞不是悲剧，而是一个有限的人做了有限的事之后停下来。而托瓦兹那句“如果 386BSD 当时可用，Linux 可能永远不会发生”，恰恰说明了历史的转向往往系于一个人是否在某个时刻停下了手。USL v. BSDi 和解协议的保密与公开亦为本章重要考据点：显而易见却罕有人知道的是，1994 年和解的“BSD 胜诉”叙事实则建立在一纸保密协议之上，直到 2004 年 Pamela Jones 援引《加州公共记录法》解封该协议，史学叙事才得以从简化走向复杂——真历史（项目史观）的重建始终受法律密封的约束

## 不同时期人员的采访录

> 采访录子节覆盖 1991-1993 年 386BSD 兴衰时期的当事人自述、专访与邮件列表存档，含 Lynne Jolitz Salon 2000 专访、Rachel Chalmers Salon 2000 报道、林纳斯·托瓦兹（Linus Torvalds）Meta 杂志 1993 末采访三则，每则采访按 5 字段深化，考据过程另见 **原材料/研究/考据记录/** 下对应文件。详见 [采访录.md](采访录.md)。

