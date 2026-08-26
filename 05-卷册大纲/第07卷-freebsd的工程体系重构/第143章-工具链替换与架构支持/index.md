---
chapter: 第 143 章
id: CH143
volume: 07
---

# 第143章 工具链替换与架构支持

## 要点

- i386 和 amd64（x86）是 Clang/LLVM 最早支持且最成熟的架构，也是 FreeBSD 首批完成 Clang 迁移的架构。Roman Divacky 于 2009 年 2 月宣布 Clang 可编译可启动的 i386/amd64 内核；FreeBSD 9.0（2012）中 i386/amd64 world 和 GENERIC 内核已可完整使用 Clang 构建；2012 年 11 月 Brooks Davis 在 -CURRENT 中切换 Clang 为 x86 默认编译器；FreeBSD 10.0（2014.1.20）正式在 RELEASE 版本中将 Clang 设为 i386/amd64 默认且不再默认安装 GCC。x86 架构的 Clang 支持成熟得益于 Apple 的长期投入——macOS/iOS 均运行在 x86（及后续 Apple Silicon）上，Clang x86 后端是优化最好、测试最充分的后端之一。
- arm64（AArch64）架构在 FreeBSD 中的支持是 Clang/LLVM 迁移的重要副产品——GCC 4.2.1 完全不支持 AArch64（ARM 64 位架构在 2011 年才发布，远晚于 GCC 4.2.1 的 2007 年），因此没有 Clang 就不可能有 FreeBSD/arm64。Andrew Turner（andrew@）是 FreeBSD/arm64 移植的主要开发者，在 FreeBSD Foundation 和商业赞助商支持下完成了 arm64 支持。FreeBSD 11.0（2016.10.10）首次将 arm64 作为支持架构发布（但非 Tier 1）；FreeBSD 13.0（2021.4.13）正式将 arm64/AArch64 提升为 Tier 1 架构，与 amd64 并列获得发布镜像、二进制包、安全更新的全面支持。Clang/LLVM 对 AArch64 的原生支持（AArch64 后端由 ARM 公司和 Apple 工程师联合开发，质量极高）使 FreeBSD/arm64 从一开始就有高质量编译器支持——这与 mips/powerpc/sparc64 等旧架构在 Clang 迁移中挣扎形成鲜明对比。arm64 升为 Tier 1 标志着 FreeBSD 正式进入 64 位 ARM 服务器、云原生和嵌入式市场。
- powerpc、mips、sparc64 等旧架构的 Clang 支持远落后于 x86 和 arm64，是 GCC 4.2.1 在 FreeBSD base 中保留多年的主要原因。powerpc（32 位和 64 位 powerpc64）的 Clang 支持在 FreeBSD 11/12 时期逐步完善，但在某些 powerpc 变体上仍有问题；mips 架构因 MIPS 公司转向 RISC-V 和 MIPS 设计本身的复杂性（多种 ABI、尾码、原子操作模型），Clang 支持长期不完善；sparc64（Sun/Oracle SPARC 64 位）的 Clang 支持进展最慢，且 SPARC 硬件市场在 Oracle 收购 Sun 后急剧萎缩。这些架构的支持路径分三种：①Clang 支持逐步完善后切换（如 powerpc64 在较晚版本完成）；② 架构本身因市场萎缩而被降级或废弃（sparc64 在 FreeBSD 13 降级为 Tier 2，mips 在 FreeBSD 13 后也逐步降级）；③ 社区通过外部 GCC 工具链（ports/devel/gcc 或外部 binutils）继续支持非 Tier 1 架构。RISC-V 作为新架构从一开始就依赖 Clang/LLVM 支持（GCC 4.2.1 不可能支持 RISC-V），FreeBSD/riscv 从开发初期即使用 Clang。各架构 Clang 支持与迁移状态汇总见下表。
- 非 x86 架构的 Clang 支持进度是 GCC 从 FreeBSD base 完全移除的主要阻塞因素。迁移的关键时间节点如下：①2009.2——i386/amd64 内核可启动（Divacky）；②2012.1——FreeBSD 9.0 发布，Clang 导入 base 但 GCC 默认；③2012.11——x86 -CURRENT 默认 Clang；④2014.1——FreeBSD 10.0 发布，i386/amd64 默认 Clang，GCC 仍为其他架构保留；⑤2016.10——FreeBSD 11.0 发布，arm64 首次作为支持架构；⑥2018.12——FreeBSD 12.0 发布，lld 为 x86/armv7 默认 linker，gdb 移至 libexec，LLVM 6.0.1，ELF Tool Chain r3614；⑦2018——Warner Losh 宣布 GCC 4.2.1 退休（所有受支持架构已使用 Clang 或外部工具链）；⑧2021.4——FreeBSD 13.0 发布，arm64 升为 Tier 1，LLVM Clang 11，移除过时 GNU 工具（含 GCC 和 grep）；⑨2024.7——FreeBSD 16-CURRENT 移除 dialog（最后一个 GPL 组件）。
- OpenBSD 在 FreeBSD 之后也进行了 Clang 迁移，但时间更晚、策略更分阶段。OpenBSD 长期使用 GCC 3.x（GPLv2 版本）作为默认编译器以回避 GPLv3 问题；当 GCC 3.x 过老无法支持新硬件和 C++ 标准时，OpenBSD 开始评估 Clang。OpenBSD 的 Clang 迁移分架构逐批完成：amd64/i386 于 2017 年 7 月 26 日（OpenBSD 6.2 开发周期）切换默认编译器（Robert Nagy 提交）；armv7 于 2018 年 1 月 19 日切换（Mark Kettenis（马克·凯特尼斯） 提交）；octeon（Cavium OCTEON MIPS64）于 2019 年 7 月切换；powerpc 于 2020 年 4 月切换；loongson（MIPS64 Loongson）于 2020 年 12 月切换。OpenBSD 的许可证纯洁化更广泛：mandoc（Ingo Schwarze（英戈·施瓦茨） 开发，OpenBSD 项目）替代 groff、LibreSSL（2014 年 Heartbleed 后 Theo de Raadt（西奥·德·若特） 领导 fork）替代 OpenSSL，但需注意 LibreSSL 仅在 OpenBSD base 中为默认，FreeBSD base 仍使用 OpenSSL。

