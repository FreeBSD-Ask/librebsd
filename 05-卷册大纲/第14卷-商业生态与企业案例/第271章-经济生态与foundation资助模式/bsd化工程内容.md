# 附录：原文件嵌入的 68.x 系列 BSD 化工程内容

> 本附录内容来自原 `大纲/第06卷-netbsd的历史/第133章-freebsd的商业生态.md` 文件史观映射段之后、`---` 分隔符之前的额外内容。
> 这些内容以 `68.XX` 编号体系呈现，不属于第 133 章 `#### 133.X` 子节体系，可能是原文件编辑时的误植或附录材料。
> 按“不得篡改原文内容”原则，完整保留此段内容作为附录备查，供后续考据与归位参考。
> 拆分日期：2026-07-20

68.17 **GCC → Clang/LLVM：最大的 BSD 化工程**——**GCC** 自 1987 年由 **Richard Stallman** 创建以来一直是 **GNU** 项目的核心编译器，**GPLv2** 许可证，2007 年 **GPLv3** 升级引发 **BSD** 社区担忧；**LLVM**（Low Level Virtual Machine）项目 2000 年由伊利诺伊大学香槟分校（**UIUC**）**Chris Lattner** 发起，采用 **UIUC/NCSA** 许可证（**BSD** 兼容），2005 年 **Apple** 聘用 **Lattner** 后大幅投入 **LLVM** 开发；**Clang**（C Language Frontend）2006 年作为 **LLVM** 前端发布；**FreeBSD 9.0**（2012.1）首次将 **Clang** 作为可选编译器；**FreeBSD 10.0**（2014.1）正式将 **Clang/LLVM** 作为默认编译器，移除 **GCC** 作为基本系统编译器——这是 **FreeBSD** 历史上最大的单一 **BSD** 化工程；**GCC → Clang** 迁移的技术动机包括：**Clang** 编译速度更快、错误信息更友好、模块化设计便于 IDE 集成、支持 ARC（**Objective-C** 自动引用计数）；许可证动机：**GCC GPLv3** §3 专利反制条款意味着任何使用 **GCC** 编译的代码都可能涉及专利授权问题，而 **Clang** 的 **BSD** 许可证无此限制；**Linus Torvalds** 也拒绝将 **Linux** 内核从 **GPLv2** 升级到 **GPLv3**，但 **Linux** 内核仍使用 **GCC** 编译；参见相关章节 **FreeBSD** 安全模型部分；

| 时间 | 事件 | 许可证 |
|---|---|---|
| 1987 | **GCC** 创建（**Stallman**） | **GPLv2** |
| 2000 | **LLVM** 项目发起（**Lattner**/**UIUC**） | **UIUC/NCSA** |
| 2005 | **Apple** 聘用 **Lattner** | — |
| 2006 | **Clang** 发布 | **BSD** |
| 2007 | **GPLv3** 发布 | **GPLv3** |
| 2012.1 | **FreeBSD 9.0** **Clang** 可选 | — |
| 2014.1 | **FreeBSD 10.0** **Clang/LLVM** 默认 | — |

｜ **子-子节**：68.17.1 迁移的技术与许可证动机；68.17.2 迁移过程与版本里程碑；68.17.3 与 **Linux** 编译器策略比较；68.17.4 史料辨析

68.18 **GNU binutils → BSD-licensed 替代**——**GNU binutils**（`as` 汇编器、`ld` 链接器、`ar` 归档工具、`objdump`、`readelf` 等）为 **GPLv3** 许可证；**FreeBSD** 的替换路径：① **LLD**（**LLVM** Linker）替代 **GNU** `ld`——**LLD** 是 **LLVM** 项目的一部分，**BSD** 许可证，**FreeBSD 11.0**（2016.10）开始使用 **LLD** 作为默认链接器；② `llvm-ar` 替代 **GNU** `ar`；③ `llvm-objdump` 替代 **GNU** `objdump`；④ `llvm-readelf` 替代 **GNU** `readelf`；⑤ **FreeBSD** 自带的 `as` 汇编器在部分架构上仍依赖 **GNU** `as`，但逐步被 **LLVM** 集成汇编器替代；**BSD** 化的未完成部分：部分嵌入式架构仍需 **GNU** `as`；

| GNU 工具 | BSD 化替代 | 许可证 | 状态 |
|---|---|---|---|
| `ld` | **LLD** | **BSD** | 完成 |
| `ar` | `llvm-ar` | **BSD** | 完成 |
| `objdump` | `llvm-objdump` | **BSD** | 完成 |
| `readelf` | `llvm-readelf` | **BSD** | 完成 |
| `as` | **LLVM** 集成汇编器 | **BSD** | 部分完成 |

｜ **子-子节**：68.18.1 替换路径与版本详情；68.18.2 替换过程的影响与局限；68.18.3 与其他 **OS** 工具链比较；68.18.4 史料辨析

68.19 **GNU coreutils → BSD 工具**——**GNU coreutils** 是 **GPLv3** 许可证的核心工具集，**FreeBSD** 逐步替换为 **BSD** 许可证的工具：① **GNU** `grep`（**GPLv3**）→ **BSD** `grep`——**FreeBSD** 自带的 `grep` 实现，**BSD** 许可证；② **GNU** `awk`/`gawk`（**GPLv3**）→ **BSD** `awk`（one-true-awk）——由 **BWK**（**Brian Kernighan**）原始 `awk` 演化，**BSD** 许可证；③ **GNU** `sed`（**GPLv3**）→ **BSD** `sed`——**FreeBSD** 自带实现；④ **GNU** `sort`（**GPLv3**）→ **BSD** `sort`——**FreeBSD** 自带实现，2005 年由 **David O'Brien** 重写以支持多字节字符；⑤ **GNU** `diff`/`diffutils`（**GPLv3**）→ **BSD** `diff`——**FreeBSD** 自带实现；⑥ **GNU** `patch`（**GPLv3**）→ **BSD** `patch`——**FreeBSD** 自带实现；⑦ **GNU** `cpio`（**GPLv3**）→ **BSD** `cpio`——基于 `libarchive`；⑧ **GNU** `findutils`（**GPLv3**）→ **BSD** `find`——**FreeBSD** 自带实现；这些工具的替换确保了 **FreeBSD** 基本系统的许可证纯化；

| **GNU** 工具 | **BSD** 化替代 | 关键人物/备注 |
|---|---|---|
| `grep` | **BSD** `grep` | **FreeBSD** 自带 |
| `awk`/`gawk` | **BSD** `awk` | **Brian Kernighan** 原始 |
| `sed` | **BSD** `sed` | **FreeBSD** 自带 |
| `sort` | **BSD** `sort` | **David O'Brien** 2005 重写 |
| `diff` | **BSD** `diff` | **FreeBSD** 自带 |
| `patch` | **BSD** `patch` | **FreeBSD** 自带 |
| `cpio` | **BSD** `cpio` | 基于 `libarchive` |
| `find` | **BSD** `find` | **FreeBSD** 自带 |

｜ **子-子节**：68.19.1 逐项替换的版本详情；68.19.2 替换对基本系统的影响；68.19.3 与 **NetBSD**/**OpenBSD** 工具比较；68.19.4 史料辨析

