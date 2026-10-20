---
chapter: 第 210 章
id: CH210
volume: 第10卷-openbsd的历史
---

# 第 210 章 openbsd的安全至上哲学

## 要点

- OpenBSD 治理结构以 de Raadt 为单一决策核心（BDFL 模式），FreeBSD 走 Core Team 集体治理（9 人核心团队，2000 年起直选制），NetBSD 走 Foundation 董事会治理（1995 年成立）；de Raadt 自 1995-10-18 fork 之初即主导所有重大技术决策——1999-10-01 OpenSSH-1.0 commit bf74e86
- OpenBSD 长期依赖 CD 销售（每张约 50 USD，每 6 个月发行一版）、海报销售（如 posters 系列）与捐赠维持运转；2014 年 1 月因卡尔加里电费危机（约 20,000 USD/月）发出募捐公告，引发全球募捐（HTTP dues 与 Winamp 创始人 Justin Frankel 等捐赠），最终募集资金超过 100,000 USD；OpenBSD 资金模式与 FreeB
- OpenBSD 自 2.0（1997-06-01 发布）起保持每年 5 月与 11 月 6 个月固定发布周期传统——OpenBSD 7.9（2026-05-19 发布）是第 60 个 release，从未出现因外部事件推迟发布的情况（OpenBSD 各版本发布日期均见 <https://www.openbsd.org/> 各版本页面）；CD 封面艺术（每版由不同艺术家创作，如 3.4 的 Puff
- OpenBSD 生态多元群体贡献包括 de Raadt 本人（南非裔加拿大人，1968 年生于比勒陀利亚，1977 年随家移居加拿大）、Niels Provos（尼尔斯·普罗沃斯）（德国，OpenSSH 主导开发者，openbsd.duckdb openbsd-src 仓库 provos 贡献者记录）、Jun-ichiro itojun Hagino（日本，IPv6 贡献者，2007-10-29
- OpenBSD（BDFL 模式，de Raadt 单一决策，openbsd.duckdb 显示 deraadt 27181 commits 占 OpenBSD 总 245857 commits 约 11%）、FreeBSD（Core Team 9 人集体治理，2000 年起直选制）、NetBSD（Foundation 董事会治理，1995 年成立）、Linux（Linus Torvalds BDF

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3907] 卷“第10卷-openbsd的历史”第 210 章，匹配置信度 folder，原因：folder 第208章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- OpenBSD 治理结构的“独裁”性质在不同叙事中存在评价分歧——支持者列举 2014-04-14 LibreSSL fork 当日决策效率、2015-10 pledge 引入快速推进等案例；批评者列举 2003-04 DARPA 撤销约 230 万 USD 资助后项目无资金应急机制、2014-04 de Raadt 公开斥责 OpenSSL 维护者导致社区关系紧张等案例；de Raadt 个人风
- OpenBSD 资金困境的具体程度在不同叙事中存在差异——OpenBSD Foundation 年报披露的 2023 年收入约 30 万 USD 与 de Raadt 在 misc@ 邮件列表多次提及的“无法承担电费”叙事并存，须区分“项目运营资金”（CD/海报销售维持 hackathon 等）与“Foundation 接受捐赠”（用于法律/财务事务）两个口径；2014 年电费危机的具体经过是 d
- 原叙事中“2003 年因 Iraq War 推迟 3.4 发布”的说法与官方记录不符——OpenBSD 3.4 于 2003-11-01 按期发布（<https://www.openbsd.org/34.html>），与 Iraq War（2003-03-20 开始）无推迟关系；DARPA 撤资事件发生于 2003-04，亦未影响 3.4 发布；〔待核：原文截断，后文待回源〕
- 多元群体贡献的发掘基于 commit log 与邮件列表记录——de Raadt 1968 年生于南非比勒陀利亚，1977 年随家移居加拿大，其反战立场（2003-04 伊拉克战争公开言论导致 DARPA 撤销 OpenBSD 项目约 230 万 USD 资助）对项目资金结构产生长期影响；DARPA 撤资的具体时间点是 2003-04-21 前后（DARPA 项目经理 Jan Cargnelli
- 各项目治理结构的比较须避免简单褒贬——BDFL 模式在 OpenBSD 31 年历史中（1995-2026）未出现 succession 危机，但这不证明 BDFL 模式可持续，仅证明 de Raadt 个人持续活跃（openbsd.duckdb 显示其 2026-07-16 仍有 commit）；〔待核：原文截断，后文待回源〕

