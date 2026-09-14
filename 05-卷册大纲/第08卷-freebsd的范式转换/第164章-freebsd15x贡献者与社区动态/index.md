---
chapter: 第 164 章
id: CH164
volume: 第08卷-freebsd的范式转换
---

# 第164章 freebsd15x贡献者与社区动态

## 史料

- FreeBSD 15.0-RELEASE Release Notes 与发布公告（freebsd.org/releases）；Core Team 32 位平台弃用公告（2023.2）；John Baldwin freebsd-arch 邮件（2025-06-18）；Ed Maste freebsd-current 邮件（2024-01-24）与提交 `f817f6e7f4a8`；FreeBSD Foundation 赞助的驱动退役提交系列 ［A］

## 要点

- FreeBSD 15.0-RELEASE 将传统 **ftpd(8)** 守护进程从基础系统中移除，commit 259bb93b80c0 由 Lexi Winter（<ivy@FreeBSD.org>）于 2025.9.29 起草、2025.10.1 合入 stable/15 分支，Phabricator 评审编号 D52739，由 Colin Percival（cperciva@）批准；该删除在更早版本中已标为 deprecated 并预告 15.0 移除；接续路径为 ftp/freebsd-ftpd port，PAM 服务 ftp(d) 保留以供其他 FTP 守护进程使用；/etc/inetd.conf 中条目相应改为指向 /usr/local 路径；ObsoleteFiles.inc 列出 usr/libexec/ftpd、etc/rc.d/ftpd、share/man/man5/ftpchroot.5.gz、share/man/man8/ftpd.8.gz 等删除条目，但配置文件保留以便用户迁移至 port；共删除 6972 行、38 个文件
- FreeBSD 15.0-RELEASE 正式退役 i386、armv6、32 位 powerpc 三大 32 位硬件平台，仅 armv7 作为 “最后支持的 32 位平台” 保留 Tier-2 支持；32 位应用兼容性通过 64 位平台的 lib32 兼容层延续，lib32 本身不在退役范围；Core Team 于 2023.2 公布 32 位平台弃用计划，John Baldwin（约翰·鲍德温）（<jhb@FreeBSD.org>）于 2025.6.18 在 freebsd-arch 邮件列表详述退役时间线——2025.6 起在 main 分支禁用 i386 内核配置并将 32 位 powerpc 移出 universe 默认目标列表、停止 i386/powerpc 的 release 镜像构建与二进制包构建、禁用 CI 作业；2025.9 stable/15 分支后排除 i386/powerpc 的 CI 与包构建；BSDCan 2026 devsummit 评估 stable/14 弃用平台是否受 MFC 影响，决定是否开始从 main 删除 i386/powerpc 内核代码；最终在 14.x 最后一个版本（2027.9）后将退役代码 MFC 至 stable/15
- FreeBSD 15.0-RELEASE 标记 **bsdlabel(8)** 与 **fdisk(8)** 为 deprecated，建议用户迁移至 **gpart(8)**；Ed Maste（埃德·马斯特） 于 2024.1.24 在 freebsd-current 发布 “Removing fdisk and bsdlabel (legacy partition tools)” 邮件，原计划 15.0 移除，Phabricator 评审 D43575（fdisk 断开构建）与 D43563（bsdlabel 手册页弃用提示）；但 15.0-RELEASE 发布时实际移除并未发生，Ed Maste 于 2025.10.24 提交 commit `f817f6e7f4a8dc507f3e1b1603dfd2d81093e3bd` 将 fdisk 移除时间推迟至 16.0，理由为 “Removal did not happen prior to 15.0”；该改动经 `2be4c64a0d27`（stable/15，2025.10.27）与 `61d4640720e5`（releng/15.0，2025.10.30）MFC 至各分支，由 FreeBSD Foundation 赞助；bsdlabel 弃用提示亦同步更新至 16.0 移除
- FreeBSD 15.0-RELEASE 将多项驱动标记为 deprecated 并计划 16.0 移除：**agp(4)** 总线驱动（commit `92af7c97e197`、`cadadd1a0398`）、IBM PC 软盘控制器 **fdc(4)** 及相关工具（commit `4c736cfc69a7`，FreeBSD Foundation 赞助）、**firewire(4)** 总线及相关驱动（commit `fc889167c319`，FreeBSD Foundation 赞助，原计划 15.0 但未及时完成）、**syscons(4)** 控制台驱动（commit `2bc5b1d60512`，FreeBSD Foundation 赞助，建议迁移至 **vt(4)**）、USB 802.11g 无线驱动 **upgt(4)**（commit `7f8a5c5a1585`，FreeBSD Foundation 赞助）；同时 **gvinum(8)** 卷管理器已在 15.0 从 base 移除（commit 系列由 FreeBSD Foundation 赞助，gvinum 作为 legacy 逻辑卷管理器长期缺乏维护，现代存储管理由 ZFS 与 GEOM 类承担）；**agp(4)**——Accelerated Graphics Port 总线驱动用于旧款 AGP 显卡的 GART 管理，现代系统均使用 PCI Express 与集成 GPU 驱动；**fdc(4)**——3.5 英寸软盘控制器在现代硬件中已完全消失，最后一批带软驱的 PC 生产于 2000 年代中后期；**firewire(4)**——IEEE 1394 火线接口曾用于视频采集与高速外设，2010 年代后被 USB 3.x 与 Thunderbolt 完全取代；**syscons(4)**——旧版系统控制台驱动已被 **vt(4)**（Newcons）取代多年，**vt(4)** 支持 KMS、Unicode、高分辨率等现代特性；**upgt(4)**——GW3887 芯片 USB 无线网卡驱动支持 802.11g，已被现代 WiFi 5/6 驱动完全取代
- 15.x 周期（2025-2026）FreeBSD 社区纪念的重要贡献者：① **Mike Karels**（1956-08-02 至 2024-06-02）——CSRG BSD 核心开发者、4.3BSD 架构师、FreeBSD Release Engineering 长期成员、《4.3BSD/4.4BSD Design and Implementation》合著者，2024 年 6 月去世，FreeBSD 14.2（2024.12）献词给他〔生卒经 2026-09-12 核查报告 C223 按基准订正，原「1955/56?-2024.10」卒月误〕；② **Peter G. Neumann**（1932-）——Computer-Related Risks 作者、Multics 安全贡献者，2026 年仍在世（94 岁），FreeBSD 15.1（2026.6）献词给他以表彰他在计算机安全领域 60 年的贡献〔原「Capsacam capability security 理论奠基人」表述删除：Capsacam 系 Capsicum 拼写错误，且 Capsicum 系 Watson 团队成果与 Neumann 无直接谱系〕；③ **Hans Petter Selasky**（hselasky@）——FreeBSD USB 子系统维护者、核心开发者，2023 年去世，FreeBSD 14.0（2023.11）献词给他〔存疑：原稿生卒「1978?-2023」带问号且单源，待核〕

