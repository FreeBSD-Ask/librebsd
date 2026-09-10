---
chapter: 第 231 章
id: CH231
volume: 第11卷-dragonflybsd的历史
---

# 第 231 章 dragonfly6x的现代化与持续维护

## 要点

- bsd_commits.db dragonfly-src 仓库 commits 表提供 v6.2/v6.4 系列 GPU 与驱动支持改进的具体 commit。v6.2 系列（2022-01-09 至 2022-06-09）期间 sys/dev/drm/ 目录 commit 集中于 Linux DRM 回移；v6.4 系列（2022-12-30 起）期间 sys/dev/netif/ 与 sys/d
- dragonfly.db dragonfly-src 仓库 commits 表提供 v6.4.1/v6.4.2 发布说明的 commit 级核验——v6.4.1 target_commit_hash = 9408681d90f4953a150a1682b6413610234981fa（2025-04-29）、v6.4.2 target_commit_hash = 54d7118100cb99b74
- bsd_commits.db 不直接记录 commit 权限变动，权限授予与撤销须以 DragonFly 邮件列表（lists.dragonflybsd.org）中 Dillon 或 kernel@ 的公告为准。lists.dragonflybsd.org 完整归档 2003-2026 年间 kernel@、commits@、users@、bugs@ 等邮件列表，未发生类似 FreeBSD 201
- bsd_commits.db dragonfly-src 仓库 tags 表共 131 个 tag，按 tagger_date 升序首 tag 为 v2.1.1（2008-12-03），末 tag 为 v6.4.2（2025-05-09）。2019-2026 年间发布记录：v6.0.0（2021-05-07）、v6.0.1（2021-10-11）、v6.2.1（2022-01-09）、v6.2.2
- DragonFly BSD 无正式 Security Advisory（SA）系统，安全修复通过 commit message 与 kernel@ 邮件列表通知用户——这与 FreeBSD SA（14.x 周期 80 个 PGP 签名 SA）、OpenBSD errata（逐版本发布 errata patches）形成鲜明对比；6.x 周期 16 条 CVE commit 中，仅 CVE-2024

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4114] 卷“第11卷-dragonflybsd的历史”第 231 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- commit log 可能不完整反映改进全貌——部分改进可能分散在多个 commit 中，部分改进可能合并入单一 commit；bsd_commits.db 显示 v6.2 系列期间 sys/dev/drm/ 目录 commit 多为 Linux DRM 回移，DragonFly 自研 GPU 改进贡献有限
- release notes 与 commit log 偶有不一致——bsd_commits.db 显示 v6.4.1 与 v6.4.2 间隔仅 10 天，反映 v6.4.1 可能存在已知 bug 由 v6.4.2 快速修复；正式撰写时须以 commit log 为事实依据，release notes 为辅助参考
- 邮件记录可能不完整——部分权限决策可能在私下邮件或 IRC 中进行；bsd_commits.db 显示 Aaron LI 首 commit = 2017-09-27，但其在 kernel@ 邮件列表的首次发言 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证] 须单独核验；权限撤销记录在 DragonFly 中罕见——bsd_commits.db contr
- 仓库统计须考虑 commit 粒度差异——dragonfly.db 显示 DragonFly 2024 年 277 条 commit 中 Aaron LI 贡献 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]，须按 author_email 按年分组核验；v6.5.0 tag 与 v6.4.0rc1 同日（2022-12-20）且相差仅 2 分钟（23:
- *无 SA 系统可持续性的辨析（vs 5.x 周期）**：5.x 周期无 SA 系统在 Dillon 主导代码贡献的背景下可行（Dillon 4 条 CVE commit 中 2 条为 embargo 期内修复），6.x 周期无 SA 系统面临 Dillon 淡出的可持续性挑战——bsd_commits.db 显示 6.x 周期 Dillon 仅 1 条 CVE commit，其余 15 条由其他

## 文献

