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
- NetBSD Foundation Annual Reports 2010-2015；Wasabi 工程资产主线合并记录[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Wasabi Systems 公司公告；NetBSD Foundation Annual Report 2000[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Michaelson"On Wasabi"访谈；Wasabi 产品介绍 ［B］
- BSD vs GPL 商业化对比研究；Wasabi 战略文档摘要[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Wasabi Certified BSD 产品介绍；Wasabi 产品文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Wasabi 雇佣公告；NetBSD Foundation 利益冲突声明；Mewburn 个人主页[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- AMD x86-64 移植项目记录；Wasabi 公司公告 2001.6[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- NetBSD Project. Formal Releases History [EB/OL]. [2026-07-19]. <https://www.netbsd.org/releases/formal.html>[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- Intel Capital 投资公告 2002.9；Wasabi-Intel 合作协议摘要[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

<!-- PODCAST_MINE v20260827 -->
<!-- Chapter: 第68章-netbsd的贡献者与de-raadt被驱逐事件 -->

## 要点（播客口述史提取）
- How did you first get involved and find your way to BSD?
- head yet it's not an 11 uh but it should land in time for freebsd 11.0's release uh but right now
- started with FreeBSD. So of course, we'll have the link to that in the show notes. You'll have to go
- Well, I think it started around 1998 or something like that, as far as BSD is concerned.
- Because my first year at BSDCon, I was the very last talk.
- desktop which is being developed on pcbsd so that was pretty cool and then of course drew did a
- So you can take a look at that and see what's changed in PCBSD land.
- So if you're on 9, 10, or any supported version of FreeBSD,

## 史料（播客提及）
- [BSD Now EP144 @ 218.45999145507812] So that, and he also mentioned in the slides here, working with other OSs that may want pledge support as well, which, frankly, I think that would complement a lot of the other BSDs very well.
- [BSD Now EP144 @ 2340.639892578125] But when you create your new account, don't forget to use the coupon code FREEBSDNOW, which is going to give you that $10 credit so you can run basically two months of their lower-end VM, which for a low-end VM, it's actually pretty not bad.
- [BSD Now EP144 @ 2939.33984375] follow-up to last week, we had, of course, the breaking news that FreeBSD actually was growing
- [BSD Now EP144 @ 3423.179931640625] that's actually a convention that's purposely used in the FreeBSD documentation
- [BSD Now EP144 @ 593.260009765625] this one actually has landed already in FreeBSD Head,

## 史观（播客当事人观点与总纲映射）
- [BSD Now EP144 @ 218.45999145507812] So that, and he also mentioned in the slides here, working with other OSs that may want pledge support as well, which, frankly, I think that would complement a lot of the other BSDs very well.
- [BSD Now EP144 @ 2340.639892578125] But when you create your new account, don't forget to use the coupon code FREEBSDNOW, which is going to give you that $10 credit so you can run basically two months of their lower-end VM, which for a low-end VM, it's actually pretty not bad.
  → 史观映射：总纲23——一切历史写作都是基于哲学设定的历史小说; 总纲18——时间是一种形式主义
- [BSD Now EP144 @ 2939.33984375] follow-up to last week, we had, of course, the breaking news that FreeBSD actually was growing
- [BSD Now EP144 @ 3423.179931640625] that's actually a convention that's purposely used in the FreeBSD documentation
- [BSD Now EP144 @ 593.260009765625] this one actually has landed already in FreeBSD Head,
- [BSD Now EP43 @ 1011.2999267578125] Yeah, well, that's kind of the focus the FreeBSD Foundation has been doing on which jobs they're actually funding.
  → 史观映射：总纲11——商品是形式主义
- [BSD Now EP43 @ 1398.47998046875] Well, I think it started around 1998 or something like that, as far as BSD is concerned.
- [BSD Now EP43 @ 1424.9599609375] And well, it turned out that OpenBSD was the only thing which had any kind of documentation

## 辨析（播客争议与存疑点）
- （该章节匹配播客中暂未提取到相关争议点）

## 文献（播客参考条目）
- [BSD Now EP144] Pennington J. BSD Now: 144: The PF life[EB/OL]. (2016-06-01)[2026-08-15]. https://www.bsdnow.tv/144.
- [BSD Now EP43] Pennington J. BSD Now: 43: Package Design[EB/OL]. (2014-06-25)[2026-08-15]. https://www.bsdnow.tv/43.
- [BSD Now EP376] Pennington J. BSD Now: 376: Build stable packages[EB/OL]. (2020-11-12)[2026-08-15]. https://www.bsdnow.tv/376.

<!-- /PODCAST_MINE -->