## 史观

- 总纲第 4 条——分离聚合是永恒规律：ftpd 移除是 BSD 项目持续剥离非核心网络服务的具体显现，与 14.x telnetd 移除、13.x ip6fw 移除构成同一长期工程脉络——base 仅保留必要组件，传统服务交由 Ports 系统维护；专题语（不设条号）：通过 ObsoleteFiles 机制平滑过渡，体现 “为正确性减负” 的工程治理原则（原挂“总纲第 17 条——软件工程”非基线条目名）
  - 辨析：ftpd 与 telnetd 在 14.x/15.x 期间相继移除，同属 base 内老旧网络服务的批量清理（详见辨析行）
- 总纲第 22 条——知识注定过时：32 位平台退役是 FreeBSD 对硬件代际更替的工程回应——AMD 64 位 Opteron 2003.4.22 发布至今已逾 22 年，与 Intel 8086 1978 发布时 x86 整体年龄相当（原挂“总纲第 7 条——硬件与软件辩证”非基线条目名，按报告建议改挂）；专题语（不设条号）：32 位 “硬件平台” 终结但 32 位 “应用兼容性” 通过 lib32 延续，体现 BSD 项目 “终结以延续为前提” 的辩证结构（原挂“总纲第 25 条——终结与延续”非基线条目名）
- 专题语（不设条号）：弃用工具的 “标记-推迟-移除” 三阶段流程是软件工程治理成熟度的体现，bsdlabel 的 longstanding buffer overflow 漏洞成为推动弃用的直接动因——维护资源应聚焦当代工具而非历史包袱；弃用标记本身是形式化治理的延伸，每次标记都是对工具生命周期的形式化宣告（原挂“总纲第 17 条——软件工程”“总纲第 3 条——形式主义膨胀”均非基线条目名或主题语不符）
  - 辨析：须严格区分 “bsdlabel/fdisk 标为弃用” 与 “从源码树移除” 两类事实（详见辨析行）
