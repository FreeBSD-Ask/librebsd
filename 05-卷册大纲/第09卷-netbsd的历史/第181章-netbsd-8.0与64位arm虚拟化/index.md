---
chapter: 第 181 章
id: CH181
volume: 第09卷-netbsd的历史
---

# 第 181 章 netbsd-8.0与64位arm虚拟化

## 要点

- NetBSD 8.0（**2018.7**）引入 aarch64（ARM64）支持，由 Ryo Shimizu 等推动；~~开发历时 3 年（2015-2018）~~（经 netbsd.db 验证：aarch64 后端最早由 joerg 于 2013-02-04 引入 LLVM/Clang AArch64 后端，实际开发周期约 5 年 2013-2018）；涉及内核 ABI、虚拟内存、中断控制器（
- NVMM 设计文档由 Maxime Villard 撰写，散见于 man **nvmm(4)**、tech-virt 邮件列表、Villard 个人博客；源码考据需对照 CVS commit log 与 Villard 的 commit 署名；考据需注意 NVMM 在 8.0 之后的持续演进
- NetBSD 8.0（**2018.7**）引入 KASLR（Kernel Address Space Layout Randomization）内核安全特性；旧内核无 KASLR，存在固定地址空间布局的攻击面；KASLR 由 Maxime Villard 实现；此改进让 NetBSD 在内核安全上追赶 OpenBSD，体现 “在虚假中寻找仅存的真实”。~~原叙事中 “NetBSD 8.0 引入
- 2018 年 ARM64 虚拟化成竞争点：Linux KVM 在服务器领先，FreeBSD bhyve 偏 x86，NetBSD 8.0 推 ARM64 虚拟化 + SMP，OpenBSD 6.3 安全利基，Windows Hyper-V 守企业 x86；NetBSD 8.0 以“ARM64 虚拟化 + 多核”强化可移植哲学的现代延伸。
- 8.x 周期 NetBSD Security Officer Team 的 15 个 SA 在数量、节奏、覆盖面三个维度呈现“过渡期”特征——年化速率约 7.5 SA/年（2018 年 9 个、2019 年 6 个），高于 9.x 周期的约 3.6 SA/年，反映 8.0 新代码引入的攻击面集中暴露；**8.x 周期 SA 发布节奏**：2018 年 9 个 SA 集中于 8.0 发布前后（SA2

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4088] 卷“第09卷-netbsd的历史”第 181 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4089] 卷“第09卷-netbsd的历史”第 181 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:bsdnow_podcast:outline_mappings:om_10426] BSD Now 第 676 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10512] BSD Now 第 661 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10527] BSD Now 第 656 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10534] BSD Now 第 655 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10542] BSD Now 第 654 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10557] BSD Now 第 652 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10567] BSD Now 第 651 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10591] BSD Now 第 645 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10609] BSD Now 第 642 期，匹配 CH181 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10633] BSD Now 第 638 期，匹配 CH181 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NetBSD aarch64 支持与 Linux aarch64 支持的成熟度对比缺乏权威基准。经 netbsd.db netbsd-src 仓库 commits 表验证：aarch64 后端最早于 2013.2.4 由 joerg 引入（LLVM/Clang snapshot r174288），AARCH64 定义于 2013.10.29 由 matt 添加，远早于 8.0 发布 2018.7
- Villard 的 commit 在 CVS 与 Git 仓库中的署名可能略有差异——需对照多源核验；NVMM 在 9.0/10.0 的具体改进需考据
- 8.0 KASLR 是否默认启用在不同叙事中存在分歧——需对照源码核验。经 netbsd.db netbsd-src 仓库 commits 表验证：KASLR 首次引入时间为 2017-10-07（maxv commit 650b1fa4d5f1e80900b37549c6a3e41dbf4e4f8b"Add GENERIC_KASLR, only toolchain parts for now"
- 虚拟化市场由云生态主导，NetBSD 8.0 在嵌入式/教育利基具价值。
- *数量对比的辨析**：8.x 周期 15 个 SA（年化 7.5 SA/年）与 9.x 周期 18 个 SA（年化 3.6 SA/年）的对比须考虑三个因素：其一，8.x 周期时间窗约 2 年，9.x 周期约 5 年，年化速率差异反映 8.0 新代码攻击面集中暴露；其二，8.x 周期 4 个网络栈 SA（SA2018-003/004/006/007）是 8.0 IPv6/IPsec 改进伴随的攻击面

## 文献

