# 复核摘要 第7/8部分（文件 151-175）

## [151] 2021_FreeBSD_社区论文FP-2021-006_Routing_Stack_Changes_in_FreeBSD_13Alexander.pdf
- 大小: 857KB  类型: .pdf  页数: 31
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: ALEXANDER CHERNIKOV < MELIFARO@FREEBSD.ORG > Routing in FreeBSD 13 rethinking ALEXANDER CHERNIKOV < MELIFARO@FREEBSD.ORG > •Motivation •Nexthops & Nexthop groups •fib(9) KPI •Lookup algorithms framework •Algorithms overview •Performance •Next steps Agenda ALEXANDER CHERNIKOV < MELIFARO@FREEBSD.ORG > •Working multipath •Improving control plane performance under traffic load •Desire for the new high-performance lookup algos •Build the base for other new features Motivation ALEXANDER CHERNIKOV < MELIFARO@FREEBSD.ORG > •Lack of isolation •Tightly coupled with almost all other network parts •struct rtentry widely used by external callers (~100 places) •Extremely hard to change Problems with routi

## [152] 2021_FreeBSD_社区论文FP-2021-007_Serving_Netflix_Video_at_400Gbs_on_FreeBSDDr.pdf
- 大小: 1019KB  类型: .pdf  页数: 97
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: Serving Netﬂix Video at 400Gb/s on FreeBSD Drew Gallatin EuroBSDCon 2021 Outline: ● Motivation ● Description of production platform ● Description of workload ● To NUMA or not to NUMA? ● Inline Hardware (NIC) kTLS ● Alternate platforms Motivation: ● Since 2020, Netflix has been able to serve 200Gb/s of TLS encrypted video traffic from a single server. ● How can we serve ~400Gb/s of video from the same servers? Netflix Video Serving Workload ● FreeBSD-current ● NGINX web server ● Video served via sendfile(2) and encrypted using software kTLS Netflix Video Serving Hardware ● AMD EPYC 7502P (“Rome”) ○ 32 cores @ 2.5GHz ○ 256GB DDR4-3200 ■ 8 channels ■ ~150GB/s mem bw ● Or ~1.2Tb/s in networking 

## [153] 2021_FreeBSD_社区论文FP-2021-010_FreeBSD_networking_in_virtualised_hosting_20.pdf
- 大小: 1813KB  类型: .pdf  页数: 27
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2021eurobsdconhausenvirtualisedhostingpaper, 2021eurobsdconhausenvirtualisedhostingpaperpdf, hausenvirtualisedhostingpaper
- 日志题名: 
- 内容头部: FreeBSD Networking in Virtualised Hosting Patrick M. Hausen EuroBSDCon 2021, not Vienna Agenda •Introduction •Our Current Architecture •Going IPv6 Only •Layer 2 Challenges •What's Wrong with Ethernet? About Me •Working in IT since 1986 •Minix 1.1 since 1989 •FreeBSD since 1993 •In charge of network and data centre operations at punkt.de About Our Team •mOps – the Magnificent Operators •3 (originally) operators •1 (originally) developer About punkt.de •Founded in 1996 •Started as an ISP •Today: Hosting and development of web applications •Roughly 100 Servers •RIPE Member •DENIC Member •4 development, 1 operations team VIMAGE/VNET •Introduces the epair(4) virtual interface •Essentially a virtu

