# 98 【Linux社区】TAB选举章程与术语正反

> 来源：tech-board-discuss p2（50 封全读，2007-08 至 2026-03，维护者支持小组讨论、EXPORT_SYMBOL_GPL 与 LTTng、2017 选举结果与 SDAPS 计票、章程修订缺席投票、Fixes 标签日期之辩、苏联新话之警）
> 判定：43 CAND / 7 NV。主题分布：维护者支持小组讨论 1、反对 EXPORT_SYMBOL_GPL 苛刻政策 1、TAB 竞选自提名声明 1、2017 TAB 选举结果公告 1、说明 TAB 过去一年工作 1、受理 Corbet 自提名 1、2024 TAB 选举候选人征集 1、自提名兼批评 TAB 1、TAB 竞选自提名 2、TAB 章程修订公告 1、Fixes 标签加提交日期提案 1、回应 TAB 透明度质疑 1、反对包容性术语补丁 1、TAB 被提名人名单汇总 1、质疑 CoC 解释文档制定过程 1、反对 Fixes 标签加日期 1、2013 TAB 选举公告 1、术语辩论：红黑树类比 1、解答选举资格问题 1、提议 slave 译为 device 1、选举提名操作细则 1、审阅 CoC 季度报告 1、LLM 重写与版权法 1、反驳旧硬件驱动与电子垃圾论 1、驱动开发硬件获取计划 1、主张扩大 TAB 投票人范围 1、认可补丁并给出关键出处 1、CoC 委员会 2019 年 12 月报告 1、确认 TAB 纪要已补齐 1、贡献者投票资格讨论 1、选举最终提醒与流程 1、否决 SPI 式会员投票制 1、分工协调 checkpatch 更新 1、反驳 Alan Cox 立场反复 1、LPC 2016 组委会任命公告 1、术语选择建议 1、Fixes 加日期的历史与权衡 1、TAB 投票资格治理立场 1、拒绝 Fixes 标签加日期 1、2007 TAB 选举公告 1、指出文档表述范围过窄 1、预告竞选纲领 1。

## 【Linux社区】零、体例说明

本文件系 tech-board-discuss p2（实锚 pk 9362642-9362690）的逐封提取（43 CAND / 7 NV），全 42 块采用**单行摘要体例**（丙型）：每块由“## 98.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 98.1 维护者支持小组讨论

- 【Linux社区】补充倦怠风险自查清单资源；主张在维护者峰会前先开公开会议，征集未获邀开发者的意见 `<!-- ROW_MINE: tech-board-discuss.messages.9362642 -->`

## 98.2 反对 EXPORT_SYMBOL_GPL 苛刻政策

- 【Linux社区】驳斥“照顾朋友”指控；说明 LTTng 75K SLOC 上游化困境：无子系统接手、无人评审 75K 行代码 `<!-- ROW_MINE: tech-board-discuss.messages.9362643 -->`

## 98.3 TAB 竞选自提名声明

- 【Linux社区】陈述 TAB 职责与个人文件系统/Meta 背景，寻求连任 TAB 主席 `<!-- ROW_MINE: tech-board-discuss.messages.9362644 -->`

## 98.4 2017 TAB 选举结果公告

- 【Linux社区】73 张选票各候选人得票数；SDAPS 自动计票加人工复核的流程记录与开源计票脚本发布 `<!-- ROW_MINE: tech-board-discuss.messages.9362646 -->`

## 98.5 说明 TAB 过去一年工作

- 【Linux社区】概述 TAB 职能清单：kernel.org 接管与恢复、与 SFC 讨论 GPL 执法、UEFI 安全启动应对 `<!-- ROW_MINE: tech-board-discuss.messages.9362647 -->`

## 98.6 受理 Corbet 自提名

- 【Linux社区】TAB 主席确认提名程序：KS 当天宣读声明，欢迎提前张贴到列表 `<!-- ROW_MINE: tech-board-discuss.messages.9362648 -->`

## 98.7 2024 TAB 选举候选人征集

- 【Linux社区】完整公告：任期名单、投票资格判据（3 个 tag commit）、CIVS 电子投票与提名截止时间 `<!-- ROW_MINE: tech-board-discuss.messages.9362649 -->`

## 98.8 自提名兼批评 TAB

- 【Linux社区】表态参选，但指从会议纪要看不出该组织实际在做什么 `<!-- ROW_MINE: tech-board-discuss.messages.9362650 -->`

