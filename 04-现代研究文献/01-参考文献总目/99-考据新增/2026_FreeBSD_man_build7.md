# build(7) — FreeBSD 杂类手册页（构建系统导引）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=build&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.5.2“交叉构建的目标描述”（b023）＋V37.6.6.1“基本系统与 Ports 树的分界”／V37.6.3.3“并行构建的作业调度”／V37.6.5.1“DESTDIR 的安装根”（b024）补证（D2 块）：四段节选（D2 块，ref_id 见库）

## 抓取正文（节选一）

```

NAME
     build -- general instructions on how to build the FreeBSD system

DESCRIPTION
     The  sources  for	the FreeBSD system and its applications are contained in
     three directories, normally:

     /usr/src	 "base system", loosely defined as everything required to  build
		 the system to a useful state

     /usr/doc	 system documentation, excluding manual pages

     /usr/ports  third-party  software, with a consistent interface for building
		 and installing them; see ports(7)

     These directories may be initially empty or non-existent until updated with
     Git (devel/git from the FreeBSD Ports Collection).

     The make(1) command is used in each of these directories to build	and  in-
     stall the things in that directory.  Issuing the make(1) command in any di-
     rectory issues the make(1) command recursively in all subdirectories.  With
     no  target specified, the items in the directories are built and no further
     action is taken.

     A source tree is allowed to be read-only.	As described in make(1), objects
     are usually built in a separate object directory hierarchy specified by the
     environment  variable  MAKEOBJDIRPREFIX,  or  under  /usr/obj  if	variable
     MAKEOBJDIRPREFIX  is  not set.  The canonical object directory is described
     in the documentation for the buildworld target below.

     The build may be controlled by defining make(1) variables described in  the
     "ENVIRONMENT"   section   below,	and   by  the  variables  documented  in
     make.conf(5).

     The default components included in the build  are	specified  in  the  file
     /etc/src.conf  in	the  source tree.  To override the default file, include
     the SRCCONF option in the make steps, pointing to a custom  src.conf  file.
```

## 抓取正文（节选二）

```
		      release(7) and is unrelated  to  building  freebsd-base(7)
		      packages.

     installworld     Install  everything  built  by a preceding buildworld step
		      into the directory hierarchy pointed to by  make(1)  vari-
		      able DESTDIR.

		      If  installing onto an NFS file system and running make(1)
		      with the -j option, make sure that rpc.lockd(8) is running
		      on both client and server.  See rc.conf(5) on how to  make
		      it start at boot time.

     toolchain	      Create the build toolchain needed to build the rest of the
		      system.	For cross-architecture builds, this step creates
		      a cross-toolchain.

     universe	      For each architecture, execute a buildworld followed by  a
		      buildkernel for all kernels for that architecture, includ-
		      ing LINT.  This command takes a long time.

     kernels	      Like universe with WITHOUT_WORLDS defined so only the ker-
		      nels for each architecture are built.

     worlds	      Like  universe  with  WITHOUT_KERNELS  defined so only the
		      worlds for each architecture are built.

     targets	      Print a list of supported TARGET / TARGET_ARCH  pairs  for
		      world and kernel targets.

     tinderbox	      Execute the same targets as universe.  In addition print a
		      summary  of all failed targets at the end and exit with an
		      error if there were any.

     toolchains       Create a build toolchain for each  architecture  supported
		      by the build system.

     xdev	      Builds  and installs a cross-toolchain and sysroot for the
		      given TARGET and TARGET_ARCH.  The sysroot contains target
```

## 抓取正文（节选三）

