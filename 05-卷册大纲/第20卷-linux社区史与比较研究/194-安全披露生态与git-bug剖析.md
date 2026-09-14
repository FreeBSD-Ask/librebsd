# 194 【Linux社区】安全披露生态与git-bug剖析

> 来源：ksummit 独有 p58（50 封全读，2024-07 至 2025-02：Greg KH 系统阐述安全披露生态稳定树修复 99% 已知漏洞谷歌两年数据 Android 为最大用户与 LF 不能托管闭门 distros 列表的法律政府风险及 CRA 立法压力；Ted Tso 对 git-bug 架构五点安全剖析含拉取绕过反垃圾与 Jia Tan 式供应链类比系 kernel.org 弃 Bugzilla 转向关键文献；Lyude Paul 长篇当事人叙述 Rust 上游化困境说服成本维护者倦怠语气常态化与 Asahi Rust 代码几乎零 bug；kallsyms 栈回溯行号 RFC 实测 459 万条目 +44MiB 与 vmlinux +8.3%；Rust 内核争议四封、设备直通争议三封）
> 判定：43 CAND / 7 NV。主题分布：Rust策略编译器告警 2、设备直通争议 2、维护者支持小组 1、V4L2与DRM之争 2、安全披露机制 2、stable回溯机制 1、trivial补丁政策 2、文档构建性能 1、AI生成内容指南 1、git-bug缺陷追踪 2、Rust内核争议 4、回归处理流程 1、混合会议主持 1、文档工具链 1、Folios议题归属 1、PGP信任与密钥 2、AI代码标注政策 2、GitLab工作流 1、内核文档议题 3、linux-next构建 1、Rust别名模型 2、栈回溯行号 1、补丁收件人筛选 1、CoC执行争议 1、HIGHMEM淘汰 1、UALink驱动归属 1、Bugzilla通知争议 1、用户态开源要求 1、峰会代表性 1。

## 194.1 Rust策略编译器告警

- **要点**：Carpenter 谈 Smatch 在宏内静默告警、过滤惯用溢出以消假阳性，称“文化争论而非技术问题”，举 DPMCP_MIN_VER_MINOR 与 set_iter_tags 例。Carpenter 澄清：Sparse 忽略 pragma；amdgpu 实因 #pragma pack() 致 1KB 静态断言失败而中断 Sparse 检查。
- **史料**：`ksummit.messages.9007`（Dan Carpenter，2025-02-22）、`ksummit.messages.9067`（Dan Carpenter，2025-02-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9007 -->` `<!-- ROW_MINE: ksummit.messages.9067 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Smatch 在宏内静默告警、过滤惯用溢出等具体实现为分析单位）；经验优先（总纲第 9 条——经验优先：以 DPMCP_MIN_VER_MINOR 与 set_iter_tags 两个可查实例为判据）
- **辨析**：两条均系 Dan Carpenter 的说明；“文化争论而非技术问题”为其对争论性质的判断；#pragma pack() 致静态断言失败为可复现的编译事实。
- **文献**：DSLXC-11052、DSLXC-11062（`ksummit.messages.9007`、`ksummit.messages.9067`，2025-02-22、2025-02-24），全文见 `raw_source.raw_json`

## 194.2 设备直通争议

- **要点**：fwctl 僵局讨论：Gunthorpe 称三年会议已形成多维护者共识，Williams 引 MGLRU 在 LSF/MM 2022 面对面破冰先例，Bottomley 提供 Plumbers BoF 场地。Bottomley 称 DPDK 是“蜜罐”，项目替换内核功能后需重写全套而烂尾；Gunthorpe 称大量互联网流量与 ORAN 已规模化依赖 DPDK。
- **史料**：`ksummit.messages.9008`（James Bottomley，2024-08-07）、`ksummit.messages.9028`（James Bottomley，2024-07-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9008 -->` `<!-- ROW_MINE: ksummit.messages.9028 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：fwctl 多维护者共识与面对面破冰先例并置；“蜜罐”说与 DPDK 规模化依赖的实况并置）；动手者叙事（总纲第 10 条——动手者创造历史：以 Plumbers BoF 场地这一具体机制为分析单位）
- **辨析**：“三年会议已形成多维护者共识”与“大量互联网流量与 ORAN 已规模化依赖 DPDK”分属两方，本页未见裁决；MGLRU 先例为类比论证。
- **文献**：DSLXC-11053、DSLXC-11055（`ksummit.messages.9008`、`ksummit.messages.9028`，2024-08-07、2024-07-11），全文见 `raw_source.raw_json`

