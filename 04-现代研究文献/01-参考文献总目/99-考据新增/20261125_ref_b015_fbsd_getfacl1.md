# ref-fbsd-getfacl1 登记卡（V61 b015 新登记：FreeBSD《GETFACL(1)》手册页）

- **来源**：The FreeBSD Project. GETFACL(1)[EB/OL]. FreeBSD Manual Pages, (FreeBSD 15.0-RELEASE 卷)[2026-11-25]. https://man.freebsd.org/cgi/man.cgi?query=getfacl&sektion=1&manpath=FreeBSD+15.0-RELEASE.
- **性质**：FreeBSD getfacl 工具手册（trivial ACL 判据：仅含 owner/group/other 且与文件模式匹配），official_doc 类。
- **取文途径**：man.freebsd.org 经 curl 直取全文（59 389 字节，2026-11-25；FreeBSD 15.0-RELEASE manpath）。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=getfacl&sektion=1&...，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b015（2.4.3 与传统权限位的映射〔trivial ACL 判据句〕）。

## 逐字引文池（供本批取用，均取自上述手册页正文；roff 断词照录）

1. [2.4.3 用] Skip files that only have a trivial ACL, as defined by acl_is_triv- ial_np (3) . Notably, files with POSIX.1e ACLs that only represent the owner, group and other to match the mode of the file will be skipped.
   - **判据披露（b015）**：trivial ACL（仅 owner/group/other 与模式匹配）即退化为九位权限的等价态；"acl_is_triv- ial_np" 系折行断词照录。
