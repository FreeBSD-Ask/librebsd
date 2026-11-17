# ref-eichin-rochlis-1989 登记卡（V61 b003 新登记：Eichin & Rochlis《With Microscope and Tweezers》）

- **来源**：Eichin M W, Rochlis J A. With Microscope and Tweezers: An Analysis of the Internet Virus of November 1988[C/OL]. Proceedings of the 1989 IEEE Symposium on Research in Security and Privacy. 1989-02-09[2026-11-18]. https://www.d.umn.edu/~pahp/readings/internet-worm-MIT-1989.pdf.
- **性质**：MIT 应急分析组当事人侧第三方权威技术分析（基于逐例反编译，载 sendmail debug、fingerd 栈溢出、rsh/rexec 信任、时间线与防御诸节；IEEE S&P 1989 发表版），academic_work 类。
- **取文途径**：d.umn.edu 课程镜像 PDF 经 exa 搜索通道取正文（2026-11-18；MIT 主站 HTML 版与其并存的 web.mit.edu/eichin/www/virus/main.html 未取，以本镜像为登记源）。**抽取伪影披露**：双栏 PDF 抽文有行末断词空格（“cur rent／in cluding／pro gram／ma chine／ac count／Novem ber”等），引文池照录；块内引文只取无伪影连续段；tex 式引号 ‘‘ ’’ 照录。
- **四键查重**：source_url（d.umn.edu/~pahp/readings/internet-worm-MIT-1989.pdf，库内无命中）；题名＋首作者＋年份（With Microscope and Tweezers＋Eichin＋1989，库内无命中）——新登记。
- **tier 依据**：academic_work／source_tier=secondary_authoritative；块内 claim 取 L3（公开文献记载，第三方分析非当事人直接证词）。
- **用途**：V61 b003（1.3.1 邮件服务的调试后门、1.3.2 finger 服务的越界写入、1.3.3 远程执行服务的信任滥用、1.3.4 漏洞利用的自动化转向、1.3.5 应用层漏洞的利用方式）。

## 逐字引文池（供本批取用，均取自上述 PDF 镜像正文；断词伪影照录）

1. [1.3.1 用，含“cur rent”断词照录] The virus exploited the ‘‘debug’’ function of sendmail, which enables debugging mode for the duration of the cur rent connection.

2. [1.3.2 用] when he looked at the source for fingerd, he found that the buffer it was using was located on the stack; in addition, the program used the C library gets function, which assumes that the buffer it is given is long enough for the line it is about to read

3. [1.3.3 用] This system has an important design flaw, which is that the local host only knows the remote host by its network address, which can often be forged.

4. [1.3.4 用] The virus was tested or launched at 5:01:59pm. The logs show it infecting a second Cornell machine at 5:04pm.

5. [1.3.5 用] The fact that debug was enabled by default was reported to Berkeley by several sources during the 4.2BSD release. The 4.3BSD release as well as Sun releases still had this option enabled by default

6. [备用（1.1.5 可读文件面后续批），照录] A common, world readable file (/etc/passwd) that containsthe user names and encrypted passwords for every user on the system fa cilitated this search.

7. [备用，照录] The virus attempted to use the Berkeley remote shell pro gram (called rsh) to attack other machines without using passwords.