## 194.3 维护者支持小组

- **要点**：Brown 赞同 Rostedt 的“维护者支持小组”预防性提议，强调提交者也会受挫且更易一走了之，机制须同样覆盖提交者。
- **史料**：`ksummit.messages.9011`（Mark Brown，2023-09-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9011 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：维护者与提交者同受挫折，机制须同样覆盖）；经验优先（总纲第 9 条——经验优先：以“提交者也会受挫且更易一走了之”这一经验观察为判据）
- **辨析**：本块系 Mark Brown 对 Rostedt 提议的附议与扩充；“更易一走了之”为当事人判断，非统计结论。
- **文献**：DSLXC-11054（`ksummit.messages.9011`，2023-09-20），全文见 `raw_source.raw_json`

## 194.4 V4L2与DRM之争

- **要点**：Pinchart 主张 V4L2 与 DRM 规则应相近：命令缓冲可传但须充分文档或开源实现；称 IPU3 文档不足是未执行规则的教训。Pinchart 要求举出使用命令缓冲的 ISP 实例以推进讨论；引 V4L2 有状态解码接口证明通用低层接口路线可行。
- **史料**：`ksummit.messages.9040`（Laurent Pinchart，2024-07-25）、`ksummit.messages.9104`（Laurent Pinchart，2024-08-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9040 -->` `<!-- ROW_MINE: ksummit.messages.9104 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以命令缓冲的文档或开源实现要求这一可操作规则为分析单位）；经验优先（总纲第 9 条——经验优先：以“IPU3 文档不足是未执行规则的教训”这一实际案例为判据）
- **辨析**：两条均系 Laurent Pinchart 的主张与举证；其“要求举出使用命令缓冲的 ISP 实例”为对话推进手段，本页未见对方实例回应。
- **文献**：DSLXC-11056、DSLXC-11074（`ksummit.messages.9040`、`ksummit.messages.9104`，2024-07-25、2024-08-13），全文见 `raw_source.raw_json`

## 194.5 安全披露机制

- **要点**：Greg KH 反对闭门预公告列表：稳定树修复 99% 已知安全问题（谷歌两年数据）、Android 为最大用户、硬件 embargo 各方皆怨、CRA 立法施压。Greg KH 谈 embargo 代码测试：Intel 内部 0day 结果未随补丁披露、需私密测试实例防泄露、建议由硬件厂商提供、改文档措辞需律师同意。
- **史料**：`ksummit.messages.9045`（Greg KH，2023-08-15）、`ksummit.messages.9173`（Greg KH，2023-08-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9045 -->` `<!-- ROW_MINE: ksummit.messages.9173 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“稳定树修复 99% 已知安全问题（谷歌两年数据）”这一量化判断为判据）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：CRA 立法施压与硬件 embargo 的各方抱怨被还原为合规与商业利益格局）
- **辨析**：两条均系 Greg KH 的一手阐述；“99%”与“谷歌两年数据”为当事人引用的统计，落书须标明来源；“改文档措辞需律师同意”表明法律审阅介入文档修订。
- **文献**：DSLXC-11057、DSLXC-11093（`ksummit.messages.9045`、`ksummit.messages.9173`，2023-08-15、2023-08-15），全文见 `raw_source.raw_json`

## 194.6 stable回溯机制