## 史观

- 总纲第 17 条——软件工程：架构支持优先级与商业生态直接相关——x86 作为服务器/桌面主流架构获得最优先支持，而这与 Apple 自身产品需求高度重合，FreeBSD 搭了 Apple 投入的便车。
  - 辨析：“Clang 可编译内核” 和 “Clang 可编译所有内核模块” 是两个不同里程碑——2009 年是 GENERIC 内核可启动，但部分第三方模块和非标准配置仍需修复。
  - 文
- 总纲第 25 条——终结与延续：GCC 4.2.1 从 base 移除的标志不是 “所有架构都用 Clang”，而是 “所有 Tier 1 架构都用 Clang，Tier 2/Tier 3 架构可依赖 ports GCC”。这标志着 FreeBSD 工具链策略从 “base 支持所有架构” 转向 “base 保证 Tier 1 质量，其他架构由 ports/社区支持” 的分层模式。
- 辨析：架构
- 总纲第 6 条——技术路线分化：OpenBSD 比 FreeBSD 晚约三年半切换 amd64/i386 默认 Clang（FreeBSD 2014.1 vs OpenBSD 2017.7），这反映了两个项目不同的工程优先级——FreeBSD 因 C++11 支持需求和 Apple 投入更迫切需要迁移，OpenBSD 因长期停留在 GCC 3（GPLv2）而推迟了切换压力。
  - 辨析：原文件误
- 总纲第 6 条——技术路线分化：Linux 无需迁移 Clang 的法律基础是 Torvalds 在 2006-2007 年拒绝将 Linux 内核升级到 GPLv3——GCC 4.3+ 的 GPLv3 许可证适用于编译器本身，但编译输出（内核）的许可证由内核作者决定而非编译器许可证决定（FSF 明确确认），因此 GCC GPLv3 对 Linux 内核不构成许可证危机。这一法律解释的差异是 Li
- 总纲第 11 条——国家政策：中文开源社区的许可证认知受 Linux 在中国的普及路径深刻影响——Linux 作为最早进入中国的开源操作系统之一，其 GPL 话语通过红旗 Linux、中国开源软件推进联盟等渠道成为默认认知框架，BSD 家族（FreeBSD/OpenBSD/NetBSD）在中国用户基数较小，声音相对微弱。
  - 辨析：阮一峰 2008-2011 年博客文章将 BSD 许可证描述为

## 辨析

- “Clang 可编译内核” 和 “Clang 可编译所有内核模块” 是两个不同里程碑——2009 年是 GENERIC 内核可启动，但部分第三方模块和非标准配置仍需修复。
  - 文献：Divacky R. 2009 kernel announcement [EB/OL]；Davis B. 2012 default announcement [EB/OL]；FreeBSD 9.0/10.0 Rel
