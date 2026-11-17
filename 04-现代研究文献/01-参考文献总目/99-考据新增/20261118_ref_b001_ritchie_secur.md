# ref-ritchie-secur 登记卡（V61 b001 新登记：Ritchie《On the Security of UNIX》）

- **来源**：Ritchie D M. On the Security of UNIX[R/OL]. Murray Hill: Bell Laboratories（UNIX Supplementary Documents 收录）. 1979[2026-11-18]. https://www.tom-yam.or.jp/2238/ref/secur.pdf.
- **性质**：UNIX 设计者本人对当时系统安全形态的技术记述（提权位、保护位三档授权、超级用户边界、口令枚举实测），属当事人一手技术文献（academic_work 类）。
- **取文途径**：TUHS／minnie.tuhs.org 直连与 exa 抓取均失败（CRAWL_NOT_FOUND），本机直连 tom-yam.or.jp 亦失败；最终经 exa 搜索通道取该 PDF 镜像正文（2026-11-18）。**抽取伪影披露**：exa 抽文存在行末断词空格（如“reason ably”“installa tions”“pre vent”“exam ple”），引文池照录原抽文；块内引文只取无伪影连续段，断词段不入引。
- **年代披露**：原文未标注成文日期；ACM 图灵奖得主官方书目与 Scholar 条目均系于 “Unix Supplementary Documents, 1979”，登记年份取 1979（块内 claim 不倚赖此年份）。
- **四键查重**：source_url（tom-yam.or.jp/2238/ref/secur.pdf，库内无命中）；题名＋首作者＋年份（On the Security of UNIX＋Ritchie＋1979，库内无命中）；isbn_doi 空；sha256 为本卡件——新登记。
- **tier 依据**：academic_work／source_tier=primary；块内 claim 取 L4（当事人一手记载，属过程性证据）。
- **用途**：V61 b001（1.1.1 超级用户的全能边界、1.1.2 UID 与 GID 的授权粒度、1.1.3 setuid 位的提权通道、1.1.5 口令文件的猜测资源）。

## 逐字引文池（供本批取用，均取自上述 PDF 镜像正文；断词伪影照录）

1. [1.1.1 用] Another, and from the point of view of security, much more serious special case is that there is a ''super user'' who is able to read any file and write any non-directory. The super-user is also able to change the protection mode and the owner UID and GID of any file and to invoke privileged system calls. It must be recognized that the mere notion of a super-user is a theoretical, and usually practical, blemish on any protection scheme.

2. [1.1.2 用] Each UNIX file has associated with it eleven bits of protection information together with a user identification number and a user-group identification number (UID and GID). Nine of the protection bits are used to specify independently permission to read, to write, and to execute the file to the user himself, to members of the user's group, and to all other users.

3. [1.1.3 用] If, in this case, the set-UID bit is on for the file, the effective UID for the process is changed to the UID associated with the file; the change persists until the process terminates or until the UID changed again by another execution of a set-UID file.

4. [1.1.5 用，自 These 起句以避前句“installa tions”断词] These were tested against all five-letter combinations, all combinations of letters and digits of length four or less, and all words in Webster's Second unabridged dictionary; 60 of the 67 passwords were found. The whole process took about 12 hours of machine time.

5. [语境照录，含伪影，不入引] Since both the encryption algorithm and the encrypted passwords are available, exhaustive enumeration of potential passwords is feasible up to a point. As a practical test of the possibilities in this area, 67 encrypted passwords were collected from 10 UNIX installa tions.

6. [1.1.3 备用（可写 su 风险段），照录] The set-UID (set-GID) notion must be used carefully if any security is to be maintained. The first thing to keep in mind is that a writable set-UID file can have another program copied onto it. For example, if the super-user (su) command is writable, anyone can copy the shell onto it and get a password-free version of su.
