---
chapter: 第 85 章
id: CH85
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第85章 分裂时期的流行文化呈现

## 要点

- 1992-1996 年间 BSD 在技术媒体（Dr. Dobb's Journal、Salon、Wired 等）中的文化呈现——媒体将 BSD 描绘为 “古老而高贵的 UNIX 后裔”、“被 Linux 取代的悲剧英雄”、“极客文化的活化石”；媒体呈现塑造公众对 BSD 的认知
- BSD is dying 叙事的文化根源——1990 年代中期 Linux 崛起后，技术媒体对 BSD 的悲观叙事，反映 “新事物取代旧事物” 的文化心理；叙事的流行与 Slashdot 等技术媒体的兴起同步
- 分裂时期 BSD 与 Linux 在流行文化中的差异化形象——BSD 被描绘为 “古老、保守、精英、稳定” 的 UNIX 后裔，Linux 被描绘为 “年轻、激进、社区驱动、革命性” 的新兴力量；差异化形象塑造公众认知
- BSD 流行文化的史料辨析需区分 “媒体呈现” 与 “实际状况”——前者是媒体的描绘，后者是 BSD 社区的实际状况；辨析需对照媒体呈现与社区档案
- 1992-1996 年 FreeBSD 的地理中心——核心开发者主要集中在美国（加州 Walnut Creek CDROM、犹他州、华盛顿州等），Walnut Creek CDROM 作为 FreeBSD 商业发行商成为地理中心；地理分布反映 FreeBSD 与美国商业的紧密结合

## 史观

- 总纲第 15 条——文化即形式主义。项目史观总纲第 14 章 14.5 节载 “真正使项目得以成立的，不是代码，而是这些外围的形式主义的东西”——媒体呈现作为外部视角塑造 BSD 社区自我认知即形式主义建构的体现，14.7 节 “去中心化的悖论” 提示媒体叙事本身亦可能产生新的中心化（如 “悲剧英雄” 叙事将 BSD 钉死在 “被 Linux 取代” 的位置上），须自反地审视媒体呈现的形式主义
- 总纲第 5 条——没有必然性，只有偶然性。项目史观总纲第 5 章 5.1 节载 “世界上没有必然性，只有偶然性”——FreeBSD 的地理分布（美国集中）与商业结合的技术路径并非 “地理必然塑造技术路径” 的规律展开，而是 Walnut Creek CDROM 加州设立、Hubbard 等核心开发者位于美国西海岸等偶然条件组合的层叠；5.3 节 “记忆将许多偶然性认识为一种必然性” 警示事后叙事可
- 总纲第 20 条——历史地理塑造思想土壤：冷战结束作为地缘政治结构变化，为 BSD 全球扩散提供了新的思想土壤
  - 辨析：冷战结束对 BSD 的影响兼有全球化与互联网扩散两个归因——1991 年苏联解体后前苏联与东欧开发者通过 Internet 接入 BSD 社区（如俄罗斯 FreeBSD 用户组 1990 年代中期建立），但 Internet 扩散本身亦受冷战结束推动（NSFNET 1991 年解除商业限制）；两个
- 总纲第 5 条——没有必然性，只有偶然性。项目史观总纲第 5 章 5.1 节载 “世界上没有必然性，只有偶然性”——三项目的文化地理建构（加州商业务实、全球可移植精英、加拿大安全孤岛）并非 “地理必然塑造文化” 的规律展开，而是 Walnut Creek CDROM 加州设立、NetBSD 核心团队全球分布、de Raadt 卡尔加里迁移等偶然条件组合的层叠；事后叙事易将这些偶然层叠重构为“地理决定文化”的必然（第 5 章 5.3 节“记忆将许多偶然性认识为一种必然性”），引用时须以偶然条件逐项呈现
- 总纲第 5 条——没有必然性，只有偶然性：CSRG 解散是当事人主观决定的偶然事件而非校方裁撤的必然结果（第 5 章 5.1 节原文 “世界上没有必然性，只有偶然性”）；CSRG 收到 DARPA 最后资助至 1995 年解散的节奏、McKusick 等人的个人选择与加州预算环境共同构成解散时点的偶然组合，不构成“必然终结”的目的论叙事

## 辨析

