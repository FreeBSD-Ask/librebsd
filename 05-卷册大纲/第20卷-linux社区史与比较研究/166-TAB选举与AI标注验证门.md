# 166 【Linux社区】TAB选举与AI标注验证门

> 来源：ksummit 独有 p30（50 封全读，2023-07 至 2025-08：Rajat Gupta 提出安全提交四道验证门框架 3/4 可全自动 CI 并记录 netdevconf 0x1A 检测 AI 不可能也非目标的维护者共识；Jiri Kosina AI 辅助补丁标注峰会提案原文主张标明哪个 LLM 辅助谁真正理解代码系整条 AI 标注争论源头；comex 系统论证 C 因无泛型无法复制 Rust 类型安全抽象 Option/Result/Arc/Mutex 逐项对比；DAMON 维护者 2023 峰会提案含服务商实测内存占用降约 16% 数据；TAB 选举四封、Bugzilla 争论四封、维护者倦怠三封）
> 判定：44 CAND / 6 NV。主题分布：DAMON技术提案 1、设备直通争论 2、AI辅助审查 1、UMN研究评价 1、TAB选举 2、AI内容政策 1、AI版权争论 1、next树提交流程 2、AI补丁标注 3、面板驱动上游化 2、链接标签之争 3、richACL提案 1、维护者列表分流 2、Bugzilla争论 3、AI验证门提案 1、Rust内核论战 3、stable标签规则 2、UALink上游路径 1、维护者倦怠 3、stable邮件争论 1、sashiko评审 1、Folios议题安排 1、DT绑定争议 1、用户态门槛议题 1、UMN回退评估 1、补丁收件过滤 1、加速器用户态 1、功能进退机制 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p30 的逐封提取（2023-07 至 2025-08，44 CAND / 6 NV），全 28 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 166.1 DAMON技术提案

- 【Linux社区】Park 提议2023峰会分享DAMON进展：某服务商以DAMOS方案降内存占用约16%，议题含ABI工具、DAMOS自调优、分层内存与内存超卖VM管理计划，自2019年历届峰会持续汇报。 `<!-- ROW_MINE: ksummit.messages.4664 -->`

## 166.2 设备直通争论

- 【Linux社区】Pinchart 披露某大型SoC厂商险些开放相机栈，听闻可借直通经其他子系统合入后临阵反悔；Bottomley 主张以商业利益“胡萝卜”而非仅靠GPL等强制手段促厂商开放。 `<!-- ROW_MINE: ksummit.messages.4666 -->`
- 【Linux社区】Ribalda 称现行策略致99%相机市场靠树外驱动、DRM混合模式更可行；Pinchart 要求举出“现代ISP皆命令缓冲”实例，指DRM与V4L2技术差异被夸大，核心在文档与开源用户态要求。 `<!-- ROW_MINE: ksummit.messages.4680 -->`

## 166.3 AI辅助审查

- 【Linux社区】Levin 示范用claude命令行审查tracing补丁，AI正确指出转用hashtable后丢失__read_mostly注解并给出修法，借此论证AI长于审查而非写作且无法律风险。 `<!-- ROW_MINE: ksummit.messages.4670 -->`

## 166.4 UMN研究评价

- 【Linux社区】Kosina 评UMN假提交研究：证明“投入足够精力可暂混入恶意代码”属显而易见，是浪费时间的练习；真正值得研究的是漏洞多久未被察觉等课题。 `<!-- ROW_MINE: ksummit.messages.4672 -->`

## 166.5 TAB选举

- 【Linux社区】Corbet公告2024年TAB选举9月20至27日投票，五席空缺，候选人七人含Amit Shah、Borkmann、Dave Hansen、Kicinski、Cook、Pieralisi、Shuah，LPC周五设TAB答疑会。 `<!-- ROW_MINE: ksummit.messages.4674 -->`
- 【Linux社区】Corbet发布2022年TAB选举细节：9月12至14日CIVS投票，资格须2021年以来3个带tag提交、50个自动获票；届满者Abbott、Brauner、Cook、Mason、Williams，TAB一年工作含UMN善后。 `<!-- ROW_MINE: ksummit.messages.4700 -->`

