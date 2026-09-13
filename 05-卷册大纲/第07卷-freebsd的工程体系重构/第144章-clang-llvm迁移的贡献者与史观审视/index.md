# 第 144 章 clang-llvm迁移的贡献者与史观审视

---
chapter: 第 144 章
id: CH144
volume: 第07卷-freebsd的工程体系重构
---

## 要点

- FreeBSD Clang/LLVM 迁移由一批核心 committer 历时多年完成，按主要贡献领域划分：①Roman Divacky（rdivacky@）——先锋探索者，2009 年 2 月首次宣布 Clang 可编译启动 i386/amd64 FreeBSD 内核，是迁移可行性的证明者；②Brooks Davis（brooks@）——项目协调人，2012 年 11 月宣布 x86 默认切换 Clang，长期参与工具链和架构支持工作；③David Chisnall（戴维·奇斯纳尔）（theraven@）——C++ 栈负责人，主导 libc++/libcxxrt 引入和 xlocale 实现，解决 C++11 支持问题；注意其姓名为 David Chisnall，非 “Theresa Chisnall”（这是对 theraven 用户名的误读）；④Dimitry Andric（dim@）——版本维护者，承担了历年 LLVM/Clang 版本导入、ports 兼容性修复和大量 bug 修正工作，是持续时间最长的日常维护者；⑤Ed Schouten（ed@）——早期贡献者，参与 2010-2012 年 Clang 导入和 world/kernel 修复；⑥Andrew Turner（andrew@）——arm64/AArch64 移植负责人，使 FreeBSD 在 ARM64 时代获得 Tier 1 地位；⑦Warner Losh（沃纳·洛什）（imp@）——GCC 4.2.1 退休执行者，推动 sparc64/mips 等旧架构的工具链切换或废弃；⑧Pawel Worach——早期测试和补丁贡献者（2012 Q1 status report 列为联系人之一）；⑨FreeBSD Foundation——资助多个工具链迁移子项目（包括 lld 默认切换、arm64 移植等）。
- 除编译器外的许可证纯洁化子项目各有其主要贡献者：①bmake——Simon J. Gerraty 等人从 NetBSD 移植，10.0 默认替换 GNU make；②BSD grep——主要由 Gábor Kövesdán（gabor@）等人开发（基于 TRE 正则表达式库）；③BSD sort——Q1 2012 status report 报告为 Tim Kientzle 等人开发（原文件未具体记载，待进一步核）；④BSD patch——Pedro Giffuni（pfg@）移植 OpenBSD 版本，r246074（2013.1.29）导入，r253689 成为默认；⑤mandoc——Ingo Schwarze（英戈·施瓦茨）（OpenBSD）开发，FreeBSD 逐步引入作为 groff 替代；⑥ELF Tool Chain——Kai Wang、Joseph Koshy（约瑟夫·科希） 等人开发的 BSD 许可 ELF 工具；⑦lld/lldb 集成——由 Dimitry Andric、Ed Maste（埃德·马斯特） 等人维护；⑧Unbound——替代 BIND 导入 base；⑨BSD dialog——2024 年完成替换（FreeBSD 16），具体提交者待查。FreeBSD Foundation 资助了多个上述项目（Growing Filesystems Online、auditdistd、NAND 等非工具链项目也获得资助，但工具链迁移同样受益于 Foundation 资助）。
- Clang/LLVM 迁移的成功不仅依赖 base 系统 committer，大量 ports 维护者和测试者的工作同样不可或缺。迁移期间需要修复数千个 ports 软件的 Clang 兼容性问题（GCC 扩展依赖、嵌套函数、VLA in struct、特定 builtins、typeof 等），这些工作由数百名 ports committer 逐 port 完成。Ports 集群定期进行 Clang exp-run（全量 ports 树使用 Clang 编译测试），发现并报告编译错误。FreeBSD 10.0 之前的数年中，所有 -CURRENT 和 -STABLE 用户自愿测试 Clang 构建的 world/kernel，报告 bug 并提交补丁。这些测试者和 ports 贡献者构成了迁移的群众基础，但他们的名字大多湮没在邮件列表和 PR 数据库中。
- 贡献者名单的史料主要来自 Quarterly Status Reports 联系人列表、commit log 作者字段、邮件列表发件人。Q1 2012 status report 的 Clang 条目明确列出 6 位联系人（Davis/Chisnall/Andric/Schouten/Worach/Divacky），这是 Clang 迁移核心团队最权威的一手名单。其他子项目（bmake/BSD patch/BSD grep/mandoc/ELF Tool Chain/lld 等）的贡献者需逐项目通过 SVN/Git 历史追溯，部分项目贡献者记录不完整。
- dialog 是一种基于文本的用户界面库（用于 shell 脚本中的对话框），FreeBSD base 系统长期使用的 **dialog(1)** 是 GNU dialog（GPLv2 许可）。随着其他 GPL 组件逐一被替换，dialog 成为 FreeBSD base 中最后一个 GPL 许可的软件组件。2024 年 7 月，Linuxiac 等科技媒体报道 FreeBSD 16-CURRENT 开发分支正式移除了 GNU dialog，替换为 BSD 许可的实现（可能是基于 OpenBSD 或 NetBSD 的 BSD dialog 版本，或新项目）。这标志着从 2007 年 GCC 冻结开始的许可证纯洁化工程在代码层面最终完成——FreeBSD base 系统不再包含任何 GPL 许可的代码，全部由 BSD/MIT/ISC/Apache 2.0/CDDL 等宽容许可证或 FreeBSD 可接受的弱 copyleft 许可证（CDDL 文件级 copyleft 不传染）代码构成。

