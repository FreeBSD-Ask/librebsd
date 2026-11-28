# ref-cacm2016 登记卡（V17 b001／b002 新登记：Lessons Learned from 30 Years of MINIX）

- **来源**：Tanenbaum, A. S. Lessons Learned from 30 Years of MINIX[J]. Communications of the ACM, 2016, 59(3). https://cacm.acm.org/research/lessons-learned-from-30-years-of-minix.
- **性质**：academic_work 类；source_tier=primary；first_hand=1／contemporary=0／retrospective=1。
- **取文途径**：Tanenbaum 2016 年 CACM 回顾（93 633 字符，2026-11-27 取文）。文内链接标记在引文截取处已避让（1.1.3 引文止于 platforms，不含 `(see [Figure 2]...)`）。
- **四键查重**：source_url（https://cacm.acm.org/research/lessons-learned-from-30-years-of-minix，references 表 0 命中）＋题名（0 命中）——新登记。
- **用途**：V17 第 1 章 b001／b002：V17.1.1.2、V17.1.1.3、V17.1.1.4、V17.1.2.1、V17.1.2.3、V17.1.2.4、V17.1.3.1、V17.1.3.5。

## 逐字引文池

1. [V17.1.1.2 用] Because early PCs did not have a hard disk, I designed MINIX to be V7 compatible yet run on an IBM PC with 256kB RAM and a single 360kB 5¼-inch floppy disk—a far smaller configuration than the PDP-11 V7 ran on.
2. [V17.1.1.3 用] By 1991, MINIX 1.5, had been ported to the Apple Macintosh, Amiga, Atari, and Sun SPARCstation, among other platforms
3. [V17.1.1.4 用] My idea was to write the system, called MIni-uNIX, or MINIX, for the new IBM PC, which was cheap enough (starting at $1,565) a student could own one.
4. [V17.1.2.1 用] In 1985, Intel released its 386 processor with a full protected-mode 32-bit architecture. With the help of many users, notably Bruce Evans of Australia, I was able to release a 32-bit protected mode version of MINIX.
5. [V17.1.2.3 用] in Amsterdam in order to provide a UNIX-compatible operating system my students could study in a course or on their own.
6. [V17.1.2.4 用] Within a few days of its release, a USENET newsgroup, comp.os.minix, was started.
7. [V17.1.3.1 用] So the next release, V7 (1979), came equipped with a license that explicitly forbade anyone from writing a book about it or teaching it to students.
8. [V17.1.3.5 用] Figuring out how to distribute the code was a big problem. In those days (1987) almost nobody had a proper Internet connection (though newsgroups on USENET via the UUCP program and email existed at some universities).

## 第 2 章追加引文池（b003／b004）

- [V17.2.1.2 用] Since I was always thinking about future hardware, from day 1, the code clearly distinguished what code ran in “kernel mode” and what code ran as separate processes in “user mode,” even though the 8088 had only one mode.
- [V17.2.1.3 用] like Lions did before me, and have my publisher, Prentice Hall, distribute the system, including all source code
- [V17.2.1.5 用] In 2000, I finally convinced Prentice Hall to release MINIX 2 under the BSD license and make it (including all source code) freely available on the Internet.
- [V17.2.1.6 用] My design goals for MINIX were as follows: * Build a V7 clone that ran on an IBM PC with only a single 360kB floppy disk; * Build and maintain the system using itself, or “self-hosting”
- [V17.2.2.4 用] Have a clean design students could easily understand
- [V17.2.2.5 用] Although the system was supposed to run on this configuration (and did), I realized from the start that to actually compile and build the whole system on a PC, I would need a larger system, namely one with the maximum possible RAM (640kB) and two 360kB 5¼-inch floppy disks.
- [V17.2.3.1 用] Before a month had gone by, it had 40,000 readers, a huge number considering how few people even had access to USENET. MINIX became an instant cult item.
- [V17.2.3.4 用] In 1997, MINIX 2, now changed to be POSIX-compatible rather than UNIX V7-compatible, was released, along with a second edition of my book _Operating Systems Design and Implementation_, now co-authored with Albert Woodhull, a professor at Hampshire College in Massachusetts.
