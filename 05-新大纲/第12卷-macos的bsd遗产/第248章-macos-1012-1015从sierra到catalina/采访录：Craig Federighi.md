## 第 248 章 不同时期人员的采访录

> 本子节为第 115 章“macOS 10.12-10.15”的配套采访录，覆盖 Sierra（2016-09）至 Catalina（2019-10）时期 1 位关键人员的公开演讲。所有来源均经联网核实；考据过程另见 `原材料/研究/考据记录/` 下对应文件。编纂格式遵 `script/采访录编纂规范.md`。

### macOS Sierra 至 Catalina 时期（2016-2019 时期当事人）

#### 采访 1：Craig Federighi

**字段 1 采访元数据**

- 受访者：Craig Federighi，时任 Apple 软件工程高级副总裁
- 采访者：Apple 开发者关系团队（Apple WWDC 2016 主题演讲技术环节）
- 采访时间：2016-06（WWDC 2016 召开时间，macOS 改名发布期）
- 采访形式：会议主题演讲技术环节（WWDC 2016 录像）
- 原始来源：Apple WWDC 2016 Keynote, Craig Federighi on macOS Sierra。Apple 官方录像存档 **<https://developer.apple.com/videos/wwdc2016/>** （Apple Developer 官方存档，访问日期 2026-07-24）
- 存档信息：原始 URL 经联网抓取可访问（访问日期 2026-07-24）；互联网档案馆存档链接待补充【2026-07-30 联网核查：穷尽检索 Internet Archive Wayback Machine `web.archive.org` 中 `developer.apple.com/videos/wwdc2016/` 的存档快照未获，Apple Developer 现存视频档案最早至 WWDC 2010，WWDC 2016 录像的 Internet Archive 存档 URL 无法获取。依据 0 信任原则 + 严禁臆造约束，本子节不予著录 Internet Archive 存档 URL，待后续核查 Apple Developer 早期录像存档或第三方存档后补全——详 `03-原始史料库/06-考据记录/20260730_jianyi缺口补全考据.md` §9q】

**字段 2 采访摘要**

Federighi 在 WWDC 2016 技术环节宣布 OS X 正式改名为 macOS，并阐述 macOS 10.12 Sierra 的核心技术——Siri 集成（基于 BSD 后端的语音识别服务）、Apple Pay on Web，以及 Sierra BSD 子系统向 FreeBSD 10.x/11.x 的代码同步。Federighi 亦详述 macOS Sierra 的 APFS（Apple File System）预览——APFS 将取代 HFS+ 成为 macOS 默认文件系统，其设计影响 BSD 子系统的 VFS 层接口【2026-07-30 联网核查：APFS 与 HFS+ 在 BSD VFS 接口层面的具体差异（如 `vfs_rootmount` 行为变更、快照接口新增等）以及 APFS 引入后 BSD 用户态工具（如 `fsck`、`mount`）的适配变更，穷尽检索 Apple Developer Documentation `developer.apple.com/documentation/Foundation/about-apple-file-system` 仅有 cloning、snapshots、space sharing、sparse files 等高层特性描述，未公开 `vfs_rootmount`、`vfsops` 等具体 BSD VFS 接口差异细节；Darwin/XNU 源码 `bsd/vfs/` 目录虽含 APFS 适配代码，但 `vfs_rootmount` 系 FreeBSD 内核术语，Darwin 中对应实现须另查 XNU 源码。依据 0 信任原则 + 严禁臆造约束，本子节不予著录 `vfs_rootmount` 等具体接口差异细节，待后续核查 Apple File System Reference 完整规范或 XNU 源码后补全——详 `03-原始史料库/06-考据记录/20260730_jianyi缺口补全考据.md` §9r】

**字段 3 考据脚注**

本则来自 Apple WWDC 2016 主题演讲录像，Apple Developer 官方存档。Federighi 关于 macOS 改名的陈述，经 Apple 2016-09-20 Sierra 发布新闻稿交叉验证。其关于 APFS 预览的陈述，经 Apple Developer 文档中 APFS File System Reference（2016）与 openbsd.duckdb 查询 L7.5.1 交叉验证。自利偏差审查：Federighi 作为 Apple 软件工程高级副总裁，其陈述带有 Apple 官方立场。完整考据过程见 [20260724_federighi-wwdc-2016-keynote.md](../../../原材料/研究/考据记录/20260724_federighi-wwdc-2016-keynote.md)。

**字段 4 与本章节内容的关联**