## 史观

- 总纲第 10 条——动手者创造历史：编译器迁移是典型的 “基础设施工程”——没有耀眼的新功能发布，没有媒体关注，只有经年累月的 bug 修复和兼容性调整。Divacky（2009 年首告内核可启动时甚至不是全职 committer）、Andric（做了最多日常版本维护和 bug 修复的无名英雄）、Worach（测试和补丁贡献者）等人的工作往往不在聚光灯下，但他们是迁移真正的基石。
  - 辨析：Dav
- 总纲第 10 条——动手者创造历史：每个 GNU 工具的替换都是一个独立的小型工程项目，由 1-2 名核心开发者主导，历经数年渐进完成。这些工具替换工作在 Release Notes 中仅占一行，但背后是数百个 commit 和数千小时的测试工作。
  - 辨析：BSD sort 的主要开发者在 Q1 2012 status report 中未明确署名（仅列为项目条目），需对照 SVN 历史确认具体贡
- 总纲第 3 条——不存在进步，只有权力再分配（原挂“总纲第 25 条——终结与延续”系伪标签，依核查报告改挂）：dialog 移除是一个时代的终结——从 1992/1993 年 FreeBSD 创立以来，GPL 代码（GCC、gdb、binutils、groff、make、dialog、grep、sort、patch、BIND、texinfo、rcs 等）一直是 FreeBSD base 的重要组成部分（CSRG 时代 BSD 即包含 GCC 和 GNU 工具）。2024 年
- 软件工程（专题语，不设总纲条号；原挂“总纲第 17 条”系伪标签，依核查报告订正）：编译速度是影响开发者生产力的关键因素——Clang 的编译速度优势在 FreeBSD 这类需频繁从源码构建整个系统的 OS 项目中尤为明显（buildworld 时间缩短对开发者体验有直接影响）。但运行时性能在服务器/生产环境中通常比编译速度更重要，这也是为什么 Clang 运行时性能追赶花费了近十年时间才达到与 GCC 持平。
  - 辨析：基准测试结果高度依赖测试
- 软件工程（专题语，不设总纲条号；原挂“总纲第 17 条”系伪标签，依核查报告订正）：双编译器支持虽然增加了代码复杂度，却迫使内核代码更符合标准 C、减少对编译器特定行为的依赖，长期来看提高了代码质量。迁移完成后，Clang 独有的安全工具（CFI、sanitizers）为 FreeBSD 内核安全加固提供了 GCC 生态无法提供的能力。
  - 辨析：Linux 内核 Clang 编译的许多问题（如 variable length arrays in

## 辨析

- David Chisnall 的姓名错误——原文件和多个中文资料中出现的 “Theresa Chisnall” 是对其用户名 **theraven@** 的误读（theraven → “The Raven” → 误联想为女性名字 Theresa），其 AsiaBSDCon 2014 论文作者署名明确为 David Chisnall，此错误已修正。
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

