# 4.4BSD inetd(8) 手册页（TUHS 收录）（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/usr.sbin/inetd/inetd.8`（internet 超级服务器手册页，`@(#)inetd.8 8.1 (Berkeley) 6/6/93`）；本机 Chrome UA urllib 直取，`<pre>` 块 10,148 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b007；source_url 四键查重：库内 inetd 无条目）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/usr.sbin/inetd/inetd.8>
- **quote（逐字，三处；mroff 渲染后）**：
  1. When a connection is found on one of its sockets, it decides what service the socket corresponds to, and invokes a program to service the request.
  2. The wait/nowait entry is applicable to datagram sockets only
  3. Essentially, inetd allows running one daemon to invoke several others, reducing load on the system.
- **考据注**：第 1 句是**按需调用的动作序列**（发现连接—判定服务—调起程序），用于 8.3.2；第 2 句把 wait/nowait 的适用面限死在数据报套接字（原句续“other sockets should have a … nowait entry”），用于 8.3.4；第 3 句自陈枢纽地位（一守护调起多服务、降低负载），用于 8.3.6。**引文边界**：第 2 句为**截引**，括号内补充未取；第 1 句含双空格（mroff 排印），照录。**能证与不能证**：只证 4.4BSD 手册页所写行为与字段语义，不证 inetd 的首创版本与部署规模（另见 8.3.1／8.3.5）。**未取**：内置服务列表与 `-R` 速率限制的默认值，留待 8.3.5 复核
- **本批落点**：V31.8.3.2 第 1 块（第 1 句）、V31.8.3.4 第 1 块（第 2 句）、V31.8.3.6 第 1 块（第 3 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b007；official_doc／L3）
