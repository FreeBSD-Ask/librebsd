# FreeBSD Handbook, Chapter 23: The Z File System (ZFS) 引用卡

> 用途：V71.2.5.1／2.5.4／2.5.5 内容补证（G8-S2 V71 b004）。

## 一、著录

The FreeBSD Project. FreeBSD Handbook, Chapter 23: The Z File System (ZFS)[EB/OL]. The FreeBSD Project, （日期不详）[2026-11-12]. https://docs.freebsd.org/en/books/handbook/zfs/.

- 责任者：The FreeBSD Project（官方手册）
- 载体：HTML 手册章节；`source_tier=primary`（项目官方文档）
- 访问日：2026-11-12
- 说明：手册随版本滚动更新，无固定出版日；引文照录，HTML 双空格按行合并。

## 二、逐字引文（英文，未翻译）

ZFS 的来源与三个设计目标：

> ZFS is an advanced file system designed to solve major problems found in previous storage subsystem software. Originally developed at Sun Microsystems™, ongoing open source ZFS development has moved to the OpenZFS Project.

数据完整性目标：

> Data integrity: All data includes a checksum of the data. ZFS calculates checksums and writes them along with the data. When reading that data later, ZFS recalculates the checksums. If the checksums do not match, meaning detecting one or more data errors, ZFS will attempt to automatically correct errors when ditto-, mirror-, or parity-blocks are available.

安装器直接装到 ZFS 池：

> The FreeBSD installer can install the system directly onto a ZFS pool, a configuration known as Root-on-ZFS; see Guided Root-on-ZFS.

池化存储与数据集：

> ZFS' combination of the volume manager and the file system solves this and allows the creation of file systems that all share a pool of available storage.

## 三、考据说明

- 手册以专章（第 23 章）系统讲述 ZFS，并把开源开发归属 OpenZFS Project，是 2.5.1“基本系统位次”的官方依据。
- 数据完整性段是 2.5.5 的工程承诺原文：校验和随数据写入、读取时重算、不匹配时在 ditto／镜像／奇偶校验块可用时自动纠正。
- Root-on-ZFS 句与安装手册的 Auto (ZFS) 段互为两文献，支撑 2.5.4。
- 按 L3 采信；官方手册，非独立测评。
