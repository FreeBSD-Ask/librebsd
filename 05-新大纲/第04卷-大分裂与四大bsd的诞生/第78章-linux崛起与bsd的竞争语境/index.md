---
chapter: 第 78 章
id: CH78
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 78 章 linux崛起与bsd的竞争语境

## 要点

- Linux Kernel 仓库共 1474341 次提交（1970-01-01 至 2026-08-24），33601 位贡献者，贡献者数是 FreeBSD 的 9 倍，反映 Linux 生态规模优势

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4362] 卷“第04卷-大分裂与四大bsd的诞生”第 78 章，匹配置信度 0.9，原因：本文以 Raymond《大教堂与集市》为靶，批判集市（Linux）模式、哀叹 Unix 大教堂（BSD/UNIX）没落，直接切入本章“Linux vs BSD”的竞争语境；作者为 FreeBSD 核心开发者，属一手史料。

- [DB:code_repos:linux-kernel.duckdb] Linux Kernel 仓库共 1474341 次提交（1970-01-01 至 2026-08-24），33601 位贡献者，贡献者数是 FreeBSD 的 9 倍，反映 Linux 生态规模优势
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 78.7-关键词行级挖掘素材线索（19 条，CL-RM 段，见 78.7-关键词行级挖掘素材线索.md）

## 史观

- 循环而非进步：Linux 与 BSD 的竞争不是谁胜谁负，而是分离-聚合的循环；多方平等：在本体论层面平等对待两者

## 辨析

- 史料来源的代表性是核心辨析点——外部叙事（Salus 1994）与内部叙事（Raymond 1999、McKusick 1999）的权重须区别对待，外部叙事采信度高于内部叙事
- 辨析的具体维度经 GPL 与 BSD 许可证原文、Linux 内核贡献统计与 BSD 衍生产品统计交叉验证——GPL 聚拢效应在 “贡献回流” 维度有据可循，BSD 散逸效应在 “商业产品使用” 维度有据可循，二者非对立而是不同许可证哲学的体现
- 梗的真实性在 “市场份额” 维度有据可循（Netcraft 服务器统计显示 FreeBSD 在 Web 服务器市场占比 2000 年约 6%、2010 年约 3%，确有下滑），但在 “BSD 是否真的在消亡” 维度存在夸大——FreeBSD 在 CDN（Netflix Open Connect 2007 年起基于 FreeBSD，且 Netflix 致力与主线 FreeBSD 保持零差分）、路由器（Juniper JunOS 经典版自 1998 年 7 月首版起基于 FreeBSD，其改进持续回馈 FreeBSD 主线）、存储（Isilon/NetApp ONTAP GX、TrueNAS）与游戏主机（Sony PlayStation 4/5 运行 FreeBSD 改良版）等关键基础设施领域持续承载真实负载——份额下滑与生态承重并存，“消亡论”在后者维度不成立
- BSD 劣势的 “已发生” 维度有据可循（386BSD 维护停顿、FreeBSD 1994.11.22 重建后仍需追赶 Linux 1.0 1994.3 的 8 个月窗口），但在 “被夸大” 维度须谨慎——FreeBSD 在服务器市场（Yahoo、Hotmail 后端 1990 年代后期使用 FreeBSD）、CDN（Netflix Open Connect 2007 年起，承载北美高峰时段相当份额的流量）、骨干路由（Juniper JunOS 经典版）等场景的实际承重仍具规模，“劣势被夸大”的判断在这些承重证据上有据可循，但引用时须注明承重场景与市场份额下滑可以并存
- 诉讼后果的归因在 “直接后果” 维度有共识（18 个月窗口期 1992.12-1994.1 由 USL v. BSDi 诉讼档案直接证实），但在 “长期影响” 维度存在分歧——部分归因于诉讼（BSDi 1994 年起法律费用与和解成本拖累商业发展），部分归因于许可证（BSD 散逸效应使商业公司无法构建 GPL 式贡献循环），部分归因于组织（BSD Core Team 精英治理模式在 1990 年代决策带宽有限、缺乏 Linux 基金会式的全职维护人机制，三项目分治亦分散了工程资源）——三重归因各自部分成立且相互纠缠，单独任何一维都不足以完整解释 1990 年代后期的格局变化，正式引用时须并列呈现而非择一采信

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 linux-kernel.duckdb

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-735 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-735`；w172 YouTube 章节路由采纳）

据〔Migrating to FreeBSD from a Linux sysadmins perspective 报告（来源不详）〕讲者 Albert Dengg 口述：他已将若干系统迁至 FreeBSD 或 FreeBSD 衍生产品，如 pfSense。（YouTube EPlPS6bffVQkI，[238.04-247.43]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->
