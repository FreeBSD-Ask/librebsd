---
chapter: 第 201 章
id: CH201
volume: 第10卷-openbsd的历史
---

# 第 201 章 openbsd-6x的安全机制综合演进

## 要点

- 2017-2021 应用沙箱：OpenBSD 6.x 的 pledge/unveil 以极简声明引领，FreeBSD Capsicum 以能力句柄深入，Linux seccomp 以 BPF 灵活，Windows AppContainer 与 macOS Sandbox 闭源/半开源；OpenBSD 6.x 的极简沙箱影响行业（如部分思路入 Linux）  **2017-2021 同期应用沙箱机制
- 6.x 周期是 OpenBSD“主动审计—快速修复—加固重构”循环的形成期——**主动审计** 体现于 6.0 errata 中 8 月 3 日单日发布 029-039 共 11 个 patch（含 9 个 SECURITY FIX），反映一次系统性的内核安全审计；**快速修复** 体现于 Spectre v2 披露后 14 天内提交修复 commit（kettenis `d855ec95cfe6
- 从项目史观总纲第 5 条“没有必然性，只有偶然性”与总纲第 13 条“法律与道德是利益分配”审视，LibreSSL fork 与 RETGUARD 皆非“安全必然性”的产物，亦非纯粹的工程道德选择，而是偶然事件与利益分配的交汇。总纲第 5 条指出，每一次 fork、每一个技术决定都是不可替代的偶然——Heartbleed 于 2014 年 4 月 7 日披露是偶然事件，OpenBSD 团队当日即由
- OpenBSD 6.2（2017-10-09）引入 **unveil(2)** 系统调用用于文件系统路径访问限制——unveil(2) 允许进程在启动时声明所需访问的文件系统路径（如 `unveil("/var/www", "r")`），内核据此限制进程的文件系统访问范围，未声明的路径对进程不可见；unveil(2) 与 5.9 引入的 **pledge(2)** 共同构成“进程权限 + 文件路径

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3900] 卷“第10卷-openbsd的历史”第 201 章，匹配置信度 folder，原因：folder 第199章
- [DB:references_fulltext:chapter_matches:chmatch_4015] 卷“第10卷-openbsd的历史”第 201 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 沙箱“简洁 vs 灵活”是设计权衡——pledge 的采用门槛最低（一行 `pledge()` 调用），seccomp 的表达力最强（BPF 过滤器可定义任意系统调用过滤规则），Capsicum 的粒度最细（能力句柄可绑定至单个文件描述符）
- *须精确说明 6.0 errata 8 月 3 日单日 11 个 patch 的性质**：029_sigio（RELIABILITY）、030_sendsyslog（RELIABILITY）、031_fuse（SECURITY）、032_recv（SECURITY）、033_tcp_usrreq（SECURITY）、034_sockaddr（SECURITY）、035_ptrace（SECURIT
- 考据过程留痕——【查证来源】总纲第 5 条与第 13 条原文经 据原文第 25 章 一手核验，第 5 条明确“每一次 fork、每一个技术决定，都是不可替代的偶然”，第 13 条明确“任何道德问题本质上是利益问题”；LibreSSL fork 的 commit 时间线经 bsd_commits.db openbsd-src 仓库 commits 表一手核验（djm `af0b15b8442f` 2
- unveil(2) 引入的考据须遵循 0 信任原则——【查证来源】（1）OpenBSD 6.2 release 页面（<https://www.openbsd.org/62.html>）经 2026-07-23 检索，记载发布日期 2017-10-09 与 unveil(2) 引入；（2）**unveil(2)** 手册页记载 unveil(2) 系统调用的设计与约束机制；（3）bsd_commi

## 文献

- OpenBSD 6.x Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；各系统沙箱文档 ［B］---<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD Project. OpenBSD 6.0 Errata [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata60.html>; OpenBSD Project. OpenBSD 6.4 Errata [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata64.html>; OpenBSD Project. pledge(2) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/pledge.2>; OpenBSD Project. unveil(2) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/unveil.2>; OpenBSD Project. syspatch(8) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/syspatch.8>; OpenBSD Project. signify(1) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/signify.1>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. [2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. bsd_commits.db — openbsd-src 6.x security commits [DB/OL]. 2026-07-22. SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name ='openbsd-src' AND author_date >='2016-09-01' AND author_date <‘2019-10-01’ AND (message_subject LIKE '%CVE-%’ OR message_body LIKE '%CVE-%’ OR message_subject LIKE '%security%’ OR message_subject LIKE '%spectre%’ OR message_subject LIKE '%meltdown%’) ORDER BY author_date ASC ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 项目史观总纲第 5 条、第 13 条。见：据原文第 25 章；项目史观总纲第 5 章偶然性论述。见：据原文第 5 章；bsd_commits.db openbsd-src 仓库 LibreSSL/RETGUARD 相关 commit（af0b15b8442f、b6553af36068、e688c2b0648a）；LibreSSL 官方公告 [EB/OL]. <https://www.libressl.org/>；OpenSSL Apache 许可证文本；LibreSSL ISC 许可证文本 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 6.2 release 页面 ［EB/OL］. <https://www.openbsd.org/62.html>；**unveil(2)** 手册页；OpenBSD 邮件列表存档；undeadly.org 报道；原材料/研究/考据记录/20260723_announcements-openbsd.md § 二.4.3；bsd_commits.db openbsd-src 仓库 ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/><!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
