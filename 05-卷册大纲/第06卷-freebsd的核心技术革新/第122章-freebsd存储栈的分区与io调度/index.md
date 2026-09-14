---
chapter: 第 122 章
id: CH122
volume: 第06卷-freebsd的核心技术革新
---

# 第 122 章 freebsd存储栈的分区与io调度

## 要点

- 2010-2020 年存储栈呈现 “卷管理分层（Linux LVM）vs 统一变换层（FreeBSD GEOM）vs 存储池（Windows Storage Spaces）vs CoW 合一（ZFS/btrfs/HAMMER）” 的多路线格局；FreeBSD 的 GEOM 以模块化、可组合著称，UFS 的 soft updates 提供元数据一致性保障，在非 ZFS 领域保持工程简洁性。同期主流操〔存疑：原文截断，待回源补全〕
- FreeBSD 磁盘命名演进历史：早期 MFM/RLL 磁盘为 wd?（Winchester Disk），SCSI 磁盘为 sd?；FreeBSD 3.x CAM 引入后 SCSI 磁盘改为 da?（Direct Access）；FreeBSD 5.x 时期 ATA 磁盘为 ad?（ATA Direct Access）；〔存疑：原文截断，待回源补全〕
- FreeBSD 网络存储生态除 iSCSI 和 HAST 外，还包括：NFS（Network File System）作为最古老的分布式文件系统协议在 FreeBSD 中有完整的客户端/服务器实现（NFSv2/v3/v4，详见 78.4.4 节）；**ggate(8)**（GEOM Gate）允许用户态程序通过网络导出块设备，是 HAST 和其他用户态 GEOM 模块的基础；**nfsv4(4)**〔存疑：原文截断，待回源补全〕
- Valerie Aurora（当时名 Valerie Henson，ext4 文件系统开发者）于 2009 年 7 月 1 日在 LWN.net 发表文章 “Soft updates, hard problems”（lwn.net/Articles/339337/），从 Linux 文件系统开发者视角对 Soft Updates 提出系统性批评，核心论点包括：Soft Updates 实现极端复杂〔存疑：原文截断，待回源补全〕
- **统计分析印证**——`freebsd.duckdb` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；ARIMA(5,0,5) 模型拟合 AIC = 107.39（统计结论 C-29）；非〔存疑：原文截断，待回源补全〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3706] 卷“第06卷-freebsd的核心技术革新”第 122 章，匹配置信度 folder，原因：folder 第120章

## 史观

- 章级史观：从项目史观总纲第 4 条（分离聚合是永恒规律）与第 10 条（动手者创造历史）审视 FreeBSD 存储栈——GEOM 模块化分层、CAM 统一设备层与 UFS soft updates 路线同 ZFS 存储池路线并存互补，呈现存储技术形态的分合流转；GEOM、CAM、GELI、SUJ 各由具体动手者在具体场景中写成，存储栈历史由动手者的持续劳动承载，而非路线图式顶层设计；日志文件系统的产业集体转向与许可证约束则体现利益分配结构对技术命运的支配（总纲第 13 条）。细目详见子节文件史观/辨析字段。

## 辨析

- 不应将 “非 ZFS” 视为 FreeBSD 存储的弱点——GEOM+UFS 在简洁性、可审计性与嵌入式场景仍有价值；ZFS 与 GEOM 在 FreeBSD 中互补共存。
- “FreeBSD 设备名混乱” 是一个常见批评——与 Linux sda/sdb 看似稳定的命名对比，FreeBSD 设备名确实随着架构整合变化过多次；但 Linux 从 hd?（IDE）到 sd?（libata 统一）也经历过类似变化，而且 Linux 的 sd? 命名同样依赖探测顺序，实际生产中也使用 UUID/LVM 标签引用设备而非 sd? 名称；两者只是走了不同的演进路径，最终都收敛到〔存疑：原文截断，待回源补全〕
- FreeBSD 基础系统不包含 Ceph、Gluster 等分布式存储，这些都通过 ports/pkg 提供；这与 Linux 发行版将客户端/服务器全部打包入默认安装不同，体现了 FreeBSD “基础系统最小化、附加软件通过 ports” 的设计哲学；**ggate(8)** 是一个常被忽视但技术上很优雅的设计——它允许用户态进程实现 GEOM provider，这使得 HAST 等网络块设备〔存疑：原文截断，待回源补全〕
- 需要准确引用 Aurora 的原话："soft updates are, simply put, too hard to understand, implement, and maintain to be part of the mainstream of file system development"——这句话有具体语境：Aurora 讨论的是为什么 Soft Updates 没有成为文件系统〔存疑：原文截断，待回源补全〕
- **统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但存储栈实际演进须结合具体子系统（GEOM、CAM、GELI、UFS2）的版本化分析；(2) 非 ZFS 存储栈贡献率未量化：commit 量统计不区分存储栈相关 commit 与其他子系统 commit，非 ZFS〔存疑：原文截断，待回源补全〕

