---
chapter: 第 25 章
id: CH25
volume: 第01卷-unix的起源
---

# 第 25 章 Plan 9 的起源与技术演化

## 要点

Plan 9 是 Bell Labs 在 UNIX 之后对分布式操作系统的激进实验——“一切皆文件”原则被推向极致，9P 协议将本地与远程资源统一为文件系统命名空间。Plan 9 从未成为商业产品，但其设计理念深刻影响了后来的系统设计：UTF-8 编码（Rob Pike 与 Ken Thompson 在 Plan 9 中设计）、/proc 文件系统、r fork 语义等。本章考察 Plan 9 的起源（1980 年代末“后 UNIX”研究）、技术演化（从 Plan 9 到 Inferno 到 9front），以及它对 BSD 的间接影响——Plan 9 的“失败”不是技术失败，而是市场生态的缺席。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1540] 卷“第01卷-unix的起源”第 25 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:bsdnow_podcast:outline_mappings:om_12452] BSD Now 第 424 期，匹配 CH25 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11449] BSD Now 第 535 期，匹配 CH25 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12055] BSD Now 第 463 期，匹配 CH25 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12165] BSD Now 第 448 期，匹配 CH25 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12862] BSD Now 第 275 期，匹配 CH25 章，关联度 1.0
- Pike R, Presotto D, Thompson K, Trickey H. Plan 9 from Bell Labs[C]//UKUUG Proceedings of the Summer 1990 Conference. 1990（当事人一手文献）
- 9fans 邮件列表档案（9fans.net archives）〔L1 邮件〕
## 史观

总纲第 4 条——分离聚合是永恒规律，Plan 9 作为 UNIX 研究传统的“终结”是其理念通过 UTF-8、/proc 等在后续系统中延续的开端，分合循环是历史的根本结构；总纲第 5 条——没有必然性，只有偶然性，Plan 9 未能取代 UNIX 不是技术不足，而是 1990 年代 Linux 的偶然崛起占据了“开源 UNIX 替代品”的生态位；总纲第 6 条——和解优于斗争，Plan 9 与 UNIX 不是竞争关系而是技术哲学对话。

## 辨析

- Plan 9 的“失败”定性需审慎：其市场缺席与 1990 年代 UNIX 商业版图固化、AT&T 拆分后贝尔实验室研究环境收缩等结构因素交织，不宜简化为单一技术或商业原因，须与第 26 章哲学审视对照
- UTF-8 的发明归属须精确到 Rob Pike 与 Ken Thompson 二人（1988 年 Xerox 时期初稿、1992 年 Plan 9 落地），单记 Thompson 与单记 Pike 均失准
- Plan 9 对 BSD 的影响路径（/proc 文件系统、rfork 语义、9P→v9fs）为间接传播，直接代码双向流动有限，因果强度须逐条核验，避免夸大

## 文献

- Pike R, Presotto D, Thompson K, Trickey H, Winterbottom P. The Use of Name Spaces in Plan 9[J]. ACM SIGOPS Operating Systems Review, 1992.
- Pike R, Presotto D, Thompson K, Trickey H. Plan 9 from Bell Labs[C]//UKUUG Proceedings of the Summer 1990 Conference. 1990.
- 9fans 邮件列表档案（9fans.net archives，1995 年起）〔L1 邮件〕
- [DB:references_fulltext:chapter_matches:chmatch_1540]
- [DB:bsdnow_podcast] BSD Now 第 275/424/448/463/535 期（outline_mappings om_12862/om_12452/om_12165/om_12055/om_11449）

