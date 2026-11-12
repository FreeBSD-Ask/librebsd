# Berkeley 发行手册前言（4.1／4.2／4.3 前言，NetBSD 源码所存）引用卡

> 用途：V11.4.2.1“成果入编的通道梳理”、4.2.3“移植改造中的再创造”、4.2.5“承接者的身份与动机”内容补证（V11 补证批 b017）。

## 一、著录

The Regents of the University of California. Preface to the 4.2 Berkeley distribution; Preface to the 4.3 Berkeley distribution[Z/OL]. 见 `share/man/man0/title.urm`（Berkeley 4.x 手册总页前言，随 NetBSD 源码树递藏）[2026-11-13]. 工作副本：`03-原始史料库/02-man源与posix仓库/01-repos/netbsd-src/share/man/man0/title.urm`；上游：https://cgit.netbsd.org/src/tree/share/man/man0/title.urm.

- 责任者：加州大学董事会（正文由 CSRG 成员署名：4.2 前言署 S. J. Leffler、W. N. Joy、M. K. McKusick；4.3 前言署 M. K. McKusick、M. J. Karels、J. M. Bloom）
- 载体：手册源文件（roff 文档，`man0/title.urm`）
- `source_tier=primary`（发行方当期自述，一手）
- 访问日：2026-11-13
- 说明：roff 标记与行内强调符已剥离，仅保留正文字句；原文分句换行处按语义接续，未改字。

## 二、逐字引文（英文，未翻译）

4.2 发行前言的定位句：

> This update to the 4.1 distribution of June 1981 provides support for the VAX 11/730, full networking and interprocess communication support, an entirely new file system, and many other new features.

4.2 发行前言论网络代码的来源：

> Rob Gurwitz of BBN wrote the initial version of the code upon which the current networking support is based.

4.2 发行前言之资助申谢（署名：S. J. Leffler、W. N. Joy、M. K. McKusick）：

> Once again, the financial support of the Defense Advanced Research Projects Agency is gratefully acknowledged.

4.3 发行前言的定位句：

> This update to the 4.2 distribution of August 1983 provides substantially improved performance, reliability, and security, the addition of Xerox Network System (NS) to the set of networking domains, and partial support for the VAX 8600 and MICROVAXII.

## 三、考据说明

1. 该文件是 Berkeley 手册总页的“发行前言”合集，逐版一序（第四版、4.1、4.2、4.3 各有序），序末署名与资助申谢一并留存——**发行方可自陈资助关系，这是入编通道的一手证据**，无须依赖事后追述。
2. 4.2 前言把“full networking and interprocess communication support, an entirely new file system”列为该版要点，同段又说“Rob Gurwitz of BBN wrote the initial version of the code upon which the current networking support is based”——来源（BBN 初版）与再创造（伯克利改造为发行版）在同段并陈。
3. 版次与年份（4.1：1981 年 6 月；4.2：1983 年 8 月；4.3 序述及 4.2 发行）可用于时序判定，但**序述年份不等于物证年份**，须与发行说明、源码版本标识互证。
4. 禁引核查：源码树内原始文档，`banned_source=0`；属发行方自述，按 L4 纪律标注，涉及版本事实时以 L5 级文书（发行说明／源码标识）复核。
