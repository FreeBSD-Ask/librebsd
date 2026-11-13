<!-- 网页存档｜来源：https://www.netbsd.org/docs/guide/en/chap-kernel.html｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# NetBSD Guide 第 34 章 Compiling the kernel（§34.1–34.2）

## 抓取正文（章首至 §34.3 前，节选）

```
There are several reasons you might want to compile a NetBSD
 kernel: 
 you can install bug-fixes, security updates, or new
 functionality by rebuilding the kernel from updated
 sources. 
 by removing unused device drivers and kernel sub-systems
 from your configuration, you can dramatically reduce kernel size
 and, therefore, memory usage and attack surface. Care must be taken
 when doing this, since it can result in an unusable system.
 Always back up old working kernels. 
 you can access additional features by enabling kernel
 options or sub-systems, some of which are experimental or
 disabled by default. 
 you can get a deeper knowledge of the system. 
 34.1. Requirements and procedure 
 To recompile the kernel you must have installed the compiler set
 ( comp.tgz ). 
 The basic steps to an updated or customised kernel then are:
 Install or update the kernel sources 
 Create or modify the kernel configuration file 
 Building the kernel from the configuration file, either
 manually or using build.sh 
 Install the kernel 
 34.2. Installing the kernel sources 
 You can get the kernel sources from AnonCVS (see
 Chapter 32, Obtaining the sources ), or from the
 syssrc.tgz 
 tarball that is located in the source/sets/ 
 directory of the release that you are using. 
 If you chose to use AnonCVS to fetch the entire source tree,
 be patient, the operation can last many minutes, because the
 repository contains thousands of files. 
 If you have a source tarball, you can extract it as root: 
 # cd / 
 # tar zxf /path/to/syssrc.tgz 
 Even if you used the tarball from the release, you may wish to
 use AnonCVS to update the sources with changes that have been
 applied since the release.
 This might be especially relevant if you are updating the kernel
 to include the fix for a specific bug, including a vulnerability
 described in a NetBSD Security Advisory.
 You might want to get the latest sources on the relevant release
 or critical updates branch for your version, or Security
 Advisories will usually contain information on the dates or
 revisions of the files containing the specific fixes concerned.
 See Section 32.4, “Fetching by CVS” for more details on the
 CVS commands used to update sources from these branches.
 Once you have the sources available, you can create a custom
 kernel: this is not as difficult as you might think. 
 In fact, a new kernel can be created in a few steps which will
 be described in the following sections. 
 34.3. Creating the kernel configuration file 
 Note 
 The directories described in this section are amd64
 specific. Users of other architectures must substitute the
 appropriate directories, see the subdirectories of
 src/sys/arch for a list. 
 The kernel configuration file defines the type, the number and
 the characteristics of the devices supported by the kernel as
 well as several kernel configuration options. For the amd64
 port, kernel configuration files are located in the
 /usr/src/sys/arch/amd64/conf directory. 
 Please note that the names of the kernel configuration files
 are historically in all uppercase, so they are easy to
 distinguish from other files in that directory: 
 $ cd /usr/src/sys/arch/amd64/conf/ 
 $ ls 
ALL INSTALL XEN3_DOM0 kern.ldscript.kaslr
CVS INSTALL_XEN3_DOMU XEN3_DOMU majors.amd64
GENERIC MODULAR files.amd64 std.amd64
GENERIC_KASLR Makefile.amd64 kern.ldscript std.xen
GENERIC_USERMODE NOCOMPAT kern.ldscript.Xen 
 The easiest way to create a new file is to copy an existing one
 and modify it. Usually the best choice on most platforms is the
 GENERIC configuration, as it contains most drivers and options.
 In the configuration file there are comments describing the
 options; a more detailed description is found in the
 options (4) man page. So, the usual procedure is: 
 $ cp GENERIC MYKERNEL 
 $ vi MYKERNEL 
 The modification of a kernel configuration file basically
 involves three operations: 
 support for hardware devices is included/excluded in the kernel
 (for exampl
```

## 用途注记

Task 8.2 G5-P2 · V41.1.3.4“内核配置表的裁剪能力”P2 联网补证（D2 块；官方 Guide 记载以裁剪配置缩小内核体积、内存占用与攻击面）。
