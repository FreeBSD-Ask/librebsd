---
chapter: 第 230 章
id: CH230
volume: 第11卷-dragonflybsd的历史
---

# 第 230 章 dragonfly5x的现代化与hammer2持续改进

## 要点

- dragonfly.duckdb dragonfly-src 仓库 tags 表提供 v5.0.0（**2017-10-15**）与 v5.2.0（**2018-04-08**）的 tagger_date、tagger_name、target_commit_hash 字段，作为发布日期的最权威代码级证据。tagger_date 与 target_commit_date 对照如下： | tag | t |

- dragonfly.duckdb dragonfly-src 仓库 commits 表提供 v5.4-v5.6 时期 HAMMER 2 相关 commit 的具体记录。2018 年 HAMMER2 关键词 commit **75 条**、2019 年 **156 条**，其中 v5.6.0（**2019-06-16**）发布前的 HAMMER 2 commit 集中于性能优化与默认切换准备。HAMMER2〔原文截断，后续缺失待补〕

- dragonfly.duckdb dragonfly-src 仓库 tags 表提供 v5.8.0 与 v6.0.0 的 tagger_date、tagger_name、target_commit_date 字段。v5.8.0 与 v6.0.0 对照如下：

| tag | tagger_date | target_commit_date | 时间差 | 发布模式 |
| --- | --- | --- | --- | --- |
| v5.8.0 | 2020-02-29 | 2020-02-28 | — | 大版本发布 |
| v6.0.0 | 2021-05-07 | 2021-04-27 | 423 天 | 大版本发布（半年节奏延展） |


- dragonfly.duckdb dragonfly-src 仓库 contributors 表中 first_commit_date 字段是权限授予时间的间接证据，须与 lists.dragonflybsd.org 邮件列表公告交叉验证。dragonfly.duckdb 显示 Aaron LI 首 commit = 2017-09-27（<aly@aaronly.me> 邮箱），Huete Jimenez〔原文截断，后续缺失待补〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4110] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4111] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4112] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4113] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- release notes 与 commit log 偶有不一致——bsd_commits.duckdb 显示 v5.2.0 的 tagger_date（2018-04-08）与 target_commit_date（2018-04-03）相差 5 天，反映 tag 创建与最后 commit 提交的时间差；AMD64 与 NVMe 改进的具体 commit 须以 commit_files 表核验 ［考据完——原文截断，待补全］
- commit log 可能不完整反映改进全貌——dragonfly.duckdb 关键词搜索仅基于 message_subject，部分 HAMMER 2 commit 可能未在 message_subject 中提及‘HAMMER2’；Dillon 2019 年 HAMMER 2 commit 占比须以 commit_files 表核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. dragonflybsd.org/release/；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2017-2020 年间：163,928 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 commits 表（HAMMER2 关键词与 Dillon 按年统计）；kernel@ 邮件列表档案；HAMMER 2 性能 benchmark 报告 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2018-2019 年间：94,083 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 tags 表（v5.8.0/v6.0.0 完整字段）；DragonFly 5.8/6.0 release notes [EB/OL]. dragonflybsd.org/release/；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2020-2021 年间：92,381 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- lists.dragonflybsd.org 邮件列表归档；mail-index.netbsd.org 邮件列表归档；lists.freebsd.org 邮件列表归档；marc.info OpenBSD 邮件列表备份；dragonfly.duckdb commits 表（关键词统计） ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2023-2026 年间：72,611 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 contributors 表（first_commit_date 序列）；lists.dragonflybsd.org 邮件列表归档；Dillon 个人网站；DragonFly commit log ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2017-2026 年间：348,708 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- 各 BSD 项目 release notes；DragonFly BSD Digest 2019.7.30 与 2021.1.8；DragonFly 5.6/6.0 release notes［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）**<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>**

### 史观映射

> DragonFly 5.x 时代是“会者定离”在 BSD 世界的最终呈现——Dillon 在不被看见的角落持续维护 DragonFly，HAMMER 2 与 LWKT 的技术优秀并未为 DragonFly 带来市场份额；DragonFly 的现状是“在虚假中寻找仅存的真实”的另一种诠释——当 Linux 以 cgroups/Docker/Kubernetes 垄断数据中心，DragonFly 在 HAMMER 2 与 LWKT 中守护着另一种“真实”；而 Dillon 个人主导模式的可持续性问题，则是“动手者”存在主义的极限——一个人在不被理解中坚持，但这种坚持能持续多久是 DragonFly 最大的不确定性

