# audit_control(5) — FreeBSD 文件格式手册页（审计系统参数）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=audit_control&sektion=5
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.4“审计策略的配置粒度”补证（D2 块）：类别清单＋前缀（D2 块，ref_id 见库）

## 抓取正文（节选）

```
	     records extracted from the queue and currently being  prepared  for
	     or  undergoing  I/O.   Other  operational limits may be affected by
	     this parameter, such as the minimum free space on disk required  to
	     continue  system  operation, estimated as the maximum number of al-
	     lowable in-flight records multiplied by the  maximum  audit  record
	     size.

AUDIT FLAGS
     Audit  flags  are a comma-delimited list of audit classes as defined in the
     audit_class(5) file.  Event classes may  be  preceded  by	a  prefix  which
     changes  their interpretation.  The following prefixes may be used for each
     class:

	   (none)  Record both successful and failed events.
	   +	   Record successful events.
	   -	   Record failed events.
	   ^	   Record neither successful nor failed events.
	   ^+	   Do not record successful events.
	   ^-	   Do not record failed events.

AUDIT POLICY FLAGS
     The policy flags field is a comma-delimited list of policy flags  from  the
     following list:

	   cnt	     Allow  processes to continue running even though events are
		     not being audited.  If not set, processes will be suspended
		     when the audit store space is exhausted.	Currently,  this
		     is not a recoverable state.
	   ahlt      Fail stop the system if unable to audit an event--this con-
		     sists  of	first draining pending records to disk, and then
		     halting the operating system.
	   argv      Audit command line arguments to execve(2).
	   arge      Audit environmental variable arguments to execve(2).
	   seq	     Include a unique audit sequence number token  in  generated
		     audit records (not implemented on FreeBSD or Darwin).
	   group     Include   supplementary  groups  list  in	generated  audit
		     records (not implemented on FreeBSD or  Darwin;  supplemen-
		     tary  groups  are	never  included in records on these sys-
```

## 引文摘录（空白已归一，供逐字核对）

records extracted from the queue and currently being prepared for or undergoing I/O. Other operational limits may be affected by this parameter, such as the minimum free space on disk required to continue system operation, estimated as the maximum number of al- lowable in-flight records multiplied by the maximum audit record size. AUDIT FLAGS Audit flags are a comma-delimited list of audit classes as defined in the audit_class(5) file. Event classes may be preceded by a prefix which changes their interpretation. The following prefixes may be used for each class: (none) Record both successful and failed events. + Record successful events. - Record failed events. ^ Record neither successful nor failed events. ^+ Do not record successful events. ^- Do not record failed events. AUDIT POLICY FLAGS The policy flags field is a comma-delimited list of policy flags from the following list: cnt Allow processes to continue running even though events are not being audited. If not set, processes will be suspended when the audit store space is exhausted. Currently, this is not a recoverable state. ahlt Fail stop the system if unable to audit an event--this con- sists of first draining pending records to disk, and then halting the operating system. argv Audit command line arguments to execve(2). arge Audit environmental variable arguments to execve(2). seq Include a unique audit sequence number token in generated audit records (not implemented on FreeBSD or Darwin). group Include supplementary groups list in generated audit records (not implemented on FreeBSD or Darwin; supplemen- tary groups are never included in records on these sys-
