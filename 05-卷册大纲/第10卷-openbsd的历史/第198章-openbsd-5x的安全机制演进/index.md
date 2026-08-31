---
chapter: 第 198 章
id: CH198
volume: 第10卷-openbsd的历史
---

# 第 198 章 openbsd-5x的安全机制演进

## 要点

- 2005-2012 年间各 BSD 项目与 Linux 的发布数据与市场份额是研究 BSD 边缘化的核心史料；FreeBSD Release 周期约 18-24 个月，OpenBSD 6 个月，NetBSD 不规律；Linux 发行版市场份额远超 BSD，但 BSD 在服务器、嵌入式、安全领域仍有存在感
- gcc→clang 替代与 OpenSSL→LibreSSL fork 的合图层论点包含三个历史定位。第一是 LibreSSL 与 OpenSSL 并存至今的历史结果——OpenSSL 在 Heartbleed 后启动 LibreSSL 之外的改革（OpenSSL 1.1.0 重构），LibreSSL 推动 OpenSSL 改进但未完全替代，证明 fork 是双轨而非替代；第二是 gcc 与 cl
- 从总纲第 21 条“革命与改革是历史方法论的分歧”切入，GNU/OpenSSL 阵营的再回应本身也呈现革命与改革的交织。OpenSSL 1.1.0 重构是“革命性重构”（API 简化、master 头文件引入、线程安全改进）嵌入“渐进性改革”路径——OpenSSL 项目在 Heartbleed 后选择渐进改进（2014-2016 年持续修复 CVE），但 1.1.0 版本的重构规模具有革命性（移除
- OpenBSD 5.x 时期除 OpenSSL 外的基本系统组件漏洞分散于 BIND、DHCP、expat、nginx、sendmail 等——CVE-2012-1667（BIND 拒绝服务，sthen 从 ISC BIND 回溯修复，commit `4ca673f3df5d9679d1d3bdb337a97b8ceec3e666`，2012-06-06，无 CVSS v3 评分，技术机制类型为拒
- OpenBSD 5.x 时期共发布 10 次 release（5.0 至 5.9）；5.0-5.8 严格遵循 5 月/11 月发布周期，5.9（2016-03-29）打破 5 月/11 月传统改为 3 月发布——此为 OpenBSD 发布周期的重要调整，5.9 引入 **pledge(2)** 系统调用用于进程权限限制，release 日期调整与 pledge(2) 引入相关；5.x 时期 rel

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3897] 卷“第10卷-openbsd的历史”第 198 章，匹配置信度 folder，原因：folder 第196章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 市场份额统计无权威数据源——DistroWatch 排名仅反映桌面用户关注度，不反映服务器部署；BSD 实际部署规模以厂商报告（如 Juniper JunOS 基于 FreeBSD、NetApp ONTAP 基于 FreeBSD）与调查为准 [考据完成：2026-07-28 BSD 实际部署规模无单一权威统计，厂商报告仅覆盖商业用户]
- 考据过程留痕——【查证来源】LibreSSL 与 OpenSSL 的并存状态以两项目当前 Release Notes（<https://www.openssl.org/news/> 与 <https://www.libressl.org/>）与部署统计为来源——OpenSSL 仍是多数 Linux 发行版与商业产品的默认 TLS 库，LibreSSL 是 OpenBSD 默认 TLS 库并被部分其
- 革命与改革的交织须以 bsd_commits.db openbsd-src 仓库 commit log 的代码级证据为基准——LibreSSL fork 后的渐进性改革（2014-04-13 至 2014-04-14 代码清理 commit、2014-07-12 后持续演进）与 OpenSSL 1.1.0 的革命性重构（2016.9 移除 SSLv2/SSLv3 默认支持）在时间上形成对照，证明革
- CVE-2013-4547 的 nginx 认证绕过具体利用路径须对照 nginx 安全公告核验——涉及 URI 解析与 location 匹配；CVE-2015-8605 的 DHCP 拒绝服务是否影响 OpenBSD 默认配置须核验——是否需要特定 DHCP 选项；CVE-2016-0718 的 expat 缓冲区溢出在 OpenBSD 基本系统中的暴露面须考据——哪些程序链接 expat
- RELEASE 公告日期与 release song 标题的考据须遵循 0 信任原则并以三段式呈现——【查证来源】（1）OpenBSD 官网各版本 release 页面（如 <https://www.openbsd.org/50.html> 至 59.html）经 2026-07-23 检索，记载各版本 release song 标题；（2）<announce@openbsd.org> 邮件列表存

## 文献

