# FreeBSD sendfile(2) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=sendfile&sektion=2&manpath=FreeBSD+15.1-RELEASE+and+Ports.quarterly
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.12.4“sendfile 的零拷贝路径”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
SENDFILE(2)		       System Calls Manual		     SENDFILE(2)

NAME
     sendfile -- send a file to a socket

SYNOPSIS
     #include <sys/types.h>
     #include <sys/socket.h>
     #include <sys/uio.h>

     int
     sendfile(int fd, int s, off_t offset, size_t nbytes, struct sf_hdtr *hdtr,
	 off_t *sbytes, int flags);

DESCRIPTION
     The  sendfile()  system  call  sends a regular file or shared memory object
     specified by descriptor fd out a stream socket specified by descriptor s.

     The offset argument specifies where to begin in the  file.   Should  offset
     fall  beyond  the	end of file, the system will return success and report 0
     bytes sent as described below.  The  nbytes  argument  specifies  how  many
     bytes of the file should be sent, with 0 having the special meaning of send
     until the end of file has been reached.

     An  optional  header  and/or  trailer can be sent before and after the file
     data by specifying a pointer to a struct sf_hdtr, which has  the  following
     structure:

	   struct sf_hdtr {
		   struct iovec *headers;  /* pointer to header iovecs */
		   int hdr_cnt; 	   /* number of header iovecs */
		   struct iovec *trailers; /* pointer to trailer iovecs */
		   int trl_cnt; 	   /* number of trailer iovecs */
	   };
```

## 说明

节选 NAME／SYNOPSIS 与 DESCRIPTION 前三段（含头尾附加数据的 sf_hdtr 结构）；返回值、SF_* 标志语义（SF_NODISKIO 等）与 ERRORS 未全引。抓取件保留手册页原始换行与缩进。
