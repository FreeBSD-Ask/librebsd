---
chapter: 第 176 章
id: CH176
volume: 第09卷-netbsd的历史
---

# 第 176 章 netbsd-pkgsrc的早期演进

## 要点

- NetBSD 仓库构成：netbsd-pkgsrc(1225351)、netbsd-src(774061)。pkgsrc 提交量占比最大，与 FreeBSD Ports 形成镜像

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3994] 卷“第09卷-netbsd的历史”第 176 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:references_fulltext:chapter_matches:chmatch_3995] 卷“第09卷-netbsd的历史”第 176 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:netbsd.duckdb] NetBSD 仓库构成：netbsd-pkgsrc(1225351)、netbsd-src(774061)。pkgsrc 提交量占比最大，与 FreeBSD Ports 形成镜像

## 史观

- 形式主义：pkgsrc 是‘跨平台软件包管理’的形式主义解决方案，与 FreeBSD Ports 形成镜像

## 辨析

- 移植的具体范围需考据——FreeBSD Ports 与 pkgsrc 的代码 diff 需对照源码核实。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：pkgsrc 早期发展实际涉及两位核心贡献者——agc（Alistair G. Crooks）1997-06-05 首次导入 FreeBSD packaging tool（pkg_install），1997-08-20〔存疑：本句自“1997-08-20”后截断，该日期对应事件的后续表述缺失；公开史料（netbsd.org pkgsrc 十年回顾）仅载 1997-10-03 pkgsrc 系统由 Alistair Crooks 与 Hubert Feyrer 创建，待重新实查 netbsd-src 仓库 commits 表补录〕
- commit 记录的完整性需考据——部分 commit 可能未完整记录；需对照多源档案核实。统计结论 [C-13] 局限性继承：netbsd-src 月度 commit 量 Pettitt 检验变点为 2012-04、BUISHAND R 检验变点为 2011-09（10,000 次 Monte Carlo），两检验变点年份均晚于本章覆盖时期（1997-2004）约 7-8 年，两检验变点既均落在覆盖期之外，统计结论对本章时期的 commit 量演变不具刻画力〔存疑：本句自“反映本章时期的 c”处截断，原结论文字缺失，待重新实查补录〕
- OpenBSD Ports 与 pkgsrc 的分化时间需考据——OpenBSD 1996 年 7 月 fork 后软件包管理何时完全独立需对照 commit log 核验；OpenBSD 1.1 CVS 标签日期（1995.10.18）与 OpenBSD 1.2 首次正式发行日期（1996.7）在不同来源中混用，需对照 OpenBSD 官方发布档案进一步核验。〔存疑：数据库验证过程与结论文字自“经 **netbsd.duckdb** o”处截断缺失，待重新实查补录〕
- 不可断言 pkgsrc “优于” RPM/DEB——二者服务不同生态（BSD 跨平台 vs Linux 发行版分发）。
- CVE-2002-0429 的 CVE 编号年份（2002）与修复 commit 日期（2004-03-11）相差近 2 年，反映该漏洞可能在 2002 年即被披露但修复延迟至 2004 年，或 CVE 编号系事后回溯分配——具体时序须对照 NetBSD-SA 公告与 NVD 条目核验；httpd 漏洞群（CVE-2006-2937/2940/3738/4343）由同一 commit〔存疑：commit 哈希自“897b3”处截断且反引号未闭合，完整哈希与本次修复的定性须重新实查 pkgsrc 仓库 commits 表补录〕

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 netbsd.duckdb

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-253 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-253`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：讲者指出历史上 BSD Unix 一直在自己独立的源码树内开发，涵盖内核、通用命令与配置文件。（YouTube EP5235CsD1QwQ，[199.9-210.7]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2191 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2191`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan P03B: Hardening pkgsrc - Pierre Pronchery〕讲者口述：pkgsrc 是 NetBSD 的打包软件来源，同时也运行于 SmartOS 与 MINIX（讲者表示不确定），当时共支持一万七千余个包、覆盖十余个独立平台。（YouTube EPW36UZiX4Kt0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2192 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2192`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan P03B: Hardening pkgsrc - Pierre Pronchery〕讲者口述：pkgsrc 设有两个负责团队：一个专门处理安全问题（security team），另一个是发布工程组（release engineering group）。（YouTube EPW36UZiX4Kt0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2193 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2193`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan P03B: Hardening pkgsrc - Pierre Pronchery〕讲者口述：pkgsrc 的漏洞数据库并非单一来源，而是汇集多路信息；讲者并称工单会从各来源的 RSS 与邮件列表自动创建，再由人工处理，属半自动流程。（YouTube EPW36UZiX4Kt0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2194 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2194`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan P03B: Hardening pkgsrc - Pierre Pronchery〕讲者口述：讲者介绍 RELRO 机制：在程序启动时应用重定位并将对应页设为只读，使攻击者无法覆写其中的偏移量，从而收缩攻击面；pkgsrc 现已支持该机制，讲者并称其约数年前由 OpenBSD 引入、后进到 GCC 上游。（YouTube EPW36UZiX4Kt0，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2203 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2203`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie 演讲“Is it done yet：The never ending story of pkg tools”〕讲者口述：讲者说明新版 pkg tools 把签名放在 gzip 头的注释字段里、即签名置于归档之外，使未安装 pkg tools 的一方看到的仍是完全正常的 gzip 文件。（YouTube EP7hmBgniE00s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2204 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2204`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie 演讲“Is it done yet：The never ending story of pkg tools”〕讲者口述：讲者称 OpenBSD 不采用证书链信任机制，理由是它过于复杂且常被做错，因此只要密钥被安装在正确目录中即被视为有效密钥。（YouTube EP7hmBgniE00s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2205 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2205`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie 演讲“Is it done yet：The never ending story of pkg tools”〕讲者口述：讲者称 OpenBSD 与其他操作系统的一大差别在于没有已安装内容的全局数据库，var/db/pkg 下每个已装包各占一个子目录，不存在全局数据库。（YouTube EP7hmBgniE00s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2206 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2206`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Marc Espie 演讲“Is it done yet：The never ending story of pkg tools”〕讲者口述：讲者表示主动破坏兼容性是有意决定——虽当时旧签名方式并无安全洞，仍决定正式弃用旧流程、只接受新签名；并称在 OpenBSD，安全与可用性必须二选一时一律偏向安全。（YouTube EP7hmBgniE00s，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2452 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2452`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2014《Carve your NetBSD》Pierre Pronchery、Guillaume Lasmayous 讲〕讲者口述：讲者称当时该项目同时支持两个主要发行分支，而包源码树按季度发布——即每三个月重新编译并向终端用户提供一批二进制包——下载路径中却对包树不作明示。（YouTube EPvh-TjLUj6os，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2453 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2453`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2014《Carve your NetBSD》Pierre Pronchery、Guillaume Lasmayous 讲〕讲者口述：讲者称在该 BSD 操作系统里安装第三方包不止一种工具、不止一种途径，多种包管理工具并存，对使用者高度令人困惑。（YouTube EPvh-TjLUj6os，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2454 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2454`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2014《Carve your NetBSD》Pierre Pronchery、Guillaume Lasmayous 讲〕讲者口述：讲者称包源码早在十二年前就已支持二进制包签名，但据其判断几乎从未有人使用；他一年前检查时该功能已经坏掉、完全不能工作，而这一需求仍未被修复。（YouTube EPvh-TjLUj6os，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2455 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2455`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔AsiaBSDCon 2014《Carve your NetBSD》Pierre Pronchery、Guillaume Lasmayous 讲〕讲者口述：讲者称 NetBSD 用的是 CVS——他承认这工具本身不错、自己也喜欢——但它是集中式的，厂商这类需要去中心化开发的角色很难把它当去中心化系统来用。（YouTube EPvh-TjLUj6os，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2929 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2929`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔devsetup local development environment based on pkgsrc（Pierre Pronchery, EuroBSDcon 2022）讲者口述：pkgsrc（转写音作 package shows／packet Source）是 NetBSD 的官方软件包来源，也可用于其他操作系统：NetBSD 支持 16 种架构，pkgsrc 同样覆盖，此外还支持 23 种其他操作系统（Linux 只是其中之一）。（YouTube EPR_gQ44lDlEc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2930 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2930`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔devsetup local development environment based on pkgsrc（Pierre Pronchery, EuroBSDcon 2022）讲者口述：pkgsrc 无特权（unprivileged）模式由若干变量驱动：UNPRIVILEGED 以 yes／no 开启，写进 pkgsrc 的 make 配置；UNPRIVILEGED_USER 默认为当前用户，组与所属组同理。（YouTube EPR_gQ44lDlEc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2931 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2931`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔devsetup local development environment based on pkgsrc（Pierre Pronchery, EuroBSDcon 2022）讲者口述：pkgtools 中的 rc.d server 包源自 NetBSD——本是其 init 系统中负责运行服务的部分，打包后可在任何地方利用 NetBSD 的 rc.d 系统（转写音作 net DSD）；讲者发现其在无特权模式下不受支持，遂动手修补。（YouTube EPR_gQ44lDlEc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2932 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2932`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔devsetup local development environment based on pkgsrc（Pierre Pronchery, EuroBSDcon 2022）讲者口述：讲者自建的 devsetup 把 pkgsrc 的所有包收进单一脚本管理，借 pkgsrc 约三个月一次的发布节奏（转写音作 really cycle，疑为 release cycle）获得持续更新。（YouTube EPR_gQ44lDlEc，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
