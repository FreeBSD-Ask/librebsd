# netmap(4) — FreeBSD 内核接口手册页（高速分组 I/O 框架）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=netmap&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.6.1“Netmap 的零拷贝收包”补证（D2 块）：端口类型与队列直接访问（D2 块，ref_id 见库）

## 抓取正文（节选）

```

NAME
     netmap -- a framework for fast packet I/O

SYNOPSIS
     device netmap

DESCRIPTION
     netmap is a framework for extremely fast and efficient packet I/O for user-
     space  and  kernel  clients, and for Virtual Machines.  It runs on FreeBSD,
     Linux and some versions of Windows, and supports a variety of netmap ports,
     including

     physical NIC ports
	   to access individual queues of network interfaces;

     host ports
	   to inject packets into the host stack;

     VALE ports
	   implementing a very fast and modular in-kernel software  switch/data-
	   plane;

     netmap pipes
	   a shared memory packet transport channel;

     netmap monitors
	   a mechanism similar to bpf(4) to capture traffic

     All  these netmap ports are accessed interchangeably with the same API, and
     are at least one order of magnitude  faster  than	standard  OS  mechanisms
     (sockets,	bpf, tun/tap interfaces, native switches, pipes).  With suitably
     fast hardware (NICs, PCIe buses, CPUs), packet I/O  using	netmap	on  sup-
     ported  NICs reaches 14.88 million packets per second (Mpps) with much less
     than one core on 10 Gbit/s NICs; 35-40 Mpps on 40 Gbit/s NICs  (limited  by
     the hardware); about 20 Mpps per core for VALE ports; and over 100 Mpps for
     netmap  pipes.  NICs without native netmap support can still use the API in
     emulated mode, which uses unmodified device drivers and is 3-5 times faster
```

## 引文摘录（空白已归一，供逐字核对）

NAME netmap -- a framework for fast packet I/O SYNOPSIS device netmap DESCRIPTION netmap is a framework for extremely fast and efficient packet I/O for user- space and kernel clients, and for Virtual Machines. It runs on FreeBSD, Linux and some versions of Windows, and supports a variety of netmap ports, including physical NIC ports to access individual queues of network interfaces; host ports to inject packets into the host stack; VALE ports implementing a very fast and modular in-kernel software switch/data- plane; netmap pipes a shared memory packet transport channel; netmap monitors a mechanism similar to bpf(4) to capture traffic All these netmap ports are accessed interchangeably with the same API, and are at least one order of magnitude faster than standard OS mechanisms (sockets, bpf, tun/tap interfaces, native switches, pipes). With suitably fast hardware (NICs, PCIe buses, CPUs), packet I/O using netmap on sup- ported NICs reaches 14.88 million packets per second (Mpps) with much less than one core on 10 Gbit/s NICs; 35-40 Mpps on 40 Gbit/s NICs (limited by the hardware); about 20 Mpps per core for VALE ports; and over 100 Mpps for netmap pipes. NICs without native netmap support can still use the API in emulated mode, which uses unmodified device drivers and is 3-5 times faster
