# 复核摘要 第6/8部分（文件 126-150）

## [126] 2019_FreeBSD_社区论文与演讲_191191_Brooks_Davis_CheriABI_Hardware_enforced_memor.pdf
- 大小: 654KB  类型: .pdf  页数: 15
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019bsdcandavischeriabipaperpdf, 2019eurobsdcondavischeriabihardwareenforcedmemorysafetyforfreebsdslidespdf, davischeriabipaper
- 日志题名: 
- 内容头部: CheriABI: Enforcing Valid Pointer Provenance and Minimizing Pointer Privilege in the POSIX C Run-time Environment Brooks Davis∗ brooks.davis@sri.com Robert N. M. Watson† robert.watson@cl.cam.ac.uk Alexander Richardson† alexander.richardson@cl.cam.ac.uk Peter G. Neumann∗ peter.neumann@sri.com Simon W. Moore† simon.moore@cl.cam.ac.uk John Baldwin‡ john@araratriver.co David Chisnall§ David.Chisnall@microsoft.com Jessica Clarke† jessica.clarke@cl.cam.ac.uk Nathaniel Wesley Filardo† nwf20@cam.ac.uk Khilan Gudka† khilan.gudka@cl.cam.ac.uk Alexandre Joannou† alexandre.joannou@cl.cam.ac.uk Ben Laurie⁄pilcrow benl@google.com A. Theodore Markettos† theo.markettos@cl.cam.ac.uk J. Edward Maste† emaste@f

## [127] 2019_FreeBSD_社区论文与演讲_197197_Andrew_Turner_Fuzzing_the_kernel_Porting_the_.pdf
- 大小: 4989KB  类型: .pdf  页数: 50
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019bsdcanturnerfuzzingthekernelpaperpdf, 2019turnerfuzzingthekernelportingtheclangsanitizerstofreebsden, turnerfuzzingthekernelpaper
- 日志题名: 
- 内容头部: Fuzzing the kernel Andrew Turner andrew@FreeBSD.org Who am I? •FreeBSD Committer (andrew@) •Research Associate in the University of Cambridge •Sometimes a Freelance Software Engineer Sanitizers Sanitizers •A tool from the compiler to instrument code •Add function calls on in interesting points in the code, e.g.: •Entry to a basic block •On comparison operations •Every memory access •The compiler provides a runtime for userspace •We need our own runtime in the kernel Undefined Behaviour KUBSAN –Undefined Behaviour Sanitizer •Instruments code that may be undefined depending on input, e.g. •Misaligned or NULL pointer •Shift out of bounds •From the NetBSD µUBsan •imported 3 August 2018 •Imported

## [128] 2019_FreeBSD_社区论文与演讲_199199_Matt_Ahrens_How_ZFS_snapshots_really_work_and.pdf
- 大小: 934KB  类型: .pdf  页数: 38
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019bsdcanahrenshowzfssnapshotsreallyworkpaper, 2019bsdcanahrenshowzfssnapshotsreallyworkpaperpdf, ahrenshowzfssnapshotsreallyworkpaper
- 日志题名: 
- 内容头部: How ZFS Snapshots Really Work Matt Ahrens BSDCAN 2019 What are snapshots? ● Store an old “copy” of the data ● “Oops” recovery ● Malware recovery ● Replication with zfs send/receive How to use snapshots zfs snapshot pool/fs@snap zfs snapshot -r pool@snap zfs destroy pool/fs@snap zfs send -i @oldsnap pool/fs@newsnap | \ ssh … zfs receive … zfs get … pool/fs@snap How to use snapshots 1. Take a snapshot of every filesystem every hour (8700 snapshots per filesystem per year) 2. … 3. Wonder where all your space went How do snapshots work? Copy-On-Write Transaction Groups (TXG’s) 1. Initial block tree 2. COW some blocks 4. Rewrite uberblock (atomic)3. COW indirect blocks ZFS Snapshots ● How to crea

