# The Design and Implementation of the 4.4BSD Operating System：序言与设计目标（节录）

- 文献：MCKUSICK M K, BOSTIC K, KARELS M J, QUARTERMAN J S. The Design and Implementation of the 4.4BSD Operating System[M]. Reading: Addison-Wesley, 1996.
- 底本：`references_fulltext.duckdb` ref1137 全文块 `block_index=51／58／254`（2026-11-13 自库内逐字节导出，未改一字）。
- 性质：CSRG 核心成员撰写的系统专著（含序言与发行信息），属当事人参与的学术性一手记述。
- 说明：三块按原序并列，块间以分隔线标记；OCR 断行保留。

---

## block 29（书名页与作者栏）

The Design and Implementation of the
4.4BSD
Operating System
Marshall Kirk McKusick
Consultant
Keith Bostic
Berkeley Software Design, Inc.
Michael J. Karels
Berkeley Software Design, Inc.
John S. Quarterman
Texas Internet Consulting
•
TT
ADDISON-WESLEY
Boston
• San Francisco
• New York
• Toronto
• Montreal
London
• Munich
• Paris
• Madrid
Capetown
• Sydney
• Tokyo
• Singapore
• Mexico City

---

## block 51（Preface：Berkeley 发行谱系）

viii
Preface
Berkeley Software Distributions
These Berkeley systems have introduced several useful programs and facilities to
the UNIX community:
• 2BSD (the Berkeley PDP - I I system): the text editor vi
• 3BSD (the first Berkeley VAX system): demand-paged virtual-memory support
• 4.0BSD: performance improvements
• 4. 1 BSD: job control, autoconfiguration, and long C identifiers
• 4.2BSD and 4.3BSD: reliable signals; a fast filesystem; improved networking,
including a reference implementation of TCP/IP; sophisticated interprocess
communication (IPC) primitives; and more performance improvements
• 4.4BSD: a new virtual memory system; a stackable and extensible vnode
interface; a network filesystem (NFS); a log-structured filesystem, numerous
filesystem types, including loopback, union, and uid/gid mapping layers; an
IS09660 filesystem (e.g., CD-ROM); ISO networking protocols; support for 68K,
SPARC, MIPS, and PC architectures; POSIX support, including termios, sessions,
and most utilities; multiple IP addresses per interface; disk labels; and improved
booting
4.2BSD, 4.3BSD, and 4.4BSD are the bases for the UNIX systems of many vendors,
and are used internally by the development groups of many other vendors. Many
of these developments have also been incorporated by System V ,  or have been
added by vendors whose products are otherwise based on System V .
The implementation of the T CP/IP networking protocol suite in 4.2BSD and
4.3BSD, and the availability of those systems, explain why the TCP/IP networking
protocol suite is implemented so widely throughout the world. Numerous vendors
have adapted the Berkeley networking implementations, whether their base system
is 4.2BSD, 4.3BSD, 4.4BSD, System V, or even Digital Equipment Corporation's
V MS or Microsoft's Winsock interface in Windows '95 and Windows/NT.
4BSD has also been a strong influence on the POSIX (IEEE Std 1003 . 1 )
operating-system interface standard, and on related standards. Several features
such as reliable signals, job control, multiple access groups per process, and the
routines for directory operations-have been adapted from 4.3BSD for P OSIX.
Material Covered in this Book
This book is about the internal structure of 4.4BSD [Quarterman et al, 1985], and
about the concepts, data structures, and algorithms used in implementing 4.4BSD's
system facilities. Its level of detail is similar to that of Bach's book about UNIX
System V [Bach, 1 986] ; however, this text focuses on the facilities, data structures,
and algorithms used in the Berkeley variant of the UNIX operating system. The
book covers 4.4BSD from the system-call level down-from the interface to the
kernel to the hardware itself. The kernel includes system facilities, such as

---

## block 58（Preface：Getting 4.4BSD）

