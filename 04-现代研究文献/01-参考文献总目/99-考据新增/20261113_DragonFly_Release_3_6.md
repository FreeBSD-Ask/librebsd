<!-- 网页存档｜来源：https://www.dragonflybsd.org/release36/｜抓取：2026-11-13｜正文经 HTML 标签剥离与空白归一；<li> 逐条转“- ”保留条目边界 -->

# DragonFly BSD Release 3.6 发行说明（dragonflybsd.org/release36/）

DragonFly Release 3.6
Version 3.6.0 released 25 November 2013.
Version 3.6.1 released 21 February 2014.
Big-ticket items
Default to dports
Dports, which uses the FreeBSD ports system as a base, and the 'pkg' tools for installation, is now default on DragonFly. Over 20,000 packages are available in binary or source form.
SMP scaling improvements
Using the parallel building of the 20,000 packages in dports as a test case, contention in the kernel has been nearly eliminated. Improvements scale up with the number of cores in the system.
Experimental i915 and KMS support
Support for newer Intel and ATI chipsets is present in the system. This may not work for every hardware combination, but a number of users have reported success with hardware-accelerated video using this update.
Locale update
locales and libiconv work have brought DragonFly up to date on language support. Utilities should be usable in your native language.
Availability
Two release options are now available for 32-bit as well as for 64-bit x86 machines. 64-bit installations are recommended if you do not need the Linux emulation layer. 32-bit images are only required by legacy, non-64-bit capable hardware such as early Pentium 4 or Athlon based machines.
- An ISO, to be burned to a physical CD or used as an image to install a virtual machine.
- A bootable USB disk-key image. (minimum 2G USB stick needed)
The release ISO images should be available on most of the mirrors. If the ISO is not available on a certain mirror, please try another one or download it from the DragonFly master site. Each image is in the "Live CD" format, meaning that it boots into a running and fully functional DragonFly system, which can be used for testing or system recovery tasks as well as installation. Check the hardware page or boot a Live CD to check for compatibility.
"GUI" images with a desktop are not ready at release time due to the dports switch. It's still possible to install all needed packages via binary download using pkg.
MD5 sums
MD5 sums for the compressed images:
- MD5 (dfly-i386-3.6.0_REL.img.bz2) = be9e47794b539f375f20e3f8de0efa1e
- MD5 (dfly-i386-3.6.0_REL.iso.bz2) = 5ad9ec35ec14e5dfd58ad7b189b21039
- MD5 (dfly-x86_64-3.6.0_REL.img.bz2) = d01b48eab753df8d4fb4665dcab2cbf0
- MD5 (dfly-x86_64-3.6.0_REL.iso.bz2) = 95a12c19dc3f8eb3b09bf8215d06186d
MD5 sums for the uncompressed images:
- MD5 (dfly-i386-3.6.0_REL.img) = 30a312b1daf6f171db52ae4698d3b0e8
- MD5 (dfly-i386-3.6.0_REL.iso) = 4ceb7ccc38a4cb4c2880c4ec7ce6c47f
- MD5 (dfly-x86_64-3.6.0_REL.img) = e0059e91742ea07229f80428903b624a
- MD5 (dfly-x86_64-3.6.0_REL.iso) = 948feb1c946ad1246c06686282968191
pkgsrc packages
There are no prebuilt pkgsrc packages; pkgsrc itself can be installed from tarballs or the cvs repository at http://www.pkgsrc.org/ or see the how-to use pkgsrc page.
dports packages
Packages for dports on DragonFly 3.6 are available, for both 32 and 64 bit platforms. The 'pkg' command will automatically access the main dports repository for DragonFly. Modify /usr/local/etc/pkg.conf if you want to change this and select a different mirror.
If you have pkgsrc packages installed, move or rename /usr/pkg and /var/db/pkg before installing from dports. Dump databases before starting this process. Use 'pkg search' to verify the existence of your needed packages before moving the existing pkgsrc files away, and 'pkg install' to add them.
If you need specific build options for dports packages that aren't on by default, you will need to build your own versions of the software. Download the dports src repository with 'make dports-create' in the /usr directory, and build from there.
See the DPortsUsage page for more details on using and maintaining dports.
DragonFly 3.6 Special Installation and Upgrade Notes
This is the most important part of this page.
- Reboot before performing 'make upgrade' if upgrading from DragonFly 3.4 to DragonFly 3.6
- ABI changes will force reinstallation of all pkgsrc or dports packages. Use 'pkg clean' to remove any cached older dports packages before upgrading.
- See 'dports packages' above for details on pkgsrc -> dports transition.
- HAMMER installations should be over 50G in size to accomodate filesystem history. Otherwise, use UFS.
- The boot loader may need manual intervention (hit ?) if you are using Virtual PC, since Virtual PC does not supply disk serial numbers.
- Qemu users can boot with ACPI disabled or with hw.ioapic_enable=0 in /boot/loader.conf, to reduce console error message.
- xorg may require a config file on i386 DragonFly, under VMWare.
- The installer can only encrypt the root and swap volumes.
DragonFly 3.6.0 Release Notes
For a list of per-commit changes, see the 3.6.0rc tag commit and the 3.6.0 tag commit.
Kernel changes
- Drivers have been made to behave when using a bigger than 128KB maximum IO transfer size
- CLOCK_PROCESS_CPUTIME_ID support added
- Support for memory page attributes added
- Cache invalidation functions enhanced
- Various advanced memory management functions implemented in the x86_64/amd64 64-bit kernel
- drm code updated, initially based on the FreeBSD drm2 code from 2012 and later enhanced with OpenBSD and Linux imports
- GEM and TTM memory managers added
- Many fixes and performance improvements in the network stack
- socket: Extend SO_REUSEPORT to distribute workload to available sockets
- vkernels can now use hardware nested page tables on Intel CPUs
- dirfs, a pseudo-filesystem for vkernels has been implemented. Experimental.
Hardware changes
- Special support for Cyrix CPUs removed
- i915/kms support up to Ivy Bridge chips (Xeon E3v2 / Core i 3000)
- radeon/kms support (very new and still buggy, Xorg driver not enabled by default)
- drm/kms is only expected to work on 64-bit x86_64/amd64 systems
- 32-bit i386 systems use an old xorg-server 1.7 based graphic stack by default, better suited to 10-year old machines
- Many issues fixed and new drivers added in the usb4bsd stack
- A driver for the Emulex OneConnect 10Gb NICs has been added, oce(4)
- I/O performance regression seen in VMware ESXi fixed
- Support for nvidia MCP79 AHCI controllers added
- 10Ge TSO performance improved
- bnx driver: multiple RX/TX rings and MSI-X support for 5718/57785
- cputimer: Allow MP synchronized TSC to become cputimer
- em, igb drivers enhanced. Support for i217 and i218 Intel 1Gb adapters added
- re(4) driver updated, support added for various new chip variants
- ecc(4): Support for E3-1200 v2 and E3-1200 V3 memory controllers added
- Many improvements in the mxge(4) driver for Myricom Myri10GE 10 Gigabit Ethernet adapters
Hardware support:
- Add multiple TX queue and RX queue support in bnx(4)
- Add I217 and I218 support in em(4) and emx(4)
- Add I354 support in igb(4)
- Add 8411/8168G/8168EP/8168GU/8411B and 8401/8402/8106 support in re(4)
- Add Ivy Bridge and Haswell support in ecc(4)
- Add multiple TX queue, RX queue, multiple vector MSI-X and polling(4) support for mxge(4)
- Use TSC as cputimer if TSC is MP synchronized
- Add AMD CPUs family > 10h support in ACPI P-State
Network changes
- Add new semantic to SO_REUSEPORT, so this socket option is useful for TCP listen sockets and unicast UDP sockets. This greatly improves TCP accept(2) performance, overall receiving and sending performance. An nginx patch is integrated into dports to support SO_REUSEPORT.
- Greatly improve both blocking and non-blocking connect(4) performance for TCP sockets.
- Improve TSO performance by using 4KB cluster whenever possible on TCP sending path.
- Add byte based limit to IFQ to reduce buffer-bloat on IFQ for TSO.
- IFQ is now by default two level priority queue, improving dual side TCP sending performance.
HAMMER2
- HAMMER2 is in the system but not ready for use. Development of HAMMER2 is ongoing in DragonFly 3.7.
Removals
- Default pkgsrc installation
Contributed Software
- mdocml updated to 1.12.2.
- libexpat (libbsdxml) updated to 2.1.0.
- grep updated to 2.14.
- diffutils updated to 3.3.
- libmpfr updated to 3.1.2.
- gcc47 updated to 4.7.3.
- zlib updated to 1.2.8.
- awk updated to 20121220.
- tcsh updated to 6.18.01.
- libedit updated to 2012-12-13.
- less updated to 458.
- nvi updated to 2.1.1.
- GDB updated to 7.6.1.
- ldns updated to 1.6.16.
- tnftp updated to 20121224.
Security related
- CVE-2013-5691
DragonFly BSD/
release36
Last edited Tue Aug 13 05:59:46 2024
Wed Nov 6 22:40:15 2013 -->
Site copyright © 2003-2022
