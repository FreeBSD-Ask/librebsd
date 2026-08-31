---
chapter: 第 103 章
id: CH103
volume: 05
---

# 第103章 pf防火墙

## 要点

- PF（Packet Filter）由 Daniel Hartmeier（丹尼尔·哈特迈尔） 与 OpenBSD 团队于 2001 年开发，替代因许可证争议被移除的 IPFilter；PF 采用规则集优化（skip steps）与状态保持（stateful inspection）设计，首版随 OpenBSD 3.0（2001.12）发布
- FreeBSD 于 2004 年（5.3 RELEASE，2004.11.4，release/5.3.0 tagger_date = 2004-11-04T19:12:42Z，tagger = Ken Smith）首次将 PF 作为可选防火墙引入，由 Pyun YongHyeon、Max Laier 等完成移植；PF 导入 commit 为 2004-06-16T23:03:14Z（commit_hash = 32b30983561ed562aa495d8e124488ab94b332aa，committer = Max Laier，message_subject = "Import pf from OpenBSD 3.5 (OPENBSD_3_5_BASE)"），早于 5.3-RELEASE 约 4.5 个月，属 5-CURRENT 开发周期；移植包括内核钩子、用户态 pfctl 工具与 ALTQ 流量整形框架
- PF 从 OpenBSD 流入 FreeBSD/NetBSD/DragonFly BSD，体现 BSD 生态的代码共享性；但各 BSD 对 PF 的维护投入不同，FreeBSD 增加了 SMP 扩展与 VNET 支持，导致功能分化
- 移植史料疑点：(1) 移植起始时间（2003 年 编程之夏 项目 vs 2004 年 5.3 集成）；(2) 主要移植者的归属；(3) OpenBSD 团队是否参与 FreeBSD 移植
- Linux iptables（1998，Rusty Russell 设计）采用规则链 + 目标设计，是 Linux 2.4+ 主流防火墙；nftables（2014，Patrick McHardy 主导）采用虚拟机字节码设计，替代 iptables；二者是 Linux 主流防火墙路线

## 史观

- 总纲第 1 条——偶然性改写历史，IPFilter 许可证争议催生 PF 这一全新防火墙
  - 辨析：PF 是否完全由 Hartmeier 一人开发，需查 commit log 确认其他 OpenBSD 开发者的贡献；0 信任原则适用说明：L2.3.1.pf 查询在中观模式挖掘报告中缺失，须直接查询 netbsd.db 验证 PF 引入周期；L2.4.1.Import from 查询使用 "Im
- 总纲第 7 条——BSD 与 UNIX 谱系的连续性，PF 跨 BSD 项目流动体现谱系共享
  - 辨析：经 bsd_commits.db commits 表验证，PF 导入 commit 为 2004-06-16T23:03:14Z（早于 5.3-RELEASE 约 4.5 个月，属 5-CURRENT 开发周期）；经 bsd_commits.db tags 表验证，5.3-RELEASE 的
- 总纲第 9 条——简洁与复杂的辩证，iptables 重简洁、nftables 重灵活
  - 辨析：iptables/nftables 与 PF 优劣，需查基准测试
  - 文献：iptables 文档；nftables 文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

##

- 总纲第 9 条——简洁与复杂的辩证，三者设计哲学反映对简洁与复杂的不同取舍
  - 辨析：三者优劣，需查基准测试；设计哲学差异是否决定性能差异
  - 文献：作者不详. ipfw(8)/ipf(5)/pf.conf(5) 手册页[Z]. 年份不详 ［A］

## 102.2.2 争论的社区过程

