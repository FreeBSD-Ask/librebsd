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
- 从项目史观总纲审视，FreeBSD 社区发展史的批评、反批评与再批评各方（外部批评者、Core Team 阵营、内部异议者、商业公司 committer、社区普通用户、CoC 支持者与反对者）在本体论上地位相等——其一，偶然性视角（总纲第 5 条“没有必然性，只有偶然性”）：Core Team 选举制的代际共识、CoC 于 2020-06-09 引入、committer 权限撤销程序的“18 个月

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

- NIST CMVP；Common Criteria Portal；The Open Group Registry；FedRAMP Marketplace[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- NEWREF:2638 --><!-- NEWREF:2639 --><!-- NEWREF:2640 --><!-- NEWREF:2641 --><!-- NEWREF:2642 --><!-- NEWREF:2643 --><!-- 2026-08-05 补：Schrems I/II（C-362/14、C-311/18）+ GDPR 全文 + DPC v. Facebook（IEHC 545）+ 2 CJEU 新闻稿 --><!-- NEWREF:2644 --><!-- NEWREF:2645 --><!-- 2026-08-05 补：CJEU 官方新闻稿 PR 117/15（Schrems I）、PR 91/20（Schrems II）作为第二渠道凭证 -->
- 统计； 调查 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- 本项目 index.md 体例说明“多元群体贡献强制要求”；bsd_commits.db。 ［A］
- 各社区治理文档 Archive[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- 项目史观总纲第 5、8、13、19 条；FreeBSD Core Team Election Results Core.13（同 140.27a）；FreeBSD Code of Conduct 官方页面（同 140.27a）；FreeBSD Core Team bylaws（同 140.27a）；FreeBSD Foundation 年报；bsd_commits.db freebsd-src 仓库 committer 地理分布；第 140.27.1-140.27.4、140.27a、140.27b、140.27c 节辩证链补足；参见相关章节 Core Team 选举制度、committers 机制、商业公司与社区关系、社区多样性批评部分史料 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2003-2026 年间：1,102,265 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