## 文献

- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］

## 采访录（详见 [采访录.md](采访录.md)）

## 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）

---

**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=15）

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. **ada(4)**, **da(4)**, **nda(4)**, **glabel(8)** Manual Pages; Lucas, M. W. (2018). *FreeBSD Mastery: Storage Essentials*.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. **ggate(4)**, **ggated(8)** Manual Pages; FreeBSD Project. *FreeBSD Handbook - Network Filesystems*. docs.freebsd.org. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Aurora, V. (2009-07-01). *Soft updates, hard problems*. LWN.net, lwn.net/Articles/339337/; Seltzer, M. I. et al. (2000). *Journaling Versus Soft Updates: Asynchronous Meta-data Protection in File Systems*. USENIX ATC '00; McKusick, M. K., & Roberson, J. (2010). *Journaled Soft-updates*. mckusick.com/softdep/suj.pdf. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/02-FreeBSD/db/duckdb/freebsd.duckdb**; LibreBSD Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5; LibreBSD Project. 时间序列分析.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/时间序列分析.md** Task 14; LibreBSD Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第五卷第 56 章映射。［A］### 史观映射> GEOM 的模块化架构是 phk 一个人对着存储层发呆时想出来的东西——偶然而非必然，一个人的洞察决定了 FreeBSD 存储栈此后二十年的骨骼。CAM 同样是 Gibbs 一个人的手笔，GELI 是 Dawidek 的作品，SUJ 是 Roberson 的补丁。动手者创造历史，不是群体的决议而是具体的人在具体的夜晚写下的代码。但 soft updates 的命运提醒着：一个工程师的执念能支撑一个文件系统四十年——从 McKusick 1983 年的研究生时期到 2012 年 Roberson 的 SUJ 补丁——却无法逆转整个产业的选择。当 Aurora 说 soft updates “过于难以理解、实现和维护”，当 Solaris、ext3/ext4、XFS、NTFS 集体转向日志，当 NetBSD 和 OpenBSD 先后移除 Soft Updates 支持，McKusick 的执念从工程遗产变成了一个时代拒绝放手的美学姿态。FFS 从 1983 年 8KB 块加柱面组开始，一路演进到 UFS2 的 64 位块指针加 SUJ 日志，这不是 “向前兼容” 的保守，而是一个工程师对自己创造物的责任——他没有像 Sun 那样放弃 UFS 转投 ZFS，像 Linux 那样在 ext2/ext3/ext4/Btrfs/XFS 之间反复试错，而是在自己创造的基础上修修补补了四十年。这是 BSD 方式的优点也是缺点：你信任一个聪明人四十年前写的代码能修到今天，你也要承担这份信任带来的历史负担。

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd.duckdb（freebsd-src）；FreeBSD 贡献者多样性研究（如有）〔存疑：原 doubt-resolved-649 消解未完成，此文献待考据验证〕

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2008-2018 年间：455,206 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP361、BSD Now EP109、BSDTalk EP61（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Firecracker 由 AWS 于 2018 年开源，是依赖 KVM 的微虚拟机监控器；作者以 NetBSD 最小内核配置并绕过引导装载器构建“函数式微虚拟机”。（BSD Now EP361，[749.58-1016.66]，L2）
- Warner Losh 的 2.11BSD 复原工程公开，目标是以可复现方式重建 2.11BSD 发行磁带，并生成含全部 patch 点的 Git 仓库。（BSD Now EP361，[442.48-732.66]，L2）
- Warner Losh 的磁盘分区史文章梳理 Unix 第一至第七版从静态分区到多分区设备的演进，指出分区表曾编译进驱动而非写盘。（BSD Now EP361，[1266.82-1931.02]，L2）
- OpenBSD 发布首个 PowerPC64 快照，在 Raptor Blackbird 与 Talos II 上开发，并计划支持 Power8 系统。（BSD Now EP361，[1075.56-1141.02]，L2）
- 内核模块自动加载的技术路线：Losh 观察到几乎所有设备驱动都在其表中携带即插即用信息（厂商 ID 等字段），先由同事 Hans Petter Selasky 以独立 ELF 节存表并生成 devfs 脚本作为原型，其方案则改为把即插即用信息与既有模块依赖信息一并以标准化形式编码进 KLD 文件，使引导器、内核与用户态工具均可读取，配合小型匹配脚本语言在总线无匹配事件时将设备与驱动配对，并以实验代码动态生成 devd.conf；最终目标是从 generic 内核大量移除驱动（树中已有名为 Minimal 的内核模块作为工作目标），时间表指向 FreeBSD 11 分支，并预期对嵌入式环境尤为有用。　[存疑脚注] 同事名转写为 Hans Peter，据 USB 栈开发背景推断应为 Hans Petter Selasky。（BSD Now EP109，[488.14-734.96]，L1）
- one-wire 温度传感器项目显示开发者以手边器物解决问题的取向：其稻草 Bale 高效住宅依靠夜间引入冷空气并日间缓释蓄冷，须以数据检验各房间冷暖与通风手段的实效，遂购入 Dallas Semiconductor 设计的单总线温度传感器——既有 eBay 整件，亦有以约十分之一价格购自中国厂商的散芯片——并复用住宅既有 RJ11 电话线布线组建 one-wire 网络，代码自行完成总线设备枚举、驱动匹配与周期测温，经 sysctl 发布数据供报表或控制环使用，并在 BSDCan 展出引发兴趣。（BSD Now EP109，[2081.48-2186.52]，L1）
- lighttpd 定位为极快、极轻量的 Web 服务器，目标是在低资源占用下维持大量并行连接，面向大量短连接的 Web 2.0 应用；与 Apache（在不使用事件 MPM 时每连接占一进程或线程）不同，lighttpd 为完全事件驱动的单进程单线程架构，无线程也无 fork，基于非阻塞 I/O——等待中的连接只是进程内的一个文件描述符加少量内存；仅受单进程文件描述符数限制且可调，可同时维持一万至两万连接；Keep-Alive 场景下等待连接近乎零成本，这对 AJAX 类低延迟小请求尤为关键。（BSDTalk EP61，[179.02-344.98]，L1）
- 项目起源：最初是 Boa、Mathopd、thttpd、Zeus 一类擅长静态内容的小型 Web 服务器（当年常被用作 Apache 的静态卸载前端），但自始即带 FastCGI 与 PHP 支持、sendfile 等系统级优化和 kqueue 等事件接口，迅速长成全功能服务器；作者自述直接动因是读到 Dan Kegel 论 C10K 问题（单机万级并行连接）的论文，想以此做概念验证，结果一做即快。（BSDTalk EP61，[88.68-146.44]，L1）
- 事件接口分层决定扩展性：select 与 poll 在所有平台可用（macOS 的 poll 为 select 模拟）但先天受限——select 默认上限 1024 连接、poll 每次返回全部描述符须线性扫描，连接越多系统调用开销越大；kqueue（BSD）、epoll（Linux）、dev-poll（Solaris）只返回发生变更的描述符，使服务器可按事件量而非连接量扩展，接近线性；lighttpd 维护多个事件处理器以适配各平台。（BSDTalk EP61，[539.84-733.94]，L1）
- 安全设计上，lighttpd 从不使用 C 字符串库函数，一切字符串操作先行长度检查、先确认内存再写入，以自有字符串函数集消除缓冲区溢出这一 C 语言服务器的主要攻击面；长度可知同时带来速度（便于追加与复用）；开发中以 Valgrind 与 KCacheGrind 检查性能与内存；重大漏洞约半年前与一年半前各一次，均与 Windows、macOS 默认大小写不敏感的文件系统有关——改变大小写即可绕过安全模式检查，Windows 从非其推荐的生产环境，macOS 则因 Web 服务器部署更多而受影响更实；对外提供 mod_secdownload 限时哈希 URL（10-30 秒有效，防深链盗链）与 X-Sendfile 式头部卸载：后端完成 LDAP、数据库、Kerberos 或 NTLM 等认证后交由服务器以 sendfile 零拷贝发送，兼顾认证安全与传输效率。（BSDTalk EP61，[1237.72-1657.12]，L1）
- 1.5 版本重写核心组件：Rails 社区改用 Mongrel（Ruby 小型 HTTP 服务器）以 HTTP 与前置服务器对话，暴露了现役 lighttpd HTTP 代理模块的最大短板——不处理故障转移，后端宕机时连接直接报错、由客户端重试其他后端；新版 mod_proxy_core 整合 FastCGI、SCGI、HTTP 协议，向后端提供 keep-alive 与 HTTP/1.1，内置轮询与哈希两种负载均衡、故障转移，并向后端提供 sendfile 支持；哈希均衡按 URL 分区，使同一页面的请求恒达同一后端，从而大幅提升后端缓存利用率。（BSDTalk EP61，[733.94-941.52]，L1）

