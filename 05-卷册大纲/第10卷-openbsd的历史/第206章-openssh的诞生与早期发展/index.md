---
chapter: 第 206 章
id: CH206
volume: 第10卷-openbsd的历史
---

# 第 206 章 openssh的诞生与早期发展

## 要点

- OpenSSH 仓库共 14372 次提交（1999-10-27 至 2026-08-20），173 位贡献者，是 OpenBSD 项目最具全球影响力的子项目

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3904] 卷“第10卷-openbsd的历史”第 206 章，匹配置信度 folder，原因：folder 第204章
- [DB:references_fulltext:chapter_matches:chmatch_4017] 卷“第10卷-openbsd的历史”第 206 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:openssh.duckdb] OpenSSH 仓库共 14372 次提交（1999-10-27 至 2026-08-20），173 位贡献者，是 OpenBSD 项目最具全球影响力的子项目

## 史观

- 动手者创造历史：OpenSSH 的全球采纳是无数系统管理员默默部署的结果，非营销之功

## 辨析

- fork 日期在不同叙事中存在差异——部分来源称“1999 年 9 月（随 OpenBSD 2.6 于 1999-12-01 正式发布）”（以 OpenSSH-1.0 commit 日期 1999-10-01 为准），部分称“1999 年 9 月”（以初始导入 commit 84959968510b 日期 1999-09-26 为准）；经 openbsd.db 核查，初始导入为 1999-09-2
- 考据过程留痕——【查证来源】合图“成功”判定的各项事实经以下一手史料核验：SSH1 移除时间线，经 OpenSSH 7.4 Release Notes（<https://www.openssh.com/txt/release-7.4>，2026-07-23 WebFetch 一手核验）确认原文"This release removes server support for the SSH v.1 
- 纯洁化工作的具体范围经 OpenSSH 官方历史页面确认涵盖四项——de Raadt 的非可移植代码移除、Provos 的加密与 GPL 组件移除、Friedl 的 SSH 1.3→1.5 协议替换、Beck 的 RSA 专利规避 Makefile；纯洁化完成时间节点为 OpenSSH 1.2.2 随 OpenBSD 2.6 发布日 1999-12-01，因 1.2.2 是首个随 OpenBSD 
- FreeBSD 4.0（2000-03-14）包含 OpenSSH 但 sshd 未默认启用——vendor import 在 2000-02-24，MFC 至 4-STABLE 在 2000-03-13，但"sshd enabled by default"MFC 在 2000-09-07（commit 94e00feef2e1），故 FreeBSD 4.0 用户需手动启用 sshd，FreeBS
- SSH1 移除时间线经 OpenSSH 官方 Release Notes 与 openbsd.db 双重核实——7.4（2016-12-19）移除服务端 SSH1，7.6（2017-10-03）完全删除客户端 SSH1（含配置选项与文档），部分二手资料将"OpenSSH 8.2（2020-02-14）"误记为 SSH1 移除版本，但 8.2 Release Notes 实际记载的是 FIDO/U2

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openssh.duckdb
