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
- BSD 许可证作为 Wasabi 商业模型基石——允许专有衍生品与商业闭源扩展，与 GPL 商业化路径（服务订阅、双许可证）形成对比；Wasabi 选择 BSD 路径依赖 Wasabi Certified BSD 产品线

## 史料

> 订正注：以下 references_fulltext 前 8 条（chmatch_3710、chmatch_3834-3840）系库侧自动生成行，其“原因：folder 第67章”与本章（第 68 章）章号不符，疑为目录名“第67章”历史残留导致的匹配错挂；按库侧生成块处置规约，本文件不擅改块数据本体，仅在此留痕说明，匹配归属修正须由库侧（references_fulltext 的 chmatch_3710/3834-3840 复查）专项处理。人工史料清单暂缺，补齐属新增内容，待专项。

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

- 总纲第 10 条——动手者创造历史：NetBSD 边缘贡献者通过 CVS 直接提交、补丁间接贡献与文档测试贡献实际创造了多平台移植史，贡献记录的重建须以动手痕迹为准
- 总纲第 4 条——分离聚合是永恒规律：de Raadt 被驱逐出 NetBSD Core Team 后分离创建 OpenBSD，Wasabi 商业化尝试亦是社区与商业力量的分离聚合形态，工程资产最终沉淀回 NetBSD 主线
- 总纲第 5 条——没有必然性，只有偶然性：驱逐事件与 Wasabi 兴衰均属偶然事件链，无历史必然性；驱逐发生于 1994 年 12 月、OpenBSD 1996 年发布，均非预设结果
- 总纲第 13 条——法律与道德是利益分配：BSD 许可证允许专有衍生品与商业闭源扩展，Wasabi 的商业模型本质是以许可证条款分配商业化利益，与 GPL 双许可证路径形成对比
- 总纲第 22 条——知识注定过时：Wasabi 工程资产（WAPBL、x86-64、XScale）与商业化经验教训随时间沉淀，其“商业化尝试失败记忆”对 Foundation 后续决策的影响亦随新形势需要重新检验

> 回填留痕：本节原为占位符“(待人工回填——详见子节文件史观/辨析字段)”，系按核查报告（C114）要求依据子节文件史观/辨析字段回填并映射总纲条号；条号对照《一刻哲学 25 条总纲权威编号表》（remediation_zongang_canonical.md）校正。

## 辨析

- 贡献记录的完整性与代表性是核心辨析点——部分贡献可能未留下记录，需对照多源核实
- 长期影响的正负评估在不同叙事中差异较大——部分视为警示，部分视为可借鉴经验；需对照 Foundation 后续决策核实
- 商业化冲动的具体诱因在不同成员叙事中差异较大——部分归因于个人经济压力，部分归因于社区可持续性；需对照多成员自述核实
- 商业支持定位的实际效果存在争议——部分商业用户认为有效，部分认为不足；需对照用户案例核实
- BSD 商业化路径的实际优势在不同叙事中评估不一——部分强调灵活性，部分强调商业吸引力不足；需对照 Wasabi 实际营收数据核实

## 文献

- NetBSD CVS 历史全量；补丁提交记录；邮件列表历年贡献者统计
- NetBSD Foundation Annual Reports 2010-2015；Wasabi 工程资产主线合并记录［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Wasabi Systems 公司公告；NetBSD Foundation Annual Report 2000［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Michaelson《On Wasabi》访谈；Wasabi 产品介绍
- BSD vs GPL 商业化对比研究；Wasabi 战略文档摘要［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Wasabi Certified BSD 产品介绍；Wasabi 产品文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Wasabi 雇佣公告；NetBSD Foundation 利益冲突声明；Mewburn 个人主页［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- AMD x86-64 移植项目记录；Wasabi 公司公告 2001.6［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- NetBSD Project. Formal Releases History [EB/OL]. [2026-07-19]. **<https://www.netbsd.org/releases/formal.html>**［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Intel Capital 投资公告 2002.9；Wasabi-Intel 合作协议摘要［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

