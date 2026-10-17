# 172 【Linux社区】fwctl征稿与API废弃执行

> 来源：ksummit 独有 p36（50 封全读，2021-04 至 2026-08：Dan Williams fwctl 提案峰会征稿原文系统梳理 /dev/mem、NVMe、CXL 设备直通史实并给慢路径管控方案；Jason Gunthorpe 对 Rust 安全收益数据化质疑要求按周期统计新驱动中 Rust 机会与 C 行数并指收益分布不均才是社会压力根源；Al Viro 以 dma_buf_fd 八处调用点泄漏与 UAF 实例论证 API 废弃执行路径；Liam Howlett 2026 峰会存废改革提案含主题席位双代表与子系统预备会；AI 评审政策五封、加速器用户态四封、维护者峰会存废二封）
> 判定：41 CAND / 9 NV。主题分布：AI评审政策 5、内核文档工具链 3、Rust引入争论 2、设备直通争论 2、UMN事件 1、维护者峰会存废 2、加速器用户态 4、Bugzilla存废 1、C内存安全 1、trivial补丁政策 1、文件系统信任 1、cleanup.h风格 1、API废弃执行 2、MAINTAINERS路由 1、Rust内存模型 2、linus-next测试 1、补丁评审工具 1、Rust安全收益 2、回归处理流程 2、Link标记改革 1、Rust维护者权限 1、stable邮件量 2、Fixes标记语义 1、devres生命周期 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p36 的逐封提取（2021-04 至 2026-08，41 CAND / 9 NV），全 24 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 172.1 AI评审政策

- 【Linux社区】Kozlowski反对把内核编码规则复制进LLM专用提示词，主张先修好kerneldoc与子系统文档让LLM去读，并自述在devicetree列表沉淀“writing bindings”规则供人与AI共用。 `<!-- ROW_MINE: ksummit.messages.5586 -->`
- 【Linux社区】Brown指AI补丁之害在量大且非重复、缺模式匹配红利；引Trond称提交者夸大“安全漏洞”抄送stable逼人停下手头事务，致维护者疲劳。 `<!-- ROW_MINE: ksummit.messages.5615 -->`
- 【Linux社区】Rostedt主张LTS用户应自费支持评审人力，盼可共享的开源内核评审模型，提议既有bug单独公开发而非发给补丁作者，并期待交互模式。 `<!-- ROW_MINE: ksummit.messages.5652 -->`
- 【Linux社区】Rostedt提议把AI评审挂到patchwork由服务器侧运行、成本不落在提交者，并称锁定风险有限；引Pinchart坚持不得强迫提交者运行专有工具。 `<!-- ROW_MINE: ksummit.messages.5675 -->`
- 【Linux社区】Williams主张提交说明应交代假设与取舍，视“不愿为补丁现状辩护”为信任警示；引Cook称“如何构造此方案”难以浓缩为trailer标签。 `<!-- ROW_MINE: ksummit.messages.5724 -->`

## 172.2 内核文档工具链

- 【Linux社区】Ted以LaTeX两遍编译类比intersphinx须两遍构建生成objects.inv，追问单本书单遍构建是否够编辑自查，并建议提供可下载的库存文件。 `<!-- ROW_MINE: ksummit.messages.5589 -->`
- 【Linux社区】Corbet确认kernel.org文档站搜索框可按符号定位，指出system_state仅在编码风格文档出现一次，坦言未考察过无浏览器访问方式。 `<!-- ROW_MINE: ksummit.messages.5613 -->`
- 【Linux社区】Nikula指出kernel-doc脚本对同一头文件重复解析四次，主张改写为带缓存的Sphinx扩展（如Hawkmoth），并链接Sphinx域命名空间修复。 `<!-- ROW_MINE: ksummit.messages.5701 -->`

## 172.3 Rust引入争论

- 【Linux社区】Walleij赞同Bottomley“惰性癌症”论，引帕金森定律“阻碍时代”之说，直言“Rust很好，合并试试”，并担心内核对年轻人失去吸引力、成包容性问题。 `<!-- ROW_MINE: ksummit.messages.5590 -->`
- 【Linux社区】Torvalds断言C++仍非好语言：不解决C的安全问题反添设计缺陷，new关键字既违命名又依赖内核不可用的异常处理，不值得再费心兼容。 `<!-- ROW_MINE: ksummit.messages.5659 -->`

## 172.4 设备直通争论

- 【Linux社区】Pinchart主张内核须校验可引发DMA的命令，开放度最终靠信任与违约后果（援引明尼苏达封禁先例），要求厂商开放几乎全部ISP特性及调参文档。 `<!-- ROW_MINE: ksummit.messages.5591 -->`
- 【Linux社区】Dan Williams提案峰会讨论fwctl：细数/dev/mem、pci-sysfs、USB raw、NVMe直通史实，指CXL禁专属命令收效差，主张管控慢路径配置面。 `<!-- ROW_MINE: ksummit.messages.5606 -->`

## 172.5 UMN事件

- 【Linux社区】hpa断言未经许可渗透测试不道德且常属违法；引文载Hellwig称UMN实验当获荣誉勋章、Figa主张应有社区监督，呈现制裁争论两极。 `<!-- ROW_MINE: ksummit.messages.5592 -->`

## 172.6 维护者峰会存废

- 【Linux社区】Stoakes指峰会“宣传为X实为Y”、议程征集形同虚设；引Airlie称其为“Linus的员工例会”并反对按MAINTAINERS条目投票定议题。 `<!-- ROW_MINE: ksummit.messages.5595 -->`
- 【Linux社区】Howlett以未与会者身份指人选集中于“老面孔”，提议按主题设临时席位、每子系统双代表、会前预备会与反馈环、代行人机制。 `<!-- ROW_MINE: ksummit.messages.5631 -->`

## 172.7 加速器用户态

- 【Linux社区】Arnd区分固定功能与可编程接口，主张GEMM或oneDNN类抽象可作内核固定功能入口，并指出这将把开源用户态问题转化为开源固件问题。 `<!-- ROW_MINE: ksummit.messages.5597 -->`
- 【Linux社区】Pinchart质疑“必须进发行版包”标准是否适配存量极少的设备，举车载dewarp引擎无标准API，主张先收特定设备的开放实现、日后再成框架。 `<!-- ROW_MINE: ksummit.messages.5716 -->`
- 【Linux社区】Chehab认可“一个开放用户态真实应用”即可作准入，承认厂商藏私技术无法根绝，主张以政策促整改乃至移除违规驱动并封禁厂商。 `<!-- ROW_MINE: ksummit.messages.5718 -->`
- 【Linux社区】Pinchart回溯OMAP3公开数据手册、IPU3参数blob头文件不足以驱动、树莓派ISP开放用户态获赞，据libcamera两年半经验主张要求真实用例的开放实现。 `<!-- ROW_MINE: ksummit.messages.5727 -->`

## 172.8 Bugzilla存废

- 【Linux社区】用户Artem自述lore界面“令人恐惧”，连问开放议题、状态、指派如何查，扬言若删Bugzilla绝不用lore，呈现普通用户视角的真实阻力。 `<!-- ROW_MINE: ksummit.messages.5609 -->`

## 172.9 C内存安全

- 【Linux社区】引文载Uecker拟在GCC试验C内存安全子集、Stitt已建size_t溢出消毒器与wrapping_ok宏，Carpenter提saturate_math饱和宏；hpa称此类事C++易做而C需编译器扩展。 `<!-- ROW_MINE: ksummit.messages.5618 -->`

## 172.10 trivial补丁政策

- 【Linux社区】Van Assche反对复活trivial树，称不愿另盯一份列表核对块层与SCSI补丁的注释是否被改错，主张琐碎补丁留在各子系统列表。 `<!-- ROW_MINE: ksummit.messages.5626 -->`

## 172.11 文件系统信任

- 【Linux社区】Kosina以“把U盘文档直接在LibreOffice打开必然用mmap”反驳Torvalds“FAT只作数据传输不需mmap”之说，维护完整文件系统实现标准。 `<!-- ROW_MINE: ksummit.messages.5638 -->`

## 172.12 cleanup.h风格

- 【Linux社区】Bottomley主张变量生存期小于代码块时可用显式作用域块承载__free变量，类比guard与scoped_guard之择，认可变量活到末尾返回时改用内部声明。 `<!-- ROW_MINE: ksummit.messages.5644 -->`

## 172.13 API废弃执行

- 【Linux社区】Viro列举dma_buf_fd八处调用约定互异且多处泄漏或UAF，主张替换API应在成败两途都吞引用，或定期全树排查并经porting.rst过渡后拔除。 `<!-- ROW_MINE: ksummit.messages.5646 -->`
- 【Linux社区】Golaszewski自述接手GPIO时新旧API已并存，列出TODO条目、技术债演讲与多批descriptor转换补丁，说明无集中清单、进展散见各系列。 `<!-- ROW_MINE: ksummit.messages.5668 -->`

