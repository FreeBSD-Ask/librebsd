---
chapter: 第 143 章
id: CH143
volume: 第07卷-freebsd的工程体系重构
---

# 第143章 工具链替换与架构支持

## 要点

- i386 和 amd64（x86）是 Clang/LLVM 最早支持且最成熟的架构，也是 FreeBSD 首批完成 Clang 迁移的架构。Roman Divacky 于 2009 年 2 月宣布 Clang 可编译可启动的 i386/amd64 内核；FreeBSD 9.0（2012）中 i386/amd64 world 和 GENERIC 内核已可完整使用 Clang 构建；2012 年 11 月 Brooks Davis 在 -CURRENT 中切换 Clang 为 x86 默认编译器；FreeBSD 10.0（2014.1.20）正式在 RELEASE 版本中将 Clang 设为 i386/amd64 默认且不再默认安装 GCC。x86 架构的 Clang 支持成熟得益于 Apple 的长期投入——macOS/iOS 均运行在 x86（及后续 Apple Silicon）上，Clang x86 后端是优化最好、测试最充分的后端之一。
- arm64（AArch64）架构在 FreeBSD 中的支持是 Clang/LLVM 迁移的重要副产品——GCC 4.2.1 完全不支持 AArch64（ARM 64 位架构在 2011 年才发布，远晚于 GCC 4.2.1 的 2007 年），因此没有 Clang 就不可能有 FreeBSD/arm64。Andrew Turner（andrew@）是 FreeBSD/arm64 移植的主要开发者，在 FreeBSD Foundation 和商业赞助商支持下完成了 arm64 支持。FreeBSD 11.0（2016.10.10）首次将 arm64 作为支持架构发布（但非 Tier 1）；FreeBSD 13.0（2021.4.13）正式将 arm64/AArch64 提升为 Tier 1 架构，与 amd64 并列获得发布镜像、二进制包、安全更新的全面支持。Clang/LLVM 对 AArch64 的原生支持（AArch64 后端由 ARM 公司和 Apple 工程师联合开发，质量极高）使 FreeBSD/arm64 从一开始就有高质量编译器支持——这与 mips/powerpc/sparc64 等旧架构在 Clang 迁移中挣扎形成鲜明对比。arm64 升为 Tier 1 标志着 FreeBSD 正式进入 64 位 ARM 服务器、云原生和嵌入式市场。
- powerpc、mips、sparc64 等旧架构的 Clang 支持远落后于 x86 和 arm64，是 GCC 4.2.1 在 FreeBSD base 中保留多年的主要原因。powerpc（32 位和 64 位 powerpc64）的 Clang 支持在 FreeBSD 11/12 时期逐步完善，但在某些 powerpc 变体上仍有问题；mips 架构因 MIPS 公司转向 RISC-V 和 MIPS 设计本身的复杂性（多种 ABI、尾码、原子操作模型），Clang 支持长期不完善；sparc64（Sun/Oracle SPARC 64 位）的 Clang 支持进展最慢，且 SPARC 硬件市场在 Oracle 收购 Sun 后急剧萎缩。这些架构的支持路径分三种：①Clang 支持逐步完善后切换（如 powerpc64 在较晚版本完成）；② 架构本身因市场萎缩而被降级或废弃（sparc64 在 FreeBSD 13 降级为 Tier 2，mips 在 FreeBSD 13 后也逐步降级）；③ 社区通过外部 GCC 工具链（ports/devel/gcc 或外部 binutils）继续支持非 Tier 1 架构。RISC-V 作为新架构从一开始就依赖 Clang/LLVM 支持（GCC 4.2.1 不可能支持 RISC-V），FreeBSD/riscv 从开发初期即使用 Clang。各架构 Clang 支持与迁移状态汇总见下表。
- 非 x86 架构的 Clang 支持进度是 GCC 从 FreeBSD base 完全移除的主要阻塞因素。迁移的关键时间节点如下：①2009.2——i386/amd64 内核可启动（Divacky）；②2012.1——FreeBSD 9.0 发布，Clang 导入 base 但 GCC 默认；③2012.11——x86 -CURRENT 默认 Clang；④2014.1——FreeBSD 10.0 发布，i386/amd64 默认 Clang，GCC 仍为其他架构保留；⑤2016.10——FreeBSD 11.0 发布，arm64 首次作为支持架构；⑥2018.12——FreeBSD 12.0 发布，lld 为 x86/armv7 默认 linker，gdb 移至 libexec，LLVM 6.0.1，ELF Tool Chain r3614；⑦2018——Warner Losh 宣布 GCC 4.2.1 退休（所有受支持架构已使用 Clang 或外部工具链）；⑧2021.4——FreeBSD 13.0 发布，arm64 升为 Tier 1，LLVM Clang 11，移除过时 GNU 工具（含 GCC 和 grep）；⑨2024.7——FreeBSD 15-CURRENT 移除 dialog（最后一个 GPL 组件；2024 年 7 月主线为 15-CURRENT，16-CURRENT 当时未分支）。
- OpenBSD 在 FreeBSD 之后也进行了 Clang 迁移，但时间更晚、策略更分阶段。OpenBSD 长期使用 GCC 3.x（GPLv2 版本）作为默认编译器以回避 GPLv3 问题；当 GCC 3.x 过老无法支持新硬件和 C++ 标准时，OpenBSD 开始评估 Clang。OpenBSD 的 Clang 迁移分架构逐批完成：amd64/i386 于 2017 年 7 月 26 日（OpenBSD 6.2 开发周期）切换默认编译器（Robert Nagy 提交）；armv7 于 2018 年 1 月 19 日切换（Mark Kettenis（马克·凯特尼斯） 提交）；octeon（Cavium OCTEON MIPS64）于 2019 年 7 月切换；powerpc 于 2020 年 4 月切换；loongson（MIPS64 Loongson）于 2020 年 12 月切换。OpenBSD 的许可证纯洁化更广泛：mandoc（Ingo Schwarze（英戈·施瓦茨） 开发，OpenBSD 项目）替代 groff、LibreSSL（2014 年 Heartbleed 后 Theo de Raadt（西奥·德·若特） 领导 fork）替代 OpenSSL，但需注意 LibreSSL 仅在 OpenBSD base 中为默认，FreeBSD base 仍使用 OpenSSL。

