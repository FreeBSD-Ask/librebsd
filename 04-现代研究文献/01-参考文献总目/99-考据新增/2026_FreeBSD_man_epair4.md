# epair(4) — FreeBSD 内核接口手册页（成对虚拟以太网接口）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=epair&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.3.5“虚拟网络的路由界限”补证（D2 块）：成对接口与克隆创建（D2 块，ref_id 见库）

## 抓取正文（节选）

```
	   device epair

     Alternatively, to load the driver as a module at boot time, place the
     following line in loader.conf(5):

	   if_epair_load="YES"

DESCRIPTION
     The  epair  is  a pair of Ethernet-like software interfaces, which are con-
     nected back-to-back with a virtual cross-over cable.

     Each epair interface pair is created at runtime  using  interface	cloning.
     This  is  most easily done with the ifconfig(8) create command or using the
     cloned_interfaces variable in rc.conf(5).	While for cloning you only  give
     either  epair  or	epair<n> the epair pair will be named like epair<n>[ab].
     This means the names of the first epair  interfaces  will	be  epair0a  and
     epair0b.

     Like  any	other  Ethernet  interface, an epair needs to have a network ad-
     dress.  If the tunable net.link.epair.ether_gen_addr=0, each epair will  be
     assigned  a random locally administered address, that is only guaranteed to
     be    unique     within	 one	 network     stack.	 The	 tunable
     net.link.epair.ether_gen_addr=1  will  generate  a  stable MAC address with
     FreeBSD OUI  using  ether_gen_addr(9).   This  tunable  defaults  to  1  in
     FreeBSD  15.0  and might be removed in FreeBSD 16.0.  To change the default
     addresses one may use the SIOCSIFADDR ioctl(2)or ifconfig(8)utility.

     The basic intent is to provide connectivity  between  two	virtual  network
     stack  instances.	When connected to an if_bridge(4), one end of the inter-
     face pair can also be part of another (virtual) LAN.   As	with  any  other
     Ethernet interface, epair can have a vlan(4) configured on top of it.

     The  epair  has  RXCSUM and RXCSUM6 enabled because it may receive a packet
     where the checksum has already been validated by a physical interface.

     The epair supports TXCSUM and TXCSUM6 for TCP and UDP, but only by forward-
     ing the order to compute the checksum.  Thus, when using  an  epair  inter-
     face,  a  TCP  or UDP sender can offload checksum computation to a physical
```

## 引文摘录（空白已归一，供逐字核对）

device epair Alternatively, to load the driver as a module at boot time, place the following line in loader.conf(5): if_epair_load="YES" DESCRIPTION The epair is a pair of Ethernet-like software interfaces, which are con- nected back-to-back with a virtual cross-over cable. Each epair interface pair is created at runtime using interface cloning. This is most easily done with the ifconfig(8) create command or using the cloned_interfaces variable in rc.conf(5). While for cloning you only give either epair or epair<n> the epair pair will be named like epair<n>[ab]. This means the names of the first epair interfaces will be epair0a and epair0b. Like any other Ethernet interface, an epair needs to have a network ad- dress. If the tunable net.link.epair.ether_gen_addr=0, each epair will be assigned a random locally administered address, that is only guaranteed to be unique within one network stack. The tunable net.link.epair.ether_gen_addr=1 will generate a stable MAC address with FreeBSD OUI using ether_gen_addr(9). This tunable defaults to 1 in FreeBSD 15.0 and might be removed in FreeBSD 16.0. To change the default addresses one may use the SIOCSIFADDR ioctl(2)or ifconfig(8)utility. The basic intent is to provide connectivity between two virtual network stack instances. When connected to an if_bridge(4), one end of the inter- face pair can also be part of another (virtual) LAN. As with any other Ethernet interface, epair can have a vlan(4) configured on top of it. The epair has RXCSUM and RXCSUM6 enabled because it may receive a packet where the checksum has already been validated by a physical interface. The epair supports TXCSUM and TXCSUM6 for TCP and UDP, but only by forward- ing the order to compute the checksum. Thus, when using an epair inter- face, a TCP or UDP sender can offload checksum computation to a physical