## 172.14 MAINTAINERS路由

- 【Linux社区】Torvalds赞成后端自动汇聚补丁成patches@lists.linux.dev，并提出按文件模式订阅的“虚拟列表”，使感兴趣者自动收到相关补丁。 `<!-- ROW_MINE: ksummit.messages.5665 -->`

## 172.15 Rust内存模型

- 【Linux社区】Torvalds称所论主要在unsafe与C互操作，Rust全局旗标语法若靠accessor遮掩不如继续写C，并讥C++内存序“标准混乱、代码难读”。 `<!-- ROW_MINE: ksummit.messages.5680 -->`
- 【Linux社区】Feng释疑WRITE_ONCE即relaxed原子写、内核原子操作并无编译器屏障，举smp_store_release发布后WRITE_ONCE例证r1可为0或1，驳Overstreet顾虑。 `<!-- ROW_MINE: ksummit.messages.5736 -->`

## 172.16 linus-next测试

- 【Linux社区】Geert在确认Rostedt流程完备后指出linux-next仍可捕获冷门架构与配置的编译失败，如间接包含头所致问题。 `<!-- ROW_MINE: ksummit.messages.5683 -->`

## 172.17 补丁评审工具

- 【Linux社区】Bottomley称Gerrit之弊在改变工作流而非界面，建议为lore加Gerrit式前端做行内评论转换，称可用AI快速实现并交Ryabitsev部署。 `<!-- ROW_MINE: ksummit.messages.5684 -->`

## 172.18 Rust安全收益

- 【Linux社区】Gunthorpe请求按周期统计各子系统新驱动中Rust机会与C行数，判断安全收益占比小，称服务器领域鲜有绿地驱动，须如binder般重写存量方能成立。 `<!-- ROW_MINE: ksummit.messages.5686 -->`
- 【Linux社区】Van Assche称终极目标为运行前证明代码正确，须形式化规约与硬件模型而超出Rust范围，举DMA误配、提权、log4shell为语言不设防之例。 `<!-- ROW_MINE: ksummit.messages.5702 -->`

## 172.19 回归处理流程

- 【Linux社区】Leemhuis给出四项峰会提案链接，并称其回归追踪专用账号若少打扰某子系统，即说明该处流程无恙。 `<!-- ROW_MINE: ksummit.messages.5689 -->`
- 【Linux社区】Leemhuis拟成文回归处理规则并求Linus或核心维护者背书，指次级子系统维护者远离Linus不谙其规，转引Laurent提议办维护者培训。 `<!-- ROW_MINE: ksummit.messages.5730 -->`

## 172.20 Link标记改革

- 【Linux社区】Desnoyers剖析Link截记实为补丁多版本缺唯一标识的变通，对比Gerrit Change-Id语义，指出Linus不信其价值而工具派重视，期待Ryabitsev方案。 `<!-- ROW_MINE: ksummit.messages.5703 -->`

## 172.21 Rust维护者权限

- 【Linux社区】Rostedt主张内核内API用途由维护者定义，异于用户态“既发布即担责”原则，自述tracing头文件暴露内部结构并要求有权禁止滥用。 `<!-- ROW_MINE: ksummit.messages.5704 -->`

## 172.22 stable邮件量

- 【Linux社区】Iwai指出补丁偶因cherry-pick带模糊合入出错而须查验全文，建议摘要邮件列出无法无模糊应用的提交以便核验，回应lore/lei可替代论。 `<!-- ROW_MINE: ksummit.messages.5705 -->`
- 【Linux社区】转引Kosina称stable抄送邮件量大到无法有效利用、宜改可选订阅，Bottomley建议统一X-Stable头便于过滤，Levin追问是否已有无头之邮。 `<!-- ROW_MINE: ksummit.messages.5710 -->`

## 172.23 Fixes标记语义

- 【Linux社区】Rostedt释义Fixes不带Cc stable可仅示改进或风险大不回移，述user events修复被Linus以非回归为由拒收，分辨发行版与稳定性两种回移观。 `<!-- ROW_MINE: ksummit.messages.5706 -->`

## 172.24 devres生命周期

- 【Linux社区】转引Brown称devres应用极广、Bottomley提议延迟释放至模块卸载以解中断回调问题，Greg KH点破症结在模块与设备结构生存期被混淆。 `<!-- ROW_MINE: ksummit.messages.5708 -->`
