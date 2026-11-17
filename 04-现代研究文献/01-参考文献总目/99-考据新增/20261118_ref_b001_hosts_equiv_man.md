# ref-hosts-equiv-man 登记卡（V61 b001 新登记：FreeBSD hosts.equiv(5) 手册页）

- **来源**：FreeBSD Project. HOSTS.EQUIV(5): trusted remote host and user name data base[EB/OL]. FreeBSD Manual Pages, FreeBSD 15.1-RELEASE and Ports.quarterly[2026-11-18]. https://man.freebsd.org/cgi/man.cgi?query=hosts.equiv&sektion=5.
- **性质**：BSD 官方手册页（格式文件卷），对 hosts.equiv／.rhosts 受信主机与用户机制的现时制度化表述（official_doc 类）。
- **取文途径**：man.freebsd.org 经 exa 通道实取页面正文（2026-11-18；本机直连 docs.freebsd.org SSL 握手失败、exa 抓取手册正文成功）。roff 排版多空格与制表符照录；块内引文经空白规范化后取连续句。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=hosts.equiv&sektion=5，库内无命中）；题名＋作者＋年份（HOSTS.EQUIV(5)＋FreeBSD Project＋2026，库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（公开文献记载，非当事人直接证词；现时手册只证制度延续，不充当 1988—1995 当期文书）。
- **用途**：V61 b001（1.1.4 受信主机免口令的信任假设）。

## 逐字引文池（供本批取用，均取自上述手册页正文；roff 空白照录）

1. [1.1.4 用] The hosts.equiv and .rhosts files contain information regarding trusted hosts and users on the network.

2. [备用（后续批可用），照录] For security reasons, a user's .rhosts file will be ignored if it is not a regular file, or if it is not owned by the user, or if it is writable by anyone other than the user.

3. [备用，照录] Trust user "foo" from host "bar.com".

## b002 追加引文池（2026-11-18 V61 b002 取用，同源异句异锚）

4. [1.2.5 用] A single "+" matches all hosts or users.
