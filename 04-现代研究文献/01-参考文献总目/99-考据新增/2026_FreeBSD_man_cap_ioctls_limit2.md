# cap_ioctls_limit(2) — FreeBSD 系统调用手册页（ioctl 命令数组白名单）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=cap_ioctls_limit&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.3“文件描述符的权利收缩”补证（D2 块）：ioctl 命令数组白名单（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     int
     cap_ioctls_limit(int fd, const unsigned long *cmds, size_t ncmds);

     ssize_t
     cap_ioctls_get(int fd, unsigned long *cmds, size_t maxcmds);

DESCRIPTION
     If a file descriptor is granted the CAP_IOCTL capability right, the list of
     allowed  ioctl(2)	commands can be selectively reduced (but never expanded)
     with the cap_ioctls_limit() system call.  The cmds argument is an array  of
     ioctl(2)  commands  and the ncmds argument specifies the number of elements
     in the array.  There can be up to 256 elements in the array.  Including  an
     element  that  has been previously revoked will generate an error.  After a
     successful call only those listed in the array may be used.

     The list of allowed ioctl commands for a given file descriptor can  be  ob-
     tained  with the cap_ioctls_get() system call.  The cmds argument points at
     memory that can hold up to maxcmds values.  The function populates the pro-
     vided buffer with up to maxcmds elements, but always returns the total num-
     ber of ioctl commands allowed for the given  file	descriptor.   The  total
     number  of ioctls commands for the given file descriptor can be obtained by
     passing NULL as the cmds argument and 0 as the maxcmds  argument.	 If  all
     ioctl  commands  are allowed (CAP_IOCTL capability right is assigned to the
     file descriptor and the cap_ioctls_limit() system call was never called for
     this  file  descriptor),  the  cap_ioctls_get()  system  call  will  return
     CAP_IOCTLS_ALL  and will not modify the buffer pointed to by the cmds argu-
     ment.

RETURN VALUES
     The cap_ioctls_limit() function returns the value 0 if  successful;  other-
     wise the value -1 is returned and the global variable errno is set to indi-
     cate the error.

     The  cap_ioctls_get()  function, if successful, returns the total number of
     allowed ioctl commands or the value CAP_IOCTLS_ALL if all	ioctls	commands
     are  allowed.   On failure the value -1 is returned and the global variable
     errno is set to indicate the error.
```

## 引文摘录（空白已归一，供逐字核对）

int cap_ioctls_limit(int fd, const unsigned long *cmds, size_t ncmds); ssize_t cap_ioctls_get(int fd, unsigned long *cmds, size_t maxcmds); DESCRIPTION If a file descriptor is granted the CAP_IOCTL capability right, the list of allowed ioctl(2) commands can be selectively reduced (but never expanded) with the cap_ioctls_limit() system call. The cmds argument is an array of ioctl(2) commands and the ncmds argument specifies the number of elements in the array. There can be up to 256 elements in the array. Including an element that has been previously revoked will generate an error. After a successful call only those listed in the array may be used. The list of allowed ioctl commands for a given file descriptor can be ob- tained with the cap_ioctls_get() system call. The cmds argument points at memory that can hold up to maxcmds values. The function populates the pro- vided buffer with up to maxcmds elements, but always returns the total num- ber of ioctl commands allowed for the given file descriptor. The total number of ioctls commands for the given file descriptor can be obtained by passing NULL as the cmds argument and 0 as the maxcmds argument. If all ioctl commands are allowed (CAP_IOCTL capability right is assigned to the file descriptor and the cap_ioctls_limit() system call was never called for this file descriptor), the cap_ioctls_get() system call will return CAP_IOCTLS_ALL and will not modify the buffer pointed to by the cmds argu- ment. RETURN VALUES The cap_ioctls_limit() function returns the value 0 if successful; other- wise the value -1 is returned and the global variable errno is set to indi- cate the error. The cap_ioctls_get() function, if successful, returns the total number of allowed ioctl commands or the value CAP_IOCTLS_ALL if all ioctls commands are allowed. On failure the value -1 is returned and the global variable errno is set to indicate the error.
