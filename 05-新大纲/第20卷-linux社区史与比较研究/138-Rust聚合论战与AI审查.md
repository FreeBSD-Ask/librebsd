# 138 【Linux社区】Rust聚合论战与AI审查

> 来源：ksummit 独有 p2（50 封全读，2021-04 至 2026-07，C 聚合传递与 Linus unsafe 语义论战（stacked borrows 提案）、Rust PL061 try_writeb 开销分析与 git log 定位方法论、AI 审查议题提案（Sashiko 入 KernelCI/MCP 服务器/BPF CI）、generated-content.rst v3 多维护者 Reviewed-by、b4 dig 88% 成功率实测与 ATOM_MESSAGEID 补丁、sashiko 审查模型 opt-in 统计）
> 判定：46 CAND / 4 NV。主题分布：邮件删减礼仪 1、Rust 内核政策 2、驱动 probe 失败与注册 1、Rust for Linux 4、C 聚合传递（Rust 政策） 4、cdev/devm 生命周期 1、sashiko 审查模型 1、MAINTAINERS“THE REST”改投递 1、工具生成内容文档 v2 2、峰会 2021 规划 1、AI 与 LLM 在内核流程中的角色 1、b4 git notes 补丁 1、拒绝补丁透明度 1、Link trailer 替换 2、TAB 选举 CIVS 投票 1、维护者互助小组 1、AI 辅助补丁标注 2、文档 intersphinx 1、防止回归性 backport 1、内核文档构建 2、工具生成内容文档 v3 1、文件系统信任与维护 1、kallsyms 行号信息 1、静态分析 1、CONFIG_HIGHMEM 淘汰 1、加速器驱动用户态要求 1、next 中的隐藏提交 1、trivial 补丁接收政策 1、Link trailer 文档 1、头文件排序与 cleanup.h 1、嵌入式优雅关机议题 1、AI 代码审查（Sashiko） 1、AI 补丁审查工具 1、stable 分支提交标注 1、设备直通 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p2 的逐封提取（2021-04 至 2026-07，46 CAND / 4 NV），全 35 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 138.1 邮件删减礼仪

- 【Linux社区】指出过度引用致邮件被直接忽略、辩论中对方选择性删减不利引文的现象，属社区沟通规范论点。 `<!-- ROW_MINE: ksummit.messages.206 -->`

## 138.2 Rust 内核政策

- 【Linux社区】反驳“驱动开发者学 Rust 难”称其为短期问题，主张至少让 Rust 驱动易于支持。 `<!-- ROW_MINE: ksummit.messages.211 -->`
- 【Linux社区】明确原则：迫使人类写不直观代码是错解，应改进工具而非迁就工具的垃圾告警。 `<!-- ROW_MINE: ksummit.messages.279 -->`

## 138.3 驱动 probe 失败与注册

- 【Linux社区】分析 probe 失败后驱动仍注册成 defunct 的问题，提出接口驱动未绑定时注销的方案及异步 probe 限制。 `<!-- ROW_MINE: ksummit.messages.216 -->`

## 138.4 Rust for Linux

- 【Linux社区】讨论 Rc<T> 与内核多线程引用计数模型差异及 UB，追问 Rust Rc 饱和保护如何衔接内核实现。 `<!-- ROW_MINE: ksummit.messages.218 -->`
- 【Linux社区】逐条分析 Rust 版 PL061 驱动的 try_writeb 与 revocable 资源开销，提出 vet_offsetb 思路并批评“为展示方案而造问题”。 `<!-- ROW_MINE: ksummit.messages.250 -->`
- 【Linux社区】支持议题并提出以 git log 数据定位 Rust 最擅长问题的假设收集改写验证方法论，担忧实现语言碎片化。 `<!-- ROW_MINE: ksummit.messages.313 -->`
- 【Linux社区】解释弱引用升级失败语义与 Option<Ref<T>> 类型安全设计，类比锁的受控访问。 `<!-- ROW_MINE: ksummit.messages.351 -->`

## 138.5 C 聚合传递（Rust 政策）

- 【Linux社区】质疑对方 MIRI 实验结果的可复现性并要求提供输出证据，属对数据主张的直接反驳。 `<!-- ROW_MINE: ksummit.messages.223 -->`
- 【Linux社区】主张需更清晰的 ATOMIC_RELAXED 定义，并举 memset 后发布再 WRITE_ONCE 的隐患例。 `<!-- ROW_MINE: ksummit.messages.233 -->`
- 【Linux社区】深入比较 time crate 破坏与 C/C++兼容性案例，实测驳斥对方 C23 auto 示例并批评 Rust editions 的语义变更。 `<!-- ROW_MINE: ksummit.messages.267 -->`
- 【Linux社区】与 Linus 论战 unsafe 语义，主张 stacked/tree borrows 补上 C 缺失的指针派生别名模型。 `<!-- ROW_MINE: ksummit.messages.292 -->`

