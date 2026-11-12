# FreeBSD zfs(4) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=zfs&sektion=4
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.7.1“ZFS 进入内核的路径”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
ZFS(4)			     Kernel Interfaces Manual			  ZFS(4)

NAME
     zfs -- tuning of the ZFS kernel module

DESCRIPTION
     The ZFS module supports these parameters:

     dbuf_cache_max_bytes=UINT64_MAXB (u64)
	     Maximum size in bytes of the dbuf cache.  The target size is deter-
	     mined by the MIN versus 1/2^dbuf_cache_shift (1/32nd) of the target
	     ARC  size.
```

## 说明

节选 NAME 与 DESCRIPTION 首段及第一个 tunable；其余 tuning 参数（dbuf／dmu／zfs_* 系列）未引。抓取件保留手册页原始换行与缩进。