68.20 **GNU tar → bsdtar/libarchive**——**GNU** `tar` 为 **GPLv3** 许可证；`libarchive` 由 **Tim Kientzle** 开发，**BSD** 许可证，是一个统一的归档读写库；`bsdtar` 是基于 `libarchive` 的 `tar` 实现；**FreeBSD 5.3**（2004.10）将 `bsdtar` 作为默认 `tar`，替换 **GNU** `tar`；`libarchive` 还支持 `cpio`、`zip`、`ISO9660`、`7-Zip` 等多种归档格式；`libarchive` 后来被 **macOS**、**Windows** 等平台采用，是 **BSD** 化的最成功案例之一；｜ **子-子节**：68.20.1 `libarchive` 与 `bsdtar` 设计；68.20.2 替换过程与跨平台影响；68.20.3 作为最成功案例的辨析；68.20.4 史料辨析

68.21 **GNU make → BSD make**——**GNU** `make` 为 **GPLv3** 许可证；**FreeBSD** 使用 **BSD** `make`（又称 `pmake`）作为默认构建工具；**BSD** `make` 源自 **4.4BSD**，语法与 **GNU** `make` 不兼容（如 `.if`/`.else`/`.endif` vs `ifeq`/`else`/`endif`）；**FreeBSD** **Ports** 系统使用 `bsd.port.mk` 基于 **BSD** `make`；部分第三方软件仍依赖 **GNU** `make`，但作为 ports 依赖安装而非基本系统组件；｜ **子-子节**：68.21.1 **BSD** `make` 的语法与设计；68.21.2 **Ports** 系统对 **BSD** `make` 的依赖；68.21.3 与 **GNU** `make` 兼容性辨析；68.21.4 史料辨析

68.22 **GNU groff → mandoc**——**GNU** `groff` 为 **GPLv3** 许可证，是传统的 `man` page 格式化工具；`mandoc` 由 **Kristaps Dzonsons**（**OpenBSD**）和 **Ingo Schwarze（英戈·施瓦茨）**（**OpenBSD**）开发，**ISC** 许可证（**BSD** 兼容）；**OpenBSD** 率先在 2010 年采用 `mandoc` 替换 `groff`；**FreeBSD 14.0**（2023.11）将 `mandoc` 作为默认 `man` page 工具；`mandoc` 的优势：更小、更快、更安全，且支持 `man` page 的完整渲染；｜ **子-子节**：68.22.1 `mandoc` 的设计与优势；68.22.2 **OpenBSD** 率先采用与 **FreeBSD** 跟随；68.22.3 与 `groff` 功能比较；68.22.4 史料辨析

68.23 **GNU readline → libedit**——**GNU** `readline` 为 **GPLv3** 许可证，是交互式命令行编辑库；`libedit`（又称 `libeditline`）由 **Christos Zoulas（克里斯托斯·祖拉斯）**（**NetBSD**）开发，**BSD** 许可证，提供与 `readline` 兼容的 **API**；**FreeBSD** 基本系统使用 `libedit` 而非 `readline`；**NetBSD** 也使用 `libedit`；许多 **FreeBSD** 基本系统工具（如 `sh`、`bc`、`ftp`）使用 `libedit` 提供命令行编辑功能；｜ **子-子节**：68.23.1 `libedit` 的设计与 **API** 兼容性；68.23.2 基本系统工具的 `libedit` 集成；68.23.3 与 `readline` 功能比较；68.23.4 史料辨析

