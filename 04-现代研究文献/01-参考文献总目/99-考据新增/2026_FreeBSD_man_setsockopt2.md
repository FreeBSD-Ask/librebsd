# setsockopt(2) — FreeBSD 系统调用手册页（套接字选项）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=setsockopt&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.9.8.2“网络缓冲的容量值”补证（D2 块）：缓冲增减与绝对上限（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     With protocols that support out-of-band data, the SO_OOBINLINE  option  re-
     quests  that  out-of-band	data be placed in the normal data input queue as
     received; it will then be accessible with recv(2) or read(2) calls  without
     the MSG_OOB flag.	Some protocols always behave as if this option is set.

     SO_SNDBUF and SO_RCVBUF are options to adjust the normal buffer sizes allo-
     cated  for  output and input buffers, respectively.  The buffer size may be
     increased for high-volume connections, or may be  decreased  to  limit  the
     possible  backlog	of incoming data.  The system places an absolute maximum
     on these values, which is accessible through  the	sysctl(3)  MIB	variable
     "kern.ipc.maxsockbuf".

     SO_SNDLOWAT  is  an  option to set the minimum count for output operations.
     Most output operations process all of the data supplied by the call, deliv-
     ering data to the protocol for transmission and blocking as  necessary  for
     flow  control.   Nonblocking output operations will process as much data as
     permitted subject to flow control without blocking,  but  will  process  no
     data if flow control does not allow the smaller of the low water mark value
     or  the  entire request to be processed.  A select(2) operation testing the
     ability to write to a socket will return true only if the	low  water  mark
     amount  could  be processed.  The default value for SO_SNDLOWAT is set to a
     convenient size for network efficiency, often 1024.

     SO_RCVLOWAT is an option to set the minimum count for input operations.  In
     general, receive calls will block until any (non-zero) amount  of	data  is
     received,	then  return  with  the  smaller  of the amount available or the
     amount requested.	The default value for SO_RCVLOWAT is 1.  If  SO_RCVLOWAT
     is  set  to a larger value, blocking receive calls normally wait until they
     have received the smaller of the low water  mark  value  or  the  requested
     amount.   Receive calls may still return less than the low water mark if an
     error occurs, a signal is caught, or the type of data next in  the  receive
     queue is different from that which was returned.

     SO_SNDTIMEO  is an option to set a timeout value for output operations.  It
     accepts a struct timeval argument with the number of seconds and  microsec-
     onds  used to limit waits for output operations to complete.  If a send op-
     eration has blocked for this much time, it returns with a partial count  or
     with  the error EWOULDBLOCK if no data were sent.	In the current implemen-
```

## 引文摘录（空白已归一，供逐字核对）

With protocols that support out-of-band data, the SO_OOBINLINE option re- quests that out-of-band data be placed in the normal data input queue as received; it will then be accessible with recv(2) or read(2) calls without the MSG_OOB flag. Some protocols always behave as if this option is set. SO_SNDBUF and SO_RCVBUF are options to adjust the normal buffer sizes allo- cated for output and input buffers, respectively. The buffer size may be increased for high-volume connections, or may be decreased to limit the possible backlog of incoming data. The system places an absolute maximum on these values, which is accessible through the sysctl(3) MIB variable "kern.ipc.maxsockbuf". SO_SNDLOWAT is an option to set the minimum count for output operations. Most output operations process all of the data supplied by the call, deliv- ering data to the protocol for transmission and blocking as necessary for flow control. Nonblocking output operations will process as much data as permitted subject to flow control without blocking, but will process no data if flow control does not allow the smaller of the low water mark value or the entire request to be processed. A select(2) operation testing the ability to write to a socket will return true only if the low water mark amount could be processed. The default value for SO_SNDLOWAT is set to a convenient size for network efficiency, often 1024. SO_RCVLOWAT is an option to set the minimum count for input operations. In general, receive calls will block until any (non-zero) amount of data is received, then return with the smaller of the amount available or the amount requested. The default value for SO_RCVLOWAT is 1. If SO_RCVLOWAT is set to a larger value, blocking receive calls normally wait until they have received the smaller of the low water mark value or the requested amount. Receive calls may still return less than the low water mark if an error occurs, a signal is caught, or the type of data next in the receive queue is different from that which was returned. SO_SNDTIMEO is an option to set a timeout value for output operations. It accepts a struct timeval argument with the number of seconds and microsec- onds used to limit waits for output operations to complete. If a send op- eration has blocked for this much time, it returns with a partial count or with the error EWOULDBLOCK if no data were sent. In the current implemen-
