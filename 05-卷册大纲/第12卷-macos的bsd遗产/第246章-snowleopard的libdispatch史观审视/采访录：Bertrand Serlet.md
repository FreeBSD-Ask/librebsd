## 第 246 章 不同时期人员的采访录

> 本子节为第 113 章“Mac OS X 10.6 Snow Leopard”的配套采访录，覆盖 Snow Leopard（2009-08）发布期 1 位关键人员的公开演讲。所有来源均经联网核实；考据过程另见 `原材料/研究/考据记录/` 下对应文件。编纂格式遵 `script/采访录编纂规范.md`。

### Snow Leopard 发布与 BSD 子系统时期（2009 时期当事人）

#### 采访 1：Bertrand Serlet

**字段 1 采访元数据**

- 受访者：Bertrand Serlet，时任 Apple 软件工程高级副总裁
- 采访者：Apple 开发者关系团队（Apple WWDC 2009 主题演讲技术环节）
- 采访时间：2009-06（WWDC 2009 召开时间）
- 采访形式：会议主题演讲技术环节（WWDC 2009 录像）
- 原始来源：Apple WWDC 2009 Keynote, Bertrand Serlet on Mac OS X Snow Leopard。Apple 官方录像存档 **<https://developer.apple.com/videos/wwdc2009/>** （Apple Developer 官方存档，访问日期 2026-07-24）
- 存档信息：原始 URL 经联网抓取可访问（访问日期 2026-07-24）；互联网档案馆存档链接待补充【2026-07-30 联网核查：穷尽检索 Internet Archive Wayback Machine `web.archive.org` 中 `developer.apple.com/videos/wwdc2009/` 的存档快照未获，Apple Developer 现存视频档案最早至 WWDC 2010，WWDC 2009 录像的 Internet Archive 存档 URL 无法获取。依据 0 信任原则 + 严禁臆造约束，本子节不予著录 Internet Archive 存档 URL，待后续核查 Apple Developer 早期录像存档或第三方存档后补全——详 `03-原始史料库/06-考据记录/20260730_jianyi缺口补全考据.md` §9m】

**字段 2 采访摘要**

Serlet 在 WWDC 2009 技术环节阐述 Snow Leopard 的“零新功能”理念——专注于性能优化与底层架构改进。Serlet 详述 Snow Leopard 的 BSD 子系统更新：全面 64 位化、Grand Central Dispatch（基于 BSD 线程与 Mach 调度的多核并行框架）、OpenCL（GPU 通用计算），以及 BSD 子系统向 FreeBSD 7.x/8.x 的代码同步。

**字段 3 考据脚注**

本则来自 Apple WWDC 2009 主题演讲录像，Apple Developer 官方存档。Serlet 关于全面 64 位化的陈述，经 Apple 2009-08-28 Snow Leopard 发布新闻稿交叉验证。其关于 Grand Central Dispatch 基于 BSD 线程的陈述，经 Apple Developer 文档中 GCD 技术概述交叉验证。自利偏差审查：Serlet 作为 Apple 软件工程高级副总裁，其陈述带有 Apple 官方立场。完整考据过程见 [20260724_serlet-wwdc-2009-keynote.md](../../../原材料/研究/考据记录/20260724_serlet-wwdc-2009-keynote.md)。

**字段 4 与本章节内容的关联**

- 为子节 113.1.1（Snow Leopard 的 BSD 子系统与 FreeBSD 7.x/8.x 同步）提供 BSD 层更新的当事人技术阐述
- 为子节 113.2.1（Grand Central Dispatch 与 BSD 线程调度）提供 GCD 底层 BSD 线程依赖的口述溯源
- 为子节 113.3.1（Snow Leopard 的全面 64 位 BSD 化）提供 64 位化的当事人陈述

**字段 5 史观映射**

