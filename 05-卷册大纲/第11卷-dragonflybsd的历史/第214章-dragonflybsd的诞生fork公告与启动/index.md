---
chapter: 第 214 章
id: CH214
volume: 第11卷-dragonflybsd的历史
---

# 第 214 章 dragonflybsd的诞生fork公告与启动

## 要点

- DragonFly BSD 仓库共 656207 次提交（2003-06-17 至 2026-08-18），160 位贡献者，贡献者数远少于三大 BSD，反映 Dillon 个人主导模式

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4030] 卷“第11卷-dragonflybsd的历史”第 214 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4051] 卷“第11卷-dragonflybsd的历史”第 214 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4052] 卷“第11卷-dragonflybsd的历史”第 214 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:dragonfly.duckdb] DragonFly BSD 仓库共 656207 次提交（2003-06-17 至 2026-08-18），160 位贡献者，贡献者数远少于三大 BSD，反映 Dillon 个人主导模式

## 史观

- 偶然性优先：DragonFly BSD 的诞生源于 Dillon 与 FreeBSD 5.x 技术路线的偶然分歧

## 辨析

- 不同引述版本的措辞差异主要源于邮件正文换行符处理（CRLF/LF 差异）与邮件客户端显示差异，原始邮件头 Message-ID 与 Date 字段须以 lists.freebsd.org 归档源为准
- archive.org 快照保留多个时间点（2004、2005、2007、2008），各快照内容基本一致但 HTML 格式差异可能影响引述文字的换行与标点——正式撰写时须以最早快照（2004 年）为准
- 【史观应用的界限】项目史观总纲第 6、8 条是史观审视框架，非史实判定标准——“和解优于斗争”不意味着 fork 是“错误”，“本体论上各方平等”不意味着 SMPng 与 LWKT 路线“同样成功”（dragonfly.duckdb 显示 DragonFly 2024 年 commit 量仅 277 条，远低于 FreeBSD 主线，市场选择的结果差异是经验事实而非本体论判断）；【“短暂的接纳”的考据】2

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 dragonfly.duckdb

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2038 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2038`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔But have you tried DragonflyBSD? The new, revised BSD?〕讲者口述：DragonFly BSD 由 Matthew Dillon 从 FreeBSD 分叉而来；讲者称其 1994 至 2003 年间为 FreeBSD 开发者，2003 年 6 月开始做 DragonFly，并于 2003 年 7 月 16 日在邮件列表宣布。（YouTube EPPxeiGB3q17M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2039 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2039`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔But have you tried DragonflyBSD? The new, revised BSD?〕讲者口述：Dillon 分叉 DragonFly 的动机，是相信 FreeBSD 5 所采用的线程方法会带来性能与维护上的问题。（YouTube EPPxeiGB3q17M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2040 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2040`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔But have you tried DragonflyBSD? The new, revised BSD?〕讲者口述：DragonFly 在轻量内核线程与内核消息传递上都采用了与既有实现显著不同的做法，并配有名为 Hammer 的文件系统。（YouTube EPPxeiGB3q17M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2041 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2041`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔But have you tried DragonflyBSD? The new, revised BSD?〕讲者口述：DragonFly 与 FreeBSD 两个项目仍然保持合作，互相交换错误修正、驱动更新与其他改进。（YouTube EPPxeiGB3q17M，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2577 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2577`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Matt Dillon BayLISA 2005年12月讲座〕讲者口述：DragonFly 在多处理器方面采取了相对其他 BSD 更激进的路线：发展天然 CPU 本地化的算法，以尽可能避免加锁。（YouTube EPEfNZ4jMQic4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2578 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2578`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Matt Dillon BayLISA 2005年12月讲座〕讲者口述：DragonFly 的网络协议栈已线程化：每个 CPU 上都有 TCP 线程，按地址与端口分派，特定 TCP 线程总是拿到特定连接的包，处理 TCB 时完全无需加锁。（YouTube EPEfNZ4jMQic4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2579 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2579`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Matt Dillon BayLISA 2005年12月讲座〕讲者口述：DragonFly 用作测量工具的 KTR 内核跟踪日志最初由 BSDI 开发，用法是内核例程调用日志例程写入关键字参数，写入极快且 MP 安全。（YouTube EPEfNZ4jMQic4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2580 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2580`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Matt Dillon BayLISA 2005年12月讲座〕讲者口述：DragonFly 的长期目标被讲者表述为透明集群化（transparent clustering）。（YouTube EPEfNZ4jMQic4，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
