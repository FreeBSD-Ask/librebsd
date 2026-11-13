# auditpipe(4) — FreeBSD 内核接口手册页（实时审计事件跟踪伪设备）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=auditpipe&sektion=4
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.3“内核审计的挂钩点”补证（D2 块）：审计管道 tee（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     files are owned by the audit daemon until terminated making  them	somewhat
     unwieldy  for live monitoring applications such as host-based intrusion de-
     tection.  For example, the log may be cycled and new records written  to  a
     new file without notice to applications that may be accessing the file.

     The audit facility provides an audit pipe facility for applications requir-
     ing direct access to live BSM audit data for the purposes of real-time mon-
     itoring.	Audit  pipes  are  available  via  a  clonable	special  device,
     /dev/auditpipe, subject to the permissions on the device node, and  provide
     a	"tee"  of  the audit event stream.  As the device is clonable, more than
     one instance of the device may be opened at a time;  each	device	instance
     will provide independent access to all records.

     The  audit  pipe  device  provides  discrete BSM audit records; if the read
     buffer passed by the application is too small to hold the	next  record  in
     the  sequence,  it will be dropped.  Unlike audit data written to the audit
     trail, the reliability of record delivery is not guaranteed.   In	particu-
     lar,  when  an audit pipe queue fills, records will be dropped.  Audit pipe
     devices are blocking by default, but support non-blocking I/O, asynchronous
     I/O using SIGIO, and polled operation via select(2) and poll(2).

     Applications may choose to track the global audit trail, or configure local
     preselection parameters independent of the global audit trail parameters.

   Audit Pipe Queue Ioctls
     The following ioctls retrieve and set various audit pipe record queue prop-
     erties:

     AUDITPIPE_GET_QLEN 	 Query the current number of  records  available
				 for reading on the pipe.

     AUDITPIPE_GET_QLIMIT	 Retrieve  the current maximum number of records
				 that may be queued for reading on the pipe.

     AUDITPIPE_SET_QLIMIT	 Set the current maximum number of records  that
				 may be queued for reading on the pipe.  The new
				 limit must fall between the queue limit minimum
				 and  queue  limit  maximum  queryable using the
```

## 引文摘录（空白已归一，供逐字核对）

files are owned by the audit daemon until terminated making them somewhat unwieldy for live monitoring applications such as host-based intrusion de- tection. For example, the log may be cycled and new records written to a new file without notice to applications that may be accessing the file. The audit facility provides an audit pipe facility for applications requir- ing direct access to live BSM audit data for the purposes of real-time mon- itoring. Audit pipes are available via a clonable special device, /dev/auditpipe, subject to the permissions on the device node, and provide a "tee" of the audit event stream. As the device is clonable, more than one instance of the device may be opened at a time; each device instance will provide independent access to all records. The audit pipe device provides discrete BSM audit records; if the read buffer passed by the application is too small to hold the next record in the sequence, it will be dropped. Unlike audit data written to the audit trail, the reliability of record delivery is not guaranteed. In particu- lar, when an audit pipe queue fills, records will be dropped. Audit pipe devices are blocking by default, but support non-blocking I/O, asynchronous I/O using SIGIO, and polled operation via select(2) and poll(2). Applications may choose to track the global audit trail, or configure local preselection parameters independent of the global audit trail parameters. Audit Pipe Queue Ioctls The following ioctls retrieve and set various audit pipe record queue prop- erties: AUDITPIPE_GET_QLEN Query the current number of records available for reading on the pipe. AUDITPIPE_GET_QLIMIT Retrieve the current maximum number of records that may be queued for reading on the pipe. AUDITPIPE_SET_QLIMIT Set the current maximum number of records that may be queued for reading on the pipe. The new limit must fall between the queue limit minimum and queue limit maximum queryable using the
