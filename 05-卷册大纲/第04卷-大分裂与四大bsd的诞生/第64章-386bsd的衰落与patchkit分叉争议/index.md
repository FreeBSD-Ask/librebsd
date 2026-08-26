---
chapter: 第 64 章
id: CH64
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 64 章 386bsd的衰落与patchkit分叉争议

## 要点

- 综合前述七层辩证，386BSD 停滞与分叉争议不能简化为 “个人英雄主义 vs 社区协作” 或 “个人过失 vs 系统困境” 的二元结构——双方叙事都存在选择性记忆与形式主义化重构。批评方的 “单点故障” “个人维护导致停滞” “阻碍 BSD 在 x86 上的发展” 三主线在事实层面成立（commit 量、版本发布时间、市场窗口可量化考据），但 “个人英雄主义” 标签遮蔽了 Jolitz 夫妇面临
- 386BSD patchkit fork 争议是“革命与改革”方法论分歧在 BSD 内部的具体呈现——Linux 靠革命，BSD 靠改革，而 386BSD 的停滞与 patchkit fork 恰恰是 BSD 改革路径内部的张力爆发。Jolitz 夫妇坚持“高质量门槛 + 单一维护者决策”的工程哲学，是 BSD 改革传统的延续——CSRG 在 4.xBSD 系列中亦是 small team 主导、

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3680] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3688] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3691] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3709] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3785] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3793] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3795] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:references_fulltext:chapter_matches:chmatch_3889] 卷“第04卷-大分裂与四大bsd的诞生”第 64 章，匹配置信度 folder，原因：folder 第63章
- [DB:bsdnow_podcast:outline_mappings:om_10563] BSD Now 第 651 期，匹配 CH64 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11010] BSD Now 第 586 期，匹配 CH64 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11401] BSD Now 第 541 期，匹配 CH64 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11619] BSD Now 第 514 期，匹配 CH64 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11661] BSD Now 第 507 期，匹配 CH64 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12202] BSD Now 第 446 期，匹配 CH64 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12521] BSD Now 第 418 期，匹配 CH64 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 考据过程留痕——【查证来源】合图层不引入新的事实考据，仅综合前述七层辩证，新事实考据分散于 25.1-25.14 各节；本节所引史料均为前述辩证已核验的一手史料；【交叉验证方法】合图层的事实判断（如 “386BSD 1.0 仍基于 0.1 而非 4.4BSD-Lite” “FreeBSD 在 USL 诉讼期间以约 2-6 个月周期持续发布” “Linux 1.0 发布于 1994 年 3 月 14
- 考据过程留痕——【查证来源】项目史观总纲第 21 条原文“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”经 据原文第 25 章 第 25 行 Read 一手核验；Eric Raymond"A Brief History of Hackerdom"第 7 节"release every week"对照经 catb.org 一手核验；L

## 文献

- 综合前述七层辩证所引文献；本节不引入新文献 ［A］
- 综合 25.1-25.15 各节文献；项目史观总纲第 21 条原文；Raymond, E. S. "A Brief History of Hackerdom"in Open Sources (O'Reilly 1999)；Linux 1.0 Release Announcement (14 March 1994)；FreeBSD 1.0 RELEASE Announcement (1 Nov 1993)；NetBSD 0.8 Release Notes (April 1993) ［A］### 史观映射> Jolitz 停下了——没有宏大的理由，只是一个人在某个时刻选择了不再继续。这个 “不再继续” 是偶然的：如果他的补丁来得及发布，如果社区的需求没有超过他一个人能承载的限度——FreeBSD 也许永远不会诞生。386BSD 的停滞不是悲剧，而是一个有限的人做了有限的事之后停下来。而托瓦兹那句 “如果 386BSD 当时可用，Linux 可能永远不会发生”，恰恰说明了历史的转向往往系于一个人是否在某个时刻停下了手。本章新增 25.11 节专述 USL v. BSDi 和解协议的保密与公开：显而易见却罕有人知道的是，1994 年和解的 “BSD 胜诉” 叙事实则建立在一纸保密协议之上，直到 2004 年 Pamela Jones 援引《加州公共记录法》解封该协议，史学叙事才得以从简化走向复杂——真历史（项目史观总纲第 2 条）的重建始终受法律密封的约束---## 第 25.17 不同时期人员的采访录（详见 [采访录.md](采访录.md)）> 第 25 章采访录子节，覆盖 1991-1993 年 386BSD 兴衰时期的当事人自述、专访与邮件列表存档，含 Lynne Jolitz Salon 2000 专访、Rachel Chalmers Salon 2000 报道、林纳斯·托瓦兹（Linus Torvalds）Meta 杂志 1993 末采访三则，每则采访按 5 字段深化，考据过程另见 原材料/研究/考据记录/ 下对应文件。## 第 25.18 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）
