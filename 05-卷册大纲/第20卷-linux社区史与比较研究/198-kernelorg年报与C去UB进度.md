# 198. kernel.org 工具链年报、C 去 UB 进度硬数据与 LKMM 冲突论（ks p62）

> 来源：ksummit 独有 p62（50 封全读，2022-10 至 2025-09：Ryabitsev kernel.org 工具链年度报告一手总结 b4 AI 集成失败教训 AI 爬虫对基础设施冲击 SMTP 持续恶化与废弃 Bugzilla 主张系 2025 年基础设施史核心单篇；ISO C 工作组委员 Uecker 给出硬数据 C23 核心尚有 87 处 UB C2Y 已删 17 处另有 12 项提案并披露 GCC 前端分区域 C 内存安全模式试验；Ralf Jung 从内存模型理论指出 LKMM 依赖机制与 GVN/CSE 基础编译优化根本冲突匹配 LKMM 效率的并发原语仍是未解难题；Levin 给出 kallsyms 嵌入行号完整实测 459 万条目 .rodata +44MiB vmlinux +8.3%；Rust 内核策略论战六封）
> 判定：42 CAND / 8 NV。主题分布：Bugzilla存废之争 3、维护者倦怠与自动化 1、Rust内核策略论战 6、KTODO任务标记 1、fwctl设备直通之争 1、用户态API准入标准 1、Link标签之争 2、琐碎补丁政策 1、AI代码版权责任 2、内核文档工具链 3、C语言RAII手段 1、eBPF接口稳定性 1、kernel.org工具链报告 1、AI审查工具政策 1、Rust早期讨论 1、Rust内核进展 1、栈回溯行号方案 1、静态分析改进 1、补丁发送工具 1、峰会远程参会 1、内存模型与编译器 1、AI生成内容规范 1、AI辅助回迁补丁 1、linus-next集成树 3、LLM标注与合规 1、C语言安全标准化 1、MAINTAINERS列表变革 1、驱动对象生命周期 1、AI时代访问控制 1。

## 198.1 Bugzilla存废之争

- 【Linux社区】Tashkinov称其讥讽被误解，为Bugzilla辩护：邮件无跟踪能力，反对者却提不出可行替代方案，与Pinchart就“侮辱开发者”互斥。 `<!-- ROW_MINE: ksummit.messages.9719 -->`
- 【Linux社区】Pinchart引LWN 904776反驳Rostedt：以“买外接摄像头”回避内置摄像头故障的变通曾令用户极度不满，被忽视的报告未必无关紧要。 `<!-- ROW_MINE: ksummit.messages.9723 -->`
- 【Linux社区】Pinchart指邮件缺缺陷跟踪能力；Leemhuis介绍regzbot借Link标签串联报告与补丁追踪回归，Pinchart称其依赖启发式、盼邮件支持结构化数据。 `<!-- ROW_MINE: ksummit.messages.9790 -->`

## 198.2 维护者倦怠与自动化

- 【Linux社区】Chamberlain细述自动化抗倦怠的前提：Samsung共享裸机与Oracle OCI等硬件资源、Song Liu的eBPF patchwork即时测试、kdevops整合与“要求测试”之辩。 `<!-- ROW_MINE: ksummit.messages.9726 -->`

## 198.3 Rust内核策略论战

- 【Linux社区】Overstreet指Rust不安全层别名规则（tree/stacked borrows）仍未定型，若固化成功可减少spill与reload，令VLIW架构重获实用价值。 `<!-- ROW_MINE: ksummit.messages.9727 -->`
- 【Linux社区】Sakkinen称用Rust测试文档编译DMA补丁却陷入“无测试不放行”境地，指出DMA的doc测试仅为函数定义无法运行，自荐以内核QA为参与第一步。 `<!-- ROW_MINE: ksummit.messages.9733 -->`
- 【Linux社区】Overstreet称bcachefs已有btree核心API的Rust绑定，拟先在debugfs试点；反驳“2034年才可用”说，称数年内新硬件驱动将需要Rust。 `<!-- ROW_MINE: ksummit.messages.9749 -->`
- 【Linux社区】Overstreet回应Linus：Rust的W^X引用保证独占写，仅UnsafeCell边界禁止store加宽；多线程环形缓冲区头尾指针须用原子类型标注。 `<!-- ROW_MINE: ksummit.messages.9755 -->`
- 【Linux社区】Rostedt追问Uecker：若编译器如LTO般可见全程序，能否自行判定跨线程可见性并据此优化，点出全程序优化与内存模型语义的张力。 `<!-- ROW_MINE: ksummit.messages.9768 -->`
- 【Linux社区】Laight抨击Rust读取非0/1的bool即属UB，称语言须如调用约定般精确定义行为，断言bool非硬件类型、实现成本高，不如用int表真假。 `<!-- ROW_MINE: ksummit.messages.9773 -->`

## 198.4 KTODO任务标记

