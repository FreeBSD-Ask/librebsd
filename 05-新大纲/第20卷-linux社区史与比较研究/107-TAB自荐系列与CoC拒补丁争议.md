# 107 【Linux社区】TAB自荐系列与CoC拒补丁争议

> 来源：tech-board-discuss p10（50 封全读，2006-08 至 2026-03，Kosina/Pieralisi/Kicinski/Lawall 等自荐声明系列、Greg 确认借 CoC 反制拒补丁非新现象、Steve Fixes 日期 NAK“为问题找方案”、LLM 重写=维护者大分叉之论、2007 git 配额选举批评、2013/2018 选举结果）
> 体例说明：本页 37 块采用**速览体例**——块下仅存单行摘记（主题陈述＋史料锚），要点、史观、辨析、文献四字段另立详表承载；五字段完整体例见 00-总览 §一.2。本页卷头未登记 claim 编号区间，文献著录与史观映射待详表单独立卷时补录。
> 判定：41 CAND / 9 NV。主题分布：TAB non-nomination 1、TAB 选举投票资格脚本 1、TAB 自荐（Julia Lawall） 1、CodingStyle 包容性术语 2、TAB 提名声明更新 1、TAB 自荐（Jiri Kosina） 1、TAB 自荐（Lorenzo Pieralisi） 1、xz 事件与供应链攻击 1、项目连续性文档 2、TAB 选举提名征集 1、TAB 自荐（Jakub Kicinski） 1、TAB 自荐与双重角色质询 1、贡献成熟度模型 1、2007 TAB 选举程序 1、CoC 委员会 2020 年 10 月报告 1、Fixes 标签加作者日期 2、2024 TAB 选举结果 1、LPC 2017 组办方征集 1、SCSI 文档与硬件需求 1、unwind 符号 GPL 导出 2、CodingStyle 包容性术语 v2 1、2007 TAB 选举代表性质 1、CoC 委员会 2024 下半年报告 v2 1、TAB 参选声明格式 1、CoC 报告与拒补丁争议 1、TAB 选举资格脚本 1、2013 TAB 选举结果 1、TAB 自荐（Ricardo Neri） 1、2018 TAB 选举结果 1、CoC 后续与 Linus 姿态 1、TAB 2016 连任自荐 1、2007 选举投票机制提案 1、2009 TAB 选举与提名 1、TAB 提名（Theodore Ts'o） 1、TAB 提名（Kent Overstreet） 1、CoC 更新过程说明 1、LLM 重写与许可证分叉 1。

## 107.1 TAB non-nomination

- 【Linux社区】用 git 标签统计核算 Perches 约列第240名，指出 git 统计客观但指标易被刷分且难以衡量新架构支持等真实贡献价值 `<!-- ROW_MINE: tech-board-discuss.messages.9363042 -->`

## 107.2 TAB 选举投票资格脚本

- 【Linux社区】确认资格脚本输出的含义后，追问该资格标准今后是否同样适用于 TAB 主席与联合主席选举 `<!-- ROW_MINE: tech-board-discuss.messages.9363043 -->`

## 107.3 TAB 自荐（Julia Lawall）

- 【Linux社区】以 TAB 主席身份背书 Julia 参选并称其为楷模，同时确认 Sasha Levin 三届任期后不再连任 `<!-- ROW_MINE: tech-board-discuss.messages.9363044 -->`

## 107.4 CodingStyle 包容性术语

- 【Linux社区】主张 allow-list 无需作 whitelist 的逐词替换，改写为“add the syscall to the allow-list”即可自然表达 `<!-- ROW_MINE: tech-board-discuss.messages.9363045 -->`
- 【Linux社区】语言学分析：allow 与 list 皆可为动词致“双动词”违和感，预期高频接触后会自然接受该用法 `<!-- ROW_MINE: tech-board-discuss.messages.9363064 -->`

## 107.5 TAB 提名声明更新

- 【Linux社区】提交更新版参选声明：内核瘦身、嵌入式与 IoT、RCU 审阅，愿推动 TAB 与核心基础设施计划持续对话 `<!-- ROW_MINE: tech-board-discuss.messages.9363046 -->`

## 107.6 TAB 自荐（Jiri Kosina）

- 【Linux社区】完整自荐声明：HID 与 livepatching 维护者、SUSE 工程总监，强调技术之外协调与化解冲突的经验 `<!-- ROW_MINE: tech-board-discuss.messages.9363048 -->`

## 107.7 TAB 自荐（Lorenzo Pieralisi）

- 【Linux社区】完整自荐声明：ACPI/PSCI/CPUidle 与 PCI 控制器维护者、LPC 计划委员会成员，愿以组织经验服务 TAB `<!-- ROW_MINE: tech-board-discuss.messages.9363049 -->`

