# 198 【Linux社区】kernelorg年报与C去UB进度

> 来源：ksummit 独有 p62（50 封全读，2022-10 至 2025-09：Ryabitsev kernel.org 工具链年度报告一手总结 b4 AI 集成失败教训 AI 爬虫对基础设施冲击 SMTP 持续恶化与废弃 Bugzilla 主张系 2025 年基础设施史核心单篇；ISO C 工作组委员 Uecker 给出硬数据 C23 核心尚有 87 处 UB C2Y 已删 17 处另有 12 项提案并披露 GCC 前端分区域 C 内存安全模式试验；Ralf Jung 从内存模型理论指出 LKMM 依赖机制与 GVN/CSE 基础编译优化根本冲突匹配 LKMM 效率的并发原语仍是未解难题；Levin 给出 kallsyms 嵌入行号完整实测 459 万条目 .rodata +44MiB vmlinux +8.3%；Rust 内核策略论战六封）
> 判定：42 CAND / 8 NV。主题分布：Bugzilla存废之争 3、维护者倦怠与自动化 1、Rust内核策略论战 6、KTODO任务标记 1、fwctl设备直通之争 1、用户态API准入标准 1、Link标签之争 2、琐碎补丁政策 1、AI代码版权责任 2、内核文档工具链 3、C语言RAII手段 1、eBPF接口稳定性 1、kernel.org工具链报告 1、AI审查工具政策 1、Rust早期讨论 1、Rust内核进展 1、栈回溯行号方案 1、静态分析改进 1、补丁发送工具 1、峰会远程参会 1、内存模型与编译器 1、AI生成内容规范 1、AI辅助回迁补丁 1、linus-next集成树 3、LLM标注与合规 1、C语言安全标准化 1、MAINTAINERS列表变革 1、驱动对象生命周期 1、AI时代访问控制 1。

## 198.1 Bugzilla存废之争

- **要点**：Tashkinov称其讥讽被误解，为Bugzilla辩护：邮件无跟踪能力，反对者却提不出可行替代方案，与Pinchart就“侮辱开发者”互斥。Pinchart引LWN 904776反驳Rostedt：以“买外接摄像头”回避内置摄像头故障的变通曾令用户极度不满，被忽视的报告未必无关紧要。Pinchart指邮件缺缺陷跟踪能力；Leemhuis介绍regzbot借Link标签串联报告与补丁追踪回归，Pinchart称其依赖启发式、盼邮件支持结构化数据。
- **史料**：`ksummit.messages.9719`（Artem S. Tashkinov，2022-10-02）、`ksummit.messages.9723`（Laurent Pinchart，2022-10-03）、`ksummit.messages.9790`（Laurent Pinchart，2022-09-30）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9719 -->` `<!-- ROW_MINE: ksummit.messages.9723 -->` `<!-- ROW_MINE: ksummit.messages.9790 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：为 Bugzilla 辩护与“被忽视的报告未必无关紧要”两方互斥并置）；经验优先（总纲第 9 条——经验优先：以“邮件无跟踪能力”“regzbot 依赖启发式”等实际能力为判据）
- **辨析**：三条分属 2022-09/10 同一争论；Pinchart 引 LWN 904776 的“买外接摄像头”个案为可反查文献；Leemhuis 的 regzbot 机制说明与 Pinchart 的“盼邮件支持结构化数据”为工具路线分歧。
- **文献**：DSLXC-11228、DSLXC-11229、DSLXC-11246（`ksummit.messages.9719`、`ksummit.messages.9723`、`ksummit.messages.9790`，2022-10-02、2022-10-03、2022-09-30），全文见 `raw_source.raw_json`

## 198.2 维护者倦怠与自动化

