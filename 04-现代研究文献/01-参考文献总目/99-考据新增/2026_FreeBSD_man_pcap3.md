# pcap(3) — FreeBSD 库函数手册页（Packet Capture library）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=pcap&sektion=3
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.6.4“高速抓包的工具链”补证（D2 块）：用户态高层接口与 savefile（D2 块，ref_id 见库）

## 抓取正文（节选）

```
NAME
     pcap - Packet Capture library

SYNOPSIS
     #include <pcap/pcap.h>

DESCRIPTION
     The  Packet  Capture library provides a high level interface to packet cap-
     ture systems. All packets on the network, even  those  destined  for  other
     hosts, are accessible through this mechanism.  It also supports saving cap-
     tured packets to a ``savefile'', and reading packets from a ``savefile''.

   Initializing
     pcap_init()  initializes the library.  It takes an argument giving options;
     currently, the options are:

     PCAP_CHAR_ENC_LOCAL
	    Treat all strings supplied as arguments, and return all  strings  to
	    the caller, as being in the local character encoding.

     PCAP_CHAR_ENC_UTF_8
	    Treat  all	strings supplied as arguments, and return all strings to
	    the caller, as being in UTF-8.

     On UNIX-like systems, the local character encoding is assumed to be  UTF-8,
     so no character encoding transformations are done.

     On Windows, the local character encoding is the local ANSI code page.

     If  pcap_init()  is  called, the deprecated pcap_lookupdev() routine always
     fails, so it should not be used, and, on Windows,	pcap_create()  does  not
     attempt to handle UTF-16LE strings.

     If  pcap_init()  is  not  called, strings are treated as being in the local
     ANSI code page on Windows, pcap_lookupdev() will succeed if there is a  de-
     vice  on  which  to  capture,  and  pcap_create() makes an attempt to check
     whether the string passed as an argument is a UTF-16LE string -  note  that
     this  attempt is unsafe, as it may run past the end of the string - to han-
```

## 引文摘录（空白已归一，供逐字核对）

NAME pcap - Packet Capture library SYNOPSIS #include <pcap/pcap.h> DESCRIPTION The Packet Capture library provides a high level interface to packet cap- ture systems. All packets on the network, even those destined for other hosts, are accessible through this mechanism. It also supports saving cap- tured packets to a ``savefile'', and reading packets from a ``savefile''. Initializing pcap_init() initializes the library. It takes an argument giving options; currently, the options are: PCAP_CHAR_ENC_LOCAL Treat all strings supplied as arguments, and return all strings to the caller, as being in the local character encoding. PCAP_CHAR_ENC_UTF_8 Treat all strings supplied as arguments, and return all strings to the caller, as being in UTF-8. On UNIX-like systems, the local character encoding is assumed to be UTF-8, so no character encoding transformations are done. On Windows, the local character encoding is the local ANSI code page. If pcap_init() is called, the deprecated pcap_lookupdev() routine always fails, so it should not be used, and, on Windows, pcap_create() does not attempt to handle UTF-16LE strings. If pcap_init() is not called, strings are treated as being in the local ANSI code page on Windows, pcap_lookupdev() will succeed if there is a de- vice on which to capture, and pcap_create() makes an attempt to check whether the string passed as an argument is a UTF-16LE string - note that this attempt is unsafe, as it may run past the end of the string - to han-
