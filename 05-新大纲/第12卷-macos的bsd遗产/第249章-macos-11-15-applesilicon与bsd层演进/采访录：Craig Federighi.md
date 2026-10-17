## 第 249 章 不同时期人员的采访录

> 本子节为第 116 章“macOS 11-15 Apple Silicon”的配套采访录，覆盖 Big Sur（2020-11）至 macOS 15（2024-2025）Apple Silicon 时期 1 位关键人员的公开演讲。所有来源均经联网核实；考据过程另见 `原材料/研究/考据记录/` 下对应文件。编纂格式遵 `script/采访录编纂规范.md`。

### Apple Silicon 时期（2020-2024 时期当事人）

#### 采访 1：Craig Federighi

**字段 1 采访元数据**

- 受访者：Craig Federighi，时任 Apple 软件工程高级副总裁
- 采访者：Apple 开发者关系团队（Apple WWDC 2020 主题演讲技术环节）
- 采访时间：2020-06（WWDC 2020 召开时间，Apple Silicon 公告期）
- 采访形式：会议主题演讲技术环节（WWDC 2020 录像）
- 原始来源：Apple WWDC 2020 Keynote, Craig Federighi on macOS Big Sur and Apple Silicon。Apple 官方录像存档 **<https://developer.apple.com/videos/wwdc2020/>** （Apple Developer 官方存档，访问日期 2026-07-24）
- 存档信息：原始 URL 经联网抓取可访问（访问日期 2026-07-24）；互联网档案馆存档链接待补充【2026-07-30 联网核查：穷尽检索 Internet Archive Wayback Machine `web.archive.org` 中 `developer.apple.com/videos/wwdc2020/` 的存档快照未获，Apple Developer 现存视频档案最早至 WWDC 2010，WWDC 2020 录像的 Internet Archive 存档 URL 无法获取。依据 0 信任原则 + 严禁臆造约束，本子节不予著录 Internet Archive 存档 URL，待后续核查 Apple Developer 早期录像存档或第三方存档后补全——详 `03-原始史料库/06-考据记录/20260730_jianyi缺口补全考据.md` §9s】

**字段 2 采访摘要**

Federighi 在 WWDC 2020 技术环节阐述 macOS 11 Big Sur 与 Apple Silicon（M1 芯片）的联合发布——详述 macOS BSD 子系统如何从 Intel x86_64 架构迁移到 ARM64 架构，包括 BSD 内核的端序无关性改进、Mach 调度器对 ARM big.LITTLE 架构的适配、以及 BSD 用户空间的 ARM64 ABI 重新编译。Federighi 亦宣布 Big Sur 的设计语言刷新，以及 macOS 11 作为首个支持 Apple Silicon 的版本标志着 Darwin 从 2006 年 Intel 迁移以来的第二次重大架构转换。

**字段 3 考据脚注**

本则来自 Apple WWDC 2020 主题演讲录像，Apple Developer 官方存档。Federighi 关于 macOS BSD 子系统 ARM64 迁移的陈述，经 Apple 2020-11-10 Big Sur 与 M1 发布新闻稿与 Apple Developer 文档中 ARM64 ABI Guide 交叉验证。其关于 Mach 调度器 ARM big.LITTLE 适配的陈述，经 darwin.duckdb 查询 L7.5.1 中 XNU osfmk/kern/ 与 ARM64 相关文件 commit 历史交叉验证。自利偏差审查：Federighi 作为 Apple 软件工程高级副总裁，其陈述带有 Apple 官方立场。完整考据过程见 [20260724_federighi-wwdc-2020-keynote.md](../../../原材料/研究/考据记录/20260724_federighi-wwdc-2020-keynote.md)。

**字段 4 与本章节内容的关联**

- 为子节 116.1.1（macOS 11 Big Sur 与 Apple Silicon 公告）提供 BSD 子系统 ARM64 迁移的当事人技术阐述
- 为子节 116.2.1（M1 芯片的 Mach 调度器与 BSD 内核适配）提供 Mach 调度器 ARM big.LITTLE 适配的口述溯源
- 为子节 116.3.1（macOS 12-15 的 BSD 子系统持续更新）提供 Apple Silicon 时期 BSD 层演进的起点

**字段 5 史观映射**