## 史观

- 总纲第 15 条——文化即形式主义（存疑）：架构支持优先级与商业生态直接相关——x86 作为服务器/桌面主流架构获得最优先支持，而这与 Apple 自身产品需求高度重合，FreeBSD 搭了 Apple 投入的便车。〔订正注：原挂“总纲第 17 条——软件工程”系伪标签，权威第 17 条为“证明世界先于解释和改造世界”；按核查处方改挂第 15 条〕
  - 辨析：“Clang 可编译内核” 和 “Clang 可编译所有内核模块” 是两个不同里程碑——2009 年是 GENERIC 内核可启动，但部分第三方模块和非标准配置仍需修复。
  - 文献：Divacky R. 2009 kernel announcement [EB/OL]；Davis B. 2012 default announcement [EB/OL]；FreeBSD 9.0/10.0 Release Notes [Z].〔存疑：原句截断（“文”），按辨析节同源文献行补全〕
- 总纲第 3 条——不存在进步，只有权力再分配（存疑）：GCC 4.2.1 从 base 移除的标志不是 “所有架构都用 Clang”，而是 “所有 Tier 1 架构都用 Clang，Tier 2/Tier 3 架构可依赖 ports GCC”。这标志着 FreeBSD 工具链策略从 “base 支持所有架构” 转向 “base 保证 Tier 1 质量，其他架构由 ports/社区支持” 的分层模式。〔订正注：原挂“总纲第 25 条——终结与延续”系伪标签，权威第 25 条为“逻辑是形式主义而非世界本身的结构”；按核查处方改挂第 3 条〕
- 辨析：架构的 Tier 级别是动态调整的——sparc64 从 FreeBSD 13 起不再是 Tier 1，mips 支持也大幅缩水，但这不完全归因于 Clang 迁移；SPARC 和 MIPS 硬件市场在 2010 年代的整体衰退是更深层原因〔存疑：原句截断，按辨析节同源文本补全〕
- 总纲第 21 条——革命与改革是历史方法论的分歧（存疑）：OpenBSD 比 FreeBSD 晚约三年半切换 amd64/i386 默认 Clang（FreeBSD 2014.1 vs OpenBSD 2017.7），这反映了两个项目不同的工程优先级——FreeBSD 因 C++11 支持需求和 Apple 投入更迫切需要迁移，OpenBSD 因长期停留在 GCC 3（GPLv2）而推迟了切换压力。〔订正注：原挂“总纲第 6 条——技术路线分化”系伪标签，权威第 6 条为“和解优于斗争”；按核查处方改挂第 21 条〕
  - 辨析：原文件误称 “OpenBSD 5.5 默认 Clang” 或 “2014 年”——经 OpenBSD CVS commit log 交叉验证，amd64/i386 实际切换时间为 2017 年 7 月 26 日（commit 时间戳精确到日），5.5 是 2014 年 5 月发布〔存疑：原句截断，按辨析节同源文本补全〕
- 总纲第 4 条——分离聚合是永恒规律（存疑）：Linux 无需迁移 Clang 的法律基础是 Torvalds 在 2006-2007 年拒绝将 Linux 内核升级到 GPLv3——GCC 4.3+ 的 GPLv3 许可证适用于编译器本身，但编译输出（内核）的许可证由内核作者决定而非编译器许可证决定（FSF 明确确认），因此 GCC GPLv3 对 Linux 内核不构成许可证危机。这一法律解释的差异是 Linux 与 FreeBSD 在编译器许可证路线上分合的生态背景〔存疑：原句截断（“这一法律解释的差异是 Li”），结尾按辨析节同源文本改写补全〕〔订正注：原挂“总纲第 6 条——技术路线分化”系伪标签，权威第 6 条为“和解优于斗争”；按核查处方改挂第 4 条〕
- 总纲第 4 条——分离聚合是永恒规律（存疑）：中文开源社区的许可证认知受 Linux 在中国的普及路径深刻影响——Linux 作为最早进入中国的开源操作系统之一，其 GPL 话语通过红旗 Linux、中国开源软件推进联盟等渠道成为默认认知框架，BSD 家族（FreeBSD/OpenBSD/NetBSD）在中国用户基数较小，声音相对微弱。〔订正注：原挂“总纲第 11 条——国家政策”系伪标签，权威第 11 条为“商品是形式主义”；按论旨改挂第 4 条〕
  - 辨析：阮一峰 2008-2011 年博客文章将 BSD 许可证描述为“更宽松但允许闭源”，系其时代局限性产物，史实主张须以一手史料独立核验〔存疑：原句截断，按辨析节同源文本补全；阮一峰系禁引来源，仅作观点元引用考据〕

## 辨析

- “Clang 可编译内核” 和 “Clang 可编译所有内核模块” 是两个不同里程碑——2009 年是 GENERIC 内核可启动，但部分第三方模块和非标准配置仍需修复。
  - 文献：Divacky R. 2009 kernel announcement [EB/OL]；Davis B. 2012 default announcement [EB/OL]；FreeBSD 9.0/10.0 Release Notes [Z].〔存疑：原行截断，按要点时间线同源信息补全〕
