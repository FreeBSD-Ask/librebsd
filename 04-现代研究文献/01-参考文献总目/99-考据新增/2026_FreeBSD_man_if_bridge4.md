# if_bridge(4) — FreeBSD 内核接口手册页（链路层桥接）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=if_bridge&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.3.5“虚拟网络的路由界限”补证（D2 块）：桥接的帧格式同域约束（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     Alternatively, to load the driver as a module at boot time, place the
     following lines in loader.conf(5):

	   if_bridge_load="YES"
	   bridgestp_load="YES"

DESCRIPTION
     The  if_bridge  driver  creates a logical link between two or more IEEE 802
     networks that use the same (or "similar enough") framing format.  For exam-
     ple, it is possible to bridge Ethernet and 802.11 networks together, but it
     is not possible to bridge Ethernet and Token Ring together.

     Each if_bridge interface is created at  runtime  using  interface	cloning.
     This  is  most easily done with the ifconfig(8) create command or using the
     cloned_interfaces variable in rc.conf(5).

     When it is created, the if_bridge interface gets assigned a link (MAC)  ad-
     dress  in	the range of universally administered addresses reserved for the
     FreeBSD Foundation by hashing the host UUID, jail name, and  the  interface
     name.   If  this fails, a random, locally administered address is generated
     instead.  This address is guaranteed to be unique only across all if_bridge
     interfaces on the local machine.	Thus  you  can	theoretically  have  two
     bridges  on  different  machines with the same link addresses.  The address
     can be changed by assigning the desired link address using ifconfig(8).

     If sysctl(8) node net.link.bridge.inherit_mac has	a  non-zero  value,  the
     newly created bridge will inherit the MAC address from its first member in-
     stead of choosing a random link-level address.  This will provide more pre-
     dictable  bridge  MAC  addresses  without any additional configuration, but
     currently this feature is known to break some L2 protocols, for example PP-
     PoE that is provided by ng_pppoe(4) and ppp(8).  Currently this feature  is
     considered as experimental and is turned off by default.

     A	bridge	can  be  used  to  provide  several  services,	such as a simple
     802.11-to-Ethernet bridge for wireless hosts, or traffic isolation.

     A bridge works like a switch, forwarding traffic from one interface to  an-
```

## 引文摘录（空白已归一，供逐字核对）

Alternatively, to load the driver as a module at boot time, place the following lines in loader.conf(5): if_bridge_load="YES" bridgestp_load="YES" DESCRIPTION The if_bridge driver creates a logical link between two or more IEEE 802 networks that use the same (or "similar enough") framing format. For exam- ple, it is possible to bridge Ethernet and 802.11 networks together, but it is not possible to bridge Ethernet and Token Ring together. Each if_bridge interface is created at runtime using interface cloning. This is most easily done with the ifconfig(8) create command or using the cloned_interfaces variable in rc.conf(5). When it is created, the if_bridge interface gets assigned a link (MAC) ad- dress in the range of universally administered addresses reserved for the FreeBSD Foundation by hashing the host UUID, jail name, and the interface name. If this fails, a random, locally administered address is generated instead. This address is guaranteed to be unique only across all if_bridge interfaces on the local machine. Thus you can theoretically have two bridges on different machines with the same link addresses. The address can be changed by assigning the desired link address using ifconfig(8). If sysctl(8) node net.link.bridge.inherit_mac has a non-zero value, the newly created bridge will inherit the MAC address from its first member in- stead of choosing a random link-level address. This will provide more pre- dictable bridge MAC addresses without any additional configuration, but currently this feature is known to break some L2 protocols, for example PP- PoE that is provided by ng_pppoe(4) and ppp(8). Currently this feature is considered as experimental and is turned off by default. A bridge can be used to provide several services, such as a simple 802.11-to-Ethernet bridge for wireless hosts, or traffic isolation. A bridge works like a switch, forwarding traffic from one interface to an-
