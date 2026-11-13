# auditreduce(1) — FreeBSD 用户命令手册页（审计踪迹记录选取）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=auditreduce&sektion=1
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.5“合规审计的工程含义”补证（D2 块）：判据检索面（D2 块，ref_id 见库）

## 抓取正文（节选）

```

SYNOPSIS
     auditreduce [-A] [-a YYYYMMDD[HH[MM[SS]]]] [-b YYYYMMDD[HH[MM[SS]]]]
		 [-c flags] [-d YYYYMMDD] [-e euid] [-f egid] [-g rgid] [-j id]
		 [-m event] [-o object=value] [-r ruid] [-u auid] [-v] [-z zone]
		 [file ...]

DESCRIPTION
     The auditreduce utility selects records from the audit trail files based on
     the specified criteria.  Matching audit records are printed to the standard
     output  in  their	raw  binary form.  If no file argument is specified, the
     standard input is used by default.  Use the praudit(1) utility to print the
     selected audit records in human-readable form.

     The options are as follows:

     -A      Select all records.

     -a YYYYMMDD[HH[MM[SS]]]
	     Select records that occurred after or on the given datetime.

     -b YYYYMMDD[HH[MM[SS]]]
	     Select records that occurred before the given datetime.

     -c flags
	     Select records matching the given	audit  classes	specified  as  a
	     comma  separated  list  of audit flags.  See audit_control(5) for a
	     description of audit flags.

     -d YYYYMMDD
	     Select records that occurred on a given date.  This  option  cannot
	     be used with -a or -b.

     -e euid
	     Select records with the given effective user ID or name.

     -f egid
	     Select records with the given effective group ID or name.
```

## 引文摘录（空白已归一，供逐字核对）

SYNOPSIS auditreduce [-A] [-a YYYYMMDD[HH[MM[SS]]]] [-b YYYYMMDD[HH[MM[SS]]]] [-c flags] [-d YYYYMMDD] [-e euid] [-f egid] [-g rgid] [-j id] [-m event] [-o object=value] [-r ruid] [-u auid] [-v] [-z zone] [file ...] DESCRIPTION The auditreduce utility selects records from the audit trail files based on the specified criteria. Matching audit records are printed to the standard output in their raw binary form. If no file argument is specified, the standard input is used by default. Use the praudit(1) utility to print the selected audit records in human-readable form. The options are as follows: -A Select all records. -a YYYYMMDD[HH[MM[SS]]] Select records that occurred after or on the given datetime. -b YYYYMMDD[HH[MM[SS]]] Select records that occurred before the given datetime. -c flags Select records matching the given audit classes specified as a comma separated list of audit flags. See audit_control(5) for a description of audit flags. -d YYYYMMDD Select records that occurred on a given date. This option cannot be used with -a or -b. -e euid Select records with the given effective user ID or name. -f egid Select records with the given effective group ID or name.
