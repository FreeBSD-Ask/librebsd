---
chapter: 第 218 章
id: CH218
volume: 第11卷-dragonflybsd的历史
---

# 第 218 章 dragonflybsd早期演进的vkernel虚拟内核

## 要点

- Linux User Mode Linux (UML) 自 Linux 2.6.0（2003-12）起进入主线，与 vkernel 设计理念相似但实现不同——UML 通过 ptrace 拦截实现用户态内核，vkernel 基于 LWKT 消息传递架构实现。UML 在 Linux 2.6 系列后维护逐渐停滞（Linux 内核复杂度提升导致 UML 同步困难），vkernel 在 DragonFly
- userland 分化使 DragonFly 与 FreeBSD 之间的用户迁移成本增加——bsd_commits.db 显示两仓库 userland 目录 2010-2026 年间独立演进，用户迁移须重新学习命令行为与配置文件格式。但差异小于 FreeBSD 与 OpenBSD 之间的差异（OpenBSD 移除 config 语法、独立维护 openssl 替代品 LibreSSL 等），Dra
- bsd_commits.db 提供 DragonFly/FreeBSD/NetBSD/OpenBSD 四仓库同口径 commits/contributors/tags 表统计（dragonfly-src/freebsd-src/netbsd-src/openbsd-src），是跨项目比较的可靠数据来源。Linux 内核与 illumos 不在 bsd_commits.db 范围内，须以各自官方仓库
- 以总纲第 13 条（法律与道德是利益分配）审视 DragonFly 早期发展方向争议——批评方以“方向不明确”与“代码同步停止”质疑 fork 必要性，反批评方以“工程产出证明”维护 fork 合法性，二者的“项目利益”界定本身即利益分配的争议焦点：批评方界定的“项目利益”是 BSD 阵营整体竞争力（DragonFly fork 削弱 BSD 阵营对 Linux 的竞争力），反批评方界定的“项目利

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4035] 卷“第11卷-dragonflybsd的历史”第 218 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4036] 卷“第11卷-dragonflybsd的历史”第 218 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- UML 与 vkernel 的比较须考虑内核架构差异——Linux 内核代码量数倍于 DragonFly 内核，UML 维护难度高于 vkernel 是客观事实；vkernel 在 DragonFly 中“更实用”的判断须以具体使用场景为准（开发调试 vs 生产部署），不得简单优劣判断；vkernel 性能与真硬件的具体差距 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公
- 迁移成本是主观感受，须基于多案例归纳——bsd_commits.db 不直接提供迁移成本数据，正式撰写时须以 lists.dragonflybsd.org 与 lists.freebsd.org 邮件列表中用户迁移讨论案例统计核验；DragonFly 与 FreeBSD userland 差异“小于 FreeBSD 与 OpenBSD”的判断须以同口径 userland 目录文件 diff 量化核
- 跨项目统计比较的方法论须谨慎——bsd_commits.db 四仓库同口径统计避免苹果与橘子比较，但 Linux/illumos 比较须考虑 commit 定义差异；Foundation 年报数据反映财务状况但非技术活跃度，二者不得混用；bsd_commits.db 不提供下载量、用户数等数据，正式撰写时须以各项目官方统计（如 FreeBSD Foundation 年报下载量、OpenBSD CD
- 【总纲第 13 条的引用边界】总纲第 13 条“法律与道德是利益分配”在 DragonFly 案例中的适用性须以 BSDL 法律延续性为前提——fork 改变代码走向但不改变许可证形式，法律层面的延续性使利益分配冲突限定在技术路线层面；若 fork 涉及许可证变更（如 GPL fork 自 BSDL），法律层面的利益分配冲突将更为复杂；【0 信任原则·许可证延续性的核验】dragonfly.db 

## 文献

- bsd_commits.db dragonfly-src 仓库 commits 表（sys/platform/vkernel/ 目录）；Linux 2.6 内核变更日志 [EB/OL]. <https://kernelnewbies.org/LinuxVersions>；DragonFly vkernel 文档 [EB/OL]. <https://www.dragonflybsd.org/docs/>；UML 文档 [EB/OL]. <http://user-mode-linux.sourceforge.net/> ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db dragonfly-src/freebsd-src/openbsd-src 仓库 commit_files 表（userland 目录文件变更对照）；DragonFly BSD mailing lists [EB/OL]. <https://www.dragonflybsd.org/mailinglists/>；FreeBSD mailing lists [EB/OL]. <https://lists.freebsd.org/archives/> ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- freebsd.db dragonfly-src/freebsd-src/netbsd-src/openbsd-src 仓库 commits/contributors/tags 表（同口径统计对照）；Linux kernel repository [EB/OL]. <https://git.kernel.org/>；illumos repository [EB/OL]. <https://github.com/illumos/illumos-gate>；FreeBSD Foundation. Annual Reports [EB/OL]. <https://www.freebsdfoundation.org/our-donors/> ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13、19、21 条原文）；bsd_commits.db commits/contributors/tags/commit_files 表；DragonFly BSD Project. DragonFly BSD history [EB/OL]. <https://www.dragonflybsd.org/history/>；Dillon M. Annoucning DragonFly BSD! [EB/OL]. 2003-07-16. lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html ［A］FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>### 史观映射> Dillon 的 fork 是分离聚合律的又一次上演——从 FreeBSD 的躯体中分裂出去，带着 4.x 的基因走上一条独立的演化道路；DragonFly 在技术上令人尊敬，却始终无法撼动 FreeBSD 主线的惯性，技术优秀并不足以逆转生态的向心力；而 DragonFly 沿用 BSD 许可证这一事实，与其说是哲学选择不如说是法律基础的惯性延续——分裂可以改变代码的走向，却改变不了许可证的形式主义约束---<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