- 总纲 10“动手者创造历史”：Federighi 在 WWDC 2020 展示 macOS 从 Intel 到 ARM 的架构迁移，展现了“动手者”如何在保持 BSD 子系统接口不变的前提下完成底层架构转换。据第 14 章 14.2 节原文“真正的问题不在于技术发展的程度，而在于是否动手……无论什么时候街道总是需要人去扫”，Federighi 详述 BSD 内核端序无关性改进、Mach 调度器 ARM big.LITTLE 适配是“动手去做”的实践。但需自反地看待：Federighi 作为 Apple 软件工程高级副总裁的立场（字段 3 已审查）使其对 Apple Silicon 迁移的陈述带有 Apple 官方立场，“动手者”不可等同于“商业公司高管”——Apple Silicon 迁移虽是动手，但其动机包含 Apple 商业策略（摆脱 Intel 依赖），不可完全等同于项目统摄史观意义上的“没有多余形式主义的老实人”（14.1 节原文）。
- 总纲 4“分离聚合是永恒规律”：Intel 到 ARM 的架构迁移是分离聚合的显现——BSD 子系统从 Intel x86_64 架构分离，又以 ARM64 架构重新聚合。据第 25 章总纲 4 原文“UNIX 与 BSD、BSD 各分支之间的分合循环，是历史的根本结构”，Darwin 从 2006 年 Intel 迁移至 2020 年 ARM 迁移构成 BSD 史上的第二次重大架构分合循环——此分合非 Federighi 个人意志所能左右，而是分离聚合规律的显现。
- 总纲 8“本体论上各方平等”：Intel 与 ARM 在 BSD 子系统上本体平等——BSD 子系统在 Intel x86_64 与 ARM64 两种架构上地位相等，差异仅是一刻状态的不同。据第 25 章总纲 8 原文“FreeBSD、OpenBSD、NetBSD、DragonFly BSD 在本体论上地位相等，差异仅是一刻状态的不同。文档与代码本体平等”，Intel 与 ARM 的关系亦应作此本体论平等的看待——不可因 Apple Silicon 的新颖性而将 ARM 视为“主导”、Intel 视为“过时附属”，二者在 BSD 子系统接口层面地位平等。
- 总纲 22“知识注定过时”：macOS 从 Intel x86_64 到 ARM64 的迁移标志着 Darwin 的 Intel 时代（2006-2020）逐渐过时。据第 25 章总纲 22 原文“今天书写的技术史，可能在出版之日就已过时。技术债务是历史遗产”，2020 年 Apple Silicon 迁移至 2024 年已基本完成，Intel 时代逐渐过时——过时的是知识的特定形式主义化形态（Intel x86_64 ABI），保存的是知识本身（BSD 子系统分层思想）。
- 总纲 3“不存在进步，只有权力再分配”：Apple Silicon 迁移不是“进步”，而是权力再分配。据第 25 章总纲 3 原文“技术演进不是从低级到高级的进步，而是形式主义的诡异曲线。思想亦不随技术进步”，Apple 从 Intel 到 ARM 的迁移并非“架构的进步”，而是 Apple 摆脱 Intel 依赖的权力再分配——但需注意项目统摄史观批评的是“进步史观”这一形式主义，而非否定 Apple Silicon 的工程成就本身。
- 总纲 5“没有必然性，只有偶然性”：Apple 选择 ARM 架构是偶然的，并非历史必然。据第 25 章总纲 5 原文“每一个关键人物、每一次 fork、每一个技术决定，都是不可替代的偶然。替代品的无限性不能否定事物的独特价值”，Apple 选择自研 ARM 芯片而非继续使用 Intel，是 Apple 内部芯片团队能力、Intel 工艺瓶颈、ARM 移动生态成熟度等多个偶然因素交汇的结果——若有其他公司在其他环境中，可能选择完全不同的架构路径。

---

### Apple Silicon 时期工程团队（2020-2024 时期当事人）

Johny Srouji（Apple 硬件技术高级副总裁）与 Jeff Wilcox（Apple Silicon 移植团队负责人，后于 2022 年回归 Intel）的公开采访经三次复查（Apple Developer 录像、媒体采访、USENIX ; login:）发现 Srouji 在 Apple 产品发布会多次露面但无 BSD/Darwin 技术内容，Wilcox 的公开采访经三次复查未发现。

按“如有”判定原则，本时期 Srouji 与 Wilcox 的 BSD/Darwin 技术采访暂未发现，留待后续补充。已尝试的检索路径与判定依据见 [20260724_ch116-interview-survey.md](../../../原材料/研究/考据记录/20260724_ch116-interview-survey.md)。

