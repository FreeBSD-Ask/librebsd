# audit(4) — FreeBSD 内核接口手册页（安全事件审计设施）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=audit&sektion=4
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.2“审计日志的记录格式”／V37.5.2.3“内核审计的挂钩点”补证（D2 块）：BSM 标准承继＋dtaudit 捕获面（D2 块，ref_id 见库）

## 抓取正文（节选）

```

SYNOPSIS
     options AUDIT

DESCRIPTION
     Security  Event  Audit  is a facility to provide fine-grained, configurable
     logging of security-relevant events, and is intended to meet  the	require-
     ments  of	the Common Criteria (CC) Common Access Protection Profile (CAPP)
     evaluation.  The FreeBSD audit facility implements the  de  facto	industry
     standard  BSM API, file formats, and command line interface, first found in
     the Solaris operating system.  Information on the user space implementation
     can be found in libbsm(3).

     Audit support is enabled at boot,	if  present  in  the  kernel,  using  an
     rc.conf(5) flag.  The audit daemon, auditd(8), is responsible for configur-
     ing  the kernel to perform audit, pushing configuration data from the vari-
     ous audit configuration files into the kernel.

   Audit Special Device
     The kernel audit facility provides a special device, /dev/audit,  which  is
     used  by  auditd(8)  to monitor for audit events, such as requests to cycle
     the log, low disk space conditions, and  requests	to  terminate  auditing.
     This device is not intended for use by applications.

   Audit Pipe Special Devices
     Audit  pipe  special  devices, discussed in auditpipe(4), provide a config-
     urable live tracking mechanism to	allow  applications  to  tee  the  audit
     trail,  as  well  as  to  configure custom preselection parameters to track
     users and events in a fine-grained manner.

   DTrace Audit Provider
     The DTrace Audit Provider, dtaudit(4), allows D scripts to  enable  capture
     of  in-kernel  audit records for kernel audit event types, and then process
     their contents during audit commit or BSM generation.

SEE ALSO
     auditreduce(1), praudit(1), audit(2), auditctl(2), auditon(2), getaudit(2),
     getauid(2), poll(2), select(2), setaudit(2), setauid(2), libbsm(3),  audit-
```

## 引文摘录（空白已归一，供逐字核对）

SYNOPSIS options AUDIT DESCRIPTION Security Event Audit is a facility to provide fine-grained, configurable logging of security-relevant events, and is intended to meet the require- ments of the Common Criteria (CC) Common Access Protection Profile (CAPP) evaluation. The FreeBSD audit facility implements the de facto industry standard BSM API, file formats, and command line interface, first found in the Solaris operating system. Information on the user space implementation can be found in libbsm(3). Audit support is enabled at boot, if present in the kernel, using an rc.conf(5) flag. The audit daemon, auditd(8), is responsible for configur- ing the kernel to perform audit, pushing configuration data from the vari- ous audit configuration files into the kernel. Audit Special Device The kernel audit facility provides a special device, /dev/audit, which is used by auditd(8) to monitor for audit events, such as requests to cycle the log, low disk space conditions, and requests to terminate auditing. This device is not intended for use by applications. Audit Pipe Special Devices Audit pipe special devices, discussed in auditpipe(4), provide a config- urable live tracking mechanism to allow applications to tee the audit trail, as well as to configure custom preselection parameters to track users and events in a fine-grained manner. DTrace Audit Provider The DTrace Audit Provider, dtaudit(4), allows D scripts to enable capture of in-kernel audit records for kernel audit event types, and then process their contents during audit commit or BSM generation. SEE ALSO auditreduce(1), praudit(1), audit(2), auditctl(2), auditon(2), getaudit(2), getauid(2), poll(2), select(2), setaudit(2), setauid(2), libbsm(3), audit-
