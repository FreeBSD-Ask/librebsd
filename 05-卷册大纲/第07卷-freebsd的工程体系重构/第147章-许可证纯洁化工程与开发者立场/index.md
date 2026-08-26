---
chapter: 第 147 章
id: CH147
volume: 07
---

# 第147章 许可证纯洁化工程与开发者立场

## 要点

- Clang/LLVM 迁移仅是 FreeBSD 许可证纯洁化工程（License Purification）中最大的单一项目，整个替换工程历时十余年（约 2007-2024），覆盖基础系统中几乎所有 GNU 工具：① 编译器：GCC→Clang/LLVM（2009-2014 完成 i386/amd64）；②C++ 标准库：libstdc++→libc+++libcxxrt（David Chisnall（戴维·奇斯纳尔） 主导，9.1 可选，10.0 默认）；③ 链接器：GNU **ld(1)** → **lld(1)**（FreeBSD 12 成为 amd64/i386/armv7 bootstrap linker，后续版本全架构默认）；④ 调试器：GDB→LLDB（FreeBSD 12 将旧 **gdb(1)** 移至 `/usr/libexec/gdb` 仅供 **crashinfo(8)** 使用，交互式调试推荐 **lldb(1)** 或 ports/devel/gdb）；⑤ 二进制工具：GNU binutils（**ar(1)**/**as(1)**/**ld(1)**/**objdump(1)**/**ranlib(1)**/**nm(1)**/**readelf(1)**/**size(1)**/**strings(1)**/**strip(1)**）→ELF Tool Chain 项目（BSD 许可的 **ar(1)**/**ranlib(1)**/**readelf(1)**/**objdump(1)**/**nm(1)**/**size(1)**/**strings(1)**/**strip(1)**）+ LLVM 工具链；⑥ 构建工具：GNU make→bmake（从 NetBSD 移植，10.0 默认替换 **make(1)**）；⑦ 文本处理：GNU sort→BSD sort（2012 Q1 status report 报告 BSD-licensed sort 开发中，后导入 base）、GNU grep→BSD grep（约 FreeBSD 12/13 完成替换）、GNU diff→BSD diff、GNU patch→BSD patch（r246074 2013.1.29 导入，r253689 成为默认）；⑧ 手册页排版：**groff(1)**（GPL）→ **mandoc(1)**（mdocml）——由 OpenBSD Ingo Schwarze（英戈·施瓦茨） 开发的 BSD 许可手册页编译器；⑨DNS 服务器：BIND→Unbound（10.0 移除 BIND，导入 Unbound 作为本地缓存 DNS 解析器）；⑩ 软件包管理：pkg_install（BSD 许可但架构过时）→ **pkg(7)**（10.0 默认切换，非许可证驱动但同期完成）；⑪ 其他：GNU rcs 移除、GNU texinfo 替换、GNU dialog→BSD dialog（2024 年 FreeBSD 16-CURRENT 完成替换，最后一个 GPL 组件移除）。GPL 软件替换工程组件汇总见下表。
- 许可证纯洁化工程对 FreeBSD 生态产生了双重影响。正面影响：①base 系统彻底摆脱 GPL 许可证不确定性，商业用户可无顾虑地基于 FreeBSD 构建产品；② 工具链现代化（Clang 错误诊断、lld 高速链接、libc++ 完整 C++ 标准支持）显著改善开发体验；③ 部分 GNU 工具替换后性能提升（bmake 并行构建、lld 链接速度数倍于 GNU ld）；④ 推动了 ELF Tool Chain、mandoc 等 BSD 许可基础设施项目的发展；⑤ 为 arm64/AArch64 等新架构支持扫清编译器障碍（Clang 原生支持 AArch64，GCC 4.2.1 完全不支持）。负面影响：① 部分专业用户和 ports 软件仍需 GCC（通过 ports/devel/gcc 安装现代版本 GCC），导致系统存在双编译器现实；②GNU 工具替换初期存在功能缺失和兼容性问题（如 BSD sort/grep/diff 早期版本缺少部分 GNU 扩展）；③ 替换工程消耗了本可用于新功能开发的大量开发者资源；④ 部分架构（sparc64）因 Clang 支持不完善且 GCC 被移除而最终被废弃（sparc64 在 FreeBSD 13 降级为 Tier 2，14 后基本停止支持）；⑤GDB→LLDB 过渡中调试体验落差（LLDB 对 C++ 模板和多线程调试的支持初期不如 GDB）。
- FreeBSD 许可证纯洁化运动自启动以来即面临“意识形态驱动而非工程需要”的批评。批评者（主要来自 GPL/Linux 阵营）认为：①GPLv3 的实际法律风险被夸大，FSF 明确表示 GPLv3§11 不会对非 GPL 代码产生“传染性”影响；② 为许可证纯洁性牺牲功能兼容性和用户便利性是教条主义；③ 十余年工具替换消耗巨大资源但并未带来相应技术收益；④Jordan Hubbard 等早期核心成员对 GPL 的批评带有强烈个人立场而非客观工程评估。FreeBSD 社区的回应包括：①GCC 4.2.1 无法编译 C++11 代码，继续冻结意味着 C++ 生态永久停留在 2003 标准，迁移在工程上是必要的；②Clang 在编译速度、错误诊断、静态分析、IDE 集成、模块化等方面确实技术上优于旧 GCC；③Apple、Google、Microsoft、Sony 等大公司对 LLVM 的持续投入保证了项目的长期生命力；④base 系统许可证纯洁化降低了商业用户的法律风险，扩大了 FreeBSD 的企业采用。
- 许可证纯洁化工程的史料主要散落在各版本 Release Notes、Quarterly Status Reports、svn commit log 和邮件列表中，缺乏单一的官方文档完整叙述整个工程。这导致外部叙述常将整个工程简化为"GCC→Clang"单一事件，忽略了 bmake、mandoc、ELF Tool Chain、BSD sort/grep/patch、lld、lldb、libc++、Unbound、dialog 替换等十余个平行项目。部分工具替换的时间线和具体贡献者记录不完整，需通过 svn commit 历史逐步追溯。
- FreeBSD 许可证纯洁化工程自启动即在 GPL/Linux 阵营引发批评，批评可归纳为四层。第一层为“误解兼容性”批评：FSF 官方许可证列表明确将修改版 BSD（3-clause）与 FreeBSD（2-clause）许可证列为“兼容 GNU GPL 的自由软件许可证”，FSF 据此认为 FreeBSD 以“GPLv3 不兼容”为由驱逐 GPL 代码是对许可证兼容性法律概念的根本误读——BSDL 代码可自由流入 GPL 项目，二者在 FSF 的法律框架内并非对立关系。第二层为“意识形态驱动”批评：批评者认为纯洁化工程并非工程必需而是教条主义，十余年工具替换消耗本可用于新功能开发的开发者资源，且 Jordan Hubbard 等早期核心成员对 GPL 的“病毒式许可证”定性带有强烈个人立场而非客观工程评估。第三层为“割裂生态”批评：将 GPL 工具逐出 base 系统人为割裂了 BSD 与 GNU 长期共存的工具链生态，导致部分 GNU 工具的 BSD 替代品初期存在功能缺失（如 BSD grep/sort 早期缺少 GNU 扩展，LLDB 对 C++ 模板与多线程调试的初期支持不及 GDB）。第四层为“自由定义之争”批评：FSF 的哲学立场是宽容许可证允许专有锁定，是“较弱的自由保护”，纯洁化工程以“许可证纯洁”为名实则削弱了对用户免于被锁定自由的保护。需注意：FSF 并未发布单一官方文件专门点名批评 FreeBSD 纯洁化工程，上述批评系从 FSF 许可证列表官方立场、Stallman 自由软件哲学文集与 GPL/Linux 社区评论综合重构，属考据重构而非直接引用单一文献。