## [129] 2019_FreeBSD_社区论文与演讲_201201_Simon_Gerraty_mac_grantbylabel_Securely_contr.pdf
- 大小: 149KB  类型: .pdf  页数: 8
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 043freebsdmandatoryaccesscontrolusageforimplementingenterprisesecuritypolicies, pubscholar043freebsdmandatoryaccesscontrolusageforimplementingenterprisesecuritypolicies, pubscholar043freebsdmandatoryaccesscontrolusageforimplementingenterprisesecuritypoliciespdf
- 日志题名: 
- 内容头部: 5/18/2019 Running daemons non-root ﬁle:///Users/sjg/work/rst/talks/obj/run-daemons-non-root-slides.htm 1/8 Running daemons non-root Simon J. Gerraty Juniper Networks, Inc. 2019 Imagine something very witty here Agenda Introduction Daemons need privileges Approach Progress Further work Q&A Introduction Running daemons non-root was goal 20 years ago Hacking kernel always an option Modern FreeBSD offers better solutions Capabilities (Capsicum) Mandatory Access Control (MAC) Daemons need privileges open AF_UNIX sockets in protected dirs open raw sockets bind reserved ports set ﬁb (routing instance) read[/write] routing socket set sysctl values tweak rlimits conﬁgure devices read/write /dev/mem 5

## [130] 2019_FreeBSD_社区论文与演讲_202202_Albert_Dengg_Managing_Jails_with_Ansible_A_sh.pdf
- 大小: 146KB  类型: .pdf  页数: 18
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: freesoftwarefoundationincvciscosystemsincsdny2008, richardstallmansayshehasreturnedtothefreesoftwarefoundationboardofdirectors, wallacevfreesoftwarefoundation105cv00618sdind2006
- 日志题名: 
- 内容头部: Managing Jails with Ansible A showcase for building a container infrastructure on FreeBSD Albert Dengg <albert@fsfe.org> Free Software Foundation Europe 2019-05-18 About Me Sysadmin been using mostly Linux for > 20 years relativly new to FreeBSD ( 5 years or so) WHY? Why would you want to do that? WHY? Contra ▶ There is already tool X1 that does that ▶ You will have python as a dependency in every jail ▶ It’s complicated ▶ ... 1for any X∀Z>0 tools WHY? Pro ▶ I’m already using ansible to setup most stuﬀ ▶ I already have python as a dependency for that reason ▶ Once you have done it "the hard way", you will have a better idea what’s actually going on ▶ ... Building Blocks Basics ▶ FreeBSD ▶ ja

## [131] 2019_FreeBSD_社区论文与演讲_205205_Jonathan_Looney_Netflix_and_FreeBSD_Reflectio.pdf
- 大小: 955KB  类型: .pdf  页数: 25
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: netflixopenconnectappliancefreebsdbased, 衍生组采集2024netflixopenconnectappliancefreebsdbmd, 衍生组采集22024netflixopenconnectappliancefreebsdmd
- 日志题名: 
- 内容头部: Netflix and FreeBSD: Observations from ~3 Years of Running Head Jonathan Looney BSDCan 2019 NETFLIX AND FREEBSD BSDCan 2019 Open Connect Open Connect is Netflix’s CDN. It is global, efficient, and purpose-built for distributing Netflix’s content. NETFLIX AND FREEBSD BSDCan 2019 The Open Connect Appliance The OCA is the workhorse of the Open Connect network. The OCA almost exclusively runs open-source software. NETFLIX AND FREEBSD BSDCan 2019 40Gb/s Storage Appliance with 248TB storage (2RU form factor) Open Connect Traffic NETFLIX AND FREEBSD BSDCan 2019 Video Apps Video Apps Video Apps Video Apps Open Connect Netflix OCA Workload NETFLIX AND FREEBSD BSDCan 2019 CPU RAM Disks Plain-text Data

## [132] 2019_FreeBSD_社区论文与演讲_208208_Quentin_Garnier_Virtualization_of_BSD_Using_t.pdf
- 大小: 1141KB  类型: .pdf  页数: 25
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019bsdcangarniervirtualizationofbsdusingtheqnxhypervisorpaper, 2019bsdcangarniervirtualizationofbsdusingtheqnxhypervisorpaperpdf, garniervirtualizationofbsdusingtheqnxhypervisorpaper
- 日志题名: 
- 内容头部: © 2018 BlackBerry. All Rights Reserved. 1 © 2019 BlackBerry. All Rights Reserved. 1 Confidential – Internal Use Only Virtualization of BSD Using the QNX Hypervisor Quentin Garnier Senior Kernel Developer qgarnier@blackberry.com May 2019 © 2018 BlackBerry. All Rights Reserved. 2 © 2019 BlackBerry. All Rights Reserved. 2 Confidential – Internal Use Only © 2018 BlackBerry. All Rights Reserved. 2 2 • The virtualization environment: QNX Neutrino and QNX Hypervisor • Goals for the exercise • Stories from the trenches Agenda © 2018 BlackBerry. All Rights Reserved. 3 © 2019 BlackBerry. All Rights Reserved. 3 Confidential – Internal Use Only QNX Host Environment © 2018 BlackBerry. All Rights Reserved

