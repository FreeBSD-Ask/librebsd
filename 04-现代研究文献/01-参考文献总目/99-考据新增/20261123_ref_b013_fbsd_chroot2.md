# ref-fbsd-chroot2 登记卡（V61 b013 新登记：FreeBSD《CHROOT(2)》手册页）

- **来源**：The FreeBSD Project. CHROOT(2)[EB/OL]. FreeBSD Manual Pages, (FreeBSD 15.0-RELEASE 卷)[2026-11-23]. https://man.freebsd.org/cgi/man.cgi?query=chroot&sektion=2&manpath=FreeBSD+15.0-RELEASE.
- **性质**：FreeBSD chroot/fchroot 系统调用手册（作用界限、超级用户限定、开放目录描述符 sysctl 开关、BUGS 工作目录残留），official_doc 类。
- **取文途径**：man.freebsd.org 经 curl 直取全文（61 151 字节，2026-11-23；FreeBSD 15.0-RELEASE manpath）。
- **四键查重**：source_url（man.freebsd.org/cgi/man.cgi?query=chroot&sektion=2&...，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b013（2.2.1 根目录替换的作用界限〔不改当前目录句〕、2.2.2 搜索权限的前置条件〔EACCES 句〕、2.2.3 开放目录描述符的风险〔sysctl 开关段〕、2.2.4 特权降级的配套要求〔BUGS 残留句〕、2.2.5 隔离强度的经验上限〔historic insecure 句〕，五题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述手册页正文；man 页 roff 原形照录——断词连字、函数名后语义空格照录）

1. [2.2.1 用] It should be noted that chroot () has no effect on the process's current di- rectory.
   - **roff 原形披露（b013）**："chroot ()"（函数名后语义空格）与 "di- rectory"（折行断词连字）均系 roff 原形，照录。

2. [2.2.2 用] [EACCES] Search permission is denied for any component of the path name.
   - ERRORS 列表项照录（本页方括号无内空格，与 OpenBSD 页形态相异——两站 roff 排版差异如实记）。

3. [2.2.3 用] Depending on the setting of the `kern.chroot_allow_open_directories' sysctl variable, open filedescriptors which reference directories will make the chroot () fail as follows: If `kern.chroot_allow_open_directories' is set to zero, chroot () will al- ways fail with EPERM if there are any directories open.
   - 开关段前两句；续句 "If ... set to one (the default), chroot () will fail with EPERM if there are any directories open and the process is already subject to the chroot () system call." 见条目 5 前段。

4. [2.2.4 用，BUGS 节] If the process is able to change its working directory to the target direc- tory, but another access control check fails (such as a check for open di- rectories, or a MAC check), it is possible that this system call may return an error, with the working directory of the process left changed.

5. [2.2.5 用] Any other value for `kern.chroot_allow_open_directories' will bypass the check for open directories, mimicking the historic insecure behavior of ch- root () still present on other systems.