- 【Linux社区】Bird提议为KTODO标记建仪表盘量化技术债存量，自述FIXTHIS前缀经验，并质疑任务完成后KTODO注释应随提交删除以免误导。 `<!-- ROW_MINE: ksummit.messages.9734 -->`

## 198.5 fwctl设备直通之争

- 【Linux社区】Williams为fwctl辩护：区分FPGA比特流式配置面与CXL厂商调试日志命令，承认网络维护者异议不能忽视，邮件信任赤字难解故提议面对面调解。 `<!-- ROW_MINE: ksummit.messages.9735 -->`

## 198.6 用户态API准入标准

- 【Linux社区】Romanovsky主张API须进入发行版软件栈方能扩展，斥HabanaLabs绕过RDMA社区为搭便车；Greg KH反驳厂商都该上游、发行版仅是少数场景，反问门槛何在。 `<!-- ROW_MINE: ksummit.messages.9737 -->`

## 198.7 Link标签之争

- 【Linux社区】Bottomley重申把Link标签之争一分为二：工具自动化追踪用message-id即可，维护者手写背景注释另立，Link兼两职正是争议根源。 `<!-- ROW_MINE: ksummit.messages.9743 -->`
- 【Linux社区】Anvin披露Link标签来历：其原始方案直接放Message-ID被Linus以不可点击否决，折中为kernel.org域名下编码msgid的URL，兼作URN防档案失效。 `<!-- ROW_MINE: ksummit.messages.9799 -->`

## 198.8 琐碎补丁政策

- 【Linux社区】Verkuil说明媒体29个被回退补丁早于pm_runtime_resume_and_get()问世；引Leon方案在__pm_runtime_resume失败时自动递减usage_count，Brown称runtime PM API本就难用。 `<!-- ROW_MINE: ksummit.messages.9753 -->`

## 198.9 AI代码版权责任

- 【Linux社区】Rostedt剖析SoB链版权责任：AI注入侵权代码时提交者与维护者何者担责不明，律师澄清前维护者难免顾虑，透明标注或反成把柄。 `<!-- ROW_MINE: ksummit.messages.9756 -->`
- 【Linux社区】Mauro判断AI生成代码大抵源于公开许可代码（企业禁用公共AI处理私有码），视SoB为授权保证，只要人类把关质量便不介意是否用AI。 `<!-- ROW_MINE: ksummit.messages.9849 -->`

## 198.10 内核文档工具链

- 【Linux社区】Nikula指kernel-doc脚本对头文件重复解析四次，主张改造为可缓存的Python Sphinx扩展，反对预处理RST，忆旧DocBook败于各阶段阻抗失配。 `<!-- ROW_MINE: ksummit.messages.9772 -->`
- 【Linux社区】Ryabitsev以系统管理者立场主张脚本行为可预期：python3脚本应遵循系统默认解释器，自动改选其他版本令人困扰。 `<!-- ROW_MINE: ksummit.messages.9795 -->`
- 【Linux社区】Nikula透露媒体子系统CI已做到W=1零告警构建，询问如何滤除非媒体告警，盼统一要求贡献者修复全部编译警告而非学会忽略。 `<!-- ROW_MINE: ksummit.messages.9848 -->`

## 198.11 C语言RAII手段

- 【Linux社区】Hemminger针对驱动错误路径RAII需求，示范直接以GCC cleanup属性定义_cleanup_free_，认为比Van Assche的错误易发宏方案更简洁。 `<!-- ROW_MINE: ksummit.messages.9776 -->`

## 198.12 eBPF接口稳定性

- 【Linux社区】Rostedt质疑依内核内部信息编写的eBPF程序会形成事实稳定API：多年后维护者改动代码将触发“破坏用户态”条款而被要求回退。 `<!-- ROW_MINE: ksummit.messages.9785 -->`

## 198.13 kernel.org工具链报告

- 【Linux社区】Ryabitsev年度报告：b4普及与AI集成失败教训、AI爬虫冲击、SMTP恶化、lore渐成分布式消息总线、local lore维护者容器、拟废Bugzilla、与OpenSSF重构信任网。 `<!-- ROW_MINE: ksummit.messages.9796 -->`

## 198.14 AI审查工具政策

- 【Linux社区】Torvalds主张AI工具应优先服务维护者而非普通开发者，举安全列表AI垃圾报告与Jens Axboe因AI爬虫放弃自建git服务器为例。 `<!-- ROW_MINE: ksummit.messages.9798 -->`

## 198.15 Rust早期讨论

- 【Linux社区】Wedson以强弱双计数与弱引用升级方案回应引用计数之问；Greg KH追问Rust如何对接dentry/inode/kobject等内核自管计数，称需先见真实驱动。 `<!-- ROW_MINE: ksummit.messages.9800 -->`

## 198.16 Rust内核进展

- 【Linux社区】Ojeda的LPC 2024提案：概述Rust安全抽象与构建系统进展、kernel crate拆分、多版本编译器支持使发行版开箱可用、Linux列入Rust 2024h2目标并进预合并CI。 `<!-- ROW_MINE: ksummit.messages.9803 -->`

