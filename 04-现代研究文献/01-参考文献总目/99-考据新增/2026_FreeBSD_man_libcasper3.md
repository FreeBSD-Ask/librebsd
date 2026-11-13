# libcasper(3) — FreeBSD 库函数手册页（casper 应用能力库）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=libcasper&sektion=3
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.5“能力模型的应用迁移”补证（D2 块）：服务能力通道（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     The cap_recv_nvlist() function receives the given nvlist(9) over the  given
     capability.

     The  cap_xfer_nvlist() function sends the given nvlist(9), destroys it, and
     receives a new nvlist(9) in response over the given  capability.	It  does
     not matter if the function succeeds or fails, the nvlist(9) given for send-
     ing will always be destroyed before the function returns.

     The  cap_service_open() function opens the casper service named in the call
     using the casper capability obtained  via	the  cap_init()  function.   The
     cap_service_open()  function  returns  a capability that provides access to
     the opened service.  Casper supports the following  services  in  the  base
     system:

	   system.dns	  provides libc compatible DNS API
	   system.fileargs
			  provides  an API for opening files specified on a com-
			  mand line
	   system.grp	  provides a getgrent(3) compatible API
	   system.net	  provides a libc compatible network API
	   system.netdb   provides libc compatible network proto API
	   system.pwd	  provides a getpwent(3) compatible API
	   system.sysctl  provides a sysctlbyname(3) compatible API
	   system.syslog  provides a syslog(3) compatible API

     cap_init() must be called from  a	single-threaded  context.   cap_clone(),
     cap_close(),     cap_limit_get(),	  cap_limit_set(),    cap_send_nvlist(),
     cap_recv_nvlist(), and cap_service_open() are  reentrant  but  not  thread-
     safe.   That is, they may be called from separate threads only with differ-
     ent cap_channel_t arguments or with synchronization.

RETURN VALUES
     The   cap_clone(),   cap_init(),	cap_recv_nvlist(),   cap_service_open(),
     cap_wrap()  and  cap_xfer_nvlist()  functions return NULL and set the errno
     variable on failure.

     The cap_limit_get(), cap_limit_set() and cap_send_nvlist() functions return
     -1 and set the errno variable on failure.
```

## 引文摘录（空白已归一，供逐字核对）

The cap_recv_nvlist() function receives the given nvlist(9) over the given capability. The cap_xfer_nvlist() function sends the given nvlist(9), destroys it, and receives a new nvlist(9) in response over the given capability. It does not matter if the function succeeds or fails, the nvlist(9) given for send- ing will always be destroyed before the function returns. The cap_service_open() function opens the casper service named in the call using the casper capability obtained via the cap_init() function. The cap_service_open() function returns a capability that provides access to the opened service. Casper supports the following services in the base system: system.dns provides libc compatible DNS API system.fileargs provides an API for opening files specified on a com- mand line system.grp provides a getgrent(3) compatible API system.net provides a libc compatible network API system.netdb provides libc compatible network proto API system.pwd provides a getpwent(3) compatible API system.sysctl provides a sysctlbyname(3) compatible API system.syslog provides a syslog(3) compatible API cap_init() must be called from a single-threaded context. cap_clone(), cap_close(), cap_limit_get(), cap_limit_set(), cap_send_nvlist(), cap_recv_nvlist(), and cap_service_open() are reentrant but not thread- safe. That is, they may be called from separate threads only with differ- ent cap_channel_t arguments or with synchronization. RETURN VALUES The cap_clone(), cap_init(), cap_recv_nvlist(), cap_service_open(), cap_wrap() and cap_xfer_nvlist() functions return NULL and set the errno variable on failure. The cap_limit_get(), cap_limit_set() and cap_send_nvlist() functions return -1 and set the errno variable on failure.