```

     tinderbox	      Execute the same targets as universe.  In addition print a
		      summary  of all failed targets at the end and exit with an
		      error if there were any.

     toolchains       Create a build toolchain for each  architecture  supported
		      by the build system.

     xdev	      Builds  and installs a cross-toolchain and sysroot for the
		      given TARGET and TARGET_ARCH.  The sysroot contains target
		      library  and  headers.   The  target  is	an   alias   for
		      xdev-build  and  xdev-install.   The location of the files
		      installed can be controlled with DESTDIR.  The target  lo-
		      cation  in  DESTDIR  is  ${DESTDIR}/${XDTP} where XDTP de-
		      faults   to   /usr/${XDDIR}   and   XDDIR   defaults    to
		      ${TARGET_ARCH}-freebsd.

     update-packages  Create  or  update  the freebsd-base(7) package repository
		      for the base system.

		      *   If an old repository is being updated,  then	packages
			  whose  contents  have  not  changed since the previous
			  version will be copied  into	the  new  repository  to
			  avoid needless updating of the version number.

		      *   If  PKG_REPO_SIGNING_KEY  is defined, the repo will be
			  signed according to pkg-repo(8).

     xdev-build       Builds for the xdev target.

     xdev-install     Installs the files for the xdev target.

     xdev-links       Installs	autoconf-style	symlinks  to  ${DESTDIR}/usr/bin
		      pointing into the xdev toolchain in ${DESTDIR}/${XDTP}.

     Kernel specific build targets in /usr/src are:

     buildkernel       Rebuild	the  kernel  and the kernel modules.  The object
```

## 抓取正文（节选四）

```

     DEBUG_FLAGS       Defines a set of debugging flags that  will  be	used  to
		       build   all   userland  binaries  under	/usr/src.   When
		       DEBUG_FLAGS is defined, the install and installworld tar-
		       gets install binaries from the  current	MAKEOBJDIRPREFIX
		       without	stripping,  so that debugging information is re-
		       tained in the installed binaries.

     DESTDIR	       The directory hierarchy prefix where built  objects  will
		       be  installed.  If not set, DESTDIR defaults to the empty
		       string.	If set, DESTDIR must specify an absolute path.

     MAKEOBJDIRPREFIX  Defines the prefix for directory names  in  the	tree  of
		       built  objects.	 Defaults  to  /usr/obj  if not defined.
		       This variable should only be set in  the  environment  or
		       /etc/src-env.conf   and	 not   via   /etc/make.conf   or
		       /etc/src.conf or the command line.  MAKEOBJDIRPREFIX must
		       specify an absolute path.

     WITHOUT_WERROR    If defined, compiler warnings will not cause the build to
		       halt, even if the makefile says otherwise.

     WITH_CTF	       If defined, the build process will  run	the  DTrace  CTF
		       conversion tools on built objects.

     Additionally,  builds  in	/usr/src are influenced by the following make(1)
     variables:

     CROSS_TOOLCHAIN	Requests use of an external toolchain  to  build  either
			the  world  or	kernel.  This value of this variable can
			either be the full path to a file, or the base name of a
			file in ${LOCALBASE}/share/toolchains.	The file  should
			be a make file which sets variables to request an exter-
			nal toolchain such as XCC.

			External toolchains are available in ports for both LLVM
			and  GCC/binutils.  For external toolchains available in
			ports, CROSS_TOOLCHAIN should be set to the name of  the
```

## 引文摘录（空白已归一，供逐字核对）

NAME build -- general instructions on how to build the FreeBSD system DESCRIPTION The sources for the FreeBSD system and its applications are contained in three directories, normally: /usr/src "base system", loosely defined as everything required to build the system to a useful state /usr/doc system documentation, excluding manual pages /usr/ports third-party software, with a consistent interface for building and installing them; see ports(7) These directories may be initially empty or non-existent until updated with Git (devel/git from the FreeBSD Ports Collection). The make(1) command is used in each of these directories to build and in- stall the things in that directory. Issuing the make(1) command in any di- rectory issues the make(1) command recursively in all subdirectories. With no target specified, the items in the directories are built and no further action is taken. A source tree is allowed to be read-only. As described in make(1), objects are usually built in a separate object directory hierarchy specified by the environment variable MAKEOBJDIRPREFIX, or under /usr/obj if variable MAKEOBJDIRPREFIX is not set. The canonical object directory is described in the documentation for the buildworld target below. The build may be controlled by defining make(1) variables described in the "ENVIRONMENT" section below, and by the variables documented in make.conf(5). The default components included in the build are specified in the file /etc/src.conf in the source tree. To override the default file, include the SRCCONF option in the make steps, pointing to a custom src.conf file.

