---
chapter: 第 304 章
id: CH304
volume: 第16卷-开源运动与合规治理
---

# 第 304 章 合规认证与标准遵守-commoncriteria

## 要点

- 医疗设备 BSD 部署的具体记录受商业机密与 FDA 监管双重限制，公开档案稀少
- 汇丰、渣打、中银香港等金融企业使用 FreeBSD 满足 SOX 合规的具体案例多见于 FreeBSD Foundation case studies 与厂商技术白皮书
- 各法域 FreeBSD 部署的合规记录公开档案稀少，主要依靠企业技术博客与 Foundation case studies
- TrustedBSD 工程部分参照 CC EAL 4 要求设计但未正式申请 CC 认证，DARPA 资助项目结束后的工程延续情况需考据
- FreeBSD Foundation 2023 年公开 SSDF 自证公告后是否获得 NIST 官方背书需考据，NIST 通常不“背书”特定供应商的自证

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_11239] BSD Now 第 561 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11267] BSD Now 第 558 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11287] BSD Now 第 556 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11335] BSD Now 第 550 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11416] BSD Now 第 539 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11558] BSD Now 第 522 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11578] BSD Now 第 520 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11686] BSD Now 第 506 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11738] BSD Now 第 498 期，匹配 CH304 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11796] BSD Now 第 488 期，匹配 CH304 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- FDA 510(k) 数据库中检索"BSD"或"FreeBSD"的命中率低，需结合厂商技术文档与维修手册交叉验证；MAUDE 数据库中是否有 BSD 相关事故需查
- 汇丰/渣打/中银香港是否“公开”使用 FreeBSD 需查证，部分信息可能源自旧 Foundation case studies 而未更新；金融科技企业的具体合规细节多受银行保密法限制
- 百度/阿里巴巴/腾讯是否“公开”使用 FreeBSD 需查企业技术博客，部分信息可能过时；Nubank 等巴西金融科技企业是否使用 FreeBSD 需查工程博客
- DARPA 资助 TrustedBSD 的具体金额与起止时间需查 DARPA 公开合同数据库；TrustedBSD 与 SRI International 的 CHERI 项目是否共享资金需区分
- NIST 是否“认可”Foundation 自证需明确区分“接收”与“背书”；自证文档在 NIST SSP 库中的检索状态需查

## 文献

- FDA 510(k) Database；FDA MAUDE Database[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- FreeBSD Foundation Case Studies（金融业条目）；LinkedIn BSD 技能招聘数据[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Tencent Cloud Security White Paper；Nubank Engineering Blog[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- DARPA 2001-2005 年度报告；Watson"TrustedBSD Final Report" ［B］
- NIST SSP Repository；FreeBSD Foundation 2023-09 SSDF Statement[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- NIST SP 800-218 Appendix C；FedRAMP SSP Template[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP558（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人转述 Telnet 协议史：1972 年 John Postel 撰写的 RFC 奠定 Telnet 协议，Postel 在文中自嘲该文档未能兑现及时、清晰与简洁的承诺；1990 年代早期 Telnet 曾用于访问国会图书馆、NASA 新闻与最高法院判决。（BSD Now EP558，[1253.14-1360.36]，L2）
- 主持人介绍 towel.blinkenlights.nl 的 ASCII 版《星球大战》与 telehack.com 等项目，后者以 Telnet 重现 ARPANET 时代的 BBS、MUD 与文本冒险，构成对早期网络文化的保存。（BSD Now EP558，[956.74-1151.44]，L2）
- FreeBSD 基金会发布 SSDF 自证报告第一版，面向美国政府软件供应链合规（NIST SP 800-218 与 Executive Order 14028）；NetApp 与 RG Nets 等伙伴引用该报告支持其向政府客户供货。（BSD Now EP558，[483.30-730.50]，L2）
- BSDCan 组织委员会自述 Dan Langille 在主持二十年后交棒，委员会成立加拿大非营利组织 BSDCan Conferences Incorporated 以承接资金与赞助；当届白金赞助商为 Netflix，金级为 Apple 与 ARM。（BSD Now EP558，[2801.24-3400.76]，L1）
- 委员会回顾 BSDCan 票价自 2005 年起十五年间维持 199 美元未变，现调整为 256 美元；其拍卖传统所得捐给 Ottawa Mission 慈善机构。（BSD Now EP558，[3545.42-3667.88]，L1）

**史料**：

- 本期史料包括 Telnet 历史的二手文章、FreeBSD 基金会 SSDF 公告，以及 BSDCan 组织委员会 Michael Lucas、Patrick 与 Peter Hansteen 的一手自述。（BSD Now EP558，[483.30-3400.76]，L1）

**史观**：

- 总纲18 时间是一种形式主义：Telnet 从主流远程访问工具变为小众怀旧文化，呈现技术生命周期随时代需求而更替的形式化进程。（BSD Now EP558，[1253.14-1412.28]，L2）
- 总纲10 动手者创造历史：Dan Langille 与历届志愿者持续二十年操办 BSDCan，其交棒与新机构设立延续了社区会议，体现动手者对社区基础的长期投入。（BSD Now EP558，[2801.24-3108.48]，L1）
- 总纲13 法律与道德是利益分配：SSDF 自证是软件供应商满足政府采购合规的制度安排，反映安全标准背后的法律与利益分配。（BSD Now EP558，[483.30-730.50]，L2）

**辨析**：

- Telnet 1972 年 RFC 的作者归属与 John Postel 的自嘲引文来自二手文章，须以 RFC 原文核实。　[存疑脚注] RFC 作者与引文为二手转述，未经 RFC 原文核实。（BSD Now EP558，[1253.14-1319.76]，L4）
- BSDCan 票价自 2005 年起十五年未变的说法为委员口述，须以历年会议档案核实。　[存疑脚注] 票价历史为委员口述，未经历年会议档案核实。（BSD Now EP558，[3545.42-3563.30]，L4）

**文献**：

- [BSD Now EP558] Pennington J. BSD Now: 558: Worlds of telnet[EB/OL]. (2024-05-09)[2026-08-15]. https://www.bsdnow.tv/558.

<!-- /PODCAST_REVIEW -->
