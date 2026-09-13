---
chapter: 第 209 章
id: CH209
volume: 第10卷-openbsd的历史
---

# 第 209 章 openntpd与opensmtpd的安全工具生态

## 要点

- 本节补足 LibreSSL fork 的四层辩证链，呈现 LibreSSL 阵营对 OpenSSL 阵营批评的反批评、OpenSSL 阵营对反批评的再回应，以及二者长期演进的合图层；反批评层——LibreSSL 主导者 Ted Unangst（tedu@openbsd.org）主张“删除式清理”优于渐进改良（“Not the worst bug ever”），再回应层为 OpenSSL 阵营的路线图坚持与 CII 资金说明，合图层显示二者并存、部分理念互渗〔截断据 209.5 子节论旨补全〕openbsd.org>）于 EuroBSDCon 2014 演讲“LibreSSL: More Than 30 Days Later”中系统反
- 本节补足 OpenSMTPD 的四层辩证链，呈现 OpenSMTPD 阵营对 Sendmail 阵营批评的反批评、Sendmail 阵营对反批评的再回应，以及二者长期演进的合图层；反批评层——OpenSMTPD 主导者 Gilles Chehade 与 Eric Faurot 回应“重写风险”批评，主张配置语言与队列模型的简化即安全收益，合图层显示其便携版采用有限但在 OpenBSD 内为默认〔截断据 209.3 子节论旨补全〕ric Faurot 通过 AsiaBSDCon 2013 演讲“OpenSMTPD: We deliver !”与项目目标页面系统回应 Sen
- 本节补足 OpenNTPD 的四层辩证链，呈现 OpenNTPD 阵营对 ntpd 阵营批评的反批评、ntpd 阵营对反批评的再回应，以及二者长期演进的合图层；反批评层——OpenNTPD 主导者 Henning Brauer（亨宁·布劳尔） 主导的 ntpd 重写以“合理精度、不牺牲安全”为纲，回应“精度不足”批评，合图层显示 OpenNTPD portable 采用有限但引导了源端口随机化等实践〔截断据 209.4 子节论旨补全〕ON 04（2004-09，苏黎世）、OpenCon 2004（2004-12，威尼斯）、21C3（2004-12，柏林）三次演讲与项目目标页面
- 本节从项目史观总纲第 13 条（法律与道德是利益分配）、第 19 条（解释学循环是历史认识的根本条件）、第 21 条（革命与改革是历史方法论的分歧）切入，补充 93.10 节（从第 15、19、21 条切入）对三大 fork 辩证链的审视，重点在许可证哲学与治理机制对 fork 成败的塑造〔截断据子节论旨补全〕与利益分配维度；总纲第 13 条揭示三大 fork 的许可证选择与资金流向构成利益分配的具体显现——LibreSSL 采用 OpenSSL/IS
- LibreSSL fork 为 OpenBSD 项目响应 2014-04 OpenSSL Heartbleed 漏洞（CVE-2014-0160）的重大事件公告，须严格区分三阶段时间线——（1）Heartbleed 漏洞爆发：2014-04-07 OpenSSL 官方披露（CVE-2014-0160）；（2）fork 公告：2014-04-13 OpenBSD 导入 OpenSSL 1.0.1g 并启动 LibreSSL 清理；（3）长期演进：2014-07 LibreSSL portable 发布、2018 起 OpenSSL 转 Apache 2.0〔截断据 198.2/209.5 时间线补全〕SSL 官方发布安全公告 CVE-2014-0160，披露 Heartbleed 漏洞允许远程读取服务器内存；（2）OpenBSD fork 决

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4019] 卷“第10卷-openbsd的历史”第 209 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_4021] 卷“第10卷-openbsd的历史”第 209 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 章级史观（依 209.1-209.5 子节史观字段汇总）：OpenNTPD/OpenSMTPD/LibreSSL 三大 fork 的辩证链共同呈现“上游修复承诺与下游安全自决”的分离聚合（总纲4 分离聚合是永恒规律）；许可证与治理机制（OpenBSD Foundation 的资金中立）决定 fork 的可持续性，属利益分配结构（总纲13 法律与道德是利益分配）；“重写 vs 渐进改良”之争是革命与改革方法论的分歧在安全工具生态的再现（总纲21 革命与改革是历史方法论的分歧）。

