<!-- 网页存档｜来源：https://man.netbsd.org/kauth.9｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# kauth.9 — NetBSD 手册页（kernel authorization subsystem）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
KAUTH(9) NetBSD Kernel Developer's Manual KAUTH(9)
 NAME 
 kauth -- kernel authorization framework
 SYNOPSIS 
 #include <sys/kauth.h> 
 DESCRIPTION 
 kauth , or kernel authorization, is the subsystem managing all authoriza-
 tion requests inside the kernel. It manages user credentials and rights,
 and can be used to implement a system-wide security policy. It allows
 external modules to plug-in the authorization process.
 kauth introduces some new concepts, namely ``scopes'' and ``listeners'',
 which will be detailed together with other useful information for kernel
 developers in this document.
 Types 
 Some kauth types include the following:
 kauth_cred_t Representing credentials that can be associated with an
 object. Includes user- and group-ids (real, effective,
 and save) as well as group membership information.
 kauth_scope_t Describes a scope.
 kauth_listener_t Describes a listener.
 Terminology 
 kauth operates in various ``scopes'', each scope holding a group of
 ``listeners''.
 Each listener works as a callback for when an authorization request
 within the scope is made. When such a request is made, all listeners on
 the scope are passed common information such as the credentials of the
 request context, an identifier for the requested operation, and possibly
 other information as well.
 Every listener examines the passed information and returns its decision
 regarding the requested operation. It can either return:
 KAUTH_RESULT_ALLOW The listener allows the operation.
 KAUTH_RESULT_DENY The listener denies the operation.
 KAUTH_RESULT_DEFER The listener defers the decision to other listeners.
 For an operation to be allowed, at least one listener has to return
 KAUTH_RESULT_ALLOW while no other listener returned KAUTH_RESULT_DENY.
 Scopes manage listeners that operate in the same aspect of the system.
 Kernel Programming Interface 
 kauth exports a KPI that allows developers both of NetBSD and third-party
 products to authorize requests, access and modify credentials, create and
 remove scopes and listeners, and perform other miscellaneous operations
 on credentials.
 Authorization Requests 
 kauth provides a single authorization request routine, which all autho-
 rization requests go through. This routine dispatches the request to the
 listeners of the appropriate scope, together with four optional user-data
 variables, and returns the augmented result.
 It is declared as
 int kauth_authorize_action ( kauth_scope_t scope , kauth_cred_t cred ,
 kauth_action_t op , void *arg0 , void *arg1 , void *arg2 , void *arg3 )
 An authorization request can return one of two possible values:
 0 (zero) indicates success; operation is allowed.
 EPERM indicates failure; operation is denied. See errno(2) .
 Each scope has its own authorization wrapper, to make it easy to call
 from various places by eliminating the need to specify the scope and/or
 cast values. The authorization wrappers are detailed in each scope's
 section.
 kauth_authorize_action () has several special cases, when it will always
 allow the request. These are for when the request is issued by the ker-
 nel itself (indicated by the credentials being either NOCRED or FSCRED),
 or when there was no definitive decision from any of the listeners (i.e.,
 it was not explicitly allowed or denied) and no security model was
 loaded.
 Generic Scope 
 The generic scope, ``org.netbsd.kauth.generic'', manages generic autho-
 rization requests in the kernel.
 The authorization wrapper for this scope is declared as
 int kauth_authorize_generic ( kauth_cred_t cred , kauth_action_t op , void 
 *arg0 )
 The following operations are available for this scope:
 KAUTH_GENERIC_ISSUSER
 Checks whether the credentials belong to the super-user.
 Using this request is strongly discouraged and should only be
 done as a temporary place-holder, as it is breaking the separa-
 tion between the interface for authorization requests from the
 back-end implementation.
 System Scope 
 The system scope, ``org.netbsd.kauth.system'', manages authorization
 requests affecting the entire system.
 The authorization wrapper for this scope is declared as
 int kauth_authorize_system ( kauth_cred_t cred , kauth_action_t op , enum 
 kauth_system_req req , void *arg1 , void *arg2 , void *arg3 )
 The following requests are available for this scope:
 KAUTH_SYSTEM_ACCOUNTING
 Check if enabling/disabling accounting allowed.
 KAUTH_SYSTEM_CHROOT
 req can be any of the following:
 KAUTH_REQ_SYSTEM_CHROOT_CHROOT
 Check if calling chroot(2) is allowed.
 KAUTH_REQ_SYSTEM_CHROOT_FCHROOT
 Check if calling fchroot(2) is allowed.
 KAUTH_SYSTEM_CPU
 Check CPU-manipulation access.
 req can be any of the following:
 KAUTH_REQ_SYSTEM_CPU_SETSTATE
 Set CPU state, including setting it online or offline.
 KAUTH_SYSTEM_DEBUG
 This request concentrates several debugging-related operations.
 KAUTH_SYSTEM_DEVMAPPER
 Check if operations on the device mapper dm(4) device are
 allowed.
 KAUTH_SYSTEM_FILEHANDLE
 Check if file handle operations allowed.
 KAUTH_SYSTEM_FS_EXTATTR
 Check if starting, stopping, enabling, or disabling extended
 attributes is allowed. arg1 is a struct mount * of the mount-
 point on which the operation is performed.
 KAUTH_SYSTEM_FS_SNAPSHOT
 Check if setting up a file system snapshot is allowed. arg1 is
 a struct mount * of the mount-point of which the snapshot is
 taken, and arg2 is a struct vnode * of the vnode where the snap-
 shot is expected to be.
 KAUTH_SYSTEM_FS_QUOTA
 Check if file system quota operations are allowed.
 arg1 is a struct mount * describing the file system mount in
 question. req can be one of the following:
 KAUTH_REQ_SYSTEM_FS_QUOTA_GET
 Check if retrieving quota information is allowed.
 arg2 is a uid_t with the user-id of the user whose
 quota information is to be retrieved.
 KAUTH_REQ_SYSTEM_FS_QUOTA_ONOFF
 Check if turning quota on/off is allowed.
 KAUTH_REQ_SYSTEM_FS_QUOTA_MANAGE
 Check if managing the quota by setting the quota/quota
 use is allowed.
 arg2 is a uid_t with the user-id of the user whose
 quota/quota use is to be set.
 KAUTH_REQ_SYSTEM_FS_QUOTA_NOLIMIT
 Check if bypassing the quota (not enforcing it) is
 allowed.
 KAUTH_SYSTEM_FS_RESERVEDSPACE
 Check if using the file system reserved space is allowed.
 KAUTH_SYSTEM_LFS
 Check if LFS-related operations are allowed. req can be one of
 the following:
 KAUTH_REQ_SYSTEM_LFS_MARKV
 Check if calling lfs_markv(2) is allowed.
 KAUTH_REQ_SYSTEM_LFS_BMAPV
 Check if calling lfs_bmapv(2) is allowed.
 KAUTH_REQ_SYSTEM_LFS_SEGCLEAN
 Check if calling lfs_segclean(2) is allowed.
 KAUTH_REQ_SYSTEM_LFS_SEGWAIT
 Check if calling lfs_segwait(2) is allowed.
 KAUTH_REQ_SYSTEM_LFS_FCNTL
 Check if operations on LFS through fcntl(2) are
 allowed.
 KAUTH_SYSTEM_MAP_VA_ZERO
 Check if changing the status of memory mapping of virtual
 address zero is allowed.
 KAUTH_SYSTEM_MODULE
 Check if a module request is allowed.
 arg1 is the command.
 KAUTH_SYSTEM_MKNOD
 Check if creating devices is allowed.
 KAUTH_SYSTEM_MOUNT
 Check if mount-related operations are allowed.
 req can be any of the following:
 KAUTH_REQ_SYSTEM_MOUNT_DEVICE
 Check if mounting a device is allowed. arg1 is a
 vnode_t * of the device, arg2 is a struct mount * with
 the mount-point, and arg3 is a mode_t with the desired
 access mode.
 KAUTH_REQ_SYSTEM_MOUNT_GET
 Check if retrieving information about a mount is
 allowed. arg1 is a struct mount * with the mount
 structure in question, arg2 is a void * with file sys-
 tem specific data, if any.
 KAUTH_REQ_SYSTEM_MOUNT_NEW
 Check if mounting a new file system is allowed.
 arg1 is the struct vnode * on which the file system is
 to be mounted, arg2 is an int with the mount flags, and
 arg3 is a void * with file system specific data, if
 any.
 KAUTH_REQ_SYSTEM_MOUNT_UNMOUNT
 Checks if unmounting a file system is allowed.
 arg1 is a struct mount * with the mount in question.
 KAUTH_REQ_SYSTEM_MOUNT_UPDATE
 Checks if updating an existing mount is allowed.
 arg1 is the struct mount * of the existing mount, arg2 
 is an int with the new mount flags, and arg3 is a void 
 * with file system specific data, if any.
 KAUTH_REQ_SYSTEM_MOUNT_UMAP
 Check if mounting the user and group id remapping file
 system. See mount_umap(8) .
 KAUTH_SYSTEM_MQUEUE
 Check if bypassing permissions on a message queue object are
 allowed. arg1 is a mqueue_t * describing the message queue.
 KAUTH_SYSTEM_PSET
 Check processor-set manipulation.
 req can be any of the following:
 KAUTH_REQ_SYSTEM_PSET_ASSIGN
 Change processor-set processor assignment.
 KAUTH_REQ_SYSTEM_PSET_BIND
 Bind an LWP to a processor-set.
 KAUTH_REQ_SYSTEM_PSET_CREATE
 Create a processor-set.
 KAUTH_REQ_SYSTEM_PSET_DESTROY
 Destroy a processor-set.
 KAUTH_SYSTEM_REBOOT
 Check if rebooting is allowed.
 KAUTH_SYSTEM_SETIDCORE
 Check if changing coredump settings for set-id processes is
 allowed.
 KAUTH_SYSTEM_SEMAPHORE
 Check if access to a kernel semaphore is allowed. arg1 is a
 ksem_t * describing the semaphore.
 KAUTH_SYSTEM_SWAPCTL
 Check if privileged swapctl(2) requests are allowed.
 KAUTH_SYSTEM_SYSCTL
 This requests operations related to sysctl(9) . req indicates
 the specific request and can be one of the following:
 KAUTH_REQ_SYSTEM_SYSCTL_ADD
 Check if adding a sysctl(9) node is allowed.
 KAUTH_REQ_SYSTEM_SYSCTL_DELETE
 Check if deleting a sysctl(9) node is allowed.
 KAUTH_REQ_SYSTEM_SYSCTL_DESC
 Check if adding description to a sysctl(9) node is
 allowed.
 KAUTH_REQ_SYSTEM_SYSCTL_MODIFY
 Check if modifying a sysctl(9) node variable that
 doesn't have a custom sysctl helper function is
 allowed.
 This request might be deprecated in the future.
 KAUTH_REQ_SYSTEM_SYSCTL_PRVT
 Check if accessing private sysctl(9) nodes is allowed.
 KAUTH_SYSTEM_SYSVIPC
 Check SysV IPC related operations. req indicates the specific
 request and can be one of the following:
 KAUTH_REQ_SYSTEM_SYSVIPC_BYPASS
 Check if bypassing a SysV IPC object's permissions is
 allowed. arg1 is a struct ipc_perm * with the object's
 permissions and arg2 is a mode_t indicating the
 requested access mode.
 KAUTH_REQ_SYSTEM_SYSVIPC_SHM_LOCK
 Check if shared memory locking is allowed.
 KAUTH_REQ_SYSTEM_SYSVIPC_SHM_UNLOCK
 Check if shared memory unlocking is allowed.
 KAUTH_REQ_SYSTEM_SYSVIPC_MSGQ_OVERSIZE
 Check if oversizing a message queue is allowed. arg1 
 is a msglen_t indicating the size of the message
 buffer, and arg2 is a msglen_t indicating the size of
 the message queue.
 KAUTH_SYSTEM_TIME
 This request groups time-related operations. req can be any of
 the following:
 KAUTH_REQ_SYSTEM_TIME_ADJTIME
 Check if changing the time using adjtime(2) is allowed.
 KAUTH_REQ_SYSTEM_TIME_NTPADJTIME
 Check if setting the time using ntp_adjtime(2) is
 allowed.
 KAUTH_REQ_SYSTEM_TIME_SYSTEM
 Check if changing the time (usually via
 settimeofday(2) ) is allowed.
 arg1 is a struct timespec * with the new time, arg2 is
 a struct timeval * with the delta from the current
 time, arg3 is a bool indicating whether the caller is a
 device context (e.g. /dev/clockctl ) or not.
 KAUTH_REQ_SYSTEM_TIME_RTCOFFSET
 Check if changing the RTC offset is allowed.
 KAUTH_REQ_SYSTEM_TIME_TIMECOUNTERS
 Check if manipulating timecounters is allowed.
 KAUTH_SYSTEM_VERIEXEC
 Check if operations on the veriexec(8) subsystem are allowed.
 req can be one of the following:
 KAUTH_REQ_SYSTEM_VERIEXEC_ACCESS
 Check if access to the veriexec(8) subsystem is
 allowed.
 KAUTH_REQ_SYSTEM_VERIEXEC_MODIFY
 Check if modifications to the state of veriexec(8) are
 allowed.
 Process Scope 
 The process scope, ``org.netbsd.kauth.process'', manages authorization
 requests related to processes in the system.
 The authorization wrapper for this scope is declared as
 int kauth_authorize_process ( kauth_cred_t cred , kauth_action_t op , struct 
 proc *p , void *arg1 , void *arg2 , void *arg3 )
 The following operations are available for this scope:
 KAUTH_PROCESS_KTRACE
 Checks whether an object with one set of credentials can
 ktrace(1) another process p , possibly with a different set of
 credentials.
 If arg1 is KAUTH_REQ_PROCESS_KTRACE_PERSISTENT, this checks if
 persistent tracing can be done. Persistent tracing maintains
 the trace across a set-user-id/set-group-id exec(3) , and nor-
 mally requires privileged credentials.
 KAUTH_PROCESS_PROCFS
 Checks whether object with passed credentials can use procfs to
 access process p .
 arg1 is the struct pfsnode * for the target element in the tar-
 get process, and arg2 is the access type, which can be either
 KAUTH_REQ_PROCESS_PROCFS_READ, KAUTH_REQ_PROCESS_PROCFS_RW, or
 KAUTH_REQ_PROCESS_PROCFS_WRITE, indicating control , read ,
 read-write , or write access respectively.
 KAUTH_PROCESS_PTRACE
 Checks whether object with passed credentials can use ptrace(2) 
 to access process p .
 arg1 is the ptrace(2) command.
 KAUTH_PROCESS_CANSEE
 Checks whether an object with one set of credentials can access
 information about another process, possibly with a different set
 of credentials.
 arg1 indicates the class of information being viewed, and can be
 either of KAUTH_REQ_PROCESS_CANSEE_ARGS,
 KAUTH_REQ_PROCESS_CANSEE_ENTRY, KAUTH_REQ_PROCESS_CANSEE_ENV, or
 KAUTH_REQ_PROCESS_CANSEE_OPENFILES.
 KAUTH_PROCESS_SCHEDULER_GETAFFINITY
 Checks whether viewing the scheduler affinity is allowed.
 KAUTH_PROCESS_SCHEDULER_SETAFFINITY
 Checks whether setting the scheduler affinity is allowed.
 KAUTH_PROCESS_SCHEDULER_GETPARAM
 Checks whether viewing the scheduler policy and parameters is
 allowed.
 KAUTH_PROCESS_SCHEDULER_SETPARAM
 Checks whether modifying the scheduler policy and parameters is
 allowed.
 KAUTH_PROCESS_SIGNAL
 Checks whether an object with one set of credentials can post
 signals to another process.
 p is the process the signal is being posted to, and arg1 is the
 signal number.
 KAUTH_PROCESS_CORENAME
 Controls access to process corename.
 arg1 can be KAUTH_REQ_PROCESS_CORENAME_GET or
 KAUTH_REQ_PROCESS_CORENAME_SET, indicating access to read or
 write the process' corename, respectively.
 When modifying the corename, arg2 holds the new corename to be
 used.
 KAUTH_PROCESS_FORK
 Checks if the process can fork. arg1 is an int indicating how
 many processes exist on the system at the time of the check.
 KAUTH_PROCESS_KEVENT_FILTER
 Checks whether setting a process kevent(2) filter is allowed.
 KAUTH_PROCESS_NICE
 Checks whether the nice value of p can be changed to arg1 .
 KAUTH_PROCESS_RLIMIT
 Controls access to process resource limits.
 arg1 can be KAUTH_REQ_PROCESS_RLIMIT_GET or
 KAUTH_REQ_PROCESS_RLIMIT_SET, indicating access to read or write
 the process' resource limits, respectively, or
 KAUTH_REQ_PROCESS_RLIMIT_BYPASS to check if the limit enforce-
 ment can be bypassed.
 When modifying resource limits, arg2 is the new value to be used
 and arg3 indicates which resource limit is to be modified.
 KAUTH_PROCESS_SETID
 Check if changing the user- or group-ids, groups, or login-name
 for p is allowed.
 KAUTH_PROCESS_STOPFLAG
 Check if setting the stop flags for exec(3) , exit(3) , and
 fork(2) is allowed.
 arg1 indicates the flag, and can be either P_STOPEXEC,
 P_STOPEXIT, or P_STOPFORK respectively.
 Network Scope 
 The network scope, ``org.netbsd.kauth.network'', manages networking-
 related authorization requests in the kernel.
 The authorization wrapper for this scope is declared as
 int kauth_authorize_network ( kauth_cred_t cred , kauth_action_t op , enum 
 kauth_network_req req , void *arg1 , void *arg2 , void *arg3 )
 The following operations are available for this scope:
 KAUTH_NETWORK_ALTQ
 Checks if an ALTQ operation is allowed.
 req indicates the ALTQ subsystem in question, and can be one of
 the following:
 KAUTH_REQ_NETWORK_ALTQ_AFMAP
 KAUTH_REQ_NETWORK_ALTQ_BLUE
 KAUTH_REQ_NETWORK_ALTQ_CBQ
 KAUTH_REQ_NETWORK_ALTQ_CDNR
 KAUTH_REQ_NETWORK_ALTQ_CONF
 KAUTH_REQ_NETWORK_ALTQ_FIFOQ
 KAUTH_REQ_NETWORK_ALTQ_HFSC
 KAUTH_REQ_NETWORK_ALTQ_JOBS
 KAUTH_REQ_NETWORK_ALTQ_PRIQ
 KAUTH_REQ_NETWORK_ALTQ_RED
 KAUTH_REQ_NETWORK_ALTQ_RIO
 KAUTH_REQ_NETWORK_ALTQ_WFQ
 KAUTH_NETWORK_BIND
 Checks if a bind(2) request is allowed.
 req allows to indicate the type of the request to structure lis-
 teners and callers easier. Supported request types:
 KAUTH_REQ_NETWORK_BIND_PORT
 Checks if binding to a non-privileged/reserved port is
 allowed.
 KAUTH_REQ_NETWORK_BIND_PRIVPORT
 Checks if binding to a privileged/reserved port is
 allowed.
 KAUTH_NETWORK_FIREWALL
 Checks if firewall-related operations are allowed.
 req indicates the sub-action, and can be one of the following:
 KAUTH_REQ_NETWORK_FIREWALL_FW
 Modification of packet filtering rules.
 KAUTH_REQ_NETWORK_FIREWALL_NAT
 Modification of NAT rules.
 KAUTH_NETWORK_INTERFACE
 Checks if network interface-related operations are allowed.
 arg1 is (optionally) the struct ifnet * associated with the
 interface. arg2 is (optionally) an int describing the inter-
 face-specific operation. arg3 is (optionally) a pointer to the
 interface-specific request structure. req indicates the sub-
 action, and can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_GET
 Check if retrieving information from the device is
 allowed.
 KAUTH_REQ_NETWORK_INTERFACE_GETPRIV
 Check if retrieving privileged information from the
 device is allowed.
 KAUTH_REQ_NETWORK_INTERFACE_SET
 Check if setting parameters on the device is allowed.
 KAUTH_REQ_NETWORK_INTERFACE_SETPRIV
 Check if setting privileged parameters on the device is
 allowed.
 KAUTH_REQ_NETWORK_INTERFACE_FIRMWARE
 Check if manipulating the firmware on a network inter-
 face device is allowed.
 Note that unless the struct ifnet * for the interface was passed
 in arg1 , there's no way to tell what structure arg3 is.
 KAUTH_NETWORK_INTERFACE_BRIDGE
 Check if operations performed on the bridge(4) network interface
 are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_BRIDGE_GETPRIV
 Check if getting privileges parameters is allowed.
 KAUTH_REQ_NETWORK_INTERFACE_BRIDGE_SETPRIV
 Check if setting privileges parameters is allowed.
 KAUTH_NETWORK_INTERFACE_PPP
 Checks if operations performed on the ppp(4) network interface
 are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_PPP_ADD
 Checks if adding and enabling a ppp(4) interface to the
 system is allowed.
 KAUTH_NETWORK_INTERFACE_PVC
 Check if operations performed on a PVC device (e.g. en(4) ) are
 allowed. req can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_PVC_ADD
 Check if adding a PVC device is allowed.
 KAUTH_NETWORK_INTERFACE_SLIP
 Checks if operations performed on the sl(4) network interface
 are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_SLIP_ADD
 Checks if adding and enabling a sl(4) interface to the
 system is allowed.
 KAUTH_NETWORK_INTERFACE_STRIP
 Checks if operations performed on the strip(4) network interface
 are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_STRIP_ADD
 Check if adding and enabling a strip(4) interface to
 the system is allowed.
 KAUTH_NETWORK_INTERFACE_TUN
 Checks if operations performed on the tun(4) network interface
 are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_INTERFACE_TUN_ADD
 Checks if adding and enabling a tun(4) interface to the
 system is allowed.
 KAUTH_NETWORK_IPSEC
 Check if operations related to ipsec(4) connections are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_IPSEC_BYPASS
 Check if bypassing ipsec(4) policy is allowed.
 KAUTH_NETWORK_IPV6
 Check if IPv6-specific operations are allowed. req can be one
 of the following:
 KAUTH_REQ_NETWORK_IPV6_HOPBYHOP
 Check if setting hop-by-hop packet options is allowed.
 KAUTH_REQ_NETWORK_IPV6_JOIN_MULTICAST
 Check if joining a multicast network is allowed.
 KAUTH_NETWORK_FORWSRCRT
 Checks whether status of forwarding of source-routed packets can
 be modified or not.
 KAUTH_NETWORK_NFS
 Check if an NFS related operation is allowed.
 req can be any of the following:
 KAUTH_REQ_NETWORK_NFS_EXPORT
 Check if modifying the NFS export table is allowed.
 KAUTH_REQ_NETWORK_NFS_SVC
 Check if access to the NFS nfssvc(2) syscall is
 allowed.
 KAUTH_NETWORK_ROUTE
 Checks if a routing-related request is allowed.
 arg1 is the struct rt_msghdr * for the request.
 KAUTH_NETWORK_SMB
 Check if operations related to SMB are allowed.
 req can be one of the following:
 KAUTH_REQ_NETWORK_SMB_SHARE_ACCESS
 Check if accessing an SMB share is allowed.
 arg1 is a struct smb_share * describing the SMB share,
 and arg2 is a mode_t with the desired access mode.
 KAUTH_REQ_NETWORK_SMB_SHARE_CREATE
 Check if creating an SMB share is allowed.
 arg1 is a struct smb_sharespec * describing the share
 to be created.
 KAUTH_REQ_NETWORK_SMB_VC_ACCESS
 Check if accessing an SMB VC is allowed.
 arg1 is a struct smb_vc * describing the SMB VC, and
 arg2 is a mode_t with the desired access mode.
 KAUTH_REQ_NETWORK_SMB_VC_CREATE
 Check if creating an SMB VC is allowed.
 arg1 is a struct smb_vcspec * describing the VC to be
 created.
 KAUTH_NETWORK_SOCKET
 Checks if a socket related operation is allowed.
 req allows to indicate the type of the request to structure lis-
 teners and callers easier. Supported request types:
 KAUTH_REQ_NETWORK_SOCKET_RAWSOCK
 Checks if opening a raw socket is allowed.
 KAUTH_REQ_NETWORK_SOCKET_OPEN
 Checks if opening a socket is allowed. arg1 , arg2 , and
 arg3 are all int parameters describing the domain,
 socket type, and protocol, respectively.
 KAUTH_REQ_NETWORK_SOCKET_CANSEE
 Checks if looking at the socket passed is allowed.
 arg1 is a struct socket * describing the socket.
 KAUTH_REQ_NETWORK_SOCKET_DROP
 Checks if a connection can be dropped.
 arg1 is a struct socket * describing the socket.
 KAUTH_REQ_NETWORK_SOCKET_SETPRIV
 Checks if setting privileged socket options is allowed.
 arg1 is a struct socket * describing the socket, arg2 
 is a u_long describing the socket option.
 Machine-dependent Scope 
 The machine-dependent (machdep) scope, ``org.netbsd.kauth.machdep'', man-
 ages machine-dependent authorization requests in the kernel.
 The authorization wrapper for this scope is declared as
 int kauth_authorize_machdep ( kauth_cred_t cred , kauth_action_t op , void 
 *arg0 , void *arg1 , void *arg2 , void *arg3 )
 The actions on this scope provide a set that may or may not affect all
 platforms. Below is a list of available actions, along with which plat-
 forms are affected by each.
 KAUTH_MACHDEP_CACHEFLUSH
 Request to flush the whole CPU cache. Affects m68k Linux emula-
 tion.
 KAUTH_MACHDEP_CPU_UCODE_APPLY
 Request to apply a CPU microcode to a CPU. This is related to
 CPU_UCODE , see options(4) . Affects i386 and xen .
 KAUTH_MACHDEP_IOPERM_GET
 Request to get the I/O permission level. Affects amd64 , i386 ,
 xen .
 KAUTH_MACHDEP_IOPERM_SET
 Request to set the I/O permission level. Affects amd64 , i386 ,
 xen .
 KAUTH_MACHDEP_IOPL
 Request to set the I/O privilege level. Affects amd64 , i386 ,
 xen .
 KAUTH_MACHDEP_LDT_GET
 Request to get the LDT (local descriptor table). Affects amd64 ,
 i386 , xen .
 KAUTH_MACHDEP_LDT_SET
 Request to set the LDT (local descriptor table). Affects amd64 ,
 i386 , xen .
 KAUTH_MACHDEP_MTRR_GET
 Request to get the MTRR (memory type range registers). Affects
 amd64 , i386 , xen .
 KAUTH_MACHDEP_MTRR_SET
 Request to set the MTRR (memory type range registers). Affects
 amd64 , i386 , xen .
 KAUTH_MACHDEP_NVRAM
 Request to access (read/write) the NVRAM. Affects i386 .
 KAUTH_MACHDEP_PXG
 Request to start or stop the pxg(4) CPU. arg0 is true or false ,
 respectively. Affects pmax .
 KAUTH_MACHDEP_UNMANAGEDMEM
 Request to access unmanaged memory. Affects alpha , amd64 , arm ,
 i386 , powerpc , sh3 , vax , x68k , xen .
 Device Scope 
 The device scope, ``org.netbsd.kauth.device'', manages authorization
 requests related to devices on the system. Devices can be, for example,
 terminals, tape drives, Bluetooth accessories, and any other hardware.
 Network devices specifically are handled by the network scope.
 In addition to the standard authorization wrapper:
 int kauth_authorize_device ( kauth_cred_t cred , kauth_action_t op , void 
 *arg0 , void *arg1 , void *arg2 , void *arg3 )
 this scope provides authorization wrappers for various device types.
 int kauth_authorize_device_tty ( kauth_cred_t cred , kauth_action_t op ,
 struct tty *tty )
 Authorizes requests for terminal devices on the system. The third argu-
 ment, tty , is the terminal device in question. It is passed to the lis-
 tener as arg0 . The second argument, op , is the action and can be one of
 the following:
 KAUTH_DEVICE_TTY_OPEN
 Open the terminal device pointed to by tty .
 KAUTH_DEVICE_TTY_PRIVSET
 Set privileged settings on the terminal device pointed to by
 tty .
 KAUTH_DEVICE_TTY_STI
 Use the ``TIOCSTI'' device ioctl(2) , allowing to inject charac-
 ters into the terminal buffer, simulating terminal input.
 KAUTH_DEVICE_TTY_VIRTUAL
 Control the virtual console. tty is the current console tty(4) .
 int kauth_authorize_device_spec ( kauth_cred_t cred , enum kauth_device_req 
 req , struct vnode *vp )
 Authorizes requests for special files , usually disk devices, but also
 direct memory access, on the system.
 It passes KAUTH_DEVICE_RAWIO_SPEC as the action to the listener, and
 accepts two arguments. req , passed to the listener as arg0 , is access
 requested, and can be one of KAUTH_REQ_DEVICE_RAWIO_SPEC_READ,
 KAUTH_REQ_DEVICE_RAWIO_SPEC_WRITE, or KAUTH_REQ_DEVICE_RAWIO_SPEC_RW,
 representing read, write, or both read/write access respectively. vp is
 the vnode of the special file in question, and is passed to the listener
 as arg1 .
 Keep in mind that it is the responsibility of the security model devel-
 oper to check whether the underlying device is a disk or the system mem-
 ory, using iskmemdev ():
 if ((vp->v_type == VCHR) &&
 iskmemdev(vp->v_un.vu_specinfo->si_rdev))
 /* system memory access */
 int kauth_authorize_device_passthru ( kauth_cred_t cred , dev_t dev , u_long 
 mode , void *data )
 Authorizes hardware passthru requests, or user commands passed directly
 to the hardware. These have the potential of resulting in direct disk
 and/or memory access.
 It passes KAUTH_DEVICE_RAWIO_PASSTHRU as the action to the listener, and
 accepts three arguments. dev , passed as arg1 to the listener, is the
 device for which the request is made. mode , passed as arg0 to the lis-
 tener, is a generic representation of the access mode requested. It can
 be one or more (binary-OR'd) of the following:
 KAUTH_REQ_DEVICE_RAWIO_PASSTHRU_READ
 KAUTH_REQ_DEVICE_RAWIO_PASSTHRU_READCONF
 KAUTH_REQ_DEVICE_RAWIO_PASSTHRU_WRITE
 KAUTH_REQ_DEVICE_RAWIO_PASSTHRU_WRITECONF
 data , passed as arg2 to the listener, is device-specific data that may be
 associated with the request.
 Bluetooth Devices 
 Authorizing actions relevant to Bluetooth devices is done using the stan-
 dard authorization wrapper, with the following actions:
 KAUTH_DEVICE_BLUETOOTH_BCSP
 Check if operations on a bcsp(4) device are allowed.
 arg0 is an enum kauth_device_req with one of the following val-
 ues:
 KAUTH_REQ_DEVICE_BLUETOOTH_BCSP_ADD
 Check if adding and enabling a bcsp(4) device is
 allowed.
 KAUTH_DEVICE_BLUETOOTH_BTUART
 Check if operations on a btuart(4) device are allowed.
 arg0 is an enum kauth_device_req with one of the following val-
 ues:
 KAUTH_REQ_DEVICE_BLUETOOTH_BTUART_ADD
 Check if adding and enabling a btuart(4) device is
 allowed.
 KAUTH_DEVICE_BLUETOOTH_RECV
 Check if a packet can be received from the device.
 arg0 is the packet type. For HCI_CMD_PKT packets, arg1 is the
 opcode, for HCI_EVENT_PKT packets, arg1 is the event ID, and for
 HCI_ACLDATA_PKT or HCI_SCODATA_PKT packets, arg1 is the connec-
 tion handle.
 KAUTH_DEVICE_BLUETOOTH_SEND
 Check if a packet can be sent to the device.
 arg0 is a struct hci_unit * describing the HCI unit, arg1 is a
 hci_cmd_hdr_t * describing the packet header.
 KAUTH_DEVICE_BLUETOOTH_SETPRIV
 Check if privileged settings can be changed.
 arg0 is a struct hci_unit * describing the HCI unit, arg1 is a
 struct btreq * describing the request, and arg2 is a u_long 
 describing the command.
 Kernel random device 
 Authorization actions relevant to the kernel random device, rnd(4) , is
 done using the standard authorization wrapper, with the following
 actions:
 KAUTH_DEVICE_RND_ADDDATA
 Check if adding data to the entropy pool is allowed.
 KAUTH_DEVICE_RND_GETPRIV
 Check if privileged settings and information can be retrieved.
 KAUTH_DEVICE_RND_SETPRIV
 Check if privileged settings can be changed.
 Wscons devices 
 Authorization actions relevant to wscons(4) are done using the standard
 authorization wrapper, with the following actions:
 KAUTH_DEVICE_WSCONS_KEYBOARD_BELL
 Check if setting the default bell is allowed.
 KAUTH_DEVICE_WSCONS_KEYBOARD_KEYREPEAT
 Check if setting the default key-repeat is allowed.
 Vnode Scope 
 The vnode scope, ``org.netbsd.kauth.vnode'', authorizes operations made
 on vnodes representing file system objects.
 The authorization wrapper for this scope is declared as
 int kauth_authorize_vnode ( kauth_cred_t cred , kauth_action_t action ,
 vnode_t *vp , vnode_t *dvp , int fs_decision )
 This scope is heavily used in file system code and can potentially affect
 system-wide performance. Therefore, there are several things developers
 should know when using it.
 First, the action parameter is a bit-mask and multiple actions can be
 binary-OR'd and authorized in a single call. Two helper functions help
 generate the action value for a couple of common cases: translating file
 system access to a kauth action and checking access to a vnode.
 The first, kauth_mode_to_action ( mode_t access_mode ), and returns a
 kauth_action_t representing the desired access modes. Another function,
 kauth_access_action ( mode_t access_mode , enum vtype v_type , mode_t 
 file_mode ), returns a kauth_action_t suitable for use in many file system
 access(2) implementations. It calls the aforementioned
 kauth_mode_to_action (), but before returning also adds the
 KAUTH_VNODE_IS_EXEC flag if needed. See below for the meaning of this
 flag and how its necessity is determined.
 Second, it is recommended to be very careful with adding listeners on
 this scope. A special parameter, fs_decision , allows different file sys-
 tems to instrument different policies without adding their own listener.
 This parameter is special because it also serves as a fall-back decision
 when no secmodel(9) is present to prevent a fail-open scenario. It can
 take either an errno(2) value or ``KAUTH_VNODE_REMOTEFS'', indicating
 that the file system on which the authorization is made is remote and
 cannot provide us with a fall-back decision. In this case, kauth can
 only short-circuit the request but the file system will have the last
 word if there is no definitive allow or deny decision.
 The value of fs_decision can be hard-coded or determined by calling an
 internal function implementing a policy. For the latter case, genfs(9) 
 provides a set of helper functions that implement common policies that
 file systems can use. The calling convention is as follows:
 int error;
 error = kauth_authorize_vnode(..., genfs_can_foo(...));
 Actions on the vnode scope are of two types: operations and flags. An
 operation is similar in concept to actions on other scopes in the sense
 that it represents an operation desired by the caller. A flag is an
 indicator of additional information about the vnode that a file system
 can set in order to allow the listener to make a more informed decision.
 Actions include the following:
 KAUTH_VNODE_READ_DATA
 Read file data.
 KAUTH_VNODE_LIST_DIRECTORY
 Read directory listing. Identical to the above.
 KAUTH_VNODE_WRITE_DATA
 Write file data.
 KAUTH_VNODE_ADD_FILE
 Add a file to a directory. Identical to the above.
 KAUTH_VNODE_EXECUTE
 Execute a file.
 KAUTH_VNODE_SEARCH
 Search (enter) a directory. Identical to the above.
 KAUTH_VNODE_DELETE
 Delete a file.
 KAUTH_VNODE_APPEND_DATA
 Append data to a file.
 KAUTH_VNODE_ADD_SUBDIRECTORY
 Add a subdirectory to a directory. Identical to the
 above.
 KAUTH_VNODE_READ_TIMES
 Read the created, last accessed, and last modified times
 of a file.
 KAUTH_VNODE_WRITE_TIMES
 Modify the created, last accessed, or last modified times
 of a file.
 KAUTH_VNODE_READ_FLAGS
 Read file flags.
 KAUTH_VNODE_WRITE_FLAGS
 Modify file flags.
 KAUTH_VNODE_READ_SYSFLAGS
 Read file system flags.
 KAUTH_VNODE_WRITE_SYSFLAGS
 Modify file system flags.
 KAUTH_VNODE_RENAME
 Rename a file.
 KAUTH_VNODE_CHANGE_OWNERSHIP
 Change ownership of a file.
 KAUTH_VNODE_READ_SECURITY
 Read the permissions of a file.
 KAUTH_VNODE_WRITE_SECURITY
 Change the permissions of a file, for example by using
 chmod(2) .
 KAUTH_VNODE_READ_ATTRIBUTES
 Read attributes of a file.
 KAUTH_VNODE_WRITE_ATTRIBUTES
 Modify attributes of a file.
 KAUTH_VNODE_READ_EXTATTRIBUTES
 Read extended attributes of a file.
 KAUTH_VNODE_WRITE_EXTATTRIBUTES
 Modify extended attributes of a file.
 KAUTH_VNODE_RETAIN_SUID
 Check if retaining the set-user-id bit on files after
 chown(2) is allowed.
 KAUTH_VNODE_RETAIN_SGID
 Check if retaining the set-group-id bit on files after
 chown(2) is allowed.
 KAUTH_VNODE_REVOKE
 Revoke a file.
 Flags include the following:
 KAUTH_VNODE_IS_EXEC
 The vnode is executable.
 The macro FS_OBJECT_CAN_EXEC () can be used to help deter-
 mine if this flag should be set. This macro determines a
 file system object to be executable if it is a directory
 (in which case we say it is searchable) or if it has at
 least one executable bit set in its mode.
 Setting this flag helps a listener know that a vnode is
 executable and is used in implementing privileged access
 to files and directories while maintaining semantics that
 prevent execution until a file is marked as an executable.
 An example for using this in listener code is:
 if (privileged) {
 /* Always allow read/write; execute only if executable. */
 if ((action & KAUTH_VNODE_EXECUTE) == 0 ||
 (action & KAUTH_VNODE_IS_EXEC))
 result = KAUTH_RESULT_ALLOW;
 }
 Finally, the vnode scope authorization wrapper returns
 EACCES in case of an error, to maintain file system seman-
 tics. File systems can override this value if needed.
 KAUTH_VNODE_HAS_SYSFLAGS
 The file system object represented by the vnode has system
 flags set.
 KAUTH_VNODE_ACCESS
 The authorization is advisory only and no actual operation
 is to be performed. This is not implemented.
 Credentials Scope 
 The credentials scope, ``org.netbsd.kauth.cred'', is a special scope used
 internally by the kauth framework to provide hooking to credential-
 related operations.
 It is a ``notify-only'' scope, allowing hooking operations such as ini-
 tialization of new credentials, credential inheritance during a fork, and
 copying and freeing of credentials. The main purpose for this scope is
 to give a security model a way to control the aforementioned operations,
 especially in cases where the credentials hold security model-private
 data.
 Notifications are made using the following function, which is internal to
 kauth :
 int kauth_cred_hook ( kauth_cred_t cred , kauth_action_t action , void *arg0 ,
 void *arg1 )
 With the following actions:
 KAUTH_CRED_COPY
 cred are the credentials that are being copied. arg0 is a
 kauth_cred_t representing the destination credentials. That is
 the credentials are copied from cred to arg0 .
 KAUTH_CRED_FORK
 The credentials are being inherited from a parent to a child
 process during a fork.
 cred are the credentials of the lwp context doing the fork, and
 arg0 and arg1 are both struct proc * of the parent and child
 processes, respectively.
 KAUTH_CRED_CHROOT
 The credentials in cred belong to a process whose root directory
 is changed through change_root () (see vfs(9) ).
 Arg0 is the new struct cwdinfo * of the process.
 KAUTH_CRED_FREE
 The credentials in cred are being freed.
 KAUTH_CRED_INIT
 The credentials in cred are being initialized.
 Since this is a notify-only scope, all listeners are required to return
 KAUTH_RESULT_ALLOW.
 Credentials Accessors and Mutators 
 kauth has a variety of accessor and mutator routines to handle
 kauth_cred_t objects.
 The following routines can be used to access and modify the user- and
 group-ids in a kauth_cred_t :
 uid_t kauth_cred_getuid ( kauth_cred_t cred )
 Returns the real user-id from cred .
 uid_t kauth_cred_geteuid ( kauth_cred_t cred )
 Returns the effective user-id from cred .
 uid_t kauth_cred_getsvuid ( kauth_cred_t cred )
 Returns the saved user-id from cred .
 void kauth_cred_setuid ( kauth_cred_t cred , uid_t uid )
 Sets the real user-id in cred to uid .
 void kauth_cred_seteuid ( kauth_cred_t cred , uid_t uid )
 Sets the effective user-id in cred to uid .
 void kauth_cred_setsvuid ( kauth_cred_t cred , uid_t uid )
 Sets the saved user-id in cred to uid .
 gid_t kauth_cred_getgid ( kauth_cred_t cred )
 Returns the real group-id from cred .
 gid_t kauth_cred_getegid ( kauth_cred_t cred )
 Returns the effective group-id from cred .
 gid_t kauth_cred_getsvgid ( kauth_cred_t cred )
 Returns the saved group-id from cred .
 void kauth_cred_setgid ( kauth_cred_t cred , gid_t gid )
 Sets the real group-id in cred to gid .
 void kauth_cred_setegid ( kauth_cred_t cred , gid_t gid )
 Sets the effective group-id in cred to gid .
 void kauth_cred_setsvgid ( kauth_cred_t cred , gid_t gid )
 Sets the saved group-id in cred to gid .
 u_int kauth_cred_getrefcnt ( kauth_cred_t cred )
 Return the reference count for cred .
 The following routines can be used to access and modify the group list in
 a kauth_cred_t :
 int kauth_cred_ismember_gid ( kauth_cred_t cred , gid_t gid , int *resultp )
 Checks if the group-id gid is a member in the group list of
 cred .
 If it is, resultp will be set to one, otherwise, to zero.
 The return value is an error code, or zero for success.
 u_int kauth_cred_ngroups ( kauth_cred_t cred )
 Return the number of groups in the group list of cred .
 gid_t kauth_cred_group ( kauth_cred_t cred , u_int idx )
 Return the group-id of the group at index idx in the group list
 of cred .
 int kauth_cred_setgroups ( kauth_cred_t cred , const gid_t *groups , size_t 
 ngroups , uid_t gmuid , enum uio_seg seg )
 Copy ngroups groups from array pointed to by groups to the group
 list in cred , adjusting the number of groups in cred appropri-
 ately. seg should be either UIO_USERSPACE or UIO_SYSSPACE indi-
 cating whether groups is a user or kernel space address.
 Any groups remaining will be set to an invalid value.
 gmuid is unused for now, and to maintain interface compatibility
 with the Darwin KPI.
 The return value is an error code, or zero for success.
 int kauth_cred_getgroups ( kauth_cred_t cred , gid_t *groups , size_t 
 ngroups , enum uio_seg seg )
 Copy ngroups groups from the group list in cred to the buffer
 pointed to by groups . seg should be either UIO_USERSPACE or
 UIO_SYSSPACE indicating whether groups is a user or kernel space
 address.
 The return value is an error code, or zero for success.
 Credential Private Data 
 kauth provides an interface to allow attaching security-model private
 data to credentials.
 The use of this interface has two parts that can be divided to direct and
 indirect control of the private-data. Directly controlling the private
 data is done by using the below routines, while the indirect control is
 often dictated by events such as process fork, and is handled by listen-
 ing on the credentials scope (see above).
 Attaching private data to credentials works by registering a key to serve
 as a unique identifier, distinguishing various sets of private data that
 may be associated with the credentials. Registering, and deregistering,
 a key is done by using these routines:
 int kauth_register_key ( secmodel_t sm , kauth_key_t *keyp )
 Register new key for private data for security model sm . keyp 
 will be used to return the key to be used in further calls.
 The function returns 0 on success and an error code (see
 errno(2) ) on failure.
 int kauth_deregister_key ( kauth_key_t key )
 Deregister private data key key .
 Once registered, private data may be manipulated by the following rou-
 tines:
 void kauth_cred_setdata ( kauth_cred_t cred , kauth_key_t key , void *data )
 Set private data for key in cred to be data .
 void * kauth_cred_getdata ( kauth_cred_t cred , kauth_key_t key )
 Retrieve private data for key in cred .
 Note that it is required to use the above routines every time the private
 data is changed, i.e., using kauth_cred_getdata () and later modifying the
 private data should be accompanied by a call to kauth_cred_setdata () with
 the ``new'' private data.
 Credential Inheritance and Reference Counting 
 kauth provides an interface for handling shared credentials.
 When a kauth_cred_t is first allocated, its reference count is set to 1.
 However, with time, its reference count can grow as more objects (pro-
 cesses, LWPs, files, etc.) reference it.
 The following routines are available for managing credentials reference
 counting:
 kauth_cred_t kauth_cred_hold ( kauth_cred_t cred )
 Increases reference count to cred by one and returns cred verba-
 tim.
 void kauth_cred_free ( kauth_cred_t cred )
 Decreases the reference count to cred by one.
 If the reference count dropped to zero, the memory used by cred 
 will be freed.
 Credential inheritance happens during a fork(2) , and is handled by the
 following function:
 void kauth_proc_fork ( struct proc *parent , struct proc *child )
 When called, it references the parent's credentials from the child, and
 calls the credentials scope's hook with the KAUTH_CRED_FORK action to
 allow security model-specific handling of the inheritance to take place.
 Credentials Memory Management 
 Data-structures for credentials, listeners, and scopes are allocated from
 memory pools managed by the pool(9) subsystem.
 The kauth_cred_t objects have their own memory management routines:
 kauth_cred_t kauth_cred_alloc ( void )
 Allocates a new kauth_cred_t , initializes its lock, and sets its
 reference count to one.
 Conversion Routines 
 Sometimes it might be necessary to convert a kauth_cred_t to userland's
 view of credentials, a struct uucred , or vice versa.
 The following routines are available for these cases:
 void kauth_uucred_to_cred ( kauth_cred_t cred , const struct uucred *uucred )
 Convert userland's view of credentials to a kauth_cred_t .
 This includes effective user- and group-ids, a number of groups,
 and a group list. The reference count is set to one.
 Note that kauth will try to copy as many groups as can be held
 inside a kauth_cred_t .
 void kauth_cred_to_uucred ( struct uucred *uucred , const kauth_cred_t cred )
 Convert kauth_cred_t to userland's view of credentials.
 This includes effective user- and group-ids, a number of groups,
 and a group list.
 Note that kauth will try to copy as many groups as can be held
 inside a struct uucred .
 int kauth_cred_uucmp ( kauth_cred_t cred , struct uucred *uucred )
 Compares cred with the userland credentials in uucred .
 Common values that will be compared are effective user- and
 group-ids, and the group list.
 Miscellaneous Routines 
 Other routines provided by kauth are:
 void kauth_cred_clone ( kauth_cred_t cred1 , kauth_cred_t cred2 )
 Clone credentials from cred1 to cred2 , except for the lock and
 reference count.
 kauth_cred_t kauth_cred_dup ( kauth_cred_t cred )
 Duplicate cred .
 What this routine does is call kauth_cred_alloc () followed by a
 call to kauth_cred_clone ().
 kauth_cred_t kauth_cred_copy ( kauth_cred_t cred )
 Works like kauth_cred_dup (), except for a few differences.
 If cred already has a reference count of one, it will be
 returned. Otherwise, a new kauth_cred_t will be allocated and
 the credentials from cred will be cloned to it. Last, a call to
 kauth_cred_free () for cred will be done.
 kauth_cred_t kauth_cred_get ( void )
 Return the credentials associated with the current LWP. This
 does not change the reference count of the resulting
 kauth_cred_t object.
 Scope Management 
 kauth provides routines to manage the creation and deletion of scopes on
 the system.
 Note that the built-in scopes, the ``generic'' scope and the ``process''
 scope, can't be deleted.
 kauth_scope_t kauth_register_scope ( const char *id , kauth_scope_callback_t 
 cb , void *cookie )
 Register a new scope on the system. id is the name of the
 scope, usually in reverse DNS-like notation. For example,
 ``org.netbsd.kauth.myscope''. cb is the default listener, to
 which authorization requests for this scope will be dispatched
 to. cookie is optional user-data that will be passed to all
 listeners during authorization on the scope.
 void kauth_deregister_scope ( kauth_scope_t scope )
 Deregister scope from the scopes available on the system, and
 free the kauth_scope_t object scope .
 Listener Management 
 Listeners in kauth are authorization callbacks that are called during an
 authorization request in the scope which they belong to.
 When an authorization request is made, all listeners associated with a
 scope are called to allow, deny, or defer the request.
 It is enough for one listener to deny the request in order for the
 request to be denied; but all listeners are called during an authoriza-
 tion process none-the-less. All listeners are required to allow the
 request for it to be granted, and in a case where all listeners defer the
 request -- leaving the decision for other listeners -- the request is
 denied.
 The following KPI is provided for the management of listeners:
 kauth_listener_t kauth_listen_scope ( const char *id ,
 kauth_scope_callback_t cb , void *cookie )
 Create a new listener on the scope with the id id , setting the
 default listener to cb . cookie is optional user-data that will
 be passed to the listener when called during an authorization
 request.
 void kauth_unlisten_scope ( kauth_listener_t listener )
 Removes listener from the scope which it belongs to, ensuring it
 won't be called again, and frees the kauth_listener_t object
 listener .
 kauth provides no means for synchronization within listeners. It is the
 programmer's responsibility to make sure data used by the listener is
 properly locked during its use, as it can be accessed simultaneously from
 the same listener called multiple times. It is also the programmer's
 responsibility to do garbage collection after the listener, possibly
 freeing any allocated data it used.
 The common method to do the above is by having a reference count to each
 listener. On entry to the listener, this reference count should be
 raised; on exit, lowered.
 During the removal of a listener, first kauth_scope_unlisten () should be
 called to make sure the listener code will not be entered in the future.
 Then, the code should wait (possibly sleeping) until the reference count
 drops to zero. When that happens, it is safe to do the final cleanup.
 Listeners might sleep, so no locks can be held when calling an authoriza-
 tion wrapper.
 EXAMPLES 
 Older code had no abstraction of the security model, so most privilege
 checks looked like this:
 if (suser(cred, &acflag) == 0)
 /* allow privileged operation */
 Using the new interface, you must ask for a specific privilege explic-
 itly. For example, checking whether it is possible to open a socket
 would look something like this:
 if (kauth_authorize_network(cred, KAUTH_NETWORK_SOCKET,
 KAUTH_REQ_NETWORK_SOCKET_OPEN, PF_INET, SOCK_STREAM,
 IPPROTO_TCP) == 0)
 /* allow opening the socket */
 Note that the securelevel implications were also integrated into the
 kauth framework so you don't have to note anything special in the call to
 the authorization wrapper, but rather just have to make sure the security
 model handles the request as you expect it to.
 To do that you can just grep(1) in the relevant security model directory
 and have a look at the code.
 EXTENDING KAUTH 
 Although kauth provides a large set of both detailed and more or less
 generic requests, it might be needed eventually to introduce more scopes,
 actions, or requests.
 Adding a new scope should happen only when an entire subsystem is intro-
 duced and it is assumed other parts of the kernel may want to interfere
 with its inner-workings. When a subsystem that has the potential of
 impacting the security of the system is introduced, existing security
 modules must be updated to also handle actions on the newly added scope.
 New actions should be added when sets of operations not covered at all
 belong in an already existing scope.
 Requests (or sub-actions) can be added as subsets of existing actions
 when an operation that belongs in an already covered area is introduced.
 Note that all additions should include updates to this manual, the secu-
 rity models shipped with NetBSD, and the example skeleton security model.
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》第 9 章安全机制联网补证（D2 块；官方手册页，collection=NetBSD-current）。