- man **nvmm(4)**；tech-virt 邮件列表；Maxime Villard 博客 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2018-2018 年间：43,308 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD 8.0 Release Notes；Maxime Villard 博客；tech-kern 邮件列表；maxv. Add GENERIC_KASLR, only toolchain parts for now. netbsd-src 仓库 [DB/OL]. 2017-10-07T10:16:47Z. commit: 650b1fa4d5f1e80900b37549c6a3e41dbf4e4f8b；maxv. Add a new option in libsa, to load dynamic binaries. netbsd-src 仓库 [DB/OL]. 2017-10-07T10:26:38Z. commit: a8d8f69c27897a4f3e4c90cc075d9038a10d29ed；maxv. Bump bootloader version, support for booting KASLR amd64 kernels. netbsd-src 仓库 [DB/OL]. 2017-10-07T10:32:56Z. commit: d37438c8bb2c5630e82aafa11470be5c585f14e6；maxv. KASLR: add workarounds to compute the bootinfo VAs. netbsd-src 仓库 [DB/OL]. 2017-10-08T09:06:50Z. commit: 53aa2af033e38e189ca4b120c3cf110483a00d58；mortimer. Add RETGUARD to clang for amd64. openbsd-src 仓库 [DB/OL]. 2018-06-06T00:14:29Z. commit: e688c2b0648a80551cf7353d9f455c7cbb98f13c ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD. 8.0 Release Notes [EB/OL]；虚拟化生态史料。［B］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2018-2018 年间：43,308 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2018-2019)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>; NetBSD Project. NetBSD Security Officer Team — SA Release Process [EB/OL]. [2026-07-22]. <https://www.netbsd.org/support/security/>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2023-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. OpenBSD Errata Patches [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata.html>; NetBSD Project. netbsd.db — netbsd-src SA pull-up commits [DB/OL]. 2026-07-22. `SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name='netbsd-src' AND author_date>='2018-05-01' AND author_date<'2020-05-01' AND (message_subject LIKE '%SA%' OR message_subject LIKE '%pull-up%' OR message_subject LIKE '%ticket%') ORDER BY author_date ASC` ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第181章-netbsd-8.0与64位arm虚拟化 第 181 章 netbsd-8.0与64位arm虚拟化（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：13911 条 -->

### 要点（播客口述史提取）
- This is the first security bug fix update of the NetBSD 6.1 release branch.（BSD Now EP1 @ 6405.640）
- Since then it's been ported to FreeBSD, NetBSD, DragonflyBSD, and Mac OS X.（BSD Now EP35 @ 3067.179）

### 史料（播客当事人陈述）
- But it looks like they're going to be having presentations on ARM on NetBSD and FreeBSD.（BSD Now EP26 @ 328.0999）
- So next up, we have an article about the use of NetBSD（BSD Now EP16 @ 548.5599）
- And I guess next up, we also have an article about NetBSD today, and I guess they dumped（BSD Now EP22 @ 919.3599）
- trend at other conferences. So if you're a NetBSD developer, user, fan, definitely come on out and（BSD Now EP39 @ 411.2199）

### 史观（播客当事人观点与总纲映射）
- And honestly, that lack of experience with NetBSD and OpenBSD hurt my score on the（BSD Now EP21 @ 4976.139）
  → 史观映射：总纲9——经验优先

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.
- [BSD Now EP16] Pennington J. BSD Now: 16: Cryptocrystalline[EB/OL]. (2013-12-18)[2026-08-15]. https://www.bsdnow.tv/16.
- [BSD Now EP21] Pennington J. BSD Now: 21: Tendresse for Ten[EB/OL]. (2014-01-22)[2026-08-15]. https://www.bsdnow.tv/21.
- [BSD Now EP22] Pennington J. BSD Now: 22: Journaled News-Updates[EB/OL]. (2014-01-29)[2026-08-15]. https://www.bsdnow.tv/22.
- [BSD Now EP23] Pennington J. BSD Now: 23: Time Signatures[EB/OL]. (2014-02-05)[2026-08-15]. https://www.bsdnow.tv/23.
- [BSD Now EP25] Pennington J. BSD Now: 25: A Sixth pfSense[EB/OL]. (2014-02-19)[2026-08-15]. https://www.bsdnow.tv/25.
- [BSD Now EP26] Pennington J. BSD Now: 26: Port Authority[EB/OL]. (2014-02-26)[2026-08-15]. https://www.bsdnow.tv/26.
- [BSD Now EP32] Pennington J. BSD Now: 32: PXE Dust[EB/OL]. (2014-04-09)[2026-08-15]. https://www.bsdnow.tv/32.

<!-- /PODCAST_MINE -->
