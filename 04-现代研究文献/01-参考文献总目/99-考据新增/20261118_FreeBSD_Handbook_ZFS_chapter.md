<!-- 网页存档｜来源：https://docs.freebsd.org/en/books/handbook/zfs/｜抓取：2026-11-18（exa 通道，直连 docs.freebsd.org 超时）｜HTML 标签剥离与空白归一｜本卡为 Task 8.2 V51—V55 五卷线 V52 b002 引文载体 -->

# Chapter 23. The Z File System (ZFS) | FreeBSD Documentation Portal

（章目录与前导段以下逐字；引文取自本卡以下段落）

ZFS is an advanced file system designed to solve major problems found in previous storage subsystem software.

Originally developed at Sun Microsystems™, ongoing open source ZFS development has moved to the OpenZFS Project.

ZFS has three major design goals:

- Data integrity: All data includes a checksum of the data. ZFS calculates checksums and writes them along with the data. When reading that data later, ZFS recalculates the checksums. If the checksums do not match, meaning detecting one or more data errors, ZFS will attempt to automatically correct errors when ditto-, mirror-, or parity-blocks are available.
- Pooled storage: adding physical storage devices to a pool, and allocating storage space from that shared pool. Space is available to all file systems and volumes, and increases by adding new storage devices to the pool.
- Performance: caching mechanisms provide increased performance. ARC is an advanced memory-based read cache. ZFS provides a second level disk-based read cache with L2ARC, and a disk-based synchronous write cache named ZIL.

A complete list of features and terminology is in ZFS Features and Terminology.

## 23.1. What Makes ZFS Different

More than a file system, ZFS is fundamentally different from traditional file systems. Combining the traditionally separate roles of volume manager and file system provides ZFS with unique advantages. The file system is now aware of the underlying structure of the disks. Traditional file systems could exist on a single disk at a time. If there were two disks then creating two separate file systems was necessary. A traditional hardware RAID configuration avoided this problem by presenting the operating system with a single logical disk made up of the space provided by physical disks on top of which the operating system placed a file system. Even with software RAID solutions like those provided by GEOM, the UFS file system living on top of the RAID believes it is dealing with a single device. ZFS' combination of the volume manager and the file system solves this and allows the creation of file systems that all share a pool of available storage. One big advantage of ZFS' awareness of the physical disk layout is that existing file systems grow automatically when adding extra disks to the pool. This new space then becomes available to the file systems. ZFS can also apply different properties to each file system. This makes it useful to create separate file systems and datasets instead of a single monolithic file system.

（后续小节为操作指南面，与本批引文无关，未录入本卡；页尾 Last modified on: June 20, 2026 by Dave Cottlehuber）
