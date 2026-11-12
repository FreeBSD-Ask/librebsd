# FreeBSD cam(4) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=cam&sektion=4
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 用途：Task 8.2 G4 · V37.4.11.1“CAM 对 SCSI 子系统的替代”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
CAM(4)			     Kernel Interfaces Manual			  CAM(4)

NAME
     CAM -- Common Access Method Storage subsystem

SYNOPSIS
     device scbus
     device ada
     device cd
     device ch
     device da
     device pass
     device pt
     device sa

DESCRIPTION
     The CAM subsystem provides a uniform and modular system for the implementa-
     tion  of  drivers to control various SCSI, ATA, NVMe, and MMC / SD devices,
     and to utilize different SCSI, ATA,  NVMe,  and  MMC  /	SD  host	 adapters
     through  host  adapter  drivers.  When the system probes buses, it attaches
     any devices it finds to the appropriate drivers.
```

## 说明

节选 NAME／SYNOPSIS／DESCRIPTION 首段；KERNEL CONFIGURATION 及后文未引。抓取件保留手册页原始换行与缩进。
