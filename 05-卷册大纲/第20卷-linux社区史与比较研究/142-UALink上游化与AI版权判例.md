142 【Linux社区】UALink上游化与AI版权判例

> 来源：ksummit 独有 p7（50 封全读，2021-04 至 2026-08，UALink 驱动三封路线之争（drivers/ual 第一天正式提交 vs misc 轻量起步 vs Greg/DRM 代管）、Bartz/Kadrey 判例 AI 版权三选项、security@ 获 6 个月全职资助与 LLM 分诊行不通论、Tree Borrows 满足 LLVM noalias 约束、老旧文件系统只读最低支持线、GPIO 数千处遗留调用全局重构呼吁、修复滞后数周至两月峰会提案总纲）
> 判定：44 CAND / 6 NV。主题分布：老旧文件系统维护 2、工具生成内容指南 4、stable邮件量 1、cleanup.h变量放置规则 1、Bugzilla改进 2、C聚合值传递 1、邮件列表文档补丁 1、-Werror与旧内核编译 1、UALink驱动上游化 4、Link标签最佳实践 1、维护者倦怠与匿名评审 1、malloc提案 2、LLM评审工具依赖 1、AI产出版权 1、kallsyms行号信息 1、Rust别名模型 2、回归修复滞后场景 1、AI评审工具 2、C聚合与C++26 1、设备直通之争 2、维护者峰会存废 1、驱动probe失败议题 1、trivial补丁政策 1、安全流程扩展 1、峰会2021形式 1、Rust内核政策 2、安全议题embargo 1、新开发者洪流 1、C安全属性机制 1、Rust for Linux 1、API弃用执行 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p7 的逐封提取（2021-04 至 2026-08，44 CAND / 6 NV），全 31 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 142.1 老旧文件系统维护

- 【Linux社区】主张老旧文件系统不能一删了之，指出QEMU已弃用i440fx故虚拟化非万能药；建议降低志愿者贡献门槛，并让云厂商分担syzbot报告分诊压力。 `<!-- ROW_MINE: ksummit.messages.993 -->`
- 【Linux社区】提议以只读为最低支持线：便于取回旧数据且无需新特性更新，回应Chinner“只读仍在ring 0解析不可信数据”的安全顾虑。 `<!-- ROW_MINE: ksummit.messages.1099 -->`

## 142.2 工具生成内容指南

- 【Linux社区】决策记录：Corbet宣布该指南文档补丁已就绪并由其正式应用合入。 `<!-- ROW_MINE: ksummit.messages.995 -->`
- 【Linux社区】单句反驳Linus“AI无需特殊对待”论：新意在于AI能从零批量生成代码，而非仅做机械转换。 `<!-- ROW_MINE: ksummit.messages.1007 -->`
- 【Linux社区】以网络子系统为例反驳“AI是新问题”：无专长者投递早已有之，自己对疑似slop作者整批拒绝但留一封教其入门，LLM与checkpatch同类。 `<!-- ROW_MINE: ksummit.messages.1040 -->`
- 【Linux社区】流程问询：追问v3文档补丁状态与应走哪棵树，同页Dave回应确认未弃置、将出后续版本。 `<!-- ROW_MINE: ksummit.messages.1081 -->`

## 142.3 stable邮件量

- 【Linux社区】赞同Sasha的汇总邮件方案，建议再把回移范围写进正文，便于一眼看出回移不到位之处。 `<!-- ROW_MINE: ksummit.messages.998 -->`

## 142.4 cleanup.h变量放置规则

- 【Linux社区】讨论显式作用域块可读性：变量作用域小于两侧代码才宜用块，若活到函数末返回则内部声明更合理，类比for循环初始化。 `<!-- ROW_MINE: ksummit.messages.1003 -->`

## 142.5 Bugzilla改进

- 【Linux社区】反驳Willy：核心问题是注意力，邮件在出差一周后即失效；邮件跟进需知References头且须先订阅列表，对多数人不可行。 `<!-- ROW_MINE: ksummit.messages.1004 -->`
- 【Linux社区】流程立场：Fedora式按版本自动关闭陈旧bug“烦人多于收益”，但若成社区共识愿意实现。 `<!-- ROW_MINE: ksummit.messages.1020 -->`

## 142.6 C聚合值传递

- 【Linux社区】详解C++按值传聚合需调用拷贝运算符与析构且有悬挂指针陷阱；指出聚合返回一律经隐藏指针，而u64/u128却可用寄存器对返回。 `<!-- ROW_MINE: ksummit.messages.1009 -->`

