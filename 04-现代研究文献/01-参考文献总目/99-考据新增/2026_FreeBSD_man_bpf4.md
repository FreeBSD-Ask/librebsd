# bpf(4) — FreeBSD 内核接口手册页（Berkeley Packet Filter）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=bpf&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.6.4“高速抓包的工具链”补证（D2 块）：内核侧原始接口与设备节点（D2 块，ref_id 见库）

## 抓取正文（节选）

```

NAME
     bpf -- Berkeley Packet Filter

SYNOPSIS
     device bpf

DESCRIPTION
     The  Berkeley Packet Filter provides a raw interface to data link layers in
     a protocol independent fashion.  All packets on  the  network,  even  those
     destined for other hosts, are accessible through this mechanism.

     The  packet  filter appears as a character special device, /dev/bpf.  After
     opening the device, the file descriptor must be bound to a specific network
     interface with the BIOCSETIF ioctl.  A given interface  can  be  shared  by
     multiple  listeners,  and the filter underlying each descriptor will see an
     identical packet stream.

     Associated with each open instance of a bpf file is a user-settable  packet
     filter.   Whenever  a packet is received by an interface, all file descrip-
     tors listening on that interface apply their filter.  Each descriptor  that
     accepts the packet receives its own copy.

     A	packet	can be sent out on the network by writing to a bpf file descrip-
     tor.  The writes are unbuffered, meaning only one packet can  be  processed
     per  write.   Currently,  only  writes to Ethernets and SLIP links are sup-
     ported.

BUFFER MODES
     bpf devices deliver packet data to the application via memory buffers  pro-
     vided  by the application.  The buffer mode is set using the BIOCSETBUFMODE
     ioctl, and read using the BIOCGETBUFMODE ioctl.

   Buffered read mode
     By default, bpf devices operate in the BPF_BUFMODE_BUFFER	mode,  in  which
     packet  data  is  copied  explicitly  from  kernel to user memory using the
     read(2) system call.  The user process will declare  a  fixed  buffer  size
     that  will be used both for sizing internal buffers and for all read(2) op-
```

## 引文摘录（空白已归一，供逐字核对）

NAME bpf -- Berkeley Packet Filter SYNOPSIS device bpf DESCRIPTION The Berkeley Packet Filter provides a raw interface to data link layers in a protocol independent fashion. All packets on the network, even those destined for other hosts, are accessible through this mechanism. The packet filter appears as a character special device, /dev/bpf. After opening the device, the file descriptor must be bound to a specific network interface with the BIOCSETIF ioctl. A given interface can be shared by multiple listeners, and the filter underlying each descriptor will see an identical packet stream. Associated with each open instance of a bpf file is a user-settable packet filter. Whenever a packet is received by an interface, all file descrip- tors listening on that interface apply their filter. Each descriptor that accepts the packet receives its own copy. A packet can be sent out on the network by writing to a bpf file descrip- tor. The writes are unbuffered, meaning only one packet can be processed per write. Currently, only writes to Ethernets and SLIP links are sup- ported. BUFFER MODES bpf devices deliver packet data to the application via memory buffers pro- vided by the application. The buffer mode is set using the BIOCSETBUFMODE ioctl, and read using the BIOCGETBUFMODE ioctl. Buffered read mode By default, bpf devices operate in the BPF_BUFMODE_BUFFER mode, in which packet data is copied explicitly from kernel to user memory using the read(2) system call. The user process will declare a fixed buffer size that will be used both for sizing internal buffers and for all read(2) op-