68.24 **版本控制系统迁移：CVS、SVN、Git**——**FreeBSD** 源代码管理系统的迁移路径：① **CVS**（Concurrent Versions System）——**GPLv2** 许可证，**FreeBSD** 1993-2008 年使用；② **SVN**（**Subversion**）——**Apache 2.0** 许可证（**BSD** 兼容），**FreeBSD** 2008-2021 年使用，**Benno Rice（本诺·赖斯）** 描述：

> “**FreeBSD** 直到 2008 年还在使用 **CVS**。为什么呢？因为大家对于应该用什么来代替它没有达成共识。考虑过 **BitKeeper**、**Git** 和 **Mercurial**，最后都无疾而终了”

> “2008 年，经过八年的争论，**Peter Wemm（彼得·韦姆）** 强行推进了向 **Subversion** 的转换”

③ **Git**——**GPLv2** 许可证，**FreeBSD** 2021 年迁移至 **Git**（参见相关章节版本控制系统迁移部分）；**Git** 虽然是 **GPLv2**，但因 **Linus Torvalds** 拒绝 **GPLv3**，且 **Git** 的使用方式（克隆仓库后本地操作）不触发 **GPL** 分发条款，**BSD** 社区接受 **Git** 作为版本控制工具；

| 版本控制系统 | 使用时期 | 许可证 |
|---|---|---|
| **CVS** | 1993-2008 | **GPLv2** |
| **SVN** | 2008-2021 | **Apache 2.0** |
| **Git** | 2021- | **GPLv2** |

｜ **子-子节**：68.24.1 **CVS** → **SVN** → **Git** 的迁移路径；68.24.2 迁移过程中的社区争议；68.24.3 **Git** 许可证的辨析；68.24.4 史料辨析

68.25 **GNU gettext → BSD-licensed 替代**——**GNU** `gettext` 为 **GPLv3** 许可证，是国际化（i18n）工具；**FreeBSD** 开发了 **BSD** 许可证的 `gettext` 替代品，但功能有限；**FreeBSD** 基本系统的国际化支持较少依赖 `gettext`，主要在 **Ports** 系统中处理；｜ **子-子节**：68.25.1 **BSD** `gettext` 替代品的开发；68.25.2 国际化支持的局限；68.25.3 与 **Linux** i18n 策略比较；68.25.4 史料辨析

68.26 **OpenPAM 替代 Linux PAM**——**Linux PAM** 为 **LGPL**/**GPL** 兼容许可证，存在许可证复杂性；**OpenPAM** 由 **Dag-Erling Smørgrav**（**FreeBSD** `committer`）开发，**BSD** 许可证；**FreeBSD 5.0**（2003.1）采用 **OpenPAM** 作为默认 **PAM** 实现；**OpenPAM** 的设计目标：更简洁的 **API**、**BSD** 许可证、与 **Linux PAM** 的二进制兼容；**OpenPAM** 是 **FreeBSD** 原创的 **BSD** 化成果；｜ **子-子节**：68.26.1 **OpenPAM** 的设计与目标；68.26.2 **FreeBSD 5.0** 采用与影响；68.26.3 与 **Linux PAM** 比较辨析；68.26.4 史料辨析

68.27 **BSD 化的哲学意义：自由之路**——**BSD** 化不仅是工程实践，更是 **BSD** 哲学的具体落实：① 自由即许可——**BSD** 社区认为真正的自由是允许所有人自由使用而不附加条件，**copyleft** 的“强制回馈”本质上是一种限制；② 许可证纯化——确保 **FreeBSD** 基本系统的每个组件都在 **BSDL** 条款下可用，使下游用户（如 **Apple**、**Sony**、**Juniper**）无需处理 **GPL** 兼容性问题；③ 自给自足——**BSD** 化体现了 **BSD** 社区“不依赖外部许可证”的自给自足精神，与 **Linux** 社区“拥抱 **GPL** 生态”的策略形成对照；④ 自由之路的悖论——**BSD** 化使 **FreeBSD** 基本系统更加自由，但也使 **FreeBSD** 更容易被商业巨头零回馈使用（如 **Apple** 取 **Darwin** 而不回馈），这是 **BSDL** 设计的必然结果；｜ **子-子节**：68.27.1 自由即许可的哲学论证；68.27.2 许可证纯化的工程意义；68.27.3 自由之路的悖论辨析；68.27.4 史料辨析

68.28 **BSD 化的局限与未完成的部分**——**BSD** 化并非完全完成：① 部分架构仍依赖 **GNU** `as` 汇编器（如部分嵌入式 **ARM**/**MIPS** 配置）；② **Ports** 系统中大量软件仍依赖 **GPL** 组件（如 **GCC** 作为某些语言的编译器、**GNU** `gettext` 作为国际化工具）；③ **Linux** 兼容层（`linuxulator`）可能涉及 **GPL** 影响的代码；④ **Git** 虽为 **GPLv2**，但被 **BSD** 社区接受为版本控制工具；⑤ 部分固件（如无线网卡固件）可能为专有或 **GPL** 许可证；⑥ **LLDB**（**LLVM Debugger**）虽为 **BSD** 许可证，但在功能上仍不及 **GDB**（**GPLv3**）完整；**BSD** 化是一个持续的过程，而非一次性完成的工程；｜ **子-子节**：68.28.1 未完成替换的具体组件；68.28.2 局限对 **FreeBSD** 的影响；68.28.3 **BSD** 化完成度的辨析；68.28.4 史料辨析

