# 4.4BSD ftpd(8) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/libexec/ftpd/ftpd.8`（FTP 服务器手册页）；本机 Chrome UA urllib 直取，`<pre>` 块 8,755 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b004；source_url 四键查重：库内 ftpd 相关条目无该路径）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/libexec/ftpd/ftpd.8>
- **quote（逐字，一处；mroff 渲染后的句子，宏标记不入引文）**：The server performs a chroot(2) to the home directory of the "ftp" user.
- **考据注**：此句把 chroot 的**早期实用场景**写实：匿名登录（用户名 anonymous 或 ftp）时，服务器对 ftp 用户执行 chroot，客户端访问被限在其主目录之下——隔离不是设想，而是 4.4BSD 发行里默认开启的服务器措施。用于 5.2.5“隔离用途的早期实践”。**能证与不能证**：只证**该发行的手册页这样说明**行为与配置前提（须存在 ftp 账户），不证该做法首见于哪一版或是否所有站点启用。**同页配套**：文内另有“ftp 账户须在口令库中存在”“登录名不得列于 /etc/ftpusers”等前置条件，本批未逐一引。**载体说明**：TUHS 转录，按原文核对
- **本批落点**：V31.5.2.5 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b004；official_doc／L3）
