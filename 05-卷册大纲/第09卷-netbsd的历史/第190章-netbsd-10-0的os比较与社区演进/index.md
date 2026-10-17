---
chapter: 第 190 章
id: CH190
volume: 第09卷-netbsd的历史
---

# 第 190 章 netbsd-10-0的os比较与社区演进

## 要点

- 2010-2026 年间市场份额数据——Linux 服务器市场占有率约 70%-80%（云时代主导），FreeBSD 约 1%-2%，NetBSD 不足 0.1%，OpenBSD 不足 0.1%；BSD 整体在云时代被 Linux 进一步挤压
- NetBSD 10.x 周期（**2023 年 4 月 1 日** 至 **2026 年 7 月 22 日**，覆盖 10.0 发布前后主流与稳定分支维护期）共发布 **仅 2 个 NetBSD-SA**——**NetBSD-SA2024-001**（**utmp_update(8)** 用户主机名验证不足）与 **NetBSD-SA2024-002**（OpenSSH CVE-2024-6387 “regreSSHion”——sshd 信号处理竞态条件，未认证远程攻击者可触发远程代码执行或拒绝服务）
- NetBSD 10.x 周期安全响应文化呈现三个根本性转变：① **SA 发布近乎停滞**——10.x 周期仅 2 个 SA（2024 年发布），2025-2026 两年零 SA，与 9.x 周期 5 年 18 个 SA（年化 3.6 SA/年）形成断崖式下降，与 FreeBSD 14.x 周期不足 3 年 80 个 SA（年化约 30 SA/年）形成两极对照——SA 发布停滞反映 NetBSD 安全维护方式的结构性转变——从“SA+ 二进制补丁”转向“vendor import commit”，而非安全维护的终止
- pkgsrc-2026Q2 分支于 **2026 年 6 月 24 日** 由 maya（<maya@NetBSD.org>，即 Maya Rashbox，pkgsrc PMC 成员）在 netbsd-announce 邮件列表公告（邮件主题“Announcing the pkgsrc-2026Q2 branch”，UTC 时间 22:25）；pkgsrc 季度分支遵循惯例——每季度末从 HEAD 切出 pkgsrc-YYYYQn 稳定分支（Q1-Q4 对应 3、6、9、12 月末），切出后进入该分支的稳定维护期

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3756] 卷“第10卷-openbsd的历史”第 190 章，匹配置信度 folder，原因：folder 第188章〔存疑：经 2026-09-12 实查 chapter_matches 表，id=3756 行 primary_volume 确为“第10卷-openbsd的历史”、match_confidence 字段值为 folder，系库侧 auto_keyword 匹配错挂，须库侧修复，非本文件可改〕
- [DB:references_fulltext:chapter_matches:chmatch_3896] 卷“第10卷-openbsd的历史”第 190 章，匹配置信度 folder，原因：folder 第188章〔存疑：经 2026-09-12 实查 chapter_matches 表，id=3896 行 primary_volume 确为“第10卷-openbsd的历史”、match_confidence 字段值为 folder，系库侧 auto_keyword 匹配错挂，须库侧修复，非本文件可改〕
- [DB:references_fulltext:chapter_matches:chmatch_4025] 卷“第10卷-openbsd的历史”第 190 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集〔存疑：经 2026-09-12 实查 references_fulltext.duckdb chapter_matches 表，id=4025 行 primary_volume 确为“第10卷-openbsd的历史”（task4_official 来源），系库侧匹配错挂——本章属第09卷 netbsd 第 190 章，须库侧修复，非本文件可改〕

## 史观

- 总纲第 3 条——不存在进步，只有权力再分配：2010-2026 年 BSD 与 Linux 在服务器市场的份额消长系云计算时代资源与注意力的再分配，并非进步序列上的先进与落后之别
- 总纲第 9 条——经验优先：10.x 周期安全维护的实际状态须以 SA 原文、CVE commit 与 netbsd-announce 公告等一手记录为准——SA 发布近乎停滞不等于安全维护停滞，维护方式已转向 vendor import commit

## 辨析

