---
chapter: 第 219 章
id: CH219
volume: 第11卷-dragonflybsd的历史
---

# 第 219 章 dragonfly1x的10发布与lwkt子系统

## 要点

- DragonFly 早期邮件列表（users@、kernel@、submit@）与 commit log 是研究 fork 后开发过程的核心史料；考据需对照多个邮件列表档案与 CVS commit log 以核验特性引入时间
- LWKT 的设计文档与 DragonFly 源码（sys/kern/lwkt_thread.c、sys/sys/lwkt_token.h 等）是研究 LWKT 的核心史料；考据需对照设计文档、源码、邮件列表以核验实现细节
- DragonFly 1.2-1.8 的 Release Notes 与 CVS commit log 是研究此时期持续改进的核心史料；考据需对照 Release Notes、commit log、邮件列表以核验特性引入时间
- token 机制的 CVS commit log 与设计文档是研究 token 演进的核心史料；考据需对照 commit log、源码、邮件列表以核验实现细节
- 通过对 DragonFly 与 FreeBSD 4.x 源码的 diff 分析，考据 2003-2010 年间共享代码的减少轨迹，量化二者分化的进程

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4037] 卷“第11卷-dragonflybsd的历史”第 219 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4038] 卷“第11卷-dragonflybsd的历史”第 219 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4039] 卷“第11卷-dragonflybsd的历史”第 219 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 邮件列表档案的完整性需考据——部分早期档案可能丢失；commit log 中的早期 commit 需对照源码核验
- 设计文档与源码的差异需考据——部分文档可能滞后于实现；commit log 中的 LWKT 相关 commit 需对照源码核验；【数据缺口】netbsd.duckdb 数据分析规划中 L2.3.1.lwkt（LWKT 特性引入周期）与 L2.2.1.sys_sys_lwkt（sys/sys/lwkt 子系统 commit 演化）两项查询在卷章数据映射中已登记，但实际数据报告中未见对应查询结果——L2.3.
- Release Notes 的完整性需考据——部分细节可能滞后于实际代码；commit log 中的 HAMMER/SMP/网络栈/VFS 相关 commit 需对照源码核验
- 设计文档与源码的差异需考据——部分文档可能滞后于实现；commit log 中的 token 相关 commit 需对照源码核验
- diff 量化需考虑代码风格变化、自动格式化、注释增删等因素——纯粹行数 diff 可能高估或低估共享程度

## 文献

- DragonFly 邮件列表档案；DragonFly CVS 仓库；Dillon 设计文档 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2004-2004 年间：3,366 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly 设计文档；DragonFly 源码；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2006 年间：10,441 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly Release Notes；DragonFly CVS 仓库；DragonFly 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2005-2006 年间：6,068 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly CVS 仓库；DragonFly 源码；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2007-2008 年间：5,491 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- DragonFly git 仓库；FreeBSD 4.x 仓库镜像；BSD 源码 diff 相关研究 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2010 年间：305,499 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- DragonFly 邮件列表档案；Dillon 个人网站；DragonFly commit log ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2010 年间：22,761 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 6、8 条）；Dillon fork 公告（**lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html**）；DragonFly BSD history（**dragonflybsd.org/history/**）；dragonfly.duckdb dragonfly-src 仓库 commits/contributors/tags 表（1.x 时代客观数据、2003-2007 代码回移记录、2024 commit 量） ［A］FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>### 史观映射> DragonFly 1.x 时代是“分离聚合律”的又一次重演——Dillon 从 FreeBSD 4.x 分裂出去，带着 LWKT 的设计走上一条独立的道路；LWKT 与 token 机制是 Dillon 对 FreeBSD 5.x SMPng“过度复杂化”的回应——他选择重新设计一个“轻量级”的形式主义结构，而非沿用 FreeBSD 的细粒度锁；然而 DragonFly 社区规模的持续萎缩让“轻量级内核”的理想成为一种会者定离的修行——Dillon 在不被理解中坚持自己的架构哲学；50.7 **网络栈 MPSAFE 演进（每 CPU 线程模型、IPI 消息传递）**——每 CPU 线程模型的设计：每个 CPU 拥有独立的网络栈线程；IPI（Inter-Processor Interrupt）消息传递替代传统锁的工程实现；与 FreeBSD 细粒度锁路径的对比：消息传递 vs 细粒度锁的哲学分歧；MPSAFE 网络栈对 DragonFly 多核扩展的影响：线性扩展性；消息传递模型的局限性：延迟、复杂度、调试困难；Dillon 为何选择消息传递而非锁：对 FreeBSD 5.x SMPng 的反思 ｜ **子-子节**：50.7.1 每 CPU 线程模型的设计与网络栈并行化；50.7.2 IPI 消息传递替代锁的工程实现；50.7.3 与 FreeBSD 细粒度锁路径的对比及哲学分歧；50.7.4 MPSAFE 网络栈对多核扩展的影响及消息传递模型的局限性；50.8 **DragonFly SMP 性能 benchmark 与 FreeBSD 对比**——DragonFly 声称 SMP 性能优于 FreeBSD 的 benchmark（2.x-3.x 时代）；benchmark 方法的争议：测试场景选择、硬件配置、测量指标；独立第三方测试结果：部分支持、部分质疑 DragonFly 的声称；SMP 性能叙事对 DragonFly 社区信心的影响：技术优越感的建立；后续 benchmark 的反转：FreeBSD 8.x/9.x 性能超越 DragonFly；性能叙事的演变：从“超越 FreeBSD”到“小而美”｜ **子-子节**：50.8.1 DragonFly 声称 SMP 性能优于 FreeBSD 的 benchmark；50.8.2 benchmark 方法的争议与独立第三方测试结果；50.8.3 SMP 性能叙事对 DragonFly 社区信心的影响；50.8.4 后续 benchmark 的反转及性能叙事的演变 | DragonFly 1.x 时代体现了项目统摄史观中“分离聚合律”与“形式主义化”的双重运作：从 FreeBSD 4.x 分离是分离聚合律的又一次重演，LWKT 与 token 的设计是形式主义化的工程实践——将“轻量级内核”的哲学固化为代码结构；Dillon 的个人主导模式则是“动手者”存在主义的体现---

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- dangan-20260908 消解回写 -->
- OSNews.. FreeBSD 4.x Forked Into DragonFly [EB/OL]. 2003-07-17. **osnews.com/story/4058/**（含 51 条评论）[EB/OL]. 2003. ［DKC-0104→fulltext:5469］
<!-- /dangan-20260908 -->
