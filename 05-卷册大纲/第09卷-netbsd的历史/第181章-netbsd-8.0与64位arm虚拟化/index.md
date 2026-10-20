---
chapter: 第 181 章
id: CH181
volume: 第09卷-netbsd的历史
---

# 第 181 章 netbsd-8.0与64位arm虚拟化

## 要点

- NetBSD 8.0（**2018.7**）引入 aarch64（ARM64）支持，由 Ryo Shimizu 等推动；~~开发历时 3 年（2015-2018）~~（经 netbsd.duckdb 验证：aarch64 后端最早由 joerg 于 2013-02-04 引入 LLVM/Clang AArch64 后端，实际开发周期约 5 年 2013-2018）；〔待核：原文截断，后文待回源〕
- NVMM 设计文档由 Maxime Villard 撰写，散见于 man **nvmm(4)**、tech-virt 邮件列表、Villard 个人博客；源码考据需对照 CVS commit log 与 Villard 的 commit 署名；考据需注意 NVMM 在 8.0 之后的持续演进
- NetBSD 8.0（**2018.7**）引入 KASLR（Kernel Address Space Layout Randomization）内核安全特性；旧内核无 KASLR，存在固定地址空间布局的攻击面；KASLR 由 Maxime Villard 实现；此改进让 NetBSD 在内核安全上追赶 OpenBSD，体现 “在虚假中寻找仅存的真实”。〔待核：原文截断，后文待回源〕
- 2018 年 ARM64 虚拟化成竞争点：Linux KVM 在服务器领先，FreeBSD bhyve 偏 x86，NetBSD 8.0 推 ARM64 虚拟化 + SMP，OpenBSD 6.3 安全利基，Windows Hyper-V 守企业 x86；NetBSD 8.0 以“ARM64 虚拟化 + 多核”强化可移植哲学的现代延伸。
- 8.x 周期 NetBSD Security Officer Team 的 15 个 SA 在数量、节奏、覆盖面三个维度呈现“过渡期”特征——年化速率约 7.5 SA/年（2018 年 9 个、2019 年 6 个），高于 9.x 周期的约 3.6 SA/年，反映 8.0 新代码引入的攻击面集中暴露；〔待核：原文截断，后文待回源〕

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

- NetBSD aarch64 支持与 Linux aarch64 支持的成熟度对比缺乏权威基准。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：aarch64 后端最早于 2013.2.4 由 joerg 引入（LLVM/Clang snapshot r174288），AARCH64 定义于 2013.10.29 由 matt 添加，远早于 8.0 发布 2018.7
- Villard 的 commit 在 CVS 与 Git 仓库中的署名可能略有差异——需对照多源核验；NVMM 在 9.0/10.0 的具体改进需考据
- 8.0 KASLR 是否默认启用在不同叙事中存在分歧——需对照源码核验。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：KASLR 首次引入时间为 2017-10-07（maxv commit 650b1fa4d5f1e80900b37549c6a3e41dbf4e4f8b“Add GENERIC_KASLR, only toolchain parts for now”
- 虚拟化市场由云生态主导，NetBSD 8.0 在嵌入式/教育利基具价值。
- **数量对比的辨析**：8.x 周期 15 个 SA（年化 7.5 SA/年）与 9.x 周期 18 个 SA（年化 3.6 SA/年）的对比须考虑三个因素：其一，8.x 周期时间窗约 2 年，9.x 周期约 5 年，年化速率差异反映 8.0 新代码攻击面集中暴露；其二，8.x 周期 4 个网络栈 SA（SA2018-003/004/006/007）是 8.0 IPv6/IPsec 改进伴随的攻击面

## 文献