## [133] 2019_FreeBSD_社区论文与演讲_211211_Philip_Paeps_The_ZFS_filesystem_CCOSCUP_2019_.pdf
- 大小: 1339KB  类型: .pdf  页数: 36
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: The ZFS filesystem COSCUP 2019 Philip Paeps —Trouble 麻煩 18 August 2019 Taipei, Taiwan FreeBSDis an open source Unix-like operating systemdescended from patches developed at the University of California, Berkeley in the 1970s. The FreeBSD Projectis an active open source communitysince 1993 with hundreds of committers and thousands of contributors around the world. The FreeBSD Foundationis a non-profit organisationregistered in Colorado, USA in 2001 dedicated to supporting the FreeBSD Project, its development and its community. What is FreeBSD? Who uses FreeBSD? Community •Friendly and professional •Many active contributors and committers for 10+ and even 20+ years (and longer) Mentoring •Buil

## [134] 2019_FreeBSD_社区论文与演讲_215215_Brooks_Davis_CheriABI_Hardware_enforced_memor.pdf
- 大小: 491KB  类型: .pdf  页数: 29
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019eurobsdcondavischeriabihardwareenforcedmemorysafetyforfreebsdslides, 2019eurobsdcondavischeriabihardwareenforcedmemorysafetyforfreebsdslidespdf, davischeriabihardwareenforcedmemorysafetyforfreebsdslides
- 日志题名: 
- 内容头部: CheriABI Hardware enforced memory safety for FreeBSD Brooks Davis, Robert N. M. Watson, Alexander Richardson, Peter G. Neumann, Simon W . Moore, John Baldwin, David Chisnall, James Clarke, Nathaniel Wesley Filardo, KhilanGudka, Alexandre Joannou, Ben Laurie, A. Theodore Markettos, J. Edward Maste, Alfredo Mazzinghi, Edward Napierala, Robert Norton, Michael Roe, Peter Sewell, Stacey Son, Jonathan Woodruff SRI International, University of Cambridge, Microsoft Research, Google, Inc 1 Approved for public release; distribution is unlimited. This work was supported by the Defense Advanced Research Projects Agency (DARPA) and the Air Force Research Laboratory (AFRL), under contracts FA8750-10-C-023

## [135] 2019_FreeBSD_社区论文与演讲_227227_Dan_Langille_ZFS_for_newbies_CEuroBSDcon_2019.pdf
- 大小: 39389KB  类型: .pdf  页数: 52
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: ZFS For Newbies Dan Langille EuroBSDCon 2019 Lillehammer @dlangille https://dan.langille.org/ Disclaimer •This is ZFS for newbies •grossly simpliﬁed •stuﬀ omitted •options skipped •because newbies…. What? •a short history of the origins •an overview of how ZFS works •replacing a failed drive •why you don’t want a RAID card •scalability •data integrity (detection of ﬁle corruption) •why you’ll love snapshots •sending of ﬁlesystems to remote servers •creating a mirror •how to create a ZFS array with multiple drives which can lose up to 3 drives without loss of data. •mounting datasets anywhere in other datasets •using zfs to save your current install before upgrading it •simple recommendations

## [136] 2019_FreeBSD_社区论文与演讲_231231_Jeremy_Bennett_Embedded_FreeBSD_on_a_five-cor.pdf
- 大小: 2384KB  类型: .pdf  页数: 19
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: Embedded FreeBSD on a five-core RISC-V processor using LLVM How hard can it be? Jeremy Bennett Copyright © 2019 Embecosm. Freely available under a Creative Commons license. Target Hardware RV64IMACRV64IMAC RV64IMAC RV64IMAC Memory RV32IMAC Memory Prototype Platform: HiFive Unleashed HiFive Unleashed Schematic Image copyright © SiFive Inc Pre-prototype: QEMU FreeBSD Berkeley Boot Loader (BBL) Kernel Arch specific kernel code Device tree User land ● Build user land – create RAM disc ● Build kernel – supply RAM disc details ● Build BBL wrapper – adds device tree ● Result: image to load Compiler Tool Chain ● Clang/LLVM ● GNU binutils ● GNU Debugger – including remote debugger ● C libraries from 