## 辨析

- 考据过程留痕——【查证来源】Ted Unangst EuroBSDCon 2014 演讲经 <https://www.openbsd.org/papers/eurobsdcon2014-libressl.html> 一手核验，演讲中“Not the worst bug ever”、“We gutted the junk”、“apply the brakes”、"The first 30 days
- 考据过程留痕——【查证来源】OpenSMTPD 项目目标页面经 <https://www.opensmtpd.org/goals.html> 一手核验，原文明确"Be as secure as possible. Code carefully, do strict validity checks especially in the network input path, and use bound〔待核：原文截断〕
- 考据过程留痕——【查证来源】OpenNTPD 项目目标页面经 <http://www.openntpd.org/goals.html> 一手核验，原文明确"Reach a reasonable accuracy. Do not sacrifice secure design for getting that last nanosecond or obscure edge case“与”Be as
- 考据过程留痕——【查证来源】项目史观总纲第 13、19、21 条原文经 **据原文第25章.md** 一手核验；OpenNTPD 主页经 <https://www.openntpd.org/> 一手核验，明确"The software is freely usable and re-usable by everyone under a BSD
- LibreSSL fork 时间线考据须遵循 0 信任原则并以三段式呈现——【查证来源】（1）LibreSSL 官网 <https://www.libressl.org/> 经 2026-07-23 检索，载明 LibreSSL 项目基本信息但未明确标注 fork 决议日期与首次 portable 发布日期；（2）OpenSSL 2014-04-07 Heartbleed 安全公告经 OpenSS

## 文献

- Ted Unangst EuroBSDCon 2014 演讲 [EB/OL]. <https://www.openbsd.org/papers/eurobsdcon2014-libressl.html>；OpenSSL 2014-07 路线图 [EB/OL]. <https://www.openssl.org/about/>（须查互联网档案馆存档）；51CTO 2014-07-04 编译报道 [EB/OL]. <https://www.51cto.com/article/444640.html>；Linux Foundation Core Infrastructure Initiative [EB/OL]. <https://www.coreinfrastructure.org/>；Ars Technica LibreSSL PRNG 报道 [EB/OL]. <https://developer.aliyun.com/article/115394>（中文编译）；LibreSSL 邮件列表存档 [EB/OL]. <https://marc.info/?l=libressl>；BoringSSL 项目 [EB/OL]. <https://boringssl.googlesource.com/boringssl/>；openbsd.duckdb openbsd-src commit b6553af36068 [G/OL]. <https://github.com/openbsd/src/commit/b6553af36068> ［A］**LibreSSL fork 四层辩证链结构**：

