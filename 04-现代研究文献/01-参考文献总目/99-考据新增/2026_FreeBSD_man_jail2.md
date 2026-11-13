# jail(2) — FreeBSD 系统调用手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=2
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.1.5“Jail 与进程树的管辖”补证（D2 块）：进程锁入 prison（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     int
     jail_get(struct iovec *iov, u_int niov, int flags);

     int
     jail_set(struct iovec *iov, u_int niov, int flags);

DESCRIPTION
     The jail() system call sets up a jail and locks the current process in it.

     The argument is a pointer to a structure describing the prison:

	   struct jail {
		   uint32_t	   version;
		   char 	   *path;
		   char 	   *hostname;
		   char 	   *jailname;
		   unsigned int    ip4s;
		   unsigned int    ip6s;
		   struct in_addr  *ip4;
		   struct in6_addr *ip6;
	   };

     "version" defines the version of the API in use.  JAIL_API_VERSION  is  de-
     fined for the current version.

     The  "path"  pointer should be set to the directory which is to be the root
     of the prison.

     The "hostname" pointer can be set to the hostname of the prison.  This  can
     be changed from the inside of the prison.

     The "jailname" pointer is an optional name that can be assigned to the jail
     for example for management purposes.

     The "ip4s" and "ip6s" give the numbers of IPv4 and IPv6 addresses that will
     be passed via their respective pointers.

```

## 引文摘录（空白已归一，供逐字核对）

int jail_get(struct iovec *iov, u_int niov, int flags); int jail_set(struct iovec *iov, u_int niov, int flags); DESCRIPTION The jail() system call sets up a jail and locks the current process in it. The argument is a pointer to a structure describing the prison: struct jail { uint32_t version; char *path; char *hostname; char *jailname; unsigned int ip4s; unsigned int ip6s; struct in_addr *ip4; struct in6_addr *ip6; }; "version" defines the version of the API in use. JAIL_API_VERSION is de- fined for the current version. The "path" pointer should be set to the directory which is to be the root of the prison. The "hostname" pointer can be set to the hostname of the prison. This can be changed from the inside of the prison. The "jailname" pointer is an optional name that can be assigned to the jail for example for management purposes. The "ip4s" and "ip6s" give the numbers of IPv4 and IPv6 addresses that will be passed via their respective pointers.
