# ports(7) — FreeBSD 杂类手册页（Ports 套件）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=ports&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.6.1“基本系统与 Ports 树的分界”补证（D2 块）：Collection 统一编译安装（D2 块，ref_id 见库）

## 抓取正文（节选）

```
PORTS(7)		 Miscellaneous Information Manual		PORTS(7)

NAME
     ports -- contributed applications

DESCRIPTION
     The  FreeBSD  Ports  Collection  offers a simple way to compile and install
     third party applications.	It is also used to build  packages,  to  be  in-
     stalled using pkg(8).

     The  ports  tree,	typically located at /usr/ports, consists of subdirecto-
     ries, one for each category; those in turn contain individual ports.   Each
     port  is a directory with metadata and patches necessary to make the origi-
     nal application source code compile and run on FreeBSD.  Compiling  an  ap-
     plication	is  as simple as typing "make build" in the port directory.  The
     Makefile automatically fetches the application source code, either  from  a
     local  disk  or  the network, unpacks it, applies the patches, and compiles
     it.  It also recursively handles dependencies -- other pieces  of	software
     the port depends on in order to build and work.  Afterwards, "make install"
     installs the application.

     The  FreeBSD Ports Collection is maintained in several branches, which dif-
     fer mostly by versions of software provided: the main branch  contains  all
     the  latest  changes  and	corresponds to the latest package set, while the
     quarterly branches only provide critical fixes.  The  main  branch  can  be
     cloned and updated from the Git repository located at:

     https://git.FreeBSD.org/ports.git

     so eg:

     git clone https://git.FreeBSD.org/ports.git

     The  quarterly branches can be found in Git as branches like yyyyQn , where
     yyyy indicates the year and n indicates the quarter (1 to 4), eg:

```

## 引文摘录（空白已归一，供逐字核对）

PORTS(7) Miscellaneous Information Manual PORTS(7) NAME ports -- contributed applications DESCRIPTION The FreeBSD Ports Collection offers a simple way to compile and install third party applications. It is also used to build packages, to be in- stalled using pkg(8). The ports tree, typically located at /usr/ports, consists of subdirecto- ries, one for each category; those in turn contain individual ports. Each port is a directory with metadata and patches necessary to make the origi- nal application source code compile and run on FreeBSD. Compiling an ap- plication is as simple as typing "make build" in the port directory. The Makefile automatically fetches the application source code, either from a local disk or the network, unpacks it, applies the patches, and compiles it. It also recursively handles dependencies -- other pieces of software the port depends on in order to build and work. Afterwards, "make install" installs the application. The FreeBSD Ports Collection is maintained in several branches, which dif- fer mostly by versions of software provided: the main branch contains all the latest changes and corresponds to the latest package set, while the quarterly branches only provide critical fixes. The main branch can be cloned and updated from the Git repository located at: https://git.FreeBSD.org/ports.git so eg: git clone https://git.FreeBSD.org/ports.git The quarterly branches can be found in Git as branches like yyyyQn , where yyyy indicates the year and n indicates the quarter (1 to 4), eg:
