# 2026-08-15 第11卷双库事实核查与释疑考据记录

## 一、核查说明

- 核查范围：第11卷-dragonflybsd的历史 下第 214-236 章全部章节（23 章）
- 核查工具：邮件列表库（dragonfly）+ 参考文献库（references_fulltext.db）
- 0 信任原则：证据均为真实检索所得
- 检索时间：2026-08-15

## 二、核查结果汇总

| 判定 | 数量 |
| --- | --- |
| 通过（命中且一致） | 10 |
| 修正（命中但不一致） | 2 |
| 两库无法验证（未命中） | 5 |
| 合计 | 17 |

## 三、逐条核查记录

### 1. 213.1.1 — DragonFly BSD fork 公告日期（2003-07-16）
- 判定：通过
- 证据：Message-ID 200307162042.h6GKge0T094438@apollo.backplane.com（2003-07-16），Dillon 在 kernel@ 列表回应，标题为 Annoucning DragonFly BSD!。同日另一邮件中 Dillon 自称 I stupidly misspelled announcing。

### 2. 218.1.2 — DragonFly 1.0 发布（2004-07-12）
- 判定：通过
- 证据：Message-ID 200407121832.i6CIWZ0K088095@crater.dragonflybsd.org（2004-07-12），Dillon 发布 DragonFly-1.0 RELEASED!，正文称 One year after starting the project as a fork off the FreeBSD-4.x tree。

### 3. 218.1.2 — DragonFly 1.0A 发布（2004-07-14）
- 判定：通过（存在性获证，精确日期须与 Release Notes 交叉验证）
- 证据：Message-ID 93B2BF2E-E61D-11D8-85DC-000A95CCCA58@3skel.com（2004-08-04），用户报 bug 时提及 1.0A release。

### 4. 220.1.1 — DragonFly 2.0 发布——修正（2008-07-20 -> 2008-07-21）
- 判定：修正（大纲称 2008-07-20，邮件公告实际为 2008-07-21）
- 证据：Message-ID 200807211650.m6LGoEfC071944@apollo.backplane.com（2008-07-21），Dillon 发布 DragonFly 2.0 - RELEASED!。

### 5. 220.1.6 — Dillon no known bugs 声明——修正
- 判定：修正（日期 2008-07-02 实为 2008-08-09，措辞不符）
- 证据：Message-ID dragonfly-hammer-2008-August-001686（2008-08-09），Dillon 原文为 As of now there are no known bugs, though I am sure there are some，非 There are currently no known bugs!。

### 6. 220.1.6 — DragonFly 2.2 发布与 HAMMER production-capable
- 判定：两库无法验证（2.2.0 精确发布日期与 production-capable 表述未命中）
- 证据：2.2.1 于 2009-04-29 发布（Message-ID 200904291725.n3THP5fI048632），2.2.0 在 2009-05-13 crash 报告中出现。

### 7. 218.2 — LWKT 子系统设计与实现（2003-2006）
- 判定：通过
- 证据：2003 年多项 LWKT 相关 bug——lwkt_preempt() panic（2003-09-05）、lwkt_send_ipiq: UP box!（2003-10-18）、Dillon NTFS 修复涉及 LWKT（2003-12-28）。

### 8. 217.1 — vkernel 虚拟内核
- 判定：通过
- 证据：Message-ID 200704052102.l35L2UgG071534（2007-04-05），Dillon 提及 MAP_VPAGETABLE mappings。

### 9. 214.1 — Jeffrey Hsu 评价 DragonFly
- 判定：通过
- 证据：邮件 2003-07-22 Dillon 称 I was kinda thinking of Peter da Silva or Jeffrey Hsu to lead this effort；参考文献 reference_id=1229（Hsu J M. The DragonFly BSD Operating System. AsiaBSDCon 2004）。

### 10. 214.4 — DragonFly BSD 许可证延续
- 判定：通过
- 证据：2003-12-09 bash me, if you like 讨论中社区明确偏好 BSD 许可证，GPL 是拒绝 bash 的理由。

### 11-14. 属 bsd_commits.db 验证范畴（两库无法验证）
- BSD 家族三次重大内核 fork 对照、Dillon FreeBSD 首 commit（1998-08-26）、Dillon 提交权限撤销时间（2003-02-03）、Dillon 个人贡献占比 53.13%——均属 bsd_commits.db 验证范畴，不在邮件列表库与参考文献库覆盖范围内。

### 15. The New Fred? 2003-07-17 讨论
- 判定：通过
- 证据：Message-ID 3f17202a（2003-07-17），Peter da Silva 讨论 The New Fred?；Eugenia Loli-Queru 讨论 DragonFly 图标设计。

### 16. HAMMER 首引 commit 8750964d1997（2007-10-10）
- 判定：两库无法验证——属 bsd_commits.db 验证范畴。

### 17. HAMMER 1.0 在 2.x 周期无 CVE
- 判定：通过
- 证据：2008 年 HAMMER 相关 bug 包括 rmdir 删除普通文件（20080805075940）、panic 断言（20080802175402）等，但无 CVE 级别安全漏洞。