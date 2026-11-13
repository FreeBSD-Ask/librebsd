<!-- 网页存档｜来源：https://www.dragonflybsd.org/release24/｜抓取：2026-11-13｜正文经 HTML 标签剥离与空白归一；<li> 逐条转“- ”保留条目边界 -->

# DragonFly BSD Release 2.4 发行说明（dragonflybsd.org/release24/）

DragonFly Release 2.4
16 September 2009 (2.4.0)
01 October 2009 (2.4.1)
The DragonFly 2.4 release is here!
Three release options are now available: Our bare-bones CD ISO, a DVD ISO which includes a fully operational X environment, and a bare-bones bootable USB disk-key image (1G disk keys recommended).
In addition we will for the first time be shipping a 64-bit ISO. 64-bit support is stable but there will only be limited
pkgsrc support in this release. Both the bare-bones CD ISO and a bootable USB disk-key image are available for the 64-bit release.
Availability
The release ISO images should be available on most of the mirrors. If the ISO is not available on a certain mirror, please try another one or download it from the DragonFly FTP server.
Special Note on 2.4.1 mirror availability - Unfortunately one of our primary mirrors, which other mirrors use as a source, had a snafu
that probably will not be fixed any time soon. Our second fastest mirror is avalon.dragonflybsd.org, so please use that to obtain the 2.4.1 ISOs and IMGs
you desire if you cannot find them on a more local mirror.
MD5 sums
- MD5 (dfly-2.4.0_REL.img.gz) = d879282c1ed9d1b36282c4b55aa13b83
- MD5 (dfly-2.4.0_REL.iso.gz) = 1a7d1980671e96564d74e9c128d80009
- MD5 (dfly-amd64-2.4.0_REL.iso.gz) = 226139fe8127b406d1bf8239eef420eb
- MD5 (dfly-gui-2.4.0_REL.iso.gz) = 219eb1f640d2b8034b685a74645fef23
- MD5 (dfly-2.4.0_REL.img) = 2ac933f712a9138af1fba712c21cc80a
- MD5 (dfly-2.4.0_REL.iso) = 495183dfe161af066935f6ffa8093556
- MD5 (dfly-amd64-2.4.0_REL.iso) = f06135a066ef8e5b8d413d65371d98c8
- MD5 (dfly-gui-2.4.0_REL.iso) = 191fc66f6822af04eff9b3fd0693dbfc
- MD5 (dfly-2.4.1_REL.img.gz) = 3fd8412329de1db906e09e3115e512b6
- MD5 (dfly-2.4.1_REL.iso.gz) = 5a828b57db2869e718adacf63943d270
- MD5 (dfly-gui-2.4.1_REL.iso.gz) = 015e3c56ac3f2a7f8073a126a282ff01
- MD5 (dfly-amd64-2.4.1_REL.img.gz) = 17aa83495fd1b11484c7e5dd4342a447
- MD5 (dfly-amd64-2.4.1_REL.iso.gz) = e3ccc01771b8e37b330014afa30a4f9b
- MD5 (dfly-2.4.1_REL.img) = 3cd38cdbc191a8635a87db9adb34b7bd
- MD5 (dfly-2.4.1_REL.iso) = 0f32153897fe25aa2bd8c168a2fce9a7
- MD5 (dfly-amd64-2.4.1_REL.img) = 34f9c6bd2ec8794ff24eed64c1abd03c
- MD5 (dfly-amd64-2.4.1_REL.iso) = c7d84edd1a85cab012a4b0f6e4cda5ec
- MD5 (dfly-gui-2.4.1_REL.iso) = bef875c47c1d7b81d664a8ba236cfdbe
pkgsrc packages
We offer over 6000 pre-built pkgsrc packages for this release. The pkg_radd(1) utility may be used to download pre-built binary packages. By default this script will query the main package site for a random redirect to one of our mirrors. The path can be overridden by setting BINPKG_SITES in /etc/settings.conf.
To get a list of all packages, let pkg_search(1) download the summary file for that release:
# pkg_search -d
We supply a Makefile in /usr to track the pkgsrc tree. We also supply a GIT mirror of the NetBSD pkgsrc CVS repo as
well as the pkgsrc/wip (work in progress) repo at git://git.dragonflybsd.org/pkgsrc.git and we recommend that
users use it instead of pulling from NetBSD with CVS. Our GIT mirror is updated four times a day.
DragonFly 2.4.x Special Installation and Upgrade Notes
VirtualBox and VMWare users - Unless your virtual hard disk is 50G or larger we recommend
doing a UFS install and not the default HAMMER install. We also recommend installing from the CD ISO
and not the DVD ISO. The DVD ISO HAMMER install has bugs (see Known Release Issues).
DVD ISO HAMMER install bugs (2.4.0 only) - You will get a 'guard1x fail @...' loader panic.
See Known Release Issues on how to fix.
2.4.x is a bigger release than normal. The single most invasive change is the introduction of DEVFS.
The /dev filesystem is now mounted by the kernel after it mounts the root filesystem. All major and
minor numbers have changed and the old /dev is no longer meaningful. People who use jails or chroots
will need to adjust their scripts to either mount_null /dev into their jails and chroots or to make
independent DEVFS mounts via mount_devfs into their jails and chroots.
Within DEVFS the entire tty/pty scheme has changed. Users upgrading from 2.2 need to be absolutely
sure to upgrade their world and kernel at the same time or fireworks may ensue.
With this release the libc major number has also been bumped from 6 to 7. Applications should remain
fairly compatible across the upgrade but we recommend that all applications be recompiled and/or
fresh binary packages be loaded from pkgsrc. Certain pty-based applications such as "screen"
may require recompiling.
With this release our new native AHCI driver is now standard. If your system is AHCI-capable and
AHCI-enabled the new driver will take over from NATA and drives may wind up being renamed due to
this. For example, ad6 might become da0. Any legacy ATA ports will continue to be probed by the NATA
driver but their drives may be named differently. USB mass storage devices will also be numbered starting
at 8, for example da8, to avoid conflicting with lower-numbered da* devices.
DEVFS now probes serial numbers. The serial numbers for all ATA, SATA, and SCSI devices will be
recorded by DEVFS in /dev/serno/. USB mass storage devices are more problematic
as the on-device controllers typically do not implement serial number reporting. Users are
encouraged to use /dev/serno/ paths in their /etc/fstab and /etc/rc.conf, and
to even specify the root mount in /boot/loader.conf using a devfs-relative serial number
path such as: vfs.root.mountfrom="hammer:serno/AB34394.s1d". The use of serial numbers to
specify the location of mass storage devices allows you to attach those devices in virtually any
manner without confusing the system. This is particularly important as SATA Port Multiplier
enclosures and systems with large numbers of SATA and E-SATA connectors become prevalent.
The installer now installs (and we recommend) a BOOT+HAMMER setup by default. The installer will
also reference mount points by serial numbers.
We expect there will be numerous issues with this release and we intend to roll a 2.4.1
out in about a month to address what comes up. Known Release Issues
So upgrading to 2.4.x will certainly be a bit painful for users of 2.2.x or earlier releases. We
believe the pain will be well worth the effort.
DragonFly 2.4.0 Release Notes
Release Improvements
Kernel changes
- acpi(4): Import acpica-unix-20090521.
- acpi(4): Improved power & frequency management for cpus.
- acpi(4): Significantly improved APIC support.
- buf/bio: New read-prioritizing bioq sort algorithm. The new algorithm does a much better job
prioritizing reads over writes and also contains features to avoid starving-out writes. It
works best with CAM based drivers but NATA uses some of its functionality too.
- buf/bio: Make biowait(), getpbuf(), and most other buf/bio functions MPSAFE.
- buffer-cache: Improved pipe-lining for writes.
- bpf(4): Add autocloning support
- devfs(5): Replaced the static /dev directory with a dynamic device file system written by Alex Hornung during the Google Summer of Code 2009.
- All block devices now auto-probe their slices and partitions.
- All block devices now auto-probe serial numbers and may be mounted and otherwise referenced by serial number.
- loader.conf now supports specifying the root device by serial number.
- Autocloning support for cloning devices such as VN.
- ddb(4): Fix an IPI messaging lockup which can occur while in ddb(4).
- disklabel64(5): Add UFS + HAMMER boot support (was previously just HAMMER boot support).
- drm(4): Sync code with latest from FreeBSD.
- ext2fs: Support variable inode size (from FreeBSD).
- mountctl/mount -v: New infrastructure for reporting mount flags.
- NFS
- The client-side RPC code has been rewritten. Two kernel threads are now created
for each NFS mount. One handles reading from the socket and the other handles
writing to the socket. A virtually unlimited number of RPCs may be in-flight
at any given moment. The days of multiplicative threads each running synchronous
RPCs are over!
- Use TCP mounts by default as the new RPC architecture can now trivally blow
out UDP sockbufs.
- Hugely improved client-side performance.
- Fixed fsx test regressions.
- Fixed Linux compatibility issues (fix bugs in readdirplus)
- msdos(5): Fixed a number of bugs.
- pci(4): Sync code with FreeBSD 7.2.
- Bring iscsi_initiator(4) from FreeBSD.
- pipe(2): Pipes are now 100% MPSAFE.
- Add new cred/privilege infrastructure for jail and general use.
- Consolidate VOP access tests in vop_helper_access().
- usched_set: Add USCHED_CPU_GET for retrieving the current CPU.
- revoke(2): Reimplemented the revoke code.
- pty: Add Unix98 ptys (/dev/ptmx and /dev/pts/*).
- sound: add autocloning support for dsp devices.
- tcp: Fixed a reestablishment bug for TCP connections if one side reboots without
closing the connection. A port pair could wind up becoming unusable for
upwards of an hour or longer.
- tcp: Improve performance by implementing an automatic high-water mark when
it is not otherwise specified, allowing hysteresis between the kernel and
the tcp protocol stack.
- tsleep: New tsleep interlock mechanics implemented to fix races.
- vkernel(7)
- Fixed entry into ddb(4) when running a SMP vkernel. Fixes stop/cont.
- Fixed startup race with I/O cothread support.
- Fixed some issues - enable ithread preemption, races, and more.
- Fixed races in stopsig() and ipisig().
- libkvm now understands live vkernels.
- libkvm: Add support for accessing a running vkernel's memory by reading its /proc/$pid/mem file.
- vn(4): Add autocloning support
- Fixed permissions check for utimes() - owner can call even if u-w.
- Replace the old BSD malloc code with a port of our slab allocator.
- Fix various clang compile issues
- Add HPET cputimer.
- Add lapic timer and enable it by default.
- Add kernel-layer support for chflags checks, remove (most) from the VFS layer.
HAMMER changes
- Return shorter-form softlinks "@@-1:%05d" when appropriate.
- Add a B-Tree rebalancing feature (hammer rebalance).
- Fixed improper cred checks for utimes().
- Fixed edge case in mirroring code.
- Fixed nohistory mounts and a rare lost inode issue.
- Fixed sticky bit directory handling for deletions.
- Break-up initial mirroring batch so restarts do not start from scratch.
- Better CRC handling, bad-file handling.
- Refactor merged search function to try to avoid missed entries.
- Limit recursion for long directory chains, update mtime/ctime.
- Improve performance for large write loads.
- Improve directory layout (in-place upgrade to version 2).
- Allow hammer -b to specify bytes per second if no suffix is supplied.
- Extract PFS null mounts from anywhere in the filesystem, instead of just from the /pfs subdirectory.
- Add hammer info directive which prints useful info about a hammer filesystem.
Hardware changes (non-networking)
- cxm(4): Add new driver for Hauppauge PVR-250/350 video capture cards (from FreeBSD).
- kbdmux(4): Add multiple keyboards on the console via keyboard multiplexer (from FreeBSD).
- mpi(4): Sync the driver with the latest version from FreeBSD.
- mpt(4): Sync the driver with the latest version from FreeBSD.
- ahci(4): Implement a native AHCI driver with full hot-plug and port multiplier support.
Also implement ATA pass-through. Uses CAM.
- sili(4): Implement a native Silicon Image 3132 driver with full hot-plug and port multiplier support.
Also implement ATA pass-through. Uses CAM.
Hardware changes (networking)
- ae(4): Add driver for Attansic/Atheros L2 FastEthernet (from FreeBSD).
- ath(4): Add open source HAL code (from FreeBSD) and make it possible to build it into the kernel.
- em(4): Synced with Intel's em-6.9.6 (from FreeBSD).
- emx(4): Copy of em(4) which supports only 8257{1,2,3} parts.
- iwi(4): Upgrade to use 3.0 firmware and use firmware(9) API to load firmware.
- mxge(4): Add driver for mxge 10GigE (from FreeBSD + minor adjustments)
- tap(4): Add ifclone support and autoclone support.
- vke(4): Convert from kqueue API to cothread API.
- Turn on adaptive MPSAFE for network threads, and MPSAFE for IP and ARP.
- RSS: Add Toeplitz hash function.
- Split ifnet serializer.
- Add ifpoll, which support hardware TX/RX queues based polling.
Userland changes
- Fixed a huge number of compiler warnings for various userland utilities.
- battd(8): Fix some errors and improve the man page
- compilers.conf(5): This file allows to configure ''external'' compilers (e.g. LLVM/clang) for usage with the DragonFly build(7) system.
- cpdup(1): Allow uid/gid/flags changes to fail if running as user.
- env(1): unbreak build of 2.2 release branch under HEAD.
- expr(1): Add support for -- as required by POSIX.
- fetch(1): Synced with FreeBSD.
- devtab: As devfs(5) support access to devices via serial numbers, /etc/devtab can be used to map serial number to human readable labels.
- devfsctl(1): New utility to add/remove/control devfs(5) rules.
- dma(1): The DragonFly Mail Agent is now more robust and reliable.
- ifconfig(8): Add static ARP support.
- installer: Fix the bug when used from console with the LiveDVD.
- installer: Fixed various bugs and cleaned the code.
- iscontrol(8): Brought from FreeBSD.
- libc
- Synced various parts with FreeBSD and NetBSD.
- Add some new system calls.
- Add locale support for static binaries.
- Apply FreeBSD-SA-09:07.libc - fix information leak in db(3).
- Version bump to libc.so.7
- libfetch(3): Synced with FreeBSD.
- libiconv: Add support for static binaries.
- libm
- Imported complex arithmetic functions from {Net,Free}BSD.
- Imported maximum, minimum, and positive difference functions from FreeBSD.
- magic(3): Fix program name extraction from core dumps.
- mount_msdos(8): Add UTF8 support.
- mount_ntfs(8): Add UTF8 support.
- ncal(1): Highlight current day (from FreeBSD).
- pax(1): Add a -O option: force one volume (from NetBSD).
- pkgsrc: pkgsrc GIT repo now shipped instead of CVS repo.
- telnetd(8): Apply FreeBSD-SA-09:05.telnet - fix environment based code execution vulnerability.
- window(1): Synced with NetBSD.
- vknetd(8): Add features, allow IP address to be set in unsecure mode, allow address 0.
- smbfs(8): Add UTF8 support.
- syslogd(8): Sync with FreeBSD.
- telnet(1): Autologin is now disabled by default.
- undo(1)
- Fixed @@ formatting used by undo -ad and fix duplicate test
- Use a Red-Black tree to track HAMMER transaction IDs.
- It can now detect all prior replacements of a file.
- Add an indexing feature to the -t option.
- unix98 ptys
- Implement posix_openpt, ptsname, grantpt, unlockpt
- Change openpty(3) to use unix98 ptys by default and let it fall back to bsd ptys if any problem occurs.
- vinum(8): Support for geometries larger than 2 TB was added.
- A pkgsrc git repo is now available on the CD. You can copy it to /usr/pkgsrc and then use
standard GIT commands to do an incremental update to the latest pkgsrc.
amd64 related changes
- From Jordan Gordeev's Google Summer of Code 2009 project.
- Kernel can now map 512G if KVA space.
- Kernel now supports the entire user VM space.
- Signal stacks, handlers, dynamic binaries, compiler warnings, etc.
- Misc fixes for cross-building amd64.
- Add a build system for amd64 build/test environments.
- Both cross-build and native world/kernel builds work.
- Pkgsrc builds are ramping up.
- Load testing using parallel pkgsrc bulk builds succeeded!
- SMP now works!
Removals
- GNU cpio(1) was removed. The BSD licensed rewrite based on libarchive(3) is now default.
- GNU GCC 3.4 was removed. GCC 4.1.2 and 4.4.1 remain in base.
- Kerberos/heimdal was removed. Use the version from pkgsrc (security/heimdal).
- iwicontrol(8) was removed. The iwi(4) firmware is now loaded automatically.
Contributed Software
- Update file to version 5.03.
- GCC 4.4.1 was added to base, but is not enabled by default.
- Update less to version 429.
- Update OpenSSH to version 5.2p1.
- Update OpenSSL to version 0.9.8k.
- Sync zoneinfo database with tzdata2009l.
DragonFly 2.4.1 Release Notes
General Improvements
- Issues with kqueue and SIGIO not working properly on pipes have been fixed. This issue affected numerous programs including postfix, dovecot,
and others,which use pipes and kqueue for I/O notification.
- 64-bit kernels were unable to probe USB mass storage devices. Now fixed, and a 64-bit USB image is now available for 2.4.1.
- cdrecord sometimes paniced after burning completed.
- Kernel failed to finish CAM probes during boot. (Note that some drivers may still register their CAM busses too late, and this problem
has not yet been tracked down).
- Manual pages specified with relative paths which include a directory component did not work.
- Misc. setuid/setgid issues with exec and [f]chdir, operations sometimes failed.
- Installer's beastie.4th (boot loader issues) have been corrected.
- Boot loader now contains real-mode fixes which may improve booting from USB memory sticks.
- tcsh updated (fixes incorrect default autologout settings)
- Added support for VIA Nano and VIA C7
- Added support for probing OpenBSD slices
- Misc manual page improvements.
- New aibs(4) driver for ASUSTeK AI Booster ACPI ATK0110 voltage, temperature and fan sensors.
Contributed Software
- Updated tcsh to 6.17.00
DragonFly BSD/
release24
Last edited Tue Dec 14 06:08:20 2010
Tue Feb 24 03:24:08 2009 -->
Site copyright © 2003-2022
