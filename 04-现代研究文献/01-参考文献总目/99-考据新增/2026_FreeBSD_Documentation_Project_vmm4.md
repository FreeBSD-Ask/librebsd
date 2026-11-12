# FreeBSD vmm(4) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=vmm&sektion=4
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly，手册页日期 December 30, 2024
- 用途：Task 8.2 G4 · V37.3.7.2“bhyve 与 KVM 的架构对照”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
NAME
     vmm.ko -- bhyve virtual machine monitor

SYNOPSIS
     To load the driver as a module at boot, add this line to loader.conf(5):

	   vmm_load="YES"

     The module can also be loaded manually with kldload(8):

	   kldload vmm

DESCRIPTION
     vmm.ko provides the kernel portion of the bhyve(4) hypervisor.  The follow-
     ing platforms are supported:

     *	 amd64:  An  Intel  CPU with VT-x/EPT or AMD CPU with SVM support is re-
	 quired.

     *	 arm64: The boot CPU must start in EL2 and the system must have a  GICv3
	 interrupt controller.	VHE support will be used if available.

     *	 riscv: The CPUs must implement the H (hypervisor) RISC-V ISA extension.

     PCI  device  passthrough  to  a virtual machine requires hardware with VT-d
     support and is available only on amd64.

HISTORY
     vmm.ko  first appeared in FreeBSD 10.0.  arm64 and riscv support first ap-
     peared in FreeBSD 15.0.
```

## 说明

节选 NAME／SYNOPSIS／DESCRIPTION／HISTORY；PCI PASSTHROUGH、LOADER TUNABLES、EXAMPLES 未引。抓取件保留手册页原始换行与缩进。
