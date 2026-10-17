# 151 【Linux社区】malloc统一提案与7GB数据

> 来源：ksummit 独有 p15（50 封全读，2021-04 至 2026-08，内核 malloc 统一 vmalloc/kmalloc/GFP 提案兼作 Rust std::alloc 基础、bufferhead vs folio 2.5→7GB/s CPU 降 70% 实测、GKI 冻结后常需扩展核心内核、疫情期间包机往来欧美提议、UMN 道歉信分析（损信任未损内核）、Qualcomm 合规反证、2928 个 Fixes 统计更正）
> 判定：46 CAND / 4 NV。主题分布：议题提案：内核实现 malloc 1、议题讨论：trivial 补丁受理政策 1、议题讨论：bugzilla 退役与 LLM 解码栈回溯 1、议题记录：linux-next 隐藏提交 1、议题讨论：合并树过平 1、峰会组织：2021 赴美行程 1、数据更正：bugzilla 有用性论战 1、议题讨论：bugzilla 强制订阅 1、议题讨论：DRM 上游流程与合并窗口 1、议题讨论：C 聚合传递与内存模型 1、议题征集：ChromeOS 内核议题反馈 1、议题讨论：AI 代码审查发现项跟踪 1、议题讨论：C 聚合传递与数据竞争语义 1、议题讨论：合并树过平与主题分支 1、流程记录：TAB 选举 CIVS 投票操作 1、议题讨论：stable 邮件语义过滤 1、议题讨论：指针返回值注记分类 1、议题讨论：Rust 与 devres 生命周期 1、补丁反馈：kallsyms 行号信息 1、议题讨论：bugzilla 与邮件报障 1、议题讨论：LKL 块层与遗留存储 1、议题讨论：UMN 论文与 trivial 补丁 1、议题讨论：加速器驱动的用户态要求 1、工具信息：Coccinelle 注记能力 1、流程记录：Message-Id 标签工具化 1、提案：git bisect 包装脚本 1、治理记录：叫停偏离议题言论 1、议题讨论：AI 审查工具进峰会议程 1、议题讨论：Qualcomm 上游合规反证 1、议题讨论：bugzilla 之后的定位与经费 1、议题讨论：Fixes 标签强制实践 1、议题讨论：UnsafeCell 别名语义 1、议题讨论：AI 在内核流程的角色 1、议题讨论：C 内存模型与依赖序 1、议题提问：Rust 反向替代子系统 1、议题讨论：linux-next 合并顺序分析 1、议题讨论：遗留文件系统的存废 1、议题提案：每 cgroup 交换设备控制 1、议题讨论：dt-bindings 与 DT 一致性 1、议题讨论：linus-next 测试报告成本 1、议题讨论：bufferhead 与高阶 folio 1、议题讨论：文档构建自动选 Python 版本 1、议题讨论：GKI 冻结后的核心改动 1、议题讨论：AI 审查的局限与定位 1、议题讨论：文档构建 PATH 行为定论 1、提案：Fixes 标签规则 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p15 的逐封提取（2021-04 至 2026-08，46 CAND / 4 NV），全 46 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 151.1 议题提案：内核实现 malloc

- 【Linux社区】提议实现 malloc()/calloc() 屏蔽 vmalloc/kmalloc/GFP 细节，讨论失败语义、越界与释放后使用检测，兼作 Rust std::alloc 基础。 `<!-- ROW_MINE: ksummit.messages.2260 -->`

## 151.2 议题讨论：trivial 补丁受理政策

- 【Linux社区】说明新列表服务器可拒收 HTML 邮件，但跨消息校验封面信抄送不可行，主张改进提交者工具而非服务端拦截。 `<!-- ROW_MINE: ksummit.messages.2266 -->`

## 151.3 议题讨论：bugzilla 退役与 LLM 解码栈回溯

- 【Linux社区】反驳确定性工具论：自编译内核无调试符号时无确定性方案可 retroactively 解码，承认语气不当但坚持质疑者应给出替代方案。 `<!-- ROW_MINE: ksummit.messages.2267 -->`

## 151.4 议题记录：linux-next 隐藏提交

- 【Linux社区】记录其九月维护者峰会议题提案获得采纳并引发实际讨论，附 LWN 报道链接。 `<!-- ROW_MINE: ksummit.messages.2270 -->`

## 151.5 议题讨论：合并树过平

- 【Linux社区】以 tip 树多主题分支协同维护为例，说明热点树分摊合并负载的可行方向。 `<!-- ROW_MINE: ksummit.messages.2272 -->`

## 151.6 峰会组织：2021 赴美行程

- 【Linux社区】因疫情与机场交叉暴露风险提议包机往来欧美较空闲机场，附按里程计价的初步成本考察。 `<!-- ROW_MINE: ksummit.messages.2274 -->`

## 151.7 数据更正：bugzilla 有用性论战

- 【Linux社区】更正自身 grep 别名造成的统计误差，确认 v5.19..master 约 2928 个 Fixes 提交且误报不足百条，结论不变。 `<!-- ROW_MINE: ksummit.messages.2275 -->`

## 151.8 议题讨论：bugzilla 强制订阅

- 【Linux社区】质疑按 git 提交自动订阅开发者收 bug 邮件的方案在欧盟法律上可能不可行。 `<!-- ROW_MINE: ksummit.messages.2280 -->`

## 151.9 议题讨论：DRM 上游流程与合并窗口

- 【Linux社区】阐述 AMD/Intel 数十人团队难以适配合并窗口、缺 CI、Fixes 标签与 cherry-pick 严重失准，导致开发回流公司内部。 `<!-- ROW_MINE: ksummit.messages.2287 -->`

## 151.10 议题讨论：C 聚合传递与内存模型

- 【Linux社区】厘清可观察行为与线程可见性之别，指出 UB 被现代优化器利用的历史及 TS 6010 未入 C23 的原因。 `<!-- ROW_MINE: ksummit.messages.2289 -->`

## 151.11 议题征集：ChromeOS 内核议题反馈

- 【Linux社区】认可议题有价值并建议补充 drivers/platform/chrome 独立存在理由与 ACPI 固件 quirk 取舍经验两个讨论点。 `<!-- ROW_MINE: ksummit.messages.2297 -->`

## 151.12 议题讨论：AI 代码审查发现项跟踪

- 【Linux社区】主张 AI 审查发现应像 syzkaller 一样进入公共看板持续跟踪，不阻塞提交者，便于委派他人修复。 `<!-- ROW_MINE: ksummit.messages.2299 -->`

## 151.13 议题讨论：C 聚合传递与数据竞争语义

- 【Linux社区】区分可观察行为与可见性，讨论加强数据竞争语义、编译器需识别锁保护对象，承诺与编译器开发者沟通。 `<!-- ROW_MINE: ksummit.messages.2301 -->`

## 151.14 议题讨论：合并树过平与主题分支

- 【Linux社区】介绍自身实践：为 rtla 代传 pull、应 Linus 要求拆主题分支便于单项否决，建议维护者先分拆工作再谈层级化。 `<!-- ROW_MINE: ksummit.messages.2303 -->`

## 151.15 流程记录：TAB 选举 CIVS 投票操作

- 【Linux社区】说明 CIVS opt-in 必须使用收到原信的同一邮箱，输入确认码后才会出现投票链接，解决投票失败问题。 `<!-- ROW_MINE: ksummit.messages.2307 -->`

## 151.16 议题讨论：stable 邮件语义过滤

- 【Linux社区】引 LPC 报告主张以底层设计期望文档为语义过滤基础，分步降低 stable 邮件墙的审查负担。 `<!-- ROW_MINE: ksummit.messages.2314 -->`

## 151.17 议题讨论：指针返回值注记分类

- 【Linux社区】补充第五类返回值模式：有效指针、NULL 或错误指针皆可，如各 *get*_optional() 函数。 `<!-- ROW_MINE: ksummit.messages.2317 -->`

## 151.18 议题讨论：Rust 与 devres 生命周期

- 【Linux社区】主张模块生命周期必含设备生命周期，devm 内存可延至模块释放统一回收以消除中断处理器的释放后使用。 `<!-- ROW_MINE: ksummit.messages.2319 -->`

## 151.19 补丁反馈：kallsyms 行号信息