- **要点**：Chamberlain细述自动化抗倦怠的前提：Samsung共享裸机与Oracle OCI等硬件资源、Song Liu的eBPF patchwork即时测试、kdevops整合与“要求测试”之辩。
- **史料**：`ksummit.messages.9726`（Luis Chamberlain，2023-08-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9726 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Samsung 共享裸机、Oracle OCI、Song Liu 的 eBPF patchwork 即时测试、kdevops 整合等具体资源与工具为分析单位）；经验优先（总纲第 9 条——经验优先：以“要求测试”之辩这一实际争议为判据）
- **辨析**：本块系 Luis Chamberlain 的详述；“自动化抗倦怠的前提”表明其条件性表述，属一手。
- **文献**：DSLXC-11230（`ksummit.messages.9726`，2023-08-16），全文见 `raw_source.raw_json`

## 198.3 Rust内核策略论战

- **要点**：Overstreet指Rust不安全层别名规则（tree/stacked borrows）仍未定型，若固化成功可减少spill与reload，令VLIW架构重获实用价值。Sakkinen称用Rust测试文档编译DMA补丁却陷入“无测试不放行”境地，指出DMA的doc测试仅为函数定义无法运行，自荐以内核QA为参与第一步。Overstreet称bcachefs已有btree核心API的Rust绑定，拟先在debugfs试点；反驳“2034年才可用”说，称数年内新硬件驱动将需要Rust。Overstreet回应Linus：Rust的W^X引用保证独占写，仅UnsafeCell边界禁止store加宽；多线程环形缓冲区头尾指针须用原子类型标注。Rostedt追问Uecker：若编译器如LTO般可见全程序，能否自行判定跨线程可见性并据此优化，点出全程序优化与内存模型语义的张力。Laight抨击Rust读取非0/1的bool即属UB，称语言须如调用约定般精确定义行为，断言bool非硬件类型、实现成本高，不如用int表真假。
- **史料**：`ksummit.messages.9727`（Kent Overstreet，2025-02-22）、`ksummit.messages.9733`（Jarkko Sakkinen，2025-02-19）、`ksummit.messages.9749`（Kent Overstreet，2025-02-22）、`ksummit.messages.9755`（Kent Overstreet，2025-02-26）、`ksummit.messages.9768`（Steven Rostedt，2025-02-27）、`ksummit.messages.9773`（David Laight，2025-02-26）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9727 -->` `<!-- ROW_MINE: ksummit.messages.9733 -->` `<!-- ROW_MINE: ksummit.messages.9749 -->` `<!-- ROW_MINE: ksummit.messages.9755 -->` `<!-- ROW_MINE: ksummit.messages.9768 -->` `<!-- ROW_MINE: ksummit.messages.9773 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：别名规则未定型、DMA doc 测试无法运行、bool 语义之抨击与全程序优化之问六方并置）；动手者叙事（总纲第 10 条——动手者创造历史：以 tree/stacked borrows、W^X 引用保证、原子类型标注等具体机制为分析单位）
- **辨析**：六条分属 2025-02 同一论战；Laight 的“bool 非硬件类型、实现成本高”为对语言设计的直接批评；Overstreet 的“2034 年才可用”之反驳与“数年内新硬件驱动将需要 Rust”均属预测。
- **文献**：DSLXC-11231、DSLXC-11232、DSLXC-11237、DSLXC-11239、DSLXC-11241、DSLXC-11243（`ksummit.messages.9727`、`ksummit.messages.9733`、`ksummit.messages.9749`、`ksummit.messages.9755`、`ksummit.messages.9768`、`ksummit.messages.9773`，2025-02-22、2025-02-19、2025-02-22、2025-02-26、2025-02-27、2025-02-26），全文见 `raw_source.raw_json`

## 198.4 KTODO任务标记

- **要点**：Bird提议为KTODO标记建仪表盘量化技术债存量，自述FIXTHIS前缀经验，并质疑任务完成后KTODO注释应随提交删除以免误导。
- **史料**：`ksummit.messages.9734`（Bird, Tim，2023-10-19）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9734 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“为 KTODO 标记建仪表盘量化技术债存量”这一具体工具为分析单位）；经验优先（总纲第 9 条——经验优先：以自述 FIXTHIS 前缀经验为判据）
- **辨析**：本块系 Tim Bird 的提议；“质疑任务完成后 KTODO 注释应随提交删除以免误导”为对既有做法的批评，属开放问题。
- **文献**：DSLXC-11233（`ksummit.messages.9734`，2023-10-19），全文见 `raw_source.raw_json`