## 166.6 AI内容政策

- 【Linux社区】Stoakes 主张文档应明确对LLM“垃圾浪潮”可不加容忍地拒收，警告官方政策若显得“欢迎LLM”会被媒体放大，并称Linus“LLM只是工具”言论已被媒体引用。 `<!-- ROW_MINE: ksummit.messages.4676 -->`

## 166.7 AI版权争论

- 【Linux社区】Chehab 反驳AI逐字复制版权风险论：LLM训练来源海量只存高频重复模式，人类凭记忆写“Hello world”同样不知出处，逐字复制概率反低于人照搬教科书。 `<!-- ROW_MINE: ksummit.messages.4679 -->`

## 166.8 next树提交流程

- 【Linux社区】Berg 解释linux-next重复提交检测：同一补丁以不同commit ID进多树会被标记并通知，Pinchart 担忧media子系统cherry-pick其pull request的影响由此可消除。 `<!-- ROW_MINE: ksummit.messages.4681 -->`
- 【Linux社区】Carpenter 建议修复linux-next破坏者应在报告后说明何时合入，因常有人静默修复或额外多测一两天，令测试者无从判断进度。 `<!-- ROW_MINE: ksummit.messages.4690 -->`

## 166.9 AI补丁标注

- 【Linux社区】Pinchart 归纳标注两大目的：助维护者按LLM来源调整审查重点，无需trailer、信任commit说明即可；GPL法律风险则需trailer便于批量列出受影响提交。 `<!-- ROW_MINE: ksummit.messages.4686 -->`
- 【Linux社区】Cook 主张现阶段LLM参与时“宁可过度说明”，trailer标签承载不了，需在commit信息中详述过程，由社区随时间自行淘汰冗余内容。 `<!-- ROW_MINE: ksummit.messages.4716 -->`
- 【Linux社区】Kosina 提出AI标注峰会提案：需以补丁元数据表达“由哪个LLM辅助、谁真正理解代码”，质疑S-O-B链首位约定不够用，并引Pinchart“维护者心中信任分”论LLM放大失职问题。 `<!-- ROW_MINE: ksummit.messages.4737 -->`

## 166.10 面板驱动上游化

- 【Linux社区】Walleij 指面板供应链为DDIC、面板厂、系统厂双层NDA结构，文档难求；提议以需完整gamma校正的Wacom等专业厂商为突破点，并抄送Wacom开发者征询意向。 `<!-- ROW_MINE: ksummit.messages.4689 -->`
- 【Linux社区】Pinchart 指说服传感器厂商的关键在证明开放文档符合其商业利益；Walleij出示nt35510 gamma曲线代码称无datasheet难推进；Armstrong述高通下游超通用面板驱动与碎片化。 `<!-- ROW_MINE: ksummit.messages.4779 -->`

## 166.11 链接标签之争

- 【Linux社区】Bottomley 倡议git am自动把message-id写入commit头（拟新增ATOM_MESSAGEID），主张把争议拆为“自动化追踪”与“人工补充背景”两层，Link标签之争源于混担两职。 `<!-- ROW_MINE: ksummit.messages.4693 -->`
- 【Linux社区】Bottomley 澄清git格式机制：Link可由trailer改为commit头标签，git默认仅打印部分头信息（如AuthorDate），借此兼顾Linus诉求与自动化追踪。 `<!-- ROW_MINE: ksummit.messages.4728 -->`
- 【Linux社区】Ellerman 支持Konstantin的patch.msgid.link域名方案：补丁链接置于行首易辨认、可grep，lore加“# patch”尾注在长message-id时会溢出屏幕。 `<!-- ROW_MINE: ksummit.messages.4732 -->`

## 166.12 richACL提案

