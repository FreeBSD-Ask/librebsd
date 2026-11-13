# UNIX System Laboratories, Inc. v. Berkeley Software Design, Inc. 等——1993-03-03 裁定意见（D.N.J. Civ. No. 92-1667）

- 文献：UNITED STATES DISTRICT COURT FOR THE DISTRICT OF NEW JERSEY，UNIX SYSTEM LABORATORIES, INC. v. BERKELEY SOFTWARE DESIGN, INC., and certain named individuals in their collective capacity as The Regents of the University of California，Civ. No. 92-1667，O P I N I O N，Debevoise, District Judge。
- 抓取：2026-11-13，`https://www.nokia.com/bell-labs/about/dennis-m-ritchie/bsdi/930303.ruling.txt`（Dennis M. Ritchie 存档；Dennis Ritchie 自述该批文件 1992–1993 年间经 FTP 自 UUNET 取得）。
- 说明：本文为裁定书正文的**节录转录**（页面正文至“II. PROCEDURAL HISTORY”起首处截断，原件续文不在本卡范围）。引文逐字照录，保留原件拼写与断开处（含 `230,9995` 等原件讹字与 `court-` 截断）。

---

UNITED STATES DISTRICT COURT

FOR THE DISTRICT OF NEW JERSEY

UNIX SYSTEM LABORATORIES, INC. Plaintiff, Civ. No. 92-1667 vs. O P I N I O N

BERKELEY SOFTWARE DESIGN, INC., and certain named individuals in their collective capacity as The Regents of the University of California, Defendants.

Attorneys for Plaintiff

Crummy, Del Deo, Dolan, Griffinger & Vecchione, P.C. One Riverfront Plaza Newark, NJ 07102 By: Gary F. Werner, Esq.

Paul, Hastings, Janofsky & Walker 399 Park Avenue NY, NY 10022 By: George L. Graff, Esq. James W. Kennedy, Esq.

Attorneys for Defendant Regents of the University of California

Crosby, Heafey, Roach & May 1999 Harrison Street Oakland, CA 94612 By: Joel Linzner, Esq.

Post, Polak & Goodsel 280 Corporate Center 65 Livingston Avenue Roseland, New Jersey 07068 By: Frederick B. Polak, Esq.

Attorneys for Defendant Berkeley Software Design, Inc.

Saiber Schlesinger Satz & Goldstein One Gateway Center Newark, NJ 07102-5311 By: James H. Forte, Esq.

Debevoise, District Judge. Plaintiff UNIX System Laboratories, Inc. instituted this action to seek relief from Defendants' ongoing distribution of computer software in alleged violation of USL's proprietary rights in the UNIX operating system. Plaintiff pleads eleven claims for relief, including federal copyright and trademark claims, and state contract, tort, and trademark dilution claims. Defendants now move (i) to dismiss, for lack of personal jurisdiction because Defendant Regents lack capacity to be sued and because of improper venue; (ii) to transfer because of improper venue and inconvenience; and (iii) to strike parts of the pleadings. Plaintiff cross-moves to amend its complaint and for a preliminary injunction.

## I. STATEMENT OF FACTS

Plaintiff UNIX System Laboratories ("USL") is a Delaware corporation and majority-owned subsidiary of American Telephone and Telegraph Company ("AT&T"), with its principal place of business in Summit, New Jersey.

Defendant Berkeley Software Designs, Inc. ("BSDI") is a recently-formed Delaware corporation with its principal place of business in Richmond Falls, Virginia. BSDI someday plans to develop, manufacture, and sell computer operating systems like Plaintiff. Defendant individuals are members of the Board of Regents (the "Regents") of the University of California ("Berkeley"). The Regents are a non-profit public corporation organized to administer the University of California pursuant to the California constitution, art. 9 § 9, and California state law.

The central issue here is whether Defendants BSDI and Regents appropriated parts of Plaintiff's allegedly proprietary program "UNIX," and then used and distributed these parts without authorization in violation of Plaintiff's copyrights and trade secrets. UNIX is a computer operating system; that is, it is a software program that oversees a computer's internal and external activities, including processing, resource allocation, communications, and applications use. AT&T's Bell Laboratories developed UNIX in the 1970s, and registered the name UNIX as Trademark No. 1,392,203 on May 6, 1986.

The parties executed their first UNIX licensing agreement in 1973, and by 1979 the parties had executed their first agreement covering the software that Plaintiff now seeks to protect, UNIX version 32V. The parties' most recent 32V agreement is the Educational Software License Agreement, or E-SOFT-00089, executed in 1985 ("the 00089 agreement"). (Forte Aff., Ex. F.) The 00089 agreement permits the Regents to create derivatives of UNIX and, to the extent that the derivatives are free of proprietary information, to distribute them without restriction.

