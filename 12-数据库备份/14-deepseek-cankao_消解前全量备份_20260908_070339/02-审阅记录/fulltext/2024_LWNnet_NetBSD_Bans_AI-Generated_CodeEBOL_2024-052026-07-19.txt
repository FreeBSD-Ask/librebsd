---
title: "NetBSD_Bans_AI-Generated_CodeEBOL_2024-052026-07-19"
source_url: https://lwn.net/
download_date: 2026-09-07
---

# NetBSD_Bans_AI-Generated_CodeEBOL_2024-052026-07-19

来源: https://lwn.net/

         

          Welcome to LWN.net [LWN.net] 

             LWN .net 
             News from the source  

           Content     Weekly Edition    Archives    Search    Kernel    Security    Events calendar    Unread comments       LWN FAQ    Write for us    

          User:     
		  Password:          |

             |

                 Log in   /
                 Subscribe   /
                 Register  

 Welcome to LWN.net 

       LWN.net is a reader-supported news site dedicated to producing the best
       coverage from within the Linux and free software development communities.
       See  the LWN FAQ  for more information, and
       please consider  subscribing  to gain full
       access and support our activities.

 [ $ ] Deterministic testing for multithreaded Python 

         [Development] Posted Sep 4, 2026 15:29 UTC (Fri) by jake 

        Python's support for multithreaded programs has improved considerably over
the last few years with the advent of the  "free-threaded" version of the language .  But
testing multithreaded programs is notoriously difficult, because the
underlying host system determines the thread-execution ordering, which adds
an element of non-determinism.  At PyCon US, Larry Hastings gave a talk ( YouTube video )
about his  blanket  project,
which is meant to provide mechanisms for deterministic testing of
multithreaded Python code.

         Full Story  ( comments: 3 )

 [ $ ] Recent work in memory tiering 

         [Kernel] Posted Sep 3, 2026 14:11 UTC (Thu) by corbet 

        Tiered-memory systems are built with multiple types of memory, each of
which has different performance characteristics.  In addition to the usual
DRAM, a tiered system might also provide faster high-bandwidth memory or
slower CXL memory.  On these systems, the placement of memory allocations
has a significant effect on the performance that a workload will obtain.
While work on tiered-memory improvements has been ongoing for years, it
feels like the pace has slowed a bit recently.  Even so, there are a few
efforts underway, but they are facing questions about whether the tiering
design makes sense.

         Full Story  ( comments: 3 )

 [ $ ] LWN.net Weekly Edition for September 3, 2026 

         Posted Sep 3, 2026 0:22 UTC (Thu)  
        The LWN.net Weekly Edition for September 3, 2026 is available.

         Inside this week's LWN.net Weekly Edition 

   Front : Python JIT; rnull block driver; steal time; GNOME governance; 7.3 merge window; LUKS.
               Briefs : Kernel infrastructure; Debian AI; Dolphin 26.08; Firefox 155; Incus 7.4; OpenShot 4.0; Quotes; ...
               Announcements : Newsletters, conferences, security updates, patches, and more.

 Read the full article 

 [ $ ] Securely suspending LUKS-encrypted disks 

         [Security] Posted Sep 2, 2026 17:14 UTC (Wed) by daroc 

When a laptop is asleep, its memory is not unreadable. The right
tooling can attach to the computer's memory bus and read out its contents, and

cold-boot attacks  can theoretically read values from memory for a short time
after the computer loses power. That
is really an unavoidable fact about the hardware, but some users would still
like to ensure that, even if this happens, their long-term encryption keys, such as
the key for full-disk encryption, remain unreadable. In June&nbsp;2026, Ingo
Blechschmidt

discovered  that Linux kernel versions after 6.9 (released in
May&nbsp;2024)
were not erasing disk-encryption keys when a laptop was put to sleep, even
when configured to do so. He quickly identified a potential fix, which has been
merged, but it was not a comprehensive solution.

         Full Story  ( comments: 27 )

 [ $ ] Governing GNOMEs: how the project's technical decision-making is evolving 

         [Development] Posted Sep 2, 2026 15:03 UTC (Wed) by jzb 

         Emmanuele Bassi kicked off a project to improve GNOME's technical governance
with a  presentation about his
ideas  ( video ) at
 GUADEC&nbsp;2025 . His nudging
has led the project to, slowly, work on creating more formal structures for
technical governance. It is adopting a teams structure and looking toward
creating a steering committee, as well as bootstrapping a Request for Comments
(RFC) process. If adopted, GNOME would require RFCs for design, user experience,
architectural, and other changes that carry a major impact on the project. 

         Full Story  ( comments: 5 )

 [ $ ] A pause for the Python JIT 

         [Development] Posted Sep 1, 2026 14:40 UTC (Tue) by jzb 

         In 2024 the  Python&nbsp;3.13 
