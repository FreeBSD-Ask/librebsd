# cap_rights_limit(2) — FreeBSD 系统调用手册页（能力权利收窄）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=cap_rights_limit&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.1“Capsicum 的能力句柄”补证（D2 块）：权利只收不放（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     int
     cap_rights_limit(int fd, const cap_rights_t *rights);

DESCRIPTION
     When  a  file  descriptor	is  created  by  a  function  such as fhopen(2),
     kqueue(2), mq_open(2), open(2), pdfork(2), pipe(2), shm_open(2),  socket(2)
     or  socketpair(2), it is assigned all capability rights; for accept(2), ac-
     cept4(2) or openat(2), it inherits capability rights from the "parent" file
     descriptor.  Those rights can be reduced (but never expanded) by using  the
     cap_rights_limit() system call.  Once capability rights are reduced, opera-
     tions on the file descriptor will be limited to those permitted by rights.

     The  rights  argument should be prepared using cap_rights_init(3) family of
     functions.

     Capability rights assigned to a file descriptor can be  obtained  with  the
     cap_rights_get(3) function.

     The  complete  list  of the capability rights can be found in the rights(4)
     manual page.

RETURN VALUES
     Upon successful completion, the value 0 is returned; otherwise the value -1
     is returned and the global variable errno is set to indicate the error.

EXAMPLES
     The following example demonstrates how to limit file descriptor  capability
     rights to allow reading only.

     cap_rights_t setrights;
     char buf[1];
     int fd;

     fd = open("/tmp/foo", O_RDWR);
     if (fd < 0)
	     err(1, "open() failed");

     if (cap_enter() < 0)
```

## 引文摘录（空白已归一，供逐字核对）

int cap_rights_limit(int fd, const cap_rights_t *rights); DESCRIPTION When a file descriptor is created by a function such as fhopen(2), kqueue(2), mq_open(2), open(2), pdfork(2), pipe(2), shm_open(2), socket(2) or socketpair(2), it is assigned all capability rights; for accept(2), ac- cept4(2) or openat(2), it inherits capability rights from the "parent" file descriptor. Those rights can be reduced (but never expanded) by using the cap_rights_limit() system call. Once capability rights are reduced, opera- tions on the file descriptor will be limited to those permitted by rights. The rights argument should be prepared using cap_rights_init(3) family of functions. Capability rights assigned to a file descriptor can be obtained with the cap_rights_get(3) function. The complete list of the capability rights can be found in the rights(4) manual page. RETURN VALUES Upon successful completion, the value 0 is returned; otherwise the value -1 is returned and the global variable errno is set to indicate the error. EXAMPLES The following example demonstrates how to limit file descriptor capability rights to allow reading only. cap_rights_t setrights; char buf[1]; int fd; fd = open("/tmp/foo", O_RDWR); if (fd < 0) err(1, "open() failed"); if (cap_enter() < 0)