- 要点：FreeBSD 社区在 ipfw/IPF/PF 三者间争论持续多年（2001-2006），核
- 总纲第 1 条——偶然性改写历史，许可证修改偶然引发 PF 诞生
  - 辨析：修改的具体内容与时间，需查 LICENSE 文件版本对比；Reed 修改的动机
  - 文献：IPFilter LICENSE 文件；OpenBSD misc 邮件[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补

## 辨析

- PF 是否完全由 Hartmeier 一人开发，需查 commit log 确认其他 OpenBSD 开发者的贡献；0 信任原则适用说明：L2.3.1.pf 查询在中观模式挖掘报告中缺失，须直接查询 netbsd.db 验证 PF 引入周期；L2.4.1.Import from 查询使用 "Import from" 关键词未命中 PF 导入 commit（message_subject 为 "Im
- 经 bsd_commits.db commits 表验证，PF 导入 commit 为 2004-06-16T23:03:14Z（早于 5.3-RELEASE 约 4.5 个月，属 5-CURRENT 开发周期）；经 bsd_commits.db tags 表验证，5.3-RELEASE 的 tagger_date 为 2004-11-04T19:12:42Z（非旧叙事 2004.11.6，误差
- iptables/nftables 与 PF 优劣，需查基准测试
  - 文献：iptables 文档；nftables 文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 102.10.2 Windows Firewall 与 Solaris IP Filter

- 要
- 三者优劣，需查基准测试；设计哲学差异是否决定性能差异
  - 文献：作者不详. ipfw(8)/ipf(5)/pf.conf(5) 手册页[Z]. 年份不详 ［A］

## 102.2.2 争论的社区过程

- 要点：FreeBSD 社区在 ipfw/IPF/PF 三者间争论持续多年（2001-2006），核心是默认防火墙的选择；最终 FreeBSD 同时保留三者，由用户选择，但 PF 逐渐成为推
- 修改的具体内容与时间，需查 LICENSE 文件版本对比；Reed 修改的动机
  - 文献：IPFilter LICENSE 文件；OpenBSD misc 邮件[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 102.3.2 开源合规质疑的爆发

- 要点：OpenBSD

## 文献

- Hartmeier "OpenBSD Packet Filter"（ONLamp 2002）；**pf.conf(5)** 手册页 ［A］；freebsd.db L2.3.1.pf 查询结果（中观模式挖掘报告缺失，须直接查询）[DB/OL]；freebsd.db L2.4.1.Import from 查询结果（PF 导入 commit 未命中，关键词匹配局限）[DB/OL]；freebsd.db L2.2.1.sys_net 查询结果（freebsd-src sys/net/ 年度 commit 量 2004-2010）[DB/OL] ［A］

## 102.1.2 移植的工程过程

- 要点
- FreeBSD 5.3 Release Notes；freebsd-pf 邮件列表；Max Laier. Import pf from OpenBSD 3.5 (OPENBSD_3_5_BASE). freebsd-src [DB/OL]. 2004-06-16T23:03:14Z. commit: 32b30983561ed562aa495d8e124488ab94b332aa；release/5.3.0. freebsd-src 仓库 tag [DB/OL]. 2004-11-04T19:12:42Z. tag: release/5.3.0; commit: f8d4987d7271c10
- iptables 文档；nftables 文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 102.10.2 Windows Firewall 与 Solaris IP Filter

- 要点：Windows Firewall（2001，Windows XP 引入，2004 SP2 默认启用）采用规则列表设计；Solaris IP Filter（即 IPFilter，Sun 移植）采用 NAT+ 状态保持设计；二者代表商业 OS 防火墙路线
- 史料：MSDN
- 作者不详. ipfw(8)/ipf(5)/pf.conf(5) 手册页[Z]. 年份不详 ［A］

## 102.2.2 争论的社区过程

- 要点：FreeBSD 社区在 ipfw/IPF/PF 三者间争论持续多年（2001-2006），核心是默认防火墙的选择；最终 FreeBSD 同时保留三者，由用户选择，但 PF 逐渐成为推荐选项
- 史料：freebsd-security、freebsd-hackers 邮件列表存档 ［A］
- 史观：总纲第 6 条——形式主义膨胀与抽象克制，三者并存是否形式主义膨胀
- 辨析：争论是否促进改进，需查改进记录；三者并存是否增加维护成本
  
- IPFilter LICENSE 文件；OpenBSD misc 邮件[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 102.3.2 开源合规质疑的爆发

- 要点：OpenBSD 团队（Theo de Raadt（西奥·德·若特） 等）于 2001 年公开质疑 IPFilter 许可证合规性，认为修改后的措辞不符合 OpenBSD 的许可证政策；OpenBSD 3.0（2001.12）移除 IPFilter 并以 PF 替代
- 史料：OpenBSD misc 邮
- IPFilter LICENSE 文件[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 102.4.2 社区的应对策略

- 要点：各 BSD 社区对 IPFilter 许可证变迁的应对：(1) OpenBSD 移除并自建 PF；(2) FreeBSD 保留 IPFilter 但推荐 PF/ipfw；(3) NetBSD 维持 IPFilter 支持；不同策略反映各社区的风险偏好与法律判断
- 史料：各 BSD Release Notes、邮件列表 ［A］
- 史
- DragonFly BSD commit log ［A］

## 102.5.2 移除的工程效应

- 要点：移除 IPFilter 后，DragonFly BSD 用户需迁移至 PF 或 ipfw；移除简化了内核维护但增加了用户迁移成本
- 史料：DragonFly BSD Release Notes[考据完成：2026-07-28 经穷尽联网考据，上述史料清单为已知公开来源汇总，部分原始档案未公开数字化或须档案馆藏地现场核验，属史料缺口，须待原始档案公开后方可补充确证] 〔L3 官方文档〕
- 史观：总纲第 9 条——简洁与复杂的辩证，移除简化内核但增加用户负担
- 辨析：迁移
- Adamo & Tablo 论文（USENIX ; login: 2005） ［B］

## 102.6.2 Linux nftables 自建路线

- 要点：Linux netfilter 社区选择自建 nftables（2014 发布，Patrick McHardy 主导）而非移植 PF，理由是 PF 的 OpenBSD 内核耦合度不适合 Linux；nftables 采用虚拟机字节码设计，提供更灵活的规则表达
- 史料：nftables 文档、netfilter 邮件列表 ［A］
- 史观：总纲第 14 条——话语权与边缘者，Linux 自建 nftables 是对 PF 路线

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP651、BSD Now EP648、BSD Now EP360、BSD Now EP640、BSD Now EP213、BSD Now EP143、BSD Now EP46、BSD Now EP24、BSD Now EP18、BSD Now EP11（共 10 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 邮件服务器作者以 PF 表加载 MaxMind GeoLite2 的约 27 万条 CIDR，对客户端端口按国家限制、仅 SMTP 保持全球可达，实现暴力破解日志下降约九成。（BSD Now EP651，[110.76-456.00]，L1）
- Alan Jude 的 ZFS 生产部署文章强调，ZFS 事故多为早期布局决策与运维漂移的延迟后果；数据集划分、VDEV 布局、快照策略与持续监控比依赖单一特性更重要。（BSD Now EP651，[782.30-1438.40]，L1）
- FreeBSD 的 Linuxulator 经 SSHD 环境变量引导 Linux bash，使 VS Code Remote SSH 透明运行 Linux 二进制，作者视为 Linux ABI 稳定性与 FreeBSD 兼容层实现质量的证明。（BSD Now EP651，[2152.32-2509.78]，L1）
- OpenBSD arm64 在 Apple Hypervisor 上以客户机运行的提交修复了 VIGPU 地址映射与 DMA 同步问题，并支持 virtio 网络 MTU 协商。（BSD Now EP651，[2838.30-2965.62]，L2）
- FreeBSD Foundation 2026 募款文显示资金约三分之二用于软件开发，其余用于宣传教育、基础设施与筹款管理，强调捐赠直接支撑笔记本电脑、构建测试与持续集成。（BSD Now EP648，[103.42-208.70]，L2）
- Peter N. M. Hansteen 自述 2007 年起运行 spamd 灰度陷阱，截至 2025 年 8 月陷阱条目超过 562 万、超过挪威人口，数据显示垃圾邮件活动呈下降趋势但伴随突发峰值。（BSD Now EP648，[257.02-1152.28]，L1）
- BSDCan 组织委员会回顾会议由 Dan Langille 在渥太华大学创办并连续举办 22 年，领导权经 Dan Langille、Michael W. Lucas 逐代交接，规划委员会维持约 12 人。（BSD Now EP648，[1246.88-1475.48]，L1）
- BSDCan 2026 延续教程加两天会议的形式，AV 团队与 ScaleEngine 合作向 YouTube 与 PeerTube 同步直播，并计划提高分辨率与音频质量。（BSD Now EP648，[2144.22-2315.56]，L1）
- Chris Siebenmann 以 400 余行既有 PF 规则、本地运维工具与团队知识三个理由说明从 OpenBSD PF 迁往 Linux nftables 的代价高于收益。（BSD Now EP648，[3328.02-3441.68]，L1）
- 追查坏提交的文章介绍用 git bisect 二分定位引入回归的提交，并指出破坏可能来自非直观的依赖变更。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 完成 2020 年第十一届 Core 团队选举，Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Kyle Evans、Mark Johnston、Scott Long、Sean Chittenden、Warner Losh 当选。（BSD Now EP360，[460.69-614.65]，L2）
- NetBSD 在 Pinebook Pro 上以 NetBSD 9 用户态搭配 Current 内核运行，以兼顾二进制包与更好的硬件支持。（BSD Now EP360，[624.57-842.58]，L2）
- pf 状态表存在默认大小限制，FreeBSD 另有 `net.pf.request_maxcount` sysctl 控制单次 ioctl 载入表项数；DragonFly 侧限制为静态内核值。（BSD Now EP360，[1199.40-1404.41]，L2）
- FreeBSD 在 OCI Runtime Specification 1.3 中被列为官方支持平台，路径包括 Samuel Karp 的 RunJ、Doug Rabson 的 Buildah 与 Podman 移植以及官方镜像。（BSD Now EP640，[106.30-305.54]，L2）
- Jim Salter 的 ZFS 灾难恢复文章以 Sanoid 与 Syncoid 实现快照、销毁与复制的自动化，并强调 RAID 不是备份、备份机应主动拉取而非被动接收。（BSD Now EP640，[339.80-818.48]，L1）
- Chris Siebenmann 通过阅读 DSL 源码说明 ZFS 的 written 与 written@ 属性即时计算，written 需回加已释放空间以避免负值。（BSD Now EP640，[849.96-1060.68]，L1）
- Justin Sherrill 提醒间歇运行的 DragonFly BSD 虚拟机与笔记本因 cron 不触发而无法自动执行 HAMMER 清理，须手动运行 cleanup 以防空间耗尽。（BSD Now EP640，[1070.44-1192.64]，L1）
- CHM 2024 年发布的 Ken Thompson 与 Doug McIlroy 口述史含转录与约四个半小时视频，回顾贝尔实验室与早期 Unix。（BSD Now EP640，[1218.68-1264.24]，L2）
- 1966 年 Joseph Weizenbaum 发表 ELIZA 一文，ELIZA 被视为最早聊天机器人之一，其引发的拟人化反应即 Eliza 效应，并推动作者转向人工智能批评。（BSD Now EP640，[1272.40-1486.48]，L2）
- David Gwynne 在 OpenBSD 引入 source 与 state limiters，以单一限流器跨多端口限制状态数与创建速率，缓解规则重载带来的状态计数重置问题。（BSD Now EP640，[1581.78-1846.92]，L1）
- EuroBSDCon 2017 在巴黎举行，主持人参会期间组织开发者以七分钟短讲介绍各自正在推进或寻求反馈的工作，这一 work in progress 形式与 AsiaBSDCon 类似。（BSD Now EP213，[376.86-393.88]，L1）
- FreeBSD 基金会董事会在巴黎举行，与会成员讨论 FreeBSD 10.4 测试与发布稳定、注册截止等问题；主持人还介绍 EuroBSDCon 次年将移师罗马尼亚布加勒斯特。（BSD Now EP213，[757.00-1311.38]，L1）
- PF 缺陷故事：Christophe 提交的博客还原了一个 vnet jail 中 PF 与宿主机 PF 实例相互干扰导致 panic 的问题，修复要点是把 purge 状态的索引变量改为 per-vnet 变量，避免多 PF 实例共享状态。（BSD Now EP213，[1335.70-1904.14]，L2）
- Matthew Macy 自述其 BSD 历程：在伯克利操作系统课上接触 FreeBSD 2.1.x，此后完成 i386 版 Xen 的 FreeBSD 移植并由此获得 commit bit，随后参与 Chelsio 万兆网卡驱动，并在 DragonFly 时期完成进程检查点设施与虚拟内存页粒度锁下推等工作。（BSD Now EP143，[1505.00-1702.00]，L1）
- Macy 说明更新图形栈的动机链条：因机器学习需要 GPGPU 且 CUDA 仅限 Linux，AMD Radeon Open Compute 提供跨厂商替代，但其依赖链 AMDKFD、AMDGPU 迫使先更新 DRM；他选择从 i915 入手，理由是 Intel 约占七成 GPU 市场且驱动质量最好。（BSD Now EP143，[2233.00-2459.00]，L1）
- 图形栈更新的核心策略是 Linux KPI 路线：保持驱动尽量接近上游、本地 diff 仅约四百五十行（对照 12.8 万行的 i915 4.6 驱动），长期维护负担取决于驱动对内核接口使用面的扩张而非驱动自身改动；在 KPI 稳定于 11.1 或 11.2 前以 ports 形式独立发布。（BSD Now EP143，[3168.00-3326.00]，L1）
- Macy 解释 iflib 的设计：网络驱动间大量复制粘贴导致厂商自行维护时抹去性能优化，iflib 抽象队列分配、调度、TX 清理等设备无关代码，驱动只负责寄存器、固件与描述符转换；Netflix 在 Intel 40GbE 上用 iflib 获得优于 legacy 驱动的性能与最坏情况 CPU 占用。（BSD Now EP143，[1943.00-2117.00]，L1）
- Macy 回顾其 ZFS 工作：低端 OCZ SSD 因写放大特性用 UFS 几不可用而 ZFS 反而可用，由此在 ARC 做锁下推并修复 Solaris 开发者一度不愿承认的 prefetch 争用；又因 ZFS 的 ARC 大量 wire 内存使 minidump 巨大，他增加 no-dump 页排除特性使 ZFS 上的 core dump 重归可用。（BSD Now EP143，[1755.00-1939.00]，L1）
- 新闻综述：Package Base 未赶上 FreeBSD 11.0 而推迟至 11.1，pkg 1.8 将 precious 标志更名 vital；11 起新支持模型规定后续 minor 版本发布后旧版本即过期，以解决 8.4、9.3 长期拖住 ports tree 的问题。（BSD Now EP143，[4934.00-5134.00]，L2）
- Olivier 的 PF 基准实测四百万状态条目：states hash 每条目约占 80 字节、须取 2 的幂，128 条与四百万条之间吞吐差距约百分之十二，验证小型硬件在充分内存与 hash 配置下可承载大规模并发会话。（BSD Now EP143，[128.00-330.00]，L2）
- PHK 在 VarnishCache 博客中以 FreeBSD 为其项目首要的“keep us honest”平台：三个 jail 分别承载 varnish、hitch 与工具链，从裸机到可运行约十五分钟；他自述 jail 系其 1998 年所写，配置全部入版本控制、备份即 git clone。（BSD Now EP143，[995.00-1250.00]，L2）
- Bryan Drewery（转写误作 Brian Drury）自述入圈路径：2003 年前后经 IRC 结识经营 shell 服务的 FreeBSD 4.11 用户而入坑，2012 年因不满包安装状态找到 pkgng 项目并协同 Baptiste Daroussin，从提交补丁到获 ports 提交权，再到以包框架贡献者身份进入 Port Manager 团队并新获 source 提交权——包体系维护者由工具建设者自然生长而成。（BSD Now EP46，[1963.44-2018.28]，L1）
- FreeBSD 官方包构建集群的一手运维细节：四台号称 beefy 的机器各配 32 核与 96—100GB 内存，每周二 UTC 凌晨一点对 ports 树拍快照并按各发布版与 head 构建 x86 包集，全量需三至五天；另有八套每日测试系统覆盖非 root 构建、打包测试与 QA，quarterly 季度分支自 head 切出并回灌安全修复，属仍在试验中的稳定化机制。（BSD Now EP46，[2439.92-2628.96]，L1）
- iodine DNS 隧道演示的实操要点构成其技术史价值：服务端以特权分离用户与 chroot 运行但密码将以明文见于进程列表，且 iodined 须独占一个 IP 承担 DNS 应答而无法与既有域名服务共存；客户端探测可用查询类型并按 DNS 包尺寸协商 MTU，建隧道后经压缩 SSH 登录验证，并可与 stunnel、SSH 链式跳板教程组合成受限网络下的成套突围方案。（BSD Now EP46，[5978.10-6327.42]，L1）
- NYCBSDCon 2014 以“BSD in production”为主题，Dru Lavigne 开场，议题包括 FreeNAS/PC-BSD 的 ZFS 管理、BSD 路由器及以 FreeBSD 与 ZFS 运行 PostgreSQL。（BSD Now EP24，[73.68-95.60]，L2）
- Luke Marsden 自述 15 岁起经营主机公司，在牛津学习理论计算机科学后创立 HybridCluster，以解决主机业务中反复出现的宕机与扩展问题。（BSD Now EP24，[1074.80-1171.02]，L1）
- HybridCluster 以 jail 或容器为应用单元，基于 ZFS 快照与 send/receive 实现异步复制、故障转移与亚秒级活迁移，作为 SAN 与虚拟机方案的替代。（BSD Now EP24，[1282.16-1548.36]，L1）
- HybridCluster 部署的操作系统为略经修改的 FreeBSD 9.2 stable，工程师 Andriy Gapon 为 FreeBSD 开发者并将修复回馈社区；产品以每服务器每月 160 美元许可销售。（BSD Now EP24，[1557.08-1612.28]，L1）
- 新闻讨论 FreeBSD 10 作为防火墙：PF 经 SMP 优化后性能更强但规则语法较旧，简单规则场景下 IPFW 因解析路径更短而更快。（BSD Now EP24，[480.68-577.34]，L2）
- 主持人转述 Justin Sherrill 的观点：PF 已被 FreeBSD、NetBSD、macOS 等吸收，但各实现基于不同时期的 OpenBSD 版本且无版本号，导致规则语法与功能分化。（BSD Now EP18，[346.52-362.32]，L2）
- 节目讨论以 OpenSSH portable 或 OpenZFS 共同核心为参照，为 PF 建立可移植层（被称为 PPL 或 OpenPF 构想）；Henning Brauer 表示愿意协助，但该项目当时尚未落地。（BSD Now EP18，[454.58-557.28]，L2）
- Baptiste Daroussin 自述因厌倦反复源码编译而设计 PackageNG，后在 BSDCan 演讲并取得 ports commit bit，成为 portmgr 成员。（BSD Now EP18，[993.58-1029.66]，L1）
- PackageNG 方向为将 poudriere 由面向最终用户的安装工具转为基础设施构建工具，并引入 staging、autoplist、子包、flavors/providers 及基于 fingerprint 的仓库签名，以解决冲突、改名与多版本包问题。（BSD Now EP18，[1049.62-1253.12]，L1）
- OpenBSD 长期缺乏官方跨版本升级工具，第三方 ksh 脚本 OpenBSD Binary Upgrade 可完成 5.3 到 5.4 的二进制升级与旧文件清理，但仅校验 SHA256 而不提供签名。（BSD Now EP18，[2198.60-2266.36]，L2）
- Justin Sherrill 自述约 2000 年首次接触 BSD，后因 Matt Dillon 从 FreeBSD 分支 DragonFly 而加入，长期负责 DragonFly Digest、发布管理与 Summer of Code 组织工作。（BSD Now EP11，[681.7-851.1]，L1）
- 他说明 DragonFly 分叉源于 Matt Dillon 与 FreeBSD 在对称多处理路线上的分歧，Dillon 倾向轻量、简单的并发方式，最终使 DragonFly 网络栈几乎去除 BSD 世界常见的大型锁。（BSD Now EP11，[903.6-1005.7]，L1）
- DragonFly BSD 3.6 将 dports（基于 Poudriere 构建的 DragonFly 版 ports）设为默认，并加入 SMP 扩展性改进与 Intel、AMD 图形支持的移植。（BSD Now EP11，[4692.8-496.0]，L3）
- 新闻提及 OpenSSH 6.5 将 Curve25519 设为默认密钥交换算法，FreeBSD 引导菜单加入内核选择功能，Colin Percival 推出内核 panic 报告工具。（BSD Now EP11，[4762.8-4812.0]，L2）

**史料**：

- Klara Systems（Alan Jude）博客文章 ZFS in Production: Real-World Deployments, Patterns, and Pitfalls。（BSD Now EP651，[782.30-1438.40]，L1）
- Rubenerd 博客关于 XFCE 桌面与 FreeBSD Linuxulator 远程开发的两篇文章。（BSD Now EP651，[1500.36-1745.60]，L1）
- Undeadly.org 关于 OpenBSD arm64 支持 Apple Hypervisor 的提交报道。（BSD Now EP651，[2838.30-2965.62]，L2）
- Peter N. M. Hansteen 博客《18 years of grey trapping》及历年陷阱数据文件。（BSD Now EP648，[257.02-1152.28]，L1）
- FreeBSD Foundation 由 Deb Goodkin 署名的年度募款文章 Powering the Future of BSD。（BSD Now EP648，[103.42-208.70]，L2）
- BSDCan 2026 组织委员会 Pat、Peter、Michael 访谈。（BSD Now EP648，[1226.50-2782.18]，L1）
- 追查坏提交博文与 git bisect 说明。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 2020 年 Core 团队选举公告，由主持人转述当选名单。（BSD Now EP360，[460.69-614.65]，L2）
- FreeBSD Foundation 博客 FreeBSD Officially Supported in the OCI Runtime Specification 1.3。（BSD Now EP640，[106.30-305.54]，L2）
- Jim Salter 于 Klara Systems 的 ZFS 灾难恢复文章。（BSD Now EP640，[339.80-818.48]，L1）
- Chris Siebenmann 关于 OpenZFS written 与 written@ 属性的博客。（BSD Now EP640，[849.96-1060.68]，L1）
- Justin Sherrill 的 DragonFly BSD Digest。（BSD Now EP640，[1070.44-1192.64]，L1）
- David Gwynne 的 Undeadly 文章 source and state limiters in PF。（BSD Now EP640，[1581.78-1846.92]，L1）
- Christophe 关于 PF 缺陷修复的博客；EuroBSDCon 2017 会议议程与 FreeBSD 基金会董事会记录。（BSD Now EP213，[1335.70-1904.14]，L2）
- Macy 提供的图形栈测试材料：DRM next 4.6 分支、可直接写入 U 盘启动的测试镜像（XFCE 与 KDE、SNA/UXA 加速模式切换）与 PC-BSD 每月 current 镜像拉入补丁的安排。（BSD Now EP143，[3784.00-3965.00]，L1）
- Peter 在 DragonFly 邮件列表的 xWayland 运行报告（GTK3 应用与 Firefox 可用、Chrome 失败）与 Olivier 的 PF 状态表基准博客，均为当期可追溯的一手技术记述。（BSD Now EP143，[5451.00-5503.00]，L2）
- 本期经主持人提及可资查证的一手史料：FreeBSD 9.3-RELEASE 公告与 release notes（iSCSI 可加载、ARC 元数据限额运行时可调、on-if-console 便于 bhyve 直用官方镜像）、pkgng 1.3 RC2 邮件列表通告、LibreSSL 便携版 2.0.x 于 OpenBSD FTP 发布并已入 ports、2014 年 FreeBSD 核心团队九人选举名单（Gavin Atkinson、David Chisnall、Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Gleb Smirnoff、Peter Wemm、Robert Watson）、EuroBSDCon 2014 索菲亚注册页与开发者峰会邀请制说明。（BSD Now EP46，[1052.16-1090.52]，L2）
- 本期史料包括 NYCBSDCon 2014 议程与现场反馈、Luke Marsden 访谈（当事人自述）、HybridCluster 产品说明及 FreeBSD 10 PF/IPFW 讨论。（BSD Now EP24，[1059.58-1612.28]，L1）
- 本期史料包括 Justin Sherrill 博客观点、Henning Brauer 对 PF 可移植层的表态、Baptiste Daroussin 访谈（当事人自述）以及 OpenBSD Binary Upgrade 第三方脚本。（BSD Now EP18，[346.52-557.28]，L1）
- 当事人提及 DragonFly 分叉公告约在访谈时点的十年前发布，并称其并发模型以 token 传递为主，进程在获得内存或系统资源时持有 token、阻塞时即释放。（BSD Now EP11，[985.4-1010.8]，L1）

**史观**：

- 总纲9 经验优先：总纲9 经验优先：邮件服务器作者以实际运维数据评估地理过滤的收益与代价，而非依赖纸面推断。（BSD Now EP651，[449.80-530.32]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Alan Jude 记录的 ZFS 事故源于接错线缆、换错盘等一线操作，运维纪律而非技术神话决定成败。（BSD Now EP651，[1336.04-1395.14]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：OpenBSD 与 FreeBSD 在虚拟化与兼容层上各自吸收上游技术又保持分化，构成分合循环。（BSD Now EP651，[2852.22-2965.62]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Hansteen 以十八年持续运维累积的灰度陷阱数据，记录的是不被聚光灯照到的反垃圾邮件一线工作。（BSD Now EP648，[257.02-1152.28]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：BSDCan 领导权在代际之间交接、规划委员会持续吸纳新人，体现社区组织的聚合与再分配。（BSD Now EP648，[1382.64-1467.34]，L1）
- 总纲9 经验优先：总纲9 经验优先：Siebenmann 从自身运维规则集与工具链出发评估防火墙迁移，而非依赖抽象性能宣传。（BSD Now EP648，[3368.44-3441.68]，L1）
- 总纲10 动手者创造历史：FreeBSD 决策由“到场者”作出，主持人与提问者强调社区参与决定项目走向。（BSD Now EP360，[2452.99-2456.55]，L2）
- 总纲4 分离聚合是永恒规律：Core 团队成员更替体现治理层的分离与再聚合。（BSD Now EP360，[460.69-614.65]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：OCI 支持由 Samuel Karp、Doug Rabson 等志愿者的多年内核与工具链工作累积而成。（BSD Now EP640，[227.38-305.54]，L2）
- 总纲9 经验优先：总纲9 经验优先：Jim Salter 以亲身经历过的断电、火灾、失窃等故障说明为何 RAID 不等于备份。（BSD Now EP640，[630.76-692.68]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：HAMMER 清理依赖 cron 定时触发的假设在笔记本关机场景下失效，反映旧运维假设随硬件使用方式变化而过时。（BSD Now EP640，[1081.24-1215.64]，L1）
- 总纲10 动手者创造历史：Christophe 通过测试脚本复现 vnet 中的 PF panic 并逐行修复，是动手者以调试实践改进防火墙代码的典型记录。（BSD Now EP213，[1413.72-1904.14]，L2）
- 总纲10 动手者创造历史：Macy 的 dogfooding 议程主张 FreeBSD 应在任意笔记本上开箱可用，路径是让 Linux 开发者的驱动工作经由 KPI 直接为 FreeBSD 复用——以动手者的具体可用性而非抽象优越性为目标。（BSD Now EP143，[2489.00-2634.00]，L1）
- 总纲5 没有必然性，只有偶然性：Package Base 错过 11.0 属冻结窗口内缺陷集中暴露的偶然事件，节目将其归因于“最后一刻努力仍不够”的具体条件，而非路线本身失败。（BSD Now EP143，[4943.00-4974.00]，L2）
- 总纲10 动手者创造历史：包体系的演进由动手者驱动而非领袖钦定：Google Summer of Code 学生写出新的依赖求解器使 package set -o 大半退役，构建集群从小两台机器被不断塞机器式地扩张并由个人以自写脚本勉力管理，Port Manager lurker 计划以 IRC 频道吸纳 Matt、Steve Wills 等新血——基础设施史的正主是这些具体操持者，正合总纲之动手者创造历史。（BSD Now EP46，[2126.10-2148.62]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Luke Marsden 自建主机公司并发展为 HybridCluster，是动手者以创业实践推动系统应用的代表。（BSD Now EP24，[1074.80-1171.02]，L1）
- 总纲11 商品是形式主义：总纲11 商品是形式主义：HybridCluster 以许可模式售卖基于 jail 与 ZFS 的虚拟 SAN 与容器平台，体现软件商品化的形式。（BSD Now EP24，[1587.16-1612.28]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：通过 ZFS 复制与 jail 迁移，实现计算与存储在集群中的分离与再聚合。（BSD Now EP24，[1282.16-1548.36]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：PF 随各 BSD 分支而分离，又出现以共同核心重新聚合的讨论，呈现分离与聚合的循环。（BSD Now EP18，[359.44-413.44]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Baptiste Daroussin 因个人反复编译的痛点动手重写包系统，改变 FreeBSD 软件分发方式。（BSD Now EP18，[993.58-1029.66]，L1）
- 总纲18 时间是一种形式主义：总纲18 时间是一种形式主义：PF 缺乏版本号使各实现难以按时间锚定演进，说明版本命名是形式化的时间标记。（BSD Now EP18，[425.34-439.46]，L2）
- 总纲4 分离聚合是永恒规律：DragonFly 的分叉呈现为多处理路线分歧推动的一次分离，而非单一技术演进的必然结果。（BSD Now EP11，[903.6-965.6]，L1）
- 总纲10 动手者创造历史：Justin Sherrill 长期承担文档、发布与组织工作而非核心代码，说明项目维护依赖多元角色的动手者共同支撑。（BSD Now EP11，[774.9-861.7]，L1）

**辨析**：

- 转录将 Klara Systems 误记为 Clara Systems，将 Rubenerd 误记为 Rubinerd 或 Ruben Nerd，正文按业界通行名处理。　[考据脚注] 机构与博客名存在语音转写偏差，须以原文链接核验（BSD Now EP651，[782.30-782.70]，L4）
- 转录中 OpenBSD PA-RISC 移植者被记作 Michael Shaliff，实为 Michael Shalayeff；因语音转写歧义，人名须以代码仓库与邮件列表核验。　[存疑脚注] 人名拼写存在转写歧义，未以 OpenBSD 代码仓库核验（BSD Now EP651，[2700.56-2735.66]，L4）
- 转录将 Peter N. M. Hansteen 误记为 Peter N.M. Hanstein，且陷阱总数 17,8238 的数字断词存疑，须对照原文与数据文件。　[存疑脚注] 人名与统计数字存在语音转写歧义，须以原文与数据文件核验（BSD Now EP648，[997.58-1005.20]，L4）
- DragonFly 的 pf 表限制是静态内核值且未暴露为可调 sysctl，是否需要仿照 FreeBSD 改造仍待确认。　[存疑脚注] DragonFly 侧改造计划待核实（BSD Now EP360，[1360.80-1390.40]，L4）
- 转录将 Doug Rabson 记作 Doug Rapson、将 Dave Cottlehuber 记作 Dave Cossel-Huber，人名拼写存在转写歧义。　[存疑脚注] 贡献者姓名存在语音转写偏差，须以 FreeBSD Foundation 公告核验（BSD Now EP640，[227.38-290.18]，L4）
- ELIZA 作者名在转录中拼作 Weisenbaum 或 Weisenbalm，通行写法为 Joseph Weizenbaum，须以原始论文核验。　[考据脚注] 人名拼写存在转写偏差，以 Communications of the ACM 1966 年原文为准（BSD Now EP640，[1279.84-1342.08]，L4）
- Macy 澄清更新 Linux KPI 与 Linux ABI 兼容层基本无关：ABI 层自 2.6.32 以来新增系统调用甚少，inotify 等缺失仍是 Dropbox 类应用的障碍；填平 ABI 缺口是其桌面 dogfooding 计划的另一部分。　[考据脚注] 关于 i965 支持与 Intel Gen10 二进制 blob 是否会为 FreeBSD 重编，Macy 仅引述未经证实的内部消息（BSD Now EP143，[4418.00-4484.00]，L1）
- 关于 Netflix 存储架构的孤证说法须存疑：主持人称 Netflix 以 discrete wire 将 SATA 磁盘一对一接 LSI HBA 而回避 SAS 扩展器，并自认“我不是百分百确定”（4922.54）；此说既非当事人自述亦无文档佐证，且转写将 HBA 误作 HPA，引用前应以 Netflix 工程实践一手材料核证。　[存疑脚注] 说话人自陈不确定且非当事人，属单一来源推断，Netflix 磁盘直连实践待核（BSD Now EP46，[4918.94-4944.68]，L4）
- PF 双雄之争在节目中仅为转述层材料：OpenBSD 邮件列表风暴中社区主张与其仅 SMP 化 PF 不如做通用 SMP 改造，DragonFly 已多线程化 PF，FreeBSD 侧则有 PF 前途之问与 IPFW 复兴的杂音；“快四倍”“随核数线性”等数字均出自主持人复述，且网卡多队列等底层论断含糊，映射入史前必须回查 2014 年邮件列表原帖。　[存疑脚注] 争论细节与性能数字仅经主持人转述，须以邮件列表一手原文复核（BSD Now EP46，[668.06-893.54]，L2）
- HybridCluster 活迁移亚秒级为其商业宣传口径，需独立验证；NYCBSDCon 议题与演讲细节为主持人转述，需与会议议程核对。　[存疑脚注] 活迁移性能与会议细节以官方发布为准，需交叉验证。（BSD Now EP24，[1494.88-1500.64]，L4）
- 主持人将 DragonFly 的 PF 对应 OpenBSD 4.4、FreeBSD 对应 4.5 等版本关系为口头转述，需与各项目代码核对；OpenPF 项目在 2014 年成立属对未来的期许而非既成事实。　[存疑脚注] 各 BSD 的 PF 版本对应与 OpenPF 立项状态需以源码与邮件列表原始记录复核。（BSD Now EP18，[386.32-439.46]，L4）

**文献**：

- [BSD Now EP651] Pennington J. BSD Now: 651: Spatially aware ZFS[EB/OL]. (2026-02-19)[2026-08-15]. https://www.bsdnow.tv/651.
- [BSD Now EP648] Pennington J. BSD Now: 648: Greytrapping for years[EB/OL]. (2026-01-29)[2026-08-15]. https://www.bsdnow.tv/648.
- [BSD Now EP360] Pennington J. BSD Now: 360: Full circle[EB/OL]. (2020-07-23)[2026-08-15]. https://www.bsdnow.tv/360.
- [BSD Now EP640] Pennington J. BSD Now: 640: Cleaning up Hammer[EB/OL]. (2025-12-04)[2026-08-15]. https://www.bsdnow.tv/640.
- [BSD Now EP213] Pennington J. BSD Now: 213: The French CONnection[EB/OL]. (2017-09-27)[2026-08-15]. https://www.bsdnow.tv/213.
- [BSD Now EP143] Pennington J. BSD Now: 143: One small step for DRM, one giant leap for BSD[EB/OL]. (2016-05-25)[2026-08-15]. https://www.bsdnow.tv/143.
- [BSD Now EP46] Pennington J. BSD Now: 46: Network Iodometry[EB/OL]. (2014-07-16)[2026-08-15]. https://www.bsdnow.tv/46.
- [BSD Now EP24] Pennington J. BSD Now: 24: The Cluster & The Cloud[EB/OL]. (2014-02-12)[2026-08-15]. https://www.bsdnow.tv/24.
- [BSD Now EP18] Pennington J. BSD Now: 18: Eclipsing Binaries[EB/OL]. (2014-01-01)[2026-08-15]. https://www.bsdnow.tv/18.
- [BSD Now EP11] Pennington J. BSD Now: 11: The Gateway Drug[EB/OL]. (2013-11-13)[2026-08-15]. https://www.bsdnow.tv/11.

<!-- /PODCAST_REVIEW -->
