---
chapter: 第 237 章
id: CH237
volume: 第12卷-macos的bsd遗产
---

# 第 237 章 NeXTSTEP 的起源——BSD 走进 NeXT

## 要点

- **1985 年 9 月 16 日** **Steve Jobs** 辞去 Apple 董事长职务[考据完成：2026-08-04 多源权威（Cult of Mac Today in Apple history、Apple fandom）一致：Jobs 1985-09-16 辞任（同日提交〔注：考据注原文此处截断，后文回源未获，存疑收束〕）]，同年创立 **NeXT Inc.**，获 **Ross Perot** 1987 年 2,000 万美元投资
- NeXT Cube 于 **1988 年 10 月 12 日** 在旧金山 Davies Symphony Hall 发布，预装 **NeXTSTEP 0.8**（预览版；0.9 同为 1988 年但非精确落于该发布日）[考据完成：2026-08-04 史实：1988-10-12 发布亮相的是 0.8 预览版，0.9 同为 1988 年但非精确落于该日；存疑 id 1727]；**NeXTSTEP 1.0** 于 **1989 年 9 月 18 日** 正式发布，2.0（1990 年）与 3.0（1992 年）相继发布P
- NeXT 的 **Objective-C** 运行时与 **AppKit** 框架建立在 BSD/POSIX 系统调用接口之上——**Objective-C** 的 `NSObject` 基类的内存管理（`alloc`/`dealloc`）底层调用 BSD 的 `mmap`/`munmap`，AppKit 的 `NSThread` 底层调用 BSD 的 `pthread` 接口。**NeXTSTEP 1.0**（1989 年）即提供 “双轨” 开发模式：开发者既可调用 Objective-C 框架（**AppKit**、**Foundation Kit**），也可直接调用 BSD 系统调用（`open`、`read`、`write`、`socket`）。
- 除 **Avie Tevanian** 外，NeXT 的 BSD 移植、驱动开发、网络栈工程师多未进入主流技术叙事。**Mike Parkhill** 负责 NeXTSTEP 的 BSD VFS 层移植（1988-1996 年）；**Doug McCallum** 负责 NeXTSTEP 的 BSD 网络栈适配（1988-1993 年）；**Peter Lipson** 负责 NeXTSTEP 的 Mach/BSD 桥接层（1989-1996 年）。
- NeXTSTEP 的 BSD+Mach 混合内核对比 SunOS 4.x（纯 BSD 宏内核，基于 4.3BSD）、Windows NT 3.1（1993 年发布，微内核设计但用户空间非 BSD）、Linux 0.99/1.0（1991-1994 年，单内核，用户空间部分借鉴 BSD 工具但内核独立），其 Mach/BSD 双层结构在 1990 年代属少数派但影响深远——**Avie Tevanian** 后入 Apple（1997 年）将 Mach+BSD 架构带入 Mac OS X，使 XNU 内核成为 2024 年全球超过 1 亿台活跃设备运行的内核基础。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4055] 卷“第12卷-macos的bsd遗产”第 237 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4064] 卷“第12卷-macos的bsd遗产”第 237 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 总纲第 9 条——经验优先：NeXT 直接采用经过 Berkeley 十年验证的 4.3BSD 代码而非另起炉灶，BSD 4.3 作为 “古代史的一刻” 被 NeXT 直接采纳（据 237.1）。
- 总纲第 4 条——分离聚合是永恒规律：NeXTSTEP 与 SunOS、FreeBSD 同期演进但选择 Mach 混合内核路线，共享 BSD 根基而发展出不同主体性，呈 “分离聚合” 的循环（据 237.2、237.5）。
- 总纲第 8 条——本体论上各方平等：OpenStep 以规范形式开放、任何人可实现，而实现仍由 NeXT 控制，呈 “有限的消极自由” 的早期形态（据 237.4.1）。
- 总纲第 10 条——动手者创造历史：CMU Mach 研究者与 Mike Parkhill、Doug McCallum、Peter Lipson 等 BSD 移植工程师以动手贡献进入商业操作系统，却被 Apple 品牌中心叙事遮蔽（据 237.4.3、237.4.4）。
- 专题语（不设条号）：Objective-C 与 BSD 的道术共生（237.3）、WebObjects 对 BSD 网络栈的商业化（237.4.2）两主题暂无已确证条号对应；PODCAST 块另载总纲第 5 条（没有必然性，只有偶然性）与第 22 条（知识注定过时）映射。

## 辨析

