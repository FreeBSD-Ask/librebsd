# chroot(2) — FreeBSD 系统调用手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=chroot&sektion=2
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.1.1“UNIX 隔离传统的来源”补证（D2 块）：chroot 的权限前提（D2 块，ref_id 见库）

## 抓取正文（节选）

```
DESCRIPTION
     The  dirname argument is the address of the pathname of a directory, termi-
     nated by an ASCII NUL.  The chroot() system call causes dirname  to  become
     the  root directory, that is, the starting point for path searches of path-
     names beginning with `/'.

     In order for a directory to become the root directory a process  must  have
     execute (search) access for that directory.

     It should be noted that chroot() has no effect on the process's current di-
     rectory.

     This    call    is    restricted	 to    the    super-user,   unless   the
     `security.bsd.unprivileged_chroot' sysctl variable is  set  to  1	and  the
     process has enabled the PROC_NO_NEW_PRIVS_CTL procctl(2).

     Depending on the setting of the `kern.chroot_allow_open_directories' sysctl
     variable,	open  file descriptors which reference directories will make the
     chroot() fail as follows:

     If `kern.chroot_allow_open_directories' is set to zero, chroot()  will  al-
     ways fail with EPERM if there are any directories open.

     If  `kern.chroot_allow_open_directories'  is  set to one (the default), ch-
     root() will fail with EPERM if there  are	any  directories  open	and  the
     process is already subject to the chroot() system call.

     Any  other  value	for `kern.chroot_allow_open_directories' will bypass the
     check for open directories, mimicking the historic insecure behavior of ch-
     root() still present on other systems.

     The fchroot() system call is identical to chroot() except it takes  a  file
```

## 引文摘录（空白已归一，供逐字核对）

DESCRIPTION The dirname argument is the address of the pathname of a directory, termi- nated by an ASCII NUL. The chroot() system call causes dirname to become the root directory, that is, the starting point for path searches of path- names beginning with `/'. In order for a directory to become the root directory a process must have execute (search) access for that directory. It should be noted that chroot() has no effect on the process's current di- rectory. This call is restricted to the super-user, unless the `security.bsd.unprivileged_chroot' sysctl variable is set to 1 and the process has enabled the PROC_NO_NEW_PRIVS_CTL procctl(2). Depending on the setting of the `kern.chroot_allow_open_directories' sysctl variable, open file descriptors which reference directories will make the chroot() fail as follows: If `kern.chroot_allow_open_directories' is set to zero, chroot() will al- ways fail with EPERM if there are any directories open. If `kern.chroot_allow_open_directories' is set to one (the default), ch- root() will fail with EPERM if there are any directories open and the process is already subject to the chroot() system call. Any other value for `kern.chroot_allow_open_directories' will bypass the check for open directories, mimicking the historic insecure behavior of ch- root() still present on other systems. The fchroot() system call is identical to chroot() except it takes a file
