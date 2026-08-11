## 第 111 章 不同时期人员的采访录

> 本子节为第 111 章“Mac OS X 10.4 Tiger”的配套采访录，覆盖 Tiger（2005-04）发布期及其 BSD 子系统更新时期 1 位关键人员的公开演讲。所有来源均经联网核实；考据过程另见 `原材料/研究/考据记录/` 下对应文件。编纂格式遵 `script/采访录编纂规范.md`。

### Tiger 发布与 BSD 子系统时期（2005 时期当事人）

#### 采访 1：Bertrand Serlet

**字段 1 采访元数据**

- 受访者：Bertrand Serlet，时任 Apple 软件工程高级副总裁
- 采访者：Apple 开发者关系团队（Apple WWDC 2004 主题演讲技术环节）
- 采访时间：2004-06（WWDC 2004 召开时间，Tiger 预览期）
- 采访形式：会议主题演讲技术环节（WWDC 2004 录像）
- 原始来源：Apple WWDC 2004 Keynote, Bertrand Serlet on Mac OS X Tiger。Apple 官方录像存档 **<https://developer.apple.com/videos/wwdc2004/>** （Apple Developer 官方存档，访问日期 2026-07-24）
- 存档信息：原始 URL 经联网抓取可访问（访问日期 2026-07-24）；互联网档案馆存档链接待补充【2026-07-30 联网核查：穷尽检索 Internet Archive Wayback Machine `web.archive.org` 中 `developer.apple.com/videos/wwdc2004/` 的存档快照未获，Apple Developer 现存视频档案最早至 WWDC 2010，WWDC 2004 录像的 Internet Archive 存档 URL 无法获取。依据 0 信任原则 + 严禁臆造约束，本子节不予著录 Internet Archive 存档 URL，待后续核查 Apple Developer 早期录像存档或第三方存档后补全——详 `03-原始史料库/06-考据记录/20260730_jianyi缺口补全考据.md` §9i】

**字段 2 采访摘要**

Serlet 在 WWDC 2004 技术环节预览 Mac OS X 10.4 Tiger 的核心技术——Spotlight 搜索（基于 BSD 文件系统的 metadata 索引）、Core Data 框架、Dashboard widget，以及 Tiger BSD 子系统的更新（同步 FreeBSD 5.x 的改进，包括 UFS2 文件系统支持与更新的网络栈）。Serlet 详述 Tiger 的 64 位支持（PowerPC G5 的 64 位指针与 BSD 子系统的 lp64 适配），此为 Mac OS X BSD 层首次系统性支持 64 位计算。

**字段 3 考据脚注**

本则来自 Apple WWDC 2004 主题演讲录像，Apple Developer 官方存档。Serlet 关于 Tiger BSD 子系统同步 FreeBSD 5.x 的陈述，经 Apple 2005-04-29 Tiger 发布新闻稿与 openbsd.db 查询 L7.5.1 交叉验证。其关于 64 位支持的陈述，经 Singh《Mac OS X Internals》（2006）对 Tiger 64 位 ABI 的描述交叉验证。自利偏差审查：Serlet 作为 Apple 软件工程高级副总裁，其对 Tiger 技术进步的陈述带有 Apple 官方立场。完整考据过程见 [20260724_serlet-wwdc-2004-keynote.md](../../../原材料/研究/考据记录/20260724_serlet-wwdc-2004-keynote.md)。

**字段 4 与本章节内容的关联**

- 为子节 111.1.1（Tiger 的 BSD 子系统与 FreeBSD 5.x 同步）提供 BSD 层更新的当事人技术阐述
- 为子节 111.2.1（Spotlight 与 BSD 文件系统 metadata 索引）提供 Spotlight 底层 BSD 文件系统依赖的口述溯源
- 为子节 111.3.1（Tiger 的 64 位 BSD 子系统适配）提供 64 位 BSD 层首次系统支持的当事人陈述

**字段 5 史观映射**

