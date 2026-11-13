# audit_class(5) — FreeBSD 文件格式手册页（审计事件类别登记）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=audit_class&sektion=5
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.1“OpenBSM 的审计事件构型”补证（D2 块）：类别位掩码登记（D2 块，ref_id 见库）

## 抓取正文（节选）

```
AUDIT_CLASS(5)		       File Formats Manual		  AUDIT_CLASS(5)

NAME
     audit_class -- audit event class descriptions

DESCRIPTION
     The  audit_class  file contains descriptions of the auditable event classes
     on the system.  Each auditable event is a member of an event  class.   Each
     line  maps  an audit event mask (bitmap) to a class and a description.  En-
     tries are of the form:

	   classmask:eventclass:description

     Example entries in this file are:

	   0x00000000:no:invalid class
	   0x00000001:fr:file read
	   0x00000002:fw:file write
	   0x00000004:fa:file attribute access
	   0x00000080:pc:process
	   0xffffffff:all:all flags set

FILES
     /etc/security/audit_class

SEE ALSO
     audit(4), audit_control(5), audit_event(5), audit_user(5)

HISTORY
     The OpenBSM implementation was created by McAfee Research, the security di-
     vision of McAfee Inc., under contract to Apple Computer Inc. in  2004.   It
     was  subsequently	adopted  by the TrustedBSD Project as the foundation for
     the OpenBSM distribution.

AUTHORS
     This software was created by McAfee Research, the security  research  divi-
     sion of McAfee, Inc., under contract to Apple Computer Inc.  Additional au-
     thors include Wayne Salamon, Robert Watson, and SPARTA Inc.
```

## 引文摘录（空白已归一，供逐字核对）

AUDIT_CLASS(5) File Formats Manual AUDIT_CLASS(5) NAME audit_class -- audit event class descriptions DESCRIPTION The audit_class file contains descriptions of the auditable event classes on the system. Each auditable event is a member of an event class. Each line maps an audit event mask (bitmap) to a class and a description. En- tries are of the form: classmask:eventclass:description Example entries in this file are: 0x00000000:no:invalid class 0x00000001:fr:file read 0x00000002:fw:file write 0x00000004:fa:file attribute access 0x00000080:pc:process 0xffffffff:all:all flags set FILES /etc/security/audit_class SEE ALSO audit(4), audit_control(5), audit_event(5), audit_user(5) HISTORY The OpenBSM implementation was created by McAfee Research, the security di- vision of McAfee Inc., under contract to Apple Computer Inc. in 2004. It was subsequently adopted by the TrustedBSD Project as the foundation for the OpenBSM distribution. AUTHORS This software was created by McAfee Research, the security research divi- sion of McAfee, Inc., under contract to Apple Computer Inc. Additional au- thors include Wayne Salamon, Robert Watson, and SPARTA Inc.
