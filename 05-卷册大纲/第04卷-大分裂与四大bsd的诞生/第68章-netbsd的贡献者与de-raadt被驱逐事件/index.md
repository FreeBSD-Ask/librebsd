---
chapter: 第 68 章
id: CH68
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 68 章 netbsd的贡献者与de-raadt被驱逐事件

## 要点

- NetBSD 边缘贡献者的史料辨析需关注贡献记录的完整性、来源的多样性与叙事的偏差——部分贡献者通过 CVS 直接提交，部分通过补丁间接贡献，部分通过文档与测试贡献；辨析需对照多源史料重建
- Wasabi 事件后 NetBSD 长期无同等规模商业支持公司，Wasabi 工程资产（WAPBL、x86-64、XScale）在 NetBSD 主线长期沉淀；“商业化尝试失败记忆”对 NetBSD Foundation 后续决策产生长期影响
- 2000 年中 Wasabi Systems 成立的背景是 NetBSD 核心团队对商业化的冲动——长期资金不足与社区贡献的可持续性问题推动部分成员寻求商业路径
- Jay Michaelson 提出“让商业用户安心选用 NetBSD”的商业支持定位——通过提供测试套件、源码、工具链、90 天支持让商业用户降低选用 NetBSD 的风险
- BSD 许可证作为 Wasabi 商业模型基石——允许 proprietary 衍生品与商业闭源扩展，与 GPL 商业化路径（服务订阅、双许可证）形成对比；Wasabi 选择 BSD 路径依赖 Wasabi Certified BSD 产品线

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3710] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3834] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3835] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3836] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3837] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3838] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3839] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_3840] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 folder，原因：folder 第67章
- [DB:references_fulltext:chapter_matches:chmatch_1410] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 0.7，原因：关键词匹配: security holes
- [DB:references_fulltext:chapter_matches:chmatch_1510] 卷“第04卷-大分裂与四大bsd的诞生”第 68 章，匹配置信度 0.7，原因：关键词匹配: cache attack
- [DB:bsdnow_podcast:outline_mappings:om_10417] BSD Now 第 676 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10450] BSD Now 第 671 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10470] BSD Now 第 666 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10497] BSD Now 第 663 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10664] BSD Now 第 634 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10685] BSD Now 第 630 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10796] BSD Now 第 613 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11081] BSD Now 第 578 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11168] BSD Now 第 567 期，匹配 CH68 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11192] BSD Now 第 565 期，匹配 CH68 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 贡献记录的完整性与代表性是核心辨析点——部分贡献可能未留下记录，需对照多源核实
- 长期影响的正负评估在不同叙事中差异较大——部分视为警示，部分视为可借鉴经验；需对照 Foundation 后续决策核实
- 商业化冲动的具体诱因在不同成员叙事中差异较大——部分归因于个人经济压力，部分归因于社区可持续性；需对照多成员自述核实
- 商业支持定位的实际效果存在争议——部分商业用户认为有效，部分认为不足；需对照用户案例核实
- BSD 商业化路径的实际优势在不同叙事中评估不一——部分强调灵活性，部分强调商业吸引力不足；需对照 Wasabi 实际营收数据核实

## 文献

- NetBSD CVS 历史全量；补丁提交记录；邮件列表历年贡献者统计 ［A］
- NetBSD Foundation Annual Reports 2010-2015；Wasabi 工程资产主线合并记录［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- Wasabi Systems 公司公告；NetBSD Foundation Annual Report 2000［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- Michaelson“On Wasabi”访谈；Wasabi 产品介绍 ［B］
- BSD vs GPL 商业化对比研究；Wasabi 战略文档摘要［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- Wasabi Certified BSD 产品介绍；Wasabi 产品文档［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- Wasabi 雇佣公告；NetBSD Foundation 利益冲突声明；Mewburn 个人主页［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- AMD x86-64 移植项目记录；Wasabi 公司公告 2001.6［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- NetBSD Project. Formal Releases History [EB/OL]. [2026-07-19]. <https://www.netbsd.org/releases/formal.html>［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- Intel Capital 投资公告 2002.9；Wasabi-Intel 合作协议摘要［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

