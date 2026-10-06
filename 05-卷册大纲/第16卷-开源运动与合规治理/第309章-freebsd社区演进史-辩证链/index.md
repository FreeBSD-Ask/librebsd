---
chapter: 第 309 章
id: CH309
volume: 第16卷-开源运动与合规治理
---

# 第309章 freebsd社区演进史-辩证链

## 史料

- [WEB:freebsd.org/administration.html] FreeBSD 官方治理架构（一手）：Core Team 选举制（committer 直选）、各功能团队 charter 制——治理演进的一手制度文本

## 要点

- 批评者指出 FreeBSD 社区发展面临三个结构性挑战——其一，贡献者老龄化：FreeBSD committer 群体平均年龄偏大（多数 40+），CSRG 一代（McKusick、Karels、Bostic）已步入晚年，Mike Karels 于 2024-06-07 去世（John Baldwin（约翰·鲍德温） 在 freebsd-announce 邮件列表发布讣告），反映 CSRG 一代的自然衰退；freebsd.duckdb 查询 L1.2.3 显示每年流失贡献者数（连续 2 年无 commit）从 1995 年 27 人激增至 2010 年 5,443 人、2015 年 14,079 人、2019 年 22,210 人，社区流动性大幅增加；其二，新生代吸引力不足：FreeBSD 在年轻开发者中认知度低，操作系统教材多数以 Linux 为主，FreeBSD 缺乏现代开发工具链（如 GitHub PR）的完整支持，2020 年才完成 Git 迁移，相比 Linux（2005 年即采用 Git）迟缓约 15 年；其三，与 Linux 社区规模差距扩大：Linux 6.5 内核（2023-08-27 发布）单版本有 1,921 位开发者贡献，其中 271 位为首次贡献者（LWN 2023-08-28 Jonathan Corbet 报道），而 FreeBSD 2021 年全年活跃贡献者（≥10 commit/年）为 2,094 人——Linux 单版本开发者数已接近 FreeBSD 全年活跃贡献者数；资金规模差距更为悬殊，Linux Foundation 2023 年总收入约 2.626 亿美元（Linux Foundation 2023 年度报告官方 PDF：Rising Tides of Open Source），FreeBSD Foundation 2024 年总收入约 152 万美元（FreeBSD Foundation 2024 年损益表），差距约 173 倍；批评者总结认为，三个维度均反映 FreeBSD 社区发展的结构性挑战——老龄化使核心知识传承困难，新生代吸引力不足使代际更替滞后，与 Linux 规模差距扩大使 FreeBSD 在开源生态中的边际地位面临压力
- 反批评者认为 FreeBSD 社区发展并非危机而是“质量优于规模”的理性选择——其一，社区质量优于规模：FreeBSD committer 制度保证了代码质量，freebsd.duckdb 查询 L3.4.1.top10 显示 4 大 BSD src 仓库合计前 10 贡献者占总 commit 比例从 1993 年 80.98% 下降至 2008 年 17.25%，2015 年 20.97%、2020 年 26.46% 有所回升（非“持续下降”）〔存疑：该组数值经逐库 top10 汇总、四库全局并集 top10、全史 top10 逐年占比三种口径复算均不可复现，精确值与查询口径待复核〕，bus factor 显著改善的结论须据此审慎采信，反映 FreeBSD 社区的贡献分散度总体提升但非单调下降而非集中度危机；FreeBSD src 仓库的代码审查流程（Committer's Guide 规定）保证了补丁质量，与 Linux 的高流量补丁讨论模式形成对比；其二，FreeBSD Foundation 的专业化运作：2024 年 FreeBSD Foundation 在 src、ports、doc 三仓库合计完成 1360+ 代码提交（FreeBSD Foundation 2024-12-20 博客‘FreeBSD Foundation: A Year of Sponsored Development in 2024’），基金会雇佣 4 名安全开发者、1 名基础设施与测试开发者（FreeBSD Foundation 2024-12-30 Deb Goodkin（德布·古德金） 博客‘Reflecting on a Successful 2024’），企业合作伙伴从 2019-2023 年平均 10 家增至 2024 年 15 家，2024 年还获得 Alpha-Omega Fund 与 Silicon Valley Community Fund 两项重要资助用于安全审计与基础设施现代化；2024 年 9 月启动的笔记本电脑支持项目投资超过 100 万美元（Quantum Leap Research 资助），反映基金会积极扩大 FreeBSD 影响力的战略；其三，核心贡献者的稳定性：Core.13 选举（2024-06-12 Hiroki Sato（佐藤広生） 在 freebsd-announce 邮件列表发布）8 名成员构成具有显著地理多样性——Li-Wen Hsu（台湾）、Allan Jude（加拿大）、Gleb Smirnoff（俄罗斯）、Tobias C. Berner（瑞士）、Hiroki Sato（日本）、Olivier Cochard（法国）、Dave Cottlehuber（荷兰/新西兰）、Mathieu Arnold（法国），8 名成员中无一人以美国为主要居住地，反映 FreeBSD 社区从 1990 年代美国中心到 2020 年代全球分布的演化；Core.13 与 Core.12 outgoing 成员（Baptiste Daroussin（巴蒂斯特·达鲁桑）、Benedict Reuschling、Ed Maste（埃德·马斯特）、Greg Lehey、John Baldwin、Emmanuel Vadot（埃马纽埃尔·瓦多）、Mateusz Piotrowski）在传承与更替间保持平衡，选举制保证了技术路线的代际共识；反批评者总结认为，三个维度均反映 FreeBSD 社区的“质量-专业化-稳定性”路径是合理选择，不应以 Linux 的“规模即生命力”标准评判 FreeBSD
- 再批评者指出，反批评的“质量-专业化-稳定性”论证不能掩盖三个当代挑战——其一，“质量优于规模”无法掩盖规模差距的结构性问题：Linux 6.5 单版本开发者数（1,921）已接近 FreeBSD 全年活跃贡献者数（2,094），且 Linux 每个版本都有 271 位首次贡献者（LWN 2023-08-28 报道），FreeBSD 的代际更替速度明显滞后；freebsd.duckdb L1.2.3 显示每年流失贡献者数从 1995 年 27 人激增至 2019 年 22,210 人，bus factor 改善是相对趋势而非绝对优势——FreeBSD 的 bus factor 改善可能反映贡献者基数扩大而非质量提升，且 commit 量不直接等于代码质量；其二，Foundation 专业化运作是积极信号但资金规模差距使可持续性存疑：FreeBSD Foundation 2024 年净运营亏损约 108 万美元（Total Income $1,524,259.17 - Total Expenses \$2,602,007.64，据 FreeBSD Foundation 2024 年损益表），基金会动用储备金维持运作；Linux Foundation 2023 年收入 2.626 亿美元（搜狐 2024-01-08 报道），其中 2% 即约 525 万美元用于 Linux 内核支持——单是 Linux Foundation 对内核的投入就约为 FreeBSD Foundation 全年收入的 3 倍以上；FreeBSD Foundation 2024 年 15 家企业合作伙伴相比 Linux Foundation 2023 年 1709 家支持会员公司，企业参与差距约 114 倍；其三，核心贡献者稳定性是相对的：Mike Karels 2024-06-07 去世反映 CSRG 一代的自然衰退，Core.13 的 8 人方案是 Mike Karels 去世后的应急处理而非制度化解决方案——若 Mike Karels 未去世，Core.13 应为 9 人，Core Team 对第 9 人席位空缺的处理缺乏明确规则；Core.13 的地理多样性虽然是积极信号，但 8 名成员的地理分布是选举结果的偶然呈现而非设计目标，且 Core Team 选举的投票权仅限 active committer，社区普通用户与文档贡献者无投票权，代际共识是 committer 群体内部的共识而非社区整体的共识；再批评者总结认为，三个维度均反映“质量-专业化-稳定性”论证的限度——FreeBSD 社区在 2000 年小规模社区条件下形成的“质量优先”路径在 2020 年代大规模开源生态中面临结构性挑战，如扩大 Foundation 资金来源、建立 Core Team 席位空缺的补选规则、扩大 Core Team 选举投票权范围等
- 综合三层辩证，FreeBSD 社区发展争议的批评、反批评与再批评三个层面既具有合理性（反批评层的“质量-专业化-稳定性”）也面临当代挑战（再批评层的“规模差距-资金可持续性-代际更替”），二者并非非此即彼——“质量优于规模”是 FreeBSD 在 2000 年小规模社区条件下的理性选择（反批评层的合理性），但 Linux 6.5 单版本开发者数（1,921）接近 FreeBSD 全年活跃贡献者数（2,094）是 2020 年代大规模开源生态中的结构性挑战（再批评层的代价）；Foundation 专业化运作是积极信号（反批评层的合理性），但 2024 年净运营亏损约 108 万美元与 Linux Foundation 2.626 亿美元收入的差距是治理代价（再批评层的代价）；Core.13 地理多样性是选举结果的偶然呈现（反批评层的合理性），但 Mike Karels 去世后的 8 人应急方案与投票权仅限 active committer 是治理代价（再批评层的代价）；最终评价应区分“历史语境中的合理性”与“当代条件下的适应性”——FreeBSD 社区在 2000 年小规模社区条件下形成的“质量优先”路径在 2020 年代大规模开源生态中可能需要调整，如扩大 Foundation 资金来源、建立 Core Team 席位空缺的补选规则、扩大 Core Team 选举投票权范围、增加新生代吸引力（如与现代开发工具链整合、加强教材合作）；批评、反批评与再批评的辩证过程本身揭示了 FreeBSD 社区发展问题的复杂性——任何简单的“FreeBSD 社区衰落/繁荣”二元判断都不足以涵盖贡献者老龄化、新生代吸引力、与 Linux 规模差距三个维度的多维度评价；FreeBSD 社区是否需要结构性改革是一个需要社区自身回答的问题——史学分析可以揭示问题但不能替代社区的主体选择；本体论上，CSRG 一代与新生代、committer 与非 committer、企业 committer 与志愿者、批评者与反批评者在本体论上地位相等，各方皆是 FreeBSD 社区发展实践的一刻状态——差异是社区角色与立场偏好上的不同而非本体等级的高下
- 从项目史观总纲第 13、19、21 条审视，FreeBSD 社区发展争议的批评、反批评与再批评各方（批评者、反批评者、再批评者、Core Team 阵营、Foundation、企业 committer、志愿者、新生代开发者）在本体论上地位相等——其一，许可证哲学与利益分配视角（总纲第 13 条“法律与道德是利益分配”）：FreeBSD 社区发展争议的根源在于 BSD 许可证哲学未能形成“投入-回馈”的共荣共生生态——BSD 许可证允许企业自由使用代码而不强制回馈，这使 Netflix、Apple、Juniper 等企业能够使用 FreeBSD 而无需像 RedHat/Canonical 对 Linux 那样大规模投入；Linux Foundation 2023 年收入 2.626 亿美元（含 1709 家支持会员公司）与 FreeBSD Foundation 2024 年收入 152 万美元（含 15 家企业合作伙伴）的差距约 173 倍，是许可证哲学塑造的利益分配结构的具体显现——GPL 的‘copyleft’强制回馈机制形成了 Linux 的共荣共生生态，BSD 的‘permissive’自由使用机制使 FreeBSD 未能形成类似生态；但许可证哲学的差异并非道德缺陷而是历史选择——BSD 许可证体现了“自由即允许不回馈”的哲学，GPL 体现了“自由即强制回馈”的哲学，二者在本体论上地位相等，差异是利益分配机制的不同而非本体等级的高下；FreeBSD Foundation 2024 年动用储备金维持运作（净运营亏损约 108 万美元）是许可证哲学的治理代价，但这一代价是 FreeBSD 社区选择 BSD 许可证哲学的结构性后果而非道德失败；其二，解释学循环与权力知识共谋视角（总纲第 19 条“解释学循环是历史认识的根本条件”）：FreeBSD 社区发展争议的历史认识受前理解差异制约——批评者以“规模即生命力”为前理解，反批评者以“质量即生命力”为前理解，再批评者以“当代条件下的适应性”为前理解，三者难以通约；权力与知识在 FreeBSD 社区发展争议的历史书写中共谋——FreeBSD 官方叙事（如 Foundation 年报、Core Team 公告、Release Notes）强调“质量-专业化-稳定性”，外部批评者叙事（如 LWN/Phoronix 报道、Slashdot/Reddit 讨论）强调“老龄化-吸引力不足-规模差距”，二者在“什么被记录、什么被遗忘”上本身就是权力行使；本节（309.34.1-309.34.4、309.35）的辩证链补足与项目统摄史观审视即是试图打破单一叙事的权力垄断，使批评者、反批评者、再批评者的论点对称呈现；解释学循环亦适用于本审视自身——项目统摄史观审视嵌入项目统摄史观的前理解，须自觉呈现这一前理解而非伪装中立，合图（309.34.4）不是辩证链的终结而是阶段性综合，随 FreeBSD 社区发展演进（如 Foundation 资金来源扩大、Core Team 治理改革、新生代吸引力措施）须重新展开；其三，革命与改革的方法论分歧视角（总纲第 21 条“革命与改革是历史方法论的分歧”）：Linux 靠革命，BSD 靠改革——Linux 的“革命”模式体现为大规模投入（Linux Foundation 2023 年 2.626 亿美元）、快速迭代（Linux 6.5 单版本 1,921 位开发者、271 位首次贡献者）、独裁决策（Linus Torvalds 直接决定采用 Git 2005）；FreeBSD 的“改革”模式体现为小规模精耕（FreeBSD Foundation 2024 年 152 万美元）、稳健演进（FreeBSD 2020 年才完成 Git 迁移，迟缓约 15 年）、共识决策（Core Team 选举 + 共识模式）；改革的困难远高于革命——“破山中贼易，破心中贼难”，FreeBSD 社区在 2000 年小规模社区条件下形成的“质量优先”路径在 2020 年代大规模开源生态中面临结构性挑战，但改革模式的调整需要社区共识的长期积累，不可能像革命模式那样由单一决策者快速调整；FreeBSD 社区发展争议的本质是改革模式的当代困境——批评者以革命模式的标准（规模、速度、新生代吸引力）评判改革模式，反批评者以改革模式的标准（质量、稳定性、代际共识）回应，二者在前理解层面难以通约；最终，FreeBSD 社区是否需要从“改革”模式向“革命”模式部分调整是一个需要社区自身回答的问题——史学分析可以揭示改革模式的当代困境但不能替代社区的主体选择；本体论上，革命模式与改革模式在本体论上地位相等，差异是历史方法论的不同而非本体等级的高下

