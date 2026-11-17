# ref-rlogind8-man 登记卡（V61 b002 新登记：FreeBSD rlogind(8) 手册页）

- **来源**：FreeBSD Project. RLOGIND(8): remote login server[EB/OL]. FreeBSD Manual Pages, FreeBSD 15.0-RELEASE[2026-11-18]. https://man.freebsd.org/cgi/man.cgi?query=rlogind&sektion=8.
- **性质**：BSD 官方系统管理手册页，对 rlogin 远程登录服务器（基于特权端口号与受信主机的认证、鉴权假设完整性、4.2BSD 出典）的现时制度化表述（official_doc 类）。
- **取文途径**：man.freebsd.org 经 exa 通道实取页面正文（2026-11-18）。roff 多空格照录；HISTORY 节载“The rlogind utility appeared in 4.2BSD”（硬事实，卡内出典）。BUGS 节自陈认证假设之不安全（“insecure but useful in an open environment”），为该机制的官方自我定性质证句。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=rlogind&sektion=8，库内无命中）；题名＋作者＋年份（RLOGIND(8)＋FreeBSD Project＋2026，库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（公开文献记载，非当事人直接证词）。
- **用途**：V61 b002（1.2.4 远程登录与文件传送的入口、1.2.5 网络信任链的传递性）。

## 逐字引文池（供本批取用，均取自上述手册页正文；roff 空白照录）

1. [1.2.4 用] The rlogind utility is the server for the rlogin(1) program. The server provides a remote login facility with authentication based on privileged port numbers from trusted hosts.

2. [1.2.5 用] The authentication procedure used here assumes the integrity of each client machine and the connecting medium. This is insecure, but is useful in an "open" environment.

3. [HISTORY 节照录（卡内出典）] The rlogind utility appeared in 4.2BSD.

4. [备用，照录] The rlogind utility listens for service requests at the port indicated in the "login" service specification; see services(5).
