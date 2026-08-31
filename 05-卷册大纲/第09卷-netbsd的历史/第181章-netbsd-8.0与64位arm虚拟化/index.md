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

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP345、BSD Now EP200、BSD Now EP141（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- NetBSD 8.2 作为 8.x 树的第三个点版本发布，聚合此前安全修复与旧硬件引导、Hyper-V、EFI 等改进。（BSD Now EP345，[81.96-118.92]，L2）
- 本期主体是 JT 征集的社区反馈：多位听众讲述从 Linux 转投 BSD 的经历，涉及 systemd 反感、PF 抗攻击、ZFS 回滚与 BSD 社区友好度。（BSD Now EP345，[1090.66-1183.78]，L2）
- 许可证争论在反馈中被表述为‘BSD 许可证是温和路径、GPL 是强制路径’的对立，主持人回应两者在自由目标上同路。（BSD Now EP345，[1188.74-1223.54]，L2）
- NetBSD announce 中 Soren Jacobsen 公告 netbsd-8 分支已创建，标志 NetBSD 8.0 发布流程启动；相比 7.0 的重大改进包括 USB 3.0 支持与含内核混音器的音频子系统重构。（BSD Now EP200，[154.14-195.94]，L2）
- 关于“scrub of death”的讨论指出：ZFS 校验和使其能发现镜像读到的坏数据，而普通 RAID 镜像无校验、无法察觉副本不同步；真正需担心的是“邪恶磁盘控制器”写错位置，ZFS 至少会检测而非返回错误数据。（BSD Now EP200，[3827.28-3924.82]，L2）
- 主持人援引 ZFS 联合创始人 Matt Ahrens 的说法：ZFS 并不比其他文件系统更需要或鼓励 ECC 内存，ECC 是可靠机器的通用要求；scrub of death 并非真实机制。（BSD Now EP200，[3933.54-4042.18]，L2）
- 该期还报道 FreeBSD 11.1 Beta 3 发布、OpenBSD 把 AMD64 汇编中的 NOP 填充改为 int3 以削弱 ROP gadget 的补丁，以及 ZFS 原生加密将先入 Linux、再经 illumos 进入 FreeBSD 的路线。（BSD Now EP200，[4148.72-5415.98]，L2）
- Ike 回顾其 BSD 入圈：九十年代末因 Linux 不合意而转向 BSD，称 FreeBSD 4.5 上下是其第一个不内核恐慌的版本；他强调当时系统管理员文化里没有开发者与非开发者之分，“你是 Unix hacker”身份鼓励他至今不取 commit bit 而以贡献补丁为日常纪律。（BSD Now EP141，[1388.00-1553.00]，L1）
- Ike 介绍其 OpenSense 工作：与日本协作者重建国际化翻译（pfSense 时期成果因许可证疑虑消失，fork 后以 PO 文件从零重来）；架构上把 OpenSense 组件从操作系统剥离，HardenedBSD 之上亦可构建；未来设想包括 RPC 管理服务、可换 OpenBSD 底座与对标商业产品的负载均衡功能。（BSD Now EP141，[1776.00-2117.00]，L1）
- Ike 以运行 ISP 时的 SSH 零日为转折点，主张任何加密组件终会被攻破，因此能够在 LibreSSL 与 OpenSSL 之间切换重启的模块化系统是关键能力，并因此构建 IPsec 之外的备用通道。（BSD Now EP141，[2242.00-2320.00]，L1）
- Ike 描述 NYCBUG 的治理哲学：非营利、无资产可争的“朋克后台”结构使组织免于内耗，每月例会以从业者演讲带动酒吧讨论；他力主让系统管理员上台分享日常，因为开发者与用户的双向反馈最有价值。（BSD Now EP141，[2427.00-2670.00]，L1）
- 新闻综述：Trendly 项目以 FreeBSD jail 加 manifest 文件方式提供预构建容器，因 GPLv3 引发社区争议后改以 MIT 再发布；NetBSD 自 OpenBSD 移植 NVMe 驱动，单设备可达读三千八百兆每秒；PC-BSD 五月镜像改用 package base 安装约四百余个包。（BSD Now EP141，[3194.00-3380.00]，L2）
- PC-BSD 侧披露的 package base 早期缺陷与处置：setuid 位在 ZFS 上丢失（pkg 1.8 修复中）、时区文件缺失、以 make distribution 变通补 /etc，以及一次 install world 覆盖 etc/passwd 导致用户被清空的事故与回滚讨论。（BSD Now EP141，[3905.00-4111.00]，L2）

