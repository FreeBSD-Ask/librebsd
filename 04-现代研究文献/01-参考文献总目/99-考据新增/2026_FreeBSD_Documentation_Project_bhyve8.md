# FreeBSD bhyve(8) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.7.4“替代关系的生态位”、3.5.4“bhyve 的启动与控制接点”、3.5.3“虚拟设备的模拟层”、3.8.2“虚拟化平台的驱动支持”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
NAME
     bhyve -- run a guest operating system inside a virtual machine

DESCRIPTION
     bhyve  is	a  hypervisor that runs guest operating systems inside a virtual
     machine.  It can run guests on amd64  and	arm64  platforms  with	suitable
     hardware support.

     Parameters  such as the number of virtual CPUs, amount of guest memory, and
     I/O connectivity can be specified with command-line parameters.

     bhyve  runs until the guest operating system reboots or an unhandled hyper-
     visor exit is detected.

OPTIONS
     -c [[cpus=]numcpus][,sockets=n][,cores=n][,threads=n]
		 Number of guest virtual CPUs and/or the CPU topology.	The de-
		 fault value for each of numcpus, sockets, cores, and threads is
		 1.  If numcpus is not specified then it will be calculated from
		 the  other  arguments.  The topology must be consistent in that
		 the numcpus must equal  the  product  of  sockets,  cores,  and
		 threads.  If a setting is specified more than once the last one
		 has precedence.

		 The  maximum  number of virtual CPUs defaults to the number of
		 active  physical  CPUs  in  the  system   available   via   the
		 hw.vmm.maxcpu	sysctl(8)  variable.  The limit can be adjusted
		 via the hw.vmm.maxcpu loader tunable.
```

## 抓取正文（节选二：启动用固件与装载器）

```
     bhyve is typically used with a boot ROM that can load the guest operating
     system.  On  arm64  platforms, this is currently required.  If not using a
     boot ROM, the guest operating system must be loaded with bhyveload(8) or  a
     similar  boot  loader  before  running  bhyve, otherwise.   On  amd64, the
     edk2-bhyve package provides a UEFI firmware that can be used to  boot  the
     guest; on arm64 the u-boot-bhyve-arm64 package provides a U-Boot image that
     can be used to boot the guest.
```

## 抓取正文（节选三：-s 选项与 PCI EMULATION）

```
     -s slot,emulation[,conf]
		 Configure a virtual PCI slot and function.

		 bhyve	provides  PCI bus emulation and virtual devices that can
		 be attached to slots on the bus.  There are 32 available slots,
		 with the option of providing up to 8 functions per slot.

		 The slot can be specified in one of the following formats:

		 *   pcislot
		 *   pcislot:function
		 *   bus:pcislot:function

PCI EMULATION
     bhyve  provides  emulation  for various PCI devices.  They are specified by
     the -s slot,emulation,conf configuration's emulation argument, which can be
     one of the following:

     hostbridge      A simple host bridge.  This is usually configured	at  slot
		     0, and is required by most guest operating systems.

     amd_hostbridge  Emulation	identical to hostbridge using a PCI vendor ID of
		     AMD.

     passthru	     PCI pass-through device.

     virtio-net      Virtio network interface.

     virtio-blk      Virtio block storage interface.

     virtio-scsi     Virtio SCSI interface.

     virtio-9p	     Virtio 9p (VirtFS) interface.

     virtio-rnd      Virtio RNG interface.

     virtio-console  Virtio console interface, which exposes multiple  ports  to
		     the  guest in the form of simple char devices for simple IO
		     between the guest and host userspaces.

     virtio-input    Virtio input interface.

     ahci	     AHCI controller attached to arbitrary devices.

     ahci-cd	     AHCI controller attached to an ATAPI CD/DVD.

     ahci-hd	     AHCI controller attached to a SATA hard drive.

     e1000	     Intel e82545 network interface.

     uart	     PCI 16550 serial device.

     lpc	     LPC PCI-ISA bridge with COM1, COM2, COM3, and	COM4  16550
		     serial  ports, a boot ROM, and, optionally, a TPM module, a
		     fw_cfg type, and the debug/test device.

     fbuf	     Raw framebuffer device attached to VNC server.

     xhci	     eXtensible Host Controller Interface (xHCI) USB controller.

     nvme	     NVM Express (NVMe) controller.

     hda	     High Definition Audio Controller.
```

## 抓取正文（节选四：块存储后端）

```
   Block storage device backends:
     *	 /filename[,block-device-options]

     *	 /dev/xxx[,block-device-options]
```

## 说明

节选 NAME／DESCRIPTION 首三段与 `-c` 选项（虚拟 CPU 上限段）；其余选项与 EXAMPLES 未引。抓取件保留手册页原始换行与缩进。

节选二取自同页 DESCRIPTION 第三段（boot ROM／bhyveload／edk2-bhyve），与节选一为同一份抓取件的切片。

节选三取自同页 `-s` 选项首段与 PCI EMULATION 全节（hostbridge／passthru／virtio 系列／AHCI／e1000／nvme 等设备清单）；后端参数（网络、块存储）与后续 EXAMPLES 未引。

节选四取自同页“Block storage device backends”首两行（`/filename` 与 `/dev/xxx` 两种后端形式）；块设备选项（nocache／direct 等）与文件后端细则未引。
