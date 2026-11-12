<!-- 网页存档｜来源：https://www.dragonflybsd.org/features/｜抓取：2026-11-11T21:40+08:00｜HTML 标签剥离与空白归一 -->

# DragonFly Major Features List

DragonFlyBSD: DragonFly's Major Features List
DragonFly BSD
Edit Page
|
RecentChanges
|
History
|
Preferences
About
History
Features
Performance
Team
Images
Community
Download
Mirrors
Documentation
Mailing Lists
Source
Commercial
Donations
Bugs
Security
PGP Keys
Exports
Hammer
DragonFly's Major Features List
KERNEL
EXTREME SCALING
HAMMER - DragonFly Filesystem
NULLFS - NULL Filesystem Layer
TMPFS - Temporary FileSystem VFS
DM_TARGET_CRYPT, TCPLAY - Transparent disk encryption
SWAPCACHE - Managed SSD support
VARIANT SYMLINKS
PROCESS CHECKPOINTING
DNTPD - DragonFly Network Time Daemon
DMA - DragonFly Mail Agent
KERNEL
Please keep in mind that major modifications have been made to nearly the entire DragonFly kernel with regard to the original FreeBSD-4.8 fork. Significant changes have been made to every kernel subsystem, as a consequence this list is constrained to the largest, most user-visible changes unique to DragonFly.
The scheduler abstraction has been split up into two layers. The LWKT (Light Weight Kernel Thread) scheduler is used by the kernel to schedule all executable entities. The User Thread Scheduler is a separate scheduler which selects one user thread at a time for each CPU and schedules it using the LWKT scheduler. Both scheduler abstractions are per-CPU but the user thread scheduler selects from a common list of runnable processes.
The User Thread Scheduler further abstracts out user threads. A user process contains one or more LWP (Light Weight Process) entities. Each entity represents a user thread under that process. The old
rfork(2)
mechanism still exists but is no longer used. The threading library uses LWP-specific calls.
The kernel memory allocator has two abstracted pieces. The basic kernel malloc is called
kmalloc(9)
and is based on an enhanced per-CPU slab allocator. This allocator is essentially lockless. There is also an object-oriented memory allocator in the kernel called
objcache(9)
which is designed for high volume object allocations and deallocations and is also essentially lockless.
DEVFS - is the DragonFly device filesystem. It works similarly to device filesystems found on other modern UNIX-like operating systems. The biggest single feature is DEVFS's integration with block device serial numbers which allows a DragonFly system to reference disk drives by serial number instead of by their base device name. Thus drives can be trivially migrated between physical ports and driver changes (e.g., base device name changes) become transparent to the system.
VKERNEL - DragonFly implements a virtual kernel feature for running DragonFly kernels in userland inside DragonFly kernels. This works similarly to Usermode Linux and allows DragonFly kernels to be debugged as a userland process. The primary use is to make kernel development easier.
NFS V3 RPC Asynchronization - DragonFly sports a revamped NFSv3 implementation which gets rid of the
nfsiod(8)
threads and implements a fully asynchronous RPC mechanism using only two kernel threads. The new abstraction fixes numerous stalls in the I/O path related to misordered read-ahead requests.
EXTREME SCALING
DragonFly will autotune kernel resources and scaling metrics such as kernel hash-tables based on available memory. The autoscaling has reached a point where essentially all kernel components will scale to extreme levels.
Process and thread components now scale to at least a million user processes or threads, given sufficient physical memory to support that much (around 128GB minimum for one million processes). The PID is currently limited to 6 digits, so discrete user processes are capped at one million, but the (process x thread) matrix can conceivably go much higher. Process creation, basic operation, and destruction have been tested to 900,000 discrete user processes.
File data caching scales indefinitely, based on available memory. A very generous kern.maxvnodes default allows the kernel to scale up to tracking millions of files for caching purposes.
IPI signaling between CPUs has been heavily optimized and will scale nicely up to the maximum hardware thread limit (256 cpu threads, typically in a 128-core/256-thread configuration). Unnecessary IPIs are optimized out, and the signaling of idle cpus can be further optimized via sysctl parameters.
All major kernel resource components are fully SMP-aware and use SMP-friendly algorithms. This means that regular UNIX operations that manipulate PIDs, GIDs, SSIDs, process operations, VM page faults, memory allocation and freeing, pmap updates, VM page sharing, the name cache, most common file operations, process sleep and wakeup, and locks, are all heavily optimized and scale to systems with many cpu cores. In many cases, concurrent functions operate with no locking conflicts or contention.
The network subsystem was rewritten pretty much from the ground-up to fully incorporate packet hashes into the entire stack, allowing connections and network interfaces to operate across available CPUs concurrently with little to no contention. Pipes and Sockets have also been heavily optimized for SMP operation. Given a machine with sufficient capability, hundreds of thousands of concurrent TCP sockets can operate efficiently and packet routing capabilities are very high.
The disk subsystem, particularly AHCI (SATA) and NVMe, are very SMP friendly. NVMe, in particular, will configure enough hardware queues such that it can dispatch requests and handle responses on multiple cpus simultaneously with no contention.
The scheduler uses per-cpu algorithms and scales across any number of cpus. In addition, the scheduler is topology-aware and gains hints from whatever IPC (Inter-Process Communications) occurs to organize active processes within the cpu topology in a way that makes maximum use of cache locality. Load is also taken into account, and can shift how cache locality is handled.
The kernel memory manager is somewhat NUMA aware. Most per-cpu operations use NUMA-local memory allocations. User memory requests are also NUMA aware, at least for short-lived user programs. Generally speaking, the scheduler will try to keep a process on the same cpu socket but ultimately we've determined that load balancing is sometimes more important. CPU caches generally do a very good job of maximizing IPC (Instructions Per Clock). Because memory management is fully SMP-aware, a multi-core system can literally allocate and free memory at a rate in the multiple gigabytes/sec range.
Generally very high concurrency with very low kernel overhead. The kernel can handle just about any load thrown at it and still be completely responsive to other incidental tasks. Systems can run efficiently at well over 100% load.
Supports up to 4 swap devices for paging and up to 55TB (Terabytes) of configured swapspace. Requires 1MB of physical ram per 1GB of configured swap. When multiple swap devices are present, I/O will be interleaved for maximum effectiveness. The paging system is extremely capable under virtually any load conditions, particularly when swap is assigned to NVMe storage. Concurrent page-in across available cpus, in particular, works extremely well. Asynchronous page-out. Extended filesystem data caching via the swapcache mechanism can operate as an extended (huge) disk cache if desired, and/or used to increase the apparent total system memory.
HAMMER - DragonFly Filesystem
HAMMER
(5) is the DragonFly filesystem, replacing
UFS(5)
. HAMMER supports up to an Exabyte of storage, implements a fast UNDO/REDO FIFO for
fsync(2)
, recovers instantly on boot after a crash (no
fsck(8)
), and implements a very sophisticated fine-grained historical access and snapshot mechanism. HAMMER also supports an extremely robust streaming, queueless master->multiple-slave mirroring capability which is also able to mirror snapshots and other historical data.
All non-temporary HAMMER filesystems in DragonFly by default automatically maintain 60 days worth of 1-day snapshots and 1-day worth of fine-grained (30-second) snapshots. These options can be further tuned to meet one's needs.
HAMMER is also designed to accommodate today's large drives.
NULLFS - NULL Filesystem Layer
A null or loop-back filesystem is common to a number of operating systems. The DragonFly null(5) filesystem is quite a different animal. It supports arbitrary mount points that do not loop, a problem on other operating systems, making it extremely flexible in its application. It is also extremely fast and reliable, something that few other operating systems can claim of their null filesystem layers.
TMPFS - Temporary FileSystem VFS
Originally a NetBSD port the guts have been radically adjusted and carefully tuned to provide a low-contention read path and to directly tie the backing store to the VM/paging system in a way that treats it almost like normal memory. Only memory pressure will force
tmpfs(5)
data pages into swap.
tmpfs(5)
replaces MFS and MD (for post-boot use).
DM_TARGET_CRYPT, TCPLAY - Transparent disk encryption
DragonFly has a device mapper target called
dm_target_crypt(4)
(compatible with Linux's
dm-crypt
) that provides transparent disk encryption. It makes best use of available cryptographic hardware, as well as multi-processor software crypto.
DragonFly fully supports LUKS (
cryptsetup(8)
) and TrueCrypt as disk encryption methods.
tcplay(8)
, is a free (BSD-licensed) 100% compatible TrueCrypt implementation built on
dm_target_crypt(4)
.
SWAPCACHE - Managed SSD support
The
swapcache(8)
feature allows SSD-configured swap to also be used to cache clean filesystem data and meta-data. This feature is carefully managed to maximize the write endurance of the SSD.
swapcache(8)
is typically used to reduce or remove seek overheads related to managing filesystems with a large number of discrete inodes. DragonFly's swap subsystem also supports much larger than normal swap partitions. 64-bit systems support up to 512G of swap by default.
VARIANT SYMLINKS
Variant (context-sensitive) symlinks
varsym(2)
give users, administrators and application authors an extremely useful tool to aid in configuration and management. Special varsym variables can be used within an otherwise conventional symbolic link and resolved at run-time.
PROCESS CHECKPOINTING
Processes under DragonFly may be "checkpointed" or suspended to disk at any time. They may later be resumed on the originating system, or another system by "thawing" them. See
sys_checkpoint(2)
and
checkpt(1)
for more details.
DNTPD - DragonFly Network Time Daemon
DragonFly has its own from-scratch time daemon. After pulling our hair out over the many issues with open source time daemons we decided to write one by ourselves and add new system calls to support it.
dntpd(8)
uses a double staggered linear regression and correlation to make time corrections. It will also properly deal with network failures (including lack of connectivity on boot), duplicate IPs resolved by DNS, and time source failures (typically 1 second off) when multiple time sources are available. The linear regression and correlation allows
dntpd(8)
to make rough adjustments and frequency corrections within 5 minutes of boot and to make more fine-grained adjustments at any time following when the linear regression indicates accuracy beyond the noise floor.
DMA - DragonFly Mail Agent
The DragonFly Mail Agent (
dma(8)
) is a bare-bones (though not so bare-bones any more) mail transfer and mail terminus SMTP server which provides all the functionalities needed for local mail delivery and simple remote mail transfers.
DragonFly BSD
/
DragonFly's Major Features List
Last edited
Fri Jul 23 00:41:47 2021
Sat Jul 10 17:49:09 2010
-->
Site copyright © 2003-2022