## 98.9 TAB 竞选自提名

- 【Linux社区】宣布参选并计划亲赴首尔 Kernel Summit 出席选举 `<!-- ROW_MINE: tech-board-discuss.messages.9362651 -->`
- 【Linux社区】单句自提名参选 2008 年 TAB 选举，属选举流程记录 `<!-- ROW_MINE: tech-board-discuss.messages.9362671 -->`

## 98.10 TAB 章程修订公告

- 【Linux社区】“受邀者投票”改为“与会者投票”，新增可设缺席投票标准的条款（附 diff） `<!-- ROW_MINE: tech-board-discuss.messages.9362652 -->`

## 98.11 Fixes 标签加提交日期提案

- 【Linux社区】以 git log 统计证明主题大量重复，主张 Fixes 含提交日期可杜绝哈希碰撞歧义并支持两字段检索 `<!-- ROW_MINE: tech-board-discuss.messages.9362653 -->`

## 98.12 回应 TAB 透明度质疑

- 【Linux社区】确认章程规定被提名人须作陈述；已补齐官网可查的会议纪要 `<!-- ROW_MINE: tech-board-discuss.messages.9362655 -->`

## 98.13 反对包容性术语补丁

- 【Linux社区】以苏联“新话”亲身经历警告语言管制的滑坡，反驳“良好意图”论证 `<!-- ROW_MINE: tech-board-discuss.messages.9362656 -->`

## 98.14 TAB 被提名人名单汇总

- 【Linux社区】发布含 5 人声明链接的共享文档，声明更新截止时间与提名顺序规则 `<!-- ROW_MINE: tech-board-discuss.messages.9362657 -->`

## 98.15 质疑 CoC 解释文档制定过程

- 【Linux社区】严格辨析“基于社区输入”的表述，指该文档未走正常公开评审即合并，属不透明操作 `<!-- ROW_MINE: tech-board-discuss.messages.9362658 -->`

## 98.16 反对 Fixes 标签加日期

- 【Linux社区】日期无参考价值，用 git describe --contains 查所在版本更高效 `<!-- ROW_MINE: tech-board-discuss.messages.9362659 -->`

## 98.17 2013 TAB 选举公告

- 【Linux社区】爱丁堡 KS 选举安排、4 名现任被提名人名单及提名截止时间 `<!-- ROW_MINE: tech-board-discuss.messages.9362660 -->`

## 98.18 术语辩论：红黑树类比

- 【Linux社区】论证颜色作任意标签无语义负载而 whitelist/blacklist 有实际含义，反驳 Willy 的类比 `<!-- ROW_MINE: tech-board-discuss.messages.9362661 -->`

## 98.19 解答选举资格问题

- 【Linux社区】说明任何人都可自提名；电子投票后改为书面声明，历史上缺席者难以当选 `<!-- ROW_MINE: tech-board-discuss.messages.9362662 -->`

## 98.20 提议 slave 译为 device

- 【Linux社区】针对 w1 总线这一内核最大 master/slave 术语使用方提出替换建议 `<!-- ROW_MINE: tech-board-discuss.messages.9362663 -->`

## 98.21 选举提名操作细则

- 【Linux社区】按提交顺序排名、勿以回复形式提名以免漏计等流程规则 `<!-- ROW_MINE: tech-board-discuss.messages.9362664 -->`

## 98.22 审阅 CoC 季度报告

- 【Linux社区】认可调查结论，并追问教育辅导能否转化为文档改进 `<!-- ROW_MINE: tech-board-discuss.messages.9362665 -->`

## 98.23 LLM 重写与版权法

- 【Linux社区】指明清洁室重写的定义门槛；LLM 已使版权法进入未定义领域，引 Uber 先扩散后合法化策略类比 `<!-- ROW_MINE: tech-board-discuss.messages.9362666 -->`

## 98.24 反驳旧硬件驱动与电子垃圾论

- 【Linux社区】以 SCSI 与 SATA 容量带宽数据反驳；阐述自由软件“自己修或付费修”原则与 git revert 恢复机制 `<!-- ROW_MINE: tech-board-discuss.messages.9362667 -->`

## 98.25 驱动开发硬件获取计划

- 【Linux社区】LF 执行主管同意先积累再宣布，并提供 CRM 系统协助对接各成员公司技术联系人 `<!-- ROW_MINE: tech-board-discuss.messages.9362668 -->`

