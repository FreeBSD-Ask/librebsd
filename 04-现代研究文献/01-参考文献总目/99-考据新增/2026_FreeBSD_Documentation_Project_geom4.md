# FreeBSD geom(4) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=geom&sektion=4&manpath=FreeBSD+15.1-RELEASE+and+Ports.quarterly
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.4.2“provider 与 geom 的配对”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
GEOM(4) 		     Kernel Interfaces Manual			 GEOM(4)

NAME
     GEOM -- modular disk I/O request transformation framework

SYNOPSIS
     options GEOM_CACHE
     options GEOM_CONCAT
     options GEOM_ELI
     options GEOM_GATE
     options GEOM_JOURNAL
     options GEOM_LABEL
     options GEOM_LINUX_LVM
     options GEOM_MAP
     options GEOM_MIRROR
     options GEOM_MOUNTVER
     options GEOM_MULTIPATH
     options GEOM_NOP
     options GEOM_PART_APM
     options GEOM_PART_BSD
     options GEOM_PART_BSD64
     options GEOM_PART_EBR
     options GEOM_PART_EBR_COMPAT
     options GEOM_PART_GPT
     options GEOM_PART_LDM
     options GEOM_PART_MBR
     options GEOM_RAID
     options GEOM_RAID3
     options GEOM_SHSEC
     options GEOM_STRIPE
     options GEOM_UZIP
     options GEOM_VIRSTOR
     options GEOM_ZERO

DESCRIPTION
     The  GEOM	framework provides an infrastructure in which "classes" can per-
     form transformations on disk I/O requests on their path from the upper ker-
     nel to the device drivers and back.

     Transformations in a GEOM context range from the simple geometric displace-
     ment performed in typical disk partitioning modules  over	RAID  algorithms
     and  device  multipath resolution to full blown cryptographic protection of
     the stored data.

     Compared to traditional "volume management", GEOM differs from most and  in
     some cases all previous implementations in the following ways:

     *	 GEOM  is  extensible.	 It  is trivially simple to write a new class of
	 transformation and it will not be given stepchild treatment.  If  some-
	 one  for  some reason wanted to mount IBM MVS diskpacks, a class recog-
	 nizing and configuring their VTOC information would be a  trivial  mat-
	 ter.

     *	 GEOM is topologically agnostic.  Most volume management implementations
	 have  very  strict  notions of how classes can fit together, very often
	 one fixed hierarchy is provided, for instance, subdisk - plex - volume.
```

## 抓取正文（节选二：TERMINOLOGY AND TOPOLOGY）

```
TERMINOLOGY AND TOPOLOGY
     GEOM is quite object oriented and consequently the  terminology  borrows  a
     lot of context and semantics from the OO vocabulary:

     A "class", represented by the data structure g_class implements one partic-
     ular  kind of transformation.  Typical examples are MBR disk partition, BSD
     disklabel, and RAID5 classes.

     An instance of a class is called a  "geom"  and  represented  by  the  data
     structure g_geom.	In a typical i386 FreeBSD system, there will be one geom
     of class MBR for each disk.

     A	"provider",  represented  by the data structure g_provider, is the front
     gate at which a geom offers service.  A  provider	is  "a	disk-like  thing
     which appears in /dev" - a logical disk
```

## 说明

节选 NAME／SYNOPSIS（类选项清单）与 DESCRIPTION 前三段；SYNOPSIS 后文、类间堆叠规则与 IO 请求路径细节未引。抓取件保留手册页原始换行与缩进。

节选二取自同一页 TERMINOLOGY AND TOPOLOGY 节前三段（class／geom／provider 三段定义）；后续拓扑示例与实现细节未引。两段节选页码一致，为同一份网页抓取件的两处切片。
