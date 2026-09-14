---
chapter: 第 196 章
id: CH196
volume: 第10卷-openbsd的历史
---

# 第 196 章 openbsd-3x的持续安全改进

## 要点

- FreeBSD 社区质疑 OpenBSD“硬件支持不足”——OpenBSD 因代码审计需求对新硬件支持保守；部分厂商文档要求 NDA，OpenBSD 拒绝 NDA 导致支持滞后；OpenBSD 在 1996-2004 年间硬件支持广度不及 FreeBSD 与 Linux
- 外部批评的原始发言散见于 Linux 邮件列表、Slashdot、OSNews、Bugtraq、Full Disclosure 等；考据需对照原始帖的发布时间、作者、上下文；部分“批评”可能是误解或基于过时信息
- 1996-2004 年间 OpenBSD 主要贡献者的 commit 记录与邮件列表讨论是研究社区动态的核心史料；除 de Raadt、Provos、Keromytis、Hartmeier、Beck 外，还包括 Todd C. Miller（托德·C·米勒）、Deraadt、Markus Friedl（马库斯·弗里德尔）、Jason Ishmael 等；考据需对照 CVS commit log 与
- OpenBSD 3.1（2002.5）引入 W^X（Write XOR Execute）内存保护机制，由 Niels Provos（尼尔斯·普罗沃斯） 主导，利用 i386 与 amd64 的 NX bit 等硬件特性使栈与堆内存不可执行；OpenBSD 3.3（2003.5）引入 stack protector（ProPolice/SSP），由 Hiroaki Etoh 与 IBM Tokyo
- 1996-2004 年间市场份额数据——Linux 服务器市场占有率从约 5% 升至约 20%，FreeBSD 约 2%-3%，NetBSD 不足 0.5%，OpenBSD 不足 0.5%；Solaris 从约 30% 降至约 15%；BSD 整体被 Linux 挤压但 OpenBSD 在安全场景保持存在

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4098] 卷“第10卷-openbsd的历史”第 196 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4099] 卷“第10卷-openbsd的历史”第 196 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充
- [DB:references_fulltext:chapter_matches:chmatch_4100] 卷“第10卷-openbsd的历史”第 196 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- OpenBSD 拒绝 NDA 的具体案例需考据——部分资料称 OpenBSD 完全拒绝，部分称有例外；硬件支持不足的具体硬件类别需对照硬件兼容性列表核验
- 批评发言的代表性需考据——单一用户的抱怨不等于社区共识；【0 信任原则·comp.unix.bsd 与 LKML 考据】2026-07-30 经 Google Groups advanced search 检索 comp.unix.bsd（**<https://groups.google.com/g/comp.unix.bsd>**）以“OpenBSD”为关键词，返回 11 条 1997-2004
- 主要贡献者的具体 commit 数量在不同统计工具中差异较大；邮件列表署名与 CVS author 字段可能不完全对应【代码级证据·openbsd.duckdb openbsd-src 仓库】author_name 维度 commit 计数（全仓库，非 3.x 时期限定）：provos（Niels Provos）834、angelos（Angelos Keromytis）〔待核：原文截断，后文待回源〕
- OpenBSD W^X 与 Linux PaX、FreeBSD exec shield 的关系需考据——PaX 项目更早但未集成至 Linux 主线；i386 不支持 NX bit 的硬件（如 Pentium III）的兼容性需考据；SSP 的具体实现细节（canary 类型、函数选择）在不同来源中存在差异，需对照源码核验；SSP 的性能开销在不同工作负载上差异较大
- OpenBSD 在防火墙场景的部署（如 pfSense 早期基于 m0n0wall）未被服务器市场报告统计；市场份额数据在不同调查中差异较大

## 文献

- OpenBSD 邮件列表；de Raadt 演讲；硬件兼容性列表 ［A］
- Linux 邮件列表；Slashdot/OpenBSD；Bugtraq/Full Disclosure；Google Groups comp.unix.bsd 存档（**<https://groups.google.com/g/comp.unix.bsd>**）— 11 条 1997-2004 年 OpenBSD 相关帖 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD CVS 仓库统计；邮件列表存档；BSDCan/AsiaBSDCon 演讲视频档案 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 3.1/3.3 Release Notes；Provos W^X 文档；ProPolice 文档；IBM Tokyo Research Lab 论文；PaX 项目文档 ［B］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2001-2004 年间：67,797 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- Netcraft Web Server Survey 1996-2004；IDC 服务器操作系统市场报告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1996-2004 年间：593,615 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- openbsd.duckdb openbsd-src 仓库；OpenBSD 3.x errata patches [EB/OL]. **<https://www.openbsd.org/errata.html**>；MIT Kerberos 安全公告；zlib 安全公告 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2001-2006 年间：103,490 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md（总纲第 13、19、21 条原文）；OpenBSD security.html [EB/OL]. **<https://www.openbsd.org/security/**>；OpenBSD 3.0-3.6 Release Notes [EB/OL].** <https://www.openbsd.org/plus.html**>；FreeBSD 5.x Release Notes [EB/OL]. **<https://www.freebsd.org/releases/**>；Linux 2.6 内核 changelog [EB/OL].** <https://www.kernel.org/**>；NSA SELinux 项目文档；FreeBSD TrustedBSD 项目文档；openbsd.duckdb openbsd-src 与 freebsd-src 仓库 commits 表 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 官网 release 页面；OpenBSD 邮件列表存档；OpenBSD CD 销售海报存档 ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