## 198.5 fwctl设备直通之争

- **要点**：Williams为fwctl辩护：区分FPGA比特流式配置面与CXL厂商调试日志命令，承认网络维护者异议不能忽视，邮件信任赤字难解故提议面对面调解。
- **史料**：`ksummit.messages.9735`（Dan Williams，2024-07-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9735 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 FPGA 比特流式配置面与 CXL 厂商调试日志命令的区分、面对面调解这一具体提议为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：承认网络维护者异议不能忽视）
- **辨析**：本块系 Dan Williams 的辩护；“邮件信任赤字难解故提议面对面调解”表明争议已至渠道层面，属一手。
- **文献**：DSLXC-11234（`ksummit.messages.9735`，2024-07-09），全文见 `raw_source.raw_json`

## 198.6 用户态API准入标准

- **要点**：Romanovsky主张API须进入发行版软件栈方能扩展，斥HabanaLabs绕过RDMA社区为搭便车；Greg KH反驳厂商都该上游、发行版仅是少数场景，反问门槛何在。
- **史料**：`ksummit.messages.9737`（Leon Romanovsky，2021-09-12）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9737 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：API 准入之争被还原为发行版软件栈与厂商搭便车的边界）；多方平等（总纲第 8 条——本体论上各方平等：进入发行版方能扩展的主张与“厂商都该上游”的反驳并置）
- **辨析**：本块含 Leon Romanovsky 与 Greg KH 的两方；“斥 HabanaLabs 绕过 RDMA 社区为搭便车”为具名指控，落书须标明。
- **文献**：DSLXC-11235（`ksummit.messages.9737`，2021-09-12），全文见 `raw_source.raw_json`

## 198.7 Link标签之争

- **要点**：Bottomley重申把Link标签之争一分为二：工具自动化追踪用message-id即可，维护者手写背景注释另立，Link兼两职正是争议根源。Anvin披露Link标签来历：其原始方案直接放Message-ID被Linus以不可点击否决，折中为kernel.org域名下编码msgid的URL，兼作URN防档案失效。
- **史料**：`ksummit.messages.9743`（James Bottomley，2025-10-16）、`ksummit.messages.9799`（H. Peter Anvin，2025-10-13）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9743 -->` `<!-- ROW_MINE: ksummit.messages.9799 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 message-id 自动化追踪与维护者手写背景注释的两分、kernel.org 域名下编码 msgid 的 URL 为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：原始方案直接放 Message-ID 被 Linus 以不可点击否决）
- **辨析**：Anvin 的“原始方案被 Linus 以不可点击否决”系对历史决议的披露，属关键沿革一手；Bottomley 的“Link 兼两职正是争议根源”为机制判断。
- **文献**：DSLXC-11236、DSLXC-11250（`ksummit.messages.9743`、`ksummit.messages.9799`，2025-10-16、2025-10-13），全文见 `raw_source.raw_json`

## 198.8 琐碎补丁政策

- **要点**：Verkuil说明媒体29个被回退补丁早于pm_runtime_resume_and_get()问世；引Leon方案在__pm_runtime_resume失败时自动递减usage_count，Brown称runtime PM API本就难用。
- **史料**：`ksummit.messages.9753`（Hans Verkuil，2021-04-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9753 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“媒体 29 个被回退补丁早于 pm_runtime_resume_and_get() 问世”这一时间线为判据）；多方平等（总纲第 8 条——本体论上各方平等：Leon 的自动递减方案与 Brown 的“runtime PM API 本就难用”并置）
- **辨析**：本块系 Hans Verkuil 的说明，属对 UMN 补丁争议的另一方举证；与 197.23 Mauro 的时间线一致，Brown 的评语为转引。
- **文献**：DSLXC-11238（`ksummit.messages.9753`，2021-04-22），全文见 `raw_source.raw_json`

