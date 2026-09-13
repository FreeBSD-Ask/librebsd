# 187. Rust 政策三原则提炼、b4 匹配实测与历届 TAB 选举记录（ks p51）

> 来源：ksummit 独有 p51（50 封全读，2025-02 至 2026-08：Pinchart 把 Rust 政策争论提炼为不强制处理 Rust 不得 nack 抽象不得破坏构建三原则最多同时成立两条的矛盾系整场辩论最清晰立场陈述；Ryabitsev 给出 b4 自动化十次错九次实测与六种 Message-ID 匹配失败场景直接催生 patch.msgid.link 域约定；Laura Abbott 2021 TAB 选举完整结果原始记录 1012 名合格投票者 237 投票前五名当选；Ralf Jung 对 Miri 与 C 标准形式化 Cerberus CompCert 与规范哲学系统阐述；Rust 引入讨论六封、Rust 政策讨论四封、峰会存废讨论四封）
> 判定：47 CAND / 3 NV。主题分布：峰会存废讨论 3、TAB选举 2、Rust引入讨论 6、AI审查工具 3、AI补丁标注 1、稳定树回移 2、信任网与PGP 2、THE REST分流 1、linus-next测试 3、next隐藏提交 1、LLM标签与信任 2、设备直通争论 3、AI生成内容规范 2、Rust政策讨论 3、Bugzilla存废 2、Rust形式化验证 2、UMN假补丁事件 1、cleanup.h规则 1、回归追踪 1、补丁接收政策 1、老旧文件系统 1、stable邮件量 1、C内存安全提案 1、安全流程扩展 1、Link标签规范 1。

## 187.1 峰会存废讨论

- 【Linux社区】Greg KH批驳Airlie的DRM合并窗口说：开发者无需停工，只需分清新功能与修复入不同队列；并称DRM树模式致Fixes:标签全错、回归与CVE追踪尽坏，殃及稳定树回移。 `<!-- ROW_MINE: ksummit.messages.7917 -->`
- 【Linux社区】Rostedt认同Rafael所指conclave.rst应急计划：维护者峰会已具正式地位，若大幅改格式须同步修订这份“制定计划的计划”。 `<!-- ROW_MINE: ksummit.messages.7924 -->`
- 【Linux社区】Airlie称AMD与Intel各50至100人跨多团队喂同一驱动，难要求全员理解上游周期；Geert指先合入next再发布有助减少冲突但破坏commit ID唯一性，殃及stable追踪与Fixes:标签。 `<!-- ROW_MINE: ksummit.messages.8025 -->`

## 187.2 TAB选举

- 【Linux社区】Laura Abbott澄清TAB选举投票规则：超50提交者自动获寄选票，3至49提交者须主动申请，承认表述混乱并承诺次年改进流程。 `<!-- ROW_MINE: ksummit.messages.7921 -->`
- 【Linux社区】2021年TAB选举结果：1012名有资格投票者中237人投票，Greg KH、Corbet、Rostedt、Ts'o、Levin当选两年任期，Hansen、Overstreet、Taht落选。 `<!-- ROW_MINE: ksummit.messages.8019 -->`

## 187.3 Rust引入讨论

- 【Linux社区】Belloni审视Rust版PL061与C版反汇编对比，质疑示例关闭溢出检查、rust_helper_readb未内联成函数调用，并指简单驱动才代表多数待转换场景。 `<!-- ROW_MINE: ksummit.messages.7926 -->`
- 【Linux社区】Wedson详解Rust版PL061：编译期边界检查决定writeb与try_writeb取舍、drvdata类型安全免运行时代价、可撤销资源防设备移除后误用、RAII取代goto清理链。 `<!-- ROW_MINE: ksummit.messages.7939 -->`
- 【Linux社区】Leon Romanovsky列第二语言两大代价：跨子系统grep替换式重构变难、CONFIG组合下编译与验证矩阵翻倍；经Walleij解释“整块替换而非第二内核”后表示可以接受。 `<!-- ROW_MINE: ksummit.messages.8008 -->`
- 【Linux社区】Pinchart认为若目标只是RAII等特性C++勉强算替代但弊大于利，Rust是第二语言佳选；惟收益能否抵过开发流程扰动尚待观察，并希望Rust语法当初更贴近C。 `<!-- ROW_MINE: ksummit.messages.8013 -->`
- 【Linux社区】Pinchart部分反驳Linus对C++的否定：析构函数、unique_ptr、类型安全模板对内核有用，但承认C++无真正类型与运行时安全，只盼纯C能拥有带析构的对象。 `<!-- ROW_MINE: ksummit.messages.8016 -->`
- 【Linux社区】Ojeda回应Levin“抽象成孤儿”论：此问题与语言无关且RFC已承认第二语言代价；过渡期由子系统维护者与Rust团队协助重构，长期仍需多数开发者掌握Rust。 `<!-- ROW_MINE: ksummit.messages.8055 -->`