### 本章后续子节大纲（旧章号 54.6-54.9；重排为 230.x 及 230.8/230.9 补建须主理人裁断）

- 54.6 **DragonFly 的 ARM64 支持现状**——DragonFly 6.x 对 ARM64 的支持情况：实验性、未达 Tier-1；与 FreeBSD arm64 Tier-1 的对比：FreeBSD 早已 Tier-1，DragonFly 滞后；ARM64 支持滞后的原因：社区规模小、Dillon 个人精力有限；ARM64 支持对 DragonFly 嵌入式市场的影响：难以进入 ARM 服务器市场；与 NetBSD（ARM 早期生态先发）的对比：历史轮回 ｜ **子-子节**：54.6.1 DragonFly 6.x 对 ARM64 的支持情况；54.6.2 与 FreeBSD arm64 Tier-1 的对比；54.6.3 ARM64 支持滞后的原因；54.6.4 ARM64 支持对嵌入式市场的影响及与 NetBSD 的历史对比
- 54.7 **DragonFly 的资金/赞助情况**——Dillon 个人资助项目的历史：长期自掏腰包维护基础设施；企业赞助情况：少量企业赞助、无长期商业支持公司；与 FreeBSD Foundation（资金充裕）/NetBSD Foundation（资金紧张）/OpenBSD Foundation（2014 危机）的对比；资金问题对 DragonFly 可持续性的影响：基础设施老化、开发者流失；DragonFly 无独立 Foundation 的治理风险 ｜ **子-子节**：54.7.1 Dillon 个人资助项目的历史；54.7.2 企业赞助情况及与三大 BSD Foundation 的对比；54.7.3 资金问题对 DragonFly 可持续性的影响；54.7.4 DragonFly 无独立 Foundation 的治理风险
- 54.8 **DragonFly 的虚拟化支持**——vkernel 之外的虚拟化支持：bhyve、Xen、KVM 等；DragonFly 对 bhyve 的支持情况：从 FreeBSD 移植、维护滞后；DragonFly 对 Xen 的支持情况：早期实验、未深度集成；DragonFly 作为虚拟机 guest 的支持：virtio 驱动、性能优化；虚拟化支持对 DragonFly 服务器市场的影响：有限采用 ｜ **子-子节**：54.8.1 vkernel 之外的虚拟化支持概述；54.8.2 DragonFly 对 bhyve 的支持情况；54.8.3 DragonFly 对 Xen 的支持情况及作为 guest 的支持；54.8.4 虚拟化支持对服务器市场的影响；54.9 **DragonFly 的 NVIDIA GPU 驱动支持**——DragonFly 对 NVIDIA 专有驱动的支持：从 FreeBSD 移植；与 FreeBSD NVIDIA 驱动的关系：版本同步、补丁差异；NVIDIA 驱动对新版 DragonFly 的滞后：NVIDIA 官方支持有限；NVIDIA 驱动对 DragonFly 桌面用户体验的影响：图形性能；与 OpenBSD（拒绝 NVIDIA 专有驱动）的对比 ｜ **子-子节**：54.9.1 DragonFly 对 NVIDIA 专有驱动的支持；54.9.2 与 FreeBSD NVIDIA 驱动的关系；54.9.3 NVIDIA 驱动对新版 DragonFly 的滞后；54.9.4 NVIDIA 驱动对桌面用户体验的影响及与 OpenBSD 的对比

DragonFly 5.x 时代体现了项目统摄史观中“会者定离”与“在虚假中寻找仅存的真实”的双重运作：Dillon 在不被看见中持续维护是会者定离的修行，HAMMER 2 与 LWKT 的坚守是在虚假（Linux 容器垄断）中寻找仅存的真实（轻量级内核哲学）；而 Dillon 个人主导模式的可持续性问题，则是“动手者”存在主义的极限——一个人能坚持多久，决定了 DragonFly 的未来

