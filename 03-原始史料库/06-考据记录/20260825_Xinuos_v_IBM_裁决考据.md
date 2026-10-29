# Xinuos v. IBM 第二巡回上诉法院裁决考据

## 基本信息

- **案号**：No. 25-1073（第二巡回上诉法院）
- **裁决日期**：2026 年 8 月 10 日
- **裁决法院**：美国第二巡回上诉法院（United States Court of Appeals for the Second Circuit）
- **法官组成**：Guido Calabresi、Steven J. Menashi、Sarah A. L. Merriam（三名法官一致裁定）
- **裁决类型**：Summary Order（不具判例效力，但可引用）
- **裁决结果**：维持纽约南区联邦地区法院（Seibel 法官）的即决判决，驳回 Xinuos 对 IBM 的版权上诉
- **裁决书全文**：`04-现代研究文献/03-文献下载/01-pdf/20260825_Xinuos_v_IBM_Second_Circuit_Summary_Order_25-1073.pdf`（187 KB）
- **裁决书在线链接**：<https://storage.courtlistener.com/recap/gov.uscourts.ca2.aa1a7e3d-39a0-439a-b5e1-8abbc67cb8a2/gov.uscourts.ca2.aa1a7e3d-39a0-439a-b5e1-8abbc67cb8a2.66.0.pdf>

## 案件背景

### 起源：Project Monterey（1998-2001）

- 1998 年，IBM、Santa Cruz Operation（SCO）、Intel、Sequent 等联合启动 Project Monterey，目标是开发能在多种处理器架构（含 IA-64 Itanium 和 IBM POWER）上运行的 UNIX 系统
- SCO 贡献了 x86 相关代码，IBM 贡献了 AIX 相关代码，双方签署 Joint Development Agreement（JDA）约定相互授权使用对方贡献的代码
- 随着 Linux 迅速崛起，IBM 于 2001 年终止参与 Project Monterey，并将部分 Monterey 代码贡献给 Linux

### SCO v. IBM 阶段（2003-2021）

- 2003 年 3 月，SCO Group（Caldera 更名后）起诉 IBM，最初索赔 10 亿美元，后升至 50 亿美元，指控 IBM 将 Project Monterey 中的 UNIX 代码非法贡献给 Linux
- 2007 年，SCO Group 申请破产保护（Bankr. D. Del.，案号 07-bk-11337）
- 2007 年 8 月 10 日，犹他联邦地区法院 Judge Kimball 裁定 Novell（而非 SCO）保留 UNIX 版权（SCO v. Novell, 2:04-cv-00139）
- 2011 年 1 月，SCO Group 破产程序中向 Xinuos（当时名为 UnXis）出售 Unix 业务资产，但资产购买协议（APA）明确排除了针对 IBM 等公司的诉讼权利
- 2021 年 8 月，SCO 后继实体之一 TSG Group 与 IBM 以 1425 万美元和解

### Xinuos v. IBM 阶段（2021-2026）

- 2021 年 3 月，Xinuos 对 IBM 和 Red Hat 提起新的诉讼，主张版权侵权和反垄断
- 2024 年 4 月，纽约南区联邦地区法院（Seibel 法官）驳回版权主张
- 2025 年 4 月，Xinuos 放弃反垄断部分，仅保留版权上诉
- 2026 年 6 月 22 日，第二巡回上诉法院开庭审理
- **2026 年 8 月 10 日，第二巡回上诉法院维持原判，驳回上诉**

## 裁决核心要点

1. **诉讼时效已过**：法院认定 Xinuos 的版权主张实质上是对代码所有权的争议（而非许可争议），适用更短的诉讼时效。IBM 在 2001 年即已公开将 Monterey 代码用于其产品，Xinuos 的诉因在当时即已产生，远早于诉讼时效期限
2. **许可 vs 所有权区分**：Xinuos 试图将案件定性为"许可条款争议"以规避诉讼时效，但法院认定实质争议是"代码所有权归属"，不适用许可争议的较长时效
3. **剩余论点"毫无根据"**：法院对 Xinuos 的其余论点判定为"without merit"
4. **2011 年资产购买协议的范围**：APA 明确排除了针对 IBM 的诉讼权利，Xinuos 所购资产不包括旧的 SCO 诉权