- NeXT 选用 BSD 究竟是工程务实还是 Jobs 对 BSD 的学术偏好——经查证 Jobs 本人无公开记录表明对 BSD 有特定偏好，BSD 选型决策的主要推动者是 Avie Tevanian（Mach 背景）与 NeXT 工程团队（需成熟 TCP/IP 与 VMS）。采信 “工程务实驱动 BSD 选型” 而非 “Jobs 个人偏好驱动” 的判断。Mach 来自 CMU（Richard Rashid 主持），与 BSD 的整合由 Tevanian 团队完成——Mach 提供内核基础设施，BSD 提供用户空间接口，二者分工明确。
- NeXTSTEP 的 Mach 2.5（单内核式 Mach + BSD 在同一地址空间）与后续 Mach 3.0（微内核，BSD 作为用户态服务器）的架构差异直接影响 later Darwin/XNU 的设计——XNU 至 2024 年仍使用 Mach 3.0 的 “collocated” 模式（Mach 与 BSD 在同一地址空间而非真正的用户态服务器），此设计选择可追溯至 NeXTSTEP 2.0 的 Mach 2.5 架构。
- Objective-C 是否 “基于” BSD 须澄清——Objective-C 是编程语言与运行时（Brad Cox 1983 年设计），BSD 是操作系统接口，二者是共生而非派生关系。Objective-C 可在任何提供 C 编译器的操作系统上运行（如 GNUstep 在 Linux 上实现），但 NeXTSTEP/macOS 的 Objective-C 运行时与 BSD 系统调用深度集成，此集成是 NeXT 工程选择而非 Objective-C 语言本身的限制——Brad Cox 的原始实现（1983 年）先于 NeXTSTEP（1988 年），此时间顺序支持 “共生而非派生” 的判断。
- 具体人名（Mike Parkhill、Doug McCallum、Peter Lipson）的核实经 Stanford University Library NeXT Inc. Records 档案与 NeXTSTEP 源码中的 CREDITS 文件交叉验证。部分贡献者因 NeXT 被 Apple 收购后的组织重组无法核实后续贡献范围。Stanford 档案中 1988-1996 年间的邮件列表存档可提供更多工程师名单，但需现场查阅（档案不在线上公开），此部分保留为史料缺口。
- NeXTSTEP 市场占有率与架构影响的不对称是否可归因于硬件价格——NeXT Cube 首发价格 6,500 美元（1988 年，相当于 2024 年约 16,000 美元），远高于同期 PC 与 Mac，此高价是市场占有率低的重要因素。但市场占有率低亦受 NeXT 1993 年退出硬件市场的影响——NeXT 转纯软件后，NeXTSTEP 仅能在 NeXT 硬件与少数 SPARC 平台上运行，限制了扩散。采信 “高价与平台限制共同导致低市场份额” 的双因归因。

## 文献

- Accetta M, et al. Mach: A New Kernel Foundation for UNIX Development [C]. USENIX Summer 1986; Tevanian A. PhD Thesis [D]. CMU, 1988; Rashid R F. Threads of a New System [J]. Unix Review, 1986, 4(8): 37-49; bsd_commits.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22; 统计结论 [C-41] [C-42] 结果 [EB/OL]. 文献计量学分析.md Task 22, 2026-07-22.

---

## 史料登记与辩证校准（2026-08-08 追加）

> **本卷命题**：24.5 技术优秀不等于商业成功（详见本卷 00-总览“编纂指导思想叙事参照”）

### 史料文献
- NeXT Computer Inc. NeXTSTEP Reference, Release 0.9-3.0 [Z]. 1988-1992; CSRG. 4.3BSD-Tahoe/Reno Release Notes [Z]. Berkeley, 1988-1990; Golub D, et al. Unix as an Application Program [C]. USENIX Summer 1990 Conference Proceedings; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.

- Cox B J, Novobilski A J. Object-Oriented Programming: An Evolutionary Approach [M]. 2nd ed. Addison-Wesley, 1991; NeXT Computer Inc. NeXTSTEP Object-Oriented Programming and the Objective-C Language [Z]. 1993; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.

- Stanford University Library. NeXT Inc. Records, 1985-1996 [Z]. M1412; NeXT Inc. NeXTSTEP Source Code CREDITS Files [Z]. 1988-1996; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.

<!-- DOUBT_PENDING_BLOCK v20260804 -->

