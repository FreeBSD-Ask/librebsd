# 110 【Linux社区】自荐系列与slave用量统计

> 来源：tech-board-discuss p14（50 封全读，2007-08 至 2026-03，Mason/Sang/Hildenbrand/Rostedt/Taht 自荐、Wilcox drivers/ slave 用量 grep 统计、Kees 2018-2024 投票率数据、纪要公开至 kernel.org git、列表迁移 lore 归档、CoC 私下 ack 三选择困境、Pavel 对 denylist 投 NAK）
> 体例说明：本页 46 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：47 CAND / 3 NV。主题分布：TAB竞选自荐（重发） 1、TAB选举CIVS投票链接问题 1、千行补丁系列的流程建议 1、TAB竞选自荐 1、TAB会议纪要发布承诺 1、2010 TAB选举最终提醒 1、包容性术语补丁审阅 1、2007 TAB提名进展 1、EXPORT_SYMBOL_GPL政策立场 1、CIVS重复激活缺陷报告 1、TAB自荐 2、2008 TAB选举BoF安排 1、“device”替代slave之争 1、TAB纪要公开git仓库 1、借用SPI选举系统 1、2019选举候选人不足 1、KS举办选举本是权宜 1、章程修改与kernel.org账户投票 1、Fixes标签加作者日期提案被拒 1、自荐加入2009 TAB名单 1、2024 TAB选举开票通知 1、2010 TAB选举结果 1、TAB在LF三论坛中的定位 1、LLM改写与净室成本论证 1、CoC私下征求ack的困境分析 1、列表迁移lists.linux.dev公告 1、2022年9月CoC委员会报告 1、TAB选举投票率数据 1、CIVS配置页无投票列表 1、2015自荐TAB 1、代码之外的多元文化讨论 1、slave术语的个人观察 1、贡献成熟度模型公司偏向补丁 1、Dave Taht自荐（200词版） 1、反对denylist替换blacklist 1、反对纯民主的治理立场 1、slave用法量化统计 1、提名规则澄清 1、选举方式沿革 1、CoC报告反馈与提议 1、多邮箱合并成投票痛点 1、热点讨论流程两项提案 1、为驱动开发获取硬件的提案 1、质疑blacklist替换必要性 1、包容性术语详细技术反馈 1、为device替代辩护 1。

## 110.1 TAB竞选自荐（重发）

- 【Linux社区】Chris Mason自荐连任TAB主席，回顾Btrfs与存储背景，强调协作质量与行为准则共识。 `<!-- ROW_MINE: tech-board-discuss.messages.9363242 -->`

## 110.2 TAB选举CIVS投票链接问题

- 【Linux社区】选举协调人Laura Abbott确认已重新发送投票链接并解释CIVS邮件服务器缓慢。 `<!-- ROW_MINE: tech-board-discuss.messages.9363243 -->`

## 110.3 千行补丁系列的流程建议

- 【Linux社区】Arjan提出发千行补丁前应先询问最可能的审阅者偏好方式的最佳实践。 `<!-- ROW_MINE: tech-board-discuss.messages.9363244 -->`

## 110.4 TAB竞选自荐

- 【Linux社区】Wolfram Sang自荐，关注维护者与审阅者短缺及TAB透明度，强调嵌入式与咨询背景。 `<!-- ROW_MINE: tech-board-discuss.messages.9363245 -->`

## 110.5 TAB会议纪要发布承诺

- 【Linux社区】Jim Zemlin确认纪要存在并承诺会后尽快发布，提及发布前先在内部列表审核。 `<!-- ROW_MINE: tech-board-discuss.messages.9363246 -->`

## 110.6 2010 TAB选举最终提醒

- 【Linux社区】列出7名被提名人、提名截止为选举当晚，开放KS与Plumbers与会者投票。 `<!-- ROW_MINE: tech-board-discuss.messages.9363247 -->`

## 110.7 包容性术语补丁审阅

- 【Linux社区】Shuah Khan论证allowlist/denylist更直观且全球语义统一，主动提供Signed-off-by。 `<!-- ROW_MINE: tech-board-discuss.messages.9363248 -->`

## 110.8 2007 TAB提名进展

- 【Linux社区】Bottomley通报5人提名名单，距形成真正竞争还差1人。 `<!-- ROW_MINE: tech-board-discuss.messages.9363249 -->`

## 110.9 EXPORT_SYMBOL_GPL政策立场

- 【Linux社区】Hellwig坚持无现成用户不得导出的政策，反对例外以免侵蚀原则，建议upstreaming lttng。 `<!-- ROW_MINE: tech-board-discuss.messages.9363250 -->`

## 110.10 CIVS重复激活缺陷报告

