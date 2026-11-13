# cap_fcntls_limit(2) — FreeBSD 系统调用手册页（fcntl 命令白名单）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=cap_fcntls_limit&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.3“文件描述符的权利收缩”补证（D2 块）：fcntl 命令面逐项收缩（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     int
     cap_fcntls_limit(int fd, uint32_t fcntlrights);

     int
     cap_fcntls_get(int fd, uint32_t *fcntlrightsp);

DESCRIPTION
     If a file descriptor is granted the CAP_FCNTL capability right, the list of
     allowed  fcntl(2)	commands can be selectively reduced (but never expanded)
     with the cap_fcntls_limit() system call.

     A bitmask of allowed fcntls commands for a given file descriptor can be ob-
     tained with the cap_fcntls_get() system call.

FLAGS
     The following flags may be specified in the  fcntlrights  argument  or  re-
     turned in the fcntlrightsp argument:

     CAP_FCNTL_GETFL   Permit F_GETFL command.

     CAP_FCNTL_SETFL   Permit F_SETFL command.

     CAP_FCNTL_GETOWN  Permit F_GETOWN command.

     CAP_FCNTL_SETOWN  Permit F_SETOWN command.

RETURN VALUES
     Upon successful completion, the value 0 is returned; otherwise the value -1
     is returned and the global variable errno is set to indicate the error.

ERRORS
     cap_fcntls_limit() succeeds unless:

     [EBADF]		The fd argument is not a valid descriptor.

     [EINVAL]		An invalid flag has been passed in fcntlrights.

```

## 引文摘录（空白已归一，供逐字核对）

int cap_fcntls_limit(int fd, uint32_t fcntlrights); int cap_fcntls_get(int fd, uint32_t *fcntlrightsp); DESCRIPTION If a file descriptor is granted the CAP_FCNTL capability right, the list of allowed fcntl(2) commands can be selectively reduced (but never expanded) with the cap_fcntls_limit() system call. A bitmask of allowed fcntls commands for a given file descriptor can be ob- tained with the cap_fcntls_get() system call. FLAGS The following flags may be specified in the fcntlrights argument or re- turned in the fcntlrightsp argument: CAP_FCNTL_GETFL Permit F_GETFL command. CAP_FCNTL_SETFL Permit F_SETFL command. CAP_FCNTL_GETOWN Permit F_GETOWN command. CAP_FCNTL_SETOWN Permit F_SETOWN command. RETURN VALUES Upon successful completion, the value 0 is returned; otherwise the value -1 is returned and the global variable errno is set to indicate the error. ERRORS cap_fcntls_limit() succeeds unless: [EBADF] The fd argument is not a valid descriptor. [EINVAL] An invalid flag has been passed in fcntlrights.
