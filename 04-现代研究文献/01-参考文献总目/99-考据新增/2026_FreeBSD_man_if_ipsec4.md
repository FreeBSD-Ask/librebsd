# if_ipsec(4) — FreeBSD 内核接口手册页（IPsec 虚拟隧道接口）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=if_ipsec&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.9.2“内核 VPN 的路由接入”补证（D2 块）：route-based VPN 与路由表（D2 块，ref_id 见库）

## 抓取正文（节选）

```
	   options IPSEC

     It can also be loaded as part of the ipsec kernel module if the kernel was
     compiled with

	   options IPSEC_SUPPORT

DESCRIPTION
     The  if_ipsec  network interface is targeted for creating route-based VPNs.
     It can tunnel IPv4 and IPv6 traffic over either IPv4 or IPv6 and secure  it
     with ESP.

     if_ipsec  interfaces  are dynamically created and destroyed with the ifcon-
     fig(8) create and destroy subcommands.  The  administrator  must  configure
     IPsec  tunnel  endpoint  addresses.   These  addresses will be used for the
     outer IP header of ESP packets.  The administrator can also  configure  the
     protocol and addresses for the inner IP header with ifconfig(8), and modify
     the routing table to route the packets through the if_ipsec interface.

     When the if_ipsec interface is configured, it automatically creates special
     security policies.  These policies can be used to acquire security associa-
     tions  from the IKE daemon, which are needed for establishing an IPsec tun-
     nel.  It is also possible to create needed security  associations	manually
     with the setkey(8) utility.

     Each  if_ipsec  interface	has  an  additional numeric configuration option
     reqid id.	This id is used to distinguish traffic and security policies be-
     tween several if_ipsec interfaces.  The reqid can be specified on interface
     creation and changed later.  If not  specified,  it  is  automatically  as-
     signed.   Note  that changing reqid will lead to generation of new security
     policies, and this may require creating new security associations.

EXAMPLES
     The example below shows manual configuration of an IPsec tunnel between two
     FreeBSD hosts.  Host A has the IP address 192.168.0.3, and host B	has  the
     IP address 192.168.0.5.

     On host A:
```

## 引文摘录（空白已归一，供逐字核对）

options IPSEC It can also be loaded as part of the ipsec kernel module if the kernel was compiled with options IPSEC_SUPPORT DESCRIPTION The if_ipsec network interface is targeted for creating route-based VPNs. It can tunnel IPv4 and IPv6 traffic over either IPv4 or IPv6 and secure it with ESP. if_ipsec interfaces are dynamically created and destroyed with the ifcon- fig(8) create and destroy subcommands. The administrator must configure IPsec tunnel endpoint addresses. These addresses will be used for the outer IP header of ESP packets. The administrator can also configure the protocol and addresses for the inner IP header with ifconfig(8), and modify the routing table to route the packets through the if_ipsec interface. When the if_ipsec interface is configured, it automatically creates special security policies. These policies can be used to acquire security associa- tions from the IKE daemon, which are needed for establishing an IPsec tun- nel. It is also possible to create needed security associations manually with the setkey(8) utility. Each if_ipsec interface has an additional numeric configuration option reqid id. This id is used to distinguish traffic and security policies be- tween several if_ipsec interfaces. The reqid can be specified on interface creation and changed later. If not specified, it is automatically as- signed. Note that changing reqid will lead to generation of new security policies, and this may require creating new security associations. EXAMPLES The example below shows manual configuration of an IPsec tunnel between two FreeBSD hosts. Host A has the IP address 192.168.0.3, and host B has the IP address 192.168.0.5. On host A:
