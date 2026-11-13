# audit(8) — FreeBSD 系统管理手册页（审计管理工具）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=audit&sektion=8
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.5“合规审计的工程含义”补证（D2 块）：过期判据驱动的留存（D2 块，ref_id 见库）

## 抓取正文（节选）

```

SYNOPSIS
     audit -e | -i | -n | -s | -t

DESCRIPTION
     The  audit utility controls the state of the audit system.  One of the fol-
     lowing flags is required as an argument to audit:

     -e      Forces the audit system to immediately remove audit log files  that
	     meet  the	expiration  criteria specified in the audit control file
	     without doing a log rotation.

     -i      Initializes and starts auditing.  This option is currently for  Mac
	     OS  X  only  and  requires  auditd(8) to be configured to run under
	     launchd(8).

     -n      Forces the audit system to close the existing audit  log  file  and
	     rotate  to a new log file in a location specified in the audit con-
	     trol file.  Also, audit log files that meet the expiration criteria
	     specified in the audit control file will be removed.

     -s      Specifies that the audit system should [re]synchronize its configu-
	     ration from the audit control file.  A new log file  will	be  cre-
	     ated.

     -t      Specifies	that  the  audit system should terminate.  Log files are
	     closed and renamed to indicate the time of the shutdown.

NOTES
     The auditd(8) daemon must already be running.  Optionally, it can	be  con-
     figured  to  be started on-demand by launchd(8) (Mac OS X only).  The audit
     utility requires audit administrator privileges for successful operation.

FILES
     /etc/security/audit_control  Audit policy file used to configure the audit-
				  ing system.

SEE ALSO
```

## 引文摘录（空白已归一，供逐字核对）

SYNOPSIS audit -e | -i | -n | -s | -t DESCRIPTION The audit utility controls the state of the audit system. One of the fol- lowing flags is required as an argument to audit: -e Forces the audit system to immediately remove audit log files that meet the expiration criteria specified in the audit control file without doing a log rotation. -i Initializes and starts auditing. This option is currently for Mac OS X only and requires auditd(8) to be configured to run under launchd(8). -n Forces the audit system to close the existing audit log file and rotate to a new log file in a location specified in the audit con- trol file. Also, audit log files that meet the expiration criteria specified in the audit control file will be removed. -s Specifies that the audit system should [re]synchronize its configu- ration from the audit control file. A new log file will be cre- ated. -t Specifies that the audit system should terminate. Log files are closed and renamed to indicate the time of the shutdown. NOTES The auditd(8) daemon must already be running. Optionally, it can be con- figured to be started on-demand by launchd(8) (Mac OS X only). The audit utility requires audit administrator privileges for successful operation. FILES /etc/security/audit_control Audit policy file used to configure the audit- ing system. SEE ALSO