---

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 commits 表（HAMMER2 关键词统计）；McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015；各系统 release notes ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,207 次提交。> 仓库总览：656,207 次提交，213 位贡献者，2003-06-17 至 2026-08-18。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP324（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Dan Langille 记录把 ZFS 池从 Dell R710 迁至 R720 的过程：停止应用、导出池、换盘、导入即可，且 ZFS 能跨端序（如 amd64 到 sparc64）处理，远超依赖同型 RAID 控制器的传统迁移。（BSD Now EP324，[261.86-321.34]，L2）
- 《OpenBSD in 2019》体验帖列举其优点（安全优先、base 与 /usr/local 分离、高质量 man page、clang 支持 C++17）与缺点（升级需手动清理、RAM 耗尽死机、find/du/tar 等工具差异），结论是仍愿继续使用。（BSD Now EP324，[501.72-909.04]，L2）
- Hammer2 增加紧急空间模式，允许在无空间写历史时继续磁盘操作，但会牺牲断电保护并可能损坏快照，与 ZFS 预留 slop 空间、UFS 超 100% 的策略形成对照。（BSD Now EP324，[1526.06-1671.52]，L2）
- ICCCM 选择机制的吐槽揭示 X11 规范以 atom 表达一切、缺少目标类型与属性类型的显式关联，实现者各自解读导致兼容性 creep 与增量传输的脆弱。（BSD Now EP324，[1304.40-1519.02]，L2）
- DragonFly BSD 更新 zlib 至 1.2.11、导入 dhcpcd 8.1.1，并把 PAM SSH/TacPlus/Radius 模块移出 base 改由 ports 提供，以换取更频繁的更新节奏。（BSD Now EP324，[923.76-987.80]，L2）

**史料**：

- Dan Langille 博客的 ZFS 迁移记录，含 zpool status 快照、驱动托盘与 ICY Dock 适配器换装细节。（BSD Now EP324，[133.60-235.80]，L2）
- 用户体验帖《OpenBSD in 2019》及其对 GNU cpio 1994 年遗留 bug 的对照检查。（BSD Now EP324，[388.92-402.52]，L2）
- DragonFly BSD 关于 Hammer2 emergency mode 的提交说明，及 zlib、dhcpcd、PAM 模块调整的维护记录。（BSD Now EP324，[937.08-993.00]，L2）
- Brian Kernighan《Unix: A History and a Memoir》由 Princeton 于 2019 年 10 月出版的信息。（BSD Now EP324，[1938.08-1996.44]，L2）

**史观**：

- 总纲9 经验优先：ZFS 迁移与 OpenBSD 评估都来自动手记录与亲身使用，而非厂商宣传或抽象判断。（BSD Now EP324，[106.52-115.00]，L2）
- 总纲8 本体论上各方平等：OpenBSD 的优点被承认、缺点被具体列出，不神话也不贬低任何一方。（BSD Now EP324，[501.72-909.04]，L2）
- 总纲4 分离聚合是永恒规律：ZFS 数据可从一台机器分离、在另一台聚合，硬件代际更替体现分离聚合的循环。（BSD Now EP324，[263.66-301.54]，L2）
- 总纲12 科学是形式主义：写时复制、紧急模式、slop 空间是文件系统对空间与安全的形式化约定。（BSD Now EP324，[1542.42-1671.52]，L2）
- 总纲22 知识注定过时：OpenBSD 体验帖中列出的坏项可能已被修复，工具行为随版本变化，知识需持续更新。（BSD Now EP324，[898.80-921.40]，L2）
- 总纲5 没有必然性，只有偶然性：能否顺利迁移取决于托盘规格、热插拔适配等偶然硬件条件，而非抽象必然。（BSD Now EP324，[142.44-153.60]，L2）

**辨析**：

- Hammer2 紧急模式的“损坏快照”风险与 ZFS 预留空间对比为二手转述，未读 DragonFly 源码验证其具体实现边界。　[存疑脚注] 需对照 DragonFly 提交与手册核实危险程度（BSD Now EP324，[1557.86-1562.90]，L4）
- OpenBSD 体验帖的 RAM 耗尽死机成因不确定是 OpenBSD 本身还是 Vultr 虚拟化环境，作者本人未下定论。　[考据脚注] 环境变量未隔离，因果归属存疑（BSD Now EP324，[691.12-706.72]，L4）

**文献**：

- [BSD Now EP324] Pennington J. BSD Now: 324: Emergency Space Mode[EB/OL]. (2019-11-14)[2026-08-15]. <https://www.bsdnow.tv/324>.

<!-- /PODCAST_REVIEW -->