**史料**：

- “Fakecracker：NetBSD as function-based micro-VM”教程，含最小内核配置与 Sailor 工具说明。（BSD Now EP361，[749.58-1016.66]，L2）
- Warner Losh 的 2.11BSD 复原项目页面与早期 Unix 磁盘分区史博客。（BSD Now EP361，[442.48-732.66]，L2）
- 当事人自述其 BSD 履历的起点：二十世纪八十年代大学时期在约 3 MB 内存、40 名用户共用的 VAX 11/750 上为课业编写编译器与链接器，构成其首次接触 BSD 的经验；此后经由 Jordan Hubbard 之请，用一个周末将同时实现 OpenLook 与 Motif 两套交互模型的 GUI 工具包 Object Builder 移植至 FreeBSD 1.0 早期——其时 sysinstall 尚未编写，Hubbard 直接寄来一块克隆硬盘并说“祝你好运，你只能靠自己”（397.66-402.12）——加之以 FreeBSD 可经 SLIP 拨号完成工作而彼时的 Linux 频繁崩溃，遂长期投身 FreeBSD，先后担任 PCCard 与 CardBus 维护者、PCI 子系统贡献者并编写 SD 卡栈。（BSD Now EP109，[277.60-332.12]，L1）
- 当事人自述 Netflix 的生产架构：作为视频点播服务，其全部视频经由 FreeBSD 服务器分发给机顶盒，其职务即优化这一 FreeBSD 机群；因同期 SSD 在读写并发时以 trim 使旧数据失效、触发日志结构底层的垃圾回收而侵占带宽，遂编写以读取优先的 I/O 调度器，将写入限制在每秒约 20 至 25 MB 以内即可消除病态效应，实现边加载内容边流化视频；框架为可插拔设计，支持对读写带宽与 IOPS 的静态限制，并新加入以读取延迟阈值（约 4 毫秒）动态约束写入的机制，代码置于 Perforce 分支 projects.io.sked。（BSD Now EP109，[1073.10-1186.44]，L1）
- 该期提供 2006 年 lighttpd 大规模采用的当事人证词：YouTube 的 Flash 影片文件经 lighttpd 服务器发送（作者与其有读取路径优化的接触，瓶颈完全在磁盘寻道），Wikipedia 的全部图片经 Wikimedia 的 lighttpd 缩放后发送；Netcraft 月度统计中 Apache 约占七成，lighttpd 最近统计约九万套安装、多为此前受性能困扰而寻求扩展的站点；许多部署者从不联系作者，仅靠陌生邮件告知其服务器身份。（BSDTalk EP61，[1028.1-1230.56]，L1）