**史料**：

- NetBSD 8.2 发布公告（Maya Rashish 撰写），列出安全修复与引导改进。（BSD Now EP345，[81.96-118.92]，L2）
- 听众来信中的亲身经历：Debian 防火墙受攻击、改用 OpenBSD 与 PF 后稳定、再以 FreeBSD 与 ZFS 搭存储。（BSD Now EP345，[1722.54-1828.54]，L1）
- FreeBSD 打包故事：陌生人在作者完成 Debian 打包前即已将其应用打包进 FreeBSD。（BSD Now EP345，[1257.9-1307.1]，L1）
- NetBSD announce 邮件列表 Soren Jacobsen 公告；Matt Ahrens 在 Ars Technica 评论及《ZFS 书》中的引语；OpenBSD trap sled 提交说明。（BSD Now EP200，[154.14-4042.18]，L3）
- Ike 在 AsiaBSDCon 的现场采访录音，含 OpenSense 架构路线、AWS 云构建经历与 Steve Bourne 周末偷换 BSD 的轶事引述。（BSD Now EP141，[2372.00-2410.00]，L1）
- Trendly 的许可证讨论串与改 MIT 的再发布记录、DragonFly Bay Trail C6/C7 挂死修复帖，均为可追溯的原始链接材料。（BSD Now EP141，[3324.00-3380.00]，L2）

**史观**：

- 总纲6 和解优于斗争：总纲6 和解优于斗争：听众与主持人共同主张 Linux 与 BSD 目标相同、应减少阵营内耗，以展示各自优势代替互相贬低。（BSD Now EP345，[1151.7-1183.78]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：对 Linux 与 BSD 的许可证、社区规模比较被归结为不同哲学路径，而非优劣高下。（BSD Now EP345，[1188.74-1223.54]，L2）
- 总纲9 经验优先：“scrub of death”被澄清为对 ZFS 数据完整性机制的误解，当事人 Matt Ahrens 的一手说明优先于流传的恐惧叙事，体现经验与考据对传闻的修正。（BSD Now EP200，[3933.54-4042.18]，L2）
- 总纲6 和解优于斗争：OpenSense 从 pfSense 分叉后不与母项目对抗而是按自身路线重建（国际化、架构解耦），Ike 视上游化与模块化为把对抗转为并行的做法。（BSD Now EP141，[1955.00-2020.00]，L1）
- 总纲5 没有必然性，只有偶然性：Ike 的 pfSense 日语翻译成果因上游许可证工具变动而一夜归零，OpenSense 分叉才使其重见天日——技术存续取决于许可证与组织结构的偶然事件而非代码本身优劣。（BSD Now EP141，[1805.00-1848.00]，L1）

**辨析**：

- 转写中多名写信人姓名与内容混杂（如‘Jason’ 与‘Jamie’ 指代可能互换），引用社区反馈时须以原邮件为准。　[存疑脚注] 转写写信人姓名存疑（BSD Now EP345，[1113.94-1225.54]，L4）
- Trendly 改 MIT 的直接动因是社区对 GPLv3 与“基于 FreeBSD”宣传相悖的批评，节目归功于外部贡献尚少使再许可可行，但这只是主持人推断，项目方动机未经当事人证实。　[存疑脚注] 改许可证的确切决策过程与时间点未见一手声明（BSD Now EP141，[3347.00-3377.00]，L4）

**文献**：

- [BSD Now EP345] Pennington J. BSD Now: 345: Switchers to BSD[EB/OL]. (2020-04-09)[2026-08-15]. https://www.bsdnow.tv/345.
- [BSD Now EP200] Pennington J. BSD Now: 200: Getting Scrubbed to Death[EB/OL]. (2017-06-28)[2026-08-15]. https://www.bsdnow.tv/200.
- [BSD Now EP141] Pennington J. BSD Now: 141: BSD Likes Ike![EB/OL]. (2016-05-11)[2026-08-15]. https://www.bsdnow.tv/141.

<!-- /PODCAST_REVIEW -->