## 史观

- 总纲第 4 条——分离聚合是永恒规律：CSRG 一代的自然衰退是世代分离的具体显现；总纲第 13 条——法律与道德是利益分配：Linux Foundation 与 FreeBSD Foundation 的资金差距是利益分配结构的具体显现；专题语（不设总纲条号）——信息技术工具采用速度受治理模式影响：FreeBSD 2020 年才完成 Git 迁移反映共识模式的迟缓
- 总纲第 13 条——法律与道德是利益分配：BSD 许可证哲学与 GPL 许可证哲学的差异是利益分配机制的具体显现——Linux Foundation 与 FreeBSD Foundation 的资金差距是许可证哲学塑造的利益分配结构；总纲第 19 条——解释学循环：FreeBSD 社区发展争议的历史认识受前理解差异制约，无中立旁观者；权力与知识在社区发展争议的历史书写中共谋；总纲第 21 条——革命与改革是历史方法论的分歧：Linux 的革命模式与 FreeBSD 的改革模式在本体论上地位相等，分歧在于历史路径与社区条件而非高下

## 辨析

- 考据过程留痕——【查证来源】Linux 6.5 内核开发者数据经 LWN 2023-08-28 Jonathan Corbet 文章一手核验（<https://lwn.net/Articles/941675/> ），1,921 位开发者与 271 位首次贡献者数字确认；Linux Foundation 2023 年收入 2.626 亿美元经 Linux Foundation 官方年度报告 PDF
- 考据过程留痕——【查证来源】项目史观总纲第 13、19、21 条经 据原文第 25 章 一手核验；第 13 条原文“法律与道德是利益分配。任何道德问题本质上是利益问题，社区治理亦是形式主义的政治产物”；第 19 条原文“解释学循环是历史认识的根本条件。前理解的差异使分歧不可避免。权力与知识在历史书写中共谋——什么被记录、什么被遗忘，本身就是权力行使”；〔待核：原文截断，后文待回源〕

