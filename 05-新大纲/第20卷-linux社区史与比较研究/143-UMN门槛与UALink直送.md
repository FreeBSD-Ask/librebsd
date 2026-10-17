# 143 【Linux社区】UMN门槛与UALink直送

> 来源：ksummit 独有 p9（50 封全读，2021-04 至 2026-07，tglx“业界特性优先与底层无人出资”根因论、Kees 防寒蝉效应提高门槛论、jgg UALink 独立子系统直送 Linus 主张、Kees“雕鱼”喻长会话 LLM 难声明与 show-your-work 惯例、Lawall AI 做“注释质量的 0-day”提案、Ted 四档析 LLM 硬件成本并提议 LKML 存档微调开源模型、HIGHMEM 退场 HIGHPTE 先删与 64 位模拟提案、hch 以 Debian BTS 为正例）
> 判定：48 CAND / 2 NV。主题分布：linux-next 隐藏提交 1、trivial 补丁接收政策（UMN） 2、linus-next 测试 2、2021 维护者峰会议题 1、文件系统维护（FUSE 方案） 1、Rust for Linux 1、kernel-doc Python 版本 1、trivial 补丁与 CC 过滤 1、设备直通（fwctl） 2、AI/LLM 在内核流程 3、bugzilla 退役与 LLM 分诊 1、UALink 驱动上游化 1、stable 邮件量 2、KTODO 与邮件引用 1、AI 辅助代码标注 1、文件系统维护困境 1、UMN 事件与内核开发根因 1、Rust 与设备生命周期管理 1、加速器用户空间要求 2、Rust 内核政策（V4L2 视角） 1、linux-next 与 0-day 之别 1、Sashiko AI 审阅 1、功能移除与 bcachefs 1、Link trailer 最佳实践 1、CONFIG_HIGHMEM 退场 1、Rust 编译器版本政策 1、工具生成内容指南 2、内核文档愿景 1、C aggregate passing（Rust） 2、Rust 与 devres 1、LLM 标签与新贡献者 1、bugzilla 退役 2、Bugzilla 分诊人力 1、Revocable 机制 1、设备直通 1、Bugzilla 与 Debian BTS 1、LLM 依赖与本地模型 1、kernel-doc 告警检查 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p9 的逐封提取（2021-04 至 2026-07，48 CAND / 2 NV），全 38 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 143.1 linux-next 隐藏提交

- 【Linux社区】提案：可信子维护者的树应进 linux-next；给出测量方法与 133 个提交的统计，列隐藏提交的四大害处及两类成因。 `<!-- ROW_MINE: ksummit.messages.1293 -->`

## 143.2 trivial 补丁接收政策（UMN）

- 【Linux社区】给出反例数据：commit 8e949363f017 引入 UAF，后由 31634bf5dcc4 修复；追问是否属“实验”补丁。 `<!-- ROW_MINE: ksummit.messages.1295 -->`
- 【Linux社区】同意提高审阅门槛而非一刀切禁止，防 UMN 事件对合法琐碎改进产生寒蝉效应。 `<!-- ROW_MINE: ksummit.messages.1327 -->`

## 143.3 linus-next 测试

- 【Linux社区】回忆 Linus 在 ARM 峰会要求把 -next 失败 CC 给他并自省未做到；论证 Linus 不知道问题就无法拒绝拉取。 `<!-- ROW_MINE: ksummit.messages.1297 -->`
- 【Linux社区】主张最有价值的检查点是合并窗口首个 PR，其后多为修复、-next 浸泡价值低。 `<!-- ROW_MINE: ksummit.messages.1307 -->`

## 143.4 2021 维护者峰会议题

- 【Linux社区】把加速器议题拆为“驱动树位置与维护归属”“新用户空间 API 接收条件”两题，属峰会议题组织记录。 `<!-- ROW_MINE: ksummit.messages.1298 -->`

## 143.5 文件系统维护（FUSE 方案）

- 【Linux社区】质疑 Kent 的“文件系统跑用户空间/FUSE”设想：引 xkcd 1200 讽攻击面扩大，追问迁出内核后维护是否会更好。 `<!-- ROW_MINE: ksummit.messages.1300 -->`

## 143.6 Rust for Linux

- 【Linux社区】回答 Geert：忽略 Option 的写法无法通过编译并附 godbolt 链接，佐证 Rust 编译期强制。 `<!-- ROW_MINE: ksummit.messages.1301 -->`

## 143.7 kernel-doc Python 版本

- 【Linux社区】反驳 Mauro 的自动换新版 Python 方案：等同覆盖用户配置的 PATH，若做也须显式开关。 `<!-- ROW_MINE: ksummit.messages.1302 -->`

## 143.8 trivial 补丁与 CC 过滤

- 【Linux社区】指出对过滤收件人的补丁视而不见会造成“没有反对”的假象。 `<!-- ROW_MINE: ksummit.messages.1309 -->`

