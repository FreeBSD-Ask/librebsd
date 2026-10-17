---
chapter: 第 121 章
id: CH121
volume: 第06卷-freebsd的核心技术革新
---

# 第 121 章 FreeBSD 存储栈的 FFS 与 UFS 演进

## 要点

- 中文网络上关于 UFS/FFS 历史的常见错误包括：FFS 发布年份误作 1984 年（应为 1983 年 8 月随 4.2BSD 发布，论文 1984 年发表）、Soft Updates 引入 FreeBSD 版本误作 5.0（应为 3.x 时期集成，4.x 默认启用）、UFS2 设计者遗漏 Poul-Henning Kamp（McKusick 与 phk 共同设计）、SUJ 引入版本误作 Fr
- GEOM 引入 FreeBSD 的精确时间为 FreeBSD 5.0（2003 年 1 月），但开发工作从 2001-2002 年即已开始，在 FreeBSD 5.0-CURRENT 分支中逐步替换旧存储层；GEOM 与 Linux Device Mapper（2002 年 Red Hat 主导开发，随 Linux 2.6 引入）是同时代产物，但设计哲学存在关键差异：GEOM 是纯内核态框架，用户
- CAM 从仅支持并行 SCSI 到统一支持 SCSI/SAS/SATA/USB/NVMe 的演进历时 20 余年（1998-2020+），核心阶段包括：FreeBSD 3.0（1998）CAM 导入支持并行 SCSI；FreeBSD 5.x USB **umass(4)** 通过 CAM 接入；FreeBSD 8.x-9.x ATA/SATA 整合入 CAM 成为 **ada(4)**；FreeB
- FreeBSD NFS 支持历史：NFSv2 在 BSD 4.3 时代即已引入，NFSv3 在 FreeBSD 3.x/4.x 时期支持，NFSv4 由 Rick Macklem 主导重写，新的 NFSv4 客户端/服务器实现随 FreeBSD 8.2/9.0（2012 年前后）引入，支持 NFSv4.0、NFSv4.1（含 pNFS 部分特性），旧 NFS 实现仍保留为兼容；NFS 实现位于内核

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3661] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3662] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3664] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_348] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_351] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_352] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_359] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:references_fulltext:chapter_matches:chmatch_363] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 0.8，原因：关键词重合 1 项 + 加分 1
- [DB:bsdnow_podcast:outline_mappings:om_11314] BSD Now 第 552 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11691] BSD Now 第 505 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_11841] BSD Now 第 484 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12067] BSD Now 第 461 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12108] BSD Now 第 456 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12136] BSD Now 第 454 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12534] BSD Now 第 417 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12634] BSD Now 第 401 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_12678] BSD Now 第 379 期，匹配 CH121 章，关联度 2.0
- [DB:bsdnow_podcast:outline_mappings:om_10637] BSD Now 第 637 期，匹配 CH121 章，关联度 1.0
- [DB:historical_claims:claim] 关键词行级挖掘素材线索 121.5-关键词行级挖掘素材线索（3 条，CL-RM 段，见 121.5-关键词行级挖掘素材线索.md）

## 史观

总纲第 4 条——分离聚合是永恒规律：UFS 与 FFS 分层共生——ufs/ 承担目录结构与元数据处理，ffs/ 承担数据块分配与物理布局，二者分离而聚合为完整的文件系统实现；存储栈自旧 UFS、Soft Updates、SUJ 至 GEOM/CAM 的演进，亦呈各层反复分离与重新聚合的循环。章级各子节的逐条史观映射详见本章各子节文件的史观字段。

## 辨析

