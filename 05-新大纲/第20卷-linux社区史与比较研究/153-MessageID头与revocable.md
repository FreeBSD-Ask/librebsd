# 153 【Linux社区】MessageID头与revocable

> 来源：ksummit 独有 p17（50 封全读，2021-04 至 2026-08，Ted 提议 Message-ID 头替代 Link:、Shih revocable 可撤销资源机制 ChromeOS EC 实证、Airlie 峰会=Linus 员工会议论、Greg KH 车企芯片公司 stable 审计失败案例与 Google 90% 覆盖数据、Rostedt WRITE_ONCE 防撕裂规则、Wedson 弱引用升级即 refcount_inc_not_zero、tip 树主题分支拉取合流范例）
> 判定：46 CAND / 4 NV。主题分布：Link trailer 替代方案 1、议题讨论：加速器用户态 API 设计方法论 1、议题讨论：linus-next 树提案评估 1、议题提案：revocable 机制防 use-after-free 1、议题讨论：C 整数溢出与饱和运算 1、流程记录：stable 合并窗口排队澄清 1、补丁评审：Link trailer 注释格式 1、议题讨论：提交与讨论可靠映射 1、议题讨论：Rust 抽象与全局重构 1、补丁评审：kallsyms 行号表边界 1、治理立场：维护者峰会性质 1、议题讨论：新人补丁应基于哪棵树 1、议题讨论：AI 评审的法律风险反驳 1、议题讨论：AI 评审工具目标定位 1、治理立场：Bugzilla 去留 1、议题讨论：linus-next 失败定位 1、议题讨论：Rust 弱引用升级语义 1、议题讨论：ISP 驱动 DRM 与 V4L2 路线之争 1、议题讨论：编译器重复读全局规则 1、议题讨论：无 Fixes 标签补丁为何进 stable 1、议题讨论：AI 逐字复制风险 1、议题讨论：文件系统信任模型与维护策略 1、治理立场：Bugzilla 维护现状 1、治理立场：全量采用 stable 修复 1、议题讨论：unwinding 与 stack walking 辨析 1、议题讨论：Rust 规范依赖澄清 1、议题讨论：UALink 上游策略回应 1、议题讨论：b4 ai dig 目标说明 1、数据：kernel-doc 构建耗时 1、议题讨论：变量声明位置规则反驳 1、议题讨论：厂商直通与小众设备 1、议题讨论：本地小模型评审可行性 1、流程记录：主题分支与 PR 工作流 1、议题讨论：Rust 工具链架构覆盖 1、议题讨论：htmldocs 构建性能 1、补丁评审：工具生成内容文档措辞 1、议题讨论：pre-git 历史 Fixes 标签 1、补丁评审：Link 注释格式文档一致性 1、议题讨论：Rust GPIO 驱动切入点 1、议题讨论：highmem 淘汰假设修正 1、补丁评审：工具生成内容增量补丁 1、议题讨论：stable 回归修复义务反驳 1、议题讨论：Rust 兼容性保证修正 1、议题讨论：KTODO 与既有任务源差异 1、议题讨论：web 表单报障优势 1、议题讨论：base-commit 指定语义 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p17 的逐封提取（2021-04 至 2026-08，46 CAND / 4 NV），全 46 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 153.1 Link trailer 替代方案

- 【Linux社区】提议以 Message-ID 头替代 Link: 标签，raw 消息号 Patchwork 可直接获取，回应 rostedt 对 patchwork 可见性的需求 `<!-- ROW_MINE: ksummit.messages.2570 -->`

## 153.2 议题讨论：加速器用户态 API 设计方法论

- 【Linux社区】反对“API 必须一次设计对”前提，主张 fail fast 迭代重做、先求最小操作集、API 版本化，并可推荐复用既有接口 `<!-- ROW_MINE: ksummit.messages.2571 -->`

## 153.3 议题讨论：linus-next 树提案评估

- 【Linux社区】质疑 PR 后期测试时机与覆盖集中在周期末尾、连续树 bisection 利弊、坏补丁被 rebase 后的人工处理流程，另提议按稳定度再拆分 -next `<!-- ROW_MINE: ksummit.messages.2575 -->`

## 153.4 议题提案：revocable 机制防 use-after-free