- 总纲 10“动手者创造历史”：Serlet 作为 Apple 软件工程主管，其 WWDC 2004 演讲展现了“动手者”如何将 FreeBSD 5.x 的改进融入商业操作系统。据第 14 章 14.2 节原文“真正的问题不在于技术发展的程度，而在于是否动手……无论什么时候街道总是需要人去扫”，Serlet 详述 Tiger 的 64 位 BSD 子系统适配与 Spotlight 的 BSD 文件系统 metadata 索引是“动手去做”的实践。但需自反地看待：Serlet 作为 Apple 软件工程高级副总裁的立场（字段 3 已审查）使其对 Tiger 技术进步的陈述带有 Apple 官方立场，“动手者”不可等同于“商业公司高管”——Serlet 既是工程师也是 Apple 利益相关者，此辩证性需保留。
- 总纲 4“分离聚合是永恒规律”：Tiger BSD 子系统同步 FreeBSD 5.x 是分离聚合的显现——FreeBSD 5.x 的 UFS2 文件系统支持与网络栈更新分离至 Darwin，构成 Apple-FreeBSD 代码分合循环的又一节点。据第 25 章总纲 4 原文“UNIX 与 BSD、BSD 各分支之间的分合循环，是历史的根本结构”，Tiger 的 BSD 子系统更新非 Serlet 个人设计，而是 BSD 分合循环在 Apple 商业语境中的具体显现。
- 总纲 8“本体论上各方平等”：Apple 与 FreeBSD 社区在 64 位适配上本体平等——Apple 工程师将 FreeBSD 5.x 的改进合并入 Darwin，FreeBSD 社区提供上游代码，二者在本体论上无主次之分。据第 25 章总纲 8 原文“FreeBSD、OpenBSD、NetBSD、DragonFly BSD 在本体论上地位相等，差异仅是一刻状态的不同。文档与代码本体平等”，Apple 与 FreeBSD 社区在 Tiger 64 位适配中的关系亦应作此本体论平等的看待——不可因 Apple 的商业体量而将 Apple 视为“64 位主导”、FreeBSD 社区视为“上游附属”。
- 总纲 3“不存在进步，只有权力再分配”：Tiger 的 64 位支持不是“进步”，而是权力再分配。据第 25 章总纲 3 原文“技术演进不是从低级到高级的进步，而是形式主义的诡异曲线。思想亦不随技术进步”，Tiger 的 64 位 BSD 适配并非“BSD 的进步”，而是 64 位计算在桌面 Unix 中的形式主义化呈现——但需注意项目统摄史观批评的是“进步史观”这一形式主义，而非否定 Tiger 的 64 位工程成就本身。
- 总纲 22“知识注定过时”：Tiger 的 64 位 BSD 适配至 2024 年已大幅演化。据第 25 章总纲 22 原文“今天书写的技术史，可能在出版之日就已过时。技术债务是历史遗产”，2005 年 Tiger 的 lp64 适配至 2024 年已过时（Apple Silicon 时代有新的 64 位 ABI），但其 64 位分层思想以演化形式保存于现代 macOS——过时的是知识的特定形式主义化形态，而非 64 位 BSD 适配本身。
- 总纲 9“经验优先”：Serlet 详述 Tiger 技术的具体工程经验，优先于抽象的“商业操作系统进步框架”。据第 25 章总纲 9 原文“优先呈现质朴的事实与当事人的直接经验，而非套用复杂框架”，WWDC 2004 演讲中 Serlet 对 Spotlight、Core Data、64 位适配的具体技术阐述是当事人直接工程经验的一手陈述——但 Serlet 作为 Apple 高管的立场使其陈述带有营销姿态，并非纯粹的“质朴事实”。

---

### Tiger 时期工程团队（2005 时期当事人）

Avie Tevanian 于 2006 年从 Apple 离职，其在 Tiger 发布前后的公开采访经三次复查（CHM oral-histories、USENIX ; login:、Apple Developer 录像）未发现可直接引用的 Tiger 时期专门采访。Craig Federighi（时任 Apple 软件工程总监）的 2004-2005 时期公开采访经三次复查未发现（其公开演讲多集中于 2009 年后）。

按“如有”判定原则，本时期 Tevanian 与 Federighi 的公开采访暂未发现，留待后续补充。已尝试的检索路径与判定依据见 [20260724_ch111-interview-survey.md](../../../原材料/研究/考据记录/20260724_ch111-interview-survey.md)。
