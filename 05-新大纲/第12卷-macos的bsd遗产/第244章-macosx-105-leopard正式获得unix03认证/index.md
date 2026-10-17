---
chapter: 第 244 章
id: CH244
volume: 第12卷-macos的bsd遗产
---

# 第 244 章 Mac OS X 10.5 Leopard 正式获得 UNIX 03 认证

## 要点

- **Mac OS X 10.5 Leopard** 于 **2007 年 10 月 26 日** 发布，是首个通过 **The Open Group UNIX 03** 认证的 Apple 操作系统。认证基于 **Single UNIX Specification v3（SUSv3）**，覆盖 Leopard 的 BSD/POSIX 用户空间——包括 `libc`、`pthread`、`socket`、文件系统接口、shell 工具（`sh`、`bash`、`csh`）等 POSIX 合规性。
- **macOS** 因 Apple 付费并通过 The Open Group 测试套件而 **持有 UNIX 03 证书**；**FreeBSD** 虽实际遵守 POSIX（FreeBSD 5.0 起持续通过 POSIX 合规测试），但 **从未申请 UNIX 03 认证**（成本与社区意愿——认证费用约 10 万美元以上，且 FreeBSD 项目无商业实体承担此费用）。
- **Mac OS X 10.5 Leopard**（**2007 年 10 月 26 日**发布）引入 **BSM（Basic Security Module）审计框架**，源自 **TrustedBSD 项目**的 **OpenBSM** 子项目——OpenBSM 由 **Robert N. M. Watson（罗伯特·N·M·沃森）** 主导开发，TrustedBSD 官方主页 **trustedbsd.net** 明确列 **Apple Computer, Inc.** 为赞助商之一。
- **2007 年** Leopard 对比 **FreeBSD 7.0**（**2008 年 2 月 27 日** 发布）、**Linux 2.6.23**（**2007 年 10 月 9 日** 发布）、**Solaris 10**（**2005 年 1 月 31 日** 发布，已获 **UNIX 03**）、**Windows Vista**（**2006 年 11 月 30 日** 发布），其 UNIX 03 认证在桌面 OS 中独一无二。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4067] 卷“第12卷-macos的bsd遗产”第 244 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

总纲映射（汇总 244.1-244.4 子节史观字段）：总纲第 2 条（历史是形式主义化的非存在）——UNIX 03 认证是“形式”的获取（法律身份），macOS 的 POSIX 实质合规在认证前已存在，形式与内容分离；总纲第 10 条（动手者创造历史）——Robert Watson（OpenBSM）与 Bryan Cantrill 等（DTrace）BSD 谱系工程师的贡献经反向流动进入 macOS，其姓名在 Apple 主线叙事中被遮蔽；总纲第 4 条（分离聚合是永恒规律）——OpenBSM 从 TrustedBSD 聚合入 FreeBSD 与 macOS，DTrace 自 OpenSolaris 分离至 Darwin 与 FreeBSD，BSD 谱系技术跨系统流动；总纲第 6 条（和解优于斗争）——Leopard、FreeBSD、Linux、Solaris 与 Windows 共享 POSIX/Unix 哲学根基却发展出不同合规主体性（持证、实质遵守不持证、不适用）；总纲第 25 条（逻辑是形式主义而非世界本身的结构）——UNIX 03 认证作为形式化的合规契约，是“持证 vs 实质遵守”法律区分的规则化显现。

## 辨析

- UNIX 03 认证针对 Leopard 的具体构建（含 Darwin 9.x 版本），后续 macOS 版本须各自维持认证或重新认证——Darwin 9.x（对应 Leopard）通过认证不代表 Darwin 10.x（对应 Snow Leopard）自动通过，Apple 须为每个 macOS 版本单独申请认证。认证范围限于用户空间 POSIX 接口，不含内核 Mach 层——Mach 微内核不属 POSIX 规范范围，故认证不覆盖 Mach。
- 不得将 macOS 的 UNIX 03 认证误用于论证 FreeBSD 也 “是 UNIX 认证系统”——macOS 持证，FreeBSD 不持证，二者法律状态明确不同。FreeBSD 可称 “遵守 POSIX” 但不可称 “通过 UNIX 03 认证”。采信 “macOS 持证、FreeBSD 不持证，二者 POSIX 实质合规相近但法律状态不同” 的判断。
- macOS BSM 审计与 FreeBSD OpenBSM 共享上游源码但实现细节有差异——macOS BSM 与 Apple 私有安全机制（如 `sandbox_init`）协同，FreeBSD OpenBSM 与 Capsicum 协同；macOS BSM 审计日志路径为 **/var/audit/**，FreeBSD OpenBSM 审计日志路径亦为 **/var/audit/**，二者格式兼容
- 认证带来合规优势但市场份额仍不及 Windows——2007 年 macOS 市场份额约 5%，Windows 约 90%，认证未直接带来市场份额提升。避免 “UNIX 03 认证使 macOS 成功” 的简化归因——采信 “UNIX 03 认证带来开发者认可与合规优势，但市场份额提升源于硬件生态与品牌战略” 的判断。

## 文献

- The Open Group. UNIX 03 Registered Products [EB/OL]. <https://www.opengroup.org/openbrand/register/>; Apple Inc. Mac OS X 10.5 Leopard Release Notes [EB/OL]. (2007-10-26). Apple Developer.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。
> 2007-2007 年间：70 次提交。
<!-- /DB_REF -->
- The Open Group. UNIX 03 Certification Process [EB/OL]. <https://www.opengroup.org/certification/programs/unix>; FreeBSD Project. FreeBSD POSIX Compliance [EB/OL]. <https://docs.freebsd.org/en/books/porters-handbook/standards/>.

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1985-2026 年间：1,294,851 次提交。
<!-- /DB_REF -->
- TrustedBSD Project. *TrustedBSD Home Page*[EB/OL]. <http://www.trustedbsd.net/>; Apple Inc. *Mac OS X 10.5 Leopard Release Notes*[EB/OL]. (2007-10-26). Apple Developer; Watson, R. N. M. (2003). *TrustedBSD: Adding Trusted Operating System Features to FreeBSD*. USENIX Annual Technical Conference 2003, FREENIX Track.

<!-- DB_REF:darwin.duckdb -->
> **数据库引用（darwin.duckdb）**：本子节对应 darwin 代码仓库。
> 2007-2007 年间：70 次提交。
<!-- /DB_REF -->
