# 89 【Linux社区】Rust大辩论与背光uAPI

> 来源：ksummit-discuss p141（50 封全读，2014-05-04 至 2022-06-20，2022 Rust 大辩论主线、文档与 Sphinx 议题、背光 uAPI 提案与 policy 之争、2014 测试标准与 PM 依赖档案线）
> 判定：46 CAND / 4 NV。主题分布：门控与企业内核滞后 1、峰会列表地址混乱 1、eBPF紧耦合价值疑 1、HID-BPF稳定性契约 1、eBPF避免新增API 1、类Windows过滤驱动 1、旧列表应关闭改向 1、文档愿景议题提案 1、建文档需求登记处 1、Sphinx缺陷与构建 1、rustdoc转ReST 1、Rust维护面议题扩展 1、峰会规模碍讨论 1、hch评Rust利弊 1、Rust门槛与倦怠 1、Rust反C偏见论 1、斥担忧为精英主义 1、生命周期管理欠账 1、灾难担忧之辩 1、Rust实验可逆论 1、过于恐惧之问 1、无响应维护者流程 1、Rust是否过早 1、Rust动能论 1、背光新uAPI提案 1、policy归属之争 1、eBPF非ABI后门 1、显隐资源管理之辨 1、何谓复杂PM 1、genpd简化工程 1、测试标准议题提案 1、启动农场扩容议 1、平台去留三选项 1、两段式DT迁移 1、ACPI载DT三层次 1、平台头文件清理 1、XScale归类之议 1、非企业发行版反驳 1、rebase之痛权衡 1、Fedora回归测试框架 1、复杂PM平台界定 1、distro测试自荐 1、农场扩容与测试目标 1、qemu启动测试现状 1、主动被动ACPI之辨 1、属性APIchurn之辩 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p141（实锚 pk 351256-351305）的逐封提取（46 CAND / 4 NV），全 46 块采用**单行摘要体例**（丙型）：每块由“## 89.x 题名”与若干“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 89.1 门控与企业内核滞后

- 【Linux社区】Greg KH 论断多数用户要等数年后企业内核才用上新特性，并以 cgroups 接口“发现太糟时用户已依赖、须无限期保留”为例证 ABI 难收回 `<!-- ROW_MINE: ksummit-discuss.messages.351256 -->`

## 89.2 峰会列表地址混乱

- 【Linux社区】Hans 指出 2022 CFP 写旧列表 ksummit-discuss 而 LPC 官网指示投 ksummit@lists.linux.dev，其背光议题投稿两边悬置待澄清 `<!-- ROW_MINE: ksummit-discuss.messages.351257 -->`

## 89.3 eBPF紧耦合价值疑

- 【Linux社区】Jan Kara 质问紧耦合 eBPF 较普通模块钩子优势何在，自述 eBPF 多用于“不合上游”的调试微调 `<!-- ROW_MINE: ksummit-discuss.messages.351258 -->`

## 89.4 HID-BPF稳定性契约

- 【Linux社区】Tissoires 阐明 HID-BPF：udev 自动加载字节码加速用户测试，钩子稳定性仅是维护者与用户的个人契约而非全社区 ABI 保证 `<!-- ROW_MINE: ksummit-discuss.messages.351259 -->`

## 89.5 eBPF避免新增API

- 【Linux社区】Hans 追问后 Tissoires 确认：eBPF 意在取代单用户的 sysfs 属性与模块参数，“并非用 eBPF 实现新 API” `<!-- ROW_MINE: ksummit-discuss.messages.351260 -->`

## 89.6 类Windows过滤驱动

- 【Linux社区】Hans 提出类比：HID-BPF 近乎 Windows HID filter drivers，与 BPF 包过滤传统相通 `<!-- ROW_MINE: ksummit-discuss.messages.351261 -->`

## 89.7 旧列表应关闭改向

