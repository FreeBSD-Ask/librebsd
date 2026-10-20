---
chapter: 第 205 章
id: CH205
volume: 第10卷-openbsd的历史
---

# 第 205 章 openbsd安全文化的奠基

## 要点

- OpenBSD 代码审计方法论由 de Raadt 主导自 1996 年 fork 后逐步建立，核心实践为逐行审查基本系统源码，重点关注缓冲区溢出与格式化字符串漏洞、信任边界与权限提升；审计流程为发现问题 → 修复 →commit log 详细记录 →security advisory；OpenBSD Security Advisories 自 1996 年起在 <www.openbsd.org/
- OpenBSD “默认安全”（secure by default）原则体现在默认关闭非必要服务（如默认不启用 telnetd、ftpd）、默认启用加密（如 SSH 默认开启）、默认最小权限等多方面；该原则自 1996 年 fork 之初即确立；防火墙方面，ipf（Darren Reed（达伦·里德） 的 IP Filter）〔待核：原文截断，后文待回源〕
- OpenBSD 1996-2000 年间通过代码审计发现并修复大量安全漏洞，包括缓冲区溢出（如 ftpd、telnetd 远程溢出）、格式化字符串漏洞（如 wu-ftpd Format String Vulnerability CVE-2000-0573，2000-06 披露）、信任边界问题；部分漏洞在审计前已被利用（如 1999 年 BIND NXT 漏洞 CVE-1999-0833），部分是审
- OpenBSD 审计成果通过 cross-BSD 协调（vendor branch 同步）反馈至 FreeBSD/NetBSD，部分修复被 Linux 发行版移植；〔待核：原文截断，后文待回源〕
- FreeBSD 1990 年代后期建立 Security Officer 制度（如 Warner Losh（沃纳·洛什）、Kris Kennaway 等任职）但未系统性代码审计，安全修复以反应式（收到报告后修复）为主；Linux 1990 年代缺乏系统性审计，依赖用户与厂商报告，1999 年 Linux Security Audit Project 由 Daniel Stone 等发起但规模有限；

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3778] 卷“第10卷-openbsd的历史”第 205 章，匹配置信度 folder，原因：folder 第203章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 审计方法论在不同叙事中存在差异——部分资料强调 “逐行审查”（de Raadt 在 misc@ 邮件列表多次提及 “audit every line”），部分强调 “分类审查”（按漏洞类型如 buffer overflow、format string、integer overflow 分类扫描），二者非互斥而是互补——逐行审查是方法论基础，分类审查是针对特定漏洞类型的专项扫描；审计范围限定为基本系
- ipf 与 pf 的替代关系——ipf 自 1996 年 fork 前即存在于 NetBSD 代码库，OpenBSD 继承使用至 2.9（2001-05）；2001 年 Darren Reed 修改 ipf 许可证引发争议，OpenBSD 于 2001-06-24 引入 pf（commit 148b55c022b1）作为 ipf 兼容替代品，pf 随 OpenBSD 3.0（2001-12-01）
- “数千个漏洞” 的具体数字——OpenBSD Security Advisories 页面（<https://www.openbsd.org/security.html>）逐条记录了 1996 年至今的 advisory，1996-2000 年间的 advisory 可直接在该页面计数；advisory 数量与实际修复的漏洞数量非一一对应——一条 advisory 可能修复多个相关漏洞，一个漏洞的
- strlcpy/strlcat 引入时间——bsd_commits.duckdb 显示 millert 于 1998-07-01 commit 1dc0268a4106 引入 strlcpy.c/strlcat.c/strlcpy.3，部分二手资料误记为 1996 年，实际引入时间为 1998-07-01；strlcpy/strlcat 被 glibc 采纳的过程曲折——glibc 维护者 Ulrich
- 三者安全实践的 “严格程度” 对比缺乏权威量化评估——OpenBSD Security Advisories 与 FreeBSD Security Advisories 的 advisory 数量可通过各自页面计数，但 advisory 数量受多个因素影响（审计范围、披露政策、版本发布频率等），不能直接作为安全质量排名依据；“反应式安全” 与 “主动审计” 的界定——OpenBSD 自 1996

## 文献

- OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html>；OpenBSD **security(8)** 手册页 [EB/OL]. <https://man.openbsd.org/security.8>；OpenBSD **afterboot(8)** 手册页 [EB/OL]. <https://man.openbsd.org/afterboot.8>；OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；openbsd.duckdb 查询 L3.1.1.audit（来源：原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.1.1，数据缺口） ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD **afterboot(8)** 手册页 [EB/OL]. <https://man.openbsd.org/afterboot.8>；OpenBSD commit 148b55c022b1 [G/OL]. <https://github.com/openbsd/src/commit/148b55c022b1>；OpenBSD misc@ 邮件列表存档 [EB/OL]. <https://marc.info/?laccopenbsd-misc> ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- FreeBSD Security Advisories [EB/OL]. <https://www.freebsd.org/security/advisories/>；NetBSD Security Advisories [EB/OL]. <https://www.netbsd.org/support/security/>；OpenBSD **strlcpy(3)** 手册页 [EB/OL]. <https://man.openbsd.org/strlcpy.3>；OpenBSD commit 1dc0268a4106 [G/OL]. <https://github.com/openbsd/src/commit/1dc0268a4106>；Linux Security Audit Project [EB/OL]. <https://www.linux.org.au/lsec/> ［A］**OpenBSD 安全 API 扩散时间线**：

