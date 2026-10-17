# 147 【Linux社区】richACL重审与UALink上架

> 来源：ksummit 独有 p11（50 封全读，2021-04 至 2026-08，RichACL 重审提案（AI 存储场景 POSIX ACL 不敷使用/百万装机）、UALink drivers/ualink 独立子系统经 DRM 流转决策、两周回归修复时限“最坏主意”之驳、SoftISP 量化验收标准与校准文件≈固件 blob、DT 绑定即 ABI 过渡路径原则、b4 tip 启发式 commitish→lore 已实现、lock-free 算法反驳“总有锁”）
> 判定：45 CAND / 5 NV。主题分布：AI工具生成内容文档争论 1、新开发者洪水与stable回迁 1、bugzilla默认订阅争论 1、Rust内核策略UBSan争论 1、本地LLM评审Sashiko实测 1、richACL与AI相册共享场景 1、内核malloc提案反驳 1、linus-next树运作机制 1、AI辅助代码标注争论 1、THE REST收件列表讨论 1、维护者峰会存废争论 1、Rust聚合体传参与aliasing 1、richACL议题征集 1、AI辅助补丁标注与SOB链 1、UALink驱动上架决策 1、回归修复时限提案反驳 1、API废弃执行机制 1、崩溃回溯价值争论 1、补丁自动测试反馈机制 1、linus-next与next路线之争 1、trivial补丁受理政策 1、LLM补丁洪流归因之争 1、Link trailer替换提案 1、bugzilla与邮件报告流程 1、内核文档构建噪音治理 1、维护者支持小组讨论 1、b4 dig实现进展 1、Rust GPIO包装层布局 1、栈回溯源码行号与调试符号 1、bugzilla triage自荐 1、安全embargo披露机制 1、C聚合体与无锁代码 1、文件系统维护与虚拟硬件 1、工具生成内容文档v5评审 1、特性纳入与驱逐程序 1、工具生成内容文档背书 1、设备直通开放性争议 1、dt-bindings独立仓库动议 1、per-cgroup swap控制路由 1、工具生成内容文档v3质疑 1、工具生成内容文档措辞 1、UnsafeCell与C指针语义 1、DT绑定ABI变更原则 1、静态分析注解探讨 1、内核文档质量与CI 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p11 的逐封提取（2021-04 至 2026-08，45 CAND / 5 NV），全 45 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 147.1 AI工具生成内容文档争论

- 【Linux社区】主张LLM不改变问题只改变数量级；建议文档明示维护者可径直拒绝疑似slop并已提交增量diff。 `<!-- ROW_MINE: ksummit.messages.1556 -->`

## 147.2 新开发者洪水与stable回迁

- 【Linux社区】建议以邮件头中stable版本前缀识别例外补丁；指出跨树应用检查受依赖与linux-next冲突制约。 `<!-- ROW_MINE: ksummit.messages.1558 -->`

## 147.3 bugzilla默认订阅争论

- 【Linux社区】全文反驳“把近半年开发者默认订阅进bugzilla邮件”方案：未经同意只会被过滤进垃圾箱。 `<!-- ROW_MINE: ksummit.messages.1564 -->`

## 147.4 Rust内核策略UBSan争论

- 【Linux社区】反驳UBSan用于产线：Clang sanitizer不应在生产环境启用并附oss-security先例链接。 `<!-- ROW_MINE: ksummit.messages.1565 -->`

## 147.5 本地LLM评审Sashiko实测

- 【Linux社区】报告经PR用Ollama本地量化模型跑Sashiko评审，并提及tiwai等小模型评审agent实测结论。 `<!-- ROW_MINE: ksummit.messages.1566 -->`

## 147.6 richACL与AI相册共享场景

- 【Linux社区】就AI照片共享用例追问权限模型并提出中间目录方案；建议议题归Tech Topic而非维护者峰会。 `<!-- ROW_MINE: ksummit.messages.1569 -->`

## 147.7 内核malloc提案反驳

- 【Linux社区】反驳Wilcox的例证：zlib本就由调用方传入分配函数，无需malloc式接口。 `<!-- ROW_MINE: ksummit.messages.1571 -->`

## 147.8 linus-next树运作机制

- 【Linux社区】说明PR被NACK即revert合并、lei自动化约八成、冲突处理与CI结果监控的分工设想。 `<!-- ROW_MINE: ksummit.messages.1573 -->`

## 147.9 AI辅助代码标注争论

- 【Linux社区】反驳“Hello World”类比：AI输出可含罕见受版权文本，平均值论据在法律层面不成立。 `<!-- ROW_MINE: ksummit.messages.1575 -->`

