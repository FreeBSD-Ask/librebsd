---
chapter: 第 239 章
id: CH239
volume: 第12卷-macos的bsd遗产
---

# 第 239 章 apple收购next与rhapsody

## 要点

- **Apple** 于 **1996 年 12 月** 宣布收购 **NeXT**，**1997 年 2 月** 完成收购，交易金额约 **4.29 亿美元**（含 150 万股 Apple 股票）。**Jobs** 回归 Apple 任顾问，后任临时 CEO（iCEO，**1997 年 9 月 16 日** 任命）。**NeXTSTEP** 的 BSD 层与 Mach 内核成为 Apple 下一
- Rhapsody 采用 **Yellow Box** 与 **Blue Box** 双层架构——**Yellow Box** 是 Rhapsody 的面向对象应用框架（基于 NeXTSTEP 的 Foundation/AppKit，跨平台可移植至 Windows NT），提供 OpenStep API 兼容；〔待核：原文截断，后文待回源〕
- Rhapsody 早期工程团队由原 NeXT 团队与 Apple 收购后并入的 BSD/Mach 工程师构成。核心工程师包括 Avie Tevanian（原 NeXT 工程副总裁，Mach 内核核心开发者，随收购并入 Apple 任软件工程高级副总裁，主持 Rhapsody/Mac OS X 开发）；Wilfredo Sanchez（Apple 工程师，前 Apple/NeXT 工程师，负责 Da
- **1999 年** Mac OS X Server 1.0（3 月 16 日发布）对比 **FreeBSD 3.1**（1999 年 2 月 15 日发布）、**Linux 2.2**（1999 年 1 月 26 日发布）、**Windows NT 4.0 Server**（1996 年发布，1999 年仍为主流服务器 OS）、**Solaris 7**（1998 年 11 月发布，32 位与

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4066] 卷“第12卷-macos的bsd遗产”第 239 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 收购金额——以 Apple 1997 年 Form 10-K 与多源新闻报道交叉核验，约 4.29 亿美元（含 150 万股 Apple 股票），部分二手资料称 4.27 亿美元，差异源于汇率换算与股票估值时点，采信 “约 4.29 亿美元” 的判断。Jobs 回归与 NeXT 技术入选的因果关系——Jobs 回归是 Apple 董事会的人事决策，NeXT 技术入选是 Apple 工程团队的评估结
- Yellow Box 与 Cocoa 的关系——Yellow Box 是 Rhapsody 期的命名，Cocoa 是 Mac OS X 期（2000 年后）的命名，二者为同一 OpenStep API 实现的不同命名阶段。Blue Box 与 Classic/Carbon 的关系——Blue Box 是 Rhapsody 期的命名，Classic 是 Mac OS X 期的运行环境命名，Carbo
- Apple 与 FreeBSD 3.x 的代码关系——以 Darwin 源码仓库为准，Rhapsody 期（1997-1999）Darwin 的 BSD 层主要基于 NeXTSTEP 的 4.3BSD 派生代码，FreeBSD 3.x 的代码同步在 later Darwin 版本（Darwin 1.x，2001 年后）才显著。Jordan Hubbard 加入 Apple 的时间为 2001 年
- Mac OS X Server 1.0 的服务器市场定位——Apple 首次进入 “类 Unix 服务器” 市场，但其 Mach/BSD 混合内核在服务器性能上较 FreeBSD/Linux 单内核存在上下文切换开销，且 Apple 的硬件生态（Power Macintosh G3/G4）与服务器市场的 x86/SPARC 主流不兼容。Mac OS X Server 1.0 的 BSD 身份——其

## 文献

