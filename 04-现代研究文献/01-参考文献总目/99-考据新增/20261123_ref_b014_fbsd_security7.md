# ref-fbsd-security7 登记卡（V61 b014 新登记：FreeBSD《SECURITY(7)》手册页）

- **来源**：The FreeBSD Project. SECURITY(7)[EB/OL]. FreeBSD Manual Pages, (FreeBSD 15.0-RELEASE 卷)[2026-11-23]. https://man.freebsd.org/cgi/man.cgi?query=security&sektion=7&manpath=FreeBSD+15.0-RELEASE.
- **性质**：FreeBSD 安全概述手册（securelevel 分档清单、单向性、kern.securelevel 默认初始值），official_doc 类。
- **取文途径**：man.freebsd.org 经 curl 直取全文（107 499 字节，2026-11-23；FreeBSD 15.0-RELEASE manpath）。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=security&sektion=7&...，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b014（2.3.1 安全级别的单向提升〔raise/lower 不对称句〕、2.3.2 内核状态的写入限制〔级别 1 raw devices 句〕、2.3.4 级别与越权路径的对应〔分档清单起句〕、2.3.5 传递到各分支的条款〔默认初始值句〕，四题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述手册页正文；man 页 roff 原形照录）

1. [2.3.1 用] Any super-user process can raise the level, but no process can lower it.

2. [2.3.2 用] Once you have set the security level to 1, write access to raw devices will be denied and special chflags (1) flags, such as schg , will be enforced.

3. [2.3.4 用] The security levels are: -1 Permanently insecure mode - always run the system in insecure mode.

4. [2.3.5 用] -1 Permanently insecure mode - always run the system in insecure mode. This is the default initial value.