## [137] 2019_FreeBSD_社区论文与演讲_234234_Luca_Pizzamiglio_How_to_build_a_FreeBSD_CICD_.pdf
- 大小: 165KB  类型: .pdf  页数: 14
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: How to build a FreeBSD CI/CD environment based on pot containers Luca Pizzamiglio pizzamig@FreeBSD.org FOSDEM 2019 2019-02-02How to build a FreeBSD CI/CD environment whoami(1) ● Luca Pizzamiglio aka pizzamig@ ● FreeBSD enthusiast ● Port committer since August 2017 ● Building packages at trivago 2019-02-02How to build a FreeBSD CI/CD environment Motivations CI/CD is a well established best practices in any modern software development process Growing interest on build/test software on FreeBSD Improve portability Provide FreeBSD support Provide artifacts for FreeBSD Lack of FreeBSD support on all major CI systems Exception for Cirrus CI VM based support to FreeBSD 2019-02-02How to build a FreeB

## [138] 2019_FreeBSD_社区论文与演讲_235235_Thomas_Barabosch_KLEAK_-_Practical_Kernel_Mem.pdf
- 大小: 1297KB  类型: .pdf  页数: 44
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019fosdembaraboschkleakpaper, 2019fosdembaraboschkleakpaperpdf, baraboschkleakpaper
- 日志题名: 
- 内容头部: © Fraunhofer KLEAK Practical Kernel Memory Disclosure Detection Thomas Barabosch Fraunhofer FKIE thomas.barabosch@fkie.fraunhofer.de Maxime Villard NetBSD m00nbsd.net © Fraunhofer System Call - Recap User Space Kernel Space calls syscall X Program Syscall Dispatcher Syscall X Syscall returns to user Program continues normal execution additional preparation © Fraunhofer Kernel/User Space Data Exchange - copyin trust boundary User Space Kernel Space kernel S T A C K heapprogram heap copyin  User space programs can not directly write to kernel space  It points the kernel to a buffer, the kernel fetches this data  copyin, copyinstr, … © Fraunhofer Kernel/User Space Data Exchange - copyout tru

## [139] 2019_FreeBSD_社区论文与演讲_237237_Jonathan_Looney_Netflix_and_FreeBSD_Using_Ope.pdf
- 大小: 954KB  类型: .pdf  页数: 25
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: netflixopenconnectappliancefreebsdbased, 衍生组采集2024netflixopenconnectappliancefreebsdbmd, 衍生组采集22024netflixopenconnectappliancefreebsdmd
- 日志题名: 
- 内容头部: Netflix and FreeBSD: Using Open Source to Deliver Streaming Video Jonathan Looney FOSDEM 2019 NETFLIX AND FREEBSD FOSDEM 2019 Open Connect Open Connect is Netflix’s CDN. It is global, efficient, and purpose-built for distributing Netflix’s content. NETFLIX AND FREEBSD FOSDEM 2019 The Open Connect Appliance The OCA is the “backbone” of the Open Connect network. The OCA almost exclusively runs open-source software. NETFLIX AND FREEBSD FOSDEM 2019 40Gb/s Storage Appliance with 248TB storage (2RU form factor) Open Connect Traffic NETFLIX AND FREEBSD FOSDEM 2019 Video Apps Video Apps Video Apps Video Apps Open Connect Netflix OCA Workload NETFLIX AND FREEBSD FOSDEM 2019 CPU RAM Disks Plain-text D

