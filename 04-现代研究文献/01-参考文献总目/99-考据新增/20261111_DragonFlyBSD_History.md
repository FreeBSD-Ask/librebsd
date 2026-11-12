<!-- 网页存档｜来源：https://www.dragonflybsd.org/history/｜抓取：2026-11-11T21:31+08:00｜正文经 HTML 标签剥离与空白归一 -->

# DragonFly BSD — History

DragonFlyBSD: history
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
history
A technical introduction: The ultimate goal of the DragonFly project at its inception was to provide native clustering support in the kernel. This type of functionality requires a sophisticated cache management framework for filesystem namespaces, file spaces and VM spaces. These and other features eventually culminate in the ability to allow heavily interactive programs to run across multiple machines with cache coherency fully guaranteed in all respects. This also requires being able to divide resources, including the CPU by way of a controlled VM context, for safe assignment to potentially unsecured third-party clusters over the internet. This original design direction, although no longer the primary goal of the DragonFly project, has influenced many of the design decisions made in the intervening years. While full cache coherency is no longer a top level goal, filesystem coherency is, and that direction continues to guide the project in a number of ways.
DragonFly BSD was forked from FreeBSD 4.8 in June of 2003, by Matthew Dillon. The project was originally billed as "the logical continuation of the FreeBSD 4.x series", as quoted in
the announcement, but this description has long since become obsolete. From a performance perspective DragonFly's only real competitor these days is Linux.
DragonFly BSD has been going through rapid and ever increasing development since the fork. One of the important works included the simplification and general cleanup of the majority of the kernel subsystems. This work was originally intended to support single system image clustering, but has had the effect of making the kernel much more reliable, understandable and easily maintainable. One of the fundamental synchronization concepts that DragonFly uses throughout the kernel, the token, lends itself directly to ease of maintenance and understandability of the kernel.
During the first major phase of the project, which lasted until early 2007, the DragonFly project focused on rewriting most of the major kernel subsystems to implement required abstractions and to support mechanics for the second phase of the project, which at the time was intended to be single system image clustering. This involved a great deal of work in nearly every subsystem, particularly the filesystem APIs and kernel core. During this time a paramount goal was to keep the system updated with regard to the third party applications and base system utilities needed to make any system usable in production. This resulted in the adoption of the
pkgsrc
framework for management of all non-base-system third-party applications in order to pool our resources with other BSD projects using this framework.
In the 2007-2008 time frame, a new filesystem called
HAMMER
was developed for DragonFly BSD. HAMMER saw its first light of day in July 2008 with the DragonFly 2.0 release. This filesystem has been designed to solve numerous issues and to add many new capabilities to DragonFly, such as fine-grained history retention (snapshots), instant crash recovery, and near real-time mirroring. The HAMMER filesystem is also intended to serve as a basis for the clustering and other work that makes up the second phase of the project.
From 2009 onward many developers have focused on SMP scalability while others have put an emphasis on new feature development and driver porting. The VM system was finally fine-grain locked all the way down to the pmap in late 2011, resulting in huge performance gains on many-core machines. Major kernel subsystems were also scaled one after another.
In 2012 François Tigeot and a dedicated group of helpers began retooling DRM (the graphics subsystem) with an active port from Linux, slowly bringing DragonFly up to modern standards. As of 2015 fully accelerated 2D, 3D, and video support is operational with Xorg. At around the same time there was also a concerted effort to upgrade the sound system with a major HDA port from FreeBSD. Graphics, Video, and Sound have turned DragonFly into quite a nice desktop.
In 2013 the PID, PGRP, and SESSION subsystems were SMP-scaled. In 2014 one of the few remaining SMP-critical scalability paths, the fork/exec/exit/wait sequence, including related page-faulting and library mapping, was fully scaled, greatly boosting bulk build performance and concurrency.
Also during this period the network stack underwent a continuous stream of small SMP improvements to the point where today all major protocols, including both ipfw and PF, are fully concurrent with few locking collisions. DragonFly BSD enjoys phenomenal networking performance today.
Further and more up to date information on the project goals and status are available on this website, and discussion of the project is possible on a variety of newsgroups, mailing lists and IRC.
See all past DragonFly
releases.
The original photograph that inspired the name:
DragonFly BSD
/
history
Last edited
Thu Jan 17 13:32:06 2019
Wed Mar 10 08:41:35 2010
-->
Site copyright © 2003-2022
