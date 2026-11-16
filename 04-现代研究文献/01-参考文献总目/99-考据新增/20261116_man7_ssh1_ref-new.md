# Linux man-pages：`ssh(1)`（新 ref）引用卡

- **性质**：man7.org 的 Linux man-pages 在线页 `ssh(1)`（66,593 字节），正文取自 OpenSSH 发行包 `openssh-9.9p2.tar.gz` 内的手册页，由 man7.org 渲染发布
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b027；查重：库内无 `man7.org` 条目）
- **source_url**：<https://man7.org/linux/man-pages/man1/ssh.1.html>
- **计数（抓取正文实测）**：`BSD` 3 次、`OpenBSD` 2 次、`OpenSSH` 6 次
- **quote（逐字，三处，分落三块）**：
  1. OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH.
  2. This page is part of the openssh (Portable OpenSSH) project. Information about the project can be found at http://www.openssh.com/portable.html.
  3. ssh — OpenSSH remote login client
- **考据注**：三处对应三个层次。第 1 处是**再解释的正面写法**（3.9.1）：派生关系（ssh 1.2.12 by Tatu Ylonen）与六位改造者姓名并列，说明“再解释”不等于抹除。第 2 处是**归属的文档层**（3.9.3）：COLOPHON 把文档归到 Portable OpenSSH 项目并给出 `portable.html` 入口；与 Debian 包页（b011 实测 `OpenBSD` 0 次）并置，可定出“手册层留名、包页层不留名”的区间。第 3 处是**磨损点定位**（3.10.3）：NAME 段只有“ssh — OpenSSH remote login client”，BSD／OpenBSD 不在这一行——而这是被反复引用最多的那一行。
- **载体与版本披露（要紧）**：本页是 **man7.org 的渲染副本**，其正文来自 OpenSSH 9.9p2 tarball；与 OpenSSH 上游仓库的当前 `ssh.1` 可能有版本差（COLOPHON 自记 “obtained from the tarball openssh-9.9p2.tar.gz”）。因此本卡引文的第一作者层是 **OpenSSH 上游作者段**，man7.org 是发布载体。另：COLOPHON 中 URL 与句点之间原文有一个空格（链接渲染所致），块内引文已并拢，余字未改。
- **限度**：①本页属发行版生态的文档分发层，不等于 Linux 发行版自身的叙述（后者见 Debian／Ubuntu／Fedora 包页，b011／b015）；②AUTHORS 段是上游原文照录，可作上游自述的**转移证据**（说明上游署名随文档传播），但不可用来证明下游语境。
- **本批落点**：V35.3.9.1（第 1 处）、V35.3.9.3（第 2 处）、V35.3.10.3（第 3 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b027；official_doc／L3）