## 198.9 AI代码版权责任

- **要点**：Rostedt剖析SoB链版权责任：AI注入侵权代码时提交者与维护者何者担责不明，律师澄清前维护者难免顾虑，透明标注或反成把柄。Mauro判断AI生成代码大抵源于公开许可代码（企业禁用公共AI处理私有码），视SoB为授权保证，只要人类把关质量便不介意是否用AI。
- **史料**：`ksummit.messages.9756`（Steven Rostedt，2025-11-10）、`ksummit.messages.9849`（Mauro Carvalho Chehab，2025-08-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9756 -->` `<!-- ROW_MINE: ksummit.messages.9849 -->`
- **史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：SoB 链版权责任在提交者与维护者之间的归属未明）；多方平等（总纲第 8 条——本体论上各方平等：透明标注或反成把柄的顾虑与“只要人类把关便不介意”的立场并置）
- **辨析**：Rostedt 的“律师澄清前维护者难免顾虑”为风险判断；Mauro 的“AI 生成代码大抵源于公开许可代码”为其经验估计，非法律意见。
- **文献**：DSLXC-11240、DSLXC-11263（`ksummit.messages.9756`、`ksummit.messages.9849`，2025-11-10、2025-08-18），全文见 `raw_source.raw_json`

## 198.10 内核文档工具链

- **要点**：Nikula指kernel-doc脚本对头文件重复解析四次，主张改造为可缓存的Python Sphinx扩展，反对预处理RST，忆旧DocBook败于各阶段阻抗失配。Ryabitsev以系统管理者立场主张脚本行为可预期：python3脚本应遵循系统默认解释器，自动改选其他版本令人困扰。Nikula透露媒体子系统CI已做到W=1零告警构建，询问如何滤除非媒体告警，盼统一要求贡献者修复全部编译警告而非学会忽略。
- **史料**：`ksummit.messages.9772`（Jani Nikula，2022-06-23）、`ksummit.messages.9795`（Konstantin Ryabitsev，2025-09-03）、`ksummit.messages.9848`（Jani Nikula，2025-09-02）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9772 -->` `<!-- ROW_MINE: ksummit.messages.9795 -->` `<!-- ROW_MINE: ksummit.messages.9848 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以可缓存的 Python Sphinx 扩展、遵循系统默认解释器、W=1 零告警等具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“kernel-doc 对头文件重复解析四次”与“媒体子系统 CI 已做到 W=1 零告警”等实际状况为判据）
- **辨析**：三条分属 2022-06 至 2025-09；Nikula 的“忆旧 DocBook 败于各阶段阻抗失配”为历史归因；Ryabitsev 的“脚本行为可预期”为系统管理者立场。
- **文献**：DSLXC-11242、DSLXC-11247、DSLXC-11262（`ksummit.messages.9772`、`ksummit.messages.9795`、`ksummit.messages.9848`，2022-06-23、2025-09-03、2025-09-02），全文见 `raw_source.raw_json`

## 198.11 C语言RAII手段

- **要点**：Hemminger针对驱动错误路径RAII需求，示范直接以GCC cleanup属性定义_cleanup_free_，认为比Van Assche的错误易发宏方案更简洁。
- **史料**：`ksummit.messages.9776`（Stephen Hemminger，2021-07-06）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9776 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“直接以 GCC cleanup 属性定义 _cleanup_free_”这一具体代码手段为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：cleanup 属性与 Van Assche 的错误易发宏方案并置）
- **辨析**：本块系 Stephen Hemminger 的方案；“认为比 Van Assche 的错误易发宏方案更简洁”为其比较判断。
- **文献**：DSLXC-11244（`ksummit.messages.9776`，2021-07-06），全文见 `raw_source.raw_json`

## 198.12 eBPF接口稳定性

- **要点**：Rostedt质疑依内核内部信息编写的eBPF程序会形成事实稳定API：多年后维护者改动代码将触发“破坏用户态”条款而被要求回退。
- **史料**：`ksummit.messages.9785`（Steven Rostedt，2022-06-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9785 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：依内部信息编写的 eBPF 程序与“破坏用户态”条款的张力被明示）；偶然性优先（总纲第 5 条——没有必然性，只有偶然性：多年后维护者改动代码将触发回退要求）
- **辨析**：本块系 Steven Rostedt 的质疑；“会形成事实稳定 API”为其推断，属对既有条款后果的预判。
- **文献**：DSLXC-11245（`ksummit.messages.9785`，2022-06-23），全文见 `raw_source.raw_json`

## 198.13 kernel.org工具链报告

- **要点**：Ryabitsev年度报告：b4普及与AI集成失败教训、AI爬虫冲击、SMTP恶化、lore渐成分布式消息总线、local lore维护者容器、拟废Bugzilla、与OpenSSF重构信任网。
- **史料**：`ksummit.messages.9796`（Konstantin Ryabitsev，2025-12-10）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9796 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 b4 普及、lore 渐成分布式消息总线、local lore 维护者容器、与 OpenSSF 重构信任网等具体项目为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：SMTP 持续恶化、拟废 Bugzilla）
- **辨析**：本块系 kernel.org 工具链年度报告要点，属 2025 年基础设施史核心单篇一手；“AI 集成失败教训”与“AI 爬虫冲击”为可追溯的年度记录。
- **文献**：DSLXC-11248（`ksummit.messages.9796`，2025-12-10），全文见 `raw_source.raw_json`

## 198.14 AI审查工具政策

- **要点**：Torvalds主张AI工具应优先服务维护者而非普通开发者，举安全列表AI垃圾报告与Jens Axboe因AI爬虫放弃自建git服务器为例。
- **史料**：`ksummit.messages.9798`（Linus Torvalds，2025-10-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9798 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“AI 工具应优先服务维护者”这一具体定位为分析单位）；经验优先（总纲第 9 条——经验优先：以安全列表 AI 垃圾报告与 Jens Axboe 因 AI 爬虫放弃自建 git 服务器两个实际案例为判据）
- **辨析**：本块系 Linus Torvalds 的主张；两个案例为具名可核事实，其定位表述属顶层判断。
- **文献**：DSLXC-11249（`ksummit.messages.9798`，2025-10-09），全文见 `raw_source.raw_json`

## 198.15 Rust早期讨论

- **要点**：Wedson以强弱双计数与弱引用升级方案回应引用计数之问；Greg KH追问Rust如何对接dentry/inode/kobject等内核自管计数，称需先见真实驱动。
- **史料**：`ksummit.messages.9800`（Greg KH，2021-07-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9800 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以强弱双计数、弱引用升级方案与 dentry/inode/kobject 的对接为分析单位）；经验优先（总纲第 9 条——经验优先：以“需先见真实驱动”这一实证前提为判据）
- **辨析**：本块含 Wedson Almeida Filho 的方案与 Greg KH 的追问两方，署名为本封发件人 Greg KH；“称需先见真实驱动”为维护者对提案的门槛要求。
- **文献**：DSLXC-11251（`ksummit.messages.9800`，2021-07-08），全文见 `raw_source.raw_json`

## 198.16 Rust内核进展

- **要点**：Ojeda的LPC 2024提案：概述Rust安全抽象与构建系统进展、kernel crate拆分、多版本编译器支持使发行版开箱可用、Linux列入Rust 2024h2目标并进预合并CI。
- **史料**：`ksummit.messages.9803`（Miguel Ojeda，2024-06-22）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9803 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 kernel crate 拆分、多版本编译器支持、进预合并 CI 等具体进展为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：Rust 安全抽象与构建系统进展属随版本演进的议题）
- **辨析**：本块系 Miguel Ojeda 的 LPC 2024 提案；“Linux 列入 Rust 2024h2 目标”为可核的项目级事实。
- **文献**：DSLXC-11252（`ksummit.messages.9803`，2024-06-22），全文见 `raw_source.raw_json`

## 198.17 栈回溯行号方案

- **要点**：Levin实测kallsyms嵌入源码行号开销：459万条目令.rodata增约44MiB，vmlinux由529MiB至573MiB（+8.3%）；对Babka模块化之议称首次崩溃即可用decode_stacktrace.sh在用户态解码。
- **史料**：`ksummit.messages.9805`（Sasha Levin，2026-03-03）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9805 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“459 万条目令 .rodata 增约 44MiB，vmlinux 由 529MiB 至 573MiB（+8.3%）”这一实测为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“首次崩溃即可用 decode_stacktrace.sh 在用户态解码”这一具体方案为分析单位）
- **辨析**：本块为带数字的可复算实测；“对 Babka 模块化之议”为对他人提议的回应，属对话记录。
- **文献**：DSLXC-11253（`ksummit.messages.9805`，2026-03-03），全文见 `raw_source.raw_json`

## 198.18 静态分析改进

- **要点**：Pinchart提议为函数加注解标明返回错误码或错误指针，助静态分析识别“if (!ret) return ret;”类反转bug，忆gcc 4.2未初始化告警时代每版皆获真bug。
- **史料**：`ksummit.messages.9814`（Laurent Pinchart，2021-07-24）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9814 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“为函数加注解标明返回错误码或错误指针”这一具体机制为分析单位）；经验优先（总纲第 9 条——经验优先：以“gcc 4.2 未初始化告警时代每版皆获真 bug”这一历史经验为判据）
- **辨析**：本块系 Laurent Pinchart 的提议；“助静态分析识别 if (!ret) return ret; 类反转 bug”为目标表述，属提案。
- **文献**：DSLXC-11254（`ksummit.messages.9814`，2021-07-24），全文见 `raw_source.raw_json`

## 198.19 补丁发送工具

- **要点**：Anderson推荐源自U-Boot的patman：逐补丁get_maintainer加CC、封面信全员抄送、自动整理版本历史，并转述Olof批评其令大型系列过易发送。
- **史料**：`ksummit.messages.9819`（Doug Anderson，2021-04-23）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9819 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 patman 的逐补丁 get_maintainer 加 CC、封面信全员抄送、自动整理版本历史等具体功能为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：工具便利与“令大型系列过易发送”的批评并置）
- **辨析**：本块系 Doug Anderson 的推荐；“转述 Olof 批评”属引述，落书须与原话核对。
- **文献**：DSLXC-11255（`ksummit.messages.9819`，2021-04-23），全文见 `raw_source.raw_json`

## 198.20 峰会远程参会

- **要点**：Pinchart主张混合峰会设专人看聊天区转述远程提问；指出工作坊远程参与最大障碍是现场者不用麦克风，须强制执行并增配话筒。
- **史料**：`ksummit.messages.9822`（Laurent Pinchart，2021-06-18）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9822 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“设专人看聊天区转述远程提问”“强制执行用麦并增配话筒”等具体安排为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：远程与现场参会者的参与条件被明确权衡）
- **辨析**：本块系 Laurent Pinchart 的会务主张；“现场者不用麦克风”为其归因的现场障碍，属经验判断。
- **文献**：DSLXC-11256（`ksummit.messages.9822`，2021-06-18），全文见 `raw_source.raw_json`

## 198.21 内存模型与编译器

- **要点**：Jung阐释原子写禁止编译器凭空新增写，指LKMM依赖机制与GVN/CSE等基础优化根本冲突，为优化型语言找到匹配LKMM效率的并发原语仍是未解难题。
- **史料**：`ksummit.messages.9823`（Ralf Jung，2025-03-04）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9823 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：LKMM 依赖机制与 GVN/CSE 基础优化被明示为根本冲突）；知识注定过时（总纲第 22 条——知识注定过时：为优化型语言找到匹配 LKMM 效率的并发原语仍是未解难题）
- **辨析**：本块系 Ralf Jung 的理论阐述，属内存模型层一手；“仍是未解难题”明示为开放问题，落书不得写成已解决。
- **文献**：DSLXC-11257（`ksummit.messages.9823`，2025-03-04），全文见 `raw_source.raw_json`

## 198.22 AI生成内容规范

- **要点**：Stoakes坚持指南须开宗明义拒绝AI slop，举Carpenter遇提交者以AI幻觉规格搪塞质询为例，引Postgres的Freund帖警示，并指Linus立场被外界误传。
- **史料**：`ksummit.messages.9828`（Lorenzo Stoakes，2026-01-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9828 -->`
- **史观**：多方平等（总纲第 8 条——本体论上各方平等：指南须开宗明义拒绝 AI slop 与“Linus 立场被外界误传”并置）；经验优先（总纲第 9 条——经验优先：以“Carpenter 遇提交者以 AI 幻觉规格搪塞质询”这一实际案例为判据）
- **辨析**：本块系 Lorenzo Stoakes 的坚持；“引 Postgres 的 Freund 帖”为跨项目参照；“指 Linus 立场被外界误传”属对既有印象的订正。
- **文献**：DSLXC-11258（`ksummit.messages.9828`，2026-01-09），全文见 `raw_source.raw_json`