## 187.4 AI审查工具

- 【Linux社区】Gushchin谈Sashiko AI审查：可用自定义提示审查LTS回移，有主线基线噪音更小；多模型并行跑发现阶段1至7可互相协作提质；可查预存缺陷库避免重复上报。 `<!-- ROW_MINE: ksummit.messages.7931 -->`
- 【Linux社区】Mason澄清BPF的AI评审已在GitHub kernel-patches/bpf运行（如PR 9962即评审提示产物）；Rostedt提议把AI挂到patchwork由服务器侧付费运行而非转嫁提交者。 `<!-- ROW_MINE: ksummit.messages.7971 -->`
- 【Linux社区】Bottomley不认同AI审查的专有技术锁定担忧：先例有BitKeeper与Kubernetes的Slack；更可能是AI泡沫破裂投资退潮、开源AI上位；无论如何AI进CI优于压给贡献者。 `<!-- ROW_MINE: ksummit.messages.8032 -->`

## 187.5 AI补丁标注

- 【Linux社区】Tony Luck指当前AI只会按提示在输出上贴“SPDX-License-Identifier: GPL-2.0-only”即自称成功，要确保许可兼容须付费用仅含GPL代码训练的专用模型。 `<!-- ROW_MINE: ksummit.messages.7933 -->`

## 187.6 稳定树回移

- 【Linux社区】Leemhuis提案区分紧急与非紧急回移：稳定树只回移主线存在约两周或到rc4后的修复，扩展Fixes:标签加延时注记，并指补丁系列依赖关系无从识别致回移出错。 `<!-- ROW_MINE: ksummit.messages.7941 -->`
- 【Linux社区】Carpenter实测Link:标签不可靠：抽查首例即v1链接配v3提交；按函数名在lore检索排第44、按作者排第113，感叹逐补丁溯源不可行。 `<!-- ROW_MINE: ksummit.messages.7996 -->`

## 187.7 信任网与PGP

- 【Linux社区】Mauro强调PGP信任网仍用于签git标签请Linus合并，git 2.52.0前标签签名仅允许PGP；kernel.org密钥环约600个密钥，欢迎ssh推送但须有同等信任机制。 `<!-- ROW_MINE: ksummit.messages.7948 -->`
- 【Linux社区】Mauro想换后量子算法主密钥加3至5年有效期可撤销子密钥，但gpg 2.4不支持、升2.5会生成不兼容LibrePGP密钥，远程重建信任网亦难，只能等新版本再动。 `<!-- ROW_MINE: ksummit.messages.7973 -->`

## 187.8 THE REST分流

- 【Linux社区】Bonzini质疑lore存档完整性：lkml下git仓库收不全补丁，也无从过滤非Linux项目的/all/1.git，影响“THE REST”迁出vger的可行性。 `<!-- ROW_MINE: ksummit.messages.7949 -->`

## 187.9 linus-next测试

