---
chapter: 第 204 章
id: CH204
volume: 第10卷-openbsd的历史
---

# 第 204 章 openbsd的起源从netbsd分叉

## 要点

- OpenBSD 时间跨度（1995-10-18 至 2026-08-25），始于 1995 年 10 月 de Raadt 被 NetBSD 逐出后立即启动

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3903] 卷“第10卷-openbsd的历史”第 204 章，匹配置信度 folder，原因：folder 第202章

- [DB:code_repos:openbsd.duckdb] OpenBSD 时间跨度（1995-10-18 至 2026-08-25），始于 1995 年 10 月 de Raadt 被 NetBSD 逐出后立即启动

## 史观

- 偶然性优先：OpenBSD 的诞生源于 de Raadt 被 NetBSD 逐出这一偶然人事事件

## 辨析

- fork 动因在不同叙事中存在分歧——de Raadt 自述与技术争议（如 i386 移植方向、SPARC 代码合并风格）相关，NetBSD Core Team 则强调个人作风问题（邮件列表言辞激烈）；被逐时间为 1994-12-23（Adam Glass 通知邮件日期），部分资料提及的 “1996.5” 系误记——openbsd.duckdb 显示 OpenBSD 仓库最早 commit 为 1
- 考据过程留痕——【查证来源】项目史观总纲第 5、8、19 条原文经原材料/哲学/项目统摄史观/第 25 章.md 一手核验，三条总纲的原文表述与本节引用一致；Adam Glass 通知邮件措辞经 <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html> 一手核验，“asked to resign” "long history
- 考据过程留痕——【查证来源】Adam Glass 通知邮件原文经 <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html> 一手核验，邮件头 Date 字段为 12/23/1994 11:26:09，正文首句 “On December 20, Theo de Raadt was asked to resign” "remai
- 考据过程留痕——【查证来源】Adam Glass 通知邮件原文经 <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html> 一手核验，"long history of rudeness towards and abuse of users and developers“ ”remaining members of ‘core
- 考据过程留痕——【查证来源】项目史观总纲第 13、19、21 条原文经原材料/哲学/项目统摄史观/第 25 章.md 一手核验，三条总纲的原文表述与本节引用一致；Adam Glass 通知邮件措辞经 <https://mail-index.netbsd.org/netbsd-users/1994/12/23/0000.html> 一手核验；openbsd.duckdb openbsd-src 仓库

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP428（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- OpenBSD 于 1995 年 10 月作为 NetBSD 分叉起步，其默认安装长期仅报告两个远程漏洞，被描述为默认安全的系统。（BSD Now EP428，[135.74-145.1]，L2）
- OpenBSD 率先随系统搭载 IPsec 等强密码学，并因此卷入美国出口管制，这是其基地设于加拿大的原因之一。（BSD Now EP428，[145.1-160.3]，L2）
- OpenBSD 形成发现漏洞后不再单点修补，而是在全树范围内寻找并修复同类模式的代码审计文化。（BSD Now EP428，[164.94-184.78]，L2）
- OpenBSD 是 OpenSSH、OpenBGPD、PF、OpenNTPD、IKED、Mandoc 与 LibreSSL 等广泛使用组件的上游来源。（BSD Now EP428，[247.2-262.74]，L2）[订正：原 OpenSMTPD、IKE，2026-09-30 SenseAudio 重转核对]

**史料**：

- Peter Hansteen 的 What every IT person needs to know about OpenBSD 系列文章，作为本期 OpenBSD 历史叙述的主要二手来源。（BSD Now EP428，[70.74-76.44]，L2）

**史观**：

- 总纲10 动手者创造历史：OpenBSD 以代码审计与全树范围修复确立安全实践，体现动手者在具体工程中塑造项目文化。（BSD Now EP428，[164.94-191.78]，L2）
- 总纲13 法律与道德是利益分配：美国出口管制把加密技术纳入法律约束，迫使 OpenBSD 调整基地布局，体现法律与道德作为利益分配工具的现实效应。（BSD Now EP428，[145.1-160.3]，L2）

**辨析**：

- “默认安装仅两个远程漏洞”为 OpenBSD 项目长期自述口径，其统计口径与时间范围需与官方安全公告逐条核对。　[存疑脚注] 远程漏洞计数为项目自述，统计边界需对照 OpenBSD 官方安全公告确认。（BSD Now EP428，[138.94-145.1]，L4）

**文献**：

- [BSD Now EP428] Pennington J. BSD Now: 428: Cult of BSD[EB/OL]. (2021-11-11)[2026-08-15]. <https://www.bsdnow.tv/428>.

<!-- /PODCAST_REVIEW -->