- 架构的 Tier 级别是动态调整的——sparc64 从 FreeBSD 13 起不再是 Tier 1，mips 支持也大幅缩水，但这不完全归因于 Clang 迁移；SPARC 和 MIPS 硬件市场在 2010 年代的整体衰退（Oracle 终止 SPARC 服务器开发、MIPS 公司转向 RISC-V）是更深层原因。
- 文献：FreeBSD Project. Supported Architectures [EB/OL]. freebsd.org/platforms/〔存疑：原行截断，按文献节同源条目补全〕
- 原文件误称 “OpenBSD 5.5 默认 Clang” 或 “2014 年”——经 OpenBSD CVS commit log 交叉验证，amd64/i386 实际切换时间为 2017 年 7 月 26 日（commit 时间戳精确到日），5.5 是 2014 年 5 月发布，此错误已修正。〔待核：原文截断，后文待回源〕
- “GCC GPL 传染编译产物” 是常见误解——FSF 明确表示 GCC 的 GPL 许可证不适用于 GCC 编译输出的程序（只要不是基于 GCC 运行时库的 GPL 代码片段衍生），GCC Runtime Library Exception 进一步明确了这一点。因此 Linux 使用 GCC 4.3+（GPLv3）不涉及许可证问题，但 FreeBSD base 系统中包含 GCC 二进制和库文件〔存疑：原文截断，后文待回源〕
- 阮一峰 2008-2011 年博客文章将 BSD 许可证描述为“更宽松但允许闭源”〔阮一峰为禁引来源，本辨析仅作其观点元引用考据，其全部史实主张须独立核验〕是其时代局限性产物——当时 Clang 尚未成为 FreeBSD 默认（2014.1.20 才默认化），LLVM/Clang 技术成熟度也远不及 2020 年代；阮一峰博客作为中文世界早期开源启蒙材料有其历史贡献，但其对 BSD 许可证批评的具体展开在此著录截断〔存疑：原文截断，后文待回源〕

## 文献

- Divacky R. 2009 kernel announcement [EB/OL]；Davis B. 2012 default announcement [EB/OL]；FreeBSD 9.0/10.0 Release Notes [Z].［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
    FreeBSD 社区论文与演讲 [258]，[258] Ryan Stone. Oblivious Sandboxing with Capsicum and EBPF [C]//BS〔存疑：著录截断，会议名待回源；编号双写 [258]，[258] 待统一〕
- FreeBSD Project. Supported Architectures [EB/OL]. freebsd.org/platforms/；FreeBSD 12.0/13.0 Release Notes [Z]；Losh W. GCC 4.2.1 retirement email [EB/OL]. freebsd-arch, 2018. ［A］


<!-- dangan-20260908 消解回写 -->
- Google.. Clang is now used to build Chrome for Windows [EB/OL]. LLVM Project Blog, 2018-03-05[EB/OL]. 2018. ［DKC-2149→fulltext:6085］
<!-- /dangan-20260908 -->
## 143.10.4 架构支持对迁移时间线的效应

- 要点：非 x86 架构的 Clang 支持进度是 GCC 从 FreeBSD base 完全移除的主要阻塞因素。迁移的关键时间节点如下：①2009.2——i386/amd64 内核可启动（Divacky）；②2012.1——FreeBSD 9.0 发布，Clang 导入 base 但 GCC 默认；③2012.11——x86 -CURRENT 默认 Clang；④2014.1——FreeBSD 10.0 发布，i386/amd64 默认 Clang
- OpenBSD Project. OpenBSD 6.2 Release Notes [Z]. 2017-10-09；Nagy R. switch the default compiler on amd64 and i386 to clang [EB/OL]. openbsd-cvs, 2017-07-26；Schwarze I. mandoc history [EB/OL]. mandoc.bsd.lv；OpenBSD Project. LibreSSL [EB/OL]. libressl.org, 2014. ［A］
    FreeBSD 社区论文与演讲 [179] David Carlier. LLVM and the state of sanitizers on BSD [C]//AsiaBSDCon 2019. [S.l.]: [s.n.], 2019.〔存疑：原行截断（“[179]，[179] Davi”），按本文件文献段同源条目补全并去编号双写〕
- Linux Kernel Project. COPYING: Linux Kernel Licensing (GPLv2 only)[Z]. kernel.org；Linux Kernel Documentation. Building Linux with Clang/LLVM [EB/OL]. kernel.org/doc；Free Software Foundation. GCC Runtime Library Exception [Z]. gcc.gnu.org.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. 2008-2011 年间系列文章。〔禁引来源·仅作线索·须与一手史料交叉验证·不得直接采信〕［C］
    FreeBSD 社区论文与演讲 [179]，[179] David Carlier. LLVM and the state of sanitizers on BSD [C]//AsiaBSDCon 2019. [S.l.]: [s.n.], 2019. 获取路径：<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>
- Torvalds L. LKML postings on BSD license [Z]. lkml.org, various dates；Williams S. Free as in Freedom: Richard Stallman’s Crusade for Free Software [M]. Sebastopol: O’Reilly, 2002. ISBN: 0-596-00287-4.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 143.7.4 史料辨析

