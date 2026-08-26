---
chapter: 第 230 章
id: CH230
volume: 第11卷-dragonflybsd的历史
---

# 第 230 章 dragonfly5x的现代化与hammer2持续改进

## 要点

- dragonfly.db dragonfly-src 仓库 tags 表提供 v5.0.0（**2017-10-15**）与 v5.2.0（**2018-04-08**）的 tagger_date、tagger_name、target_commit_hash 字段，作为发布日期的最权威代码级证据。tagger_date 与 target_commit_date 对照如下：    | tag | t
- bsd_commits.db dragonfly-src 仓库 commits 表提供 v5.4-v5.6 时期 HAMMER 2 相关 commit 的具体记录。2018 年 HAMMER2 关键词 commit **75 条**、2019 年 **156 条**，其中 v5.6.0（**2019-06-16**）发布前的 HAMMER 2 commit 集中于性能优化与默认切换准备。HAMME
- bsd_commits.db dragonfly-src 仓库 tags 表提供 v5.8.0 与 v6.0.0 的 tagger_date、tagger_name、target_commit_date 字段。v5.8.0 与 v6.0.0 对照如下：    | tag | tagger_date | target_commit_date | 时间差 | 发布模式 |    |---|---|--
- DragonFly（lists.dragonflybsd.org）、NetBSD（mail-index.netbsd.org）、FreeBSD（lists.freebsd.org）、OpenBSD（marc.info/?l = openbsd-misc）四个项目的邮件列表归档完整保留 2023-2026 年间 AI 代码政策相关讨论。四项目邮件列表归档对照如下：    | 项目 | 归档域名 |
- bsd_commits.db dragonfly-src 仓库 contributors 表中 first_commit_date 字段是权限授予时间的间接证据，须与 lists.dragonflybsd.org 邮件列表公告交叉验证。bsd_commits.db 显示 Aaron LI 首 commit = 2017-09-27（<aly@aaronly.me> 邮箱），Huete Jimene

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4110] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4111] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4112] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4113] 卷“第11卷-dragonflybsd的历史”第 230 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- release notes 与 commit log 偶有不一致——bsd_commits.db 显示 v5.2.0 的 tagger_date（2018-04-08）与 target_commit_date（2018-04-03）相差 5 天，反映 tag 创建与最后 commit 提交的时间差；AMD64 与 NVMe 改进的具体 commit 须以 commit_files 表核验 [考据完
- commit log 可能不完整反映改进全貌——bsd_commits.db 关键词搜索仅基于 message_subject，部分 HAMMER 2 commit 可能未在 message_subject 中提及‘HAMMER2’；Dillon 2019 年 HAMMER 2 commit 占比须以 commit_files 表核验 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待
- release notes 与 commit log 偶有不一致——dragonfly.db 显示 v6.0.0 的 target_commit_date（2021-04-27）与 tagger_date（2021-05-07）相差 10 天，反映 tag 创建与最后 commit 提交的时间差；v5.8.0 的 commit 与 tag 同日须以 commit_hash 与 target_com
- 政策发言可能被断章取义——须结合完整上下文辨析，避免简化引用；bsd_commits.db 关键词搜索可能低估 AI 相关讨论——部分讨论可能以‘machine learning’/‘language model’等术语进行而未提及‘AI’；私人邮件与 IRC 讨论不可考，仅以公开邮件列表为准
- 邮件发言需考据时间与上下文——Dillon 早期发言（2003-2005 年）与后期发言（2020-2026 年）风格有变化，需结合具体时期辨析；bsd_commits.db contributors 表 first_commit_date 是权限授予的间接证据，可能晚于实际权限授予时间——Dillon 可能在邮件列表公告权限授予后数日才让新 committer 提交首条 commit；权限撤销记

## 文献

- bsd_commits.db dragonfly-src 仓库 tags 表（v5.0.0/v5.2.0 完整字段）；DragonFly 5.0/5.2 release notes [EB/OL]. dragonflybsd.org/release/；kernel@ 邮件列表档案 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2017-2020 年间：163,928 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db dragonfly-src 仓库 commits 表（HAMMER2 关键词与 Dillon 按年统计）；kernel@ 邮件列表档案；HAMMER 2 性能 benchmark 报告 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2018-2019 年间：94,083 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db dragonfly-src 仓库 tags 表（v5.8.0/v6.0.0 完整字段）；DragonFly 5.8/6.0 release notes [EB/OL]. dragonflybsd.org/release/；kernel@ 邮件列表档案 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2020-2021 年间：92,381 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- lists.dragonflybsd.org 邮件列表归档；mail-index.netbsd.org 邮件列表归档；lists.freebsd.org 邮件列表归档；marc.info OpenBSD 邮件列表备份；bsd_commits.db commits 表（关键词统计） ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2023-2026 年间：72,611 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db dragonfly-src 仓库 contributors 表（first_commit_date 序列）；lists.dragonflybsd.org 邮件列表归档；Dillon 个人网站；DragonFly commit log ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2017-2026 年间：348,708 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- 各 BSD 项目 release notes；DragonFly BSD Digest 2019.7.30 与 2021.1.8；DragonFly 5.6/6.0 release notes[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]FreeBSD 社区论文：[FP-2004-001] The Challenges of Dynamic Network Interfaces（Brooks Davis，2004）<https://papers.freebsd.org/2004/eurobsdcon/davis-challenges_of_dynamic_network_interfaces/>### 史观映射> DragonFly 5.x 时代是“会者定离”在 BSD 世界的最终呈现——Dillon 在不被看见的角落持续维护 DragonFly，HAMMER 2 与 LWKT 的技术优秀并未为 DragonFly 带来市场份额；DragonFly 的现状是“在虚假中寻找仅存的真实”的另一种诠释——当 Linux 以 cgroups/Docker/Kubernetes 垄断数据中心，DragonFly 在 HAMMER 2 与 LWKT 中守护着另一种“真实”；而 Dillon 个人主导模式的可持续性问题，则是“动手者”存在主义的极限——一个人在不被理解中坚持，但这种坚持能持续多久是 DragonFly 最大的不确定性；54.6 **DragonFly 的 ARM64 支持现状**——DragonFly 6.x 对 ARM64 的支持情况：实验性、未达 Tier-1；与 FreeBSD arm64 Tier-1 的对比：FreeBSD 早已 Tier-1，DragonFly 滞后；ARM64 支持滞后的原因：社区规模小、Dillon 个人精力有限；ARM64 支持对 DragonFly 嵌入式市场的影响：难以进入 ARM 服务器市场；与 NetBSD（ARM 早期生态先发）的对比：历史轮回 ｜ **子-子节**：54.6.1 DragonFly 6.x 对 ARM64 的支持情况；54.6.2 与 FreeBSD arm64 Tier-1 的对比；54.6.3 ARM64 支持滞后的原因；54.6.4 ARM64 支持对嵌入式市场的影响及与 NetBSD 的历史对比；54.7 **DragonFly 的资金/赞助情况**——Dillon 个人资助项目的历史：长期自掏腰包维护基础设施；企业赞助情况：少量企业赞助、无长期商业支持公司；与 FreeBSD Foundation（资金充裕）/NetBSD Foundation（资金紧张）/OpenBSD Foundation（2014 危机）的对比；资金问题对 DragonFly 可持续性的影响：基础设施老化、开发者流失；DragonFly 无独立 Foundation 的治理风险 ｜ **子-子节**：54.7.1 Dillon 个人资助项目的历史；54.7.2 企业赞助情况及与三大 BSD Foundation 的对比；54.7.3 资金问题对 DragonFly 可持续性的影响；54.7.4 DragonFly 无独立 Foundation 的治理风险；54.8 **DragonFly 的虚拟化支持**——vkernel 之外的虚拟化支持：bhyve、Xen、KVM 等；DragonFly 对 bhyve 的支持情况：从 FreeBSD 移植、维护滞后；DragonFly 对 Xen 的支持情况：早期实验、未深度集成；DragonFly 作为虚拟机 guest 的支持：virtio 驱动、性能优化；虚拟化支持对 DragonFly 服务器市场的影响：有限采用 ｜ **子-子节**：54.8.1 vkernel 之外的虚拟化支持概述；54.8.2 DragonFly 对 bhyve 的支持情况；54.8.3 DragonFly 对 Xen 的支持情况及作为 guest 的支持；54.8.4 虚拟化支持对服务器市场的影响；54.9 **DragonFly 的 NVIDIA GPU 驱动支持**——DragonFly 对 NVIDIA 专有驱动的支持：从 FreeBSD 移植；与 FreeBSD NVIDIA 驱动的关系：版本同步、补丁差异；NVIDIA 驱动对新版 DragonFly 的滞后：NVIDIA 官方支持有限；NVIDIA 驱动对 DragonFly 桌面用户体验的影响：图形性能；与 OpenBSD（拒绝 NVIDIA 专有驱动）的对比 ｜ **子-子节**：54.9.1 DragonFly 对 NVIDIA 专有驱动的支持；54.9.2 与 FreeBSD NVIDIA 驱动的关系；54.9.3 NVIDIA 驱动对新版 DragonFly 的滞后；54.9.4 NVIDIA 驱动对桌面用户体验的影响及与 OpenBSD 的对比 | DragonFly 5.x 时代体现了项目统摄史观中“会者定离”与“在虚假中寻找仅存的真实”的双重运作：Dillon 在不被看见中持续维护是会者定离的修行，HAMMER 2 与 LWKT 的坚守是在虚假（Linux 容器垄断）中寻找仅存的真实（轻量级内核哲学）；而 Dillon 个人主导模式的可持续性问题，则是“动手者”存在主义的极限——一个人能坚持多久，决定了 DragonFly 的未来---<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- bsd_commits.db dragonfly-src 仓库 commits 表（HAMMER2 关键词统计）；McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015；各系统 release notes ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
