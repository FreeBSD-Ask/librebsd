# kqueue(2) — FreeBSD 系统调用手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.5.5“服务器框架的适配层”补证（D2 块）：filter 与 kevent 的标识（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     kevent(int kq, const struct kevent *changelist, int nchanges,
	 struct kevent *eventlist, int nevents, const struct timespec *timeout);

     EV_SET(kev, ident, filter, flags, fflags, data, udata);

DESCRIPTION
     The  kqueue()  system  call provides a generic method of notifying the user
     when an event happens or a condition holds, based on the results  of  small
     pieces  of  kernel  code  termed  filters.   A  kevent is identified by the
     (ident, filter) pair; there may only be one unique kevent per kqueue.

     The filter is executed upon the initial registration of a kevent  in  order
     to  detect whether a preexisting condition is present, and is also executed
     whenever an event is passed to the filter for evaluation.	 If  the  filter
     determines that the condition should be reported, then the kevent is placed
     on the kqueue for the user to retrieve.

     The  filter  is also run when the user attempts to retrieve the kevent from
     the kqueue.  If the filter indicates that the condition that triggered  the
     event no longer holds, the kevent is removed from the kqueue and is not re-
     turned.

     Multiple  events which trigger the filter do not result in multiple kevents
     being placed on the kqueue; instead, the filter will aggregate  the  events
     into a single struct kevent.  Calling close() on a file descriptor will re-
     move any kevents that reference the descriptor.

     The kqueue() system call creates a new kernel event queue and returns a de-
     scriptor.	 The  queue  is  not  inherited by a child created with fork(2).
     However, if rfork(2) is called without the RFFDG flag, then the  descriptor
     table  is	shared,  which	will  allow  sharing  of  the kqueue between two
     processes.
```

## 引文摘录（空白已归一，供逐字核对）

kevent(int kq, const struct kevent *changelist, int nchanges, struct kevent *eventlist, int nevents, const struct timespec *timeout); EV_SET(kev, ident, filter, flags, fflags, data, udata); DESCRIPTION The kqueue() system call provides a generic method of notifying the user when an event happens or a condition holds, based on the results of small pieces of kernel code termed filters. A kevent is identified by the (ident, filter) pair; there may only be one unique kevent per kqueue. The filter is executed upon the initial registration of a kevent in order to detect whether a preexisting condition is present, and is also executed whenever an event is passed to the filter for evaluation. If the filter determines that the condition should be reported, then the kevent is placed on the kqueue for the user to retrieve. The filter is also run when the user attempts to retrieve the kevent from the kqueue. If the filter indicates that the condition that triggered the event no longer holds, the kevent is removed from the kqueue and is not re- turned. Multiple events which trigger the filter do not result in multiple kevents being placed on the kqueue; instead, the filter will aggregate the events into a single struct kevent. Calling close() on a file descriptor will re- move any kevents that reference the descriptor. The kqueue() system call creates a new kernel event queue and returns a de- scriptor. The queue is not inherited by a child created with fork(2). However, if rfork(2) is called without the RFFDG flag, then the descriptor table is shared, which will allow sharing of the kqueue between two processes.
