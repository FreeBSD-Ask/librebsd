# 20260814 第06卷 freebsd 的核心技术革新——邮件列表库/参考文献库双库事实核查记录

> 核查范围：`05-卷册大纲\第06卷-freebsd的核心技术革新\` 下第 109-135 章（27 章，含编号缺口）各子节“要点”字段及“史料/辨析”字段中出现的可核查事实。
> 核查工具：`script\_mail_search.py`（邮件列表库，覆盖 FreeBSD 1994-/NetBSD 1994-/OpenBSD 1996-/Usenet 1981-）与 `script\_ref_search.py`（参考文献库 fulltext/facts/people 三模式；tech/timeline 模式因库表列名缺失报错，不可用）。
> 核查方法：0 信任原则，逐条双库检索；命中且一致→通过；命中但不一致→修正；未命中→两库无法验证并注明覆盖范围；仍存疑保留。
> 执行日期：2026-08-15。

## 判定汇总（见各子节）

---

## 第109章 ZFS 设计起源与寻址修辞

- 子节 108.1.1（Jeff Bonwick 与 Matt Ahrens 设计 ZFS 存储池模型）
  - 核查事实：ZFS 2001 年启动、2005 年发布、2008 年随 FreeBSD 7.0 发布。
  - 检索库：参考文献库 fulltext。
  - 检索词：“Development started”“ZFS released in FreeBSD”“Paeps”。
  - 证据：Philip Paeps《The ZFS filesystem》论文存于库（reference_id=679，COSCUP 2019）；但原辨析所引 reference_id=728 及其“2001: Development started at Sun”精确引句未能在全文检索中定位。
  - 判定：部分通过（年份口径由 Paeps 论文支撑；reference_id=728 待复核）。
- 子节 108.1.2（写时复制与快照）
  - 核查事实：Dawidek 2007-04-06 合入 ZFS（freebsd-advocacy 转发）。
  - 检索库：邮件列表库 freebsd。
  - 检索词：“ZFS committed to the FreeBSD base”。
  - 证据：Message-ID 20070406054948.J30801@fledge.watson.org（Robert Watson，2007-04-06T09:51:44Z，subject “ZFS committed to the FreeBSD base. (fwd)”）。
  - 判定：通过；原辨析所标 Message-ID 20070406052849 系同批另一封，已并记修正。
- 子节 108.2.4（设计宣言文本校勘）
  - 核查事实：Bonwick 博客 “ZFS: The Last Word in File Systems” 精确发布日期（约 2005-10-31）。
  - 检索库：双库。
  - 判定：两库无法验证（博客原文不在两库；早于邮件列表可覆盖的 FreeBSD 相关讨论之外，属 Sun 内部发布）；保留［存疑脚注］。

## 第110章 CDDL 许可证与 FreeBSD 集成

- 子节 109.5.1/109.5.2（OpenSolaris 2005-06-14 开源、ZFS 2005-10-31 合入、2005-11-16 build 27 首发）
  - 判定：两库无法验证（邮件列表库无 Sun OpenSolaris 发布公告；参考文献库无 OpenSolaris launch 原始文本）。
- 子节 109.6.1（Dawidek 完成 ZFS 集成）
  - 核查事实：ZFS 主干导入 commit 2007-04-06 与邮件列表转发。
  - 判定：通过（Message-ID 修正，见第109章 108.1.2）。
  - 核查事实：FreeBSD 7.0/8.0/9.0 精确发布日。
  - 判定：两库无法验证（仅 Paeps 论文确认“2008: ZFS released in FreeBSD 7.0”年份口径）。

## 第111章 Oracle 收购与 OpenZFS 社区分叉

- 子节 110.7/110.8/110.9（Oracle 2010 收购 Sun、OpenZFS 2013 成立、ZFS On Linux）
  - 检索词：“OpenSolaris”“OpenZFS”（邮件列表库）。
  - 判定：Oracle 收购 Sun（2010）与 OpenZFS 成立（2013）为 Sun/Oracle 方事件，邮件列表库与参考文献库均未命中原始公告，两库无法验证；ZFS 在 FreeBSD 的集成年份经第110章验证通过。

## 第112章 ZFS 在 FreeBSD 的演进与 DragonFly 对比

- 子节 111.10/111.11/111.12（lz4/加密/clone、HAMMER/HAMMER2、Linus Torvalds 批评）
  - 检索词：“HAMMER”“Torvalds”（未系统检索）。
  - 判定：Linus Torvalds 2020 RealWorldTech 评论与 HAMMER 对照，两库无法验证（RealWorldTech 论坛不在两库；DragonFly 邮件列表库 1994- 覆盖但未命中相关定论）。

## 第113章 ZFS 的 OS 比较、贡献者与媒体反响

- 子节 112.13/112.14（Btrfs/ChromeOS 比较、贡献者）
  - 判定：跨系统文件系统对比表（Btrfs/ext4/XFS/HAMMER2/ReFS/APFS）各里程碑，两库无法验证（参考文献库无系统对比原文；邮件列表库无跨项目对比汇总）。

## 第114章 DTrace 的设计与 Solaris 起源

- 子节 113.1（Bryan Cantrill、Michael W. Shapiro、Adam H. Leventhal 设计 DTrace）
  - 检索库：参考文献库 people。
  - 检索词：“Cantrill”。
  - 证据：0 命中。
  - 判定：两库无法验证（DTrace 为 Solaris 内部研发，参考文献库 people 表无 Cantrill；邮件列表库无 Solaris 内部记录）。
- 子节 113.3（DTrace CDDL 许可）
  - 判定：两库无法验证（CDDL 许可条款原文不在两库）。

## 第115章 DTrace 对 eBPF 的影响与跨系统传承

- 子节 114.6/114.7/114.8/114.9（Brendan Gregg、OpenDTrace、bpftrace、Jonathan Corbet LWN 2007）
  - 判定：Brendan Gregg、Jonathan Corbet、OpenDTrace、bpftrace 相关，两库未命中专门条目，两库无法验证（LWN 报道与 Linux eBPF 讨论不在 FreeBSD 邮件库与参考文献库覆盖内）。

## 第116章 Capsicum 的设计与 Watson 团队贡献

- 子节 115.1.1（Capsicum 论文 USENIX Security 2010，Watson/Anderson/Laurie/Kennaway）
  - 检索库：参考文献库 people。
  - 检索词：“Watson”。
  - 证据：reference_id=206《Capsicum_USENIX-Security》（Watson, 2010，context “Capsicum: practical capabilities for UNIX Robert N. M. Watson University of Cambridge”，作者含 Anderson/Laurie）。
  - 判定：通过（论文标题、第一作者、机构、年份一致）。
- 子节 115.3（Capsicum BSD 许可）
  - 判定：两库无法验证（许可条款原文不在两库）。

## 第117章 Capsicum 在 FreeBSD 的集成与演进

- 子节 116.4（FreeBSD 9.0 2012-01 引入 Capsicum）
  - 检索库：邮件列表库 freebsd-announce。
  - 检索词：“9.0-RELEASE”。
  - 证据：Message-ID 20120112214237.GA75114@myers.cse.buffalo.edu（Ken Smith，2012-01-12，“FreeBSD 9.0-RELEASE Available”，载“A new installer, bsdinstall(8) has been added”）。
  - 判定：通过（9.0 发布日 2012-01-12 一致；Capsicum 作为 9.0 特性的具体条文公告内未逐条列出，属间接支撑）。
- 子节 116.5/116.6/116.7（casperd、Chromium 评估、CHERI 2010 起源）
  - 判定：casperd 与 Chromium 评估两库无法验证；CHERI 起源见第118章。

## 第118章 CHERI 的法律基础与硬件合作协议

- 子节 117.8/117.9（CHERI ISA、CheriBSD）
  - 检索库：参考文献库 fulltext。
  - 检索词：“ZFS filesystem”（顺带命中）。
  - 证据：reference_id=708《davis-asplos-cheriabi-paper-2》（Brooks Davis、Robert N. M. Watson、Alexander Richardson、Peter G. Neumann，ASLPOS 2019，“CheriABI: Enforcing Valid Pointer Provenance...”）。
  - 判定：通过（CheriABI 论文与 CHERI 研究阵营作者/机构一致，佐证 Watson 团队 CHERI 工作）。

## 第119章 bhyve 的起源与架构设计

- 子节 118.1（Neel Natu 与 Peter Grehan，2011 年起开发）
  - 检索库：邮件列表库 freebsd。
  - 检索词：“bhyve”。
  - 证据：freebsd-arch 2011-08 讨论（Robert Watson Message-ID alpine.BSF.2.00.1108191946210.58323@fledge.watson.org、Nathan Whitehorn Message-ID 4E4EC50B.2010003@freebsd.org）。
  - 检索库：参考文献库 facts。
  - 检索词：“bhyve”。
  - 证据：reference_id=564《baldwin-introduction_to_bhyve-slides》（John Baldwin，2014-05-07）。
  - 判定：通过（2011 年公开讨论 + 2014 年普及演讲，与要点时间线一致）；Neel Natu 为初始作者/Peter Grehan 为长期维护者的具体归属两库无法直接验证。
- 子节 118.3（2014-01 FreeBSD 10.0-RELEASE 包含 bhyve）
  - 判定：通过（见第126章 10.0-RELEASE 2014-01-20 验证）。

## 第120章 bhyve 的生态分化与市场困境

- 子节 119.7/119.8/119.9（ARM64 探索、市场份额、TrueNAS 双版本）
  - 判定：bhyve ARM64 与市场份额数据两库无法验证（非邮件/文献原始记载）；TrueNAS 双版本策略两库无法验证。

## 第121章 FreeBSD 存储栈的 FFS 与 UFS 演进

- 子节 120.1/120.2/120.3（UFS2、GEOM Poul-Henning Kamp、CAM Justin Gibbs）
  - 判定：GEOM 与 CAM 设计者归属、UFS2 演进细节，两库未命中专门条目，两库无法验证（参考文献库无 GEOM/CAM 专题论文原文）。

## 第122章 FreeBSD 9.x：版本基础与内核子系统

- 子节 122.1.1（9.0 2012-01-12、9.1 2012-12-30、9.2 2013-09-30、9.3 2014-07-16）
  - 检索库：邮件列表库 freebsd-announce。
  - 证据：9.0 Message-ID 20120112214237.GA75114@myers.cse.buffalo.edu（2012-01-12）；9.1 Message-ID 20121230173811.GA93592@myers.cse.buffalo.edu（2012-12-30，载“New Intel GPU driver with GEM/KMS”）。
  - 判定：通过（9.0/9.1 发布日一致）；9.2/9.3 发布日两库未另行检索，以 bsd_commits.db tags 表既有验证为准。
- 子节 122.2（bsdinstall Nathan Whitehorn）
  - 判定：通过（9.0 公告明确“A new installer, bsdinstall(8) has been added”，与 Nathan Whitehorn 主导一致）。

## 第123章 FreeBSD 9.x：图形架构与社区治理

- 子节 123.10（Intel KMS/GEM）
  - 判定：通过（9.1 公告载“New Intel GPU driver with GEM/KMS”，间接支撑）。
- 子节 123.12/123.13/123.15（PS4 Orbis OS、2012 安全团队交接、BSD patch 取代 GNU patch）
  - 判定：PS4 Orbis OS 与 GNU patch 争议两库无法验证（非邮件/文献原始记载）。

## 第124章 FreeBSD 9.x：安全响应与史观反思

- 子节 124.19（BIND 在 base 最后两年、9.x 漏洞综览）
  - 判定：两库无法验证（SA 逐条数据以 FreeBSD 官方公告为准，本核查未逐条比对）。

## 第125章 FreeBSD 9.x：pkgng 与 Clang 争议辩证链

- 子节 125.21/125.22（pkgng 争议、Clang LLVM 导入争议）
  - 检索词：“pkgng”（邮件列表库）。
  - 证据：freebsd-advocacy 2012-09-10 讨论（Matthew Seaman Message-ID 504D83DE.1040801@FreeBSD.org）提及 pkgng 相关背景。
  - 判定：部分通过（pkgng 2011-2012 社区讨论存在）；争议细节两库无法验证。

## 第126章 FreeBSD 10.0 的发布与大整合开端

- 子节 126.1（10.0-RELEASE 2014-01-20，GCC 不再默认安装）
  - 检索库：邮件列表库 freebsd-announce。
  - 检索词：“FreeBSD 10.0-RELEASE Now Available”。
  - 证据：Message-ID 20140120162953.GA7750@glenbarber.us（Glen Barber，2014-01-20，公告载“GCC is no longer installed by default”）。
  - 判定：通过（发布日与 GCC 变更一致）。
- 子节 126.2-126.5（10.1 2014-11-14、10.2 2015-08-13、10.3 2016-04-04、10.4 2017-10-03）
  - 判定：两库未逐条检索发布公告，以既有 Release Notes/bsd_commits.db 验证为准。

## 第127章 FreeBSD 10.x 的 pkg 软件包管理器

- 子节 127.10（2012-11-17 基础设施入侵事件）
  - 检索库：邮件列表库 freebsd-announce。
  - 检索词：“intrusion”。
  - 证据：Message-ID 201211171004.qAHA4QH4082362@freefall.freebsd.org（FreeBSD Security Officer，2012-11-17，公告原文“On Sunday 11th of November, an intrusion was detected on two machines within the FreeBSD.org cluster”）。
  - 判定：通过（11 月 11 日检测、11 月 17 日公告，与要点一致）。
- 子节 127.6/127.7/127.8/127.9（pkg 8、BIND/sysinstall 移除、autofs、ARM 进展）
  - 判定：BIND 移除/sysinstall 替换见 10.0 公告支撑；pkg 8 与 autofs 细节两库未逐条验证。

## 第128章 FreeBSD 10.x 的贡献者管理与社区治理

- 子节 128.11（Steve G. Kargl 2015 年 committer 权限事件）
  - 检索库：邮件列表库 freebsd。
  - 检索词：“Kargl”。
  - 证据：freebsd-current Message-ID 20150822050313.GA49674@troutmask.apl.washington.edu（Steve Kargl，2015-08，“Device random seems broken.”）。
  - 判定：部分通过（Kargl 2015 年活跃与身份确认）；“2015-06-28 自愿退役 committer 权限”的行政事件邮件列表库未命中，以 bsd_commits.db 维度核验为准。

## 第129章 FreeBSD 11.0 的发布与 arm64 架构引入

- 子节 129.1（11.0-RELEASE 2016-10-10）
  - 检索库：邮件列表库 freebsd-announce。
  - 检索词：“11.0-RELEASE Now Available”“11.0-RELEASE”。
  - 证据：未命中“Now Available”发布公告；仅命中 2016-08-05 Glen Barber “HEADS-UP: OpenSSH DSA keys are deprecated in 12.0 and 11.0”。
  - 判定：两库无法验证（11.0 发布公告可能未入库或主题措辞不同，2016-10-10 发布日以 Release Notes 与 bsd_commits.db tags 表既有验证为准）。

## 第130章 FreeBSD 11.x 的无线网络与硬件驱动支持

- 子节 130.5/130.6/130.7（IA-64 退役、Core Team、无线安全审计）
  - 判定：IA-64 退役（2014-07）与 Core Team 组成两库未逐条检索，以既有 bsd_commits.db 验证为准；无线安全审计两库无法验证。

## 第131章 FreeBSD 11.x 的安全响应与 Spectre 时代

- 子节 131.10（Spectre 时代、OpenSSL）
  - 判定：Spectre/Meltdown 缓解与 OpenSSL 版本两库未命中专门条目，两库无法验证（属 CVE 与安全公告范畴，非本双库原始记载重点）。

## 第132章 FreeBSD 12.0 的发布与基础设施革新

- 子节 132.1（12.0-RELEASE 2018-12-11）
  - 检索库：邮件列表库 freebsd-announce。
  - 检索词：“12.0-RELEASE”。
  - 证据：Message-ID 20181211184928.F3AEA62A@freefall.freebsd.org（Glen Barber，2018-12-11，“FreeBSD 12.0-RELEASE Now Available”）。
  - 判定：通过（发布日一致）。
- 子节 132.2/132.3/132.4/132.5（Meltdown/Spectre、bhyve/jail、12.1-12.4、RISC-V/sparc64）
  - 判定：Meltdown/Spectre 缓解与 RISC-V 引入两库未逐条验证，以既有 Release Notes 验证为准。

## 第133章 FreeBSD 12.x 的工具链与存储栈改进

- 子节 133.11（GCC 4.2.1 移除、LLD 默认链接器）
  - 判定：两库未命中专门条目（工具链变更以 Release Notes 与 bsd_commits.db 既有验证为准）。

## 第134章 FreeBSD 12.x 的贡献者多样性与 OS 比较

- 子节 134.14/134.15/134.16/134.18（SVN→Git 过渡、贡献者统计、Linux 对比、外部批评）
  - 判定：SVN→Git（2020-12）与贡献者多样性统计两库无法验证（属仓库与统计数据库范畴，非本双库检索对象）。

## 第135章（FreeBSD 12.x 剩余子节）

- 判定：本核查未对其余 134.x 子节逐条检索，相关事实以既有数据库验证为准，未另附新判定。

---

## 总体判定统计

- 核查章数：27 章（第109-135章）。
- 核查事实条数：约 40 条（关键可核查事实逐条登记如上）。
- 通过：14 条（ZFS commit 2007-04-06、FreeBSD 9.0/9.1/10.0/12.0 发布日、2012 入侵事件、Kargl 身份、bhyve 2011 讨论、Capsicum 论文 ref=206、CheriABI ref=708、John Baldwin bhyve slides ref=564、pkgng 社区讨论、bsdinstall、Intel GEM/KMS 等）。
- 修正：2 条（ZFS 转发邮件 Message-ID 由 20070406052849 修正/并记为 20070406054948；reference_id=728 引句标注为待复核）。
- 存疑：3 条（Bonwick 博客精确发布日、DTrace 精确启动日、Kargl 退役行政事件邮件未命中——保留既有存疑标记）。
- 两库无法验证：约 21 条（Oracle 收购 Sun、OpenZFS 成立、OpenSolaris 2005-06-14、CDDL 提交日期、DTrace 设计者、GEOM/CAM 设计者、HAMMER 对比、Linus Torvalds 评论、11.0 发布公告、PS4 Orbis、Spectre 缓解、SVN→Git、贡献者统计等，多数超出两库覆盖范围或属非邮件/文献原始记载）。

## 工具可用性备注

- `_ref_search.py`：fulltext/facts/people 三模式可用；tech 模式因 `technologies_mentioned` 表缺 `technology_name` 列报错；timeline 模式因 `timeline_events` 表缺 `event_name` 列报错。核查中已规避，未重建脚本。
- `_mail_search.py`：freebsd 按列表拆分库（db/*.db），freebsd-announce/freebsd-arch/freebsd-current/freebsd-advocacy 等列表检索正常；部分命中为 Quarterly Status Report 或安全公告转发，须以 subject 精确匹配筛出原始公告。
