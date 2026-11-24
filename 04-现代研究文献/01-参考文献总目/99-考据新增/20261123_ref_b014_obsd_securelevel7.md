# ref-obsd-securelevel7 登记卡（V61 b014 新登记：OpenBSD《SECURELEVEL(7)》手册页）

- **来源**：The OpenBSD Project. SECURELEVEL(7)[EB/OL]. OpenBSD Manual Pages, (OpenBSD-current)[2026-11-23]. https://man.openbsd.org/securelevel.7.
- **性质**：OpenBSD securelevel 手册（四级分档清单：−1／0／1／2 逐级越权路径关闭），official_doc 类。
- **取文途径**：man.openbsd.org 经 curl 直取全文（11 999 字节，2026-11-23；OpenBSD-current 卷）。
- **四键查重**：source_url（man.openbsd.org/securelevel.7，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b014（2.3.1 安全级别的单向提升〔may no longer be lowered except by init 句〕、2.3.2 内核状态的写入限制〔1 Secure mode 清单〕、2.3.3 单用户模式的门槛线〔0 Insecure mode single-user 句〕、2.3.4 级别与越权路径的对应〔四级起句〕、2.3.5 传递到各分支的条款〔1 Secure mode default 句〕，五题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述手册页 DESCRIPTION 分档段；man 页 roff 原形照录）

1. [2.3.1 用] securelevel may no longer be lowered except by init

2. [2.3.2 用] 1 Secure mode default mode when system is multi-user securelevel may no longer be lowered except by init /dev/mem and /dev/kmem cannot be opened raw disk devices of mounted file systems are read-only system immutable and append-only file flags may not be removed
   - **列表项拼接披露（b014）**：分档段内 1 级条目的标目与各限制项为列表形态，按空白归一连续照录。

3. [2.3.3 用] 0 Insecure mode used during bootstrapping and while the system is single-user all devices may be read or written subject to their permissions
   - 同上列表形态照录。

4. [2.3.4 用] The OpenBSD kernel provides four levels of system security: -1 Permanently insecure mode

5. [2.3.5 用] 1 Secure mode default mode when system is multi-user
