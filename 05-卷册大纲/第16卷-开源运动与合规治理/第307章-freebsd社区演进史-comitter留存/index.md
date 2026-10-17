---
chapter: 第 307 章
id: CH307
volume: 第16卷-开源运动与合规治理
---

# 第 307 章 freebsd社区演进史-comitter留存

## 要点

- committer 活跃度统计可通过 src commit log 分析，但需区分“提交”与“审查”两种贡献
- FUSE 项目从 2012 年编程之夏引入到 2019 年更新的具体 commit 时间线需通过 src/sys/fs/fusefs 仓库 commit log 考据
- Bugzilla PR 统计是衡量外部贡献的重要依据，但需区分“提交 PR”与“合并入树”两种结果
- 企业赞助与基金会预算数据是评估 FreeBSD 商业生态的关键，需交叉验证
- 基金会年报与捐赠记录是评估资金结构的关键，需交叉验证

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10429] BSD Now 第 676 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10438] BSD Now 第 675 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10443] BSD Now 第 674 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10455] BSD Now 第 671 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10458] BSD Now 第 670 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10463] BSD Now 第 668 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10467] BSD Now 第 667 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10473] BSD Now 第 666 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10485] BSD Now 第 665 期，匹配 CH307 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10491] BSD Now 第 664 期，匹配 CH307 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- commit log 是否能完整反映贡献需评估；emeritus 状态的 committer 是否计入需明确
- 2012 年编程之夏 FUSE 项目的具体学生与导师需查编程之夏 archive；2019 年更新的具体 commit hash 需考据
- Bugzilla PR 是否完整保留需查；合并率统计方法需明确
- Foundation 990 表是否完整公开需查；企业赞助的具体金额需核实
- 考据过程留痕——【查证来源】外部批评来源包括 LKML Archive、Reddit r/freebsd 与 r/linux 讨论、freebsd-hackers 邮件列表争论串、Hacker News 评论等；社区回应包括 Core Team 公告、freebsd-announce 邮件列表声明、Foundation 年报中关于社区治理的章节；〔待核：原文截断，后文待回源〕

## 文献

- FreeBSD src commit log；Core Team Activity Reports ［A］
- 编程之夏 2012 FreeBSD Project Page；FreeBSD src/sys/fs/fusefs history［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD Bugzilla Statistics；freebsd-hackers 讨论 ［A］
- FreeBSD Foundation 990 Forms；freebsd-foundation 邮件列表 ［A］
- FreeBSD Foundation 990 Forms；Annual Reports 2014-2024［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD src/access 历史；Core Team Reports ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：开源治理
- freebsd-hackers Archive；Majordomo Logs ［A］
- Core Team Meeting Minutes；freebsd-core Archive ［A］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：开源治理
- FreeBSD Security Advisories Archive；ERRATA Notices［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD doc Repository History；Handbook Archives ［B］## 史料考据补充（2026-08-04 任务3 联网核验）> 主题：开源治理

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1233 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1233`；w172 YouTube 章节路由采纳）

据 BSDCan 19 Dev Summit 讲者口述：FreeBSD 项目曾把从干净检出到 build world 的耗时从 15 分钟压缩到 3 分钟。（YouTube EP8feuiZqQovU，[4283.4-4305.5]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1238 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1238`；w172 YouTube 章节路由采纳）

据 BSDCan '19 Dev Summit 讲者口述：FreeBSD 基金会做过一份 2016 年的基金会调查（原文 the 2016 foundation survey）。（YouTube EP9nc8N6GtAPg，[673.61-676.78]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1239 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1239`；w172 YouTube 章节路由采纳）

据 BSDCan '19 Dev Summit 讲者口述：核心团队章程（原文讹字 core Chartered）自 2002 年以来一直在被审视。（YouTube EP9nc8N6GtAPg，[2510.69-2515.69]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1284 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1284`；w172 YouTube 章节路由采纳）

据〔BSDCan '19 Dev Summit〕讲者口述：讲者所在 Intel 设有 BSD 工程团队，这是一个较新的团队。（YouTube EPZOKQRCvWnho，[9.67-19.31]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-978 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-978`；w172 YouTube 章节路由采纳）

据〔BSDCan 2023 开幕〕讲者 Dan Langille 口述：讲者约十年前了解到 Cisco 为非网络侧的重度 FreeBSD 用户。（YouTube EPtxgMehXW860，[319.44-327.11]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1406 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1406`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Dev Summit 文档翻译〕讲者口述：葡萄牙语文档翻译者自2012年起持续从事 FreeBSD 文档翻译而未能完成，改用以 Web 工具为核心的翻译工作流后，在六个月内完成了过去六年的工作，工具形态的改变是其得以完成的必要前提。（YouTube EPNApPDGb1H4A，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1407 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1407`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Dev Summit 文档翻译〕讲者口述：文档翻译贡献者预计逐步成为评审者，并可能进而成为文档贡献者、ports 贡献者或源码贡献者；Web 端低门槛入口（一句即可、午间二十分钟即可完成）是承接这类轻度参与者的通道。（YouTube EPNApPDGb1H4A，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1408 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1408`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan '19 Dev Summit 文档翻译〕讲者口述：参与者在讨论工作小组与 FCP 的分工时指出，FCP 在实际运作中容易变成个人工程，起草文件的人主导整个过程，而工作小组在结构上更协作，FCP 或许可作为工作小组产出的后续载体而非首选工具。（YouTube EPNApPDGb1H4A，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2094 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2094`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Romain Tartière 在 BSDCan 2018 的 Puppet 演讲〕讲者口述：在 FreeBSD 上落地 Puppet 的第一步是 ports 里的 puppet5 端口，装出的即 Puppet 5。（YouTube EPCb4VmhuyIMo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2095 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2095`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Romain Tartière 在 BSDCan 2018 的 Puppet 演讲〕讲者口述：FreeBSD 的 ports 树中另有 puppetserver5 端口可装 Puppet master；在部分环境下还需调整 puppet server 的 login class 才能正常运行。（YouTube EPCb4VmhuyIMo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2096 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2096`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Romain Tartière 在 BSDCan 2018 的 Puppet 演讲〕讲者口述：FreeBSD 用户若遇到 Puppet 与 FreeBSD 的兼容问题并已有补丁、但尚未请求上游合并，可致函 FreeBSD 侧的 puppet 联系渠道；维护者会在 FreeBSD 的 puppet 端口里额外打上一个补丁，使修复早于上游正式发行即可取用。（YouTube EPCb4VmhuyIMo，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
