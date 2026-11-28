# ref-fbsd-loginconf5 登记卡（V61 b017 新登记：FreeBSD《LOGIN.CONF(5)》手册页）

- **来源**：The FreeBSD Project. LOGIN.CONF(5)[EB/OL]. FreeBSD Manual Pages, (FreeBSD 15.0-RELEASE 卷)[2026-11-25]. https://man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5&manpath=FreeBSD+15.0-RELEASE.
- **性质**：FreeBSD 登录类能力数据库手册（登录类定义、资源限制表、软硬限、类继承），official_doc 类。
- **取文途径**：man.freebsd.org 经 curl 直取全文（77 880 字节，2026-11-25；FreeBSD 15.0-RELEASE manpath，--ssl-no-revoke）。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5&...，references 表无命中）；题名（references 表无 login.conf 卡片）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b017（2.6.1 登录类的资源上限、2.6.4 进程数阈值）。

## 逐字引文池（取自 DESCRIPTION／RESOURCE LIMITS 段；roff 断词与空白按归一照录）

1. [2.6.1 用] A login class (an optional annotation against each record in the user ac- count database, /etc/master.passwd) determines session accounting, resource limits and user environment settings.
2. [2.6.4 用] maxproc number Maximum number of processes.

- 原页 DESCRIPTION 段含 roff 断词 `ac- count`（account 折行），引文照录；RESOURCE LIMITS 为制表清单（Name／Type／Default／Description），maxproc 行按空白归一连续照录。同段另有“These resource limit entries actually specify both the maximum and current limits (see getrlimit(2)).”说明软硬限双值，本批未入块。
