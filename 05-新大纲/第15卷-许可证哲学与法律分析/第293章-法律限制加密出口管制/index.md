---
chapter: 第 293 章
id: CH293
volume: 第15卷-许可证哲学与法律分析
---

# 第293章 法律限制加密出口管制

## 史料

- [WEB:congress.gov H.Rept.106-117] 美国国会报告 SAFE Act（一手）：1990s 加密出口管制立法辩论；56-bit 以上加密出口许可例外与 Wassenaar 瓦森纳安排（1996，39 国）多边管制框架
- [WEB:9th Cir. Bernstein v. United States, 176 F.3d 1132 (1999)] 第九巡回法院判决（一手）：加州大学伯克利研究生 Daniel J. Bernstein 的 Snuffle 加密源码属第一修正案保护的言论；出口管制构成事前限制（prior restraint）；EFF 代理诉讼；该判决促成 2000 年美国加密出口管制放宽
- [WEB:Bernstein v. US 案件史] Bernstein I（922 F. Supp. 1426, 1996-04-15 N.D.Cal. Patel 法官）/ Bernstein II（945 F. Supp. 1279, 1996-12-09）/ Bernstein III（176 F.3d 1132, 1999-05-06 9th Cir. en banc 重审令 192 F.3d 1308）

## 要点

- 美国国务院依据《国际武器贸易条例》（ITAR）将含加密功能的软件列入“军需品清单”，1990 年代初 Kerberos、PGP、SSL 等含加密代码的 BSD 软件一度被视为受管制物项，源代码出口需逐案申请许可
- 1996 年 11 月 15 日克林顿政府签署第 13026 号行政命令（Executive Order 13026），修正第 12981 号行政命令（EO 12981，原签署于 1995 年 12 月 5 日），将非军用加密软件出口管制由国务院（ITAR）移交至商务部（EAR），BSD 加密相关代码出口门槛降低，但强加密仍需一次性审查 [已核证：依据 Federal Register Vol. 61 No. 224（1996-11-19）载入的 EO 13026 原文，明确"Executive Order 12981, as amended by Executive Order 13020 of October 12, 1996, is further amended as follows"，且 EO 13026 签署日为 1996 年 11 月 15 日]
- 1990 年代 FreeBSD 与 OpenBSD 在国际镜像站点发布加密代码（如 Kerberos、SSL、IPsec）时面临法律不确定性，部分镜像站点（如南非、俄罗斯镜像）需个案评估，影响了 BSD 加密栈在境外部署的时序
- ITAR 与 EAR 史料散落于美国国务院、商务部档案与 BSD 邮件列表，部分内部审批文件未解密，需通过公开判例与镜像站点时序交叉验证
- **Junger v. Daley**（后被告变更为商务部长，称 Junger v. Walker），原告 Peter D. Junger 为凯斯西储大学（Case Western Reserve University）法学院教授，教授“计算机与法律”课程并撰写相关教材，1996 年欲在个人网站上发布自己编写的加密程序源码以作教学示例；1996 年 11 月 15 日克林顿总统签发第 13026 号行政令，将非军用加密产品出口管制管辖权从国务院（ITAR）移交商务部（EAR 出口管理条例），商务部将加密软件（含源码）列为 5D002 管制物项，要求出口许可，网络发布视为出口；Junger 于 1996 年 8 月在北俄亥俄联邦地区法院（N.D. Ohio）起诉商务部长等，主张 EAR 对加密源码的管制违反第一修正案（言论自由）、构成事前限制且模糊过度宽泛，侵犯学术自由；1998 年 7 月地区法院（James S. Gwin 法官）判决政府胜诉——8 F. Supp. 2d 708 (N.D. Ohio 1998)，认定源码“本质上具功能性”、不构成受保护言论，管制属内容中立并适用中间审查（O'Brien 标准）

## 史观

- 国家政策，加密出口管制是国家主权对密码学技术流动的直接干预
  - 辨析：ITAR（22 CFR Part 121，国务院管辖）在 1996 年 11 月 15 日 EO 13026 签署前对加密软件有完整管辖权，11 月 19 日 Federal Register 公开后管辖权移交至 EAR（15 CFR Part 730-774，商务部管辖），边界以 EO 13026 签署
- 总纲第 12 条法律结构——Junger 案与 Bernstein 案（本卷 292.8）同属“代码即言论”宪法议题：政府以“功能性”为由管制加密源码出口，实质是把“能运行的表达”排除出第一修正案保护范围——法律结构的界定（什么是言论）直接决定技术交流的边界
- 辨析：一审判决与第九巡回 Bernstein 案（1999 年三人合议庭认定源码受第一修正案保护）直接冲突，形成巡回法院分裂；Gwin
- 总纲第 12 条法律结构——“源码是言论”的法律确认使加密源码的学术交流、开源分发获得宪法层面保障：BSD 社区在 1990 年代分发含加密代码的版本（如 OpenSSL、Kerberos、IPSEC 相关代码）长期受出口管制阴影，Junger 与 Bernstein 两案为此类分发提供了宪法抗辩基础——法律结构的确认直接降低了开源加密软件分发的法律风险
- 辨析：第六巡回判决的局限须标注——法院
- 总纲第 24 条许可证——加密源码从“管制物”到“受宪法保护的言论”的转变，是法律结构与技术实践互动的典型案例：BSD 系开源系统对加密组件的集成需求（技术实践）与法院对源码表达性的确认（法律结构）相互推动，最终以出口管制条例修订（2000）收束——法律、技术与政治三者的长时段互动在此具体呈现
- 辨析：须避免时代错置——2000 年条例修订后，加密软件出口管制主要针对军用与大规模杀伤性相关物项，
- 总纲第 12 条法律结构——Welte 案确认 GPL 作为“附条件许可”（conditional license）在版权法框架内的可执行性：违反条件（不提供源码）→ 许可自动终止 → 分发构成侵权 → 可申请禁令；此法律结构是 copyleft 机制在司法层面的首次实证，直接支撑 BSD 系软件“以许可证自治”的制度前提（BSD 许可证虽无 copyleft 义务，但同属“附条件许可”结构）
-

