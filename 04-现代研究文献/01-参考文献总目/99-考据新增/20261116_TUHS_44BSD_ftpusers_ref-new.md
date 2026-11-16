# 4.4BSD `etc/ftpusers`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/etc/ftpusers` 全文，取自 TUHS utree（474 字节原文；正文四行）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b015；source_url 四键查重：库内 TUHS 条目无 `etc/ftpusers`）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/etc/ftpusers>
- **quote（逐字，正文四行）**：

  ```
  # list of users disallowed any ftp access.
  # read by ftpd(8).
  root
  uucp
  ```

- **考据注**：这是**局限的名单式登记**：1993 年 4.4BSD 把 FTP 禁入账户写成两行名单（root、uucp），界线由“哪几个账户不可登录”表达，而非由能力模型表达——用于 5.3.4 的“窗口口径”。**口径披露（要紧）**：本件只证该名单的内容与时点（4.4BSD 树内），不证“当时服务器无其他隔离手段”；名单式登记与 chroot 之类机制并存，两者不互斥。**载体披露**：原文为纯文本两行注释＋两行账户名，引文照录，行序未改。
- **本批落点**：V31.5.3.4 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b015；official_doc／L3）