## 史观

- 总纲第 24 条——许可证：FreeBSD 的许可证纯洁化工程是开源历史上规模最大的系统性 GPL 代码替换运动。这不是单一决策的结果，而是持续十余年的“逐点清除”工程，每个 GNU 工具的替换都是独立的工程项目，有各自的时间表和贡献者。整个工程的核心理念是：基础系统（base system）应完全由 BSD 或 BSD 兼容许可证（如 MIT、ISC、Apache 2.0）的代码构成，将 GPL
- 总纲第 22 条——开源运动：Hubbard 的 GPL 批评是 1990 年代 "BSD vs GPL" 圣战的典型话语，这种话语在当时的 Usenet 和邮件列表中普遍存在，反映了自由软件运动内部 copyleft 阵营与宽容许可阵营的深刻分歧。
  - 辨析：Hubbard 的 GPL 批评必须置于其历史语境中理解——1990 年代是 BSDi vs USL 诉讼刚结束、Linux 刚兴起、
- 总纲第 3 条——形式主义膨胀：1990 年代 Usenet 圣战言论在 2020 年代被抽离语境反复引用，成为制造 "BSD vs Linux" 对立的素材。历史书写应还原话语语境而非强化刻板印象。
  - 辨析：Hubbard 离开 FreeBSD 后对项目的评论频率降低，他后来在 iXsystems 工作时支持 TrueNAS 基于 FreeBSD 的产品开发，其观点随时间可能有所演变。