## [154] 2021_FreeBSD_社区论文与演讲_278278_Lutz_Donnerhacke_A_Carrier-Grade_L2BSA_Gatewa.pdf
- 大小: 851KB  类型: .pdf  页数: 19
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2021eurobsdcondonnerhackecarrierl2bsanetgraphslides, 2021eurobsdcondonnerhackecarrierl2bsanetgraphslidespdf, donnerhackecarrierl2bsanetgraphslides
- 日志题名: 
- 内容头部: A Carrier-Grade L2BSA Gateway with Netgraph Lutz Donnerhacke IKS Service GmbH Personal background • Grown up with a C64 in Eastern Germany • Short excurse to MSDOS and Win3.11 • Switched to Linux in 1992 • Individual Network e.V. in Germany • grassroot Internet for ordinary people • Build regional ISP in 1996 • infrastructure provider of two regional Broadband-ISPs in Thuringia • Switch to FreeBSD in 2013 • Replace commercial LNS by netgraph/MPD Broadband in Germany • 1983 – CDU (German conservatives) choose copper over fiber • Probably due to corruption via the minister Schwarz-Schilling • 1995 – CDU privatization created Deutsche Telekom • Got the whole cable network as gift, hence a (copp

## [155] 2021_FreeBSD_社区论文与演讲_287287_Michael_Dexter_Chuck_Tuffli_smart8_Update_A_P.pdf
- 大小: 903KB  类型: .pdf  页数: 35
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: bsdtalk066interviewwithmichaeldexteraboutsysjail, bsdtalk128sysjailrevisitedwithmichaeldexter, bsdtalk175bsdfundwithmichaeldexter
- 日志题名: 
- 内容头部: smart(8) Update A Permissively-Licensed Alternative to smartctl(8) Chuck Tuﬄi and Michael Dexter EuroBSDcon 2021 smart(8) Genesis ● “Let’s do to smartctl what mandoc did to groﬀ” ● Formally proposed as diskctl(8) in a 2016 AsiaBSDCon paper by Michael ● Inspired by OpenBSD/NetBSD atactl(8), hence the name ● First prototyped (poorly) with camcontrol camcontrol cmd ada0 -a "B0 D0 00 4F C2 00 00 00 00 00 00 00" \ -i 512 - | od -tx1 0000000 01 00 05 33 00 64 64 00 00 00 00 00 00 00 09 32 0000020 00 63 63 63 02 00 00 00 00 00 0c 32 00 63 63 49... smart(8) Design Goals ● “The Plural of Regex is Regrets” – smartctl output is neither human nor machine-readable, though it now supports JSON output ● At

## [156] 2021_FreeBSD_社区论文与演讲_288288_Tom_Jones_Use_Dummynet_to_explore_space_QUIC_.pdf
- 大小: 27281KB  类型: .pdf  页数: 56
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2021eurobsdconjonesdummynetspacequicslides, 2021eurobsdconjonesdummynetspacequicslidespdf, jonesdummynetspacequicslides
- 日志题名: 
- 内容头部: 04/10/2021, 12:00Use Dummynet to explore space, QUIC! - Tom Jones Page 1 of 56http://localhost:8000/output.html#1 Use Dummynet to explore space, QUIC! Tom Jones tj@enoti.me 1 / 56 04/10/2021, 12:00Use Dummynet to explore space, QUIC! - Tom Jones Page 2 of 56http://localhost:8000/output.html#1 2 / 56 04/10/2021, 12:00Use Dummynet to explore space, QUIC! - Tom Jones Page 3 of 56http://localhost:8000/output.html#1 Three altitudes of orbit are used for satellite networks LEO (ISS, hubble, starlink, iridiumn and others) MEO (GPS, O3B ) GEO (all the vsat services you can buy today) 3 / 56 04/10/2021, 12:00Use Dummynet to explore space, QUIC! - Tom Jones Page 4 of 56http://localhost:8000/output.htm

## [157] 2022_OpenBSD_softraid4_手册页_EBOL_AFreeBSD_社区论文FP-2022-001_Refining_FreeBSD.pdf
- 大小: 202KB  类型: .pdf  页数: 25
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 2022bsdcanbaldwinrefiningfreebsdskernelcryptoframeworkslides, 2022bsdcanbaldwinrefiningfreebsdskernelcryptoframeworkslidespdf, baldwinrefiningfreebsdskernelcryptoframeworkslides
- 日志题名: 
- 内容头部: Refining FreeBSD's Kernel Crypto Framework John Baldwin BSDCan June 2022 Overview •What is the kernel crypto framework? •Brief History •Changes in FreeBSD 13 •Future Work What is OCF? •OCF (formerly OpenBSD Crypto Framework, now Open Crypto Framework) is an interface around crypto drivers •Supports symmetric operations (encryption, authentication) •Aimed at supporting in-kernel uses (IPsec, KTLS, GELI) •Does not include “library” APIs for direct software crypto –Software ”drivers” sometimes use these APIs OCF History •OCF originally ported from OpenBSD to FreeBSD 5.0 by Sam Leffler •Initialversionsupported IPsec and userland /dev/cryptointerface •Supported asymmetric operations useful for pu

## [158] 2023_Corbet_J_Development_statistics_for_the_65_kernel_EBOL_LWN_2023-08-28_访问日期_20.md
- 大小: 14KB  类型: .md  页数: None
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: --- title: "J_Development_statistics_for_the_65_kernel_EBOL_LWN_2023-08-28_访问日期_20" source_url: https://lwn.net/Articles/941675/ download_date: 2026-09-07 --- # J_Development_statistics_for_the_65_kernel_EBOL_LWN_2023-08-28_访问日期_20 来源: https://lwn.net/Articles/941675/ Development statistics for the 6.5 kernel [LWN.net] LWN .net News from the source Content Weekly Edition Archives Search Kernel Security Events calendar Unread comments LWN FAQ Write for us Edition Return to the Front page User: Password: | | Log in / Subscribe / Register Development statistics for the 6.5 kernel Please consider subscribing to LWN Subscriptions are the lifeblood of LWN.net. If you appreciate this content and wo

## [159] 2023_Stanford_Existentialism.md
- 大小: 100KB  类型: .md  页数: None
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: --- title: "Existentialism" source_url: https://plato.stanford.edu/entries/existentialism/ download_date: 2026-09-07 --- # Existentialism 来源: https://plato.stanford.edu/entries/existentialism/ --> Existentialism (Stanford Encyclopedia of Philosophy) Stanford Encyclopedia of Philosophy Menu Browse Table of Contents What's New Random Entry Chronological Archives About Editorial Information About the SEP Editorial Board How to Cite the SEP Special Characters Advanced Tools Contact Support SEP Support the SEP PDFs for SEP Friends Make a Donation SEPIA for Libraries Entry Navigation Entry Contents Bibliography Academic Tools

## [160] 2024_CVE-_-6387_EBOL.md
- 大小: 0KB  类型: .md  页数: None
- 来源URL: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: -6387 [EB/OL]. <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387>
- 内容头部: --- title: "-6387_EBOL" source_url: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387 download_date: 2026-09-07 --- # -6387_EBOL 来源: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387 Common vulnerabilities and Exposures (CVE) We're sorry but the CVE Website doesn't work properly without JavaScript enabled. Please enable it to continue.

## [161] 2024_Freund_A_2024-03-29_backdoor_in_upstream_xzliblzma_leading_to_ssh_server_comp.md
- 大小: 14KB  类型: .md  页数: None
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: --- title: "A_2024-03-29_backdoor_in_upstream_xzliblzma_leading_to_ssh_server_comp" source_url: https://www.openwall.com/lists/oss-security/2024/03/29/4 download_date: 2026-09-07 --- # A_2024-03-29_backdoor_in_upstream_xzliblzma_leading_to_ssh_server_comp 来源: https://www.openwall.com/lists/oss-security/2024/03/29/4 oss-security - backdoor in upstream xz/liblzma leading to ssh server compromise Products Openwall GNU/*/Linux &nbsp; server OS Linux Kernel Runtime Guard John the Ripper &nbsp; password cracker Free &amp; Open Source for any platform in the cloud Pro for Linux Pro for macOS Wordlists &nbsp; for password cracking passwdqc &nbsp; policy enforcement Free &amp; Open Source for Unix Pr

## [162] 2024_LWNnet_FreeBSD_considers_Rust_in_the_base_system_EBOL_2024-08-192026-07-19.md
- 大小: 130KB  类型: .md  页数: None
- 来源URL: https://lwn.net/Articles/985210/
- DKC对齐: DKC-2304
- 重复探针: 无
- 日志题名: FreeBSD considers Rust in the base system [EB/OL]. (2024-08-19)[2026-07-19]. <https://lwn.net/Articl
- 内容头部: --- title: "FreeBSD_considers_Rust_in_the_base_system_EBOL_2024-08-192026-07-19" source_url: https://lwn.net/Articles/985210/ download_date: 2026-09-07 --- # FreeBSD_considers_Rust_in_the_base_system_EBOL_2024-08-192026-07-19 来源: https://lwn.net/Articles/985210/ FreeBSD considers Rust in the base system [LWN.net] LWN .net News from the source Content Weekly Edition Archives Search Kernel Security Events calendar Unread comments LWN FAQ Write for us Edition Return to the Front page User: Password: | | Log in / Subscribe / Register FreeBSD considers Rust in the base system Did you know...? LWN.net is a subscriber-supported publication; we rely on subscribers to keep the entire operation going.

## [163] 2025_Apple_Inc_macOS_Tahoe_26_Security_Content_EBOL_2025-09-15.md
- 大小: 83KB  类型: .md  页数: None
- 来源URL: https://support.apple.com/en-us/125110
- DKC对齐: DKC-0135
- 重复探针: 无
- 日志题名: Inc. macOS Tahoe 26 Security Content [EB/OL]. (2025-09-15). <https://support.apple.com/en-us/125110>
- 内容头部: --- title: "Inc_macOS_Tahoe_26_Security_Content_EBOL_2025-09-15" source_url: https://support.apple.com/en-us/125110 download_date: 2026-09-07 --- # Inc_macOS_Tahoe_26_Security_Content_EBOL_2025-09-15 来源: https://support.apple.com/en-us/125110  About the security content of macOS Tahoe 26 - Apple Support Apple Store Mac iPad iPhone Watch Vision AirPods TV &amp; Home Entertainment Accessories Support 0 + About the security content of macOS Tahoe 26 This document describes the security content of macOS Tahoe 26. About Apple security updates For our customers' protection, Apple doesn't disclose, discuss, or confirm security issues until an investigation

## [164] 2025_DragonFly_BSD_Project_Homepage_EBOL_last_edited_2025-10-03.md
- 大小: 6KB  类型: .md  页数: None
- 来源URL: https://www.dragonflybsd.org/
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: BSD Project. Homepage [EB/OL]. <https://www.dragonflybsd.org/> (last edited 2025-10-03)
- 内容头部: --- title: "BSD_Project_Homepage_EBOL_last_edited_2025-10-03" source_url: https://www.dragonflybsd.org/ download_date: 2026-09-07 --- # BSD_Project_Homepage_EBOL_last_edited_2025-10-03 来源: https://www.dragonflybsd.org/ DragonFlyBSD: DragonFly BSD DragonFly BSD Edit Page | RecentChanges | History | Preferences About History Features Performance Team Images Community Download Mirrors Documentation Mailing Lists Source Commercial Donations Bugs Security PGP Keys Exports Hammer DragonFly BSD DragonFly 6.4.2 released DragonFly version 6.4.2 is released. The 6.4 series has hardware support for type-2 hypervisors with NVMM, an amdgpu driver, the experimental ability to remote-mount HAMMER2 volumes,

## [165] 2025_FreeBSD_社区论文与演讲_326326_Christos_Margiolis_Vox_FreeBSD_How_sound4_wor.pdf
- 大小: 1163KB  类型: .pdf  页数: 23
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: Vox FreeBSD: How sound(4) works Christos Margiolis christos@FreeBSD.org June 14, 2025 BSDCan 2025 — Ottawa, Canada Who? ▶ FreeBSD committer. ▶ The guy who keeps churning out sound bugs. Contents ▶ How does sound travel from application to the real world (and vice versa)? ▶ Layers: userland,sound(4), device drivers. ▶ New improvements. ▶ FreeBSD for music and audio production? Userland proc0 proc1 proc2 /dev/dsp0 /dev/dsp1 sound(4) Driver Sound card Microphone Speakers Userland Interacts withsound(4)through the Open Sound System (OSS) API, using a few basic syscalls on/dev/dsp*and/dev/mixer* character devices: open(2) Open device, obviously... close(2) Close device. read(2) Record audio. writ

## [166] 2025_FreeBSD_社区论文与演讲_327327_Mateusz_Piotrowski_ZFS_Direct_IO_Benchmarking.pdf
- 大小: 25687KB  类型: .pdf  页数: 41
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: Mateusz Piotrowski Ottawa 2025-06-13 ZFS Direct IO Benchmarking Hey! My Name Is Mateusz Mateusz Piotrowski <0mp@FreeBSD.org Based in Berli FreeBSD user since 201 Committer since 2018 Mateusz Piotrowski Ottawa 2025-06-13 Ports rc(8) ZFS Benchmarking Areas of interest: Not holding direct IO wrong is a great first step to potential performance gains! IntroMateusz Piotrowski Ottawa 2025-06-13 I m p l e m e n t a t i o n 3 P i t f a l l s 2 Z F S 1 0 1 1 a gend aMa teusz Pio tro wsk i O tt a w a 2025-06-13 agendaMateusz Piotrowski Ottawa 2025-06-13 1Mateusz Piotrowski ZFS 101 Ottawa 2025-06-13 ZFS Architecture Overview Mateusz Piotrowski Ottawa 2025-06-13 What Is ZFS? Copy-on-write file syste Unl

## [167] 2025_FreeBSD_社区论文与演讲_328328_Olivier_Certner_Controlled_credentials_transi.pdf
- 大小: 379KB  类型: .pdf  页数: 61
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: Controlled credentials transitions without privileges: mac_do(4), mdo(1) and setcred(2) Olivier Certner Kumacom SARL Sponsored by The FreeBSD Foundation EuroBSDCon 2025 Prologue Involvement With FreeBSD Private Using FreeBSD since 2004 Using it everywhere I can Maintaining small private changes (ports, userland, kernel) Public Since ~20 years: Sporadic bug reports and mails on lists Since ~4 years: Gradual increase in involvement Maintaining a few ports Reporting bugs in base and submitting patches Since ~2 years: Working full time Contractor for the FreeBSD Foundation since 2023/09 Committer since ~1 year and a half ( olce@) Presented at AsiaBSDCon 2024, EuroBSDCon 2024, BSDCan 2025 Olivier

## [168] 2025_FreeBSD_社区论文与演讲_329329_Christos_Margiolis_Re-decentralizing_the_Inte.pdf
- 大小: 4627KB  类型: .pdf  页数: 54
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: [NEED_OCR] 扫描件/图片型PDF，文本层提取失败

## [169] 2025_MITRE_CVE-2025-14558_EBOL_2025-122026-07-19.md
- 大小: 0KB  类型: .md  页数: None
- 来源URL: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-14558
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: CVE-2025-14558 [EB/OL]. (2025-12)[2026-07-19]. <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2
- 内容头部: --- title: "CVE-2025-14558_EBOL_2025-122026-07-19" source_url: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-14558 download_date: 2026-09-07 --- # CVE-2025-14558_EBOL_2025-122026-07-19 来源: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-14558 Common vulnerabilities and Exposures (CVE) We're sorry but the CVE Website doesn't work properly without JavaScript enabled. Please enable it to continue.

## [170] 2025_September_27_2025EBOL_2026-08-15.md
- 大小: 0KB  类型: .md  页数: None
- 来源URL: https://www.youtube.com/watch?v=ZGmuZz5ETHs
- DKC对齐: 未对齐
- 重复探针: eurobsdconroomd2zagrebcroatiaseptember272025
- 日志题名: 27, 2025[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=ZGmuZz5ETHs>
- 内容头部: --- title: "27_2025EBOL_2026-08-15" source_url: https://www.youtube.com/watch?v=ZGmuZz5ETHs download_date: 2026-09-07 --- # 27_2025EBOL_2026-08-15 来源: https://www.youtube.com/watch?v=ZGmuZz5ETHs EuroBSDCon Room D2 Zagreb, Croatia; September 27, 2025 - YouTube About Press Copyright Contact us Creators Advertise Developers Terms Privacy Policy &amp; Safety How YouTube works Test new features &copy; 2026 Google LLC

## [171] 2026_Apple_Hypervisorframework_Documentation_EBOL_2026-07-19.md
- 大小: 0KB  类型: .md  页数: None
- 来源URL: https://developer.apple.com/documentation/hypervisor
- DKC对齐: DKC-1942
- 重复探针: 无
- 日志题名: Hypervisor.framework Documentation [EB/OL]. [2026-07-19]. <https://developer.apple.com/documentation
- 内容头部: --- title: "Hypervisorframework_Documentation_EBOL_2026-07-19" source_url: https://developer.apple.com/documentation/hypervisor download_date: 2026-09-07 --- # Hypervisorframework_Documentation_EBOL_2026-07-19 来源: https://developer.apple.com/documentation/hypervisor Hypervisor | Apple Developer Documentation This page requires JavaScript. Please turn on JavaScript in your browser and refresh the page to view its content. Automated tools and assistive tools: A Markdown version of the page content is available: View Markdown

## [172] 2026_Apple_Security_Releases_EBOL_2026-07-23_访问.md
- 大小: 40KB  类型: .md  页数: None
- 来源URL: https://support.apple.com/en-us/100100
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: Security Releases [EB/OL]. <https://support.apple.com/en-us/100100>, 2026-07-23 访问
- 内容头部: --- title: "Security_Releases_EBOL_2026-07-23_访问" source_url: https://support.apple.com/en-us/100100 download_date: 2026-09-07 --- # Security_Releases_EBOL_2026-07-23_访问 来源: https://support.apple.com/en-us/100100  Apple security releases - Apple Support Apple Store Mac iPad iPhone Watch Vision AirPods TV &amp; Home Entertainment Accessories Support 0 + Apple security releases This document lists security updates for Apple software. About Apple security releases For the protection of our customers, Apple doesn't disclose, discuss, or confirm security issues until an investigation has occurred and patches or releases are generally available. This document

## [173] 2026_Arabeyes_项目_EBOL_访问日期_2026-07-23.md
- 大小: 2KB  类型: .md  页数: None
- 来源URL: https://www.arabeyes.org/
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 项目 [EB/OL]. <https://www.arabeyes.org/> （访问日期 2026-07-23）
- 内容头部: --- title: "项目_EBOL_访问日期_2026-07-23" source_url: https://www.arabeyes.org/ download_date: 2026-09-07 --- # 项目_EBOL_访问日期_2026-07-23 来源: https://www.arabeyes.org/ ويكي عربآيز Anonymous Not logged in English Create account Log in ويكي عربآيز Search Main Page From ويكي عربآيز Namespaces Main Page Discussion More More Page actions Read View source History Arabeyes Arabeyes Wiki is a collaborative website. Anyone can freely browse and edit it. It provides a platform for projects and information related to Arabic support in free open source software. See ArabeyesTodo for a list of tasks to complete to improve Arabic support in open source software. Translation If you are the author of open source s

## [174] 2026_Associated_Students_of_the_University_of_California_About_accessed_2026-07-25.md
- 大小: 10KB  类型: .md  页数: None
- 来源URL: https://asuc.org/about/
- DKC对齐: DKC-1399
- 重复探针: 无
- 日志题名: Students of the University of California. About. <https://asuc.org/about/> (accessed 2026-07-25)
- 内容头部: --- title: "Students_of_the_University_of_California_About_accessed_2026-07-25" source_url: https://asuc.org/about/ download_date: 2026-09-07 --- # Students_of_the_University_of_California_About_accessed_2026-07-25 来源: https://asuc.org/about/ About | ASUC Press and Media Home Official Statements Home About Organization Chart History Constitution ASUC Bylaws Drive ASUC Central Drive Our Units Legislative Branch Intro to Bylaws Agendas Public Notice Senate Livestream Elected Officials Appointed Officials Judicial Council Elections Our Services Chartered Programs Commissions &#038; Committees Our Resources Finance &#038; Sponsorship Apply for Sponsorship 2027 ASUC Budget 2027 ASUC Space Allocat

## [175] 2026_FedRAMP_Marketplace_EBOL_2026-07-22_访问.md
- 大小: 3KB  类型: .md  页数: None
- 来源URL: 
- DKC对齐: 未对齐
- 重复探针: 无
- 日志题名: 
- 内容头部: --- title: "Marketplace_EBOL_2026-07-22_访问" source_url: https://www.fedramp.gov/ download_date: 2026-09-07 --- # Marketplace_EBOL_2026-07-22_访问 来源: https://www.fedramp.gov/ FedRAMP | FedRAMP.gov Skip to main content An official website of the United States government Here's how you know Here's how you know Menu Community &amp; Updates Expand menu Changelog Blog Events Community Updates Public Notices Requests For Comment Rules &amp; Requirements Expand menu Consolidated Rules for 2026 Legacy Documentation Reference FedRAMP 20x Marketplace Search Search Search Submit Icon FedRAMP Marketplace: Your Fast Track to FedRAMP Certified Cloud Solutions. The FedRAMP Marketplace is a searchable databas