## 文献

- OpenBSD Foundation 文档 [EB/OL]. <https://www.openbsdfoundation.org/>；de Raadt 邮件列表发言存档 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；OpenBSD 项目主页 [EB/OL]. <https://www.openbsd.org/>；OpenBSD 项目目标 [EB/OL]. <https://www.openbsd.org/goals.html>；openbsd.duckdb 查询 L3.4.1.top10（来源：原材料/研究/bsd 仓库分析/数据分析/深层信息挖掘.md §L3.4.1.top10） ［A］**四大 BSD/Linux 治理结构对比**：

| 项目 | 治理模式 | 决策核心 | Foundation 职能 |
| --- | --- | --- | --- |
| OpenBSD | BDFL | de Raadt（1995-10-18 起） | OpenBSD Foundation（2007）仅法律/财务 |
| FreeBSD | Core Team 集体 | 9 人核心团队（2000 起直选） | FreeBSD Foundation（2000）兼法律/财务/技术 |
| NetBSD | Foundation 董事会 | 1995 年成立 | NetBSD Foundation 主导 |
| Linux | BDFL + 子系统维护者 | Linus Torvalds | Linux Foundation 雇佣全职维护者 |
- OpenBSD 募捐公告 [EB/OL]. <https://www.openbsd.org/donations.html>；2014 年电费危机 misc@ 邮件列表讨论 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；OpenBSD Foundation 财务报告 [EB/OL]. <https://www.openbsdfoundation.org/>；FreeBSD Foundation Annual Report [EB/OL]. <https://www.freebsdfoundation.org/annual-report/> ［A］**OpenBSD Foundation vs FreeBSD Foundation 财务对比（2023 年报）**：

| 维度 | OpenBSD Foundation | FreeBSD Foundation |
| --- | --- | --- |
| 2023 年收入 | 约 30 万 USD | 约 500 万 + USD |
| 资金来源 | CD/海报销售、个人捐赠 | 企业赞助（Google、Netflix、Juniper 等） |
| 全职员工 | 无 | 数十名 |
| 职能范围 | 法律/财务（不干预技术） | 法律/财务/技术资助 |
| 2014 年电费危机 | 约 20,000 USD/月，全球募捐超 100,000 USD | 无类似危机 |
- OpenBSD CD/海报艺术存档 [EB/OL]. <https://www.openbsd.org/lyrics.html>；OpenBSD Release Songs [EB/OL]. <https://www.openbsd.org/lyrics.html>；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD 3.4 Release Page [EB/OL]. <https://www.openbsd.org/34.html> ［A］**OpenBSD 6 个月发布周期关键节点**：

| 版本 | 发布日期 | 备注 |
| --- | --- | --- |
| 2.0 | 1997-06-01 | 6 个月固定周期传统确立 |
| 3.4 | 2003-11-01 | 按期发布，与 Iraq War（2003-03-20）无推迟关系 |
| 7.9 | 2026-05-19 | 第 60 个 release |
- OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；DARPA 资助撤销事件 misc@ 邮件列表讨论 2003 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；de Raadt 公开采访 [EB/OL]. <https://undeadly.org/>；OpenBSD GitHub 镜像 [EB/OL]. <https://github.com/openbsd> ［A］**OpenBSD 核心贡献者地理分布**：

| 贡献者 | 国籍/地区 | 主要贡献 | bsd_commits.duckdb 记录 |
| --- | --- | --- | --- |
| de Raadt | 南非裔加拿大人（1968 生于比勒陀利亚） | 项目主导 | 27181 commits（1995-10-18 起） |
| Niels Provos | 德国 | OpenSSH 主导 | openbsd-src provos 贡献者记录 |
| Jun-ichiro itojun Hagino | 日本 | IPv6 贡献 | contributors 表 itojun；最后 commit 2007-08-03（`44be632afd37`），2007-10-29 逝世 |
| Damien Miller | 澳大利亚 | OpenSSH portable 维护 | contributors 表 djm |
| Bob Beck | 加拿大 | LibreSSL、unveil | commit `8b23add8c74b`（2018-07-13） |
- FreeBSD Foundation 文档 [EB/OL]. <https://www.freebsdfoundation.org/>；NetBSD Foundation Bylaws [EB/OL]. <https://www.NetBSD.org/foundation/bylaws.html>；Linux Foundation Annual Reports [EB/OL]. <https://www.linuxfoundation.org/reports/>；OpenBSD Foundation 文档 [EB/OL]. <https://www.openbsdfoundation.org/> ［A］**四大 Foundation 2023 年资金规模对比**：

