---
chapter: 第 106 章
id: CH106
volume: 第05卷-freebsd的工程化奠基
---

# 第 106 章 freebsd8x的虚拟化与网络栈演进

## 要点

- XEN 移植史料疑点：(1) 移植起始时间；(2) 主要移植者归属；(3) 是否有 Citrix/Amazon 参与
- SCO v. Novell 终局澄清了 UNIX 版权归属，消除了对 BSD 生态的法律威胁；BSD 社区可安心开发而不必担心 SCO 诉讼
- FreeBSD 早期使用独立的 ATA 驱动栈（`sys/dev/ata/`）管理 ATA/ATAPI/SATA 设备，与 SCSI 子系统（CAM，Common Access Method）并行存在；ATA 驱动栈源自 4.x 时期的设计，存在 SMP 扩展性差、与新硬件兼容性不足、维护困难等问题；CAM ATA 子系统的基础架构由 Scott Long 于 2009-07-10T08:18:0
- VNET 史料疑点：(1) 设计起始时间；(2) Zec 的灵感来源；(3) 是否有学术背景
- 透明大页史料疑点：(1) 自动化的时间线；(2) 与 7.0 SUPERPAGE 的关系；(3) 是否参考 Linux THP

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3705] 卷“第05卷-freebsd的工程化奠基”第 106 章，匹配置信度 folder，原因：folder 第104章
- [DB:references_fulltext:chapter_matches:chmatch_3775] 卷“第05卷-freebsd的工程化奠基”第 106 章，匹配置信度 folder，原因：folder 第104章
- [DB:references_fulltext:chapter_matches:chmatch_3787] 卷“第05卷-freebsd的工程化奠基”第 106 章，匹配置信度 folder，原因：folder 第104章
- [DB:references_fulltext:chapter_matches:chmatch_3791] 卷“第05卷-freebsd的工程化奠基”第 106 章，匹配置信度 folder，原因：folder 第104章
- [DB:references_fulltext:chapter_matches:chmatch_3794] 卷“第05卷-freebsd的工程化奠基”第 106 章，匹配置信度 folder，原因：folder 第104章
- [DB:references_fulltext:chapter_matches:chmatch_3808] 卷“第05卷-freebsd的工程化奠基”第 106 章，匹配置信度 folder，原因：folder 第104章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 厂商参与，需查；**统计局限性标注**——统计显著 ≠ 实际显著，C-40 Kaplan-Meier 中位数寿命 3.64 年仅反映 freebsd-src 全仓库文件寿命分布的中位数，不等于 XEN 移植相关文件的实际寿命；95% CI [1,329.3, 1,344.8] 窗口较窄反映大样本下的精确估计但不可消除右删失 14.39% 引入的偏差；右删失文件可能在未来被复活或永久弃用，生存估计对
- 经 freebsd.duckdb commit_files 表验证，原大纲称“新 CAM ATA 子系统由 Alexander Motin 等主导开发”需修正——CAM ATA 子系统的基础架构（sys/cam/ata/ 与 sys/dev/ahci/）由 Scott Long 于 2009-07-10 commit `52c9ce25d8339ad0228be8aaf0e44b45314b38dc` 引

## 文献