| API | OpenBSD 引入时间 | commit hash | 采纳系统 |
| --- | --- | --- | --- |
| **strlcpy(3)**/**strlcat(3)** | 1998-07-01 | `1dc0268a4106` | FreeBSD、NetBSD、glibc（2019 年 2.30）、macOS libc |
| **arc4random(3)** | 1996-12 | `af7d239111f9` | FreeBSD、NetBSD、macOS、Linux libbsd |
- FreeBSD Security Advisories 1996-2000 [EB/OL]. <https://www.freebsd.org/security/advisories/>；Linux Security Audit Project [EB/OL]. <https://www.linux.org.au/lsec/>；OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html> ［A］**OpenBSD/FreeBSD/Linux 1990 年代安全实践对比**：

| 维度 | OpenBSD | FreeBSD | Linux |
| --- | --- | --- | --- |
| 安全模型 | 主动逐行审计 | Security Officer 制度（反应式） | 各发行版各自为政（反应式） |
| 审计范围 | 基本系统（src/ 与 sys/） | 无系统性审计 | 1999 年 Linux Security Audit Project（规模有限） |
| 关键人物 | de Raadt、Brauer、millert 等 | Warner Losh、Kris Kennaway 等 | Daniel Stone 等 |
| 安全发现来源 | 内生于审计流程 | 外生于用户报告 | 外生于用户与厂商报告 |
| 跨项目扩散 | strlcpy/strlcat、arc4random、OpenSSH | Security Advisories 标注 OpenBSD fix | 各发行版各自打包修复 |
- OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；OpenBSD Security Advisories [EB/OL]. <https://www.openbsd.org/security.html>；BUGTRAQ 邮件列表存档 [EB/OL]. <https://seclists.org/bugtraq/>；外部基准报告：外部基准-StackOverflow-PackageEcosystem.md 第 3.2 节 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/外部基准-StackOverflow-PackageEcosystem.md** ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP498、BSD Now EP428、BSD Now EP348、BSD Now EP330、BSDTalk EP29（共 5 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Florian Obser 阐述 OpenBSD 三类利用缓解：降权、权限分离与受限服务操作模式，作为攻击者达成任意代码执行后的最后防线；降权是最弱但最古老的缓解，权限分离将不可信数据解析移入低权限进程，受限模式则以 pledge 限制进程能力。（BSD Now EP498，[514.74-603.96]，L2）
- Obser 回溯 ping 降权的历史：Theo de Raadt 逾 26 年前重构 ping，使其先打开原始套接字再丢弃 root 权限，以防本地用户借 ping 缺陷提权；二十年后又发现以 root 调用 ping 时只是从 root 降到 root，遂改为降级到专用用户。（BSD Now EP498，[598.70-632.26]，L2）
- Obser 叙述 pledge 的由来：systrace 由 Niels Provos 开发但因基于系统调用参数而难用，OpenBSD 基本系统中长期仅 sshd 使用；2015 年 Theo 诱使 Nicholas Marriott 用 systrace 沙箱 file 却只坚持半年，成为压垮性体验，Theo 遂开发 tame（后改名 pledge）。（BSD Now EP498，[784.74-861.42]，L2）
- pledge 通过对 OpenBSD 基础程序的需求归类而成，程序违规即被内核以不可捕获的 SIGABRT 终止；当约 50 个程序加入 pledge 后被认为成熟并合入主线，半年内几乎所有基础程序均使用 pledge。（BSD Now EP498，[861.42-931.54]，L2）
- 其余新闻包括 OPNsense 23.1.1 发布、Ansible Clone 工具、NetBSD 在 FOSDEM 2023 的 BSD dev room 报告、FreeBSD Foundation 的 BSDCan 旅行资助，以及 Game of Trees 0.81 与 x-only PKU、pinsyscall 等 OpenBSD 新进展。（BSD Now EP498，[1156.64-2330.00]，L2）
- OpenBSD 于 1995 年 10 月作为 NetBSD 分叉起步，其默认安装长期仅报告两个远程漏洞，被描述为默认安全的系统。（BSD Now EP428，[135.74-145.1]，L2）
- OpenBSD 率先随系统搭载 IPsec 等强密码学，并因此卷入美国出口管制，这是其基地设于加拿大的原因之一。（BSD Now EP428，[145.1-160.3]，L2）
- OpenBSD 形成发现漏洞后不再单点修补，而是在全树范围内寻找并修复同类模式的代码审计文化。（BSD Now EP428，[164.94-184.78]，L2）
- OpenBSD 是 OpenSSH、OpenBGPD、PF、OpenNTPD、IKED、Mandoc 与 LibreSSL 等广泛使用组件的上游来源。（BSD Now EP428，[247.2-262.74]，L2）[订正：原 OpenSMTPD、IKE，2026-09-30 SenseAudio 重转核对]
- FuryBSD 2020 第二季度镜像（XFCE 与 KDE）发布，团队自述把精力放在开箱即用的 Wi-Fi、摄像头与虚拟机支持上。（BSD Now EP348，[68.68-103.08]，L2）
- Ars Technica 评测 GhostBSD：安装体验较 FreeBSD 更顺畅、桌面可用，但存在 MATE 面板崩溃、ZFS 4K 块对齐失效等瑕疵。（BSD Now EP348，[494.58-736.64]，L2）
- OpenBSD malloc 安全分配器内部机制被逐行解读：chunk canary（0xdb 填充）在 free 时校验，越界写会触发 abort。（BSD Now EP348，[1291.52-1359.6]，L2）
- 技术选型文章主张 FreeBSD 相对 GNU/Linux 具有基本系统与滚动软件包结合、ZFS、启动环境、jail 等优势。（BSD Now EP348，[253.24-297.16]，L2）
- OpenBSD 的 BSD Authentication 认证绕过漏洞源于 login_passwd 对 challenge 协议的处理缺陷，用户名形如 -schallenge 时会被自动判定成功；该漏洞远程可利用于 smtpd、ldapd、radiusd 等应用，但 sshd 因纵深防御机制不受影响。（BSD Now EP330，[185.76-440.9]，L2）[订正：原 [185.76-193.66]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 在初次联系后约 40 小时内修复该漏洞，主持人以此与其它项目耗时数月乃至数年的修复形成对照，凸显其把安全响应置于优先位置的组织惯性。（BSD Now EP330，[562.80-584.46]，L3）
- NetBSD 9.0 RC1 在四个月发布流程中处理逾 500 次 pull-up，新增 aarch64（含 Arm ServerReady）、NVMM 硬件虚拟化、更新版 ZFS、内核 ASLR、KLEAK/KASAN 等 sanitizer、NPF 改进与 SATA NCQ 支持。（BSD Now EP330，[724.00-968.5]，L2）[订正：原 [724.00-802.99]，2026-09-30 SenseAudio 重转核对]
- FreeNAS 在 DigitalOcean 的部署教程通过第二块设备安装后再以 dd 重灌引导区完成，主持人补充 ZFS 的校验与校验和使消费级磁盘配合 RAID-Z1 冗余在家庭 NAS 场景可用，并强调以独立备份兜底。（BSD Now EP330，[1084.88-1299.54]，L2）
- NomadBSD 1.3 是基于 FreeBSD 12.1 的 USB 持久化 Live 系统，通过 SMBIOS 检测自动适配 VirtualBox，新增 ZFS 安装支持，并因 Lenovo 兼容问题从 GPT 改回 MBR。（BSD Now EP330，[1790.46-1962.9]，L2）[订正：原 [1790.46-1892.38]，2026-09-30 SenseAudio 重转核对]
- e2k19 黑客松重写 RPKI 客户端的 X.509 验证，将证书与 CRL 表改为红黑树查找、以 rename 原子替换输出文件，使 VRP 验证从 20 余分钟降至约 1 分钟。（BSD Now EP330，[2281.90-2516.12]，L2）
- 当事人自述 386BSD 的历史定位：他们是诸多 BSD 分支的早期源头，打破了局面，但发起大型项目后人人议程各异、无法兼顾所有方向，由此产生的摩擦只是任何庞大事物成长中的阵痛；夫妇二人选择不对议程争执，允许 FreeBSD 等继续生长；386BSD 至 2006 年的定位是遗产（heritage）与操作系统另类用法的试验场，仍可运行但支持机器有限。（BSDTalk EP29，[532.88-803.64]，L1）
- 在 386BSD 文章系列发表 15 周年之际，当事人恢复了当年因版面被剪除的内容：杂志页数随广告量浮动，大量图表、侧栏乃至整节模块讨论被删，腾出版面给 Intel 等广告商；同时其数据中心监测显示，近两年对操作系统早期根源文献的引用兴趣显著上升，尤其来自中国、印度等亚洲地区与法国、德国，遂将恢复工程扩展为更接近原始设想的完整版本，建于 **porting-unix-2-the-386.jolix.com**（Jolix 为 386BSD 的通行别称）。（BSDTalk EP29，[222.56-383.16]，L1）
- 当事人提出 BSD 家族的受众分化论：386BSD 文章系列的本意是在 Windows 之前把 PC 受众转化为 BSD 用户，第二代 CD-ROM 曾试图将其做成面向大众的类 Windows 95 系统但目标中道失落；此后各 BSD 各自服务不同受众，如 FreeBSD 服务浸透 version 6、version 7 血统的严格 UNIX 类型用户；各项目共同的困难在于清晰聆听受众并真正交付。（BSDTalk EP29，[695.64-763.48]，L1）
- Lynne Jolitz 对 BSD 提出软件优先级批评：各开源内核尤其是 BSD 在系统低层骨架上耗时过多，应尽快将底层做定、转向用户实际感知与价值所在的高层抽象；她以 CNET 文章“Misplaced Software Priorities”阐述此论，并以 Ubuntu 凭高层亲和力使 Linux 获益为反例；让中断更快、集群接口更快并非要害（她在 Tandem 见过 256 处理器集群，认为集群永远是特殊用途），BSD 若将创造力投向高层将有更大未来；她还特别强调不应忘记 NetBSD，并称对其创建记忆犹新。（BSDTalk EP29，[1408.7-1558.5]，L1）

**史料**：

- Florian Obser《Privilege drop, privilege separation and restricted service operating mode in OpenBSD》（sha256.net 博客），为 OpenBSD 开发者本人的一手技术文章，经节目转述。（BSD Now EP498，[508.82-1144.64]，L1）
- OpenBSD tech 邮件列表中 Theo de Raadt 关于 pinsyscall 的帖子，涉及 ExecVE 与 ROP pivot，为当事人一手陈述，经节目转述。（BSD Now EP498，[2272.22-2304.38]，L1）
- Game of Trees 0.81 发布与 Stefan Sperling 在 FOSDEM 2023 的演讲及幻灯片，为官方发布线索，经节目转述。（BSD Now EP498，[1823.68-1923.94]，L2）
- Peter Hansteen 的 What every IT person needs to know about OpenBSD 系列文章，作为本期 OpenBSD 历史叙述的主要二手来源。（BSD Now EP428，[70.74-76.44]，L2）
- FuryBSD 网站的季度状态报告（Joe Maloney 撰写）。（BSD Now EP348，[78.58-89.28]，L2）
- Jim Salter 在 Ars Technica 发表的 GhostBSD 评测。（BSD Now EP348，[483.98-491.34]，L2）
- OpenBSD malloc 内部机制博客及所引 otto 的 malloc 论文、PHK malloc 论文与旧提交记录。（BSD Now EP348，[1381.56-1400.8]，L3）
- OpenBSD 官方安全公告与 CVE 记录（认证绕过，涉及 smtpd/ldapd/radiusd，sshd 因纵深防御免责），经主持人转述并引其代码分析。（BSD Now EP330，[256.84-267.32]，L2）
- NetBSD releng 团队发布的 9.0 RC1 公告，列明 pull-up 数量、硬件支持与安全特性清单。（BSD Now EP330，[734.06-745.10]，L2）
- Claudio Jeker 的 e2k19 黑客松报告《Nobody Can Hear You Scream》，当事人自述 RPKI 客户端 X.509 重写过程。（BSD Now EP330，[2288.98-2299.82]，L1）
- 当事人罕见的早期 BSD 在场证词：William Jolitz 在 NASA Ames 研究中心因购置约两万美元的语音程序附带 UNIX 环境而偶然入行；其后在伯克利目击 Bill Joy 与 Chuck Haley 在身旁的 ADM-3 终端上编写后来称为 vi 的软件并为一款内核的命名反复争执，当时它只是 vi、电子邮件与同侪邮件程序工作的集合，尚无 BSD 内核之名；加州大学在可分发代码枯竭后请 William 做 PDP-11 移植，他遂参与 2.8/2.9BSD 的发行工作，并向 Mike Karels 引入 UNIX。（BSDTalk EP29，[89.44-213.88]，L1）

**史观**：

- 总纲10 动手者创造历史：安全机制由开发者逐个程序地审计与归类累积而成，而非一次性顶层设计。：Theo 与 Obser 等通过逐个程序的重构与需求归类塑造 OpenBSD 安全机制。（BSD Now EP498，[861.42-931.54]，L2）
- 总纲9 经验优先：以基本系统中真实程序的可用性经验为标准，淘汰难以使用的 systrace。：systrace 因难用而被 pledge 取代，设计取舍来自真实程序的实践经验。（BSD Now EP498，[784.74-861.42]，L2）
- 总纲5 没有必然性，只有偶然性：pledge 的诞生由 systrace 实践中的偶然挫败触发，而非预先规划。：file 沙箱半年即弃的偶然失败促成 tame 与 pledge 的诞生。（BSD Now EP498，[784.74-861.42]，L2）
- 总纲10 动手者创造历史：OpenBSD 以代码审计与全树范围修复确立安全实践，体现动手者在具体工程中塑造项目文化。（BSD Now EP428，[164.94-191.78]，L2）
- 总纲13 法律与道德是利益分配：美国出口管制把加密技术纳入法律约束，迫使 OpenBSD 调整基地布局，体现法律与道德作为利益分配工具的现实效应。（BSD Now EP428，[145.1-160.3]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：FuryBSD 团队承继 PC-BSD/TrueOS 脉络，靠具体功能改进而非叙事口号推动桌面 BSD。（BSD Now EP348，[107.08-120.08]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：OpenBSD malloc 的 canary 等防御手段是阶段性的安全知识，需随攻击方法演进而更新。（BSD Now EP348，[1291.52-1359.6]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：OpenBSD 开发者与黑客松参与者在雪山小屋中直接动手重写 X.509 代码，把验证时间压缩 20 倍，历史由动手者而非口号推进。（BSD Now EP330，[2505.66-2516.12]，L2）
- 总纲9 经验优先：总纲9 经验优先：主持人从自身 24×7 使用廉价盘与 ZFS 的实际经验回答磁盘选型问题，实践知识优先于厂商宣传。（BSD Now EP330，[3813.36-3853.76]，L1）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：本期同时呈现 OpenBSD、NetBSD、FreeBSD/FreeNAS、NomadBSD，各分支被平等对待，不以规模论高下。（BSD Now EP330，[1790.46-1814.48]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：OpenBSD 罕见的远程认证漏洞出现与 40 小时修复并非必然，而是具体代码缺陷与具体响应条件的偶然叠加。 [存疑脚注] 漏洞为偶发事件这一判断系史学概括，非节目明言（BSD Now EP330，[245.98-255.10]，L4）
- 总纲3 不存在进步，只有权力再分配：总纲3 不存在进步，只有权力再分配：NomadBSD 从 GPT 改回 MBR、UnionFS 换为 FUSE 等变化并非线性进步，而是兼容性与约束在不同硬件间的重新分配。（BSD Now EP330，[1872.70-1888.38]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：本期多则教程与工具（如云主机装 FreeNAS 的旧法）提醒知识会随平台与版本过期，需持续核验。（BSD Now EP330，[1482.36-1494.88]，L2）
- 总纲8 本体论上各方平等：当事人主张技术方案多元平等的市场观：不存在单一赢家或垄断者，应就具体问题审视特定系统对人的益处；企业常因流行度先采用 Linux，随后撞上流行度解决不了、须以架构处置的障碍，此时 BSD 恰好承接且两者往来迁移常见；开源对他们而言是降低工具成本的恩惠——90 年代中期半导体 CAD 工具成本已从百万美元级降至十万级，节省的资金可回流至真正设计与创造的人。（BSDTalk EP29，[1066.6-1268.46]，L1）
- 总纲3 不存在进步，只有权力再分配：当事人对泡沫破裂后 BSD 投资环境的判断：投资正在大规模回归，但只流向无人做过的方向，任何聚焦他人已完成领域的项目都无法说服商人；BSD 不能以取代 Linux 为目标，正如 Linux 取代 Windows 的空间有限；正确路径是把开源理解为一种市场颠覆，如同互联网对整个经济体的颠覆，网络开发模式正在颠覆传统软件模型，商人深知如何利用市场颠覆，但组织不当的想法无法借此占领闲置市场；钱就在那里，问题在于以更高层抽象构思并让人确信值得投资。（BSDTalk EP29，[1664.26-1865.58]，L1）

**辨析**：

- Obser 所述 Theo 逾 26 年前重构 ping 的具体年份需与 OpenBSD 提交史核验，节目转述未给出提交编号。 [存疑脚注] ping 重构年份为口述概数，须以 OpenBSD 提交记录与变更日志核验。（BSD Now EP498，[598.70-632.26]，L4）
- pledge 从 tame 更名的具体时间与 5.8、5.9 版本对应关系为概略叙述，需以 OpenBSD 发布说明与 man 页核验。 [存疑脚注] tame 更名 pledge 及对应版本为概略叙述，需以 pledge(2) 手册与发布说明确认。（BSD Now EP498，[861.42-931.54]，L4）
- “默认安装仅两个远程漏洞”为 OpenBSD 项目长期自述口径，其统计口径与时间范围需与官方安全公告逐条核对。 [存疑脚注] 远程漏洞计数为项目自述，统计边界需对照 OpenBSD 官方安全公告确认。（BSD Now EP428，[138.94-145.1]，L4）
- 转写中 FuryBSD 与 FurryBSD 混淆，GhostBSD 的 Chrome 兼容问题被节目归因于临时打包故障，未经核实。 [存疑脚注] GhostBSD Chrome 故障原因未核实（BSD Now EP348，[687.6-695.68]，L4）
- OpenBSD 认证绕过漏洞的“远程可利用”与 sshd 免责边界需逐应用分析，实际影响应按个案评估，不能笼统宣称整个系统不安全。 [存疑脚注] 转写对漏洞细节的表述为口语转述，建议以官方 errata 与 CVE 原文核对（BSD Now EP330，[193.66-204.80]，L4）
- NetBSD 9.0 当时尚未正式发布，RC1 特性清单可能随正式版调整，所引安全与虚拟化特性宜以正式公告为准。 [考据脚注] RC1 为发布前状态，存在后续变更可能（BSD Now EP330，[971.00-979.36]，L4）
- 当事人回忆 80 年代参加规划 BSD 未来的架构组会议时，为尽快推出 sockets，关于 socket 安全性的讨论被推到议程末尾并最终砍掉；他认为其中许多问题正是 OpenBSD 日后聚焦的领域。该回忆将 OpenBSD 安全工程追认至早期 BSD 的结构性遗留，但口述无同期会议文献佐证，会议时间与名录未详。 [存疑脚注] 单一当事人回忆，架构组会议的具体届次、日期与出席者均未言明，须与 CSRG 会议记录及邮件档案交叉验证（BSDTalk EP29，[630.68-664.96]，L1）

**文献**：

- [BSD Now EP498] Pennington J. BSD Now: 498: Dropping Privileges[EB/OL]. (2023-03-16)[2026-08-15]. <https://www.bsdnow.tv/498>.
- [BSD Now EP428] Pennington J. BSD Now: 428: Cult of BSD[EB/OL]. (2021-11-11)[2026-08-15]. <https://www.bsdnow.tv/428>.
- [BSD Now EP348] Pennington J. BSD Now: 348: BSD Community Collections[EB/OL]. (2020-04-30)[2026-08-15]. <https://www.bsdnow.tv/348>.
- [BSD Now EP330] Pennington J. BSD Now: 330: Happy Holidays, All(an)[EB/OL]. (2019-12-26)[2026-08-15]. <https://www.bsdnow.tv/330>.
- [BSDTalk EP29] Backman W. BSDTalk: 29: bsdtalk029 - Interview with Lynne and William Jolitz[EB/OL]. (2006-03-30)[2026-08-27]. <https://archive.org/details/bsdtalk029>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-10-070 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-10-070`；login 逐条遍历判定采纳）

2000年初DDoS攻击工具（trinoo、TFN、TFN2K、Stacheldraht）大量利用ISP的UNIX系统作为攻击代理；Dave Dittrich等从业者发布分析工具与检测脚本，CERT CA-99-17确立了master/daemon术语体系，形成社区化的应急响应实践。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-425 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-425`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：FreeBSD 与 Mac 均曾采用 POSIX 1e 安全扩展机制。（YouTube EPDGY7qJBbG5c，[1345.04-1348.63]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-450 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-450`；w172 YouTube 章节路由采纳）

据〔EuroBSDcon 2023〕讲者口述：讲者统计其系统上约 39% 的进程启用了 unveil，并认为 unveil 比 pledge 更难使用、pledge 更易实现。（YouTube EPE3ITPlL8AkM，[2244.319-2254.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1095 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1095`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：在其它开源项目中存在类似机制，例如 OpenBSD 的 pledge（YouTube EPWl2hewfxcKM，[3193.04-3201.27]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-359 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-359`；w172 YouTube 章节路由采纳）

据〔bluhm.genua.de OpenBSD 测试基础设施演讲〕讲者 Jan Klemkow 口述：MPI 与一位 OpenBSD 相关人员 Chris 提供了两台机器（YouTube EPbTZ7YhZpVeg，[1630.56-1636.03]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-360 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-360`；w172 YouTube 章节路由采纳）

据〔bluhm.genua.de OpenBSD 测试基础设施演讲〕讲者 Jan Klemkow 口述：在 Spark、PowerPC 与 MIPS 上测试 OpenBSD 所需投入很大（YouTube EPbTZ7YhZpVeg，[1599.12-1603.23]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-751 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-751`；w172 YouTube 章节路由采纳）

据〔FIDO and Webauthn on BSD 报告（来源不详）〕讲者 Taylor R Campbell 口述：他数月前列出一个 NetBSD 缺陷，他人核实 FreeBSD 同样存在。（YouTube EPmHfVwEPaDws，[2223.3-2231.569]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1623 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1623`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building a Large Scale Threat Intelligence System with OpenBSD，讲者 Lawrence Teo〕讲者口述：其自 2000 年起即为 OpenBSD 用户，并称那大约是 OpenBSD 2.5 到 2.6 的时候。（YouTube EPqQdcAn4-3CE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1624 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1624`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building a Large Scale Threat Intelligence System with OpenBSD，讲者 Lawrence Teo〕讲者口述：其自 2012 年起成为 OpenBSD 开发者，用户名 lteo；早期主要从事网络相关事务，涉及 libpcap、tcpdump、divert 等。（YouTube EPqQdcAn4-3CE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1625 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1625`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building a Large Scale Threat Intelligence System with OpenBSD，讲者 Lawrence Teo〕讲者口述：其系统以安装 pkg 包中携带的 dynamic-rules 规则文件、经 pfctl 载入 dynamic-rules 锚点的方式动态下发规则，借 pf 锚点特性在不刷新其余规则集的前提下追加规则。（YouTube EPqQdcAn4-3CE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1626 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1626`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Building a Large Scale Threat Intelligence System with OpenBSD，讲者 Lawrence Teo〕讲者口述：divert 是 OpenBSD 中在内核与用户态之间转发分组的功能，其以 IPS 模式运行的 snort 即依赖该功能；但该功能当时相当有限，在存在多个出口网卡、客户接入多条 ISP 线路等条件下工作不佳。（YouTube EPqQdcAn4-3CE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1867 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1867`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ingo Schwarze 于 BSDCan 2018 演讲〕讲者口述：他把 SQLite 从 OpenBSD 基本系统里删掉的理由是，SQLite 发版频繁，大约每月一次，且每次都有实质改动，平均每年约新增 15,000 行代码，而 OpenBSD 会对基本系统里的软件做审计，没人能每年审计这样一个工具里 15,000 行新代码。（YouTube EPN26pBxJPMxs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1868 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1868`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ingo Schwarze 于 BSDCan 2018 演讲〕讲者口述：他口述删除 SQLite 的直接收益是——基本系统少维护约 200,000 行代码、每年少审 15,000 行、数据库体积减半、查找速度翻倍。（YouTube EPN26pBxJPMxs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1869 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1869`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ingo Schwarze 于 BSDCan 2018 演讲〕讲者口述：他口述这个 OpenSSL 的分支是 2014 年在“hot blade”事件之后从 open SSL 分出来的，而且不只因为那一个漏洞，而是因为对基本安全实践的普遍忽视；最初的重点是删除不必要的代码。（YouTube EPN26pBxJPMxs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1870 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1870`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Ingo Schwarze 于 BSDCan 2018 演讲〕讲者口述：他说就文档工具而言，man doc 自大约 BSDCan 2015 以来，已成为各 BSD 命令行工具的标准文档工具包，并且正在成为面向 Web 的标准，原因在于其对语义标记的支持。（YouTube EPN26pBxJPMxs，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2223 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2223`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 在 BSDCan 2018 演讲〕讲者口述：飞利浦医疗 X 光机与数字荧光透视机上用于把机器内部以太网与医院外部以太网二层次隔离的小盒子，最初由 Holger Mickelan 在飞利浦的硕士论文中实现，跑了约五年前飞利浦想让部分改动进入 OpenBSD 主线，因此找来讲者接手重写。（YouTube EPDOCAYXeu5Fc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2224 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2224`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 在 BSDCan 2018 演讲〕讲者口述：该 OpenBSD 隔离盒运行自定义 RAM 盘，仅含 bridge、PF、SSH、SSHD 与少量基础工具，不是完整安装；RAM 盘无任何持久配置，采用 10.0.0.0 网段的固定"魔法 IP"，由内部管理系统连入并下发 PF 规则与桥接过滤器。（YouTube EPDOCAYXeu5Fc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2225 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2225`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 在 BSDCan 2018 演讲〕讲者口述：讲者重写桥接 ARP 过滤器时发现过滤器逻辑本身仅约 40 行，真正的工程难点在 ifconfig 桥接规则解析器——它把行拆词塞进 argc/argv，词数组上限曾限为 8，导致部分规则能工作、部分不能；含全部相关改动整个 diff 仍仅约 400 行。（YouTube EPDOCAYXeu5Fc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2226 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2226`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Henning Brauer 在 BSDCan 2018 演讲 Q&A〕讲者口述：飞利浦对付费给讲者的代码不做限制，反而非常希望这些改动进入 OpenBSD 主线；讲者评价飞利浦真正理解开源的 give and take，愿意回馈社区。（YouTube EPDOCAYXeu5Fc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2726 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2726`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hack the Puffy: OpenBSD advocacy through CTF（Jason Testart）讲者口述：讲题真身是 CTF 而非段子；他自述安全背景（早年玩 honeynet project 的扫描月赛之类），做完公开挑战后意犹未尽，2018 年起了自己做挑战的念头。（YouTube EPh5uUEJDqtaE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2727 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2727`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hack the Puffy: OpenBSD advocacy through CTF（Jason Testart）讲者口述：其 OpenBSD 挑战设两面旗——先拿到 user 权限，再提权（转写作 group）。（YouTube EPh5uUEJDqtaE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2728 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2728`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Hack the Puffy: OpenBSD advocacy through CTF（Jason Testart）讲者口述：做完一批挑战后的观察之一是没有任何涉及 LDAP 的题目——而这恰是他日常工作里用得多的东西。（YouTube EPh5uUEJDqtaE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3442 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3442`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Slackathon 2009: A quick show of things that make Bob scream 讲者口述：在 OpenBSD 里每次 I/O 都要经过 vnode 与 VFS；讲者称当下并未重构 vnode，但 Bob 正在做这件事。（YouTube EPHTD9Gow1wTU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3443 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3443`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Slackathon 2009: A quick show of things that make Bob scream 讲者口述：讲者自述一项工作因 C2K9 灾难而取消，即缓冲区的磁盘排序：每次把 buffer 交给 SCSI 或 SD 并落到转写音作 BD 之处时，该函数本应靠排序 I/O 操作来提速。（YouTube EPHTD9Gow1wTU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3444 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3444`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Slackathon 2009: A quick show of things that make Bob scream 讲者口述：一位 OpenBSD 开发者建议其什么排序都别做，只把请求留在队列里加一点延迟；讲者改用简单 tail Q 加 delay 后，自测磁盘 I/O 速度最多快 15%。（YouTube EPHTD9Gow1wTU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3445 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3445`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Slackathon 2009: A quick show of things that make Bob scream 讲者口述：讲者自述在地下室实验后断言转写音作 Disord 的磁盘排序很蠢、改为排队即可，并发现逆序取用仍更快，把这一堆逻辑称作八十年代遗物。（YouTube EPHTD9Gow1wTU，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
