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

- 总纲 10“动手者创造历史”——磁盘加密（GBDE/GELI）、CSPRNG 与 freebsd-update 等安全基础设施均系具体 committer 的个体工程实践累积，事件响应亦由一线志愿者劳动推进（概括 137.5-137.8 各节史观字段）。
- 总纲 8“本体论上各方平等”——跨 OS 安全模型比较中，FreeBSD、OpenBSD、Linux 的安全路线被置于对等比较而非优劣裁决；厂商认证产品与上游项目的关系亦非单向优劣。
- 总纲 15“文化即形式主义”——Security Team 流程正规化、SA/EN 分类、PGP 签名公告与支持周期政策的制度化，是开源安全响应成熟度的文化表征。
- 总纲 4“分离聚合是永恒规律”——OpenBSD 与 FreeBSD 安全哲学的路线分化（默认最大安全 vs 渐进稳健）是 BSD 家族内部分合循环的具现。

## 辨析

- 原大纲本节无专门子节，磁盘加密和随机数生成内容缺失，已补全；“FreeBSD 使用 NSA 后门加密算法” 是阴谋论——AES 是 NIST 标准化算法，经过公开密码分析，FreeBSD 实现为公开源码可审计；GELI 支持多种算法，用户可自行选择
- “VuXML 由 FreeBSD Security Team 维护”——不准确，VuXML 主要由 ports 社区和安全团队共同维护，ports committer 可以直接提交 VuXML 条目；“VuXML 包含 FreeBSD 基本系统漏洞”——不包含，基本系统漏洞通过 SA/EN 公告处理；“pkg audit 自动更新 VuXML 数据库”——需要定期运行 `pkg audit -F`
- 原大纲本节列入的 “Anthropic Claude Mythos 2026.4 AI 发现 OpenBSD TCP SACK 27 年漏洞” 事件——经多轮 WebSearch 核查，截至 2026 年 7 月 19 日无任何公开可验证的一手来源（Anthropic 官网、OpenBSD 官网、MITRE CVE、oss-security 邮件列表）证实该事件，按 0 信任原则标注为〔无一手来源，不采信〕。
- “macOS 是 FreeBSD 所以 macOS 的安全就是 FreeBSD 的安全”——这是极其常见的误解；macOS/Darwin 仅在用户层和部分 API 层面源自 FreeBSD，XNU 内核是 Mach + FreeBSD 紧密混合，安全机制（SIP、Seatbelt、Code Signing、Notarization、Secure Enclave）均为 Apple 私有技术；“FreeBSD 没有 Common Criteria 认证所以不安全”——CC 认证是过程/文档认证，不是安全性的直接度量；OpenBSD 也没有 CC 认证，但被普遍认为是最安全的通用 OS 之一（完整辨析见 137.8 节）。

## 文献

- Kamp P H. GBDE (USENIX Security 2003). ［A］
- Ferguson N, Schneier B. Practical Cryptography (2003).
- FreeBSD Project. **gbde(8)**, **geli(8)**, **random(4)** Manual Pages; FreeBSD cgit commit history for geom/bde, geom/eli, dev/random. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2020-2024 年间：291,070 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. VuXML Homepage. vuxml.freebsd.org; FreeBSD Project. **pkg-audit(8)** Manual Page; FreeBSD Project. FreeBSD Ports Collection: security/vuxml/.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

- FreeBSD Project. Security Advisories Archives. security.freebsd.org; MITRE CVE Database. cve.mitre.org; LWN.net Security Coverage. lwn.net.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