68.29 **BSD 化与 NetBSD/OpenBSD/DragonFly BSD 的对比**——① **OpenBSD** 是最激进的 **BSD** 化推行者——**OpenBSD** 不仅替换 **GCC** → **Clang**，还发起了 **LibreSSL**（替换 **OpenSSL** 的 **Apache 2.0** 许可证）、`mandoc`（替换 **GNU** `groff`）、**OpenNTPD**（替换 **ISC NTP** 的 **ISC** 许可证但 **OpenBSD** 重新实现）、**OpenBGPD**、**OpenSMTPD** 等一系列“去 **GPL**/去 **Apache**/去 **ISC**”的重新实现；**OpenBSD** 的 **BSD** 化驱动力来自 **Theo de Raadt（西奥·德·若特）** 对许可证纯洁性的严格要求；② **NetBSD** 也进行了 **BSD** 化，如 `libedit`（**NetBSD** 原创）、**BNF** 替代 **GNU** `bison` 等，但程度不及 **OpenBSD**；③ **DragonFly BSD** 继承了 **FreeBSD** 的 **BSD** 化成果，并在此基础上发展了自研工具；④ **FreeBSD** 的 **BSD** 化程度介于 **OpenBSD**（最激进）与 **NetBSD**（温和）之间；

| BSD 系统 | BSD 化程度 | 关键项目 | 驱动力 |
|---|---|---|---|
| **OpenBSD** | 最激进 | **LibreSSL**/`mandoc`/**OpenNTPD** | **Theo de Raadt** |
| **FreeBSD** | 中等 | **Clang/LLVM**/**LLD**/**OpenPAM** | 工程实用+**GPLv3** |
| **NetBSD** | 温和 | `libedit`/**BNF** | 跨平台实用 |
| **DragonFly BSD** | 继承 | 继承 **FreeBSD** 成果 | 无独立立场 |

｜ **子-子节**：68.29.1 各 **BSD** 系统的 **BSD** 化程度；68.29.2 **OpenBSD** 领先的驱动力；68.29.3 **BSD** 化节奏差异的辨析；68.29.4 史料辨析

68.30 **BSD 化的时代背景：GPLv3 2007 年的推动**——**GPLv3** 于 2007.6.29 由 **FSF** 发布，相比 **GPLv2** 增加了：①§3 专利反制——明确要求贡献者授予专利许可，防止专利攻击；②§6 反铁盒化（anti-tivoization）——要求用户可在修改后的设备上运行修改后的软件；③§7 附加许可——允许添加进一步限制；④§11 抗辩条款——明确免责声明；**BSD** 社区对 **GPLv3** 的反应：① **FreeBSD** 开发者担心 **GPLv3** 的专利条款会影响使用 **GCC** 编译的代码；② **Apple** 强烈反对 **GPLv3**，加速了 **LLVM**/**Clang** 的开发投入；③ **Linus Torvalds** 也拒绝将 **Linux** 内核升级到 **GPLv3**，认为反铁盒化条款过于限制；④ **GPLv3** 的发布成为 **FreeBSD** **BSD** 化的最大外部推动力，加速了 **GCC** → **Clang**、**GNU binutils** → **LLD** 等替换进程；

| **GPLv3** 新增条款 | 内容 | **BSD** 社区影响 |
|---|---|---|
| §3 专利反制 | 贡献者授予专利许可 | **GCC** 编译代码风险 |
| §6 反铁盒化 | 修改后设备可运行 | **Apple** 强烈反对 |
| §7 附加许可 | 允许添加限制 | 法律复杂性增加 |
| §11 抗辩条款 | 明确免责声明 | 影响有限 |

｜ **子-子节**：68.30.1 **GPLv3** 新增条款详情；68.30.2 **BSD** 社区与 **Apple** 的反应；68.30.3 **GPLv3** 作为 **BSD** 化推动力的辨析；68.30.4 史料辨析

