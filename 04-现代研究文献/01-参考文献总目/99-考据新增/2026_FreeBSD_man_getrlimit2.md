# getrlimit(2) — FreeBSD 系统调用手册页（资源限额控制）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=getrlimit&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.9.8.1“文件描述符的极限”补证（D2 块）：进程级开文件限额（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     RLIMIT_FSIZE    The largest size (in bytes) file that may be created.

     RLIMIT_KQUEUES  The  maximum  number  of kqueues this user id is allowed to
		     create.

     RLIMIT_MEMLOCK  The maximum size (in bytes) which a process may  lock  into
		     memory using the mlock(2) system call.

     RLIMIT_NOFILE   The maximum number of open files for this process.

     RLIMIT_NPROC    The  maximum number of simultaneous processes for this user
		     id.

     RLIMIT_NPTS     The maximum number of pseudo-terminals this user id is  al-
		     lowed to create.

     RLIMIT_PIPEBUF  The  maximum  total size of in-kernel buffers for bi-direc-
		     tional pipes/fifos that this user id is allowed to consume.
		     The buffers for kernel FIFOs created on the first open of a
		     filesystem object created by (mkfifo(2)) are  also  charged
		     to  the  user  ID of the process opening it, not the FIFO's
		     filesystem owner.	Despite somewhat unexpected, this is  in
		     fact fair, since user of the fifo is not necessary its cre-
		     ator.

     RLIMIT_RSS      When there is memory pressure and swap is available, prior-
		     itize  eviction  of  a  process' resident pages beyond this
		     amount (in bytes).  When memory is not under pressure, this
		     rlimit is effectively ignored.

		     Processes that exceed their set  RLIMIT_RSS  are  not  sig-
		     nalled  or  halted.   The	limit is merely a hint to the VM
		     daemon to prefer to deactivate pages  from  processes  that
		     have exceeded their set RLIMIT_RSS.

     RLIMIT_SBSIZE   The maximum size (in bytes) of socket buffer usage for this
		     user.   This limits the amount of network memory, and hence
		     the amount of mbufs, that this user may hold at any time.
```

## 引文摘录（空白已归一，供逐字核对）

RLIMIT_FSIZE The largest size (in bytes) file that may be created. RLIMIT_KQUEUES The maximum number of kqueues this user id is allowed to create. RLIMIT_MEMLOCK The maximum size (in bytes) which a process may lock into memory using the mlock(2) system call. RLIMIT_NOFILE The maximum number of open files for this process. RLIMIT_NPROC The maximum number of simultaneous processes for this user id. RLIMIT_NPTS The maximum number of pseudo-terminals this user id is al- lowed to create. RLIMIT_PIPEBUF The maximum total size of in-kernel buffers for bi-direc- tional pipes/fifos that this user id is allowed to consume. The buffers for kernel FIFOs created on the first open of a filesystem object created by (mkfifo(2)) are also charged to the user ID of the process opening it, not the FIFO's filesystem owner. Despite somewhat unexpected, this is in fact fair, since user of the fifo is not necessary its cre- ator. RLIMIT_RSS When there is memory pressure and swap is available, prior- itize eviction of a process' resident pages beyond this amount (in bytes). When memory is not under pressure, this rlimit is effectively ignored. Processes that exceed their set RLIMIT_RSS are not sig- nalled or halted. The limit is merely a hint to the VM daemon to prefer to deactivate pages from processes that have exceeded their set RLIMIT_RSS. RLIMIT_SBSIZE The maximum size (in bytes) of socket buffer usage for this user. This limits the amount of network memory, and hence the amount of mbufs, that this user may hold at any time.
