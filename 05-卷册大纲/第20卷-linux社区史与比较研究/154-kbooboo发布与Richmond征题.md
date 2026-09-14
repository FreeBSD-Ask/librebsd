154 【Linux社区】kbooboo发布与Richmond征题

> 来源：ksummit 独有 p18（50 封全读，2021-04 至 2026-08，kbooboo 崩溃工具源码发布求托管、2023 Richmond 维护者峰会 30 人征题公告、Tower of Weakenings 与 std::ptr 文档推荐、UMN media sp8870 if(err) 缺陷实证、linux-distros 7/14 天与 PoC 公开政策分歧、trivial.git 无 UMN 补丁事实声明、checkpatch Fixes 警告已加、Sphinx 缓存与分级告警五策）
> 判定：42 CAND / 8 NV。主题分布：工具讨论：bugzilla 退役 1、Rust 政策：C 聚合传参与别名模型 1、维护者峰会：自动审查机器人与倦怠 1、TAB 选举：候选人提名提醒 1、峰会议题：LLM 标签与新人洪流 1、trivial 补丁政策：UMN 实验危害确认 1、回归处理：深化维护者树质疑 1、静态分析：指针返回值语义标注 1、Rust 政策：UBSan 生产可用性反驳 1、峰会组织：混合会议与活动形式 1、MAINTAINERS 校验：CC 列表治理 1、Rust for Linux：寄存器映射 DSL 提问 1、Rust 政策：RefinedRust 与 Miri 关系澄清 1、安全披露：linux-distros 与 s@k.o 政策分歧 1、AI 代码标注：法律风险评估 1、加速器驱动：用户态接口层级争论 1、AI 代码标注：默认假设需文档化 1、设备直通：跨子系统 NAK 措辞纠正 1、AI 代码标注：算法常见度界线 1、文件系统维护：syzbot 与信任边界 1、峰会组织：疫情下线下与远程之辩 1、AI 代码标注：法律风险显性化 1、Rust for Linux：示例驱动选择之争 1、linux-next 反馈：临时提交检测工具 1、Rust 政策：Miri 能力与 LLVM 缺陷辨析 1、内核文档：构建提速与告警治理 1、峰会议题：LLM 标签信噪比与依赖风险 1、AI 与 LLM：测试代码审阅容量 1、Rust 政策：编译器标准与 C++ 路线 1、linus-next：合并前全量过 next 目标 1、维护者峰会：接口设计需弃版重来 1、Sashiko 审查模型：威胁模型文档对接 1、内核文档：SUSE 文档团队参与度 1、稳定分支标签：Fixes 强制推进 1、trivial 补丁政策：UMN media 补丁质量之辩 1、峰会组织：2023 维护者峰会征题 1、trivial 补丁政策：与 UMN 事件切割 1、Rust for Linux：引用计数编译期局限 1、峰会议题：LKML 语料微调专项模型 1、linus-next：工作流自辩与质疑 1、2021 峰会议题：UMN 议题承接 1、峰会议题：回归跟踪与修复现状 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p18 的逐封提取（2021-04 至 2026-08，42 CAND / 8 NV），全 42 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 154.1 工具讨论：bugzilla 退役

- 【Linux社区】提议为缺陷跟踪做“bug 版 patchwork”系统，每条缺陷有独立状态页并汇集相关邮件，自述 trace-cmd/kernelshark 的缺陷积压长期未清理 `<!-- ROW_MINE: ksummit.messages.2729 -->`

## 154.2 Rust 政策：C 聚合传参与别名模型

- 【Linux社区】认为对 Rust 未定义别名模型的担忧被夸大，提出“确定允许、确定 UB、尚未定夺”三分框架，并推荐 Tower of Weakenings 分层记忆模型与 std::ptr 文档作实用依据 `<!-- ROW_MINE: ksummit.messages.2734 -->`

## 154.3 维护者峰会：自动审查机器人与倦怠

- 【Linux社区】反驳机器人只报告不评判即可减负的设想，指出审阅者仍需逐条处理机器人报告，担心提交者反复刷未准备好的补丁，提议设暂存列表承接 `<!-- ROW_MINE: ksummit.messages.2737 -->`

## 154.4 TAB 选举：候选人提名提醒

- 【Linux社区】重发 TAB 选举提名征集全文并提醒 9 月 20 日硬截止，重列资格标准（2020-2021 年三枚带签章 tag 的主线/稳定提交）与本届任期将满的五人名单 `<!-- ROW_MINE: ksummit.messages.2738 -->`

## 154.5 峰会议题：LLM 标签与新人洪流

