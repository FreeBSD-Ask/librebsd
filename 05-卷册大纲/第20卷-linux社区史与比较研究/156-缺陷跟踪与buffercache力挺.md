# 156 【Linux社区】缺陷跟踪与buffercache力挺

> 来源：ksummit 独有 p20（50 封全读，2021-04 至 2026-08：MAINTAINERS B: 行 70 条分类统计与 bugzilla 三年无起色、Leemhuis regzbot 重启；Linus 力挺 buffer cache 引 Unix v6《Lions' Commentary on UNIX 6th Edition》渊源与 20 余旧文件系统清单；Linus 反汇编实证 cleanup.h DEFINE_FREE 省略 kfree(NULL) 并论可读性优先；Pinchart 披露大 SoC 厂因直通空白支票在最后关头放弃开放相机栈；fwctl ABI 边界、维护者倦怠与发布节奏、AI 使用政策与标注 DCO 冲突、Rust ftrace/所有权/GCC 后端、hfsplus 工具现状）
> 判定：43 CAND / 7 NV。主题分布：AI使用政策 1、邮件列表投递工具 1、TAB选举 1、编码风格规则 1、cleanup.h优化 1、AI审阅自动化 1、Rust ftrace支持 1、发布节奏与倦怠 1、封面信Cc策略 1、协作文档工具 1、反对预生成文件 1、DRM运行时失败 1、THE REST迁移 1、kernel-doc性能 1、sashiko信任模型 1、维护者倦怠 2、Rust所有权模型 1、fwctl ABI边界 2、内核malloc讨论 1、Web of Trust工具 1、保密漏洞通报 1、CI门禁之辩 1、AUTOSEL与stable 1、Rust驱动测试 1、AI标注与DCO 1、缺陷跟踪工具 2、付费文档失败 1、缓冲缓存辩护 1、Rust对比C++ 1、旧文件系统维护 1、Android更新与CRA 1、Rust GCC后端 1、损坏文件系统判定 1、直通与闭源驱动 1、维护者培养路径 1、hfsplus工具现状 1、回归修复时限 1、C聚合传参 1、linus-next测试 1、linux-next合并策略 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p20 的逐封提取（2021-04 至 2026-08，43 CAND / 7 NV），全 40 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 156.1 AI使用政策

- 【Linux社区】Lorenzo支持用AI查找难察觉问题、整理代码并帮非英语母语者润色注释，反对一刀切“禁AI”，主张细粒度披露规则。 `<!-- ROW_MINE: ksummit.messages.3048 -->`

## 156.2 邮件列表投递工具

- 【Linux社区】Kicinski向新人推荐lei订阅netdev子集，认为POP3拉取比SMTP订阅更稳，愿劝“永不打开的gmail文件夹”订阅者迁移。 `<!-- ROW_MINE: ksummit.messages.3064 -->`

## 156.3 TAB选举

- 【Linux社区】2024年TAB选举11人获提名（含Dave Hansen、Kees Cook、Miguel Ojeda、Shuah Khan等），CIVS投票至9月27日。 `<!-- ROW_MINE: ksummit.messages.3069 -->`

## 156.4 编码风格规则

- 【Linux社区】Dobriyan称头文件排序规则无意义但无害、重复包含靠工具即可查，而初始化器排序影响代码生成、此类规则可能有害。 `<!-- ROW_MINE: ksummit.messages.3071 -->`

## 156.5 cleanup.h优化

- 【Linux社区】Linus反汇编证实编译器能省略kfree(NULL)，归功cleanup.h中DEFINE_FREE内联“if (_T)”写法（PeterZ等设计），强调首要目标是人类可读。 `<!-- ROW_MINE: ksummit.messages.3072 -->`

## 156.6 AI审阅自动化

- 【Linux社区】Mason赞同由0-day机器人统一跑checkpatch与AI测试建立基线，维护者获益明显；指出AI推理不免费，需云厂商捐赠算力。 `<!-- ROW_MINE: ksummit.messages.3074 -->`

## 156.7 Rust ftrace支持

- 【Linux社区】Ojeda答复Rostedt：Rust已有mcount支持（PR 57220），fentry仍为开放issue（#55092）；基于LLVM，Clang能做的rustc亦可。 `<!-- ROW_MINE: ksummit.messages.3083 -->`

## 156.8 发布节奏与倦怠

- 【Linux社区】Kicinski为2023峰会提议议题：发布流程时机影响维护者安排离线休息的能力，指向倦怠问题。 `<!-- ROW_MINE: ksummit.messages.3084 -->`

## 156.9 封面信Cc策略

- 【Linux社区】Leon引Mauro实测：umn.edu撤销系列（190补丁）封面信自动生成221个Cc必被判垃圾邮件；并指RDMA撤销应Cc Gunthorpe与Ledford。 `<!-- ROW_MINE: ksummit.messages.3096 -->`

## 156.10 协作文档工具

