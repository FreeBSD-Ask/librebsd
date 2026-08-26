---
chapter: 第 122 章
id: CH122
volume: 第06卷-freebsd的核心技术革新
---

# 第 122 章 freebsd存储栈的分区与io调度

## 要点

- 2010-2020 年存储栈呈现 “卷管理分层（Linux LVM）vs 统一变换层（FreeBSD GEOM）vs 存储池（Windows Storage Spaces）vs CoW 合一（ZFS/btrfs/HAMMER）” 的多路线格局；FreeBSD 的 GEOM 以模块化、可组合著称，UFS 的 soft updates 提供元数据一致性保障，在非 ZFS 领域保持工程简洁性。同期主流操
- FreeBSD 磁盘命名演进历史：早期 MFM/RLL 磁盘为 wd?（Winchester Disk），SCSI 磁盘为 sd?；FreeBSD 3.x CAM 引入后 SCSI 磁盘改为 da?（Direct Access）；FreeBSD 5.x 时期 ATA 磁盘为 ad?（ATA Direct Access）；FreeBSD 9.0 ATA 接入 CAM 后改为 ada?（ATA Dir
- FreeBSD 网络存储生态除 iSCSI 和 HAST 外，还包括：NFS（Network File System）作为最古老的分布式文件系统协议在 FreeBSD 中有完整的客户端/服务器实现（NFSv2/v3/v4，详见 78.4.4 节）；**ggate(8)**（GEOM Gate）允许用户态程序通过网络导出块设备，是 HAST 和其他用户态 GEOM 模块的基础；**nfsv4(4)*
- Valerie Aurora（当时名 Valerie Henson，ext4 文件系统开发者）于 2009 年 7 月 1 日在 LWN.net 发表文章 "Soft updates, hard problems"（lwn.net/Articles/339337/），从 Linux 文件系统开发者视角对 Soft Updates 提出系统性批评，核心论点包括：Soft Updates 实现极端复杂
- **统计分析印证**——`bsd_commits.db` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；ARIMA(5,0,5) 模型拟合 AIC = 107.39（统计结论 C-29）；非

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3706] 卷“第06卷-freebsd的核心技术革新”第 122 章，匹配置信度 folder，原因：folder 第120章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 不应将 “非 ZFS” 视为 FreeBSD 存储的弱点——GEOM+UFS 在简洁性、可审计性与嵌入式场景仍有价值；ZFS 与 GEOM 在 FreeBSD 中互补共存。
- “FreeBSD 设备名混乱” 是一个常见批评——与 Linux sda/sdb 看似稳定的命名对比，FreeBSD 设备名确实随着架构整合变化过多次；但 Linux 从 hd?（IDE）到 sd?（libata 统一）也经历过类似变化，而且 Linux 的 sd? 命名同样依赖探测顺序，实际生产中也使用 UUID/LVM 标签引用设备而非 sd? 名称；两者只是走了不同的演进路径，最终都收敛到
- FreeBSD 基础系统不包含 Ceph、Gluster 等分布式存储，这些都通过 ports/pkg 提供；这与 Linux 发行版将客户端/服务器全部打包入默认安装不同，体现了 FreeBSD “基础系统最小化、附加软件通过 ports” 的设计哲学；**ggate(8)** 是一个常被忽视但技术上很优雅的设计——它允许用户态进程实现 GEOM provider，这使得 HAST 等网络块设备
- 需要准确引用 Aurora 的原话："soft updates are, simply put, too hard to understand, implement, and maintain to be part of the mainstream of file system development"——这句话有具体语境：Aurora 讨论的是为什么 Soft Updates 没有成为文件系统
- *统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但存储栈实际演进须结合具体子系统（GEOM、CAM、GELI、UFS2）的版本化分析；(2) 非 ZFS 存储栈贡献率未量化：commit 量统计不区分存储栈相关 commit 与其他子系统 commit，非 ZFS

## 文献

- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］> ## 第 56.12 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 56.13 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）---**【本节文献综述】** 详见 [04-现代研究文献/05-参考文献全文数据库/references_fulltext.db](04-现代研究文献/05-参考文献全文数据库/references_fulltext.db) `chapter_reviews` 表（id=15）<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. **ada(4)**, **da(4)**, **nda(4)**, **glabel(8)** Manual Pages; Lucas, M. W. (2018). *FreeBSD Mastery: Storage Essentials*.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. **ggate(4)**, **ggated(8)** Manual Pages; FreeBSD Project. *FreeBSD Handbook - Network Filesystems*. docs.freebsd.org. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- Aurora, V. (2009-07-01). *Soft updates, hard problems*. LWN.net, lwn.net/Articles/339337/; Seltzer, M. I. et al. (2000). *Journaling Versus Soft Updates: Asynchronous Meta-data Protection in File Systems*. USENIX ATC '00; McKusick, M. K., & Roberson, J. (2010). *Journaled Soft-updates*. mckusick.com/softdep/suj.pdf. ［B］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Project. bsd_commits.db freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\bsd_commits.db`; Hibsd Project. 推断性统计.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\推断性统计.md` Task 5; Hibsd Project. 时间序列分析.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\时间序列分析.md` Task 14; Hibsd Project. 卷章数据映射.md [R/OL]. 2026-07-27. `c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\卷章数据映射.md` 第五卷第 56 章映射。［A］### 史观映射> GEOM 的模块化架构是 phk 一个人对着存储层发呆时想出来的东西——偶然而非必然，一个人的洞察决定了 FreeBSD 存储栈此后二十年的骨骼。CAM 同样是 Gibbs 一个人的手笔，GELI 是 Dawidek 的作品，SUJ 是 Roberson 的补丁。动手者创造历史，不是群体的决议而是具体的人在具体的夜晚写下的代码。但 soft updates 的命运提醒着：一个工程师的执念能支撑一个文件系统四十年——从 McKusick 1983 年的研究生时期到 2012 年 Roberson 的 SUJ 补丁——却无法逆转整个产业的选择。当 Aurora 说 soft updates “过于难以理解、实现和维护”，当 Solaris、ext3/ext4、XFS、NTFS 集体转向日志，当 NetBSD 和 OpenBSD 先后移除 Soft Updates 支持，McKusick 的执念从工程遗产变成了一个时代拒绝放手的美学姿态。FFS 从 1983 年 8KB 块加柱面组开始，一路演进到 UFS2 的 64 位块指针加 SUJ 日志，这不是 “向前兼容” 的保守，而是一个工程师对自己创造物的责任——他没有像 Sun 那样放弃 UFS 转投 ZFS，像 Linux 那样在 ext2/ext3/ext4/Btrfs/XFS 之间反复试错，而是在自己创造的基础上修修补补了四十年。这是 BSD 方式的优点也是缺点：你信任一个聪明人四十年前写的代码能修到今天，你也要承担这份信任带来的历史负担。<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- bsd_commits.db（freebsd-src）；0 信任原则方法论；FreeBSD 贡献者多样性研究（如有）据一手文献印证消解^doubt-resolved-649：此文献待 0 信任原则考据验证 ］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2008-2018 年间：455,206 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