- **要点**：Greg KH 解释无 Fixes/cc:stable 提交被回溯系因 “Stable-dep-of” 标签，并指该 SCSI strlcpy 转换回溯疑似引入 bug。
- **史料**：`ksummit.messages.9050`（Greg KH，2024-06-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9050 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Stable-dep-of 标签这一具体机制为分析单位）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：SCSI strlcpy 转换回溯疑似引入 bug）
- **辨析**：本块系 Greg KH 的机制解释；“疑似引入 bug”为当事人措辞，落书不得写成已定因果。
- **文献**：DSLXC-11058（`ksummit.messages.9050`，2024-06-13），全文见 `raw_source.raw_json`

## 194.7 trivial补丁政策

- **要点**：Al Viro 质疑全面禁收 trivial 补丁提案：若维护者已核实“显然的修复”真实且正确，该政策下应如何处置？Sudip 建议设独立 trivial 树、配专门审阅者在 GregKH 指导下运作；引 Mauro 称明尼苏达发往媒体子系统的补丁多可合入。
- **史料**：`ksummit.messages.9054`（Al Viro，2021-04-21）、`ksummit.messages.9069`（Sudip Mukherjee，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9054 -->` `<!-- ROW_MINE: ksummit.messages.9069 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：全面禁收 trivial 补丁的提案与“显然的修复”应如何处置的反问并置）；动手者叙事（总纲第 10 条——动手者创造历史：以独立 trivial 树与专门审阅者这一具体组织方案为分析单位）
- **辨析**：Al Viro 的反问为对政策完备性的诘问；Sudip 引 Mauro 之语属转述，其“配专门审阅者在 GregKH 指导下运作”为提案。
- **文献**：DSLXC-11059、DSLXC-11063（`ksummit.messages.9054`、`ksummit.messages.9069`，2021-04-21、2021-04-22），全文见 `raw_source.raw_json`

## 194.8 文档构建性能

- **要点**：实测 make htmldocs：Brown -j56 需 26 分 14 秒，Dunlap -j8 笔记本 6 分 05 秒，量化文档构建过慢问题。
- **史料**：`ksummit.messages.9065`（Mark Brown，2025-09-01）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9065 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 make htmldocs 的 -j56 需 26 分 14 秒、-j8 笔记本 6 分 05 秒两组实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以并行度与耗时的量化对照为分析单位）
- **辨析**：本块为全页最可复算的量化实测；“文档构建过慢”为基于数据的判断，其两组配置差异须与构建机规格一并引用。
- **文献**：DSLXC-11060（`ksummit.messages.9065`，2025-09-01），全文见 `raw_source.raw_json`

## 194.9 AI生成内容指南

- **要点**：Bottomley 反对在 AI 内容指南使用 “slop” 一词，主张历时稳定的通用表述，举 rawdog、chad 等年度词渐失语义为例。
- **史料**：`ksummit.messages.9066`（James Bottomley，2026-01-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9066 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：用词之争被还原为“历时稳定的通用表述”与年度词渐失语义两说）；知识注定过时（总纲第 22 条——知识注定过时：rawdog、chad 等年度词渐失语义）
- **辨析**：本块系 James Bottomley 的单方主张；其反对“slop”一词属措辞之争，非技术判断。
- **文献**：DSLXC-11061（`ksummit.messages.9066`，2026-01-10），全文见 `raw_source.raw_json`

## 194.10 git-bug缺陷追踪