- 需澄清一个常见误解：“UFS 是 FFS 的另一个名字”——在 BSD 术语中，UFS 指上层目录结构和元数据处理代码（src/sys/ufs/ufs/），FFS 指下层数据块分配和物理布局代码（src/sys/ufs/ffs/），两者共同构成完整的文件系统实现；Solaris UFS、macOS 旧版 UFS 均从 BSD UFS/FFS 衍生但各自有扩展（如 Solaris UFS Loggi
- 需纠正一个关于 GEOM 设计来源的说法：“GEOM 是 Netgraph 移植到存储”——phk 本人多次表示 GEOM 受 Netgraph 启发，但存储与网络有本质差异：存储 I/O 必须按请求顺序完成（生物序等价性），网络包可乱序、复制、丢弃，因此 GEOM 的实现与 Netgraph 完全独立；GEOM 是否 “未完成”——**geom_sched(8)**（I/O 调度器）模块长期处于
- 需澄清 “Linux SCSI midlayer 与 CAM 谁更先进” 的无意义比较——两者架构目标不同：CAM 是所有存储传输的统一抽象，Linux SCSI midlayer 仅处理 SCSI 协议类设备，ATA 走 libata、NVMe 走独立驱动，块层是另一层抽象；两种架构各有优劣：CAM 的统一带来工具和错误处理的一致性，但要让新协议适配 CAM 需要额外工作；Linux 的分层更灵
- 时间线错误：“NFSv4 在 FreeBSD 8.0 引入”——新 NFSv4 客户端/服务器代码在 FreeBSD 8.2（2011 年 7 月）和 9.0（2012 年 1 月）中正式发布，旧的 NFSv2/v3 实现继续可用，用户可通过 mount 选项选择使用新/旧实现；FreeBSD NFSv4.1/pNFS 支持在 FreeBSD 12/13 中持续完善；**aio(4)** 的一个误

## 文献