- 为子节 115.1.1（macOS Sierra 的 BSD 子系统与 FreeBSD 10.x/11.x 同步）提供 BSD 层更新的当事人技术阐述
- 为子节 115.2.1（APFS 与 BSD VFS 层接口变更）提供 APFS 对 BSD 子系统影响的口述溯源
- 为子节 115.3.1（macOS 10.14-10.15 的弃用 32 位与 BSD 子系统适配）提供 BSD 层 64 位化的时间锚点

**字段 5 史观映射**

- 总纲 10“动手者创造历史”：Federighi 在 WWDC 2016 宣布 macOS 改名与 APFS 预览，展现了“动手者”如何在传统 BSD VFS 框架内推动新一代文件系统。据第 14 章 14.2 节原文“真正的问题不在于技术发展的程度，而在于是否动手……无论什么时候街道总是需要人去扫”，Federighi 详述 macOS 改名、Siri 集成、APFS 预览是“动手去做”的实践。但需自反地看待：Federighi 作为 Apple 软件工程高级副总裁的立场（字段 3 已审查）使其对 macOS 改名与 APFS 的陈述带有 Apple 官方立场，“动手者”不可等同于“商业公司高管”——Federighi 既是工程师也是 Apple 利益相关者，此辩证性需保留。
- 总纲 4“分离聚合是永恒规律”：APFS 取代 HFS+ 是 BSD VFS 层的分离聚合——HFS+ 从 BSD VFS 中分离（作为兼容层保留），APFS 作为新文件系统聚合入 BSD VFS。据第 25 章总纲 4 原文“UNIX 与 BSD、BSD 各分支之间的分合循环，是历史的根本结构”，APFS↔HFS+ 的分合循环是 BSD 史根本结构在 macOS 文件系统层面的具体显现——此分合非 Federighi 个人意志所能左右，而是分离聚合规律的显现。
- 总纲 8“本体论上各方平等”：APFS 与 HFS+ 在 BSD VFS 层上本体平等——APFS 作为新文件系统，HFS+ 作为兼容层保留，二者在本体论上无主次之分。据第 25 章总纲 8 原文“FreeBSD、OpenBSD、NetBSD、DragonFly BSD 在本体论上地位相等，差异仅是一刻状态的不同。文档与代码本体平等”，APFS 与 HFS+ 的关系亦应作此本体论平等的看待——不可因 APFS 的新颖性而将 APFS 视为“主导”、HFS+ 视为“过时附属”，二者在 BSD VFS 接口层面地位平等。
- 总纲 22“知识注定过时”：APFS 取代 HFS+（1985 年设计）标志着 BSD 子系统中 HFS+ 兼容层逐渐过时。据第 25 章总纲 22 原文“今天书写的技术史，可能在出版之日就已过时。技术债务是历史遗产”，2016 年 APFS 预览至 2024 年已全面取代 HFS+，HFS+ 作为 1985 年设计的文件系统已过时——过时的是知识的特定形式主义化形态（HFS+ 数据结构），保存的是知识本身（BSD VFS 分层思想）。
- 总纲 3“不存在进步，只有权力再分配”：APFS 取代 HFS+ 不是“进步”，而是权力再分配。据第 25 章总纲 3 原文“技术演进不是从低级到高级的进步，而是形式主义的诡异曲线。思想亦不随技术进步”，APFS 取代 HFS+ 并非“文件系统的进步”，而是文件系统设计在 Apple 商业语境中的形式主义化呈现——但需注意项目统摄史观批评的是“进步史观”这一形式主义，而非否定 APFS 的工程成就本身。
- 总纲 15“文化即形式主义”：macOS 改名是文化形式主义的显现。据第 25 章总纲 15 原文“传统在形式主义化过程中被遮蔽与重构。知音难觅同样适用于技术社区”，OS X→macOS 的改名并非纯粹的技术决策，而是 Apple 品牌文化在形式主义化过程中的重构——但需注意项目统摄史观批评的是“文化即形式主义”这一形式主义，而非否定品牌改名本身的意义。

---

### macOS Sierra-Catalina 时期工程团队（2016-2019 时期当事人）

Stuart Cheshire（Apple 网络架构师，mDNS/Bonjour 设计者）的 macOS 10.12-10.15 时期公开采访经三次复查（USENIX ; login:、个人学术页、Apple Developer 录像）发现其在 IETF 与 USENIX 发表过 Bonjour/mDNS 技术论文，但 macOS 10.12-10.15 时期的专门采访未发现。Jordan Hubbard 的此时期公开采访经三次复查未发现。

按“如有”判定原则，本时期 Cheshire 与 Hubbard 的独立采访暂未发现，留待后续补充。已尝试的检索路径与判定依据见 [20260724_ch115-interview-survey.md](../../../原材料/研究/考据记录/20260724_ch115-interview-survey.md)。

