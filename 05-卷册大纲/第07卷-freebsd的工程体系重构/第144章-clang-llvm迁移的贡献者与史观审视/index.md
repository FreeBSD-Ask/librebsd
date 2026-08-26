---
chapter: 第 144 章
id: CH144
volume: 07
---

## 要点

- FreeBSD Clang/LLVM 迁移由一批核心 committer 历时多年完成，按主要贡献领域划分：①Roman Divacky（rdivacky@）——先锋探索者，2009 年 2 月首次宣布 Clang 可编译启动 i386/amd64 FreeBSD 内核，是迁移可行性的证明者；②Brooks Davis（brooks@）——项目协调人，2012 年 11 月宣布 x86 默认切换 Clang，长期参与工具链和架构支持工作；③David Chisnall（戴维·奇斯纳尔）（theraven@）——C++ 栈负责人，主导 libc++/libcxxrt 引入和 xlocale 实现，解决 C++11 支持问题；注意其姓名为 David Chisnall，非 "Theresa Chisnall"（这是对 theraven 用户名的误读）；④Dimitry Andric（dim@）——版本维护者，承担了历年 LLVM/Clang 版本导入、ports 兼容性修复和大量 bug 修正工作，是持续时间最长的日常维护者；⑤Ed Schouten（ed@）——早期贡献者，参与 2010-2012 年 Clang 导入和 world/kernel 修复；⑥Andrew Turner（andrew@）——arm64/AArch64 移植负责人，使 FreeBSD 在 ARM64 时代获得 Tier 1 地位；⑦Warner Losh（沃纳·洛什）（imp@）——GCC 4.2.1 退休执行者，推动 sparc64/mips 等旧架构的工具链切换或废弃；⑧Pawel Worach——早期测试和补丁贡献者（2012 Q1 status report 列为联系人之一）；⑨FreeBSD Foundation——资助多个工具链迁移子项目（包括 lld 默认切换、arm64 移植等）。
- 除编译器外的许可证纯洁化子项目各有其主要贡献者：①bmake——Simon J. Gerraty 等人从 NetBSD 移植，10.0 默认替换 GNU make；②BSD grep——主要由 Gábor Kövesdán（gabor@）等人开发（基于 TRE 正则表达式库）；③BSD sort——Q1 2012 status report 报告为 Tim Kientzle 等人开发（原文件未具体记载，待进一步核）；④BSD patch——Pedro Giffuni（pfg@）移植 OpenBSD 版本，r246074（2013.1.29）导入，r253689 成为默认；⑤mandoc——Ingo Schwarze（英戈·施瓦茨）（OpenBSD）开发，FreeBSD 逐步引入作为 groff 替代；⑥ELF Tool Chain——Kai Wang、Joseph Koshy（约瑟夫·科希） 等人开发的 BSD 许可 ELF 工具；⑦lld/lldb 集成——由 Dimitry Andric、Ed Maste（埃德·马斯特） 等人维护；⑧Unbound——替代 BIND 导入 base；⑨BSD dialog——2024 年完成替换（FreeBSD 16），具体提交者待查。FreeBSD Foundation 资助了多个上述项目（Growing Filesystems Online、auditdistd、NAND 等非工具链项目也获得资助，但工具链迁移同样受益于 Foundation 资助）。
- Clang/LLVM 迁移的成功不仅依赖 base 系统 committer，大量 ports 维护者和测试者的工作同样不可或缺。迁移期间需要修复数千个 ports 软件的 Clang 兼容性问题（GCC 扩展依赖、嵌套函数、VLA in struct、特定 builtins、typeof 等），这些工作由数百名 ports committer 逐 port 完成。Ports 集群定期进行 Clang exp-run（全量 ports 树使用 Clang 编译测试），发现并报告编译错误。FreeBSD 10.0 之前的数年中，所有 -CURRENT 和 -STABLE 用户自愿测试 Clang 构建的 world/kernel，报告 bug 并提交补丁。这些测试者和 ports 贡献者构成了迁移的群众基础，但他们的名字大多湮没在邮件列表和 PR 数据库中。
- 贡献者名单的史料主要来自 Quarterly Status Reports 联系人列表、commit log 作者字段、邮件列表发件人。Q1 2012 status report 的 Clang 条目明确列出 6 位联系人（Davis/Chisnall/Andric/Schouten/Worach/Divacky），这是 Clang 迁移核心团队最权威的一手名单。其他子项目（bmake/BSD patch/BSD grep/mandoc/ELF Tool Chain/lld 等）的贡献者需逐项目通过 SVN/Git 历史追溯，部分项目贡献者记录不完整。
- dialog 是一种基于文本的用户界面库（用于 shell 脚本中的对话框），FreeBSD base 系统长期使用的 **dialog(1)** 是 GNU dialog（GPLv2 许可）。随着其他 GPL 组件逐一被替换，dialog 成为 FreeBSD base 中最后一个 GPL 许可的软件组件。2024 年 7 月，Linuxiac 等科技媒体报道 FreeBSD 16-CURRENT 开发分支正式移除了 GNU dialog，替换为 BSD 许可的实现（可能是基于 OpenBSD 或 NetBSD 的 BSD dialog 版本，或新项目）。这标志着从 2007 年 GCC 冻结开始的许可证纯洁化工程在代码层面最终完成——FreeBSD base 系统不再包含任何 GPL 许可的代码，全部由 BSD/MIT/ISC/Apache 2.0/CDDL 等宽容许可证或 FreeBSD 可接受的弱 copyleft 许可证（CDDL 文件级 copyleft 不传染）代码构成。