- 总纲第 22 条——知识注定过时：这批驱动的批量标弃用是硬件代际更替在软件层面的直接体现——AGP、软驱、FireWire 分别代表 1990 年代末至 2000 年代中期的主流接口技术，它们的退役不是技术优劣判断，而是硬件生态迭代的必然结果〔注：句尾原文截断，按上下文收束〕（原挂“总纲第 7 条——硬件与软件辩证”）
- 总纲第 10 条——动手者创造历史：FreeBSD 的 Dedication 传统是项目历史意识的体现——每个大版本都可能献词给一位逝去或有重大贡献的社区成员；这一传统提醒每位 committer：他们写的每一行代码都将加入一个持续 30 多年的代码库，这个代码库的寿命将超过任何个人的职业生涯；代码是给后人的遗产（原挂“总纲第 25 条——终结与延续”非基线条目名，纪念动手者论旨改挂第 10 条）

## 辨析

- ftpd 与 telnetd 在 14.x/15.x 期间相继移除体现 BSD 项目对 “上古网络服务” 的批量清理态度；但须严格区分 “ftpd 从 base 移除” 与 “ftpd 工具消失” 两类事实——前者为 15.0 实际事件，后者并未发生，ftp/freebsd-ftpd port 仍持续维护；FreeBSD FTP 客户端 **ftp(1)**（基于 tnftp）继续保留在 base
- 须严格区分 “32 位硬件平台退役” 与 “32 位应用兼容性移除” 两类事实——前者为 15.0 实际事件，后者并未发生且按 Colin Percival 在 freebsd-arch 邮件中的回应 “Hopefully never” 明确不会发生；社区讨论中出现 Vadim Goncharov 等用户对 32 位虚拟机构建持续需求的关切，反映退役决策对低内存虚拟机场景的影响；15.1 公告提到〔注：句尾原文截断，待回源〕
- 须严格区分 “bsdlabel/fdisk 标为弃用” 与 “bsdlabel/fdisk 从源码树移除” 两类事实——前者为 15.0 实际事件，后者原计划 15.0 实施但实际推迟至 16.0；社区讨论中 Warner Losh（沃纳·洛什）（<imp@bsdimp.com>）指出 nanobsd 的 legacy.sh 仍使用 disklabel，需要先迁移才能完全移除；fdisk 早期在其他平台的部署细节〔原文截断，待回源〕
- 须严格区分 “标记为 deprecated” 与 “已从源码树移除” 两类事实——上述 5 项驱动（agp/fdc/firewire/syscons/upgt）在 15.0 中仅标记为弃用，计划 16.0 移除，15.x 周期内仍可使用且默认编译；**gvinum(8)** 则是 **已在 15.0 实际移除**，接续路径为 ports 中的 sysutils/gvinum 或迁移至 ZFS/GE
- Dedication 献词选择由 Release Engineering Team 决定，通常纪念逝去的重要贡献者（如 Karels、Selasky）或表彰长期贡献者（如 Neumann）；不是每个版本都有 Dedication——15.0 公告中就没有 Dedication 部分
  - 文献：FreeBSD Project. Release Announcements Archive [EB/OL]. <https://www.freebsd.org/releases/>

