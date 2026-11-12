# FreeBSD Handbook · Chapter 23 The Z File System (ZFS)（网页抓取件）

- 来源 URL：https://docs.freebsd.org/en/books/handbook/zfs/
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 用途：Task 8.2 G4 · V37.1.7.2“存储池与卷的语义”、V37.1.7.5“ZFS 与 GEOM 的接合处”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

ZFS has three major design goals:

- Data integrity: All data includes a checksum of the data. ZFS calculates checksums and writes them along with the data. When reading that data later, ZFS recalculates the checksums. If the checksums do not match, meaning detecting one or more data errors, ZFS will attempt to automatically correct errors when ditto-, mirror-, or parity-blocks are available.
- Pooled storage: adding physical storage devices to a pool, and allocating storage space from that shared pool. Space is available to all file systems and volumes, and increases by adding new storage devices to the pool.
- Performance: caching mechanisms provide increased performance. ARC is an advanced memory-based read cache. ZFS provides a second level disk-based read cache with L2ARC, and a disk-based synchronous write cache named ZIL.

### 23.1. What Makes ZFS Different

More than a file system, ZFS is fundamentally different from traditional file systems. Combining the traditionally separate roles of volume manager and file system provides ZFS with unique advantages. The file system is now aware of the underlying structure of the disks. Traditional file systems could exist on a single disk at a time. If there were two disks then creating two separate file systems was necessary. A traditional hardware RAID configuration avoided this problem by presenting the operating system with a single logical disk made up of the space provided by physical disks on top of which the operating system placed a file system. Even with software RAID solutions like those provided by GEOM, the UFS file system living on top of the RAID believes it is dealing with a single device. ZFS' combination of the volume manager and the file system solves this and allows the creation of file systems that all share a pool of available storage. One big advantage of ZFS' awareness of the physical disk layout is that existing file systems grow automatically when adding extra disks to the pool. This new space then becomes available to the file systems. ZFS can also apply different properties to each file system. This makes it useful to create separate file systems and datasets instead of a single monolithic file system.

### 23.2.2. RAID-Z（题名与首句）

Disks fail. One way to avoid data loss from disk failure is to use RAID. ZFS supports this feature in its pool design. RAID-Z pools require three or more disks b…（抓取截断于此）

## 说明

节选章首“三大设计目标”与 23.1 全节、23.2.2 首段（截断处为抓取字符上限，未再取）；23.2 其余操作示例、23.3 起术语与属性细节未引。
