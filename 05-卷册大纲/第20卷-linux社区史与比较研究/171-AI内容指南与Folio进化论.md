# 171 【Linux社区】AI内容指南与Folio进化论

> 来源：ksummit 独有 p35（50 封全读，2022-06 至 2025-11：完整转抄 TAB 起草的 generated-content.rst 全文含工具与提示词披露及维护者处置权系 2025 年 AI 内容政策核心一手文献；Ted Tso 以 Linux 是进化而非智能设计为 Folio 辩护引 USB 与网络栈三次重写史；Ted 一手叙述 2023 维护者峰会上 Linus buffer cache 言论被 Dave Chinner 指为 CoC 违规争议；Daniel Vetter 论厂商开源真实驱动机制法律障碍无用成功项目与 DRM uAPI 要求文档才是大棒；加速器用户态要求六封、AI 生成内容指南四封、Rust 入核初期争论三封、稳定树回归治理四封）
> 判定：43 CAND / 7 NV。主题分布：文档Sphinx版本 1、CoC执行边界 1、bugzilla治理困境 1、稳定树回归治理 4、加速器用户态要求 6、AI生成内容指南 4、明大假补丁事件 1、设计文档可及性 1、TAB选举投票故障 1、LKML流量改造方案 1、错误指针返回规范 1、DAMON峰会提案 1、Rust政策与C安全 4、strscpy替换争论 1、补丁基址标注 1、厂商开源驱动机制 1、Rust入核初期争论 3、HIGHMEM淘汰进展 2、RHEL GitLab工作流 1、Folio演进论辩护 1、峰会远程参与 1、面板厂商贡献策略 1、eBPF接口稳定争论 1、栈回溯行号内嵌 1、ChatGPT驱动质量 1、内核密钥信任网 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p35 的逐封提取（2022-06 至 2025-11，43 CAND / 7 NV），全 26 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 171.1 文档Sphinx版本

- 【Linux社区】Mauro称若弃旧版兼容Sphinx最低需3.1.0，openSUSE Leap 15.4仅有2.3.1与4.2.0包，建议脚本优先推荐发行版原生包否则回退venv。 `<!-- ROW_MINE: ksummit.messages.5406 -->`

## 171.2 CoC执行边界

- 【Linux社区】Ted称维护者峰会上Linus“buffer cache is trivial”言论被Dave Chinner公开指为CoC违规，认为此类边缘案例令开发者惧怕并抹黑CoC。 `<!-- ROW_MINE: ksummit.messages.5412 -->`

## 171.3 bugzilla治理困境

- 【Linux社区】Greg称雇主极少允许维护者长期处理上游bug，LF仅托管bugzilla不负责内容，其本人是LF资助的少数者，改进需说服700+维护者且仅Thorsten在做。 `<!-- ROW_MINE: ksummit.messages.5413 -->`

## 171.4 稳定树回归治理

- 【Linux社区】Brown指stable测试者池小、响应周期紧限制测试类型，主张帮用户在stable内bisect，并关注无需重构基础设施即可构建运行的诉求。 `<!-- ROW_MINE: ksummit.messages.5414 -->`
- 【Linux社区】Bottomley举无Fixes与stable标记的strlcpy转换commit仍被回溯（因Stable-dep-of链），Greg承认此类依赖无法自动发现，请提交stable@排队。 `<!-- ROW_MINE: ksummit.messages.5492 -->`
- 【Linux社区】Kara提用Message-Id标签经lore自动定位所属系列，stable应整系列取舍勿随机抽子集；称每年数次子集回溯致损，Amir上周刚拦下一次。 `<!-- ROW_MINE: ksummit.messages.5517 -->`
- 【Linux社区】Kosina反对在内核文档写死回归修复时限：徒增维护者压力无实益，复杂度休假与疏漏皆致延迟，且给报告者不实预期。 `<!-- ROW_MINE: ksummit.messages.5566 -->`

## 171.5 加速器用户态要求

- 【Linux社区】Bottomley引GPLv2系统例外论：API一旦暴露给用户态即无法限制专有程序使用，修改例外不明智，唯一手段是对恶意用途不导出接口。 `<!-- ROW_MINE: ksummit.messages.5420 -->`
- 【Linux社区】Bottomley以机密计算为例：厂商标准多止于实验室原型，上游化后共性浮现、不可行实现被修正，最终形成事实标准而非厂商标准。 `<!-- ROW_MINE: ksummit.messages.5444 -->`
- 【Linux社区】Bottomley系统论证EXPORT_SYMBOL_USERSPACE_GPL无法律基础：GPLv2系统例外已放弃对用户态程序类型的控制，修改例外将危及其他专有软件。 `<!-- ROW_MINE: ksummit.messages.5468 -->`
- 【Linux社区】Vetter列四类设备编程模型自MMIO独占到全抢占直提，Laurent补V4L2 M2M与ISP单进程限制；二人批评高通misc加速驱动绕过两子系统审查。 `<!-- ROW_MINE: ksummit.messages.5476 -->`
- 【Linux社区】Brown指kselftest须控制依赖，BPF测试因依赖过重已默认禁用并曾干扰实际使用者；内核庞大不必万物归一，测试应服务实际使用者。 `<!-- ROW_MINE: ksummit.messages.5536 -->`
- 【Linux社区】Pinchart称GPU/ISP接口是设备专属命令缓冲ioctl（举ipu3_uapi_params），接口级自测无意义，“要测GPU得把Mesa搬进内核”。 `<!-- ROW_MINE: ksummit.messages.5540 -->`

