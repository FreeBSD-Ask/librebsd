# FreeBSD kqueue(2) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 用途：Task 8.2 G4 · V37.2.10.1“Kqueue 的内核数据结构”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
KQUEUE(2)		       System Calls Manual		       KQUEUE(2)

NAME
     kqueue, kevent -- kernel event notification mechanism

DESCRIPTION
     The  kqueue()  system  call provides a generic method of notifying the user
     when an event happens or a condition holds, based on the results  of  small
     pieces  of  kernel code  termed filters.   A  kevent is identified by the
     (ident, filter) pair; there may only be one unique kevent per kqueue.

     The filter is executed upon the initial registration of a kevent  in  order
     to  detect whether a preexisting condition is present, and is also executed
     whenever an event is passed to the filter for evaluation.	 If  the  filter
     determines that the condition should be reported, then the kevent is placed
     on the kqueue for the user to retrieve.
```

## 说明

节选为 NAME 与 DESCRIPTION 前两段；后文逐项列出系统过滤器（EVFILT_READ 等），本批未引。抓取件保留手册页原始换行与缩进。