- **要点**：Ted Tso 剖析 git-bug 架构安全疑虑：git pull 绕过反垃圾、桥接与数据格式攻击面、类比 Jia Tan 式供应链攻击，称极为不安。Konstantin 详述规划：按子系统建 git-bug 仓库、bugs.kernel.org 重定向器统一寻址、上报经前端预分析、讨论留 lore、同步可选。
- **史料**：`ksummit.messages.9072`（Theodore Tso，2026-04-02）、`ksummit.messages.9145`（Konstantin Ryabitsev，2026-04-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9072 -->` `<!-- ROW_MINE: ksummit.messages.9145 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：git-bug 的供应链风险被类比 Jia Tan 事件，落在信任与责任分配上）；动手者叙事（总纲第 10 条——动手者创造历史：以按子系统建仓、bugs.kernel.org 重定向器等具体规划为分析单位）
- **辨析**：Ted Tso 的五点安全剖析与“极为不安”为其风险立场；Konstantin 的规划为实施方口径，两者本页未见交锋。
- **文献**：DSLXC-11064、DSLXC-11083（`ksummit.messages.9072`、`ksummit.messages.9145`，2026-04-02、2026-04-02），全文见 `raw_source.raw_json`

## 194.11 Rust内核争议

- **要点**：Lyude Paul 详述 Rust 上游困境：说服维护者耗散精力、倦怠语气被常态化、Asahi 的 Rust 代码几乎零 bug，呼吁给 Rust 证明机会。Bart Van Assche 持保留立场：C 比 Rust 易学，“过路式”驱动开发者未必具备学习 Rust 的技能。Feng 与 Contreras 争论“驱动皆可写成 Rust”：Feng 以黑天鹅谬误质疑全部驱动可用 Rust 的假设，Feng 要求对方澄清逻辑。Leon 明言立场：不知 Rust 能解决哪些 C 难解的真实内核问题，故不认同“Rust 收益大于成本”论。
- **史料**：`ksummit.messages.9080`（Lyude Paul，2025-02-20）、`ksummit.messages.9084`（Bart Van Assche，2025-02-19）、`ksummit.messages.9125`（Boqun Feng，2025-02-24）、`ksummit.messages.9172`（Leon Romanovsky，2021-07-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9080 -->` `<!-- ROW_MINE: ksummit.messages.9084 -->` `<!-- ROW_MINE: ksummit.messages.9125 -->` `<!-- ROW_MINE: ksummit.messages.9172 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：Lyude Paul 的一手困境叙述、Assche 的学习成本保留、Feng 的黑天鹅谬误质疑与 Leon 的收益成本否定四方并置）；经验优先（总纲第 9 条——经验优先：以“Asahi 的 Rust 代码几乎零 bug”与“C 比 Rust 易学”等实际经验为判据）
- **辨析**：四条分属不同时段与发言人，构成本页最高密度的正反交锋；Lyude Paul 的“倦怠语气被常态化”为一手当事人证言，落书须保留其证言性质；Feng 与 Contreras 的逻辑之争本页未见结论。
- **文献**：DSLXC-11065、DSLXC-11066、DSLXC-11081、DSLXC-11092（`ksummit.messages.9080`、`ksummit.messages.9084`、`ksummit.messages.9125`、`ksummit.messages.9172`，2025-02-20、2025-02-19、2025-02-24、2021-07-07），全文见 `raw_source.raw_json`

## 194.12 回归处理流程

- **要点**：Rostedt 认为若 Leemhuis 有硬数据证明工作流致回归，议题应升格维护者峰会，并鼓励以数据推动流程改变。
- **史料**：`ksummit.messages.9090`（Steven Rostedt，2024-06-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9090 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“以数据推动流程改变”这一方法论主张为分析单位）；经验优先（总纲第 9 条——经验优先：以“若 Leemhuis 有硬数据证明工作流致回归”这一证据前提为判据）
- **辨析**：本块系 Steven Rostedt 的程序性建议；“议题应升格维护者峰会”为条件性主张，以硬数据为前提。
- **文献**：DSLXC-11067（`ksummit.messages.9090`，2024-06-12），全文见 `raw_source.raw_json`

## 194.13 混合会议主持