- 【Linux社区】Coly Li 探讨AI/LLM负载下的富ACL：指出do_unlinkat先调security_path_unlink、后于vfs_unlink内may_delete，父目录无写权限时安全规则放行删除也无法生效；其公司拟投工程师推上游。 `<!-- ROW_MINE: ksummit.messages.4703 -->`

## 166.13 维护者列表分流

- 【Linux社区】Rostedt 对把MAINTAINERS“THE REST”从LKML改投patches@lists.linux.dev的RFC表态：可接受，但调度器、定时、追踪、中断等核心改动必须仍发LKML。 `<!-- ROW_MINE: ksummit.messages.4710 -->`
- 【Linux社区】Ryabitsev 披露ksummit列表消息残缺系mlmmj-1.4.0rc2缺陷所致，已回滚1.3.0，并称该RFC部分目的是借较大列表测试新版。 `<!-- ROW_MINE: ksummit.messages.4733 -->`

## 166.14 Bugzilla争论

- 【Linux社区】用户Artem列5.19.12上watchdog、ACPI、TPM等无法判断严重性的dmesg报错清单；Takashi归因BIOS缺陷，Geert认为内核多数无法自判，需进一步排查。 `<!-- ROW_MINE: ksummit.messages.4711 -->`
- 【Linux社区】Rostedt 指LKML日均约800封、无人通读（除Corbet与Morton），正确做法是同时抄送维护者与公开列表，使维护者知众目共睹。 `<!-- ROW_MINE: ksummit.messages.4739 -->`
- 【Linux社区】Hemminger 自述为网络类bugzilla默认接收人，只扫垃圾并转发netdev，盼其消亡并断言问题追踪不合社区流程；Leemhuis 引LWN称bugzilla三年无改善、曾近弃用。 `<!-- ROW_MINE: ksummit.messages.4759 -->`

## 166.15 AI验证门提案

- 【Linux社区】Gupta 提四道安全提交验证门（触发崩溃、根因证据、补丁前后对比、自测试），3道可全自动CI化；引netdevconf 0x1A共识“检测AI不可能也非目标，可验证证据才是关键”。 `<!-- ROW_MINE: ksummit.messages.4715 -->`

## 166.16 Rust内核论战

- 【Linux社区】Jung 向Linus解释Rust全局flag用AtomicBool实现，编译器不得二次载入，并发仅经原子操作，C++内存模型按访问理解即可兼顾优化与可靠并发、消除TOCTOU。 `<!-- ROW_MINE: ksummit.messages.4717 -->`
- 【Linux社区】comex 论证C无泛型故无法复制Rust类型安全：逐一对比Option、Result、Arc、Mutex与Clang注解方案，称“安全C”存在表达力鸿沟，bounds-safety仅护越界一隅。 `<!-- ROW_MINE: ksummit.messages.4762 -->`
- 【Linux社区】Overstreet 与Linus辩CPU功耗：RC电机5-10kW/kg仍须高效率否则熔毁，CPU受热与功耗墙约束、看重直线性能；Linus引VLIW数十年失败史与亲历反驳。 `<!-- ROW_MINE: ksummit.messages.4777 -->`

## 166.17 stable标签规则

- 【Linux社区】Carpenter 力挺Fixes: 1da177e4c3f4标签：审查无Fixes的回移须盲审，其五小时回移经历令其默认最坏情形；安全补丁尤需此标签，举Dumazet补丁为例。 `<!-- ROW_MINE: ksummit.messages.4718 -->`
- 【Linux社区】Greg KH 定调stable树第一规则是不给不愿参与的维护者增加负担；多数子系统可opt-out autosel与Fixes自动回移，提交ignore_list即生效，反对惩罚式管理。 `<!-- ROW_MINE: ksummit.messages.4763 -->`

## 166.18 UALink上游路径

- 【Linux社区】Vivi 表态UALink驱动应自首日起设drivers/ualink独立子系统目录，合并流程可暂经DRM或Greg引导，类比drivers/accel管理模式。 `<!-- ROW_MINE: ksummit.messages.4719 -->`