- FreeBSD Project. *FreeBSD Release Notes Archive*. freebsd.org/releases; McKusick, M. K. *Soft Updates, Snapshots, and Background Fsck Resources*. mckusick.com/softdep/; Aurora, V. (2009-07-01). *Soft updates, hard problems*. LWN.net, lwn.net/Articles/339337/; McKusick, M. K., Neville-Neil, G. V., & Watson, R. N. M. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Addison-Wesley, Chapter 8. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Kamp, P.-H. (2004). *GEOM Tutorial*. BSDCan 2004; FreeBSD Project. **geom(4)**, **geom(8)** Manual Pages; Linux Kernel Documentation. *Device Mapper*. kernel.org/doc; Lucas, M. W. (2018). *FreeBSD Mastery: Storage Essentials*. Chapter 3-5.［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. **camcontrol(8)** Manual Page; McKusick, M. K. et al. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Chapter 10; FreeBSD Project. *CAM Subsystem Source Tree*. src/sys/cam/. ［B］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. **nfs(5)**, **aio(4)**, **nfsstat(1)** Manual Pages; Macklem, R. (2009-2012). *New NFSv4 Client/Server Implementation Commits*; FreeBSD Project. *FreeBSD 9.0 Release Notes* NFSv4 section; McKusick, M. K. et al. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Chapter 9. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP298、BSD Now EP278、BSDTalk EP250（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 本期报道 UFS/FFS 一个源自 4.1BSD（约 1982 年）的目录项填充未初始化字节泄露，可经构造文件名泄露最多 254 字节内核栈；FreeBSD 修补并新增 fsck -z 清零填充。（BSD Now EP298，[53.24-347.78]，L2）
- NomadBSD 1.2 为基于 FreeBSD 12.0 的 live 桌面系统，采用 Openbox 与 DSB 桌面套件，新增 Qt 图形安装器，用于数据恢复与桌面体验。（BSD Now EP298，[723.52-1023.4]，L2）
- 本期介绍用 rdsetroot 与 autoinstall 应答文件实现 OpenBSD 无人值守升级，并预告 6.6 将随 sysupgrade 工具。（BSD Now EP298，[1060.66-1234.28]，L2）
- McKusick 亲述伯克利早期四张桌四人同处一室、与 Bill Joy 为办公室同僚，办公室仅一部电话且十之八九是找 Bill Joy；他形容 Bill Joy 更像营销者，四处演讲、散发磁带、动员他人贡献。（BSD Now EP278，[173.80-287.60]，L1）[订正：原 [176.66-198.66]，2026-09-30 SenseAudio 重转核对]
- McKusick 认为 FreeBSD 二十五年来最大的成就是形成一套能持续吸纳新人并让其上升的治理机制：文档 committer 与源码 committer 同样有权选举 core，营销背景者也能当选。（BSD Now EP278，[533.12-611.68]，L1）
- McKusick 援引 MIT 与法国南部高校的社会学研究，称多数开源项目约五年内沉寂，只有 Apache 与 FreeBSD 等项目完成三次以上成功的领导层更替，FreeBSD 已历约五代。（BSD Now EP278，[725.94-848.56]，L1）
- McKusick 亲述 FreeBSD 基金会起源：早期发行由 Walnut Creek CD-ROM 支撑，后依赖 Yahoo 提供基础设施十余年，Justin Gibbs 因担忧单一公司退出而发起基金会。（BSD Now EP278，[1883.72-1965.34]，L1）
- McKusick 亲述 UFS 三十年：其保存的 1982 年磁盘镜像在当代仍可读写，UFS 适合资源受限的嵌入式设备，ZFS 适合大资源环境，二者各解决不同问题。（BSD Now EP278，[1093.34-1174.26]，L1）
- McKusick 判断容器概念发明于 FreeBSD 却在他处获得成功，FreeBSD 常把项目推进到九成而缺最后一成产品化，恰如“先驱挨箭、定居者得地”。（BSD Now EP278，[2596.78-2625.54]，L1）
- Rick Reed 于 MeetBSD California 2014 自述 WhatsApp 架构与规模：200 台 chat 前端与约 350 台多媒体服务器辅以后端账户数据与离线存储集群，后者仅在消息于收发双方之间传输时暂存数据；当时已逾 6 亿月活用户，峰值 1.4 亿并发连接、每秒 44 万新连接、每秒 110 万条用户消息（含在线状态等事件约每秒 300 万次）、每日图片逾 10 亿；其技术底座为 Erlang actor 模型与 FreeBSD SMP 扩展性——每个手机连接对应一个约 1600 字节的 BEAM 轻量进程，无共享状态、纯消息传递、调度线程逐一绑定 CPU 线程，单机可承载数百万连接；当事人将一台 chat 前端负载加倍实测，CPU 利用率自约 55% 平滑升至 98% 至 99% 并可全天满载，调度器利用率曲线与 CPU 曲线贴合、争用损耗极小，内核经少量调优后几乎不构成障碍，集群曾因节点持续 95% 满载 24 小时而触发过热告警，系统本身仍稳定运行。（BSDTalk EP250，[537.44-1153.74]，L1）
- FreeBSD 选型先于现团队：创始人 Jan Koum 与 Brian Acton 均出身 Yahoo 平台工程，凭其大规模互联网服务经验认定 FreeBSD 的 TCP 栈质量与稳定性突出、发布可预期、文档与内核内部资料齐备，足以支撑预想中的大规模服务；当事人本人在 Yahoo 曾编写内核模块并负责平台库与操作系统之间的接口层，此前任职 Silicon Graphics 从事视频服务。（BSDTalk EP250，[305.48-392.50]，L1）
- 当事人梳理生产版本迁移史：2009 至 2010 年运行 FreeBSD 7，升级 8 后性能改善但遇到 zero-copy socket 导致消息在写入 socket 与发出网卡之间损坏的问题（关闭该特性解决）、IGB 网卡锁死（回移稳定分支驱动修复）与内核拒绝采用稳定的 TSC 时钟源（补丁强制启用）；2011 年优化后单机曾达约 280 万连接；2013 年迁至 FreeBSD 9 后运行近两年，随机 panic 几乎绝迹，仅余机器检查异常与 UFS 因此前崩溃损坏引发的停机。（BSDTalk EP250，[2001.16-2151.66]，L1）
- 存储实践：全线使用 UFS 并以 JBOD 直连磁盘、弃用 RAID 卡（仅视频服务器以 gmirror 提供镜像），文件系统按离线信箱、图片、视频等负载分别定制块大小与 fragment 大小；实测机械盘在持续满负荷下写入上限约每秒 45 至 50 MB（曾与 Kirk McKusick 协作分析），离线消息约半数在写入后 25 秒内即被取走，大量落盘仅服务持久化冗余；调宽 dirty buffer 与拉长 sync 延迟会使 syncer 行为突发化、总体吞吐反降，遂回退默认写穿并以应用层缓存补足读取；崩溃恢复采取三级策略——先以 soft updates 快速恢复上线，再崩溃则并行全量 fsck，必要时顺序 fsck，另以扩容 UFS dirhash 缓存超过 2 GB 的哈希目录树。（BSDTalk EP250，[1891.88-2477.94]，L1）

