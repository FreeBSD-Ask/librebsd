# 194. 安全披露生态阐述、git-bug 五点安全剖析与 Rust 上游化困境（ks p58）

> 来源：ksummit 独有 p58（50 封全读，2024-07 至 2025-02：Greg KH 系统阐述安全披露生态稳定树修复 99% 已知漏洞谷歌两年数据 Android 为最大用户与 LF 不能托管闭门 distros 列表的法律政府风险及 CRA 立法压力；Ted Tso 对 git-bug 架构五点安全剖析含拉取绕过反垃圾与 Jia Tan 式供应链类比系 kernel.org 弃 Bugzilla 转向关键文献；Lyude Paul 长篇当事人叙述 Rust 上游化困境说服成本维护者倦怠语气常态化与 Asahi Rust 代码几乎零 bug；kallsyms 栈回溯行号 RFC 实测 459 万条目 +44MiB 与 vmlinux +8.3%；Rust 内核争议四封、设备直通争议三封）
> 判定：43 CAND / 7 NV。主题分布：Rust策略编译器告警 2、设备直通争议 2、维护者支持小组 1、V4L2与DRM之争 2、安全披露机制 2、stable回溯机制 1、trivial补丁政策 2、文档构建性能 1、AI生成内容指南 1、git-bug缺陷追踪 2、Rust内核争议 4、回归处理流程 1、混合会议主持 1、文档工具链 1、Folios议题归属 1、PGP信任与密钥 2、AI代码标注政策 2、GitLab工作流 1、内核文档议题 3、linux-next构建 1、Rust别名模型 2、栈回溯行号 1、补丁收件人筛选 1、CoC执行争议 1、HIGHMEM淘汰 1、UALink驱动归属 1、Bugzilla通知争议 1、用户态开源要求 1、峰会代表性 1。

## 194.1 Rust策略编译器告警

- 【Linux社区】Carpenter 谈 Smatch 在宏内静默告警、过滤惯用溢出以消假阳性，称“文化争论而非技术问题”，举 DPMCP_MIN_VER_MINOR 与 set_iter_tags 例。 `<!-- ROW_MINE: ksummit.messages.9007 -->`
- 【Linux社区】Carpenter 澄清：Sparse 忽略 pragma；amdgpu 实因 #pragma pack() 致 1KB 静态断言失败而中断 Sparse 检查。 `<!-- ROW_MINE: ksummit.messages.9067 -->`

## 194.2 设备直通争议

- 【Linux社区】fwctl 僵局讨论：Gunthorpe 称三年会议已形成多维护者共识，Williams 引 MGLRU 在 LSF/MM 2022 面对面破冰先例，Bottomley 提供 Plumbers BoF 场地。 `<!-- ROW_MINE: ksummit.messages.9008 -->`
- 【Linux社区】Bottomley 称 DPDK 是“蜜罐”，项目替换内核功能后需重写全套而烂尾；Gunthorpe 称大量互联网流量与 ORAN 已规模化依赖 DPDK。 `<!-- ROW_MINE: ksummit.messages.9028 -->`

## 194.3 维护者支持小组

- 【Linux社区】Brown 赞同 Rostedt 的“维护者支持小组”预防性提议，强调提交者也会受挫且更易一走了之，机制须同样覆盖提交者。 `<!-- ROW_MINE: ksummit.messages.9011 -->`

## 194.4 V4L2与DRM之争

- 【Linux社区】Pinchart 主张 V4L2 与 DRM 规则应相近：命令缓冲可传但须充分文档或开源实现；称 IPU3 文档不足是未执行规则的教训。 `<!-- ROW_MINE: ksummit.messages.9040 -->`
- 【Linux社区】Pinchart 要求举出使用命令缓冲的 ISP 实例以推进讨论；引 V4L2 有状态解码接口证明通用低层接口路线可行。 `<!-- ROW_MINE: ksummit.messages.9104 -->`

## 194.5 安全披露机制

- 【Linux社区】Greg KH 反对闭门预公告列表：稳定树修复 99% 已知安全问题（谷歌两年数据）、Android 为最大用户、硬件 embargo 各方皆怨、CRA 立法施压。 `<!-- ROW_MINE: ksummit.messages.9045 -->`
- 【Linux社区】Greg KH 谈 embargo 代码测试：Intel 内部 0day 结果未随补丁披露、需私密测试实例防泄露、建议由硬件厂商提供、改文档措辞需律师同意。 `<!-- ROW_MINE: ksummit.messages.9173 -->`

## 194.6 stable回溯机制

- 【Linux社区】Greg KH 解释无 Fixes/cc:stable 提交被回溯系因 “Stable-dep-of” 标签，并指该 SCSI strlcpy 转换回溯疑似引入 bug。 `<!-- ROW_MINE: ksummit.messages.9050 -->`

