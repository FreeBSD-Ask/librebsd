---
chapter: 第 194 章
id: CH194
volume: 第10卷-openbsd的历史
---

# 第 194 章 openbsd-2x的安全机制早期演进

## 要点

- OpenBSD 2.x 时期的多元群体贡献史料存在两块局限——（1）提交元数据因 @openbsd.org 统一账号而丢失机构/国别信号，须依赖邮件列表与访谈补救；（2）“贡献”定义须扩展到代码之外——文档（jmc 等）、安全审计（tb 等）、端口（ports）与翻译同样来自多元志愿者；任何群体画像均须遵循 0 信任原则，避免由姓名推断身份。
- OpenBSD 自 2.x 时代起使用 Darren Reed（达伦·里德） 的 IPFilter（IPF）作为防火墙；IPF 在 OpenBSD 2.6-2.9（1999-2001）时期作为基本系统组件部署；此时期 OpenBSD 团队对 IPF 的许可证与维护模式已有不满，但尚未 fork；〔待核：原文截断，后文待回源〕
- 2000-2004 安全文化分野：OpenBSD 2.x 以集中代码审计建立“安全优先”标杆，FreeBSD 4.x/NetBSD 1.x 在工程/可移植中兼顾，Linux 2.4 靠社区响应，Windows 闭源响应；OpenBSD 2.x 的审计文化成为 BSD 家族乃至行业的安全范式源头。
- OpenBSD 2.6-2.9 时期的加密栈与安全工具漏洞标志着“安全操作系统”自身安全组件的信任危机——2.6 的 `sslUSA26` 软件包（美国版 SSL 库）在 **isakmpd(8)** 中启用 SSL/RSA 特性时可被利用，errata 建议使用国际版 `sslUSA26` 替代（1999-12-02）；〔待核：原文截断，后文待回源〕
- 总纲第 13 条“法律与道德是利益分配”指出“任何道德问题本质上是利益问题，社区治理亦是形式主义的政治产物”。OpenSSH fork 争议表面上是“软件自由 vs 商业可持续性”的道德论辩，本质上是利益分配的政治产物——（1）Ylönen 阵营的利益结构：Ylönen 数年开发 SSH 的投入需要商业回报维持，SSH Communications Security 的商业模式依赖 SSH 许可证

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4012] 卷“第10卷-openbsd的历史”第 194 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4028] 卷“第10卷-openbsd的历史”第 194 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 本库 contributors 表仅覆盖提交者，未覆盖文档/ports/翻译等非提交贡献者，故“多元群体”的全貌需补充非提交贡献记录；相关缺口标注 据 Mockus-et-al (2002) 一手文献印证消解^doubt-resolved-870：此处事实待多源交叉验证 ］。
- OpenBSD 2.x 时期对 IPF 的具体不满程度在不同叙事中存在差异——部分资料称 de Raadt 早期已计划 fork，部分称 fork 是 2001 年许可证变更后的被动反应，需对照 1999-2001 年 <misc@openbsd.org> 邮件列表存档核验；IPF 在 OpenBSD 2.x 时期的实际部署规模缺乏权威统计
- 安全文化非“优劣”线性——OpenBSD 2.x 的极端审计适合其目标，其他系统有不同权衡。
- `sslUSA26` 的美国版与国际版具体差异须考据——涉及 RSA 专利与美国出口管制；`USER_LDT` 漏洞的具体利用路径（LDT 操纵如何访问内核内存）须对照 i386 架构手册核验；**rm(1)** 竞态条件与 fts 库漏洞的关联须考据 fts 库 commit 历史
- 利益分配审视的辨析须以三段式呈现——【查证来源】（1）原材料/哲学/项目统摄史观/第 25 章.md 总纲第 13 条原文经 2026-07-23 一手核验，确认“任何道德问题本质上是利益问题，社区治理亦是形式主义的政治产物”措辞原文存在；（2）OpenSSH 官方历史页面（<https://www.openssh.com/history.html>）经 2026-07-23 WebFetch 一

## 文献

