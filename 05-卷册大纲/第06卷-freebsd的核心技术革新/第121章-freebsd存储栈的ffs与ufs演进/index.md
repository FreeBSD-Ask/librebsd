---
chapter: 第 121 章
id: CH121
volume: 第06卷-freebsd的核心技术革新
---

# 第 121 章 freebsd存储栈的ffs与ufs演进

## 要点

- 中文网络上关于 UFS/FFS 历史的常见错误包括：FFS 发布年份误作 1984 年（应为 1983 年 8 月随 4.2BSD 发布，论文 1984 年发表）、Soft Updates 引入 FreeBSD 版本误作 5.0（应为 3.x 时期集成，4.x 默认启用）、UFS2 设计者遗漏 Poul-Henning Kamp（McKusick 与 phk 共同设计）、SUJ 引入版本误作 Fr
- GEOM 引入 FreeBSD 的精确时间为 FreeBSD 5.0（2003 年 1 月），但开发工作从 2001-2002 年即已开始，在 FreeBSD 5.0-CURRENT 分支中逐步替换旧存储层；GEOM 与 Linux Device Mapper（2002 年 Red Hat 主导开发，随 Linux 2.6 引入）是同时代产物，但设计哲学存在关键差异：GEOM 是纯内核态框架，用户
- CAM 从仅支持并行 SCSI 到统一支持 SCSI/SAS/SATA/USB/NVMe 的演进历时 20 余年（1998-2020+），核心阶段包括：FreeBSD 3.0（1998）CAM 导入支持并行 SCSI；FreeBSD 5.x USB **umass(4)** 通过 CAM 接入；FreeBSD 8.x-9.x ATA/SATA 整合入 CAM 成为 **ada(4)**；FreeB
- FreeBSD NFS 支持历史：NFSv2 在 BSD 4.3 时代即已引入，NFSv3 在 FreeBSD 3.x/4.x 时期支持，NFSv4 由 Rick Macklem 主导重写，新的 NFSv4 客户端/服务器实现随 FreeBSD 8.2/9.0（2012 年前后）引入，支持 NFSv4.0、NFSv4.1（含 pNFS 部分特性），旧 NFS 实现仍保留为兼容；NFS 实现位于内核

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3827] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 folder，原因：folder 第119章
- [DB:references_fulltext:chapter_matches:chmatch_3967] 卷“第06卷-freebsd的核心技术革新”第 121 章，匹配置信度 folder，原因：folder 第119章
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

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 需澄清一个常见误解：“UFS 是 FFS 的另一个名字”——在 BSD 术语中，UFS 指上层目录结构和元数据处理代码（src/sys/ufs/ufs/），FFS 指下层数据块分配和物理布局代码（src/sys/ufs/ffs/），两者共同构成完整的文件系统实现；Solaris UFS、macOS 旧版 UFS 均从 BSD UFS/FFS 衍生但各自有扩展（如 Solaris UFS Loggi
- 需纠正一个关于 GEOM 设计来源的说法：“GEOM 是 Netgraph 移植到存储”——phk 本人多次表示 GEOM 受 Netgraph 启发，但存储与网络有本质差异：存储 I/O 必须按请求顺序完成（生物序等价性），网络包可乱序、复制、丢弃，因此 GEOM 的实现与 Netgraph 完全独立；GEOM 是否 “未完成”——**geom_sched(8)**（I/O 调度器）模块长期处于
- 需澄清 “Linux SCSI midlayer 与 CAM 谁更先进” 的无意义比较——两者架构目标不同：CAM 是所有存储传输的统一抽象，Linux SCSI midlayer 仅处理 SCSI 协议类设备，ATA 走 libata、NVMe 走独立驱动，块层是另一层抽象；两种架构各有优劣：CAM 的统一带来工具和错误处理的一致性，但要让新协议适配 CAM 需要额外工作；Linux 的分层更灵
- 时间线错误：“NFSv4 在 FreeBSD 8.0 引入”——新 NFSv4 客户端/服务器代码在 FreeBSD 8.2（2011 年 7 月）和 9.0（2012 年 1 月）中正式发布，旧的 NFSv2/v3 实现继续可用，用户可通过 mount 选项选择使用新/旧实现；FreeBSD NFSv4.1/pNFS 支持在 FreeBSD 12/13 中持续完善；**aio(4)** 的一个误

