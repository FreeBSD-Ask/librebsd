---
chapter: 第 18 章
id: CH18
volume: 第01卷-unix的起源
---

# 第 18 章 小型机的诞生与dec-pdp谱系

## 要点

DEC PDP系列小型机（PDP-1至PDP-11）的诞生标志着计算从大型机向小型化的关键转折：PDP-7是UNIX的最初开发平台，PDP-11则是UNIX扩散与C语言移植的决定性硬件载体。DEC的模块化设计理念——以UNIBUS总线与PDP-11的MMU为代表——在技术层面为多用户分时系统提供了物质基础，但其"为UNIX而生"的叙事本身就是一种后见之明的形式主义重构。PDP-11的16位寻址空间限制（64KB直接寻址）在UNIX发展初期既构成了约束也激发了创新——如分离指令与数据空间（I/D space）的引入。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3619] 卷“第01卷-unix的起源”第 18 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1536] 卷“第01卷-unix的起源”第 18 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题
- [DB:bsdnow_podcast:outline_mappings:om_10434] BSD Now 第 675 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10449] BSD Now 第 671 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10476] BSD Now 第 665 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10496] BSD Now 第 663 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10508] BSD Now 第 661 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10519] BSD Now 第 659 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10531] BSD Now 第 655 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10573] BSD Now 第 648 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10597] BSD Now 第 644 期，匹配 CH18 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10614] BSD Now 第 641 期，匹配 CH18 章，关联度 1.0

## 史观

PDP-11 作为 UNIX 母机的地位存在叙事风险——将 PDP-11 与 UNIX 的共生关系本质化为"天作之合"可能掩盖了历史的偶然性。UNIX 最初是为 PDP-7 编写的，PDP-11 的引入是后来的升级；UNIX 在 PDP-11 上的成功部分源于 PDP-11 的内存管理单元（MMU）恰好支持 UNIX 的多用户需求，但这不是"设计"而是"巧合"。DEC 在 1990 年代被 Compaq 收购、最终消亡，其硬件遗产主要通过 PDP-11 模拟器（如 SIMH）和 UNIX 的持续发展得以保存。

## 辨析

PDP-11与UNIX的共生关系常被简化为"天作之合"，但UNIX最初是为PDP-7编写的，PDP-11是后来的升级：PDP-11的MMU恰好支持UNIX的多用户需求，但这种"适配"是工程上的事后选择而非设计上的先见之明。DEC在1990年代被Compaq收购后的消亡与其未能及时转向RISC架构有关，将DEC的衰落简单归因于"小型机被微机取代"的线性叙事遮蔽了PDP谱系内部的技术演进逻辑（如VAX与Alpha的尝试）。PDP-11的硬件细节（如UNIBUS的DMA机制、内存映射I/O）对UNIX内核设计的具体影响程度，需要更精确的源代码考古证据。

## 文献

（待补：Bell C G, Mudge J C, McNamara J E. Computer Engineering: A DEC View of Hardware Systems Design[M]. Digital Press, 1978；Ceruzzi P E. A History of Modern Computing[M]. 2nd ed. MIT Press, 2003；[DB:references_fulltext:chapter_matches:chmatch_3619]；[DB:references_fulltext:chapter_matches:chmatch_1536]）

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第18章-小型机的诞生与dec-pdp谱系 -->

## 要点（播客口述史提取）
- This week on BSD Now, we have the Project Rite in 18.12 release.
- And so this version is based off the 18.12 stable branch of TrueOS, so 3BSD13 current,
- Then they have also the 18.12 release has been a long time in development and I wish
- Oh, time for news roundup this week. We have OpenSense release 18.7.10 being out.
- uh major new releases come every two years or so 12 was pushed out in december 2018 12.2 in october
- submitting proposals for the open source summits in 2018. Yeah, so this is on our long term
- Up next is our news roundup for this week, starting with Ghost for Unix released on the 18th birthday of that software.

## 史料（播客提及）
- [BSD Now EP119 @ 4127.4599609375] Linux kernel 3.18, which I think that includes. That's definitely Broadwell, but might even include
- [BSD Now EP282 @ 2957.7] January 25th at 1815 to 2100 and it's back at the wheel systems offices. I think last
- [BSD Now EP282 @ 399.84] driving amazing. And they actually have 18.12 update one available already.

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP119 @ 4127.4599609375] Linux kernel 3.18, which I think that includes. That's definitely Broadwell, but might even include
- [BSD Now EP282 @ 2957.7] January 25th at 1815 to 2100 and it's back at the wheel systems offices. I think last
- [BSD Now EP282 @ 399.84] driving amazing. And they actually have 18.12 update one available already.