68.31 **committer 权限记录**——本时期（2002-2026）**BSD** 化过程中未发生因 **BSD** 化争议而公开撤销 `committer` 权限的事件；但 **GCC** → **Clang** 迁移引发了社区内部的技术分歧，部分偏好 **GCC** 的 `committer` 减少了参与度；**BSD** 化进程中的关键 `committer` 包括：**Chris Lattner**（**LLVM**/**Clang** 创建者，非 **FreeBSD** `committer` 但对 **FreeBSD** **BSD** 化有重大影响）、**Dag-Erling Smørgrav**（**OpenPAM** 创建者）、**Tim Kientzle**（`libarchive`/`bsdtar` 创建者）、**Christos Zoulas**（`libedit` 创建者，**NetBSD** `committer`）、**Kristaps Dzonsons** 与 **Ingo Schwarze**（`mandoc` 创建者，**OpenBSD** `committer`）；

| `committer` | 项目 | 所属 BSD |
|---|---|---|
| **Chris Lattner** | **LLVM**/**Clang** | 非 **FreeBSD** `committer` |
| **Dag-Erling Smørgrav** | **OpenPAM** | **FreeBSD** |
| **Tim Kientzle** | `libarchive`/`bsdtar` | **FreeBSD** |
| **Christos Zoulas** | `libedit` | **NetBSD** |
| **Kristaps Dzonsons**/**Ingo Schwarze** | `mandoc` | **OpenBSD** |

｜ **子-子节**：68.31.1 **BSD** 化进程中的权限变动；68.31.2 关键提交者与贡献；68.31.3 权限治理的辨析；68.31.4 史料辨析

68.32 **许可证立场派系与排外**——**BSD** 与 **GPL** 两大许可证阵营在哲学立场上的根本分歧长期形成跨项目、跨社区、跨企业的派系对立与排外现象：（1）**BSD** 阵营内部的“纯化派”vs“实用派”——纯化派以 **OpenBSD** 的 **Theo de Raadt** 为代表，主张基本系统必须 100% **BSD** 许可证，对任何 **GPL** 组件零容忍，**LibreSSL**、`mandoc`、`libedit` 等 **BSD** 化工程均由 **OpenBSD** 率先推动；实用派以 **FreeBSD Core Team** 为代表，承认 **BSD** 化的工程价值但允许在过渡期保留部分 **GPL** 组件（如部分架构的 **GNU** `as`），强调“工程优先于意识形态”；**NetBSD** 处于两者之间，既推进 **BSD** 化但不激进；这种内部分歧导致 **OpenBSD** 社区长期嘲讽 **FreeBSD**“不够纯粹”，**FreeBSD** 社区则视 **OpenBSD** 为“许可证原教旨主义”；（2）**GPL** 阵营对 **BSD** 的批评与排外——**Richard Stallman** 与 **FSF** 长期将 **BSD** 许可证归类为“非 **copyleft** 自由许可证”但强调其“允许专有化”的“缺陷”，**FSF** 官方文档中对 **BSD** 许可证的描述带有警示色彩；**GPL** 社区在邮件列表（如 `lwn.net` 评论、`reddit r/linux`）长期嘲讽 **BSD**“为大公司免费打工”，“**BSD** 是 **Apple** 的免费午餐”；**Linux** 内核社区对 **BSD** 项目态度冷淡，**Linus Torvalds** 虽公开批评 **BSDL** 但极少参与 **BSD** 相关讨论；（3）**BSD** 项目的反向排外——**BSD** 社区在邮件列表（如 `freebsd-hackers`、`misc@openbsd`）对 **GPL** 持警惕态度，“**GPL** 是病毒”“**GPL** 是共产主义”等话语在 **BSD** 圈子长期存在；**OpenBSD** 邮件列表 `misc@openbsd` 对 **GPL** 相关讨论常以“这不是我们关心的问题”回应；**FreeBSD** 社区对 **GPL** 许可证的 ports 软件包持保留态度，优先收录 **BSD** 许可证的软件；（4）**Foundation** 对许可证问题的官方立场——**FreeBSD Foundation** 在许可证问题上持中立-温和态度，既支持 **BSD** 化工程但不强制要求所有组件 **BSD** 化，与 **OpenBSD Foundation**（实体为 **OpenBSD** 基金会）的激进立场形成对照；**Foundation** 对 **GPL** 社区的合作持开放但谨慎态度，避免与 **FSF** 正式结盟；（5）商业公司对许可证派系的影响——**Apple** 作为 **LLVM**/**Clang** 最大资助方，间接推动 **FreeBSD** 的 **BSD** 化，但 **Apple** 自身不参与 **BSD** 社区的许可证争论；**Juniper**、**Netflix** 等企业 **BSD** 用户对许可证问题持实用主义态度，不关心 **BSD** 化意识形态；**iXsystems** 在 **TrueNAS** 转向 **Linux** 后对 **FreeBSD** 许可证问题的态度趋于冷淡；（6）跨项目派系矛盾——**OpenBSD** 与 **FreeBSD** 在 **BSD** 化节奏上的分歧（**OpenBSD** 领先、**FreeBSD** 跟随）导致两社区之间存在“谁引领 **BSD** 化”的隐性竞争；**NetBSD** 因跨平台特性对许可证问题持最温和态度，被 **OpenBSD** 视为“不够坚定”、被 **FreeBSD** 视为“过于保守”；**DragonFlyBSD** 基本沿用 **FreeBSD** 的许可证策略，无独立立场；（7）许可证派系与邮件列表文化的交织——`freebsd-hackers` 邮件列表上 **BSD** 化讨论常引发“是否过度意识形态化”的争论，实用派与纯化派反复交锋；`misc@openbsd` 邮件列表对任何 **GPL** 相关讨论几乎零容忍，新用户提问 **GPL** 软件常被直接关闭；这种派系文化使 **BSD** 项目之间的技术交流（如共享代码、共同移植）受到许可证立场的过滤；｜ **子-子节**：68.32.1 纯化派与实用派的分歧；68.32.2 跨社区排外与反向排外；68.32.3 派系对立的哲学辨析；68.32.4 史料辨析；68.33 **与同时期操作系统的比较**：1989-2026 年同期 **Linux** **GPL** 许可证（**Linus Torvalds** 1991 年采用 **GPLv2**，2007 年拒绝 **GPLv3**）、**Apache 2.0** 许可证（2004 年 **Apache** 软件基金会发布，含专利授权条款）、**MIT** 许可证（更宽松，与 **BSD 2-Clause** 类似）、**Mozilla Public License 2.0**（2012 年，弱 **copyleft**）、**Microsoft** **MIT**/**Apache 2.0**（2014 年起 **Microsoft** 开源策略转变）——**BSD** 许可证是开源世界最宽松的许可证之一，其设计哲学与 **GPL** 形成最鲜明对照；**Linux** 内核始终使用 **GCC** 编译（虽拒绝 **GPLv3** 但接受 **GPLv2** **GCC**），与 **FreeBSD** 的 **GCC** → **Clang** 迁移形成对照；**OpenBSD** 是 **BSD** 化最激进的推行者（**LibreSSL**、`mandoc` 等），**NetBSD** 温和，**FreeBSD** 介于两者之间；｜ **子-子节**：68.33.1 各许可证文本对比；68.33.2 **BSD** 化策略的差异化；68.33.3 许可证哲学的比较辨析；68.33.4 史料辨析；68.34 **外部批评与反对者：GPL 阵营与 Copyleft 支持者**——**Richard Stallman** 与 **FSF** 对 **BSD** 许可证“允许专有化”的批评、**Linux** 社区对 **BSDL**“为大公司免费打工”的嘲讽、**GPLv3** 支持者对 **BSD** 化运动的质疑、阮一峰等中文社区对 **BSDL** 的批评；｜ **子-子节**：68.34.1 主要批评者与论点；68.34.2 批评对 **BSD** 社区的影响；68.34.3 批评的哲学辨析；68.34.4 史料辨析；68.35 **重要贡献者与边缘者：BSD 化工程的无名移植者**——**Dag-Erling Smørgrav**（**OpenPAM**）、**Tim Kientzle**（`libarchive`/`bsdtar`）、**Christos Zoulas**（`libedit`）、**Kristaps Dzonsons** 与 **Ingo Schwarze**（`mandoc`）、**David O'Brien**（**BSD** `sort` 重写）等 **BSD** 化工程的关键开发者；｜ **子-子节**：68.35.1 关键开发者与贡献；68.35.2 边缘者的历史影响；68.35.3 贡献者叙事的辨析；68.35.4 史料辨析；68.36 时代背景：1978-2026 总统科技政策、伯克利校园、IC、英美哲学、文化运动与社会运动、美苏争霸与冷战地缘、资本主义发展与经济危机、软件工程与编程语言标准、美国国防部投入、社会环境与舆论、气候与环境、密码学与信息安全——1978-2026 美国总统科技政策：**Carter**（1977-1981，Stevenson-Wydler Technology Innovation Act 1980.10.21、Bayh-Dole Act 1980.12.12 P.L. 96-517 允许联邦资助研究成果商业化）、**Reagan**（1981-1989，SDI 1983.3.23 战略防御倡议、Federal Technology Transfer Act 1986、商业放松管制）、**Bush 41**（1989-1993，HPCC 1991 高性能计算与通信法案、Gore NII 提议）、**Clinton**（1993-2001，NII/GII 1993、Telecom Act 1996.2.8、DMCA 1998.10.28、US v. Microsoft 1998.5.18）、**Bush 43**（2001-2009，USA PATRIOT Act 2001.10.26、Cybersecurity、2008 金融危机与 TARP 2008.10.3）、**Obama**（2009-2017，ARRA 2009.2.17、Open Internet Order 2015、Paris Agreement 2016）、**Trump** 第一任期（2017-2021，Tax Cuts and Jobs Act 2017、网络中立废除 2017、Operation Warp Speed 2020）、**Biden**（2021-2025，ARP 2021.3.11、IIJA 2021.11.15、CHIPS and Science Act 2022.8.9 P.L. 117-167 拨款 527 亿美元、IRA 2022.8.16、EO 14110 AI 2023.10.30）、**Trump** 第二任期（2025-，AI 政策调整）；1978-2026 伯克利校长谱系：**Bowker**（1971-1980，预算紧缩时期）、**Heyman**（1980-1990，第 6 任校长，10 年任期当时最长，民权与平权法案支持者）、**Tien**（1990-1997，第 7 任校长，首位亚裔美国人担任主要研究型大学校长，Proposition 209 1996.11.5 反平权法案冲击校园多元化，1990s 初期加州经济衰退导致 7000 万美元预算削减）、**Berdahl**（1997-2004，2000-2001 California electricity crisis 与 9/11 后加州财政紧缩）、**Birgeneau**（2004-2013，2008 金融危机应对、2009-2010 UC 预算危机与 32% 学费上涨）、**Dirks**（2013.6.1-2017.7.1）、**Christ**（2017.7.1-2024.6.28，首位女校长、COVID-19 应对）、**Lyons**（2024.7.1-，12th Chancellor，首位本科校友校长）；1978-2026 集成电路发展与 **BSD** 硬件平台演进：**VAX-11/780** 1977.10（**BSD** 原始平台，32V 1978 移植 Unix Version 7 到 **VAX**）、**Motorola 68000** 1979（16/32 位混合处理器，**Sun-1** 1982、**Sun-2** 1984 工作站，2BSD/4BSD 移植）、**Intel 8086** 1978/x86 体系（PC 革命，**386BSD** 1992.3.12 Jolitz 移植 4.3BSD-Reno 到 386）、**SPARC** 1987（**Sun-4**，4BSD 移植）、**PowerPC** 1991（**Apple**/**IBM**/**Motorola** 联盟，**PPC Mac OS X** 2001-2005）、**AMD K6** 1997/**Athlon** 1999.6/**Athlon 64** 2003.4 AMD64/x86-64 架构（**FreeBSD 5.1** 2003.6.9 新增 amd64）、**ARM** StrongARM 1995/Cortex-A8 2005/2007.6.29 iPhone ARM11、**ARMv8**/**AArch64** 2011 规范、**Apple A7** 2013 首个 64 位 **ARM** SoC、**AMD Zen** 2017 复兴、**RISC-V** 2010 规范发布、**Apple M1** 2020.11.10 ARM Mac 转型（5nm **TSMC**），**BSD** 硬件平台 **FreeBSD 1.0** 1993.11.3 386/x86、3.0 1998.10.16 Alpha、5.0 2003.1.19 sparc64 与 ia64、6.0 2005.11.1 powerpc、8.0 2009.11.25 MIPS、9.0 2012.1.12 powerpc64、11.0 2016.10.10 arm64/AArch64 Tier-2、12.0 2018.12.11 riscv64、13.0 2021.4.13 arm64 Tier-1、14.0 2023.11.20 弃用 MIPS 与 armv6，**BSD** 许可证哲学与硬件平台演进的关系——宽松许可证使 **BSD** 代码可被 **Apple**、**Sun**、**Juniper**、**Netflix** 等商业公司直接采用，推动 **BSD** 在多样化硬件平台上的商业部署；1978-2026 英美哲学历程：实证主义余响至后实证主义（**Popper** 证伪主义 1934/1963、**Lakatos** 研究纲领、**van Fraassen** 1980 建构经验主义）；实用主义复兴与新实用主义（**Quine** 1951、**Rorty** 1979《哲学与自然之镜》与 1989《偶然、反讽与团结》、**Putnam** 内在实在论、**Brandom** 1994 推论主义、**Misak** 副真主义）；分析哲学扩展（**Kripke** 可能世界语义学、**Lewis** 反事实条件句、**Davidson** 彻底解释、**Chomsky**/**Fodor** 心灵哲学、**Chalmers** 1996 意识难题）；科学哲学演进（**Kuhn** 1962→ **Lakatos** → **Feyerabend** → **Longino** → **Kitcher**）；结构主义至后现代主义弧线：结构主义兴起（**Levi-Strauss** 1958《结构人类学》）→ 后结构主义（**Foucault** 1975《规训与惩罚》、**Derrida** 1967《论文字学》）→ 解构主义美国化（耶鲁学派 de Man/Miller/Hartman 1970s-80s）→ 后现代主义高峰（**Lyotard** 1979《后现代状况》、**Jameson** 1991《后现代主义与文化逻辑》、**Sokal** 1996）→ 后现代主义退潮（**Hayles** 1999 后人类主义）→ 思辨实在论（**Meillassoux** 2006《有限性之后》、**Harman** 2002 客体导向哲学）→ 加速主义与去殖民哲学（**Fisher** 2009、**Mignolo**）；实验哲学兴起与成熟（**Knobe** 2003→ **Nichols** 2008→ 跨文化 X-phi）；横切商业生态视角：实证主义对工程验证文化塑造、实用主义与 **BSD** 做中学传统共鸣、分析哲学对形式化方法影响、结构主义对系统工程形式化影响、后现代主义对开源叙事建构批评、思辨实在论对 **AI** 本体论维度、去殖民哲学对 **BSD** 全球社区包容性反思；｜ **子-子节**：68.36.1 1978-2026 总统科技政策：**Carter** 至 **Trump** 第二任期；68.36.2 1978-2026 伯克利校长谱系：**Bowker** 至 **Lyons**；68.36.3 1978-2026 集成电路发展与 **BSD** 硬件平台演进：**VAX**、68k、x86、**ARM**、**RISC-V** ｜ **子-子-子节**：68.36.3.1 硬件厂商与半导体产业：1978-2026 主要厂商兴衰与产业格局变迁——**DEC**、**Sun**、**MIPS**、**Intel**、**AMD**、**ARM**、**RISC-V** 的商业与技术博弈；68.36.3.2 物理与芯片工艺：1978-2026 工艺节点从微米到 3nm 的演进、摩尔定律的经济极限与物理极限、半导体物理对计算性能的长期约束；68.36.3.3 操作系统与硬件的辩证关系：**BSD** 跨越四十年硬件变迁的抽象与适配——操作系统随硬件演进但不被硬件定义；68.36.4 1978-2026 英美哲学历程：结构主义至思辨实在论、实用主义与分析哲学；68.36.5 1978-2026 文化运动与社会运动：自由软件/开源运动的文化维度（**Stallman** 1983→ **Torvalds** 1991→OSA 1998→ 去中心化 2010s）、hacker 伦理演变（**Levy** 1984 四信条 → 开源实用主义 → 科技伦理反思）、数字权利运动（**EFF** 1990→DMCA 抗争 → **Snowden** 2013→ **GDPR** 2018→ **AI** 权利）、反全球化至占领华尔街（Seattle 1999→Occupy 2011）、LGBTQ+ 权利运动全程（Stonewall 1969→ACT UP 1980s→ 婚姻平等 2015→ 跨性别权利 2020s）、从嬉皮士到数字游民的文化变迁；｜ **子-子节**：68.36.6 1978-2026 美苏争霸与冷战地缘：从缓和到新冷战；68.36.7 1978-2026 资本主义发展与经济危机：里根经济学到量化宽松；68.36.8 1978-2026 软件工程与编程语言标准：C89 至 C23 全程；68.36.9 1978-2026 美国国防部投入：SAGE 到零信任；68.36.10 1978-2026 社会环境与舆论：hacker 妖魔化到 **AI** 伦理；68.36.11 1978-2026 气候与环境：环保到碳中和；68.36.13 1978-2026 基础科学与计算机科学发展：计算理论四十年对计算机工程的基础支撑 ｜ **子-子-子节**：68.36.13.1 基础科学：从图灵可计算性到量子计算——计算理论的四十年演进对计算机工程的基础支撑；68.36.13.2 计算机科学：从 Unix 哲学到云原生——CS 理论发展与 **BSD** 的全程互构：分时系统 → 网络协议 →SMP 并发 → 虚拟化 → 容器化 → 异构计算；68.36.13.3 基础科学、CS 与 **BSD** 的互构：**BSD** 作为 CS 理论的工程实验室——每一代 CS 理论突破均在 **BSD** 中找到工程回响；68.36.14 1978-2026 密码学、加密技术、数学原理与信息安全 ｜ **子-子-子节**：68.36.14.1 密码学与加密技术：从 **DES**（1977）至 **AES**（2001）至后量子密码（2024）的对称与公钥密码演化全程；从 **SSL**（1995）至 **TLS 1.3**（2018）至 **QUIC**（2021）的传输加密协议演进；**PGP**（1991）至 **Signal**（2013）的端到端加密范式变迁；加密出口管制从 **ITAR** 军需品管制至 2000 年放松至 **Wassenaar Arrangement** 的政策演变；68.36.14.2 数学原理：数论（模运算、大数分解、离散对数）支撑 **RSA**/**DH** 四十八年；椭圆曲线密码学从理论（1985）到标准化到后量子替代；计算复杂度理论从 NP 完全性到格密码 **LWE** 的范式转移；**Shor** 算法对经典公钥密码的量子威胁推动后量子密码数学基础建设；68.36.14.3 信息技术安全：从 **Morris** 蠕虫（1988）至 **SolarWinds** 供应链攻击（2020）至 **XZ utils** 后门（2024）的安全威胁演化；从 **CERT/CC**（1988）到零信任架构（2020）的安全范式转型；从 **Patriot Act**（2001）到 **GDPR**（2018）的隐私与监控法律框架演变；**BSD** 安全通告体系从 ad-hoc 到系统化的成熟；68.36.14.4 与 **BSD** 的关联：**OpenSSL**/`libcrypto` 在 **FreeBSD** 的长期集成与维护；**IPsec**/**WireGuard** 在 **FreeBSD** 的实现；`geli` 全盘加密、**jail(8)** 隔离、**Capsicum** 沙箱、**OpenBSM** 审计构成 **FreeBSD** 安全工具链；**FreeBSD** 在 **FIPS 140** 合规认证中的角色；**BSD** 安全哲学对开源安全实践的影响 | 许可证之争的深处是一个本体论问题——何为自由？证明世界先于改造世界，意味着必须先弄清“自由是什么”才能动手建构“自由的制度”；**BSD** 许可证条款本身就是形式主义化的法律建构，它以文本的形式将一种自由观固化为可执行的规则；而许可证作为形式主义化的商品形式，其交换价值早已脱离了代码的使用价值——**Apple** 取走 **BSD** 代码时支付的代价是零，这正是商品形式对使用价值的彻底脱离；**Foundation** 的治理结构则揭示了权力与知识的共谋：谁有权定义“自由”，谁就拥有了话语的制高点；从 **Carter** 到 **Trump** 第二任期的科技政策、从 **Bowker** 到 **Lyons** 的伯克利校园、从 **VAX** 到 **RISC-V** 的硬件演进、从实证主义到实验哲学的英美思想历程——四重维度共同塑造了 **BSD** 许可证哲学演变的思想土壤 |

**要点**：本节核心：68.17 **GCC → Clang/LLVM：最大的 BSD 化工程**——**GCC** 自 1987 年由 **Richard Stallman** 创建以来一直是 **GNU** 项目的核心编译器，**GPLv2** 许可证，2007 年 **GPLv3** 升级引发 **BSD** 社区（据本节正文提炼）
**史料**：本节史料基础：2012.1；2014.1；GNU 工具；`ld`（据本节文献表/引用整理）
- 史观：和解优于斗争：商业生态中的 BSD 与 GPL 不应是对立，而是不同形式主义路径的并置
**辨析**：本节辨析的核心张力在于“本节核心：68.17 **GCC → Clang/LLVM：最大的 BSD 化工程**——**GCC** 自 1987 年由 **Richard Stallma”所述内容的边界条件：其史料基础与史观立场须交叉验证，防止单一来源叙事预设（据本节要点整理）
- 文献：[DB:historical_claims] 历史主张数据库（853 条主张，26,898 条证据）