- 【Linux社区】提出资源提供方可撤销访问的通用机制，已在 ChromeOS EC 驱动修复真实 UAF，附此前 LPC 演讲与补丁链接；自述漏交网站第二步提交 `<!-- ROW_MINE: ksummit.messages.2577 -->`

## 153.5 议题讨论：C 整数溢出与饱和运算

- 【Linux社区】说明内核 -fwrapv 下有符号溢出已定义故只查无符号，提议 saturate_math 宏替代嵌套 size_add，解释 kmalloc 溢出致内存损坏场景 `<!-- ROW_MINE: ksummit.messages.2579 -->`

## 153.6 流程记录：stable 合并窗口排队澄清

- 【Linux社区】更正自己此前说法：合并窗口期间并无持续排入 stable 补丁的树，当时无暇处理，回应 leemhuis 的核查 `<!-- ROW_MINE: ksummit.messages.2581 -->`

## 153.7 补丁评审：Link trailer 注释格式

- 【Linux社区】指出“# 注释”写法与既有两种 trailer 注释机制不一致，主张 Link 等所有 trailer 统一采用其一 `<!-- ROW_MINE: ksummit.messages.2584 -->`

## 153.8 议题讨论：提交与讨论可靠映射

- 【Linux社区】认为仅靠既有 trailer 不够，除非新增 Submission: 标签指向 lore 原始补丁，且需让开发者看到明确收益才会采用 `<!-- ROW_MINE: ksummit.messages.2590 -->`

## 153.9 议题讨论：Rust 抽象与全局重构

- 【Linux社区】主张变更经维护者且其需懂 Rust；树级重构者至少需基本 Rust 知识；希望第二语言尽量多人在一定时间内参与 `<!-- ROW_MINE: ksummit.messages.2596 -->`

## 153.10 补丁评审：kallsyms 行号表边界

- 【Linux社区】质疑 addr 高于 _text 时偏移截断为 u32 的风险，追问是否被 __sprint_symbol 前置检查排除 `<!-- ROW_MINE: ksummit.messages.2600 -->`

## 153.11 治理立场：维护者峰会性质

- 【Linux社区】峰会实为“Linus 的员工会议”，无技术内容亦无投票；否认小圈子观感但承认与 in-group 实质等同；反对按 M: 条目投票定议题 `<!-- ROW_MINE: ksummit.messages.2607 -->`

## 153.12 议题讨论：新人补丁应基于哪棵树

- 【Linux社区】多数子系统接受基于 linux-next 的补丁；net/bpf 等例外需主题标注目标树；针对 LTS 分支提交违反 stable 规则 `<!-- ROW_MINE: ksummit.messages.2610 -->`

## 153.13 议题讨论：AI 评审的法律风险反驳

- 【Linux社区】反驳“仅评审无法律问题”：版权不止覆盖代码，引在诉案件与 Napster 类比 `<!-- ROW_MINE: ksummit.messages.2615 -->`

## 153.14 议题讨论：AI 评审工具目标定位

- 【Linux社区】认为工具上线后低质 v1 减少反而降低上游流量；维护者需信任明显错误已被过滤；回应工具应面向所有人而非仅维护者 `<!-- ROW_MINE: ksummit.messages.2618 -->`

## 153.15 治理立场：Bugzilla 去留

- 【Linux社区】以日均约四封报错流量质疑工具存续价值，建议直接停用或改为各子系统列表收件，且仍需人维护 `<!-- ROW_MINE: ksummit.messages.2621 -->`

## 153.16 议题讨论：linus-next 失败定位

- 【Linux社区】认为只有自动化而非人工定位引入失败的树才可行，否则人力会耗尽；怀疑测试延迟使其不现实 `<!-- ROW_MINE: ksummit.messages.2623 -->`

## 153.17 议题讨论：Rust 弱引用升级语义

- 【Linux社区】解释升级即 refcount_inc_not_zero，成功表示强计数非零；失败表示对象已消亡但内存保留以免 UAF `<!-- ROW_MINE: ksummit.messages.2624 -->`

## 153.18 议题讨论：ISP 驱动 DRM 与 V4L2 路线之争

