# FreeBSD ktls(4) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=ktls&sektion=4&manpath=FreeBSD+15.1-RELEASE+and+Ports.quarterly
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.8.1“kTLS 的对称加密卸载”、2.8.3“用户态与内核态的边界”、2.8.4“加密加速的硬件接口”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
KTLS(4) 		     Kernel Interfaces Manual			 KTLS(4)

NAME
     ktls -- kernel Transport Layer Security

SYNOPSIS
     options KERN_TLS

DESCRIPTION
     The  ktls	facility  allows  the kernel to perform Transport Layer Security
     (TLS) framing on TCP sockets.  With  ktls,  the  initial  handshake  for  a
     socket using TLS is performed in userland.  Once the session keys are nego-
     tiated,  they  are  provided  to  the  kernel  via the TCP_TXTLS_ENABLE and
     TCP_RXTLS_ENABLE socket options.	Both  socket  options  accept  a  struct
     tls_enable  structure as their argument.  The members of this structure de-
     scribe the cipher suite used for the TLS session and  provide  the  session
     keys used for the respective direction.

     ktls  only permits the session keys to be set once in each direction.  As a
     result, applications must disable rekeying when using ktls.

   Modes
     ktls can operate in different modes.  A  given  socket  may  use  different
     modes  for  transmit and receive, or a socket may only offload a single di-
     rection.  The available modes are:

     TCP_TLS_MODE_NONE	    ktls is not enabled.

     TCP_TLS_MODE_SW	    TLS records are encrypted or decrypted in the kernel
			    in the socket layer via  crypto(9).   Typically  the
			    encryption	or  decryption is performed in software,
			    but it may also be performed by co-processors.

     TCP_TLS_MODE_IFNET     TLS records are encrypted or decrypted by  the  net-
			    work  interface card (NIC).  In this mode, the net-
			    work stack does not work with encrypted  data.   In-
			    stead,  the NIC encrypts TLS records as they are be-
			    ing transmitted, or decrypts received  TLS  records
			    before providing them to the host.

			    Network  interfaces  which support this feature will
			    advertise the TXTLS4 (for IPv4) and/or  TXTLS6  (for
			    IPv6)   capabilities  as  reported	by  ifconfig(8).
			    These capabilities can also be controlled by  ifcon-
			    fig(8).

			    If	a network interface supports rate limiting (also
			    known as packet pacing) for TLS offload, the  inter-
			    face will advertise the TXTLS_RTLMT capability.
```

## 说明

节选 NAME／SYNOPSIS 与 DESCRIPTION 首两段、Modes 全节；Transmit／Receive 操作细节与后续节未引。抓取件保留手册页原始换行与缩进。