## 107.8 xz 事件与供应链攻击

- 【Linux社区】主张勿过度聚焦本次倦怠攻击路径，国家级行动者下次手法或异，提出比对发行版与 git 构建二进制差异等检测思路 `<!-- ROW_MINE: tech-board-discuss.messages.9363050 -->`

## 107.9 项目连续性文档

- 【Linux社区】澄清该文档目的非穷举所有坏场景，而是说明“若现有方案失灵将如何组织未来计划”的元计划定位 `<!-- ROW_MINE: tech-board-discuss.messages.9363051 -->`
- 【Linux社区】支持 Greg 的立场：关键价值在于白纸黑字写明“存在计划”，破除 LF 深处藏有秘密遗嘱的猜测 `<!-- ROW_MINE: tech-board-discuss.messages.9363069 -->`

## 107.10 TAB 选举提名征集

- 【Linux社区】以 TAB 主席身份发布 2017 布拉格 KS 选举程序、五席改选、提名截止与声明汇总文档等流程安排 `<!-- ROW_MINE: tech-board-discuss.messages.9363052 -->`

## 107.11 TAB 自荐（Jakub Kicinski）

- 【Linux社区】参选声明：netdev 维护者谋求第二任期，坦承推动参与度与透明度成效有限，并呼吁更多人参选带来新视角 `<!-- ROW_MINE: tech-board-discuss.messages.9363053 -->`

## 107.12 TAB 自荐与双重角色质询

- 【Linux社区】追问 Ted 参选是否构成 LF CTO 代表与 TAB 委员的双重角色，触及治理角色冲突问题 `<!-- ROW_MINE: tech-board-discuss.messages.9363054 -->`

## 107.13 贡献成熟度模型

- 【Linux社区】质疑自上而下方法论与自下而上协作的错配，指出 LCMM 已偏离 CMMI 分级逻辑且 commit 计数或非正确指标 `<!-- ROW_MINE: tech-board-discuss.messages.9363057 -->`

## 107.14 2007 TAB 选举程序

- 【Linux社区】批评 git commit 配额式选举不民主将损及公信力，抨击 KS 排他性名额与 USENIX 高预算的辩护理由 `<!-- ROW_MINE: tech-board-discuss.messages.9363058 -->`

## 107.15 CoC 委员会 2020 年 10 月报告

- 【Linux社区】官方报告：1至10月共3起举报，处置含教育辅导、锁定 github 仓库、澄清 CoC 仅适用于个人行为 `<!-- ROW_MINE: tech-board-discuss.messages.9363059 -->`

## 107.16 Fixes 标签加作者日期

- 【Linux社区】反对在 Fixes 加日期：判断修复适用性只需 commit id 加 git tag --contains，日期几乎无用 `<!-- ROW_MINE: tech-board-discuss.messages.9363060 -->`
- 【Linux社区】NAK：重复主题多源于 merge 提交，git show 即可消歧，加日期是给全体开发者添噪的“为问题找方案” `<!-- ROW_MINE: tech-board-discuss.messages.9363091 -->`

## 107.17 2024 TAB 选举结果

- 【Linux社区】指出投票率不足25%的数据观察，祝贺当选者并感谢 Corbet 组织为期一周的投票 `<!-- ROW_MINE: tech-board-discuss.messages.9363061 -->`

## 107.18 LPC 2017 组办方征集

- 【Linux社区】代表 TAB 发布 Linux Plumbers 2017 组委会申请条件、10月1日截止与11月11日前决定的流程 `<!-- ROW_MINE: tech-board-discuss.messages.9363062 -->`

## 107.19 SCSI 文档与硬件需求

- 【Linux社区】列出 Adaptec/Qlogic 驱动文档与 SAS 卡、扩展器等硬件清单，请求规格与早期访问以支持开发 `<!-- ROW_MINE: tech-board-discuss.messages.9363063 -->`

## 107.20 unwind 符号 GPL 导出

- 【Linux社区】反驳 Rostedt：无人因友善或既有贡献而获免费通行，坚持不为 LTTng 放宽 EXPORT_SYMBOL_GPL 政策 `<!-- ROW_MINE: tech-board-discuss.messages.9363065 -->`
- 【Linux社区】回应 Greg：已尝试找 perf 方而无果，主张让 LTTng 访问 Mathieu 参与开发的函数，否则形同过河拆桥 `<!-- ROW_MINE: tech-board-discuss.messages.9363087 -->`

## 107.21 CodingStyle 包容性术语 v2