## [140] 2019_FreeBSD_社区论文与演讲_240240_Allan_Jude_ZFS_Powered_Magic_Upgrades_CFOSDEM.pdf
- 大小: 378KB  类型: .pdf  页数: 24
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2026freebsdfreebsdcoreteamarchitecturesupporttierdefinitionsebov5, 2026freebsdfreebsdcoreteamarchitecturesupporttierdefinitionsebov5html, freebsdcoreteamelections
- 日志题名: 
- 内容头部: ZFS Powered Magic Upgrades Using boot environments for atomic in-place upgrades Summary & Introductions Allan Jude FreeBSD Core Team OpenZFS Developer Klara Inc. FreeBSD Professional Services and Support Covered in this presentation What is a boot environment? How do they work? Creating and managing boot environments Deploying boot environments remotely Doing it even better next time What we had before: NanoBSD ● Divides the disk into 2 partitions (firmware images) ● Install the stock image to both ● At upgrade time, overwrite the inactive image ● Boot-once to the newer image. If it fails, or is otherwise unserviceable, reboot to good image ● If the new image is accepted, configure it as the

## [141] 2019_FreeBSD_社区论文与演讲_247247_John_Baldwin_In-Kernel_TLS_Framing_and_Encryp.pdf
- 大小: 912KB  类型: .pdf  页数: 35
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2020bsdcanbaldwinkerneltlsinfreebsdpaper, 2020bsdcanbaldwinkerneltlsinfreebsdpaperpdf, baldwinkerneltlsinfreebsdpaper
- 日志题名: 
- 内容头部: In-Kernel TLS Framing and Encryp6on for FreeBSD John Baldwin vBSDCon September 6, 2019 Overview • Mo6va6on • Kernel TLS • SoJware TLS • NIC TLS • Numbers Why KTLS? • The story of KTLS is really a repeat of the story of sendfile(2) • So let’s start with that… Pre-sendﬁle(2) HTTP/FTP Workﬂow Kernel I/O Devices Disk NIC Pages Pages Pages Pages Pages Pages Userland Pages Pages Pages Request DMA Copy read(2) write(2) Request DMA Copy Pre-sendﬁle(2) HTTP/FTP Workﬂow Kernel I/O Devices Disk NIC Pages Pages Pages Pages Pages Pages Userland Pages Pages Pages Request DMA Copy read(2) write(2) Request DMA Copy sendﬁle(2) HTTP/FTP Workﬂow Kernel I/O Devices Disk NIC Pages Pages Pages Userland Request DM

## [142] 2019_FreeBSD_社区论文与演讲_251251_Allan_Jude_OpenZFS_Best_Filesystem_for_every_.pdf
- 大小: 715KB  类型: .pdf  页数: 30
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2026freebsdfreebsdcoreteamarchitecturesupporttierdefinitionsebov5, 2026freebsdfreebsdcoreteamarchitecturesupporttierdefinitionsebov5html, freebsdcoreteamelections
- 日志题名: 
- 内容头部: OpenZFS The Best FileSystem for Every OS Summary & Introductions Allan Jude FreeBSD Core Team OpenZFS Developer Klara Inc. FreeBSD Professional Services and Support Covered in this presentation What is ZFS? Why all the excitement? What is OpenZFS? How do I Join? What new features are in OpenZFS? What does the future hold for OpenZFS? What is ZFS? ● ZFS is a filesystem with a built in volume manager (RAID) ● Space from the pool of disks is thin-provisioned to multiple filesystems or block volumes (zvols) ● All data and metadata is checksummed ● Optional transparent compression (LZ4, GZIP , soon: ZSTD) ● Copy-on-Write with snapshots and clones ● Each filesystem is tunable with properties What 

## [143] 2020_CVE-_-8794_EBOL.md
- 大小: 0KB  类型: .md  页数: None
- 来源URL: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8794
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: -8794 [EB/OL]. <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8794>
- 内容头部: --- title: "-8794_EBOL" source_url: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8794 download_date: 2026-09-07 --- # -8794_EBOL 来源: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8794 Common vulnerabilities and Exposures (CVE) We're sorry but the CVE Website doesn't work properly without JavaScript enabled. Please enable it to continue.

