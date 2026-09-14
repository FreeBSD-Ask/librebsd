---
chapter: 第 43 章
id: CH43
volume: 第02卷-伯克利的岁月
---

# 第 43 章 USL v. BSDi 和解协议原文翻译

## 要点

- 1992 年，AT&T 的子公司 UNIX System Laboratories（USL）向新泽西联邦地区法院起诉 Berkeley Software Design, Inc.（BSDi）与加州大学董事会（The Regents of the University of California），指控 BSDi 销售的 BSD/386 操作系统与 CSRG 发布的 Networking Release 2（NET-2）侵犯 USL 对 UNIX 的版权（回源据 43.1 节）
- 1994 年 2 月 4 日签署的 USL v. BSDi 和解协议包含八项关键条款：（1）4.4BSD-Lite 将不含任何争议文件地发布；（2）加州大学鼓励现有 NET-2 许可证持有者迁移至 4.4BSD-Lite；（3）加州大学停止分发特定的争议文件；（4）USL 给予争议文件的现有用户三个月宽限期（可在宽限期内继续使用）；（5）加州大学分发的部分文件须附加 USL 版权声明；（6）USL 分发的部分文件须附加加州大学版权声明；（7）USL 允许特定文件的免费分发；（8）加州大学不得积极协助任何质疑 USL 对特定文件权利的法律行动（回源据 43.2 节）
- 2026 年 8 月 10 日，美国第二巡回上诉法院三名法官一致裁定驳回 Xinuos（SCO 后继者）对 IBM 的版权上诉，维持纽约南区联邦地区法院的即决判决。核心理由为诉讼时效已过——法院认定 Xinuos 的实质争议是 Project Monterey 代码的所有权归属（而非许可条款），IBM 在 2001 年即已公开将 Monterey 代码用于产品，诉因距今已逾 20 年。〔注：本条目句尾“2026 年”后原文截断，残句按核查报告建议删除，裁决后影响见辨析行〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3729] 卷“第03卷-伯克利学术文化外溢影响”第 43 章，匹配置信度 folder，原因：folder 第42章
- [DB:references_fulltext:chapter_matches:chmatch_3730] 卷“第03卷-伯克利学术文化外溢影响”第 43 章，匹配置信度 folder，原因：folder 第42章
- [DB:references_fulltext:chapter_matches:chmatch_1554] 卷“第03卷-伯克利学术文化外溢影响”第 43 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

- 总纲第 13 条——法律与道德是利益分配：和解协议以法律形式划定 UNIX 代码归属与市场边界，是 USL 与 BSDi/加州大学之间的利益再分配契约
- 总纲第 3 条——不存在进步，只有权力再分配：诉讼与和解并非技术进步叙事，而是 UNIX 资产权力结构的重组
- 总纲第 4 条——分离聚合是永恒规律：和解催生 4.4BSD-Lite，代码经 FreeBSD、NetBSD、OpenBSD 三大 fork 分离聚合延续至今
- 专题语（不设条号）：“技术优秀不等于商业成功”（本卷命题 24.5）在本章显现为 BSD 赢得法律清白却失去市场窗口的错位（详见文献增补与辩证校准节的辩证校准条目）

## 辨析

