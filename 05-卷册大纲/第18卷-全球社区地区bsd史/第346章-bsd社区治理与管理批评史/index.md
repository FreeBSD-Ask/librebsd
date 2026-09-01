---
chapter: 第 346 章
id: CH346
volume: 第18卷-全球社区地区bsd史
---

# 第 346 章 bsd社区治理与管理批评史

## 要点

- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），13,875 位贡献者
- freebsd 代码仓库共 1,294,851 次提交（1993-06-12 至 2026-08-25），13,875 位贡献者
- 自媒体《FreeBSD 大败局》2026-01-26 版（今日头条·灵巧光束，主库 id=2351）治理段论断——“Linux 有 Linus 拍板”“FreeBSD 靠开会、邮件列表、拉共识”“CVS 转 Git 拖了十五年，Linux 两年搞定”“核心组从五个人涨到三十多个后，一个驱动模块挂半年没人认领”“Matthew Dillon（马修·狄龙） 当年出走不是闹脾气，是等一个决定等太久，干脆
- netbsd 代码仓库共 1,999,412 次提交（1992-07-13 至 2026-08-24），4,754 位贡献者
- openbsd 代码仓库共 491,195 次提交（1995-10-18 至 2026-08-25），3,352 位贡献者

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10495] BSD Now 第 664 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10507] BSD Now 第 662 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10613] BSD Now 第 642 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10622] BSD Now 第 641 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10650] BSD Now 第 637 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10706] BSD Now 第 629 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10712] BSD Now 第 627 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10768] BSD Now 第 618 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10855] BSD Now 第 606 期，匹配 CH346 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10873] BSD Now 第 604 期，匹配 CH346 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证
- 自媒体治理批评的“机制跑不动”为观点层，与本节精英制共识治理的权威叙述（决策透明度批评）可互补；但“三十多个”“Linux 两年搞定 git”为事实层失实，须剥离——前者更正为 8–9 人，后者更正为 git 约 10 天；Dillon 出走与 104 章（DragonFly 分叉）互证
- 贡献者高度集中——Top 1 贡献者 wiz 占比 33.4%，需考量'个人主导'与'社区协作'的叙事张力
- 数据库统计受 CVS-to-Git 迁移、镜像滞后等因素影响，commit 数量与贡献者统计存在系统性偏差，须结合一手史料交叉验证

## 文献

- 78.7.5/78.7.6 逐句考据；FreeBSD Core Team 官方页；Committer's Guide §6；主库 id=2351 ［A/自媒体］> **双库核查（2026-08-15）**：播客 BSDTalk #114（2007-05-25）转写确认 Core Team 选举制度与有限人数结构；播客 BSD Now #148（2016-06-29）转写明确 ninth core team has been elected... will officially take over from the eighth core team on Wednesday July 6th，确认定期选举制度。参考文献库 ref 198（Jorgensen 2005, Incremental and Decentralized Integration in FreeBSD）讨论 FreeBSD 治理结构。Core Team 固定 8-9 人论断经官方页面（freebsd.org/internal/core-team）与播客转写互证。考据记录见 03-原始史料库/06-考据记录/20260815_第18卷-全球社区地区bsd史-mail-ref-db-factcheck.md。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1993-1993 年间：868 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP155（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- DaemonForums 的起源是一次社区自救：bsdforums.org 自 2002 年运转良好，但管理员失联约两年，垃圾信息尤其是色情广告泛滥且无从处置，原社群于 2008 年 5 月自立门户；新论坛定位为官方 FreeBSD 邮件列表之外的互联网论坛补充，服务偏好论坛形态的用户；因旧论坛内容的版权归属无法迁移旧帖，论坛全新起步，而原社区几乎所有用户迁入。（BSDTalk EP155，[58.64-93.76]，L1）
- 运营形态：论坛暂由加拿大用户 Stukoff 托管并计划数月内自置服务器，运行于 FreeBSD；论坛软件经试用多个免费包（不完整、过简或缺功能）后购入商业授权使用（转写软件名不可靠，疑为 vBulletin）；反垃圾依托较新的 CAPTCHA，而旧论坛因软件多年未更新其 CAPTCHA 已被攻破，必要时将追加措施。（BSDTalk EP155，[104.84-201.00]，L1）
- 用户生态面向全体：从提问一次即离开的新人到有三十年经验的 BSD 老手均在其中；各 BSD 中 FreeBSD 用户最多、OpenBSD 次之、NetBSD 远少，与 BSDStats.org 的使用统计大体一致，Tournoij 认为论坛构成反映了真实的使用分布。（BSDTalk EP155，[208.48-263.52]，L1）
- 个人使用图景：Tournoij 约 2000 年因厌倦 Windows 而在 Linux、Solaris 与 BSD 间比较，最终以 FreeBSD 落定并沿用至今；家用桌面以 FreeBSD 承担视频播放、游戏与文字处理等全部事务，任系统管理员时混用 BSD、Linux 与 Windows；他强调选择 BSD 出于使用体验而非技术指标，就是喜欢其工作方式且简单；硬件以廉价或免费的旧机为主，含一台 SPARCstation，运行 FreeBSD 6 与 7 的 STABLE 分支，升级到 7 对终端用户几乎无感。（BSDTalk EP155，[281.96-394.42]，L1）

**史料**：

- 本期为 2008 年 7 月对 DaemonForums 创始人 Martin Tournoij 的口述访谈，保留 bsdforums.org 衰落与 DaemonForums 创立过程的当事人陈述、BSDStats.org 用户统计引用、论坛软件与托管安排等社区基础设施史料；转写人名与软件名多处受损，引用须以原始音频核对。（BSDTalk EP155，[0.00-53.24]，L1）

**史观**：

- 总纲4 分离聚合是永恒规律：bsdforums.org 的失效与管理员失联引发社群脱离旧载体、重组为 DaemonForums 的过程，显示 BSD 社区的交流载体并非稳态结构：旧的社区形式僵死后，人群分离并在新形式下重新聚合，社区存续依靠的是这种分离与聚合的循环而非某个固定平台。（BSDTalk EP155，[66.20-93.76]，L1）

**辨析**：

- 论坛软件名转写严重失真（FeeBudderPan 疑为 vBulletin）须以音频核对；几乎所有用户迁移的规模为当事人自述且无量化数据；bsdforums.org 此后的最终去向本期未提及，需以存档页面与后续访谈补充。　[存疑脚注] 论坛软件身份与迁移规模均为单一来源陈述，未经独立验证。（BSDTalk EP155，[122.00-145.96]，L4）

**文献**：

- [BSDTalk EP155] Backman W. BSDTalk: 155: bsdtalk 155 - Martin Tournoij from DaemonForums.org[EB/OL]. (2008-07-21)[2026-08-27]. https://bsdtalk.blogspot.com/2008/07/bsdtalk-155-martin-tournoij-from.html.

<!-- /PODCAST_REVIEW -->