## 143.9 设备直通（fwctl）

- 【Linux社区】反驳 Laurent：信任是双向的；大型子系统和复杂设备上维护者通晓全栈是一厢情愿。 `<!-- ROW_MINE: ksummit.messages.1316 -->`
- 【Linux社区】断言 netdev 无被忽略的技术审阅意见，分歧是哲学性的；主张维护者可以无视哲学异议。 `<!-- ROW_MINE: ksummit.messages.1415 -->`

## 143.10 AI/LLM 在内核流程

- 【Linux社区】与 Lorenzo 论战：LLM 细微错误人难察觉、统计推断无动力学基础；反指训练可改进，主张先索要 AI 置信度。 `<!-- ROW_MINE: ksummit.messages.1320 -->`
- 【Linux社区】建议用 AI 扫描难察觉的常见问题与润色非母语注释，做“注释质量的 0-day”。 `<!-- ROW_MINE: ksummit.messages.1396 -->`
- 【Linux社区】核心担忧生成与审阅的精力不对称；以带新人经验类比；信任 AI 帮自己调试代码甚于其写的代码。 `<!-- ROW_MINE: ksummit.messages.1410 -->`

## 143.11 bugzilla 退役与 LLM 分诊

- 【Linux社区】不愿让 LLM 生成补丁发给用户以免担责；报告量小成本可控；可先 grep “Call Trace” 筛出 oops 报告。 `<!-- ROW_MINE: ksummit.messages.1321 -->`

## 143.12 UALink 驱动上游化

- 【Linux社区】UALink 是带交换与寻址的多主机网络 fabric，近 RDMA 而非 DRM；应建独立子系统直送 Linus，并先有树内用户驱动。 `<!-- ROW_MINE: ksummit.messages.1322 -->`

## 143.13 stable 邮件量

- 【Linux社区】autosel 误选补丁必须有知悉渠道；同意显式打标且顺利应用的提交不必通知。 `<!-- ROW_MINE: ksummit.messages.1324 -->`
- 【Linux社区】同意把 X-Stable 头写进 stable 流程文档并承诺不随意变更；或干脆只发 stable-commits 列表供 lore 存档。 `<!-- ROW_MINE: ksummit.messages.1326 -->`

## 143.14 KTODO 与邮件引用

- 【Linux社区】过度裁剪引用与全文引用加文末 R-b 都妨碍讨论；区分删除无关内容与删除相关内容。 `<!-- ROW_MINE: ksummit.messages.1328 -->`

## 143.15 AI 辅助代码标注

- 【Linux社区】长会话 LLM 协作难以在提交信息声明（以“从浮木雕鱼”作喻）；主张推广与工具无关的“展示过程”惯例。 `<!-- ROW_MINE: ksummit.messages.1330 -->`

## 143.16 文件系统维护困境

- 【Linux社区】新 API 其实更易用，难在无人理解老实现；HFS 自 2011 无维护者；syzbot 自动骚扰加剧维护者倦怠。 `<!-- ROW_MINE: ksummit.messages.1331 -->`

## 143.17 UMN 事件与内核开发根因

- 【Linux社区】认同 UMN 未公开原始数据；根因是业界“特性优先”心态与底层基础无人出资，技术对策仅治标。 `<!-- ROW_MINE: ksummit.messages.1334 -->`

## 143.18 Rust 与设备生命周期管理

- 【Linux社区】提案在 C 中用简易精确 GC 或弱引用管理设备指针图，可借 sparse 辅助实现。 `<!-- ROW_MINE: ksummit.messages.1336 -->`

## 143.19 加速器用户空间要求

- 【Linux社区】主张进发行版软件包是质量门槛；指 HabanaLabs 曾绕过 netdev/RDMA 社区；反对任意设规阻止上游化。 `<!-- ROW_MINE: ksummit.messages.1337 -->`
- 【Linux社区】DRM/KMS 先交用户空间补丁并预核准架构的联锁模式可行；libcamera 正成相机事实标准；忧无标准栈的领域。 `<!-- ROW_MINE: ksummit.messages.1374 -->`

## 143.20 Rust 内核政策（V4L2 视角）

- 【Linux社区】Rust 特殊在规模；V4L2 需先重写对象生命周期才谈 bindings；倦怠成常态是心理健康问题；协助修基础可重建 C 与 Rust 阵营互信。 `<!-- ROW_MINE: ksummit.messages.1338 -->`

## 143.21 linux-next 与 0-day 之别

- 【Linux社区】linux-next 的独特价值是暴露跨分支干扰；自建 build/boot 测试；fixes 分支曾被 Linus 直接拉取。 `<!-- ROW_MINE: ksummit.messages.1347 -->`

## 143.22 Sashiko AI 审阅

- 【Linux社区】硬件不可预设恶意，DMA TOCTOU 质疑不成立；审阅提示词应按子系统定制（USB/virtio 为例），可提 PR 补 drivers.md。 `<!-- ROW_MINE: ksummit.messages.1349 -->`

