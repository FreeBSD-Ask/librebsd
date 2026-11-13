# mutex(9) — FreeBSD 内核开发者手册页（互斥锁）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=mutex&sektion=9
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.10.4“并发访问的锁保护”补证（D2 块）：互斥锁的设计取舍（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     void
     mtx_assert(const struct mtx *mutex, int what);

     #include <sys/kernel.h>

     MTX_SYSINIT(name, struct mtx *mtx, const char *description, int opts);

DESCRIPTION
     Mutexes are the most basic and primary method  of	thread	synchronization.
     The major design considerations for mutexes are:

     1.   Acquiring and releasing uncontested mutexes should be as cheap as pos-
	  sible.

     2.   They	must  have the information and storage space to support priority
	  propagation.

     3.   A thread must be able to recursively acquire a  mutex,  provided  that
	  the mutex is initialized to support recursion.

     There  are currently two flavors of mutexes, those that context switch when
     they block and those that do not.

     By default, MTX_DEF mutexes will context switch when they are already held.
     As an optimization, they may spin for some amount of  time  before  context
     switching.   It  is  important  to remember that since a thread may be pre-
     empted at any time, the possible context switch introduced by  acquiring  a
     mutex is guaranteed to not break anything that is not already broken.

     Mutexes  which  do  not  context switch are MTX_SPIN mutexes.  These should
     only be used to protect data shared with primary interrupt code.  This  in-
     cludes  interrupt	filters and low level scheduling code.	In all architec-
     tures both acquiring and releasing of a uncontested spin mutex is more  ex-
     pensive  than  the same operation on a non-spin mutex.  In order to protect
     an interrupt service routine from blocking against  itself  all  interrupts
     are  either  blocked  or deferred on a processor while holding a spin lock.
     It is permissible to hold multiple spin mutexes.

```

## 引文摘录（空白已归一，供逐字核对）

void mtx_assert(const struct mtx *mutex, int what); #include <sys/kernel.h> MTX_SYSINIT(name, struct mtx *mtx, const char *description, int opts); DESCRIPTION Mutexes are the most basic and primary method of thread synchronization. The major design considerations for mutexes are: 1. Acquiring and releasing uncontested mutexes should be as cheap as pos- sible. 2. They must have the information and storage space to support priority propagation. 3. A thread must be able to recursively acquire a mutex, provided that the mutex is initialized to support recursion. There are currently two flavors of mutexes, those that context switch when they block and those that do not. By default, MTX_DEF mutexes will context switch when they are already held. As an optimization, they may spin for some amount of time before context switching. It is important to remember that since a thread may be pre- empted at any time, the possible context switch introduced by acquiring a mutex is guaranteed to not break anything that is not already broken. Mutexes which do not context switch are MTX_SPIN mutexes. These should only be used to protect data shared with primary interrupt code. This in- cludes interrupt filters and low level scheduling code. In all architec- tures both acquiring and releasing of a uncontested spin mutex is more ex- pensive than the same operation on a non-spin mutex. In order to protect an interrupt service routine from blocking against itself all interrupts are either blocked or deferred on a processor while holding a spin lock. It is permissible to hold multiple spin mutexes.
