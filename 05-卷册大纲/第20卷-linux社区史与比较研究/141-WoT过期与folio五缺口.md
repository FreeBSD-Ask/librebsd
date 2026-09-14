# 141 【Linux社区】WoT过期与folio五缺口

> 来源：ksummit 独有 p4（50 封全读，2021-04 至 2026-07，sq cert lint 637 证书 SHA-1 数据论证密钥过期、folio 流程五大缺口剖析与 DAX 类比、Bug-fix-from: 激励标签提案、DRM panel 即 bridge 与 eBPF quirk 用户空间化、Rust 与 Wedson 资源撤销之辩、wifi 子系统因 Sphinx 同名 bug 改名决策、Linux 过大不敢冒险之问）
> 判定：47 CAND / 3 NV。主题分布：stable 回退回归防范 2、MAINTAINERS 条目校验 1、CONFIG_HIGHMEM 淘汰 1、C 聚合传参（Rust 政策） 2、文件系统维护信任之争 1、内核文档 2、Link 尾注与 Message-ID 1、Rust 内核政策 1、Web of Trust 与密钥有效期 1、稳定分支提交打标 1、维护者倦怠与审查机器人 1、邮件引用修剪与 KTODO 1、Link 尾注文档补丁 1、工具生成内容准则 1、维护者倦怠与 CI 1、DRM panel API 现代化 1、C 聚合传参 1、设备直通议题组织 1、eBPF 用户态边界 1、trivial 补丁接收政策 2、sashiko 审查模型 1、维护者倦怠与激励 1、替换 Link 尾注 1、硬件使能的期望管理 1、MAINTAINERS 校验 1、Folios 议题与流程 2、维护者导师制 1、trivial 补丁政策 2、加速器驱动的用户态要求 1、项目连续性文档 1、MAINTAINERS THE REST 改抄送 1、字符串助手迁移 1、Rust for Linux 2、bugzilla 退役与崩溃日志工具 1、AI 审查的位置 1、未订阅列表的回信方法 1、Rust for Linux 与 irqchip 1、Bugzilla 改进与回归追踪 1、cdev/devm 陷阱 1、项目过大与过度恐惧 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p4 的逐封提取（2021-04 至 2026-07，47 CAND / 3 NV），全 40 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 141.1 stable 回退回归防范

- 【Linux社区】认同“能提前告知回归就告知”，并逐一回应推迟回传、紧急标记、按 Fixes: 延迟回传三方案的可行性。 `<!-- ROW_MINE: ksummit.messages.491 -->`
- 【Linux社区】稳定团队称已有机制识别补丁是否属于系列，但实践中多数系列内部并无相互依赖。 `<!-- ROW_MINE: ksummit.messages.516 -->`

## 141.2 MAINTAINERS 条目校验

- 【Linux社区】主张按 git 历史抄送基本总是错的，并提出把 Makefile 集成进 Kconfig 的语法设想。 `<!-- ROW_MINE: ksummit.messages.494 -->`

## 141.3 CONFIG_HIGHMEM 淘汰

- 【Linux社区】提议移除仅 ARM 部分系统使用的 kmap_high_get()，并问 HASHED_PAGE_VIRTUAL 能否一并去掉。 `<!-- ROW_MINE: ksummit.messages.497 -->`

## 141.4 C 聚合传参（Rust 政策）

- 【Linux社区】用 i386/ARM/x86_64/aarch64 汇编对比说明双字段结构体返回的 ABI 差异，补充 -freg-struct-return 线索。 `<!-- ROW_MINE: ksummit.messages.498 -->`
- 【Linux社区】从语言设计层面批评 Rust：读并发全局标志竟需 unsafe，若编译器重 materialize 读操作则语言糟糕。 `<!-- ROW_MINE: ksummit.messages.530 -->`

## 141.5 文件系统维护信任之争

- 【Linux社区】反驳 James Bottomley 的和稀泥，坚持 Linus 的嘲讽不可接受、维护者须以更高标准示范，属治理立场。 `<!-- ROW_MINE: ksummit.messages.500 -->`

## 141.6 内核文档

- 【Linux社区】讨论 kernel-doc 移植 Python 的复杂度，提出在源码 DOC: 标记内列符号清单以便内核文档自校验。 `<!-- ROW_MINE: ksummit.messages.501 -->`
- 【Linux社区】报告因 Sphinx C domain 同名符号的长期 bug，wifi 子系统已放弃等待而直接改名符号。 `<!-- ROW_MINE: ksummit.messages.525 -->`

## 141.7 Link 尾注与 Message-ID

- 【Linux社区】说明自己的 sed 脚本因大小写失配而漏替换，建议 Paolo 的 applypatch-msg 钩子改大小写不敏感匹配。 `<!-- ROW_MINE: ksummit.messages.502 -->`