## 147.10 THE REST收件列表讨论

- 【Linux社区】提议对无列表抄送补丁设reply-to指向lkml便于讨论可见；半玩笑提出LLM摘要服务设想。 `<!-- ROW_MINE: ksummit.messages.1577 -->`

## 147.11 维护者峰会存废争论

- 【Linux社区】反驳另设常年维护者列表的提议：workflows@列表本就为此目的存在。 `<!-- ROW_MINE: ksummit.messages.1583 -->`

## 147.12 Rust聚合体传参与aliasing

- 【Linux社区】解释restrict/noalias下常量折叠成立的原因；Rust借用检查器禁止双重可变借用及soundness设计难点。 `<!-- ROW_MINE: ksummit.messages.1591 -->`

## 147.13 richACL议题征集

- 【Linux社区】提案重审RichACL：AI存储场景POSIX ACL不敷使用，用户态规则方案扩展性与性能差，宣称超百万装机。 `<!-- ROW_MINE: ksummit.messages.1599 -->`

## 147.14 AI辅助补丁标注与SOB链

- 【Linux社区】引现有文档指出“须回应评审”却未要求回应有意义；建议把SOB链反映真实路径的说明推广到全内核。 `<!-- ROW_MINE: ksummit.messages.1610 -->`

## 147.15 UALink驱动上架决策

- 【Linux社区】决策记录：从第一天起建drivers/ualink迷你子系统、经DRM树流转、后续讨论抄送dri-devel。 `<!-- ROW_MINE: ksummit.messages.1612 -->`

## 147.16 回归修复时限提案反驳

- 【Linux社区】强烈抨击两周内mainline修复的目标：对志愿者施压将致流失、拒加入或因怕罚而停滞。 `<!-- ROW_MINE: ksummit.messages.1616 -->`

## 147.17 API废弃执行机制

- 【Linux社区】认为LKP/build警告长期有效；提出以sparse属性标记废弃API并对存量用户抑制警告。 `<!-- ROW_MINE: ksummit.messages.1621 -->`

## 147.18 崩溃回溯价值争论

- 【Linux社区】反驳“无回溯好过错误回溯”：栈上代码地址清单即可推断调用序列，最好附栈hexdump。 `<!-- ROW_MINE: ksummit.messages.1625 -->`

## 147.19 补丁自动测试反馈机制

- 【Linux社区】介绍BPF patchwork Checks实践：起VM跑selftests，让评审者投稿前即可见测试反馈。 `<!-- ROW_MINE: ksummit.messages.1627 -->`

## 147.20 linus-next与next路线之争

- 【Linux社区】表态支持改进linux-next而非再造next类树；说明自己PR先入next三至七天以消除冲突。 `<!-- ROW_MINE: ksummit.messages.1630 -->`

## 147.21 trivial补丁受理政策

- 【Linux社区】反对独立whitespace/风格补丁：损害git log -p与blame追溯代码演化能力，随bug系列则可。 `<!-- ROW_MINE: ksummit.messages.1633 -->`

## 147.22 LLM补丁洪流归因之争

- 【Linux社区】指出Sasha立场矛盾：既称无AI依赖之虞又称AI可催化维护者工具化改进。 `<!-- ROW_MINE: ksummit.messages.1643 -->`

## 147.23 Link trailer替换提案

- 【Linux社区】提议Konstantin跑bot对Linus推送做b4 dig建commit到邮件公开映射，兼审计无讨论来源的提交。 `<!-- ROW_MINE: ksummit.messages.1648 -->`

## 147.24 bugzilla与邮件报告流程

- 【Linux社区】辨析邮件协议与客户端职责并援引OEM邮件驱动集成测试先例；断言根因是维护者时间瓶颈。 `<!-- ROW_MINE: ksummit.messages.1649 -->`

## 147.25 内核文档构建噪音治理

- 【Linux社区】已修复几乎全部可修警告；分析usb_string重名警告根因是Sphinx单一符号命名空间且补丁未合并。 `<!-- ROW_MINE: ksummit.messages.1650 -->`

## 147.26 维护者支持小组讨论

- 【Linux社区】倡议低成本收集冲突谈判等资源并列出书单；主张社区规模已大到应引入专业心理帮助。 `<!-- ROW_MINE: ksummit.messages.1651 -->`

## 147.27 b4 dig实现进展

- 【Linux社区】澄清Konstantin已在b4 tip实现commitish到lore链接查找，当前用启发式栈而非AI。 `<!-- ROW_MINE: ksummit.messages.1656 -->`

