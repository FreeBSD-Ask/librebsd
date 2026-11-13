# wg(4) — FreeBSD 内核接口手册页（WireGuard 协议驱动）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=wg&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.9.1“WireGuard 的接口设计”补证（D2 块）：peer 与按需隧道（D2 块，ref_id 见库）

## 抓取正文（节选）

```

DESCRIPTION
     The wg driver provides Virtual Private Network (VPN) interfaces for the se-
     cure exchange of layer 3 traffic with other WireGuard peers using the Wire-
     Guard protocol.

     A	wg  interface  recognizes one or more peers, establishes a secure tunnel
     with each on demand, and tracks each peer's UDP endpoint for exchanging en-
     crypted traffic with.

     The interfaces can be created at runtime using the ifconfig wgN create com-
     mand.  The interface itself can be configured with wg(8).

     The following glossary provides a brief overview of WireGuard terminology:

	Peer	Peers exchange IPv4 or IPv6 traffic over secure  tunnels.   Each
		wg interface may be configured to recognize one or more peers.

	Key	Each  peer  uses its private key and corresponding public key to
		identify itself to others.  A peer  configures	a  wg  interface
		with its own private key and with the public keys of its peers.

	Pre-shared key
		In addition to the public keys, each peer pair may be configured
		with  a  unique pre-shared symmetric key.  This is used in their
		handshake to guard against future compromise of the  peers'  en-
		crypted tunnel if an attack on their Diffie-Hellman exchange be-
		comes feasible.  It is optional, but recommended.

	Allowed IP addresses
		A single wg interface may maintain concurrent tunnels connecting
		diverse  networks.   The interface therefore implements rudimen-
```

## 引文摘录（空白已归一，供逐字核对）

DESCRIPTION The wg driver provides Virtual Private Network (VPN) interfaces for the se- cure exchange of layer 3 traffic with other WireGuard peers using the Wire- Guard protocol. A wg interface recognizes one or more peers, establishes a secure tunnel with each on demand, and tracks each peer's UDP endpoint for exchanging en- crypted traffic with. The interfaces can be created at runtime using the ifconfig wgN create com- mand. The interface itself can be configured with wg(8). The following glossary provides a brief overview of WireGuard terminology: Peer Peers exchange IPv4 or IPv6 traffic over secure tunnels. Each wg interface may be configured to recognize one or more peers. Key Each peer uses its private key and corresponding public key to identify itself to others. A peer configures a wg interface with its own private key and with the public keys of its peers. Pre-shared key In addition to the public keys, each peer pair may be configured with a unique pre-shared symmetric key. This is used in their handshake to guard against future compromise of the peers' en- crypted tunnel if an attack on their Diffie-Hellman exchange be- comes feasible. It is optional, but recommended. Allowed IP addresses A single wg interface may maintain concurrent tunnels connecting diverse networks. The interface therefore implements rudimen-
