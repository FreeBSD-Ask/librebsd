---
chapter: 第 186 章
id: CH186
volume: 第09卷-netbsd的历史
---

# 第 186 章 netbsd社区治理与事件考据

## 要点

- NetBSD Top 5 贡献者：wiz(222791)、adam(71900)、taca(66560)、christos(58421)、joerg(57785)

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4000] 卷“第09卷-netbsd的历史”第 186 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:netbsd.duckdb] NetBSD Top 5 贡献者：wiz(222791)、adam(71900)、taca(66560)、christos(58421)、joerg(57785)

## 史观

- 多方平等：NetBSD 核心团队的高度集中与‘开源民主’神话形成张力

## 辨析

- 文化对照易陷入刻板印象，需以具体事件与一手史料为依据。L3.7.1 查询基于 message_subject LIKE 匹配社区文化相关关键词（如“community”“culture”“foundation”“bylaw”“election”等），1993-2022 年的 commit 数字均为下限，实际涉及社区文化的 commit 可能更多；社区文化 commit 量从 79 降至 43 的下
- formal.html 旧链接（people/formal.html）已 404（2026-08-06 验证），用 releases/formal.html 替代；本次归档为 2026-08-06 时点快照，后续 Foundation 页面变动不影响本节考据（本地档案为准）；2025.txt 为年度大会纪要（IRC 记录文本），含 Board/Core/releng 等团队报告，是 2026 年治
- 复核关键词覆盖 mercurial/Migration/migrate/anonhg/cvs to hg 等 13 个变体，2019-2020 共 24 个月份全量检索；2020-04 与 2020-08 两处命中均非迁移公告，判定“无迁移完成公告”成立；局限——netbsd-announce 之外的列表（tech-repository、source-changes）未纳入本次检索，迁移公告可能发

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 netbsd.duckdb

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP352（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 本期主话题是 NetBSD 内核对随机数生成机制的重写，目标是把熵池升级到满足 256 位不可预测性等新期望。（BSD Now EP352，[182.96-190.12]，L2）
- 主持人的核心判断是：随机数在操作系统中多处不可或缺，现代系统通常把 RD-RAND、RD-SEED 等硬件输出与哈希混合，单一熵源失效不应击穿整个系统。（BSD Now EP352，[159.08-178.48]，L2）
- 新闻部分记载 NetBSD core team 人事变动：Matt Thomas 在服务十余年后卸任，Robert Elz 受邀加入；同期 FreeBSD core team 进行两年一度的民主选举。（BSD Now EP352，[764.8-901.42]，L2）

**史料**：

- NetBSD rnd(4) 手册页及其引用的随机性论文，节目提示可阅读 rnd(4) 了解熵源设计。（BSD Now EP352，[448.56-454.56]，L2）
- NetBSD 公告邮件列表中 Alistair Crooks 发布的 core team 变更公告，记载 Matt Thomas 的 ELF、VAX 维护与 GCC 贡献。（BSD Now EP352，[764.8-788.16]，L2）
- Bill Joy 1999 年 Linux Magazine 采访与 2003 年离任 Sun 时的报道，提及 BSD Unix、NFS、UltraSPARC、Java 与 1976 年创作的 vi。（BSD Now EP352，[1860.4-1891.92]，L3）

**史观**：

- 总纲10 动手者创造历史：总纲10 动手者创造历史：Matt Thomas、Robert Elz 等长期维护 ELF、VAX、shell 与 POSIX 的动手者构成社区治理的实质基础。（BSD Now EP352，[764.8-810.32]，L2）
- 总纲9 经验优先：总纲9 经验优先：开发者对 Allwinner ARM 真随机数设备实测统计测试，发现输出高度偏置，遂以经验判定不能仅依赖该硬件熵源。（BSD Now EP352，[366.88-377.24]，L2）

**辨析**：

- 转写中‘Robert Ells’ 疑为 Robert Elz，写作时须以 cross_indexes.duckdb 译名表校正，不宜直接照搬语音转写。 [存疑脚注] 转写人名拼写存疑（BSD Now EP352，[764.8-800.48]，L4）
- 转写中‘Rastrad’ 等拼写疑指 NetBSD 开发者 Riastradh（Taylor R Campbell），其 Allwinner RNG 驱动与统计测试的准确姓名需另核。 [存疑脚注] 转写人名拼写存疑（BSD Now EP352，[366.88-377.24]，L4）

**文献**：

