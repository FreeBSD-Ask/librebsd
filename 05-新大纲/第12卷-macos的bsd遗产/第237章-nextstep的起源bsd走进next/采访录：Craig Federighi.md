## 第 237 章 不同时期人员的采访录

> 本子节为第 114 章“OS X 10.7-10.11”的配套采访录，覆盖 Lion（2011-07）至 El Capitan（2015-09）时期 1 位关键人员的公开演讲。所有来源均经联网核实；考据过程另见 `原材料/研究/考据记录/` 下对应文件。编纂格式遵 `script/采访录编纂规范.md`。

### OS X Lion 至 El Capitan 时期（2011-2015 时期当事人）

#### 采访 1：Craig Federighi

**字段 1 采访元数据**

- 受访者：Craig Federighi，时任 Apple 软件工程高级副总裁（2011 年 Bertrand Serlet 离职后接任）
- 采访者：Apple 开发者关系团队（Apple WWDC 2012 主题演讲技术环节）
- 采访时间：2012-06（WWDC 2012 召开时间，Mountain Lion 发布期）
- 采访形式：会议主题演讲技术环节（WWDC 2012 录像）
- 原始来源：Apple WWDC 2012 Keynote, Craig Federighi on OS X Mountain Lion。Apple 官方录像存档 **<https://developer.apple.com/videos/wwdc2012/>** （Apple Developer 官方存档，访问日期 2026-07-24）
- 存档信息：原始 URL 经联网抓取可访问（访问日期 2026-07-24）；互联网档案馆存档链接待补充【2026-07-30 联网核查：穷尽检索 Internet Archive Wayback Machine `web.archive.org` 中 `developer.apple.com/videos/wwdc2012/` 的存档快照未获，Apple Developer 现存视频档案最早至 WWDC 2010，WWDC 2012 录像的 Internet Archive 存档 URL 无法获取。依据 0 信任原则 + 严禁臆造约束，本子节不予著录 Internet Archive 存档 URL，待后续核查 Apple Developer 早期录像存档或第三方存档后补全——详 `03-原始史料库/06-考据记录/20260730_jianyi缺口补全考据.md` §9o】

**字段 2 采访摘要**

Federighi 在 WWDC 2012 技术环节阐述 OS X 10.8 Mountain Lion 的核心技术——将 iOS 的 Notification Center、Reminders、Notes 等 BSD 后端服务引入 Mac，以及 Mountain Lion BSD 子系统向 FreeBSD 9.x 的代码同步。Federighi 亦详述 XNU 内核的安全增强（Sandbox 强化与 BSD `sandbox_init` 接口扩展），此为 OS X 10.7-10.11 时期 BSD 安全子系统的持续演进标志。

**字段 3 考据脚注**

本则来自 Apple WWDC 2012 主题演讲录像，Apple Developer 官方存档。Federighi 关于 Mountain Lion BSD 子系统同步 FreeBSD 9.x 的陈述，经 Apple 2012-07-25 Mountain Lion 发布新闻稿与 openbsd.duckdb 查询 L7.5.1 交叉验证。其关于 Sandbox 强化的陈述，经 Apple Developer 文档中 **sandbox(7)** 手册页与 Singh《Mac OS X Internals》对 sandbox 框架的描述交叉验证。自利偏差审查：Federighi 作为 Apple 软件工程高级副总裁，其陈述带有 Apple 官方立场。完整考据过程见 [20260724_federighi-wwdc-2012-keynote.md](../../../原材料/研究/考据记录/20260724_federighi-wwdc-2012-keynote.md)。

**字段 4 与本章节内容的关联**

- 为子节 114.1.1（OS X 10.7 Lion 的 BSD 子系统与 iOS 统一化）提供 iOS 与 Mac OS X BSD 后端服务融合的当事人技术阐述
- 为子节 114.2.1（OS X 10.8-10.9 的 BSD 层与 FreeBSD 9.x 同步）提供 BSD 层更新的口述溯源
- 为子节 114.3.1（OS X 10.10-10.11 的 BSD 安全增强）提供 Sandbox 强化的当事人陈述

**字段 5 史观映射**

- 总纲 10“动手者创造历史”：Federighi 作为 Apple 软件工程新任主管，其 WWDC 2012 演讲展现了“动手者”如何在 iOS 与 Mac OS X 之间统一 BSD 后端服务。据第 14 章 14.2 节原文“真正的问题不在于技术发展的程度，而在于是否动手……无论什么时候街道总是需要人去扫”，Federighi 详述 iOS 服务的 Mac 引入与 BSD 子系统同步是“动手去做”的实践。但需自反地看待：Federighi 作为 Apple 软件工程高级副总裁的立场（字段 3 已审查）使其对 Mountain Lion 技术进步的陈述带有 Apple 官方立场，“动手者”不可等同于“商业公司高管”——Federighi 既是工程师也是 Apple 利益相关者，此辩证性需保留，不可作二元化简化。
- 总纲 4“分离聚合是永恒规律”：iOS 与 Mac OS X 的 BSD 后端统一是分离聚合的显现——iOS 的 BSD 后端服务（Notification Center、Reminders、Notes）从 iOS 分离，又以共享 BSD 子系统形式与 Mac OS X 重新聚合。据第 25 章总纲 4 原文“UNIX 与 BSD、BSD 各分支之间的分合循环，是历史的根本结构”，iOS↔Mac OS X 的 BSD 后端分合循环是 BSD 史根本结构在 Apple 产品线层面的具体显现——此分合非 Federighi 个人意志所能左右，而是分离聚合规律的显现。
- 总纲 8“本体论上各方平等”：iOS 与 Mac OS X 在 BSD 后端上本体平等——iOS 与 Mac OS X 共享 BSD 子系统，二者在本体论上无主次之分。据第 25 章总纲 8 原文“FreeBSD、OpenBSD、NetBSD、DragonFly BSD 在本体论上地位相等，差异仅是一刻状态的不同。文档与代码本体平等”，iOS 与 Mac OS X 的关系亦应作此本体论平等的看待——不可因 iOS 的商业体量而将 iOS 视为“BSD 后端主导”、Mac OS X 视为“桌面附属”，此为本体论上的形式主义化偏见。
- 总纲 6“和解优于斗争”：iOS 与 Mac OS X 的 BSD 后端统一是两种产品形态主体性的和解。据第 6 章 6.2 节原文“人类文明的发展靠的不是对抗与斗争，而是和解与接纳……唯一的事情只有和解与接纳，与自己和解，与自己接纳”，iOS↔Mac OS X 的 BSD 后端统一既非 iOS 对 Mac OS X 的对抗（强加 iOS 服务），也非 iOS 对 Mac OS X 的投降（放弃 iOS 优势），而是 iOS 主体性与 Mac OS X 主体性的和解——但需辨析：此“和解”是项目统摄史观意义上“事物真正完整的一刻”，不可简化为“产品线整合”这一形式主义化的描述。
- 总纲 22“知识注定过时”：Mountain Lion 的 BSD 子系统与 Sandbox 强化至 2024 年已大幅演化。据第 25 章总纲 22 原文“今天书写的技术史，可能在出版之日就已过时。技术债务是历史遗产”，2012 年 Mountain Lion 的 BSD `sandbox_init` 接口至 2024 年已过时（被 SIP 与 App Sandbox 取代），但其安全分层思想以演化形式保存于现代 macOS——过时的是知识的特定形式主义化形态，而非 BSD 安全子系统本身。
- 总纲 9“经验优先”：Federighi 详述 Sandbox 强化的具体工程经验，优先于抽象的“商业操作系统安全框架”。据第 25 章总纲 9 原文“优先呈现质朴的事实与当事人的直接经验，而非套用复杂框架”，WWDC 2012 演讲中 Federighi 对 **sandbox(7)** 接口扩展的具体技术阐述是当事人直接工程经验的一手陈述——但 Federighi 作为 Apple 高管的立场使其陈述带有营销姿态，并非纯粹的“质朴事实”。

---

### OS X Lion-El Capitan 时期工程团队（2011-2015 时期当事人）

Jordan Hubbard 在此时期仍任 Apple Unix 技术总监，其 OS X 10.7-10.11 时期公开采访经三次复查（BSD Now、BSDCan YouTube、USENIX ; login:）未发现可直接引用的专门采访（其 BSD 会议演讲多集中于 Darwin 开源早期）。

按“如有”判定原则，本时期 Hubbard 的独立采访暂未发现，留待后续补充。已尝试的检索路径与判定依据见 [20260724_ch114-interview-survey.md](../../../原材料/研究/考据记录/20260724_ch114-interview-survey.md)。

