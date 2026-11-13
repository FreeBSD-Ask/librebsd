# capsicum(4) — FreeBSD 内核接口手册页（Capsicum 能力与沙箱框架）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=capsicum&sektion=4
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.1“Capsicum 的能力句柄”／V37.5.4.2“能力模式的进程沙箱”补证（D2 块）：描述符→能力令牌＋标志继承（D2 块，ref_id 见库）

## 抓取正文（节选）

```
DESCRIPTION
     Capsicum  is a lightweight OS capability and sandbox framework implementing
     a hybrid capability system model.	Capsicum is designed to blend  capabili-
     ties with UNIX.  This approach achieves many of the benefits of least-priv-
     ilege  operation,	while preserving existing UNIX APIs and performance, and
     presents application authors with an adoption path for  capability-oriented
     design.

     Capabilities  are unforgeable tokens of authority that can be delegated and
     must be presented to perform an action.  Capsicum	makes  file  descriptors
     into capabilities.

     Capsicum  can be used for application and library compartmentalisation, the
     decomposition of larger bodies of software into isolated (sandboxed) compo-
     nents in order to implement security policies and limit the impact of soft-
     ware vulnerabilities.

     Capsicum provides two core kernel primitives:

     capability mode
	     A process mode, entered by invoking cap_enter(2), in  which  access
	     to  global  OS  namespaces  (such	as the file system and PID name-
	     spaces) is restricted; only explicitly delegated rights, referenced
	     by memory mappings or file descriptors, may be used.  Once set, the
	     flag is inherited by future children  processes,  and  may  not  be
	     cleared.

	     Access  to system calls in capability mode is restricted: some sys-
	     tem calls requiring global namespace access are unavailable,  while
	     others  are  constrained.	 For  instance, sysctl(2) can be used to
	     query process-local information such as address space  layout,  but
	     also  to monitor a system's network connections.  sysctl(2) is con-
	     strained by explicitly marking ~~60 of  over  15000  parameters  as
	     permitted in capability mode; all others are denied.

	     The   system   calls   which  require  constraints  are  sysctl(2),
	     shm_open(2) (which is permitted to create anonymous memory  objects
	     but  not named ones) and the openat(2) family of system calls.  The
```

## 引文摘录（空白已归一，供逐字核对）

DESCRIPTION Capsicum is a lightweight OS capability and sandbox framework implementing a hybrid capability system model. Capsicum is designed to blend capabili- ties with UNIX. This approach achieves many of the benefits of least-priv- ilege operation, while preserving existing UNIX APIs and performance, and presents application authors with an adoption path for capability-oriented design. Capabilities are unforgeable tokens of authority that can be delegated and must be presented to perform an action. Capsicum makes file descriptors into capabilities. Capsicum can be used for application and library compartmentalisation, the decomposition of larger bodies of software into isolated (sandboxed) compo- nents in order to implement security policies and limit the impact of soft- ware vulnerabilities. Capsicum provides two core kernel primitives: capability mode A process mode, entered by invoking cap_enter(2), in which access to global OS namespaces (such as the file system and PID name- spaces) is restricted; only explicitly delegated rights, referenced by memory mappings or file descriptors, may be used. Once set, the flag is inherited by future children processes, and may not be cleared. Access to system calls in capability mode is restricted: some sys- tem calls requiring global namespace access are unavailable, while others are constrained. For instance, sysctl(2) can be used to query process-local information such as address space layout, but also to monitor a system's network connections. sysctl(2) is con- strained by explicitly marking ~~60 of over 15000 parameters as permitted in capability mode; all others are denied. The system calls which require constraints are sysctl(2), shm_open(2) (which is permitted to create anonymous memory objects but not named ones) and the openat(2) family of system calls. The
