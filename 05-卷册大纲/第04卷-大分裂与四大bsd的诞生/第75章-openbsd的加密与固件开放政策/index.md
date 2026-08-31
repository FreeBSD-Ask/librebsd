---
chapter: 第 75 章
id: CH75
volume: 第04卷-大分裂与四大bsd的诞生
---

# 第 75 章 openbsd的加密与固件开放政策

## 要点

- OpenBSD 对固件许可证持严格立场——厂商为节省成本不再在芯片内固化固件、改由操作系统加载后，固件分发许可证冲突显现；OpenBSD 把可自由再分发的固件纳入 base 系统，许可证不兼容的固件经 `fw_update(8)` 从端口单独分发，多数为 WiFi、显卡与 Intel 芯片组（afresh1, 2024）。
- Linux、Windows NT 4.0、Solaris 2.5 与 OpenBSD 的安全比较需辨析——不同项目的安全目标、用户基数、商业模型差异较大；辨析需对照多方原始文档交叉验证；freebsd.db 统计结论 C-05 显示：openbsd-src 总 commit 数 245,904（SQL 查询 `SELECT COUNT(*) FROM commits WHERE repo_name
- OpenBSD 2.6/2.7/2.8/2.9 时期（1999-2001）的漏洞响应模型呈现 errata 机制成熟化特征——errata 条目从 2.0/2.1 时期的纯补丁发布演化为 2.7 时期的密集安全修复期（2000 年 10 月多条 SECURITY FIX 条目）与 2.9 时期的末条 errata（2002 年 6 月 25 日第 027 条）；hackathon 文化（首次 19
- 从项目史观总纲第 5 条 “没有必然性，只有偶然性”、第 6 条 “和解优于斗争”、第 21 条 “革命与改革是历史方法论的分歧” 三条切入审视，de Raadt 独裁模式、代码审计团队与被疏远贡献者并非 “独裁必然产生安全至上” 或 “独裁必然排斥贡献者” 的目的论结果，而是 1996 年夏天 OpenBSD 启动全代码审计（security.html 一手记载 "We have been au

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3826] 卷“第04卷-大分裂与四大bsd的诞生”第 75 章，匹配置信度 folder，原因：folder 第73章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- OpenBSD 的严格许可证立场与硬件厂商的省钱考量构成持续冲突——rtwn(4)/urtwn(4) 固件经 kevlo 联系 Realtek 去除专利条款后移入 base，是许可证谈判成功的少数案例；多数不兼容固件仍须经 `fw_update(8)` 分发（afresh1, 2024）。
- 比较的具体维度在不同叙事中略有差异——需对照多方原始文档交叉验证；【0 信任原则·commit 量不等于质量】C-05 openbsd-src 245,904 与 C-03 freebsd-src 444,203 的量级差异不等于两项目代码质量或安全性的差异——OpenBSD 的安全审计文化（自 1996 年夏天起全代码审计）使单次 commit 可能包含更密集的审计修正，commit 量与安全质
- errata 机制从 2.0 至 2.9 的成熟化路径须逐版本对照 errata 页面核实——2.0 时期 errata 为纯补丁发布，2.7 时期出现密集安全修复期，2.9 末条 errata 为收尾，3.x 起引入架构性防御，各阶段边界须以 errata 条目数量与内容为据而非史家主观分期；hackathon 对漏洞响应的具体贡献须对照 hackathons.html 记录与 errata 时
- 考据过程留痕——【查证来源】项目史观总纲第 5 条原文经 据原文第 25 章 第 11 行 Read 一手核验，第 6 条原文经第 13 行 Read 一手核验，第 21 条原文经第 25 行 Read 一手核验；OpenBSD security.html 经 <https://www.openbsd.org/security.html> WebFetch 一手核验，"We have been a

## 文献

- afresh1, 2024《Why rewrite fw_update(8)?》BSDCan 2024 演讲<!-- DB_REF:openbsd.duckdb -->> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1992-1995 年间：770 次提交。> 仓库总览：491,195 次提交，3,352 位贡献者，1995-10-18 至 2026-08-25。
- 四个项目 1995-1996 年安全文档；安全对比研究[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]；本项目。freebsd.db 数据分析报告：描述性统计与推断性统计 [R/OL]. 2026.（统计结论 C-05 openbsd-src 总 commit 数 245,904，SQL 查询 `SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`；统计结论 C-03 freebsd-src 总 commit 数 444,203；统计结论 C-14 openbsd-src 变点 Pettitt 2001-01 / BUISHAND 2017-09，Python 脚本自实现 Pettitt + BUISHAND R 检验 10,000 次 Monte Carlo；统计结论 C-12 freebsd-src 变点 1999-08 双检验一致 p < 0.001） ［A］
- OpenBSD 2.6/2.7/2.8/2.9 errata 页面；OpenBSD hackathons.html；OpenBSD security.html；OpenBSD 3.x errata 页面；本项目。原材料/研究/bsd 漏洞史/版本周期/openbsd-2.x.md；本项目。bsd_commits.db 数据分析报告：宏观趋势统计 [R/OL]. 2026. ［A］
- 项目史观总纲第 5 条、第 6 条、第 21 条（据原文第 25 章）；OpenBSD security.html [EB/OL]. <https://www.openbsd.org/security.html>；OpenBSD hackathons.html [EB/OL]. <https://www.openbsd.org/hackathons.html>；OpenBSD goals.html [EB/OL]. <https://www.openbsd.org/goals.html>；bsd_commits.db openbsd-src 仓库 deraadt 首 commit 与累计 commit 量 ［A］### 史观映射> de Raadt 被逐出 NetBSD——一封邮件通知，没有上诉，没有告别。分离从来不是和平的，但分离之后必有新的聚合：OpenBSD 从 NetBSD 的废墟中诞生，以代码审计为旗帜。de Raadt 的天才加速了 OpenBSD 的崛起——PF、OpenSSH、全代码审计方法论，每一项都是他驱动下的产物。但同一种不妥协的气质，既是他创造的动力，也是他冲突的根源：与 NetBSD 的决裂只是开始，此后与 FreeBSD 的隔阂、与 DARPA 的冲突、与社区新人的摩擦，都是同一种结构的反复。天才不总是灾厄，但天才的边界往往就是灾厄的起点---## 第 29.15 不同时期人员的采访录（详见 [采访录.md](采访录.md)）> 第 29 章采访录子节，覆盖 1996-2001 年 OpenBSD 安全文化奠基的当事人陈述，含 Theo de Raadt（西奥·德·若特） OpenBSD 安全文化奠基演讲、Bob Beck OpenBSD 安全响应工程两则，每则采访按 5 字段深化，考据过程另见 原材料/研究/考据记录/ 下对应文件。## 第 29.16 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP428、BSD Now EP164、BSD Now EP16（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- OpenBSD 于 1995 年 10 月作为 NetBSD 分叉起步，其默认安装长期仅报告两个远程漏洞，被描述为默认安全的系统。（BSD Now EP428，[135.74-145.1]，L2）
- OpenBSD 率先随系统搭载 IPsec 等强密码学，并因此卷入美国出口管制，这是其基地设于加拿大的原因之一。（BSD Now EP428，[145.1-160.3]，L2）
- OpenBSD 形成发现漏洞后不再单点修补，而是在全树范围内寻找并修复同类模式的代码审计文化。（BSD Now EP428，[164.94-184.78]，L2）
- OpenBSD 是 OpenSSH、OpenBGPD、PF、OpenSMTPD、IKE、Mandoc 与 LibreSSL 等广泛使用组件的上游来源。（BSD Now EP428，[247.2-262.74]，L2）
- DragonFly vkernel 类似 jail 但虚拟化整个内核，新支持 copy-on-write 镜像模式，使多个 vkernel 可从同一镜像启动，运行时变更保留在各自层而不写回原镜像文件，近似 UnionFS。（BSD Now EP164，[197.82-249.56]，L2）
- 若将镜像设为只读，多个 vkernel 共享同一镜像且互不修改；对镜像的改动被保留在分离的变更层中。（BSD Now EP164，[226.9-239.82]，L2）
- FreeBSD 在 Raspberry Pi 3 上的有限支持已提交 head，多数驱动可用上游，但 RNG 的 call-out 模式失效、SMP 尚未完成、VCHIQ 驱动存在仅对 ARM 成立的假设，且尚无 HDMI 支持。（BSD Now EP164，[328.18-412.58]，L2）
- OpenBSD 自成立起一直使用 CVS，与 NetBSD 及早期 FreeBSD 相同；本期公布位于 github.com/openbsd 的官方只读镜像，含源码与 ports 等仓库。（BSD Now EP164，[3816.62-3848.04]，L2）
- OpenBSD GitHub 镜像的 exporter 稳定性尚无保证，若基于该分支做 fork，数据可能以不同哈希重新导出而使 rebase 困难。（BSD Now EP164，[3902.24-3915.58]，L2）
- Libreboot.org 发布以开源 BIOS 引导 OpenBSD 或 LibertyBSD 的文档，含 USB 镜像制作、Grub 配置与排障，但 Libreboot 加 Grub 尚不支持全盘加密。（BSD Now EP164，[3926.18-4004.28]，L2）
- 主持人评论认为随着 EFI 增长，开源系统越发依赖闭源固件甚至迷你操作系统来引导，Libreboot 针对的正是最后一块不受控制的区域。（BSD Now EP164，[4007.8-4038.48]，L1）
- Josh Paetzel 亲述协助 FreeBSD Foundation 调试 Supermicro 服务器的 PXE 引导：串口看似故障，实为系统启动停止，改为静态 DHCP 预留后正常引导，根因仍未完全查明。（BSD Now EP164，[1641.44-1928.76]，L1）
- Josh Paetzel 认为 ZFS 中延迟敏感负载宜用 RAID10，容量优先与非延迟敏感负载宜用 RAIDZ/RAIDZ2；其团队运行过 200 至 300 盘的 RAIDZ2 与 RAID10 池且未因硬件故障丢失池。（BSD Now EP164，[2049.82-2203.34]，L1）
- Josh Paetzel 以客机比喻 ZFS：非常安全，多数故障被冗余吸收，但一旦突破临界即彻底崩溃，且没有理解 RAID-Z 布局的数据恢复工具。（BSD Now EP164，[2434.64-2497.76]，L1）
- Josh Paetzel 指出 ZFS 自 2011 年开源后五年间约 45% 的代码为新写，并认为文件系统需要商业实体与专业工程资源支撑。（BSD Now EP164，[2522.4-2603.72]，L1）
- 教程演示在 FreeBSD 与 OpenBSD 上执行全盘加密安装；FreeBSD 侧以脚本化方式处理 GELI 与 ZFS 根文件系统，OpenBSD 侧则结合加密根分区与引导加载器。（BSD Now EP16，[4289.6-4418.6]，L2）
- 新闻讨论 FreeBSD Ports 将引入季度稳定分支（2014Q1），快照维护三个月，期间仅接受安全修复、构建与运行时修复及基础设施变更。（BSD Now EP16，[4690.7-4766.9]，L2）
- PackageNG 社区讨论类似 pkgsrc acceptable licenses 的许可证过滤，使用户可按许可证决定是否允许安装软件包，并考虑提供查看已装包许可证的命令。（BSD Now EP16，[4496.2-4585.9]，L2）

**史料**：

- Peter Hansteen 的 What every IT person needs to know about OpenBSD 系列文章，作为本期 OpenBSD 历史叙述的主要二手来源。（BSD Now EP428，[70.74-76.44]，L2）
- DragonFly vkernel copy-on-write 镜像模式的功能说明。（BSD Now EP164，[197.82-249.56]，L2）
- FreeBSD 提交者关于 Raspberry Pi 3 支持的博客。　[存疑脚注] 博客作者全名须核验。（BSD Now EP164，[328.18-412.58]，L2）
- OpenBSD 官方只读 GitHub 镜像（github.com/openbsd）。（BSD Now EP164，[3816.62-3915.58]，L2）
- Libreboot.org 关于以开源 BIOS 引导 OpenBSD/LibertyBSD 的文档。（BSD Now EP164，[3926.18-4004.28]，L2）
- Josh Paetzel 访谈自述（iXsystems，FreeNAS/TrueNAS 相关运维经验）。（BSD Now EP164，[1600.0-2610.0]，L1）
- 本期提及 NetBSD 在 Marvell Kirkwood 平台（插头式迷你服务器）上的使用文章，以及 FreeBSD Foundation 年终募款与开发者差旅资助。（BSD Now EP16，[548.6-570.2]，L2）

**史观**：

- 总纲10 动手者创造历史：OpenBSD 以代码审计与全树范围修复确立安全实践，体现动手者在具体工程中塑造项目文化。（BSD Now EP428，[164.94-191.78]，L2）
- 总纲13 法律与道德是利益分配：美国出口管制把加密技术纳入法律约束，迫使 OpenBSD 调整基地布局，体现法律与道德作为利益分配工具的现实效应。（BSD Now EP428，[145.1-160.3]，L2）
- 总纲4 分离聚合是永恒规律：vkernel 以只读镜像为基底、以 copy-on-write 层承载差异，多个实例分离运行又共享同一映像，呈现分离与聚合的结构。（BSD Now EP164，[197.82-249.56]，L3）
- 总纲3 不存在进步，只有权力再分配：Libreboot 试图把引导固件的控制权从闭源厂商转移给用户，是围绕系统控制权的权力再分配。（BSD Now EP164，[4007.8-4038.48]，L3）
- 总纲9 经验优先：ZFS 的可靠性来自 Sun 时期大量工程投入与后续商业资源，专业经验沉淀为可用的复杂系统。（BSD Now EP164，[2522.4-2603.72]，L3）
- 总纲25 逻辑是形式主义而非世界本身的结构：ZFS 以冗余与校验把故障可能性压到极低，但剩余风险以极端方式集中爆发，安全是形式化边界内的构造。（BSD Now EP164，[2434.64-2497.76]，L3）
- 总纲22 知识注定过时：OpenBSD 长期使用 CVS，在 Git 成为主流后以镜像方式补足浏览体验，旧工具随生态变化而需要新形式。（BSD Now EP164，[3816.62-3900.24]，L3）
- 总纲10 动手者创造历史：全盘加密教程把复杂的 GELI/ZFS 流程固化为可重复脚本，使普通用户得以动手部署并复现。（BSD Now EP16，[4331.5-4418.6]，L2）

**辨析**：

- “默认安装仅两个远程漏洞”为 OpenBSD 项目长期自述口径，其统计口径与时间范围需与官方安全公告逐条核对。　[存疑脚注] 远程漏洞计数为项目自述，统计边界需对照 OpenBSD 官方安全公告确认。（BSD Now EP428，[138.94-145.1]，L4）
- [存疑脚注] 转写未给出 DragonFly vkernel copy-on-write 功能的具体提交与作者，须核验 DragonFly 仓库与提交记录。　[存疑脚注] COW 功能提交与作者须核验。（BSD Now EP164，[197.82-249.56]，L4）
- 教程中的加密安装步骤由主持人演示并录制，涉及 FreeBSD 9.2/10 与 OpenBSD 特定版本的实现细节，属于演示与转述而非当事人一手史料。（BSD Now EP16，[0.0-10.2]，L2）

**文献**：

- [BSD Now EP428] Pennington J. BSD Now: 428: Cult of BSD[EB/OL]. (2021-11-11)[2026-08-15]. https://www.bsdnow.tv/428.
- [BSD Now EP164] Pennington J. BSD Now: 164: Virtualized COW / PI?[EB/OL]. (2016-10-19)[2026-08-15]. https://www.bsdnow.tv/164.
- [BSD Now EP16] Pennington J. BSD Now: 16: Cryptocrystalline[EB/OL]. (2013-12-18)[2026-08-15]. https://www.bsdnow.tv/16.

<!-- /PODCAST_REVIEW -->
