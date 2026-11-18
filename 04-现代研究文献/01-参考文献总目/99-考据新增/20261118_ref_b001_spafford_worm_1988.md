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

## b002 追加引文池（2026-11-18 V61 b002 取用，同源异句异锚）

5. [1.2.1 用，止于 spread quickly 以避后句 adminis-trators 断词] Although the program would only infect Sun Microsystems Sun 3 systems, and VAX computers running variants of 4 BSD UNIX, the program spread quickly

6. [1.2.2 用] The sendmail program is of immense importance on most Berkeley-derived (and other) UNIX systems because it handles the complex tasks of mail routing and delivery.

7. [1.2.3 用] One way to deal with the general problem is have every daemon and subsystem run with a separate userid. That way, the command and data files for each subsystem could be protected in such a way that only that subsystem could have write (and perhaps read) access to the files.

8. [语境照录，含断词 sys-tem，不入引] A security flaw not exploited by the Worm, but now becoming obvious, is that many sys tem services have configuration and command files owned by a common userid.

## b003 追加引文池（2026-11-18 V61 b003 取用，同源异句异锚）

9. [1.3.1 用] The bug exploited in sendmail had to do with functionality provided by a debugging option in the code. The Worm would issue the DEBUG command to sendmail and then specify a set of commands instead of a user address as the recipient of the message.

10. [1.3.2 用] The bug exploited to break fingerd involved overrunning the buffer the daemon used for input. The standard C library has a few routines that read input without checking for bounds on the buffer involved. In particular, the gets call takes input to a buffer without doing any bounds checking; this was the call exploited by the Worm.

11. [1.3.4 用] A worm is a program that can run by itself and can propagate a fully working version of itself to other machines. It is derived from the word tapeworm, a parasitic organism that lives inside a host and saps its resources to maintain itself.

12. [1.3.5 用] Although the Worm exploited flaws in only two server programs, its behavior has served to illustrate a few fundamental problems that have not yet been widely addressed.

## b004 追加引文池（2026-11-18 V61 b004 取用，同源异句异锚）

13. [1.4.1 用] This program eventually spread to thousands of machines, and disrupted normal activities and Internet connectivity for many days.

14. [1.4.2 用] As time went on, some of these machines became so loaded that they were unable to continue any processing; some machines failed completely when their swap space or process tables were exhausted.

15. [1.4.3 用] The actions of the Internet Worm exposed some specific security flaws in standard services provided by BSD-derived versions of UNIX.

16. [1.4.4 用] Although UNIX has long been known to have some security weaknesses (cf. [Ritc79], [Gram84], and [Reid87]), the scope of the breakins came as a great surprise to almost everyone.
