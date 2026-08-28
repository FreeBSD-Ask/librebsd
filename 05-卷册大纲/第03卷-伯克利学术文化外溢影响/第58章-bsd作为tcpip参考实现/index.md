---
chapter: 第 58 章
id: CH58
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 58 章 bsd作为tcpip参考实现

## 要点

- NFS（Network File System）由 Sun Microsystems 于 1984 年设计，基于 Sun RPC（Remote Procedure Call，RFC 1057，1988 年 6 月）与 XDR（eXternal Data Representation，RFC 1014，1987 年 6 月）构建；NFS Version 2 协议于 1989 年 3 月以 RFC 1
- Apache 许可证（Apache License 1.0 1995、2.0 2004）与 BSD 许可证在哲学上共鸣：（1）二者均为宽松开源许可证，允许商业使用与闭源衍生；（2）Apache 许可证 1.0 借鉴 BSD 许可证，增加专利反诉条款；（3）Apache 与 BSD 的宽松许可证哲学与 GPL 的 copyleft 哲学形成对比；（4）Apache 服务器在 BSD 系统上的主导地位
- Apache 最初在 BSD 系统上开发——NCSA httpd 运行于 BSD/OS，Apache 的 prefork 模型直接受益于 BSD fork() 实现效率。sendmail（Eric Allman（埃里克·奥尔曼）, 1981）为 4.1cBSD 开发，是互联网 SMTP 事实标准。
- 对互联网与 BSD 关系批评的形式主义分析：（1）批评本身存在形式主义倾向，将“市场遗忘”归因于 BSD 许可证，忽视其他因素（如 Linux 商业化 Red Hat 1999 IPO、Microsoft 营销）；（2）批评以现代市场份额衡量历史 BSD，存在时代错置——1980-1990 年代 BSD 作为互联网基础设施核心（BIND/Sendmail/TCP/IP），1990 年代后期 Lin

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4206] 卷“第03卷-伯克利学术文化外溢影响”第 58 章，匹配置信度 1.0，原因：SMM:9 sendmail 邮件路由
- [DB:references_fulltext:chapter_matches:chmatch_4207] 卷“第03卷-伯克利学术文化外溢影响”第 58 章，匹配置信度 1.0，原因：SMM:10 BIND 域名服务器
- [DB:references_fulltext:chapter_matches:chmatch_4208] 卷“第03卷-伯克利学术文化外溢影响”第 58 章，匹配置信度 1.0，原因：SMM:10 BIND 补充
- [DB:bsdnow_podcast:outline_mappings:om_10896] BSD Now 第 601 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11278] BSD Now 第 556 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11509] BSD Now 第 528 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11658] BSD Now 第 507 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11701] BSD Now 第 504 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11769] BSD Now 第 491 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11902] BSD Now 第 479 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11979] BSD Now 第 467 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12182] BSD Now 第 447 期，匹配 CH58 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12361] BSD Now 第 435 期，匹配 CH58 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NFS 设计始于 1984 年，RFC 1094（1989.3）是 NFSv2 的正式标准发布，先前已有 SunOS 实现；NFS 首次集成入 BSD 的确切版本存在模糊性 [据 Lessig (1999) 一手文献印证消解^doubt-resolved-124——经 bsd_commits.db 查询未得明确证据（查询条件：`SELECT * FROM commits WHERE message
- Apache License 1.0（1995）与 2.0（2004）经多源确认（Apache License 1.0 借鉴 BSD 许可证，2.0 增加专利反诉条款与 Apache 品牌保护条款）；BSD 许可证版本——BSD 2-Clause（Simplified BSD License）与 BSD 3-Clause（New BSD License）为两种主要变体，均允许商业使用与闭源衍生，保
- 批评的具体文本——freebsd-questions 邮件列表、LWN 文章与社区博客中的 BSD 互联网遗产批评（缺乏系统性学术分析）；形式主义分析方法的适用性——形式主义作为 19-20 世纪数学哲学流派（斯坦福哲学百科"Formalism in Mathematics"与"Mathematical Style"词条），本节引申为“以形式标签替代实质判断”的方法论批评，适用于分析“用市场份额标

## 文献

- RFC 1094（Sun Microsystems, 1989）NFS: Network File System Protocol Specification；RFC 1057（Sun, 1988）RPC: Remote Procedure Call Protocol Specification；RFC 1014（Sun, 1987）XDR: External Data Representation Standard；Sandberg, R., Goldberg, D., Kleiman, S., Walsh, D. & Lyon, B. (1985) "Design and Implementation of the Sun Network Filesystem" Proc. USENIX Summer Conference 1985, pp. 119-130；Stern, H. (1991) "Managing NFS and NIS" O'Reilly ISBN 0-937175-75-7 ［B］
- Apache License 1.0/2.0 原文；BSD 许可证原文；开源许可证比较研究（如 Rosen, L. (2005) "Open Source Licensing"）[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Apache 历史； Allman 1983 ［A］
- 互联网与 BSD 关系批评文本；市场史方法论研究；BSD 历史语境研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证][^doubt-resolved-124]: 据 new-york-basic-books (Lessig, 1999) 消解

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第58章-bsd作为tcpip参考实现 第 58 章 bsd作为tcpip参考实现（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：15831 条 -->

### 要点（播客口述史提取）
- （该章节匹配播客中未提取到高置信度核心史实，需人工深挖）

### 史料（播客当事人陈述）
- （待人工提取）

### 史观（播客当事人观点与总纲映射）
- （该章节匹配播客中未提取到当事人观点性陈述）

### 辨析（播客争议与存疑点）
- （该章节匹配播客中未提取到争议性陈述）

### 文献（播客参考条目）
- [BSD Now EP76] Pennington J. BSD Now: 76: Time for a Change[EB/OL]. (2015-02-11)[2026-08-15]. https://www.bsdnow.tv/76.
- [BSD Now EP121] Pennington J. BSD Now: 121: All your hyves are belong to us[EB/OL]. (2015-12-23)[2026-08-15]. https://www.bsdnow.tv/121.
- [BSD Now EP149] Pennington J. BSD Now: 149: The bhyve has been disturbed, and a wild Dexter appears![EB/OL]. (2016-07-06)[2026-08-15]. https://www.bsdnow.tv/149.
- [BSD Now EP170] Pennington J. BSD Now: 170: Sandboxing Cohabitation[EB/OL]. (2016-11-30)[2026-08-15]. https://www.bsdnow.tv/170.
- [BSD Now EP173] Pennington J. BSD Now: 173: Carry on my Wayland son[EB/OL]. (2016-12-21)[2026-08-15]. https://www.bsdnow.tv/173.
- [BSD Now EP186] Pennington J. BSD Now: 186: The Fast And the Firewall: Tokyo Drift[EB/OL]. (2017-03-22)[2026-08-15]. https://www.bsdnow.tv/186.
- [BSD Now EP198] Pennington J. BSD Now: 198: BSDNorth or You can’t handle the libtruth[EB/OL]. (2017-06-14)[2026-08-15]. https://www.bsdnow.tv/198.
- [BSD Now EP210] Pennington J. BSD Now: 210: Your questions, part I[EB/OL]. (2017-09-06)[2026-08-15]. https://www.bsdnow.tv/210.

<!-- /PODCAST_MINE -->