**史观**：

- 总纲10 动手者创造历史：Firecracker 微虚拟机与 2.11BSD 复原均由个体以工程实践填补生态空白。（BSD Now EP361，[749.58-1016.66]，L2）
- 总纲22 知识注定过时：早期 Unix 的分区表硬编码与设备号约定随存储工业演进而被淘汰。（BSD Now EP361，[1885.08-1931.02]，L2）
- 总纲4 分离聚合是永恒规律：镜像构建工具的碎片化与再聚合是基础设施层的分离聚合循环：NanoBSD 出自 Poul-Henning Kamp 之手后交由 Losh 维护，而 crochet、发行工程镜像、root-on-ZFS 方案各自将树莓派、BeagleBoard、uBoot 端口等板级知识硬编码于自身，致其无法复用且随硬件演进而失效；Losh 的更新策略并非就地修补 NanoBSD，而是先抽取通用工具层——为各 uBoot 端口提供生成镜像的脚本、以包装器统一 gpart 操作、沉淀入基系统——再令 NanoBSD 与其他方案复用，Netflix 亦以 NanoBSD 双分区镜像与自动回滚向数十万台设备每六周滚动固件；分散的工具形态并不构成线性进步，聚合出的公共层才是新一轮构造的起点。（BSD Now EP109，[2414.12-2653.10]，L1）
- 总纲10 动手者创造历史：构建 FreeBSD 设备的知识大量以部落知识形态存在于动手者之间——Losh 称其足以支撑一整天的教程——既未进入手册亦未进入脚本与自动化，且文档不应止于工具用法，还应覆盖可预期的行为与各工具间的取舍；这一自述从当事人视角印证了动手者创造历史：技术史的实存层是这些未被书写的手工诀窍，将其转化为脚本与文档即是对历史的打捞，而非可有可无的锦上添花。（BSD Now EP109，[2764.50-2806.62]，L1）
- 总纲13 法律与道德是利益分配：许可证在该案例中表现为利益分配的形式装置：作者此前的 GPL 项目（Webalizer 类日志分析器）限制其商业化路径，改用 BSD 则同时向贡献者（免版权转让）与使用者（可自由部署建业）开放收益空间，他自称这是“懒人的决定”——许可证的选择即利益结构的选定。（BSDTalk EP61，[1689.12-1788.84]，L1）

