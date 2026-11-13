<!-- 网页存档｜来源：https://man.netbsd.org/autoconf.9｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# autoconf.9 — NetBSD 手册页（autoconfiguration framework）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
AUTOCONF(9) NetBSD Kernel Developer's Manual AUTOCONF(9)
 NAME 
 autoconf , config_search , config_found , config_match , config_attach ,
 config_attach_pseudo , config_detach , config_detach_children ,
 config_deactivate , config_defer , config_interrupts , config_mountroot ,
 config_pending_incr , config_pending_decr , config_finalize_register --
 autoconfiguration framework
 SYNOPSIS 
 #include <sys/param.h> 
 #include <sys/device.h> 
 #include <sys/errno.h> 
 cfdata_t 
 config_search ( device_t parent , void *aux , const struct cfargs * );
 device_t 
 config_found ( device_t parent , void *aux , cfprint_t print ,
 const struct cfargs * );
 int 
 config_match ( device_t parent , cfdata_t cf , void *aux );
 int 
 config_probe ( device_t parent , cfdata_t cf , void *aux );
 device_t 
 config_attach ( device_t parent , cfdata_t cf , void *aux , cfprint_t print ,
 const struct cfargs * );
 device_t 
 config_attach_pseudo ( cfdata_t cf );
 int 
 config_detach ( device_t dev , int flags );
 int 
 config_detach_children ( device_t dev , int flags );
 int 
 config_deactivate ( device_t dev );
 int 
 config_defer ( device_t dev , void (*func)(device_t) );
 void 
 config_interrupts ( device_t dev , void (*func)(device_t) );
 void 
 config_mountroot ( device_t dev , void (*func)(device_t) );
 void 
 config_pending_incr ();
 void 
 config_pending_decr ();
 int 
 config_finalize_register ( device_t dev , int (*func)(device_t) );
 DESCRIPTION 
 Autoconfiguration is the process of matching hardware devices with an
 appropriate device driver. In its most basic form, autoconfiguration
 consists of the recursive process of finding and attaching all devices on
 a bus, including other busses.
 The autoconfiguration framework supports direct configuration where the
 bus driver can determine the devices present. The autoconfiguration
 framework also supports indirect configuration where the drivers must
 probe the bus looking for the presence of a device. Direct configuration
 is preferred since it can find hardware regardless of the presence of
 proper drivers.
 The autoconfiguration process occurs at system bootstrap and is driven by
 a table generated from a ``machine description'' file by config(1) . For
 a description of the config(1) ``device definition'' language, see
 config(9) .
 Each device must have a name consisting of an alphanumeric string that
 ends with a unit number. The unit number identifies an instance of the
 driver. Device data structures are allocated dynamically during autocon-
 figuration, giving a unique address for each instance.
 Several of the autoconfiguration functions take a strongly-typed variadic
 list of arguments to pass information from driver autoconfiguration func-
 tions to the kernel's autoconfiguration system. This list is constructed
 using the CFARGS () macro, like this example:
 config_search(self, NULL,
 CFARGS(.search = mainbus_search,
 .iattr = "mainbus"));
 Each tag is followed by a tag-specific value.
 submatch A pointer to a `submatch' function used in direct con-
 figuration.
 search A pointer to a `search' function used in indirect con-
 figuration.
 iattr A pointer to a constant C string ( const char * ) specify-
 ing an interface attribute. If a parent device carries
 only a single interface attribute, then this argument
 may be omitted. If an interface attribute is specified
 that the parent device does not carry, or no interface
 attribute is specified and the parent device carries
 more than one, behavior is undefined. On kernels built
 with the DIAGNOSTIC option, this may result in an asser-
 tion panic.
 locators A pointer to a constant array of integers ( const int * )
 containing interface attribute-specific locators.
 devhandle A devhandle_t (passed by value) corresponding to the
 device being attached.
 If no arguments are to be passed, the special value CFARGS_NONE may be
 used in place of the CFARGS () macro.
 FUNCTIONS 
 config_search ( parent , aux , cfargs )
 Cfargs consumed: search , iattr , locators .
 Performs indirect configuration of physical devices.
 config_search () iterates over all potential children, calling
 the given search function If no search function is specified,
 applies the potential child's match function instead. The
 argument parent is the pointer to the parent's device struc-
 ture. If an interface attribute is specified, only potential
 children eligible to attach to that interface attribute will be
 consulted. If specified, the locators argument lists the loca-
 tor values for the device and are passed to the search func-
 tion. The given aux argument describes the device that has
 been found and is simply passed on through the search function
 to the child. config_search () returns a pointer to the config-
 uration data that indicates the best-matched child or NULL oth-
 erwise.
 The role of the search function is to call config_probe () for
 each potential child and call config_attach () for any positive
 matches. If no search function is specified, then the parent
 should record the return value from config_search () and call
 config_attach () itself.
 Note that this function is designed so that it can be used to
 apply an arbitrary function to all potential children. In this
 case callers may choose to ignore the return value.
 config_found ( parent , aux , print , cfargs )
 Cfargs consumed: submatch , iattr , locators , devhandle .
 Performs direct configuration on a physical device.
 config_found () is called by the parent and in turn calls the
 specified submatch function as determined by the configuration
 table. The submatch function compares user-specified locators
 from the machine description file against those specifying a
 found device, calling config_match () if they match (including
 wildcard matching). If a submatch function is not specified,
 then driver match functions are called directly. The argument
 parent is the pointer to the parent's device structure. If an
 interface attribute is specified, only potential children eli-
 gible to attach to that interface attribute will be consulted.
 If specified, the locators argument lists the locator values
 for the found device and may be used by the submatch function
 and will be recorded in the device structure of the child
 device. The given aux argument describes the device that has
 been found. config_found () internally uses config_search ().
 The softc structure for the matched device will be allocated,
 and the appropriate driver attach function will be called. If
 the device is matched, the system prints the name of the child
 and parent devices, and then calls the print function to pro-
 duce additional information if desired. If no driver takes a
 match, the same print function is called to complain. The
 print function is called with the aux argument and, if the
 matches failed, the full name (including unit number) of the
 parent device, otherwise NULL. The print function must return
 an integer value.
 Two special strings, ``not configured'' and ``unsupported''
 will be appended automatically to non-driver reports if the
 return value is UNCONF or UNSUPP respectively; otherwise the
 function should return the value QUIET. If a device handle is
 specified, that handle will be associated with the resulting
 child device structure if a driver matches.
 config_found () returns a pointer to the attached device's
 device structure if the device is attached, NULL otherwise.
 Most callers can ignore this value, since the system will
 already have printed a diagnostic.
 config_match ( parent , cf , aux )
 Match a device (direct configuration). Invokes the driver's
 match function according to the configuration table. The
 config_match () function returns a nonzero integer indicating
 the confidence of supporting this device and a value of 0 if
 the driver doesn't support the device.
 config_probe ( parent , cf , aux )
 Probe for a device (indirect configuration). Invokes the
 driver's match function according to the configuration table.
 The config_probe () function returns a nonzero integer to indi-
 cate a successful probe and a value of 0 otherwise. Unlike
 config_match (), the return value of config_probe () is not
 intended to reflect a confidence value.
 config_attach ( parent , cf , aux , print , cfargs )
 Cfargs consumed: locators , devhandle .
 Attach a found device. Allocates the memory for the softc 
 structure and calls the drivers attach function according to
 the configuration table. If successful, config_attach ()
 returns a pointer to the device structure. If unsuccessful, it
 returns NULL.
 config_attach_pseudo ( cf )
 Create an instance of a pseudo-device driver. config(5) syntax
 allows the creation of pseudo-devices from which regular
 device_t instances can be created. Such objects are similar to
 the devices that attach at the root of the device tree.
 The caller is expected to allocate and fill the cfdata_t object
 and pass it to config_attach_pseudo (). The content of that
 object is similar to what is returned by config_search () for
 regular devices.
 config_detach ( dev , flags )
 Called by the parent to detach the child device. The second
 argument flags contains detachment flags. Valid values are
 DETACH_FORCE (force detachment, e.g., because of hardware
 removal) and DETACH_QUIET (do not print a notice).
 config_detach () returns zero if successful and an error code
 otherwise. config_detach () is always called from a thread con-
 text, allowing condition variables to be used while the device
 detaches itself.
 config_detach_children ( dev , flags )
 Iterate through all attached devices, calling config_detach ()
 for each child of dev , passing flags . If detaching any child
 results in an error, the iteration will halt and any remaining
 devices will not be detached. config_detach_children () returns
 zero if successful and an error code otherwise.
 config_deactivate ( dev )
 Called by the parent to deactivate the child device dev .
 config_deactivate () is called from interrupt context to immedi-
 ately relinquish resources and notify dependent kernel subsys-
 tems that the device is about to be detached. At some later
 point config_detach () will be called to finalise the removal of
 the device.
 config_defer ( dev , func )
 Called by the child to defer the remainder of its configuration
 until all its parent's devices have been attached. At this
 point, the function func is called with the argument dev .
 config_interrupts ( dev , func )
 Called by the child to defer the remainder of its configuration
 until interrupts are enabled. At this point, the function func 
 is called with the argument dev .
 config_mountroot ( dev , func )
 Called by the child to defer the remainder of its configuration
 until the root file system is mounted. At this point, the
 function func is called with the argument dev . This is used
 for devices that need to load firmware image from a mounted
 file system.
 config_pending_incr ()
 Increment the config_pending semaphore. It is used to account
 for deferred configurations before mounting the root file sys-
 tem.
 config_pending_decr ()
 Decrement the config_pending semaphore. It is used to account
 for deferred configurations before mounting the root file sys-
 tem.
 config_finalize_register ( dev , func )
 Register a function to be called after all real devices have
 been found.
 Registered functions are all executed until all of them return
 0. The callbacks should return 0 to indicate they do not
 require to be called another time, but they should be aware
 that they still might be in case one of them returns 1.
 CODE REFERENCES 
 The autoconfiguration framework itself is implemented within the file
 sys/kern/subr_autoconf.c . Data structures and function prototypes for
 the framework are located in sys/sys/device.h .
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》联网补证（D2 块；官方手册页，collection=NetBSD-current）。