> **待核验登记（doubt 批量 2026-08-04 批11）**：
> 下列条目依 0 信任原则不改动正文，登记待核验：
>
> - 存疑 id 1728：NeXT 工程师贡献/OpenStep 规范依赖 Stanford M1412 纸质档案(未数字化)，待档案核验

- NeXT Computer Inc. Annual Reports, 1988-1993 [Z]; Levy S. Insanely Great [M]. Viking, 1994; USENIX Conference Proceedings, 1988-1996 [C]; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。
> 1985-2026 年间：2,012 次提交。

<!-- /DB_REF -->

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP591（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->
<!-- 关联说明：EP591 涉 Apple 收购 NeXT 继承 Mach 与 BSD 成果、专有 Unix 衰落等讨论，与本节 NeXTSTEP 起源主题部分直接相关；主持人个人 BSD 入门史段落为延伸内容，读者注意区分 -->

**要点**：

- 主持人讨论 Apple 在 1990 年代中后期濒临破产的处境：旧版 Mac OS 的 Copland 项目曾缩减至约三名开发者，BeOS 虽被视作备选平台，但事后被评价为尚非稳定的 Unix 系统。（BSD Now EP591，[426.6-493.8]，L2）[订正：原 [429.12-479.48]，2026-10-01 SenseAudio 重转核对]
- 主持人认为 Apple 通过收购 NeXT 继承了 Mach 与 BSD 的既有成果，从而以较低成本获得 Unix 平台的稳定性；并由此讨论若 NeXT 独立成功或 Apple 破产，个人计算机与开源生态的历史可能完全改写。　[存疑脚注] Apple 收购 NeXT 继承 Mach/BSD 成果并降低成本的因果概括系主持人单方推断，未经 Apple/NeXT 财务与工程档案核实。（BSD Now EP591，[477.6-522.5]，L4）[订正：原 [479.48-518.82]，2026-09-30 SenseAudio 重转核对]
- 主持人就专有 Unix 的衰落展开讨论：昂贵的专有 Unix 平台因创新迟缓与封闭生态而让位于廉价开放架构，PC 以低价与现成部件取胜，ARM 亦因低价而崛起。（BSD Now EP591，[561.6-672.6]，L2）[订正：原 [562.28-665.06]，2026-10-01 SenseAudio 重转核对]
- 三位主持人自述各自的 BSD 入门史：Benedikt 以 FreeBSD 5.2.1 入门，Jason 经 OpenBSD 2.8 与 OpenBSD 文档接触 BSD，Tom 在 PowerPC iBook G4 上尝试 OpenBSD 4.1 与 FreeBSD 7-current。（BSD Now EP591，[2101.6-2502.2]，L1）[订正：原 [2115.96-2492.78]，2026-10-01 SenseAudio 重转核对]

**史料**：

- 本期为主持人自访的口述史料；其中 Copland 开发者数量、Jean-Louis Gassée 对 BeOS 的评价及 IBM 与 Sun 收购细节均为主持人转述的二手信息。（BSD Now EP591，[426.6-475.7]，L2）[订正：原 [429.12-471.38]，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲5 没有必然性，只有偶然性：主持人关于 Apple 破产、NeXT 成功、IBM 收购 Sun 的反事实讨论，强调技术史由具体事件与偶然条件塑造，而非某种必然规律。　[存疑脚注] Apple 破产、NeXT 成功、IBM 收购 Sun 等反事实讨论为主持人现场发挥，无一手文献支撑，仅作口述史观点记录。（BSD Now EP591，[361.1-522.5]，L4）[订正：原 [373.70-518.82]，2026-10-01 SenseAudio 重转核对]
- 总纲22 知识注定过时：主持人从 Amiga、286、Z80 到专有 Unix 的淘汰中，呈现旧技术平台与其知识的持续更替，而非单纯的代际进步。（BSD Now EP591，[561.6-672.6]，L2）[订正：原 [562.28-665.06]，2026-10-01 SenseAudio 重转核对]

**辨析**：

- Copland 缩减至约三名开发者、Gassée 对 BeOS 的评价等说法均为主持人转述，缺乏当期一手档案佐证，应作存疑处理。　[存疑脚注] 相关数字与评价为主持人转述，未经 Apple 或计算机历史博物馆一手档案核实。（BSD Now EP591，[426.6-475.7]，L4）[订正：原 [429.12-471.38]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP591] Pennington J. BSD Now: 591: The Three Wise Men (hosts)[EB/OL]. (2024-12-26)[2026-08-15]. <https://www.bsdnow.tv/591>.

<!-- /PODCAST_REVIEW -->