## 文献

- freebsd.duckdb 查询 L1.2.3、L1.2.2（查询留痕原引 `原材料/研究/bsd仓库分析/数据分析/宏观趋势统计.md` §L1.2.3、§L1.2.2，该路径已不在库内，档案去向待查〔存疑：原材料目录归档位置待回溯〕）；Mike Karels 讣告 [EB/OL]. John Baldwin, 2024-06-07. <https://lists.freebsd.org/archives/freebsd-announce/2024-June/000135.html>（访问日期 2026-07-24）；Corbet J. Development statistics for the 6.5 kernel [EB/OL]. LWN, 2023-08-28.
- 项目史观总纲第 13、19、21 条（据原文第 25 章）；第 309.34.1-309.34.4 节辩证链补足；Linux Foundation 2023 Annual Report（同 309.34.1 节）；FreeBSD Foundation 2024 Profit and Loss Report（同 309.34.1 节）；Corbet J. Development statistics for the 6.5 kernel（同 309.34.1 节）；参见 309.17、309.18、309.27a、309.27b、309.27c、309.32 节史料 ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-16-040 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-16-040`；login 逐条遍历判定采纳）

2000 年 Mark Burgess 在 ;login: 倡导以科学实证方法研究系统管理，提出在相同硬件上比较 FreeBSD、GNU/Linux、NT 等系统与 Apache/IIS 的效率等可检验问题，标志系统管理作为研究学科的自觉。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

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

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