- man **nvmm(4)**；tech-virt 邮件列表；Maxime Villard 博客 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2018-2018 年间：43,308 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 8.0 Release Notes；Maxime Villard 博客；tech-kern 邮件列表；maxv. Add GENERIC_KASLR, only toolchain parts for now. netbsd-src 仓库 [DB/OL]. 2017-10-07T10:16:47Z. commit: 650b1fa4d5f1e80900b37549c6a3e41dbf4e4f8b；maxv. Add a new option in libsa, to load dynamic binaries. netbsd-src 仓库 [DB/OL]. 2017-10-07T10:26:38Z. commit: a8d8f69c27897a4f3e4c90cc075d9038a10d29ed；maxv. Bump bootloader version, support for booting KASLR amd64 kernels. netbsd-src 仓库 [DB/OL]. 2017-10-07T10:32:56Z. commit: d37438c8bb2c5630e82aafa11470be5c585f14e6；maxv. KASLR: add workarounds to compute the bootinfo VAs. netbsd-src 仓库 [DB/OL]. 2017-10-08T09:06:50Z. commit: 53aa2af033e38e189ca4b120c3cf110483a00d58；mortimer. Add RETGUARD to clang for amd64. openbsd-src 仓库 [DB/OL]. 2018-06-06T00:14:29Z. commit: e688c2b0648a80551cf7353d9f455c7cbb98f13c ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD. 8.0 Release Notes [EB/OL]；虚拟化生态史料。［B］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2018-2018 年间：43,308 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2018-2019)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>; NetBSD Project. NetBSD Security Officer Team — SA Release Process [EB/OL]. [2026-07-22]. <https://www.netbsd.org/support/security/>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2023-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. OpenBSD Errata Patches [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata.html>; NetBSD Project. netbsd.duckdb — netbsd-src SA pull-up commits [DB/OL]. 2026-07-22. `SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name='netbsd-src' AND author_date>='2018-05-01' AND author_date<'2020-05-01' AND (message_subject LIKE '%SA%' OR message_subject LIKE '%pull-up%' OR message_subject LIKE '%ticket%') ORDER BY author_date ASC` ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP345、BSD Now EP200（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- NetBSD 8.2 作为 8.x 树的第三个点版本发布，聚合此前安全修复与旧硬件引导、Hyper-V、EFI 等改进。（BSD Now EP345，[81.96-118.92]，L2）
- 本期主体是 JT 征集的社区反馈：多位听众讲述从 Linux 转投 BSD 的经历，涉及 systemd 反感、PF 抗攻击、ZFS 回滚与 BSD 社区友好度。（BSD Now EP345，[1090.66-1183.78]，L2）
- 许可证争论在反馈中被表述为‘BSD 许可证是温和路径、GPL 是强制路径’的对立，主持人回应两者在自由目标上同路。（BSD Now EP345，[1188.74-1223.54]，L2）
- NetBSD announce 中 Soren Jacobsen 公告 netbsd-8 分支已创建，标志 NetBSD 8.0 发布流程启动；相比 7.0 的重大改进包括 USB 3.0 支持与含内核混音器的音频子系统重构。（BSD Now EP200，[154.14-195.94]，L2）
- 关于“scrub of death”的讨论指出：ZFS 校验和使其能发现镜像读到的坏数据，而普通 RAID 镜像无校验、无法察觉副本不同步；真正需担心的是“邪恶磁盘控制器”写错位置，ZFS 至少会检测而非返回错误数据。（BSD Now EP200，[3827.28-3924.82]，L2）
- 主持人援引 ZFS 联合创始人 Matt Ahrens 的说法：ZFS 并不比其他文件系统更需要或鼓励 ECC 内存，ECC 是可靠机器的通用要求；scrub of death 并非真实机制。（BSD Now EP200，[3933.54-4042.18]，L2）
- 该期还报道 FreeBSD 11.1 Beta 3 发布、OpenBSD 把 AMD64 汇编中的 NOP 填充改为 int3 以削弱 ROP gadget 的补丁，以及 ZFS 原生加密将先入 Linux、再经 illumos 进入 FreeBSD 的路线。（BSD Now EP200，[4148.72-5415.98]，L2）

**史料**：