## 198.17 栈回溯行号方案

- 【Linux社区】Levin实测kallsyms嵌入源码行号开销：459万条目令.rodata增约44MiB，vmlinux由529MiB至573MiB（+8.3%）；对Babka模块化之议称首次崩溃即可用decode_stacktrace.sh在用户态解码。 `<!-- ROW_MINE: ksummit.messages.9805 -->`

## 198.18 静态分析改进

- 【Linux社区】Pinchart提议为函数加注解标明返回错误码或错误指针，助静态分析识别“if (!ret) return ret;”类反转bug，忆gcc 4.2未初始化告警时代每版皆获真bug。 `<!-- ROW_MINE: ksummit.messages.9814 -->`

## 198.19 补丁发送工具

- 【Linux社区】Anderson推荐源自U-Boot的patman：逐补丁get_maintainer加CC、封面信全员抄送、自动整理版本历史，并转述Olof批评其令大型系列过易发送。 `<!-- ROW_MINE: ksummit.messages.9819 -->`

## 198.20 峰会远程参会

- 【Linux社区】Pinchart主张混合峰会设专人看聊天区转述远程提问；指出工作坊远程参与最大障碍是现场者不用麦克风，须强制执行并增配话筒。 `<!-- ROW_MINE: ksummit.messages.9822 -->`

## 198.21 内存模型与编译器

- 【Linux社区】Jung阐释原子写禁止编译器凭空新增写，指LKMM依赖机制与GVN/CSE等基础优化根本冲突，为优化型语言找到匹配LKMM效率的并发原语仍是未解难题。 `<!-- ROW_MINE: ksummit.messages.9823 -->`

## 198.22 AI生成内容规范

- 【Linux社区】Stoakes坚持指南须开宗明义拒绝AI slop，举Carpenter遇提交者以AI幻觉规格搪塞质询为例，引Postgres的Freund帖警示，并指Linus立场被外界误传。 `<!-- ROW_MINE: ksummit.messages.9828 -->`

## 198.23 AI辅助回迁补丁

- 【Linux社区】Levin估计约八至九成回迁失败仅是上下文冲突或缺依赖，属初级工程师可解、AI能胜任；其余一至两成因子系统大重构，现有AI尚不可托付。 `<!-- ROW_MINE: ksummit.messages.9832 -->`

## 198.24 linus-next集成树

- 【Linux社区】Brown举linus-next脚本首例即绊倒：KVM arm64提交afa9b48f327c未见于lore亦未进-next而Linus照拉，惟其曾埋在邮件列表回复中。 `<!-- ROW_MINE: ksummit.messages.9839 -->`
- 【Linux社区】Torvalds界定所需为Guenter式每_rc跨多架构实机启动的功能测试，每个合并窗口总能揪出数个问题，类比linux-next多架构构建测试的价值。 `<!-- ROW_MINE: ksummit.messages.9862 -->`
- 【Linux社区】McKenney质疑linus-next激励效应：更多测试者既可能倒逼快速修复、也可能令人避之不及，戏言除非Linus拒绝“停留过短”的拉取请求。 `<!-- ROW_MINE: ksummit.messages.9863 -->`

## 198.25 LLM标注与合规

- 【Linux社区】Levin披露Assisted-by详注工具名意在日后审计工具实效，主张按提交质量而非工具论英雄，提AGENTS.md改进合规，并质疑对专有AI工具的真实依赖度。 `<!-- ROW_MINE: ksummit.messages.9842 -->`

## 198.26 C语言安全标准化

- 【Linux社区】Uecker（ISO C工作组委员）称C23核心尚有87处UB、C2Y已除17处另有12项提案，正于GCC前端试验可分区域启用的内存安全模式，呼吁内核社区参与标准化。 `<!-- ROW_MINE: ksummit.messages.9854 -->`

## 198.27 MAINTAINERS列表变革

- 【Linux社区】Perches自述已不订阅LKML、极少参与讨论，仅偶以关键词检索lore并手动下载线程，为“THE REST”迁离vger之议提供资深维护者工作流佐证。 `<!-- ROW_MINE: ksummit.messages.9858 -->`

## 198.28 驱动对象生命周期

- 【Linux社区】Golaszewski提案梳理驱动对象生命周期乱象脉络（Pinchart LPC 2022、其FOSDEM 2023、Sang EOSS 2023），计划分多年多阶段统一子系统对驱动数据的处理。 `<!-- ROW_MINE: ksummit.messages.9872 -->`

## 198.29 AI时代访问控制

- 【Linux社区】Coly Li转达应用团队评估：现以BPF做规则控制、规则持久化繁琐；举AI相册硬链接隐私场景与父目录无写权删除之困，Moore重申LSM只能拒不能授、系有意设计。 `<!-- ROW_MINE: ksummit.messages.9878 -->`