- OpenBSD 提交/文档/ports 贡献记录；0 信任原则方法论 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 2.6-2.9 Release Notes；IPFilter 早期 LICENSE 文件；OpenBSD 邮件列表存档 ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-011] A Deep Dive into FreeBSD's Kernel RNG（W. Dean Freeman and John-Mark Gurney，2017）<https://papers.freebsd.org/2017/vbsdcon/gurney-a_deep_dive_into_freebsds_kernel_rng/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>### 史观映射> OpenBSD 2.x 时代是“修道者以物度人”在安全领域的极致呈现——de Raadt 带领团队逐行审计代码，发现并修复数千个漏洞，OpenSSH 从这个审计过程中诞生，如今守护着全球数亿台服务器；pf 因 IPFilter 许可证变更而 fork，是“许可证即形式主义的产物”在工程层面的具体体现——当许可证的形式主义约束改变，代码的形式主义结构也随之重组；“默认安装仅两个远程漏洞”的口号是 OpenBSD 安全叙事的形式主义化——它将“安全”量化为一个可计数的指标，但批评者指出这种计数本身依赖于严格定义，形式主义的量化反而遮蔽了安全的复杂性；44.5 **OpenBSD SMP 演进史（1996-2004）**——OpenBSD 早期 SMP 支持的缺失：2.x 时代几乎无 SMP 支持；OpenBSD 3.x 时代的 SMP 实验：big-lock 模型、性能瓶颈；与 FreeBSD SMPng（5.x 时代细粒度锁）的对比：OpenBSD 长期滞后；SMP 不足对 OpenBSD 服务器市场的影响：难以进入企业服务器领域；de Raadt 对 SMP 的态度：安全优先于性能 ｜ **子-子节**：44.5.1 OpenBSD 2.x 时代 SMP 支持的缺失；44.5.2 OpenBSD 3.x 时代的 SMP 实验与 big-lock 模型；44.5.3 与 FreeBSD SMPng 的对比及长期滞后；44.5.4 SMP 不足对服务器市场的影响及 de Raadt 的态度；44.6 **OpenSSH 商业化与 OpenBSD 未获益的讽刺**——OpenSSH 的全球部署规模：数亿台服务器、几乎所有 Unix-like 系统；商业公司从 OpenSSH 获利：Cisco、Apple、IBM、Red Hat 等；OpenBSD 项目未获商业回报：BSD 许可证允许但不要求回馈；OpenSSH 维护成本由 OpenBSD 项目承担，商业公司“搭便车”；开源许可证与商业回报的张力：BSD 许可证的“自由”代价 ｜ **子-子节**：44.6.1 OpenSSH 的全球部署规模与商业公司获利；44.6.2 OpenBSD 项目未获商业回报的现状；44.6.3 OpenSSH 维护成本与商业公司“搭便车”现象；44.6.4 开源许可证与商业回报的张力及 BSD 许可证的“自由”代价 | OpenBSD 2.x-3.x 时代体现了项目统摄史观中“修道度人”与“形式主义化”的双重运作：代码审计是“以物度人”的工程实践（通过修复漏洞度化用户），OpenSSH 与 pf 的诞生是“形式主义化”的产物（从 SSH 与 IPFilter 中抽象出新的形式主义结构）；“两个远程漏洞”口号的争议则揭示了形式主义化的认识论困境——量化指标既是真实的（确实只有两个），又是虚假的（依赖于严格定义）

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2001 年间：63,666 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD. Security Practices (2000-2004)[EB/OL]；BSD 安全文化史料。［B］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2000-2004 年间：81,488 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 2.6-2.9 errata patches [EB/OL]. **<https://www.openbsd.org/errata.html**>；openbsd.duckdb openbsd-src 仓库；i386 LDT 架构手册 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1996-2001 年间：63,666 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- 原材料/哲学/项目统摄史观/第 25 章.md 总纲第 13 条；OpenSSH 项目历史 ［EB/OL］. <https://www.openssh.com/history.html>；SSH Communications Security 商业产品 ［EB/OL］. <https://www.ssh.com/>；84.3.3 节记录；84.5.1-84.5.2 节记录；openbsd.duckdb openbsd-src commit 84959968510b、bf74e864c129、76c6bcb9f8b9、d9d42abc7ed4、84174f65ff52、348a6efc411d；comp.security.ssh Usenet 1999-2000 存档；OpenBSD misc@ 邮件列表 1999-2000 存档 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 官网 3.0 release 页面 ［EB/OL］. <https://www.openbsd.org/30.html>；OpenBSD 邮件列表存档；OpenBSD Jumpstart 项目介绍 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD Project. *OpenBSD 2.0 Release Notes*[EB/OL]. (1996-10-18). <https://www.openbsd.org/>; OpenBSD Project. *ktrace(1) Manual Page*[EB/OL]. <https://man.openbsd.org/ktrace.1>; Provos, N. (2002). *Improving Host Security with System Call Policies*. USENIX Security 2002.

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
