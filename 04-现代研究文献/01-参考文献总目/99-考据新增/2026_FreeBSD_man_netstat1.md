# netstat(1) — FreeBSD 用户命令手册页（网络状态）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=netstat&sektion=1
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.9.8.4“并发连接的压测法”补证（D2 块）：-m 内存统计观察面（D2 块，ref_id 见库）

## 抓取正文（节选一）

```
	     -M      Use an alternative core See "GENERAL OPTIONS".

	     -N      Use an alternative kernel image See "GENERAL OPTIONS".

	     -j jail
		     Run inside a jail.  See "GENERAL OPTIONS".

     netstat -m [-M core] [-N system] [-j jail]
	     Show  statistics  recorded  by  the  memory   management	routines
	     (mbuf(9)).  The network manages a private pool of memory buffers.

	     -M      Use an alternative core See "GENERAL OPTIONS".

	     -N      Use an alternative kernel image See "GENERAL OPTIONS".

	     -j jail
		     Run inside a jail.  See "GENERAL OPTIONS".

     netstat -B [-z] [-I interface] [-j jail]
	     Show statistics about bpf(4) peers.  This includes information like
	     how many packets have been matched, dropped and received by the bpf
	     device,  also  information  about	current  buffer sizes and device
	     states.

	     The bpf(4) flags displayed when netstat is invoked with the -B  op-
	     tion  represent  the  underlying  parameters of the bpf peer.  Each
	     flag is represented as a single lower case letter.  The mapping be-
	     tween the letters and flags in order of appearance are:

	     p	  Set if listening promiscuously
	     i	  BIOCIMMEDIATE has been set on the device
	     f	  BIOCGHDRCMPLT status: source link addresses are  being  filled
		  automatically
	     s	  BIOCGSEESENT	status:  see packets originating locally and re-
		  motely on the interface.
	     a	  Packet reception generates a signal
	     l	  BIOCLOCK status: descriptor has been locked

```

## 抓取正文（节选二）

```

	     -N      Use an alternative kernel image See "GENERAL OPTIONS".

	     -j jail
		     Run inside a jail.  See "GENERAL OPTIONS".

     netstat -m [-M core] [-N system] [-j jail]
	     Show  statistics  recorded  by  the  memory   management	routines
	     (mbuf(9)).  The network manages a private pool of memory buffers.

	     -M      Use an alternative core See "GENERAL OPTIONS".

	     -N      Use an alternative kernel image See "GENERAL OPTIONS".

	     -j jail
		     Run inside a jail.  See "GENERAL OPTIONS".

     netstat -B [-z] [-I interface] [-j jail]
	     Show statistics about bpf(4) peers.  This includes information like
	     how many packets have been matched, dropped and received by the bpf
	     device,  also  information  about	current  buffer sizes and device
	     states.

	     The bpf(4) flags displayed when netstat is invoked with the -B  op-
	     tion  represent  the  underlying  parameters of the bpf peer.  Each
	     flag is represented as a single lower case letter.  The mapping be-
	     tween the letters and flags in order of appearance are:

	     p	  Set if listening promiscuously
	     i	  BIOCIMMEDIATE has been set on the device
	     f	  BIOCGHDRCMPLT status: source link addresses are  being  filled
		  automatically
	     s	  BIOCGSEESENT	status:  see packets originating locally and re-
		  motely on the interface.
	     a	  Packet reception generates a signal
	     l	  BIOCLOCK status: descriptor has been locked

	     For more information about these flags, please refer to bpf(4).
```

## 引文摘录（空白已归一，供逐字核对）

-M Use an alternative core See "GENERAL OPTIONS". -N Use an alternative kernel image See "GENERAL OPTIONS". -j jail Run inside a jail. See "GENERAL OPTIONS". netstat -m [-M core] [-N system] [-j jail] Show statistics recorded by the memory management routines (mbuf(9)). The network manages a private pool of memory buffers. -M Use an alternative core See "GENERAL OPTIONS". -N Use an alternative kernel image See "GENERAL OPTIONS". -j jail Run inside a jail. See "GENERAL OPTIONS". netstat -B [-z] [-I interface] [-j jail] Show statistics about bpf(4) peers. This includes information like how many packets have been matched, dropped and received by the bpf device, also information about current buffer sizes and device states. The bpf(4) flags displayed when netstat is invoked with the -B op- tion represent the underlying parameters of the bpf peer. Each flag is represented as a single lower case letter. The mapping be- tween the letters and flags in order of appearance are: p Set if listening promiscuously i BIOCIMMEDIATE has been set on the device f BIOCGHDRCMPLT status: source link addresses are being filled automatically s BIOCGSEESENT status: see packets originating locally and re- motely on the interface. a Packet reception generates a signal l BIOCLOCK status: descriptor has been locked

-N Use an alternative kernel image See "GENERAL OPTIONS". -j jail Run inside a jail. See "GENERAL OPTIONS". netstat -m [-M core] [-N system] [-j jail] Show statistics recorded by the memory management routines (mbuf(9)). The network manages a private pool of memory buffers. -M Use an alternative core See "GENERAL OPTIONS". -N Use an alternative kernel image See "GENERAL OPTIONS". -j jail Run inside a jail. See "GENERAL OPTIONS". netstat -B [-z] [-I interface] [-j jail] Show statistics about bpf(4) peers. This includes information like how many packets have been matched, dropped and received by the bpf device, also information about current buffer sizes and device states. The bpf(4) flags displayed when netstat is invoked with the -B op- tion represent the underlying parameters of the bpf peer. Each flag is represented as a single lower case letter. The mapping be- tween the letters and flags in order of appearance are: p Set if listening promiscuously i BIOCIMMEDIATE has been set on the device f BIOCGHDRCMPLT status: source link addresses are being filled automatically s BIOCGSEESENT status: see packets originating locally and re- motely on the interface. a Packet reception generates a signal l BIOCLOCK status: descriptor has been locked For more information about these flags, please refer to bpf(4).
