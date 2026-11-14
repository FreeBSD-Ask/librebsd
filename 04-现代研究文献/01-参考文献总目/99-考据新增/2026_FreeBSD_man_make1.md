# make(1) — FreeBSD 用户命令手册页（程序维护工具）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=make&sektion=1
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.3.3“并行构建的作业调度”补证（D2 块）：-j 递归协同（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     -i      Ignore non-zero exit of shell commands in the makefile.  Equivalent
	     to specifying `-' before each command line in the makefile.

     -J private
	     This option should not be specified by the user.

	     When  the	-j option is in use in a recursive build, this option is
	     passed by a make to child makes to allow all the make processes  in
	     the build to cooperate to avoid overloading the system.

     -j max_jobs
	     Specify  the  maximum  number of jobs that make may have running at
	     any one time.  If max_jobs is a floating point number, or ends with
	     `C', then the value is multiplied by the number  of  CPUs	reported
	     online   by   sysconf(3).	 The  value  of  max_jobs  is  saved  in
	     .MAKE.JOBS.  Turns compatibility mode off, unless the -B option  is
	     also specified.  When compatibility mode is off, all commands asso-
	     ciated  with  a target are executed in a single shell invocation as
	     opposed to the traditional one shell invocation per line.	This can
	     break traditional scripts which change directories on each  command
	     invocation and then expect to start with a fresh environment on the
	     next line.  It is more efficient to correct the scripts rather than
	     turn backwards compatibility on.

	     A	job token pool with max_jobs tokens is used to control the total
	     number of jobs running.  Each instance of make will wait for a  to-
	     ken from the pool before running a new job.

     -k      Continue processing after errors are encountered, but only on those
	     targets  that do not depend on the target whose creation caused the
	     error.

     -m directory
	     Specify a directory in which to search for sys.mk and makefiles in-
	     cluded via the <file>-style include statement.  The -m  option  can
	     be  used multiple times to form a search path.  This path overrides
	     the default system include path  /usr/share/mk.   Furthermore,  the
```

## 引文摘录（空白已归一，供逐字核对）

-i Ignore non-zero exit of shell commands in the makefile. Equivalent to specifying `-' before each command line in the makefile. -J private This option should not be specified by the user. When the -j option is in use in a recursive build, this option is passed by a make to child makes to allow all the make processes in the build to cooperate to avoid overloading the system. -j max_jobs Specify the maximum number of jobs that make may have running at any one time. If max_jobs is a floating point number, or ends with `C', then the value is multiplied by the number of CPUs reported online by sysconf(3). The value of max_jobs is saved in .MAKE.JOBS. Turns compatibility mode off, unless the -B option is also specified. When compatibility mode is off, all commands asso- ciated with a target are executed in a single shell invocation as opposed to the traditional one shell invocation per line. This can break traditional scripts which change directories on each command invocation and then expect to start with a fresh environment on the next line. It is more efficient to correct the scripts rather than turn backwards compatibility on. A job token pool with max_jobs tokens is used to control the total number of jobs running. Each instance of make will wait for a to- ken from the pool before running a new job. -k Continue processing after errors are encountered, but only on those targets that do not depend on the target whose creation caused the error. -m directory Specify a directory in which to search for sys.mk and makefiles in- cluded via the <file>-style include statement. The -m option can be used multiple times to form a search path. This path overrides the default system include path /usr/share/mk. Furthermore, the