- bsd_commits.db dragonfly-src 仓库 commits 表与 commit_files 表（v6.2/v6.4 系列 GPU 与驱动 commit）；kernel@ 邮件列表档案；DragonFly 硬件兼容性列表 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2022-2025 年间：123,092 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.db dragonfly-src 仓库 tags 表（v6.4.1/v6.4.2 target_commit_hash）；dragonfly.db dragonfly-src 仓库 commits 表（v6.4.1 与 v6.4.2 间 commit）；DragonFly 6.4.1/6.4.2 release notes [EB/OL]. dragonflybsd.org/release/ ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2023-2025 年间：71,438 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- lists.dragonflybsd.org 邮件列表归档；bsd_commits.db dragonfly-src 仓库 contributors 表（first_commit_date 序列）；marc.info DragonFly 备份 ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2019-2026 年间：263,468 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.db dragonfly-src 仓库 tags 表（131 条 tag 完整序列）；dragonfly.db 查询 L1.1.1（dragonfly-src 2019-2026 年按年 commit 量）；宏观趋势统计.md §L1.1.1；DragonFly BSD Project. Releases [EB/OL]. <https://www.dragonflybsd.org/release/> ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2026-2026 年间：1,173 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- FreeBSD Project. bsd_commits.db — four repos annual commit count comparison [DB/OL]. 2026-07-22. SQL: SELECT repo_name, strftime('%Y’, author_date) AS year, count(*) FROM commits WHERE repo_name IN (‘dragonfly-src’,‘freebsd-src’,‘openbsd-src’,‘netbsd-src’) AND author_date >=‘2024-01-01’ AND author_date <‘2026-07-22’ GROUP BY repo_name, year ORDER BY repo_name, year; DragonFly BSD Project. Mailing Lists Archives [EB/OL]. [2026-07-22]. <https://www.dragonflybsd.org/mailinglists/>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. [2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. OpenBSD Errata Patches [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata.html> ［A］<!-- DB_REF:dragonfly.duckdb -->> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP491（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- DragonFly BSD 发布 6.4（2022 年 12 月 30 日），延续 6.x 系列：内核修复涉及 exec CVPE 环境传递、名称缓存膨胀与 vnode 回收、HAMMER2 的批量释放与内存分配，并引入来自 FreeBSD 的 GTaskQ API；默认编译器仍为 GCC 8，新增对 Type 2 hypervisor（NVMM）、AMD GPU 驱动与 HAMMER2 卷远程挂载的实验性支持。（BSD Now EP491，[188.06-530.00]，L2）
- 节目转述 Clara 关于 OpenZFS 在 FreeBSD 与 Linux 间取舍的文章，指出 2020 年 12 月 OpenZFS 统一了 FreeBSD 与 Linux 平台的代码库；FreeBSD 安装器原生默认支持 OpenZFS root，而 Ubuntu 依赖未完成的 ZSys 项目并遗留过多 dataset 与快照管理问题。（BSD Now EP491，[525.06-993.02]，L2）
- Peter 的博客回顾其约 15 年的 greytrapping 与灰名单实践：其 bsdly.net 兼作个人邮件服务与蜜罐，用于生成 IP 信誉数据；他讨论 71% 垃圾邮件捕获率的衡量问题，并指出在内容过滤前尽早丢弃垃圾流量可降低资源与能耗。（BSD Now EP491，[1134.30-1417.44]，L2）
- 节目报道第六届可复现构建峰会 2022 于威尼斯举行，NetBSD 基础系统自 8.0 起可复现构建，pkgsrc 也已迈出第一步，但包级可复现仍有待完善。（BSD Now EP491，[1922.36-2086.72]，L2）
- 其余内容涉及 Ubuntu 在 FreeBSD 的 Linux 二进制兼容搭建、疯狂 shell 提示符的 misc 邮件，以及用 Ansible 管理 FreeBSD jail 的问答。（BSD Now EP491，[1705.60-1922.36]，L2）

**史料**：

- DragonFly BSD 6.4 发布说明，涉及内核、HAMMER2、GCC 默认版本与 NVMM 支持，为官方发布线索，经节目转述。（BSD Now EP491，[188.06-530.00]，L2）
- Clara 关于 OpenZFS 在 FreeBSD 与 Linux 平台差异的文章，为二手技术文本，经节目转述。（BSD Now EP491，[525.06-993.02]，L2）
- Peter 关于 greytrapping 与垃圾邮件捕获衡量的博客及其 bsdly.net 数据，为当事人一手实践叙述，经节目转述。（BSD Now EP491，[1134.30-1417.44]，L1）
- NetBSD 可复现构建峰会报告由 Pierre Pronchery 撰写，为参会者一手叙述，经节目转述。（BSD Now EP491，[1922.36-2086.72]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：OpenZFS 跨平台实现先分离后统一，社区与代码在聚合中重新整合。：OpenZFS 在 2020 年统一 FreeBSD 与 Linux 代码库，体现长期分离后的再次聚合。（BSD Now EP491，[562.70-573.74]，L2）
- 总纲10 动手者创造历史：版本演进由内核、文件系统与驱动的逐项修复累积而成。：DragonFly 与 NetBSD 的维护者以持续提交累积系统改进，动手者的日常修复构成系统演进。（BSD Now EP491，[188.06-530.00]，L2）
- 总纲9 经验优先：以长期运行积累的实测数据评估垃圾邮件防护，而非仅凭厂商宣称。：greytrapping 以十五年实测数据衡量防护效果，经验数据优先于营销性宣称。（BSD Now EP491，[1134.30-1417.44]，L1）

**辨析**：

- DragonFly 6.4 的具体内核修复与特性为发布说明转述，其中 GCC 默认版本与 HAMMER2 远程挂载状态需以官方发布说明与提交核验。　[存疑脚注] 版本细节为节目转述，须以 DragonFly 官方发布说明与提交记录核验。（BSD Now EP491，[188.06-530.00]，L4）
- OpenZFS 统一时间为 2020 年 12 月的表述为节目转述，需以 OpenZFS 官方公告核验。　[存疑脚注] 代码库统一的具体时间需以 OpenZFS 项目公告与提交记录确认。（BSD Now EP491，[562.70-573.74]，L4）

**文献**：

- [BSD Now EP491] Pennington J. BSD Now: 491: Catch the Spammers[EB/OL]. (2023-01-26)[2026-08-15]. <https://www.bsdnow.tv/491>.

<!-- /PODCAST_REVIEW -->