## 198.23 AI辅助回迁补丁

- **要点**：Levin估计约八至九成回迁失败仅是上下文冲突或缺依赖，属初级工程师可解、AI能胜任；其余一至两成因子系统大重构，现有AI尚不可托付。
- **史料**：`ksummit.messages.9832`（Sasha Levin，2025-08-05）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9832 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“约八至九成回迁失败仅是上下文冲突或缺依赖”这一实际估计为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“初级工程师可解、AI 能胜任”与“一至两成因子系统大重构”的能力分档为分析单位）
- **辨析**：本块系 Sasha Levin 的能力分档；“八至九成”“一至两成”为当事人估计，非统计结果，落书须标明。
- **文献**：DSLXC-11259（`ksummit.messages.9832`，2025-08-05），全文见 `raw_source.raw_json`

## 198.24 linus-next集成树

- **要点**：Brown举linus-next脚本首例即绊倒：KVM arm64提交afa9b48f327c未见于lore亦未进-next而Linus照拉，惟其曾埋在邮件列表回复中。Torvalds界定所需为Guenter式每_rc跨多架构实机启动的功能测试，每个合并窗口总能揪出数个问题，类比linux-next多架构构建测试的价值。McKenney质疑linus-next激励效应：更多测试者既可能倒逼快速修复、也可能令人避之不及，戏言除非Linus拒绝“停留过短”的拉取请求。
- **史料**：`ksummit.messages.9839`（Mark Brown，2024-10-22）、`ksummit.messages.9862`（Linus Torvalds，2024-10-23）、`ksummit.messages.9863`（Paul E. McKenney，2024-10-21）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9839 -->` `<!-- ROW_MINE: ksummit.messages.9862 -->` `<!-- ROW_MINE: ksummit.messages.9863 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“Guenter 式每 rc 跨多架构实机启动的功能测试”这一具体方案为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：倒逼快速修复与令人避之不及两种激励效应并置）
- **辨析**：Brown 的“KVM arm64 提交 afa9b48f327c 未见于 lore 亦未进 -next 而 Linus 照拉”为可反查的具体首例；McKenney 的“戏言除非 Linus 拒绝停留过短的拉取请求”为修辞性表述。
- **文献**：DSLXC-11260、DSLXC-11266、DSLXC-11267（`ksummit.messages.9839`、`ksummit.messages.9862`、`ksummit.messages.9863`，2024-10-22、2024-10-23、2024-10-21），全文见 `raw_source.raw_json`