- 架构的 Tier 级别是动态调整的——sparc64 从 FreeBSD 13 起不再是 Tier 1，mips 支持也大幅缩水，但这不完全归因于 Clang 迁移；SPARC 和 MIPS 硬件市场在 2010 年代的整体衰退（Oracle 终止 SPARC 服务器开发、MIPS 公司转向 RISC-V）是更深层原因。
- 文献：FreeBSD Project. Supported Archit
- 原文件误称 “OpenBSD 5.5 默认 Clang” 或 “2014 年”——经 OpenBSD CVS commit log 交叉验证，amd64/i386 实际切换时间为 2017 年 7 月 26 日（commit 时间戳精确到日），5.5 是 2014 年 5 月发布，此错误已修正。Theo de Raadt 在许可证问题上的立场比 FreeBSD 更为激进（他对 GPL 和 NDA
- “GCC GPL 传染编译产物” 是常见误解——FSF 明确表示 GCC 的 GPL 许可证不适用于 GCC 编译输出的程序（只要不是基于 GCC 运行时库的 GPL 代码片段衍生），GCC Runtime Library Exception 进一步明确了这一点。因此 Linux 使用 GCC 4.3+（GPLv3）不涉及许可证问题，但 FreeBSD base 系统中包含 GCC 二进制和库文件
- 阮一峰 2008-2011 年博客文章将 BSD 许可证描述为“更宽松但允许闭源”〔阮一峰为禁引来源，本辨析仅作其观点元引用考据，其全部史实主张须独立核验〕是其时代局限性产物——当时 Clang 尚未成为 FreeBSD 默认（2014.1.20 才默认化），LLVM/Clang 技术成熟度也远不及 2020 年代；阮一峰博客作为中文世界早期开源启蒙材料有其历史贡献，但其对 BSD 许可证的批评基

## 文献

- Divacky R. 2009 kernel announcement [EB/OL]；Davis B. 2012 default announcement [EB/OL]；FreeBSD 9.0/10.0 Release Notes [Z].[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
    FreeBSD 社区论文与演讲 [258]，[258] Ryan Stone. Oblivious Sandboxing with Capsicum and EBPF [C]//BS
- FreeBSD Project. Supported Architectures [EB/OL]. freebsd.org/platforms/；FreeBSD 12.0/13.0 Release Notes [Z]；Losh W. GCC 4.2.1 retirement email [EB/OL]. freebsd-arch, 2018. ［A］

## 142.10.4 架构支持对迁移时间线的效应

- 要点：非 x86 架构的 Clang 支持进度是 GCC 从 FreeBSD base 完全移除的主要阻塞因素。迁移的关键时间节点如下：①2009.2——i386/amd64 内核可启动
- OpenBSD Project. OpenBSD 6.2 Release Notes [Z]. 2017-10-09；Nagy R. switch the default compiler on amd64 and i386 to clang [EB/OL]. openbsd-cvs, 2017-07-26；Schwarze I. mandoc history [EB/OL]. mandoc.bsd.lv；OpenBSD Project. LibreSSL [EB/OL]. libressl.org, 2014. ［A］
    FreeBSD 社区论文与演讲 [179]，[179] Davi
- Linux Kernel Project. COPYING: Linux Kernel Licensing (GPLv2 only)[Z]. kernel.org；Linux Kernel Documentation. Building Linux with Clang/LLVM [EB/OL]. kernel.org/doc；Free Software Foundation. GCC Runtime Library Exception [Z]. gcc.gnu.org.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史
- 中文技术博客。开源许可证的比较 [EB/OL]. 2008-2011 年间系列文章。〔禁引来源·仅作线索·须与一手史料交叉验证·不得直接采信〕［C］
    FreeBSD 社区论文与演讲 [179]，[179] David Carlier. LLVM and the state of sanitizers on BSD [C]//AsiaBSDCon 2019. [S.l.]: [s.n.], 2019. 获取路径：<<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_b>
- Torvalds L. LKML postings on BSD license [Z]. lkml.org, various dates；Williams S. Free as in Freedom: Richard Stallman's Crusade for Free Software [M]. Sebastopol: O'Reilly, 2002. ISBN: 0-596-00287-4.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 142.7.4 史料辨析

- Torvalds L. LKML postings on BSD license and GPLv3 [Z]. lkml.org, 1999-2007；Williams S, DiBona C, et al. Open Sources 2.0: The Continuing Evolution [M]. Sebastopol: O'Reilly, 2005. ISBN: 0-596-00802-3.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
    FreeBSD 社区论文
- FreeBSD 9.1/10.0 Release Notes [Z]；Chisnall D. GNU-Free C++11 Stack entry in FreeBSD Quarterly Status Report [R]. 2012 Q1；LLVM Project. libc++ C++ Standard Library [EB/OL]. libcxx.llvm.org.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 142.9.2 lld 链接器替换 GNU ld

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
