# capsicum_helpers(3) — FreeBSD 库函数手册页（Capsicum 辅助函数集）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=capsicum_helpers&sektion=3
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.4.5“能力模型的应用迁移”补证（D2 块）：等效函数与降级兼容（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     void
     caph_cache_tzdata(void);

     void
     caph_cache_catpages(void);

DESCRIPTION
     The  caph_enter, caph_rights_limit, caph_ioctls_limit and caph_fcntls_limit
     are   respectively   equivalent   to   cap_enter(2),   cap_rights_limit(2),
     cap_ioctls_limit(2)  and  cap_fcntls_limit(2),  it returns success when the
     kernel is built without support of the capability mode.

     The caph_enter_casper is equivalent to the caph_enter  it	returns  success
     when the system is built without Casper support.

     The capsicum helpers are a set of a inline functions which simplify modify-
     ing  programs  to use Capsicum.  The goal is to reduce duplicated code pat-
     terns.  The capsicum helpers are part of libcapsicum but there is	no  need
     to link to the library.

     caph_limit_stream()  restricts  capabilities  on fd to only those needed by
     POSIX stream objects (that is, FILEs).

     These flags can be provided:

	   CAPH_IGNORE_EBADF  Do not return an error if file descriptor  is  in-
			      valid.
	   CAPH_READ	      Set CAP_READ on limited descriptor.
	   CAPH_WRITE	      Set CAP_WRITE on limited descriptor.

     caph_limit_stdin(), caph_limit_stderr() and caph_limit_stdout() limit stan-
     dard descriptors using the caph_limit_stream function.

     caph_limit_stdio() limits stdin, stderr and stdout.

     caph_stream_rights  may  be  used to initialize rights with the same rights
     that a stream would be limited to, as if caph_limit_stream() had  been  in-
     voked using the same flags.
```

## 引文摘录（空白已归一，供逐字核对）

void caph_cache_tzdata(void); void caph_cache_catpages(void); DESCRIPTION The caph_enter, caph_rights_limit, caph_ioctls_limit and caph_fcntls_limit are respectively equivalent to cap_enter(2), cap_rights_limit(2), cap_ioctls_limit(2) and cap_fcntls_limit(2), it returns success when the kernel is built without support of the capability mode. The caph_enter_casper is equivalent to the caph_enter it returns success when the system is built without Casper support. The capsicum helpers are a set of a inline functions which simplify modify- ing programs to use Capsicum. The goal is to reduce duplicated code pat- terns. The capsicum helpers are part of libcapsicum but there is no need to link to the library. caph_limit_stream() restricts capabilities on fd to only those needed by POSIX stream objects (that is, FILEs). These flags can be provided: CAPH_IGNORE_EBADF Do not return an error if file descriptor is in- valid. CAPH_READ Set CAP_READ on limited descriptor. CAPH_WRITE Set CAP_WRITE on limited descriptor. caph_limit_stdin(), caph_limit_stderr() and caph_limit_stdout() limit stan- dard descriptors using the caph_limit_stream function. caph_limit_stdio() limits stdin, stderr and stdout. caph_stream_rights may be used to initialize rights with the same rights that a stream would be limited to, as if caph_limit_stream() had been in- voked using the same flags.