- Apple Inc. Apple Platform Security. support.apple.com/guide/security/; Apple Inc. XNU Source Code (opensource.apple.com); The Open Group. Common Criteria Portal. commoncriteriaportal.org; The Open Group. UNIX Certification Directory. opengroup.org. ［A］
<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP120、BSD Now EP52（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 本期核心为对 FreeBSD committer Pawel Jakub Dawidek（转写作 Pavel Davidek）的专访：其公司以 FreeBSD 为基座打造两款安全设备——FUDO 面向特权用户会话的录制与审计，Lynx 面向企业 TLS/SSL 流量的解密卸载；他自述设计哲学“信任开始之处即安全终结之处”（1827.17-1833.98），并指出近年重大安全事件多出自雇员与承包商，内部威胁的监控由此成为产品定位的核心。（BSD Now EP120，[1600.47-1742.97]，L1）
- FUDO 的技术栈揭示 FreeBSD 内核安全特性进入商业生产的深度：geli 承担全盘加密，Capsicum 承担会话沙箱，嘉宾称其设备“是比 FreeBSD 本体更大的 Capsicum 消费者”（1927.59-1934.81），认证前进程仅获一秒 CPU 配额与三个文件描述符；加密代价因客户端、服务端、落盘三方向而三倍叠加，图形会话另需 OCR 以支持文本检索，多主集群则依赖 ZFS 增量快照复制完成节点间同步。（BSD Now EP120，[1917.11-2234.32]，L1）
- Sean Webb 与 Oliver Pinter 在 HardenedBSD 项目内推进 ASLR/PIE，并将其作为补丁提交上游 FreeBSD，目标是进入 11 版本。（BSD Now EP52，[1109.1-1952.2]，L1）[订正：原 [1110.02-1421.06]，2026-09-30 SenseAudio 重转核对]
- ASLR 使程序可加载到任意内存地址，PIE 进一步支持应用级随机化，用于提高缓冲区溢出与信息泄露攻击的门槛；该实现默认关闭，需编译内核选项并可通过 sysctl 控制。（BSD Now EP52，[1109.1-1586.3]，L1）[订正：原 [1110.02-1183.22]，2026-09-30 SenseAudio 重转核对]
- 该 ASLR 实现借鉴 PaX 与 NetBSD 的实现谱系，并在除 ARM 外的 FreeBSD 支持架构上工作，包括 32 位 Linux 兼容层。（BSD Now EP52，[1351.3-1639.9]，L1）[订正：原 [1351.34-1501.26]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 将 BIND 与 nginx 一并移出基本系统：基本系统转而包含 nsd 与 unbound 供 5.6 与 5.7 用户过渡，BIND 可从 ports 获取最新版本，nginx 则为其新写的自定义 HTTP 守护进程让位。（BSD Now EP52，[397.6-447.6]，L2）[订正：原 OpenBSD 以 nginx 在基本系统中难以维护、且其自定义内存分配器遮蔽安全缓解机制为由，将其移出基本系统改由 ports 提供。（BSD Now EP52，[400.96-426.04]，L2），2026-09-30 SenseAudio 重转核对]

**史料**：

- 本期一手史料以嘉宾第一人称口述为主：FUDO 与 Lynx 的架构决策、geli 开发史（XTS 模式缺席年代实现 CBC 不可预测初始化向量、4K 扇区时代放弃块级认证）与 open crypto 框架改造及厂商补丁处境；辅以主持人转述的公开材料——PS4 越狱开发者发布的 GitHub 信息与推文、OpenBSD 运行于 EC2 T2 Micro 的实测帖、AsiaBSDCon 与 BSDCan 2016 征稿公告、2002 与 2015 两版开发者桌面截图页、OpenSSH 历史提权漏洞（二进制仅差一比特）与 TrueCrypt 重现构建事例，以及两封读者来信（大学集群迁移事故、帐篷公司 FreeNAS 改造）。（BSD Now EP120，[1600.47-1742.97]，L2）
- Sean Webb（Laddera）访谈（ASLR/PIE 实现者当事人自述）。（BSD Now EP52，[933.90-2162.30]，L1）

**史观**：

- 总纲10 动手者创造历史：嘉宾从昔日高产 committer 转向培养新一代动手者——推动 Mariusz Zaborski 成为 committer 从事 Capsicum 与 Casper、Konrad Witaszczyk 打磨加密内核转储补丁历时两年；他以 vendor 视角点出生态症结：厂商补丁常有九成就绪而最后一步永无余力完成者（3919.84-3932.04），故寄望基金会雇用专人收尾入库。BSD 史的推进动力在此显形为具体人手的持续劳动与“加入 FreeBSD 项目是我技术生涯最大的加速器”（4290.64-4303.08）式的代际传承，而非路线图或宣言。（BSD Now EP120，[3892.59-4303.08]，L2）
- 总纲5 没有必然性，只有偶然性：geli 开发史成为偶然性优先的注脚：当年可预测初始化向量的 CBC 模式被普遍视为安全，嘉宾凭超出共识的直觉实现不可预测初始化向量（3764.35-3772.27），日后该共识方案确被证明不安全，一次未按主流走的工程选择意外成为先见；与之呼应，OpenSSH 历史提权漏洞仅系一个比较运算符之差、修复前后二进制只差一比特，安全史的走向悬于这类无必然性的微小偶然。（BSD Now EP120，[3736.59-3778.55]，L1）
- 总纲10 动手者创造历史：Sean Webb 以动手实现并上游 ASLR/PIE 的方式直接改变 FreeBSD 安全能力。（BSD Now EP52，[1110.02-1421.06]，L1）
- 总纲5 没有必然性，只有偶然性：ASLR 采用 PaX 模型而非 OpenBSD 模型，源于实现者个人偏好与 HardenedBSD 协作的偶然路径。（BSD Now EP52，[1381.32-1435.42]，L1）
- 总纲8 本体论上各方平等：FreeBSD、OpenBSD 与 HardenedBSD 在 ASLR 实现上各有路径，被置于对等比较而非优劣判定。（BSD Now EP52，[1381.32-1449.58]，L1）

**辨析**：

- PS4 越狱条目需谨慎使用：越狱者经由 WebKit 进程取得内核执行权，与 FreeBSD jail 机制无关，越狱一词仅借自 iPhone 语境；Orbis OS 基于 FreeBSD 9.0，但 Sony 版本号不披露其回移了哪些 FreeBSD 补丁，主持人的“该漏洞可能早已在 FreeBSD 修复”属无法判定的推测；开发者公开 PID 列表与根文件系统转储并声明不为盗版服务，其身份、动机与操作细节均系单一来源。　[存疑脚注] 转写将越狱开发者记作“C-Chert”（疑为 CTurt），Orbis OS 补丁回移状态无公开可核记录，主持人推断未经多源验证（BSD Now EP120，[4538.64-4651.02]，L4）
- Zero Trust 倡议暴露开源承诺与二进制分发之间的结构性落差：发布源码无法证明用户安装的二进制由其构建——Signal 的 App Store 二进制不可验证，TrueCrypt 的重现构建需穷举编译环境且工作量浩大；嘉宾强调该倡议“不想让人们信任 zero trust initiative 本身”（3522.06-3530.33），拒绝自任受信第三方，转而设想以基于 geli 的可移植磁盘加密项目先行示范；同期听众事故（OpenSSL 升级致 openldap 二进制失配、无人可登录）与 FreeBSD 侧 Ed Maste（转写作 Ed Mass）参加可重现构建会议，说明可重现构建在 2015 年仍属前沿工程而非成熟机制。（BSD Now EP120，[2893.17-3045.95]，L2）
- Sean Webb 坦言上游化过程中存在私下邮件列表讨论与政治博弈，其本人一度无法参与辩护，具体争议内容未在本期披露。　[存疑脚注] 上游化受阻的具体技术或治理争议仅凭当事人单方叙述（BSD Now EP52，[1880.06-1929.90]，L4）

**文献**：

- [BSD Now EP120] Pennington J. BSD Now: 120: I’m talking about the man in the middle[EB/OL]. (2015-12-16)[2026-08-15]. <https://www.bsdnow.tv/120>.
- [BSD Now EP52] Pennington J. BSD Now: 52: Reverse Takeover[EB/OL]. (2014-08-27)[2026-08-15]. <https://www.bsdnow.tv/52>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