- 【Linux社区】主张 Assisted-by 标签不必列具体产品名仍有价值；警告 LLM 新人跨数十子系统大改而维护者承载力不足；重提对专有审查工具（Sashiko 类）撤资风险的担忧 `<!-- ROW_MINE: ksummit.messages.2740 -->`

## 154.6 trivial 补丁政策：UMN 实验危害确认

- 【Linux社区】确认所举 UMN 实验 patch（mlx5 缺失检查）确实引入 UAF 且问题在后续 commit 中才被修复，为 UMN 补丁的实际危害提供第一手事实 `<!-- ROW_MINE: ksummit.messages.2741 -->`

## 154.7 回归处理：深化维护者树质疑

- 【Linux社区】以自身经验反驳以更深维护者树缓解维护者压力的提案，认为层级间传递补丁本身即引入延迟，集体维护制只能缓解休假不能缓解稳定期 `<!-- ROW_MINE: ksummit.messages.2744 -->`

## 154.8 静态分析：指针返回值语义标注

- 【Linux社区】主张内核对 NULL 与 ERR_PTR 返回语义缺乏标准化是缺陷与痛点之源，即便无法全局统一，也应让开发者无需深挖调用栈即可查知各函数语义 `<!-- ROW_MINE: ksummit.messages.2748 -->`

## 154.9 Rust 政策：UBSan 生产可用性反驳

- 【Linux社区】引用 Clang 官方文档“存在适合生产环境的最小 UBSan runtime”反驳 sanitizer 不可用于生产的断言，并指对方批评未针对其原论点 `<!-- ROW_MINE: ksummit.messages.2749 -->`

## 154.10 峰会组织：混合会议与活动形式

- 【Linux社区】就混合会议包容性给出在末页幻灯片列出会后讨论渠道（列表、IRC、Matrix、私人邮箱）的具体做法，主张会议与黑客松分开办、以更频繁的小型专题活动取代大型联合活动 `<!-- ROW_MINE: ksummit.messages.2755 -->`

## 154.11 MAINTAINERS 校验：CC 列表治理

- 【Linux社区】认为“教育”不能解决 MAINTAINERS 条目失准，数千开发者无人能尽知其动向与动机；自述按人名手动删 CC，并指出 netdev 与 wireless 的划分最令人困惑 `<!-- ROW_MINE: ksummit.messages.2757 -->`

## 154.12 Rust for Linux：寄存器映射 DSL 提问

- 【Linux社区】针对 memory_map! 宏示例追问能否表达与 CPU 无关的大端寄存器访问，指出 readl/writel 类宏的字节序交换需求是该 API 设计必须覆盖的场景 `<!-- ROW_MINE: ksummit.messages.2758 -->`

## 154.13 Rust 政策：RefinedRust 与 Miri 关系澄清

- 【Linux社区】澄清 RefinedRust 核心基于其 RustBelt 博士论文的 Coq 形式化借检工作，并非复用 Miri 的 UB 检查与抽象机，至多共用 rustc MIR 提取逻辑或测试用例 `<!-- ROW_MINE: ksummit.messages.2763 -->`

## 154.14 安全披露：linux-distros 与 s@k.o 政策分歧

- 【Linux社区】梳理两处政策冲突（修复就绪后 7 天 vs 通知后 14 天强制披露、共享给列表的 PoC 是否须公开），提议在 oss-security 公开讨论，并纠正文档中 linux-distros 规则无助修复的误导措辞 `<!-- ROW_MINE: ksummit.messages.2765 -->`

## 154.15 AI 代码标注：法律风险评估

- 【Linux社区】给出 GitHub 训练语料约六成宽松许可、两成五 GPL、一成五不明的构成估计，认为 copyleft 项目采用 AI 风险低收益高，预测基础模型终将声明以宽松许可代码训练 `<!-- ROW_MINE: ksummit.messages.2767 -->`

## 154.16 加速器驱动：用户态接口层级争论

- 【Linux社区】归纳支持固定功能内核接口的两个理由（通用化使现有用户态开箱即用、厂商借闭源固件换取上游驱动），并以低成本嵌入式 SoC 场景反驳 AI 加速器必然走向完全共享编程模型的判断 `<!-- ROW_MINE: ksummit.messages.2769 -->`

## 154.17 AI 代码标注：默认假设需文档化

- 【Linux社区】主张需把“收到的补丁默认被作者与提交者真正理解”这一隐含假设明确文档化，因 LLM 使大规模无人理解的提交成为可能；引 maintainer-tip.rst 的 SOB 链条规则讨论是否推广到全内核 `<!-- ROW_MINE: ksummit.messages.2776 -->`

## 154.18 设备直通：跨子系统 NAK 措辞纠正