- 要点：中文社区对 BSD 许可证的认知深受 Linux/GPL 话语影响（红旗 Linux、中国开源软件推进联盟等渠道），BSD 家族在中国用户基数较小、声音相对微弱；早期中文启蒙材料（如阮一峰 2008-2011 年博客）对 BSD 许可证的描述带有时代局限，其史实主张须以一手史料独立核验，阮一峰系禁引来源，仅作观点元引用考据。
- Torvalds L. LKML postings on BSD license and GPLv3 [Z]. lkml.org, 1999-2007；Williams S, DiBona C, et al. Open Sources 2.0: The Continuing Evolution [M]. Sebastopol: O'Reilly, 2005. ISBN: 0-596-00802-3.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
    FreeBSD 社区论文与演讲 [179]，[179] David Carlier. LLVM and the state of sanitizers on BSD [C]//AsiaBSDCon 2019. [S.l.]: [s.n.], 2019.
- FreeBSD 9.1/10.0 Release Notes [Z]；Chisnall D. GNU-Free C++11 Stack entry in FreeBSD Quarterly Status Report [R]. 2012 Q1；LLVM Project. libc++ C++ Standard Library [EB/OL]. libcxx.llvm.org.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 143.9.2 lld 链接器替换 GNU ld

- 要点：lld 自 FreeBSD 12.0 起成为 x86/armv7 默认链接器，替换 GNU ld；此后逐架构推进，至 13.0 时期随过时 GNU 工具移除完成主体切换（详见本章要点时间线⑥⑧）。lld 替换消除了 base 中对 GNU binutils 链接器组件的许可依赖，并与 ELF Tool Chain 工具更新同步推进。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP631（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Dr. Brian Robert Callahan 为 QBE 的 ARM64 后端编写窥孔优化，消除冗余寄存器拷贝与可即时数化的算术指令，说明 ARM64 定长指令下只能通过删除指令获利。（BSD Now EP631，[280.3-735.8]，L1）[订正：原 [286.40-737.76]，2026-10-01 SenseAudio 重转核对]

**史料**：

- Dr. Brian Robert Callahan 博客 QBE ARM64 窥孔优化系列。（BSD Now EP631，[280.3-735.8]，L1）[订正：原 [286.40-737.76]，2026-10-01 SenseAudio 重转核对]

**史观**：

- 总纲10 动手者创造历史：Callahan 亲手为 QBE ARM64 后端编写窥孔优化，以逐条删除指令获取性能，属编译器一线动手者的直接经验。（BSD Now EP631，[280.3-735.8]，L1）[订正：原 [286.40-737.76]，2026-10-01 SenseAudio 重转核对]

**辨析**：

- 本块原注入六条要点中五条（失效模式定理、Nvidia/Xorg 驱动、jail 设备名、ZFS 快照、PeerTube 迁移）与本章工具链与架构主题无关，已按核查报告移除，原文见 BSD Now EP631 转写；Callahan 系列优化细节须以其博客原文核验。

**文献**：

- [BSD Now EP631] Pennington J. BSD Now: 631: Endorphin Rush[EB/OL]. (2025-09-25)[2026-08-15]. <https://www.bsdnow.tv/631>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-247 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-247`；w172 YouTube 章节路由采纳）

据〔BSDCan〕讲者口述：Simon Gerrity（转写音作 Simon Garrity）2014 年在 BSDCan 发表议题，2015 年合入主树。（YouTube EP4s1Mfb_w61o，[857.92-867.19]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-246 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-246`；w172 YouTube 章节路由采纳）

据〔BSDCan〕讲者口述：make legacy 构建兼容库，允许项目从 FreeBSD 9.1 版本开始构建。（YouTube EP4s1Mfb_w61o，[416.919-425.51]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-277 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-277`；w172 YouTube 章节路由采纳）

据〔BSDCan 2018〕讲者口述：讲者查到引用显示 FreeBSD 对 Linux 的支持自 1995 年起即已存在。（YouTube EP9N3NrPeCJpk，[156.22-163.05]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-423 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-423`；w172 YouTube 章节路由采纳）

据〔AsiaBSDCon 2009〕讲者口述：讲者指出 FreeBSD/mips 于 2006 年底的进展之后，2007 年已在数种不同的 MIPS 处理器实机上运行。（YouTube EPDF_YqNIiU-o，[784.25-793.32]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-424 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-424`；w172 YouTube 章节路由采纳）

据〔AsiaBSDCon 2009〕讲者口述：RMI 拥有 FreeBSD 6.1 移植版本，正与 FreeBSD 项目组合作以期将其纳入主线。（YouTube EPDF_YqNIiU-o，[1654.44-1663.71]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-660 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-660`；w172 YouTube 章节路由采纳）

据讲者口述：FreeBSD 自带的 netcat 就是 OpenBSD 版 netcat（转写音作 the OpenBSD netcat），讲者据此展示 kTLS（转写音作 lip TLS）相关工具链。（YouTube EPJGgoBQ0hVpw，[357.91-365.86]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-661 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-661`；w172 YouTube 章节路由采纳）

据讲者口述：讲者按时间梳理 FreeBSD 中使用的 OpenSSL 版本谱系——0.9.8 发布于 2005 年，1.0.0 发布于 2010 年，1.0.1 发布于 2012 年（转写音作 0-9 8 / 100 / 101）。（YouTube EPJGgoBQ0hVpw，[1316.289-1324.009]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-939 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-939`；w172 YouTube 章节路由采纳）

据〔会议不详（推测）〕讲者口述：FreeBSD 的 rISC-V 移植（转写音作 risk 5）在 FreeBSD Dev Summit 上有专场演讲，讲者补充其细节。（YouTube EPSR6m5gcayZs，[245.879-253.229]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1025 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1025`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Joerg Sonnenberger 口述：在 FreeBSD 上可用 chroot（转写音作“change hood”）进行批量构建，但也可使用 jail（YouTube EPV_HqMATqtlA，[137.54-141.04]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1071 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1071`；w172 YouTube 章节路由采纳）

据〔FreeBSD Day 2024〕讲者 Ed Maste 口述：BSD 系列会议主要包括 BSDCan、AsiaBSDCon 与 EuroBSDCon。（YouTube EPW-Xqg9e1JmU，[1178.48-1183.35]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-610 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-610`；w172 YouTube 章节路由采纳）