- 各 BSD 项目 Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>、<https://www.freebsd.org/releases/；bsd_commits.db> tags 表；Linux 发行版统计[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2012 年间：711,435 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- OpenSSL 与 LibreSSL Release Notes [EB/OL]. <https://www.openssl.org/news/>、<https://www.libressl.org/；Linux> 与 BSD 发行版编译器记录；bsd_commits.db openbsd-src 仓库 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- bsd_commits.db openbsd-src 仓库 commit b6553af36068、84938a7b9c57、1c93e2863e3b；OpenSSL 1.1.0 Release Notes [EB/OL]. <https://www.openssl.org/news/openssl-1.1.0-notes.html>；LibreSSL 官方文档 [EB/OL]. <https://www.libressl.org/>；Ted Unangst EuroBSDCon 2014 演讲 [EB/OL]. <https://www.openbsd.org/papers/eurobsdcon2014-libressl.html>；LibreSSL Project Goals [EB/OL]. <https://www.libressl.org/goals.html> ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- openbsd.db openbsd-src 仓库；NVD CVE-2012-1667/CVE-2012-2978/CVE-2012-2979/CVE-2012-5195/CVE-2013-4547/CVE-2014-3956/CVE-2014-7844/CVE-2015-8605/CVE-2015-8607/CVE-2016-0718/CVE-2016-1238；OpenBSD 5.x errata patches [EB/OL]. **<https://www.openbsd.org/errata.html>** ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 官网 release 页面 ［EB/OL］. <https://www.openbsd.org/{50-59}.html>；<announce@openbsd.org> 邮件列表存档 ［EB/OL］. <https://marc.info/?laccopenbsd-announce>；原材料/研究/考据记录/20260723_announcements-openbsd.md § 二.2 与 § 二.4.2；bsd_commits.db openbsd-src 仓库 ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/><!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP23、BSD Now EP22、BSD Now EP19（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Ted Unangst 自述约 2000 年接触 OpenBSD 并因其稳定性成为用户，此后 11 年担任 OpenBSD 开发者，因提交大规模 VFS 锁修复 diff 而获得 commit 权限。（BSD Now EP23，[728.56-800.12]，L1）
- signify 是仅用于密码学签名与校验的简单工具，不含加密功能；自 2013 年 12 月 21 日开发，Ted Unangst 为主要作者，Marc Espie 编写包工具集成，Alexander Hall 编写安装器部分。（BSD Now EP23，[898.44-1006.76]，L1）
- OpenBSD 自 5.5 起以 signify 签名基础发行集与第三方包，采用 SHA256.sig 签名校验和清单；使用单一密钥而非 PKI 信任链，公钥检入源码库并经邮件列表扩散。（BSD Now EP23，[934.36-1387.66]，L1）
- FreeBSD Foundation 2013 年筹款总额为 768,562 美元，来自约 1,659 名捐赠者，并已启动 2014 年百万美元目标。（BSD Now EP23，[76.32-139.56]，L2）
- 教程演示自建 NTP 服务器，并报道 OpenBSD 在 BeagleBone Black 上的 ARMv7 移植经验，涉及不同存储选项与已知问题的规避。（BSD Now EP23，[428.10-474.86]，L2）
- George Neville-Neal 自述早期在加州大学做软件基础设施支持并结识 CSRG，后参与 NetBSD 笔记本移植，最终长期使用 FreeBSD，并担任 FreeBSD Foundation 董事与 committer。（BSD Now EP22，[1375.20-1461.06]，L1）
- FreeBSD Journal 由 FreeBSD Foundation 资助一年，为双月刊纯电子杂志，经 Kindle、Google Play 与 Apple 应用商店发行；编委会包括 John Baldwin、Kirk McKusick、Robert Watson、Michael Lucas、Hiroki Sato 等。（BSD Now EP22，[1641.94-1716.58]，L1）
- 创刊号以 FreeBSD 10 为主题，收录 David Chisnall 论 Clang、John Baldwin 论内核 sysctl 节点、Tim Kientzle 论 BeagleBone Black 及 Alan Jude 论 ZFS 等文章，并设 ports 报告与 SVN 更新等固定栏目。（BSD Now EP22，[1801.70-1917.06]，L1）
- 教程演示 OpenBSD 5.4 的 errata 补丁应用，以及从 CVS 检出 current/stable、先升级内核再升级 userland 的自建流程，强调遵循官方补丁说明以避免系统损坏。（BSD Now EP22，[3009.78-3553.32]，L2）
- FreeBSD 2013 年第四季度状态报告涵盖 EC2（Colin Percival）、Xen（Justin Gibbs、Roger Pau Monné）、CAM 锁与 iSCSI（Alexander Motin）及 iwn 无线驱动（Adrian Chadd）等进展。（BSD Now EP22，[383.96-451.54]，L2）
- 本期以 installfest 形式逐项演示 FreeBSD 10.0、OpenBSD 5.4、NetBSD 6.1.2、DragonFly BSD 3.6 与 PC-BSD 10.0 的安装流程，比较文本式、引导式与图形式安装器的交互差异。（BSD Now EP19，[1011.60-1046.72]，L2）
- FreeBSD 10 安装器新增键位测试、自动 root-on-ZFS、GELI 磁盘加密与 shell 安装模式，改进主要由 Devin Teske 与 Warren Block 等完成。（BSD Now EP19，[1069.32-1330.48]，L2）
- OpenBSD 在 5.4 前后提交 signify，用于签名基础发行集与第三方包，以解决此前 SHA256 校验在 X 集同步时因多机多时构建而出现的时序错配。（BSD Now EP19，[321.52-347.64]，L2）
- PC-BSD 使用 pc-sysinstall 脚本化安装器，图形安装可保存配置用于批量部署；TrueOS 为无 GUI 的服务器版本，内置 PEFS 与 Life Preserver 等命令行组件。（BSD Now EP19，[2244.04-2352.08]，L2）
- NetBSD 社区发布 pkgsrc 2013Q4；FreeBSD 侧由 Julio Merino 自 NetBSD 带入 Kyua 测试框架并搭建持续测试基础设施，以替代旧 Tinderbox 思路。（BSD Now EP19，[91.48-144.40]，L2）