## 144.12.3 被忽视的测试者和 ports 贡献者

- 要点：Clang/LLVM 迁移的成功不仅依赖 base 系统 committer，大量 ports 维护者和测试者的工作同样不可或缺。迁移期间需要修复数千个 ports 软件的 Clang 兼
- Linuxiac. FreeBSD Base System Is Now GPL-Free [EB/OL]. linuxiac.com, 2024-07-17；FreeBSD Git repository. dialog removal commit [Z]. cgit.freebsd.org/src, 2024. ［A］

## 144.13.2 许可证纯洁化的法律里程碑意义

- 要点：FreeBSD base 系统 GPL 代码清零具有重要的法律和生态里程碑意义：① 法律确定性——商业用户可确信 FreeBSD base 不包含 GPLv2/v3 代码，不存在 GPL 许可证合规风险（除〔存疑：原文截断，回源补全待考〕
- Clang Team. Clang Features and Goals: Fast compiles and Low Memory Use [EB/OL]. clang.llvm.org/features.html, 2007；Larabel M. GCC 4.9 VS. LLVM Clang 3.5 Benchmarks [EB/OL]. OpenBenchmarking.org, 2014-04-14；Larabel M. LLVM Clang 16 vs. GCC 13 Performance [EB/OL]. Phoronix, 2023-05-11.［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］. wiki.freebsd.org；LLVM Project. Clang Control Flow Integrity [EB/OL]. clang.llvm.org/docs/ControlFlowIntegrity.html. ［B］

## 144.14.3 静态分析与工具链质量工具

- 要点：Clang/LLVM 带来的不仅是编译器替换，更包括一系列基于 Clang AST 的代码质量工具：Clang Static Analyzer（静态分析器，可在编译时检测空指针解引用、内存泄漏、
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13 条）；Free Software Foundation. GNU General Public License Version 3 [Z]. 2007-06-29（§11）；Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01（§3）.［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 19 条）；原材料/哲学/项目统摄史观/第 19 章.md（19.2、19.3 节）. ［A］

## 144.15.3 总纲第 21 条审视——革命与改革的方法论分歧

- 要点：总纲第 21 条断言“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命”。以此审视 FreeBSD 许可证纯洁化工程，可见其方法论本质是典型的“改革”而非“革命”——FreeBSD 采取“导入 → 可选 → 默认 → 移除”四阶段渐进策略（以 GCC 为例：2009 可编译 →2012 base 可选 →2014 默认 →
- Free Software Foundation. 各类许可证及其评论 [EB/OL]. **<https://www.gnu.org/licenses/license-list.html**>（2026-07-23 核验）；Free Software Foundation. GNU General Public License Version 3 [Z]. 2007-06-29；Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01. ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP229、BSDTalk EP233（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 该期综述 OpenBSD、DragonFly BSD、NetBSD 对 Meltdown/Spectre 的响应：OpenBSD 引入微码更新工具，DragonFly 提交 MMU 隔离与 IBRS/IBPB，NetBSD 引入 Hot Patch 与 SVS 分离页表。（BSD Now EP229，[931.46-1482.64]，L2）
- IT Wire 报道 Theo de Raadt 的批评：仅一级厂商获得预先披露属选择性披露，并援引其 2007 年对 Intel 芯片设计问题的邮件。（BSD Now EP229，[695.8-835.26]，L2）
- 转述 Drew DeVault 的文章：追溯 1971 年 PDP-11 上 fork 的诞生、vfork 与 posix_spawn 的局限，以及 Plan 9 的 rfork 与 spawn 模型。（BSD Now EP229，[4297.5-4945.7]，L2）
- Ed Maste 提交使 LLD 成为 AMD64 默认引导链接器，标志 FreeBSD 用户态向非 GNU 工具链迁移的推进。（BSD Now EP229，[4975.44-5145.06]，L2）
- 采访 DragonFly BSD 用户：其因减少锁与高性能设计而选择 DragonFly，使用 HAMMER 的 undo 功能与快照、HAMMER2 的透明压缩。（BSD Now EP229，[2246.7-2489.82]，L1）
- FreeBSD 对 Clang 的采用始于 2009 年 2 月 Roman 与 Pavel 的构建实验，当时距 GPLv2 版 GCC 最后一次发布已近两年；实验迅速达到可编译内核并引导的程度，随即在 LLVM Bugzilla 开设元缺陷 PR2696 追踪全部阻塞项。2010 年 1 月 Clang 实现自举，距 2006 年 C 解析器入库约三年半，且依赖 Apple 与 Google 的全职投入；同年 9 月可构建全部基础系统，2011 年 5 月元缺陷关闭、x86-64 上以标准优化级别完成全量编译。此后 9.0 将 Clang 列为可选编译器，10-CURRENT 使其成为 tier-1 架构默认编译器并以 libc++ 与 libcxxrt 取代 GNU C++ 栈。（BSDTalk EP233，[706.77-841.00]，L1）
- 编译器切换的收尾长尾集中在调试端：Clang 默认输出 Dwarf 4，而基础系统 GDB 仅支持 Dwarf 2，ports 中的 GDB 虽支持 Dwarf 4 却属 GPLv3，以旧 GDB 调试 Clang 代码时行号时有时无、断点失效、变量列表错乱乃至解析器崩溃。Ed 移植源自 Apple 的 LLDB，彼时支持 AMD64 单线程活调试、多线程近于完成、核心转储可用，32 位与 MIPS 尚未支持，内核调试器集成被排在最后；FreeBSD Foundation 另拟资助以 Capsicum 将调试器沙箱化，以应对被调试程序元数据损坏或恶意输入对调试器本身的攻击面。（BSDTalk EP233，[3591.80-3765.87]，L1）

