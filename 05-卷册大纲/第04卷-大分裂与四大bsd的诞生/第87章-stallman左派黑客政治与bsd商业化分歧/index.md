---
chapter: 第 87 章
id: CH87
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 87 章 stallman左派黑客政治与bsd商业化分歧

## 要点

- 1990 年代分裂时期黑客社区对 Stallman 政治立场的反应呈现多元图景——BSD 社区内部政治立场分化（部分开发者倾向 BSD 许可证的 “自由市场” 路径，部分认同 copyleft 理念）；OSI 1998 年创立 “作为对 FSF 左派政治的反动” 叙事须辨析；黑客社区政治立场不应简化为 “左派 FSF vs 右派 BSD/OSI” 二元，须按 0 信任原则对照 BSD 邮件列表政治
- 项目史观总纲第 19 条 “解释学循环是历史认识的根本条件。权力与知识在历史书写中共谋——什么被记录、什么被遗忘，本身就是权力行使” 审视 **1992-1996 年** 分裂时期的文化图景——BSD 分裂的叙事由 FreeBSD 阵营（Handbook 官方叙事、Contributors 文章）、NetBSD 阵营（Core Team 决策记录）、OpenBSD 阵营（de Raadt 个人演讲
- 文化比较的辨析需区分 “有依据的文化差异”（如开发模式、治理结构）与 “刻板印象”（如 “BSD 精英主义”、“Linux 混乱”）；前者有助于理解，后者需警惕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3675] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3681] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3684] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3686] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3689] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3692] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3707] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3786] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3796] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章
- [DB:references_fulltext:chapter_matches:chmatch_3830] 卷“第05卷-freebsd的工程化奠基”第 87 章，匹配置信度 folder，原因：folder 第85章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 分裂时期黑客社区政治立场的 “左派 vs 右派” 二元叙事在二手文献中流传甚广，但须按 0 信任原则对照 BSD 邮件列表政治讨论存档与 OSI 创立档案交叉验证——BSD 社区与 FSF 的政治分歧更多是许可证策略与商业路径之争，而非系统性左右翼政治对立；OSI 1998 创立 “作为对 FSF 左派政治的反动” 这一叙事主要源自 Raymond 一方表述，须对照 FSF 一方档案与第三方研究者
- 解释学循环审视的限度——承认叙事的建构性不等于否定史实的可考据性，bsd_commits.db 中的 commit 记录、tag 信息、文件引入时间是不可篡改的史实层；解释学循环审视针对的是“叙事层”（如 Handbook“创建者”叙事、Contributors 专节位置）而非“史实层”（如 commit hash、tagger_date）；不得因解释学循环而陷入虚无主义，亦不得因史实可考据而忽视
- 文化比较的边界需明确——文化是动态的，不同时期的文化特征不同；不得以某一时期的文化特征概括整个项目

## 文献

- BSD 邮件列表政治讨论存档；OSI 创立档案；自由软件 vs 开源软件研究文献；Raymond 与 Stallman 公开辩论档案 ［A］
- 项目史观总纲第 19 条与第 25 章；FreeBSD Handbook 与 Contributors 文章；NetBSD Core Team 决策记录；de Raadt 公开演讲档案 ［A］### 史观映射> 分裂不是文化差异的原因，而是文化差异的结果——FreeBSD 的务实、NetBSD 的精英、OpenBSD 的偏执，这些气质在分裂之前就已存在，分裂只是让它们各自找到了自己的容器。三项目的文化是形式主义的产物：谁先占据某个定位，谁就获得了那个定位的话语权，后来者只能选择剩余的位置。而地理在其中扮演了沉默的塑造者——FreeBSD 在加州的商业土壤中生长，OpenBSD 在卡尔加里的寒冷中被推向偏执的极致，NetBSD 在全球散点中维持着精英的幻觉。三者在本体论上平等，但平等不意味着相同——差异本身就是形式主义化的非存在，每一个标签都在遮蔽更复杂的真相---<!-- 嵌入点建议
- 文化比较方法论；BSD/Linux/Windows NT 文化研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