release added an  experimental
just-in-time (JIT) compiler  to optimize the way that CPython executes Python
code. Since then, work has proceeded on the JIT, albeit perhaps less formally
than some might like. In June, Python's  steering
council  (SC) put out an  announcement 
that no new development on the JIT land (with the exception of bug and security
fixes) in Python's main branch, until it accepts a  Python Enhancement Proposal  (PEP)
that would make the case for the JIT as a supported part of CPython. That has
led to the creation of  PEP&nbsp;836  ("JIT Go Brrr: The
Path to a Supported JIT Compiler for CPython"), which is currently under
discussion. As it stands, it seems likely that work on JIT will continue, but
when that will happen is less certain. 

         Full Story  ( comments: 18 )

 [ $ ] The rest of the 7.3 merge window 

         [Kernel] Posted Aug 31, 2026 14:12 UTC (Mon) by corbet 

        By the time Linus Torvalds  released
7.3-rc1  and closed the merge window for this release, 15,267 non-merge
changesets had been pulled into the mainline repository.  That is the
second-highest commit count for an -rc1 release in the kernel's history;
only the 6.7-rc1 release, which included nearly 3,000 commits of bcachefs
history, had more.  About 13,000 of those commits entered the mainline
after  the first 7.3 merge-window summary 
was written so, needless to say, there are a lot of changes to cover.

         Full Story  ( comments: 2 )

 [ $ ] The &quot;rnull&quot; Rust block driver 

         [Kernel] Posted Aug 28, 2026 18:26 UTC (Fri) by daroc 

The
 null block
driver  ( null_blk )
is a small driver that is mostly useful for benchmarking block-layer
implementations. It accepts all requests and marks them complete as quickly as
possible, doing as little work as possible. In June&nbsp;2026, Andreas Hindborg shared

a patch set  implementing the same functionality in Rust, in order to show
that a simple block driver is now possible to write using the kernel's
Rust APIs and to enable comparisons between the C and Rust
implementations.
A minimal version of the "rnull" driver is already present in the mainline
kernel, but Hindborg's patch set brings it up to feature parity with the C
version.

         Full Story  ( comments: 25 )

 [ $ ] Using steal time to moderate CPU demands 

         [Kernel] Posted Aug 27, 2026 14:11 UTC (Thu) by corbet 

        Virtualization can increase CPU utilization by allowing a large number of
virtual CPUs to share a smaller number of physical CPUs.  The amount of CPU
time that is actually available does not change, though, so heavy activity
on too many virtual CPUs can lead to contention and significant performance
loss.  The  steal governor
patch series  from Shrikanth Hegde is an attempt to address that problem
with a mechanism that allows virtual machines to voluntarily reduce the
number of virtual CPUs they use when contention is high.

         Full Story  ( comments: 1 )

 LWN.net Weekly Edition for August 27, 2026 

         Posted Aug 27, 2026 0:54 UTC (Thu)  
        The LWN.net Weekly Edition for August 27, 2026 is available.

         Inside this week's LWN.net Weekly Edition 

   Front : AGPL violations; OpenMDW license; quantum computing and encryption; 7.3 merge window; Remind; Quickshell.
               Briefs : arrayref; RIP Steve French; Armbian 26.8; Vanilla OS 3; Emacs 31.1; KDE Gear 26.08; LibreOffice 26.8; RPM 6.1.0; Quotes; ...
               Announcements : Newsletters, conferences, security updates, patches, and more.

 Read the full article 

 Buildroot 2026.08 released 

         [Distributions] Posted Sep 7, 2026 13:18 UTC (Mon) by jzb 

          Version
2026.08  of the  Buildroot  embedded Linux
system builder has been released. Buildroot 2026.08 includes nearly 1,000
changes from 100 contributors; some of the notable changes include support for
Linux&nbsp;7.1.x, Binutils 2.46.1, GCC 16.2.0, glibc 2.44, as well as adding the
M68K and IBM Power 10/11 architectures. 

         Comments (1 posted) 

 Security updates for Monday 

         [Security] Posted Sep 7, 2026 13:07 UTC (Mon) by jzb 

        Security updates have been issued by  AlmaLinux  (buildah, freerdp, gegl04, go-fdo-client, grafana, grafana-pcp, kernel, and pipewire),  Debian  (aom, chromium, libde265, libssh2, thunderbird, and tryton-server),  Fedora  (chromium, composer, cosmic-greeter, gegl04, greetd, ibus-table, jss, libheif, lightdm, lxdm, memcached, perl-DBD-Pg, plasma-login-manager, rust-webbrowser, sddm, selinux-policy, slitherer, and tkimg),  Mageia  (expat, mingw-expat, mbedtls, microcode, python-linkify-it-py, and tomcat),  Oracle  (buildah, container-tools:ol8, dbus-broker, freerdp, go-toolset:ol8, grafana-pcp, kernel, kernel-uek, nodejs24, php, and pipewire),  Slackware  (libpcap, libxml2, mozilla-firefox, mozilla-thunderbird, and util-linux),  SUSE  (bson-devel, busybox, bzip2, c-ares, cpio, cups-filters, dracut, ffmpeg-7, ffmpeg-8, file-roller, firefox, firefox-esr, glances-common, grafana, hauler, helm, helm3, java-17-openjdk, java-21-openjdk, lcms2, libcupsfilters, libheif, libmsgpack-c2, libsoup, libsoup2, libusb-1_0, libvirt, LibVNCServer, mcphost, ollama, opencode, openssl-1_1, openssl-3, php-composer2, podman, postgresql15, postgresql17, postgresql18, python, python-aiohttp, python-h2, python-sqlparse, python310, rpcbind, sssd, thunderbird, trivy, ucode-intel, and webkit2gtk3), and  Ubuntu  (linux, linux-aws, linux-aws-7.0, linux-gcp, linux-gke, linux-hwe-7.0, linux-realtime, linux, linux-aws, linux-fips, linux-kvm, linux-lts-xenial, linux, linux-fips, linux-gcp, linux-gcp-fips, linux-gke, linux-gkeop, linux-nvidia, linux-nvidia-6.8, linux-nvidia-lowlatency, linux-raspi, linux-realtime, linux-realtime-6.8, linux, linux-gcp, linux-gcp-fips, linux-gke, linux-gkeop, linux-hwe-5.15, linux-ibm, linux-ibm-5.15, linux-intel-iot-realtime, linux-lowlatency, linux-lowlatency-hwe-5.15, linux-nvidia, linux-nvidia-tegra, linux-nvidia-tegra-5.15, linux-realtime, linux-aws-5.4, linux-gcp, linux-gcp-5.4, linux-gcp-7.0, linux-oem-7.0, minetest, and miniupnpd).

         Full Story  ( comments: none )

 Asahi Linux now supports M3-series Macs 

         [Distributions] Posted Sep 7, 2026 12:25 UTC (Mon) by jzb 

         The Asahi Linux project has  announced  that support
for Apple's M3-series chips has been added to the Asahi installer. 

 Linux support for M3 series SoCs and the machines powered by them is now in a
state where  almost  everything supported on the M1 and M2 series
machines just works. This includes the webcam, internal microphones, USB (up to
the hardware limit of USB 3 10 Gb/s), hardware accelerated video decoding
 including support for AV1 , WiFi, Bluetooth, and much more! The
only major exceptions remain full DCP support and the GPU, which we will have
more news on in the  coming
months .  Do not expect performant or power-efficient 3D acceleration
right now.  

 See the blog post for other current limitations of M3 support. 

         Comments (none posted) 

 Kernel prepatch 7.3-rc2 

         [Kernel] Posted Sep 7, 2026 0:52 UTC (Mon) by corbet 

        The  7.3-rc2  kernel prepatch is out for
testing.  Linus said:

	This didn't *feel* like a particularly busy rc2, but it clearly
	was.  rc2 is usually the quietest time when people take a breather
	after the merge window and it takes a while to start finding
	bugs. But not this time - this is a "full fat" rc release. [...]

	Nothing looks particularly odd, even if the rc2 timing is a bit
	unusual. It might be just random, but we'll obviously all blame it
	on AI, because whether that's really the cause or not, it's an easy
	thing to blame ;)

         Comments (none posted) 

 Grml 2026.09 released 

         [Distributions] Posted Sep 4, 2026 13:30 UTC (Fri) by jzb 

          Version