**辨析**：

- NetBSD 微虚拟机引导需 multiboot 内核选项，目前仅 i386 支持、AMD64 尚缺，作者假设其为近期限制。　[存疑脚注] AMD64 multiboot 支持状态待核实（BSD Now EP361，[863.18-887.58]，L4）
- 主持人在访谈中提出的生态缺口：PC-BSD 使用 GRUB 引导，而 GRUB 无法自动加载模块依赖，只能在 grub.cfg 中预先逐一列全，且彼时缺乏可直接列出某模块依赖树的用户态工具——KLDXRef 虽可能有读取 linker.hints 的模式但状态不明；这一问答从使用者视角映照出自动加载工程尚未覆盖引导链的现实。（BSD Now EP109，[928.86-948.60]，L2）
- GEOM 在内存耗尽时的回退机制构成一个由改进放大旧缺陷的案例：既有实现以分配失败计数触发退避，将系统长期压制在每秒 10 次 IOPS；Alexander Motin 的 direct dispatch 改进使并发下发的 I/O 从个位数跃升至数千，失败分配随之放大，病态退避更易触发；Losh 的权宜修复是将病态行为上限抬至每秒 1000 次 IOPS 并改为以失败是否持续为节流条件，而根本方案是预分配 I/O 事务全栈所需内存（编译期静态数组或受限的 UMA 储备池），否则当换出页所需的内存本身无法分配时理论上可构成经典死锁——其 Netflix 服务器有 256 GB 内存故罕见触发。（BSD Now EP109，[1739.60-1993.68]，L1）
- 转写存在多处专名讹误：Mathopd 误作 Maffod、Mongrel 误作 MongoRail、Cygwin 误作 CycloN、mod_proxy_core 误作 ModFox core、Valgrind 误作 WellGriant、Kerberos 疑误作 KABROS，lighttpd 在转写中混作 Lighty、LIDI、Lys 等；作者将按 URL 哈希分配请求的首倡 RFC 归于微软，引用此说法时应核对缓存阵列路由协议一类原始文献。　[存疑脚注] 上述专名转写均存疑，以录音与 lighttpd 官方文档复核为准。（BSDTalk EP61，[1866.44-2113.54]，L5）

**文献**：

- [BSD Now EP361] Pennington J. BSD Now: 361: Function-based MicroVM[EB/OL]. (2020-07-30)[2026-08-15]. <https://www.bsdnow.tv/361>.
- [BSD Now EP109] Pennington J. BSD Now: 109: Impish BSD[EB/OL]. (2015-09-30)[2026-08-15]. <https://www.bsdnow.tv/109>.
- [BSDTalk EP61] Backman W. BSDTalk: 61: bsdtalk061 - Interview with lighttpd developer Jan Kneschke[EB/OL]. (2006-08-15)[2026-08-27]. <https://archive.org/details/bsdtalk061>.

<!-- /PODCAST_REVIEW -->
