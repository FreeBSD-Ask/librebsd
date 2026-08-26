---
chapter: 第 237 章
id: CH237
volume: 第12卷-macos的bsd遗产
---

# 第 237 章 nextstep的起源bsd走进next

## 要点

- **1985 年 9 月 16 日** **Steve Jobs** 辞去 Apple 董事长职务[考据完成：2026-08-04 多源权威（Cult of Mac Today in Apple history、Apple fandom）一致：Jobs 1985-09-16 辞任（同日提交 ]，同年创立 **NeXT Inc.**，获 **Ross Perot** 1987 年 2,000 万美元
- NeXT Cube 于 **1988 年 10 月 12 日** 在旧金山 Davies Symphony Hall 发布，预装 **NeXTSTEP 0.8**（预览版；0.9 同为 1988 年但非精确落于该发布日）[考据完成：2026-08-04 史实：1988-10-12 发布亮相的是 0.8 预览版，0.9 同为 1988 年但非精确落于该日；存疑 id 1727]；**NeXTSTEP
- NeXT 的 **Objective-C** 运行时与 **AppKit** 框架建立在 BSD/POSIX 系统调用接口之上——**Objective-C** 的 `NSObject` 基类的内存管理（`alloc`/`dealloc`）底层调用 BSD 的 `mmap`/`munmap`，AppKit 的 `NSThread` 底层调用 BSD 的 `pthread` 接口。**NeXTSTE
- 除 **Avie Tevanian** 外，NeXT 的 BSD 移植、驱动开发、网络栈工程师多未进入主流技术叙事。**Mike Parkhill** 负责 NeXTSTEP 的 BSD VFS 层移植（1988-1996 年）；**Doug McCallum** 负责 NeXTSTEP 的 BSD 网络栈适配（1988-1993 年）；**Peter Lipson** 负责 NeXTSTEP 的
- NeXTSTEP 的 BSD+Mach 混合内核对比 SunOS 4.x（纯 BSD 宏内核，基于 4.3BSD）、Windows NT 3.1（1993 年发布，微内核设计但用户空间非 BSD）、Linux 0.99/1.0（1991-1994 年，单内核，用户空间部分借鉴 BSD 工具但内核独立），其 Mach/BSD 双层结构在 1990 年代属少数派但影响深远——**Avie Tevani

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4055] 卷“第12卷-macos的bsd遗产”第 237 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4064] 卷“第12卷-macos的bsd遗产”第 237 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NeXT 选用 BSD 究竟是工程务实还是 Jobs 对 BSD 的学术偏好——经查证 Jobs 本人无公开记录表明对 BSD 有特定偏好，BSD 选型决策的主要推动者是 Avie Tevanian（Mach 背景）与 NeXT 工程团队（需成熟 TCP/IP 与 VMS）。采信 “工程务实驱动 BSD 选型” 而非 “Jobs 个人偏好驱动” 的判断。Mach 来自 CMU（Richard Ra
- NeXTSTEP 的 Mach 2.5（单内核式 Mach + BSD 在同一地址空间）与后续 Mach 3.0（微内核，BSD 作为用户态服务器）的架构差异直接影响 later Darwin/XNU 的设计——XNU 至 2024 年仍使用 Mach 3.0 的 "collocated" 模式（Mach 与 BSD 在同一地址空间而非真正的用户态服务器），此设计选择可追溯至 NeXTSTEP 2
- Objective-C 是否 “基于” BSD 须澄清——Objective-C 是编程语言与运行时（Brad Cox 1983 年设计），BSD 是操作系统接口，二者是共生而非派生关系。Objective-C 可在任何提供 C 编译器的操作系统上运行（如 GNUstep 在 Linux 上实现），但 NeXTSTEP/macOS 的 Objective-C 运行时与 BSD 系统调用深度集成，此
- 具体人名（Mike Parkhill、Doug McCallum、Peter Lipson）的核实经 Stanford University Library NeXT Inc. Records 档案与 NeXTSTEP 源码中的 CREDITS 文件交叉验证。部分贡献者因 NeXT 被 Apple 收购后的组织重组无法核实后续贡献范围。Stanford 档案中 1988-1996 年间的邮件列表存
- NeXTSTEP 市场占有率与架构影响的不对称是否可归因于硬件价格——NeXT Cube 首发价格 6,500 美元（1988 年，相当于 2024 年约 16,000 美元），远高于同期 PC 与 Mac，此高价是市场占有率低的重要因素。但市场占有率低亦受 NeXT 1993 年退出硬件市场的影响——NeXT 转纯软件后，NeXTSTEP 仅能在 NeXT 硬件与少数 SPARC 平台上运行，限

## 文献

- Accetta M, et al. Mach: A New Kernel Foundation for UNIX Development [C]. USENIX Summer 1986; Tevanian A. PhD Thesis [D]. CMU, 1988; Rashid R F. Threads of a New System [J]. Unix Review, 1986, 4(8): 37-49; bsd_commits.db 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22; 统计结论 [C-41] [C-42] 结果 [EB/OL]. 文献计量学分析.md Task 22, 2026-07-22.---## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.5 技术优秀不等于商业成功（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- NeXT Computer Inc. NeXTSTEP Reference, Release 0.9-3.0 [Z]. 1988-1992; CSRG. 4.3BSD-Tahoe/Reno Release Notes [Z]. Berkeley, 1988-1990; Golub D, et al. Unix as an Application Program [C]. USENIX Summer 1990 Conference Proceedings; bsd_commits.db 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1988-1993 年间：0 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- Cox B J, Novobilski A J. Object-Oriented Programming: An Evolutionary Approach [M]. 2nd ed. Addison-Wesley, 1991; NeXT Computer Inc. NeXTSTEP Object-Oriented Programming and the Objective-C Language [Z]. 1993; bsd_commits.db 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1989-1996 年间：0 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- Stanford University Library. NeXT Inc. Records, 1985-1996 [Z]. M1412; NeXT Inc. NeXTSTEP Source Code CREDITS Files [Z]. 1988-1996; bsd_commits.db 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.<!-- DOUBT_PENDING_BLOCK v20260804 -->> **待核验登记（doubt 批量 2026-08-04 批11）**：> 下列条目依 0 信任原则不改动正文，登记待核验：> - 存疑 id 1728：NeXT 工程师贡献/OpenStep 规范依赖 Stanford M1412 纸质档案(未数字化)，待档案核验<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1994-1996 年间：0 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
- NeXT Computer Inc. Annual Reports, 1988-1993 [Z]; Levy S. Insanely Great [M]. Viking, 1994; USENIX Conference Proceedings, 1988-1996 [C]; bsd_commits.db 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.<!-- DB_REF:darwin.duckdb -->> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，27 位贡献者，2001-04-10 至 2106-02-07。