- 【Linux社区】提交 v2 补丁：删去单独背景文档，给出 master/slave 与 blacklist/whitelist 的推荐替换词并汇总签署 `<!-- ROW_MINE: tech-board-discuss.messages.9363066 -->`

## 107.22 2007 TAB 选举代表性质

- 【Linux社区】指出以反任人唯亲为名却将绝大多数社区排除在投票外的矛盾，质疑 TAB“社区直接声音”的定位 `<!-- ROW_MINE: tech-board-discuss.messages.9363068 -->`

## 107.23 CoC 委员会 2024 下半年报告 v2

- 【Linux社区】官方报告 v2：半年4起举报含邮件与私聊频道不当言行，处置均为教育辅导并持续监控 `<!-- ROW_MINE: tech-board-discuss.messages.9363071 -->`

## 107.24 TAB 参选声明格式

- 【Linux社区】以主席身份答复 Pavel：声明为自我介绍与参选动机的一至三短段，可参考历年声明汇总文档 `<!-- ROW_MINE: tech-board-discuss.messages.9363072 -->`

## 107.25 CoC 报告与拒补丁争议

- 【Linux社区】确认有人试图借 CoC 反制补丁被拒且非新现象，并说明半年4起举报尚不构成负担 `<!-- ROW_MINE: tech-board-discuss.messages.9363074 -->`

## 107.26 TAB 选举资格脚本

- 【Linux社区】追问投票资格与候选人提名资格是否用同一脚本判定，促成资格脚本随后公开 `<!-- ROW_MINE: tech-board-discuss.messages.9363075 -->`

## 107.27 2013 TAB 选举结果

- 【Linux社区】官方宣布爱丁堡 KS 选出的五年期名单：Greg KH、Gleixner、Corbet、Sarah Sharp、Matthew Garrett `<!-- ROW_MINE: tech-board-discuss.messages.9363076 -->`

## 107.28 TAB 自荐（Ricardo Neri）

- 【Linux社区】参选声明：主张社区多元包容，认为 Tested-by 等贡献被低估，当选后将致力于接纳新人 `<!-- ROW_MINE: tech-board-discuss.messages.9363078 -->`

## 107.29 2018 TAB 选举结果

- 【Linux社区】官方公布95张选票与前五名得票数（Mason 67、Abbott 62 等）及第六名票差，感谢参选者 `<!-- ROW_MINE: tech-board-discuss.messages.9363080 -->`

## 107.30 CoC 后续与 Linus 姿态

- 【Linux社区】将 Linus 立场类比为“等真实 bug 出现再修”的代码哲学：不接受理论推演式修改，自认不同意但愿试行 `<!-- ROW_MINE: tech-board-discuss.messages.9363081 -->`

## 107.31 TAB 2016 连任自荐

- 【Linux社区】完整连任声明：x86 与 tip 树维护近十年、gcc/llvm 社区联络人、创建 kernel.org 与本次选票系统 `<!-- ROW_MINE: tech-board-discuss.messages.9363082 -->`

## 107.32 2007 选举投票机制提案

- 【Linux社区】提议按合并入主线的 git commit 数分配票数，并可为 Acked-by 等标签配票以替代现场投票资格限制 `<!-- ROW_MINE: tech-board-discuss.messages.9363083 -->`

## 107.33 2009 TAB 选举与提名

- 【Linux社区】以主席身份发布选举时间地点、五名现任候选人名单与提名截止安排 `<!-- ROW_MINE: tech-board-discuss.messages.9363084 -->`

## 107.34 TAB 提名（Theodore Ts'o）

- 【Linux社区】参选声明：1991年起贡献、组织 KS 与参与 LPC 组织，强调面对面交流对社区健康与学界桥梁的价值 `<!-- ROW_MINE: tech-board-discuss.messages.9363085 -->`

## 107.35 TAB 提名（Kent Overstreet）

- 【Linux社区】参选声明：bcache/bcachefs 作者，主张培育更协作的开发文化并鼓励大型清理与核心数据结构重构 `<!-- ROW_MINE: tech-board-discuss.messages.9363086 -->`

## 107.36 CoC 更新过程说明

- 【Linux社区】说明 CoC 更新曾征询 git 统计前200贡献者并因此修改，提及 gab.ai 外部钓鱼干扰，称完全开放讨论非万灵药 `<!-- ROW_MINE: tech-board-discuss.messages.9363088 -->`

## 107.37 LLM 重写与许可证分叉

- 【Linux社区】论证以宽松许可证发布 LLM 重写内核也只是缺维护者的大分叉，许可证偏好难成决定因素，建议列为 TAB 议题 `<!-- ROW_MINE: tech-board-discuss.messages.9363090 -->`