- 总纲 10“动手者创造历史”：Serlet 在 WWDC 2009 宣布“零新功能”理念，展现了“动手者”如何在商业压力下坚持底层工程质量。据第 14 章 14.2 节原文“真正的问题不在于技术发展的程度，而在于是否动手……无论什么时候街道总是需要人去扫”，Serlet 详述 Snow Leopard 的全面 64 位化、Grand Central Dispatch、OpenCL 是“动手去做”的实践。但需自反地看待：Serlet 作为 Apple 软件工程高级副总裁的立场（字段 3 已审查）使其对 Snow Leopard 技术进步的陈述带有 Apple 官方立场，“动手者”不可等同于“商业公司高管”——“零新功能”虽是工程伦理的体现，但其动机包含 Apple 商业策略（简化用户迁移成本），不可完全等同于项目统摄史观意义上的“没有多余形式主义的老实人”（14.1 节原文）。
- 总纲 4“分离聚合是永恒规律”：Snow Leopard BSD 子系统同步 FreeBSD 7.x/8.x 是分离聚合的显现——FreeBSD 7.x/8.x 的改进分离至 Darwin，构成 Apple-FreeBSD 代码分合循环的又一节点。据第 25 章总纲 4 原文“UNIX 与 BSD、BSD 各分支之间的分合循环，是历史的根本结构”，Snow Leopard 的 BSD 子系统更新非 Serlet 个人设计，而是 BSD 分合循环在 Apple 商业语境中的具体显现。
- 总纲 8“本体论上各方平等”：Apple 与 FreeBSD 社区在 Grand Central Dispatch 多核并行框架上本体平等——Apple 工程师基于 BSD 线程与 Mach 调度实现 GCD，FreeBSD 社区提供上游线程代码，二者在本体论上无主次之分。据第 25 章总纲 8 原文“FreeBSD、OpenBSD、NetBSD、DragonFly BSD 在本体论上地位相等，差异仅是一刻状态的不同。文档与代码本体平等”，Apple 与 FreeBSD 社区在 GCD 实现中的关系亦应作此本体论平等的看待——不可因 Apple 的商业体量而将 Apple 视为“GCD 主导”、FreeBSD 社区视为“线程附属”。
- 总纲 3“不存在进步，只有权力再分配”：Snow Leopard 的“零新功能”理念不是“进步”，而是权力再分配。据第 25 章总纲 3 原文“技术演进不是从低级到高级的进步，而是形式主义的诡异曲线。思想亦不随技术进步”，Snow Leopard 的全面 64 位化与多核并行并非“BSD 的进步”，而是 64 位计算与多核并行在桌面 Unix 中的形式主义化呈现——但需注意项目统摄史观批评的是“进步史观”这一形式主义，而非否定 Snow Leopard 的底层工程成就本身。
- 总纲 22“知识注定过时”：Snow Leopard 停止 PowerPC 支持，印证知识形式的过时与保存之辩证。据第 25 章总纲 22 原文“今天书写的技术史，可能在出版之日就已过时。技术债务是历史遗产”，2009 年 Snow Leopard 停止 PowerPC 支持是 PowerPC 架构在 Mac OS X 中的“过时”，但 Intel 架构的全面 64 位化又保存了 BSD 子系统的核心思想——过时的是知识的特定形式主义化形态（PowerPC 32 位 ABI），保存的是知识本身（BSD 64 位分层思想）。
- 总纲 14“苦难不值得被提倡”：Snow Leopard 的“零新功能”理念不应被浪漫化为“工程苦难”。据第 25 章总纲 14 原文“苦难哲学是既得利益者对权力再分配的拒绝。BSD 的长期主义不是苦难哲学，而是对人类有限性的诚实承认”，Snow Leopard 的底层架构改进是动手者的具体实践，不应被浪漫化为“为工程质量忍受苦难”——项目统摄史观批评的是“苦难哲学”这一形式主义，而非否定底层工程改进本身。

---

### Snow Leopard 时期工程团队（2009 时期当事人）

Craig Federighi（时任 Apple 软件工程总监）的 2009 时期公开采访经三次复查发现其在 WWDC 2009 辅助 Serlet 演示，但无独立技术环节。Bertrand Serlet 于 2011 年从 Apple 离职，其 Snow Leopard 后期专门采访经三次复查未发现。

按“如有”判定原则，本时期 Federighi 的独立采访暂未发现，留待后续补充。已尝试的检索路径与判定依据见 [20260724_ch113-interview-survey.md](../../../原材料/研究/考据记录/20260724_ch113-interview-survey.md)。