- 【Linux社区】对比 DRM 自定义 IOCTL 命令缓冲与 V4L2 全寄存器文档化；称抵制致 99% 摄像头驱动在树外，主张混合模型并交社区统一标准 `<!-- ROW_MINE: ksummit.messages.2625 -->`

## 153.19 议题讨论：编译器重复读全局规则

- 【Linux社区】归纳编译器不得超出代码规定多读全局、代码多次读则可缓存；WRITE_ONCE 常用于防写撕裂 `<!-- ROW_MINE: ksummit.messages.2627 -->`

## 153.20 议题讨论：无 Fixes 标签补丁为何进 stable

- 【Linux社区】列四类原因：该标未标（如 syzbot）、事后才知是修复、加 PCI ID、依赖清理补丁先行，附实例链接 `<!-- ROW_MINE: ksummit.messages.2631 -->`

## 153.21 议题讨论：AI 逐字复制风险

- 【Linux社区】反驳“AI 如人阅读”论：AI 程序可能逐字复制受限内容，且无法像人那样被追问是否照抄并可信作答 `<!-- ROW_MINE: ksummit.messages.2632 -->`

## 153.22 议题讨论：文件系统信任模型与维护策略

- 【Linux社区】syzbot 模糊测试不等于抗恶意输入，合法范围内的元数据篡改无法检测；无人维护文件系统建议循驱动惯例改 API 并标 CONFIG_BROKEN `<!-- ROW_MINE: ksummit.messages.2637 -->`

## 153.23 治理立场：Bugzilla 维护现状

- 【Linux社区】反驳零成本论：每日 5-10 分钟删垃圾还写了脚本；版本 5.1.1 并非陈旧；症结是无人愿做无聊工作而非工具 `<!-- ROW_MINE: ksummit.messages.2639 -->`

## 153.24 治理立场：全量采用 stable 修复

- 【Linux社区】以大芯片公司与车企审计失败案例及 Google 两年数据证明全取 stable 修复可覆盖 90%+ 已知漏洞，主张企业内核旧发布模式错误 `<!-- ROW_MINE: ksummit.messages.2641 -->`

## 153.25 议题讨论：unwinding 与 stack walking 辨析

- 【Linux社区】指出内核所谓“unwinding”在编译器界称“stack walking”，任务更简单，术语混淆或为 Rust 讨论分歧来源 `<!-- ROW_MINE: ksummit.messages.2648 -->`

## 153.26 议题讨论：Rust 规范依赖澄清

- 【Linux社区】别名规则并非官方绑定 LLVM，规范互相引用是常态；内核 Rust panic 不展开栈 `<!-- ROW_MINE: ksummit.messages.2654 -->`

## 153.27 议题讨论：UALink 上游策略回应

- 【Linux社区】质疑为何不立即提交补丁而等到十二月，提醒保密脚注须先移除才能发公共列表 `<!-- ROW_MINE: ksummit.messages.2655 -->`

## 153.28 议题讨论：b4 ai dig 目标说明

- 【Linux社区】目标不止找原始提交，而是挖掘补丁前后所有相关讨论线程；b4 dig 模糊匹配会搜错，AI 版更进一步 `<!-- ROW_MINE: ksummit.messages.2659 -->`

## 153.29 数据：kernel-doc 构建耗时

- 【Linux社区】实测 Ryzen 9 7900 上 kernel-doc 约 32 秒，受 GIL 无法并行，Python 去 GIL 后可恢复并行补丁 `<!-- ROW_MINE: ksummit.messages.2660 -->`

## 153.30 议题讨论：变量声明位置规则反驳

- 【Linux社区】反对“尽量低声明”硬规则：定义与赋值分离更可维护，RAII 变量例外合并；认可 include 按字母排序 `<!-- ROW_MINE: ksummit.messages.2661 -->`

## 153.31 议题讨论：厂商直通与小众设备

- 【Linux社区】赞同逆向工程由市场力量自筛选；小厂无力移植致设备在 Linux 上不可用，大市场份额厂商更有动力开源 `<!-- ROW_MINE: ksummit.messages.2667 -->`

## 153.32 议题讨论：本地小模型评审可行性