## 141.8 Rust 内核政策

- 【Linux社区】反驳 hch 的“不诚实”指控，重申 2022 峰会灵活性立场，承认证言样本有偏差并区分企业支持与企业施压。 `<!-- ROW_MINE: ksummit.messages.503 -->`

## 141.9 Web of Trust 与密钥有效期

- 【Linux社区】反驳 Linus 和 James Bottomley，主张密钥应设过期时间，并给出 sq cert lint 检查 637 份证书中 SHA-1 问题的数据。 `<!-- ROW_MINE: ksummit.messages.507 -->`

## 141.10 稳定分支提交打标

- 【Linux社区】阐明 Fixes 标签与 stable 回传完全无关、静态警告清理不宜加 Fixes，讨论修复与新功能的模糊边界。 `<!-- ROW_MINE: ksummit.messages.511 -->`

## 141.11 维护者倦怠与审查机器人

- 【Linux社区】反驳机器人不省力的说法并引 Greg 的 patch_bot 为例，认可把常见硬伤归为“一票否决项”分组处理。 `<!-- ROW_MINE: ksummit.messages.518 -->`

## 141.12 邮件引用修剪与 KTODO

- 【Linux社区】提议只标记极端修剪案例而不过分苛刻，并建议把评审标签放在提交说明之后以便读者不必再往下翻。 `<!-- ROW_MINE: ksummit.messages.523 -->`

## 141.13 Link 尾注文档补丁

- 【Linux社区】指出 b4.linkmask 默认指向 msgid.link 而非补丁所述的 patch.msgid.link，建议更新 b4 默认值。 `<!-- ROW_MINE: ksummit.messages.528 -->`

## 141.14 工具生成内容准则

- 【Linux社区】批评 v5 文档“必须能辩护一切”的表述像威胁，给出强调自查、透明测试与分批报 bug 的替代表述。 `<!-- ROW_MINE: ksummit.messages.529 -->`

## 141.15 维护者倦怠与 CI

- 【Linux社区】支持自动测试与 CI，但警告要求全部测试通过后人工才看一眼会严重挫伤贡献者积极性。 `<!-- ROW_MINE: ksummit.messages.531 -->`

## 141.16 DRM panel API 现代化

- 【Linux社区】主张承认 drm_bridge 已不只是 bridge、让面板直接变 bridge，并类比 HID-BPF 提出用 eBPF 把面板 quirk 移到用户空间。 `<!-- ROW_MINE: ksummit.messages.532 -->`

## 141.17 C 聚合传参

- 【Linux社区】指出 -freg-struct-return 须封装成每函数可用的 __attribute__ 才不会破坏既有 ABI。 `<!-- ROW_MINE: ksummit.messages.533 -->`

## 141.18 设备直通议题组织

- 【Linux社区】说明坚持上 Maintainer Summit 的动机是跨子系统 NAK 的溯源与导航，LPC 场次可另行安排。 `<!-- ROW_MINE: ksummit.messages.540 -->`

## 141.19 eBPF 用户态边界

- 【Linux社区】用 tracepoints 曾被用户态工具硬依赖而破坏的历史论证 eBPF 同理，与每位维护者相关。 `<!-- ROW_MINE: ksummit.messages.541 -->`

## 141.20 trivial 补丁接收政策

- 【Linux社区】建议组建感兴趣者小组分担 trivial 树审阅，并指出攒批合并会让补丁失去时效。 `<!-- ROW_MINE: ksummit.messages.545 -->`
- 【Linux社区】介绍 trivial 树攒批发送现状，并分析“trivial 等于不紧急”假设的隐患与实际运作尚可的原因。 `<!-- ROW_MINE: ksummit.messages.560 -->`

## 141.21 sashiko 审查模型

- 【Linux社区】反对默认信任硬件/固件：实际难以区分 bug 与恶意，举 media 驱动数组越界与除零检查经验主张按处 opt-in。 `<!-- ROW_MINE: ksummit.messages.546 -->`

## 141.22 维护者倦怠与激励

- 【Linux社区】提议增设 Bug-fix-from: 标签记录审查中发现 bug 的人，借标签体系的游戏化激励良好行为。 `<!-- ROW_MINE: ksummit.messages.547 -->`

## 141.23 替换 Link 尾注

- 【Linux社区】重申反对 Message-ID 尾注：唯一可信论据是一键体验，其余论据信息量不如 b4 dig。 `<!-- ROW_MINE: ksummit.messages.549 -->`

## 141.24 硬件使能的期望管理

- 【Linux社区】正式峰会议题提案：硅片复杂度攀升、Linux 首发系统角色下贡献者夹在项目管理与维护者怀疑之间，列三个讨论问题。 `<!-- ROW_MINE: ksummit.messages.564 -->`

