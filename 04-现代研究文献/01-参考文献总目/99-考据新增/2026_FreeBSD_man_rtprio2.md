# rtprio(2) — FreeBSD 系统调用手册页（实时／空闲优先级）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=rtprio&sektion=2
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.9.8.3“调度参数的调整法”补证（D2 块）：运行期优先级调整（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     int
     rtprio(int function, pid_t pid, struct rtprio *rtp);

     int
     rtprio_thread(int function, lwpid_t lwpid, struct rtprio *rtp);

DESCRIPTION
     The  rtprio()  system call is used to lookup or change the realtime or idle
     priority of a process, or the calling thread.  The  rtprio_thread()  system
     call is used to lookup or change the realtime or idle priority of a thread.

     The  function argument specifies the operation to be performed.  RTP_LOOKUP
     to lookup the current priority, and RTP_SET to set the priority.

     For the rtprio() system call, the pid argument specifies the process to op-
     erate on, 0 for the calling thread.  When pid is non-zero, the system  call
     reports  the highest priority in the process, or sets all threads' priority
     in the process, depending on value of the function argument.

     For the rtprio_thread() system call, the lwpid specifies the thread to  op-
     erate on, 0 for the calling thread.

     The  *rtp argument is a pointer to a struct rtprio which is used to specify
     the priority and priority type.  This structure has the following form:

     struct rtprio {
	     u_short type;
	     u_short prio;
     };

     The value of the type field may be RTP_PRIO_REALTIME for  realtime  priori-
     ties,  RTP_PRIO_NORMAL  for  normal  priorities, and RTP_PRIO_IDLE for idle
     priorities.  The priority specified by the prio field ranges between 0  and
     RTP_PRIO_MAX (usually 31).  0 is the highest possible priority.

     Realtime and idle priority is inherited through fork() and exec().

```

## 引文摘录（空白已归一，供逐字核对）

int rtprio(int function, pid_t pid, struct rtprio *rtp); int rtprio_thread(int function, lwpid_t lwpid, struct rtprio *rtp); DESCRIPTION The rtprio() system call is used to lookup or change the realtime or idle priority of a process, or the calling thread. The rtprio_thread() system call is used to lookup or change the realtime or idle priority of a thread. The function argument specifies the operation to be performed. RTP_LOOKUP to lookup the current priority, and RTP_SET to set the priority. For the rtprio() system call, the pid argument specifies the process to op- erate on, 0 for the calling thread. When pid is non-zero, the system call reports the highest priority in the process, or sets all threads' priority in the process, depending on value of the function argument. For the rtprio_thread() system call, the lwpid specifies the thread to op- erate on, 0 for the calling thread. The *rtp argument is a pointer to a struct rtprio which is used to specify the priority and priority type. This structure has the following form: struct rtprio { u_short type; u_short prio; }; The value of the type field may be RTP_PRIO_REALTIME for realtime priori- ties, RTP_PRIO_NORMAL for normal priorities, and RTP_PRIO_IDLE for idle priorities. The priority specified by the prio field ranges between 0 and RTP_PRIO_MAX (usually 31). 0 is the highest possible priority. Realtime and idle priority is inherited through fork() and exec().