## 171.6 AI生成内容指南

- 【Linux社区】Linus驳版权论：内核已有数百万行AMD GPU生成头文件，AI只是另一工具，版权要求与其他代码无异，并讽AI炒作与巨额资金。 `<!-- ROW_MINE: ksummit.messages.5434 -->`
- 【Linux社区】Babka将TAB起草的generated-content.rst全文转抄ksummit与workflows，要求披露工具提示词与影响范围、维护者可拒收，并指LKML无人读致其被忽视。 `<!-- ROW_MINE: ksummit.messages.5498 -->`
- 【Linux社区】Brauner要求删除“令人印象深刻”“无疑提升生产力”等宣传措辞保持客观，Hansen同意改为“工具会增加贡献量”，强调维护者审查带宽稀缺。 `<!-- ROW_MINE: ksummit.messages.5584 -->`
- 【Linux社区】Kees称LLM参与度跨度太大、标签暂无法准确刻画，先立“展示你的工作”文档；Rostedt赞同，把标签争论留到维护者峰会以免无尽bikeshed。 `<!-- ROW_MINE: ksummit.messages.5585 -->`

## 171.7 明大假补丁事件

- 【Linux社区】Mauro警告UMN事件宣传会吸引黑客效仿需加防范；引Geert称190封被回退补丁许多是真修复，James Morris指无同意须审计其全部贡献。 `<!-- ROW_MINE: ksummit.messages.5455 -->`

## 171.8 设计文档可及性

- 【Linux社区】Konstantin提醒Google Docs在中国被屏蔽、俄罗斯亦然，建议改用受限提交的git仓库使提交可归因，并用Link标签令邮件列表为事实源。 `<!-- ROW_MINE: ksummit.messages.5459 -->`

## 171.9 TAB选举投票故障

- 【Linux社区】TAB选举官Laura确认多邮箱贡献者地址合并尝试引发CIVS投票与收票问题，承认是明年需修复的流程痛点。 `<!-- ROW_MINE: ksummit.messages.5460 -->`

## 171.10 LKML流量改造方案

- 【Linux社区】Konstantin提三步：get_maintainer.pl默认不再抄LKML、public-inbox加RSS、设ALWAYS CC patches列表；Jason赞lore变革性，建议PR虚拟列表。 `<!-- ROW_MINE: ksummit.messages.5461 -->`

## 171.11 错误指针返回规范

- 【Linux社区】Hannes主张可返回错误指针的函数必须始终返回错误指针，回NULL属拙劣写法；Julia统计超230个文件存在NULL与ERR_PTR混返并举overlayfs为例。 `<!-- ROW_MINE: ksummit.messages.5465 -->`

## 171.12 DAMON峰会提案

- 【Linux社区】Park提交DAMON 2024峰会提案：细粒度DAMOS、自动调优、分层内存、访问感知自动伸缩、写保护监测与热迁移等子题，附2019-2023历年场次链接。 `<!-- ROW_MINE: ksummit.messages.5466 -->`

## 171.13 Rust政策与C安全

- 【Linux社区】Carpenter称内存安全pragma内核基本禁用、drm中用会关闭Sparse；静态严格检查有误报问题；运行时UB陷阱即UBSan、极有价值。 `<!-- ROW_MINE: ksummit.messages.5495 -->`
- 【Linux社区】Overstreet批C标准未有用地定义UB且被编译器作者当挡箭牌，Rust进程以用户对话与实用性驱动，“无需标准机构也可有规范”。 `<!-- ROW_MINE: ksummit.messages.5500 -->`
- 【Linux社区】Linus驳功耗论：高性能必然低效是现实规律，ARM乱序已胜、连小核也OoO，VLIW是“CPU世界的蛇”，只宜留DSP与GPU特化场景。 `<!-- ROW_MINE: ksummit.messages.5509 -->`
- 【Linux社区】Tarreau赞结构体值传递（寄存器对零开销，其ist字符串库用ptr,len可链式调用），但警告内核中赋值可能把未初始化的洞泄漏给用户态。 `<!-- ROW_MINE: ksummit.messages.5575 -->`

## 171.14 strscpy替换争论