| 层次 | 阵营 | 关键论据 | 时间 |
| --- | --- | --- | --- |
| 批评层 | OpenSSL 阵营 | Marquess 反思、路线图、CII 资助、PRNG 漏洞 | 2014-04 至 2014-10 |
| 反批评层 | LibreSSL 阵营 | “Not the worst bug ever”、FIONBIO/socklen_t、SRP timeline、“revolution to evolution” | 2014-09（EuroBSDCon） |
| 再回应层 | OpenSSL 阵营 | 路线图坚持改革、CII 资金流向、PRNG 质疑、BoringSSL fork | 2014-07 至 2014-11 |
| 合图层 | 各主体呈现与和解 | LibreSSL 在 OpenBSD 内成功，OpenSSL 经 CII 改善，二者部分理念互渗 | 2014-2024 |
- OpenSMTPD 项目目标页面 [EB/OL]. <https://www.opensmtpd.org/goals.html>；Eric Faurot AsiaBSDCon 2013 演讲 [EB/OL]. <https://www.opensmtpd.org/presentations/asiabsdcon2013-smtpd/>；OpenSMTPD 项目主页 [EB/OL]. <https://www.opensmtpd.org/>；CVE-2020-8794 [EB/OL]. <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8794>；OpenSMTPD 安全通告 [EB/OL]. <https://www.opensmtpd.org/security.html>；Postfix 项目 [EB/OL]. <http://www.postfix.org/>；sendmail 项目 [EB/OL]. <https://www.proofpoint.com/products/open-source/sendmail>；OpenSMTPD 手册页 **smtpd.conf(5)** [EB/OL]. <https://man.openbsd.org/smtpd.conf.5>；sendmail 手册页 **sendmail(8)** [EB/OL]. <https://man.openbsd.org/sendmail.8> ［A］**OpenSMTPD 四层辩证链结构**：
- OpenNTPD 项目目标页面 [EB/OL]. <http://www.openntpd.org/goals.html>；OpenNTPD 特性页面 [EB/OL]. <http://www.openntpd.org/features.html>；OpenNTPD 手册页 **ntpd.conf(5)** [EB/OL]. <https://man.openbsd.org/ntpd.conf.5>；Henning Brauer SUCON 04 演讲 [EB/OL]. <https://www.openbsd.org/papers/ntpd_sucon04/>；Henning Brauer OpenCon 2004 演讲 [EB/OL]. <https://quigon.bsws.de/papers/opencon04/ntpd/>；Henning Brauer 21C3 演讲 [EB/OL]. <https://quigon.bsws.de/papers/21c3/>；Network Time Foundation NTP 项目 [EB/OL]. <https://www.ntp.org/>；RFC 8915 Network Time Security [EB/OL]. <https://datatracker.ietf.org/doc/html/rfc8915>；Chrony 项目 [EB/OL]. <https://chrony.tuxfamily.org/>；OpenBSD 3.6 Release Notes [EB/OL]. <https://www.openbsd.org/36.html>；openbsd.duckdb openbsd-src commit a66b0f8292c9 [G/OL]. <https://github.com/openbsd/src/commit/a66b0f8292c9> ［A］**OpenNTPD 四层辩证链结构**：
- 项目史观总纲 [EB/OL]. 02-sacred源材料/dagang.md（总纲章）；OpenNTPD 项目主页 [EB/OL]. <https://www.openntpd.org/>；LibreSSL 项目主页 [EB/OL]. <https://www.libressl.org/>；OpenSMTPD 项目目标页面 [EB/OL]. <https://www.opensmtpd.org/goals.html>；NTP 版权声明 [EB/OL]. <https://www.ntp.org/documentation/4.2.8-series/copyright/>；OpenSSL Apache 2.0 许可证切换报道 [EB/OL]. <https://developer.aliyun.com/article/148956>（原始声明须查 OpenSSL 官方网站存档）；sendmail 项目 [EB/OL]. <https://www.proofpoint.com/products/open-source/sendmail>；Linux Foundation Core Infrastructure Initiative [EB/OL]. <https://www.coreinfrastructure.org/>；本卷 93.7-93.13 节引用的全部史料 ［A］**三大 fork 许可证与利益分配对比**：