## 198.25 LLM标注与合规

- **要点**：Levin披露Assisted-by详注工具名意在日后审计工具实效，主张按提交质量而非工具论英雄，提AGENTS.md改进合规，并质疑对专有AI工具的真实依赖度。
- **史料**：`ksummit.messages.9842`（Sasha Levin，2026-07-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9842 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Assisted-by 详注工具名、AGENTS.md 改进合规等具体机制为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：按提交质量而非工具论英雄与对专有 AI 工具依赖度的质疑并置）
- **辨析**：本块系 Sasha Levin 的披露与主张；“意在日后审计工具实效”为其动机说明，属一手。
- **文献**：DSLXC-11261（`ksummit.messages.9842`，2026-07-16），全文见 `raw_source.raw_json`

## 198.26 C语言安全标准化

- **要点**：Uecker（ISO C工作组委员）称C23核心尚有87处UB、C2Y已除17处另有12项提案，正于GCC前端试验可分区域启用的内存安全模式，呼吁内核社区参与标准化。
- **史料**：`ksummit.messages.9854`（Martin Uecker，2025-02-20）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9854 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“C23 核心尚有 87 处 UB、C2Y 已除 17 处另有 12 项提案”这一硬数据为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以“于 GCC 前端试验可分区域启用的内存安全模式”这一具体试验为分析单位）
- **辨析**：本块系 ISO C 工作组委员 Martin Uecker 的标准化进度陈述，属本页最硬的数据一手；“呼吁内核社区参与标准化”为行动倡议。
- **文献**：DSLXC-11264（`ksummit.messages.9854`，2025-02-20），全文见 `raw_source.raw_json`

