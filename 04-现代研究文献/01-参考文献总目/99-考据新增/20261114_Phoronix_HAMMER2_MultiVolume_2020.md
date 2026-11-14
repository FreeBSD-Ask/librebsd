<!-- 网页存档｜来源：https://www.phoronix.com/news/HAMMER2-Multi-Volume｜抓取：2026-11-14｜本机直取 403，经 exa 服务端取回正文（2026-11-14） -->

# DragonFlyBSD Adds HAMMER2 Multi-Volumes Support — Phoronix（2020-12-27）

DragonFlyBSD Adds HAMMER2 Multi-Volumes Support

Written by Michael Larabel in BSD on 27 December 2020 at 12:00 AM EST. 10 Comments

The HAMMER2 file-system that has been used by default on DragonFlyBSD for some time has lacked multi-volumes support compared to its former HAMMER1 file-system. But as of this weekend in the latest Git development code, HAMMER2 now has initial support for multiple volumes.

HAMMER2 with the upcoming DragonFlyBSD 6.0 has initial multi-volumes support in place with currently being able to handle up to 64 volumes. The functionality is similar to that of HAMMER1 for allowing a HAMMER2 file-system to span multiple block devices. The current limit of supporting up to 64 volumes is lower than the 256 volumes that HAMMER1 can span.

The code merged includes the kernel support as well as the updated user-space utilities for passing multiple volumes for creating and dealing with a HAMMER2 multi-volume setup.