## 后续动态

- 2026 年 8 月 24 日，The Register 报道 Xinuos 拟申请 en banc 全院重审（由全体法官而非三人小组审理）
- 法院批准 en banc 重审的概率极低：据 Kaplan 律所统计，第二巡回上诉法院历史上批准此类重审的比例不足 0.03%
- 若 en banc 申请被驳回，这起横跨 28 年的 UNIX 版权诉讼 saga 将正式终结

## 与本书的关联

### 与 USL v. BSDi 的对比

| 维度 | USL v. BSDi（1992-1994） | Xinuos v. IBM（2021-2026） |
|------|--------------------------|---------------------------|
| 原告 | UNIX System Laboratories（AT&T 子公司） | Xinuos（SCO 后继者） |
| 被告 | BSDi + 加州大学董事会 | IBM + Red Hat |
| 争议焦点 | NET-2 是否含 AT&T UNIX 代码 | Project Monterey 代码是否被非法贡献给 Linux |
| 版权归属关键 | AT&T 32V 版权登记瑕疵 | Novell 保留 UNIX 版权（2007 裁定） |
| 结果 | 1994 年和解（3 文件删除，约 70 文件修改） | 2026 年上诉驳回（诉讼时效已过） |
| 对生态的影响 | 4.4BSD-Lite 发布，BSD 完全自由化 | UNIX 版权诉讼 saga 终结，Linux 法律风险消除 |

### 在本书中的位置

- 作为第 41--43 章 USL 诉讼叙事的历史延续与终章
- 直接关联第 42 章 42.10 节（SCO v. IBM 对比）
- 直接关联第 43 章 43.3 节（后续影响 1994--2026）

## 查证来源

- **一手来源**：第二巡回上诉法院 Summary Order 25-1073 裁决书全文（PDF 已下载入库）
- **二手来源**：
  - The Register 2026-08-24 报道（Simon Sharwood）
  - Techzine 2026-08-24 报道（Mels Dees）
  - Slashdot 2026-08-24 汇总
  - OpenNet 2026-08-24 俄语报道
  - Habr 2026-07-22 案件背景综述（Selectel 博客）
  - Slashdot 2000-05-05 SCO 总裁访谈（历史背景）

## 交叉验证方法

- 裁决书 PDF 全文与媒体报道交叉验证：裁决日期（2026-08-10）、法官组成（Calabresi/Menashi/Merriam）、案号（25-1073）、下级法院法官（Seibel）均一致
- 案件历史与已知公开记录（SCO v. Novell 2007 裁决、SCO 破产 2007、TSG Group 和解 2021）一致
- 裁决书中的 JDA 条款引用与 Project Monterey 公开历史记录一致

## 存疑判定依据

- 裁决书为 Summary Order，不具判例效力，但作为历史事实记录具有充分证据强度
- Xinuos 是否实际提交 en banc 申请、以及法院是否批准，截至 2026-08-25 尚无公开法院记录，需后续跟踪
- SCO v. IBM 原案（2:03-cv-00294, D. Utah）的完整案卷尚未全部数字化公开，部分细节依赖于二手报道

## GB/T 7714-2015 著录

Xinuos, Inc. v. International Business Machines Corporation and Red Hat, Inc., No. 25-1073 (2d Cir. Aug. 10, 2026)[Z/OL]. 美国第二巡回上诉法院. <https://storage.courtlistener.com/recap/gov.uscourts.ca2.aa1a7e3d-39a0-439a-b5e1-8abbc67cb8a2/gov.uscourts.ca2.aa1a7e3d-39a0-439a-b5e1-8abbc67cb8a2.66.0.pdf> [2026-08-25].

Sharwood, S. Ancient who-owns-Linux case now has one foot very deep in the grave[N/OL]. The Register, 2026-08-24. <https://www.theregister.com/software/2026/08/24/ancient-who-owns-linux-case-now-has-one-foot-very-deep-in-the-grave/> [2026-08-25].

Dees, M. A stale Unix case haunts IBM: Xinuos demands a new hearing[N/OL]. Techzine, 2026-08-24. <https://www.techzine.eu/news/privacy-compliance/143772/a-stale-unix-case-haunts-ibm-xinuos-demands-a-new-hearing/> [2026-08-25].