## 198.27 MAINTAINERS列表变革

- **要点**：Perches自述已不订阅LKML、极少参与讨论，仅偶以关键词检索lore并手动下载线程，为“THE REST”迁离vger之议提供资深维护者工作流佐证。
- **史料**：`ksummit.messages.9858`（Joe Perches，2023-11-08）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9858 -->`
- **史观**：经验优先（总纲第 9 条——经验优先：以“已不订阅 LKML、仅偶以关键词检索 lore 并手动下载线程”这一实际工作流为判据）；动手者叙事（总纲第 10 条——动手者创造历史：以资深维护者的检索式工作流为分析单位）
- **辨析**：本块系 Joe Perches 的自述，为“THE REST 迁离 vger”之议提供资深维护者工作流佐证，属一手。
- **文献**：DSLXC-11265（`ksummit.messages.9858`，2023-11-08），全文见 `raw_source.raw_json`

## 198.28 驱动对象生命周期

- **要点**：Golaszewski提案梳理驱动对象生命周期乱象脉络（Pinchart LPC 2022、其FOSDEM 2023、Sang EOSS 2023），计划分多年多阶段统一子系统对驱动数据的处理。
- **史料**：`ksummit.messages.9872`（Bartosz Golaszewski，2023-08-09）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9872 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以 Pinchart LPC 2022、其 FOSDEM 2023、Sang EOSS 2023 三次公开讨论这一脉络为分析单位）；知识注定过时（总纲第 22 条——知识注定过时：驱动对象生命周期乱象跨年未决）
- **辨析**：本块系 Bartosz Golaszewski 的提案；“计划分多年多阶段统一子系统对驱动数据的处理”明示为长期工程，非短期修复。
- **文献**：DSLXC-11268（`ksummit.messages.9872`，2023-08-09），全文见 `raw_source.raw_json`

## 198.29 AI时代访问控制

- **要点**：Coly Li转达应用团队评估：现以BPF做规则控制、规则持久化繁琐；举AI相册硬链接隐私场景与父目录无写权删除之困，Moore重申LSM只能拒不能授、系有意设计。
- **史料**：`ksummit.messages.9878`（Coly Li，2025-09-16）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit.messages.9878 -->`
- **史观**：动手者叙事（总纲第 10 条——动手者创造历史：以“现以 BPF 做规则控制、规则持久化繁琐”这一实操约束与 AI 相册硬链接隐私场景为分析单位）；多方平等（总纲第 8 条——本体论上各方平等：应用团队诉求与“LSM 只能拒不能授、系有意设计”的维护者说明并置）
- **辨析**：本块系 Coly Li 转达应用团队评估；“Moore 重申 LSM 只能拒不能授”系引述维护者立场，落书须与原话核对。
- **文献**：DSLXC-11269（`ksummit.messages.9878`，2025-09-16），全文见 `raw_source.raw_json`
