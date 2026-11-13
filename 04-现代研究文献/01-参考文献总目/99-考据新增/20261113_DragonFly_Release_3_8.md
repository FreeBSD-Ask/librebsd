<!-- 网页存档｜来源：https://www.dragonflybsd.org/release38/｜抓取：2026-11-13｜正文经 HTML 标签剥离与空白归一；<li> 逐条转“- ”保留条目边界 -->

# DragonFly BSD Release 3.8 发行说明（dragonflybsd.org/release38/）

DragonFly Release 3.8
Version 3.8.0 released 04 June 2014.
Version 3.8.1 released 16 June 2014.
Version 3.8.2 released 15 August 2014.
Big-ticket items
Dynamic binaries in the root filesystem
DragonFly binaries in /bin and /sbin are now dynamic, which makes it possible to use current identification and authentication technologies such as PAM and NSS to manage user accounts.
Some libraries have been moved to /lib to support this.
New USB
USB4BSD is now default in DragonFly. USB3 devices are supported, though some network devices may not be recognized.
Graphics drivers
The drm/i915 driver had originally been ported from FreeBSD. An ongoing synchronization work with the version present in the Linux 3.8 branch is now going on. The mid-term goal is to be able to use GPUs included in Haswell and ValleyView/Bay Trail processors.
Supported GPUs are currently limited to HD4000 from the Ivy Bridge processor generation.
Even if this goal has not been reached yet, the partial synchronization with the drm/i915 implementation from Linux 3.8.x has already allowed many bugs to be fixed and general driver stability to be improved.
The drm/ttm memory manager used by the drm/radeon driver has been partially synchronized with the version present in Linux 3.9, improving its stability. Howewer, many issues remain and thus Xorg still doesn't use the drm/radeon driver by default.
Last 32-bit release
A 32-bit address space is now a significant limitation in the high-performance world where DragonFly lives.
This is the last DragonFly release planned to work on i386. Please plan to upgrade to 64-bit when possible. Note that prebuilt packages for this release will only exist for 64-bit systems; 32-bit users will have to build by hand.
Availability
64-bit (x86_64) installations are recommended. The 32-bit (i386) should only be used if your hardware cannot support 64-bit operating systems. Each version is available as:
- An ISO, to be burned to a physical CD or used as an image to install a virtual machine.
- A bootable USB disk-key image. (minimum 2G USB stick needed)
The release ISO images should be available on most of the mirrors. If the ISO is not available on a certain mirror, please try another one or download it from the DragonFly master site. Each image is in the "Live CD" format, meaning that it boots into a running and fully functional DragonFly system, which can be used for testing or system recovery tasks as well as installation. Check the hardware page or boot a Live CD to check for compatibility.
"GUI" images with a desktop are not ready at release time.
MD5 sums
MD5 sums for the compressed images:
MD5 (dfly-i386-3.8.2_REL.img.bz2) = eab5b0252c10998ef326bf67b07b2a91
MD5 (dfly-i386-3.8.2_REL.iso.bz2) = 5460fd5b153151ad946bdcfd47fdb6a2
MD5 (dfly-x86_64-3.8.2_REL.img.bz2) = 08e01bbde2a079fc85b7eb25f847a05f
MD5 (dfly-x86_64-3.8.2_REL.iso.bz2) = d620856465e449b99e6a20a4360db2a0
MD5 sums for the uncompressed images:
MD5 (dfly-i386-3.8.2_REL.img) = 795176a8e2e50f423a51a63b880912f1
MD5 (dfly-i386-3.8.2_REL.iso) = 9d65779830e326f33f07170c9790a507
MD5 (dfly-x86_64-3.8.2_REL.img) = a680535033ad7fd4db40259de95bbfad
MD5 (dfly-x86_64-3.8.2_REL.iso) = 6db0878b61e1ef9e9f8ed4c14b931076
dports packages
Packages for dports on DragonFly 3.8 are available, for 64-bit platforms. The 'pkg' command will automatically access the main dports repository for DragonFly. Modify /usr/local/etc/pkg/repos/df-latest.conf if you want to change this and select a different mirror (or replace that file with a modified df-releases.conf to switch to the static 3.8 RELEASE repository).
If you have pkgsrc packages installed, move or rename /usr/pkg and /var/db/pkg before installing from dports. Dump databases before starting this process. Use 'pkg search' to verify the existence of your needed packages before moving the existing pkgsrc files away, and 'pkg install' to add them.
If you need specific build options for dports packages that aren't on by default, you will need to build your own versions of the software. Download the dports src repository with 'make dports-create' in the /usr directory, and build from there.
See the DPortsUsage page for more details on using and maintaining dports.
DragonFly 3.8 Special Installation and Upgrade Notes
This is the most important part of this page.
- For upgrading: /boot/kernel/initrd.img will be deleted and replaced with initrd.img.gz.
- Use UFS for disks under 50G.
- Virtual PC may cause problems with the boot loader (hit ?)
- Qemu users can disable ACPI to reduce console errors (hw.ioapic_enable=0 in /boot/loader.conf).
- The installer can only encrypt the root and swap volumes.
DragonFly 3.8.2 Release Notes
This version has an updated version of OpenSSL, among other changes. See the tag commit for details.
DragonFly 3.8.1 Release Notes
The .1 release includes recent OpenSSL and PAM security updates. See the tag commit for a full list.
DragonFly 3.8.0 Release Notes
For a list of per-commit changes, see the 3.8.0rc tag, 3.8.0rc2 tag and the 3.8.0 tag commit.
Kernel changes
- Various netmap updates (still not functional).
- ohci, uhci, and xhci synced with FreeBSD.
- USB4BSD is now default
- Add native C-state support for Intel CPUs
- Fix and extend mwait C-state support
- Add Intel performance-energy hint support
- Overhaul Intel software controlled clock modulation support
Userland changes
- DragonFly now uses dynamic binaries in the root filesystem
- PAM and NSS will work with DragonFly.
- tcplay has been updated to version 2.0.
- pfi now supports authorized_keys
- tools/hammer-backup.sh, a simple Hammer backup script, added
- Updates/syncs for units(1), sed(1), cmp(1), and newgrp(1).
- fetch, patch, install, and daemon updated.
- GSoC project 'SysV IPC in userspace' committed
Hardware changes
- drm/ttm/i915 updated significantly to match Linux 3.8's DRM implementation
- Updates to bwn(4)
- Updates to vtnet(4)
- cyapa(4) support added (Chromebook touchpads)
- arcmsr(4) updated
Network changes
- Possible panics fixed in gif, pf, ip, and in.
- iwn(4) updated
- ath(4) updated
- Unnecessary network stack IPIs reduced
- ix updated to 2.5.15, with a drop in processing requirements
- TCP port token split for better TCP connect(2) performance
- IPv4 multicast support fixed
HAMMER2
- HAMMER2 is in the system but not ready for use. Development of HAMMER2 is ongoing in DragonFly 3.9.
Removals
- Last bits of Xerox NS support removed
- ATM protocol support removed
- IPX and NCP protocols support removed
- NWFS filesystem removed
Contributed Software
- bmake updated to bmake-20131001.
- mdocml updated to mdocml-1.12.3
- binutils updated to 2.24
- dma updated to version 0.9
- libpcap updated to 1.4.0
- file updated to 5.18
- OpenSSL updated to 1.0.1g
- ee updated to 1.5.2
- tzdata updated to tzdata2014c
- ACPICA updated to 20140424
Security related
- CVE-2014-3879 has been patched as of the 3.8.0 release.
DragonFly BSD/
release38
Last edited Tue Aug 13 05:59:45 2024
Thu May 29 22:17:13 2014 -->
Site copyright © 2003-2022