**史料**：

- David G. Lawrence 提交的 UFS 补丁与 Theo de Raadt 的 OpenBSD 提交说明（1997 年 read 目录返回 EOF、2016 年改报错误）。（BSD Now EP298，[315.46-472.04]，L2）
- AsiaBSDCon 关于 PowerPC64 移植 ports 的论文及 Ted Unangst 的评论。（BSD Now EP298，[1864.7-1957.6]，L2）
- McKusick 提及 FAST 大会关于文件系统三十年演进的 keynote、BSDCan 2018 的采访背景，以及 CSRG 重写 AT&T 程序时 Keith Bostic 主张将署名归于他人以自保的细节。（BSD Now EP278，[339.18-390.46]，L1）
- McKusick 提及 TeachBSD 项目，主张以真实操作系统而非玩具系统教授计算机科学，并认为 DTrace/DWatch 等工具是“玻璃制”可观测系统的重要组成部分。（BSD Now EP278，[2723.00-2781.38]，L1）
- 本期为 Rick Reed 在 MeetBSD California 2014 演讲《WhatsApp: Half a billion unsuspecting FreeBSD users》的现场录音，属 WhatsApp 生产运维的一手口述史料；其口述包含 CPU 与调度器利用率曲线、连接数与磁盘写入遥测、过热告警与 panic 事件、zero-copy socket 损坏与 TSC 时钟源补丁等一手故障记录，可与其他场合演讲及文本互证。（BSDTalk EP250，[31.96-40.90]，L1）

**史观**：