- NetBSD 服务器市场份额“不足 0.1%”在不同调查中差异较大——需对照多源核验；BSD 在嵌入式市场的部署未被服务器市场报告统计
- **需严格区分**：① “SA 发布停滞”不等于“安全维护停滞”——10.x 周期 97 条 CVE commit 与 6 条 Security fix commit 证明安全维护仍在持续，但维护方式从“SA+ 二进制补丁”转向“vendor import commit”；② **2 个 SA 的归属辨析**——SA2024-001 针对 NetBSD 自有代码 **utmp_update(8)**
- **SA 锐减的归因辨析**：10.x 周期 SA 从 9.x 周期年化 3.6 SA/年降至 0.67 SA/年（2 SA / 3 年），降幅 81%——这一降幅的可能归因有三：其一，10.x 周期 base 中贡献组件 CVE 由 vendor import 同步修复，Security Officer Team 将其视为“上游修复”而非“NetBSD SA 范畴”，故不发布 SA；其二，10.x
- **文献**：NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2024-2026)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>（完整列表共 269 条 SA，时间跨度 2000 年至 2024-07-01，2025-2026 年无新 SA）; NetBSD Project. NetBSD-SA2024-001 PGP 签名原文 [EB/OL]. (2024-03-10)[2026-07-23]. <https://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2024-001.txt.asc>（Revision History“2024-03-10 Initial release”；致谢 Adam Simuntis 发现并报告，Christos Zoulas（克里斯托斯·祖拉斯） 修复）; NetBSD Project. NetBSD-SA2024-002 PGP 签名原文 [EB/OL]. (2024-07-01)[2026-07-23]. <https://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2024-002.txt.asc>（Revision History“2024-07-01 Initial release”；文件版本 $NetBSD: NetBSD-SA2024-002.txt,v 1.4 2024/07/02 19:26:35 riastradh Exp $，含 riastradh 即 Taylor R. Campbell 署名）; NetBSD Project. netbsd.duckdb — netbsd-src commits table [DB/OL]. 2026-07-22. SQL: SELECT commit_hash, author_date, author_name, message_subject, message_body FROM commits WHERE repo_name =‘netbsd-src’ AND author_date >=‘2023-04-01’ AND author_date <‘2026-07-22’ AND (message_subject LIKE ‘%CVE-%’ OR message_body LIKE ’%CVE-%’) ORDER BY author_date ASC; NetBSD Project. 版本周期文件 netbsd-10.x.md [Z]. 2026-07-22; 考据记录 20260723_announcements-netbsd.md §A.2、§ 交叉验证方法-二、§ 存疑判定依据-一 -3/4/5 ［A］

## 文献

- Netcraft Web Server Survey 2010-2026；IDC 服务器操作系统市场报告；StatCounter 统计［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2026 年间：831,293 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2024-2026)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>; NetBSD Project. NetBSD 10.0 Release Notes — Security Section [EB/OL]. (2024-03-28)[2026-07-22]. <https://www.netbsd.org/releases/formal-10/NetBSD-10.0.html>; NetBSD Project. NetBSD 9.0 Release Notes — kernel ASLR [EB/OL]. (2020-02-14)[2026-07-22]. <https://www.netbsd.org/releases/formal-9/NetBSD-9.0.html>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2023-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; NetBSD Project. netbsd.duckdb — netbsd-src ASLR/VERIEXEC/kauth/NPF commits [DB/OL]. 2026-07-22. SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name =‘netbsd-src’ AND author_date >=‘2023-04-01’ AND author_date <‘2026-07-22’ AND (message_subject LIKE ‘%ASLR%’ OR message_subject LIKE ’%kaslr%’ OR message_subject LIKE ‘%veriexec%’ OR message_subject LIKE ’%kauth%’ OR message_subject LIKE '%npf%’) ORDER BY author_date ASC; NetBSD Project. veriexec(4) Manual Page[EB/OL]. [2026-07-22]. <https://man.netbsd.org/veriexec.4>; NetBSD Project. kauth(9) Manual Page [EB/OL]. [2026-07-22]. <https://man.netbsd.org/kauth.9>; NetBSD Project. npf(7) Manual Page [EB/OL]. [2026-07-22]. <https://man.netbsd.org/npf.7> ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- maya (Maya Rashbox). Announcing the pkgsrc-2026Q2 branch [EB/OL]. (2026-06-24)[2026-07-23]. <https://mail-index.netbsd.org/netbsd-announce/2026/06/24/msg000399.html>; NetBSD Project. netbsd-announce 2026/06 月存档 [EB/OL]. (2026-07-23 访问). <https://mail-index.netbsd.org/netbsd-announce/2026/06/date1.html>; NetBSD Foundation. Foundation 主页 [EB/OL]. (2026-07-23 访问). <https://www.netbsd.org/foundation/>; 考据记录 20260723_announcements-netbsd.md §A.3、§ 交叉验证方法-四 -2、§ 存疑判定依据-一 -8 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2024-2024 年间：29,047 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP626（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD Journal 2025 夏季刊以网络为主题，收录 Tom Jones 的 Wi-Fi 开发入门、Randall Stewart 与 Michael Tüxen 的 TCP 静态 pacing 以及 Christopher R. Bowman 的嵌入式 FreeBSD 等文章。（BSD Now EP626，[141.82-762.54]，L2）
- FreeBSD Foundation 的《Java hiding in plain sight》指出 OpenJDK 仍是 Elasticsearch、Tomcat、LibreOffice 与 Minecraft 等系统的基础，维护者的工作使 FreeBSD 上的 OpenJDK 保持最新。（BSD Now EP626，[762.54-946.78]，L2）
- Chuck Tuffley 的 BSDCan 2025 报告记录基金会社区调查与笔记本支持、Core 团队章程修订、AI 政策讨论以及 Verisign 与 NVIDIA 的产业报告。（BSD Now EP626，[948.80-1427.06]，L1）
- OpenBSD 7.8 征集 USB 摄像头测试，开发者 Kirill 为 uvideo 增加 H.264 流支持并优化 CPU 占用以支持 4K 60fps 原始流。（BSD Now EP626，[1437.62-1538.58]，L2）
- OpenSSH 新增 refuse connection 配置指令与 PKCS#11 ED25519 密钥支持，由 Damien Miller 提交。（BSD Now EP626，[1541.90-1621.92]，L2）
- NetBSD 11 分支进入发布流程，包括 32 位兼容集拆分、CD 安装镜像、x86 PVH 启动支持、RISC-V 新端口与工具链更新。（BSD Now EP626，[1636.36-1806.82]，L2）
- Nico Cartron 自述 2000 年在巴黎计算机学校初识 NetBSD 机房，后以 FreeBSD 为主，日常通过 WireGuard 与 SSH 使用家中的 FreeBSD 笔记本。（BSD Now EP626，[1950.18-2571.94]，L1）