## 147.28 Rust GPIO包装层布局

- 【Linux社区】以stable回迁难度论证包装文件应从第一天放正确路径且永不移动，避免cherry-pick失效。 `<!-- ROW_MINE: ksummit.messages.1657 -->`

## 147.29 栈回溯源码行号与调试符号

- 【Linux社区】质疑LLM取符号的必要性；盘点Debian/Fedora/Arch等debuginfo缺口，建议推动发行版改进。 `<!-- ROW_MINE: ksummit.messages.1659 -->`

## 147.30 bugzilla triage自荐

- 【Linux社区】表态愿承担bug triage工作，并认为Bugzilla应被更合工作流的系统取代。 `<!-- ROW_MINE: ksummit.messages.1662 -->`

## 147.31 安全embargo披露机制

- 【Linux社区】质疑闭列表法律风险论据；探讨仅发修复提交清单是否算预公告及linux-distros的供应链定位。 `<!-- ROW_MINE: ksummit.messages.1664 -->`

## 147.32 C聚合体与无锁代码

- 【Linux社区】反驳“总有锁保护”前提：大量简单无锁算法存在，锁不应成为普遍假设。 `<!-- ROW_MINE: ksummit.messages.1678 -->`

## 147.33 文件系统维护与虚拟硬件

- 【Linux社区】引QEMU弃用文档纠正James Bottomley：仅i440fx-1.4至1.7弃用，pc别名（8.x）未弃用。 `<!-- ROW_MINE: ksummit.messages.1679 -->`

## 147.34 工具生成内容文档v5评审

- 【Linux社区】流程记录：对TAB的generated-content.rst v5给出Reviewed-by，含维护者可拒slop段落落地。 `<!-- ROW_MINE: ksummit.messages.1682 -->`

## 147.35 特性纳入与驱逐程序

- 【Linux社区】区分特性流程/开发者除名/导师制三问题；详列社区现行ad hoc排斥机制并主张35年仅一例应慎立新规。 `<!-- ROW_MINE: ksummit.messages.1686 -->`

## 147.36 工具生成内容文档背书

- 【Linux社区】支持Carpenter观点并阐述信任资本论：提出“能实质评审同复杂度贡献再期待社区认真对待”规则。 `<!-- ROW_MINE: ksummit.messages.1695 -->`

## 147.37 设备直通开放性争议

- 【Linux社区】提出以SoftISP为参照的可量化开放性验收标准；主张校准文件等同固件blob且当前缺乏谈判筹码。 `<!-- ROW_MINE: ksummit.messages.1697 -->`

## 147.38 dt-bindings独立仓库动议

- 【Linux社区】反对DT绑定移出内核：内核硬件覆盖最广且专家在此；指出现有devicetree-rebasing仓库并指引DT BoF。 `<!-- ROW_MINE: ksummit.messages.1699 -->`

## 147.39 per-cgroup swap控制路由

- 【Linux社区】决策记录：不属维护者峰会，应投Plumbers MM或LSFMM，并当场补抄送linux-mm。 `<!-- ROW_MINE: ksummit.messages.1700 -->`

## 147.40 工具生成内容文档v3质疑

- 【Linux社区】要求定义“slop”的判定边界；指出与howto.rst既有要求重复并追问文档面向媒体的目的。 `<!-- ROW_MINE: ksummit.messages.1705 -->`

## 147.41 工具生成内容文档措辞

- 【Linux社区】反对使用“slop”一词：对部分维护者含义不明只能靠猜，主张表达明确化。 `<!-- ROW_MINE: ksummit.messages.1709 -->`

## 147.42 UnsafeCell与C指针语义

- 【Linux社区】以MIRI实测辨析&UnsafeCell<T>与C T*别名差异，明确raw pointer与引用的UB边界。 `<!-- ROW_MINE: ksummit.messages.1712 -->`

## 147.43 DT绑定ABI变更原则

- 【Linux社区】论证DT绑定即ABI：任何破坏性变更都须为既有使用者规划无断档过渡路径。 `<!-- ROW_MINE: ksummit.messages.1714 -->`

## 147.44 静态分析注解探讨

- 【Linux社区】阐明optional getter返回NULL表示特性被禁用的语义、错误指针误用模式与上报建议。 `<!-- ROW_MINE: ksummit.messages.1719 -->`

## 147.45 内核文档质量与CI

- 【Linux社区】提议按kernel-doc标记设-Wall参数或经CI落实，回应drm Makefile局部hack的经验。 `<!-- ROW_MINE: ksummit.messages.1736 -->`