2026.09 ,  code-named 
"Hättiwaritätti", of the Debian-based Grml live Linux distribution for system
administrators has been released. It is based on packages from the upcoming
Debian&nbsp;14 ("forky") release. Notable changes include an update to the Linux
7.1.8 kernel, support for booting from exfat-formatted USB devices, and an
update to GNU&nbsp;Screen&nbsp;5.0.1. 

         Comments (none posted) 

 Security updates for Friday 

         [Security] Posted Sep 4, 2026 13:18 UTC (Fri) by jzb 

        Security updates have been issued by  Debian  (chromium, firefox-esr, and pcre2),  Fedora  (cockpit, expat, freeipa, kbd, kernel, mrtg, python-pip, and valkey),  Mageia  (libopenmpt and python-gitpython),  Oracle  (dbus-broker, freerdp, gegl, gegl04, gimp:2.8, go-fdo-client, go-fdo-server, golang-github-openprinting-ipp-usb, grafana, gzip, image-builder, iperf3, kernel, libssh, libxml2, microcode_ctl, nodejs:22, nodejs:24, openssl-fips-provider, pam, php:7.4, php:8.2, tar, and wget),  SUSE  (apache2-mod_auth_openidc, apptainer, busybox, cpio, cups-filters, curl, dracut, ffmpeg, file-roller, glibc, grafana, kubevirt, virt-pr-helper-container, lcms2, libtree-sitter0_26, libvirt, postgresql14, postgresql15, postgresql16, postgresql18, suseconnect-ng, terraform-provider-susepubliccloud, and yast2-users), and  Ubuntu  (FFmpeg, gnupg2, librabbitmq, libssh2, openssh, and spice-vdagent).

         Full Story  ( comments: none )

 Audacity 4.0 released 

         [Development] Posted Sep 3, 2026 13:58 UTC (Thu) by jzb 

          Version
