---
chapter: 第 103 章
id: CH103
volume: 第05卷-freebsd的工程化奠基
---

# 第103章 pf防火墙

## 要点

- PF（Packet Filter）由 Daniel Hartmeier（丹尼尔·哈特迈尔） 与 OpenBSD 团队于 2001 年开发，替代因许可证争议被移除的 IPFilter；PF 采用规则集优化（skip steps）与状态保持（stateful inspection）设计，首版随 OpenBSD 3.0（2001.12）发布
- FreeBSD 于 2004 年（5.3 RELEASE，2004.11.4，release/5.3.0 tagger_date = 2004-11-04T19:12:42Z，tagger = Ken Smith）首次将 PF 作为可选防火墙引入，由 Pyun YongHyeon、Max Laier 等完成移植；PF 导入 commit 为 2004-06-16T23:03:14Z（commit_hash = 32b30983561ed562aa495d8e124488ab94b332aa，committer = Max Laier，message_subject = “Import pf from OpenBSD 3.5 (OPENBSD_3_5_BASE)”），早于 5.3-RELEASE 约 4.5 个月，属 5-CURRENT 开发周期；移植包括内核钩子、用户态 pfctl 工具与 ALTQ 流量整形框架
- PF 从 OpenBSD 流入 FreeBSD/NetBSD/DragonFly BSD，体现 BSD 生态的代码共享性；但各 BSD 对 PF 的维护投入不同，FreeBSD 增加了 SMP 扩展与 VNET 支持，导致功能分化
- 移植史料疑点：(1) 移植起始时间（2003 年 编程之夏 项目 vs 2004 年 5.3 集成）；(2) 主要移植者的归属；(3) OpenBSD 团队是否参与 FreeBSD 移植
- Linux iptables（1998，Rusty Russell 设计）采用规则链 + 目标设计，是 Linux 2.4+ 主流防火墙；nftables（2014，Patrick McHardy 主导）采用虚拟机字节码设计，替代 iptables；二者是 Linux 主流防火墙路线

## 史观

- 总纲第 5 条——没有必然性，只有偶然性，IPFilter 许可证争议催生 PF 这一全新防火墙
  - 辨析：PF 是否完全由 Hartmeier 一人开发，需查 commit log 确认其他 OpenBSD 开发者的贡献；0 信任原则适用说明：L2.3.1.pf 查询在中观模式挖掘报告中缺失，须直接查询 netbsd.duckdb 验证 PF 引入周期；L2.4.1.Import from 查询使用 "Im
- 专题语（不设总纲条号）——BSD 与 UNIX 谱系的连续性，PF 跨 BSD 项目流动体现谱系共享
  - 辨析：经 bsd_commits.duckdb commits 表验证，PF 导入 commit 为 2004-06-16T23:03:14Z（早于 5.3-RELEASE 约 4.5 个月，属 5-CURRENT 开发周期）；经 bsd_commits.duckdb tags 表验证，5.3-RELEASE 的
- 专题语（不设总纲条号）——简洁与复杂的辩证，iptables 重简洁、nftables 重灵活
  - 辨析：iptables/nftables 与 PF 优劣，需查基准测试
  - 文献：iptables 文档；nftables 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

