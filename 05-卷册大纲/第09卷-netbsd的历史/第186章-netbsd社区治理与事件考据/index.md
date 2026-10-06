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

- 转写中‘Robert Ells’ 疑为 Robert Elz，写作时须以 cross_indexes.duckdb 译名表校正，不宜直接照搬语音转写。　[存疑脚注] 转写人名拼写存疑（BSD Now EP352，[764.8-800.48]，L4）
- 转写中‘Rastrad’ 等拼写疑指 NetBSD 开发者 Riastradh（Taylor R Campbell），其 Allwinner RNG 驱动与统计测试的准确姓名需另核。　[存疑脚注] 转写人名拼写存疑（BSD Now EP352，[366.88-377.24]，L4）

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

