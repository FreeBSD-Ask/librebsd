# 138. Rust 聚合传递论战、AI 审查与 generated-content v3（ks p2）（ks p2）

> 来源：ksummit 独有 p2（50 封全读，2021-04 至 2026-07，C 聚合传递与 Linus unsafe 语义论战（stacked borrows 提案）、Rust PL061 try_writeb 开销分析与 git log 定位方法论、AI 审查议题提案（Sashiko 入 KernelCI/MCP 服务器/BPF CI）、generated-content.rst v3 多维护者 Reviewed-by、b4 dig 88% 成功率实测与 ATOM_MESSAGEID 补丁、sashiko 审查模型 opt-in 统计）
> 判定：46 CAND / 4 NV。主题分布：邮件删减礼仪 1、Rust内核政策 2、驱动probe失败与注册 1、Rust for Linux 4、C聚合传递（Rust政策） 4、cdev/devm生命周期 1、sashiko审查模型 1、MAINTAINERS“THE REST”改投递 1、工具生成内容文档v2 2、峰会2021规划 1、AI与LLM在内核流程中的角色 1、b4 git notes补丁 1、拒绝补丁透明度 1、Link trailer替换 2、TAB选举CIVS投票 1、维护者互助小组 1、AI辅助补丁标注 2、文档intersphinx 1、防止回归性backport 1、内核文档构建 2、工具生成内容文档v3 1、文件系统信任与维护 1、kallsyms行号信息 1、静态分析 1、CONFIG_HIGHMEM淘汰 1、加速器驱动用户态要求 1、next中的隐藏提交 1、trivial补丁接收政策 1、Link trailer文档 1、头文件排序与cleanup.h 1、嵌入式优雅关机议题 1、AI代码审查（Sashiko） 1、AI补丁审查工具 1、stable分支提交标注 1、设备直通 1。

## 138.1 邮件删减礼仪

- 【Linux社区】指出过度引用致邮件被直接忽略、辩论中对方选择性删减不利引文的现象，属社区沟通规范论点。 `<!-- ROW_MINE: ksummit.messages.206 -->`

## 138.2 Rust内核政策

- 【Linux社区】反驳“驱动开发者学Rust难”称其为短期问题，主张至少让Rust驱动易于支持。 `<!-- ROW_MINE: ksummit.messages.211 -->`
- 【Linux社区】明确原则：迫使人类写不直观代码是错解，应改进工具而非迁就工具的垃圾告警。 `<!-- ROW_MINE: ksummit.messages.279 -->`

## 138.3 驱动probe失败与注册

- 【Linux社区】分析probe失败后驱动仍注册成defunct的问题，提出接口驱动未绑定时注销的方案及异步probe限制。 `<!-- ROW_MINE: ksummit.messages.216 -->`

## 138.4 Rust for Linux

- 【Linux社区】讨论Rc<T>与内核多线程引用计数模型差异及UB，追问Rust Rc饱和保护如何衔接内核实现。 `<!-- ROW_MINE: ksummit.messages.218 -->`
- 【Linux社区】逐条分析Rust版PL061驱动的try_writeb与revocable资源开销，提出vet_offsetb思路并批评“为展示方案而造问题”。 `<!-- ROW_MINE: ksummit.messages.250 -->`
- 【Linux社区】支持议题并提出以git log数据定位Rust最擅长问题的假设收集改写验证方法论，担忧实现语言碎片化。 `<!-- ROW_MINE: ksummit.messages.313 -->`
- 【Linux社区】解释弱引用升级失败语义与Option<Ref<T>>类型安全设计，类比锁的受控访问。 `<!-- ROW_MINE: ksummit.messages.351 -->`

## 138.5 C聚合传递（Rust政策）

- 【Linux社区】质疑对方MIRI实验结果的可复现性并要求提供输出证据，属对数据主张的直接反驳。 `<!-- ROW_MINE: ksummit.messages.223 -->`
- 【Linux社区】主张需更清晰的ATOMIC_RELAXED定义，并举memset后发布再WRITE_ONCE的隐患例。 `<!-- ROW_MINE: ksummit.messages.233 -->`
- 【Linux社区】深入比较time crate破坏与C/C++兼容性案例，实测驳斥对方C23 auto示例并批评Rust editions的语义变更。 `<!-- ROW_MINE: ksummit.messages.267 -->`
- 【Linux社区】与Linus论战unsafe语义，主张stacked/tree borrows补上C缺失的指针派生别名模型。 `<!-- ROW_MINE: ksummit.messages.292 -->`