## 138.6 cdev/devm 生命周期

- 【Linux社区】系统提出 ures/uapires 命名空间、运行时检查器、cdev_disconnect 与 ures 分组等一揽子 uapi 资源设计想法。 `<!-- ROW_MINE: ksummit.messages.235 -->`

## 138.7 sashiko 审查模型

- 【Linux社区】讨论 AI 审查中硬件默认可信与按子系统 opt-in 的取舍，称已统计到三个 opt-out 并借帖征集意见。 `<!-- ROW_MINE: ksummit.messages.236 -->`

## 138.8 MAINTAINERS“THE REST”改投递

- 【Linux社区】提供自身不用固定 LKML 收件配置、靠 get_maintainer.pl 与 public-inbox/lei 读信的数据点。 `<!-- ROW_MINE: ksummit.messages.241 -->`

## 138.9 工具生成内容文档 v2

- 【Linux社区】审阅意见：删去“impressive”“undoubtedly improve productivity”等宣传性表述，要求事实性语气。 `<!-- ROW_MINE: ksummit.messages.248 -->`
- 【Linux社区】系统辨析 DCO 含义、维护者责任边界、SCO 先例与 AI 输出版权现状，主张善意接受与可追溯的 AI 标注。 `<!-- ROW_MINE: ksummit.messages.270 -->`

## 138.10 峰会 2021 规划

- 【Linux社区】建议提前指定研讨环节主持人，强调主持与发言不可兼得，属峰会组织建议。 `<!-- ROW_MINE: ksummit.messages.257 -->`

## 138.11 AI 与 LLM 在内核流程中的角色

- 【Linux社区】论证 LLM 细微错误源于统计推断的必然性并反驳 JBB，提议在峰会确定 AI 提交规则并警示媒体效应。 `<!-- ROW_MINE: ksummit.messages.260 -->`

## 138.12 b4 git notes 补丁

- 【Linux社区】提交 b4 补丁系列为 shazam 增加--add-link-note，用 git notes 记录提交与邮件关联且不污染上游历史。 `<!-- ROW_MINE: ksummit.messages.268 -->`

## 138.13 拒绝补丁透明度

- 【Linux社区】就 Baikal 补丁被拒提出议题：非技术原因拒绝时应给出详细理由以便社区协商共识。 `<!-- ROW_MINE: ksummit.messages.274 -->`

## 138.14 Link trailer 替换

- 【Linux社区】已向 git 提交 ATOM_MESSAGEID 格式补丁并给出 lore 链接，建议视结果未来切换以精简 trailer。 `<!-- ROW_MINE: ksummit.messages.278 -->`
- 【Linux社区】实测 b4 dig 在 100 个提交中约 88% 可解析，报告 stderr 调试输出与版本递增未上 list 等缺陷并附全量清单。 `<!-- ROW_MINE: ksummit.messages.291 -->`

## 138.15 TAB 选举 CIVS 投票

- 【Linux社区】流程记录：确认提名截止、投票开放，并跟进 CIVS 激活邮件重发问题。 `<!-- ROW_MINE: ksummit.messages.281 -->`

## 138.16 维护者互助小组

- 【Linux社区】澄清提案设计：不设邮件列表、公布志愿者名单、可附 IRC 联系方式。 `<!-- ROW_MINE: ksummit.messages.285 -->`

## 138.17 AI 辅助补丁标注

- 【Linux社区】认为议题超越 AI 本身属归因与 CoC 后果问题，建议另立通用归因文档与整体 AI 政策。 `<!-- ROW_MINE: ksummit.messages.288 -->`
- 【Linux社区】指出“仅用兼容许可训练”选项会带来保留版权声明等许可合规义务的连锁问题。 `<!-- ROW_MINE: ksummit.messages.334 -->`

## 138.18 文档 intersphinx

- 【Linux社区】提议将 objects.inv 清单文件预生成入库，类比 flex/bison 产物以免除双重构建。 `<!-- ROW_MINE: ksummit.messages.294 -->`

## 138.19 防止回归性 backport