| 项目 | fork 路线许可证 | 上游许可证 | 资金机制 | 市场结果 |
| --- | --- | --- | --- | --- |
| LibreSSL | OpenSSL/ISC | OpenSSL Apache 2.0（2018 起） | OpenBSD Foundation | OpenBSD 内默认，portable 采用率低 |
| OpenNTPD | BSD | NTP License（UoD + NTF） | OpenBSD Foundation | OpenBSD 内默认，portable 采用率不足 1% |
| OpenSMTPD | ISC | Sendmail License | OpenBSD Foundation | OpenBSD 内默认，portable 采用率不足 1% |
| OpenSSL（对比） | — | Apache 2.0 | CII/Linux Foundation | 主流市场默认 |
| NTP Classic（对比） | — | NTP License | Network Time Foundation | 高精度场景保留 |
| Chrony（对比） | — | GPL 2.0 | Red Hat 雇佣 | Linux 主流默认 |
- LibreSSL 官网 ［EB/OL］. <https://www.libressl.org/>；OpenSSL 2014-04-07 Heartbleed 安全公告 ［EB/OL］. <https://www.openssl.org/news/secadv/20140407.txt>；OpenBSD 5.6 release 页面 ［EB/OL］. <https://www.openbsd.org/56.html>；<announce@openbsd.org> 邮件列表存档 ［EB/OL］. <https://marc.info/?laccopenbsd-announce>；<misc@openbsd.org> 邮件列表存档 ［EB/OL］. <https://marc.info/?laccopenbsd-misc>；原材料/研究/考据记录/20260723_announcements-openbsd.md § 二.4.1；openbsd.duckdb openbsd-src 仓库 commits 表；本卷 93.1-93.11 节 LibreSSL 相关史料；外部基准报告：外部基准-Academic-CVE.md 第 2 节 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/外部基准-Academic-CVE.md**；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md** ［A］FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>FreeBSD 社区论文：[FP-2018-024] Forget reusability, aim for perfection: New lessons from mandoc development（Ingo Schwarze（英戈·施瓦茨），2018）<https://papers.freebsd.org/2018/bsdcan/schwarze-new_lessons_from_mandoc_development/>FreeBSD 社区论文：[FP-2017-011] A Deep Dive into FreeBSD's Kernel RNG（W. Dean Freeman and John-Mark Gurney，2017）<https://papers.freebsd.org/2017/vbsdcon/gurney-a_deep_dive_into_freebsds_kernel_rng/>FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2014-2014 年间：20,651 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP648、BSDTalk EP23（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD Foundation 2026 募款文显示资金约三分之二用于软件开发，其余用于宣传教育、基础设施与筹款管理，强调捐赠直接支撑笔记本电脑、构建测试与持续集成。（BSD Now EP648，[103.42-208.70]，L2）
- Peter N. M. Hansteen 自述 2007 年起运行 spamd 灰度陷阱，截至 2025 年 8 月陷阱条目超过 562 万、超过挪威人口，数据显示垃圾邮件活动呈下降趋势但伴随突发峰值。（BSD Now EP648，[257.02-1152.28]，L1）
- BSDCan 组织委员会回顾会议由 Dan Langille 在渥太华大学创办并连续举办 22 年，领导权经 Dan Langille、Michael W. Lucas 逐代交接，规划委员会维持约 12 人。（BSD Now EP648，[1246.88-1475.48]，L1）
- BSDCan 2026 延续教程加两天会议的形式，AV 团队与 ScaleEngine 合作向 YouTube 与 PeerTube 同步直播，并计划提高分辨率与音频质量。（BSD Now EP648，[2144.22-2315.56]，L1）
- Chris Siebenmann 以 400 余行既有 PF 规则、本地运维工具与团队知识三个理由说明从 OpenBSD PF 迁往 Linux nftables 的代价高于收益。（BSD Now EP648，[3328.02-3441.68]，L1）
- OpenBGPD 的缘起：BGP 即边界网关协议，依 RFC 定义，用于 ISP 之间互宣网络可达性——各 ISP 向对端宣告自有网络与客户网络，形成巨型对等 mesh，互联网路由表由此建立。当事人此前用当时人人使用的 Zebra，其 KAME 系代码有趣但问题多：事件模型错误、忙时会丢弃 BGP 会话、越忙越糟直至离线；他到处修改以提高可靠性，勉强可用但从未满意。某天重读 RFC 觉得并不复杂，受够之后坐下动手实现会话处理，九天后即有自认为完整可用的会话引擎（后来发现若干 bug 但基础正确）；2004 年末致信 Claudio Jeker 等相关者；此后项目稳步成长，如今已有相当多站点使用，通常比其他实现更快更可靠。（BSDTalk EP23，[333.28-490.80]，L1）
- BGP 会话保护：BGP 会话一旦丢失即告离线，会话是天然攻击面，保护至关重要而多数运维者毫无作为；TCP MD5 签名对任务而言可用但不优秀、聊胜于无；其他实现从不支持，因为问题的另一半在内核、只在应用层处理便失去意义。OpenBSD 很早实现了健壮的 TCP MD5，另提供他处不易获得的 IPsec，并自称是唯一以 isakmpd 做动态密钥 IPsec 的实现——其场景下零配置：拷贝密钥、启动 isakmpd，bgpd 自行完成其余协商。（BSDTalk EP23，[501.80-561.84]，L1）
- 随机化哲学：对 TCP、IP 及其上层协议，寻找 RFC 要求插入时间戳等半静态信息之处并验证能否以完全随机值替代——如完全随机的临时源端口（OpenBSD 随机选取，据其所知其他系统均为单调递增）；当年即知是好主意却无法证明，七八年后 Paul Watson 于 2004 年发表针对长生命周期 TCP 会话的注入攻击研究，随机源端口使此类攻击难得多，七年后才终于明白当初为何那样做。进程 ID、IP ID、初始序列号、DNS 查询 ID 皆正确随机化。所有需要随机数的子系统调用 arc4random 从内核熵池取数，众多来源使取数时机本身不可预测，即便熵池被单调计数器稀释仍能保持良好随机性。安全始终在开发者的头脑中：寻找可随机化之处、三思暴露什么——例如默认 Apache 1.3 暴露版本指纹，他们不删除该信息而以随机值替代。（BSDTalk EP23，[572.24-816.16]，L1）
- blob 批评（3.9 发布主题）：blob 即二进制大对象——硬件厂商隐瞒硬件 API 实属愚蠢，以太网芯片数十种、技术早已无秘密；厂商不给文档只给链接进内核的目标文件（NVIDIA 在此恶名昭著）。后果有三：内容不可知、可能藏有恶意；绑死厂商愿支持的架构，x86 目标文件无法用于 AMD64、SPARC64 或 alpha；厂商对系统影响力过大，且在内核空间运行不可信代码使安全问题遍地。这与二十年前伯克利清除 AT&T 专有代码是同一本质问题——依赖大公司，而公司利益很少与自由社会一致；为 OpenBSD 维护 blob 不可接受，直接给出文档即可；此前争取无线芯片组文档的成功是可行先例。（BSDTalk EP23，[913.68-1058.02]，L1）
- PF 取代 IPF 的始末：IPF 作者以所谓澄清为名修改许可证（当事人认为原措辞本就意在让人误读），最终明确禁止发布修改版——荒谬之处在于 IPF 问题不断、OpenBSD 修复过其中一些，许可证却禁止发布修复；意识到后一天之内 IPF 即被移出树。许可证只是压垮骆驼的最后一根稻草，此前对 IPF 早已不满；Daniel Hartmeier 随之起手编写 PF，3.0 首个随带 PF 的发布虽功能不及 IPF 全、大规模部署有问题，但已相当可用；长期看，其他曾用 IPF 的系统纷纷导入 PF，大量 IPF 用户在其他操作系统上也转向 PF，如今 PF 强大得多、其他系统基本皆已改用 PF。（BSDTalk EP23，[1059.82-1167.26]，L1）

