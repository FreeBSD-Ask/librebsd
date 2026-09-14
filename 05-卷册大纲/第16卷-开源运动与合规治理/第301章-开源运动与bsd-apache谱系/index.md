---
chapter: 第 301 章
id: CH301
volume: 第16卷-开源运动与合规治理
---

# 第 301 章 开源运动与 BSD-Apache 谱系

## 节目录

- [301.5 Apache 软件基金会：BSD 许可证的 Apache 谱系](301.5-Apache-软件基金会-BSD-许可证的-Apache-谱系-Apache.md)
- [301.6 Netscape 开源——1998 年的标志性事件](301.6-Netscape-开源-1998-年的标志性事件.md)
- [301.7 GitHub 与 PR 模式——2008 年后的协作变革](301.7-GitHub-与-PR-模式-2008-年后的协作变革.md)
- [301.8 Apache 软件基金会 BSD 许可证下的治理模式](301.8-apache软件基金会在bsd许可证下的治理模式分析.md)
- [301.9 外部批评与反对者——BSD 在开源叙事中的边缘化](301.9-外部批评与反对者-BSD-在开源叙事中的边缘化.md)

（2026-09-11 整改按磁盘实况登记：本章磁盘仅存 301.5–301.9 五节，301.1–301.4 为节号缺口，待后续规划处置）

## 史料

- [DB:research_notes:blocks:432] 关键词“开源运动”命中：参见 三、开源运动与许可证 下 ESR 相关条目。本次俚语考证（KISS、DRY、YAGNI 原则）〔待核：原文截断，后文待回源〕
- [DB:research_notes:blocks:1227] 关键词“开源运动”〔待核：原文截断，后文待回源〕
- [DB:research_notes:blocks:1595] 关键词“开源运动”命中：以下文献为第 64-71 章（FreeBSD 6.x 到 8.x 版本、jemalloc、PF 防火墙、CVS→SVN …

- [WEB:cnet.com IBM offers 500 patents] IBM 2005 年向开源社区开放 500 项软件专利（免版税，限 OSI 定义项目）；此前 2004 年获 3248 项美国专利连续 12 年第一；SCO 诉 IBM（2003-03-07）背景下的专利战略转折
- [WEB:NBER w19394] Patent Commons, Thickets, and Open Source Software Entry（NBER 工作论文）：IBM 专利共享（The Commons）与 1999-2005 开源初创进入的实证研究；SCO 诉讼抬高开源法律风险感知——专利丛（patent thickets）对 BSD/Apache 许可证谱系的学术一手分析
- [WEB:fortune.com Microsoft takes on the free world] Fortune 2007 报道（一手）：Microsoft 宣称 FOSS 侵犯其 235 项专利；2005 年 IBM/Sony/Philips/Novell/Red Hat/NEC 组建 Open Invention Network（OIN）专利防御联盟——开源合规治理史关键一手记录

## 要点

- Apache 软件基金会（ASF）于 1999 年 3 月成立，前身是 1995 年的 Apache Group（Brian Behlendorf（布莱恩·贝伦多夫）、Cliff Skolnick 等维护 NCSA HTTPd 衍生的 Apache 服务器）；ASF 组织模式借鉴 BSD 精英评审模式（committer、PMC、member 三层）；ASF 是除 FSF 与 OSI 外最具影响力的开源组织
- Apache 许可证 1.0（2000 年）基于 BSD 许可证修改，1.1（2001 年）去除 advertising 条款，2.0（2004 年）加入专利授权条款；Apache 2.0 与 BSD 三条款在精神上同属宽松许可证阵营，但 Apache 2.0 加入专利保护；二者在 OSI 认证中并列
- Apache 对 BSD 开源传统的继承：(1) 宽松许可证哲学；(2) 精英评审模式（committer/PMC/member）；(3) 基金会治理（轻治理）；Apache 对传统的发展：(1) 加入专利授权；(2) 项目孵化器（Incubator）；(3) 项目独立治理（每个顶级项目独立 PMC）；Apache 模式成为现代开源基金会的主流范式
- Apache 项目生态与 BSD 系统的交织：(1) Apache HTTP Server 长期是 FreeBSD 默认 Web 服务器；(2) Yahoo! 早期 FreeBSD + Apache 是典型组合；(3) FreeBSD Ports 中 Apache 项目占重要位置；(4) Apache 项目大量在 BSD 系统上开发与测试
- Netscape 1998 年 1 月开源 Navigator 的背景：(1) Microsoft IE 通过 Windows 捆绑抢占浏览器市场；(2) Netscape 市场份额从 80% 跌至 50%；(3) CEO Jim Barksdale 阅读 Raymond CatB 后决定开源；(4) 开源是商业策略而非哲学选择；1998 年 3 月 31 日 Mozilla 代码正式发布（mozilla.org）

## 史观

- 总纲第 4 条——分离聚合是永恒规律，Apache 谱系自 BSD 开源传统的分离与扩散（ASF 组织模式借鉴 BSD 精英评审为分离后的再聚合形态）〔注：原挂“总纲第 7 条——BSD 与 UNIX 谱系的连续性”经 25 条权威表核验不符（第 7 条为理论必须自反），按 R2140 先例改挂并留原挂注〕
  - 辨析：ASF 是否真借鉴 BSD 模式，需查早期组织文档
  - 文献：ASF 官方历史；Apache Group 早期文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