**史料**：

- DragonFly BSD 的 Matthew Dillon 1 月 5 日关于 Meltdown 为 Intel 专属缺陷、AMD 免疫的帖子。（BSD Now EP229，[1015.3-1056.54]，L2）
- Theo de Raadt 2007 年 6 月 27 日的邮件线索（IT Wire 报道所引），涉及对 Intel x86 设计问题的早期批评。（BSD Now EP229，[807.38-835.26]，L2）
- Drew DeVault 的 fork 批评文章，以 1971 年贝尔实验室的 PDP-11 语境叙述 fork 的诞生。（BSD Now EP229，[4299.5-4438.76]，L2）
- FreeBSD 的 LLD bootstrap 链接器提交（Ed Maste 的提交信息，LLVM PR 23214 与 85 个依赖 issue）。（BSD Now EP229，[5056.46-5134.62]，L2）
- 该期可提取的一手史料包括：vBSDCon 2013 演讲录音本身（bsdtalk 第 233 期，2013 年 11 月 1 日）；LLVM Bugzilla 元缺陷 PR2696 及其依赖缺陷清单，当事人称其依赖列表约占半屏；BSD camp 期间以 Clang 与 GCC 分别作为默认编译器对 ports 树反复执行的实验运行（exp runs）记录；PCC 项目网页曾宣称 C 支持基本完成、C++ 为下一步；GCC 中 Objective-C 支持集中所在的约一万行单文件；libc++ 测试用例在 FreeBSD、Linux 与 OS X 上的失败计数；以及 FreeBSD Foundation 付费委托 libc++ 移植的经 Roman 转述对话。（BSDTalk EP233，[743.75-765.63]，L1）

**史观**：