| Foundation | 2023 年资金规模 | 相对 OpenBSD 倍数 | 雇佣模式 |
| --- | --- | --- | --- |
| OpenBSD Foundation | 约 30 万 USD | 1.0× | 无全职员工，志愿者业余 |
| NetBSD Foundation | 约 5 万 USD | 0.17× | 无全职员工 |
| FreeBSD Foundation | 约 500 万 + USD | 16.7× | 数十名全职员工 |
| Linux Foundation | 资产超 1 亿 USD | 333× | 数十名全职内核维护者 |
- openbsd.duckdb openbsd-src 仓库 contributors 表；OpenBSD Project Goals [EB/OL]. <https://www.openbsd.org/goals.html>；FreeBSD Core Team bylaws [EB/OL]. <https://www.freebsd.org/internal/core-team/>；NetBSD Foundation bylaws [EB/OL]. <https://www.netbsd.org/foundation/>；de Raadt 邮件列表发言 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；OpenBSD Foundation [EB/OL]. <https://www.openbsdfoundation.org/>；**【2026-07-30 de Raadt vs Torvalds 公开争论一手报道·7av 条目】**2005-06-19 eNet 硅谷动力/新浪科技报道（**<http://tech.sina.com.cn/it/2005-06-19/1009639712.shtml>**）记录 de Raadt 接受《福布斯》采访原文 “I think our code quality is higher, and that is because of the way we develop and the focus we have，而 Linux 系统根本就无质量可言”，Torvalds 通过电子邮件回应称 “de Raadt 是个很难相处的人” 并拒绝进一步评论；de Raadt 在同一采访中称 “Linux 社区之所以这么做是因为他们憎恨微软，而我们之所以这么做是因为我们热爱 Unix”；该报道为《福布斯》英文采访的中文转译，英文原文须以《福布斯》2005 年原始采访存档为准 ［A］
- OpenBSD Foundation 财务报告 [EB/OL]. <https://www.openbsdfoundation.org/>；FreeBSD Foundation Annual Report [EB/OL]. <https://www.freebsdfoundation.org/annual-report/>；2014 年电费危机 misc@ 邮件列表讨论 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；OpenSSH 项目文档 [EB/OL]. <https://www.openssh.com/>；LibreSSL 项目文档 [EB/OL]. <https://www.libressl.org/>；商业支持案例［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；openbsd.duckdb openbsd-src 仓库 commit df174574d401 与 b6553af36068；openbsd.duckdb openbsd-src 仓库 contributors 表；de Raadt 邮件列表发言 [EB/OL]. <https://marc.info/?laccopenbsd-misc> ［A］
- de Raadt 邮件列表发言；Van Gennep (1909); Turner, V. (1969). *The Ritual Process: Structure and Anti-Structure*. [仪式理论的后续发展]; shigang.md §19（人类学）、§13（社会哲学）、§25（解释学）

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP331、BSD Now EP189、BSDTalk EP229、BSDTalk EP66（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 核心文章把 Windows 描述为企业导向开发模型，以 ABI 稳定为代价积累遗留代码；OpenBSD 以短周期 ABI 断裂、代码审计与行数上限换取干净内核。（BSD Now EP331，[244.9-537.58]，L2）[订正：原 [443.1-537.58]，2026-09-30 SenseAudio 重转核对]
- Phoronix 基准显示 FreeBSD 12.1 在 AMD Ryzen Threadripper 3970X 上与 Linux 大体持平，部分测试领先，GCC 9.2 编译在若干场景更强。（BSD Now EP331，[1130.8-1392.64]，L2）
- Jim Salter 辨析 ZIL 与 SLOG：每个 ZFS 池都有 ZIL，SLOG 只是把 ZIL 放到独立快速设备上的做法。（BSD Now EP331，[2441.46-2491.48]，L2）
- NetBSD 在其 wiki 列出 GSoC 内核级与用户态项目并标注难度；FreeBSD 的项目含 Lua bootloader、POSIX 合规测试框架、.NET Core CLR 移植等。（BSD Now EP189，[585.22-733.18]，L2）
- 受访者 Wendell 回忆 ZFS 可从多盘硬件故障且池满的状态恢复数据，并支持池在 SPARC 与 amd64 架构间跨字节序移植。（BSD Now EP189，[4340.92-4558.02]，L1）
- Wendell 用退役的 IBM NetApp 磁盘柜与 Google Search Appliance（Dell R710）搭建 10GbE 视频存储，ZFS 压缩使八百万文件遍历缩短到八分钟。（BSD Now EP189，[4702.86-5620.86]，L1）
- Ted Unangst 撰文记录在网站登录、系统登录等场景使用 YubiKey 的体验，以帮助他人少走弯路。（BSD Now EP189，[6182.44-6225.48]，L2）
- Cappuccio 幼年从叔叔处得到一台可运行 CP/M 或 Microsoft Xenix 的 TRS-80 Model 16B，九十年代初转入 386BSD 与 Linux，1995 年因 Theo 在 FTP 站点放出首个 SPARC 内核而开始使用 OpenBSD 并沿用至访谈时近二十年；早期记忆包括修复后的 SCSI 驱动将传输速率从每秒一百千字节提升到一兆字节。（BSDTalk EP229，[66.47-135.72]，L1）
- FlashRD 是把 OpenBSD 封装为只读系统的脚本：以 RAM disk 引导、经 CrunchGen 压缩工具集、装入完整通用内核而非功能受限的精简系统，把运行中系统封装为 VND 文件并支持换文件升级；其动机是闪存介质固有不可靠，当事人引 USENIX 会议实验称十五块受测闪存盘有十三块在写入断电时发生中度以上数据丢失乃至整体故障。（BSDTalk EP229，[190.13-246.25]，L1）
- 项目谱系：flashdist 需手工指定命令清单与闪存几何参数，在引导器仅支持 CHS 的年代以伪造几何参数立足；当 OpenBSD 引导器转向 LBA 且内核不再接受外部几何后其存在理由消失，flashboot 引入 RAM disk 使系统可整体升级，2009 年 flashrd 成型；作者同时观察到小型项目呈博客或邮件列表提及后热度与贡献短暂聚集、随后冷却的周期。（BSDTalk EP229，[574.35-754.16]，L1）
- NSH 源起于 2001 年作者用 WI 网卡搭建无线网络、面对熟悉 Cisco 命令行的同事需要降低 OpenBSD 路由器门槛的实操场景；它取材 telnet、ftp、ifconfig、route、arp 等常用工具思路，以单一简洁语法封装 PF、BGPD、SNMPD、OSPFD、DHCPd、smtpd 等守护进程配置，并用 SQLite 数据库区分内核自动状态与用户显式意图，写出单一 rc 风格配置文件。（BSDTalk EP229，[313.98-419.14]，L1）
- 设计哲学上作者曾计划把 pfctl 重写为共享库，因 PF 持续快速变动而放弃；NSH 改为只封装不重写既有配置语法，懂 PF 的用户无需学习第二套方言；后续方向是 Web 界面与 relayd URL 过滤文档，总目标是让不熟悉 vi 与文件系统细节的人也能使用 OpenBSD。（BSDTalk EP229，[1169.21-1263.43]，L1）
- 生产环境层面，作者长期在约二十余台异构机器（PC Engines ALIX、Super Micro Core 2 等）上运行 FlashRD，坚持最少可动部件原则，称 FlashRD 加 NSH 的组合可长期无人值守运行。（BSDTalk EP229，[769.16-815.33]，L1）
- Michael Dexter 的技术路径：1991 年读计算机科学时以 SunOS 与 Ultrix 入门真实系统；在密歇根州卡拉马祖求学拉丁语期间偶遇捐赠设立的 NeXT 实验室而接触 NextStep；1998 年前后在俄勒冈州波特兰身处 Red Hat 环境中使用 BSD 相关系统，经历 Red Hat 5.2 的 RPM、Red Hat 6 与 GNOME 测试版时代；2001 年任职 MandrakeSoft 内部 IS 团队，公司失利后迁居拉脱维亚；2002 年前后确立 BSD 主攻方向，恰逢 FreeBSD 5 带来 jls、jexec 等 jail 特性。（BSDTalk EP66，[56.68-254.04]，L1）
- 从 jails 的组织价值到 SysJail 的方案设计：受访者需要托管多个站点且拒绝与他人共享托管机，痛感软件安装散落文件系统、RPM 亦未能根治，因而看重 jail 将守护进程与宿主系统分离、开销几乎不变、得以整体删除重建的组织价值，并多年以磁盘镜像充当各 jail 的独立分区；SysJail 由此针对 FreeBSD jail 实现的短板而作——文件系统扁平化得以按守护进程或按用户切分虚拟系统，复用 Systrace 的内核级组件、自身全部实现于用户态而无需改内核，可在 Systrace 所到之处运行（NetBSD、OpenBSD、MirOS），提供虚拟终端以便 SSH 进入、以二进制安装构建完整系统；性能上其测试在一台 VIA 1GHz、512MB 内存的迷你主板上同时跑 64 个 jail、每个 sshd 约占 2MB，远低于 VMware 类方案每实例 64MB 的分配；另以用户态文件系统设想隔离各 jail 的 procfs 可见进程以补安全短板。（BSDTalk EP66，[271.24-740.94]，L1）
- 转向 OpenBSD 的动机与挫折：受访者认为 FreeBSD 5 系列不如其前的 4 系稳定，故障无 core dump、无征兆、存活时长不定，令其放弃；其眼中 OpenBSD 是血统上最纯正、守旧而创新的 BSD，却始终没有 jail——邮件列表的答复是其实现复杂、资源应集中于 OpenSSH 与整体安全，且标准答案常是“用 Systrace”；而 ports 中 Systrace profile 屈指可数，社区并未把 Systrace 的行为约束能力制度化为基线配置，SysJail 即以此引入基线 profile 并追加 Systrace 不具备的系统调用拦截。（BSDTalk EP66，[429.72-540.54]，L1）
- 拉脱维亚生态与延伸项目：受访者四年前抵拉脱维亚时当地并无开源产业、其技能被归入 Windows 管理员，遂活跃于本地社区，曾邀 MySQL 的 David Axmark 到里加；XFSscale 项目为 nnpfs（旧名 XFS）的文档工程，定位类似 FUSE 的用户态文件系统，设想跨平台 SSHFS 并充当 jail 专用 procfs；Kristaps 与大学合作波罗的海超算网格 Baltic Grid，并排定在米兰 EuroBSDCon 讲 XFSscale、在纽约市 BSD 大会讲 SysJail；BSD.LV 计划转向纯开源合同业务的商业面向，指欧洲 EU 资金只要懂申请便可得，而 DARPA 之类资金已对 OpenBSD 枯竭；又鼓动为拉脱维亚制造的 RouterBoard（现跑 Debian 的无线路由整机）移植 OpenBSD 这类真正的路由操作系统。（BSDTalk EP66，[1474.28-1743.16]，L1）
- 个人使用与 2006 年社区观察：受访者桌面用 Mac OS X（iBook），服务器用 OpenBSD；曾期待苹果以 FreeBSD 用户态与 Jordan Hubbard 的加入带来服务器与桌面同构的统一环境，但该愿景未至，且 Emmanuel Dreyfus 的 compat Darwin 等项目亟需维护；收尾时其判断苹果的开放程度恰以满足自身需要为限、Linux 渐趋平台期、BSD 阵营正经历震荡——尤其点出近日引起广泛关注的 Future of NetBSD 消息，为该事件的同时期社区感知留下口述记录。（BSDTalk EP66，[1743.16-2052.2]，L1）