**史料**：

- Peter N. M. Hansteen 博客《18 years of grey trapping》及历年陷阱数据文件。（BSD Now EP648，[257.02-1152.28]，L1）
- FreeBSD Foundation 由 Deb Goodkin 署名的年度募款文章 Powering the Future of BSD。（BSD Now EP648，[103.42-208.70]，L2）
- BSDCan 2026 组织委员会 Pat、Peter、Michael 访谈。（BSD Now EP648，[1226.50-2782.18]，L1）
- OpenBSD 开发者 Henning Brauer（21 岁，汉堡，经营 webhosting 公司/ISP）一手访谈：1999 或 2000 年因 Linux 问题与同事介绍而入坑；自称第一个较大规模试用 PF 之人，初期惨淡、与 Daniel Hartmeier 长谈修复后加入项目，现负责网络栈、PF、OpenBGPD、OpenNTPD 及树内各处；公司 ISP 基础设施（webhosting、邮件、DNS、路由与大量 BGP 节点）全跑 OpenBSD；OpenBGPD 开发史；TCP MD5 与 isakmpd 动态密钥 IPsec；随机化哲学与 Paul Watson 攻击研究的印证；3.9 发布流程与 blob 主题；生产环境大量非 i386 架构（SPARC64 服务器、alpha、VAX 时间服务器、68K/88K、HP300，其工作站为 SPARC）；桌面亦全面使用（FVWM、MG 编辑器，家人亦用）；捐赠生态与 CD 封面撤名；对未来工作的展望（包工具与网络栈）。（BSDTalk EP23，[212.60-1447.84]，L1）

