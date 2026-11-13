# cam(4) — FreeBSD 内核接口手册页（CAM 子系统）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=cam&sektion=4
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.10.2“SCSI 子系统的主导者”补证（D2 块）：CAM 的模块化分层与自动挂接（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     options SCSI_NO_SENSE_STRINGS
     options SCSI_NO_OP_STRINGS
     options SCSI_DELAY=8000

DESCRIPTION
     The CAM subsystem provides a uniform and modular system for the implementa-
     tion  of  drivers to control various SCSI, ATA, NVMe, and MMC / SD devices,
     and to utilize different SCSI, ATA,  NVMe,  and  MMC  /  SD  host	adapters
     through  host  adapter  drivers.  When the system probes buses, it attaches
     any devices it finds to the appropriate drivers.  The pass(4) driver, if it
     is configured in the kernel, will attach to all devices.

KERNEL CONFIGURATION
     There are a number of generic kernel configuration options for the CAM sub-
     system:

     CAM_BOOT_DELAY	    Additional time to wait after the  static  parts  of
			    the  kernel have run to allow for discovery of addi-
			    tional devices which may take time to connect,  such
			    as USB attached storage.

     CAM_IOSCHED_DYNAMIC    Enable  dynamic decisions in the I/O scheduler based
			    on hints and the current performance of the  storage
			    devices.

     CAM_IO_STATS	    Enable collection of statistics for periph devices.

     CAM_TEST_FAILURE	    Enable ability to simulate I/O failures.

     CAMDEBUG		    This option compiles in all the CAM debugging printf
			    code.   This  will	not actually cause any debugging
			    information to be printed out when included  by  it-
			    self.  See below for details.

     CAM_MAX_HIGHPOWER=4    This sets the maximum allowable number of concurrent
			    "high  power" commands.  A "high power" command is a
			    command that takes more electrical power  than  most
			    to	complete.   An example of this is the SCSI START
```

## 引文摘录（空白已归一，供逐字核对）

options SCSI_NO_SENSE_STRINGS options SCSI_NO_OP_STRINGS options SCSI_DELAY=8000 DESCRIPTION The CAM subsystem provides a uniform and modular system for the implementa- tion of drivers to control various SCSI, ATA, NVMe, and MMC / SD devices, and to utilize different SCSI, ATA, NVMe, and MMC / SD host adapters through host adapter drivers. When the system probes buses, it attaches any devices it finds to the appropriate drivers. The pass(4) driver, if it is configured in the kernel, will attach to all devices. KERNEL CONFIGURATION There are a number of generic kernel configuration options for the CAM sub- system: CAM_BOOT_DELAY Additional time to wait after the static parts of the kernel have run to allow for discovery of addi- tional devices which may take time to connect, such as USB attached storage. CAM_IOSCHED_DYNAMIC Enable dynamic decisions in the I/O scheduler based on hints and the current performance of the storage devices. CAM_IO_STATS Enable collection of statistics for periph devices. CAM_TEST_FAILURE Enable ability to simulate I/O failures. CAMDEBUG This option compiles in all the CAM debugging printf code. This will not actually cause any debugging information to be printed out when included by it- self. See below for details. CAM_MAX_HIGHPOWER=4 This sets the maximum allowable number of concurrent "high power" commands. A "high power" command is a command that takes more electrical power than most to complete. An example of this is the SCSI START
