# Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable

- **著录（GB/T 7714-2015）**：McKusick, M. K. "Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable." Open Sources: Voices from the Open Source Revolution. O'Reilly, 1999.
- **来源 URL**：https://www.oreilly.com/openbook/opensources/book/kirkmck.html
- **访问日期**：2026-08-04
- **说明**：本条目为联网考据新增/补录的参考文献，原件（PDF/HTML）未在本库下载，仅保留权威来源链接与著录信息，供大纲章节与存疑数据库交叉引用。内容核验遵循零信任原则，拒绝 Wikipedia/Baidu 作证据源。

## 与 1994 年和解相关的段落（2026-11-13 逐字节录）

> 节录自 Open Books 全文页同一 URL；节录范围限于 "The Lawsuit" 与 "4.4BSD" 两节，逐字照录（含原文 `talks proceed slowly` 等语病）。全文另存 `04-现代研究文献/03-文献下载/01-pdf/_literature/TwentyYearsOfBerkeleyUnix_McKusick_1999.txt`（库内 ref3778）。

At the preliminary hearing for the injunction, BSDI contended that they were simply using the sources being freely distributed by the University of California plus six additional files. They were willing to discuss the content of any of the six added files, but did not believe that they should be held responsible for the files being distributed by the University of California. The judge agreed with BSDI's argument and told USL that they would have to restate their complaint based solely on the six files or he would dismiss it. Recognizing that they would have a hard time making a case from just the six files, USL decided to refile the suit against both BSDI and the University of California.

In December 1992, Dickinson R. Debevoise, a United States District Judge in New Jersey, heard the arguments for the injunction. Although judges usually rule on injunction requests immediately, he decided to take it under advisement. On a Friday about six weeks later, he issued a forty-page opinion in which he denied the injunction and threw out all but two of the complaints. The remaining two complaints were narrowed to recent copyrights and the possibility of the loss of trade secrets. He also suggested that the matter should be heard in a state court system before being heard in the federal court system.

The University's suit claimed that USL had failed in their obligation to provide due credit to the University for the use of BSD code in System V as required by the license that they had signed with the University.

Soon after the filing in state court, USL was bought from AT&T by Novell. The CEO of Novell, Ray Noorda, stated publicly that he would rather compete in the marketplace than in court. By the summer of 1993, settlement talks had started. Unfortunately, the two sides had dug in so deep that the talks proceed slowly. With some further prodding by Ray Noorda on the USL side, many of the sticking points were removed and a settlement was finally reached in January 1994. The result was that three files were removed from the 18,000 that made up Networking Release 2, and a number of minor changes were made to other files. In addition, the University agreed to add USL copyrights to about 70 files, although those files continued to be freely redistributed.

The newly blessed release was called 4.4BSD-Lite and was released in June 1994 under terms identical to those used for the Networking releases. Specifically, the terms allow free redistribution in source and binary form subject only to the constraint that the University copyrights remain intact and that the University receive credit when others use the code. Simultaneously, the complete system was released as 4.4BSD-Encumbered, which still required recipients to have a USL source license.

The lawsuit settlement also stipulated that USL would not sue any organization using 4.4BSD-Lite as the base for their system. So, all the BSD groups that were doing releases at that time, BSDI, NetBSD, and FreeBSD, had to restart their code base with the 4.4BSD-Lite sources into which they then merged their enhancements and improvements.

The final set of changes was released as 4.4BSD-Lite, Release 2 in June 1995.

Following the release of 4.4BSD-Lite Release 2, the CSRG was disbanded.
