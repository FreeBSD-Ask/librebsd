---
chapter: 第 261 章
id: CH261
volume: 第13卷-bsd衍生操作系统
---

# 第 261 章 pfsense-opnsense

## 要点

- pfSense 由 Chris Buechler 与 Scott Ullrich 于 2004 年 9 月自 Manuel Kasper 的 m0n0wall（FreeBSD 嵌入式防火墙）分叉而来，目标是克服 m0n0wall 作为嵌入式系统的可扩展性局限——m0n0wall 功能强大但受限于嵌入式形态，pfSense 旨在提供更完整的 FreeBSD 防火墙发行版；pfSense 沿用 FreeBSD 的 `pf`/`ipfw`、Packet Filter 与 Web 管理，并由 BSD Perimeter（后更名为 Netgate）提供商业支持，是 FreeBSD 在网络防火墙领域的主导产品。m0n0wall 项目于 2015 年 2 月 15 日由 Manuel Kasper 宣布永久终止，Manuel Kasper 在终止公告中鼓励 m0n0wall 用户迁移至 OPNsense，标志 BSD 防火墙谱系中 m0n0wall 时代的终结与 pfSense/OPNsense 双雄格局的最终形成。
- pfSense/OPNsense 依赖 FreeBSD 网络栈贡献者与各自社区；Manuel Kasper（瑞士）、Deciso 团队（荷兰）属非英美贡献者。
- freebsd.duckdb 查询显示 pfsense-src 仓库共 929 条 CVE 相关 commit、567 个去重 CVE，merge commit 比例在 2016 年为 2.3%（661/28,813）、2017 年 2.4%（629/26,654）、2022 年 1.3%（133/10,179），长期维持在 1-3% 水平，显著低于 hardenedbsd-src 同期 24.3% 的 merge commit 比例。
- 2019 年 5 月 19 日，opnsense-core 仓库记录了 CVE-2019-11816 的修复 commit `03c75f71be88d4d2d930c217377b5ff23f0ecae7`（author Ad Schellevis，committer Franco Fichtner），subject 为 “system: address CVE-2019-11816 privlege”（原文拼写如此，应为 privilege）。

## 史料

- m0n0wall 项目档案（Manuel Kasper 项目存档，含 2015-02-15 终止公告）；pfSense/OPNsense 官方文档与发布记录 ［A］

## 史观

- 总纲第 4 条——分离聚合是永恒规律：pfSense 自 m0n0wall 分叉（2004）、OPNsense 又自 pfSense 分叉（2015），是 BSD 防火墙谱系持续分离聚合的典型；m0n0wall 2015 年终止引导用户迁移 OPNsense，完成谱系的再聚合。
- 总纲第 10 条——动手者创造历史：防火墙发行版的演进由 Chris Buechler、Scott Ullrich、Ad Schellevis 等动手者的具体 commit 与安全修复推动，非抽象的“产品线”演化。
- 总纲第 22 条——知识注定过时：m0n0wall 时代的嵌入式防火墙形态被 pfSense/OPNsense 迭代，CVE 修复的持续积累表明安全知识必须持续更新。

## 辨析

- pfSense 与 m0n0wall 的分支关系时间点（2004）须以项目历史核实；openbsd.duckdb 查询 L7.1.1.pfsense-src 的 commit 量须警惕 fork 分歧识别局限——pfsense-src 仓库 1993 年起的 commit 是 fork 自 FreeBSD 继承的上游历史，非 pfSense 项目本地 commit，识别 pfSense 本地特有 commit 须通过 merge commit 与 parent_hashes 交叉验证，不可仅凭时间戳判定。
- 市场份额须以独立报告（一手来源）核实；“BSD 防火墙在开源市场统治”的判断须警惕社区叙事偏差——pfSense/OPNsense 的社区声誉可能被放大为市场份额优势，实际部署数据须以第三方调研为准；IPFire 与 Untangle 的技术细节（内核版本、过滤框架）须以其官方文档核实，不得仅凭一般认知推断。
- pfsense-src 的 567 个去重 CVE 须区分 “继承自 FreeBSD 上游的修复” 与 “pfSense 本地特有 commit”——fork 仓库的 commit 历史包含上游继承部分，识别本地特有 commit 须通过 merge commit 与 parent_hashes 交叉验证，不可仅凭时间戳判定；merge commit 比例低不必然意味着安全修复滞后，须与 Netgate 的官方安全公告及发布记录交叉验证。
- CVE-2019-11816 的具体技术细节（权限提升路径）须以 NVD 条目与 OPNsense 官方公告为据，commit subject 中的 “privlege” 为原 commit 中的拼写错误（应为 “privilege”），本节保留原始 subject 文本不篡改；opnsense-core 的 4 个去重 CVE（CVE-2019-11816、CVE-2026-49131 等共 4 个〔其余编号待回源〕）的修复轨迹须逐条核对。