- [考据脚注] 案件号 832 F. Supp. 790（D.N.J. 1993）经联网复核确认（案件号经 US Courts PACER 系统核验；academic.ru/rightwiki.org 镜像类来源已按禁引规则剔除，判例细节待 CaseText/Justia 判例库复核），法官 Dickinson R. Debevoise 的否定裁决于 1993 年做出——Debevoise 曾指示 USL 仅基于六个可确证版权的文件重诉否则驳回，并驳回其禁制令动议（回源据 43.1 节）
- [考据脚注] 八项条款的精确措辞与编号——Groklaw PDF 迁移至 groklawstatic.ibiblio.org 后，各来源对条款的编号与措辞略有差异，本考据综合 Groklaw 存档 + Kolstad 公告 + softwarelicenses.org 多源表述，以实质法律效力为准，非逐字引用原始 PDF。
- [考据脚注] 和解协议的“保密十年”与“2004 年公开”时间线——经 Groklaw 存档（groklawstatic.ibiblio.org）与 California Public Records Law 公开记录核验：协议 1994 年签署时约定保密十年，2004 年 11 月经公记录法公开（Groklaw 于 2004-11 发布协议 PDF，见文献增补节）。
- Xinuos 裁决对 BSD 历史的间接意义在于：它结束了 SCO saga 对“UNIX 代码流入 Linux”这一命题的持续炒作，从而间接消除了围绕 BSD 代码合法性的残余“FUD”——尽管 4.4BSD-Lite 的法律清白自 1994 年从未被成功挑战，但 SCO saga 的存在使得“UNIX 代码侵权”作为一个法律概念持续具有威慑力。2026 年裁决后，这一威慑力实质上消散。需注意：上述意义系间接影响，BSD 法律清白本身自 1994 年和解即已确立，并不依赖 2026 年裁决。

## 文献

- UNIX System Laboratories v. Berkeley Software Design, Inc., 832 F. Supp. 790 (D.N.J. 1993). McKusick, M. K. 《Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable》. Open Sources: Voices from the Open Source Revolution. O'Reilly, 1999. Kolstad, R. “USL vs. BSDI Lawsuit Settled.” Usenet posting, comp.unix.bsd, 6 February 1994. History of FreeBSD – Part 2: BSDi and USL Lawsuits. FreeBSD Forums, 20 October 2020.<!-- NEWREF:2546 -->

---

## 文献增补与辩证校准

> 43.2-43.3 和解协议条款与影响：
> - **文献增补（ref 3778）**：McKusick 记载和解后 4.4BSD-Lite 发布——43.3 “BSD 法律基石”的一手叙述 [存疑脚注：McKusick 原文将 4.4BSD-Lite 发布记为 1992 年系对开发起始的简化表述；经考据确认 4.4BSD-Lite 实际于 1994-06 发布（USL v. BSDi 诉讼 1994-01 和解后）]
> - **文献增补（ref 3779）**：McKusick 视频讲座 Part I 详述诉讼至 4.4BSD-Lite 全过程
> - **辩证校准（总纲 24.5）**：和解不是“技术胜利”而是商业/法律权力运作——“技术优秀不等于商业成功”（24.5），BSD 赢得诉讼但失去市场，本章如实记录这种错位
- USL v. BSDi Settlement Agreement (1994). University of California Office of the General Counsel, released under California Public Records Law, November 2004. Groklaw 存档（groklawstatic.ibiblio.org/pdf/USLsettlement.pdf，2004-11 发布）. McKusick, M. K. 《Twenty Years of Berkeley Unix》. Open Sources. O'Reilly, 1999. Kolstad, R. 1994-02-06 和解公告（dnull.com 存档）. softwarelicenses.org USL v. BSDi 案件综述.〔原禁引来源已删除。〕<!-- NEWREF:2542 -->
- Xinuos, Inc. v. International Business Machines Corporation and Red Hat, Inc., No. 25-1073 (2d Cir. Aug. 10, 2026)[Z/OL]. 美国第二巡回上诉法院 Summary Order. <https://storage.courtlistener.com/recap/gov.uscourts.ca2.aa1a7e3d-39a0-439a-b5e1-8abbc67cb8a2/gov.uscourts.ca2.aa1a7e3d-39a0-439a-b5e1-8abbc67cb8a2.66.0.pdf> [2026-08-25]；Sharwood, S. Ancient who-owns-Linux case now has one foot very deep in the grave[N/OL]. The Register, 2026-08-24. <https://www.theregister.com/software/2026/08/24/ancient-who-owns-linux-case-now-has-one-foot-very-deep-in-the-grave/> [2026-08-25]
