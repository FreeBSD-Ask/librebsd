---
chapter: 第 226 章
id: CH226
volume: 第11卷-dragonflybsd的历史
---

# 第 226 章 dragonfly3x-4x时期的技术淘汰

## 要点

- BSD 阵营 sendmail 策略分化为四条路径——NetBSD 早期（1.5/2000）引入 Postfix 并行，2.0（2004）设为默认，4.0（2007）完全移除 sendmail，是 “先并行后移除” 的渐进路径；OpenBSD 2014 下半年直接移除 sendmail（5.7/2015.5 发行说明确认），是 “激进移除” 路径；DragonFly 2015.3 自研 DMA 替
- freebsd.duckdb 数据显示 2012-2014 年间 CoW FS 格局——FreeBSD 用 ZFS（freebsd-src 年均约 14148 条 commit，OpenZFS 关键词 2012 = 1、2015 = 3）、DragonFly 自研 HAMMER2（dragonfly-src 年均约 2598 条 commit，HAMMER2 关键词 2012 = 273 峰值）、
- DragonFly 3.x 周期（2011-2014）是 HAMMER 2 文件系统的开发期——3.0（2011）引入 HAMMER 2 设计讨论、3.2（2012）改进 HAMMER 1 性能、3.8-4.0（2014-2015）发布 HAMMER 2；3.x 周期 dragonfly.duckdb 未见直接归因于 HAMMER/HAMMER 2 文件系统的 CVE——HAMMER 2 在 3.x 周期
- DragonFly 2003 年 fork 后的代码共享减少演化以总纲第 21 条“革命与改革是历史方法论的分歧”审视——Dillon 2003 年选择 fork（革命）而非在 Core Team 框架内继续协商（改革），反映 DragonFly 阵营的“革命”方法论与 FreeBSD Core Team 的“改革”方法论的方法论分歧——Dillon 认为 FreeBSD 5.x 的 SMPng

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4049] 卷“第11卷-dragonflybsd的历史”第 226 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- FreeBSD 2014 起 base 中含 DMA 副本但未默认启用，需明确区分 “在 base 中可用” 与 “默认 MTA” 两个状态；OpenBSD 移除 sendmail 的精确版本（5.6 vs 5.7）需进一步考据 release notes 原文；NetBSD 在 2000-2007 年间同时维护两套 MTA 的资源成本需量化考据
- Linux btrfs 与 illumos ZFS 的 commit 量须以各自 git 仓库核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；CoW FS 选择是生态与许可权衡——ZFS 因 CDDL 许可与 Linux 内核 GPL 不兼容无法主线集成（促使 Linux 推 btrfs），HAMMER2 因 DragonFly 自研无许可问题但生
- HAMMER 2 开发期无 CVE 的原因——HAMMER 2 在 3.x 周期未进入生产部署，漏洞未充分暴露；HAMMER 1 在 3.x 周期无 CVE 可能因 HAMMER 1 代码在 2.x 周期已趋稳定，或因安全研究社区审计关注较少 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；IPSEC 安全修复的
- 考据过程留痕——【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 21 条“革命与改革是历史方法论的分歧”原文经 Read 一手核验；dragonfly.duckdb dragonfly-src 仓库 commits 表 MFC/From FreeBSD 关键词按年（2011 = 6、2012 = 34、2013 = 37、2014 = 34、2015 = 18）与 Dillon c

## 文献