- **要点**：Tarreau 介绍 IETF 混合会议经验：jabber scribe 转达聊天提问、虚拟排队、现场排队用麦，兼顾本地与远程平衡。
- **史料**：`ksummit.messages.9093`（Willy Tarreau，2021-06-11）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9093 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 IETF 的 jabber scribe、虚拟排队等实际做法为判据）；多方平等（总纲第 8 条——本体论上各方平等：本地与远程参会者兼顾的平衡设计）
- **辨析**：本块系 Willy Tarreau 的经验移植；“兼顾本地与远程平衡”为目标表述，落书须标明系借鉴自 IETF。
- **文献**：DSLXC-11068（`ksummit.messages.9093`，2021-06-11），全文见 `raw_source.raw_json`

## 194.14 文档工具链

- **要点**：Ojeda 澄清 2022 年现状：Documentation/rust 已用 ReST，rustdoc 仅输出 HTML，并表达对 Markdown 支持的期待。
- **史料**：`ksummit.messages.9094`（Miguel Ojeda，2022-06-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9094 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：2022 年现状为 Documentation/rust 已用 ReST、rustdoc 仅输出 HTML）；多方平等（总纲第 8 条——本体论上各方平等：现有 ReST 方案与 Markdown 支持期待并置）
- **辨析**：本块系 Miguel Ojeda 的现状澄清与期待；“对 Markdown 支持的期待”为意向，非决议。
- **文献**：DSLXC-11069（`ksummit.messages.9094`，2022-06-18），全文见 `raw_source.raw_json`

## 194.15 Folios议题归属

- **要点**：Bottomley 称 folio 属技术议题不宜维护者峰会，LSF/MM 停办后提议以 Plumbers BBB 基础设施办 MM 聚会。
- **史料**：`ksummit.messages.9095`（James Bottomley，2021-09-15）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9095 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：folio 属技术议题不宜维护者峰会这一归类判断与 LSF/MM 停办后的替代安排并置）；动手者叙事（总纲第 10 条——动手者创造历史：以 Plumbers BBB 基础设施办 MM 聚会这一具体方案为分析单位）
- **辨析**：本块系 James Bottomley 的议题归属意见与场地提议，属会务安排，本页未见采纳记录。
- **文献**：DSLXC-11070（`ksummit.messages.9095`，2021-09-15），全文见 `raw_source.raw_json`

## 194.16 PGP信任与密钥

- **要点**：Bottomley 驳短有效期主张：内核密钥主要用于标签签名、分发机制已足；称 GnuPG trustdb 可独立操作，指 Sequoia 说法为宣传。Uwe 力主设 PGP 有效期：引 Gentoo GLEP 63、Sequoia 默认 3 年、letsencrypt 将限 45 天，称安全是移动目标，应改进 keyring 维护。
- **史料**：`ksummit.messages.9096`（James Bottomley，2026-02-05）、`ksummit.messages.9122`（Uwe Kleine-König，2026-01-27）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9096 -->` `<!-- ROW_MINE: ksummit.messages.9122 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：短有效期主张的反驳与设有效期的力主两说并置）；经验优先（总纲第 9 条——经验优先：以 Gentoo GLEP 63、Sequoia 默认 3 年、letsencrypt 将限 45 天等外部实践为判据）
- **辨析**：Bottomley 的“内核密钥主要用于标签签名、分发机制已足”与“指 Sequoia 说法为宣传”为维护者立场；Uwe 的“安全是移动目标”为其论证前提，两者本页未见收敛。
- **文献**：DSLXC-11071、DSLXC-11080（`ksummit.messages.9096`、`ksummit.messages.9122`，2026-02-05、2026-01-27），全文见 `raw_source.raw_json`

## 194.17 AI代码标注政策

- **要点**：Kosina 主张须能知悉补丁出自 AI 以便知情决策或直接拒收：AI 代码背后可能无人理解其逻辑可供人讨论。McKenney 称 SoB 对 AI 产出的规则尚未明确，需与混沌中的法律诉讼进程对齐，现阶段指望 AI 输出安全是愚蠢的。
- **史料**：`ksummit.messages.9101`（Jiri Kosina，2025-08-21）、`ksummit.messages.9115`（Paul E. McKenney，2025-08-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9101 -->` `<!-- ROW_MINE: ksummit.messages.9115 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：AI 代码的 SoB 规则被明示为须与法律诉讼进程对齐）；多方平等（总纲第 8 条——本体论上各方平等：知情决策或直接拒收与法律未定的现实并置）
- **辨析**：Kosina 的“AI 代码背后可能无人理解其逻辑”为可维护性论证；McKenney 的“现阶段指望 AI 输出安全是愚蠢的”为价值判断，非技术结论。
- **文献**：DSLXC-11072、DSLXC-11077（`ksummit.messages.9101`、`ksummit.messages.9115`，2025-08-21、2025-08-20），全文见 `raw_source.raw_json`

## 194.18 GitLab工作流

- **要点**：Zickus 详解红帽 RHEL 内核 GitLab 流程：评审数据结构化、经 API 聚合补丁讨论、审批与 CI 状态，可抽象移植到其他传输机制。
- **史料**：`ksummit.messages.9103`（Don Zickus，2021-07-07）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9103 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以评审数据结构化、经 API 聚合补丁讨论与 CI 状态等具体流程为分析单位）；经验优先（总纲第 9 条——经验优先：以红帽 RHEL 内核 GitLab 的实际流程为判据）
- **辨析**：本块系 Don Zickus 的流程详解；“可抽象移植到其他传输机制”为其技术判断，非既成事实。
- **文献**：DSLXC-11073（`ksummit.messages.9103`，2021-07-07），全文见 `raw_source.raw_json`

## 194.19 内核文档议题

- **要点**：Corbet 反对 sphinx-pre-install 自动寻替代解释器：脚本应按预期行为运行；指 RHEL8 建文档者极少且 Leap 15 将被取代。Corbet 提交 2025 峰会文档议题：过去一年文档构建基础设施大量改进，回顾近况并讨论未来两三年文档演进方向。Nikula 主张 Sphinx 构建重质不重量：先清零 kernel-doc 与 rst 告警（i915/xe 已有本地检查、扩展至 drm 失败），不宜全量收录。
- **史料**：`ksummit.messages.9109`（Jonathan Corbet，2025-09-03）、`ksummit.messages.9151`（Jonathan Corbet，2025-08-22）、`ksummit.messages.9171`（Jani Nikula，2025-09-01）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9109 -->` `<!-- ROW_MINE: ksummit.messages.9151 -->` `<!-- ROW_MINE: ksummit.messages.9171 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 sphinx-pre-install 的预期行为、kernel-doc 与 rst 告警清零等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“RHEL8 建文档者极少且 Leap 15 将被取代”与“i915/xe 已有本地检查”等实际状况为判据）
- **辨析**：Corbet 的两条分属工具行为与议题提案，其“脚本应按预期行为运行”为维护者定则；Nikula 的“重质不重量、不宜全量收录”与 Corbet 的演进回顾构成路线差异。
- **文献**：DSLXC-11075、DSLXC-11085、DSLXC-11091（`ksummit.messages.9109`、`ksummit.messages.9151`、`ksummit.messages.9171`，2025-09-03、2025-08-22、2025-09-01），全文见 `raw_source.raw_json`

## 194.20 linux-next构建

- **要点**：Brown 谈 linux-next 实践：bisect 沿线性历史定位引入分支、ccache 因 KernelCI 平庸体验被 Stephen 关闭、按序抽样构建以控时长。
- **史料**：`ksummit.messages.9113`（Mark Brown，2026-08-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9113 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 bisect 沿线性历史定位引入分支、按序抽样构建等具体手法为分析单位）；经验优先（总纲第 9 条——经验优先：以“ccache 因 KernelCI 平庸体验被 Stephen 关闭”这一实际决定为判据）
- **辨析**：本块系 Mark Brown 的实践自述；“ccache 被关闭”系 Stephen 的决定，属他人行为转述，落书须标明。
- **文献**：DSLXC-11076（`ksummit.messages.9113`，2026-08-13），全文见 `raw_source.raw_json`

## 194.21 Rust别名模型

- **要点**：hpa 强调标准化进程价值在于写出含边角情形的正式契约；引 Alice 观点：Rust 别名模型担忧被夸大，可只留在确定合法子集内。Ralf Jung 说明 Miri 默认按 Stacked Borrows 检查（比 Tree Borrows 更严）、playground 不支持自定义旗标，盼 Miri 进入 Compiler Explorer。
- **史料**：`ksummit.messages.9118`（H. Peter Anvin，2025-02-25）、`ksummit.messages.9157`（Ralf Jung，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9118 -->` `<!-- ROW_MINE: ksummit.messages.9157 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以正式契约含边角情形、Miri 的 Stacked Borrows 检查等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：别名模型担忧被夸大的观点与 Miri 更严检查的实况并置）
- **辨析**：Anvin 引 Alice 观点属转述；Jung 的“Miri 默认按 Stacked Borrows 检查（比 Tree Borrows 更严）”为工具现状一手说明。
- **文献**：DSLXC-11078、DSLXC-11086（`ksummit.messages.9118`、`ksummit.messages.9157`，2025-02-25、2025-02-26），全文见 `raw_source.raw_json`

## 194.22 栈回溯行号

- **要点**：kallsyms 行号表实测：459 万条目、.rodata 增约 44MiB（vmlinux +8.3%）；Figa 建议移入可加载模块，崩溃后自动加载二次报告。
- **史料**：`ksummit.messages.9120`（Tomasz Figa，2026-03-03）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9120 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以 459 万条目、.rodata 增约 44MiB、vmlinux +8.3% 三项实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“移入可加载模块、崩溃后自动加载二次报告”这一具体方案为分析单位）
- **辨析**：本块为带数字的可复算实测；“建议移入可加载模块”为提案，本页未见采纳。
- **文献**：DSLXC-11079（`ksummit.messages.9120`，2026-03-03），全文见 `raw_source.raw_json`

## 194.23 补丁收件人筛选

- **要点**：Leon 指资深开发者也犯的恶习：精心筛选 TO/CC 致补丁脱离上下文、反馈割裂成“孤岛”无法对照，附 rdma 系列实例链接。
- **史料**：`ksummit.messages.9139`（Leon Romanovsky，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9139 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“资深开发者也犯的恶习”与附 rdma 系列实例链接为判据）；多方平等（总纲第 8 条——本体论上各方平等：补丁脱离上下文与反馈割裂成孤岛这一后果陈述）
- **辨析**：本块系 Leon Romanovsky 的批评，附可反查的 rdma 系列链接；“孤岛”为其定性表述，非量化结论。
- **文献**：DSLXC-11082（`ksummit.messages.9139`，2021-04-22），全文见 `raw_source.raw_json`

## 194.24 CoC执行争议

- **要点**：Shuah 披露 CoC 多数报告系对社区运作的误解、幕后化解；就 Linus buffer cache 言论被 Chinner 指违 CoC 一案表态，认为有 CoC 更好。
- **史料**：`ksummit.messages.9149`（Shuah，2023-09-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9149 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“CoC 多数报告系对社区运作的误解、幕后化解”这一实际处理记录为判据）；多方平等（总纲第 8 条——本体论上各方平等：Chinner 指违 CoC 一案与“有 CoC 更好”的表态并置）
- **辨析**：本块系 Shuah 以 CoC 相关身份的表态；“认为有 CoC 更好”为价值判断，其个案处置细节本页未展开。
- **文献**：DSLXC-11084（`ksummit.messages.9149`，2023-09-19），全文见 `raw_source.raw_json`

## 194.25 HIGHMEM淘汰

