---
chapter: 第 21 章
id: CH21
volume: 第01卷-unix的起源
---

# 第 21 章 当代大型机与 IBM Z LinuxONE

## 要点

IBM 大型机从 System/360（1964）到 IBM Z（2022）的六十年演化是计算机体系结构史上最持久的兼容性承诺。IBM Z 系列通过 LinuxONE 策略将 Linux 引入大型机生态，但 BSD 在大型机上的存在几乎为零——这构成了 BSD 硬件覆盖版图中最大的空白之一。本章考察大型机的技术演化路径、IBM Z 的当代架构，以及 BSD 在大型机平台缺席的技术史意义——大型机不是 BSD 的“失败市场”，而是 BSD 从未尝试进入的平行宇宙。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3606] 卷“第01卷-unix的起源”第 21 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_837] 卷“第01卷-unix的起源”第 21 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_880] 卷“第01卷-unix的起源”第 21 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_889] 卷“第01卷-unix的起源”第 21 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_891] 卷“第01卷-unix的起源”第 21 章，匹配置信度 0.6，原因：关键词重合 1 项
- [DB:references_fulltext:chapter_matches:chmatch_1133] 卷“第01卷-unix的起源”第 21 章，匹配置信度 0.6，原因：关键词重合 1 项

## 史观

总纲第 15 条——多方平等，大型机不是“落后”的平台，而是在特定约束下演化的技术路径；总纲第 3 条——偶然性优先，BSD 未能进入大型机生态不是技术原因而是历史偶然（IBM 选择 Linux 而非 BSD 作为开源战略合作伙伴）；总纲第 7 条——动手者创造历史，Linux on IBM Z 的开发者群体是大型机开源化的实际推动者。


补充映射：总纲第 4 条——分离聚合是永恒规律（大型机主线与 UNIX/BSD 支线的分合）；总纲第 11 条——商品是形式主义（大型机市场选择非自然选择）；总纲第 5 条——没有必然性，只有偶然性（Z 体系存续系商业偶然组合）
## 辨析

- 大型机生态与 BSD 的辨析要点——Linux on Z 的兴起并未取代大型机专有 OS（z/OS 仍为生产主体），FreeBSD/OpenBSD 在非 Z 平台的定位与大型机场景（高可靠批处理、金融事务处理）互补而非竞争；IBM Z 的 LinuxONE 发行版对 Linux 内核的长期支持周期（约 5-7 年）远超社区发行版，此差异须在比较史中显式标注

## 文献

- IBM Z 技术白皮书（IBM 官方文档库 ibm.com/support）〔L3 官方文档〕
- Linux on IBM Z 官方文档（ibm.com/docs/en/linux-on-z）〔L3 官方文档〕
- [DB:references_fulltext:chapter_matches] id=3606/837/880/889/891/1133