- 【Linux社区】要求停用“跨子系统 NAK”提法以免误读为网络层阻止 RDMA/存储新功能，指问题实质是 nVidia 将专有网关包装为可进各子系统的 misc 驱动，受影响子系统应均有发言权 `<!-- ROW_MINE: ksummit.messages.2778 -->`

## 154.19 AI 代码标注：算法常见度界线

- 【Linux社区】赞同“请 AI 代工成品交作己用属欺骗”的界线，补充以广见于教科书与 GPL 范例的常见算法（如快速排序）可接受，而最前沿新算法则成问题的区分标准 `<!-- ROW_MINE: ksummit.messages.2781 -->`

## 154.20 文件系统维护：syzbot 与信任边界

- 【Linux社区】阐明实际共识假设是处理不可信输入的代码须能经受 syzbot 模糊测试而非通过即安全；指出 Linus 已 NACK 删除缺维护文件系统的做法，故将此程序性难题提交峰会正式讨论 `<!-- ROW_MINE: ksummit.messages.2787 -->`

## 154.21 峰会组织：疫情下线下与远程之辩

- 【Linux社区】主张只要线下价值更高即不应因出行恐惧者自我设限，反对把所有人压到最低公分母；指出远程亦非最优（亚非低带宽人群被排斥），提议以地理分散 meetup 试水重启社交面 `<!-- ROW_MINE: ksummit.messages.2791 -->`

## 154.22 AI 代码标注：法律风险显性化

- 【Linux社区】提议以“Legal-risk-by”类显性标签替代 Assisted-by，使应用补丁与转发 pull request 者无法以不知情推脱法律风险，呼应诉讼未决期应谨慎的立场 `<!-- ROW_MINE: ksummit.messages.2822 -->`

## 154.23 Rust for Linux：示例驱动选择之争

- 【Linux社区】反驳以 virtio 设备作 Rust 驱动展示的建议，质问多少内核维护者写过 virtio 驱动，坚持应选真实硬件驱动方能检验语言可行性 `<!-- ROW_MINE: ksummit.messages.2826 -->`

## 154.24 linux-next 反馈：临时提交检测工具

- 【Linux社区】指出 soc 树已用 Krzysztof 的脚本与 git 钩子检测 ephemeral 提交、易推广复用但缺宣传，并评估以提交量计 linux-next 的错误率其实很低 `<!-- ROW_MINE: ksummit.messages.2828 -->`

## 154.25 Rust 政策：Miri 能力与 LLVM 缺陷辨析

- 【Linux社区】以 LLVM issue 22099 辨析严格别名缺陷现状（原测试例已修复但换用分配内存或 void 指针可复现），接受 Miri 优于 sanitizer 但仅覆盖已测路径的限定，并追问 Rust 新类型系统与求解器的兼容计划 `<!-- ROW_MINE: ksummit.messages.2829 -->`

## 154.26 内核文档：构建提速与告警治理

- 【Linux社区】系统提出提速与减警方案：放宽 Sphinx 最低版本、按文档缓存 kernel-doc 解析结果、改用 rst 原生 field list、默认并行构建，以及 W=1 入常规构建、kernel-doc 分级告警等 `<!-- ROW_MINE: ksummit.messages.2833 -->`

## 154.27 峰会议题：LLM 标签信噪比与依赖风险

- 【Linux社区】澄清支持标签者意在提高警惕而非放松审查，记录“按使用方式而非模型名”的共识倾向；批评三类 LLM 用户造成的复审时间浪费并提出超限暂停受理的 nack 构想，认同对 Sashiko 类工具的依赖已影响吞吐 `<!-- ROW_MINE: ksummit.messages.2834 -->`

## 154.28 AI 与 LLM：测试代码审阅容量

- 【Linux社区】同意以测试数据生成为更安全的边界，提出审阅测试代码者是有限资源、LLM 引发的补丁潮会构成额外负担的现实约束 `<!-- ROW_MINE: ksummit.messages.2836 -->`

## 154.29 Rust 政策：编译器标准与 C++ 路线

- 【Linux社区】主张 Rust 被施以远低于 C 的兼容标准并反推 Rust-only 代码若同等对待应推迟到 2034 年，重申以 C++14/17（C 近超集、类型安全链接、机械转换可行）编译整个内核的替代路线 `<!-- ROW_MINE: ksummit.messages.2844 -->`

## 154.30 linus-next：合并前全量过 next 目标

- 【Linux社区】支持“-rc1 后所有 PR 均先经 linux-next 浸泡”为目标，以 scsi-fixes 也进 next 的实例反驳“紧急修复分支不影响他人”的假设，并提醒首发想到的修复未必是最佳修复 `<!-- ROW_MINE: ksummit.messages.2847 -->`