- 【Linux社区】Hellwig反对NVMe改用strscpy称其几乎无文档、不如snprintf；Kees主张strtomem与kmemdup_nul消除歧义；Stitt补fortify文档链接。 `<!-- ROW_MINE: ksummit.messages.5504 -->`

## 171.15 补丁基址标注

- 【Linux社区】Pinchart称维护者也常不知系列应基于何树，b4的base-commit与prerequisite-patch-id很有用；Bottomley反对强制因系列可不变或依赖未合补丁。 `<!-- ROW_MINE: ksummit.messages.5506 -->`

## 171.16 厂商开源驱动机制

- 【Linux社区】Vetter称法律技术障碍作用边际，开放GPU栈九成MIT、GPL部分常年被无视；真正有效的是成功项目收益加DRM用户态开源要求文档这根“大棒”。 `<!-- ROW_MINE: ksummit.messages.5508 -->`

## 171.17 Rust入核初期争论

- 【Linux社区】Belloni以反问施压Miguel：既然维护者需懂Rust才能动其代码，那么维护者不懂Rust时Rust代码是否就不应合入该子系统？ `<!-- ROW_MINE: ksummit.messages.5519 -->`
- 【Linux社区】Ojeda说明健全unsafe下Rust无UB但泄漏非UB；抽象薄调devres还是自写是开放问题，红黑树即弃alloc的BTreeMap自写以贴近C API。 `<!-- ROW_MINE: ksummit.messages.5525 -->`
- 【Linux社区】Brown附和Greg并补音频例：硬件似v4l多设备混搭、经多个设备节点暴露为一个用户可见对象，多生命周期交互问题同样突出。 `<!-- ROW_MINE: ksummit.messages.5561 -->`

## 171.18 HIGHMEM淘汰进展

- 【Linux社区】Wilcox建议先删HIGHPTE：x86已弃仅剩ARM，页错误路径复杂度可除；Walleij已发RFC补丁，现仅VT8500默认启用，待Russell King表态。 `<!-- ROW_MINE: ksummit.messages.5530 -->`
- 【Linux社区】Weinberger自述负责ARMv7与PPC32、最高2GiB内存通信设备，全球五位数部署，最老4.19 LTS、十年内继续支持，预期应用与FPGA驱动受影响。 `<!-- ROW_MINE: ksummit.messages.5577 -->`

## 171.19 RHEL GitLab工作流

- 【Linux社区】Zickus介绍RHEL自PatchWork迁GitLab：集成CI、CKI强制通过、webhook自动化、减邮件增CLI，已在DevConf与CentOS Dojo宣讲并愿讲Plumbers。 `<!-- ROW_MINE: ksummit.messages.5538 -->`

## 171.20 Folio演进论辩护

- 【Linux社区】Ted引Linus“Linux是进化而非智能设计”与Greg 2006演讲，称USB与网络栈各重写三次，主张Folio有改进就该合入再演进，反对因不够彻底而NACK。 `<!-- ROW_MINE: ksummit.messages.5547 -->`

## 171.21 峰会远程参与

- 【Linux社区】Toke与Willy介绍IETF jabberscribe与排队麦克风经验；Mauro为圆桌提两案：全员用笔记本摄像麦或每桌配独立摄像麦，配发言排队软件。 `<!-- ROW_MINE: ksummit.messages.5549 -->`

## 171.22 面板厂商贡献策略

- 【Linux社区】Maxime称只能提供基础设施无法强求面板厂贡献文档；Walleij的策略是在其行为令作为客户的大公司难堪时公开点名并附lore链接。 `<!-- ROW_MINE: ksummit.messages.5551 -->`

## 171.23 eBPF接口稳定争论

- 【Linux社区】Kosina以tracepoint格式变更毁掉ubertrace类比BPF；Starovoitov反驳称tracepoint经cat/echo文件暴露API，追问BPF跟踪工具用了哪个暴露API。 `<!-- ROW_MINE: ksummit.messages.5555 -->`

## 171.24 栈回溯行号内嵌

- 【Linux社区】Rostedt评kallsyms内嵌行号：保留0x与括号免歧义；定位为内核开发者自调试特性，发行版仍用decode_stacktrace.pl；会遇gdb内联函数同类问题。 `<!-- ROW_MINE: ksummit.messages.5571 -->`

## 171.25 ChatGPT驱动质量

- 【Linux社区】Kosina称数月前见ChatGPT全写的GPIO驱动功能正确可运行，但散见错误处理缺失，以此回应“AI只犯大错不犯细微错”之问。 `<!-- ROW_MINE: ksummit.messages.5576 -->`

## 171.26 内核密钥信任网

- 【Linux社区】Konstantin透露kernel.org约600把密钥、拟议三年强制过期将提交用户列表，b4前端将发布仅邮件回环验证的宽松钥匙环，服务器正迁RHEL10。 `<!-- ROW_MINE: ksummit.messages.5582 -->`