## 文献

- pfSense 官方文档；m0n0wall 档案；freebsd.duckdb 查询 L7.1.1.pfsense-src（pfsense-src 仓库 merge commit 比例时间序列，2004-2026）；freebsd.duckdb 查询 L1.1.1（pfsense-src 仓库每年 commit 量时间序列）；〔原引用内部路径 `原材料/研究/bsd 仓库分析/数据分析/衍生项目与跨项目对比分析.md` §L7.1、`原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md` §L1.1.1 现断链，待回源定位〕。 ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2004-2014 年间：433,494 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 项目档案；bsd_derivatives.duckdb。 ［A］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 2014-2026 年间：484,691 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- 各防火墙厂商资料；IPFire 官方文档；Untangle 官方文档；Cisco ASA 文档；Fortinet FortiGate 文档。［B］

<!-- DB_REF:bsd_derivatives.duckdb -->
> **数据库引用（bsd_derivatives.duckdb）**：本子节对应 bsd_derivatives 代码仓库。> 1985-2026 年间：963,557 次提交。> 仓库总览：963,557 次提交，9,744 位贡献者（contributors 表行数，1985-06-13 至 2026-08-24）。
- bsd_commits.duckdb 查询 pfsense-src CVE commit（929 条，567 去重 CVE，2026-07-23）；bsd_commits.duckdb 查询 L7.1.1.pfsense-src；〔原引用内部路径 `原材料/研究/bsd漏洞史/数据库提取/pfsense-src-cve-commits.md`、`原材料/研究/bsd仓库分析/数据分析/衍生项目与跨项目对比分析.md` §L7.1 现断链，待回源定位〕。 ［B］
- freebsd.duckdb 查询 opnsense-core CVE commit（8 条，4 去重 CVE，2026-07-23）；NVD. CVE-2019-11816 [EB/OL]. <https://nvd.nist.gov/vuln/detail/CVE-2019-11816>（访问日期 2026-07-23）；〔原引用内部路径 `原材料/研究/bsd漏洞史/数据库提取/opnsense-core-cve-commits.md` 现断链，待回源定位〕。 ［B］
- FreeBSD 社区论文：[FP-2020-021] How an Australian IaaS uses FreeBSD（Ruben Schade，2020）<https://papers.freebsd.org/2020/linux.conf.au/schade_how_an_australian_iaas_uses_freebsd/>
- FreeBSD 社区论文：[FP-2019-045] FreeBSD and the absurdities of security compliance（Eirik Øverby，2019）<https://papers.freebsd.org/2019/eurobsdcon/oeverby-freebsd_and_the_absurdities_of_security_compliance/>
- FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>
- FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1985-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP21、BSDTalk EP255（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 10.0 于 2014 年 1 月发布，此前经历 Alpha、Beta 与多个 RC；主持人强调 10.0 经过大量测试，以降低“.0 版本”的历史风险。（BSD Now EP21，[5624.00-5655.20]，L2）
- 采访 FreeBSD 安全官 Colin Percival：SSH 私钥加密由基于 MD5 的 crypt 改为 bcrypt 作为密钥派生函数，显著提高抵御暴力破解的难度；iSCSI target 在 10.0 中被认为可用于生产。（BSD Now EP21，[531.18-545.14]，L1）
- m0n0wall 1.81 发布，为面向嵌入式设备的 BSD 防火墙发行版；pfSense 于 2004 年自 m0n0wall 分叉，面向普通 PC 且开发更活跃。（BSD Now EP21，[4455.30-4530.00]，L2）[订正：原 [4458.98-4516.38]，2026-09-30 SenseAudio 重转核对]
- NTPD 被发现可利用欺骗 UDP 包返回放大响应而充当 DDoS 放大器，FreeBSD 与 pfSense 均通过安全公告与配置更新进行缓解。（BSD Now EP21，[4540.34-4636.46]，L2）
- PC-BSD 10.0 随 FreeBSD 10 发布，RC4 支持 Wine 与 9.2 升级保留 PBI；因 FreeBSD 10 的 ABI 变化，升级需重建或重装全部包。（BSD Now EP21，[4751.26-4801.10]，L2）
- 主持人自述其所在的三镇联合学区于 2015 年暑期将防火墙整体迁移至 pfSense：选择暑期低峰窗口执行，理由是“不能在飞机飞行途中修理引擎”；上线后每台防火墙承载逾千用户，运行平稳；安装直接，主要工作量在于将旧防火墙的手写配置笔记转译为 pfSense 的规则与 NAT 写法。（BSDTalk EP255，[80.68-148.68]，L1）
- 其对 pfSense 技术层面的评价：底层 PF 的规则语法可读性好，但 pfSense 为完成自身工作会自动生成大量规则，命令行下经 PF 工具查看可达数页，多数并非管理员手写；质量图（丢包等监测）、一键式包管理与 Web 界面广受其团队好评，团队无需正式培训即可上手，整体运行被形容为“bulletproof”。（BSDTalk EP255，[149.5-250.56]，L1）
- 2015 年 8 月 BSD 社区公布 Next BSD 项目；主持人在网络论战升温之前引导听众回看 2014 年 MeetBSD California 上 Jordan Hubbard 的演讲“The Next 10 Years of BSD”以理解项目动机，并指出 Next BSD 当时仅有承载基础信息的网站。（BSDTalk EP255，[253.56-296.80]，L2）