## 194.7 trivial补丁政策

- 【Linux社区】Al Viro 质疑全面禁收 trivial 补丁提案：若维护者已核实“显然的修复”真实且正确，该政策下应如何处置？ `<!-- ROW_MINE: ksummit.messages.9054 -->`
- 【Linux社区】Sudip 建议设独立 trivial 树、配专门审阅者在 GregKH 指导下运作；引 Mauro 称明尼苏达发往媒体子系统的补丁多可合入。 `<!-- ROW_MINE: ksummit.messages.9069 -->`

## 194.8 文档构建性能

- 【Linux社区】实测 make htmldocs：Brown -j56 需 26 分 14 秒，Dunlap -j8 笔记本 6 分 05 秒，量化文档构建过慢问题。 `<!-- ROW_MINE: ksummit.messages.9065 -->`

## 194.9 AI生成内容指南

- 【Linux社区】Bottomley 反对在 AI 内容指南使用 “slop” 一词，主张历时稳定的通用表述，举 rawdog、chad 等年度词渐失语义为例。 `<!-- ROW_MINE: ksummit.messages.9066 -->`

## 194.10 git-bug缺陷追踪

- 【Linux社区】Ted Tso 剖析 git-bug 架构安全疑虑：git pull 绕过反垃圾、桥接与数据格式攻击面、类比 Jia Tan 式供应链攻击，称极为不安。 `<!-- ROW_MINE: ksummit.messages.9072 -->`
- 【Linux社区】Konstantin 详述规划：按子系统建 git-bug 仓库、bugs.kernel.org 重定向器统一寻址、上报经前端预分析、讨论留 lore、同步可选。 `<!-- ROW_MINE: ksummit.messages.9145 -->`

## 194.11 Rust内核争议

- 【Linux社区】Lyude Paul 详述 Rust 上游困境：说服维护者耗散精力、倦怠语气被常态化、Asahi 的 Rust 代码几乎零 bug，呼吁给 Rust 证明机会。 `<!-- ROW_MINE: ksummit.messages.9080 -->`
- 【Linux社区】Bart Van Assche 持保留立场：C 比 Rust 易学，“过路式”驱动开发者未必具备学习 Rust 的技能。 `<!-- ROW_MINE: ksummit.messages.9084 -->`
- 【Linux社区】Feng 与 Contreras 争论“驱动皆可写成 Rust”：Feng 以黑天鹅谬误质疑全部驱动可用 Rust 的假设，Feng 要求对方澄清逻辑。 `<!-- ROW_MINE: ksummit.messages.9125 -->`
- 【Linux社区】Leon 明言立场：不知 Rust 能解决哪些 C 难解的真实内核问题，故不认同“Rust 收益大于成本”论。 `<!-- ROW_MINE: ksummit.messages.9172 -->`

## 194.12 回归处理流程

- 【Linux社区】Rostedt 认为若 Leemhuis 有硬数据证明工作流致回归，议题应升格维护者峰会，并鼓励以数据推动流程改变。 `<!-- ROW_MINE: ksummit.messages.9090 -->`

## 194.13 混合会议主持

- 【Linux社区】Tarreau 介绍 IETF 混合会议经验：jabber scribe 转达聊天提问、虚拟排队、现场排队用麦，兼顾本地与远程平衡。 `<!-- ROW_MINE: ksummit.messages.9093 -->`

## 194.14 文档工具链

- 【Linux社区】Ojeda 澄清 2022 年现状：Documentation/rust 已用 ReST，rustdoc 仅输出 HTML，并表达对 Markdown 支持的期待。 `<!-- ROW_MINE: ksummit.messages.9094 -->`

## 194.15 Folios议题归属

- 【Linux社区】Bottomley 称 folio 属技术议题不宜维护者峰会，LSF/MM 停办后提议以 Plumbers BBB 基础设施办 MM 聚会。 `<!-- ROW_MINE: ksummit.messages.9095 -->`

## 194.16 PGP信任与密钥

- 【Linux社区】Bottomley 驳短有效期主张：内核密钥主要用于标签签名、分发机制已足；称 GnuPG trustdb 可独立操作，指 Sequoia 说法为宣传。 `<!-- ROW_MINE: ksummit.messages.9096 -->`
- 【Linux社区】Uwe 力主设 PGP 有效期：引 Gentoo GLEP 63、Sequoia 默认 3 年、letsencrypt 将限 45 天，称安全是移动目标，应改进 keyring 维护。 `<!-- ROW_MINE: ksummit.messages.9122 -->`

## 194.17 AI代码标注政策