- 【Linux社区】Konstantin 建议关闭 ksummit-discuss 旧列表并设自动应答指路新列表，指混乱源于照抄未更新地址的旧说明 `<!-- ROW_MINE: ksummit-discuss.messages.351262 -->`

## 89.8 文档愿景议题提案

- 【Linux社区】Corbet 提 [TECH TOPIC]：Documentation/ 总体结构、降低改进门槛、Sphinx 期望、构建系统去丑、rustdoc 集成与部落知识 `<!-- ROW_MINE: ksummit-discuss.messages.351263 -->`

## 89.9 建文档需求登记处

- 【Linux社区】Laurent 建议设文档愿望登记处，讥 runtime_pm.rst 读来“如微积分博士论文”而读者只想学会加法 `<!-- ROW_MINE: ksummit-discuss.messages.351264 -->`

## 89.10 Sphinx缺陷与构建

- 【Linux社区】Mauro 详列 per-C-type domain 交叉引用破损（Sphinx 3.1 起补丁至今未合）、intersphinx 未用、构建耗时、kernel-doc 简化 `<!-- ROW_MINE: ksummit-discuss.messages.351265 -->`

## 89.11 rustdoc转ReST

- 【Linux社区】Mauro 澄清主张 rustdoc 生成 ReST 供内核文档像 kerneldoc 嵌入，兼顾 html/epub/pdf 三种输出格式 `<!-- ROW_MINE: ksummit-discuss.messages.351266 -->`

## 89.12 Rust维护面议题扩展

- 【Linux社区】Laurent 要求在技术议题之外讨论 Rust 对内核整体维护的影响，超出演纳式早期采用者范围 `<!-- ROW_MINE: ksummit-discuss.messages.351268 -->`

## 89.13 峰会规模碍讨论

- 【Linux社区】Laurent 自补：该议题或宜入 Maintainers Summit，但担心 30 人受邀规模受众太窄 `<!-- ROW_MINE: ksummit-discuss.messages.351269 -->`

## 89.14 hch评Rust利弊

- 【Linux社区】hch 自述喜类型安全与所有权模型、厌“cargo cult of vendoring”，讥 showcase binder“本该一开始就在用户态” `<!-- ROW_MINE: ksummit-discuss.messages.351270 -->`

## 89.15 Rust门槛与倦怠

- 【Linux社区】Laurent 提出 Rust 编译器将宣告部分开发者无技能写内核，须给出路，且社区已过劳易 burnout `<!-- ROW_MINE: ksummit-discuss.messages.351271 -->`

## 89.16 Rust反C偏见论

- 【Linux社区】Bottomley 断言 Rust 有“anti-C bias”刻意异于 C 徒增学习曲线，但预测有 Rust 补丁的子系统审阅者会迅速变 Rust 流利 `<!-- ROW_MINE: ksummit-discuss.messages.351272 -->`

## 89.17 斥担忧为精英主义

- 【Linux社区】Axboe 称 Laurent 论调“weirdly elitist”劝其重新校准，指各子系统维护者负载悬殊将影响 Rust 采用意愿与能力 `<!-- ROW_MINE: ksummit-discuss.messages.351273 -->`

## 89.18 生命周期管理欠账

- 【Linux社区】Laurent 反驳反 C 说，指内核普遍忽视对象生命周期（devm_kzalloc 分配可被用户态触及的私有数据例），忧 Rust 长期成贡献门槛 `<!-- ROW_MINE: ksummit-discuss.messages.351274 -->`

## 89.19 灾难担忧之辩

- 【Linux社区】Laurent 回应精英主义指责：坚称不深思或“导致灾难”，不接受侥幸推进，欢迎被证明担忧无据 `<!-- ROW_MINE: ksummit-discuss.messages.351275 -->`

## 89.20 Rust实验可逆论

- 【Linux社区】Bottomley 主张先让志愿者试一年再评估、败则“quickly excised”，引 devfs 先例，最坏情形需“有主见者掌树”做决断 `<!-- ROW_MINE: ksummit-discuss.messages.351276 -->`

