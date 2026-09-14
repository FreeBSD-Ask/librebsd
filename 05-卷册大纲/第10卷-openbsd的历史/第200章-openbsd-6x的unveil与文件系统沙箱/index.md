---
chapter: 第 200 章
id: CH200
volume: 第10卷-openbsd的历史
---

# 第 200 章 openbsd-6x的unveil与文件系统沙箱

## 要点

- OpenBSD 6.0-6.9 的 Release Notes 与 openbsd.duckdb commit log 是研究此时期工程进展的核心史料；特性引入时间以 Release Notes 与 commit log 交叉验证为准——Release Notes 记录用户可见变更，commit log 记录具体代码变更
- RETGUARD 的辩证合图——RETGUARD 既是 OpenBSD 编译时安全机制的核心（反批评层）也具有性能开销与覆盖范围局限（批评层与再批评层），二者并非非此即彼；RETGUARD 在 OpenBSD 的安全优先哲学下具有工程合理性（per-function 随机 canary 防护 ROP、编译器自动插入可采用性高、与 KARL 配合形成编译时与运行时双重防护）〔待核：原文截断，后文待回源〕
- OpenBSD Foundation 的年报与财务记录是研究其治理结构的核心史料；资金流向以年报、邮件列表、加拿大政府非营利组织报告交叉验证为准；年报详细记录捐赠、支出、hackathons 资助
- 6.x 时期多元群体贡献的史料局限——openbsd.duckdb 提交元数据丢失机构/国别信号（邮箱域 100% 为 openbsd.org），且 contributors 表仅覆盖提交者；须以邮件列表、Foundation 年报与访谈多源交叉，遵循 0 信任原则
- OpenBSD 6.4（2018-10-25 发布）引入 RETGUARD 返回地址保护机制——在每个函数 prologue/epilogue 中插入随机 canary，防止 ROP（Return-Oriented Programming）攻击；RETGUARD 由 Todd Mortimer（托德·莫蒂默） 设计实现（openbsd.duckdb 显示 2018-06-06 mortimer c

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3899] 卷“第10卷-openbsd的历史”第 200 章，匹配置信度 folder，原因：folder 第198章
- [DB:bsdnow_podcast:outline_mappings:om_11748] BSD Now 第 494 期，匹配 CH200 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11794] BSD Now 第 488 期，匹配 CH200 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12397] BSD Now 第 427 期，匹配 CH200 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12510] BSD Now 第 419 期，匹配 CH200 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12619] BSD Now 第 404 期，匹配 CH200 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12654] BSD Now 第 395 期，匹配 CH200 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- Release Notes 的完整性以 plus.html 页面为准——该页面仅记录“重要的和用户可见的变更”，部分内部代码重构可能未记录；commit log 中的 xenocara/SMP/vmm 相关 commit 须通过文件路径（如 xenocara/、sys/kern/、sys/dev/pv/）筛选方可定位
- M CFI 的可能整合）须重新展开；【0 信任原则·合图的非折中主义】合图不是“RETGUARD 在 OpenBSD 内合理、在高性能场景下不合理”的简单分类，而是揭示“安全加固”与“性能可用性”的张力——OpenBSD 以性能代价换取安全加固是结构性选择而非道德缺陷，但这一选择的生态代价（市场份额低）
- 年报的完整性以 OpenBSD Foundation 官方网站为准——年报逐年发布，部分细节可能未公开；财务记录的审计情况以加拿大政府非营利组织报告为准
- 非提交贡献者（文档、ports、翻译）的记录缺口以 OpenBSD 邮件列表与 hackathons 报告为补充来源 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- RETGUARD 与 LLVM CFI、Microsoft CFG 的对比以各自设计文档为准——三者设计目标与覆盖范围不同，RETGUARD 以 per-function 随机 canary 防护返回地址，LLVM CFI 以控制流完整性图防护间接调用，Microsoft CFG 以目标地址验证防护间接调用；RETGUARD 的性能开销以 OpenBSD tech@ 邮件列表讨论为准 [考据完成：

## 文献

- OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；openbsd.duckdb openbsd-src 仓库；OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/> ［B］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2016-2019 年间：73,060 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- RETGUARD 与 LLVM CFI/Microsoft CFG 综合对比研究；OpenBSD 6.4 Release Notes [EB/OL]. <https://www.openbsd.org/64.html>；openbsd.duckdb openbsd-src 仓库 RETGUARD 相关 commit；编译时安全机制演进史 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2013-2026 年间：248,174 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD Foundation 年报 [EB/OL]. <https://www.openbsdfoundation.org/>；加拿大政府报告；Foundation 官方文档 ［B］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2013-2026 年间：248,174 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- openbsd.duckdb openbsd-src 仓库；OpenBSD 提交/文档/ports 贡献记录；OpenBSD 邮件列表存档 [EB/OL]. <https://marc.info/?laccopenbsd-misc> ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- openbsd.duckdb openbsd-src 仓库 commit e688c2b0648a；OpenBSD 6.4 Release Notes [EB/OL]. <https://www.openbsd.org/64.html>；Mortimer 邮件列表发言 [EB/OL]. <https://marc.info/?laccopenbsd-tech>；LLVM CFI 文档 [EB/OL]. <https://clang.llvm.org/docs/ControlFlowIntegrity.html>；Microsoft CFG 文档 [EB/OL]. <https://learn.microsoft.com/en-us/windows/win32/secbgctrl/control-flow-guard> ［A］---

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2016-2019 年间：73,060 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP270（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- OpenBSD 6.4 发布，引入 unveil 系统调用以限制文件系统访问，VMM 增加 QCOW2 磁盘与快照支持，并新增 RETGUARD 返回地址保护与多项 Spectre 缓解。（BSD Now EP270，[66.06-184.52]，L2）
- MeetBSD 2018 在 Intel 圣克拉拉总部举行，首次设立独立程序委员会并公开征稿，穿插闪电演讲与分组讨论，最终以 FreeBSD 25 周年庆典收尾。（BSD Now EP270，[775.34-883.66]，L1）
- Michael Dexter 的回顾称 MeetBSD 结合正式演讲与非会议活动，大型礼堂的弹性空间促成多次即兴黑客聚会，把“走廊轨道”推向新高度。（BSD Now EP270，[1475.34-1519.30]，L2）
- Bjorn Zeeb 提交 IETF draft 6man IPv6-only 标志的初始实现，使 FreeBSD 路由器可宣告链路仅支持 IPv6，并在接口层过滤 IPv4 与 ARP 帧。（BSD Now EP270，[2217.54-2447.32]，L2）

**史料**：

- MeetBSD 2018 演讲清单：Chris Moore 的 TrueOS 引导、Kirk McKusick 的“BSD 早年”互动演讲、Michael W. Lucas 的“YBSD”主题演讲、OpenZFS 专家座谈与虚拟化专题讨论。（BSD Now EP270，[993.86-1367.26]，L1）
- OpenSSH 7.9 随 OpenBSD 6.4 发布：CA 签名算法选项禁止以 DSA 作为证书机构、认证日志格式加入证书指纹，并新增按 SHA-256 哈希撤销密钥的能力。（BSD Now EP270，[577.30-750.34]，L2）

**史观**：

- 总纲18 时间是一种形式主义：FreeBSD 二十五周年被庆典化呈现，但与会者强调“二十五年才能成为二十五年项目”无法抄近路，项目年龄本身就是时间累积的形式。（BSD Now EP270，[1443.38-1475.34]，L1）
- 总纲10 动手者创造历史：unveil 与 RETGUARD 延续 OpenBSD 以安全机制逐步收紧运行边界的方向，主持人将其视为对既有代码进行持续加固而非另起炉灶。（BSD Now EP270，[175.16-247.24]，L2）

**辨析**：

- 本期对 OpenBSD 6.4 特性的转述与章节考据的发布时间（2018-10-25）一致，但 unveil 与 RETGUARD 的提交细节须以 OpenBSD commit log 与 Release Notes 交叉核实。（BSD Now EP270，[175.16-212.76]，L3）

**文献**：

- [BSD Now EP270] Pennington J. BSD Now: Episode 270: Ghostly Releases | BSD Now 270[EB/OL]. (2018-11-01)[2026-08-15]. <https://www.bsdnow.tv/270>.

<!-- /PODCAST_REVIEW -->
