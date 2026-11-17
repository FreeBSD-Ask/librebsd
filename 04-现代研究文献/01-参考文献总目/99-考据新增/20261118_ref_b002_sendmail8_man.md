# ref-sendmail8-man 登记卡（V61 b002 新登记：FreeBSD sendmail(8) 手册页）

- **来源**：FreeBSD Project. SENDMAIL(8): an electronic mail transport agent[EB/OL]. FreeBSD Manual Pages[2026-11-18]. https://man.freebsd.org/cgi/man.cgi?query=sendmail&sektion=8.
- **性质**：BSD 官方系统管理手册页，对 sendmail 邮件传输代理（含 -bd 守护进程模式监听 25 端口收 SMTP）的现时制度化表述（official_doc 类）。
- **取文途径**：man.freebsd.org 经 exa 通道实取页面正文（2026-11-18）。roff 排版多空格、制表符与行末连字符断词照录；块内引文含“lis- tening”软连字断痕（V12 b017“连字断痕照录”先例），断词处为排版换行非原文分词。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=sendmail&sektion=8，库内无命中）；题名＋作者＋年份（SENDMAIL(8)＋FreeBSD Project＋2026，库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（公开文献记载，非当事人直接证词；现时手册只证制度延续）。
- **用途**：V61 b002（1.2.2 服务进程的暴露面扩张）。

## 逐字引文池（供本批取用，均取自上述手册页正文；roff 空白与断词照录）

1. [1.2.2 用，含“lis- tening”软连字断痕照录] Run as a daemon. Sendmail will fork and run in background lis- tening on socket 25 for incoming SMTP connections.

2. [备用（后续批），照录] Sendmail sends a message to one or more recipients, routing the message over whatever networks are necessary.

3. [备用，照录] Sendmail is not intended as a user interface routine; other programs provide user-friendly front ends; sendmail is used only to deliver pre- formatted messages.