## 138.6 cdev/devm生命周期

- 【Linux社区】系统提出ures/uapires命名空间、运行时检查器、cdev_disconnect与ures分组等一揽子uapi资源设计想法。 `<!-- ROW_MINE: ksummit.messages.235 -->`

## 138.7 sashiko审查模型

- 【Linux社区】讨论AI审查中硬件默认可信与按子系统opt-in的取舍，称已统计到三个opt-out并借帖征集意见。 `<!-- ROW_MINE: ksummit.messages.236 -->`

## 138.8 MAINTAINERS“THE REST”改投递

- 【Linux社区】提供自身不用固定LKML收件配置、靠get_maintainer.pl与public-inbox/lei读信的数据点。 `<!-- ROW_MINE: ksummit.messages.241 -->`

## 138.9 工具生成内容文档v2

- 【Linux社区】审阅意见：删去“impressive”“undoubtedly improve productivity”等宣传性表述，要求事实性语气。 `<!-- ROW_MINE: ksummit.messages.248 -->`
- 【Linux社区】系统辨析DCO含义、维护者责任边界、SCO先例与AI输出版权现状，主张善意接受与可追溯的AI标注。 `<!-- ROW_MINE: ksummit.messages.270 -->`

## 138.10 峰会2021规划

- 【Linux社区】建议提前指定研讨环节主持人，强调主持与发言不可兼得，属峰会组织建议。 `<!-- ROW_MINE: ksummit.messages.257 -->`

## 138.11 AI与LLM在内核流程中的角色

- 【Linux社区】论证LLM细微错误源于统计推断的必然性并反驳JBB，提议在峰会确定AI提交规则并警示媒体效应。 `<!-- ROW_MINE: ksummit.messages.260 -->`

## 138.12 b4 git notes补丁

- 【Linux社区】提交b4补丁系列为shazam增加--add-link-note，用git notes记录提交与邮件关联且不污染上游历史。 `<!-- ROW_MINE: ksummit.messages.268 -->`

## 138.13 拒绝补丁透明度

- 【Linux社区】就Baikal补丁被拒提出议题：非技术原因拒绝时应给出详细理由以便社区协商共识。 `<!-- ROW_MINE: ksummit.messages.274 -->`

## 138.14 Link trailer替换

- 【Linux社区】已向git提交ATOM_MESSAGEID格式补丁并给出lore链接，建议视结果未来切换以精简trailer。 `<!-- ROW_MINE: ksummit.messages.278 -->`
- 【Linux社区】实测b4 dig在100个提交中约88%可解析，报告stderr调试输出与版本递增未上list等缺陷并附全量清单。 `<!-- ROW_MINE: ksummit.messages.291 -->`

## 138.15 TAB选举CIVS投票

- 【Linux社区】流程记录：确认提名截止、投票开放，并跟进CIVS激活邮件重发问题。 `<!-- ROW_MINE: ksummit.messages.281 -->`

## 138.16 维护者互助小组

- 【Linux社区】澄清提案设计：不设邮件列表、公布志愿者名单、可附IRC联系方式。 `<!-- ROW_MINE: ksummit.messages.285 -->`

## 138.17 AI辅助补丁标注

- 【Linux社区】认为议题超越AI本身属归因与CoC后果问题，建议另立通用归因文档与整体AI政策。 `<!-- ROW_MINE: ksummit.messages.288 -->`
- 【Linux社区】指出“仅用兼容许可训练”选项会带来保留版权声明等许可合规义务的连锁问题。 `<!-- ROW_MINE: ksummit.messages.334 -->`

## 138.18 文档intersphinx

- 【Linux社区】提议将objects.inv清单文件预生成入库，类比flex/bison产物以免除双重构建。 `<!-- ROW_MINE: ksummit.messages.294 -->`

## 138.19 防止回归性backport

- 【Linux社区】给出无Fixes和cc stable提交仍被backport的实例并追溯Stable-dep链至未打标提交，反驳Greg的解释。 `<!-- ROW_MINE: ksummit.messages.297 -->`

