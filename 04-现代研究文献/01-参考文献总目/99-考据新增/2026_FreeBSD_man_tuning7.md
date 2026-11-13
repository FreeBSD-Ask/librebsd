# tuning(7) — FreeBSD 杂类手册页（性能调优）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=tuning&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.9.8.1“文件描述符的极限”／V37.9.8.2“网络缓冲的容量值”补证（D2 块）：maxusers 自标定＋TCP 缓冲默认值（D2 块，ref_id 见库）

## 抓取正文（节选一）

```
     bug.numneg < debug.numcache is adhered to.

     There are various other buffer-cache and VM page cache related sysctls.  We
     do not recommend modifying these values.

     The  net.inet.tcp.sendspace  and net.inet.tcp.recvspace sysctls are of par-
     ticular interest if you are running network intensive  applications.   They
     control  the  amount of send and receive buffer space allowed for any given
     TCP connection.  The default sending buffer is 32K; the  default  receiving
     buffer  is  64K.  You can often improve bandwidth utilization by increasing
     the default at the cost of eating up more kernel memory  for  each  connec-
     tion.   We do not recommend increasing the defaults if you are serving hun-
     dreds or thousands of simultaneous connections because it	is  possible  to
     quickly  run  the	system out of memory due to stalled connections building
     up.  But if you need high bandwidth over a fewer number of connections, es-
     pecially if you have gigabit Ethernet, increasing these defaults can make a
     huge difference.  You can adjust the buffer size for incoming and	outgoing
     data separately.  For example, if your machine is primarily doing web serv-
     ing  you may want to decrease the recvspace in order to be able to increase
     the sendspace without eating too much kernel memory.  Note that the routing
     table (see route(8)) can be used to introduce route-specific send	and  re-
     ceive buffer size defaults.

     As  an  additional management tool you can use pipes in your firewall rules
     (see ipfw(8)) to limit the bandwidth going to or from particular IP  blocks
     or  ports.   For example, if you have a T1 you might want to limit your web
     traffic to 70% of the T1's bandwidth in order to leave the remainder avail-
     able for mail and interactive use.  Normally a heavily  loaded  web  server
     will  not	introduce  significant latencies into other services even if the
     network link is maxed out, but enforcing a limit can smooth things out  and
     lead  to  longer term stability.  Many people also enforce artificial band-
     width limitations in order to ensure that they are not  charged  for  using
     too much bandwidth.

     Setting the send or receive TCP buffer to values larger than 65535 will re-
     sult  in  a  marginal performance improvement unless both hosts support the
     window scaling extension of the TCP protocol, which is  controlled  by  the
     net.inet.tcp.rfc1323  sysctl.   These  extensions should be enabled and the
```

## 抓取正文（节选二）

```
LOADER TUNABLES
     Some aspects of the system behavior may not be tunable at	runtime  because
     memory  allocations  they perform must occur early in the boot process.  To
     change loader tunables, you must set their values in loader.conf(5) and re-
     boot the system.

     kern.maxusers controls the scaling of a number of static system tables, in-
     cluding defaults for the maximum number of open files,  sizing  of  network
     memory  resources, etc.  kern.maxusers is automatically sized at boot based
     on the amount of memory available in the system, and may be  determined  at
     run-time by inspecting the value of the read-only kern.maxusers sysctl.

     The  kern.dfldsiz and kern.dflssiz tunables set the default soft limits for
     process data and stack size respectively.	Processes may increase these  up
     to   the	hard   limits	by   calling  setrlimit(2).   The  kern.maxdsiz,
     kern.maxssiz, and kern.maxtsiz tunables set the  hard  limits  for  process
     data,  stack,  and  text  size respectively; processes may not exceed these
     limits.  The kern.sgrowsiz tunable controls how much the stack segment will
     grow when a process needs to allocate more stack.

     kern.ipc.nmbclusters may be adjusted to  increase	the  number  of  network
     mbufs  the system is willing to allocate.	Each cluster represents approxi-
     mately 2K of memory, so a value of 1024 represents 2M of kernel memory  re-
     served  for network buffers.  You can do a simple calculation to figure out
     how many you need.  If you have a web server which maxes out at 1000 simul-
     taneous connections, and each connection eats a 16K receive  and  16K  send
     buffer,  you  need approximately 32MB worth of network buffers to deal with
     it.  A good rule of thumb is to multiply by 2, so 32MBx2 = 64MB/2K = 32768.
     So for this case you would want to set kern.ipc.nmbclusters to  32768.   We
     recommend	values	between 1024 and 4096 for machines with moderates amount
     of memory, and between 4096 and 32768 for machines with greater amounts  of
     memory.   Under  no  circumstances  should  you specify an arbitrarily high
     value for this parameter, it could lead to a boot-time crash.  The  -m  op-
     tion to netstat(1) may be used to observe network cluster use.

     More  and	more  programs are using the sendfile(2) system call to transmit
     files over the network.  The kern.ipc.nsfbufs sysctl controls the number of
     file system buffers sendfile(2) is allowed to  use  to  perform  its  work.
```

