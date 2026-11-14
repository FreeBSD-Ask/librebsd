<!-- 网页存档｜来源：https://www.phoronix.com/review/dragonfly-bsd-hammer2｜抓取：2026-11-14｜本机直取 403，经 exa 服务端取回正文第 1 页（2026-11-14） -->

# HAMMER2 Is Looking & Performing Good As The Future DragonFlyBSD File-System — Phoronix（2017-09-13）

HAMMER2 Is Looking & Performing Good As The Future DragonFlyBSD File-System

Written by Michael Larabel in Operating Systems on 13 September 2017 at 12:06 PM EDT. Page 1 of 3. 5 Comments.

With this week DragonFlyBSD seeing HAMMER2 support added to the installer in preparation for this file-system being an option in the next DragonFly release due out in a few weeks, I've been testing out the state of this HAMMER file-system successor as well as running some benchmarks.

DragonFlyBSD founder Matthew Dillon announced the HAMMER2 file-system back in 2012 while he had been working on it since 2011. At the time he didn't think it would be until "well into 2013" before the file-system would become usable. Now in 2017, we are seeing HAMMER2 stepping closer to the spotlight. With the DragonFlyBSD 4.10 release it will be offered as an option via the installer, but it won't be used by default. Additionally, the /boot partition is still defaulting to UFS.

Among the original goals of HAMMER2 over the original HAMMER file-system were to use a copy-on-write block design, support for writable snapshots, support for multiple roots, queueless mirroring, support for multiple compression algorithms, redundancy improvements, and much more. Many of the HAMMER2 features have been implemented from deduplication to LZ4 compression support, but not all is complete yet for this DragonFly file-system.

In recent months we have seen a lot of stabilization work go into DragonFly's HAMMER2 code as well as some optimizations and finishing up some of the remaining items. Compression, snapshots, deduplication, and some clustering features are among the currently operational features. This HAMMER2 design document outlines some of the current and planned features for the HAMMER2 file-system. There's also a TODO list outlining other work that remains for this file-system focused on DragonFlyBSD.