**史料**：

- telegraph.ph 上‘为何电脑糟糕’及 OpenBSD 学习文章，比较 Windows ABI 稳定与 OpenBSD 模型。（BSD Now EP331，[101.36-316.3]，L2）
- Phoronix 的 FreeBSD 12.1 与 Ryzen Threadripper 3970X 基准测试。（BSD Now EP331，[1128.06-1139.3]，L2）
- Jim Salter 的 ZFS ZIL/SLOG 辨析文章，经 Matt Ahrens 校对。（BSD Now EP331，[2441.46-2510.14]，L3）
- NetBSD GSoC wiki 项目列表（BSD Now EP189，[670.66-741.64]，L1）
- FreeBSD GSoC 项目列表（BSD Now EP189，[585.22-667.7]，L1）
- Wendell 访谈自述（BSD Now EP189，[4340.92-6064.62]，L1）
- Ted Unangst 的 YubiKey 使用博客（BSD Now EP189，[6182.44-6225.48]，L1）
- 当事人一手口述的 OpenBSD 入坑节点：1995 年 Theo 在 FTP 站点发布首个 SPARC 内核；同期并行接触 386BSD 与 Linux 的个人编年，可作项目早期传播路径的私人证词。（BSDTalk EP229，[101.89-135.72]，L1）
- 当事人转述的学术证据：某届 USENIX 会议论文以自制断电电路测试闪存盘写入可靠性，得出十五盘中十三盘受损或失效的结论；论文未给出题名与作者，需回溯检索原文献。 [存疑脚注] 当事人转述未提供论文题名作者与年份，引用前须检索 USENIX 原文核验（BSDTalk EP229，[219.77-241.69]，L2）
- flashdist、flashboot、flashrd 三代工具的演进序列与 flashrd 2009 年发布时点，及 NSH 的 SQLite 状态库设计细节，均为开发者本人自述的一手项目史。（BSDTalk EP229，[580.65-728.39]，L1）
- 本期可作为 SysJail 早期史的一手物证：项目版本 SysJail 1.03、以 sysjail 隔离 Apache 的 BSD.LV 自用站点（2006 年 8 月约四万次点击）、提交 Freshmeat 的公告被拒、Daemon News 刊出的测试征集、德国媒体的报道、OpenBSD 3.9 磁盘镜像高负载内核 panic 的补丁记录，以及节目开头播报的 BSD 认证组织社区调查结果发布与 OpenBSD 4.0 预购开放。（BSDTalk EP66，[981.34-1404.24]，L1）

