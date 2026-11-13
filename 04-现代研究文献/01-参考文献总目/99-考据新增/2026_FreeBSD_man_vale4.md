# vale(4) — FreeBSD 内核接口手册页（netmap API 虚拟以太网）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=vale&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.6.1“Netmap 的零拷贝收包”补证（D2 块）：软件交换与客户端互联（D2 块，ref_id 见库）

## 抓取正文（节选）

```

NAME
     vale -- a very fast Virtual Local Ethernet using the netmap API

SYNOPSIS
     device netmap

DESCRIPTION
     vale  is a feature of the netmap(4) module that implements multiple Virtual
     switches that can be used to interconnect netmap clients, including traffic
     sources and sinks, packet forwarders, userspace firewalls, and so on.

     vale is implemented completely in software, and is extremely  fast.   On  a
     modern  machine it can move almost 20 Million packets per second (Mpps) per
     core with small frames, and about 70 Gbit/s with 1500 byte frames.

OPERATION
     vale dynamically creates switches and ports as clients connect to it  using
     the netmap(4) API.

     vale ports are named valeSSS:PPP where vale is the prefix indicating a VALE
     switch  rather  than  a standard interface, SSS indicates a specific switch
     (the colon is a separator), and PPP indicates a  port  within  the  switch.
     Both SSS and PPP have the form [0-9a-zA-Z_]+ , the string cannot exceed IF-
     NAMSIZ  characters,  and  PPP cannot be the name of any existing OS network
     interface.

     See netmap(4) for details on the API.

   LIMITS
     vale currently supports up to 254 ports per switch. The maximum  number  of
     switches is provided by the max_bridges sysctl variable.

SYSCTL VARIABLES
     See netmap(4) for a list of sysctl variables that affect vale bridges.

EXAMPLES
     Create  one  switch,  with a traffic generator connected to one port, and a
```

## 引文摘录（空白已归一，供逐字核对）

NAME vale -- a very fast Virtual Local Ethernet using the netmap API SYNOPSIS device netmap DESCRIPTION vale is a feature of the netmap(4) module that implements multiple Virtual switches that can be used to interconnect netmap clients, including traffic sources and sinks, packet forwarders, userspace firewalls, and so on. vale is implemented completely in software, and is extremely fast. On a modern machine it can move almost 20 Million packets per second (Mpps) per core with small frames, and about 70 Gbit/s with 1500 byte frames. OPERATION vale dynamically creates switches and ports as clients connect to it using the netmap(4) API. vale ports are named valeSSS:PPP where vale is the prefix indicating a VALE switch rather than a standard interface, SSS indicates a specific switch (the colon is a separator), and PPP indicates a port within the switch. Both SSS and PPP have the form [0-9a-zA-Z_]+ , the string cannot exceed IF- NAMSIZ characters, and PPP cannot be the name of any existing OS network interface. See netmap(4) for details on the API. LIMITS vale currently supports up to 254 ports per switch. The maximum number of switches is provided by the max_bridges sysctl variable. SYSCTL VARIABLES See netmap(4) for a list of sysctl variables that affect vale bridges. EXAMPLES Create one switch, with a traffic generator connected to one port, and a
