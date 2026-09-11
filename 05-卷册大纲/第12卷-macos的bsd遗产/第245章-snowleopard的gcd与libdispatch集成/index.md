---
chapter: 第 245 章
id: CH245
volume: 第12卷-macos的bsd遗产
---

# 第 245 章 snowleopard的gcd与libdispatch集成

## 要点

- libdispatch 开源后，FreeBSD 社区启动移植工作。freebsd.duckdb 查询显示，freebsd-src 仓库 message_subject 含 `libdispatch` 关键词返回 **0 条** commit；`GCD`/`Grand Central` 关键词查询返回 **24 条** commit，但均为 `.gcda` 文件依赖关系、`linuxkpi` gcd 函数、
- libdispatch 开源后形成独立社区，贡献者包括 Apple 工程师（如 **Doug Davidson**、**Dave Zmikly**，libdispatch 的核心开发者）与外部贡献者。FreeBSD 社区开发者 **Stanislav Sedov**（<stas@FreeBSD.org>）于 **2009-09-23T15:02:29Z** 在 freebsd-ports 仓库提交
- **2009 年** Snow Leopard 对比 **FreeBSD 8.0**（**2009 年 11 月 25 日** 发布）、**Linux 2.6.30**（**2009 年 6 月 9 日** 发布）、**Windows 7**（**2009 年 10 月 22 日** 发布），其 GCD 并发模型领先同期桌面 OS。FreeBSD 8.0 的并发模型以 `pthread` 与 `k
- 自由软件阵营与部分 BSD 社区成员对 Apple 将 libdispatch 开源持批判态度，认为此系“消费式开源”（consumer-style open source）的典型——Apple 长期从 FreeBSD 用户空间吸收代码（如 libc、网络栈、用户空间工具）却仅以 Apache 2.0 选择性回馈个别小型库（libdispatch），回馈规模与吸收规模严重不对称。freebsd.d
- BSD 阵营与 Apple 工程师对“消费式开源”批判提出反驳，认为 libdispatch 的开源是 Apple 对 BSD 社区的实质性回馈，不应被简单定性为“消费式”。其一，许可证选择本身的诚意——Apple 选择 Apache 2.0（而非 APSL 2.0）开源 libdispatch，主动放弃了 APSL 的“通报义务”与“终止权”条款，使 FreeBSD 可无障碍移植，此许可证选择与

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4125] 卷“第12卷-macos的bsd遗产”第 245 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4126] 卷“第12卷-macos的bsd遗产”第 245 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- [2026-08-15 双库核查] Snow Leopard GCD/libdispatch 引入（2009 年）经参考文献库 “Mac OS X 10.6 Snow Leopard - libdispatch/GCD debut”（Apple Inc., 2009）记录印证；libdispatch 以 Apache 2.0 开源经参考文献库 Swift corelibs-libdispatch
- libdispatch 的 FreeBSD 移植是否 “回馈” 了 Apple——libdispatch 开源后 FreeBSD 移植是 Apple→FreeBSD 的代码流动，FreeBSD 移植者未直接向 Apple 回馈代码，但移植过程中发现的 bug 通过 libdispatch 仓库的 issue tracker 反馈至 Apple。采信 “FreeBSD 移植是 Apple→FreeB
- Snow Leopard 的 “无新功能” 定位是否意味着 BSD 层无变化——BSD 层在 Snow Leopard 中有显著变化：64 位用户空间默认化、GCD 引入、PowerPC 移除、性能优化。此变化在用户可见层面较少（“无新功能” 指用户可见功能），但在 BSD 子系统层面变化显著。采信 “Snow Leopard 用户可见功能少但 BSD 子系统变化显著” 的判断。
- libdispatch 随 Swift 开源是否改变了其许可证——libdispatch 始终保持 Apache 2.0 许可证（2009 年开源时即为 Apache 2.0，2015 年随 Swift 开源时仍为 Apache 2.0），未改为 Swift 的 Apache 2.0 with Swift exceptions。采信“libdispatch 许可证始终为 Apache 2.0，未随
- GCD 与 FreeBSD 的并发演进存在间接影响——libdispatch 开源后 FreeBSD 移植使 FreeBSD 用户得以使用 GCD 的任务队列抽象，但 FreeBSD 内核的并发模型未因此改变（仍以 `pthread` 与 `kqueue`/`kevent` 为基础）。采信 “GCD 通过 libdispatch 移植间接影响 FreeBSD 用户空间并发工具，但未改变 FreeB

## 文献

- Apple Inc. Mac OS X 10.6 Snow Leopard Release Notes [EB/OL]. (2009-08-28). Apple Developer; Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>; 统计结论 [C-03] 结果 [EB/OL]. 描述性统计.md SubTask 2.1, 2026-07-22; 统计结论 [C-41] 结果 [EB/OL]. 文献计量学分析.md Task 22, 2026-07-22.## 244.1.2 libdispatch 的 FreeBSD 移植与 freebsd.duckdb 证据
- freebsd.duckdb freebsd-src 仓库 commits 表（libdispatch 关键词 0 条，GCD/Grand Central 关键词 24 条均非 GCD 本体）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，首条 2009-09-23 Sedov commit_hash `fdd841f9197f1910059414771324205d30d93a2a`）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 von Appen 972 commits 中 0 条 libdispatch 相关 [DB/OL]. script/query_ch113_von_appen_libdispatch.py, 2026-07-23；FreeBSD Ports. devel/libdispatch [EB/OL]. <https://www.freshports.org/devel/libdispatch/>；Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2009-2009 年间：89 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>; Apple Inc. Swift Open Source [EB/OL]. (2015-12-03). <https://www.swift.org/>; freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，首条 2009-09-23 Sedov commit_hash `fdd841f9197f1910059414771324205d30d93a2a`）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23; freebsd.duckdb freebsd-ports 仓库 von Appen 972 commits 中 0 条 libdispatch 相关 [DB/OL]. script/query_ch113_von_appen_libdispatch.py, 2026-07-23; FreeBSD Ports. devel/libdispatch [EB/OL]. <https://www.freshports.org/devel/libdispatch/>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2009-2009 年间：89 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- FreeBSD Project. FreeBSD 8.0 Release Notes [EB/OL]. (2009-11-25). <https://www.freebsd.org/releases/>; Linux Kernel Archives. Linux 2.6.30 Release Notes [EB/OL]. (2009-06-09). <https://www.kernel.org/>; Microsoft. Windows 7 Launch [EB/OL]. (2009-10-22). Microsoft Press Release.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- freebsd.duckdb freebsd-src 仓库 commits 表（2009-2015 年 commit 量；libdispatch 关键词 0 条，GCD/Grand Central 关键词 24 条均非 GCD 本体）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；freebsd.duckdb freebsd-ports 仓库 commits 表（libdispatch 13 条，2009-2014 年间仅 2 条）[DB/OL]. script/query_ch113_libdispatch_commits.py, 2026-07-23；Apple Inc. libdispatch Source Code [EB/OL]. (2009-09-10). <https://github.com/apple/swift-corelibs-libdispatch>；Apple Inc. Swift Open Source [EB/OL]. (2015-12-03). <https://www.swift.org/>；Free Software Foundation. FSF's Opinion of the APSL 2.0 [EB/OL]. <https://www.gnu.org/philosophy/apsl.html> ［A］## 244.4.4 合图层——不对称互惠的 libdispatch 流动史合图