**史料**：

- 本期史料包括 Colin Percival 访谈（当事人自述）、FreeBSD 10.0 发布与安全公告、m0n0wall 1.81 与 pfSense 谱系记录及 RUBSD 会议录像。（BSD Now EP21，[531.18-545.14]，L1）
- 该期指认的一手材料：2014 年 MeetBSD California 会议 Jordan Hubbard 演讲视频“The Next 10 Years of BSD”（载于 Meet BSD California 网站），被主持人视为理解 Next BSD 项目动机的原始出处；另有 Next BSD 官方网站的基础信息页。（BSDTalk EP255，[270.66-292.36]，L2）

**史观**：

- 总纲第 22 条 知识注定过时：SSH 旧密钥派生函数因安全进展被 bcrypt 取代，既有加密方法随攻防演进而过时。（BSD Now EP21，[531.18-545.14]，L1）
- 总纲第 10 条 动手者创造历史：Colin Percival 等安全工程师以具体维护与发布工作维持 FreeBSD 的安全响应体系。（BSD Now EP21，[5585.30-5655.60]，L1）[订正：原 [5597.60-5655.20]，2026-09-30 SenseAudio 重转核对]
- 总纲第 3 条 不存在进步，只有权力再分配：安全机制的替换体现攻防双方能力的再分配，而非简单的线性安全进步。（BSD Now EP21，[4540.34-4636.46]，L2）
- 总纲6 和解优于斗争：主持人明确呼吁 BSD 社区勿围绕 Next BSD 重演 Linux/systemd 式的论战机器，而应把它当作有意思的项目看待，检验哪些部分可用、哪些行不通，并声明珍视任何人引入新技术或做概念验证的意愿——以和解与实验检验取代立场斗争。（BSDTalk EP255，[303.40-334.52]，L1）

**辨析**：

- bcrypt 较 MD5 安全五亿倍为主持人粗略换算，需以密码学文献为准；m0n0wall 与 pfSense 的分叉年份及 iSCSI target 的生产就绪判断均为访谈与主持人口径。 [存疑脚注] 分叉年份与安全倍数表述需以项目发布记录和密码学原始文献复核。（BSD Now EP21，[536.90-552.02]，L4）
- Next BSD 在本期播客发布时仅有网站基础信息，无公开技术细节；该项目的后续走向、技术路线及其与 FreeBSD 的关系在本期内无法确证，需另行考据。 [存疑脚注] Next BSD 项目信息在本期仅有主持人转述与网站指引，项目实质内容待外部史料验证。（BSDTalk EP255，[290.34-296.80]，L4）

**文献**：

- [BSD Now EP21] Pennington J. BSD Now: 21: Tendresse for Ten[EB/OL]. (2014-01-22)[2026-08-15]. <https://www.bsdnow.tv/21>.
- [BSDTalk EP255] Backman W. BSDTalk: 255: bsdtalk255 - A quick update[EB/OL]. (2015-08-31)[2026-08-27]. <https://bsdtalk.blogspot.com/2015/08/bsdtalk255-quick-update.html>.