## 166.19 维护者倦怠

- 【Linux社区】Airlie 认可GPU流程长期有效但依仗庞大相邻社区，盼CI接入gitlab.freedesktop并试合并请求；Vetter建议以大会演讲加小会讨论形式介绍网络组分组维护经验。 `<!-- ROW_MINE: ksummit.messages.4720 -->`
- 【Linux社区】Romanovsky 反对匿名反馈方案：子系统贡献者名单稳定且少，维护者能凭内容猜出匿名者，匿名制反而侵蚀信任、无法化解个人恩怨。 `<!-- ROW_MINE: ksummit.messages.4769 -->`
- 【Linux社区】Pinchart 主张财力雄厚者应分摊本职外代码评审；自述两顶帽子：核心维护者重API用法，驱动维护者对大众驱动偏保守，怕破坏且无法全靠自动化测试。 `<!-- ROW_MINE: ksummit.messages.4785 -->`

## 166.20 stable邮件争论

- 【Linux社区】Kosina 质疑全量stable补丁邮件流量价值：检索可走lore/lei；Takashi反驳cherry-pick带fuzz误打时须见原补丁方可核查，Kosina称那需主动校对。 `<!-- ROW_MINE: ksummit.messages.4742 -->`

## 166.21 sashiko评审

- 【Linux社区】Bottomley 起草驱动通用AI指令：硬件默认“可能有bug但不可假定恶意”，修硬件bug须声明具体设备并实测；统计144个子系统信任倾向，已得3个opt-out。 `<!-- ROW_MINE: ksummit.messages.4747 -->`

## 166.22 Folios议题安排

- 【Linux社区】Ts'o 回应Bottomley：承认维护者峰会缺技术人力，Folios宜作LPC周五BoF，LSF/MM停办下可续用Plumbers BBB设施，凡利益相关方认可的场所皆可推进。 `<!-- ROW_MINE: ksummit.messages.4764 -->`

## 166.23 DT绑定争议

- 【Linux社区】Brown 认为“DT即ABI”已广为传播，纠正不合规源文件与托管平台无关，此类分歧靠补文档难解，属人事问题。 `<!-- ROW_MINE: ksummit.messages.4766 -->`

## 166.24 用户态门槛议题

- 【Linux社区】2021维护者峰会拟题UMN复盘与加速器驱动用户态要求（含DMA-BUF准入与EXPORT_SYMBOL_USERSPACE_GPL设想）；Pinchart 愿介绍libcamera与SoC厂商多年桥接经验。 `<!-- ROW_MINE: ksummit.messages.4768 -->`

## 166.25 UMN回退评估

- 【Linux社区】Chehab 称media被回退29补丁均无恶意仅一无效；Romanovsky举证sp8870补丁把清IRQ读返回值误判为错致驱动破坏；Mauro建议弃av7110老旧驱动，Shuah问是否全删。 `<!-- ROW_MINE: ksummit.messages.4776 -->`

## 166.26 补丁收件过滤

- 【Linux社区】Viro 反驳Romanovsky对精挑收件人的批评：60补丁系列56个属fs、4个属arch头文件时，MIPS维护者不应被迫收全系列，为按目录筛选TO/CC辩护。 `<!-- ROW_MINE: ksummit.messages.4789 -->`

## 166.27 加速器用户态

- 【Linux社区】Airlie 断言NPU用户空间无标准化共识（TVM、TensorFlow、PyTorch、Glow、LLVM分支混战），厂商入内核后仍欲全控用户态；反对“只收驱动放手不管”，恐锁死接口难查死锁。 `<!-- ROW_MINE: ksummit.messages.4791 -->`

## 166.28 功能进退机制

- 【Linux社区】Wilcox 反驳“35年仅一例无需立规”：历数文件系统圈Hans Reiser、Merkey、Harrosh、Phillips等纠纷先例，警示复杂政策机制不宜轻立，Lustre等特例也不宜套用加表册。 `<!-- ROW_MINE: ksummit.messages.4795 -->`