**史料**：

- 本期史料包括 Ted Unangst 访谈（当事人自述）、OpenBSD signify 工具与测试密钥、FreeBSD Foundation 2013 年筹款报告、NTP 教程及 OpenBSD BeagleBone Black 移植博客。（BSD Now EP23，[713.64-1387.66]，L1）
- 本期史料包括 George Neville-Neal 访谈（当事人自述）、FreeBSD Journal 创刊号目录、OpenBSD 官方 errata 补丁与 FAQ、FreeBSD 季度状态报告及 pfSense 2.1.1 快照说明。（BSD Now EP22，[1375.20-1917.06]，L1）
- 本期史料包括 Devin Teske 与 Warren Block 的安装器改动、OpenBSD signify 提交与测试密钥、Julio Merino 的 Kyua 测试框架、pc-sysinstall 脚本化安装器及 pkgsrc 2013Q4 分支。（BSD Now EP19，[91.48-1330.48]，L2）

**史观**：

- 总纲10 动手者创造历史：总纲10 动手者创造历史：Ted Unangst、Marc Espie 与 Alexander Hall 以具体工具开发补齐 OpenBSD 发布签名空白。（BSD Now EP23，[949.00-1006.76]，L1）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：Theo 的一封邮件触发 signify 开发，当事人明确不知动机，说明安全工程由具体事件偶然推动。（BSD Now EP23，[1615.30-1651.60]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：signify 以极简设计替代 GPG 的部分用途，体现工具随需求演进而更替。（BSD Now EP23，[898.44-930.08]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：George Neville-Neal 与编委会以出版实践填补 FreeBSD 无专属杂志的空白，将社区知识沉淀为周期性出版事件。（BSD Now EP22，[1492.06-1716.58]，L1）
- 总纲9 经验优先：总纲9 经验优先：教程强调按官方补丁与更新文档操作，避免因跳过说明导致 SSH 无法启动等实际故障。（BSD Now EP22，[3492.76-3530.20]，L2）
- 总纲15 文化即形式主义：总纲15 文化即形式主义：杂志作为社区文化的形式化载体，将分散于论坛与邮件列表的知识加以编排和定期发布。（BSD Now EP22，[1500.10-1553.54]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Devin Teske、Warren Block、Julio Merino 等以具体工程改进安装器与测试基础设施，推动发行流程演进。（BSD Now EP19，[1069.32-1300.48]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：sysinstall 被 bsdconfig 与脚本化安装器取代，旧安装方式随版本演进而淘汰。（BSD Now EP19，[2238.16-2399.96]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：installfest 将五大 BSD 并置演示，体现多分支在本体论上平等对待的叙述方式。（BSD Now EP19，[1011.60-1046.72]，L2）

**辨析**：

- 当事人明确表示不知 Theo 启动签名项目的动机，且 5.5 正式签名密钥当时尚未生成；发行集签名覆盖范围（源集、ports tarball 是否签名）仍属待定。　[存疑脚注] 签名动机与最终覆盖范围以 OpenBSD 官方发布说明为准，需后续考据。（BSD Now EP23，[1615.30-1651.60]，L4）
- FreeBSD Journal 创刊号当时尚待 Apple 应用商店审批；编委会名单与创刊内容为当事人及主持人转述，需与创刊号目录核对。　[存疑脚注] 创刊号上线时间与目录以出版方最终发布为准，需交叉验证。（BSD Now EP22，[1790.86-1816.90]，L4）
- OpenBSD 5.4 时期 signify 仍为测试密钥，正式签名需待 5.5；各 BSD 安装器细节为主持人实操演示，与官方手册的一致性需逐项复核。　[存疑脚注] 安装器细节与 signify 状态以官方发布说明为准，需交叉验证。（BSD Now EP19，[321.52-347.64]，L4）

**文献**：

- [BSD Now EP23] Pennington J. BSD Now: 23: Time Signatures[EB/OL]. (2014-02-05)[2026-08-15]. https://www.bsdnow.tv/23.
- [BSD Now EP22] Pennington J. BSD Now: 22: Journaled News-Updates[EB/OL]. (2014-01-29)[2026-08-15]. https://www.bsdnow.tv/22.
- [BSD Now EP19] Pennington J. BSD Now: 19: The Installfest[EB/OL]. (2014-01-08)[2026-08-15]. https://www.bsdnow.tv/19.

<!-- /PODCAST_REVIEW -->
