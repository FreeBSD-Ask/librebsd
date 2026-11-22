# ref-obsd-chroot2 登记卡（V61 b013 新登记：OpenBSD《CHROOT(2)》手册页）

- **来源**：The OpenBSD Project. CHROOT(2)[EB/OL]. OpenBSD Manual Pages, (OpenBSD-current, 2022-03-31 版)[2026-11-23]. https://man.openbsd.org/chroot.2.
- **性质**：OpenBSD chroot 系统调用手册（根目录替换定义、搜索权限前置、CAVEATS 三逃逸路径、EXAMPLES 降权配套、V7 HISTORY），official_doc 类。
- **取文途径**：man.openbsd.org 经 curl 直取全文（11 178 字节，2026-11-23；OpenBSD-current 卷）。
- **四键查重**：source_url（man.openbsd.org/chroot.2，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b013（2.2.1 根目录替换的作用界限〔路径搜索起点定义句〕、2.2.2 搜索权限的前置条件〔execute (search) access 句〕、2.2.3 开放目录描述符的风险〔recvmsg 描述符传递句〕、2.2.4 特权降级的配套要求〔EXAMPLES 降权配套句〕、2.2.5 隔离强度的经验上限〔CAVEATS 逃逸句〕，五题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述手册页正文；man 页 roff 原形照录——函数名后语义空格、HTML 实体、方括号空格照录）

1. [2.2.1 用] chroot () causes dirname to become the root directory, that is, the starting point for path searches of pathnames beginning with &#x2018; / &#x2019;.
   - **HTML 实体披露（b013）**："&#x2018; / &#x2019;" 系页内单引号实体（渲染为 ‘/’），照录原抽文形态。

2. [2.2.2 用] In order for a directory to become the root directory, a process must have execute (search) access for that directory.

3. [2.2.3 用] Passing directory file descriptors via recvmsg(2) from outside the chroot jail may also allow a process to escape.

4. [2.2.4 用，EXAMPLES 节] The following example changes the root directory to newroot , sets the current directory to the new root, and drops some setuid privileges. There may be other privileges which need to be dropped as well.
   - 续段示例代码含 chroot(newroot)／chdir("/")／setresuid(getuid(), getuid(), getuid()) 三调用（配套顺序：换根、换工作目录、降权）。

5. [2.2.5 用，CAVEATS 节] There are ways for a root process to escape from the chroot jail.
   - 续句 "Changes to the directory hierarchy made from outside the chroot jail may allow a restricted process to escape, even if it is unprivileged." 备用照录。

6. [备用（史源面），照录] The chroot () system call first appeared in Version&#x00A0;7 AT&amp;T UNIX .
   - "&#x00A0;" 系不换行空格实体、"&amp;" 系 & 实体，照录。
