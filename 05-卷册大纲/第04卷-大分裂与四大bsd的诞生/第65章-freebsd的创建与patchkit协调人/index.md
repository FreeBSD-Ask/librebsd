---
chapter: 第 65 章
id: CH65
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 65 章 freebsd的创建与patchkit协调人

## 要点

- FreeBSD 仓库共 1294851 次提交（1993-06-12 至 2026-08-25），3720 位贡献者，是从 386BSD patchkit 协调人模式演化而来的核心代码库

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3679] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3704] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3782] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3783] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3792] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3807] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3829] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章
- [DB:references_fulltext:chapter_matches:chmatch_3966] 卷“第04卷-大分裂与四大bsd的诞生”第 65 章，匹配置信度 folder，原因：folder 第64章

- [DB:code_repos:freebsd.duckdb] FreeBSD 仓库共 1294851 次提交（1993-06-12 至 2026-08-25），3720 位贡献者，是从 386BSD patchkit 协调人模式演化而来的核心代码库

## 史观

- 多方平等：FreeBSD 的创建是 patchkit 协调人模式的产物，非单一英雄叙事；动手者创造历史：默默贡献的 patchkit 提交者才是真正的奠基人

## 辨析

- FreeBSD Handbook 原文明确记载 1.0 "based on the 4.3BSD-Lite ('Net/2') tape from U.C. Berkeley, with many components also provided by 386BSD and the Free Software Foundation"；~~原 "4.3BSD-Reno" 说法错误~~，Net/2 与
- Handbook 仅记载提供 "a machine to work on and a fast Internet connection"，具体服务器规格（486）、带宽速率（T1）、Core Team 成员是否在 Walnut Creek 兼职等细节需对照合同邮件核验，避免夸大或简化；FreeBSD 2.0 公告特别感谢 Walnut Creek "continuing support and e
- Walnut Creek 提供的服务器具体规格与带宽速率需对照 1994 年邮件列表核验；FreeBSD 1.0 公告中 FTP 站点为 freebsd.cdrom.com，证实 Walnut Creek 从一开始就托管 FTP 分发
- GEOM 存储框架由 Poul-Henning Kamp 开发，但 GEOM 首次随 FreeBSD 5.0（2003 年 1 月）引入，不属于 1.0-2.0（1993-1994）时期的贡献；PHK 在 1994 年已是 FreeBSD 2.0 的 release engineer，早期贡献包括发布工程、内存分配器（malloc）、NTP 等，非 SCSI/GEOM 子系统
- 具体贡献者的具体技术工作需对照源码 commit message 核验；GEOM 为 2003 年 FreeBSD 5.0 引入的框架，不属于 1993-1994 年时期贡献

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 freebsd.duckdb