**史观**：

- 总纲22 知识注定过时：总纲22 知识注定过时：文章指出向后兼容把旧 ABI 与废弃代码永久固化，使系统知识随规模膨胀而贬值。（BSD Now EP331，[618.82-661.42]，L2）
- 总纲21 革命与改革是历史方法论的分歧：总纲21 革命与改革是历史方法论的分歧：Windows 的渐进兼容与 OpenBSD 的周期断裂分别代表改革与革命两种工程方法论。（BSD Now EP331，[524.92-600.62]，L2）
- 总纲10 动手者创造历史：受访者以退役硬件自建存储系统并迁移海量文件，历史由动手实践者推动。（BSD Now EP189，[4702.86-5620.86]，L1）
- 总纲9 经验优先：对 ZFS 健壮性的判断来自亲身数据恢复与迁移经历，经验先于宣传。（BSD Now EP189，[4462.78-4558.02]，L1）
- 总纲12 科学是形式主义：存储性能与可靠性认知源于可复现的实验、工具与度量，而非主观印象。（BSD Now EP189，[5085.26-5282.2]，L1）
- 总纲10 动手者创造历史：作者的全部工具均从自身运维需求中长出——无线网络、无盘防火墙、面向同事的可用性——而非自上而下的项目规划；FlashRD 与 NSH 二十余年由其在职维护、服务真实机器，恰是动手者而非舞台人物书写技术史的一手素材。（BSDTalk EP229，[769.16-815.33]，L1）
- 总纲22 知识注定过时：flashdist 的衰落不是失败而是环境变迁：引导器 CHS 到 LBA 的转换、内核几何探测的强制化、八吉字节闪存跌至数美元，共同使手工几何管理的存在前提消失，作者自认继续维护是愚蠢的；技术方案的合理性随其所依附的物质条件一同过时。（BSDTalk EP229，[598.14-727.85]，L1）
- 总纲10 动手者创造历史：该项目由 Kristaps 一人承担核心开发、Michael Dexter 承担项目管理与运维的两人体制驱动，处理进程限制之类功能仅花两天，而同类功能在 FreeBSD 端是一个 Google Summer of Code 项目；受访者拒绝推动其进入任何基本系统，主张工具按规格即插即用的模块化 UNIX 模式之美——默默做事的小团队以最小协作规模维持跨项目工具，正是动手者创造历史的微观形态。（BSDTalk EP66，[1246.12-1310.56]，L1）