**史观**：

- 总纲10 动手者创造历史：总纲10 动手者创造历史：Hansteen 以十八年持续运维累积的灰度陷阱数据，记录的是不被聚光灯照到的反垃圾邮件一线工作。（BSD Now EP648，[257.02-1152.28]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：BSDCan 领导权在代际之间交接、规划委员会持续吸纳新人，体现社区组织的聚合与再分配。（BSD Now EP648，[1382.64-1467.34]，L1）
- 总纲9 经验优先：总纲9 经验优先：Siebenmann 从自身运维规则集与工具链出发评估防火墙迁移，而非依赖抽象性能宣传。（BSD Now EP648，[3368.44-3441.68]，L1）
- 总纲13 法律与道德是利益分配：IPF 许可证事件是法律文本作为利益分配工具的微观标本：作者以所谓澄清之名调整措辞，修改词序之间软件能否被修复、能否随系统发布即被重新划定——一条许可证条款的改写直接决定了一条防火墙代码在树中的存亡，技术问题最终由法律文本的措辞裁决。（BSDTalk EP23，[1077.06-1112.62]，L1）

**辨析**：

- 转录将 Peter N. M. Hansteen 误记为 Peter N.M. Hanstein，且陷阱总数 17,8238 的数字断词存疑，须对照原文与数据文件。　[存疑脚注] 人名与统计数字存在语音转写歧义，须以原文与数据文件核验（BSD Now EP648，[997.58-1005.20]，L4）
- 转写讹误提示：受访者名讹作 Brower（通行拼写为 Henning Brauer），isakmpd 讹作 iSarKMPD，NVIDIA 讹作 Vidya，RFC 讹作 RCS，KAME 记作 Japanese project，Paul Watson 演讲名与会议名存疑（转写 Sleeping the Window 与 Kansas Agrest 2004 无法确证），OpenNTPD 讹作 op-menti PD，多处数字与设备名含混；引用本访谈的专名与文献信息前须逐一核对。[存疑脚注] 专名讹误与存疑处较多，需对音核实。　[存疑脚注] 人名、项目名、会议名与演讲名多处讹误或无法确证，引用前需对音核实。（BSDTalk EP23，[203.60-1466.70]，L5）

**文献**：

- [BSD Now EP648] Pennington J. BSD Now: 648: Greytrapping for years[EB/OL]. (2026-01-29)[2026-08-15]. <https://www.bsdnow.tv/648>.
- [BSDTalk EP23] Backman W. BSDTalk: 23: bsdtalk023 - Interview with OpenBSD developer Henning Brauer[EB/OL]. (2006-03-10)[2026-08-27]. <https://archive.org/details/bsdtalk023>.

<!-- /PODCAST_REVIEW -->