- 【Linux社区】Kosina 主张须能知悉补丁出自 AI 以便知情决策或直接拒收：AI 代码背后可能无人理解其逻辑可供人讨论。 `<!-- ROW_MINE: ksummit.messages.9101 -->`
- 【Linux社区】McKenney 称 SoB 对 AI 产出的规则尚未明确，需与混沌中的法律诉讼进程对齐，现阶段指望 AI 输出安全是愚蠢的。 `<!-- ROW_MINE: ksummit.messages.9115 -->`

## 194.18 GitLab工作流

- 【Linux社区】Zickus 详解红帽 RHEL 内核 GitLab 流程：评审数据结构化、经 API 聚合补丁讨论、审批与 CI 状态，可抽象移植到其他传输机制。 `<!-- ROW_MINE: ksummit.messages.9103 -->`

## 194.19 内核文档议题

- 【Linux社区】Corbet 反对 sphinx-pre-install 自动寻替代解释器：脚本应按预期行为运行；指 RHEL8 建文档者极少且 Leap 15 将被取代。 `<!-- ROW_MINE: ksummit.messages.9109 -->`
- 【Linux社区】Corbet 提交 2025 峰会文档议题：过去一年文档构建基础设施大量改进，回顾近况并讨论未来两三年文档演进方向。 `<!-- ROW_MINE: ksummit.messages.9151 -->`
- 【Linux社区】Nikula 主张 Sphinx 构建重质不重量：先清零 kernel-doc 与 rst 告警（i915/xe 已有本地检查、扩展至 drm 失败），不宜全量收录。 `<!-- ROW_MINE: ksummit.messages.9171 -->`

## 194.20 linux-next构建

- 【Linux社区】Brown 谈 linux-next 实践：bisect 沿线性历史定位引入分支、ccache 因 KernelCI 平庸体验被 Stephen 关闭、按序抽样构建以控时长。 `<!-- ROW_MINE: ksummit.messages.9113 -->`

## 194.21 Rust别名模型

- 【Linux社区】hpa 强调标准化进程价值在于写出含边角情形的正式契约；引 Alice 观点：Rust 别名模型担忧被夸大，可只留在确定合法子集内。 `<!-- ROW_MINE: ksummit.messages.9118 -->`
- 【Linux社区】Ralf Jung 说明 Miri 默认按 Stacked Borrows 检查（比 Tree Borrows 更严）、playground 不支持自定义旗标，盼 Miri 进入 Compiler Explorer。 `<!-- ROW_MINE: ksummit.messages.9157 -->`

## 194.22 栈回溯行号

- 【Linux社区】kallsyms 行号表实测：459 万条目、.rodata 增约 44MiB（vmlinux +8.3%）；Figa 建议移入可加载模块，崩溃后自动加载二次报告。 `<!-- ROW_MINE: ksummit.messages.9120 -->`

## 194.23 补丁收件人筛选

- 【Linux社区】Leon 指资深开发者也犯的恶习：精心筛选 TO/CC 致补丁脱离上下文、反馈割裂成“孤岛”无法对照，附 rdma 系列实例链接。 `<!-- ROW_MINE: ksummit.messages.9139 -->`

## 194.24 CoC执行争议

- 【Linux社区】Shuah 披露 CoC 多数报告系对社区运作的误解、幕后化解；就 Linus buffer cache 言论被 Chinner 指违 CoC 一案表态，认为有 CoC 更好。 `<!-- ROW_MINE: ksummit.messages.9149 -->`

## 194.25 HIGHMEM淘汰

- 【Linux社区】Arnd 考证 ARMv5 highmem 仅剩 OpenBlocks A7（内存须受限）等少数机器：Debian armel 已出末版、mv78xx0 平台可整体移除。 `<!-- ROW_MINE: ksummit.messages.9159 -->`

## 194.26 UALink驱动归属

- 【Linux社区】Greg KH 反对以 staging 引入 UALink：迁出 staging 成本高于树外先清理再合入，同意首日即用 drivers/accel/ual 建子系统。 `<!-- ROW_MINE: ksummit.messages.9160 -->`

## 194.27 Bugzilla通知争议

- 【Linux社区】Artem 坚持按 git 提交自动订阅、一键 opt-out 即可；Greg KH 驳称强加订阅必招反感，开发者无义务分诊 bug。 `<!-- ROW_MINE: ksummit.messages.9161 -->`

## 194.28 用户态开源要求

- 【Linux社区】tglx 主张接口门槛是文档须足以实现开源用户态，而非当下是否已存在；已存在也不保证功能完备。 `<!-- ROW_MINE: ksummit.messages.9163 -->`

## 194.29 峰会代表性

- 【Linux社区】Howlett 批评维护者峰会核心圈固化，提议专题临时席位与代表制；追问 MM 即将更换首席维护者时程序委员会如何考虑其影响。 `<!-- ROW_MINE: ksummit.messages.9174 -->`