## 98.26 主张扩大 TAB 投票人范围

- 【Linux社区】认为理想定义为“社区任何成员”，建议逐年显著扩大投票池并评估再放宽 `<!-- ROW_MINE: tech-board-discuss.messages.9362669 -->`

## 98.27 认可补丁并给出关键出处

- 【Linux社区】Acked-by 之外附 Linus 反对另立术语文档的发言链接，回答 Joe Perches 的质询 `<!-- ROW_MINE: tech-board-discuss.messages.9362670 -->`

## 98.28 CoC 委员会 2019 年 12 月报告

- 【Linux社区】官方报告：1 起邮件侮辱行为经教育辅导处理；CoC 网站将同步发布后续报告 `<!-- ROW_MINE: tech-board-discuss.messages.9362672 -->`

## 98.29 确认 TAB 纪要已补齐

- 【Linux社区】追问后确认纪要仓库已更新至 2021 年 6 月，TAB 透明度问责闭环 `<!-- ROW_MINE: tech-board-discuss.messages.9362673 -->`

## 98.30 贡献者投票资格讨论

- 【Linux社区】主张 git 时代（2.6.12 起）有补丁者即算贡献者；探讨 top-N 指标与扩大社区参与的取舍 `<!-- ROW_MINE: tech-board-discuss.messages.9362674 -->`

## 98.31 选举最终提醒与流程

- 【Linux社区】完整议程、无记名纸票与计票程序、16 名候选人全名单及写票位安排 `<!-- ROW_MINE: tech-board-discuss.messages.9362675 -->`

## 98.32 否决 SPI 式会员投票制

- 【Linux社区】引 SPI 章程说明贡献会员资格认定负担重，TAB 无人力为年度选举执行该机制 `<!-- ROW_MINE: tech-board-discuss.messages.9362676 -->`

## 98.33 分工协调 checkpatch 更新

- 【Linux社区】同意补丁合入后由 Park 负责在 checkpatch 中同步推荐替换词，给出提示文案思路 `<!-- ROW_MINE: tech-board-discuss.messages.9362677 -->`

## 98.34 反驳 Alan Cox 立场反复

- 【Linux社区】引 2006 年存档链接证明其去年反对邮件投票，与今年主张相矛盾 `<!-- ROW_MINE: tech-board-discuss.messages.9362680 -->`

## 98.35 LPC 2016 组委会任命公告

- 【Linux社区】代表 TAB 宣布主席、司库、程序委员会等 9 人名单及筹办时间地点 `<!-- ROW_MINE: tech-board-discuss.messages.9362681 -->`

## 98.36 术语选择建议

- 【Linux社区】主张用语义明确的 allow/block，而非 yes/no 等依赖上下文的泛化词 `<!-- ROW_MINE: tech-board-discuss.messages.9362682 -->`

## 98.37 Fixes 加日期的历史与权衡

- 【Linux社区】回顾社区此前已拒绝该格式；工具链不支持、哈希足够长即可，不值得为此改动 `<!-- ROW_MINE: tech-board-discuss.messages.9362683 -->`

## 98.38 TAB 投票资格治理立场

- 【Linux社区】质疑“社区任何成员”定义，主张利益攸关最大者影响力最大，防暴民式代表 `<!-- ROW_MINE: tech-board-discuss.messages.9362684 -->`

## 98.39 拒绝 Fixes 标签加日期

- 【Linux社区】会破坏全部解析工具与脚本；日期有误导性，所在发布版而非作者日期才是关键 `<!-- ROW_MINE: tech-board-discuss.messages.9362686 -->`

## 98.40 2007 TAB 选举公告

- 【Linux社区】KS BOF 选举安排、3 名被提名人、截止时间及缺席者提名代读机制 `<!-- ROW_MINE: tech-board-discuss.messages.9362687 -->`

## 98.41 指出文档表述范围过窄

- 【Linux社区】提醒种族议题与奴隶制受害不限于非洲裔，理由文档措辞应更周延 `<!-- ROW_MINE: tech-board-discuss.messages.9362688 -->`

## 98.42 预告竞选纲领

- 【Linux社区】回应 Taht 的工程原则诉求，称正在筹备并将于提名声明中提出 `<!-- ROW_MINE: tech-board-discuss.messages.9362690 -->`
