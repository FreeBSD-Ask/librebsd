---
chapter: 第 213 章
id: CH213
volume: 第10卷-openbsd的历史
---

# 第 213 章 openbsd的相关传言与都市传说考据

## 要点

- OpenBSD 安全宣传语的演化史是开源项目自我品牌化（branding）的典型案例——其措辞变化与实际的漏洞事件精确对应：（1）"Five years without a remote hole in the default install!"（约 1997-2002 年），声称默认安装五年无远程漏洞，这一宣称基于 OpenBSD 项目的安全审计实践——代码逐行审计、最小化默认服务、安全优先的设
- 2010 年 12 月 11 日，曾任 FBI 技术顾问的 Gregory Perry 通过私人邮件向 Theo de Raadt（西奥·德·若特） 声称：FBI 约在 2000-2001 年间向 NetSec 公司支付款项，让多名前 OpenBSD 开发者在 OpenBSD 加密框架（IPsec 代码）中植入后门。12 月 14 日，de Raadt 将该邮件全文转发至 openbsd-tech
- OpenBSD 的安全审计文化起源于项目创建后不久——de Raadt 被一家名为 Secure Networks, Inc.（SNI）的本地安全软件公司联系。SNI 正在开发名为"Ballista"的网络安全审计工具（后更名为 Cybercop Scanner，因 SNI 被 Network Associates 收购）。这一合作关系对 OpenBSD 早期安全审计起到了催化作用——SNI 使用

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4101] 卷“第11卷-dragonflybsd的历史”第 213 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4102] 卷“第11卷-dragonflybsd的历史”第 213 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- [考据脚注] "Five years/One remote hole/Only two remote holes" 的时间线——跨 OpenBSD 官网安全公告（openbsd.org/security.html，含宣传语历史版本）、ISS 2002 公告、Core Security 2007 公告三点交叉验证一致〔原 Wikipedia 条目为禁引来源已删除〕。[考据脚注] 宣传语的“默认安装”
- [考据脚注] Gregory Perry 的真实身份——经 marc.info 一手邮件存档核验，Perry 自称“前 FBI 技术顾问”但此身份未经 FBI 官方确认〔原经 Wikipedia 查阅为禁引，改以一手邮件存档为准〕；本考据将“FBI 后门传言”作为传言（rumor）而非经证实的事实呈现，符合项目 0 信任原则。[考据脚注] de Raadt 被 NetBSD 撤权事件——撤权公告与
- [考据脚注] Ballista/Cybercop Scanner 与 SNI 合作的精确时间——McKusick (1999) 提供的合作描述未附精确日期，本考据标注“约 1997-1998 年”（OpenBSD 2.3 发布前）〔原 Wikipedia 条目引述已删除〕。[考据脚注] Marc Espie 关于代码审计"never finished"的评论——原出处为 Espie 在某次公开访谈

## 文献

- OpenBSD Security. "Only two remote holes in the default install, in a heck of a long time!" openbsd.org/security.html. Dowd, M. "OpenSSH Challenge-Response Vulnerability." Internet Security Systems Advisory, June 2002. Ortega, A. "OpenBSD IPv6 mbuf kernel buffer overflow." Core Security Technologies, 13 March 2007. Van Sprundel, I. "Are all BSDs created equally?" DEF CON 25, 2017. Stein. "A systematic evaluation of OpenBSD's mitigations." 36C3, 2019.<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- Perry, G. / de Raadt, T. "Alleged FBI backdoor in OpenBSD IPSEC stack." openbsd-tech mailing list, December 2010. MARC mailing list archive. NetBSD Core Team. "Revocation of Theo de Raadt's commit privileges." netbsd-core mailing list, 23 December 1994. OpenBSD Project. "OpenBSD IPSEC Audit Results." openbsd-tech mailing list, January 2011.<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD Project. "Security." openbsd.org/security.html. McKusick, M. K. "OpenBSD." Open Sources: Voices from the Open Source Revolution. O'Reilly, 1999. Van Sprundel, I. "Are all BSDs created equally?" DEF CON 25, 2017. Stein. "A systematic evaluation of OpenBSD's mitigations." 36C3, 2019.<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
