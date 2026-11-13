# jail(8) — FreeBSD 系统管理手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=8
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.1.1“UNIX 隔离传统的来源”补证（D2 块）：jail 工具的参数化接口（D2 块，ref_id 见库）

## 抓取正文（节选）

```

   Backward Compatibility
     jail [-dhilqv] [-J jid_file] [-u username] [-U username] [-n jailname]
	  [-s securelevel] path hostname ip[,...] command ...

DESCRIPTION
     The  jail utility creates new jails, or modifies or removes existing jails.
     It can also print a list of configured jails and their parameters.  A  jail
     (or  "prison")  is  specified via parameters on the command line, or in the
     jail.conf(5) file.

     At least one of the options -c, -e, -m or -r must be specified.  These  op-
     tions  are  used  alone or in combination to describe the operation to per-
     form:

     -c      Create a new jail.  The jail jid and name parameters (if  specified
	     on the command line) must not refer to an existing jail.

     -e separator
	     Exhibit a list of all configured non-wildcard jails and their para-
	     meters.   No  jail  creation,  modification or removal performed if
	     this option is used.  The separator string is used to separate  pa-
	     rameters.	Use jls(8) utility to list running jails.

     -m      Modify  an  existing  jail.  One of the jid or name parameters must
	     exist and refer to an existing jail.  Some parameters  may  not  be
	     changed on a running jail.

     -r      Remove the jail specified by jid or name.	All jailed processes are
	     killed,  and  all jails that are children of this jail are also re-
	     moved.

```

## 引文摘录（空白已归一，供逐字核对）

Backward Compatibility jail [-dhilqv] [-J jid_file] [-u username] [-U username] [-n jailname] [-s securelevel] path hostname ip[,...] command ... DESCRIPTION The jail utility creates new jails, or modifies or removes existing jails. It can also print a list of configured jails and their parameters. A jail (or "prison") is specified via parameters on the command line, or in the jail.conf(5) file. At least one of the options -c, -e, -m or -r must be specified. These op- tions are used alone or in combination to describe the operation to per- form: -c Create a new jail. The jail jid and name parameters (if specified on the command line) must not refer to an existing jail. -e separator Exhibit a list of all configured non-wildcard jails and their para- meters. No jail creation, modification or removal performed if this option is used. The separator string is used to separate pa- rameters. Use jls(8) utility to list running jails. -m Modify an existing jail. One of the jid or name parameters must exist and refer to an existing jail. Some parameters may not be changed on a running jail. -r Remove the jail specified by jid or name. All jailed processes are killed, and all jails that are children of this jail are also re- moved.