- 总纲22 知识注定过时：源自 1982 年的文件系统实现多年后仍被发现新问题，旧知识需不断更新。（BSD Now EP298，[243.08-265.96]，L2）
- 总纲10 动手者创造历史：漏洞由动手阅读代码者发现并修复，OpenBSD 侧早年的 read 目录改动无意中缓解了泄露。（BSD Now EP298，[311.10-477.28]，L2）[订正：原 [392.38-477.28]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：McKusick 强调软件与项目的持续“养护”远非社区驱动项目所长，人们倾向做新奇有趣之事；文档与基础设施的默默维护恰是系统得以存活的关键。（BSD Now EP278，[451.46-489.68]，L1）
- 总纲3 不存在进步，只有权力再分配：McKusick 指出历史上 IBM、微软各自占据过绝对支配地位又相继让位，Linux 今日的支配地位同样不会永远持续，FreeBSD 甘居雷达之下反而得以延续。（BSD Now EP278，[2247.34-2342.26]，L1）
- 总纲5 没有必然性，只有偶然性：McKusick 以“容器发明于 FreeBSD 却成功于他处”为例，指出技术领先与市场成功之间并无必然因果，成功更多依赖偶然的产品化时机。（BSD Now EP278，[2596.78-2625.54]，L1）
- 总纲10 动手者创造历史：约 12 人的服务器团队维系 6 亿用户规模的服务：配置管理仅用 make 人工维护、负载分配依赖 DNS 轮询、重大变更先投放到承担约半个百分点流量的单台服务器观察；Erlang 热代码加载使系统可在数百万人在线且满速运行时完成升级，三年间全系统宕机仅一次（Facebook 收购公告之后）。大规模服务的实际承载者是少数动手运维者，而非站在台前的明星开发者。（BSDTalk EP250，[2757.34-3331.58]，L1）
- 总纲5 没有必然性，只有偶然性：关键技术选型皆为具体偶然条件的汇合而非理性推演的必然：Erlang 自创办之初即入选，因其时存在可用的开源 XMPP 服务器、且项目以替代短信为志而电信渊源的 Erlang 显得契合；FreeBSD 则系创始人 Yahoo 经历的自然延续。当事人回忆当年在 Yahoo 视 Erlang 为多余的新语言，直到亲历 WhatsApp 才体会其威力，可见技术路径由具体人事与时机决定。（BSDTalk EP250，[3243.08-3278.70]，L1）

**辨析**：

- [考据脚注] 转写所述 36 年 bug 与 4.1BSD 约 1982 年起源一致，但各 BSD 受影响程度不同，OpenBSD 因既有缓解不发布 errata，属节目对原始提交的转述。 [考据脚注] 各 BSD 影响面与 OpenBSD 不发布 errata 属单源转述（BSD Now EP298，[236.30-620.90]，L4）[订正：原 [339.1-415.76]，2026-09-30 SenseAudio 重转核对]
- McKusick 关于“文档 committer 与源码 committer 同等投票”的叙述属当事人视角，须与 FreeBSD 选举规则文件与历届 core 名单交叉核验；其对自己“不再关键”的自评也属谦辞。 [存疑脚注] 选举资格细节须以 FreeBSD Core Team 规则文件核实。（BSD Now EP278，[533.12-611.68]，L3）
- McKusick 提及的研究（MIT 与法国高校基于 commit log 分析领导层）未给出具体出处，其“只有 Apache 与 FreeBSD 等少数项目完成多次更替”的结论需核对原始研究。 [存疑脚注] 所援引研究未具名，结论无法直接追溯。（BSD Now EP278，[725.94-799.70]，L4）
- 标题所称“5 亿毫不知情的 FreeBSD 用户”点出沉默使用现象：终端用户无从感知底层操作系统，自由软件的扩散依赖企业生产采用而非用户选择，当事人开场亦以现场举手调查印证知情者寥寥；此为“沉默 BSD 企业”现象的当事人自证，但亦须辨析——企业愿意公开自述者（如本场演讲）恰是沉默群体中的例外，样本代表性有限。（BSDTalk EP250，[178.32-191.12]，L1）

**文献**：

- [BSD Now EP298] Pennington J. BSD Now: 298: BSD On The Road[EB/OL]. (2019-05-16)[2026-08-15]. <https://www.bsdnow.tv/298>.
- [BSD Now EP278] Pennington J. BSD Now: Episode 278: The Real McCoy | BSD Now 278[EB/OL]. (2018-12-27)[2026-08-15]. <https://www.bsdnow.tv/278>.
- [BSDTalk EP250] Backman W. BSDTalk: 250: bsdtalk250 - WhatsApp: Half a billion unsuspecting FreeBSD users by Rick Reed[EB/OL]. (2015-01-31)[2026-08-27]. <https://bsdtalk.blogspot.com/2015/01/bsdtalk250-whatsapp-half-billion.html>.

<!-- /PODCAST_REVIEW -->

<!-- ROW_MINE: login-zazhi.articles.CL-2-058 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-2-058`；login 逐条遍历判定采纳）

2021 年 Roscoe 在 OSDI/ATC 主题演讲中指出：操作系统研究已被 Linux 主导，OSDI 两年间仅三篇 OS 设计论文且全部基于 Linux 改进，OSDI'21 中 OS 设计仅占 6%；;login: 编辑 Farrow 认同并补充 OS 还应向用户提供熟悉 API 的观点。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1160 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1160`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：ZFS 动态分配所有数据块，并在全部 vdev 之间做条带化分布（YouTube EPYDuCB-3o5OQ，[444.88-452.07]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1295 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1295`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：一道考题出现在 Plan Nine 起步同期，据讲者回忆该考题约为 1988 年。（YouTube EPdi1W6r-0cAU，[135.9-147.4]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-597 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-597`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Pawel Dawidek 口述：在 ZFS 之上实现 jail 的常见做法是使用 ZFS 克隆。（YouTube EPhYBgoaQC-vo，[1100.24-1107.59]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-865 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-865`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Chuck Tuffli 口述：该 NVMe 设备被 NVMe 驱动报告处于只读模式。（YouTube EPq4vtp4hJfao，[1250.03-1258.62]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-864 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-864`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者 Chuck Tuffli 口述：出问题那套环境是 FreeBSD 12 系统，经 iSCSI（转写音作 ice Guzzi）提供 ZFS（转写音作 zi falls）服务，SLOG 位于一块 NVMe（转写音作 NDB）设备上。（YouTube EPq4vtp4hJfao，[1238.33-1250.02]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-891 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-891`；w172 YouTube 章节路由采纳）

据〔FreeBSDFridays〕讲者口述：在 BSD 上 UFS（又称 FFS）作为本地文件系统，其之上可再叠一层 NFS 服务器。（YouTube EPr5nFapl5C1s，[736-743.59]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1133 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1133`；w172 YouTube 章节路由采纳）

据〔AsiaBSDCon 2008〕讲者 Pawel Jakub Dawidek 口述：GEOM 的 GELI 类也会使用 CPU 自带的自动加密核心（转写音作 automatic CPU cores），从而加速加密。（YouTube EPxMpmOezBJZo，[1620.88-1626.11]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-1399 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1399`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2010 Kirk McKusick〕讲者口述：软更新机制与后台 FSCK 十余年来工作良好，但如今文件系统变得极大，FSCK 的运行时间以数小时计，而它施加给系统、尤其是 IO 子系统的负载相当可观，会让整机变慢；若 FSCK 要跑 24 小时便挤进白天的繁忙时段，用户开始反对。这正是引入日志回滚的动机。（YouTube EP_NuhRkiInvA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1400 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1400`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2010 Kirk McKusick〕讲者口述：对软更新方案要日志记录的对象，只需把这些块与 inode 记入日志，即可用日志回滚把它们放回位图，从而取代后台 FSCK；由于只涉及数量很少的事件，日志无须很大，最初主张 16 MB 后依协作开发者意见把测试值压到 1 MB，在 1 TB 文件系统上极力制造压力也难以写满。（YouTube EP_NuhRkiInvA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1401 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1401`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔BSDCan 2010 Kirk McKusick〕讲者口述：引入日志使软更新代码量近乎翻倍，从 6500 行增至 11500 行；此外还有约 2600 行日志恢复代码并入 FSCK，接近 FSCK 原有 6000 行，合计比原先多出约 50%，因此项目规模不小。（YouTube EP_NuhRkiInvA，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1680 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1680`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD 技术会议讲者 Warner Losh 的 CAM 专题〕讲者口述：在其部署里 FreeBSD 能跑满所用 NVMe 卡的全部带宽；他称这主要归功于“Drew”对整个网络栈的优化，FreeBSD 的延迟已不错但仍可优化——目前约 30 微秒，再抠掉 5 到 10 微秒仍有空间。（YouTube EPeUSNea3I-hE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1681 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1681`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD 技术会议讲者 Warner Losh 的 CAM 专题〕讲者口述：他把 CAM 的职责概括为三件：I/O 的排队与调度；出错时冻结队列以便做错误恢复、再恢复 I/O；以及施加规则、约束系统当前这一刻真正能发给磁盘的命令。（YouTube EPeUSNea3I-hE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1682 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1682`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD 技术会议讲者 Warner Losh 的 CAM 专题〕讲者口述：他解释了 CAM 的 devq 如何限流：它保证最多只往 SIM 送 32 个 I/O、不至于灌满；一旦意外超发，或错误处理过程中积压超出承受范围，就得由 SIM 自己兜住。通常做法是主动 pacing，让盘里始终恰好有适量的请求。（YouTube EPeUSNea3I-hE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1683 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1683`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔FreeBSD 技术会议讲者 Warner Losh 的 CAM 专题〕讲者口述：回答 DTrace 可否插桩 CAM 的提问时，他称 CAM 已有 tracing 例程，可以顺着看 CCB 上下来回；不少 CAM 调试路径都是 DTrace 的理想候选点，主要集中在 cam xpt 的 done 处理上，另外每个 transport（ATA xpt 与 nvme xpt）大概各需要一两个探针。（YouTube EPeUSNea3I-hE，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2074 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2074`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Warner Losh 于 BSDCan 2017 演讲〕讲者口述：其展示的 FreeBSD I/O 栈层次图，是“kirk's and George's and Roberts”那本设计与实现之书内容的简化版，自顶向下依次为系统调用、文件表项、vnode、文件系统、页缓存，再向下到设备层；本讲重点放在页缓存（缓冲缓存）层。（YouTube EPyIxsm6JI_7w，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2075 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2075`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Warner Losh 于 BSDCan 2017 演讲〕讲者口述：buffer cache 的核心是 struct buff，它并非映射整个 vnode，而是映射 vnode 的特定区段，内含 offset 与 length 字段，其页通常由 VM object 支撑（讲者补充：VM object 始终存在，只是未必已填充）。（YouTube EPyIxsm6JI_7w，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2076 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2076`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Warner Losh 于 BSDCan 2017 演讲〕讲者口述：缓冲缓存对可并行的异步写入数量施加全局上限，单一磁盘时该全局上限不成问题，但慢硬盘与快 SSD 并存时，一方会饿死另一方，究竟谁被饿死取决于请求到达顺序。（YouTube EPyIxsm6JI_7w，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2077 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2077`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Warner Losh 于 BSDCan 2017 演讲〕讲者口述：其反压设计的总纲是：在最低层，每个设备发布自己认为能承担多少工作量，以及承担该工作量的时间尺度。（YouTube EPyIxsm6JI_7w，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2245 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2245`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Send and Receive of File System Protocols: Userspace Approach With puffs〕讲者口述：puffs 的最初工作是在 HPA risk 架构上完成的，讲者强调自己说“就是在其上完成”是字面意义上的确在此硬件上运行——当时是在家里做的开发，没有合适的办公椅可用。（YouTube EPziGeB8iRA0c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2246 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2246`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Send and Receive of File System Protocols: Userspace Approach With puffs〕讲者口述：与去年相比唯一的区别是：去年这套机制还叫 puffs，现在改叫 devpts；他说明 devpts 承担消息传递机制，使 puffs 中与文件系统相关的部分与无关的部分（把请求由内核传输到用户态）解耦。（YouTube EPziGeB8iRA0c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2247 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2247`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Send and Receive of File System Protocols: Userspace Approach With puffs〕讲者口述：他写出 SSHFS 的做法仍是协议转译：把 puffs 接口改写为 SFTP 函数调用，即把 openSSH 的 SFTP 部分链接进文件系统服务器，把请求转换为对 SFTP 例程的调用；写完当天即跑通。（YouTube EPziGeB8iRA0c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2248 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2248`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Send and Receive of File System Protocols: Userspace Approach With puffs〕讲者口述：在 9P 协议中只能在一个目录内部重命名文件——不能做跨目录重命名，也不能重命名目录；这看似荒谬的限制，但若深挖正确实现一次 rename 需要做的事，就能理解它为何如此设计。（YouTube EPziGeB8iRA0c，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2541 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2541`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Attilio Rao 讲 FreeBSD VFS/vnode 接口〕讲者口述：内核同一时刻只能用一种文件系统这一难题，最重要也最知名的解法由 Sun 给出——Sun 在 FFS 问世数年之后开发了 VFS/vnode 接口，此后它基本成为整个 Unix 世界实现多文件系统支持的事实标准。（YouTube EPSpS7Ajnx9Q8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2542 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2542`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Attilio Rao 讲 FreeBSD VFS/vnode 接口〕讲者口述：1970 年代末 System V Unix 与 BSD Unix 都用 S5FS；BSD 4.2 引入时 Marshall Kirk McCusick 开发了新文件系统 FFS（fast file system），意在修复 S5 文件系统大量已知性能问题，开发于 1980 年代中期。（YouTube EPSpS7Ajnx9Q8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2543 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2543`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Attilio Rao 讲 FreeBSD VFS/vnode 接口〕讲者口述：把 1980 年代中期的最初实现与当前 FreeBSD 代码相比，VFS/vnode 代码几乎未被改动——改进固然很多，但核心思想与主体结构基本未变；他猜测 NetBSD、OpenBSD 等其他 BSD 亦然，并认为这足证 Sun 当年实现该接口的功力。（YouTube EPSpS7Ajnx9Q8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2544 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2544`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔Attilio Rao 讲 FreeBSD VFS/vnode 接口〕讲者口述：FreeBSD 在 VFS 与 I/O 路径上暴露出若干弱项，其中 name cache 是大问题——它大概从未被改动过；当时有一位受 Summer of Code 资助的学生正在实现一套可能取而代之的 name cache 新模型。（YouTube EPSpS7Ajnx9Q8，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
