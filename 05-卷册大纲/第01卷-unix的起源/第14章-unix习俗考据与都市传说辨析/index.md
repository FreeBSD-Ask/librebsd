---
chapter: 第 14 章
id: CH14
volume: 第01卷-unix的起源
---

# 第 14 章 unix习俗考据与都市传说辨析

## 要点

- V6 UNIX 内核中著名的注释 `/* You are not expected to understand this */` 位于进程上下文切换相关代码段（约第 2240-2243 行处，注释本身在第 2238 行），涉及交换标志 SSWAP 与进程切换的晦涩代码；该注释因作者对代码晦涩度的自我调侃而成为 UNIX 史上最著名的代码注释之一，是 UNIX 早期代码文化与“内核代码晦涩难懂”集体

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3599] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3600] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3602] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3605] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3607] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3636] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3652] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3653] 卷“第01卷-unix的起源”第 14 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1532] 卷“第01卷-unix的起源”第 14 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:references_fulltext:chapter_matches:chmatch_1172] 卷“第01卷-unix的起源”第 14 章，匹配置信度 0.6，原因：无匹配

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 该注释的具体作者存在争议——通常被归为 Dennis Ritchie 或 Ken Thompson，但无一手史料确证作者，二者本人均未在公开场合明确认领；注释的确切语义（SSWAP 交换标志与 u.u_eeav 错误处理的上下文）需结合 V6 内核进程调度源码考据；按 0 信任原则，将注释作者归为“Bell Labs 内核开发者群体”而非单一人物更稳妥

## 文献

- Salus P H. A Quarter Century of UNIX [M]. Reading: Addison-Wesley, 1994；UNIX V6 Source Code (TUHS Archive research/Dennis_v6)；McKusick M K, Bostic K, Karels M J, Quarterman J S. The Design and Implementation of the 4.4BSD Operating System [M]. Reading: Addison-Wesley, 1996 ［B］> （2026-08-05 清理：原文件末尾的 [^oi7-fn]~[^oi10-fn] 四个孤立脚注系 12.11 小节内容误留于此，正文无引用标记；已移回重建后的 12.11 小节，见 `12.11-贝尔实验室的学院派气质与冷战自由主义…md` 12.11.1-12.11.4 辨析字段。）
