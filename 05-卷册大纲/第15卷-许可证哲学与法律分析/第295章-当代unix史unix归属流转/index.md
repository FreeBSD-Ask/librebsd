---
chapter: 第 295 章
id: CH295
volume: 第15卷-许可证哲学与法律分析
---

# 第295章 当代unix史unix归属流转

## 要点

- 2021 年 3 月，Xinuos（SCO Group 破产后于 2011 年收购 Unix 业务资产的后继者，当时名为 UnXis）对 IBM 和 Red Hat 重新提起版权与反垄断诉讼，主张 IBM 将 Project Monterey 代码非法贡献给 Linux 违反了 JDA 非排他许可条款。2024 年 4 月纽约南区联邦地区法院（Seibel 法官）驳回版权主张，2025 年 4 月
- 2003 年 SCO v. IBM 提起诉讼后，SCO Group 2003 年 12 月向大批 UNIX 许可用户发出认证函（certification letters），要求其证明未将 UNIX 代码贡献给 Linux、未违反许可；2004 年 3 月 3 日 SCO 同日对两家企业提起诉讼，将诉讼战线从“起诉 IBM 供应方”扩展至“起诉用户方”：**SCO Group, Inc. v. A**
- 2026 年 8 月 10 日，第二巡回上诉法院驳回 Xinuos（SCO 后继者）对 IBM 的版权上诉，核心理由为诉讼时效已过。此裁决使 SCO 诉讼 saga 的所有延伸战线（AutoZone 和解、DaimlerChrysler 撤诉、Red Hat 中止、Xinuos 被驳回）全部终结。从 2003 年 SCO v. IBM 起至 2026 年 Xinuos 被驳回，23 年间 SCO

## 史观

