# build(7) — FreeBSD 杂类手册页（构建系统导引）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=build&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.5.2“交叉构建的目标描述”补证（D2 块）：xdev 的 TARGET／TARGET_ARCH（D2 块，ref_id 见库）

## 抓取正文（节选）

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

## 引文摘录（空白已归一，供逐字核对）

tinderbox Execute the same targets as universe. In addition print a summary of all failed targets at the end and exit with an error if there were any. toolchains Create a build toolchain for each architecture supported by the build system. xdev Builds and installs a cross-toolchain and sysroot for the given TARGET and TARGET_ARCH. The sysroot contains target library and headers. The target is an alias for xdev-build and xdev-install. The location of the files installed can be controlled with DESTDIR. The target lo- cation in DESTDIR is ${DESTDIR}/${XDTP} where XDTP de- faults to /usr/${XDDIR} and XDDIR defaults to ${TARGET_ARCH}-freebsd. update-packages Create or update the freebsd-base(7) package repository for the base system. * If an old repository is being updated, then packages whose contents have not changed since the previous version will be copied into the new repository to avoid needless updating of the version number. * If PKG_REPO_SIGNING_KEY is defined, the repo will be signed according to pkg-repo(8). xdev-build Builds for the xdev target. xdev-install Installs the files for the xdev target. xdev-links Installs autoconf-style symlinks to ${DESTDIR}/usr/bin pointing into the xdev toolchain in ${DESTDIR}/${XDTP}. Kernel specific build targets in /usr/src are: buildkernel Rebuild the kernel and the kernel modules. The object