## 文献

- FreeBSD 15.0-RELEASE Release Notes；lists.freebsd.org dev-commits-src-all 2025-October/061132；Phabricator D52739；FreeBSD UPDATING 20251001 条目 ［A］

## 164.10.2 i386/armv6/32 位 powerpc 架构在 15.0 正式退役

- FreeBSD 15.0-RELEASE Release Notes；lists.freebsd.org freebsd-arch 2025-June/000949 John Baldwin 头邮件；Core Team 2023.2 32 位平台弃用公告；FreeBSD Platforms 页面（freebsd.org/platforms） ［A］〔编排注：本节要点与章级要点重复，原属 163.10.2 旧号错挂节；要点已并入章级要点段，保留文献清单待结构性归并轮处置〕

## 164.10.3 bsdlabel 与 fdisk 弃用——fdisk 移除推迟至 16.0

- lists.freebsd.org freebsd-current 2024-January/005419 头邮件；lists.freebsd.org freebsd-current 2024-January/005420 Warner Losh 回复；Phabricator D43575；Phabricator D43563；lists.freebsd.org dev-commits-src-all 2025-October commit `2be4c64a0d27`；FreeBSD Project. FreeBSD 15.0-RELEASE Release Notes [EB/OL]. (2025-12-02)[2026-07-19]. <https://www.freebsd.org/releases/15.0R/relnotes/>; FreeBSD Project. agp(4) Manual Page [EB/OL]. [2026-07-19]. <https://man.freebsd.org/agp/4>; FreeBSD Project. vt(4) Manual Page [EB/OL]. [2026-07-19]. <https://man.freebsd.org/vt/4>; FreeBSD Project. Release Announcements Archive [EB/OL]. [2026-07-19]. <https://www.freebsd.org/releases/>.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准；原「<<https://ma>」截断残句已按 man.freebsd.org 惯例补全〕

## 164.8.2 核心开发者与新兴贡献者

- 要点：15.x 周期 FreeBSD 核心开发持续活跃的开发者群体包括（不完全名单）：Colin Percival（cperciva@，Release Engineer）〔原文截断，待回源〕
- FreeBSD Project. Contributors List [EB/OL]. [2026-07-19]. <https://www.freebsd.org/doc/en_US.ISO8859-1/articles/contributors/>.

## 164.8.3 30 周年后社区生态（2023-2026）

- 要点：FreeBSD 于 2023 年 6 月 19 日迎来 30 周年纪念（自 1993.6.19 FreeBSD 1.0 发布）
- FreeBSD Foundation. 30th Anniversary [EB/OL]. (2023-06)[2026-07-19]. <https://freebsdfoundation.org/blog/>; BSDCan Conference [EB/OL]. [2026-07-19]. <https://www.bsdcan.org/>. ［B］

## 164.8.4 FreeBSD 在 AI 工作负载中的角色

- 要点：截至 2026.7，FreeBSD 本身 **不包含** 任何 AI/LLM 特定的内核功能，但 FreeBSD 可作为 AI 工作负载的运行平台：① 通过 L〔原文截断，待回源〕
- FreeBSD Project. Linux Binary Compatibility [EB/OL]. [2026-07-19]. <https://docs.freebsd.org/en/books/handbook/linuxemu/>; llama.cpp on FreeBSD [EB/OL]. [2026-07-19]. <https://www.freshports.org/misc/llama.cpp/>（原始链接失效，互联网档案馆无存档）. ［B］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- dangan-20260908 消解回写 -->
- Let's Encrypt. Statistics [EB/OL]. [2026-07-19]. <https://letsencrypt.org/stats/>.〔编排注（2026-09-12 整改）：原条「Let. 's」空格异常、[EB/OL] 重复与内部定位符 DKC-2361→fulltext:6175 已清除〕
<!-- /dangan-20260908 -->