- 【Linux社区】Bart Van Assche建议把blktests纳入linus-next的LKFT与KernelCI测试，称该套件报出的失败多数最终证明是内核缺陷而非测试自身问题。 `<!-- ROW_MINE: ksummit.messages.7951 -->`
- 【Linux社区】Jiri Kosina回忆当年维护者峰会结论：多数人认为持续投入资源加固linux-next测试不划算，不如在rc1后阶段集中处理失败。 `<!-- ROW_MINE: ksummit.messages.7979 -->`
- 【Linux社区】Rostedt自述urgent与core双分支流程：修Linus树的紧急修复不进linux-next，经约8小时测试后直发PR；若-next反馈更好愿考虑纳入，并支持PR健康检查机器人报告抄送、bake时长与测试失败。 `<!-- ROW_MINE: ksummit.messages.8065 -->`

## 187.10 next隐藏提交

- 【Linux社区】Mark Brown支持子维护者树进linux-next：修复树缺席致-next坏一周会掩盖其他测试结果；多数人乐意入next只是遗忘或不了解，另有封面信附PR未经评审即藏提交的情形。 `<!-- ROW_MINE: ksummit.messages.7954 -->`

## 187.11 LLM标签与信任

- 【Linux社区】Howlett认同Weiner观点：LLM参与度是巨大光谱，二值标签信噪比差且已带污名，无法传递“谁在哪步思考”的真实分工，提交元数据难以承载这些细节。 `<!-- ROW_MINE: ksummit.messages.7958 -->`
- 【Linux社区】Rostedt质疑Kees提议的Debian式贡献者活动仪表盘：可被xz事件式手段刷分操纵，建立信任最终仍靠人与人之间的联系。 `<!-- ROW_MINE: ksummit.messages.7962 -->`

## 187.12 设备直通争论

- 【Linux社区】Pinchart建议设备直通议题改到LPC开专场，因相关专家太多峰会房间装不下；但忧心演成公开争斗，且有些论据不便在开放场合陈述。 `<!-- ROW_MINE: ksummit.messages.7959 -->`
- 【Linux社区】Kosina以hidraw与FIDO令牌反驳直通有害论：libfido2用户态驱动已普及用于kernel.org、Google等认证，生态未碎、无工作流被破坏。 `<!-- ROW_MINE: ksummit.messages.7985 -->`
- 【Linux社区】Figa澄清V4L2有无状态解码器接口，命令缓冲与固定功能两种界面在DRM与V4L2各有取舍；点名Intel IPU6及更新、Qualcomm、MediaTek的ISP原生用命令缓冲。 `<!-- ROW_MINE: ksummit.messages.8038 -->`

## 187.13 AI生成内容规范

- 【Linux社区】Stoakes主张文档明确：LLM使端到端无经验投稿成为可能，明显AI垃圾应可直接拒绝；Williams担心“猎巫”伤社区，Stoakes称只针对极端明显案例。 `<!-- ROW_MINE: ksummit.messages.7967 -->`
- 【Linux社区】Stoakes反驳Carpenter软化草案：能理解并辩护所提交代码是内核评审基本要求；若文档要求“多人仔细审”500个工具生成补丁，等于放弃直接拒绝AI垃圾的立场。 `<!-- ROW_MINE: ksummit.messages.8067 -->`

## 187.14 Rust政策讨论

- 【Linux社区】Boqun Feng称其评审中Rust补丁与C补丁同标准；政策文档讲“子系统如何引入Rust”等更高层内容；并指Jarkko的DMA补丁仅有函数定义级doc测试。 `<!-- ROW_MINE: ksummit.messages.7969 -->`
- 【Linux社区】Pinchart点破“屋里的大象”：不强制维护者处理Rust、不得nack Rust抽象、不得破坏Rust构建三条原则最多同时成立两条，质问社区准备先放弃哪条。 `<!-- ROW_MINE: ksummit.messages.7982 -->`
- 【Linux社区】Ted Ts'o批评Wedson FS幻灯的绑定对C程序员过于复杂，建议改造C侧抽象使Rust绑定易维护可自动生成、新手可更新、热路径少回归，并以“同时解决多问题”作为方向判据。 `<!-- ROW_MINE: ksummit.messages.8069 -->`

## 187.15 Bugzilla存废

