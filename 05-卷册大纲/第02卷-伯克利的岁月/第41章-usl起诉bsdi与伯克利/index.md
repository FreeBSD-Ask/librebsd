---
chapter: 第 41 章
id: CH41
volume: 第02卷-伯克利的岁月
---

# 第 41 章 usl起诉bsdi与伯克利

## 要点

- USL v. BSDi 案件号为 Civil Action No. 92-1667（D. N.J.），起诉书要点包括：BSDi 基于 Net/2 商业化 BSD/OS 侵犯 USL 版权与商业秘密、伯克利校方未授权 BSDi 使用 Net/2 商业化、Net/2 中含 USL 衍生代码（约 6 个文件）、BSDi 须停止销售 BSD/OS 与赔偿| 字段 | 内容 | 来源 || --- | --
- 经 Justia 832 F. Supp. 790 一手判例抬头确认，案件当事方与律师团队如下：原告 USL 为特拉华州公司、总部位于新泽西州 Summit（由 AT&T **1990 年** 成立、**1993 年** 出售给 Novell）；被告 BSDi 为特拉华州公司、总部位于弗吉尼亚州 Richmond Falls（由 CSRG 核心成员 Karels、McKusick、Bostic 等
- BSDi 与伯克利的应对包括：BSDi 聘请律师团队应诉、伯克利校方法律顾问介入、CSRG 提供 Net/2 重写过程文件证据、社区组织支持 BSDi（如 USENIX 声明）、1993 年 3 月初（Debevoise 法官驳回初步禁令裁决后的下一个周一）伯克利在加州州法院反诉 USL（声称 USL 未按许可证要求为 System V 中使用的 BSD 代码提供署名）
- 经 McKusick 1999《Twenty Years of Berkeley Unix》当事人一手叙述确认，诉讼期间的 “代码清理” 须区分三个阶段：① **诉前清理（1989-1991）**——Karels、Bostic、McKusick 三人 "spent the next several months going over the entire distribution, file by
- 经 FreeBSD 2.0 Release Notes 官方一手来源（freebsd.org/releases/2.0/notes/）与 McKusick 1999 交叉验证，4.4BSD-Lite 于 **1994 年 6 月** 发布，使用与 Networking Release 1/2 相同的自由再分发条款，允许源代码与二进制形式的自由再分发，仅要求保留大学版权声明与致谢；同时发布 4.4B

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3711] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3731] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3736] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3865] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3893] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3935] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章
- [DB:references_fulltext:chapter_matches:chmatch_3956] 卷“第02卷-伯克利的岁月”第 41 章，匹配置信度 folder，原因：folder 第41章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 案件号经 Justia 联邦判例汇编 832 F. Supp. 790 (D.N.J. 1993) 公开判例确认为 Civ. No. 92-1667，法院为 United States District Court, D. New Jersey（D.N.J.），法官为 Dickinson R. Debevoise；先前 “部分史料称 D. N.J. Newark” 的歧义已解决——D.N.J. 为
- [考据脚注：BSDi 总部地址] Justia 判例原文记载 BSDi 总部为 "Richmond Falls, Virginia"，但弗吉尼亚州实际地名无 "Richmond Falls"——可能为 "Richmond"（弗吉尼亚州首府）或 "Falls Church"（弗吉尼亚州城市）的笔误或 OCR 错误，原始诉状应为正确地址，Justia 判例文本可能存在抄录错误，需核对原始诉状确认 BS
- 反诉时间经 McKusick 1999 当事人一手叙述确认——法官裁决约六周后（1993 年 3 月）发布，伯克利 "following Monday morning" 即下周一在加州起诉；1992 年 6 月说法无一手来源支持，系时间线混淆
- [考据脚注：诉讼期间代码清理的辨析] 经 2026-07-28 联网核查 McKusick 1999 一手原文确认，诉讼期间的 “代码清理” 存在三个需辨析的误区——① **误区一：诉讼加速了代码清理**——实际相反，诉讼使 CSRG 成员被拘传作证、撰写数百页法律材料，代码工作停滞；真正的代码清理在 1989-1991 年诉前完成；② **误区二：和解协议要求大规模代码重写**——实际仅 3 个
- [考据脚注：FreeBSD 2.0 发布日期] FreeBSD 2.0 Release Notes 未在文档开头明确标注发布日期，但 freebsd.db freebsd-src 仓库中 RELENG_2_0_5_ALPHA 标签创建于 1995-05-29、RELENG_2_0_5_RELEASE 标签创建于 1995-06-10，Jordan K. Hubbard 于 1995-01-04 提

