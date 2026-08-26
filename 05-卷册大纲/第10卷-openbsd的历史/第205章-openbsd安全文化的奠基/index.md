---
chapter: 第 205 章
id: CH205
volume: 第10卷-openbsd的历史
---

# 第 205 章 openbsd安全文化的奠基

## 要点

- OpenBSD 代码审计方法论由 de Raadt 主导自 1996 年 fork 后逐步建立，核心实践为逐行审查基本系统源码，重点关注缓冲区溢出与格式化字符串漏洞、信任边界与权限提升；审计流程为发现问题 → 修复 →commit log 详细记录 →security advisory；OpenBSD Security Advisories 自 1996 年起在 <www.openbsd.org/
- OpenBSD “默认安全”（secure by default）原则体现在默认关闭非必要服务（如默认不启用 telnetd、ftpd）、默认启用加密（如 SSH 默认开启）、默认最小权限等多方面；该原则自 1996 年 fork 之初即确立；防火墙方面，ipf（Darren Reed（达伦·里德） 的 IP Filter）自 OpenBSD fork 前即存在于 NetBSD 代码库中（open
- OpenBSD 1996-2000 年间通过代码审计发现并修复大量安全漏洞，包括缓冲区溢出（如 ftpd、telnetd 远程溢出）、格式化字符串漏洞（如 wu-ftpd Format String Vulnerability CVE-2000-0573，2000-06 披露）、信任边界问题；部分漏洞在审计前已被利用（如 1999 年 BIND NXT 漏洞 CVE-1999-0833），部分是审
- OpenBSD 审计成果通过 cross-BSD 协调（vendor branch 同步）反馈至 FreeBSD/NetBSD，部分修复被 Linux 发行版移植；OpenBSD 提出的 **strlcpy(3)**/**strlcat(3)**（1998-07-01 millert commit 1dc0268a4106 "add strlcpy/strlcat, safe and sensib
- FreeBSD 1990 年代后期建立 Security Officer 制度（如 Warner Losh（沃纳·洛什）、Kris Kennaway 等任职）但未系统性代码审计，安全修复以反应式（收到报告后修复）为主；Linux 1990 年代缺乏系统性审计，依赖用户与厂商报告，1999 年 Linux Security Audit Project 由 Daniel Stone 等发起但规模有限；

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3778] 卷“第10卷-openbsd的历史”第 205 章，匹配置信度 folder，原因：folder 第203章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 审计方法论在不同叙事中存在差异——部分资料强调 “逐行审查”（de Raadt 在 misc@ 邮件列表多次提及 "audit every line"），部分强调 “分类审查”（按漏洞类型如 buffer overflow、format string、integer overflow 分类扫描），二者非互斥而是互补——逐行审查是方法论基础，分类审查是针对特定漏洞类型的专项扫描；审计范围限定为基本系
- ipf 与 pf 的替代关系——ipf 自 1996 年 fork 前即存在于 NetBSD 代码库，OpenBSD 继承使用至 2.9（2001-05）；2001 年 Darren Reed 修改 ipf 许可证引发争议，OpenBSD 于 2001-06-24 引入 pf（commit 148b55c022b1）作为 ipf 兼容替代品，pf 随 OpenBSD 3.0（2001-12-01）
- “数千个漏洞” 的具体数字——OpenBSD Security Advisories 页面（<https://www.openbsd.org/security.html>）逐条记录了 1996 年至今的 advisory，1996-2000 年间的 advisory 可直接在该页面计数；advisory 数量与实际修复的漏洞数量非一一对应——一条 advisory 可能修复多个相关漏洞，一个漏洞的
- strlcpy/strlcat 引入时间——bsd_commits.db 显示 millert 于 1998-07-01 commit 1dc0268a4106 引入 strlcpy.c/strlcat.c/strlcpy.3，部分二手资料误记为 1996 年，实际引入时间为 1998-07-01；strlcpy/strlcat 被 glibc 采纳的过程曲折——glibc 维护者 Ulrich 
- 三者安全实践的 “严格程度” 对比缺乏权威量化评估——OpenBSD Security Advisories 与 FreeBSD Security Advisories 的 advisory 数量可通过各自页面计数，但 advisory 数量受多个因素影响（审计范围、披露政策、版本发布频率等），不能直接作为安全质量排名依据；“反应式安全” 与 “主动审计” 的界定——OpenBSD 自 1996 

## 文献

- OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html>；OpenBSD **security(8)** 手册页 [EB/OL]. <https://man.openbsd.org/security.8>；OpenBSD **afterboot(8)** 手册页 [EB/OL]. <https://man.openbsd.org/afterboot.8>；OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；openbsd.db 查询 L3.1.1.audit（来源：原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.1.1，数据缺口） ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD **afterboot(8)** 手册页 [EB/OL]. <https://man.openbsd.org/afterboot.8>；OpenBSD commit 148b55c022b1 [G/OL]. <https://github.com/openbsd/src/commit/148b55c022b1>；OpenBSD misc@ 邮件列表存档 [EB/OL]. <https://marc.info/?l=openbsd-misc> ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- FreeBSD Security Advisories [EB/OL]. <https://www.freebsd.org/security/advisories/>；NetBSD Security Advisories [EB/OL]. <https://www.netbsd.org/support/security/>；OpenBSD **strlcpy(3)** 手册页 [EB/OL]. <https://man.openbsd.org/strlcpy.3>；OpenBSD commit 1dc0268a4106 [G/OL]. <https://github.com/openbsd/src/commit/1dc0268a4106>；Linux Security Audit Project [EB/OL]. <https://www.linux.org.au/lsec/> ［A］**OpenBSD 安全 API 扩散时间线**：| API | OpenBSD 引入时间 | commit hash | 采纳系统 || --- | --- | --- | --- || **strlcpy(3)**/**strlcat(3)** | 1998-07-01 | `1dc0268a4106` | FreeBSD、NetBSD、glibc（2019 年 2.30）、macOS libc || **arc4random(3)** | 1996-12 | `af7d239111f9` | FreeBSD、NetBSD、macOS、Linux libbsd |<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- FreeBSD Security Advisories 1996-2000 [EB/OL]. <https://www.freebsd.org/security/advisories/>；Linux Security Audit Project [EB/OL]. <https://www.linux.org.au/lsec/>；OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html> ［A］**OpenBSD/FreeBSD/Linux 1990 年代安全实践对比**：| 维度 | OpenBSD | FreeBSD | Linux || --- | --- | --- | --- || 安全模型 | 主动逐行审计 | Security Officer 制度（反应式） | 各发行版各自为政（反应式） || 审计范围 | 基本系统（src/ 与 sys/） | 无系统性审计 | 1999 年 Linux Security Audit Project（规模有限） || 关键人物 | de Raadt、Brauer、millert 等 | Warner Losh、Kris Kennaway 等 | Daniel Stone 等 || 安全发现来源 | 内生于审计流程 | 外生于用户报告 | 外生于用户与厂商报告 || 跨项目扩散 | strlcpy/strlcat、arc4random、OpenSSH | Security Advisories 标注 OpenBSD fix | 各发行版各自打包修复 |<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1995-2026 年间：1,289,123 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html>；BUGTRAQ 邮件列表存档 [EB/OL]. <https://seclists.org/bugtraq/>；外部基准报告：外部基准-StackOverflow-PackageEcosystem.md 第 3.2 节 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\外部基准-StackOverflow-PackageEcosystem.md` ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/><!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
