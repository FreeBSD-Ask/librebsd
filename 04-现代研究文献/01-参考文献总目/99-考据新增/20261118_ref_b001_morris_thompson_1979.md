# ref-morris-thompson-1979 登记卡（V61 b001 新登记：Morris & Thompson《Password Security: A Case History》）

- **来源**：Morris R, Thompson K. Password Security: A Case History[J/OL]. Communications of the ACM, 1979, 22(11): 594-597[2026-11-18]. https://rist.tech.cornell.edu/6431papers/MorrisThompson1979.pdf.
- **性质**：贝尔实验室当事人（口令机制维护者与系统原作者）对该机制设计史的技术记述（首次实现、攻击实测、salt 等），CACM 1979 年 11 月 22 卷 11 期 594—597 页，属当事人一手技术文献（academic_work 类）。
- **取文途径**：Cornell 课程镜像直连下载成功（2026-11-18，HTTP 200）；首次下载 32KB 截断，重试连接被重置，完整 PDF 未取得；最终以 exa 搜索通道取该 PDF 正文（ highlights 覆盖目标段落）。**抽取伪影披露**：exa 抽文存在行末断词空格（如“pre vent”“exam ple”“pass words”“avail able”“d!ctionary”）；其中“d!ctionary”系原刊排印如此（原文即以感叹号代 i），非抽取伪影；引文池照录原抽文，块内引文只取无伪影连续段。
- **四键查重**：source_url（rist.tech.cornell.edu/6431papers/MorrisThompson1979.pdf，库内无命中）；题名＋首作者＋年份（Password Security: A Case History＋Morris＋1979，库内无命中）；isbn_doi 空（正式 DOI 为 10.1145/359168.359172，登记于卡不单列）；sha256 为本卡件——新登记。
- **tier 依据**：academic_work／source_tier=primary；块内 claim 取 L4（当事人一手记载，属过程性证据）。
- **用途**：V61 b001（1.1.1 超级用户的全能边界、1.1.5 口令文件的猜测资源）。

## 逐字引文池（供本批取用，均取自上述 PDF 镜像正文；断词伪影照录）

1. [1.1.1 用，句中后段起句以避“exam ple”断词] is especially critical because the super-user has all sorts of permissions and has essentially unlimited access to all system resources.

2. [1.1.5 用] In a collection of 3,289 passwords gathered from many users over a long period of time, 15 were a single ASCII character; 72 were strings of two ASCII characters; 464 were strings of three ASCII characters; 477 were strings of four alphamerics; 706 were five letters, all upper-case or all lower-case; 605 were six letters, all lower-case.

3. [1.1.5 备用] The dictionary search alone, which required only five minutes to run, produced about one third of the passwords.

4. [可读文件面备用（后续批），照录] It also seemed advisable to devise a system in which neither the password file nor the password program itself needed to be protected against being read by anyone.

5. [语境照录，含伪影，不入引] The so-called "super-user" password on the UNIX system, for exam ple, is especially critical because the super-user has all sorts of permissions and has essentially unlimited access to all system resources.

6. [86% 汇总句照录（后续批可用），含伪影不入引] An additional 492 passwords appeared in various avail able dictionaries, name lists, and the like. A total of 2,831 or 86 percent of this sample of passwords fell into one of these classes.

## b004 追加引文池（2026-11-18 V61 b004 取用，同源异句异锚）

7. [1.4.4 用] Remote-access systems are peculiarly vulnerable to penetration by outsiders as there are threats at the remote terminal, along the communications link, as well as at the computer itself.