- 【Linux社区】Bottomley主张用“活文档”记录folio设计目标、各方关切与补丁状态，ack仍由作者经公共列表收集，非文档代收。 `<!-- ROW_MINE: ksummit.messages.3100 -->`

## 156.11 反对预生成文件

- 【Linux社区】Linus反对提交预生成flex/bison产物，称曾致版本地狱；引833e62245943、29c833061c1d（Kconfig）与e039139be8c2（dtc）为证。 `<!-- ROW_MINE: ksummit.messages.3101 -->`

## 156.12 DRM运行时失败

- 【Linux社区】Baryshkov峰会提议：DRM显示管线回调不应失败，而嵌入式多组件设备须调用clk/phy/pm_runtime等可失败设置，滋生易错代码，求不破API的方案。 `<!-- ROW_MINE: ksummit.messages.3102 -->`

## 156.13 THE REST迁移

- 【Linux社区】Perches指若“THE REST”迁出LKML，MAINTAINERS中约80个标注linux-kernel@的小节多非核心、过半应一并移除（附grep清单）。 `<!-- ROW_MINE: ksummit.messages.3106 -->`

## 156.14 kernel-doc性能

- 【Linux社区】Brown实测kernel-doc . --none -Wall约需90秒，与Mauro机器python3.13的31.7秒形成跨环境对比。 `<!-- ROW_MINE: ksummit.messages.3107 -->`

## 156.15 sashiko信任模型

- 【Linux社区】Berg反对默认信任硬件：wifi“硬件”多为固件、多缺陷且可遭空中攻击，主张需信任设备的高性能场景改为显式opt-out。 `<!-- ROW_MINE: ksummit.messages.3108 -->`

## 156.16 维护者倦怠

- 【Linux社区】Bacik称自动化仅解部分问题，主张汇聚经验形成最佳实践；指出维护已成主业，需可持续模式并降低新维护者上手门槛。 `<!-- ROW_MINE: ksummit.messages.3109 -->`
- 【Linux社区】Bottomley峰会提案：请资深维护者分享应对压力的真实策略（公司压力、CVE与syzbot洪流），破除“独自硬扛”心理。 `<!-- ROW_MINE: ksummit.messages.3112 -->`

## 156.17 Rust所有权模型

- 【Linux社区】Ojeda向Greg澄清：kref与Ref<T>均无需锁，Rust价值在把Doc/kref.txt规则变成编译期强制；若Rust自管对象可绕开devm_*与自引用结构。 `<!-- ROW_MINE: ksummit.messages.3114 -->`

## 156.18 fwctl ABI边界

- 【Linux社区】Gunthorpe称fwctl应接管内核与用户态可共享的操作（如重启生效的功能开关），不得劫持内核scrubber；单一全局擦除器动态控制是不佳匹配。 `<!-- ROW_MINE: ksummit.messages.3118 -->`
- 【Linux社区】Cameron赞同fwctl目标但忧ABI：以CXL Patrol Scrub为例，EDAC RAS扩展提案在推，恐fwctl暴露与之冲突，列三种处置选项求明确政策。 `<!-- ROW_MINE: ksummit.messages.3175 -->`

## 156.19 内核malloc讨论

- 【Linux社区】Brown指kzalloc(GFP_KERNEL)实际承担通用分配职责，多数调用并非深思熟虑的分配器选型，支持提供易用malloc的需求。 `<!-- ROW_MINE: ksummit.messages.3120 -->`

## 156.20 Web of Trust工具

- 【Linux社区】Ryabitsev解释kernel.org信任网工具：OpenSSF资助的安全开发者与他和Greg共同迭代，先满足关键用户需求再发0.1广泛征求意见。 `<!-- ROW_MINE: ksummit.messages.3123 -->`

## 156.21 保密漏洞通报

- 【Linux社区】Wilk代表Oracle表态愿出资雇佣专人承担向linux-distros通报已修复漏洞的“吃力不讨好”工作并协助安全修复。 `<!-- ROW_MINE: ksummit.messages.3130 -->`

## 156.22 CI门禁之辩

- 【Linux社区】Brown称CI须结果稳健、及时且可理解，主张提供结果供参考而非硬性门禁，全红时可不进入人工评审。 `<!-- ROW_MINE: ksummit.messages.3132 -->`

## 156.23 AUTOSEL与stable

- 【Linux社区】Torokhov仍为确需进stable的修复手工Cc，但认AUTOSEL选得过多，建议忽略Fixes早于约两年的提交的自动回移。 `<!-- ROW_MINE: ksummit.messages.3135 -->`

## 156.24 Rust驱动测试

- 【Linux社区】Cameron自述用qemu模拟spi/gpio测试IIO驱动，仿真代码一次性质量未上游化，开发周期快，愿分享ad7280a测试环境。 `<!-- ROW_MINE: ksummit.messages.3141 -->`

## 156.25 AI标注与DCO

- 【Linux社区】McKenney指AI辅助不同于coccinelle等工具，可能连编译都不做；并提醒依训练数据不同或难满足DCO 1.1(a)的许可权利声明。 `<!-- ROW_MINE: ksummit.messages.3151 -->`

