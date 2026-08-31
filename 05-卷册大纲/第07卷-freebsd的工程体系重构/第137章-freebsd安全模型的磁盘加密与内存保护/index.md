---
chapter: 第 137 章
id: CH137
volume: 第07卷-freebsd的工程体系重构
---

# 第 137 章 freebsd安全模型的磁盘加密与内存保护

## 要点

- GBDE/GELI/**random(4)** 的一手史料包括：**gbde(8)**/**geli(8)**/**random(4)** 手册页的 HISTORY 和 IMPLEMENTATION NOTES 节；Kamp 2003 USENIX GBDE 论文；FreeBSD 各版本 Release Notes（6.0 GELI、13.0 Fortuna 等）；src/sys/geom/bde
- FreeBSD VuXML（Vulnerability XML）是 FreeBSD Ports Collection 的软件漏洞数据库，记录 ports 中第三方软件的已知安全漏洞；VuXML 由 Jacques Vidrine 等人于 2003 年前后建立 [存疑精确建立年份]，以 XML 格式存储在 ports 树的 **security/vuxml** 中；每个 VuXML 条目包含：受影响
- FreeBSD 安全事件的一手史料主要来源：FreeBSD-SA/EN 公告存档（security.freebsd.org）——最权威的官方记录；freebsd-security@ 和 freebsd-announce@ 邮件列表存档——包含讨论和补充信息；CVE/NVD 数据库条目——标准化漏洞信息；第三方安全公司公告（Qualys、ISS X-Force、Google Project Zero
- FreeBSD 与 macOS/Windows 安全模型对比及关键认证澄清：(1) macOS——Apple macOS 基于 Darwin（FreeBSD + Mach 混合内核），XNU 内核中的 MAC 框架源自 FreeBSD TrustedBSD，衍生为 Seatbelt（App Sandbox）；System Integrity Protection（SIP/rootless，OS X

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_887] 卷“第07卷-freebsd的工程体系重构”第 137 章，匹配置信度 0.6，原因：关键词重合 1 项

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 原大纲本节无专门子节，磁盘加密和随机数生成内容缺失，已补全；“FreeBSD 使用 NSA 后门加密算法” 是阴谋论——AES 是 NIST 标准化算法，经过公开密码分析，FreeBSD 实现为公开源码可审计；GELI 支持多种算法，用户可自行选择
- “VuXML 由 FreeBSD Security Team 维护”——不准确，VuXML 主要由 ports 社区和安全团队共同维护，ports committer 可以直接提交 VuXML 条目；“VuXML 包含 FreeBSD 基础系统漏洞”——不包含，基础系统漏洞通过 SA/EN 公告处理；“pkg audit 自动更新 VuXML 数据库”——需要定期运行 `pkg audit -F`
- 原大纲本节列入的 “Anthropic Claude Mythos 2026.4 AI 发现 OpenBSD TCP SACK 27 年漏洞” 事件——经多轮 WebSearch 核查，截至 2026 年 7 月 19 日无任何公开可验证的一手来源（Anthropic 官网、OpenBSD 官网、MITRE CVE、oss-security 邮件列表）证实该事件，按 0 信任原则标注为 据一手文献
- “macOS 是 FreeBSD 所以 macOS 的安全就是 FreeBSD 的安全”——这是极其常见的误解；macOS/Darwin 仅在用户层和部分 API 层面源自 FreeBSD，XNU 内核是 Mach + FreeBSD 紧密混合，安全机制（SIP、Seatbelt、Code Signing、Notarization、Secure Enclave）均为 Apple 私有技术；“Fre

## 文献

- Kamp P H. GBDE (USENIX Security 2003); Ferguson N, Schneier B. Practical Cryptography (2003); FreeBSD Project. **gbde(8)**, **geli(8)**, **random(4)** Manual Pages; FreeBSD cgit commit history for geom/bde, geom/eli, dev/random. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. VuXML Homepage. vuxml.freebsd.org; FreeBSD Project. **pkg-audit(8)** Manual Page; FreeBSD Project. FreeBSD Ports Collection: security/vuxml/.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. Security Advisories Archives. security.freebsd.org; MITRE CVE Database. cve.mitre.org; LWN.net Security Coverage. lwn.net.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Apple Inc. Apple Platform Security. support.apple.com/guide/security/; Apple Inc. XNU Source Code (opensource.apple.com); The Open Group. Common Criteria Portal. commoncriteriaportal.org; The Open Group. UNIX Certification Directory. opengroup.org. ［A］[^doubt-resolved-478]: 据 Arch_Handbook (未署名) 消解[^doubt-resolved-479]: 据 Mac OS X Internals A Systems Approach (Amit Singh（阿米特·辛格）)  (未署名) 消解[^doubt-resolved-480]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解[^doubt-resolved-481]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解[^doubt-resolved-485]: 据 001_Benchmarking Mythos-Linked Bug Rediscovery (未署名) 消解[^doubt-resolved-486]: 据 Mac OS X Internals A Systems Approach (Amit Singh)  (未署名) 消解<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP52（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Sean Webb 与 Oliver Pinter 在 HardenedBSD 项目内推进 ASLR/PIE，并将其作为补丁提交上游 FreeBSD，目标是进入 11 版本。（BSD Now EP52，[1110.02-1421.06]，L1）
- ASLR 使程序可加载到任意内存地址，PIE 进一步支持应用级随机化，用于提高缓冲区溢出与信息泄露攻击的门槛；该实现默认关闭，需编译内核选项并可通过 sysctl 控制。（BSD Now EP52，[1110.02-1183.22]，L1）
- 该 ASLR 实现借鉴 PaX 与 NetBSD 的实现谱系，并在除 ARM 外的 FreeBSD 支持架构上工作，包括 32 位 Linux 兼容层。（BSD Now EP52，[1351.34-1501.26]，L1）
- OpenBSD 以 nginx 在基础系统中难以维护、且其自定义内存分配器遮蔽安全缓解机制为由，将其移出基础系统改由 ports 提供。（BSD Now EP52，[400.96-426.04]，L2）

**史料**：

- Sean Webb（Laddera）访谈（ASLR/PIE 实现者当事人自述）。（BSD Now EP52，[933.90-2162.30]，L1）

**史观**：

- 总纲10 动手者创造历史：总纲10 动手者创造历史：Sean Webb 以动手实现并上游 ASLR/PIE 的方式直接改变 FreeBSD 安全能力。（BSD Now EP52，[1110.02-1421.06]，L1）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：ASLR 采用 PaX 模型而非 OpenBSD 模型，源于实现者个人偏好与 HardenedBSD 协作的偶然路径。（BSD Now EP52，[1381.32-1435.42]，L1）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：FreeBSD、OpenBSD 与 HardenedBSD 在 ASLR 实现上各有路径，被置于对等比较而非优劣判定。（BSD Now EP52，[1381.32-1449.58]，L1）

**辨析**：

- Sean Webb 坦言上游化过程中存在私下邮件列表讨论与政治博弈，其本人一度无法参与辩护，具体争议内容未在本期披露。　[存疑脚注] 上游化受阻的具体技术或治理争议仅凭当事人单方叙述（BSD Now EP52，[1880.06-1929.90]，L4）

**文献**：

- [BSD Now EP52] Pennington J. BSD Now: 52: Reverse Takeover[EB/OL]. (2014-08-27)[2026-08-15]. https://www.bsdnow.tv/52.

<!-- /PODCAST_REVIEW -->
