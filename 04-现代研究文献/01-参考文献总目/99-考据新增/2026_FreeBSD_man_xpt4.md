# xpt(4) — FreeBSD 内核接口手册页（CAM 传输层接口）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=xpt&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.10.2“SCSI 子系统的主导者”补证（D2 块）：传输层向用户态暴露 CCB（D2 块，ref_id 见库）

## 抓取正文（节选）

```

NAME
     xpt -- CAM transport layer interface

SYNOPSIS
     None.

DESCRIPTION
     The  xpt  driver  provides a way for userland applications to issue certain
     CAM CCBs to the kernel.

     Since the xpt driver allows direct access to the CAM subsystem, system  ad-
     ministrators  should  exercise caution when granting access to this driver.
     If used improperly, this driver can allow userland applications to crash  a
     machine or cause data loss.

KERNEL CONFIGURATION
     There  is	no  kernel configuration required for the xpt driver.  It is en-
     abled when SCSI support is enabled in the kernel.	There is one instance of
     the xpt driver per CAM transport layer instance.  Since there is  currently
     only  one CAM transport layer, there will only be one instance of this dri-
     ver.

IOCTLS
     CAMIOCOMMAND













```

## 引文摘录（空白已归一，供逐字核对）

NAME xpt -- CAM transport layer interface SYNOPSIS None. DESCRIPTION The xpt driver provides a way for userland applications to issue certain CAM CCBs to the kernel. Since the xpt driver allows direct access to the CAM subsystem, system ad- ministrators should exercise caution when granting access to this driver. If used improperly, this driver can allow userland applications to crash a machine or cause data loss. KERNEL CONFIGURATION There is no kernel configuration required for the xpt driver. It is en- abled when SCSI support is enabled in the kernel. There is one instance of the xpt driver per CAM transport layer instance. Since there is currently only one CAM transport layer, there will only be one instance of this dri- ver. IOCTLS CAMIOCOMMAND
