# locking(9) — FreeBSD 内核开发者手册页（内核同步原语）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=locking&sektion=9
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.10.4“并发访问的锁保护”补证（D2 块）：内核同步原语总览（D2 块，ref_id 见库）

## 抓取正文（节选）

```
LOCKING(9)		    Kernel Developer's Manual		      LOCKING(9)

NAME
     locking -- kernel synchronization primitives

DESCRIPTION
     The  FreeBSD kernel is written to run across multiple CPUs and as such pro-
     vides several different synchronization primitives to allow  developers  to
     safely access and manipulate many data types.

   Mutexes
     Mutexes  (also  called  "blocking mutexes") are the most commonly used syn-
     chronization primitive in the kernel.  A thread acquires  (locks)	a  mutex
     before  accessing	data  shared  with  other  threads  (including interrupt
     threads), and releases (unlocks) it afterwards.  If the mutex cannot be ac-
     quired, the thread requesting it will wait.  Mutexes are  adaptive  by  de-
     fault,  meaning that if the owner of a contended mutex is currently running
     on another CPU, then a thread attempting to acquire  the  mutex  will  spin
     rather  than yielding the processor.  Mutexes fully support priority propa-
     gation.

     See mutex(9) for details.

   Spin Mutexes
     Spin mutexes are a variation of basic mutexes; the main difference  between
     the two is that spin mutexes never block.	Instead, they spin while waiting
     for the lock to be released.  To avoid deadlock, a thread that holds a spin
     mutex must never yield its CPU.  Unlike ordinary mutexes, spin mutexes dis-
     able  interrupts  when  acquired.	Since disabling interrupts can be expen-
     sive, they are generally slower  to  acquire  and	release.   Spin  mutexes
     should  be used only when absolutely necessary, e.g. to protect data shared
     with interrupt filter code (see  bus_setup_intr(9)  for  details),  or  for
     scheduler internals.
```

## 引文摘录（空白已归一，供逐字核对）

LOCKING(9) Kernel Developer's Manual LOCKING(9) NAME locking -- kernel synchronization primitives DESCRIPTION The FreeBSD kernel is written to run across multiple CPUs and as such pro- vides several different synchronization primitives to allow developers to safely access and manipulate many data types. Mutexes Mutexes (also called "blocking mutexes") are the most commonly used syn- chronization primitive in the kernel. A thread acquires (locks) a mutex before accessing data shared with other threads (including interrupt threads), and releases (unlocks) it afterwards. If the mutex cannot be ac- quired, the thread requesting it will wait. Mutexes are adaptive by de- fault, meaning that if the owner of a contended mutex is currently running on another CPU, then a thread attempting to acquire the mutex will spin rather than yielding the processor. Mutexes fully support priority propa- gation. See mutex(9) for details. Spin Mutexes Spin mutexes are a variation of basic mutexes; the main difference between the two is that spin mutexes never block. Instead, they spin while waiting for the lock to be released. To avoid deadlock, a thread that holds a spin mutex must never yield its CPU. Unlike ordinary mutexes, spin mutexes dis- able interrupts when acquired. Since disabling interrupts can be expen- sive, they are generally slower to acquire and release. Spin mutexes should be used only when absolutely necessary, e.g. to protect data shared with interrupt filter code (see bus_setup_intr(9) for details), or for scheduler internals.
