---
chapter: 第 190 章
id: CH190
volume: 第09卷-netbsd的历史
---

# 第 190 章 netbsd-10-0的os比较与社区演进

## 要点

- 2010-2026 年间市场份额数据——Linux 服务器市场占有率约 70%-80%（云时代主导），FreeBSD 约 1%-2%，NetBSD 不足 0.1%，OpenBSD 不足 0.1%；BSD 整体在云时代被 Linux 进一步挤压
- NetBSD 10.x 周期（**2023 年 4 月 1 日** 至 **2026 年 7 月 22 日**，覆盖 10.0 发布前后主流与稳定分支维护期）共发布 **仅 2 个 NetBSD-SA**——**NetBSD-SA2024-001**（**utmp_update(8)** 用户主机名验证不足）与 **NetBSD-SA2024-002**（OpenSSH CVE-2024-6387
- NetBSD 10.x 周期安全响应文化呈现三个根本性转变：① **SA 发布近乎停滞**——10.x 周期仅 2 个 SA（2024 年发布），2025-2026 两年零 SA，与 9.x 周期 5 年 18 个 SA（年化 3.6 SA/年）形成断崖式下降，与 FreeBSD 14.x 周期不足 3 年 80 个 SA（年化约 30 SA/年）形成两极对照——SA 发布停滞反映 NetBSD
- pkgsrc-2026Q2 分支于 **2026 年 6 月 24 日** 由 maya（<maya@NetBSD.org>，即 Maya Rashbox，pkgsrc PMC 成员）在 netbsd-announce 邮件列表公告（邮件主题"Announcing the pkgsrc-2026Q2 branch"，UTC 时间 22:25）；pkgsrc 季度分支遵循惯例——每季度末 branc

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3756] 卷“第10卷-openbsd的历史”第 190 章，匹配置信度 folder，原因：folder 第188章
- [DB:references_fulltext:chapter_matches:chmatch_3896] 卷“第10卷-openbsd的历史”第 190 章，匹配置信度 folder，原因：folder 第188章
- [DB:references_fulltext:chapter_matches:chmatch_4025] 卷“第10卷-openbsd的历史”第 190 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NetBSD 服务器市场份额“不足 0.1%”在不同调查中差异较大——需对照多源核验；BSD 在嵌入式市场的部署未被服务器市场报告统计
- *需严格区分**：① “SA 发布停滞”不等于“安全维护停滞”——10.x 周期 97 条 CVE commit 与 6 条 Security fix commit 证明安全维护仍在持续，但维护方式从“SA+ 二进制补丁”转向"vendor import commit"；② **2 个 SA 的归属辨析**——SA2024-001 针对 NetBSD 自有代码 **utmp_update(8)**
- *SA 锐减的归因辨析**：10.x 周期 SA 从 9.x 周期年化 3.6 SA/年降至 0.67 SA/年（2 SA / 3 年），降幅 81%——这一降幅的可能归因有三：其一，10.x 周期 base 中贡献组件 CVE 由 vendor import 同步修复，Security Officer Team 将其视为“上游修复”而非“NetBSD SA 范畴”，故不发布 SA；其二，10.x
- 经考据记录 20260723_announcements-netbsd.md § 交叉验证方法-四 -2 验证：pkgsrc-2026Q2 公告日期 2026-06-24 与 pkgsrc 季度分支惯例（每季度末 branching）一致，邮件列表自动归档保证时间戳不可篡改；maya（Maya Rashbox）作为 pkgsrc PMC 成员的身份经 NetBSD Foundation 主页（**

## 文献

- Netcraft Web Server Survey 2010-2026；IDC 服务器操作系统市场报告；StatCounter 统计[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2026 年间：831,293 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2024-2026)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>; NetBSD Project. NetBSD 10.0 Release Notes — Security Section [EB/OL]. (2024-03-28)[2026-07-22]. <https://www.netbsd.org/releases/formal-10/NetBSD-10.0.html>; NetBSD Project. NetBSD 9.0 Release Notes — kernel ASLR [EB/OL]. (2020-02-14)[2026-07-22]. <https://www.netbsd.org/releases/formal-9/NetBSD-9.0.html>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2023-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; NetBSD Project. netbsd.db — netbsd-src ASLR/VERIEXEC/kauth/NPF commits [DB/OL]. 2026-07-22. SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name ='netbsd-src' AND author_date >='2023-04-01' AND author_date <‘2026-07-22’ AND (message_subject LIKE '%ASLR%’ OR message_subject LIKE '%kaslr%’ OR message_subject LIKE '%veriexec%’ OR message_subject LIKE '%kauth%’ OR message_subject LIKE '%npf%’) ORDER BY author_date ASC; NetBSD Project. veriexec(4) Manual Page[EB/OL]. [2026-07-22]. <https://man.netbsd.org/veriexec.4>; NetBSD Project. kauth(9) Manual Page [EB/OL]. [2026-07-22]. <https://man.netbsd.org/kauth.9>; NetBSD Project. npf(7) Manual Page [EB/OL]. [2026-07-22]. <https://man.netbsd.org/npf.7> ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
- maya (Maya Rashbox). Announcing the pkgsrc-2026Q2 branch [EB/OL]. (2026-06-24)[2026-07-23]. <https://mail-index.netbsd.org/netbsd-announce/2026/06/24/msg000399.html>; NetBSD Project. netbsd-announce 2026/06 月存档 [EB/OL]. (2026-07-23 访问). <https://mail-index.netbsd.org/netbsd-announce/2026/06/date1.html>; NetBSD Foundation. Foundation 主页 [EB/OL]. (2026-07-23 访问). <https://www.netbsd.org/foundation/>; 考据记录 20260723_announcements-netbsd.md §A.3、§ 交叉验证方法-四 -2、§ 存疑判定依据-一 -8 ［A］<!-- DB_REF:netbsd.duckdb -->> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2024-2024 年间：29,047 次提交。> 仓库总览：1,999,412 次提交，4,754 位贡献者，1992-07-13 至 2026-08-24。
