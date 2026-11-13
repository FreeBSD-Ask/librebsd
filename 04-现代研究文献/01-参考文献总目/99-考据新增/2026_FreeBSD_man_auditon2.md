# auditon(2) — FreeBSD 系统调用手册页（配置系统审计参数）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=auditon&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.4“审计策略的配置粒度”补证（D2 块）：A_SETPOLICY 位清单（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     auditon(int cmd, void *data, u_int length);

DESCRIPTION
     The auditon() system call is used to manipulate various audit control oper-
     ations.   The  data argument should point to a structure whose type depends
     on the command.  The length argument specifies the size of *data in  bytes.
     The cmd argument may be any of the following:

     A_SETPOLICY      Set audit policy flags.  The data argument must point to a
		      int  value  set  to one or more the following audit policy
		      control  values	bitwise   OR'ed   together:   AUDIT_CNT,
		      AUDIT_AHLT,  AUDIT_ARGV,	and AUDIT_ARGE.  If AUDIT_CNT is
		      set, the system will continue even if it	becomes  low  on
		      space  and  discontinue logging events until the low space
		      condition is remedied.  If it is not set,  audited  events
		      will  block  until  the  low  space condition is remedied.
		      Unaudited events, however, are unaffected.  If  AUDIT_AHLT
		      is  set,	a  panic(9)  if  it cannot write an event to the
		      global audit log file.  If AUDIT_ARGV is set, then the ar-
		      gument list passed to the execve(2) system  call	will  be
		      audited.	If AUDIT_ARGE is set, then the environment vari-
		      ables passed to the execve(2) system call will be audited.
		      The  default  policy  is	none of the audit policy control
		      flags set.

     A_SETKAUDIT      Set the host information.  The data argument must point to
		      a auditinfo_addr_t structure containing the  host  IP  ad-
		      dress  information.  After setting, audit records that are
		      created as a result of kernel events will contain this in-
		      formation.

     A_SETKMASK       Set the kernel preselection masks (success  and  failure).
		      The data argument must point to a au_mask_t structure con-
		      taining  the  mask  values  as  defined  in <bsm/audit.h>.
		      These masks are used for non-attributable audit event pre-
		      selection.  The field am_success specifies  which  classes
		      of  successful  audit events are to be logged to the audit
		      trail.  The field am_failure specifies  which  classes  of
```

## 引文摘录（空白已归一，供逐字核对）

auditon(int cmd, void *data, u_int length); DESCRIPTION The auditon() system call is used to manipulate various audit control oper- ations. The data argument should point to a structure whose type depends on the command. The length argument specifies the size of *data in bytes. The cmd argument may be any of the following: A_SETPOLICY Set audit policy flags. The data argument must point to a int value set to one or more the following audit policy control values bitwise OR'ed together: AUDIT_CNT, AUDIT_AHLT, AUDIT_ARGV, and AUDIT_ARGE. If AUDIT_CNT is set, the system will continue even if it becomes low on space and discontinue logging events until the low space condition is remedied. If it is not set, audited events will block until the low space condition is remedied. Unaudited events, however, are unaffected. If AUDIT_AHLT is set, a panic(9) if it cannot write an event to the global audit log file. If AUDIT_ARGV is set, then the ar- gument list passed to the execve(2) system call will be audited. If AUDIT_ARGE is set, then the environment vari- ables passed to the execve(2) system call will be audited. The default policy is none of the audit policy control flags set. A_SETKAUDIT Set the host information. The data argument must point to a auditinfo_addr_t structure containing the host IP ad- dress information. After setting, audit records that are created as a result of kernel events will contain this in- formation. A_SETKMASK Set the kernel preselection masks (success and failure). The data argument must point to a au_mask_t structure con- taining the mask values as defined in <bsm/audit.h>. These masks are used for non-attributable audit event pre- selection. The field am_success specifies which classes of successful audit events are to be logged to the audit trail. The field am_failure specifies which classes of