> 本章各节要点与史观详见 103.2-103.10 对应节文件；行 27-104 系重构前第 102 章残节碎片（重复截断、不可用），已按核查报告删除。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP651、BSD Now EP648、BSD Now EP360、BSD Now EP640、BSD Now EP213、BSD Now EP144、BSD Now EP47、BSD Now EP46、BSD Now EP24、BSD Now EP18、BSD Now EP11、BSDTalk EP234（共 12 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

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
- EuroBSDCon 2017 在巴黎举行，主持人参会期间组织开发者以七分钟短讲介绍各自正在推进或寻求反馈的工作，这一 work in progress 形式与 AsiaBSDCon 类似。（BSD Now EP213，[358.7-412.6]，L1）[订正：原 [376.86-393.88]，2026-09-30 SenseAudio 重转核对]
- 主持人介绍周三下午在巴黎举行的 FreeBSD 基金会董事会会议：多数董事会成员与会，讨论未来会议、资金与新增董事等事项；主持人还介绍 EuroBSDCon 次年将移师罗马尼亚布加勒斯特。（BSD Now EP213，[102.3-1324.7]，L1）[订正：原 FreeBSD 基金会董事会在巴黎举行，与会成员讨论 FreeBSD 10.4 测试与发布稳定、注册截止等问题。（BSD Now EP213，[757.00-1311.38]，L1），2026-09-30 SenseAudio 重转核对]
- PF 缺陷故事：Christophe 提交的博客还原了一个 vnet jail 中 PF 与宿主机 PF 实例相互干扰导致 panic 的问题，修复要点是把 purge 状态的索引变量改为 per-vnet 变量，避免多 PF 实例共享状态。（BSD Now EP213，[1331.6-1922.1]，L2）[订正：原 [1335.70-1904.14]，2026-09-30 SenseAudio 重转核对]
- Provost 论证 FreeBSD PF 的 IPv6 分片处理缺陷：PF 重组分片并做出过滤决策后，IPv4 下可交回协议栈重新分片，而 IPv6 为保住路径 MTU 发现必须把分片集合原样送出，netpfil 接口却只支持一包进一包出；PF 目前自行调用 ip6_output 或 ip6_forward，既构成层级违例又存在输出/转发判断错误，特定情形下导致 panic 或丢包；OpenBSD 由协议栈告知 PF 数据包方向的做法可资借鉴，计划中的改造是让 netpfil 支持一包进一堆出，并预期 IPFW 处理 IPv6 分片时同样受益。（BSD Now EP144，[1579.66-1853.0]，L1）[订正：原 [1579.66-1794.88]，2026-09-30 SenseAudio 重转核对]
- Theo de Raadt 提交使 OpenBSD 的 W^X 违例默认不再允许：违例时内核生成日志，mprotect 与 mmap 返回 ENOTSUP，可经 sysctl 改为 SIGABRT 以便调试与取核转储；同时引入 wxallowed 挂载选项按文件系统豁免，commit 原文断言上游开发者终将理解 W^X 违例是极高风险的编程风格并终被彻底禁绝，此前建议在 /usr/local 文件系统使用该选项；主持人评价这使用户得以审计 ports 与自装程序并向上游施压推动修复。（BSD Now EP144，[972.4-1141.3]，L2）[订正：原 [975.68-1114.66]，2026-09-30 SenseAudio 重转核对]
- Theo de Raadt 的 Pledge 演讲经主持人转述：pledge 在系统调用层约束进程能力，OpenBSD 的 NTP 守护进程已在内部使用；演讲披露迄今约 10% 被 pledge 的程序被发现试图执行安全范围之外的动作；未来方向包括回头检视 2003 年前后引入的 OpenSSH 特权分离，以及向其他操作系统输出 pledge 类机制的意愿。（BSD Now EP144，[114.6-273.9]，L2）[订正：原 [130.44-250.50]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 11.0 发布前夜的两项工程经主持人详述：bhyve 在项目分支 projects/bhyve-graphics 获得 UEFI GOP 支持，用户态虚拟显卡把画面送进内建 VNC 服务器，辅以 XHCI（USB 3 仿真）与平板定位实现精准鼠标、PS2 键鼠兜底、可选等待连接后再启动，并已在 Windows 7/8/8.1/10、Server 2012/2016、Ubuntu 15.10、FreeBSD 10.3/11 上验证，grub-bhyve 被定性为权宜之计、单命令 EFI 启动才是长期目标；zfsd 则补齐内核之外的 ZFS 故障管理，监听 devctl 事件自动激活热备，按 zfs 标签与物理路径处置盘位插拔，60 秒内 50 次 IO 或校验和错误即标记故障并换盘，管理员仅经池属性 autoreplace 间接控制，默认未启用。（BSD Now EP144，[240.1-1002.4]，L2）[订正：原 [243.24-975.32]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 图形栈跟进：Linux 4.6 DRM 更新需要用户测试，bsddesktop.com/images 提供 USB 启动测试镜像，非安装器、不改动既有系统；开发者 Matt Macy 经 IRC 转达 AMD/ATI 支持将至，且此项工作主要目标本是 AMD 而非 Intel，Intel 只是副产品；同期 head 的 C++ 变更致 VLC 等断裂，使 11 中 KDE、GNOME 3、XFCE、MATE 的桌面包暂缺——约 300 个包失败、600 个被阻断，占 26000 个包不足 2%，却几乎覆盖桌面所需，Warren Block 的 notebook-stats 脚本用于收集硬件细节以定位问题配置；主持人计划携镜像赴 BSDCan 分发。（BSD Now EP144，[2928.0-3204.4]，L2）[订正：原 [2932.90-3198.18]，2026-09-30 SenseAudio 重转核对]
- 2014 年 7 月 FreeBSD 社区就 PF 防火墙展开罕见规模的大讨论：邮件列表普遍认同与 OpenBSD PF 重新同步是好事，却无人愿意承担整体维护；曾尝试导入新版的 Baptiste Daroussin 因破坏 PF 而回退，表态只愿移植与自身用法相关的个别特性，共识与动手之间出现明显断层。（BSD Now EP47，[426.5-544.6]，L2）[订正：原 [478.06-502.04]，2026-09-30 SenseAudio 重转核对]
- 安全官访谈勾勒出 FreeBSD 安全治理的全貌：章程使安全官名义上对系统中每一个安全漏洞负责，日常是安全公告的撰写与发布，实质更涵盖流程改进、漏洞缓解技术与安全特性优先级决策，2013 年 /dev/random 重构之争即由其主持裁决，其任内还推动以标准 CPE 元数据嵌入包体系以弥补 VuXML 字符串匹配易漏报的结构缺陷。（BSD Now EP47，[1810.0-2175.8]，L1）[订正：原 [1807.74-1938.24]，2026-09-30 SenseAudio 重转核对]
- Bryan Drewery（转写误作 Brian Drury）自述入圈路径：2003 年前后经 IRC 结识经营 shell 服务的 FreeBSD 4.11 用户而入坑，2012 年因不满包安装状态找到 pkgng 项目并协同 Baptiste Daroussin，从提交补丁到获 ports 提交权，再到以包框架贡献者身份进入 Port Manager 团队并新获 source 提交权——包体系维护者由工具建设者自然生长而成。（BSD Now EP46，[1963.44-2018.28]，L1）
- FreeBSD 官方包构建集群的一手运维细节：四台号称 beefy 的机器各配 32 核与 96—100GB 内存，每周二 UTC 凌晨一点对 ports 树拍快照并按各发布版与 head 构建 x86 包集，全量需三至五天；另有八套每日测试系统覆盖非 root 构建、打包测试与 QA，quarterly 季度分支自 head 切出并回灌安全修复，属仍在试验中的稳定化机制。（BSD Now EP46，[2439.92-2628.96]，L1）
- iodine DNS 隧道演示的实操要点构成其技术史价值：服务端以特权分离用户与 chroot 运行但密码将以明文见于进程列表，且 iodined 须独占一个 IP 承担 DNS 应答而无法与既有域名服务共存；客户端探测可用查询类型并按 DNS 包尺寸协商 MTU，建隧道后经压缩 SSH 登录验证，并可与 stunnel、SSH 链式跳板教程组合成受限网络下的成套突围方案。（BSD Now EP46，[5978.10-6327.42]，L1）
- NYCBSDCon 2014 以“BSD in production”为主题，Dru Lavigne 开场，议题包括 FreeNAS/PC-BSD 的 ZFS 管理、BSD 路由器及以 FreeBSD 与 ZFS 运行 PostgreSQL。（BSD Now EP24，[73.68-95.60]，L2）
- Luke Marsden 自述 15 岁起经营主机公司，在牛津学习理论计算机科学后创立 HybridCluster，以解决主机业务中反复出现的宕机与扩展问题。（BSD Now EP24，[1074.80-1171.02]，L1）
- HybridCluster 以 jail 或容器为应用单元，基于 ZFS 快照与 send/receive 实现异步复制、故障转移与亚秒级活迁移，作为 SAN 与虚拟机方案的替代。（BSD Now EP24，[1282.16-1500.20]，L1） [订正：原 [1282.16-1548.36]，2026-09-30 SenseAudio 重转核对]
- HybridCluster 部署的操作系统为略经修改的 FreeBSD 9.2 stable，工程师 Andriy Gapon 为 FreeBSD 开发者并将修复回馈社区；产品以每服务器每月 160 美元许可销售。（BSD Now EP24，[1546.30-1606.30]，L1） [订正：原 [1557.08-1612.28]，2026-09-30 SenseAudio 重转核对]
- 新闻讨论 FreeBSD 10 作为防火墙：PF 经 SMP 优化后性能更强但规则语法较旧，简单规则场景下 IPFW 因解析路径更短而更快。（BSD Now EP24，[480.68-577.34]，L2）
- 主持人转述 Justin Sherrill 的观点：PF 已被 FreeBSD、NetBSD、macOS 等吸收，但各实现基于不同时期的 OpenBSD 版本且无版本号，导致规则语法与功能分化。（BSD Now EP18，[370.8-455.4]，L2）[订正：原 [346.52-362.32]，2026-09-29 SenseAudio 重转核对]
- 节目讨论以 OpenSSH portable 或 OpenZFS 共同核心为参照，为 PF 建立可移植层（被称为 PPL 或 OpenPF 构想）；Henning Brauer 表示愿意协助，但该项目当时尚未落地。（BSD Now EP18，[456.2-546.1]，L2）[订正：原 [454.58-557.28]，2026-09-29 SenseAudio 重转核对]
- Baptiste Daroussin 自述因厌倦反复源码编译而设计 PackageNG，后在 BSDCan 演讲并取得 ports commit bit，成为 portmgr 成员。（BSD Now EP18，[1007.0-1029.7]，L1）[订正：原 [993.58-1029.66]，2026-09-29 SenseAudio 重转核对]
- PackageNG 方向为将 poudriere 由面向最终用户的安装工具转为基础设施构建工具，并引入 staging、autoplist、子包、flavors/providers 及基于 fingerprint 的仓库签名，以解决冲突、改名与多版本包问题。（BSD Now EP18，[1083.9-1667.0]，L1）[订正：原 [1049.62-1253.12]，2026-09-29 SenseAudio 重转核对]
- OpenBSD 长期缺乏官方跨版本升级工具，第三方 ksh 脚本 OpenBSD Binary Upgrade 可完成 5.3 到 5.4 的二进制升级与大部分旧文件清理，但既不清理全部旧文件、也不提供签名更新。（BSD Now EP18，[2195.5-2283.7]，L2）[订正：原 [2198.60-2266.36] 仅校验 SHA256 而不提供签名，2026-09-29 SenseAudio 重转核对]
- Justin Sherrill 自述约 2000 年首次接触 BSD，后因 Matt Dillon 从 FreeBSD 分支 DragonFly 而加入，长期负责 DragonFly Digest、发布管理与 Summer of Code 组织工作。（BSD Now EP11，[681.7-851.1]，L1）
- 他说明 DragonFly 分叉源于 Matt Dillon 与 FreeBSD 在对称多处理路线上的分歧，Dillon 倾向轻量、简单的并发方式，最终使 DragonFly 网络栈几乎去除 BSD 世界常见的大型锁。（BSD Now EP11，[903.6-1005.7]，L1）
- DragonFly BSD 3.6 将 dports（基于 Poudriere 构建的 DragonFly 版 ports）设为默认，并包含 Intel、AMD 图形支持的移植。（BSD Now EP11，[1486.8-1682.5]，L3）[订正：原 [4692.8-496.0]，2026-10-01 交叉核验订正][订正：原 并加入 SMP 扩展性改进与——该句在 EP11 [1486.8-1682.5] 区间内无转写支撑（SMP 表述仅见于 916.7 已由相邻条目覆盖），2026-10-01 交叉核验订正]
- 新闻提及 OpenSSH 6.5 将 Curve25519 设为默认密钥交换算法，FreeBSD 引导菜单加入内核选择功能，Colin Percival 推出内核 panic 报告工具。（BSD Now EP11，[4762.8-4812.0]，L2）
- Brauer 自述其在柏林 hackathon 收尾的校验和处理重写：新模型假定每条输出路径都具备校验和硬件卸载能力，栈上层不再预计算与就地修补校验和，仅需在数据包上置标记声明需要何种协议校验和，全部计算集中到输出路径末端的单一位置，仅在确知该路径无卸载能力时才回退软件实现。（BSDTalk EP234，[305.23-320.29]，L1）
- 旧实现的缺陷根源在于部分网卡（以 Intel 与 Broadcom 千兆芯片为代表，约占服务器市场九成）要求保留伪头校验和，而另一些网卡做全量卸载，PF 无法判别数据包携带的是部分校验和还是完整校验和，就地更新便可能出错；重写后栈上层彻底不管校验和，桥接路径也被修正；ICMP 错误报文中被引用原始包的校验和因多数被截断而无法验证，选择忽略，并以手工构造异常报文的专用工具对 PF 行为做验证。（BSDTalk EP234，[822.90-1029.94]，L1）
- 新排队子系统分两层：优先级排队极为简单，把 ifnet 结构的单一输出队列头改为八个队列的数组并按序处理，默认优先 CARP 公告与生成树报文以防主备双主故障，且常开不可关闭；带宽整形部分则取代约一万二千行的 AltQ——后者原是 Kenjiro Cho 十余年前的论文研究项目，2003 年 Cho 与 Brauer 将其并入 PF 使 PF 充当分类器，次年加入的 HFSC 因语法难懂而少有人用，用户多用较简单的 CBQ——新版保留可完全表达 CBQ 的 HFSC、重写胶水层并删除可插拔调度器框架，全系统缩至约三千五百行，随 OpenBSD 5.5 提交。（BSDTalk EP234，[374.70-624.38]，L1）
- 关于 PF 的可移植性，Brauer 区分了两类情形：OpenSSH 是用户态、大体以 POSIX 为边界的守护进程集合，故能维持 portable 版本；PF 是内核的内嵌成分，依赖各操作系统的内存管理，可移植难度更高，但 Apple 与 QNX 均已集成 PF，FreeBSD 的移植虽面对不同的内存管理也无需重写一半，各系统挂接网络栈的方式差异有限。（BSDTalk EP234，[1449.18-1525.40]，L1）

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
- Christophe 关于 PF 缺陷修复的博客；EuroBSDCon 2017 会议议程与 FreeBSD 基金会董事会记录。（BSD Now EP213，[1331.6-1922.1]，L2）[订正：原 [1335.70-1904.14]，2026-09-30 SenseAudio 重转核对]
- 一手材料密集：Kristof Provost 在 AsiaBSDCon 的现场访谈自述（入坑经历、补丁被批评被测试再合并的流程、搞崩共同主持人 Alan 路由器的复盘）；Theo de Raadt 的 Pledge 主题演讲视频与幻灯片；Eric McCorkle 谈 EFI 启动重构与 GELI 支持的博客（附 GitHub 代码链接与成段引文）；Sean Chittenden 的 Postgres 多数据中心高可用演讲；Michael W. Lucas 的 Faces of FreeBSD 入行自述；Netgate UFO 板卡的 dmesg 启动日志与 openssl speed 实测数据。　[存疑脚注] 转写专名多处音转失真（Kristof Provost 转作 Christophe、bhyve 转作 beehive、GELI 转作 Jelly、Consul 转作 console、W^X 转作 WXRX、Netgate UFO 转作 NetGate UFW），语义均可由上下文复原；唯 Theo de Raadt 演讲场合转写作“Dot Security 2016”无法与 2016 年已知公开演讲日程对确。（BSD Now EP144，[1277.04-2311.52]，L1）
- 本期可提炼的一手史料包括：斯洛文尼亚 OpenBSD hackathon（2014 年 7 月 8 日至 14 日）的 CVS 提交树（一周逾千次提交）与参与者分工记录、FreeBSD 邮件列表 PF 讨论串原文、BSD Router Project 公布的转发基准原始数据与运行脚本、LibreSSL tech 邮件列表的补丁流，以及安全官 Dag-Erling Smørgrav 对个人入坑与 commit bit 授予经历的亲述。（BSD Now EP47，[59.4-96.3]，L1）[订正：原 [68.2-96.2]，2026-09-30 SenseAudio 重转核对]
- 本期经主持人提及可资查证的一手史料：FreeBSD 9.3-RELEASE 公告与 release notes（iSCSI 可加载、ARC 元数据限额运行时可调、on-if-console 便于 bhyve 直用官方镜像）、pkgng 1.3 RC2 邮件列表通告、LibreSSL 便携版 2.0.x 于 OpenBSD FTP 发布并已入 ports、2014 年 FreeBSD 核心团队九人选举名单（Gavin Atkinson、David Chisnall、Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Gleb Smirnoff、Peter Wemm、Robert Watson）、EuroBSDCon 2014 索菲亚注册页与开发者峰会邀请制说明。（BSD Now EP46，[1052.16-1090.52]，L2）
- 本期史料包括 NYCBSDCon 2014 议程与现场反馈、Luke Marsden 访谈（当事人自述）、HybridCluster 产品说明及 FreeBSD 10 PF/IPFW 讨论。（BSD Now EP24，[65.60-2456.00]，L1） [订正：原 [1059.58-1612.28]，2026-09-30 SenseAudio 重转核对]
- 本期史料包括 Justin Sherrill 博客观点、Henning Brauer 对 PF 可移植层的表态、Baptiste Daroussin 访谈（当事人自述）以及 OpenBSD Binary Upgrade 第三方脚本。（BSD Now EP18，[328.6-2297.2]，L1）[订正：原 [346.52-557.28]，2026-09-29 SenseAudio 重转核对]
- 当事人提及 DragonFly 分叉公告约在访谈时点的十年前发布，并称其并发模型以 token 传递为主，进程在获得内存或系统资源时持有 token、阻塞时即释放。（BSD Now EP11，[985.4-1010.8]，L1）
- 一手史料包括：柏林 hackathon 上的校验和收尾提交；一处仅触及一两行的校验和相关提交，Brauer 与 Alexander Bluhm 曾花一天半才完全理解其含义；OpenBSD 5.5 排队子系统提交；Brauer 在自家公司的稳定树上先行对数百台 Intel 千兆机器启用校验和卸载、以大规模实际部署替代发布前测试的经验。（BSDTalk EP234，[1080.72-1241.82]，L1）
- relayd 的名称史由当事人追溯：Reyk 的最初原型即名为 RelayD，Pierre-Yves Ritschard 另提交了名为 SLBD（服务器负载均衡守护进程）的不同实现，入树时一度定名 hostated（本意 host state d），因拼写歧义与功能扩张——七层处理、取出内核的流量处理、SSL 卸载——不再相称，最终改回语义足够通用的 relayd。（BSDTalk EP234，[1673.28-1769.94]，L1）

**史观**：

- 总纲9 经验优先：总纲9 经验优先：邮件服务器作者以实际运维数据评估地理过滤的收益与代价，而非依赖纸面推断。（BSD Now EP651，[449.80-530.32]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Alan Jude 记录的 ZFS 事故源于接错线缆、换错盘等一线操作，运维纪律而非技术神话决定成败。（BSD Now EP651，[1336.04-1395.14]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：OpenBSD 与 FreeBSD 在虚拟化与兼容层上各自吸收上游技术又保持分化，构成分合循环。（BSD Now EP651，[2852.22-2965.62]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Hansteen 以十八年持续运维累积的灰度陷阱数据，记录的是不被聚光灯照到的反垃圾邮件一线工作。（BSD Now EP648，[257.02-1152.28]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：BSDCan 领导权在代际之间交接、规划委员会持续吸纳新人，体现社区组织的聚合与再分配。（BSD Now EP648，[1382.64-1467.34]，L1）
- 总纲9 经验优先：总纲9 经验优先：Siebenmann 从自身运维规则集与工具链出发评估防火墙迁移，而非依赖抽象性能宣传。（BSD Now EP648，[3368.44-3441.68]，L1）
- 总纲10 动手者创造历史：FreeBSD 决策由“到场者”作出，主持人与提问者强调社区参与决定项目走向。（BSD Now EP360，[481.5-503.3]，L2）[订正：原 [2452.99-2456.55]（错挂片尾音乐段），2026-10-01 交叉核验订正——总纲10 内容真实出处为 481.5-503.3 段（core 团队九人自荐、社区九票多数当选），片尾 2443.1-2547.8 经两次转写均无语音产出判定为收播曲]
- 总纲4 分离聚合是永恒规律：Core 团队成员更替体现治理层的分离与再聚合。（BSD Now EP360，[460.69-614.65]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：OCI 支持由 Samuel Karp、Doug Rabson 等志愿者的多年内核与工具链工作累积而成。（BSD Now EP640，[227.38-305.54]，L2）
- 总纲9 经验优先：总纲9 经验优先：Jim Salter 以亲身经历过的断电、火灾、失窃等故障说明为何 RAID 不等于备份。（BSD Now EP640，[630.76-692.68]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：HAMMER 清理依赖 cron 定时触发的假设在笔记本关机场景下失效，反映旧运维假设随硬件使用方式变化而过时。（BSD Now EP640，[1081.24-1215.64]，L1）
- 总纲10 动手者创造历史：Christophe 通过测试脚本复现 vnet 中的 PF panic 并逐行修复，是动手者以调试实践改进防火墙代码的典型记录。（BSD Now EP213，[1392.6-1907.0]，L2）[订正：原 [1413.72-1904.14]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：本期是动手者创造历史的微观样本：Kristof Provost 的入坑起因只是“因为它跑不起来”，为修一块 Marvell 板卡上的问题从此一直在找 bug，补丁经批评、测试、合并的循环把他卷成 committer；Michael W. Lucas 因深夜 DNS 管理员离职被顶上岗位、为睡安稳觉换掉 Unixware 与 Solaris 转向 BSD；系统的演进正由这类具体修补与无名测试者的反馈累积而成。（BSD Now EP144，[1277.0-1366.4]，L1）[订正：原 [1306.72-1354.34]，2026-09-30 SenseAudio 重转核对]
- 总纲22 知识注定过时：工程知识的过时性在本期反复显形：grub-bhyve 被当事人定性为“一直只是权宜之计”，单命令 EFI 启动才是长期目标；McCorkle 判定自建的 boot1 非 EFI 提供者框架与 EFI 框架既有功能重复、接口别扭且无法向内核传递密钥，重构后 boot1 缩为一个很小的源文件并与 loader 共享全部后端驱动，bcache 成为通向 EFI 驱动模型与热插拔支持的唯一阻碍——每一代被视为完成的方案，都会成为下一代重构的对象。（BSD Now EP144，[2612.8-2747.6]，L2）[订正：原 [2619.86-2734.50]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：PF 讨论与 LibreSSL 的对照揭示同一机制：社区共识不产生代码，唯有动手者启动历史——主持人引 LibreSSL 与 FreeBSD ZFS 安装器皆因一人先动手而带动集体参与，嘉宾更以亲历口吻总结“空白页是最难的起点”（638.58-645.34）；史书应当记录的是接住空白页的人，而非那纸无人执行的共识。（BSD Now EP47，[594.1-643.5]，L2）[订正：原 [609.12-645.34]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：包体系的演进由动手者驱动而非领袖钦定：Google Summer of Code 学生写出新的依赖求解器使 package set -o 大半退役，构建集群从小两台机器被不断塞机器式地扩张并由个人以自写脚本勉力管理，Port Manager lurker 计划以 IRC 频道吸纳 Matt、Steve Wills 等新血——基础设施史的正主是这些具体操持者，正合总纲之动手者创造历史。（BSD Now EP46，[2126.10-2148.62]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Luke Marsden 自建主机公司并发展为 HybridCluster，是动手者以创业实践推动系统应用的代表。（BSD Now EP24，[1074.80-1171.02]，L1）
- 总纲11 商品是形式主义：总纲11 商品是形式主义：HybridCluster 以许可模式售卖基于 jail 与 ZFS 的虚拟 SAN 与容器平台，体现软件商品化的形式。（BSD Now EP24，[1587.16-1612.28]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：通过 ZFS 复制与 jail 迁移，实现计算与存储在集群中的分离与再聚合。（BSD Now EP24，[1282.16-1500.20]，L1） [订正：原 [1282.16-1548.36]，2026-09-30 SenseAudio 重转核对]
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：PF 随各 BSD 分支而分离，又出现以共同核心重新聚合的讨论，呈现分离与聚合的循环。（BSD Now EP18，[383.7-480.3]，L2）[订正：原 [359.44-413.44]，2026-09-29 SenseAudio 重转核对]
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Baptiste Daroussin 因个人反复编译的痛点动手重写包系统，改变 FreeBSD 软件分发方式。（BSD Now EP18，[1007.0-1029.7]，L1）[订正：原 [993.58-1029.66]，2026-09-29 SenseAudio 重转核对]
- 总纲18 时间是一种形式主义：总纲18 时间是一种形式主义：PF 缺乏版本号使各实现难以按时间锚定演进，说明版本命名是形式化的时间标记。（BSD Now EP18，[426.0-437.3]，L2）[订正：原 [425.34-439.46]，2026-09-29 SenseAudio 重转核对]
- 总纲4 分离聚合是永恒规律：DragonFly 的分叉呈现为多处理路线分歧推动的一次分离，而非单一技术演进的必然结果。（BSD Now EP11，[903.6-965.6]，L1）
- 总纲10 动手者创造历史：Justin Sherrill 长期承担文档、发布与组织工作而非核心代码，说明项目维护依赖多元角色的动手者共同支撑。（BSD Now EP11，[774.9-861.7]，L1）
- 总纲10 动手者创造历史：Brauer 反复强调 FreeBSD 升级 PF 的障碍不在技术：语法变更对九成以上配置不过是两分钟的活，真正的问题是“得有人去做”，而项目内部虽有升级意向却无人执行；他公开表态愿为具体动手者义务答疑。技术变迁的推进被归于具体个体的行动意愿，而非项目层面的抽象决议。（BSDTalk EP234，[1324.98-1350.02]，L1）

**辨析**：

- 转录将 Klara Systems 误记为 clari systems，将 Rubenerd 误记为 Ruben Nerd，正文按业界通行名处理。　[考据脚注] 机构与博客名存在语音转写偏差，须以原文链接核验（BSD Now EP651，[782.30-782.70]，L4）[订正：原 误记为 Clara Systems、Rubinerd 或 Ruben Nerd，2026-10-01 SenseAudio 重转核对]
- 转录中 OpenBSD PA-RISC 移植者被记作 Michael Shalif，实为 Michael Shalayeff；因语音转写歧义，人名须以代码仓库与邮件列表核验。　[存疑脚注] 人名拼写存在转写歧义，未以 OpenBSD 代码仓库核验（BSD Now EP651，[2700.56-2735.66]，L4）[订正：原 被记作 Michael Shaliff，2026-10-01 SenseAudio 重转核对]
- 转录将 Peter N. M. Hansteen 误记为 Peter N.M. Hanstein，且陷阱总数 17,8238 的数字断词存疑，须对照原文与数据文件。　[存疑脚注] 人名与统计数字存在语音转写歧义，须以原文与数据文件核验（BSD Now EP648，[997.58-1005.20]，L4）
- DragonFly 的 pf 表限制是静态内核值且未暴露为可调 sysctl，是否需要仿照 FreeBSD 改造仍待确认。　[存疑脚注] DragonFly 侧改造计划待核实（BSD Now EP360，[1360.80-1390.40]，L4）
- 转录将 Doug Rabson 记作 Doug Rapson、将 Dave Cottlehuber 记作 Dave Cossel-Huber，人名拼写存在转写歧义。　[存疑脚注] 贡献者姓名存在语音转写偏差，须以 FreeBSD Foundation 公告核验（BSD Now EP640，[227.38-290.18]，L4）
- ELIZA 作者名在转录中拼作 Weisenbaum 或 Weisenbalm，通行写法为 Joseph Weizenbaum，须以原始论文核验。　[考据脚注] 人名拼写存在转写偏差，以 Communications of the ACM 1966 年原文为准（BSD Now EP640，[1279.84-1342.08]，L4）
- PF 性能之争呈现典型的声明—质疑—实证结构：OpenBSD 的 Henning Brauer 称算法与锁的改进使其 PF 快约四倍，FreeBSD 开发者 Gleb Smirnoff 反驳该说法未经基准支撑且双方均未公布对比数据；BSD Router Project 随后在四核万兆平台公布附原始数据与脚本的可复现转发基准，显示 FreeBSD 10 明显快于受无 SMP 限制的 OpenBSD 5.4。（BSD Now EP47，[845.9-982.4]，L3）[订正：原 [857.82-980.68]，2026-09-30 SenseAudio 重转核对]
- OTP 双因子认证进入 FreeBSD base 的争论焦点不在算法而在政策：由 root 统一管辖的可写密钥库是 HOTP/TOTP 计数与时效失效的技术前提，但放宽用户自管将招致弱化与误操作；Dag-Erling Smørgrav 断言“若在 10.1 放入半吊子方案，将被迫向后兼容五年”（2938.2-2950.76），宁可推至 11 一次做对，体现发布即承诺的工程伦理。（BSD Now EP47，[2930.2-2995.1]，L1）[订正：原 [2931.1-2957.62]，2026-09-30 SenseAudio 重转核对]
- LibreSSL portable 版在 Linux 上暴露的伪随机数复用缺陷（特定 fork 情形可产出相同随机数）显示跨平台移植会击穿原设计假设，而 Linux 内核开发者相应推动与 OpenBSD getentropy 同构的系统调用以规避文件句柄耗尽攻击，构成 OpenSSL 分叉事件反向塑造 Linux 内核接口的互构链条。　[存疑脚注] 该段涉 Linux 侧动议，转写中人名（如 Theodore So、10Uincts）疑为语音转写失真，须回查 2014 年 7 月 OpenBSD tech 邮件列表与内核邮件列表原文方可定名。（BSD Now EP47，[1058.8-1118.2]，L2）[订正：原 [1040.0-1145.72]，2026-09-30 SenseAudio 重转核对]
- 关于 Netflix 存储架构的孤证说法须存疑：主持人称 Netflix 以 discrete wire 将 SATA 磁盘一对一接 LSI HBA 而回避 SAS 扩展器，并自认“我不是百分百确定”（4922.54）；此说既非当事人自述亦无文档佐证，且转写将 HBA 误作 HPA，引用前应以 Netflix 工程实践一手材料核证。　[存疑脚注] 说话人自陈不确定且非当事人，属单一来源推断，Netflix 磁盘直连实践待核（BSD Now EP46，[4918.94-4944.68]，L4）
- PF 双雄之争在节目中仅为转述层材料：OpenBSD 邮件列表风暴中社区主张与其仅 SMP 化 PF 不如做通用 SMP 改造，DragonFly 已多线程化 PF，FreeBSD 侧则有 PF 前途之问与 IPFW 复兴的杂音；“快四倍”“随核数线性”等数字均出自主持人复述，且网卡多队列等底层论断含糊，映射入史前必须回查 2014 年邮件列表原帖。　[存疑脚注] 争论细节与性能数字仅经主持人转述，须以邮件列表一手原文复核（BSD Now EP46，[668.06-893.54]，L2）
- HybridCluster 活迁移亚秒级为其商业宣传口径，需独立验证；NYCBSDCon 议题与演讲细节为主持人转述，需与会议议程核对。　[存疑脚注] 活迁移性能与会议细节以官方发布为准，需交叉验证。（BSD Now EP24，[1494.88-1500.64]，L4）
- 主持人将 DragonFly 的 PF 对应 OpenBSD 4.4、FreeBSD 对应 4.5 等版本关系为口头转述，需与各项目代码核对；OpenPF 项目在 2014 年成立属对未来的期许而非既成事实。　[存疑脚注] 各 BSD 的 PF 版本对应与 OpenPF 立项状态需以源码与邮件列表原始记录复核。（BSD Now EP18，[383.7-558.9]，L4）[订正：原 [386.32-439.46]，2026-09-29 SenseAudio 重转核对]
- Brauer 对其他 BSD 的 PF 状况评价带鲜明立场：称 NetBSD 在“自己的 PF 克隆里重复我们所有的错误”、FreeBSD 停留在 2008/2009 年版本且无人执行升级。此为单一当事人对兄弟项目的负面判断，NetBSD 侧的工程动机与 FreeBSD 邮件列表中的实际计划细节，须以各项目邮件列表与提交记录交叉验证方可采信。　[存疑脚注] 对 NetBSD 与 FreeBSD 的评价为单一当事人立场性陈述，未提供可复核依据（BSDTalk EP234，[1277.48-1324.98]，L4）

**文献**：

- [BSD Now EP651] Pennington J. BSD Now: 651: Spatially aware ZFS[EB/OL]. (2026-02-19)[2026-08-15]. <https://www.bsdnow.tv/651>.
- [BSD Now EP648] Pennington J. BSD Now: 648: Greytrapping for years[EB/OL]. (2026-01-29)[2026-08-15]. <https://www.bsdnow.tv/648>.
- [BSD Now EP360] Pennington J. BSD Now: 360: Full circle[EB/OL]. (2020-07-23)[2026-08-15]. <https://www.bsdnow.tv/360>.
- [BSD Now EP640] Pennington J. BSD Now: 640: Cleaning up Hammer[EB/OL]. (2025-12-04)[2026-08-15]. <https://www.bsdnow.tv/640>.
- [BSD Now EP213] Pennington J. BSD Now: 213: The French CONnection[EB/OL]. (2017-09-27)[2026-08-15]. <https://www.bsdnow.tv/213>.
- [BSD Now EP144] Pennington J. BSD Now: 144: The PF life[EB/OL]. (2016-06-01)[2026-08-15]. <https://www.bsdnow.tv/144>.
- [BSD Now EP47] Pennington J. BSD Now: 47: DES Challenge IV[EB/OL]. (2014-07-23)[2026-08-15]. <https://www.bsdnow.tv/47>.
- [BSD Now EP46] Pennington J. BSD Now: 46: Network Iodometry[EB/OL]. (2014-07-16)[2026-08-15]. <https://www.bsdnow.tv/46>.
- [BSD Now EP24] Pennington J. BSD Now: 24: The Cluster & The Cloud[EB/OL]. (2014-02-12)[2026-08-15]. <https://www.bsdnow.tv/24>.
- [BSD Now EP18] Pennington J. BSD Now: 18: Eclipsing Binaries[EB/OL]. (2014-01-01)[2026-08-15]. <https://www.bsdnow.tv/18>.
- [BSD Now EP11] Pennington J. BSD Now: 11: The Gateway Drug[EB/OL]. (2013-11-13)[2026-08-15]. <https://www.bsdnow.tv/11>.
- [BSDTalk EP234] Backman W. BSDTalk: 234: bsdtalk234 - Henning Brauer at vBSDCon[EB/OL]. (2013-11-11)[2026-08-27]. <https://bsdtalk.blogspot.com/2013/11/bsdtalk234-henning-brauer-at-vbsdcon.html>.

<!-- /PODCAST_REVIEW -->