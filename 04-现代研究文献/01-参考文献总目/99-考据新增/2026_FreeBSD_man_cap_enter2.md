# cap_enter(2) — FreeBSD 系统调用手册页（能力模式系统调用）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=cap_enter&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.2“能力模式的进程沙箱”补证（D2 块）：全局命名空间切断（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     cap_enter(void);

     int
     cap_getmode(u_int *modep);

DESCRIPTION
     cap_enter() places the current process into capability mode, a mode of exe-
     cution in which processes may only issue system calls operating on file de-
     scriptors	or  reading  limited global system state.  Access to global name
     spaces, such as file system or IPC  name  spaces,	is  prevented.	 If  the
     process  is  already in a capability mode sandbox, the system call is a no-
     op.  Future process descendants created with fork(2) or pdfork(2)	will  be
     placed in capability mode from inception.

     When   combined   with  cap_rights_limit(2),  cap_ioctls_limit(2),  cap_fc-
     ntls_limit(2), cap_enter() may be used to create kernel-enforced  sandboxes
     in  which	appropriately-crafted applications or application components may
     be run.

     cap_getmode() returns a flag indicating whether or not the process is in  a
     capability mode sandbox.

RUN-TIME SETTINGS
     If  the  kern.trap_enotcap  sysctl MIB is set to a non-zero value, then for
     any process executing in a capability mode sandbox, any syscall  which  re-
     sults  in	either	an ENOTCAPABLE or ECAPMODE error also generates the syn-
     chronous SIGTRAP signal to the thread on the syscall return.  On signal de-
     livery, the si_errno member of the siginfo signal handler parameter is  set
     to the syscall error value, and the si_code member is set to TRAP_CAP.

     See  also	the  PROC_TRAPCAP_CTL  and PROC_TRAPCAP_STATUS operations of the
     procctl(2) function for similar per-process functionality.

RETURN VALUES
     The cap_enter() and cap_getmode() functions return the value 0 if	success-
     ful;  otherwise  the  value -1 is returned and the global variable errno is
     set to indicate the error.

```

## 引文摘录（空白已归一，供逐字核对）

cap_enter(void); int cap_getmode(u_int *modep); DESCRIPTION cap_enter() places the current process into capability mode, a mode of exe- cution in which processes may only issue system calls operating on file de- scriptors or reading limited global system state. Access to global name spaces, such as file system or IPC name spaces, is prevented. If the process is already in a capability mode sandbox, the system call is a no- op. Future process descendants created with fork(2) or pdfork(2) will be placed in capability mode from inception. When combined with cap_rights_limit(2), cap_ioctls_limit(2), cap_fc- ntls_limit(2), cap_enter() may be used to create kernel-enforced sandboxes in which appropriately-crafted applications or application components may be run. cap_getmode() returns a flag indicating whether or not the process is in a capability mode sandbox. RUN-TIME SETTINGS If the kern.trap_enotcap sysctl MIB is set to a non-zero value, then for any process executing in a capability mode sandbox, any syscall which re- sults in either an ENOTCAPABLE or ECAPMODE error also generates the syn- chronous SIGTRAP signal to the thread on the syscall return. On signal de- livery, the si_errno member of the siginfo signal handler parameter is set to the syscall error value, and the si_code member is set to TRAP_CAP. See also the PROC_TRAPCAP_CTL and PROC_TRAPCAP_STATUS operations of the procctl(2) function for similar per-process functionality. RETURN VALUES The cap_enter() and cap_getmode() functions return the value 0 if success- ful; otherwise the value -1 is returned and the global variable errno is set to indicate the error.