## [144] 2020_Torvalds_L_2020-01-06_Real_World_Tech_Forum_Post_EBOL_archived_via_Wayback_Mach.md
- 大小: 162KB  类型: .md  页数: None
- 来源URL: https://www.realworldtech.com/forum/?threadid=189311
- DKC对齐: DKC-1919
- 重复探针: 无
- 日志题名: L. (2020-01-06). Real World Tech Forum Post [EB/OL] (archived via Wayback Machine). 获取路径：<https://ww
- 内容头部: --- title: "L_2020-01-06_Real_World_Tech_Forum_Post_EBOL_archived_via_Wayback_Mach" source_url: https://www.realworldtech.com/forum/?threadid=189311 download_date: 2026-09-07 --- # L_2020-01-06_Real_World_Tech_Forum_Post_EBOL_archived_via_Wayback_Mach 来源: https://www.realworldtech.com/forum/?threadid=189311 Real World Technologies - Forums - Thread: A64FX front end width Real World Tech Login Cloud Mobile Graphics Chips Software CPUs GPUs Semiconductors Strategy Forums A64FX front end width By: Michael S (already5chosen.delete@this.yahoo.com), 2019-12-16 09:10 UTC Room: Moderated Discussions Chester (lamchester.delete@this.gmail.com) on December 15, 2019 5:16 pm wrote: &gt; &gt; No, it is mu

## [145] 2021_CCF_简报2021_年_6_月11_位学者获_ACM_四大技术奖项httpswwwccforgcnACM_News2021-06-16730235.md
- 大小: 0KB  类型: .md  页数: None
- 来源URL: https://www.ccf.org.cn/ACM_News/2021-06-16/730235.shtml
- DKC对齐: DKC-1354
- 重复探针: 无
- 日志题名: 简报：2021 年 6 月——11 位学者获 ACM 四大技术奖项（<https://www.ccf.org.cn/ACM_News/2021-06-16/730235.shtml）
- 内容头部: --- title: "简报2021_年_6_月11_位学者获_ACM_四大技术奖项httpswwwccforgcnACM_News2021-06-16730235" source_url: https://www.ccf.org.cn/ACM_News/2021-06-16/730235.shtml download_date: 2026-09-07 --- # 简报2021_年_6_月11_位学者获_ACM_四大技术奖项httpswwwccforgcnACM_News2021-06-16730235 来源: https://www.ccf.org.cn/ACM_News/2021-06-16/730235.shtml appkey: "CF_APP_WAF", // 应用标识var AC_Opt = {userUserId: requestInfo.userUserId TraceID: 276077fc17887837936748595ec43e --> var requestInfo = {"data":"","region":"cn","sceneId":"19x5u7lo","token":"5c7ab1c712c9ae797434e8b24a27d6fd","traceid":"276077fc17887837936748595ec43e","type":"GET","userId":"HpadJlQnz2zSKcSmjXBaqQvjYUvP4jMJIk/ZwGNDNiM=","userUserId":"VvMFdD6GTlSOAtRkGsgsgs1yUrUi1/

## [146] 2021_Chuck_Tuffli2021FreeBSD_社区论文FP-2020-021_How_an_Australian_IaaS_use.pdf
- 大小: 1368KB  类型: .pdf  页数: 37
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2020linuxconfauschadehowanaustralianiaasusesfreebsdpaper, 2020linuxconfauschadehowanaustralianiaasusesfreebsdpaperpdf, schadehowanaustralianiaasusesfreebsdpaper
- 日志题名: 
- 内容头部: FreeBSD Miniconf @ Linux.conf.au 2020 How an Australian IaaS uses FreeBSD Ruben Schade FreeBSD Miniconf at Linux.conf.au FreeBSD Miniconf @ Linux.conf.au 2020 Dedication ● NSW Rural Fire Service ● https://www.rfs.nsw.gov.au/volunteer/ support-your-local-brigade FreeBSD Miniconf @ Linux.conf.au 2020 Digression #1: Presentation Style FreeBSD Miniconf @ Linux.conf.au 2020 Agenda ● My history with FreeBSD, and introducing OrionVM ● Cloud and VPC storage with FreeBSD, OpenZFS and FreeNAS ● TidalScale for Multi-TiB memory deployments ● Securing cloud and bare metal through PFSense and FreeBSD ● Resources and Thanks ● Q&A FreeBSD Miniconf @ Linux.conf.au 2020 % whoami ● Ruben Schade Solutions Archi