- FreeBSD 8.0 src/sys/xen/ commit log；freebsd-xen mailing list 2008-2009 archives；Rabson, D. FreeBSD Xen port status (2009) ［A］；统计分析报告：描述性统计.md SubTask 2.1 + SubTask 2.4 [R/OL]. 2026-07-27. 文件路径：`c:\Users\ykla\Documents\hibsd\03-原始史料库\01-代码仓库史料\01-数据库本体\统计分析\描述性统计.md`；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. freebsd.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase2_descriptive.py`. SubTask 2.4 Kaplan-Meier 生存估计。执行日期：2026-07-27 [考据脚注：C-03、C-40 经 `script/phase2_descriptive.py` 执行结果与 `phase2_results.json` 结构化结果交叉验证；Kaplan-Meier 估计基于 lifelines 0.30.0 实现。]

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2009-2011 年间：102,147 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- LWN.net SCO v. Novell verdict coverage (2010)；Groklaw.net SCO saga coverage (2003-2010)；The FreeBSD Foundation statement on SCO verdict (2010)；FreeBSD Quarterly Status Report (2010-Q2)［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2009-2010 年间：69,391 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD 8.0/9.0/10.0-RELEASE Release Notes；Alexander Motin CAM ATA EuroBSDCon/BSDCan 演讲（2009-2012）；freebsd-scsi 邮件列表 2008-2012 年 CAM ATA 讨论；**cam(4)** 与 **ata(4)** 手册页；`sys/cam/ata/` commit log；Scott Long. Separate the parallel scsi knowledge out of the core of the XPT, and modularize it so that new transports can be created. freebsd-src [DB/OL]. 2009-07-10T08:18:08Z. commit: 52c9ce25d8339ad0228be8aaf0e44b45314b38dc；Alexander Motin. MFp4: Move Port Multiplier support code out of ATA XPT into pmp periph driver. freebsd-src [DB/OL]. 2009-10-23T12:36:42Z. commit: 65d0fb03ad2580c999c3f590fa7e77f3ed8e1def；Alexander Motin. Tune CAM ATA kernel options a bit. Move PMP support from da to scbus and add ada device option, according to man page. freebsd-src [DB/OL]. 2009-11-19T16:26:07Z. commit: 9e30fbf662781a345d55679defabb13b123f9286；freebsd.duckdb contributors 表（freebsd-src / <mav@FreeBSD.org>，8587 条 commit，2007-04-12 至 2026-07-04）；release/8.0.0. freebsd-src 仓库 tag [DB/OL]. 2009-11-21T06:13:29Z. tag: release/8.0.0; commit: 59dd044d1cb744d3dba6b41c41e196b54e8fd9f8 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-virtualization mailing list 2009-2011 archives；Zec, M. VNET design notes (2009)；freebsd-arch mailing list VNET proposal (2008) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-hackers superpage threads (2008-2010)；Cox et al. (2007) superpage paper；freebsd-current mailing list THP discussion (2010) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD 8.x src/sys/cddl/contrib/opensolaris/ commit log；freebsd-fs mailing list ZFS integration (2009-2011)；Dawidek, P. J. ZFS port status (2009) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-usb mailing list 2009-2011 archives；Selasky, H. P. USB stack rewrite notes (2009)；FreeBSD 8.0-RELEASE hardware notes ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-fs mailing list 2009-2011 archives；Mackerras, R. NFSv4 implementation notes (2009)；Linux NFSv4 documentation (kernel.org) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Macy 报告； bhyve 文档 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- freebsd-virtualization mailing list 2009-2011 archives；freebsd-hackers virtualization threads (2010)；LWN.net FreeBSD virtualization coverage (2010-2011) ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP186（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- AsiaBSDCon 2017 在东京举行，议题覆盖 FreeBSD 上的 Xen Dom0、bhyve 向 ARM 移植、OpenBSD VMM/VMD 更新与 pledge 对 capsicum 的沙箱比较。（BSD Now EP186，[432.94-560.68]，L2）
- Philipp（OpenBSD 前提交者）回顾 2002 年 Karlsruhe hackathon 参与 PF 测试与文档工作，实现接口分组并拆分 pf.c 中的 IOCTL 代码。（BSD Now EP186，[3969.0-4226.0]，L1）
- Philipp 描述 OpenBSD 路由域（rdomain）为单机上的多个虚拟路由器，可用于多租户防火墙与相同 IP 复用的隔离测试。（BSD Now EP186，[4381.84-4761.18]，L1）
- 2004 年 PF hackathon 曾发现用户态 32 位与内核 8 位规则编号溢出导致的隐蔽错误，需超过约 256 条规则才触发。（BSD Now EP186，[4227.0-4285.88]，L1）

**史料**：

- AsiaBSDCon 2017 演讲幻灯片与日程（BSD Now EP186，[432.94-560.68]，L1）
- Philipp 访谈自述（BSD Now EP186，[3969.0-5733.62]，L1）
- OpenBSD PF 邮件列表与 CVS 历史（BSD Now EP186，[3969.0-4285.88]，L1）

**史观**：

- 总纲10 动手者创造历史：PF 由测试者、文档者与提交者共同打磨，历史由大量动手协作的人推动。（BSD Now EP186，[4016.52-4285.88]，L1）
- 总纲4 分离聚合是永恒规律：路由域把一台物理路由器分离为多个逻辑路由器，体现分离聚合的循环。（BSD Now EP186，[4381.84-4761.18]，L1）
- 总纲6 和解优于斗争：OpenBSD 社区“批评即受邀修复”的协作方式，强调和解与共建而非对抗。（BSD Now EP186，[4016.52-4050.66]，L1）

**辨析**：

- [存疑脚注] 访谈中 2002 年 hackathon 地点、PF 实现细节系当事人十余年后回忆，需与 OpenBSD 邮件列表与 CVS 记录核验。　[存疑脚注] 当事人回忆性细节，缺乏独立档案印证。（BSD Now EP186，[3969.0-4285.88]，L4）

**文献**：

- [BSD Now EP186] Pennington J. BSD Now: 186: The Fast And the Firewall: Tokyo Drift[EB/OL]. (2017-03-22)[2026-08-15]. <https://www.bsdnow.tv/186>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- Barham. et al. (2003) Xen SOSP[C]. 2003. ［DKC-1783→fulltext:5975］
<!-- /dangan-20260908 -->