4.0  of the Audacity audio editor has been released. Notable changes in this
release include a rewritten interface using Qt, ability to save user-interface
layouts as "Workspaces", improvements in working with audio clips, and a new
 .aup4  project format. 

 The release is not fully feature-compatible with the Audacity&nbsp;3.x
series; see the  compatibility
notes  for a list of missing features. 

         Comments (10 posted) 

 Security updates for Thursday 

         [Security] Posted Sep 3, 2026 13:07 UTC (Thu) by jzb 

        Security updates have been issued by  AlmaLinux  (freerdp, go-fdo-server, golang-github-openprinting-ipp-usb, kernel, kernel-rt, nodejs:24, perl-DBI, and php),  Debian  (firefox-esr, libapache2-mod-auth-openidc, and libass),  Fedora  (dracut, exiv2, firefox, freerdp, gvfs, mingw-expat, mingw-gstreamer1, mingw-gstreamer1-plugins-bad-free, mingw-gstreamer1-plugins-base, mingw-gstreamer1-plugins-good, mingw-openexr, nss, proftpd, and syncthing),  Mageia  (apr-util, bubblewrap, libalsa2, libarchive, perl-Net-OAuth, perl-Text-CSV_XS, perl-XML-Bare, and perl-YAML-Syck),  Oracle  (freerdp, gimp, golang, iperf3, nginx:1.24, nodejs:22, nodejs:24, pipewire, wget, xmlrpc-c, and xorg-x11-server-Xwayland),  SUSE  (apache2-mod_auth_openidc, apptainer, apr-util, bzip2, c-ares, cosign, dhcpcd, dovecot22, emacs, erlang, gegl, gopass, gzip, httpcomponents-client, incus, kernel-devel, libgpg-error, libsoup2, mozillafirefox, mozilla-nss, mozilla-nspr,, MozillaFirefox, mozilla-nss, mozilla-nspr, rust-cbindgen, nodejs20, orthanc, orthanc-authorization, orthanc-postgresql,, postgresql14, python-cryptography, python-msgpack, quagga, snpguest, snphost, texlive, tuxguitar, udisks2, vim, wget, and yast2-users), and  Ubuntu  (apr-util, biosig, linux, linux-aws, linux-azure, linux-azure-fips, linux-fips,
 linux-hwe-5.4, linux-ibm, linux-ibm-5.4, linux-iot, linux-kvm,
 linux-oracle, linux-raspi, linux-raspi-5.4, linux-xilinx-zynqmp, linux-aws-5.15, linux-gcp-5.15, linux-oracle-5.4, sssd, and tika).

         Full Story  ( comments: none )

 Incus 7.4 released 

         [Development] Posted Sep 2, 2026 15:03 UTC (Wed) by jzb 

          Version
7.4  of the Incus container and virtual-machine management system has been
released. Notable changes in this release include UEFI Secure Boot key
management, "near-live" migration of containers between Incus instances, as well
as  burst I/O  limits for disk and network
devices. 

         Comments (none posted) 

 Eight stable kernels for Wednesday 

         [Kernel] Posted Sep 2, 2026 13:28 UTC (Wed) by jzb 

         Greg Kroah-Hartman has announced the  7.2.3 ,
 7.1.13 ,  6.18.49 ,  6.12.108 ,  6.6.156 ,  6.1.187 ,
 5.15.220 , and  5.10.269  stable kernels. Each contains a number of
important fixes throughout the tree. Users are advised to upgrade. 

 Note that 7.1.13 is the last of the 7.1 updates 

         Comments (none posted) 

         --&gt; More news items 

            Copyright &copy; 2026, Eklektix, Inc. 

            Comments and public postings are copyrighted by their creators. 
            Linux  is a registered trademark of Linus Torvalds 