## 引文摘录（空白已归一，供逐字核对）

bug.numneg < debug.numcache is adhered to. There are various other buffer-cache and VM page cache related sysctls. We do not recommend modifying these values. The net.inet.tcp.sendspace and net.inet.tcp.recvspace sysctls are of par- ticular interest if you are running network intensive applications. They control the amount of send and receive buffer space allowed for any given TCP connection. The default sending buffer is 32K; the default receiving buffer is 64K. You can often improve bandwidth utilization by increasing the default at the cost of eating up more kernel memory for each connec- tion. We do not recommend increasing the defaults if you are serving hun- dreds or thousands of simultaneous connections because it is possible to quickly run the system out of memory due to stalled connections building up. But if you need high bandwidth over a fewer number of connections, es- pecially if you have gigabit Ethernet, increasing these defaults can make a huge difference. You can adjust the buffer size for incoming and outgoing data separately. For example, if your machine is primarily doing web serv- ing you may want to decrease the recvspace in order to be able to increase the sendspace without eating too much kernel memory. Note that the routing table (see route(8)) can be used to introduce route-specific send and re- ceive buffer size defaults. As an additional management tool you can use pipes in your firewall rules (see ipfw(8)) to limit the bandwidth going to or from particular IP blocks or ports. For example, if you have a T1 you might want to limit your web traffic to 70% of the T1's bandwidth in order to leave the remainder avail- able for mail and interactive use. Normally a heavily loaded web server will not introduce significant latencies into other services even if the network link is maxed out, but enforcing a limit can smooth things out and lead to longer term stability. Many people also enforce artificial band- width limitations in order to ensure that they are not charged for using too much bandwidth. Setting the send or receive TCP buffer to values larger than 65535 will re- sult in a marginal performance improvement unless both hosts support the window scaling extension of the TCP protocol, which is controlled by the net.inet.tcp.rfc1323 sysctl. These extensions should be enabled and the

LOADER TUNABLES Some aspects of the system behavior may not be tunable at runtime because memory allocations they perform must occur early in the boot process. To change loader tunables, you must set their values in loader.conf(5) and re- boot the system. kern.maxusers controls the scaling of a number of static system tables, in- cluding defaults for the maximum number of open files, sizing of network memory resources, etc. kern.maxusers is automatically sized at boot based on the amount of memory available in the system, and may be determined at run-time by inspecting the value of the read-only kern.maxusers sysctl. The kern.dfldsiz and kern.dflssiz tunables set the default soft limits for process data and stack size respectively. Processes may increase these up to the hard limits by calling setrlimit(2). The kern.maxdsiz, kern.maxssiz, and kern.maxtsiz tunables set the hard limits for process data, stack, and text size respectively; processes may not exceed these limits. The kern.sgrowsiz tunable controls how much the stack segment will grow when a process needs to allocate more stack. kern.ipc.nmbclusters may be adjusted to increase the number of network mbufs the system is willing to allocate. Each cluster represents approxi- mately 2K of memory, so a value of 1024 represents 2M of kernel memory re- served for network buffers. You can do a simple calculation to figure out how many you need. If you have a web server which maxes out at 1000 simul- taneous connections, and each connection eats a 16K receive and 16K send buffer, you need approximately 32MB worth of network buffers to deal with it. A good rule of thumb is to multiply by 2, so 32MBx2 = 64MB/2K = 32768. So for this case you would want to set kern.ipc.nmbclusters to 32768. We recommend values between 1024 and 4096 for machines with moderates amount of memory, and between 4096 and 32768 for machines with greater amounts of memory. Under no circumstances should you specify an arbitrarily high value for this parameter, it could lead to a boot-time crash. The -m op- tion to netstat(1) may be used to observe network cluster use. More and more programs are using the sendfile(2) system call to transmit files over the network. The kern.ipc.nsfbufs sysctl controls the number of file system buffers sendfile(2) is allowed to use to perform its work.
