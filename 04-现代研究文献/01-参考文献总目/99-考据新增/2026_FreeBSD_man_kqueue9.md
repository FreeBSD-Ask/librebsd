# kqueue(9) — FreeBSD 内核开发者手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=9
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.5.5“服务器框架的适配层”补证（D2 块）：内核侧 filter 注册接口（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     KNOTE_LOCKED(struct knlist *knl, long hint);

     void
     KNOTE_UNLOCKED(struct knlist *knl, long hint);

DESCRIPTION
     The functions kqueue_add_filteropts() and kqueue_del_filteropts() allow for
     the  addition  and  removal of a filter type.  The filter is statically de-
     fined by the EVFILT_* macros.  The  function  kqueue_add_filteropts()  will
     make filt available.  The struct filterops has the following members:

     f_isfd    If  f_isfd  is  set, ident in struct kevent is taken to be a file
	       descriptor.  In this case, the knote passed  into  f_attach  will
	       have  the kn_fp member initialized to the struct file * that rep-
	       resents the file descriptor.

     f_attach  The f_attach function will be called when attaching  a  knote  to
	       the object.  The method should call knlist_add() to add the knote
	       to the list that was initialized with knlist_init().  The call to
	       knlist_add()  is  only  necessary if the object can have multiple
	       knotes associated with it.  If there is no  knlist  to  call  kn-
	       list_add() with, the function f_attach must clear the KN_DETACHED
	       bit  of	kn_status  in the knote.  The function shall return 0 on
	       success, or appropriate error for the failure, such as  when  the
	       object  is  being destroyed, or does not exist.	During f_attach,
	       it is valid to change the kn_fop pointer to a different	pointer.
	       This  will  change the f_event and f_detach functions called when
	       processing the knote.

     f_detach  The f_detach function will be called to detach the knote  if  the
	       knote  has not already been detached by a call to knlist_remove()
	       or knlist_delete().  The list lock will not  be	held  when  this
```

## 引文摘录（空白已归一，供逐字核对）

KNOTE_LOCKED(struct knlist *knl, long hint); void KNOTE_UNLOCKED(struct knlist *knl, long hint); DESCRIPTION The functions kqueue_add_filteropts() and kqueue_del_filteropts() allow for the addition and removal of a filter type. The filter is statically de- fined by the EVFILT_* macros. The function kqueue_add_filteropts() will make filt available. The struct filterops has the following members: f_isfd If f_isfd is set, ident in struct kevent is taken to be a file descriptor. In this case, the knote passed into f_attach will have the kn_fp member initialized to the struct file * that rep- resents the file descriptor. f_attach The f_attach function will be called when attaching a knote to the object. The method should call knlist_add() to add the knote to the list that was initialized with knlist_init(). The call to knlist_add() is only necessary if the object can have multiple knotes associated with it. If there is no knlist to call kn- list_add() with, the function f_attach must clear the KN_DETACHED bit of kn_status in the knote. The function shall return 0 on success, or appropriate error for the failure, such as when the object is being destroyed, or does not exist. During f_attach, it is valid to change the kn_fop pointer to a different pointer. This will change the f_event and f_detach functions called when processing the knote. f_detach The f_detach function will be called to detach the knote if the knote has not already been detached by a call to knlist_remove() or knlist_delete(). The list lock will not be held when this