## 143.23 功能移除与 bcachefs

- 【Linux社区】反驳 Mauro：“Kent 就是 bcachefs”，无团队可接手，接手者要面对 Kent、网络暴民与极复杂代码。 `<!-- ROW_MINE: ksummit.messages.1351 -->`

## 143.24 Link trailer 最佳实践

- 【Linux社区】v2 补丁：在 maintainer-tip.rst 写明 lore 与 patch.msgid.link 用法及方括号编号标注惯例。 `<!-- ROW_MINE: ksummit.messages.1353 -->`

## 143.25 CONFIG_HIGHMEM 退场

- 【Linux社区】同意先删 HIGHPTE；__GFP 位只剩 6 个；忧高内存回归难测，提议 64 位模拟 highmem 及 start/end access 式 API 改名。 `<!-- ROW_MINE: ksummit.messages.1355 -->`

## 143.26 Rust 编译器版本政策

- 【Linux社区】指出 Rust 与 C/gcc 侧稳定性标准严重不对称，“两个 Debian stable”太短，忧核心子系统用 Rust 实现。 `<!-- ROW_MINE: ksummit.messages.1356 -->`

## 143.27 工具生成内容指南

- 【Linux社区】给出 Reviewed-by，认可文档前提；提出改写两处表述并统一列表句点风格。 `<!-- ROW_MINE: ksummit.messages.1357 -->`
- 【Linux社区】说明其措辞强调补丁覆盖一切工具、不单独针对 LLM，正朝共识收敛。 `<!-- ROW_MINE: ksummit.messages.1383 -->`

## 143.28 内核文档愿景

- 【Linux社区】主张先立整体结构骨架、留空白小节，以引导补齐缺失文档。 `<!-- ROW_MINE: ksummit.messages.1359 -->`

## 143.29 C aggregate passing（Rust）

- 【Linux社区】纠正 RefinedRust 与 Miri 关系，引其仓库 README 自述复用 Miri 代码为证。 `<!-- ROW_MINE: ksummit.messages.1363 -->`
- 【Linux社区】Rust 只有极小的 soundness 修正；若内核受影响可预先修补并回移 stable；不用 stdlib 风险低。 `<!-- ROW_MINE: ksummit.messages.1387 -->`

## 143.30 Rust 与 devres

- 【Linux社区】提议把 devres 释放延迟到 module release，以修复中断处理程序悬空引用问题。 `<!-- ROW_MINE: ksummit.messages.1366 -->`

## 143.31 LLM 标签与新贡献者

- 【Linux社区】主张 Assisted-by 保留工具名供日后审计，建议 [PATCH AI] 或移剪刀线下；以正确性与测试论 LLM 新人；判断 AI 工具仍在流程外围。 `<!-- ROW_MINE: ksummit.messages.1367 -->`

## 143.32 bugzilla 退役

- 【Linux社区】提案把 decode_stacktrace.pl 与 get_maintainer.pl 串联，自动定位崩溃报告最合适的邮件列表并抄送。 `<!-- ROW_MINE: ksummit.messages.1372 -->`
- 【Linux社区】支持首页告知用户来错地方；建议内嵌 get_maintainer.pl 前端，粘路径即返回邮件地址。 `<!-- ROW_MINE: ksummit.messages.1376 -->`

## 143.33 Bugzilla 分诊人力

- 【Linux社区】自荐志愿做 bugzilla 报告分诊并与维护者 liaison，声明先表态非正式承诺。 `<!-- ROW_MINE: ksummit.messages.1375 -->`

## 143.34 Revocable 机制

- 【Linux社区】对照 GPIO 现有 RCU 置空方案，认为 revocable 的 SRCU 实现更优雅，GPIO 可轻易迁移。 `<!-- ROW_MINE: ksummit.messages.1379 -->`

## 143.35 设备直通

- 【Linux社区】libcamera 即开源框架且多厂商协作；区分直接寄存器访问与用户空间组 blob 参数两类设计，后者已有 ack 先例。 `<!-- ROW_MINE: ksummit.messages.1389 -->`

## 143.36 Bugzilla 与 Debian BTS

- 【Linux社区】以 Debian BTS 为正例：邮件接口利落、reportbug 自动收集信息、无需注册账号。 `<!-- ROW_MINE: ksummit.messages.1393 -->`

## 143.37 LLM 依赖与本地模型

- 【Linux社区】分四档梳理本地跑模型的硬件成本与带宽；量化损失精度；提议用 LKML 存档微调开源权重模型但受设备可得性限制。 `<!-- ROW_MINE: ksummit.messages.1398 -->`

## 143.38 kernel-doc 告警检查

- 【Linux社区】给出 :wall: 按标记设置、按子系统 CI 跑 -Wall、以及 dim 推送前检查等方案。 `<!-- ROW_MINE: ksummit.messages.1412 -->`