## 文献

- USL v. BSDi, Civil Action No. 92-1667（D. N.J. 1992）；Unix System Laboratories, Inc. v. Berkeley Software Design, Inc., 832 F. Supp. 790 (D.N.J. 1993)[Z/OL]. 美国新泽西联邦地区法院，1993-09-08. <https://law.justia.com/cases/federal/district-courts/FSupp/832/790/1428569/> [2026-07-28]；McKusick, K. (1999) "Twenty Years of Berkeley Unix"；Quinlan, D. (1992) "The USL v. BSDi Case" ［A］
- Unix System Laboratories, Inc. v. Berkeley Software Design, Inc., 832 F. Supp. 790 (D.N.J. 1993)[Z/OL]. 美国新泽西联邦地区法院，1993-09-08. <https://law.justia.com/cases/federal/district-courts/FSupp/832/790/1428569/> [2026-07-28]；Cal. Const. art. IX § 9（UC Regents 设立依据） ［A］
- BSDi 应诉文件；伯克利反诉状；McKusick, K. (1999) "Twenty Years of Berkeley Unix"（当事人一手叙述）；FreeBSD Project. "A Brief History of FreeBSD"（FreeBSD Handbook） ［B］<!-- NEWREF:2475 --><!-- NEWREF:2520 --><!-- NEWREF:2521 --><!-- NEWREF:2522 --><!-- NEWREF:2523 --><!-- NEWREF:2524 --><!-- NEWREF:2538 -->---## 文献增补与辩证校准（2026-08-08 追加）> 40.1-40.3 USL 诉讼进程：> - **文献增补（ref 3778）**：McKusick 亲述诉讼始末（Net/2 分发→BSDi 起诉→USL 反诉），40.1 起诉书要点的一手背景> - **文献增补（ref 3783）**：CSRG 时间线综述确认 1992 年诉讼与 1995 年 CSRG 解散的因果链> - **辩证校准（总纲 24.4）**：诉讼不是 BSD 史的断裂而是循环——4.4BSD-Lite 的发布是‘否定与再生’（24.4 原文），本章叙事应呈现循环结构
- McKusick, M. K. (1999) "Twenty Years of Berkeley Unix" [Z/OL]. O'Reilly Open Sources, ISBN 1-56592-582-6. <https://www.oreilly.com/openbook/opensources/book/kirkmck.html> [2026-07-28]；USL v. BSDi, Civil Action No. 92-1667（D. N.J. 1992-1994）；1994 年和解协议；4.4BSD-Lite Release Notes（1994.6） ［A］
- FreeBSD 2.0 Release Notes [EB/OL]. The FreeBSD Project. <https://www.freebsd.org/releases/2.0/notes/> [2026-07-28]；McKusick, M. K. (1999) "Twenty Years of Berkeley Unix" [Z/OL]. O'Reilly Open Sources, ISBN 1-56592-582-6. <https://www.oreilly.com/openbook/opensources/book/kirkmck.html> [2026-07-28]；4.4BSD-Lite Release Notes（CSRG, 1994.6）；freebsd.db freebsd-src 仓库 1994-1995 年 commit 历史；FreeBSD COPYRIGHT 文件 [EB/OL]. The FreeBSD Project. <https://raw.githubusercontent.com/freebsd/freebsd-src/main/COPYRIGHT> [2026-07-28]（含 4.4BSD-Lite 原始 4-clause BSD License 文本与 1999-07-22 William Hoskins 广告条款删除声明）；Rodney W. Grimes. This is the official 4.4 Lite copyright. freebsd-src [DB/OL]. 1994-09-11T07:53:28Z. 18bc25c1733fd8cd749502ec5ec9333e672c7397 ［A］[^doubt-resolved-241]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解
