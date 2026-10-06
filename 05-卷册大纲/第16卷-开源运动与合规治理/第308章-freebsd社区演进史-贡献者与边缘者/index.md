---
chapter: 第 308 章
id: CH308
volume: 第16卷-开源运动与合规治理
---

# 第 308 章 freebsd社区演进史-贡献者与边缘者

## 要点

- FreeBSD 不持有 FIPS 140、Common Criteria、UNIX 03、FedRAMP 等形式认证，但可作为运行环境被列入证书，叙事中须明确区分“FreeBSD 作为运行环境被列入证书”与“FreeBSD 持有证书”两类事实
- 非 committer 补丁平均审核 45 天（2023），committer 为即时。约 60% 外部贡献者在首次提交后 6 个月内不再贡献。改进方案：贡献者积分、CI pre-commit、导师配对。
- 本章对“多元群体贡献”的专章书写本身须自反——在贡献发生的当下，贡献者并不以“少数族裔”“女性”“儿童”“不同信仰者”等标签自我定位，标签是史家事后对提交记录的形式主义化归类；将一群本以“开发者/维护者”身份协作的人重新切分为六类“多元群体”，既是为纠正“英雄叙事”偏差的努力，也可能在强调“差异”的同时反而固化了差异本身。FreeBSD 的贡献史首先是技术协作史，六类标签只是对其全球性与异质性的事
- 各社区治理文档是评估治理模式的关键史料，需交叉验证
-  5 条“没有必然性，只有偶然性”）：Core Team 选举制的代际共识、CoC 于 2020-06-09 引入、committer 权限撤销程序的“18 个月自动退休”条款皆偶然地塑造了 FreeBSD 社区发展的具体形态——Core Team 选举制源于 2000 年前后 FreeBSD 社区对治理结构形式化的偶然选择（而非开源社区治理的必然演化）

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10430] BSD Now 第 676 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10439] BSD Now 第 675 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10444] BSD Now 第 674 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10456] BSD Now 第 671 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10459] BSD Now 第 670 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10464] BSD Now 第 668 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10468] BSD Now 第 667 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10474] BSD Now 第 666 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10486] BSD Now 第 665 期，匹配 CH308 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10492] BSD Now 第 664 期，匹配 CH308 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 须严格遵循 0 信任原则，证书编号、发布日期等须经 NIST CMVP、IEEE Xplore、The Open Group、EUR-Lex 等权威来源交叉验证；不得模糊表述 FreeBSD 的认证状态
- 本书对六类群体的书写以“可考据者书之、不可考据者缺之”为铁律，绝不臆造；信息缺口声明（女性/儿童/信仰三类）恰是 0 信任原则的体现，而非叙事失败。
- 项目统摄史观审视不意味着价值中立——史家仍须呈现各方的具体效应（如 Core.13 选举的具体过程、CoC 引入后的社区活跃度变化、committer 权限撤销的具体案例），但不得以“Core Team 优于外部批评者”或“外部批评者优于 Core Team”的前理解预先判定；【0 信任原则·本体论平等的非相对主义】本体论平等不意味着所有立场无差别，而是意味着差异是一刻状态的不同而非本体等级的高下

## 文献

- NIST CMVP；Common Criteria Portal；The Open Group Registry；FedRAMP Marketplace［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］<!-- NEWREF:2638 --><!-- NEWREF:2639 --><!-- NEWREF:2640 --><!-- NEWREF:2641 --><!-- NEWREF:2642 --><!-- NEWREF:2643 --><!-- 2026-08-05 补：Schrems I/II（C-362/14、C-311/18）+ GDPR 全文 + DPC v. Facebook（IEHC 545）+ 2 CJEU 新闻稿 --><!-- NEWREF:2644 --><!-- NEWREF:2645 --><!-- 2026-08-05 补：CJEU 官方新闻稿 PR 117/15（Schrems I）、PR 91/20（Schrems II）作为第二渠道凭证 -->
- 统计； 调查 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 本项目 index.md 体例说明“多元群体贡献强制要求”；bsd_commits.db。 ［A］
- 各社区治理文档 Archive［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- 项目史观总纲第 5、8、13、19 条；FreeBSD Core Team Election Results Core.13（同 140.27a）；FreeBSD Code of Conduct 官方页面（同 140.27a）；FreeBSD Core Team bylaws（同 140.27a）；FreeBSD Foundation 年报；freebsd.duckdb freebsd-src 仓库 committer 地理分布；第 140.27.1-140.27.4、140.27a、140.27b、140.27c 节辩证链补足；参见相关章节 Core Team 选举制度、committers 机制、商业公司与社区关系、社区多样性批评部分史料 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP373（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 访谈对象 Kyle Evans 因课程同学使用 FreeBSD 而入坑，从 bsdgrep 的 GSoC 项目开始参与 FreeBSD 开发，后当选 Core 团队成员。（BSD Now EP373，[163.48-233.53]，L1）
- bsdgrep 源自 2011 年前后的 GSoC 项目，旨在替换 base 中的 GNU grep；其难点在于需保持与 GNU 扩展及既有脚本依赖的 bug 兼容。（BSD Now EP373，[216.33-426.70]，L1）
- flua 是 base 中专用的 Lua 解释器，避免与 ports 中的 Lua 冲突；引导装载器由 Forth 转 Lua 后，boot 环境菜单等逻辑更易维护。（BSD Now EP373，[517.11-657.27]，L1）
- bectl 源自 GSoC 项目，用于管理 ZFS 引导环境；ZFS Boot CFG 进入上游 OpenZFS 后成为一等特性，可在 UEFI 下工作。（BSD Now EP373，[828.43-1009.87]，L1）
- certctl 将 Mozilla 根证书束纳入 base，使 FreeBSD 12.2 的新装系统默认具备 SSL 信任库，并可增删或拉黑证书。（BSD Now EP373，[1208.75-1317.09]，L1）

**史料**：

- Kyle Evans 本人口述其参与 bsdgrep、flua、bectl、certctl 与 Core 团队的经过。（BSD Now EP373，[163.48-1933.73]，L1）
- 访谈提及 Warner Losh 引入 Lua 脚本、Alan Jude 作为 GSoC 导师等当事人协作细节。（BSD Now EP373，[522.88-867.89]，L1）

**史观**：

- 总纲10 动手者创造历史：Kyle 以“找让自己不舒服的问题”为切入点，从具体缺陷入手参与系统开发，体现动手者以具体工程推动项目。（BSD Now EP373，[1604.00-1770.17]，L1）
- 总纲9 经验优先：访谈强调通过实际项目学习并建立人际网络以获取经验，而非单纯阅读文档。（BSD Now EP373，[1639.55-1710.47]，L1）

**辨析**：

- bsdgrep 尚未完整支持 GNU 扩展，替换 base 中 GNU grep 的时机与兼容性范围仍待评估。　[存疑脚注] GNU 扩展兼容范围待核实（BSD Now EP373，[394.32-426.70]，L4）

**文献**：

- [BSD Now EP373] Pennington J. BSD Now: 373: Kyle Evans Interview[EB/OL]. (2020-10-22)[2026-08-15]. <https://www.bsdnow.tv/373>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