据〔June 2021 FreeBSD Developer Summit〕讲者口述：目标 RISC-V 硬件支持 UEFI 规范，可加载 FreeBSD 引导加载器（YouTube EPiBy_XZPP3v0，[522.719-530.55]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-733 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-733`；w172 YouTube 章节路由采纳）

据〔FreeBSD 非 x86 硬件性能计数器报告（来源不详）〕讲者口述：他将介绍把该机制移植到 MIPS 架构的工作。（YouTube EPlofmFRY-yjs，[59.029-59.039]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-776 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-776`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：约两年前 FreeBSD 尚不真正支持 armv8（转写音作 mv8），这得益于 Andrew Turner 的工作。（YouTube EPn9841gqgGU8，[535.6-546.67]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-920 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-920`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Sean Bruno 口述：QEMU 用户模式在 FreeBSD 上可模拟 mips64、arm v6 与 mips32，而 PowerPC 32、PowerPC 64 与 SPARC 60（转写音，数字按原文照录）仍在开发中。（YouTube EPruNdupZOXks，[1553.15-1565.56]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1186 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1186`；w172 YouTube 章节路由采纳）

据〔FreeBSD Tool Chain 分享〕讲者 Ed Maste 口述：FreeBSD 仍对 tier 2 及更低架构（MIPS、PowerPC、sparc64）使用旧版 GCC 而非 clang。（YouTube EPz04tZ_CDVMA，[580.5-586.99]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1187 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1187`；w172 YouTube 章节路由采纳）

据〔FreeBSD Tool Chain 分享〕讲者 Ed Maste 口述：32 位 arm 与 x86 在工具链分类中较接近 LD 但仍未到位，MIPS 与 PowerPC 差距更大。（YouTube EPz04tZ_CDVMA，[2257.98-2266.52]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1434 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1434`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ELF Nightmares GOTs, PLTs, and Relocations Oh My by John Baldwin〕讲者口述：他在 FreeBSD 和其他 BSD 中所见到的静态链接器，一类是 LLVM 项目里的 LLD，另一类是 GNU binutils 的 BFD 链接器。（YouTube EPTbtCwruycU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1435 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1435`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ELF Nightmares GOTs, PLTs, and Relocations Oh My by John Baldwin〕讲者口述：在 FreeBSD 上，承担 PLT 符号延迟解析的回调函数通常以汇编写成，名为 rtld_bind_start，它最终会调用以 C 编写的 rtld_bind；传入的不透明数据指针指向 ob 表项结构，也就是 FreeBSD 运行时加载器用来描述每个共享库的结构，加载器据此反查出应修补的 GOT 表项。（YouTube EPTbtCwruycU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1436 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1436`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔ELF Nightmares GOTs, PLTs, and Relocations Oh My by John Baldwin〕讲者口述：他认为 MIPS 是一个特立独行的架构，其代价是这些机制上先行者的包袱——MIPS 不用 dynamic ELF relocations 来说明 GOT 该如何修补，而是改用隐含规则（单一 GOT，而非独立的 PLT GOT），因此任何新的计算需求都只能硬编码进这套规则，他说这正是自己不愿把 MIPS 留在树里的原因之一。（YouTube EPTbtCwruycU4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1856 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1856`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Mitchell《FreeBSD on RISC-V》FreeBSD Developer Summit 2024-05 讲者口述：）FreeBSD 在 RISC-V 上已有成熟基本系统，13 与 14 两个主版本发布时 RISC-V 为 tier two，其认为该架构基本系统已属功能完备、不再存在标记为 broken 的重大项。（YouTube EPO7zW7Z9U0ns，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1857 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1857`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Mitchell《FreeBSD on RISC-V》FreeBSD Developer Summit 2024-05 讲者口述：）FreeBSD RISC-V 的 native 打包尚不可行，原因是缺乏足够强的硬件；而按常理 native 构建本是最少出错的打包方式。（YouTube EPO7zW7Z9U0ns，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1858 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1858`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Mitchell《FreeBSD on RISC-V》FreeBSD Developer Summit 2024-05 讲者口述：）由于没有 beefy 硬件，次选方案是用 poudriere 与 QEMU user emulation 交叉编译打包，其指出此前在 ARM 与 MIPS 上曾如此操作。（YouTube EPO7zW7Z9U0ns，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1859 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1859`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Mitchell《FreeBSD on RISC-V》FreeBSD Developer Summit 2024-05 讲者口述：）FreeBSD 对当前 RISC-V 硬件支持滞后，演讲开始列举的 SoC 中约有七至九种尚未支持，且官方仓库已无 RISC-V 包在构建。（YouTube EPO7zW7Z9U0ns，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1873 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1873`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 11 月 FreeBSD 供应商峰会／Warner Losh 报告〕讲者口述：FreeBSD 引导加载器中早已存在 loader.kboot，由 Nathan 在 FreeBSD 运行于 PS3 的时代为 PS3 序列写下一个驱动。（YouTube EP-4Ec2WUhK48，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1874 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1874`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 11 月 FreeBSD 供应商峰会／Warner Losh 报告〕讲者口述：改造后的 loader.kboot 目前可在 arm 64 上工作，该公司产品已在其实验室环境中用它引导以服务客户；AMD64 约完成八成，因其由 x86 演化而来、是 FreeBSD 最古老的引导内核路径，需更多调校才能把引导环境调成内核期望的状态。（YouTube EP-4Ec2WUhK48，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1875 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1875`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 11 月 FreeBSD 供应商峰会／Warner Losh 报告〕讲者口述：他在 FreeBSD 引导加载器中另写了一个 hostfs，形式上略仿 u-boot 的 hostfs，但为 Linux 环境专门裁剪，可读取宿主上的文件。（YouTube EP-4Ec2WUhK48，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1876 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1876`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔2022 年 11 月 FreeBSD 供应商峰会／Warner Losh 报告〕讲者口述：Linux 启动时内核即全部，而 FreeBSD 须经引导加载器接口向内核传入所有可加载模块、tunables 与各类内存位置表、DTB blob，全部配置妥当后才能在调用内核入口点之前完成，这也是把内核装进 Linux 环境时的主要难点。（YouTube EP-4Ec2WUhK48，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1881 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1881`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Baptiste Daroussin，BSDCan 2018〕讲者口述：认为 FreeBSD 的新包管理器虽不完美，但至少让维护者能简便地建立与维护自有仓库，并转述使用者反馈称它好用、命令行简单；对照旧制，他认为把二进制包搬到另一台机器复现同一套环境几乎不可能、自动化接近不可能、逐台重打包极不方便，且当时对服务器上既有程序（如 Apache、PHP）的升级没有任何机制。（YouTube EPIJeOfcXVauM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1882 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1882`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Baptiste Daroussin，BSDCan 2018〕讲者口述：把 FreeBSD 基本系统几乎为全部工具、乃至驱动程序都附带内容充实的手册页，列为企业用户会感到意外的正面之处；相对地，他在 Linux 侧遇到的是常无手册页、或有则信息很少而须转到 info 页或 --help 的情况。（YouTube EPIJeOfcXVauM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1883 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1883`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Baptiste Daroussin，BSDCan 2018〕讲者口述：称 FreeBSD 系统内自带的 GDB 过于陈旧，企业用户会不解为何系统里放着如此老的调试器，他只能建议对方改用 ports 中的新版 GDB 并以特定名称调用；另述其认为 FreeBSD 能同机共存三四套工具链并各自完成构建，亦为企业用户的正面惊喜。（YouTube EPIJeOfcXVauM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1884 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1884`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Baptiste Daroussin，BSDCan 2018〕讲者口述：称 FreeBSD 在生产环境中最多的抱怨来自默认 shell；他观察到来自 Sun 与 AIX 者多半并不真会正确使用 csh；其立场是应保留 tcsh，但同时引入一个更接近 Bourne 兼容的交互 shell（其点名 mksh 与 oksh 两个选项）以便取悦使用者。（YouTube EPIJeOfcXVauM，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2115 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2115`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03B FreeBSD on IBM PowerNV，Wojciech Macek〕讲者口述：PowerPC 64 的 TOC（table of contents，目录表）有硬性限制：不能超过 64 千字节，且必须落在同一个内存段内；FreeBSD 在 PowerNV 上的内核约 20 至 30 兆字节，因而最终拥有成千上万张 TOC 表。（YouTube EPWJMj3Ktwmig，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2116 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2116`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03B FreeBSD on IBM PowerNV，Wojciech Macek〕讲者口述：内核调度切换例程偶发恐慌的根因是 TOC 表错用——scheduler switch 与 cpu_switch 多年共用同一张 TOC 表，故障虽在却不可见；加入 PowerNV 支持后二进制变大、两函数距离过远，链接器改用两张 TOC 表，潜伏缺陷方才暴露。（YouTube EPWJMj3Ktwmig，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2117 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2117`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03B FreeBSD on IBM PowerNV，Wojciech Macek〕讲者口述：PCIe 跑通后，系统中仅有一个网卡驱动能工作，其余驱动多数无法 attach、完全不工作甚至引发系统恐慌；原因是驱动用位域抽象寄存器，这类写法不具可移植性，切换到大端后一切错乱。（YouTube EPWJMj3Ktwmig，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2118 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2118`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03B FreeBSD on IBM PowerNV，Wojciech Macek〕讲者口述：FreeBSD 在 Power8 上比 Linux 慢 8 倍的根因是空闲线程未发出让出（yield／spin）语义，被 SMT 调度器当作极为重要的任务而均分资源。（YouTube EPWJMj3Ktwmig，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2133 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2133`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔R. Jaworowski 报告 FreeBSD on hi-perf. multi-core embedded PPC〕讲者口述：移植并非从零开始：树中已有单核 e500 CPU 的基础支持，那是讲者参与过、真正从零写起的项目；因此启动双核工作时已有一份坚实的可续做代码基础。（YouTube EPLpR1BgXeKwQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2134 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2134`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔R. Jaworowski 报告 FreeBSD on hi-perf. multi-core embedded PPC〕讲者口述：该项目约一年前启动，启动时所用的 FreeBSD 版本转录为“eight grand”（具体版本号转写未明确）；团队有意不使自己的工作与基线偏离过多。（YouTube EPLpR1BgXeKwQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2135 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2135`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔R. Jaworowski 报告 FreeBSD on hi-perf. multi-core embedded PPC〕讲者口述：本项目的主要目标是双核运行，即让 FreeBSD 在 PowerPC 上支持 SMP；讲者称当时尚无任何 FreeBSD 运行在 SMP 机器上。（YouTube EPLpR1BgXeKwQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2136 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2136`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔R. Jaworowski 报告 FreeBSD on hi-perf. multi-core embedded PPC〕讲者口述：重写 pmap 模块的主要挑战在于处理并发的 TLB miss：此时存在真正并行且异步运行的处理器，其 MMU 需被通知，并以软件页表加以记录。（YouTube EPLpR1BgXeKwQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2207 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2207`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Rafał Jaworowski“Embedded FreeBSD”演讲〕讲者口述：他们为嵌入式平台做的是整机移植：先把 system/world 运行环境完整建好让它能工作，再为一组组硬件模块从零开始写驱动，而不是改动既有驱动。（YouTube EP2HcIJvJX4y8，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2208 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2208`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Rafał Jaworowski“Embedded FreeBSD”演讲〕讲者口述：该嵌入式处理器的 MMU 模型与传统 PowerPC 完全不同，没有“shadows／段（segments）”等旧概念，因此传统 PPC 上定义的 pmap 层对它毫无用处，他为这次移植把 pmap 从零重写。（YouTube EP2HcIJvJX4y8，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2209 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2209`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Rafał Jaworowski“Embedded FreeBSD”演讲〕讲者口述：这个移植当时仍在进行中但已相当深入，代码放在 FreeBSD 开发者库里他自己维护的 Perforce 分支上，基准约为 FreeBSD 8.0，功能上已是可用移植，只需再做一些形式化改动；他说整合完 8 之后还可能同步整合到 FreeBSD 7。（YouTube EP2HcIJvJX4y8，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2210 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2210`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Rafał Jaworowski“Embedded FreeBSD”演讲〕讲者口述：PlayStation 3 这个平台对第三方软件与别的操作系统非常开放，从设计之初就打算让别的系统也能跑在它上面；不过他同时说，把系统真正跑上 PS3 是“相当大的挑战”，不可能一步完成——该机型缺少 SMP（双核），且无法直接跳到 64 位，必须先做大量底层内核层适配。（YouTube EP2HcIJvJX4y8，dual）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2269 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2269`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sean Chittenden 谈 FreeBSD 现代开发工具〕讲者口述：ports 里随共享库更新编译出的 sudo 链接 lib pam.so.6，而讲者下载的 11 current 虚拟机镜像只带 lib pam.so.5，导致引导时 sudo 无法执行，他最终改用符号链接绕过。（YouTube EPweUYEX9WRS4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2270 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2270`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sean Chittenden 谈 FreeBSD 现代开发工具〕讲者口述：他用 ZFS 根制作 FreeBSD 虚拟机镜像，并称 FreeBSD 安装程序的设计使 UFS 镜像与 ZFS 镜像在安装过程中某一步须按 "left" 而非 "Enter"，因此难以脚本化。（YouTube EPweUYEX9WRS4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2271 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2271`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sean Chittenden 谈 FreeBSD 现代开发工具〕讲者口述：有一位 GSoC 学生正在为 Vagrant 编写 bhyve provider，他对此持乐观态度，期待 FreeBSD 能以同一套工具在自有环境中原生运行。（YouTube EPweUYEX9WRS4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2272 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2272`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Sean Chittenden 谈 FreeBSD 现代开发工具〕讲者口述：自己至今仍阅读 SVN digests 来跟上 FreeBSD 社区的演进、理解提交动机，称那里的提交信息很好。（YouTube EPweUYEX9WRS4，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2369 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2369`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon2023 Toshaan Bharvani〕讲者口述：FreeBSD 对 OpenPOWER 的支持自其口述中的 free bsd2 起即已存在，平台形态为小端 64 位 POWER；该端口当时在FreeBSD 的架构分级里仍属 tier two，讲者称团队正争取把它推到 tier one，尚有若干缺陷待修。（YouTube EPTj4Q-m_WEh0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2370 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2370`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon2023 Toshaan Bharvani〕讲者口述：POWER 指令集分大端与小端两类子集，讲者称 FreeBSD 今天支持的是 powerpc64（大端）与 powerpc64le（小端）；对更小的 PC64-SFFS 子集目前只在 Linux 上做试验，待资源充裕才考虑扩展到 BSD。（YouTube EPTj4Q-m_WEh0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2371 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2371`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon2023 Toshaan Bharvani〕讲者口述：POWER9 内的 NX 协处理器（压缩引擎）当时尚未被 FreeBSD 利用，讲者称这一压缩卸载缺位使 FreeBSD 在 POWER 上的gzip／lzma／bzip2 一类压缩得不到硬件加速，仍属待做的工作。（YouTube EPTj4Q-m_WEh0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2372 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2372`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔EuroBSDcon2023 Toshaan Bharvani〕讲者口述：讲者自认在 FreeBSD/POWER 工作中只是倡导者，并称该项目的两名主力开发者是 Alfredo 与 Leandro，早期大部分移植工作由这二人完成。（YouTube EPTj4Q-m_WEh0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2448 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2448`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Fridays《Introduction to RISC-V on FreeBSD》Mitchell Horn 讲〕讲者口述：FreeBSD 的 RISC-V 移植大约始于 2015 年，由 Ruslan Bukin 起手；按其转述，Bukin 花了约六个月全职工作，才把引导到多用户所需的一切移植过来，其中最大的一块是内核里的 PMAP 模块，负责构建与管理硬件页表。（YouTube EPQGW3l_Bz04I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2449 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2449`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Fridays《Introduction to RISC-V on FreeBSD》Mitchell Horn 讲〕讲者口述：FreeBSD 历史上以 GCC 为基础编译器，GCC 更换许可证后与 FreeBSD 自身的许可证不再兼容，因此“摆脱 GCC、转向 LLVM”成为持续多年的项目。（YouTube EPQGW3l_Bz04I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2450 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2450`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Fridays《Introduction to RISC-V on FreeBSD》Mitchell Horn 讲〕讲者口述：2019 年 FreeBSD 的 RISC-V 支持由外部 GCC 工具链切换到 FreeBSD 基本系统自带的 Clang/LLVM；LLVM 的 RISC-V 后端工作约从 2017 年起展开。（YouTube EPQGW3l_Bz04I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2451 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2451`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD Fridays《Introduction to RISC-V on FreeBSD》Mitchell Horn 讲〕讲者口述：为 RISC-V 实现 FreeBSD 引导加载器时，最终选择把它构建为 EFI payload，使任何支持 UEFI 规范的 RISC-V 固件都能引导，这与 ARM、ARM64、AMD64 上的做法相同。（YouTube EPQGW3l_Bz04I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2548 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2548`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Luba Tang AsiaBSDCon 2014 演讲〕讲者口述：讲者给出开发新链接器的三个理由，其一是 BSD（转写音严重失真），并称链接器是 BSD C 工具链的“最后边疆”（转写音作 the final frontier of the BD C2 TR）。（YouTube EPfWgbBUPMsVw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2549 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2549`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Luba Tang AsiaBSDCon 2014 演讲〕讲者口述：讲者介绍现存最流行链接器（转写音作 G）为 GPL 许可，支持几乎所有主流设备与 a.out（转写音作 b a. out）、ELF 等格式，但代码量极大，约 50 万行。（YouTube EPfWgbBUPMsVw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2550 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2550`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Luba Tang AsiaBSDCon 2014 演讲〕讲者口述：讲者称其自称曾任架构师的链接器（转写音作 En Linker）采用 BSD 许可，理由是它必须运行在所有安卓设备上，Google 必须以 BSD 许可发布它。（YouTube EPfWgbBUPMsVw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2551 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2551`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Luba Tang AsiaBSDCon 2014 演讲〕讲者口述：Bold（转写音作 both，名称据视频标题）与转写音作 and slinker 的链接器不同，从零写起、不缠绕（twist）于 L VN，这可让 Fedora 或 BSD 社区等更容易把 Bold 移植到各自环境；但讲者又称其架构与后者非常相似并遵循相同编码风格。（YouTube EPfWgbBUPMsVw，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2556 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2556`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔《P09C: GENERIC ARM Creating a single kernel configuration for FreeBSD/armv6》演讲〕讲者口述：他在剑桥大学做兼职研究助理，在 Watson（转写音作 what Watson）手下参与 CHERI 项目（转写音作 cherry project），并称自己使用 FreeBSD（转写音作 finger stick）已有六年半（他说今年将满七年）。（YouTube EP6y1miJLbzGc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2557 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2557`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔《P09C: GENERIC ARM Creating a single kernel configuration for FreeBSD/armv6》演讲〕讲者口述：此前 FreeBSD 对每个受支持的 CPU 各带一份专属内核配置（转写音作 secret internal conflict），维护时 make universe 要把全部内核配置与模块（转写音作 criminal context）逐一构建、耗时很长，因此他希望减少需构建的内核数量，让人们真正用上 GENERIC 内核。（YouTube EP6y1miJLbzGc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2558 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2558`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔《P09C: GENERIC ARM Creating a single kernel configuration for FreeBSD/armv6》演讲〕讲者口述：对“内核被硬编码到某个物理地址、而两块板子可能没有任何共享物理加载地址”的难题，他给出的办法是在早期启动代码中设法探测内核实际加载的物理地址，再围绕该地址搭建页表并直接跳转，其余流程即可照常工作。（YouTube EP6y1miJLbzGc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2559 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2559`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔《P09C: GENERIC ARM Creating a single kernel configuration for FreeBSD/armv6》演讲〕讲者口述：他回顾 FreeBSD 对 ARMv6 的介入“很晚”，并称 ARMv7 支持始于 2011 年。（YouTube EP6y1miJLbzGc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2593 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2593`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2017 的 Work in Progress 闪电演讲环节〕讲者口述：就新链接器（转写音作 LD／health）在各架构上的进展，三六（i386）与 mips 还需要更多工作、但也已接近可用；RISC-V（转写作 risk five）当时尚无任何实现，sparc64 则完全没有支持。（YouTube EPOHApWQg7O4s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2594 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2594`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2017 的 Work in Progress 闪电演讲环节〕讲者口述：讲者报告的新特性之一是（转写作 Professor Park support）让块数据在内存缓存中保持压缩，从而在同样内存里装下更多数据；视负载不同可获二、三乃至四比一的压缩比，对数据库尤其有利，差别很大。（YouTube EPOHApWQg7O4s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2595 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2595`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2017 的 Work in Progress 闪电演讲环节〕讲者（自述名 Michael Dexter）口述：他去年宣布的以 UEFI 启动 guest（转写音作 visual booting）的支持已经入树，随后还有一些小特性；Google Summer of Code 带来了托管虚拟机的 vagrant（转写音作 vagrants）相关工作，核心开发者则忙于（音作）Madison beehive。（YouTube EPOHApWQg7O4s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2596 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2596`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2017 的 Work in Progress 闪电演讲环节〕讲者口述：几年前 NetBSD（转写音作 net BSU／net whiskey）的邮件列表上有人提议把旧的 spell 工具从 NetBSD 中移除，理由是它效果不佳、缺点很多、几乎没人用；讲者因此动手重写该工具。（YouTube EPOHApWQg7O4s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
