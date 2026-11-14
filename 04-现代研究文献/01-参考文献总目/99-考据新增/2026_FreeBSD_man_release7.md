# release(7) — FreeBSD 杂类手册页（发布构建）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=release&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.5.2“交叉构建的目标描述”／V37.6.7.1“发布工程的职责分区”补证（D2 块）：TARGET 变量＋洁净环境（D2 块，ref_id 见库）

## 抓取正文（节选一）

```
     The release procedure on some architectures may also require that the md(4)
     (memory  disk)  device  driver  be  present  in the kernel (either by being
     compiled in or available as a module).

     This document does not cover source code management, quality assurance,  or
     other aspects of the release engineering process.

CLEAN RELEASE GENERATION
     Official  releases of FreeBSD are produced in a clean environment to ensure
     consistency between the versions of the src, ports, and doc  trees  and  to
     avoid contamination from the host system (such as local patches, changes to
     make.conf(5),  etc.).   This  is  accomplished  using  the  wrapper  script
     src/release/release.sh.

     release.sh [-c release.conf]

     release.sh checks out the src/, ports/, and doc/ trees to	CHROOTDIR,  then
     calls "make buildworld" and "make installworld" to generate a chroot(8) en-
     vironment.   Next,  "make	release" is run within the chroot(8) environment
     and places the result in $CHROOTDIR/R.

     The optional release.conf configuration file supports the	following  vari-
     ables:

     CHROOTDIR	      The directory within which the release will be built.  De-
		      faults to /scratch.

     CHROOT_MAKEENV   Additional  make(1)  arguments  to pass through, which di-
		      rectly affect the tuning of the build chroot.

     NOGIT	      Do not explicitly require the git(1) port to be installed.

     GITROOT	      The git(1) host used to check out the various trees.   De-
		      faults to https://git.FreeBSD.org.

     SRCBRANCH	      The src/ branch to use.  Defaults to -b main.

     PORTBRANCH       The ports/ branch to use.  Defaults to head/@rHEAD.
```

## 抓取正文（节选二）

```

     GITROOT	      The git(1) host used to check out the various trees.   De-
		      faults to https://git.FreeBSD.org.

     SRCBRANCH	      The src/ branch to use.  Defaults to -b main.

     PORTBRANCH       The ports/ branch to use.  Defaults to head/@rHEAD.

     TARGET	      The target machine type for cross-building a release.

     TARGET_ARCH      The  target  machine architecture for cross-building a re-
		      lease.

		      For the supported list of TARGET and TARGET_ARCH	combina-
		      tions,  consult the output of "make targets" as documented
		      in build(7).

     KERNEL	      The target  kernel  configuration  to  use.   Defaults  to
		      GENERIC.	Multiple KERNEL entries may be specified.

     MAKE_CONF	      The  make.conf(5)  to use for the release build.	Defaults
		      to /dev/null to prevent polluting the release  with  local
		      system changes.

     SRC_CONF	      The src.conf(5) to use for the release build.  Defaults to
		      /dev/null to prevent polluting the release with local sys-
		      tem changes.

     MAKE_FLAGS       Additional flags to pass to make(1).

     WORLD_FLAGS      Additional   flags   to	pass   to   make(1)  during  the
		      "buildworld" phase.  Defaults to	setting  the  number  of
		      make(1)  jobs  (-j)  to  the number of CPUs available on a
		      SMP-capable system.

     KERNEL_FLAGS     Additional  flags  to   pass   to   make(1)   during   the
		      "buildkernel"  phase.   Defaults	to setting the number of
		      make(1) jobs (-j) to half the number of CPUs available  on
```

## 引文摘录（空白已归一，供逐字核对）

The release procedure on some architectures may also require that the md(4) (memory disk) device driver be present in the kernel (either by being compiled in or available as a module). This document does not cover source code management, quality assurance, or other aspects of the release engineering process. CLEAN RELEASE GENERATION Official releases of FreeBSD are produced in a clean environment to ensure consistency between the versions of the src, ports, and doc trees and to avoid contamination from the host system (such as local patches, changes to make.conf(5), etc.). This is accomplished using the wrapper script src/release/release.sh. release.sh [-c release.conf] release.sh checks out the src/, ports/, and doc/ trees to CHROOTDIR, then calls "make buildworld" and "make installworld" to generate a chroot(8) en- vironment. Next, "make release" is run within the chroot(8) environment and places the result in $CHROOTDIR/R. The optional release.conf configuration file supports the following vari- ables: CHROOTDIR The directory within which the release will be built. De- faults to /scratch. CHROOT_MAKEENV Additional make(1) arguments to pass through, which di- rectly affect the tuning of the build chroot. NOGIT Do not explicitly require the git(1) port to be installed. GITROOT The git(1) host used to check out the various trees. De- faults to https://git.FreeBSD.org. SRCBRANCH The src/ branch to use. Defaults to -b main. PORTBRANCH The ports/ branch to use. Defaults to head/@rHEAD.

GITROOT The git(1) host used to check out the various trees. De- faults to https://git.FreeBSD.org. SRCBRANCH The src/ branch to use. Defaults to -b main. PORTBRANCH The ports/ branch to use. Defaults to head/@rHEAD. TARGET The target machine type for cross-building a release. TARGET_ARCH The target machine architecture for cross-building a re- lease. For the supported list of TARGET and TARGET_ARCH combina- tions, consult the output of "make targets" as documented in build(7). KERNEL The target kernel configuration to use. Defaults to GENERIC. Multiple KERNEL entries may be specified. MAKE_CONF The make.conf(5) to use for the release build. Defaults to /dev/null to prevent polluting the release with local system changes. SRC_CONF The src.conf(5) to use for the release build. Defaults to /dev/null to prevent polluting the release with local sys- tem changes. MAKE_FLAGS Additional flags to pass to make(1). WORLD_FLAGS Additional flags to pass to make(1) during the "buildworld" phase. Defaults to setting the number of make(1) jobs (-j) to the number of CPUs available on a SMP-capable system. KERNEL_FLAGS Additional flags to pass to make(1) during the "buildkernel" phase. Defaults to setting the number of make(1) jobs (-j) to half the number of CPUs available on