## [147] 2021_FreeBSD_社区论文FP-2021-002_An_Overview_of_Scheduling_in_the_FreeBSD_Ker.pdf
- 大小: 56KB  类型: .pdf  页数: 21
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2021eurobsdconmckusickoverviewschedulingfreebsdslides, 2021eurobsdconmckusickoverviewschedulingfreebsdslidespdf, mckusickoverviewschedulingfreebsdslides
- 日志题名: 
- 内容头部: An Overview of Scheduling in the FreeBSD Kernel Brought to you by Dr.M arshall Kirk McKusick EuroBSD Conference 2021 19 September 2021 Gushaus Campus of Vienna’sT echnical University Vienna, Austria Copyright 2021 Marshall Kirk McKusick. All Rights Reserved. 1 Scheduling Classes Threads are divided into ﬁv es cheduling classes Priority Class Thread type 0–4 7 ITHD Bottom-half kernel (interrupt) 48 – 79 REALTIME Real-time user 80 – 119 KERN Top-half kernel 120 – 223 TIMESHARE Time-sharing user 224 – 255 IDLE Idle user •H igher values of priority imply lower levels of service •I THD and KERN classes are managed by the kernel •R EALTIME and IDLE classes are managed by user processes •T IMESHARE

## [148] 2021_FreeBSD_社区论文FP-2021-003_FreeBSD_Aarch64_Virtual_Machines_are_BoringV.pdf
- 大小: 11647KB  类型: .pdf  页数: 18
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2019asiabsdconcarabasmihaibhyveimprovementstovirtualmachinestatesaveandrestorepaperpdf, 2019mihaibhyveimprovementstovirtualmachinestatesaveandrestoreen, carabasmihaibhyveimprovementstovirtualmachinestatesaveandrestorepaper
- 日志题名: 
- 内容头部: ARM / Aarch64 Virtualization is BORING! By: Vincent Milum Jr Darkain.com discord.gg/n2wshsy The FreeBSD Project on Discord https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=258550 1 2 4 8 12 16 Ra spberry Pi (VM) 4106 2576 2002 Ra spberry Pi (HW ) 4446 2687 1837 Ho neyComb (VM) 3048 1633 870 512 430 373 Ho neyComb (HW) 2866 1487 790 438 319 270 MacBook Air (VM) 553 316 202 174 0 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 Seconds make buildkernel–j

## [149] 2021_FreeBSD_社区论文FP-2021-004_logstor_A_Log-structured_user_level_GEOM_lay.pdf
- 大小: 145KB  类型: .pdf  页数: 17
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: logstor: A Log-structured Use-level GEOM Layer Wuyang Chung wy-chung@outlook.com https://github.com/wy-chung/logstor/tree/ggatelog/docs EuroBSDCon 2021 Outline ● Introduction – GEOM – logstor ● Implementation ● Performance ● Future Work Introduction - GEOM DISK MBR DEV BSD DEV DEV DEV DEV ad0s1a ad0s1b ad0s1 ad0s2 ad0 logstor glogstor DEV Introduction - logstor ● Use the idea from log-structured file system – Data written are appended to the end of the log ● Can transform random write to sequential write – Implement a simple file system to store the forward map information – Also need a inverse map information for garbage collection ● Stored at the end of every segment – The algorithm used f

## [150] 2021_FreeBSD_社区论文FP-2021-005_portmgr_Behind_the_ScenesRené_Ladan2021.pdf
- 大小: 100KB  类型: .pdf  页数: 17
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2021eurobsdconladanportmgrbehindthescenespaper, 2021eurobsdconladanportmgrbehindthescenespaperpdf, ladanportmgrbehindthescenespaper
- 日志题名: 
- 内容头部: Portmgr — Behind the Scenes Ren´ e Ladan EuroBSDCon 2021-09-19 Ren´ e Ladan Portmgr — Behind the Scenes Overview What is portmgr? (brieﬂy) History Technical People Closing Ren´ e Ladan Portmgr — Behind the Scenes What is portmgr? YES NO The Ports Management Team is responsible for overseeing the overall direction of the Ports Tree, building packages, and personnel matters portmgr owns all of Mk/ portmgr is intentionally evil portmgr sets policies unilaterally Ren´ e Ladan Portmgr — Behind the Scenes History → Origins Twentieth anniversary of the FreeBSD Ports Tree (2014): https://www.youtube.com/watch?v=LiFq5D-zmBs Ren´ e Ladan Portmgr — Behind the Scenes History → Why portmgr? Information f