## 89.21 过于恐惧之问

- 【Linux社区】Bottomley 另立 [MAINTAINERS SUMMIT] 议题：内核渐成“creeping cancer of inertia”，ABI 永续恐惧扼杀创新，须温习犯错翻盘史 `<!-- ROW_MINE: ksummit-discuss.messages.351277 -->`

## 89.22 无响应维护者流程

- 【Linux社区】Dan Carpenter 总结惯例：一月 ping、二月改走 Andrew 树，被 NAK 后只能树外携带补丁，评审人稀缺是真难题 `<!-- ROW_MINE: ksummit-discuss.messages.351278 -->`

## 89.23 Rust是否过早

- 【Linux社区】Geert 质疑 Rust 是否来得太早，更类 C 的同范式安全语言或已在萌芽 `<!-- ROW_MINE: ksummit-discuss.messages.351279 -->`

## 89.24 Rust动能论

- 【Linux社区】Wilcox 论新语言需关键规模保证程序员供给，举 Haskell/Erlang/Ada 衰落为鉴，称“Rust 似乎最有动能，胜过 Go” `<!-- ROW_MINE: ksummit-discuss.messages.351280 -->`

## 89.25 背光新uAPI提案

- 【Linux社区】Hans 全文提案：sysfs/class/backlight 五大缺陷（无面板映射、多设备并存、需 root、标度不明、0 值歧义），新 uAPI 落为 drm_connector 属性 `<!-- ROW_MINE: ksummit-discuss.messages.351281 -->`

## 89.26 policy归属之争

- 【Linux社区】Hans 反驳 Walleij 热区类比：坚持 policy in userspace，亮度控制更像音量而非 thermal，环境光传感器映射另议 `<!-- ROW_MINE: ksummit-discuss.messages.351282 -->`

## 89.27 eBPF非ABI后门

- 【Linux社区】Jan Kara 否认“eBPF 或成稳定 ABI 后门”，称其附 tracepoint 冲突少于源码补丁，并明确反对作稳定 ABI 承诺 `<!-- ROW_MINE: ksummit-discuss.messages.351283 -->`

## 89.28 显隐资源管理之辨

- 【Linux社区】Walleij 梳理时钟/调节器/GPIO 等显式驱动管理 vs PM domain 隐式管理双轨并存（OMAP、SH，drivers/base/power/clock_ops.c） `<!-- ROW_MINE: ksummit-discuss.messages.351284 -->`

## 89.29 何谓复杂PM

- 【Linux社区】Walleij 称 clock_ops.c 经 drivers/sh/pm_runtime.c 处理简单平台“相当优雅”，请 Kevin 给出须硬扛的复杂 PM 平台清单并 Cc NVIDIA `<!-- ROW_MINE: ksummit-discuss.messages.351285 -->`

## 89.30 genpd简化工程

- 【Linux社区】Ulf Hansson 表明正简化 genpd，厘清其应辖职责与 pm_runtime_irq_safe 设备处理 `<!-- ROW_MINE: ksummit-discuss.messages.351286 -->`

## 89.31 测试标准议题提案

- 【Linux社区】Hiramatsu 与 Greg KH 面议 LinuxCon Japan 后提 [CORE TOPIC]：组织 make test、文档化测试法、MAINTAINERS 增 UT:/TS: 标签 `<!-- ROW_MINE: ksummit-discuss.messages.351287 -->`

## 89.32 启动农场扩容议

- 【Linux社区】Jason Cooper 补自动启动/运行时测试与功能/性能/压力分类，称 Kevin 与 Olof 启动农场饱和，荐深空压测论文并增荐 Fengguang Wu 等 `<!-- ROW_MINE: ksummit-discuss.messages.351288 -->`

## 89.33 平台去留三选项

