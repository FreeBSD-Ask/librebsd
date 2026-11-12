# FreeBSD gmirror(8) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=gmirror&sektion=8
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.6.1“软 RAID 的镜像与条带”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
GMIRROR(8)		     System Manager's Manual		      GMIRROR(8)

NAME
     gmirror -- control utility for mirrored devices

SYNOPSIS
     To compile GEOM_MIRROR into your kernel, add the following lines to your
     kernel configuration file:

	   options GEOM_MIRROR

     Alternatively, to load the GEOM_MIRROR module at boot time, add the
     following line to your loader.conf(5):

	   geom_mirror_load="YES"

     Usage of the gmirror utility:

     gmirror label [-Fhnv] [-b balance] [-s slice] name prov ...
     gmirror clear [-v] prov ...
     gmirror status
     gmirror load
     gmirror unload

DESCRIPTION
     The  gmirror  utility  is	used for mirror (RAID1) configurations.  After a
     mirror's creation, all components are  detected  and  configured automati-
     cally.   All  operations like failure detection, stale component detection,
     rebuild of stale components, etc. are also done automatically.  The gmirror
     utility uses on-disk metadata (stored in the  provider's  last  sector)  to
     store  all needed information.  Since the last sector is used for this pur-
     pose, it is possible to place a root file system on a mirror.

     The first argument to gmirror indicates an action to be performed:

     label	 Create a mirror.  The order of components is important, because
		 a component's priority is based on its position (starting  from
		 0  to 255).  The component with the biggest priority is used by
		 the prefer balance algorithm and is also used as a master  com-
		 ponent  when resynchronization is  needed, e.g. after a power
		 failure when the device was open for writing.
```

## 说明

节选 NAME／SYNOPSIS（编译与模块装载、部分子命令）与 DESCRIPTION 首两段及 `label` 子命令首段；其余子命令与 `-b balance` 算法清单（load／prefer／round-robin／split）未全引。
