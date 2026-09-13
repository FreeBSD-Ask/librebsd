---
chapter: 第 248 章
id: CH248
volume: 第12卷-macos的bsd遗产
---

# 第 248 章 macos-1012-1015从sierra到catalina

## 要点

- Apple 于 **2016 年 6 月 13 日** 在 WWDC 2016 公布 **APFS**（Apple File System），**2017 年 3 月 27 日** 随 iOS 10.3 首次部署于 iOS 设备，**2017 年 9 月 25 日** 随 macOS 10.13 High Sierra 部署于 Mac（作为可选文件系统，**2018 年 9 月 24 日** ma
- 此期 Darwin 开源仍经 **APSL 2.0 许可证**（**2003 年 8 月 6 日** 起），独立开发者贡献网络与安全补丁。freebsd.duckdb 查询显示 **2016-2019 年** 间 freebsd-src 仓库中 message_subject 含“From Apple”/“From Darwin”的 commit 数量较低（延续 2010 年后的“低密度回馈”特征
- **2016-2019 年** macOS 10.12-10.15 对比 **FreeBSD 11.x**（**2016 年 10 月 10 日** 发布）/**12.x**（**2018 年 12 月 11 日** 发布）、**Linux 4.x**（2016-2019 年）、**Windows 10**（2015-2019 年），其 APFS 与 64 位纯净化在文件系统与架构演进上各有侧重。
- BSD 社区针对 2016-2019 年（macOS 10.12 Sierra 至 10.15 Catalina）Apple 与 FreeBSD 之间代码交流的批评可归纳为三点。其一，**apple.com 邮箱 commit 在 2016-2019 年间为零**——freebsd.duckdb 查询 2-3 显示，freebsd-src 仓库中 author_email 含 apple.com
- Apple 阵营对“2016-2019 年零回馈”批评的回应可归纳为三条路径。其一，**BSDL 契约即允许零回馈**——BSD 许可证明文允许“with or without modification”的商业使用与闭源发行，“允许不回馈”是 BSDL 的哲学选择，“零回馈”是此哲学选择在 2016-2019 年间的极端显现；要求 Apple 在 BSDL 契约之外“主动”提供回馈，是将法律契约与

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4127] 卷“第12卷-macos的bsd遗产”第 248 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4128] 卷“第12卷-macos的bsd遗产”第 248 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

<!-- 整改留痕 2026-09-13：核查报告 P2 指出上方 chmatch_4127/4128 系机械检索引用直接呈现为史料、主题无关，建议删或改人工史料；机器自动块处置属 DEFERRED 枚举，登记待主代理专项处置，本次不改。 -->

## 史观

<!-- 整改留痕 2026-09-13：按核查报告 P1 回填史观占位，映射 25 条总纲权威表（依据本章要点与辨析字段）。 -->
- 总纲 3“不存在进步，只有权力再分配”——“2016-2019 年零回馈”争议的实质不是技术进步与否，而是商业权力对代码流动方向的再分配：Apple 以自有仓库（GitHub 509 仓库）与 Darwin 发布机制主导回馈节奏，FreeBSD 社区的“批评”是对这一权力结构的叙事回应。
- 总纲 13“法律与道德是利益分配”——BSDL 契约明文允许“with or without modification”的商业使用与闭源发行，“零回馈”在法律上成立；社区互惠期待属道德层面，二者分属利益分配的不同维度，不得以道德义务倒推法律责任，亦不得以法律许可否认互惠伦理的批评空间。
- 总纲 8“本体论上各方平等”——APFS 与 ZFS 分别针对固态存储与池化存储优化，闭源与开源、自研与派生在本书叙事中地位相等：设计目标不同不构成优劣序列，“APFS 落后/先进于 ZFS”的二元判断均不成立。

## 辨析

- APFS 是否“基于”BSD FFS/UFS——经 Darwin 源码仓库比对，APFS 是 Apple 自研文件系统，其代码结构与 BSD FFS/UFS 无直接派生关系。APFS 与 ZFS 均支持 Copy-on-Write 与快照，但 APFS 的设计针对固态存储（SSD/NVMe）优化，ZFS 针对池化存储（storage pool）优化。采信“APFS 是 Apple 自研，与 BSD
- 2016-2019 年间 Apple 与 FreeBSD 的代码交流是否“双向”——darwin.duckdb 显示 FreeBSD 端的 Apple 相关 commit 以硬件支持为主（FreeBSD→Apple 硬件适配），而 Apple→FreeBSD 的用户空间代码回馈较少。采信“此期代码交流以 FreeBSD 适配 Apple 硬件为主，Apple 向 FreeBSD 回馈用户空间代码
- APFS 与 ZFS 的设计哲学差异须客观论述——APFS 针对固态存储优化（SSD/NVMe），ZFS 针对池化存储优化（storage pool）；APFS 是闭源，ZFS 是开源（CDDL）。此差异不意味着优劣，而是不同的设计目标。采信“APFS 与 ZFS 是不同设计目标的文件系统，非优劣关系”的判断。
- 批评层的量化依据须明确数据库覆盖盲区——freebsd.duckdb 仅含 freebsd-src 等仓库的 commit，不含 Darwin/XNU 仓库的 commit，故“零回馈”是“FreeBSD 端可观察的零回馈”，非“Apple 端实际回馈的零”。Apple 可能在 Darwin 仓库中接受了 FreeBSD 提交者的 pull request，但此部分不在 bsd_commits.d
- Apple 阵营的回应须按 0 信任原则考据——“许可证设计意图”论点虽逻辑自洽，但 BSDL 创始者的“意图”本身是事后诠释，须谨慎对待；“509 个开源仓库”是事实但多数为 Apple 自有项目的源码发布，并非向 FreeBSD 的主动回馈；“Catalina 64 位纯净化推动 FreeBSD”属叙事建构而非因果事实。APFS 自研的合理性论点须厘清——APFS 针对 SSD/NVMe 优化

## 文献

- Apple Inc. Apple File System Guide [EB/OL]. (2017-03-27). Apple Developer Documentation; Apple Inc. WWDC 2016 Session: Apple File System [EB/OL]. (2016-06-13). Apple Developer.

<!-- 整改留痕 2026-09-13：核查报告 P1/P2 指出 DB_REF 机器块重复（1985-2026 年 2,012 次提交块 ×2，与仓库总览 2,016 混用）及文末 FreeBSD 社区论文五条串烧（仅 FP-2008-003 与本章相关）；机器自动块重复与错挂属 DEFERRED 枚举，登记待主代理专项处置，本次不改；报告所指行内 DB_REF 双箭头格式损坏现文已修为独立块（VERIFIED）。 -->

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2016-2017 年间：157 次提交。> 仓库总览：2,016 次提交，42 个 Apple 开源镜像仓库（contributors 表 43 行），2001-04-10 至 2026-04-13。
- darwin.duckdb 查询结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22; Apple Open Source. Darwin Source Releases [EB/OL]. <https://opensource.apple.com/releases/>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2018-2019 年间：154 次提交。> 仓库总览：2,016 次提交，42 个 Apple 开源镜像仓库（contributors 表 43 行），2001-04-10 至 2026-04-13。
- FreeBSD Project. FreeBSD 11.0/12.0 Release Notes [EB/OL]. (2016-10-10, 2018-12-11). <https://www.freebsd.org/releases/>; Linux Kernel Archives. Linux 4.0-4.20 Release Notes [EB/OL]. (2015-2019). <https://www.kernel.org/>; Microsoft. Windows 10 File Systems Documentation [EB/OL]. <https://docs.microsoft.com/en-us/windows-server/storage/file-systems/>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，42 个 Apple 开源镜像仓库（contributors 表 43 行），2001-04-10 至 2026-04-13。
- darwin.duckdb 查询 1-3 结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22; Apple Inc. Apple File System Guide [EB/OL]. (2017-03-27). Apple Developer Documentation; Apple OSS Distributions [EB/OL]. <https://github.com/apple-oss-distributions>, 2026-07-22 核查。## 248.4.2 反批评层：Apple 阵营对“零回馈”指控的回应
- BSD License Text [EB/OL]. <https://opensource.org/license/bsd-3-clause>, 2026-07-22; Apple OSS Distributions [EB/OL]. <https://github.com/apple-oss-distributions>, 2026-07-22; Apple Inc. libdispatch Repository [EB/OL]. <https://github.com/apple/swift-corelibs-libdispatch>; Apple Inc. macOS 10.15 Catalina Release Notes [EB/OL]. (2019-10-07). Apple Developer.## 248.4.3 再批评层：BSD 阵营对 Apple 回应的再反驳
- 项目统摄史观·经济历史哲学 [EB/OL]. 原材料/哲学/项目统摄史观/第 08 章.md; 项目统摄史观·总纲 [EB/OL]. 原材料/哲学/项目统摄史观/第 25 章.md; darwin.duckdb 查询 1-3 结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22; Apple Inc. Apple File System Guide [EB/OL]. (2017-03-27). Apple Developer Documentation.

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2016-2019 年间：184,913 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数），1993-06-12 至 2026-08-25。
- BSD License Text [EB/OL]. **<https://opensource.org/license/bsd-3-clause>**, 2026-07-24; Apple Inc. Apple Public Source License 2.0 [EB/OL]. **<https://opensource.apple.com/apsl/>**, 2026-07-24; FSF. FSF's Opinion of the Apple Public Source License (APSL) 2.0 [EB/OL]. **<https://www.gnu.org/philosophy/apsl.html>**; Apple OSS Distributions [EB/OL]. **<https://github.com/apple-oss-distributions>**, 2026-07-24; Apple Inc. macOS 10.15 Catalina Release Notes [EB/OL]. (2019-10-07). Apple Developer; Apple Inc. Apple File System Guide [EB/OL]. (2017-03-27). Apple Developer Documentation; FreeBSD Project. Platforms [EB/OL]. **<https://www.freebsd.org/platforms/>**, 2026-07-24; 项目统摄史观·总纲 [EB/OL]. 原材料/哲学/项目统摄史观/第 25 章.md; darwin.duckdb 查询 1-3 结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22.FreeBSD 社区论文：[FP-2019-075] By the numbers: ZFS Performance Results from Six Operating Systems and Their Derivatives（Michael Dexter（迈克尔·德克斯特），2019）<https://papers.freebsd.org/2019/vbsdcon/dexter-zfs_performance_results/>FreeBSD 社区论文：[FP-2019-081] OpenZFS: Best Filesystem for every OS（Allan Jude（艾伦·裘德），2019）<https://papers.freebsd.org/2019/jude-openzfs-everyos/>FreeBSD 社区论文：[FP-2018-034] The Tragedy of systemd（Benno Rice（本诺·赖斯），2018）<https://papers.freebsd.org/2018/bsdcan/rice-the_tragedy_of_systemd/>FreeBSD 社区论文：[FP-2017-008] CloudABI for FreeBSD（Ed Schouten，2017）<https://papers.freebsd.org/2017/fosdem/ed-cloudabi-for-freebsd/>FreeBSD 社区论文：[FP-2008-003] Mac OS X - From the server room to your pocket（Jordan K. Hubbard（乔丹·哈伯德），2008）<https://papers.freebsd.org/2008/lisa08/hubbard-macosx_from_the_server_room_to_your_pocket/>

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，42 个 Apple 开源镜像仓库（contributors 表 43 行），2001-04-10 至 2026-04-13。
