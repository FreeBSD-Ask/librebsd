# audit_event(5) — FreeBSD 文件格式手册页（可审计事件登记）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=audit_event&sektion=5
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.1“OpenBSM 的审计事件构型”补证（D2 块）：事件四元组登记（D2 块，ref_id 见库）

## 抓取正文（节选）

```
AUDIT_EVENT(5)		       File Formats Manual		  AUDIT_EVENT(5)

NAME
     audit_event -- audit event descriptions

DESCRIPTION
     The  audit_event  file contains descriptions of the auditable events on the
     system.  Each line maps an audit event number to a name, a description, and
     a class.  Entries are of the form:

	   eventnum:eventname:description:eventclass

     Each eventclass should have a corresponding  entry  in  the  audit_class(5)
     file.

     Example entries in this file are:

	   0:AUE_NULL:indir system call:no
	   1:AUE_EXIT:exit(2):pc
	   2:AUE_FORK:fork(2):pc
	   3:AUE_OPEN:open(2):fa

FILES
     /etc/security/audit_event

SEE ALSO
     audit(4), audit_class(5), audit_control(5), audit_user(5)

HISTORY
     The OpenBSM implementation was created by McAfee Research, the security di-
     vision  of  McAfee Inc., under contract to Apple Computer Inc. in 2004.  It
     was subsequently adopted by the TrustedBSD Project as  the  foundation  for
     the OpenBSM distribution.

AUTHORS
     This  software  was created by McAfee Research, the security research divi-
     sion of McAfee, Inc., under contract to Apple Computer Inc.  Additional au-
```

## 引文摘录（空白已归一，供逐字核对）

AUDIT_EVENT(5) File Formats Manual AUDIT_EVENT(5) NAME audit_event -- audit event descriptions DESCRIPTION The audit_event file contains descriptions of the auditable events on the system. Each line maps an audit event number to a name, a description, and a class. Entries are of the form: eventnum:eventname:description:eventclass Each eventclass should have a corresponding entry in the audit_class(5) file. Example entries in this file are: 0:AUE_NULL:indir system call:no 1:AUE_EXIT:exit(2):pc 2:AUE_FORK:fork(2):pc 3:AUE_OPEN:open(2):fa FILES /etc/security/audit_event SEE ALSO audit(4), audit_class(5), audit_control(5), audit_user(5) HISTORY The OpenBSM implementation was created by McAfee Research, the security di- vision of McAfee Inc., under contract to Apple Computer Inc. in 2004. It was subsequently adopted by the TrustedBSD Project as the foundation for the OpenBSM distribution. AUTHORS This software was created by McAfee Research, the security research divi- sion of McAfee, Inc., under contract to Apple Computer Inc. Additional au-
