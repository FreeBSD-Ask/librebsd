---
chapter: 第 118 章
id: CH118
volume: 第06卷-freebsd的核心技术革新
---

# 第 118 章 cheri的法律基础与硬件合作协议

## 要点

- CHERI 商用化进程的一手史料包括：CHERI 官方网站 cheri-cpu.org（持续更新项目进展和技术报告）；CHERI Alliance 官方网站 cheri-alliance.org（2024 年 11 月成立后的产业公告）；CheriBSD 各版本 Release Notes（22.05-25.03，记录 Morello 支持成熟度）；Arm Morello Program 官方文档
- Capsicum 和 CHERI 安全争议的一手史料包括：USENIX Security、IEEE S&P、ASPLOS、ISCA 等顶级安全/架构会议中关于能力系统局限性的论文；FreeBSD 邮件列表（freebsd-hackers@、freebsd-arch@、freebsd-security@）中关于 Capsicum 设计权衡的讨论；CHERI 技术报告系列中明确标注的 limitati
- Capsicum/CHERI 贡献者谱系的一手史料包括：各篇顶级会议论文的作者列表（USENIX Security 2010、ISCA 2014、IEEE S&P 2015、ASPLOS 2019 等核心论文）；FreeBSD/CheriBSD 源码仓库的 commit log 作者信息；剑桥大学 CHERI/Capsicum 项目页面的 people 目录；CHERI Alliance 成员公司
- Apple 在 macOS 10.7 Lion（2011）引入 Sandbox（基于 TrustedBSD MAC 框架），通过声明式 profile 限制应用资源访问；其底层借鉴 FreeBSD/TrustedBSD 的 MAC 思想，是 BSD 安全技术经 Darwin 间接影响商业桌面的案例。
- CHERI 许可策略的一手史料可在 CTSRD-CHERI GitHub 各仓库的 LICENSE 文件、CHERI 官方网站 cheri-cpu.org 的使用条款、CheriBSD 源码仓库的版权声明中查阅；CHERI 项目采用的许可证体系整体上是 BSD 风格的宽松许可，但需注意不同组件的细微差别：(1) CHERI ISA 规范文档和技术报告——Cambridge 开放发布，允许学术引用和

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3624] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3666] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3667] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3668] 卷“第06卷-freebsd的核心技术革新”第 118 章，匹配置信度 curated，原因：curated token rule
- [DB:bsdnow_podcast:outline_mappings:om_11029] BSD Now 第 583 期，匹配 CH118 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11422] BSD Now 第 538 期，匹配 CH118 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12107] BSD Now 第 456 期，匹配 CH118 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12912] BSD Now 第 148 期，匹配 CH118 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 关于 “FreeBSD Foundation 2024 年 Capsicum 与 bhyve 安全审计”——经检索 FreeBSD Foundation 官方博客和公告，2023-2024 年 FreeBSD Foundation 确实资助了多项安全审计工作，但专门针对 Capsicum+bhyve 的 Trail of Bits 审计报告公开信息有限 [存疑脚注：2026-08-17 Capsi
- 关于 “ANU 对 Capsicum/CHERI 的质疑”——原大纲提到 “ANU 质疑” 但未给出具体来源，经检索未找到澳大利亚国立大学（ANU）研究者公开发表的专门质疑 Capsicum/CHERI 的论文或文章；ANU 有计算机安全研究组，但 CHERI/Capsicum 相关批评论文主要来自其他机构（如 MIT、Georgia Tech、Google Project Zero 等），该说法
- Capsicum/CHERI 发展中 “看不见的贡献者”——代码审查者、测试人员、文档写作者、邮件列表讨论者的贡献很少被正式记录，但对项目成功同样重要；FreeBSD 基金会在 Capsicum 工程化中的资助和项目管理角色常被低估，基金会不仅提供资金，还协调开发进度和代码审查；原模板文献列表中大量无关文献已删除并替换为贡献者相关的权威来源
- macOS Sandbox 基于 MAC profile 而非 Capsicum capability，二者范式不同；但其 BSD 血统说明 BSD 安全研究对主流桌面 OS 的实际影响。
- 原大纲本节称“CHERI ISA 以 BSD 许可证发布”需更精确表述——CHERI ISA 规范不是单一许可证文件覆盖的软件项目，而是技术文档和架构规范；具体实现代码（硬件 RTL、软件）使用 BSD 许可，规范本身由 Cambridge/SRI 以允许自由实现的条款发布；“ARM Morello 原型板的硬件设计文档受 ARM 商业许可约束”这一表述准确，但研究者可以通过 DSbD 计划免费获

## 文献

- CHERI Project. CHERI CPU Official Website. cheri-cpu.org; CHERI Alliance. Industry Consortium (2024). cheri-alliance.org; CheriBSD Project. Release Notes Archive. cheribsd.org/release-notes/; UK Research and Innovation. Digital Security by Design Programme. ukri.org; DARPA. CRASH/SSITH Program Archives. darpa.mil; FreeBSD Foundation. Quarterly Status Reports (2023-2025). freebsdfoundation.org.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2023-2025 年间：182,991 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project Mailing Lists. Capsicum/CHERI Discussion Threads (2010-2025). lists.freebsd.org; University of Cambridge. CHERI Technical Report Series (UCAM-CL-TR). cl.cam.ac.uk/techreports/; Association for Computing Machinery. SIGSAC/SIGARCH Conference Proceedings (2010-2025); LWN.net. Capsicum/CHERI Coverage and Comments. lwn.net. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- CHERI/Capsicum Core Conference Papers (2010-2025); FreeBSD/CheriBSD Git Commit History. github.com/freebsd/freebsd-src, github.com/CTSRD-CHERI/cheribsd; University of Cambridge. Capsicum/CHERI People Pages. cl.cam.ac.uk; FreeBSD Foundation. Annual Reports (2012-2025). freebsdfoundation.org; Neumann, P. G. (1985-2025). ACM RISKS Forum Archive. catless.ncl.ac.uk/Risks/. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Apple. App Sandbox Design Guide [Z]. 2011；TrustedBSD Project. MAC Framework [EB/OL]. ［B］    FreeBSD 社区论文与演讲 [258] Ryan Stone. Oblivious Sandboxing with Capsicum and EBPF [C]//BSDCan 2020. [S.l.]: [s.n.], 2020. 获取路径：<https://papers.freebsd.org/2020/bsdcan/stone-oblivious_sandboxing_capsicum_ebpf/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [250] Brooks Davis. CheriABI: Enforcing Valid Pointer Provenance and Minimizing Pointer Privilege in the POSIX C Run-time Environment [C]//ASPLOS 2019. [S.l.]: [s.n.], 2019. 获取路径：<https://papers.freebsd.org/2019/davis-asplos-cheriabi/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [79] Mariusz Zaborski. Capsicum and Casper - a fairy tale about solving security problems [C]//AsiaBSDCon 2016. [S.l.]: [s.n.], 2016. 获取路径：<https://papers.freebsd.org/2016/asiabsdcon/oshogbo-capsicum_and_casper/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [27] Robert N. M. Watson. The TrustedBSD MAC Framework: Extensible Kernel Access Control for FreeBSD 5.0 [C]//BSDCon 2003. [S.l.]: [s.n.], 2003. 获取路径：<https://papers.freebsd.org/2003/rwatson-mac_framework/> [访问日期 2026-07-26].[^doubt-resolved-641]: 据 张鹏宇_基于微内核的操作系统安全机制研究 (03-15, 2024) 消解[^doubt-resolved-642]: 据 young-m-1958-the-rise-of-the-meritocracy-thames-hudson-isbn (Young, 1958) 消解[^doubt-resolved-643]: 据 unknown_Charter-of-the-City-of-Berkeley_v1 (未署名) 消解[^doubt-resolved-644]: 据 The-copyinout-Framework (未署名) 消解[^doubt-resolved-645]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-646]: 据 Design_Implementation_FreeBSD_OS (未署名) 消解

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2013 年间：148,830 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- CTSRD-CHERI Organization. GitHub Repositories and LICENSE Files. github.com/CTSRD-CHERI; CHERI Alliance. cheri-alliance.org; University of Cambridge/SRI International. CHERI Technical Report Series (UCAM-CL-TR).［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- CTSRD-CHERI. CheriBSD Repository (AUTHORS, commit history). github.com/CTSRD-CHERI/cheribsd; Davis, B. et al. (2019). CheriABI (full author list). ASPLOS '19; CheriBSD Project. Release Notes 22.05-25.03. cheribsd.org/release-notes/; CheriBSD Getting Started. ctsrd-cheri.github.io/cheribsd-getting-started/. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP529、BSD Now EP50（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人介绍 Lawrence Tratt 关于将内存分配器适配到 CHERI 的文章：CHERI 的能力架构将 64 位指针扩展为 128 位能力，purecap 模式下分配器若不将返回能力的边界限制在所分配的内存范围，就无法获得超越传统系统的安全收益。（BSD Now EP529，[652.58-1375.82]，L2）
- 主持人转述 Scott Fahlman 于 1982 年 9 月 19 日在卡内基梅隆大学公告板提出“:-)”与“:-(”作为笑话标记，其原始消息直到 2002 年才从备份磁带中找回，成为 emoticon 起源的文化史片段。（BSD Now EP529，[2636.36-2699.48]，L2）
- Robert Watson 自述其进入 BSD 的起点是高中时期学校获赠的运行 BSD/OS 的 UNIX 服务器，并由此转向操作系统安全研究。（BSD Now EP50，[1309.66-1351.62]，L1）
- Capsicum 能力沙箱设计约始于八年前，其内核接口已随 FreeBSD 发布，Google 亦将其移植至 Linux 并首次向内核邮件列表提交补丁。（BSD Now EP50，[1462.14-1489.42]，L1）
- FreeBSD 10 已将 tcpdump、gzip 等基础工具纳入 Capsicum 沙箱，以降低以 root 运行、处理不可信输入程序被利用后的影响。（BSD Now EP50，[1565.14-1606.06]，L1）
- OpenSSL 于 2014 年 8 月发布修复九个漏洞的新版本，LibreSSL 对其中五项完全受影响、一项部分受影响、三项因移除相关代码而不受影响。（BSD Now EP50，[897.62-988.06]，L2）

**史料**：

- 本期核心史料为 Lawrence Tratt 的 CHERI 内存分配器技术文章与 Scott Fahlman 的原始公告板消息截图，二者均经主持人口头转述。（BSD Now EP529，[652.58-2699.48]，L2）
- Robert Watson 访谈（当事人自述，FreeBSD 核心团队成员与剑桥大学讲师）。（BSD Now EP50，[1294.82-2231.72]，L1）
- OpenSSL 0.9.8zb、1.0.0n、1.0.1i 安全公告与 LibreSSL 新版本发布信息（主持人口头转述；新转写仅提及 LibreSSL 发布新版本，未及版本号）。（BSD Now EP50，[897.62-983.42]，L2）[订正：原 "LibreSSL 2.0.5 发布信息"，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲12 科学是形式主义：CHERI 以形式化的能力边界约束内存访问，安全收益取决于软件对形式规则的适配，呈现安全机制作为形式主义系统的特征。（BSD Now EP529，[943.14-1150.42]，L2）
- 总纲10 动手者创造历史：Robert Watson 团队以编写并落地 Capsicum、BERI/CHERI 的方式实际推动操作系统安全演进。（BSD Now EP50，[1380.46-1462.14]，L1）
- 总纲9 经验优先：访谈以当事人对代码、硬件与漏洞的一手经验为叙述依据，而非抽象安全口号。（BSD Now EP50，[1451.54-1571.28]，L1）
- 总纲22 知识注定过时：OpenSSL 与 LibreSSL 的持续修补显示安全知识处于不断失效与重写的循环之中。（BSD Now EP50，[957.56-988.06]，L2）

**辨析**：

- Scott Fahlman 提出 emoticon 的具体日期来自节目转述的推文，须以卡内基梅隆大学保存的原始消息核实。 [存疑脚注] emoticon 起源日期为二手转述，未经 CMU 原始档案核实。（BSD Now EP529，[2636.36-2699.48]，L4）
- Watson 自述尚不清楚 FreeBSD 10 发布以来沙箱化基础工具实际缓解了多少已公开漏洞，量化效果存疑。 [存疑脚注] 沙箱缓解漏洞的量化结论缺乏公开统计数据支撑（BSD Now EP50，[1578.68-1585.78]，L4）

**文献**：

- [BSD Now EP529] Pennington J. BSD Now: 529: Adapt, adopt, diffuse[EB/OL]. (2023-10-19)[2026-08-15]. <https://www.bsdnow.tv/529>.
- [BSD Now EP50] Pennington J. BSD Now: 50: VPN, My Dear Watson[EB/OL]. (2014-08-13)[2026-08-15]. <https://www.bsdnow.tv/50>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Watson. R. N. M. et al. (2024). CHERI: Hardware-Enabled C/C++ Memory Protection at Scale. IEEE Security & Privacy, 22(4)[C]. 2024. ［DKC-1908→fulltext:6004］
<!-- /dangan-20260908 -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-676 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-676`；w172 YouTube 章节路由采纳）

据〔November 2023 FreeBSD Vendor Summit〕讲者口述：讲者称 FreeBSD 首版发布于 1993 年，1996 年即出现缓冲区溢出黑客写手文 Smashing the Stack for Fun and Profit。（YouTube EPJsQoonHCGAw，[145.12-166.959]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-675 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-675`；w172 YouTube 章节路由采纳）

据〔November 2023 FreeBSD Vendor Summit〕讲者口述：讲者援引 Wikipedia 指出，缓冲区溢出作为攻击手段最早见于 1972 年的一份文献。（YouTube EPJsQoonHCGAw，[85.119-97.64]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-990 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-990`；w172 YouTube 章节路由采纳）

据〔November 2023 FreeBSD Vendor Summit〕讲者口述：1988 年 Morris 蠕虫使用的多种手段之一就是缓冲区溢出，讲者以此讲缓冲区溢出史。（YouTube EPU3lfk3tNEWU，[119-127.469]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1249 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1249`；w172 YouTube 章节路由采纳）

据来源不详讲者口述：CheriBSD 是一个 FreeBSD 的研究分支，旨在支持 Cheri CPU。（YouTube EPaMbuSbQM7Bo，[14.8-37.7]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1251 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1251`；w172 YouTube 章节路由采纳）

据来源不详讲者口述：该团队在 ASPLOS 2015 发表过一篇关于其 C 语言模型的论文，并由此认识到指针必须独立于 base 与 length 之外存在。（YouTube EPaMbuSbQM7Bo，[2645.6-2658.8]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1250 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1250`；w172 YouTube 章节路由采纳）

据来源不详讲者口述：CheriBSD 于 2013 年迁移到 GitHub。（YouTube EPaMbuSbQM7Bo，[2046.1-2050.7]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-354 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-354`；w172 YouTube 章节路由采纳）

据〔FreeBSD Developer Summit, June 2022〕讲者口述：即便已有 AddressSanitizer 与静态分析，缓冲区溢出问题依然普遍存在（YouTube EPbP546j9REKg，[202.48-206.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-373 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-373`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Brooks Davis 口述：2010 年做出的决策是在 MIPS 上采取新增指令特性的兼容扩展路径（转写音作“the MIPS II thing”）（YouTube EPcAuhWjDDM0k，[2125.29-2131.849]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-372 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-372`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Brooks Davis 口述：CheriABI 相关工作仍在进行，在 DARPA 项目资助下将 ISA 从 MIPS 移植到 RISC-V（转写音作“risk 5”）（YouTube EPcAuhWjDDM0k，[2406.109-2412.2]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-977 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-977`；w172 YouTube 章节路由采纳）

据〔CheriBSD 技术分享〕讲者 Andrew Turner 口述：讲者为 FreeBSD committer 约 10 年，主要工作为 arm64，副业项目为内核移植。（YouTube EPtwZXvKNZOvU，[25.039-32.47]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1171 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1171`；w172 YouTube 章节路由采纳）

据〔FreeBSD Fridays〕讲者口述：CHERI 项目最初以 MIPS 平台为基础（转写音作 cherry）。（YouTube EPyrk5FfjHDCo，[2088-2091.669]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1592 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1592`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔#CheriABI: Hardware enforced memory safety for #FreeBSD，Brooks Davis 演讲〕讲者口述：他声称已经得到一个完整的类 UNIX 操作系统，以硬件强制的空间与引用内存安全方式编译而成，覆盖用户态程序、库、动态链接器，以及内核访问用户内存的路径——当内核试图访问用户传入的数组而用户给出的长度参数错误时，不会越过分配边界。（YouTube EPR4iTt6rYwHM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1593 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1593`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔#CheriABI: Hardware enforced memory safety for #FreeBSD，Brooks Davis 演讲〕讲者口述：讲者介绍其纯能力模式（pure capability mode）实现建立在 Cherry BSD 之上，而 Cherry BSD 是一个带 CHERI 支持的 FreeBSD 分叉；在该模式中程序内的所有指针都是能力，包括系统调用的参数与内核返回的值。（YouTube EPR4iTt6rYwHM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1594 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1594`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔#CheriABI: Hardware enforced memory safety for #FreeBSD，Brooks Davis 演讲〕讲者口述：相较现行 FreeBSD 的构建系统，该工作改为先构建能力版库、再构建程序，因此必须改动 FreeBSD 的程序构建基础设施，使每个程序可选择以混合二进制或纯能力二进制方式链接。（YouTube EPR4iTt6rYwHM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1595 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1595`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔#CheriABI: Hardware enforced memory safety for #FreeBSD，Brooks Davis 演讲〕讲者口述：由于在该系统中所有用户态访问都经由能力，讲者指出 FreeBSD 内核原有的 copyin／copyout 系列函数需要对应的能力感知版本；在非能力型进程中调用普通版本会直接报错。（YouTube EPR4iTt6rYwHM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