<!-- 2026-09-11 整改：原此处有 L3.3.1 committer_date 时区偏移机器统计残迹一段，与流行文化呈现主题零关联，已删除留痕。 -->
- 媒体呈现存在戏剧化倾向——Dr. Dobb's Journal 1992-1996 年 BSD 报道以技术评测为主基调较为客观，Salon 与 Wired 早期 BSD 报道偏向 “悲剧英雄” 叙事框架，后者在 1995-1996 年 Linux 崛起背景下强化了 “BSD 被取代” 的戏剧化叙事 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］；多源交叉验证不可靠性规则提示——O'Reilly 文章、mckusick.com 同源，gunkies.org 独立但引用源码版本号 `8.16 (Berkeley) 5/14/95` 为代码

## 文献

- 技术媒体 BSD 报道档案（Dr. Dobb's Journal 1992-1996、Salon、Wired 早期报道存档）；Slashdot 1998-2005 BSD 相关报道存档 ［C］

## 85.4.2 BSD is dying 的文化根源

- 要点：BSD is dying 叙事的文化根源——1990 年代中期 Linux 崛起后，技术媒体对 BSD 的悲观叙事，反映 “新事物取代旧事物” 的文化心理；叙事的流行与 Slashdot 等技术媒体的兴起同步
- 史料：Slashdot 1998-2005 BSD 报道；BSD is dying 梗的传播记录；技术媒体对 BSD 的悲观叙事 ［C］
- 史观：总纲第 3 条（不存在进步，只有权力再分配）与第 15 条（文化即形式主义）。“BSD is dying” 叙事的流行反映技术话语权的再分配而非单向进步；媒体呈现作为文化形式主义建构塑造社区自我认知。释读依据见项目史观总纲第 25
- FreeBSD 地理分布档案（Walnut Creek CDROM 所在地档案、邮件列表签名档地理统计）；本项目。freebsd.duckdb 数据分析报告：深层信息挖掘 [R/OL]. 2026（旧称 bsd_commits.db 已拆库升格）.

## 85.5.2 NetBSD 与 OpenBSD 的地理分布

- 要点：NetBSD 的地理分布——核心团队分散于美国（加州、马萨诸塞州）、欧洲（英国、德国）、日本等，反映 “可移植性至上” 的全球性；OpenBSD 1995 年代码层面 fork（deraadt 1995-10-
- BSD 全球化研究；冷战结束与开源扩散分析［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 85.6.2 互联网商业化浪潮

- 要点：**1993-1996 年** 互联网商业化浪潮对 BSD 社区地理扩张的塑造——NSFNET **1995 年** 商业化、Web 兴起、ISP 普及使 BSD 代码通过互联网全球扩散；BSD 在 Web 服务器（Apache 早期基于 FreeBSD）、ISP 基础设施中的广泛应用反映互联网商业化的塑造
- 史料：NSFNET 商
- BSD 文化地理研究；文化地理学方法论［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 85.7.2 形式主义建构的体现

- 要点：三项目文化地理作为形式主义建构的体现——“加州商业务实”、“全球可移植精英”、“加拿大安全孤岛” 作为形式主义建构的标签，承载各项目的文化内容；形式主义分析揭示文化地理与组织模式的关系
- 史料：BSD 项目文化地理档案；形式主义分析方法论文献 ［B］
- 史观：总纲第 17 条——形式与内容：文化地理作为形式与组织模式作为内容形成
- McKusick M K. Twenty Years of Berkeley Unix [M]//Open Sources. O'Reilly, 1999: 31-56. ISBN 1-56592-582-3；mckusick.com/csrg/；gunkies.org/wiki/4.4BSD-Lite2；项目史观总纲第 5 章 5.1/5.3 节、第 14 章 14.1/14.2 节、第 1 章 1.1 节 ［A］

## 85.8.2 CSRG 解散后伯克利校园的 BSD 遗产

- 要点：CSRG 作为 EECS 旗下研究组办公地点在 Cory Hall（EECS 系大楼）内而非网络流传

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-4-126 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-4-126`；login 逐条遍历判定采纳）

2000 年前后，斯坦福大学在公共集群上以 Kerberos 单点登录配合 rsh 脚本实现远程批量管理，少数管理员即可管理数百台主机、每台约 30000 活跃账户；同期系统管理实践普遍采用 OS 加固（关闭不必要服务与 setuid 程序）以降低提权风险。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

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

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