- 【Linux社区】Weinberger发布kcontact原型：静态JS网站粘贴内核日志即分析栈回溯，查x86_64全模块预生成符号表映射到子系统L:条目并跳过前3帧入口代码，指引报告去向。 `<!-- ROW_MINE: ksummit.messages.7984 -->`
- 【Linux社区】Tarreau捍卫邮件为内核开发通用语：反驳“邮件在开会一周后失效”，称会议上人们屏幕只有代码、幻灯与邮件，bug报告随邮箱自然可见，bugzilla界面则无人看。 `<!-- ROW_MINE: ksummit.messages.8036 -->`

## 187.16 Rust形式化验证

- 【Linux社区】Ventura Jack问询Rust验证工具现状：Prusti数月无提交，Gillian-Rust未用stacked或tree borrows，RefinedRust复用Miri代码，关注研究原型与实用的距离。 `<!-- ROW_MINE: ksummit.messages.7994 -->`
- 【Linux社区】Jung论证Miri独一无二：C侧仅Cerberus可执行规范但只跑微型示例，C标准歧义致编译器与程序员理解冲突；Rust追求规定性无歧义规范，1.84已悄然启用新trait solver。 `<!-- ROW_MINE: ksummit.messages.8029 -->`

## 187.17 UMN假补丁事件

- 【Linux社区】Mauro披露media子系统29个被回退补丁无恶意代码，仅1个冗余其余有效，质疑盲目回退umn.edu补丁；引Morris称因不知实验范围须审计其全部贡献。 `<!-- ROW_MINE: ksummit.messages.7997 -->`

## 187.18 cleanup.h规则

- 【Linux社区】Bottomley谈__free变量放置：认同在分配处声明可免去空指针释放检查、便于新增早退；并提出以显式作用域块限定变量使用范围，配合scoped_guard处理锁与释放纠缠。 `<!-- ROW_MINE: ksummit.messages.8002 -->`

## 187.19 回归追踪

- 【Linux社区】Leemhuis拟LPC回归专场：KernelCI与regzbot已合并运作，介绍回归追踪现状与计划，并讨论AI时代regzbot是否仍有用、要不要建pending与wip修复树。 `<!-- ROW_MINE: ksummit.messages.8003 -->`

## 187.20 补丁接收政策

- 【Linux社区】Rostedt反对邮件列表强制封面信抄送校验：会破坏quilt工作流，自称、Peter Zijlstra与Andrew Morton皆用quilt；也不愿被稳定补丁封面信抄送。 `<!-- ROW_MINE: ksummit.messages.8006 -->`

## 187.21 老旧文件系统

- 【Linux社区】Hellwig反驳Linus：“别启用”不可行，老旧文件系统支持状态随内核版本变化须内核内标记，syzbot骚扰需统一停报机制；并澄清要去除的是buffer_head整文件I/O助手而非buffer cache。 `<!-- ROW_MINE: ksummit.messages.8017 -->`

## 187.22 stable邮件量

- 【Linux社区】Takashi Iwai为stable抄送邮件辩护：个别补丁经带fuzz的cherry-pick会错打，须见原补丁才能核查，完全过滤将失去这一发现渠道。 `<!-- ROW_MINE: ksummit.messages.8023 -->`

## 187.23 C内存安全提案

- 【Linux社区】Uecker提议仿GCC诊断pragma划区启用内存安全检查，含运行期陷阱的DYNAMIC模式；并展示UBSan插桩后仅当优化器未消除陷阱才告警，可借优化器证明无溢出，已有GCC补丁。 `<!-- ROW_MINE: ksummit.messages.8024 -->`

## 187.24 安全流程扩展

- 【Linux社区】Greg KH披露security@近月已理顺并将获约6个月专人全职经费；LLM仅限本地模型因涉法律约束，AI接入过滤不可行，真正难题是不回应的报告者与横插一手的中间商。 `<!-- ROW_MINE: ksummit.messages.8044 -->`

## 187.25 Link标签规范

- 【Linux社区】Ryabitsev坚持自动化需可靠锚点：b4在作者微调8/10号补丁时十次错九次；列举From与Date被覆盖、误投列表等六种匹配失败场景，提议以patch.msgid.link域或“# patch”注记标示补丁来源。 `<!-- ROW_MINE: ksummit.messages.8060 -->`