- Apple Inc. 1997 Annual Report (Form 10-K)[EB/OL]. (1997). U.S. Securities and Exchange Commission; Apple Inc. Apple to Acquire NeXT Software [EB/OL]. (1996-12-20). Apple Press Release; Apple Inc. Steve Jobs Named Interim CEO [EB/OL]. (1997-09-16). Apple Press Release; Singh A. Mac OS X Internals: A Systems Approach [M]. Addison-Wesley, 2006; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22; 统计结论 [C-49] 结果 [EB/OL]. 描述性统计.md SubTask 3.9 + 跨数据库关联分析.md Task 28, 2026-07-22.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1996-1997 年间：0 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. WWDC 1997 Technical Sessions: Rhapsody Yellow Box and Blue Box [EB/OL]. (1997-05). Apple Developer; Apple Inc. WWDC 1998 Technical Sessions: Carbon and Cocoa Roadmap [EB/OL]. (1998-05). Apple Developer; Singh A. Mac OS X Internals: A Systems Approach [M]. Addison-Wesley, 2006; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1997-1998 年间：0 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. Avie Tevanian Named Senior Vice President of Software Engineering [EB/OL]. (1997). Apple Press Release; darwin.duckdb 查询结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22; Darwin 源码仓库 opensource.apple.com [EB/OL]. <https://opensource.apple.com/>; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1999-1999 年间：0 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. Mac OS X Server 1.0 Release Notes [EB/OL]. (1999-03-16). Apple Developer; FreeBSD Project. FreeBSD 3.1 Release Notes [EB/OL]. (1999-02-15). <https://www.freebsd.org/releases/>; Linux Kernel Archives. Linux 2.2 Release Notes [EB/OL]. (1999-01-26). <https://www.kernel.org/>; Microsoft. Windows NT Server 4.0 [EB/OL]. (1996-1999). Microsoft Developer Network; Sun Microsystems. Solaris 7 Release Notes [EB/OL]. (1998-11). Sun Product Documentation; darwin.duckdb 查询 L7.5.1 结果 [EB/OL]. 衍生项目与跨项目对比分析.md §L7.5, 2026-07-22.FreeBSD 社区论文：[FP-2008-003] Mac OS X - From the server room to your pocket（Jordan K. Hubbard（乔丹·哈伯德），2008）<https://papers.freebsd.org/2008/lisa08/hubbard-macosx_from_the_server_room_to_your_pocket/>

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP591（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人讨论 Apple 在 1990 年代中后期濒临破产的处境：旧版 Mac OS 的 Copland 项目曾缩减至约三名开发者，BeOS 虽被视作备选平台，但事后被评价为尚非稳定的 Unix 系统。（BSD Now EP591，[429.12-479.48]，L2）
- 主持人认为 Apple 通过收购 NeXT 继承了 Mach 与 BSD 的既有成果，从而以较低成本获得 Unix 平台的稳定性；并由此讨论若 NeXT 独立成功或 Apple 破产，个人计算机与开源生态的历史可能完全改写。　[存疑脚注] Apple 收购 NeXT 继承 Mach/BSD 成果并降低成本的因果概括系主持人单方推断，未经 Apple/NeXT 财务与工程档案核实。（BSD Now EP591，[479.48-518.82]，L4）
- 主持人就专有 Unix 的衰落展开讨论：昂贵的专有 Unix 平台因创新迟缓与封闭生态而让位于廉价开放架构，PC 以低价与现成部件取胜，ARM 亦因低价而崛起。（BSD Now EP591，[562.28-665.06]，L2）
- 三位主持人自述各自的 BSD 入门史：Benedikt 以 FreeBSD 5.2.1 入门，Jason 经 OpenBSD 2.8 与 OpenBSD 文档接触 BSD，Tom 在 PowerPC iBook G4 上尝试 OpenBSD 4.1 与 FreeBSD 7-current。（BSD Now EP591，[2115.96-2492.78]，L1）

**史料**：

- 本期为主持人自访的口述史料；其中 Copland 开发者数量、Jean-Louis Gassée 对 BeOS 的评价及 IBM 与 Sun 收购细节均为主持人转述的二手信息。（BSD Now EP591，[429.12-471.38]，L2）

**史观**：

- 总纲5 没有必然性，只有偶然性：主持人关于 Apple 破产、NeXT 成功、IBM 收购 Sun 的反事实讨论，强调技术史由具体事件与偶然条件塑造，而非某种必然规律。　[存疑脚注] Apple 破产、NeXT 成功、IBM 收购 Sun 等反事实讨论为主持人现场发挥，无一手文献支撑，仅作口述史观点记录。（BSD Now EP591，[373.70-518.82]，L4）
- 总纲22 知识注定过时：主持人从 Amiga、286、Z80 到专有 Unix 的淘汰中，呈现旧技术平台与其知识的持续更替，而非单纯的代际进步。（BSD Now EP591，[562.28-665.06]，L2）

**辨析**：

- Copland 缩减至约三名开发者、Gassée 对 BeOS 的评价等说法均为主持人转述，缺乏当期一手档案佐证，应作存疑处理。　[存疑脚注] 相关数字与评价为主持人转述，未经 Apple 或计算机历史博物馆一手档案核实。（BSD Now EP591，[429.12-471.38]，L4）

**文献**：

- [BSD Now EP591] Pennington J. BSD Now: 591: The Three Wise Men (hosts)[EB/OL]. (2024-12-26)[2026-08-15]. <https://www.bsdnow.tv/591>.

<!-- /PODCAST_REVIEW -->
