---
chapter: 第 193 章
id: CH193
volume: 第10卷-openbsd的历史
---

# 第 193 章 openbsd-2x的fork与代码审计奠基

## 要点

- OpenBSD 仓库构成：openbsd-src(246535)、openbsd-ports(212040)、openbsd-www(32620)。src 提交量占主导，ports 和 www 为辅助，反映其‘完整系统’哲学

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4095] 卷“第10卷-openbsd的历史”第 193 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4096] 卷“第10卷-openbsd的历史”第 193 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4097] 卷“第10卷-openbsd的历史”第 193 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

- [DB:code_repos:openbsd.duckdb] OpenBSD 仓库构成：openbsd-src(246535)、openbsd-ports(212040)、openbsd-www(32620)。src 提交量占主导，ports 和 www 为辅助，反映其‘完整系统’哲学

## 史观

- 经验优先：OpenBSD 的代码审计文化是安全至上的经验性实践，非理论推演

## 辨析

- OpenBSD 邮件列表存档的完整性需考据——marc.info 与 OpenBSD 官方存档的覆盖范围可能略有差异；CVS 转 Git 迁移过程中元数据保真度需核验
- 审计 commit 与一般 commit 的区分需考据——OpenBSD commit log 中部分 commit 未明确标注 audit，需对照 advisory 推断
- OpenSSH 1.0 的具体发布日期存在 1999.10.1 与 1999.10.5 两种说法——需对照 OpenBSD 官方公告核验【代码级证据·openbsd.duckdb openbsd-src 仓库】commit `bf74e864c129cdd07c9ebd41a8db719c7c8b49d8`（committer_date `1999-10-01T18:58:56Z`，author `der
- Release Notes 的完整性需考据——部分细节可能滞后于实际代码；commit log 中的加密相关 commit 需对照 export 控制合规性核验
- 本子节的哲学审视须以三段式呈现——【查证来源】（1）原材料/哲学/项目统摄史观/第 25 章.md 总纲第 13、19、21 条原文经 2026-07-24 一手核验，确认“任何道德问题本质上是利益问题，社区治理亦是形式主义的政治产物”（第 13 条）、“前理解的差异使分歧不可避免。权力与知识在历史书写中共谋——什么被记录、什么被遗忘，本身就是权力行使”（第 19 条）〔待核：原文截断，后文待回源〕

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb
