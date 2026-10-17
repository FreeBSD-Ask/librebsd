# 139 【Linux社区】regzbot全文与conclave补丁

> 来源：ksummit 独有 p3（50 封全读，2021-04 至 2026-08，regzbot #regzb 标签设计全文、conclave.rst 项目连续性补丁提交、linus-next next-analysis 与 pr-hist.sh 工具与 PR 停留时长统计、C 聚合传递 borrows 模型作者澄清与 Miri 论文之辩、Rust 与 ISO C 工作组对话、vger 迁 subspace 通报、bugzilla 网页表单邮件化提案）
> 判定：44 CAND / 6 NV。主题分布：LLM相关话题：AI依赖 1、设备直通之害 3、Rust for Linux 3、Link尾注替换之争 1、Folios峰会议题 1、实现malloc 1、邮件列表文档补丁v2 1、Rust内核政策 3、AI补丁审查工具 2、linus-next测试改进 3、2021峰会筹备 2、管理预期 1、bugzilla退役讨论 1、AI代码审查的地位 1、-next反馈 1、bugzilla减负 1、功能纳入与剔除的形式化 1、回归须入最新stable的提案 1、DRM panel现代化 1、embargo安全议题处理 1、内核文档愿景 2、维护者支持小组 1、MAINTAINERS THE REST换列表 1、维护者峰会存废 1、C聚合传递（Rust政策） 3、工具生成内容准则补丁 1、回归四提案背景 1、项目连续性文档补丁 1、regzbot回归追踪bot RFC 1、电源时序子系统 1、-next中的隐藏提交 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p3 的逐封提取（2021-04 至 2026-08，44 CAND / 6 NV），全 31 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 139.1 LLM相关话题：AI依赖

- 【Linux社区】以电力类比反驳Laurent对生成式AI依赖的担忧，称依赖无处不在且人们多不自知。 `<!-- ROW_MINE: ksummit.messages.355 -->`

## 139.2 设备直通之害

- 【Linux社区】要求Ricardo给出使用命令缓冲的ISP具体实例及固件层细节，主张以具体例子推进讨论。 `<!-- ROW_MINE: ksummit.messages.358 -->`
- 【Linux社区】拒绝公开点名的厂商案例，反驳市场自然逆向论，区分视觉处理器与相机ISP，重申直通放行会破坏与厂商合作的长期积累。 `<!-- ROW_MINE: ksummit.messages.455 -->`
- 【Linux社区】与Ricardo长辩：界定“完全开放”标准、反驳ISP等同加速器与可编程ISP论据，指Synopsys EV7x是视觉处理器而非相机ISP。 `<!-- ROW_MINE: ksummit.messages.461 -->`

## 139.3 Rust for Linux

- 【Linux社区】给出pl061 get_direction的C与Rust并排反汇编，解释revocable资源、跨语言LTO缺失与泛型内联导致难以逐行对应。 `<!-- ROW_MINE: ksummit.messages.363 -->`
- 【Linux社区】质疑Rust代码在-stable侧的复审可行性，称C代码复审已难、稳定版二次复审者将不存在。 `<!-- ROW_MINE: ksummit.messages.412 -->`
- 【Linux社区】澄清Rust无编译器魔法式引用计数，生命周期与借用和引用计数正交并给双可变引用示例，称dentry/inode集成可处理、建议同步改进C模型。 `<!-- ROW_MINE: ksummit.messages.482 -->`

## 139.4 Link尾注替换之争

- 【Linux社区】反驳Rostedt，认为即使指向无讨论的单一补丁，Link:也能让人看出无讨论并在回归时据此发起讨论。 `<!-- ROW_MINE: ksummit.messages.365 -->`

## 139.5 Folios峰会议题

- 【Linux社区】赞同Ted对Folios合并分歧的判断，主张聚焦“匿名页是否应成为folio”这一MM核心争议并向前看。 `<!-- ROW_MINE: ksummit.messages.367 -->`

## 139.6 实现malloc

- 【Linux社区】逐项分析HW TAGS KASAN、经典KASAN与poisoning/slab_debug/debug_pagealloc的适用场景，主张各工具并存、现阶段无可替代。 `<!-- ROW_MINE: ksummit.messages.368 -->`

## 139.7 邮件列表文档补丁v2

- 【Linux社区】通报vger迁移至mlmmj/subspace，更新过时链接、废除/r/子路径建议并新增Link尾注使用指南，源自ksummit讨论。 `<!-- ROW_MINE: ksummit.messages.370 -->`

## 139.8 Rust内核政策

- 【Linux社区】不反对Rust，但补充C++社区已有contracts与profiles等安全提案，并质疑其能否迁移到C。 `<!-- ROW_MINE: ksummit.messages.382 -->`
- 【Linux社区】与ISO C工作组Uecker对话：澄清其指内核侧加固工作而非ISO C、无公司愿资助标准化，指内核已有类似字符串类型、欢迎GCC扩展补丁，并追问C“内存安全”含义。 `<!-- ROW_MINE: ksummit.messages.406 -->`
- 【Linux社区】反驳Greg：前提是驱动“能”用Rust写，引reiser4与kdbus为例，称纸面优势不等于现实可行。 `<!-- ROW_MINE: ksummit.messages.439 -->`

## 139.9 AI补丁审查工具

- 【Linux社区】详解netdev CI与patchwork对接方式：CI经API取补丁、结果以红绿灯回填，失败需人工判断，非公共CI且费用不由提交者承担。 `<!-- ROW_MINE: ksummit.messages.385 -->`
- 【Linux社区】主张把“开发者应预先跑工具”的“应”改为“能”，承认部分人达不到、CI更省力，且AI常大错、公开列表可让人纠错。 `<!-- ROW_MINE: ksummit.messages.431 -->`

## 139.10 linus-next测试改进

- 【Linux社区】确认已测通过的fixes分支进linux-next是普遍做法，并称由此发现的问题很少但非零。 `<!-- ROW_MINE: ksummit.messages.389 -->`
- 【Linux社区】公开next-analysis脚本，给出在-next停留天数直方图并找出未上lore的提交，邀请协作做bot或仪表盘。 `<!-- ROW_MINE: ksummit.messages.402 -->`
- 【Linux社区】发布pr-hist.sh脚本，可按git request-pull文件统计PR中提交在linux-next的停留时长。 `<!-- ROW_MINE: ksummit.messages.453 -->`

## 139.11 2021峰会筹备

- 【Linux社区】提议让与会者用随身手机充当麦克风，改善远程参与收音难题。 `<!-- ROW_MINE: ksummit.messages.395 -->`
- 【Linux社区】回应疫苗话题管制，转向混合会议组织：强调主持人督促用麦、增设带A/V设备的分组讨论室。 `<!-- ROW_MINE: ksummit.messages.484 -->`

## 139.12 管理预期

- 【Linux社区】回应Dan Williams：厂商做“同类事”就需共享ABI，主张社区先自行争斗达成一致，提及机密计算跨厂商案例。 `<!-- ROW_MINE: ksummit.messages.396 -->`

## 139.13 bugzilla退役讨论

- 【Linux社区】称libcap的bugzilla需求尚可，唯一要求是迁移时支持旧bug URL重定向到新系统。 `<!-- ROW_MINE: ksummit.messages.414 -->`

## 139.14 AI代码审查的地位

- 【Linux社区】认可Rodrigo所述先让开发者处理AI发现再人工复审的流程，称这与无人工介入的体验截然不同且合理得多。 `<!-- ROW_MINE: ksummit.messages.421 -->`

## 139.15 -next反馈

- 【Linux社区】对Sasha的AI合并冲突解决实验表态：不反对，但若无受益者不愿承担相关成本。 `<!-- ROW_MINE: ksummit.messages.424 -->`

## 139.16 bugzilla减负

- 【Linux社区】提议网页表单以邮件格式投递结构化bug报告，并由自动应答提示缺失字段以训练用户。 `<!-- ROW_MINE: ksummit.messages.428 -->`

## 139.17 功能纳入与剔除的形式化

- 【Linux社区】认同导师制想法但指出Brian Foster曾充当缓冲却因缺乏授权而失败，问题早已被预判、需要的是更好的缓解机制。 `<!-- ROW_MINE: ksummit.messages.438 -->`

## 139.18 回归须入最新stable的提案

- 【Linux社区】支持Laurent反对将回归修复设为维护者硬性义务，主张改进发现回归与定位起点的工具，并可作为新人的todo清单。 `<!-- ROW_MINE: ksummit.messages.445 -->`

## 139.19 DRM panel现代化

- 【Linux社区】附议Linus Walleij对面板IC厂商不公开文档的不满，建议以上游化厂商驱动为切入点，指ChromeOS偏eDP、Android GKI不利上游。 `<!-- ROW_MINE: ksummit.messages.451 -->`

## 139.20 embargo安全议题处理

- 【Linux社区】论证“跟进stable”与“预披露通知”正交，区分研究者披露类漏洞与普通补丁，提出放宽linux-distros政策、修正文档、设引导人三条路径。 `<!-- ROW_MINE: ksummit.messages.452 -->`

## 139.21 内核文档愿景

- 【Linux社区】自荐参与kernel-doc python化，主张构建链与内核开发解耦、维护单一环境，并坦言正则解析无通用方案。 `<!-- ROW_MINE: ksummit.messages.454 -->`
- 【Linux社区】逐类拆解htmldocs噪音四大来源（交叉引用、ABI校验含2815个未文档化sysfs符号、kernel-doc、Sphinx），主张推行无警告构建政策并解释sphinx-pre-install的venv选择。 `<!-- ROW_MINE: ksummit.messages.486 -->`

## 139.22 维护者支持小组

- 【Linux社区】分享倦怠风险清单资源，主张会前举办面向非受邀者的公开讨论，目标包括寻求专业帮助在内的多种方案。 `<!-- ROW_MINE: ksummit.messages.457 -->`

## 139.23 MAINTAINERS THE REST换列表

- 【Linux社区】提议后端订阅全部内核邮件列表、仅导入补丁至public-inbox git归档，使patches@开箱即用。 `<!-- ROW_MINE: ksummit.messages.458 -->`

## 139.24 维护者峰会存废

- 【Linux社区】感谢Ted详解邀请流程，建议将流程写入Documentation/process/并给出CFP措辞的具体修改diff。 `<!-- ROW_MINE: ksummit.messages.459 -->`

## 139.25 C聚合传递（Rust政策）

- 【Linux社区】澄清gccrs是GCC内新前端而rustc_codegen_gcc是Rust项目内的后端，引官方博客说明两者在协作，并cc开发者求证。 `<!-- ROW_MINE: ksummit.messages.463 -->`
- 【Linux社区】以模型作者身份说明Stacked与Tree Borrows是正确性的候选定义、一经采纳即无真假阳性的定义问题，并解释Miri做测试而非验证、能捕获单次执行的全部UB。 `<!-- ROW_MINE: ksummit.messages.469 -->`
- 【Linux社区】引Tree Borrows论文反驳“无假阳性”说法，质疑Miri作为sanitizer不能证明正确性，并指别名规则绑定LLVM后端将加大gccrs实现难度。 `<!-- ROW_MINE: ksummit.messages.470 -->`

## 139.26 工具生成内容准则补丁

- 【Linux社区】批评补丁措辞过软如“或许可以”，要求明确写出“我们不接受机器灌水”的强硬立场。 `<!-- ROW_MINE: ksummit.messages.464 -->`

## 139.27 回归四提案背景

- 【Linux社区】实地核查Greg所称stable-queue与linux-stable-rc树，发现6.10.y分支直到6.10.1发布前才建立，质询“合并窗口期间持续更新”是否属实。 `<!-- ROW_MINE: ksummit.messages.465 -->`

## 139.28 项目连续性文档补丁

- 【Linux社区】提交conclave.rst：若Linus不能继续合并主线，72小时内由上届峰会组织者或TAB主席召集上届受邀者与TAB议定接替方案。 `<!-- ROW_MINE: ksummit.messages.466 -->`

## 139.29 regzbot回归追踪bot RFC

- 【Linux社区】完整提出regzbot设计：#regzb标签驱动、开发者零额外负担、网页状态页含休眠区、标签语法与限制、python实现及NGI资助。 `<!-- ROW_MINE: ksummit.messages.476 -->`

## 139.30 电源时序子系统

- 【Linux社区】LPC24议题提交：以Qualcomm WCN/QCA为例说明封装内WLAN与BT模块互依赖，提出pwrseq提供者/消费者抽象与DT表示。 `<!-- ROW_MINE: ksummit.messages.478 -->`

## 139.31 -next中的隐藏提交

- 【Linux社区】回应Krzysztof议题：介绍其PR分析bot统计提交在-next停留时长，因未获Linus认可其价值而停发报告。 `<!-- ROW_MINE: ksummit.messages.487 -->`