## 154.31 维护者峰会：接口设计需弃版重来

- 【Linux社区】以 pin control 与 GPIO 字符设备首版均被推翻为例印证《人月神话》“总要扔掉一版”的规律，回顾 2012 ELC 白板式多厂商委员会设计出 v2 的经验，主张线下集中关键人物仍值得尝试 `<!-- ROW_MINE: ksummit.messages.2850 -->`

## 154.32 Sashiko 审查模型：威胁模型文档对接

- 【Linux社区】指出 Documentation/process/threat-model.rst 已大体包含所需内容但 Sashiko 未据此行动，追问 AI 审查工具的提示词应直接注入规则还是指引其阅读该文件 `<!-- ROW_MINE: ksummit.messages.2851 -->`

## 154.33 内核文档：SUSE 文档团队参与度

- 【Linux社区】已将外部协助请求转发 SUSE 文档团队，并分析其被内部产品文档与翻译任务挤占、并非内核文档直接消费者的现状，指出开发者才是上游技术文档的初稿作者 `<!-- ROW_MINE: ksummit.messages.2852 -->`

## 154.34 稳定分支标签：Fixes 强制推进

- 【Linux社区】反驳“太难”可作不加 Fixes 的借口（子系统专家最有条件判断），报告已加 checkpatch 警告并计划逐一向维护者索要 Fixes 标签（经 patch.msgid.link 供稳定工具拾取），主张 pre-git 补丁也应标 Fixes: 1da177e4c3f4 `<!-- ROW_MINE: ksummit.messages.2859 -->`

## 154.35 trivial 补丁政策：UMN media 补丁质量之辩

- 【Linux社区】以 sp8870_readreg 返回值检查误用 if (err) 而非 if (err < 0) 的具体缺陷，反驳“media 侧 29 个 UMN 补丁无恶意且多有效”的总体评价，实证至少一个补丁引入真 bug `<!-- ROW_MINE: ksummit.messages.2866 -->`

## 154.36 峰会组织：2023 维护者峰会征题

- 【Linux社区】正式发布 2023 年里士满维护者峰会征题公告：11 月 16 日举行、仅邀 30 人、以 [MAINTAINERS SUMMIT] 前缀发 ksummit 列表提议题即入计划委员会考量，列五人组委会与往届 LWN 纪要链接 `<!-- ROW_MINE: ksummit.messages.2867 -->`

## 154.37 trivial 补丁政策：与 UMN 事件切割

- 【Linux社区】以 trivial.git 事实维护者身份表态支持讨论受理政策但反对将其与 UMN 事件直接挂钩，并提供“无任何 umn.edu 补丁经 trivial 树合入”的关键事实 `<!-- ROW_MINE: ksummit.messages.2871 -->`

## 154.38 Rust for Linux：引用计数编译期局限

- 【Linux社区】分析 Rust 的安全保证来自独占分配跟踪而引用计数场景保证大幅弱化，至多如 kasan 运行时检出 use-after-free；编译期跟踪需语义化编码生命周期规则，即便投入博士也恐复杂到不可用 `<!-- ROW_MINE: ksummit.messages.2877 -->`

## 154.39 峰会议题：LKML 语料微调专项模型

- 【Linux社区】回应开源权重模型微调设想：需大量调参且不可直接喂未过滤 LKML 存档（避免学到 2.6 时代风格），建议借 cregit 识别被接受补丁集反向构建语料子集，并预言 2025 年后补丁默认疑为 LLM 所写 `<!-- ROW_MINE: ksummit.messages.2879 -->`

## 154.40 linus-next：工作流自辩与质疑

- 【Linux社区】详述自身全经邮件列表加 patchwork 的公开流程（修复后再以 for-next/for-linus 标签重发），反问将修复推入 linux-next 一两天能带来什么，并指出其所修 bug 恰是 next 阶段未测出者 `<!-- ROW_MINE: ksummit.messages.2880 -->`

## 154.41 2021 峰会议题：UMN 议题承接

- 【Linux社区】对 Ted 提案预设“下次该做点不同”的措辞提出微讽后，同意在峰会就明尼苏达大学事件作非技术性综述并展开讨论，属议题征集过程中的承接记录 `<!-- ROW_MINE: ksummit.messages.2882 -->`

## 154.42 峰会议题：回归跟踪与修复现状

- 【Linux社区】提出与内核峰会配套的维护者峰会续场议程：主线回归修复滞留 -next 数周、bugzilla 报告未转发维护者、CI 报告是否纳入 regzbot、回归跟踪工作方式是否需调整 `<!-- ROW_MINE: ksummit.messages.2885 -->`