- **要点**：Arnd 考证 ARMv5 highmem 仅剩 OpenBlocks A7（内存须受限）等少数机器：Debian armel 已出末版、mv78xx0 平台可整体移除。
- **史料**：`ksummit.messages.9159`（Arnd Bergmann，2025-09-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9159 -->`
- **史观**：知识注定过时（总纲第 22 条——知识注定过时：ARMv5 highmem 仅剩 OpenBlocks A7 等少数机器，Debian armel 已出末版）；经验优先（总纲第 9 条——经验优先：以“mv78xx0 平台可整体移除”这一可核平台清单为判据）
- **辨析**：本块系 Arnd Bergmann 的考证，属平台存废的可核清单；“可整体移除”为其判断，落书须与当期平台支持状态核对。
- **文献**：DSLXC-11087（`ksummit.messages.9159`，2025-09-18），全文见 `raw_source.raw_json`

## 194.26 UALink驱动归属

- **要点**：Greg KH 反对以 staging 引入 UALink：迁出 staging 成本高于树外先清理再合入，同意首日即用 drivers/accel/ual 建子系统。
- **史料**：`ksummit.messages.9160`（Greg KH，2025-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9160 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“首日即用 drivers/accel/ual 建子系统”这一具体路径为分析单位）；经验优先（总纲第 9 条——经验优先：以“迁出 staging 成本高于树外先清理再合入”这一成本比较为判据）
- **辨析**：本块系 Greg KH 的路径反对意见；“迁出 staging 成本更高”为经验判断，未附成本细目。
- **文献**：DSLXC-11088（`ksummit.messages.9160`，2025-09-12），全文见 `raw_source.raw_json`

## 194.27 Bugzilla通知争议

- **要点**：Artem 坚持按 git 提交自动订阅、一键 opt-out 即可；Greg KH 驳称强加订阅必招反感，开发者无义务分诊 bug。
- **史料**：`ksummit.messages.9161`（Artem S. Tashkinov，2022-10-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9161 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：自动订阅加一键 opt-out 的主张与“强加订阅必招反感”的反驳并置）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：开发者无义务分诊 bug 被明示为责任边界）
- **辨析**：本块含 Artem Tashkinov 的坚持与 Greg KH 的反驳两方；“开发者无义务分诊 bug”为维护者立场，非成文规则。
- **文献**：DSLXC-11089（`ksummit.messages.9161`，2022-10-02），全文见 `raw_source.raw_json`

## 194.28 用户态开源要求

- **要点**：tglx 主张接口门槛是文档须足以实现开源用户态，而非当下是否已存在；已存在也不保证功能完备。
- **史料**：`ksummit.messages.9163`（Thomas Gleixner，2021-09-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9163 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：文档须足以实现开源用户态这一门槛与“当下是否已存在”的实况被明确区分）；经验优先（总纲第 9 条——经验优先：以“已存在也不保证功能完备”这一经验判断为判据）
- **辨析**：本块系 Thomas Gleixner 的门槛界定，属规则层一手表述；“已存在也不保证功能完备”为对既有做法的限定。
- **文献**：DSLXC-11090（`ksummit.messages.9163`，2021-09-10），全文见 `raw_source.raw_json`

## 194.29 峰会代表性

- **要点**：Howlett 批评维护者峰会核心圈固化，提议专题临时席位与代表制；追问 MM 即将更换首席维护者时程序委员会如何考虑其影响。
- **史料**：`ksummit.messages.9174`（Liam R. Howlett，2026-08-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9174 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：核心圈固化之批评与专题临时席位、代表制提议并置）；动手者叙事（总纲第 10 条——动手者创造历史：以专题临时席位与代表制这一具体组织设计为分析单位）
- **辨析**：本块系 Liam R. Howlett 的批评与提议；“追问 MM 即将更换首席维护者时程序委员会如何考虑其影响”为开放问句，本页未见答复。
- **文献**：DSLXC-11094（`ksummit.messages.9174`，2026-08-10），全文见 `raw_source.raw_json`