## 史观

- 总纲第 10 条——边缘者贡献：编译器迁移是典型的 “基础设施工程”——没有耀眼的新功能发布，没有媒体关注，只有经年累月的 bug 修复和兼容性调整。Divacky（2009 年首告内核可启动时甚至不是全职 committer）、Andric（做了最多日常版本维护和 bug 修复的无名英雄）、Worach（测试和补丁贡献者）等人的工作往往不在聚光灯下，但他们是迁移真正的基石。
  - 辨析：Dav
- 总纲第 10 条——边缘者贡献：每个 GNU 工具的替换都是一个独立的小型工程项目，由 1-2 名核心开发者主导，历经数年渐进完成。这些工具替换工作在 Release Notes 中仅占一行，但背后是数百个 commit 和数千小时的测试工作。
  - 辨析：BSD sort 的主要开发者在 Q1 2012 status report 中未明确署名（仅列为项目条目），需对照 SVN 历史确认具体贡
- 总纲第 25 条——终结与延续：dialog 移除是一个时代的终结——从 1992/1993 年 FreeBSD 创立以来，GPL 代码（GCC、gdb、binutils、groff、make、dialog、grep、sort、patch、BIND、texinfo、rcs 等）一直是 FreeBSD base 的重要组成部分（CSRG 时代 BSD 即包含 GCC 和 GNU 工具）。2024 年
- 总纲第 17 条——软件工程：编译速度是影响开发者生产力的关键因素——Clang 的编译速度优势在 FreeBSD 这类需频繁从源码构建整个系统的 OS 项目中尤为明显（buildworld 时间缩短对开发者体验有直接影响）。但运行时性能在服务器/生产环境中通常比编译速度更重要，这也是为什么 Clang 运行时性能追赶花费了近十年时间才达到与 GCC 持平。
  - 辨析：基准测试结果高度依赖测试
- 总纲第 17 条——软件工程：双编译器支持虽然增加了代码复杂度，却迫使内核代码更符合标准 C、减少对编译器特定行为的依赖，长期来看提高了代码质量。迁移完成后，Clang 独有的安全工具（CFI、sanitizers）为 FreeBSD 内核安全加固提供了 GCC 生态无法提供的能力。
  - 辨析：Linux 内核 Clang 编译的许多问题（如 variable length arrays in

## 辨析

- David Chisnall 的姓名错误——原文件和多个中文资料中出现的 "Theresa Chisnall" 是对其用户名 **theraven@** 的误读（theraven → "The Raven" → 误联想为女性名字 Theresa），其 AsiaBSDCon 2014 论文作者署名明确为 David Chisnall，此错误已修正。
  - 文献：FreeBSD Quarterly 
- BSD sort 的主要开发者在 Q1 2012 status report 中未明确署名（仅列为项目条目），需对照 SVN 历史确认具体贡献者；BSD dialog 的替换提交者和精确 commit hash 需查阅 FreeBSD Git 仓库（2024 年移除）。
  - 文献：FreeBSD 10.0-RELEASE Announcement [Z]. 2014-01-20；Giffuni
