---
chapter: 第 173 章
id: CH173
volume: 第09卷-netbsd的历史
---

# 第 173 章 netbsd-1x的成熟期与pkgsrc引入

## 要点

- NetBSD 自 1.0（**1994-10-26**）起从 4.4BSD-Lite2 继承 **audio(4)** 通用音频驱动框架——其核心机制是提供设备无关的音频接口，硬件驱动通过 audio(9) 接口注册，用户态通过 /dev/audio 与 /dev/sound 设备访问。man page 见 **man.netbsd.org/audio.4**。NetBSD audio(4) 与
- NetBSD Foundation 于 1995 年在特拉华州注册成立（chartered），现行确为 501(c)(3)；但注册年份与免税资格获准年份应区分——官方发布仅称 ‘chartered in 1995’，501(c)(3) 具体获准年份一手页未列（第三方资料有 2004 年之说）。注册过程包括起草 By-Laws、申请 IRS 501(c)(3) 免税地位[考据完成：2026-08-0
- 2003 年是 NetBSD 项目第 10 周年——NetBSD Foundation 2003 年报明确称"the tenth anniversary year of the NetBSD Project"，与 NetBSD About 页面"NetBSD was originally released in 1993"及 formal.html 列出 NetBSD 0.8（1993-04-20
- 2026-08-06 将 NetBSD developers.html（committer 权限管理官方页面，103KB）与 core.html（Core Group 现任 7 人 + 历任 22 人名单）下载归档至 `03-原始史料库/11-邮件列表史料/02-netbsd/governance/`——为本节“committer 权限记录”与“18 个月不活跃自动退休”考据提供官方一手档案；de
- 贡献者 commit 记录与邮件考据——NetBSD CVS commit 日志与邮件列表讨论是研究贡献者结构的一手史料；考据需对照多源档案交叉验证

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3991] 卷“第09卷-netbsd的历史”第 173 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NetBSD audio(4) 与 FreeBSD audio(4) 在 4.4BSD-Lite2 前完全同源；与 Linux ALSA 的关键差异——ALSA 提供更丰富的 API（含 MIDI、混音器、PCM 等），audio(4) 仅提供基本音频接口；macOS CoreAudio 是 Apple 自研框架，与 BSD/Linux 音频栈无源码关系。
- 注册过程的具体时间需考据——1995.2 注册的具体日期需对照特拉华州记录核实
- 经考据记录 20260723_announcements-netbsd.md § 存疑判定依据-一 -7 验证：项目起始年份 1993 经三向印证——About 页面"NetBSD was originally released in 1993"、formal.html 列出 NetBSD 0.8（1993-04-20）、2003 年报称"the tenth anniversary year of
- developers.html 为 2026-08-06 时点快照，反映现行 committer 治理（与 1994-2004 时期规则有差异，如历史无“6 个月活跃”硬性要求）；core.html 历任名单含 de Raadt（1993-1995 任 Core），与 172.3 节考据一致；权限撤销的具体历史决议仍以 172.3 节既有考据与邮件档案为准，本节登记仅作现行规则补充
- 贡献者结构的具体情况需考据——部分贡献者可能未被完整记录；需对照多源档案核实

## 文献

- NetBSD Project. *NetBSD 1.0 Release Notes*[EB/OL]. (1994-10-26). <https://www.netbsd.org/releases/formal-1.0.html>; NetBSD Project. *audio(4) Manual Page*[EB/OL]. <https://man.netbsd.org/audio.4>; McKusick, M. K. et al. (1996). *The Design and Implementation of the 4.4BSD Operating System*. Addison-Wesley. Chapter 10.<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1999-2002 年间：295,239 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Foundation. 2003 年报 [EB/OL]. (2004-02-07)[2026-07-23]. <https://www.netbsd.org/foundation/reports/2003.html>; NetBSD Project. About 页面 [EB/OL]. (2026-07-23 访问). <https://www.netbsd.org/about/>; NetBSD Project. formal.html 历史页面 [EB/OL]. (2026-07-23 访问). <https://www.netbsd.org/releases/formal.html>; 考据记录 20260723_announcements-netbsd.md §A.4、§ 存疑判定依据-一 -7 ［A］    FreeBSD 社区论文与演讲 [287]，[287] Michael Dexter, Chuck Tuffli. smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)[C]//EuroBSDcon 2021. [S.l.]: [s.n.], 2021. 获取路径：<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [245]，[245] Michael Dexter. By the numbers: ZFS Performance Results from Six Operating Systems and Their Derivatives [C]//vBSDcon 2019. [S.l.]: [s.n.], 2019. 获取路径：<https://papers.freebsd.org/2019/vbsdcon/dexter-zfs_performance_results/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [235]，[235] Thomas Barabosch. KLEAK - Practical Kernel Memory Disclosure Detection [C]//FOSDEM 2019. [S.l.]: [s.n.], 2019. 获取路径：<https://papers.freebsd.org/2019/fosdem/barabosch-kleak/> [访问日期 2026-07-26].    FreeBSD 社区论文与演讲 [251]，[251] Allan Jude. OpenZFS: Best Filesystem for every OS [C]//独立发布 2019. [S.l.]: [s.n.], 2019. 获取路径：<https://papers.freebsd.org/2019/jude-openzfs-everyos/> [访问日期 2026-07-26].<!-- foundation-writeback: NetBSD Foundation | NetBSD Foundation 决议文件（2003-2017） -->**NetBSD Foundation 史料**（NetBSD Foundation 决议文件（2003-2017），下载日期 2026-07-26）：
- NetBSD Project. Developers' Guide [EB/OL]. (2026-08-06 归档). governance/developers.html; NetBSD Project. Core Team 名单 [EB/OL]. (2026-08-06 归档). governance/core.html; 考据记录 20260806_netbsd_core_史料采集.md ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1994-2004 年间：623,504 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 贡献者史料分析[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
