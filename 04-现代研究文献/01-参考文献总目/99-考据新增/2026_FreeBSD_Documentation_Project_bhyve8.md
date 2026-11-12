# FreeBSD bhyve(8) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.7.4“替代关系的生态位”、3.5.4“bhyve 的启动与控制接点”补证（D2 块，ref_id 见库）

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

## 说明

节选 NAME／DESCRIPTION 首三段与 `-c` 选项（虚拟 CPU 上限段）；其余选项与 EXAMPLES 未引。抓取件保留手册页原始换行与缩进。

节选二取自同页 DESCRIPTION 第三段（boot ROM／bhyveload／edk2-bhyve），与节选一为同一份抓取件的切片。