## 138.20 内核文档构建

- 【Linux社区】指出构建系统缺乏让子系统保持W=1/kernel-doc干净的支持，并以drm Makefile的hack为例。 `<!-- ROW_MINE: ksummit.messages.299 -->`
- 【Linux社区】给出Sphinx各版本性能数据，介绍venv安装法与sphinx-build-wrapper脚本方案。 `<!-- ROW_MINE: ksummit.messages.303 -->`

## 138.21 工具生成内容文档v3

- 【Linux社区】TAB协作的generated-content.rst第三版，纳入测试披露与措辞收敛等反馈并获多位维护者Reviewed-by。 `<!-- ROW_MINE: ksummit.messages.300 -->`

## 138.22 文件系统信任与维护

- 【Linux社区】强烈反对未经同意做AI缺陷报告实验，斥syzbot为rogue actor并要求新实验机器人必须opt-in。 `<!-- ROW_MINE: ksummit.messages.301 -->`

## 138.23 kallsyms行号信息

- 【Linux社区】针对+44MiB开销提出压缩存储、按需解压的缓解思路。 `<!-- ROW_MINE: ksummit.messages.310 -->`

## 138.24 静态分析

- 【Linux社区】说明gcc-10+内联使Wmaybe-uninitialized近乎不可用，呼吁寻找替代的未初始化告警手段。 `<!-- ROW_MINE: ksummit.messages.314 -->`

## 138.25 CONFIG_HIGHMEM淘汰

- 【Linux社区】要求拿出非标准PAGE_OFFSET配置下实际用户可见问题的证据，称缺实证难以推进淘汰进程。 `<!-- ROW_MINE: ksummit.messages.315 -->`

## 138.26 加速器驱动用户态要求

- 【Linux社区】提出判据：专有栈可复现而开放栈不能复现的问题，其修复不会进内核。 `<!-- ROW_MINE: ksummit.messages.319 -->`

## 138.27 next中的隐藏提交

- 【Linux社区】反驳对树进-next的顾虑，称其为标准做法且真正的风险是暴露潜在竞争等bug而非冲突。 `<!-- ROW_MINE: ksummit.messages.322 -->`

## 138.28 trivial补丁接收政策

- 【Linux社区】提议修复必须有Fixes:标签并解释bug来源以过滤垃圾修复，回应可被脚本刷标的质疑。 `<!-- ROW_MINE: ksummit.messages.330 -->`

## 138.29 Link trailer文档

- 【Linux社区】澄清b4.linkmask默认值属b4项目配置而非全局默认，承诺文档定稿后修改全局默认。 `<!-- ROW_MINE: ksummit.messages.331 -->`

## 138.30 头文件排序与cleanup.h

- 【Linux社区】解释#include排序规则源于减少补丁上下文合并冲突，patch与quilt不忽略include行差异。 `<!-- ROW_MINE: ksummit.messages.342 -->`

## 138.31 嵌入式优雅关机议题

- 【Linux社区】提交峰会演讲摘要，倡导将优先级化关机保护机制上游化以应对掉电损坏嵌入式存储。 `<!-- ROW_MINE: ksummit.messages.343 -->`

## 138.32 AI代码审查（Sashiko）

- 【Linux社区】提出将Sashiko问题发布到KernelCI问题库并介绍新MCP服务器，邀Roman合作。 `<!-- ROW_MINE: ksummit.messages.345 -->`

## 138.33 AI补丁审查工具

- 【Linux社区】提出峰会议题：以AI审查降低维护者负载，展示BPF CI接入、prompts仓库与semcode索引工具及token对比数据。 `<!-- ROW_MINE: ksummit.messages.350 -->`

## 138.34 stable分支提交标注

- 【Linux社区】提议仅回移标Stable的提交、bot提醒只发给未正确Cc stable的维护者，主张奖善罚恶。 `<!-- ROW_MINE: ksummit.messages.352 -->`

## 138.35 设备直通

- 【Linux社区】回应Ricardo：厂商应被邀请而非放任、明确规则属商业决策，并警惕niche用例坐大。 `<!-- ROW_MINE: ksummit.messages.353 -->`
