---
chapter: 第 247 章
id: CH247
volume: 第12卷-macos的bsd遗产
---

# 第 247 章 osx-107-1011从lion到elcapitan

## 要点

- **OS X 10.8 Mountain Lion**（**2012 年 7 月 25 日** 发布）引入 **Gatekeeper**——代码签名机制，限制未签名应用运行。Gatekeeper 提供“**Mac App Store**”、“**Identified Developers**”、“**Anywhere**”三档安全级别（默认为“Identified Developers”，仅允许签
- 此期 Darwin 同步吸收 FreeBSD 网络栈与安全相关补丁，独立开发者经 APSL 2.0 流程贡献。freebsd.duckdb 查询显示，**David Chisnall** 于 **2011 年 11 月 20 日** 在 freebsd-src 仓库提交“Implement xlocale APIs from Darwin, mainly for use by libc++”——此
- **2011-2015 年** OS X 10.7-10.11 对比 **FreeBSD 9.x**（**2012 年 1 月 12 日** 发布）/**10.x**（**2014 年 1 月 14 日** 发布）、**Linux 3.x**（2011-2015 年）、**Windows 8**（**2012 年 10 月 26 日** 发布）/**8.1**（**2013 年 10 月 17 日**
- BSD 社区针对 2011-2015 年（OS X 10.7 Lion 至 10.11 El Capitan）Apple 与 FreeBSD 之间桥梁贡献的批评可归纳为三点。其一，**桥梁贡献者数量稀疏**——darwin.duckdb 查询显示，此期横跨 FreeBSD 与 Apple 两个社区的桥梁贡献者仅 **David Chisnall** 与 **Pedro F. Giffuni**
- Apple 阵营对“桥梁贡献稀疏”批评的回应可归纳为三条路径。其一，**BSDL 设计意图即允许稀疏**——BSD 许可证明文允许“with or without modification”的商业使用与闭源发行，“允许不回馈”是 BSDL 的哲学选择而非 Apple 的剥削，桥梁贡献的稀疏恰是 BSDL 创始者有意授予的自由在 2011-2015 年间的自然显现；要求 Apple 在 BSDL 契

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4054] 卷“第12卷-macos的bsd遗产”第 247 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Gatekeeper 是否修改了 BSD 内核——经 Darwin 源码仓库比对，Gatekeeper 的签名验证在用户态守护进程 `amfid` 中实现，但通过 BSD 层的 `execve` 钩子触发。BSD 内核的 `execve` 接口本身未修改，但增加了签名验证的调用路径。采信“Gatekeeper 在用户态实现签名验证，但通过 BSD 层的 `execve` 钩子触发”的判断。
- David Chisnall 的 xlocale 移植是否“回馈”了 Apple——xlocale API 源自 Darwin，David Chisnall 将其移植至 FreeBSD，此为 Darwin→FreeBSD 的代码流动（非 FreeBSD→Darwin）。Apple 未直接从此次移植中获益，但 FreeBSD 的 xlocale 实现与 Darwin 保持接口兼容，间接促进了跨平台应
- SIP 与 Linux 的只读根（immutable root）设计理念相似但实现路径不同——Linux 的只读根（如 Fedora Silverblue 的 `/usr` 只读）在文件系统层实现，SIP 在内核的 MAC 框架层实现。采信“SIP 与 Linux 只读根理念相似但实现路径不同”的判断。
- 批评层的量化依据须明确数据库覆盖盲区——freebsd.duckdb 仅含 freebsd-src 等仓库的 commit，不含 Darwin/XNU 仓库的 commit，故“桥梁贡献稀疏”是“FreeBSD 端可观察的稀疏”，非“Apple 端实际回馈的稀疏”。Apple 可能在 Darwin 仓库中接受了 FreeBSD 提交者的 pull request，但此部分不在 bsd_commit
- Apple 阵营的回应须按 0 信任原则考据——“许可证设计意图”论点虽逻辑自洽，但 BSDL 创始者的“意图”本身是事后诠释，须谨慎对待；“509 个开源仓库”是事实但多数为 Apple 自有项目的源码发布，并非向 FreeBSD 的主动回馈；“LLVM/Clang 投入惠及 FreeBSD”属间接路径，Apple 赞助 LLVM 的首要动机是摆脱 GCC 对 Apple 工具链的约束，Free

## 文献

- Apple Inc. OS X 10.8 Mountain Lion Security Overview [Z]. Apple Developer Documentation, 2012; Apple Inc. WWDC 2012 Session: Gatekeeper [EB/OL]. (2012-06-11). Apple Developer.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2011-2012 年间：171 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- freebsd.duckdb 查询结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22; Chisnall D. FreeBSD-src commit: Implement xlocale APIs from Darwin [EB/OL]. (2011-11-20). freebsd.duckdb, freebsd-src repo; Apple Open Source. Darwin Source Releases [EB/OL]. <https://opensource.apple.com/releases/>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 2013-2015 年间：208 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- FreeBSD Project. FreeBSD 9.0/10.0 Release Notes [EB/OL]. (2012-01-12, 2014-01-14). <https://www.freebsd.org/releases/>; Linux Kernel Archives. Linux 3.0-3.19 Release Notes [EB/OL]. (2011-2015). <https://www.kernel.org/>; Microsoft. Windows 8/8.1/10 Security Features [EB/OL]. <https://docs.microsoft.com/en-us/windows/security/>.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- darwin.duckdb 查询 1-3 结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22; Apple OSS Distributions [EB/OL]. <https://github.com/apple-oss-distributions>, 2026-07-22 核查; Apple Open Source. Darwin Source Releases [EB/OL]. <https://opensource.apple.com/releases/>, 2026-07-22 核查。## 246.4.2 反批评层：Apple 阵营对“桥梁稀疏”指控的回应
- BSD License Text [EB/OL]. <https://opensource.org/license/bsd-3-clause>, 2026-07-22; Apple OSS Distributions [EB/OL]. <https://github.com/apple-oss-distributions>, 2026-07-22; Apple Inc. libdispatch Repository [EB/OL]. <https://github.com/apple/swift-corelibs-libdispatch>; darwin.duckdb 查询 5 结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22.## 246.4.3 再批评层：BSD 阵营对 Apple 回应的再反驳
- darwin.duckdb 查询 1 结果（David Chisnall 37 条 Apple 相关 commit、Pedro F. Giffuni 21 条 Apple 相关 commit 的子系统分布）；darwin.duckdb 查询 5 结果（Jordan Hubbard 7,101 条 commit，1993-06-18 至 2004-11-14）；Apple OSS Distributions [EB/OL]. <https://github.com/apple-oss-distributions>, 2026-07-22; Apple Open Source. Darwin Source Releases [EB/OL]. <https://opensource.apple.com/releases/>, 2026-07-22.## 246.4.4 合图层：商品形式主义下的桥梁稀疏
- 项目统摄史观·经济历史哲学 [EB/OL]. 原材料/哲学/项目统摄史观/第 08 章.md; 项目统摄史观·总纲 [EB/OL]. 原材料/哲学/项目统摄史观/第 25 章.md; darwin.duckdb 查询 1 与查询 5 结果 [EB/OL]. script/vol9_ch118_apple_darwin_commits.py, 2026-07-22.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。> 1985-2026 年间：2,012 次提交。> 仓库总览：2,016 次提交，时间跨度 2001-04-10 至 2026-04-13；contributors 表 43 行（42 个镜像仓库 + 1 行 dependabot，全部经 Apple OSS Distributions 自动化账号导入）。
- Apple Inc. Darwin 8.0.1 Release Notes [EB/OL]. (2005-04-29). <https://opensource.apple.com/static/iso/release-notes-8.0.1.txt>; OpenDarwin Core Team. OpenDarwin Shutting Down [EB/OL]. (2006-07-25). <https://web.archive.org/web/20060804104416/http://opendarwin.org/>; PureDarwin Project. Binary Drivers required for PureDarwin [EB/OL]. (2009-07-20). <https://web.archive.org/web/20091118172944/http://www.puredarwin.org/legal/binarydrivers>; PureDarwin Project. Release: PD-17.4 Test Build [EB/OL]. (2018-07-01). <https://www.puredarwin.org/news/PD17-4-released.html>.## 246.6.2 反批评层：Apple 阵营对 Darwin 开源完整性批评的回应
- PureDarwin Project. Binary Drivers required for PureDarwin [EB/OL]. (2009-07-20). <https://web.archive.org/web/20091118172944/http://www.puredarwin.org/legal/binarydrivers>; Free Software Foundation. FSF's Opinion of the APSL 2.0 [EB/OL]. <https://web.archive.org/web/20200504151500/http://www.gnu.org/philosophy/apsl.html>; Apple OSS Distributions [EB/OL]. <https://github.com/apple-oss-distributions>, 2026-07-24.## 246.6.4 合图层：许可证哲学与商品形式主义下的 Darwin 开源