<!-- /PODCAST_REVIEW -->

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 pfSense/OPNsense 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-365 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-365`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者仅提及项目支持 TLS 1.2，但该项目的 TLS 支持实际可达 1.3。（转写音作 TLs）（YouTube EPByvSwhCl8k8，[243.2-255.35]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-316 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-316`；w172 YouTube 章节路由采纳）

据〔pfSense 网络边缘冗余讲座〕讲者 Chris Buechler 口述：pfSense 使用 IPFW 实现 captive portal 功能。（YouTube EPaElQidbWUxA，[284.8-287.28]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-315 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-315`；w172 YouTube 章节路由采纳）

据〔pfSense 网络边缘冗余讲座〕讲者 Chris Buechler 口述：pfSense 1.2.2 基于 FreeBSD 7.0 基本系统构建。（YouTube EPaElQidbWUxA，[454.12-456.469]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-389 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-389`；w172 YouTube 章节路由采纳）

据〔2010 NYCBSDCon〕讲者 Chris Buechler 口述：当时 pfSense 稳定版为 1.2.8.3，基于 FreeBSD 7.2；2.0 beta 基于 FreeBSD 8.1，即将进入 RC1。（YouTube EPckesvwkNiJE，[897.2-913.6]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-390 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-390`；w172 YouTube 章节路由采纳）

据〔2010 NYCBSDCon〕讲者 Chris Buechler 口述：pfSense 立项评估时，OpenBSD 尚无 WPA 与 WPA2 支持，且没有加入计划。（YouTube EPckesvwkNiJE，[394.3-422.1]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-924 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-924`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Mariusz Zaborski 口述：FreeBSD 有两个主要文件系统，分别是 ZFS 与 NewFS（转写音作 new FS）。（YouTube EPry_TNXz-A2E，[466.509-473.629]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1413 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1413`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Richard Bejtlich《用 FreeBSD 做网络安全监测》演讲〕讲者口述：其判定思路是从主机自身视角出发——在用户机上查不到 rootkit 痕迹，并不能据此认为主机安全；真正的结论来自 FreeBSD 传感器侧的独立观察，传感器所呈现的状况才足以让他断定“这里出了问题”。（YouTube EPUM4ZrsOjmNQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1414 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1414`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Richard Bejtlich《用 FreeBSD 做网络安全监测》演讲〕讲者口述：他于 2000 年开始在单位使用 FreeBSD，起因是当时为 ASERT 编写网络监测传感器（ASERT 讲者转写作 "ASM sensors"）的开发者认为，要取得良好的网络栈，应选用 BSD 基底的系统而非 Linux。（YouTube EPUM4ZrsOjmNQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1415 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1415`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Richard Bejtlich《用 FreeBSD 做网络安全监测》演讲〕讲者口述：其选择 FreeBSD 的操作层面理由之一是，他认识 FreeBSD 的网络栈开发者，遇到网络问题可直接与之沟通； FreeBSD 当时在研的零拷贝（zero-copy）工作对其流量采集很有助益。（YouTube EPUM4ZrsOjmNQ，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2385 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2385`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03A 报告·Mariusz Zaborski〕讲者口述：他们在 FreeBSD 安全设备上有三种可选的加密手段——GBDE、GELI 与 ZFS 原生加密；他称截至该报告时 FreeBSD 仍没有原生 ZFS 加密，未来新建设备时可以再考虑采用。（YouTube EPp1L2oOIkNI0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2386 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2386`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03A 报告·Mariusz Zaborski〕讲者口述：支持工程师要在设备上登录或改动之前，公司规定必须先创建快照，弄坏了就回滚，一切恢复正常；他称这是快照非常实用的运维用途。（YouTube EPp1L2oOIkNI0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2387 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2387`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03A 报告·Mariusz Zaborski〕讲者口述：出于希望机器出问题时仍能进入、并能重置到不含客户数据状态的考虑，他们决定采用 GELI，并在其上用 UFS 存放客户数据。（YouTube EPp1L2oOIkNI0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2388 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2388`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔P03A 报告·Mariusz Zaborski〕讲者口述：他自称 Capsicum 是自己最喜欢的话题；进程进入 capability 模式后访问不到任何全局实例——不能新建连接、不能打开文件，“干不了任何可疑的事”。（YouTube EPp1L2oOIkNI0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