**史料**：

- FreeBSD Journal 2025 年夏季刊及其收录文章。（BSD Now EP626，[141.82-762.54]，L2）
- Mark Phillips 撰写的 FreeBSD Foundation 博客 Java hiding in plain sight。（BSD Now EP626，[762.54-946.78]，L2）
- Chuck Tuffley 的 BSDCan 2025 Trip Report。（BSD Now EP626，[948.80-1427.06]，L1）
- Undeadly.org 的 USB webcam 测试征集与 OpenSSH 新特性报道。（BSD Now EP626，[1437.62-1621.92]，L2）
- Martin Husemann 的 NetBSD 11 release process 博客。（BSD Now EP626，[1636.36-1806.82]，L2）
- Nico Cartron 访谈。（BSD Now EP626，[1950.18-3345.10]，L1）

**史观**：

- 总纲10 动手者创造历史：总纲10 动手者创造历史：Chuck Tuffley 报告中 Google Summer of Code 学生与 Kyle Evans 接力推进 squashfs 驱动，体现未完成工作由后来者接续。（BSD Now EP626，[1232.26-1271.62]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：NetBSD 11 将 32 位兼容、CD 安装集等旧有默认拆分为可选集，反映旧硬件假设随时代过时。（BSD Now EP626，[1647.40-1682.94]，L2）
- 总纲20 历史地理塑造思想土壤：总纲20 历史地理塑造思想土壤：Nico Cartron 的法国计算机学校以 NetBSD 教学机房塑造其 BSD 使用路径，体现机构地理对技术选择的塑造。（BSD Now EP626，[1973.62-2103.06]，L1）

**辨析**：

- 转录将 Martin Husemann 记作 Martin Hussman，且节目开场将 NetBSD 11 与 FreeBSD 11 混写，须以 NetBSD 官方博客核验。 [存疑脚注] 人名与版本号存在转写歧义，未与 NetBSD 官方公告核验（BSD Now EP626，[1636.36-1806.82]，L4）
- OpenJDK 维护者姓名在转录中作 Harold 或 Harald，具体拼写须以 FreeBSD Foundation 原文核验。 [存疑脚注] 维护者姓名存在转写歧义（BSD Now EP626，[867.98-873.02]，L4）

**文献**：

- [BSD Now EP626] Pennington J. BSD Now: 626: USB webcam testing[EB/OL]. (2025-08-28)[2026-08-15]. <https://www.bsdnow.tv/626>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- CERT. /CC. Vulnerability Note VU#962459: TCP Resource Exhaustion (SegmentSmack)[EB/OL]. (2018-08)[2026-07-22]. <https://www.kb.cert.org/vuls/id/962459>[EB/OL]. 2018. 〔已核：2026-09-12 联网核实 kb.cert.org/vuls/id/962459 确为 TCP implementations vulnerable to Denial of Service（CVE-2018-5390 SegmentSmack、CVE-2018-6922 FreeBSD 端），文献真实有效，移除“待核·needs_fix”占位标记〕［DKC-2454→fulltext:6192］
<!-- /dangan-20260908 -->