## 142.7 邮件列表文档补丁

- 【Linux社区】评审意见：更倾向用“origin”而非“provenance”，并确认v1给出的Ack与R-b继续有效。 `<!-- ROW_MINE: ksummit.messages.1013 -->`

## 142.8 -Werror与旧内核编译

- 【Linux社区】反驳改GCC的提议：约30个Makefile打补丁即可解决，编译器不应替内核收拾自身问题；建议用CONFIG_WERROR或shell包装编译器。 `<!-- ROW_MINE: ksummit.messages.1014 -->`

## 142.9 UALink驱动上游化

- 【Linux社区】维护者立场：应从一开始就按正式子系统drivers/ual提交，避免不必要的评审返工。 `<!-- ROW_MINE: ksummit.messages.1019 -->`
- 【Linux社区】流程承诺：优先完成清理使RFC骨架在12月前发出征求意见，并将改用正式SMTP配置发信。 `<!-- ROW_MINE: ksummit.messages.1037 -->`
- 【Linux社区】建议从第一天就建独立子系统drivers/ualink，初期可由Greg或DRM子维护者代管，如同drivers/accel的模式。 `<!-- ROW_MINE: ksummit.messages.1042 -->`
- 【Linux社区】回应Linus：初期RFC拟放drivers/misc轻量起步，认同UALink应像CXL一样自成子系统，长期归drivers/ual。 `<!-- ROW_MINE: ksummit.messages.1047 -->`

## 142.10 Link标签最佳实践

- 【Linux社区】补丁本体：规定lore链接的方括号编号记法，何时用patch.msgid.link域标示补丁出处，供自动化工具识别原始提交。 `<!-- ROW_MINE: ksummit.messages.1022 -->`

## 142.11 维护者倦怠与匿名评审

- 【Linux社区】反对匿名反馈：匿名评审只会招致负面评价并侵蚀信任，维护者无法向不知名的批评者解释和调整。 `<!-- ROW_MINE: ksummit.messages.1023 -->`

## 142.12 malloc提案

- 【Linux社区】反对照搬1970年代malloc：内核各内存API各有碎片化/性能/失败属性须保留；KASAN开销过高，无法取代red zone等防护。 `<!-- ROW_MINE: ksummit.messages.1028 -->`
- 【Linux社区】反驳hpa：Rust侧分配器早已正常处理GFP标志，追问现行方案到底缺什么。 `<!-- ROW_MINE: ksummit.messages.1066 -->`

## 142.13 LLM评审工具依赖

- 【Linux社区】以ext4为例：过去靠24 VM小时fstests（每次约2美元谷歌VM时）兜底，Sashiko同理但均不能替代人类评审，警惕评审能力退化。 `<!-- ROW_MINE: ksummit.messages.1030 -->`

## 142.14 AI产出版权

- 【Linux社区】援引Bartz诉Anthropic、Kadrey诉Meta判例分析AI输出版权归属三选项，指出现行美国法下非人类创作无法持有版权。 `<!-- ROW_MINE: ksummit.messages.1031 -->`

## 142.15 kallsyms行号信息

- 【Linux社区】回应44MiB开销质疑：崩溃路径刻意避免内存分配与磁盘IO，首版求简便于评审，存储效率后续可再优化。 `<!-- ROW_MINE: ksummit.messages.1033 -->`

## 142.16 Rust别名模型

- 【Linux社区】指出Miri已实现Tree Borrows等别名模型并可在playground检验代码，但涉及C FFI时不适用，并推动其进入Compiler Explorer。 `<!-- ROW_MINE: ksummit.messages.1046 -->`
- 【Linux社区】解释Rust模型须满足LLVM noalias约束方能支撑优化，承认过拟合风险并列举gcc-rs面临的C与LLVM UB差异案例（悬空指针比较、零长memcpy等）。 `<!-- ROW_MINE: ksummit.messages.1070 -->`

## 142.17 回归修复滞后场景

- 【Linux社区】峰会提案总纲：详述修复在主线与stable暴露数周至两月以上的常见场景及评审、合入、PR时点等成因，统领后续四个提案。 `<!-- ROW_MINE: ksummit.messages.1048 -->`

## 142.18 AI评审工具