- 【Linux社区】Brown报告已激活邮箱再次激活时报错且无任何投票链接，指出选举流程具体故障。 `<!-- ROW_MINE: tech-board-discuss.messages.9363251 -->`

## 110.11 TAB自荐

- 【Linux社区】David Hildenbrand首次自荐TAB，关注社区友好、行为问题处理与维护者过载。 `<!-- ROW_MINE: tech-board-discuss.messages.9363252 -->`
- 【Linux社区】Rostedt自荐连任，提出AI影响与维护者倦怠议题并计划重启相关工作。 `<!-- ROW_MINE: tech-board-discuss.messages.9363278 -->`

## 110.12 2008 TAB选举BoF安排

- 【Linux社区】公布5名被提名人、投票时间与提名截止，首次允许Plumbers与会者投票。 `<!-- ROW_MINE: tech-board-discuss.messages.9363254 -->`

## 110.13 “device”替代slave之争

- 【Linux社区】NeilBrown反驳Wilcox的device替代建议，指其语义近乎“thing”而无所指。 `<!-- ROW_MINE: tech-board-discuss.messages.9363255 -->`

## 110.14 TAB纪要公开git仓库

- 【Linux社区】Sasha Levin宣布TAB月度纪要将发布于kernel.org git仓库以提升透明度。 `<!-- ROW_MINE: tech-board-discuss.messages.9363256 -->`

## 110.15 借用SPI选举系统

- 【Linux社区】Wilcox建议借鉴Software in the Public Interest的选举系统改进TAB选举机制。 `<!-- ROW_MINE: tech-board-discuss.messages.9363257 -->`

## 110.16 2019选举候选人不足

- 【Linux社区】Dave Taht指出仅2人竞逐5席，建议加强宣传并给出投票规则链接。 `<!-- ROW_MINE: tech-board-discuss.messages.9363258 -->`

## 110.17 KS举办选举本是权宜

- 【Linux社区】Wilcox提出TAB选举在Kernel Summit举行仅为临时方案而非惯例的立场。 `<!-- ROW_MINE: tech-board-discuss.messages.9363259 -->`

## 110.18 章程修改与kernel.org账户投票

- 【Linux社区】Rostedt阐述TAB内部结论：kernel.org账户加内核活跃度是防刷票的远程投票第一步。 `<!-- ROW_MINE: tech-board-discuss.messages.9363260 -->`

## 110.19 Fixes标签加作者日期提案被拒

- 【Linux社区】Rostedt反驳加短作者日期会导致误判的说法，明确表示不会采纳。 `<!-- ROW_MINE: tech-board-discuss.messages.9363261 -->`

## 110.20 自荐加入2009 TAB名单

- 【Linux社区】Thomas Gleixner响应Grant Likely号召自荐参选TAB。 `<!-- ROW_MINE: tech-board-discuss.messages.9363263 -->`

## 110.21 2024 TAB选举开票通知

- 【Linux社区】Corbet公布11名候选人名单、CIVS投票指引与9月27日截止日期。 `<!-- ROW_MINE: tech-board-discuss.messages.9363264 -->`

## 110.22 2010 TAB选举结果

- 【Linux社区】公布8名被提名人与5位当选者名单，Corbet任监选人。 `<!-- ROW_MINE: tech-board-discuss.messages.9363265 -->`

## 110.23 TAB在LF三论坛中的定位

- 【Linux社区】Arjan反驳纯民主方案，说明TAB是面向开发者社区的论坛，与用户、厂商论坛分立。 `<!-- ROW_MINE: tech-board-discuss.messages.9363266 -->`

## 110.24 LLM改写与净室成本论证

- 【Linux社区】Bottomley论证LLM净室分离验证难以扩展且成本高昂，故不必担心内核被LLM重写。 `<!-- ROW_MINE: tech-board-discuss.messages.9363267 -->`

## 110.25 CoC私下征求ack的困境分析

- 【Linux社区】Geert分析私下渠道被邀ack已有多签补丁的三种选择及其局限，指出补丁此后未再更新。 `<!-- ROW_MINE: tech-board-discuss.messages.9363268 -->`

## 110.26 列表迁移lists.linux.dev公告

- 【Linux社区】Konstantin公布mailman-2退役、新地址、lore归档、List-ID变更等迁移细节。 `<!-- ROW_MINE: tech-board-discuss.messages.9363270 -->`

## 110.27 2022年9月CoC委员会报告

- 【Linux社区】Shuah代表CoC委员会提交半年报告：收到1起邮件不当行为投诉并已公开道歉解决。 `<!-- ROW_MINE: tech-board-discuss.messages.9363271 -->`

## 110.28 TAB选举投票率数据