## 文献

- FreeBSD Project. *FreeBSD Release Notes Archive*. freebsd.org/releases; McKusick, M. K. *Soft Updates, Snapshots, and Background Fsck Resources*. mckusick.com/softdep/; Aurora, V. (2009-07-01). *Soft updates, hard problems*. LWN.net, lwn.net/Articles/339337/; McKusick, M. K., Neville-Neil, G. V., & Watson, R. N. M. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Addison-Wesley, Chapter 8. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Kamp, P.-H. (2004). *GEOM Tutorial*. BSDCan 2004; FreeBSD Project. **geom(4)**, **geom(8)** Manual Pages; Linux Kernel Documentation. *Device Mapper*. kernel.org/doc; Lucas, M. W. (2018). *FreeBSD Mastery: Storage Essentials*. Chapter 3-5.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. **camcontrol(8)** Manual Page; McKusick, M. K. et al. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Chapter 10; FreeBSD Project. *CAM Subsystem Source Tree*. src/sys/cam/. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. **nfs(5)**, **aio(4)**, **nfsstat(1)** Manual Pages; Macklem, R. (2009-2012). *New NFSv4 Client/Server Implementation Commits*; FreeBSD Project. *FreeBSD 9.0 Release Notes* NFSv4 section; McKusick, M. K. et al. (2014). *The Design and Implementation of the FreeBSD Operating System* (2nd ed.). Chapter 9. ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP298、BSD Now EP278（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 本期报道 UFS/FFS 一个源自 4.1BSD（约 1982 年）的目录项填充未初始化字节泄露，可经构造文件名泄露最多 254 字节内核栈；FreeBSD 修补并新增 fsck -z 清零填充。（BSD Now EP298，[53.24-347.78]，L2）
- NomadBSD 1.2 为基于 FreeBSD 12.0 的 live 桌面系统，采用 Openbox 与 DSB 桌面套件，新增 Qt 图形安装器，用于数据恢复与桌面体验。（BSD Now EP298，[723.52-1023.4]，L2）
- 本期介绍用 rdsetroot 与 autoinstall 应答文件实现 OpenBSD 无人值守升级，并预告 6.6 将随 sysupgrade 工具。（BSD Now EP298，[1060.66-1234.28]，L2）
- McKusick 亲述伯克利早期四张桌四人同处一室、与 Bill Joy 为办公室同僚，办公室仅一部电话且十之八九是找 Bill Joy；他形容 Bill Joy 更像营销者，四处演讲、散发磁带、动员他人贡献。（BSD Now EP278，[176.66-198.66]，L1）
- McKusick 认为 FreeBSD 二十五年来最大的成就是形成一套能持续吸纳新人并让其上升的治理机制：文档 committer 与源码 committer 同样有权选举 core，营销背景者也能当选。（BSD Now EP278，[533.12-611.68]，L1）
- McKusick 援引 MIT 与法国南部高校的社会学研究，称多数开源项目约五年内沉寂，只有 Apache 与 FreeBSD 等项目完成三次以上成功的领导层更替，FreeBSD 已历约五代。（BSD Now EP278，[725.94-848.56]，L1）
- McKusick 亲述 FreeBSD 基金会起源：早期发行由 Walnut Creek CD-ROM 支撑，后依赖 Yahoo 提供基础设施十余年，Justin Gibbs 因担忧单一公司退出而发起基金会。（BSD Now EP278，[1883.72-1965.34]，L1）
- McKusick 亲述 UFS 三十年：其保存的 1982 年磁盘镜像在当代仍可读写，UFS 适合资源受限的嵌入式设备，ZFS 适合大资源环境，二者各解决不同问题。（BSD Now EP278，[1093.34-1174.26]，L1）
- McKusick 判断容器概念发明于 FreeBSD 却在他处获得成功，FreeBSD 常把项目推进到九成而缺最后一成产品化，恰如“先驱挨箭、定居者得地”。（BSD Now EP278，[2596.78-2625.54]，L1）

