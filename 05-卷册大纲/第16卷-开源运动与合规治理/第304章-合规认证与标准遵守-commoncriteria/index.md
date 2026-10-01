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

- FDA 510(k) 数据库中检索“BSD”或“FreeBSD”的命中率低，需结合厂商技术文档与维修手册交叉验证；MAUDE 数据库中是否有 BSD 相关事故需查
- 汇丰/渣打/中银香港是否“公开”使用 FreeBSD 需查证，部分信息可能源自旧 Foundation case studies 而未更新；金融科技企业的具体合规细节多受银行保密法限制
- 百度/阿里巴巴/腾讯是否“公开”使用 FreeBSD 需查企业技术博客，部分信息可能过时；Nubank 等巴西金融科技企业是否使用 FreeBSD 需查工程博客
- DARPA 资助 TrustedBSD 的具体金额与起止时间需查 DARPA 公开合同数据库；TrustedBSD 与 SRI International 的 CHERI 项目是否共享资金需区分
- NIST 是否“认可”Foundation 自证需明确区分“接收”与“背书”；自证文档在 NIST SSP 库中的检索状态需查

## 文献

- FDA 510(k) Database；FDA MAUDE Database［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD Foundation Case Studies（金融业条目）；LinkedIn BSD 技能招聘数据［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Tencent Cloud Security White Paper；Nubank Engineering Blog［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- DARPA 2001-2005 年度报告；Watson“TrustedBSD Final Report” ［B］
- NIST SSP Repository；FreeBSD Foundation 2023-09 SSDF Statement［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- NIST SP 800-218 Appendix C；FedRAMP SSP Template［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP558（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人转述 Telnet 协议史：1972 年 John Postel 撰写的 RFC 奠定 Telnet 协议，Postel 在文中自嘲该文档未能兑现及时、清晰与简洁的承诺；1990 年代早期 Telnet 曾用于访问国会图书馆、NASA 新闻与最高法院判决。（BSD Now EP558，[1248.1-1360.5]，L2）[订正：原 [1253.14-1360.36]，2026-10-01 SenseAudio 重转核对]
- 主持人介绍 towel.blinkenlights.nl 的 ASCII 版《星球大战》与 telehack.com 等项目，后者以 Telnet 重现 ARPANET 时代的 BBS、MUD 与文本冒险，构成对早期网络文化的保存。（BSD Now EP558，[956.6-1151.6]，L2）[订正：原 [956.74-1151.44]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 基金会发布 SSDF 自证报告第一版，面向美国政府软件供应链合规（NIST SP 800-218 与 Executive Order 14028）；NetApp 与 RG Nets 等伙伴引用该报告支持其向政府客户供货。（BSD Now EP558，[453.7-741.7]，L2）[订正：原 [483.30-730.50]，2026-10-01 SenseAudio 重转核对]
- BSDCan 组织委员会自述 Dan Langille 在主持二十年后交棒，委员会成立加拿大非营利组织 BSDCan Conferences Incorporated 以承接资金与赞助；当届白金赞助商为 Netflix，金级为 Apple 与 ARM。（BSD Now EP558，[2789.3-3401.1]，L1）[订正：原 [2801.24-3400.76]，2026-10-01 SenseAudio 重转核对]
- 委员会回顾 BSDCan 票价自 2005 年起十五年间维持 199 美元未变，现调整为 256 美元；其拍卖传统所得捐给 Ottawa Mission 慈善机构。（BSD Now EP558，[3545.0-3681.0]，L1）[订正：原 [3545.42-3667.88]，2026-10-01 SenseAudio 重转核对]

**史料**：

- 本期史料包括 Telnet 历史的二手文章、FreeBSD 基金会 SSDF 公告，以及 BSDCan 组织委员会 Michael Lucas、Patrick 与 Peter Hansteen 的一手自述。（BSD Now EP558，[453.7-3401.1]，L1）[订正：原 [483.30-3400.76]，2026-10-01 SenseAudio 重转核对]

**史观**：

- 总纲18 时间是一种形式主义：Telnet 从主流远程访问工具变为小众怀旧文化，呈现技术生命周期随时代需求而更替的形式化进程。（BSD Now EP558，[1248.1-1437.0]，L2）[订正：原 [1253.14-1412.28]，2026-10-01 SenseAudio 重转核对]
- 总纲10 动手者创造历史：Dan Langille 与历届志愿者持续二十年操办 BSDCan，其交棒与新机构设立延续了社区会议，体现动手者对社区基础的长期投入。（BSD Now EP558，[2789.3-3119.9]，L1）[订正：原 [2801.24-3108.48]，2026-10-01 SenseAudio 重转核对]
- 总纲13 法律与道德是利益分配：SSDF 自证是软件供应商满足政府采购合规的制度安排，反映安全标准背后的法律与利益分配。（BSD Now EP558，[453.7-741.7]，L2）[订正：原 [483.30-730.50]，2026-10-01 SenseAudio 重转核对]

**辨析**：

- Telnet 1972 年 RFC 的作者归属与 John Postel 的自嘲引文来自二手文章，须以 RFC 原文核实。　[存疑脚注] RFC 作者与引文为二手转述，未经 RFC 原文核实。（BSD Now EP558，[1248.1-1319.7]，L4）[订正：原 [1253.14-1319.76]，2026-10-01 SenseAudio 重转核对]
- BSDCan 票价自 2005 年起十五年未变的说法为委员口述，须以历年会议档案核实。　[存疑脚注] 票价历史为委员口述，未经历年会议档案核实。（BSD Now EP558，[3545.0-3564.0]，L4）[订正：原 [3545.42-3563.30]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP558] Pennington J. BSD Now: 558: Worlds of telnet[EB/OL]. (2024-05-09)[2026-08-15]. <https://www.bsdnow.tv/558>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Regulation. (EU) 2016/679 GDPR [S/OL]. European Parliament and Council, 2016-04-27 (effective 2018-05-25). <https://eur-lex.europa.eu/eli/reg/2016/679/oj> (2026-07-22 访问，因 JavaScript 验证未能直接获取正文)[EB/OL]. 2016.［DKC-0582→fulltext:5560］；Regulation. (EU) 2022/2554 DORA [S/OL]. European Parliament and Council, 2022-12-14. <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554> (2026-07-22 访问)[EB/OL]. 2022.［DKC-0587→fulltext:5564］
- California. Attorney General CCPA/CPRA Page [EB/OL]. <https://oag.ca.gov/privacy/ccpa> (2026-07-22 访问)[EB/OL]. 2026. ［DKC-0583→fulltext:5561］
- LEI. Nº 13.709, DE 14 DE AGOSTO DE 2018 Lei Geral de Proteção de Dados Pessoais (LGPD) [S/OL]. Presidência da República, 2018-08-14. <http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm> (2026-07-22 访问)[EB/OL]. 2018. ［DKC-0585→fulltext:5562］
- Personal. Information Protection and Electronic Documents Act (PIPEDA) [S/OL]. Office of the Privacy Commissioner of Canada. <https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/> (2026-07-22 访问)[EB/OL]. 2026. ［DKC-0586→fulltext:5563］
- Common. Criteria Publications [EB/OL]. <https://www.commoncriteriaportal.org/cc/> (2026-07-22 访问)[EB/OL]. 2026. ［DKC-0588→fulltext:5565］
- NIST. SP 800-218 Secure Software Development Framework (SSDF) Version 1.1 [S/OL]. Souppaya M, Scarfone K, Dodson D. National Institute of Standards and Technology, 2022-02. <https://csrc.nist.gov/pubs/sp/800/218/final> (2026-07-22 访问). DOI: 10.6028/NIST.SP.800-218[EB/OL]. 2022. ［DKC-0589→fulltext:5566］
<!-- /dangan-20260908 -->