- 各 BSD 项目 release notes；Ed Maste 2022.1.27 freebsd-hackers 邮件；John Baldwin 2022.1.27 回复邮件；DragonFly BSD Digest 2015.3.9 评论 ［A］FreeBSD 社区论文：[FP-2018-032] Profiling the FreeBSD kernel boot: From hammer_time to start_init（Colin Percival，2018）<https://papers.freebsd.org/2018/bsdcan/percival-profiling_the_freebsd_kernel_boot/>FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>### 史观映射> DragonFly 3.x 时代是“形式主义化”在文件系统领域的极致——HAMMER 2 的发布是 Dillon 对“轻量级写时复制文件系统”的形式主义化实现，与 OpenZFS 形成对照；然而 DragonFly 社区规模的持续萎缩让 HAMMER 2 的技术优秀成为一种会者定离的修行——Dillon 在不被理解中坚持自己的文件系统哲学；DragonFly 与 FreeBSD 代码共享的最终独立，是“分离聚合律”的最终形态——从 fork 时的共享代码到最终的完全独立，DragonFly 走完了分离聚合律的全过程；52.6 **DragonFly 从 FreeBSD DRM 转向 Linux DRM 的决策**——决策背景：FreeBSD DRM 维护困难、版本滞后严重；转向 Linux DRM 的技术论证：Linux DRM 更新更快、支持更广；社区对决策的争议：与 FreeBSD 代码共享的进一步减少；决策对 DragonFly 图形支持的影响：GPU 支持改善但与 FreeBSD 路径分叉；与其他 BSD DRM 策略的对比：OpenBSD 的简化 DRM、NetBSD 的 Linux DRM 移植 ｜ **子-子节**：52.6.1 决策背景：FreeBSD DRM 维护困难与版本滞后；52.6.2 转向 Linux DRM 的技术论证；52.6.3 社区对决策的争议及与 FreeBSD 代码共享的减少；52.6.4 决策对图形支持的影响及与其他 BSD DRM 策略的对比；52.7 **32 位弃用决策详述**——DragonFly 4.0（2014）弃用 i386 的技术论证：资源集中、x86_64 普及；与 FreeBSD/NetBSD/OpenBSD 32 位支持政策的对比：DragonFly 最早弃用；用户社区的反馈：少量 i386 用户不满但多数支持；弃用 i386 对 DragonFly 架构精简的影响：代码清理、维护负担降低；弃用决策的形式主义分析：做减法的工程哲学 ｜ **子-子节**：52.7.1 DragonFly 4.0 弃用 i386 的技术论证；52.7.2 与 FreeBSD/NetBSD/OpenBSD 32 位支持政策的对比；52.7.3 用户社区的反馈；52.7.4 弃用 i386 对架构精简的影响及形式主义分析；52.8 **DPorts 软件包管理系统**——DPorts 的设计与实现：基于 FreeBSD Ports 但适配 DragonFly；DPorts 与 FreeBSD Ports 的关系：同步机制、补丁管理；DPorts 与 pkgsrc 的并行使用：DragonFly 同时支持两套软件包管理系统；DPorts 对 DragonFly 用户体验的影响：软件可用性大幅提升；与 FreeBSD pkg/NetBSD pkgsrc/OpenBSD ports 的对比 ｜ **子-子节**：52.8.1 DPorts 的设计与实现；52.8.2 DPorts 与 FreeBSD Ports 的关系（同步机制、补丁管理）；52.8.3 DPorts 与 pkgsrc 的并行使用；52.8.4 DPorts 对用户体验的影响及与其他 BSD 软件包管理的对比；52.9 **HAMMER/HAMMER 2 设计动机与 ZFS/btrfs 详细对比**——HAMMER 设计动机：轻量级写时复制、避免 ZFS 的内存与复杂度；HAMMER 2 的多卷与去重设计：HAMMER 1 的演进；与 ZFS 的技术对比：内存消耗、功能集、稳定性、许可证；与 btrfs 的技术对比：成熟度、工具链、社区支持；HAMMER/HAMMER 2 的形式主义分析：Dillon 个人哲学的代码化；HAMMER 为何未获广泛采用：生态、文档、社区规模 ｜ **子-子节**：52.9.1 HAMMER 设计动机：轻量级写时复制与避免 ZFS 复杂度；52.9.2 HAMMER 2 的多卷与去重设计；52.9.3 与 ZFS 的技术对比（内存、功能、稳定性、许可证）；52.9.4 与 btrfs 的技术对比及 HAMMER 未获广泛采用的原因 | DragonFly 3.x 时代体现了项目统摄史观中“形式主义化”与“会者定离”的双重运作：HAMMER 2 是形式主义化的工程实践（将“轻量级写时复制”固化为代码结构），而社区萎缩与代码独立则是会者定离的宿命——DragonFly 在不被看见的角落守护着自己的架构哲学---

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- openzfs.duckdb commits 表（四仓库 2012-2014 年对照与 OpenZFS/HAMMER2 关键词按年）；McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015.；各系统 2012-2014 文件系统官方文档 ［B］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库；DragonFly 3.0-3.8 Release Notes；Matt Dillon HAMMER 2 设计文档 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 21 条原文）；dragonfly.duckdb dragonfly-src 仓库 commits 表（MFC/From FreeBSD 关键词按年与 Dillon 按年统计）；freebsd.duckdb freebsd-src 仓库 tags 表（FreeBSD 5.0-5.5 release 序列）；ONLamp. DragonFly BSD: A Fork in the FreeBSD Road [EB/OL]. 2004. 经 archive.org 核验，web.archive.org/web/2004*/onlamp.com；Dillon M. Annoucning DragonFly BSD! [EB/OL]. 2003-07-16. lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