Preface
xi
Getting 4.4BSD
Current information about the availability of 4.4BSD source code can be found at
the sites listed below. At press time, the source code for the 4.4BSD-Lite Release
2 system, as well as that for the FreeBSD version of 4.4BSD, which is compiled
and ready to run on PC-compatible hardware, are available from Walnut Creek
CDROM. Contact Walnut Creek for more information at 1 -800-786-9907, or use
orders@cdrom.com, or http://www.cdrom.com/. The NetBSD distribution is
compiled and ready to run on most workstation architectures. For more
information, contact the NetBSD Project at majordomo@NetBSD.ORG (send a
message body of "lists"), or http://www.NetBSD.ORG/.
The OpenBSD
distribution is compiled and ready to run on a wide variety of workstation
architectures and has been extensively vetted for security and reliability. For more
information, visit the OpenBSD project's Web Site at http://www.OpenBSD.org/.
A fully supported commercial release, BSD/OS, is available from Berkeley
Software
Design,
Inc.,
at
1-800-800-4273,
bsdi-info@bsdi.com,
or
http://www.bsdi.com/. The 4.4BSD manuals are jointly published by Usenix and
O'Reilly. O'Reilly sells the five volumes individually or in a set (ISBN
1 -56592-082-1): 1 -800-889-8969, order@ora.com, or http://www.ora.com/.
For you diehards who actually read to the end of the preface, your reward is
finding out that you can get T-shirts that are a reproduction of the the original
artwork drawn by John Lasseter for the cover of this book (yes, he is the John
Lasseter of Walt Disney/Pixar fame who masterminded the production of "Toy
Story"). These shirts were made available to the people who helped with the
creation, reviewing, and editing of the book and to those folks who first reported
errors in the book. A variation on these shirts that is clearly different from the
originals (so as not to diminish the rarity of the ones that people had to work to
get) is now available. For further information on purchasing a shirt, send a self
addressed envelope (United States residents please include return postage) to
M. K. McKusick
1 6 14 Oxford St.
Berkeley, CA 94709- 1 608
Alternatively, you can visit the "History of BSD T-shirts" web page at
http://www.mckusick.com/beastie/index.html.
Acknowledgments
We extend special thanks to Mike Hibler (University of Utah) who coauthored
Chapter 5 on memory management, and to Rick Macklem (University of Guelph),
whose NFS papers provided much of the material on NFS for Chapter 9.
We also thank the following people who read and commented on nearly the
entire book: Paul Abrahams (Consultant), Susan LoVerso (Orea Systems), George
Neville-Neil (Wind River Systems), and Steve Stepanek (California State
University, Northridge).
We thank the following people, all of whom read and commented on early
drafts of the book: Eric Allman (Pangaea Reference Systems), Eric Anderson

---

## block 254（§1.3 Design Goals of 4.4BSD）

Section 1 .3
Design Goals of 4BSD
1 5
4.4BSD Design Goals
4.4BSD broadened the 4.3BSD hardware base, and now supports numerous archi
tectures, including Motorola 68K, Sun SPARC, M IPS, and Intel PCs.
The 4.4BSD release remedies several deficiencies in 4.3BSD. In particular,
the virtual-memory system needed to be and was completely replaced. The new
virtual-memory system provides algorithms that are better suited to the large
memories currently available, and is much less dependent on the VAX architecture.
The 4.4BSD release also added an implementation of networking protocols in the
International Organization for Standardization (ISO) suite, and further TCP/IP per
formance improvements and enhancements.
The terminal driver had been carefully kept compatible not only with Seventh
Edition, but even with Sixth Edition. This feature had been useful, but is increas
ingly less so now, especially considering the lack of orthogonality of its com
mands and options. In 4.4BSD, the CSRG replaced it with a POSIX-compatible
terminal driver; since System V is compliant with POSIX, the terminal driver is
compatible with System V. POSIX compatibility in general was a goal. POSIX
support is not limited to kernel facilities such as termios and sessions, but rather
also includes most POSIX utilities.
The most critical shortcoming of 4.3BSD was the lack of support for multiple
filesystems. As is true of the networking protocols, there is no single filesystem
that provides enough speed and functionality for all situations. It is frequently
necessary to support several different filesystem protocols, just as it is necessary to
run several different network protocols. Thus, 4.4BSD includes an object-oriented
interface to fi lesystems similar to Sun Microsystems' vnode framework. This
framework supports multiple local and remote filesystems, much as multiple net
working protocols are supported by 4.3BSD [Sandberg et al, 1 985]. The vnode
interface has been generalized to make the operation set dynamically extensible
and to allow filesystems to be stacked. With this structure, 4.4BSD supports
numerous fi lesystem types, including loopback, union, and uid/gid mapping lay
ers, plus an IS09660 filesystem, which is particularly useful for CD-ROMs. It also
supports Sun's Network filesystem (NFS) Versions 2 and 3 and a new local disk
based log-structured fi lesystem.
Original work on the flexible configuration of IPC processing modules was
done at Bell Laboratories in UNIX Eighth Edition [Presotto & Ritchie, 1 985] .
This stream 110 system was based o n  the UNIX character I/O system. I t  allowed a
user process to open a raw terminal port and then to insett appropriate kernel-pro
cessing modules, such as one to do normal terminal line editing. Modules to pro
cess network protocols also could be inserted. Stacking a terminal-processing
module on top of a network-processing module allowed flexible and efficient
implementation of network virtual terminals within the kernel. A problem with
stream modules, however, is that they are inherently linear in nature, and thus they
do not adequately handle the fan-in and fan-out associated with multiplexing in
datagram-based networks; such multiplexing is done in device drivers, below the
modules proper. The Eighth Edition stream 1/0 system was adopted in System V,
Release 3 as the STREAMS system.