- NetBSD 8.2 发布公告（Maya Rashish 撰写），列出安全修复与引导改进。（BSD Now EP345，[81.96-118.92]，L2）
- 听众来信中的亲身经历：Debian 防火墙受攻击、改用 OpenBSD 与 PF 后稳定、再以 FreeBSD 与 ZFS 搭存储。（BSD Now EP345，[1722.54-1828.54]，L1）
- FreeBSD 打包故事：陌生人在作者完成 Debian 打包前即已将其应用打包进 FreeBSD。（BSD Now EP345，[1257.9-1307.1]，L1）
- NetBSD announce 邮件列表 Soren Jacobsen 公告；Matt Ahrens 在 Ars Technica 评论及《ZFS 书》中的引语；OpenBSD trap sled 提交说明。（BSD Now EP200，[154.14-4042.18]，L3）

**史观**：

- 总纲6 和解优于斗争：总纲6 和解优于斗争：听众与主持人共同主张 Linux 与 BSD 目标相同、应减少阵营内耗，以展示各自优势代替互相贬低。（BSD Now EP345，[1151.7-1183.78]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：对 Linux 与 BSD 的许可证、社区规模比较被归结为不同哲学路径，而非优劣高下。（BSD Now EP345，[1188.74-1223.54]，L2）
- 总纲9 经验优先：“scrub of death”被澄清为对 ZFS 数据完整性机制的误解，当事人 Matt Ahrens 的一手说明优先于流传的恐惧叙事，体现经验与考据对传闻的修正。（BSD Now EP200，[3933.54-4042.18]，L2）

**辨析**：

- 转写中多名写信人姓名与内容混杂（如‘Jason’ 与‘Jamie’ 指代可能互换），引用社区反馈时须以原邮件为准。 [存疑脚注] 转写写信人姓名存疑（BSD Now EP345，[1113.94-1225.54]，L4）

**文献**：

- [BSD Now EP345] Pennington J. BSD Now: 345: Switchers to BSD[EB/OL]. (2020-04-09)[2026-08-15]. <https://www.bsdnow.tv/345>.
- [BSD Now EP200] Pennington J. BSD Now: 200: Getting Scrubbed to Death[EB/OL]. (2017-06-28)[2026-08-15]. <https://www.bsdnow.tv/200>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Bluetooth. SIG. Bluetooth BR/EDR Security Vulnerability [EB/OL]. (2019)[2026-07-22]. <https://www.bluetooth.com/security/>[EB/OL]. 2019. ［待核·needs_fix］［DKC-2443→fulltext:6190］
<!-- /dangan-20260908 -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-266 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-266`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：讲者自二零零九年起担任 NetBSD 提交者，致力于构建更快启动的微虚拟机。（YouTube EP6znKosuX3EM，[136.67-142.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-539 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-539`；w172 YouTube 章节路由采纳）

据〔NetBSD 8.0 前瞻（会议不详，推测）〕讲者口述：讲者明确表示并未纳入 HAMMER 文件系统，其中一个原因是它涉及 VFS 层的改动。（YouTube EPG9tqr9LlnHY，[996.579-1009.079]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3021 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3021`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Virtual Host Swapping: David Gilbert〕讲者口述：以 FreeBSD 为宿主、Windows 10 为客体的 bhyve 方案尚不完全适合生产，只能应急使用；讲者听说 FreeBSD 13 会带来更好的 bhyve 磁盘性能。（YouTube EPAt6vmxbi2co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3022 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3022`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Virtual Host Swapping: David Gilbert〕讲者口述：在 Windows 宿主的 Hyper-V 下，虚拟化层只支持整块裸盘而不支持分区，因此 FreeBSD 安装必须占用一块单独的磁盘。（YouTube EPAt6vmxbi2co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3023 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3023`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Virtual Host Swapping: David Gilbert〕讲者口述：Hyper-V 的 TRIM 并未直通到宿主磁盘硬件——文档写作 supported，实际仅指以磁盘文件模拟时的块回收，并非把 TRIM 传给物理盘。（YouTube EPAt6vmxbi2co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3024 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3024`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Virtual Host Swapping: David Gilbert〕讲者口述：在 FreeBSD 12.1 上以 bhyve 运行 Windows，即便宿主空闲，启动也明显更慢；讲者怀疑虚拟磁盘设备层尚有改进空间。（YouTube EPAt6vmxbi2co，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
