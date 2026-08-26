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

- 各 BSD 项目 Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>、https://www.freebsd.org/releases/；bsd_commits.db tags 表；Linux 发行版统计[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2005-2012 年间：711,435 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- OpenSSL 与 LibreSSL Release Notes [EB/OL]. <https://www.openssl.org/news/>、https://www.libressl.org/；Linux 与 BSD 发行版编译器记录；bsd_commits.db openbsd-src 仓库 ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- bsd_commits.db openbsd-src 仓库 commit b6553af36068、84938a7b9c57、1c93e2863e3b；OpenSSL 1.1.0 Release Notes [EB/OL]. <https://www.openssl.org/news/openssl-1.1.0-notes.html>；LibreSSL 官方文档 [EB/OL]. <https://www.libressl.org/>；Ted Unangst EuroBSDCon 2014 演讲 [EB/OL]. <https://www.openbsd.org/papers/eurobsdcon2014-libressl.html>；LibreSSL Project Goals [EB/OL]. <https://www.libressl.org/goals.html> ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- openbsd.db openbsd-src 仓库；NVD CVE-2012-1667/CVE-2012-2978/CVE-2012-2979/CVE-2012-5195/CVE-2013-4547/CVE-2014-3956/CVE-2014-7844/CVE-2015-8605/CVE-2015-8607/CVE-2016-0718/CVE-2016-1238；OpenBSD 5.x errata patches [EB/OL]. **<https://www.openbsd.org/errata.html>** ［A］<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- OpenBSD 官网 release 页面 ［EB/OL］. <https://www.openbsd.org/{50-59}.html>；announce@openbsd.org 邮件列表存档 ［EB/OL］. <https://marc.info/?l=openbsd-announce>；原材料/研究/考据记录/20260723_announcements-openbsd.md § 二.2 与 § 二.4.2；bsd_commits.db openbsd-src 仓库 ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/><!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
