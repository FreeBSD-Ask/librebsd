---
title: "FAQ_Version_118_EBOL_Andrew_Josey_维护2025-05-252026-07-23"
source_url: https://www.opengroup.org/austin/papers/posix_faq.html
download_date: 2026-09-07
---

# FAQ_Version_118_EBOL_Andrew_Josey_维护2025-05-252026-07-23

来源: https://www.opengroup.org/austin/papers/posix_faq.html

 
 POSIX.1 FAQ 

 POSIX&trade; 1003.1 Frequently Asked Questions (FAQ Version 1.18) 

Last Updated : May 25 2025: freq.ques,v 1.19

This is the Frequently Asked Questions file for the POSIX 1003.1
standard (IEEE Std 1003.1).
Its maintainer is Andrew Josey (ajosey at The Open Group ).
Suggestions and contributions are always welcome.

This document can be found on the world wide web at http://www.opengroup.org/austin/papers/posix_faq.html.

This article includes answers to the following.

Q0. What is POSIX? What is POSIX.1?

Q1. What is the Portable Application Standards Committee (PASC)?

Q2. What is the Austin Group?

Q3. What is the latest version of POSIX.1?

Q4. Where can I download the 1003.1 standard from?

Q5. What are the restrictions on the 1003.1 standard drafts and the full standard?

Q6. Is the standard available in Man Pages format?

Q7. How do I become a participant in the development of the POSIX.1 standard?

Q8. What happened to the existing POSIX 1003.1-1990 and POSIX 1003.2-1992 standards when this revision completed?

Q9. What is the history of IEEE POSIX 1003.1 System Application Interface
(C API) ?

Q10. What is the IEEE POSIX 1003.2 Shell and Utilities?

Q11. What are the IEEE POSIX Standards for Real-time?

Q12. How does the 1003.1 standard compare to the Linux Standard Base?

Q13. What options are there in the POSIX.1 standard?

Q14. What are the core technical changes in the latest POSIX.1
standard over 1003.1-1990 and 1003.2-1992?

Q15. Does removal of obsolescent utility syntax mean that implementations supporting usages of  head -5 file ,  tail -5 file ,  tail -l file  are no longer allowed?

Q16. What about POSIX Certification?

Q17. How do I report a bug in the POSIX.1 standard?

Q18. What are the plans for the next revision of POSIX.1?

Q19. How do I add a question to this FAQ?

 Q0. What is POSIX? What is POSIX.1? 

POSIX is a trademark of the IEEE.

POSIX is an acronym for  P ortable  O perating  S ystem
 I nterface.

Although originated to refer to the original IEEE Std 1003.1-1988,
the name POSIX more correctly refers to a family of related standards:
IEEE Std 1003. n  (where  n  is a number) and the parts of
ISO/IEC 9945. The term POSIX was originally used as a synonym for
IEEE Std 1003.1-1988. A preferred term for that standard, POSIX.1,
emerged. This maintained the advantages of readability of the symbol
``POSIX'' without being ambiguous with the POSIX family of standards.

For a full listing of the project numbers see
PASC Standing Document  SD11 .
-->

The name POSIX was suggested by Richard Stallman. It is expected
to be pronounced pahz-icks, as in positive, not poh-six, or other
variations. The pronunciation has been published in an attempt to
promulgate a standardized way of referring to a standard operating
system interface.

The latest version of the POSIX.1 standard is IEEE Std 1003.1-2024, developed by the Austin Group (see later).
For further information on the background, audience and purpose of POSIX.1
see the following document:

URL: http://www.opengroup.org/austin/papers/backgrounder.html .

 Q1. What is the Portable Application Standards Committee (PASC)? 

The IEEE Computer Society's Portable Application Standards Committee
(PASC) is the group that has and continues to develop the POSIX family
of standards.  Historically, the major work has been undertaken within
Project 1003 (POSIX) with the best known standard being IEEE Std 1003.1
(also known as POSIX 1003.1, colloquially termed "dot 1"). The goal of
the PASC standards has been to promote application portability at the
source code level.

 Q2. What is the Austin Group? 

The Austin Common Standards Revision Group (CSRG) is a joint technical
working group established to develop and maintain the
latest version of the 1003.1 standard --- which combined
and revised ISO/IEC 9945-1,1996 edition, ISO/IEC 9945-2, 1993 Edition,
IEEE Std 1003.1,1996 edition, IEEE Std 1003.2, 1992 edition and
the appropriate parts of the Single UNIX Specification.

See http://www.opengroup.org/austin/ for more information.

 Q3. What is the latest version of POSIX.1? 

The 1003.1-2024 standard was published
in June 2024.
The standard is formally known as:

IEEE Std 1003.1-2024

The Open Group Technical Standard Base Specifications, Issue 8

POSIX.1 is also an international standard, and ISO/IEC publication
occurred in September 2009, denoted as ISO/IEC 9945:2009.
Technical Corrigendum 1 was approved by
ISO/IEC in late 2012.  Technical Corrigendum 2 was approved by
ISO/IEC in March 2017. The 2024 edition is expected
to be approved by ISO/IEC in 2025.

 Q4. Where can I download the 1003.1 standard from? 

