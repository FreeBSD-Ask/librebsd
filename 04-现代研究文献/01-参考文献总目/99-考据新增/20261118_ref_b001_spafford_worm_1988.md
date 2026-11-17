# ref-spafford-worm-1988 登记卡（V61 b001 新登记：Spafford《The Internet Worm Program: An Analysis》）

- **来源**：Spafford E H. The Internet Worm Program: An Analysis[R/OL]. West Lafayette: Department of Computer Sciences, Purdue University, 1988（Purdue Technical Report CSD-TR-823，1988-11-29 发布、1988-12-08 修订；另刊 ACM SIGCOMM CCR 19(1), 1989）[2026-11-18]. https://cisre.egr.uh.edu/wp-content/uploads/2023/09/spaf-iworm-paper-ccr.pdf.
- **性质**：1988 年互联网蠕虫事件的权威第三方技术分析（基于两份独立反编译与一份 VAX 反汇编，详述 fingerd／sendmail 漏洞、rsh 感染路径与口令攻击面），非当事人学术文献（academic_work 类）。
- **取文途径**：UH 镜像 PDF 本机直连失败，经 exa 通道取该 PDF 正文（2026-11-18，30,000 字符上限，覆盖摘要、§3 漏洞、§4 感染流程前段）。**抽取伪影披露**：exa 抽文存在行末断词空格（如“indepen dent”“adminis trators”），引文池照录原抽文；块内引文只取无伪影连续段。
- **四键查重**：source_url（cisre.egr.uh.edu/wp-content/uploads/2023/09/spaf-iworm-paper-ccr.pdf，库内无命中）；题名＋首作者＋年份（The Internet Worm Program: An Analysis＋Spafford＋1988，库内无命中）——新登记。
- **tier 依据**：academic_work／source_tier=secondary_authoritative；块内 claim 取 L3（公开文献记载，非当事人直接证词）。
- **用途**：V61 b001（1.1.4 受信主机免口令的信任假设）。

## 逐字引文池（供本批取用，均取自上述 PDF 镜像正文；断词伪影照录）

1. [1.1.4 用，自 The infection attempts 起句以避序号 8)] The infection attempts proceeded by one of three routes: rsh, fingerd, or sendmail. 8a) The attack via rsh was done by attempting to spawn a remote shell by invocation of (in order of trial) /usr/ucb/rsh, /usr/bin/rsh, and /bin/rsh. If successful, the host was infected as in steps 1 and 2a, above.

2. [口令面备用（后续批），照录] A key attack of the Worm program involved attempts to discover user passwords.

3. [口令面备用（后续批），照录] This allows an attacker to encrypt lists of possible passwords and then compare them against the actual passwords without passing through any system function.

4. [摘要照录（卡内语境）] On the evening of 2 November 1988, someone infected the Internet with a worm program. That program exploited flaws in utility programs in systems based on BSD-derived versions of UNIX. The flaws allowed the program to break into those machines and copy itself, thus infecting those systems.