- [BSD Now EP352] Pennington J. BSD Now: 352: Introducing Randomness[EB/OL]. (2020-05-28)[2026-08-15]. <https://www.bsdnow.tv/352>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-485 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-485`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Taylor Campbell 口述：FreeBSD 有 devfs，其工作方式与传统 Unix 及其他 BSD 不同。（YouTube EPf7Kgzd2HwD8，[2408.079-2412.79]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1502 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1502`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Taylor R Campbell，EuroBSDcon 2023《How to get started hacking NetBSD》〕讲者口述：2008 年他复现出一个 NetBSD 内核 bug 后，在 netbsd-users 邮件列表上提出一行改动，几天之内由 Christos Zoulas 合入；这是他首次向 NetBSD 内核提交修改。（YouTube EPgm-F3GnM8yM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1503 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1503`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Taylor R Campbell，EuroBSDcon 2023《How to get started hacking NetBSD》〕讲者口述：他接着尝试让 Broadcom 旧款 Wi-Fi 驱动在 PowerBook G4“Extreme”上工作，耗时约两个月，做法是把 OpenBSD 的代码抄过来，并以 DragonFly 的代码作参照，最终于 2008 年 9 月跑通。（YouTube EPgm-F3GnM8yM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1504 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1504`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Taylor R Campbell，EuroBSDcon 2023《How to get started hacking NetBSD》〕讲者口述：NetBSD 的 build.sh 先构建交叉编译工具链、再用该工具链构建目标系统，因此“每一次构建都是交叉构建”，使构建与主机环境隔离；在 macOS、OpenBSD、Linux 等任何接近 POSIX 的系统上，不必先安装 NetBSD 即可开发。（YouTube EPgm-F3GnM8yM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1505 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1505`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Taylor R Campbell，EuroBSDcon 2023《How to get started hacking NetBSD》〕讲者口述：NetBSD 的 rump 可在用户态进程中运行内核代码（线程、设备驱动、文件系统），项目的文件系统测试全部跑在 rump 内，他据此在用户态配 GDB 调试，并修好了 rename 系统调用。（YouTube EPgm-F3GnM8yM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2042 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2042`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD TV 录制 BSDCan 纽约站 Jeff Rizzo 演讲 Releasing NetBSD: So Many Targets, So Little Time〕讲者口述：NetBSD 5（2009 年发布）支持 55 个平台，NetBSD 6 约在一年零半年后发布时支持 60 个平台，开发中的 NetBSD 7 则为 66 个平台构建。（YouTube EP4bPduH6O7lI，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2043 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2043`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD TV 录制 BSDCan 纽约站 Jeff Rizzo 演讲 Releasing NetBSD: So Many Targets, So Little Time〕讲者口述：答问中有人问 NetBSD 是否为首个支持 AMD64 的平台，讲者确认是。（YouTube EP4bPduH6O7lI，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2044 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2044`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD TV 录制 BSDCan 纽约站 Jeff Rizzo 演讲 Releasing NetBSD: So Many Targets, So Little Time〕讲者口述：NetBSD 历来被呈现为“最可移植”，但讲者认为这一标签并未充分点出可移植性的具体价值，其价值主要在于支撑可移植性的稳健工程实践，例如保持代码质量。（YouTube EP4bPduH6O7lI，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2045 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2045`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSD TV 录制 BSDCan 纽约站 Jeff Rizzo 演讲 Releasing NetBSD: So Many Targets, So Little Time〕讲者口述：至 2014 年 NetBSD 仍使用 CVS 作版本控制，讲者称它对一些用途而言有些年头了，但运行得很好。（YouTube EP4bPduH6O7lI，ASR）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-19 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2786 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2786`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔NetBSD and Mercurial: The challenges of a long history〕讲者口述：NetBSD 是现存最大最老的 CVS 仓库之一，迁到现代版本控制系统的动机由此而来。（YouTube EP6i6CirmO0Gs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2787 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2787`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔NetBSD and Mercurial: The challenges of a long history〕讲者口述：讲者回望自 CVS 起步的二十五年，并讲 NetBSD 与 Mercurial 的现状——与 Mercurial 开发者协作修问题、以及将来可能的走向；其经验对想摆脱 subversion 的其他大项目（如 FreeBSD）同样适用。（YouTube EP6i6CirmO0Gs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3258 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3258`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2019 - Core Team March Report 讲者口述：项目长期设有工作组：早年由成员自我组织，TCP 传输工作组与 Capsicum 工作组多年前即已组建，各领域成员以定期电话会议相互协调。（YouTube EPieLN_5j7G1g，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3259 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3259`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2019 - Core Team March Report 讲者口述：本任 core 团队着力提升透明度：不少成员是打着透明旗号当选的，团队从与上一任 core 的交接会议做起，公开会议记录并发布月度报告。（YouTube EPieLN_5j7G1g，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3260 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3260`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2019 - Core Team March Report 讲者口述：行为准则更新上，团队认为不必从零重写，转而参考转写音作 GoLang 与 LLVM 的行为准则，由讲者裁剪出一个适合本项目的版本，自去年 10 月或 11 月起停留于此；讲者坦言进展不如预期。（YouTube EPieLN_5j7G1g，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3261 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3261`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2019 - Core Team March Report 讲者口述：core 报告称当周刚发出开发者版问卷，其起点是转写音作 Eurovison Econ 2018 的一次聚会，与会者当时拟出了问卷初稿。（YouTube EPieLN_5j7G1g，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