## 辨析

- ITAR（22 CFR Part 121，国务院管辖）在 1996 年 11 月 15 日 EO 13026 签署前对加密软件有完整管辖权，11 月 19 日 Federal Register 公开后管辖权移交至 EAR（15 CFR Part 730-774，商务部管辖），边界以 EO 13026 签署日为分界；“逐案申请”的实际审批率缺乏公开统计
  - 文献：ITAR 22 CFR Part
- 一审判决与第九巡回 Bernstein 案（1999 年三人合议庭认定源码受第一修正案保护）直接冲突，形成巡回法院分裂；Gwin 法官认为源码“功能性”优先于“表达性”，采纳政府在出口管制语境下的功能性论证——此立场与 Bernstein 案的 Patel 法官“计算机语言与德语法语无实质区别”形成鲜明对照，两案并读可见“代码是否言论”在 1990 年代末的美国司法界尚无共识 ［A］
- 文献：J
- 第六巡回判决的局限须标注——法院虽确认源码受第一修正案保护，但明确指出政府出于国家安全可依中间审查（intermediate scrutiny）施加合理限制，并援引“政府须证明损害真实存在而非臆测”的严格要求；判决未宣告加密出口管制本身违宪，仅确认审查标准；CRS 报告指出该判决与 Bernstein 案方向一致但与 Karn v. Department of State（第五巡回 1991）〔待核：原文截断，后文待回源〕
- 须避免时代错置——2000 年条例修订后，加密软件出口管制主要针对军用与大规模杀伤性相关物项，民用加密软件（含开源）基本自由分发；但“代码即言论”的宪法地位仍限于美国境内分析，其他国家（含中国）对加密软件与源码的管制另有法律框架，不能以美国判例推定他国结论；另须注意 Bernstein 案的撤回使第六巡回 Junger 判决成为援引主源，引用时应注明此判例格局 ［A］
- 文献：Junger v.
- 须辨析德国法与美国的差异——德国法院未直接回答“GPL 是合同还是许可”的英美法难题，而是以“违反许可条件=版权侵权”路径处理，避免了合同相对性问题；该路径后来被 Jacobsen v. Katzer（本卷 282.9）在美国联邦巡回法院呼应；另须说明 Welte 案判决书为德语，英文版为社区翻译，引用时应注明 ［A］
- 文献：WELTE v. Sitecom Deutschland GmbH,

## 文献

- ITAR 22 CFR Part 121；NSC 加密档案；Zimmermann 调查档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 293.1.2 1996 年管辖权移交与 EAR 时代

- 要点：1996 年 11 月 15 日克林顿政府签署第 13026 号行政命令（Executive Order 13026），修正第 12981 号行政命令（EO 12981，原签署于 1995 年 12 月 5 日），将非军用加密软件出口管制由国务院（ITAR）移交至商务
- Junger v. Daley, 8 F. Supp. 2d 708 (N.D. Ohio 1998)[Z/OL]. 美国北俄亥俄联邦地区法院. <https://casetext.com/case/junger-v-daley>；Executive Order 13026, 61 Fed. Reg. 58767（1996-11-15）；15 C.F.R. Part 730-774（EAR） ［A］
- Junger v. Daley, 225 F.3d 732 (6th Cir. 2000)[Z/OL]. 美国第六巡回上诉法院，2000-04-04. <https://casetext.com/case/junger-v-daley>；ACLU. In Legal First, Federal Appeals Court is Unanimous[EB/OL]. (2000-04-04). <<https://www.aclu.org/press-releases/legal-first-federal-appeals-court-unanimous-first-amendment-appli>
- Junger v. Daley, 225 F.3d 732 (6th Cir. 2000)；Bernstein v. U.S. Dept. of Justice, 176 F.3d 1132 (9th Cir. 1999)；Revisions to Encryption Items, 65 Fed. Reg. 2492（2000-01-12）；FreeBSD/OpenBSD/NetBSD 加密组件集成记录 ［A］
## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

- Junger v. Daley, 225 F.3d 732 (6th Cir. 2000)[Z]. 2000.

<!-- ROW_MINE: login-zazhi.articles.CL-15-055 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-15-055`；login 逐条遍历判定采纳）

2000年 SGI 为以 GPL 发布 XFS 文件系统，用自制工具逐行比对第三方代码以完成'产权负担解除'（encumbrance relief），并通过 linvfs 接口与 pagebuf 层将 XFS 移植到 Linux，当事人 Russell Cattelan 在 USENIX ;login: 上亲述该过程。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