- 【Linux社区】Walleij：乏人维护平台可留 legacy、删除或由 custodian 购硬件自修；与 Arnd 议定 StrongARM 属 legacy，ARMv4T+ 有活跃维护者才现代化 `<!-- ROW_MINE: ksummit-discuss.messages.351289 -->`

## 89.34 两段式DT迁移

- 【Linux社区】Walleij 详述 Legacy→DT→multiplatform 两段路线行之 U300/U8500/Integrator，versatile 全 DT 补丁在途 `<!-- ROW_MINE: ksummit-discuss.messages.351290 -->`

## 89.35 ACPI载DT三层次

- 【Linux社区】Wysocki 阐明 ACPI 纳入 DT 式信息三层次：配置对象入 ACPI spec、辅助格式文档、IP 块 DT 绑定规范 `<!-- ROW_MINE: ksummit-discuss.messages.351291 -->`

## 89.36 平台头文件清理

- 【Linux社区】Walleij 报 mach-versatile 两处 plat 头依赖：clcd.h 已备补丁，sched_clock.h 以 sched_clock_register() 内联解决 `<!-- ROW_MINE: ksummit-discuss.messages.351292 -->`

## 89.37 XScale归类之议

- 【Linux社区】Arnd 将 XScale（ixp/iop/pxa）与 StrongARM 同列 legacy，惟 PXA 仍有新开发属例外 `<!-- ROW_MINE: ksummit-discuss.messages.351293 -->`

## 89.38 非企业发行版反驳

- 【Linux社区】Josh Boyer 反驳 Greg：Fedora/Arch/Ubuntu/OpenSuSE 频繁 rebase 且用户庞大，代码入上游即获大量使用，容器需求尤热 `<!-- ROW_MINE: ksummit-discuss.messages.351294 -->`

## 89.39 rebase之痛权衡

- 【Linux社区】Linville 指重写历史令下游树受苦，bisectability 只能追到一定限度，bug 常在定稿次日现身 `<!-- ROW_MINE: ksummit-discuss.messages.351295 -->`

## 89.40 Fedora回归测试框架

- 【Linux社区】Justin Forbes 称内核构建回归测试框架为其近期大项目、测试覆盖现状是“nightmare”，倡 make tests/alltests 自动拉取树外测试 `<!-- ROW_MINE: ksummit-discuss.messages.351297 -->`

## 89.41 复杂PM平台界定

- 【Linux社区】Kevin Hilman 定义：IP 块进出低功耗须超出 clk_enable/disable 者即“interesting”，generic clock_ops 不足须自建 PM domain 或用 genpd `<!-- ROW_MINE: ksummit-discuss.messages.351298 -->`

## 89.42 distro测试自荐

- 【Linux社区】Mark Brown 建议把 distro 与 stable 维护者纳入测试议题，自荐 Linaro 席位 `<!-- ROW_MINE: ksummit-discuss.messages.351299 -->`

## 89.43 农场扩容与测试目标

- 【Linux社区】Olof 纠正“饱和”说：无法扩至 10x 但 2-3x 可行；倡 make install_tests 目标分发运行时测试 `<!-- ROW_MINE: ksummit-discuss.messages.351300 -->`

## 89.44 qemu启动测试现状

- 【Linux社区】Guenter 自述 qemu 已测多架构启动至提示符但无网络等基础能力，受时间所限难扩展 `<!-- ROW_MINE: ksummit-discuss.messages.351301 -->`

## 89.45 主动被动ACPI之辨

- 【Linux社区】Mark Brown 详析可执行方法 vs 纯数据模型（保留配置 vs 重置到已知态），主张 ACPI 经 OF APIs 呈现属性免逐驱动改造 `<!-- ROW_MINE: ksummit-discuss.messages.351304 -->`

## 89.46 属性APIchurn之辩

- 【Linux社区】Brown 认同直调 of_get_X 者须 churn API 但指仅属性读取情形，phandle 类场景“难保 Just Work” `<!-- ROW_MINE: ksummit-discuss.messages.351305 -->`