**辨析**：

- 转写对 Windows 代码行数等数字（如‘half a billion lines’）为文章作者的估计值，未经独立核实。 [存疑脚注] Windows 代码行数为作者估计（BSD Now EP331，[503.24-515.92]，L4）
- [存疑脚注] GSoC 项目名单为 2017 年计划，最终是否全部完成须以后续项目报告为准。 [存疑脚注] 计划性名单，验收结果待后续报告。（BSD Now EP189，[585.22-733.18]，L4）
- 转写将叔叔的机器记为 Triss 80 model 16B 并称可运行 CP/M 或 Xenix，机型拼写系转写噪音，TRS-80 Model 16B 的操作系统组合与购入年代需按机型史料核对，不得径直引用。[存疑脚注] 转写模糊，机型与操作系统组合待核。 [存疑脚注] 机型名与操作系统组合由受损转写推断，须与 Tandy 产品文献交叉核验后方可引用（BSDTalk EP229，[88.43-100.97]，L5）
- 受访者对 1995 年前后盒装 UNIX 时代的回顾（UNIXware、盒装 OpenStep、更早的 Coherent）带有明显个人立场：称彼时桌面与服务器 UNIX 应用尽有却全为闭源、闭源模式终究失配而大多退场，UNIXware 这类相对廉价的“真 UNIX”被“当时远逊但免费”的 Linux 击败——此为亲历者的单方回望，且转写专名普遍失真（CISJail 应为 SysJail，CISTrace/Cistrays 应为 Systrace，MirrorOS 应为 MirOS，MeSQL 应为 MySQL，flash.post 应为 Freshmeat，MonoWall 应为 m0n0wall，Soakris 应为 Soekris，altrix 应为 Ultrix，deck 应为 DEC，Viya 应为 VIA，Mike Gunncar 应为 Mike Gancarz），引用前均须回核音频。 [存疑脚注] 对 1990 年代闭源 UNIX 兴衰与 Linux 取代的因果判断为当事人单方回顾，须与比较史文献互证；转写专名失真清单如上（BSDTalk EP66，[1947.26-2003.88]，L4）