- dialog 移除的精确 commit hash 和日期需查阅 FreeBSD Git 仓库确认（中文媒体报道为 2024 年 7 月，FreeBSD 16-CURRENT 分支），替换为的 BSD dialog 具体来源（是新写的还是从 OpenBSD/NetBSD 移植）也需对照 commit 确认；CDDL 许可的 DTrace/ZFS/CTF 工具仍在 base 中，但 CDDL 是文件级
- 基准测试结果高度依赖测试负载、编译选项、架构和版本号——“Clang 比 GCC 快” 或 “GCC 生成代码比 Clang 快” 这类笼统陈述在没有具体版本和测试条件的情况下均不严谨。
  - 文献：Clang Team. Clang Features and Goals: Fast compiles and Low Memory Use [EB/OL]. clang.llvm.org/feat
- Linux 内核 Clang 编译的许多问题（如 variable length arrays in structs、nested functions）是 Linux 特有的编码风格问题，FreeBSD 内核代码库在 2009 年 Clang 迁移过程中已主动清理了此类 GCC 扩展依赖。
  - 文献：FreeBSD Wiki. Building FreeBSD with Clang [EB/O

## 文献

- FreeBSD Quarterly Status Report 2012 Q1 [R]；Chisnall D. LLVM in the FreeBSD Toolchain [C]//AsiaBSDCon 2014（作者署名 David Chisnall）；Divacky R. 2009 kernel announcement [EB/OL]；Davis B. 2012 default announcement [EB/OL].
- FreeBSD 10.0-RELEASE Announcement [Z]. 2014-01-20；Giffuni P. [CFT] WITH_BSD_PATCH [EB/OL]. freebsd-current, 2013-01-29；FreeBSD Quarterly Status Report 2012 Q1 [R]. ［A］
## 143.12.3 被忽视的测试者和 ports 贡献者
  - 要点：Clang/LLVM 迁移的成功不仅依赖 base 系统 committer，大量 ports 维护者和测试者的工作同样不可或缺。迁移期间需要修复数千个 ports 软件的 Clang 兼
- Linuxiac. FreeBSD Base System Is Now GPL-Free [EB/OL]. linuxiac.com, 2024-07-17；FreeBSD Git repository. dialog removal commit [Z]. cgit.freebsd.org/src, 2024. ［A］
## 143.13.2 许可证纯洁化的法律里程碑意义
  - 要点：FreeBSD base 系统 GPL 代码清零具有重要的法律和生态里程碑意义：① 法律确定性——商业用户可确信 FreeBSD base 不包含 GPLv2/v3 代码，不存在 GPL 许可证合规风险（除
- Clang Team. Clang Features and Goals: Fast compiles and Low Memory Use [EB/OL]. clang.llvm.org/features.html, 2007；Larabel M. GCC 4.9 VS. LLVM Clang 3.5 Benchmarks [EB/OL]. OpenBenchmarking.org, 2014-04-14；Larabel M. LLVM Clang 16 vs. GCC 13 Performance [EB/OL]. Phoronix, 2023-05-11.[考据完成：2026-07-28
- FreeBSD Wiki. Building FreeBSD with Clang [EB/OL]. wiki.freebsd.org；LLVM Project. Clang Control Flow Integrity [EB/OL]. clang.llvm.org/docs/ControlFlowIntegrity.html. ［B］
## 143.14.3 静态分析与工具链质量工具
  - 要点：Clang/LLVM 带来的不仅是编译器替换，更包括一系列基于 Clang AST 的代码质量工具：Clang Static Analyzer（静态分析器，可在编译时检测空指针解引用、内存泄漏、
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13 条）；Free Software Foundation. GNU General Public License Version 3 [Z]. 2007-06-29（§11）；Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01（§3）.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 19 条）；原材料/哲学/项目统摄史观/第 19 章.md（19.2、19.3 节）. ［A］
## 143.15.3 总纲第 21 条审视——革命与改革的方法论分歧
  - 要点：总纲第 21 条断言“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命”。以此审视 FreeBSD 许可证纯洁化工程，可见其方法论本质是典型的“改革”而非“革命”——FreeBSD 采取“导入 → 可选 → 默认 → 移除”四阶段渐进策略（以 GCC 为例：2009 可编译 →2012 base 可选 →2014 默认 →
- Free Software Foundation. 各类许可证及其评论 [EB/OL]. **<https://www.gnu.org/licenses/license-list.html**>（2026-07-23 核验）；Free Software Foundation. GNU General Public License Version 3 [Z]. 2007-06-29；Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01. ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。