The html version of the latest version of the standard (which
incorporates technical corrigendum 1) is freely available to read and download
from:
URL: http://www.unix.org/version4/ , you need to register for a copy.

PDF copies of the final standard can also be obtained either from The
IEEE (search on 1003.1) , The Open Group (Look for
documents T101,C181) or ISO (look for ISO/IEC 9945).
It is freely available in pdf format to members of The Open Group from
The Open Group publications catalog.

Ongoing draft specifications for future technical corrigenda may be available
online from the Austin Group web site at http://www.opengroup.org/austin/ .
You need to be a member of the  Austin Group. Information on how to
join the group is on the web site.

URL: 
http://www.opengroup.org/austin/ . (Austin Group Home Page)

Interpretations of the standard can be found in the Mantis bug tracker
URL: 
http://austingroupbugs.net 

 Q5. What are the restrictions on the 1003.1 standard drafts and the full standard? 

See the copyright notice on the documents and
the notice at http://www.opengroup.org/austin/login.html .
Downloading the draft is taken as agreement to abide by the
stated terms and conditions.  In brief you need to be a participant
in the Austin Group  in order to download the drafts.

URL: 
http://www.opengroup.org/austin/login.html  (Copyright Notice)

Note also that the IEEE and The Open Group have granted permission
to several open source projects to incorporate materials from the
standard.
All queries regarding permission to reproduce sections
of the standard should be sent to austin-group-permissions at The
Open Group. Permission needs to be granted by both copyright
holders, The IEEE and The Open Group.

The IEEE and The Open Group position on
implementations of the standard is as follows:
&quot; it is fair use of the standard for
implementors to use the names, labels etc  contained within the
specification. The intent of publication of the standard is to
encourage implementations of the standard.  Your attention is drawn
to the disclaimer regarding verification of patents when implementing
the standard. &quot;

 Q6. Is the standard available in Man Pages format? 

A personal use copy of the standard in html man page format
can be downloaded from
http://www.unix.net/single_unix_specification.

A set of nroff manual pages are maintained by
Michael Kerrisk,  who oversees the Linux Manual Pages Project,
with the permission of IEEE and The Open Group.
These can be obtained from
 http://man7.org/linux/man-pages/index.html 

 Q7. How do I become a participant in the POSIX.1 Working Group? 

To participate you need to join the Austin Group.
See http://www.opengroup.org/austin/lists.html for more
information.

URL: 
http://www.opengroup.org/austin/lists.html . (How to Join the Austin Group)

 Q8. What happened to the original POSIX 1003.1-1990 and POSIX 1003.2-1992 standards? 

Since the material contained in the existing POSIX 1003.1 and POSIX 1003.2 standards
is merged into the revision, POSIX 1003.1-1990 and its amendments, and
POSIX 1003.2-1992 and its amendments
were administratively withdrawn by the IEEE.

 Q9. What is the history of the IEEE POSIX 1003.1 System Application Interface (C API) ? 

Historically, POSIX 1003.1 has been the base standard upon which the POSIX
family of standards has been built. In keeping with its original focus
on the UNIX system, it is aimed at interactive timesharing computing
environments.

The first edition of IEEE Std 1003.1 was published in 1988. Subsequent
editions were published in 1990, 1996 and 2001. The 1990 edition was a
revision to the 1988 edition and became the stable base standard onto
which further amendments were added. The 1990 edition was also approved
as an international standard, ISO/IEC 9945-1:1990.

The 1996 edition added the IEEE Std 1003.1b-1993, IEEE Std 1003.1c-1995,
and 1003.1i-1995 amendments to the base standard, keeping the stable core
text unchanged.  The 1996 edition of IEEE Std 1003.1 was also approved
as an international standard, ISO/IEC 9945-1:1996.

In 1998 the first real-time profile standard, IEEE Std 1003.13-1998 was
published, enabling POSIX to address embedded real-time applications
and smaller footprint devices.

In 1999 the decision was taken to commence the first  major revision to
the core base standard in ten years, including a merger with the 1003.2
standards for Shell and Utilities which had been a separate standard
up to this point . It was agreed that this work be undertaken by the
Austin Group. As part of this decision the PASC decided
to cease rolling amendments to the base standard after completion of
IEEE Stds 1003.1a, 1003.1d, 1003.1g, 1003.1j, 1003.1q,  and 1003.2b.
These projects were rolled into the 2001 edition of IEEE Std 1003.1.
It was decided to convert other projects in progress to standalone
documents.

 Q10. What is IEEE POSIX 1003.2 Shell and Utilities? 

This standard defines a standard source level interface to the shell
and utility functionality required by application programs, including
shell scripts. This standard has been incorporated into the latest
revision of POSIX 1003.1 and thus a POSIX.2 standard no longer exists.

 Q11. What are the IEEE POSIX Standards for Real-time? 

The PASC Real-time System Services Working Group  (SSWG-RT) has developed
a series of standards that amend IEEE Std 1003.1-1990 and a profile
standard (IEEE Std 1003.13-1998).