- 总纲8 本体论上各方平等：各 BSD 在 Meltdown/Spectre 面前的独立响应路径显示本体论上的多方平等，没有单一正确解。（BSD Now EP229，[1460.82-1482.64]，L2）
- 总纲13 法律与道德是利益分配：Theo 对 Intel 的批评强调选择性披露使大厂之外者受损，呈现披露秩序中的利益分配而非技术中立。（BSD Now EP229，[706.42-720.42]，L2）
- 总纲22 知识注定过时：对 fork 的批评把近 50 年的设计选择与内存过量承诺、OOM killer 等后果联系起来，呈现旧有设计在当下的历史惯性。（BSD Now EP229，[4516.04-4624.68]，L2）
- 总纲13 法律与道德是利益分配：许可证决策在叙述中呈现为利益与风险的分配而非技术优劣的裁决：FreeBSD 阵营对 GPLv2 予以容忍、却以‘never’级别的决心拒绝 GPLv3 进入基础系统，理由不在代码质量而在法律边界与依赖失控的担忧；Chisnall 又以自己参与 GNU 项目时 LGPLv2 升级 v3 遭遇唯一开源 PDF 渲染库为 GPLv2-only 的冲突、被迫回退的亲历，说明许可证版本切换实为生态利益格局的重新切割；宽松许可的价值则被表述为让律师替你思考法律问题、从而解放开发者专注于代码。（BSDTalk EP233，[303.27-390.49]，L1）
- 总纲5 没有必然性，只有偶然性：跨平台移植中暴露的调用约定差异被当事人解读为无对错可言的历史承袭：i386 结构返回惯例上 Linux 沿 DOS 时代的做法经指针间接传递，FreeBSD 则承袭 VAX 的寄存器返回路径，且当事人明言双方都并非出于正确理由；FreeBSD、Linux 与 OS X 对向量参数的传递方式亦各不相同。系统接口差异的成因是偶然的路径依赖，而非任何一方的必然优越。（BSDTalk EP233，[1042.59-1082.11]，L1）
- 总纲19 解释学循环是历史认识的根本条件：C++ 两阶段名字查找的兼容性案例显示规范文本与实现之间的解释学循环：GCC 依其理解先行实现而与后来澄清的语义相悖，微软编译器以另一种方式同样做错，致跨两家编译器的模板代码无从适配；Clang 因晚出生约十年得以从各方错误中反推规范本意而实现正确，C++ 标准委员会又经 C++03 澄清与后续技术报告反复改口。标准是经实现碰撞而被反复重读的形式约定，而非一次写定的真理。（BSDTalk EP233，[1712.33-1771.59]，L1）

**辨析**：

- 对 fork 的批评系博客作者个人立场，节目主持人在结尾补充“无法改变应用使用习惯”的采纳难题，替代方案在 FreeBSD 仅停留在讨论阶段。　[存疑脚注] 系单一来源的个人技术立场（BSD Now EP229，[4888.6-4949.3]，L4）
- Theo de Raadt 对 Intel 的指控（“被告知忽略风险”）系其个人推断，无直接证据，节目亦未提供 Intel 回应。　[存疑脚注] 系个人推断，无直接证据（BSD Now EP229，[763.4-807.38]，L4）
- 演讲对 PCC 与 GCC 的评价带论战色彩，需与其他来源交叉验证：PCC 网页曾宣称 C++ 支持易于实现，而当事人指出 C++ 解析在一般情形下是不可计算问题、Clang 自举即耗时三年半并依赖 Apple 与 Google 的全职人力，故该宣称不足为凭；对 GCC 4.2.1 代码质量的贬抑亦系个人观感，其自陈因许可证原因从未阅读 GPLv3 代码，所评实为旧版。　[考据脚注] 对 PCC 与 GCC 的评价为当事人单方论战性叙述，PCC 网页宣称的具体时间与措辞、GCC 4.2.1 代码质量判断均需与两项目社区自身文献交叉核验。（BSDTalk EP233，[501.97-530.29]，L1）
- 以 Phoronix 基准中 FreeBSD 唯一显著落后一项为例，当事人将其归因于 Clang 当时缺失 OpenMP 支持而 GCC 内置 GNU OpenMP 库，并引 Intel 向 LLVM 捐赠 OpenMP 运行时为解决路径，预计 10.1 至 10.2 具备支持；该解释属单一来源对第三方基准的归因，且 HPC 用户通常不使用系统编译器，基准对公众认知的影响大于对实际工程的影响。　[存疑脚注] FreeBSD 在该基准中落后约 8 倍的归因仅为当事人解释，需对照 Phoronix 原始测试数据与当时 Clang/GCC 的 OpenMP 支持状态独立验证。（BSDTalk EP233，[3329.75-3394.84]，L4）

**文献**：

- [BSD Now EP229] Pennington J. BSD Now: 229: The Meltdown of Spectre[EB/OL]. (2018-01-17)[2026-08-15]. <https://www.bsdnow.tv/229>.
- [BSDTalk EP233] Backman W. BSDTalk: 233: bsdtalk233 - From GCC to LLVM/CLANG with David Chisnall[EB/OL]. (2013-11-01)[2026-08-27]. <https://bsdtalk.blogspot.com/2013/11/bsdtalk233-from-gcc-to-llvmclang-with.html>.

<!-- /PODCAST_REVIEW -->
