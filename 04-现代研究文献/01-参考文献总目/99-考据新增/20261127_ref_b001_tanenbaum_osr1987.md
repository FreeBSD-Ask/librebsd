# ref-osr1987 登记卡（V17 b001／b002 新登记：A Unix Clone with Source Code for Operating Systems Courses）

- **来源**：Tanenbaum, A. S. A Unix Clone with Source Code for Operating Systems Courses[J]. ACM SIGOPS Operating Systems Review, 1987, 21(1): 20-29. DOI:10.1145/24592.24596.
- **性质**：academic_work 类；source_tier=primary；first_hand=1／contemporary=1／retrospective=0。
- **取文途径**：Tanenbaum 本人 1987 年 SIGOPS 论文（VU Research Portal 出版商版 PDF，31 747 字节，2026-11-27 取文）。OCR 伪影：`A T & T`（字母间空格）、`Is` 实为 `ls`、`( T a n e n b a u m , 1987)`（作者名字母间空格）、`welldocumented`（无连字符）；引文照录并在块 gate 披露。
- **四键查重**：source_url（https://research.vu.nl/files/111353126/11154，references 表 0 命中）＋题名（0 命中）——新登记。
- **用途**：V17 第 1 章 b001／b002：V17.1.1.1、V17.1.1.2、V17.1.1.5、V17.1.1.6、V17.1.3.1、V17.1.3.2、V17.1.3.3、V17.1.3.4、V17.1.3.5、V17.1.3.6。

## 逐字引文池

1. [V17.1.1.1 用] This system, now finished, is called MINIX and is functionally compatible with Version 7 of the UNIX system (i.e., has the same system calls).
2. [V17.1.1.2 用] Besides, MINIX was designed to run on a PC with or without a hard disk, to keep the necessary hardware cheap.
3. [V17.1.1.5 用] neither the operating system kernel, nor any of the utility programs (cat, cp, grep, Is, make, etc.) contain even a single line of A T & T code.
4. [V17.1.1.6 用] These have now been published as a 719 page book ( T a n e n b a u m , 1987).
5. [V17.1.3.1 用] Lions' commentary fell into disuse when A T & T changed the licensing agreement starting with Version 7 to prohibit using the UNIX code in courses.
6. [V17.1.3.2 用] The books and lecture material for most courses are already heavily skewed toward the few topics that can be pulled out of context and isolated, such as monitors, schedulers, and deadlock algorithms.
7. [V17.1.3.3 用] The only reasonable approach is to distribute to the students a working, welldocumented operating system that they can study in detail and then modify.
8. [V17.1.3.4 用] This strategy has the advantage that everybody passes. Unfortunately, nobody learns anything about operating systems this way.
9. [V17.1.3.5 用] Fortunately, substantial microcomputers have now become so inexpensive that acquiring 20 machines just for the operating systems lab is becoming a real possibility at many schools.
10. [V17.1.3.6 用] The source code listing of appendix E contains line numbers, and these line numbers are used throughout the book to pinpoint the code under discussion.

## 第 2 章追加引文池（b003／b004）

- [V17.2.1.1 用] Dept. of Mathematics and Computer Science Vrije Universiteit
- [V17.2.1.2 用] Unlike UNIX which is organized as a single monolithic program that is loaded into memory at system boot time and then run, the MINIX kernel itself is structured in a much more modular way, as a collection of processes that communicate with each other and with user processes by sending and receiving messages.
- [V17.2.1.3 用] To deal with this issue, I jotted down some notes.
- [V17.2.1.5 用] The software has been copyright by Prentice-Hall. It is not public domain. However, Prentice-Hall is permitting copies of both the binaries and sources to be made for educational use without requiring a license or payment.
- [V17.2.1.6 用] Faced with this problem for my own students, and seeing no solution in sight, several years ago I simply bit the bullet and sat down and wrote a new operating system for classroom use from scratch.
- [V17.2.2.1 用] In this way they get to see a whole system close up, without having to write all the code.
- [V17.2.2.2 用] Of the 719 pages, 253 are the kernel listing, in C.
- [V17.2.2.3 用] For courses on operating systems, it is much more difficult to arrange for a suitable programming laboratory.
- [V17.2.2.4 用] First comes a thorough treatment of the relevant principles (thorough enough to be usable as a university textbook on operating systems). Next comes a general discussion of how the principles have been applied in MINIX. Finally there is a procedure by procedure description of how the relevant part of MINIX works in detail.
- [V17.2.2.5 用] I have also written a complete IBM PC simulator in C, so that MINIX can be run on the simulator on top of UNIX on an ordinary time-sharing machine.
- [V17.2.2.6 用] Appendix E is a full listing of the operating system. The utilities (mercifully) are not listed.
- [V17.2.3.6 用] Studying the principles and seeing how they are applied in a real system gives the student a better understanding of the subject than either the principles or the code alone would.