- 总纲第 17 条——软件工程：当代 FreeBSD 核心开发者的许可证话语已从 1990 年代的圣战模式转向工程风险评估模式。这种转变反映了项目从 “业余爱好者社区” 向 “企业级操作系统” 成熟的过程。
  - 辨析：原文件多次泛泛提及 “Baldwin 许可证观点邮件列表” 但未给出具体语境和观点内容，本节据其在 KTLS、bhyve、SMP 等项目中的公开论述和邮件列表发言综合概括。
  -

## 辨析

- 2014 年 license 相关 commit 量从 21,962 骤增至 35,494（增幅 61.6%），与 FreeBSD 10.0-RELEASE（2014.1.20）Clang 成为默认编译器、BIND 移除、bmake 替换 GNU make 等大规模许可证纯洁化里程碑时间点吻合；2015-2016 年 commit 量持续攀升至 53,771 峰值，反映 CDDL 许可的 ZFS/
- Hubbard 的 GPL 批评必须置于其历史语境中理解——1990 年代是 BSDi vs USL 诉讼刚结束、Linux 刚兴起、开源一词刚被创造（1998）的时代，许可证圣战是当时社区文化的常态。2007 年 GPLv3 危机发生时 Hubbard 已不在 Core Team，他的观点是 FreeBSD 许可证文化的背景之一，而非 Clang 迁移的直接决策依据。
  - 文献：Hubbar
- Hubbard 离开 FreeBSD 后对项目的评论频率降低，他后来在 iXsystems 工作时支持 TrueNAS 基于 FreeBSD 的产品开发，其观点随时间可能有所演变。
  - 文献：FreeBSD 邮件列表存档 [EB/OL]. docs.freebsd.org/mail/. ［A］
- 原文件多次泛泛提及 “Baldwin 许可证观点邮件列表” 但未给出具体语境和观点内容，本节据其在 KTLS、bhyve、SMP 等项目中的公开论述和邮件列表发言综合概括。
  - 文献：Baldwin J. KTLS: TLS Offload in the FreeBSD Kernel [C]//BSDCan 2019. Ottawa, 2019；John Baldwin freebsd-arc

## 文献

- FreeBSD 10.0/12.0/13.0 Release Notes [Z]；Giffuni P. [CFT] WITH_BSD_PATCH [EB/OL]. freebsd-current mailing list, 2013-01-29；Schwarze I. mandoc: A BSD-licensed UNIX manual page compiler [EB/OL]. mandoc.bsd.lv；FreeBSD Quarterly Status Report 2012 Q1 (BSD-licensed sort entry)[R]. 2012. ［A］

## 146.4.2 许可

- Hubbard J. FreeBSD 辞职信 [Z]. freebsd-core mailing list, 2001；Hubbard J. 各类 freebsd-advocacy 邮件列表发言 [Z]. 1998-2001. ［A］

## 146.5.2 Hubbard 观点的社区效应

- 要点：Hubbard 作为 FreeBSD 创始人和早期项目代言人，其许可证观点深刻影响了 FreeBSD 社区文化，奠定了项目 “BSD 许可证优先” 的价值取向。这种文化取向使得 2007 年 GPLv3 危机发生时，Core Team 几乎没有内部分歧就做出了 “冻结 GCC 版本、启动 BSD
- FreeBSD 邮件列表存档 [EB/OL]. docs.freebsd.org/mail/. ［A］
- Baldwin J. KTLS: TLS Offload in the FreeBSD Kernel [C]//BSDCan 2019. Ottawa, 2019；John Baldwin freebsd-arch/fireebsd-current 邮件列表存档 [Z]. lists.freebsd.org.

## 146.6.2 Baldwin 等人观点的工程实践效应

- 要点：以 Baldwin、Brooks Davis、Warner Losh（沃纳·洛什）、Dimitry Andric、Ed Schouten 等为代表的当代核心开发者采取工程务实主义立场，这一立场在实践中体现为：推进

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
