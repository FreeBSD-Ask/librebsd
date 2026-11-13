# ipsec(4) — FreeBSD 内核接口手册页（IPsec 协议）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=ipsec&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.9.2“内核 VPN 的路由接入”补证（D2 块）：传输模式与隧道模式（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     Payload)  AH  (for  Authentication Header), and IPComp (for IP Payload Com-
     pression Protocol) that provide security services	for  IP  datagrams.   AH
     both  authenticates and guarantees the integrity of an IP packet by attach-
     ing a cryptographic checksum computed using one-way hash  functions.   ESP,
     in  addition,  prevents unauthorized parties from reading the payload of an
     IP packet by also encrypting it.  IPComp tries  to  increase  communication
     performance  by  compressing  IP  payload, thus reducing the amount of data
     sent.  This will help nodes on slow links but with enough computing  power.
     ipsec  operates in one of two modes: transport mode or tunnel mode.  Trans-
     port mode is used to protect peer-to-peer communication between end  nodes.
     Tunnel mode encapsulates IP packets within other IP packets and is designed
     for security gateways such as VPN endpoints.

     System configuration requires the crypto(4) subsystem.

     The  packets can be passed to a virtual enc(4) interface, to perform packet
     filtering before outbound encryption and after decapsulation inbound.

     To properly filter on the inner packets of an ipsec tunnel with  firewalls,
     you can change the values of the following sysctls

     Name			      Default	 Enable
     net.inet.ipsec.filtertunnel      0 	 1
     net.inet6.ipsec6.filtertunnel    0 	 1

   Kernel interface
     ipsec  is	controlled by a key management and policy engine, that reside in
     the operating system kernel.  Key management is the process of  associating
     keys  with security associations, also know as SAs.  Policy management dic-
     tates when new security associations created or destroyed.

     The key management engine can be accessed from  userland  by  using  PF_KEY
     sockets.  The PF_KEY socket API is defined in RFC2367.

     The policy engine is controlled by an extension to the PF_KEY API, setsock-
     opt(2)  operations,  and sysctl(3) interface.  The kernel implements an ex-
     tended version of the PF_KEY interface and allows the programmer to  define
     IPsec  policies  which are similar to the per-packet filters.  The setsock-
```

## 引文摘录（空白已归一，供逐字核对）

Payload) AH (for Authentication Header), and IPComp (for IP Payload Com- pression Protocol) that provide security services for IP datagrams. AH both authenticates and guarantees the integrity of an IP packet by attach- ing a cryptographic checksum computed using one-way hash functions. ESP, in addition, prevents unauthorized parties from reading the payload of an IP packet by also encrypting it. IPComp tries to increase communication performance by compressing IP payload, thus reducing the amount of data sent. This will help nodes on slow links but with enough computing power. ipsec operates in one of two modes: transport mode or tunnel mode. Trans- port mode is used to protect peer-to-peer communication between end nodes. Tunnel mode encapsulates IP packets within other IP packets and is designed for security gateways such as VPN endpoints. System configuration requires the crypto(4) subsystem. The packets can be passed to a virtual enc(4) interface, to perform packet filtering before outbound encryption and after decapsulation inbound. To properly filter on the inner packets of an ipsec tunnel with firewalls, you can change the values of the following sysctls Name Default Enable net.inet.ipsec.filtertunnel 0 1 net.inet6.ipsec6.filtertunnel 0 1 Kernel interface ipsec is controlled by a key management and policy engine, that reside in the operating system kernel. Key management is the process of associating keys with security associations, also know as SAs. Policy management dic- tates when new security associations created or destroyed. The key management engine can be accessed from userland by using PF_KEY sockets. The PF_KEY socket API is defined in RFC2367. The policy engine is controlled by an extension to the PF_KEY API, setsock- opt(2) operations, and sysctl(3) interface. The kernel implements an ex- tended version of the PF_KEY interface and allows the programmer to define IPsec policies which are similar to the per-packet filters. The setsock-