## 辨析（播客争议与存疑点）
- （该章节匹配播客中暂未提取到相关争议点）

## 文献（播客参考条目）
- [BSD Now EP192] Pennington J. BSD Now: 192: SSHv1 Be Gone[EB/OL]. (2017-05-03)[2026-08-15]. https://www.bsdnow.tv/192.
- [BSD Now EP230] Pennington J. BSD Now: 230: Your questions, Part III[EB/OL]. (2018-01-24)[2026-08-15]. https://www.bsdnow.tv/230.
- [BSD Now EP119] Pennington J. BSD Now: 119: There be Dragons, BSD Dragons anyway[EB/OL]. (2015-12-09)[2026-08-15]. https://www.bsdnow.tv/119.
- [BSD Now EP229] Pennington J. BSD Now: 229: The Meltdown of Spectre[EB/OL]. (2018-01-17)[2026-08-15]. https://www.bsdnow.tv/229.
- [BSD Now EP308] Pennington J. BSD Now: 308: Mumbling with OpenBSD[EB/OL]. (2019-07-25)[2026-08-15]. https://www.bsdnow.tv/308.
- [BSD Now EP173] Pennington J. BSD Now: 173: Carry on my Wayland son[EB/OL]. (2016-12-21)[2026-08-15]. https://www.bsdnow.tv/173.
- [BSD Now EP282] Pennington J. BSD Now: 282: Open the Rsync[EB/OL]. (2019-01-24)[2026-08-15]. https://www.bsdnow.tv/282.
- [BSD Now EP312] Pennington J. BSD Now: 312: Why Package Managers[EB/OL]. (2019-08-22)[2026-08-15]. https://www.bsdnow.tv/312.
- [BSD Now EP66] Pennington J. BSD Now: 66: Conference Connoisseur[EB/OL]. (2014-12-03)[2026-08-15]. https://www.bsdnow.tv/66.
- [BSD Now EP396] Pennington J. BSD Now: 396: License to thrill[EB/OL]. (2021-04-01)[2026-08-15]. https://www.bsdnow.tv/396.
- [BSD Now EP162] Pennington J. BSD Now: 162: The Foundation of NetBSD[EB/OL]. (2016-10-05)[2026-08-15]. https://www.bsdnow.tv/162.
- [BSD Now EP61] Pennington J. BSD Now: 61: IPSECond Wind[EB/OL]. (2014-10-29)[2026-08-15]. https://www.bsdnow.tv/61.
- [BSD Now EP159] Pennington J. BSD Now: 159: Net Scaling Privacy (Flix Style)[EB/OL]. (2016-09-14)[2026-08-15]. https://www.bsdnow.tv/159.
- [BSD Now EP97] Pennington J. BSD Now: 97: Big Network, SmallWall[EB/OL]. (2015-07-08)[2026-08-15]. https://www.bsdnow.tv/97.
- [BSD Now EP209] Pennington J. BSD Now: 209: Signals: gotta catch ‘em all[EB/OL]. (2017-08-30)[2026-08-15]. https://www.bsdnow.tv/209.
- [BSD Now EP200] Pennington J. BSD Now: 200: Getting Scrubbed to Death[EB/OL]. (2017-06-28)[2026-08-15]. https://www.bsdnow.tv/200.
- [BSD Now EP351] Pennington J. BSD Now: 351: Heaven: OpenBSD 6.7[EB/OL]. (2020-05-21)[2026-08-15]. https://www.bsdnow.tv/351.
- [BSD Now EP348] Pennington J. BSD Now: 348: BSD Community Collections[EB/OL]. (2020-04-30)[2026-08-15]. https://www.bsdnow.tv/348.
- [BSD Now EP71] Pennington J. BSD Now: 71: System Disaster[EB/OL]. (2015-01-07)[2026-08-15]. https://www.bsdnow.tv/71.
- [BSD Now EP382] Pennington J. BSD Now: 382: BSDNow Q&A 2020[EB/OL]. (2020-12-24)[2026-08-15]. https://www.bsdnow.tv/382.

<!-- /PODCAST_MINE -->