- 【Linux社区】给出无 Fixes 和 cc stable 提交仍被 backport 的实例并追溯 Stable-dep 链至未打标提交，反驳 Greg 的解释。 `<!-- ROW_MINE: ksummit.messages.297 -->`

## 138.20 内核文档构建

- 【Linux社区】指出构建系统缺乏让子系统保持 W=1/kernel-doc 干净的支持，并以 drm Makefile 的 hack 为例。 `<!-- ROW_MINE: ksummit.messages.299 -->`
- 【Linux社区】给出 Sphinx 各版本性能数据，介绍 venv 安装法与 sphinx-build-wrapper 脚本方案。 `<!-- ROW_MINE: ksummit.messages.303 -->`

## 138.21 工具生成内容文档 v3

- 【Linux社区】TAB 协作的 generated-content.rst 第三版，纳入测试披露与措辞收敛等反馈并获多位维护者 Reviewed-by。 `<!-- ROW_MINE: ksummit.messages.300 -->`

## 138.22 文件系统信任与维护

- 【Linux社区】强烈反对未经同意做 AI 缺陷报告实验，斥 syzbot 为 rogue actor 并要求新实验机器人必须 opt-in。 `<!-- ROW_MINE: ksummit.messages.301 -->`

## 138.23 kallsyms 行号信息

- 【Linux社区】针对+44MiB 开销提出压缩存储、按需解压的缓解思路。 `<!-- ROW_MINE: ksummit.messages.310 -->`

## 138.24 静态分析

- 【Linux社区】说明 gcc-10+内联使 Wmaybe-uninitialized 近乎不可用，呼吁寻找替代的未初始化告警手段。 `<!-- ROW_MINE: ksummit.messages.314 -->`

## 138.25 CONFIG_HIGHMEM 淘汰

- 【Linux社区】要求拿出非标准 PAGE_OFFSET 配置下实际用户可见问题的证据，称缺实证难以推进淘汰进程。 `<!-- ROW_MINE: ksummit.messages.315 -->`

## 138.26 加速器驱动用户态要求

- 【Linux社区】提出判据：专有栈可复现而开放栈不能复现的问题，其修复不会进内核。 `<!-- ROW_MINE: ksummit.messages.319 -->`

## 138.27 next 中的隐藏提交

- 【Linux社区】反驳对树进-next 的顾虑，称其为标准做法且真正的风险是暴露潜在竞争等 bug 而非冲突。 `<!-- ROW_MINE: ksummit.messages.322 -->`

## 138.28 trivial 补丁接收政策

- 【Linux社区】提议修复必须有 Fixes:标签并解释 bug 来源以过滤垃圾修复，回应可被脚本刷标的质疑。 `<!-- ROW_MINE: ksummit.messages.330 -->`

## 138.29 Link trailer 文档

- 【Linux社区】澄清 b4.linkmask 默认值属 b4 项目配置而非全局默认，承诺文档定稿后修改全局默认。 `<!-- ROW_MINE: ksummit.messages.331 -->`

## 138.30 头文件排序与 cleanup.h

- 【Linux社区】解释#include 排序规则源于减少补丁上下文合并冲突，patch 与 quilt 不忽略 include 行差异。 `<!-- ROW_MINE: ksummit.messages.342 -->`

## 138.31 嵌入式优雅关机议题

- 【Linux社区】提交峰会演讲摘要，倡导将优先级化关机保护机制上游化以应对掉电损坏嵌入式存储。 `<!-- ROW_MINE: ksummit.messages.343 -->`

## 138.32 AI 代码审查（Sashiko）

- 【Linux社区】提出将 Sashiko 问题发布到 KernelCI 问题库并介绍新 MCP 服务器，邀 Roman 合作。 `<!-- ROW_MINE: ksummit.messages.345 -->`

## 138.33 AI 补丁审查工具

- 【Linux社区】提出峰会议题：以 AI 审查降低维护者负载，展示 BPF CI 接入、prompts 仓库与 semcode 索引工具及 token 对比数据。 `<!-- ROW_MINE: ksummit.messages.350 -->`

## 138.34 stable 分支提交标注

- 【Linux社区】提议仅回移标 Stable 的提交、bot 提醒只发给未正确 Cc stable 的维护者，主张奖善罚恶。 `<!-- ROW_MINE: ksummit.messages.352 -->`

## 138.35 设备直通

- 【Linux社区】回应 Ricardo：厂商应被邀请而非放任、明确规则属商业决策，并警惕 niche 用例坐大。 `<!-- ROW_MINE: ksummit.messages.353 -->`