- 【Linux社区】肯定补丁有用并提出去掉 0x 前缀改十进制、去掉括号噪音的具体格式建议。 `<!-- ROW_MINE: ksummit.messages.2321 -->`

## 151.20 议题讨论：bugzilla 与邮件报障

- 【Linux社区】以 Debian 邮件式缺陷跟踪少人用、Launchpad 更流行为例论证报障需网页界面，普通用户并非程序员。 `<!-- ROW_MINE: ksummit.messages.2322 -->`

## 151.21 议题讨论：LKL 块层与遗留存储

- 【Linux社区】回应 UFS/Android 性能论：仅拟废弃过旧 SCSI 协议层，LKL 与 SG_IO 面向遗留设备支持场景。 `<!-- ROW_MINE: ksummit.messages.2325 -->`

## 151.22 议题讨论：UMN 论文与 trivial 补丁

- 【Linux社区】提供作者网页澄清声明与论文入选信息，分析道歉信：破坏了信任但未实际注入内核缺陷。 `<!-- ROW_MINE: ksummit.messages.2327 -->`

## 151.23 议题讨论：加速器驱动的用户态要求

- 【Linux社区】指出 IB dma-buf 补丁经 dri-devel 与 rdma 大量专家长时间评审，批评绕过常规评审把烂摊子引入 drivers/misc 的维护者。 `<!-- ROW_MINE: ksummit.messages.2333 -->`

## 151.24 工具信息：Coccinelle 注记能力

- 【Linux社区】提供具体进展：Nishimura 正大幅改进 Coccinelle 添加与匹配注记的能力，回应注记提案可行性。 `<!-- ROW_MINE: ksummit.messages.2339 -->`

## 151.25 流程记录：Message-Id 标签工具化

- 【Linux社区】认同 Patchwork 应支持 Message-Id 标签，发现自身脚本误用 Link 标签并即时更正重拉补丁。 `<!-- ROW_MINE: ksummit.messages.2340 -->`

## 151.26 提案：git bisect 包装脚本

- 【Linux社区】提议在 scripts/ 下做内核专用 bisect 包装：自动保存 .config、每步重新配置并显示配置影响。 `<!-- ROW_MINE: ksummit.messages.2343 -->`

## 151.27 治理记录：叫停偏离议题言论

- 【Linux社区】以资深维护者身份要求 Enrico 停止宪法第二修正案言论并警告将被过滤，属峰会讨论线的行为治理。 `<!-- ROW_MINE: ksummit.messages.2345 -->`

## 151.28 议题讨论：AI 审查工具进峰会议程

- 【Linux社区】主张公开讨论而非回避，类比 BitKeeper 争议；分享 b4 摘要改用 ollama/gemma3 避免专有依赖的实践并建议 BoF。 `<!-- ROW_MINE: ksummit.messages.2346 -->`

## 151.29 议题讨论：Qualcomm 上游合规反证

- 【Linux社区】以一线经验反驳 Airlie：Qualcomm 硬件发布前九个月公开提交、BSP 纯上游，并担忧维护者双重标准开恶例。 `<!-- ROW_MINE: ksummit.messages.2349 -->`

## 151.30 议题讨论：bugzilla 之后的定位与经费

- 【Linux社区】认同指定负责人是难点，自省可否出任回归 bugmaster，支持先向 LF 争取设立职位再谈工具。 `<!-- ROW_MINE: ksummit.messages.2350 -->`

## 151.31 议题讨论：Fixes 标签强制实践

- 【Linux社区】分享驱动内部强制修复须带 Fixes 的经验，偶用 unknown 但会受维护者质疑，支持该方向。 `<!-- ROW_MINE: ksummit.messages.2358 -->`

## 151.32 议题讨论：UnsafeCell 别名语义

- 【Linux社区】以代码与 MIRI 验证澄清 &UnsafeCell<T> 与 C 指针的等价条件及引用失效构成 UB 的具体情形。 `<!-- ROW_MINE: ksummit.messages.2361 -->`

## 151.33 议题讨论：AI 在内核流程的角色