- 【Linux社区】Kees Cook给出2018至2024历年投票率统计（2024为229/934即24.5%）。 `<!-- ROW_MINE: tech-board-discuss.messages.9363272 -->`

## 110.29 CIVS配置页无投票列表

- 【Linux社区】Brown报告配置URL不列出任何poll、去激活再激活也不显示，补充缺陷细节。 `<!-- ROW_MINE: tech-board-discuss.messages.9363273 -->`

## 110.30 2015自荐TAB

- 【Linux社区】Steven Rostedt自荐参选并确认将到场投票。 `<!-- ROW_MINE: tech-board-discuss.messages.9363274 -->`

## 110.31 代码之外的多元文化讨论

- 【Linux社区】Chris Mason认同Pinchart的多元文化视角，自述避免本地习语与内部梗以照顾全球开发者。 `<!-- ROW_MINE: tech-board-discuss.messages.9363275 -->`

## 110.32 slave术语的个人观察

- 【Linux社区】Rostedt以亲身经历说明slave一词令人不适，且设备间并无奴役关系，术语本身有误导。 `<!-- ROW_MINE: tech-board-discuss.messages.9363276 -->`

## 110.33 贡献成熟度模型公司偏向补丁

- 【Linux社区】Finn Thain提交补丁修正模型只考虑企业的偏向，引用OMM/CMMI文献主张兼顾非营利组织。 `<!-- ROW_MINE: tech-board-discuss.messages.9363277 -->`

## 110.34 Dave Taht自荐（200词版）

- 【Linux社区】自述Bufferbloat与fq_codel等成绩，主张改善厂商开源流程并缩短开发部署周期。 `<!-- ROW_MINE: tech-board-discuss.messages.9363279 -->`

## 110.35 反对denylist替换blacklist

- 【Linux社区】Pavel Machek要求先理解内核中blacklist的实际用法，对v3补丁投NAK。 `<!-- ROW_MINE: tech-board-discuss.messages.9363280 -->`

## 110.36 反对纯民主的治理立场

- 【Linux社区】Ted Ts'o 主张精英制而非 Debian 式纯民主，支持实体会议投票以过滤选民资格。 `<!-- ROW_MINE: tech-board-discuss.messages.9363281 -->`

## 110.37 slave用法量化统计

- 【Linux社区】Wilcox给出drivers/各子系统slave行数统计，自嘲w1应是“最刺眼”而非最大用户。 `<!-- ROW_MINE: tech-board-discuss.messages.9363282 -->`

## 110.38 提名规则澄清

- 【Linux社区】Arjan指出Chris Wright已是TAB成员不能再被提名。 `<!-- ROW_MINE: tech-board-discuss.messages.9363283 -->`

## 110.39 选举方式沿革

- 【Linux社区】Rostedt回顾去年首用电子投票、取消现场演讲改发书面声明等选举流程变化。 `<!-- ROW_MINE: tech-board-discuss.messages.9363284 -->`

## 110.40 CoC报告反馈与提议

- 【Linux社区】Shuah称报告期活动水平可管理无隐忧，提议在会议设CoC Ask an Expert环节。 `<!-- ROW_MINE: tech-board-discuss.messages.9363285 -->`

## 110.41 多邮箱合并成投票痛点

- 【Linux社区】选举协调人Laura确认曾尝试合并多邮箱并承认是需明年修复的痛点。 `<!-- ROW_MINE: tech-board-discuss.messages.9363286 -->`

## 110.42 热点讨论流程两项提案

- 【Linux社区】Jason Cooper提出延迟归档（90天后公开）与分布式成员制列表两种流程改进。 `<!-- ROW_MINE: tech-board-discuss.messages.9363287 -->`

## 110.43 为驱动开发获取硬件的提案

- 【Linux社区】MMC维护者Chris Ball请LF设立培养厂商联系人的机制帮助维护者获得测试硬件。 `<!-- ROW_MINE: tech-board-discuss.messages.9363288 -->`

## 110.44 质疑blacklist替换必要性

- 【Linux社区】Pavel Machek称看不出blacklist有何不包容，主张先grep内核实际用法再谈替换。 `<!-- ROW_MINE: tech-board-discuss.messages.9363289 -->`

## 110.45 包容性术语详细技术反馈

- 【Linux社区】Lutomirski建议补入whitelist、提出target与master语义复杂性、主张用描述性短语替代。 `<!-- ROW_MINE: tech-board-discuss.messages.9363290 -->`

## 110.46 为device替代辩护

- 【Linux社区】Greg KH反驳NeilBrown，称controller/device是USB等规范沿用数十年的通用术语。 `<!-- ROW_MINE: tech-board-discuss.messages.9363291 -->`