**史料**：

- David G. Lawrence 提交的 UFS 补丁与 Theo de Raadt 的 OpenBSD 提交说明（1997 年 read 目录返回 EOF、2016 年改报错误）。（BSD Now EP298，[315.46-472.04]，L2）
- AsiaBSDCon 关于 PowerPC64 移植 ports 的论文及 Ted Unangst 的评论。（BSD Now EP298，[1864.7-1957.6]，L2）
- McKusick 提及 FAST 大会关于文件系统三十年演进的 keynote、BSDCan 2018 的采访背景，以及 CSRG 重写 AT&T 程序时 Keith Bostic 主张将署名归于他人以自保的细节。（BSD Now EP278，[339.18-390.46]，L1）
- McKusick 提及 TeachBSD 项目，主张以真实操作系统而非玩具系统教授计算机科学，并认为 DTrace/DWatch 等工具是“玻璃制”可观测系统的重要组成部分。（BSD Now EP278，[2723.00-2781.38]，L1）

**史观**：

- 总纲22 知识注定过时：源自 1982 年的文件系统实现多年后仍被发现新问题，旧知识需不断更新。（BSD Now EP298，[243.08-265.96]，L2）
- 总纲10 动手者创造历史：漏洞由动手阅读代码者发现并修复，OpenBSD 侧早年的 read 目录改动无意中缓解了泄露。（BSD Now EP298，[392.38-477.28]，L2）
- 总纲10 动手者创造历史：McKusick 强调软件与项目的持续“养护”远非社区驱动项目所长，人们倾向做新奇有趣之事；文档与基础设施的默默维护恰是系统得以存活的关键。（BSD Now EP278，[451.46-489.68]，L1）
- 总纲3 不存在进步，只有权力再分配：McKusick 指出历史上 IBM、微软各自占据过绝对支配地位又相继让位，Linux 今日的支配地位同样不会永远持续，FreeBSD 甘居雷达之下反而得以延续。（BSD Now EP278，[2247.34-2342.26]，L1）
- 总纲5 没有必然性，只有偶然性：McKusick 以“容器发明于 FreeBSD 却成功于他处”为例，指出技术领先与市场成功之间并无必然因果，成功更多依赖偶然的产品化时机。（BSD Now EP278，[2596.78-2625.54]，L1）

**辨析**：

- [考据脚注] 转写所述 36 年 bug 与 4.1BSD 约 1982 年起源一致，但各 BSD 受影响程度不同，OpenBSD 因既有缓解不发布 errata，属节目对原始提交的转述。　[考据脚注] 各 BSD 影响面与 OpenBSD 不发布 errata 属单源转述（BSD Now EP298，[339.1-415.76]，L4）
- McKusick 关于“文档 committer 与源码 committer 同等投票”的叙述属当事人视角，须与 FreeBSD 选举规则文件与历届 core 名单交叉核验；其对自己“不再关键”的自评也属谦辞。　[存疑脚注] 选举资格细节须以 FreeBSD Core Team 规则文件核实。（BSD Now EP278，[533.12-611.68]，L3）
- McKusick 提及的研究（MIT 与法国高校基于 commit log 分析领导层）未给出具体出处，其“只有 Apache 与 FreeBSD 等少数项目完成多次更替”的结论需核对原始研究。　[存疑脚注] 所援引研究未具名，结论无法直接追溯。（BSD Now EP278，[725.94-799.70]，L4）

**文献**：

- [BSD Now EP298] Pennington J. BSD Now: 298: BSD On The Road[EB/OL]. (2019-05-16)[2026-08-15]. https://www.bsdnow.tv/298.
- [BSD Now EP278] Pennington J. BSD Now: Episode 278: The Real McCoy | BSD Now 278[EB/OL]. (2018-12-27)[2026-08-15]. https://www.bsdnow.tv/278.

<!-- /PODCAST_REVIEW -->
