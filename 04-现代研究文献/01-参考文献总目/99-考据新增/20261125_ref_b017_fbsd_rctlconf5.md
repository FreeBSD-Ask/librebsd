# ref-fbsd-rctlconf5 登记卡（V61 b017 新登记：FreeBSD《RCTL.CONF(5)》手册页）

- **来源**：The FreeBSD Project. RCTL.CONF(5)[EB/OL]. FreeBSD Manual Pages, (FreeBSD 15.0-RELEASE 卷)[2026-11-25]. https://man.freebsd.org/cgi/man.cgi?query=rctl.conf&sektion=5&manpath=FreeBSD+15.0-RELEASE.
- **性质**：FreeBSD 资源限制数据库默认值文件格式手册（/etc/rctl.conf 的规则形与登录类示例），official_doc 类。
- **取文途径**：man.freebsd.org 经 curl 直取全文（56 452 字节，2026-11-25；FreeBSD 15.0-RELEASE manpath，--ssl-no-revoke）。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=rctl.conf&sektion=5&...，references 表无命中）；题名（references 表无 rctl.conf 卡片）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b017（2.6.3 超限动作的具体落形）。

## 逐字引文池（取自 EXAMPLES 段；空白归一照录）

1. [2.6.3 用] loginclass:testing:maxproc:deny=100/user # At most 100 processes per user

- 原页 EXAMPLES 段该行为示例规则（含行尾注释 `# At most 100 processes per user`），引文照录含注释；同页说明 `/etc/rctl.conf` 在多用户模式读入以设定 RCTL 数据库默认内容，格式即 rctl(8) 命令行。
