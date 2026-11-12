# FreeBSD bhyve(8) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.3.7.4“替代关系的生态位”补证（D2 块，ref_id 见库）

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

## 说明

节选 NAME／DESCRIPTION 首三段与 `-c` 选项（虚拟 CPU 上限段）；其余选项与 EXAMPLES 未引。抓取件保留手册页原始换行与缩进。