## 141.25 MAINTAINERS 校验

- 【Linux社区】建议调高 --git-min-signatures、默认关闭 gitfallback，并追问 lei 在 Debian stable 的打包障碍。 `<!-- ROW_MINE: ksummit.messages.565 -->`

## 141.26 Folios 议题与流程

- 【Linux社区】剖析 folio 流程五大缺口（问题共识、ack 归属、剩余工作、分步计划、测试分工），建议用两页共享文档固定下来。 `<!-- ROW_MINE: ksummit.messages.566 -->`
- 【Linux社区】反驳“正收敛”说：只是大家疲惫，补丁自合并窗口开启未变，类比 DAX 花多年才收敛。 `<!-- ROW_MINE: ksummit.messages.617 -->`

## 141.27 维护者导师制

- 【Linux社区】支持非正式导师制：现有维护者每两周约一小时离带新，指出时区是主要挑战。 `<!-- ROW_MINE: ksummit.messages.568 -->`

## 141.28 trivial 补丁政策

- 【Linux社区】回应 Al Viro 的 60 补丁系列假设：相关就该全抄送，无关则拆成多个系列。 `<!-- ROW_MINE: ksummit.messages.569 -->`
- 【Linux社区】解释 MFD 场景：多个子系统驱动只因封装在一起而并立，彼此并无实质关联。 `<!-- ROW_MINE: ksummit.messages.604 -->`

## 141.29 加速器驱动的用户态要求

- 【Linux社区】主张负责的内核维护须了解生态走向、没把握就说 No，并批评厂商借发行版上游化后另起用户态项目求控制权。 `<!-- ROW_MINE: ksummit.messages.572 -->`

## 141.30 项目连续性文档

- 【Linux社区】澄清该文档定位是“为未来制定计划的计划”，不可能也不必穷举所有坏场景。 `<!-- ROW_MINE: ksummit.messages.574 -->`

## 141.31 MAINTAINERS THE REST 改抄送

- 【Linux社区】赞同改案并给出条件：只要能抄送某邮件列表存档讨论、Link: 标记照常工作即可。 `<!-- ROW_MINE: ksummit.messages.576 -->`

## 141.32 字符串助手迁移

- 【Linux社区】反对 strncpy 改 strscpy：认为提升有限、helper 缺文档，此场景 snprintf 更合适。 `<!-- ROW_MINE: ksummit.messages.588 -->`

## 141.33 Rust for Linux

- 【Linux社区】与 Wedson 辩论 remove 路径的资源撤销 versus 阻塞调用模型，主张改进子系统与驱动间 API 才能整类消除问题。 `<!-- ROW_MINE: ksummit.messages.589 -->`
- 【Linux社区】回应 Leon 的重构与测试矩阵担忧：Rust 是整段替换而非树内第二内核，承认双语言重构成本属实。 `<!-- ROW_MINE: ksummit.messages.594 -->`

## 141.34 bugzilla 退役与崩溃日志工具

- 【Linux社区】介绍 kbooboo 工具与静态托管需求，同意数据生成交给 kernelci，前端放在易被报告者发现之处。 `<!-- ROW_MINE: ksummit.messages.590 -->`

## 141.35 AI 审查的位置

- 【Linux社区】担心按子系统定制 Sashiko 提示词会让回复冗长，建议改用维护者档案文档承载子系统特定规则。 `<!-- ROW_MINE: ksummit.messages.602 -->`

## 141.36 未订阅列表的回信方法

- 【Linux社区】回答 Tim Bird：可用 lore 页面的 reply 链接，或下载 mbox 导入本地文件夹后回复。 `<!-- ROW_MINE: ksummit.messages.606 -->`

## 141.37 Rust for Linux 与 irqchip

- 【Linux社区】解答 PL061 wake 计数与 irqdomain 映射竞争问题：irqchip 无状态无同步靠实践约定，直言该框架缺维护者。 `<!-- ROW_MINE: ksummit.messages.608 -->`

## 141.38 Bugzilla 改进与回归追踪

- 【Linux社区】介绍 regzbot 借 Link: 标签串联报告与补丁实现追踪，反驳“邮件无法跟踪状态”的论断。 `<!-- ROW_MINE: ksummit.messages.614 -->`

## 141.39 cdev/devm 陷阱

- 【Linux社区】举 v4l2 device_register 失败路径与 media controller 注册为例，说明 kobj release 错误清理难做对且部分无解。 `<!-- ROW_MINE: ksummit.messages.621 -->`

## 141.40 项目过大与过度恐惧

- 【Linux社区】回应 James Bottomley：追问是否 Linux 过大致不敢冒险，提出拆分子项目并配最低限度稳定 API 的设想。 `<!-- ROW_MINE: ksummit.messages.622 -->`