- 【Linux社区】质疑 AI 补丁回移植：上下文假设易错非 LLM 所长；反对测试代码无关紧要的假设并指出 selftests 已被轻视。 `<!-- ROW_MINE: ksummit.messages.2363 -->`

## 151.34 议题讨论：C 内存模型与依赖序

- 【Linux社区】认同标准界回避真实硬件的倾向，给出内核路线：现行编码规范配合外部工具检查 dependency ordering，附文章链接。 `<!-- ROW_MINE: ksummit.messages.2364 -->`

## 151.35 议题提问：Rust 反向替代子系统

- 【Linux社区】提出实质架构问题：能否用 Rust 重写子系统内部数据结构而让 C 驱动继续作为消费者。 `<!-- ROW_MINE: ksummit.messages.2370 -->`

## 151.36 议题讨论：linux-next 合并顺序分析

- 【Linux社区】逐项对比线性与二叉合并模式的构建成本与 bisect 效果，结论二叉模式重建开销更高，开头另更正一处笔误。 `<!-- ROW_MINE: ksummit.messages.2371 -->`

## 151.37 议题讨论：遗留文件系统的存废

- 【Linux社区】以 sysv/adfs/befs 五年补丁量论证无人爱的旧文件系统负担极小，分析用法决定风险，提出必要时可剥离 mmap 支持。 `<!-- ROW_MINE: ksummit.messages.2376 -->`

## 151.38 议题提案：每 cgroup 交换设备控制

- 【Linux社区】完整议题征集：前后台进程分级 swap、percpu 集群与 NUMA 绑定问题、swap tier 方案及与 Chris Li 的争论，附议程与六条链接。 `<!-- ROW_MINE: ksummit.messages.2378 -->`

## 151.39 议题讨论：dt-bindings 与 DT 一致性

- 【Linux社区】阐明绑定即 ABI 的处理原则：旧平台文本绑定错乱时两者取其二，影响用户的既成错误需内核兼容并顾及下游再导出者。 `<!-- ROW_MINE: ksummit.messages.2381 -->`

## 151.40 议题讨论：linus-next 测试报告成本

- 【Linux社区】给出实时构建与启动测试失败数据（14 个失败构建、28 个失败 qemu 用例），质问分析失败该由谁承担。 `<!-- ROW_MINE: ksummit.messages.2386 -->`

## 151.41 议题讨论：bufferhead 与高阶 folio

- 【Linux社区】纠正 Linus 的稻草人论证：给出 iomap 化后 2.5GB/s 升至 7GB/s、CPU 降 70%、bufferhead 每块 56 字节等数据，主张核心难题是不可测代码的管理，并指其言行失当。 `<!-- ROW_MINE: ksummit.messages.2389 -->`

## 151.42 议题讨论：文档构建自动选 Python 版本

- 【Linux社区】明确反对 kernel-doc 自动改用更高 Python 版本的“魔法”，质疑覆盖用户搜索路径是否妥当。 `<!-- ROW_MINE: ksummit.messages.2393 -->`

## 151.43 议题讨论：GKI 冻结后的核心改动

- 【Linux社区】分享测试中常需扩展核心内核方能解决问题的经验，指出认证流程各阶段均有时间压力。 `<!-- ROW_MINE: ksummit.messages.2400 -->`

## 151.44 议题讨论：AI 审查的局限与定位

- 【Linux社区】引 needle-in-a-haystack 研究说明长上下文失针风险（GPT-4 仅有效利用约一成窗口），支持 AI 优先服务维护者，澄清 linuxtv 爬虫属类 DDoS 自动化。 `<!-- ROW_MINE: ksummit.messages.2401 -->`

## 151.45 议题讨论：文档构建 PATH 行为定论

- 【Linux社区】总结辩论并定调：打印提示可接受，手动挑选 Python 解释器覆盖 python3 符号链接不可接受。 `<!-- ROW_MINE: ksummit.messages.2402 -->`

## 151.46 提案：Fixes 标签规则

- 【Linux社区】以发行版视角主张任何 bug 修复都应标 Fixes 而非依赖 Cc: stable，指出标注决策会迅速过时，下游可凭 Fixes 判断取舍。 `<!-- ROW_MINE: ksummit.messages.2412 -->`
