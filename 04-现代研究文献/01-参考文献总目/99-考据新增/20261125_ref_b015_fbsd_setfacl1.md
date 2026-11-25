# ref-fbsd-setfacl1 登记卡（V61 b015 新登记：FreeBSD《SETFACL(1)》手册页）

- **来源**：The FreeBSD Project. SETFACL(1)[EB/OL]. FreeBSD Manual Pages, (FreeBSD 15.0-RELEASE 卷)[2026-11-25]. https://man.freebsd.org/cgi/man.cgi?query=setfacl&sektion=1&manpath=FreeBSD+15.0-RELEASE.
- **性质**：FreeBSD setfacl 工具手册（ACL 条目类型、mask 条目与九位权限的映射语义），official_doc 类。
- **取文途径**：man.freebsd.org 经 curl 直取全文（70 246 字节，2026-11-25；FreeBSD 15.0-RELEASE manpath）。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=setfacl&sektion=1&...，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b015（2.4.2 授权条目的叠加顺位〔条目类型句〕、2.4.3 与传统权限位的映射〔mask 替代 group 位句〕，两题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述手册页正文；man 页 roff 原形照录——断词连字、引号形态照录）

1. [2.4.2 用] " user " or `u' specifying the access granted to the owner of the file or a specified user; " group " or `g' specifying the ac- cess granted to the file owning group or a specified group; " other " or `o' specifying the access granted to any process that does not match any user or group ACL entry; " mask " or `m' specifying the maximum access granted
   - **原形披露（b015）**：条目名双引号前后各一空格（" user "）与反引号缩写（`u'）系 roff 原形照录；"ac- cess" 系折行断词。

2. [2.4.3 用] When a mask en- try is present on the access ACL of an object, the mask entry is substi- tuted for the group bits; this occurs in programs such as stat (1) or ls (1) .
   - **映射句披露（b015）**：mask 条目替代 group 位、stat/ls 等旧工具语义随之——扩展条目与九位权限的映射决定旧工具行为的官方明文；"en- try"／"substi- tuted" 系折行断词照录。

3. [备用（group 与 mask 联动面），照录] If the POSIX.1e ACL contains a " mask " entry, the permissions of the " group " entry in the resulting ACL will be set to the permission associated with both the " group " and " mask " entries of the current ACL.