The Real-time amendments to IEEE Std 1003.1-1990 are as follows:

IEEE Std 1003.1b-1993 Realtime Extension

IEEE Std 1003.1c-1995 Threads

IEEE Std 1003.1d-1999 Additional Realtime Extensions

IEEE Std 1003.1j-2000 Advanced Realtime Extensions

IEEE Std 1003.1q-2000 Tracing

These have all been folded in as options within the revision project
undertaken by the Austin Group in producing IEEE Std 1003.1-2001.

The Real-time profile is known as IEEE Std 1003.13-1998.  At the time
of writing there is a revision to IEEE Std 1003.13-1998 in progress to
align it with IEEE Std 1003.1-2001, this project current known as IEEE
P1003.13-200x.

 Q12. How does the POSIX.1 standard compare to the Linux Standard Base? 

The POSIX.1 standard specifies application programming interfaces (APIs)
at the source level, and is about source code portability.
Its neither a code implementation nor an operating system, but
a stable definition of a programming interface that those systems supporting the
specification guarantee to provide to the application programmer.
Efforts such as the Linux Standard Base, and similarly the iBCS2 for x86
implementations of System V, are primarily about binary portability
and define a specific binary implementation of an interface to
operating system services. In general they build upon the foundations
of the POSIX standard.

Two white papers with further information on this topic are available at:

https://collaboration.opengroup.org/platform/single_unix_specification/documents.php?action=show&gdid=9045 ,
 https://collaboration.opengroup.org/platform/single_unix_specification/documents.php?action=show&gdid=9634 .

 Q13. What options are there in the POSIX.1 standard? 

[Please note this relates to the 2004 edition, for the latest
information see the UNIX information site at
 http://www.unix.org/version4 ]

For a good description of the modular options in the POSIX.1 standard see
URL:
 http://people.redhat.com/~drepper/posix-option-groups.html 

 Q14. What are the core technical changes in the
POSIX.1 standard over 1003.1-1990 and 1003.2-1992?

The main changes are as follows: alignment with ISO/IEC 9899:1999 (ISO C),
support for IPv6, integration of recent POSIX realtime amendments (
1003.1d, 1003.1j, 1003.1q), amendments to the core POSIX functionality from
the 1003.2b and 1003.1a amendments, application of technical corrigendum
from The Open Group and IEEE interpretations, revision of options ,
removal of obsolescent and legacy interfaces.

  Q15. Does removal of obsolescent utility syntax mean that implementations supporting usages of  head -5 file ,  tail -5
file ,  tail -l file  are no longer allowed? 

No, in general the intent of removing the obsolescent forms of the utility
synopses was not to disallow them to be supported by implementations but
to downgrade the status of their use in applications from conforming
application using an obsolescent feature to non-conforming application.
In general it is allowed for utilities to have extensions that violate
the utility syntax guidelines so long as the forms defined in the standard
that are required to follow the utility syntax guidelines do so.   The
cases cited fit the case.  The Austin Group has more general
cases under review at the present time.

 Q16. What about POSIX Certification? 

The IEEE and The Open Group maintain a program
covering POSIX Certification for a number of standards.
This includes 1003.1™-200 Base, 1003.1™-2016 Base, PSE54 Multipurpose Realtime 1003.13™-2003 System, and PSE52 Realtime Controller 1003.13™-2003 System.

For details see  http://get.posixcertified.ieee.org/ 
 http://www.opengroup.org/press/03nov03.htm .
-->

For a summary of web references for the program see:
 http://www.opengroup.org/certification/idx/posix.html .

The program includes a product standard for each type of product that can
be certified within the POSIX Certification Program. In this initial
iteration of the certification program these are as follows:

1003.1-2003 Base Product Standard: This is a profile product standard
that comprises the mandatory functionality from IEEE Std
1003.1, 2003 Edition. It is comprised of two component product
standards.

1003.1-2003 System Interfaces Product Standard: This is a
component product standard for the mandatory system interfaces and
headers related functionality from IEEE Std 1003.1.

1003.1-2003 Shell and Utilities Product Standard: This is a
component product standard for the mandatory shell and utilities
related functionality from IEEE Std 1003.1.

PSE54 Multipurpose Realtime 1003.13TM-2003 System:
This is for operating system environments providing realtime services
based on IEEE Std 1003.13 Profile PSE54. This supports applications
portability at the source code level and includes the provision of a
standard operating system interface and environment, including a full
file system implementation and support for multiple users.

A product can be certified against one or more product standards and
the program allows for two levels of certification: Platform Specific
Certification, which applies to a single defined hardware and software
environment, and Product Family Certification, which applies to all
members of a binary-compatible family.

 Q17. How do I report a bug in the POSIX.1 standard? 

To report a bug in the POSIX.1 standard please see
 http://www.opengroup.org/austin/defectform.html .

 Q18. What are the plans for the next revision of POSIX.1? 

Looking forward, the Austin Group is working on  maintenance of the 2024 edition, with the next major revision a longer term target.

 Q19. How do I add a question to this FAQ? 

Send the question (preferably with a proposed answer) to Andrew Josey.