- 自反性：许可证哲学辩论本身需要被审视——‘自由’的定义是形式主义化的
  - 文献：[DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）
- 总纲第 5 条偶然性——SCO saga 历经 28 年（1998-2026）、四代公司（SCO→Caldera→TSG Group→Xinuos）、多轮诉讼，最终因 1998 年 JDA 中的一条诉讼时效条款（§22.3）和 2011 年 APA 中的一条诉权排除条款而终结，偶然合同细节决定宏观历史走向；总纲第 6 条和解优于斗争——2021 年 TSG Group 与 IBM 以 1425 万
- 总纲第 10 条边缘者——SCO 起诉用户（AutoZone 为中大型企业、DaimlerChrysler 为跨国巨头）的“用户侧打击”策略，试图以诉讼威胁迫使 Linux 商业用户支付许可费（SCOsource 商业模式）；此策略与 USL v. BSDi 起诉伯克利（本卷 40 章）的“打击供应侧”策略形成对照——SCO 的战线扩展反而引发 Linux 用户社区的联合抗辩与合规自证，强化了 G
- 总纲第 12 条法律结构——SCO 用户侧诉讼的失败证明：在开源许可证（GPL/BSD）生态中，以“版权许可费”为商业模式的诉讼威胁，因代码溯源不清（UNIX 代码实际归属 Novell，本卷 82.8）与社区防御组织化（Groklaw、SFLC）而无法成立——许可证的“结构信任”（代码可自由使用）在司法上获得最终确认，BSD/Linux 生态得以在 2003-2010 年法律风暴后继续扩张
-
- 总纲第 7 条连续性——BSD 的“法律清白认证流程”（本卷 41.7，1994 和解后确立）在 SCO 风暴中经受压力测试并获得确认：1994 年和解的“3 删 70 改 + Lite 发布”为 BSD 提供了可追溯的代码边界，使 SCO 无法将 UNIX 代码追溯至 BSD 系系统——法律结构的先见之明在十多年后显现其保护价值
- 辨析：须避免“BSD 完全免疫 SCO”的过度表述——SCO

## 辨析

- 1994 年 USL v. BSDi 和解协议条款严格保密，公开信息主要来源于双方新闻稿与法院 dismissal 文书；部分二手资料（如 McKusick 1999 年论文、Kirk McKusick 个人网站问答）提及和解条款包含 “USL 不追究 4.4BSD-Lite 及其衍生版本” 的承诺，但具体法律文本从未公开。本子节采用 “和解条款保密，公开信息显示 4.4BSD-Lite 成为诉讼
- 部分二手资料称 “Novell 以 8,000 万美元将 UnixWare 与 UNIX 商标售予 SCO”，部分称 “6,000 万美元加未来版税”。考据结论：原始 Asset Purchase Agreement（APA）条款在 2004 年 Novell v. SCO 案中部分披露，确认基础价格为 8,000 万美元加 UNIX 版税分成，本子节采用此表述。
- 部分二手资料称 Project Monterey “因 Linux 兴起而失败”，但项目失败的直接原因是 Itanium（IA-64）芯片延迟发布（原定 1999 年，实际 2001 年）与 Linux 在 Intel x86 上的性能跨越；Linux 兴起是外部环境，Itanium 延迟与 IBM 内部资源重新分配是直接原因。本子节采用 “Itanium 延迟与 Linux 兴起多重因素” 的辩
- 部分二手资料称 UnixWare 7 基于 “SVR5 内核”，但 SVR5 实际是 SCO 内部对 UnixWare 2.x 与 OpenServer 5.x 合并版本的命名，未由 X/Open 或 Open Group 正式标准化为 “SVR5” 标准。本子节采用 “UnixWare 7 引入 SVR5 内核（SCO 内部命名）” 的限定性表述。
- 辨析：本章辨析的核心张力在于“自反性：许可证哲学辩论本身需要被审视——‘自由’的定义是形式主义化的”的边界条件，各子节辨析字段已展开，卷面综合辨析在正文撰写阶段横向汇总（据本章概述史观整理）
  - 文献：[DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）

## 文献

- [DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）
- Xinuos, Inc. v. International Business Machines Corporation and Red Hat, Inc., No. 25-1073 (2d Cir. Aug. 10, 2026)[Z/OL]. 美国第二巡回上诉法院 Summary Order；Sharwood, S. Ancient who-owns-Linux case now has one foot very deep in the grave[N/OL]. The Register, 2026-08-24；Dees, M. A stale Unix case haunts IBM: X
- SCO GROUP, Inc. v. AutoZone, Inc.（D. Nev. CV-S-04-0237，2004-03-03）[Z/OL]. 美国内华达联邦地区法院；SCO GROUP, Inc. v. DaimlerChrysler Corp.（Oakland County Cir. Ct. 2004）[Z/OL]. 美国密歇根州法院；Society for Computers & Law. The SCO Open Source Litigation Saga（2011） ［A］
- SCO GROUP, Inc. v. Red Hat, Inc.（D. Del. 2003）[Z/OL]. 美国特拉华联邦地区法院；SCO GROUP, Inc. v. AutoZone, Inc.（D. Nev. CV-S-04-0237，2004）；SCO v. DaimlerChrysler（Mich. 2004）；TSG Group, Inc. bankruptcy, 07-bk-11337（Bankr. D. Del. 2007）；Groklaw 档案 ［A］
- Xinuos, Inc. v. IBM, No. 25-1073 (2d Cir. 2026) Summary Order [2026-08-25]
- 文献：Groklaw 档案；FreeBSD/NetBSD 邮件列表 2003-2005 记录；本卷 41.7（BSD 代码法律清白认证流程）、81 章（4.4BSD-Lite 发布）、82 章（UNIX 版权归属争议） ［A］
## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

- 著录. SCO Group, Inc. v. Auto Zone, Inc., CV-S-04-0237 (D. Nev. 2004)——SCO 诉 Linux 用户端案件（法院 2026-08-05 更正为 D. Nevada，法官 Robert C. Jones）[Z]. 2004.

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP476（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Warren Toomey 自述 1982 年高中暑期在澳大利亚首次接触 Unix，其后在大学历经 AT&T 与 BSD 两个世界，最终在 386BSD 出现后转向可运行于廉价硬件的 BSD 系统。（BSD Now EP476，[107.28-529.28]，L1）
- Toomey 于 1994 年创办 PDP Unix Preservation Society，后因范围超出单一架构而更名为 Unix Heritage Society，三十年间以个人名义维持网站、邮件列表与档案，成为 Unix 历史保存的枢纽。（BSD Now EP476，[1222.4-1491.58]，L1）
- Toomey 指出 Unix 与 IT 历史保存的最大障碍是版权顾虑，其个人持有的隐藏档案含 System V、Solaris、Data General 等源码而无法公开，呼吁建立类似国会图书馆或计算机历史博物馆的合法保存机制。（BSD Now EP476，[1691.42-1834.3]，L1）
- Toomey 重述 Ken Thompson 1984 年编译器后门实验，指出该实验预先揭示了供应链攻击的逻辑，并提及 EuroBSDCon 上有讲者将该思想应用于 make。（BSD Now EP476，[2277.94-2364.34]，L1）

**史料**：

- Toomey 关于 1982 年接触 Unix、1986 年获得 Pyramid 90x、386BSD 迁移及 SunOS 3.5 经历的叙述，属当事人一手口述史料。（BSD Now EP476，[107.28-529.28]，L1）
- Toomey 讲述 PDP-7 Unix 源码的恢复过程：先由 Dennis Ritchie 保存单页源码，多年后有人在家中找到含 PDP-7 内容的文件夹，另有一半源码在一位已故 IT 人士的遗物中被发现，纯属偶然。（BSD Now EP476，[2564.52-2641.12]，L1）

**史观**：

- 总纲10 动手者创造历史：Toomey 以个人之力维持 Unix 档案三十年，并强调旧软件的价值在于其承载的思想而非代码本身，属动手者创造历史的典型例证。（BSD Now EP476，[2117.22-2184.1]，L1）
- 总纲5 没有必然性，只有偶然性：PDP-7 Unix 源码的恢复依赖两次偶然发现，印证历史保存并无必然性，只有具体事件与偶然条件的叠加。（BSD Now EP476，[2591.6-2641.12]，L1）

**辨析**：

- Toomey 对 Unix 历史保存困境的归因集中于版权，但软件格式老化、磁带读取设备稀缺等物质条件同样是关键因素，需多源对照。（BSD Now EP476，[1691.42-1974.38]，L3）
- 转写中关于 1994 年创办 Unix Heritage Society 与更早 PDP Unix Preservation Society 的时间细节，需与该组织档案及网站历史核对。　[考据脚注] TUHS 前身更名时间与 1994 年创办说需查 tuhs.org 与早期邮件列表档案。（BSD Now EP476，[1414.3-1471.42]，L4）

**文献**：

- [BSD Now EP476] Pennington J. BSD Now: 476: Warren Toomey interview[EB/OL]. (2022-10-13)[2026-08-15]. <https://www.bsdnow.tv/476>.

<!-- /PODCAST_REVIEW -->

## 史料

- [DB:historical_claims:claim] 关键词行级挖掘素材线索 295.7-关键词行级挖掘素材线索（1 条，CL-RM 段，见 295.7-关键词行级挖掘素材线索.md）

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