- 【Linux社区】实测 qwen3.6 36B（3B 激活）生成辅助脚本质量接近大模型；提出达前沿模型 80%-90% 质量即值得本地化，主张蒸馏小模型并试跑 Sashiko `<!-- ROW_MINE: ksummit.messages.2669 -->`

## 153.33 流程记录：主题分支与 PR 工作流

- 【Linux社区】按 Linus 建议拆分主题分支避免一处被拒整体 rebase；更新多直接自 patchwork 拉入；tip 树以拉取而非 cherry-pick 合流 `<!-- ROW_MINE: ksummit.messages.2675 -->`

## 153.34 议题讨论：Rust 工具链架构覆盖

- 【Linux社区】列出 rustc 平台支持与缺 stdlib 的架构；追问 rustc_codegen_gcc 版本与架构组合数及 libgccjit ABI 跨版本稳定性 `<!-- ROW_MINE: ksummit.messages.2682 -->`

## 153.35 议题讨论：htmldocs 构建性能

- 【Linux社区】自述 capable 桌面机约 3 分钟可完成 htmldocs，反推对方环境异常，建议升级 Sphinx 8 修复性能问题 `<!-- ROW_MINE: ksummit.messages.2684 -->`

## 153.36 补丁评审：工具生成内容文档措辞

- 【Linux社区】认为对方措辞显“不悦”，提出替代表述：工具易犯与人类不同的错误，维护者可要求证明生成代码已验证 `<!-- ROW_MINE: ksummit.messages.2685 -->`

## 153.37 议题讨论：pre-git 历史 Fixes 标签

- 【Linux社区】反对为 2005 年前引入的缺陷翻 history 树定位提交，称到那程度只是学术练习 `<!-- ROW_MINE: ksummit.messages.2687 -->`

## 153.38 补丁评审：Link 注释格式文档一致性

- 【Linux社区】查得 5.Posting.rst 示例无“# ”，为免文档互相矛盾主张该补丁不应合入除非一并修订 `<!-- ROW_MINE: ksummit.messages.2689 -->`

## 153.39 议题讨论：Rust GPIO 驱动切入点

- 【Linux社区】建议选无内核支持的 I2C/SPI 扩展器用 Rust 实现；提示 PL061 所在 ARMv4T 仅 GCC 支持会增加难度 `<!-- ROW_MINE: ksummit.messages.2692 -->`

## 153.40 议题讨论：highmem 淘汰假设修正

- 【Linux社区】反驳 Arnd 假设：1GB 内存的系统同样用 highmem，且 1GB 是 32 位后期主流配置 `<!-- ROW_MINE: ksummit.messages.2696 -->`

## 153.41 补丁评审：工具生成内容增量补丁

- 【Linux社区】提交 8 行增量补丁：全自动生成系列应预期额外审查；维护者不容忍 slop，无法解释者可能被整系列拒收 `<!-- ROW_MINE: ksummit.messages.2705 -->`

## 153.42 议题讨论：stable 回归修复义务反驳

- 【Linux社区】反对强制 Fixes 加 CC stable：AUTOSEL 已多取、Fixes 标签灌水已成风气；质疑用户直接使用内核发布的普遍性 `<!-- ROW_MINE: ksummit.messages.2706 -->`

## 153.43 议题讨论：Rust 兼容性保证修正

- 【Linux社区】指出 Rust 官方保证也允许因类型推断变更破坏兼容（time crate 事件先例） `<!-- ROW_MINE: ksummit.messages.2715 -->`

## 153.44 议题讨论：KTODO 与既有任务源差异

- 【Linux社区】区分 bot 扫出的 bug 清单与功能增强清单，以 ring buffer 一批 nice to have 小增强为例说明 KTODO 定位 `<!-- ROW_MINE: ksummit.messages.2722 -->`

## 153.45 议题讨论：web 表单报障优势

- 【Linux社区】列举 web 界面可结构化收集内核版本、是否回归、复现步骤、完整控制台日志等，邮件常需多轮往返 `<!-- ROW_MINE: ksummit.messages.2724 -->`

## 153.46 议题讨论：base-commit 指定语义

- 【Linux社区】追问强制 base commit 是否会误导想应用于更早基线者；认为仅确需特定基线时才应作硬性要求 `<!-- ROW_MINE: ksummit.messages.2725 -->`
