# FreeBSD 7.0-RELEASE Release Notes · 2.2.5 File Systems（ZFS 段，网页抓取件）

- 来源 URL：https://www.freebsd.org/releases/7.0R/relnotes/
- 抓取日期：2026-11-12
- 抓取方式：curl --http1.1 --compressed 直连取全文（138,955 字节），HTML 转文本后定位 2.2.5 节
- 页面标识：`$FreeBSD: src/release/doc/en_US.ISO8859-1/relnotes/article.sgml,v 1.1068.2.20.2.3 2008/02/16 16:03:48 bmah Exp $`
- 用途：Task 8.2 G4 · V37.1.7.4“从 Sun 到 FreeBSD 的移植途径”补证（D2 块，ref_id 见库）

## 抓取正文（节选，2.2.5 File Systems）

```
[amd64, i386] Experimental support for the TMPFS file system has been added. TMPFS is
an efficient memory file system originally developed for the NetBSD project during the
Google Summer of Code. More information can be found in the manual
page.

The unionfs file system has been re-implemented. This version solves many crashing and
locking issues compared to the previous implementation. It also adds new
“transparent” and “masquerade” modes for automatically creating
files in the upper file system layer of unions. More information can be found in the
manual page. [MERGED]

[amd64, i386, pc98] Support for Sun's ZFS has been added. More information about this
file system can be found in the manual
page or on the .

Initial (read-only) support for SGI's XFS file system has been added.
```

## 说明

HTML 转文本时链接文本被剥离（原文该句两处链接分别指向 `zfs(8)` 手册页与 `http://www.opensolaris.org/os/community/zfs/`，即 OpenSolaris ZFS page）。节选仅取 2.2.5 节 ZFS 段及其前后各一段以存语境，其余章节未引。