**文献**：

- [BSD Now EP331] Pennington J. BSD Now: 331: Why Computers Suck[EB/OL]. (2020-01-02)[2026-08-15]. <https://www.bsdnow.tv/331>.
- [BSD Now EP189] Pennington J. BSD Now: 189: Codified Summer[EB/OL]. (2017-04-12)[2026-08-15]. <https://www.bsdnow.tv/189>.
- [BSDTalk EP229] Backman W. BSDTalk: 229: bsdtalk229 - Chris Cappuccio[EB/OL]. (2013-08-07)[2026-08-27]. <https://bsdtalk.blogspot.com/2013/08/bsdtalk229-chris-cappuccio.html>.
- [BSDTalk EP66] Backman W. BSDTalk: 66: bsdtalk066 - Interview with Michael Dexter about sysjail[EB/OL]. (2006-09-20)[2026-08-27]. <https://archive.org/details/bsdtalk066>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-284 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-284`；w172 YouTube 章节路由采纳）

据〔会议不详〕讲者口述：Stuart Henderson（stn@openbsd）与 Omar Polo（op@openbsd）关注了相关作品。（YouTube EP9uTBkdQpxZo，[2654.319-2659.349]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-3102 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3102`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Fighting "Technical Fires" by Sam Smith〕讲者口述：讲者称管道（pipes）让人把工具彼此连接起来的能力在其他系统中并不存在，这一概念在其他地方没有对应物。（YouTube EPRSqs6NAsmiY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-3103 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-3103`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Fighting "Technical Fires" by Sam Smith〕讲者口述：讲者称拥有相应仓库便可获得变更通知——每当有人向 FreeBSD 仓库（转写作 FreeBSD depository）提交，消息就会发出。（YouTube EPRSqs6NAsmiY，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
