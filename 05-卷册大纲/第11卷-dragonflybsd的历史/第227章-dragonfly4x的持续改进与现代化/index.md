---
chapter: 第 227 章
id: CH227
volume: 第11卷-dragonflybsd的历史
---

# 第 227 章 dragonfly4x的持续改进与现代化

## 要点

- dragonfly.duckdb dragonfly-src 仓库 tags 表提供 v4.2.0（tagger_date = 2015-06-28T19:15:14-04:00）与 v4.4.0（tagger_date = 2015-12-03T18:58:35-05:00）的 tagger_date、tagger_name、target_commit_hash 字段。v4.2.0 target_com
- dragonfly.duckdb dragonfly-src 仓库 commits 表提供 v4.6.0 与 v4.8.0 期间 NVMe 与 vkernel 改进的具体 commit。v4.6.0（2016-08-01）至 v4.8.0（2017-03-26）间隔约 8 个月，期间 NVMe 相关 commit［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］ 卷“第11卷-dragonflybsd的历史”第 227 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- release notes 与 commit log 偶有不一致——dragonfly.duckdb 显示 v4.2.0 与 v4.4.0 间隔约 5 个月，须以 commit log 核验实际开发投入；GPU 与网络栈改进的具体 commit 须以 commit_files 表核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］；Dillon 在 v4.2
- commit log 可能不完整反映改进全貌——部分改进可能分散在多个 commit 中，须结合邮件讨论辨析；Wildner 邮箱须注意——dragonfly.duckdb 显示其 2016-2018 年使用 <saw@online.de> 而非 <swildner@dragonflybsd.org>（后者 2004-2008 年使用），两邮箱合计 3517 条 commit；NVMe 与 vkern
- 邮件记录可能不完整——部分权限决策可能在私下邮件或 IRC 中进行；dragonfly.duckdb 显示 Aaron LI 首 commit = 2017-09-27，但其在 kernel@ 邮件列表的首次发言 ［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］ 须单独核验；权限撤销记录在 DragonFly 中罕见——dragonfly.duckdb contr
- 批评发言可能被断章取义——须结合完整上下文辨析，避免简化引用；bsd_commits.db 关键词搜索可能低估批评相关讨论——部分讨论可能以 ‘community size’/‘project health’ 等术语进行；私人邮件与 IRC 讨论不可考，仅以公开邮件列表为准
- bsd_commits.db 关键词搜索可能低估个人贡献——Tigeot 的 DRM 移植 commit 可能以 ‘i915’/‘radeon’ 等具体驱动名为关键词而未提及 ‘DRM’，须以 commit_files 表 sys/dev/drm/ 目录核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］；commit 量与代码行数无简单线性关系——部分

## 文献

- dragonfly.duckdb dragonfly-src 仓库 tags 表（v4.2.0/v4.4.0 完整字段）；dragonfly.duckdb dragonfly-src 仓库 commits 表（Dillon 2014-2016 年按年统计）；DragonFly 4.2/4.4 release notes [EB/OL]. dragonflybsd.org/release/；kernel@ 邮件列表档案 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2015-2016 年间：90,164 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 commits 表（v4.6.0/v4.8.0 期间 commit 与 TOP 10 贡献者）；kernel@ 邮件列表档案；NVMe/虚拟化性能 benchmark 报告 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2016-2017 年间：88,853 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- lists.dragonflybsd.org 邮件列表归档；dragonfly.duckdb dragonfly-src 仓库 contributors 表（first_commit_date 序列）；marc.info DragonFly 备份 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2014-2017 年间：227,047 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb commits 表（两仓库对照）；lists.dragonflybsd.org 邮件列表归档；lists.freebsd.org 邮件列表归档；LKML 档案；技术媒体报道 ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
- dragonfly.duckdb dragonfly-src 仓库 commits 表与 contributors 表（2014-2017 年 TOP 10）；kernel@ 邮件列表档案；贡献者个人简历［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］ ［A］

<!-- DB_REF:dragonfly.duckdb -->
> **数据库引用（dragonfly.duckdb）**：本子节对应 dragonfly 代码仓库。> 2003-2026 年间：656,206 次提交。> 仓库总览：656,206 次提交，535 位贡献者，2003-06-17 至 2026-08-18。