## 156.26 缺陷跟踪工具

- 【Linux社区】Pinchart指邮件缺乏“跟踪”能力，public-inbox/b4/lei无法追踪bug状态；Patchwork之于补丁同理，梦想邮件支持结构化数据。 `<!-- ROW_MINE: ksummit.messages.3153 -->`
- 【Linux社区】Leemhuis统计MAINTAINERS的B:行70条（bugzilla 23、github 17、gitlab 11、mailto 12），称bugzilla三年无起色，质疑内核是否需统一缺陷跟踪；regzbot重启。 `<!-- ROW_MINE: ksummit.messages.3160 -->`

## 156.27 付费文档失败

- 【Linux社区】Corbet复盘LF出资付费文档实验失败：选题过难、写手连C基础都需讲解；根因是懂领域者写代码收入更高。 `<!-- ROW_MINE: ksummit.messages.3154 -->`

## 156.28 缓冲缓存辩护

- 【Linux社区】Linus力挺buffer cache：源自Unix v6（《Lions' Commentary on UNIX 6th Edition》），简单自包含，服务ext2、fat、isofs等20余旧文件系统，对外影响近乎零，驳斥废除论。 `<!-- ROW_MINE: ksummit.messages.3156 -->`

## 156.29 Rust对比C++

- 【Linux社区】Ojeda举例C++20 std::span指向局部变量即UB且clang/gcc均不告警，称UB在C/C++依旧易犯，Rust可避免；有Rust则选C++意义不大。 `<!-- ROW_MINE: ksummit.messages.3164 -->`

## 156.30 旧文件系统维护

- 【Linux社区】Chinner回应Kent“用户态跑现有文件系统”设想：lklfuse（github.com/lkl/linux，基于6.1）已能把内核文件系统实现作FUSE运行。 `<!-- ROW_MINE: ksummit.messages.3166 -->`

## 156.31 Android更新与CRA

- 【Linux社区】Suchánek指Android安全难题在厂商不提供更新、用户困于旧系统；Greg称欧盟已立法要求移动设备多年更新，双方认为CRA或改善现状。 `<!-- ROW_MINE: ksummit.messages.3172 -->`

## 156.32 Rust GCC后端

- 【Linux社区】Ojeda谈rustc_codegen_gcc尚早：每内核版只支持单一rustc、补丁GCC或仅支持最新版、libgccjit稳定性未知；并乐见Rust工具链上kernel.org。 `<!-- ROW_MINE: ksummit.messages.3180 -->`

## 156.33 损坏文件系统判定

- 【Linux社区】Roeck实测ntfsv3建挂拷删循环数秒即损坏、卸载常崩溃，质询何种程度应标BROKEN。 `<!-- ROW_MINE: ksummit.messages.3182 -->`

## 156.34 直通与闭源驱动

- 【Linux社区】Pinchart亲历某大SoC厂因可借直通“空白支票”换道合入而在最后关头放弃开放相机栈；称逆向愈发困难、市场力难覆盖小众设备；引DRM要求开源用户态先例。 `<!-- ROW_MINE: ksummit.messages.3183 -->`

## 156.35 维护者培养路径

- 【Linux社区】Rostedt倡导师徒制培养维护者：已带Bristot、Hiramatsu，分享脚本、PR与linux-next流程及-rc期禁忌；指现行靠试错应制度化。 `<!-- ROW_MINE: ksummit.messages.3184 -->`

## 156.36 hfsplus工具现状

- 【Linux社区】Hellwig更正前提：John Paul Adrian Glaubitz在停摆七年后复活hfsprogs包，hfsplus测试工具并非全无。 `<!-- ROW_MINE: ksummit.messages.3185 -->`

## 156.37 回归修复时限

- 【Linux社区】Leemhuis澄清“下周日前修复”非要求周末加班，而是配合Linus周日发-rc的节奏，宜周五前合入；建议措辞改为“本周内”。 `<!-- ROW_MINE: ksummit.messages.3186 -->`

## 156.38 C聚合传参

- 【Linux社区】Pinchart举std::string按值传递加move可省一次堆分配，聚合传值效率视用法而定；指出对成员std::move返回会阻止NRVO。 `<!-- ROW_MINE: ksummit.messages.3188 -->`

## 156.39 linus-next测试

- 【Linux社区】Baerts问询linus-next运作：Sasha称80%自动化（lei抓取PR邮件）、遭NACK即回滚合并，LKFT与KernelCI在测；Matt忧仪表盘缺“可拉取”总指示。 `<!-- ROW_MINE: ksummit.messages.3190 -->`

## 156.40 linux-next合并策略

- 【Linux社区】Kleine-König提议两两成对合并子系统树（先B+C再D+E）而非依次合并，便于在含B的中间树上测试；自认收益未必抵成本。 `<!-- ROW_MINE: ksummit.messages.3191 -->`
