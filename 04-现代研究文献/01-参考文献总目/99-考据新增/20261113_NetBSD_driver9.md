<!-- 网页存档｜来源：https://man.netbsd.org/driver.9｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# driver.9 — NetBSD 手册页（autoconfiguration interface for drivers）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
DRIVER(9) NetBSD Kernel Developer's Manual DRIVER(9)
 NAME 
 driver -- description of a device driver
 SYNOPSIS 
 #include <sys/param.h> 
 #include <sys/device.h> 
 #include <sys/errno.h> 
 static int 
 foo_match ( device_t parent , cfdata_t match , void *aux );
 static void 
 foo_attach ( device_t parent , device_t self , void *aux );
 static int 
 foo_detach ( device_t self , int flags );
 static int 
 foo_activate ( device_t self , enum devact act );
 DESCRIPTION 
 This page briefly describes the basic NetBSD autoconfiguration interface
 used by device drivers. For a detailed overview of the autoconfiguration
 framework see autoconf(9) .
 Each device driver must present to the system a standard autoconfigura-
 tion interface. This interface is provided by the cfattach structure.
 The interface to the driver is constant and is defined statically inside
 the driver. For example, the interface to driver `foo' is defined with:
 CFATTACH_DECL_NEW(foo, /* driver name */
 sizeof(struct foo_softc), /* size of instance data */
 foo_match, /* match/probe function */
 foo_attach, /* attach function */
 foo_detach, /* detach function */
 foo_activate); /* activate function */
 For each device instance controlled by the driver, the autoconfiguration
 framework allocates a block of memory to record device-instance-specific
 driver variables. The size of this memory block is specified by the sec-
 ond argument in the CFATTACH_DECL family of macros. The memory block is
 referred to as the driver's softc structure. The softc structure is only
 accessed within the driver, so its definition is local to the driver.
 Nevertheless, the softc structure should adopt the standard NetBSD con-
 figuration and naming conventions. For example, the softc structure for
 driver `foo' is defined with:
 struct foo_softc {
 device_t sc_dev; /* generic device info */
 /* device-specific state */
 };
 If a driver has character device interfaces accessed from userland, the
 driver must define the cdevsw structure. The structure is constant and
 is defined inside the driver. For example, the cdevsw structure for
 driver `foo' can be defined with:
 const struct cdevsw foo_cdevsw {
 .d_open = fooopen,
 .d_close = nullclose,
 .d_read = fooread,
 .d_write = nowrite,
 .d_ioctl = fooioctl,
 .d_stop = nostop,
 .d_tty = notty,
 .d_poll = foopoll,
 .d_mmap = nommap,
 .d_kqfilter = nokqfilter,
 .d_discard = nodiscard,
 .d_flag = D_OTHER | D_MPSAFE,
 };
 The structure variable must be named foo_cdevsw by appending the letters
 `_cdevsw' to the driver's base name. This convention is mandated by the
 autoconfiguration framework.
 If the driver `foo' has also block device interfaces, the driver must
 define the bdevsw structure. The structure is constant and is defined
 inside the driver. For example, the bdevsw structure for driver `foo' is
 defined with:
 const struct bdevsw foo_bdevsw {
 .d_open = fooopen,
 .d_close = fooclose,
 .d_strategy = foostrategy,
 .d_ioctl = fooioctl,
 .d_dump = nodump,
 .d_psize = nosize,
 .d_flag = D_DISK | D_MPSAFE,
 };
 The structure variable must be named foo_bdevsw by appending the letters
 `_bdevsw' to the driver's base name. This convention is mandated by the
 autoconfiguration framework.
 During system bootstrap, the autoconfiguration framework searches the
 system for devices. For each device driver, its match function is called
 (via its cfattach structure) to match the driver with a device instance.
 The match function is called with three arguments. This first argument
 parent is a pointer to the driver's parent device structure. The second
 argument match is a pointer to a data structure describing the autocon-
 figuration framework's understanding of the driver. Both the parent and
 match arguments are ignored by most drivers. The third argument aux con-
 tains a pointer to a structure describing a potential device-instance.
 It is passed to the driver from the parent. The match function would
 type-cast the aux argument to its appropriate attachment structure and
 use its contents to determine whether it supports the device. Depending
 on the device hardware, the contents of the attachment structure may con-
 tain ``locators'' to locate the device instance so that the driver can
 probe it for its identity. If the probe process identifies additional
 device properties, it may modify the members of the attachment structure.
 For these devices, the NetBSD convention is to call the match routine
 foo_probe () instead of foo_match () to make this distinction clear.
 Either way, the match function returns a nonzero integer indicating the
 confidence of supporting this device and a value of 0 if the driver
 doesn't support the device. Generally, only a single driver exists for a
 device, so the match function returns 1 for a positive match.
 The autoconfiguration framework will call the attach function (via its
 cfattach structure) of the driver which returns the highest value from
 its match function. The attach function is called with three arguments.
 The attach function performs the necessary process to initialise the
 device for operation. The first argument parent is a pointer to the
 driver's parent device structure. The second argument self is a pointer
 to the driver's device structure. The device's softc structure can be
 obtained from it using the device_private () function (see disk(9) ). The
 third argument aux is a pointer to the attachment structure. The parent 
 and aux arguments are the same as passed to the match function.
 The driver's attach function is called before system interrupts are
 enabled. If interrupts are required during initialisation, then the
 attach function should make use of config_interrupts () (see autoconf(9) ).
 Some devices can be removed from the system without requiring a system
 reboot. The autoconfiguration framework calls the driver's detach func-
 tion (via its cfattach structure) during device detachment. If the
 device does not support detachment, then the driver does not have to pro-
 vide a detach function. The detach function is used to relinquish
 resources allocated to the driver which are no longer needed. The first
 argument self is a pointer to the driver's device structure. It is the
 same structure as passed to the attach function. The second argument
 flags contains detachment flags. Valid values are DETACH_FORCE (force
 detachment; hardware gone) and DETACH_QUIET (do not print a notice).
 The activate function is used by some buses to notify drivers from inter-
 rupt context when detachment is imminent, with act set to
 DVACT_DEACTIVATE. Currently only pcmcia(9) and cardbus(9) use this. If
 the action is not supported the activate function should return
 EOPNOTSUPP.
 Most drivers will want to make use of interrupt facilities. Interrupt
 locators provided through the attachment structure should be used to
 establish interrupts within the system. Generally, an interrupt inter-
 face is provided by the parent. The interface will require a handler and
 a driver-specific argument to be specified. This argument is usually a
 pointer to the device-instance-specific softc structure. When a hardware
 interrupt for the device occurs the handler is called with the argument.
 Interrupt handlers should return 0 for ``interrupt not for me'', 1 for
 ``I took care of it'', or -1 for ``I guess it was mine, but I wasn't
 expecting it''.
 For a driver to be compiled into the kernel, config(1) must be aware of
 its existence. This is done by including an entry in files.<bus> in the
 directory containing the driver. For example, the driver foo attaching
 to bus bar with dependency on kernel module baz has the entry:
 device foo : baz 
 attach foo at bar 
 file dev/bar/foo.c foo 
 An entry can now be added to the machine description file:
 foo * at bar ? 
 For device interfaces of a driver to be compiled into the kernel,
 config(1) must be aware of its existence. This is done by including an
 entry in majors. < arch >. For example, the driver foo with character
 device interfaces, a character major device number cmaj , block device
 interfaces, a block device major number bmaj and dependency on kernel
 module baz has the entry:
 device-major foo char cmaj block bmaj baz 
 For a detailed description of the machine description file and the
 ``device definition'' language see config(9) .
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》联网补证（D2 块；官方手册页，collection=NetBSD-current）。