- 【Linux社区】主张开发者应在提交前自行运行AI评审工具，用AI投资提升PR质量，减少对维护者注意力的无谓占用。 `<!-- ROW_MINE: ksummit.messages.1049 -->`
- 【Linux社区】指出netdev CI已可作docker镜像本地运行，呼吁更多子系统开放CI工具，并把标准检查下沉到b4统一承担。 `<!-- ROW_MINE: ksummit.messages.1105 -->`

## 142.19 C聚合与C++26

- 【Linux社区】单句论点：把编译器告警当作硬性约束即可获得C++26“错误行为”的等效效果。 `<!-- ROW_MINE: ksummit.messages.1052 -->`

## 142.20 设备直通之争

- 【Linux社区】区分政治与技术两面：产业界偏好DRM的许可要求、DRM缓冲机制更成熟；V4L2须逐项检查命令缓冲，libcamera可作开放实现基座。 `<!-- ROW_MINE: ksummit.messages.1053 -->`
- 【Linux社区】以自身经历佐证用户痛点：Dell XPS新机型摄像头无Linux支持致换机受阻，为放宽厂商支持主张提供用户影响实证。 `<!-- ROW_MINE: ksummit.messages.1106 -->`

## 142.21 维护者峰会存废

- 【Linux社区】反驳AMD/Intel规模论：高通同样有50-100人团队仍努力理解上游周期，指两家不愿适应只因无人问责。 `<!-- ROW_MINE: ksummit.messages.1055 -->`

## 142.22 驱动probe失败议题

- 【Linux社区】区分设备故障与驱动bug致probe失败两情形，主张向接口驱动传播错误，避免留下带sysfs接口的僵死驱动，提出峰会讨论。 `<!-- ROW_MINE: ksummit.messages.1060 -->`

## 142.23 trivial补丁政策

- 【Linux社区】主张校准trivial定义：拼写修正可轻审，错误路径引用计数必须严查；要求对UMN研究组强力制裁并质疑IEEE论文伦理。 `<!-- ROW_MINE: ksummit.messages.1064 -->`

## 142.24 安全流程扩展

- 【Linux社区】通报security@近况：流程改进后顺畅得多并将获约6个月全职人力资助；仅本地LLM合规可用，LLM分诊行不通，真正问题是报告者失联与中间商。 `<!-- ROW_MINE: ksummit.messages.1065 -->`

## 142.25 峰会2021形式

- 【Linux社区】讨论混合会场提问机制：害羞者可打字提问，主持人应留意欲发言者并留出停顿，英语口语障碍非新问题，属峰会组织讨论。 `<!-- ROW_MINE: ksummit.messages.1072 -->`

## 142.26 Rust内核政策

- 【Linux社区】长文回应hch：网站文档仅为澄清与凝聚共识、子系统可自决不接Rust；提出由他人接管Rust相关工作等选项，承认safe抽象是另一类形态。 `<!-- ROW_MINE: ksummit.messages.1073 -->`
- 【Linux社区】质疑hpa的C++路线：引入新语言意在解决驱动复杂度与内存安全，inline与宏并非主要bug来源并索要实例。 `<!-- ROW_MINE: ksummit.messages.1107 -->`

## 142.27 安全议题embargo

- 【Linux社区】反驳“Android占绝对多数故服务器端不重要”论：企业单台服务器失陷即危及上千用户数据，装机量之外更须看影响面。 `<!-- ROW_MINE: ksummit.messages.1088 -->`

## 142.28 新开发者洪流

- 【Linux社区】提出不必强制base-commit的两点理由（系列天然可通用、依赖未合入补丁时无基可指），主张交由维护者酌定。 `<!-- ROW_MINE: ksummit.messages.1096 -->`

## 142.29 C安全属性机制

- 【Linux社区】技术细节：[[]]可挂复合语句但强制加大括号，STDC FP_CONTRACT类pragma作用域到块末而GCC未实现，需实验定夺。 `<!-- ROW_MINE: ksummit.messages.1097 -->`

## 142.30 Rust for Linux

- 【Linux社区】说明用Rust重写子系统内部的可行性与限制：安全保证无法回馈C调用方，且尚无GCC代码生成路径，gccrs成熟约需两年。 `<!-- ROW_MINE: ksummit.messages.1117 -->`

## 142.31 API弃用执行

- 【Linux社区】反驳Linus“谁引入谁维护”论：GPIO遗留API数千处调用、转换非小事且系接手既成局面，呼吁支持全局重构而非推诿给API作者。 `<!-- ROW_MINE: ksummit.messages.1128 -->`