release(7) and is unrelated to building freebsd-base(7) packages. installworld Install everything built by a preceding buildworld step into the directory hierarchy pointed to by make(1) vari- able DESTDIR. If installing onto an NFS file system and running make(1) with the -j option, make sure that rpc.lockd(8) is running on both client and server. See rc.conf(5) on how to make it start at boot time. toolchain Create the build toolchain needed to build the rest of the system. For cross-architecture builds, this step creates a cross-toolchain. universe For each architecture, execute a buildworld followed by a buildkernel for all kernels for that architecture, includ- ing LINT. This command takes a long time. kernels Like universe with WITHOUT_WORLDS defined so only the ker- nels for each architecture are built. worlds Like universe with WITHOUT_KERNELS defined so only the worlds for each architecture are built. targets Print a list of supported TARGET / TARGET_ARCH pairs for world and kernel targets. tinderbox Execute the same targets as universe. In addition print a summary of all failed targets at the end and exit with an error if there were any. toolchains Create a build toolchain for each architecture supported by the build system. xdev Builds and installs a cross-toolchain and sysroot for the given TARGET and TARGET_ARCH. The sysroot contains target

tinderbox Execute the same targets as universe. In addition print a summary of all failed targets at the end and exit with an error if there were any. toolchains Create a build toolchain for each architecture supported by the build system. xdev Builds and installs a cross-toolchain and sysroot for the given TARGET and TARGET_ARCH. The sysroot contains target library and headers. The target is an alias for xdev-build and xdev-install. The location of the files installed can be controlled with DESTDIR. The target lo- cation in DESTDIR is ${DESTDIR}/${XDTP} where XDTP de- faults to /usr/${XDDIR} and XDDIR defaults to ${TARGET_ARCH}-freebsd. update-packages Create or update the freebsd-base(7) package repository for the base system. * If an old repository is being updated, then packages whose contents have not changed since the previous version will be copied into the new repository to avoid needless updating of the version number. * If PKG_REPO_SIGNING_KEY is defined, the repo will be signed according to pkg-repo(8). xdev-build Builds for the xdev target. xdev-install Installs the files for the xdev target. xdev-links Installs autoconf-style symlinks to ${DESTDIR}/usr/bin pointing into the xdev toolchain in ${DESTDIR}/${XDTP}. Kernel specific build targets in /usr/src are: buildkernel Rebuild the kernel and the kernel modules. The object

DEBUG_FLAGS Defines a set of debugging flags that will be used to build all userland binaries under /usr/src. When DEBUG_FLAGS is defined, the install and installworld tar- gets install binaries from the current MAKEOBJDIRPREFIX without stripping, so that debugging information is re- tained in the installed binaries. DESTDIR The directory hierarchy prefix where built objects will be installed. If not set, DESTDIR defaults to the empty string. If set, DESTDIR must specify an absolute path. MAKEOBJDIRPREFIX Defines the prefix for directory names in the tree of built objects. Defaults to /usr/obj if not defined. This variable should only be set in the environment or /etc/src-env.conf and not via /etc/make.conf or /etc/src.conf or the command line. MAKEOBJDIRPREFIX must specify an absolute path. WITHOUT_WERROR If defined, compiler warnings will not cause the build to halt, even if the makefile says otherwise. WITH_CTF If defined, the build process will run the DTrace CTF conversion tools on built objects. Additionally, builds in /usr/src are influenced by the following make(1) variables: CROSS_TOOLCHAIN Requests use of an external toolchain to build either the world or kernel. This value of this variable can either be the full path to a file, or the base name of a file in ${LOCALBASE}/share/toolchains. The file should be a make file which sets variables to request an exter- nal toolchain such as XCC. External toolchains are available in ports for both LLVM and GCC/binutils. For external toolchains available in ports, CROSS_TOOLCHAIN should be set to the name of the
