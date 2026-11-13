# jail.conf(5) — FreeBSD 文件格式手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=jail.conf&sektion=5
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.1.5“Jail 与进程树的管辖”补证（D2 块）：具名定义与参数赋值（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     The  jail.conf file consists of one or more jail definitions statements for
     use by the jail(8) management program.  A jail  definition  statement  con-
     sists  of	a  single  word, the name of the jail, an opening curly brace, a
     list of at least two parameter assignments, and a closing curly  brace.   A
     parameter	assignment  consists  of  a  single word, the parameter name, an
     equals sign, a value enclosed in double quotes,  and  a  terminating  semi-
     colon.

     The syntax of a jail definition is as follows:

	   jailname {
	       parameter = "value";
	       ...
	   }

     This  is  used  by jail(8) to specify a jail on the command line and report
     the jail status, and is also passed to the kernel when creating the jail.

   Parameters
     A jail is defined by a set of named parameters, specified inside  the  jail
     definition.   See	jail(8) for a list of jail parameters passed to the ker-
     nel, as well as internal parameters used when creating and removing jails.

     A typical parameter has a name and a value.  Some	parameters  are  boolean
     and  may  be  specified  with  values of "true" or "false", or as valueless
     shortcuts, with a "no" prefix indicating a false value.  For example, these
     are equivalent:

	   allow.mount = "false";
	   allow.nomount;

     Other parameters may have more than one value.  A comma-separated	list  of
     values  may be set in a single statement, or an existing parameter list may
     be appended to using "+=":

	   ip4.addr = 10.1.1.1, 10.1.1.2, 10.1.1.3;

	   ip4.addr = 10.1.1.1;
```

## 引文摘录（空白已归一，供逐字核对）

The jail.conf file consists of one or more jail definitions statements for use by the jail(8) management program. A jail definition statement con- sists of a single word, the name of the jail, an opening curly brace, a list of at least two parameter assignments, and a closing curly brace. A parameter assignment consists of a single word, the parameter name, an equals sign, a value enclosed in double quotes, and a terminating semi- colon. The syntax of a jail definition is as follows: jailname { parameter = "value"; ... } This is used by jail(8) to specify a jail on the command line and report the jail status, and is also passed to the kernel when creating the jail. Parameters A jail is defined by a set of named parameters, specified inside the jail definition. See jail(8) for a list of jail parameters passed to the ker- nel, as well as internal parameters used when creating and removing jails. A typical parameter has a name and a value. Some parameters are boolean and may be specified with values of "true" or "false", or as valueless shortcuts, with a "no" prefix indicating a false value. For example, these are equivalent: allow.mount = "false"; allow.nomount; Other parameters may have more than one value. A comma-separated list of values may be set in a single statement, or an existing parameter list may be appended to using "+=": ip4.addr = 10.1.1.1, 10.1.1.2, 10.1.1.3; ip4.addr = 10.1.1.1;