Net2 apparently began as a project to develop a UNIX-like product devoid of AT&T proprietary code. This product contained both non-proprietary software from the BSD releases and software written specifically for Net2, sometimes by volunteers. (Kennedy Aff., Ex. 6.) To guarantee that no proprietary code remained, CSRG screened and eliminated overlapping code sections in accordance with criteria developed together with Berkeley's legal counsel. In addition, Berkeley "repeatedly contacted the USL licensing office, in an attempt to have them review software we intended to distribute." (McKusick Decl. at 8.) Plaintiff allegedly refused to cooperate, although it had performed similar services for others.

Berkeley's decision to excise AT&T's code was motivated by several related concerns. First, the University of California received substantial benefits by being the center of UNIX software development, benefits that would increase if it could expand the family of UNIX users by extending UNIX to non-licensees (Ibid.); second, the cost of an AT&T UNIX license had increased to around $200,000, excluding all but the largest users (Ibid.); third, the Net2 version of UNIX would offer new and improved services (Keith Bostic, Marshall K. McKusick, & Michael J. Karels, Berkeley UNIX Yesterday, Today and Tomorrow, in Kennedy Aff. Ex. 8); and finally, the CSRG programmers, at least those who founded BSDI (Karels, McKusick, and Bostic), presumably saw in Net2 an opportunity to profit from the widespread interest in UNIX-like systems.

The end result of Berkeley's efforts was a product that, by all accounts, contains a very small proportion of 32V code. But this is not to say that Net2 fails to display its 32V roots. Plaintiff hired Professor John Carson to unearth these roots and, after over 400 hours of digging, Professor Carson has now identified a number of instances where 32V code is embedded in the Net2 system. (Carson Aff. at 13.) The legal significance of this code is, of course, a matter of dispute.

To begin with, it is important to compare Net2 side-by-side with 32V. Net2 has far outgrown 32V and now weighs in at nearly ten times the size of its parent. The alleged overlaps between parent and child probably amount to less than a percent of the total. (Joint Decl. at 12, 13.) Indeed, ignoring header files and comments (see below), the overlap in the critical "kernel" region is but 56 lines out of 230,9995, and the overlap elsewhere is 130 lines out of 1.3 million. However, as both sides argue (but to different effect), the nature of the overlap is more significant than its size.

According to Professor Carson, eighty of the 8,000 Net2 files are "littered with textual references which are or (sic) identical or substantially similar to corresponding textual matter in the UNIX/32V source code." (Ibid.) These textual overlaps include variable and parameter names, function names, the text of noncoding comments, and the actual sequence of the instruction code itself. (Id. at 23.) Most of these textual references are concentrated in files in the "kernel" of Net2, "which forms the central core of the operating system-" (Id. at 14.)

In summary, Professor Carson has examined the traits shared by Net2, BSD/386, and 32V, and detected a common lineage. Defendants argue that virtually all of these traits reflect publicly available code, copied comments, or overlap dictated by compatibility with industry standards. Professor Carson disagrees, and has allegedly identified at least some overlapping files that are irrelevant to program interfacing. (Carson Reply Aff. at 6(d), 8-15.)

Berkeley began licensing and distributing Net2 in June 1991. Plaintiff has alleged that the "highest levels," meaning persons reporting directly to the Regents, approved Net2's release. (E.g. Proposed 2d Am. Compl. at 2, 9, 38, 64, 72, 89, 103.) Indeed, Plaintiff has alleged that the University Chancellor himself approved Net2's release. (Kennedy Aff. 16.)

In soliciting new licensees, Berkeley distributed promotional materials stating that Net2 "may be freely redistributed. It is available to anyone and requires no previous license, either from AT&T or The Regents of the University of California." (Bostic Dep. at 76, Kennedy Aff. Ex. 3K.) According to Mr. Bostic, a member of CSRG, promotional materials were mailed to firms in New Jersey, although no New Jersey firms were among the approximately 120 firms that signed a licensing agreement to use Net2.

An early Net2 licensee was UUNET, an electronic information exchange for people interested in UNIX. (Adams Dep. at 149, Kennedy Aff. Ex. 12. UUNET added Net2 to its standard archives, enabling any subscriber to UUNET to freely and anonymously copy Net2 to their own computer system. When asked the number of people who had copied Net2 from UUNET, Mr. Bostic replied that "I've been told it's in the tens of thousands." (Bostic Dep. at 81, Id.). UUNET is available to hundreds of thousands of users worldwide, including users in New Jersey.

One organization that obtained Net2 from UUNET was BSDI. (Adams Dep. at 149, Kennedy Aff. Ex. 12.) BSDI, which is not licensed by AT&T to use UNIX, used Net2 to create its sole product, the operating system BSD/386 Source. (Ans. & Countercl. at 5-6.) BSDI is now close to bringing BSD/386 to market, having distributed preliminary "alpha," "beta," and "gamma" versions of BSD/386 as well as promotional literature. This literature states that BSD/386 Source "contains no AT&T licensed code" and "does not require a license from AT&T." (1st Am. Compl. Ex. I.)

## II. PROCEDURAL HISTORY

Plaintiff filed its complaint in this action on April 20, 1992. On April 29, the parties agreed to a court-
