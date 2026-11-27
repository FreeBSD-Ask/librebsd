# Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable

- **著录（GB/T 7714-2015）**：McKusick, M. K. "Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable." Open Sources: Voices from the Open Source Revolution. O'Reilly, 1999.
- **来源 URL**：https://www.oreilly.com/openbook/opensources/book/kirkmck.html
- **访问日期**：2026-08-04
- **说明**：本条目为联网考据新增/补录的参考文献，原件（PDF/HTML）未在本库下载，仅保留权威来源链接与著录信息，供大纲章节与存疑数据库交叉引用。内容核验遵循零信任原则，拒绝 Wikipedia/Baidu 作证据源。

## 与 1994 年和解相关的段落（2026-11-13 逐字节录）

> 节录自 Open Books 全文页同一 URL；节录范围限于 "The Lawsuit" 与 "4.4BSD" 两节，逐字照录（含原文 `talks proceed slowly` 等语病）。全文另存 `04-现代研究文献/03-文献下载/01-pdf/_literature/TwentyYearsOfBerkeleyUnix_McKusick_1999.txt`（库内 ref3778）。

In addition to the groups organized to freely redistribute systems built around the Networking Release 2 tape, a company, Berkeley Software Design, Incorporated (BSDI), was formed to develop and distribute a commercially supported version of the code. Like the other groups, they started by adding the six missing files that Bill Jolitz had written for his 386/BSD release. BSDI began selling their system including both source and binaries in January 1992 for $995.

At the preliminary hearing for the injunction, BSDI contended that they were simply using the sources being freely distributed by the University of California plus six additional files. They were willing to discuss the content of any of the six added files, but did not believe that they should be held responsible for the files being distributed by the University of California. The judge agreed with BSDI's argument and told USL that they would have to restate their complaint based solely on the six files or he would dismiss it. Recognizing that they would have a hard time making a case from just the six files, USL decided to refile the suit against both BSDI and the University of California.

In December 1992, Dickinson R. Debevoise, a United States District Judge in New Jersey, heard the arguments for the injunction. Although judges usually rule on injunction requests immediately, he decided to take it under advisement. On a Friday about six weeks later, he issued a forty-page opinion in which he denied the injunction and threw out all but two of the complaints. The remaining two complaints were narrowed to recent copyrights and the possibility of the loss of trade secrets. He also suggested that the matter should be heard in a state court system before being heard in the federal court system.

The University's suit claimed that USL had failed in their obligation to provide due credit to the University for the use of BSD code in System V as required by the license that they had signed with the University.

Soon after the filing in state court, USL was bought from AT&T by Novell. The CEO of Novell, Ray Noorda, stated publicly that he would rather compete in the marketplace than in court. By the summer of 1993, settlement talks had started. Unfortunately, the two sides had dug in so deep that the talks proceed slowly. With some further prodding by Ray Noorda on the USL side, many of the sticking points were removed and a settlement was finally reached in January 1994. The result was that three files were removed from the 18,000 that made up Networking Release 2, and a number of minor changes were made to other files. In addition, the University agreed to add USL copyrights to about 70 files, although those files continued to be freely redistributed.

The newly blessed release was called 4.4BSD-Lite and was released in June 1994 under terms identical to those used for the Networking releases. Specifically, the terms allow free redistribution in source and binary form subject only to the constraint that the University copyrights remain intact and that the University receive credit when others use the code. Simultaneously, the complete system was released as 4.4BSD-Encumbered, which still required recipients to have a USL source license.

The lawsuit settlement also stipulated that USL would not sue any organization using 4.4BSD-Lite as the base for their system. So, all the BSD groups that were doing releases at that time, BSDI, NetBSD, and FreeBSD, had to restart their code base with the 4.4BSD-Lite sources into which they then merged their enhancements and improvements.

The final set of changes was released as 4.4BSD-Lite, Release 2 in June 1995.

Following the release of 4.4BSD-Lite Release 2, the CSRG was disbanded.

## supp-V73-b002 追加引文（2026-11-27，库内全文 txt ref3778 逐字；O'Reilly 官方页同文 Tavily extract 2026-11-27 复核）

> With Ken Thompson's departure at the end of the summer of 1976, Joy and Haley begin to take an interest in exploring the internals of the Unix kernel. Under Schriebman's watchful eye, they first installed the fixes and improvements provided on the "fifty changes" tape from Bell Labs.

> Thompson's remote debugging was the first example of the cooperation that sprang up between Berkeley and Bell Labs. The willingness of the researchers at the Labs to share their work with Berkeley was instrumental in the rapid improvement of the software available at Berkeley

> Although we did not yet have the complete feature set of 4.4BSD ready to ship, the CSRG decided to do an interim release to get additional feedback and experiences on the two major new additions to the system.

> This licensed interim release was called 4.3BSD-Reno and occurred in early 1990. The release was named after a big gambling city in Nevada as an oblique reminder to its recipients that running the interim release was a bit of a gamble.

- **考据注**：四句均出 Early History／4.3BSD-Reno 两节（当事人事后追述，L4）。第 1 句＝Thompson 1976 夏离任后 Joy／Haley 接手内核探索，先装 Bell Labs "fifty changes" 带——早期改动以"改动带"传递的直接记录（1.2.2／1.5.3）；第 2 句＝远程调试为 Berkeley 与 Bell Labs 合作首例（1.5.3）；第 3／4 句＝Reno 过渡发行性质与赌城命名（1.5.4，引文至 gamble 止）。
- **本批落点**：V73.1.2.2（第 1 句）、1.5.3（第 1／2 句）、1.5.4（第 3／4 句）
- **考据日期**：2026-11-27（supp-V73-b002；academic_work 表定抬头／L4）


## supp-V73-b007 追加四句（2026-11-28，库内全文 txt ref3778 逐字）

> They began running advertisements touting their 99% discount over the price charged for System V source plus binary systems. Interested readers were told to call 1-800-ITS-Unix.

> The letter demanded that they stop promoting their product as Unix and in particular that they stop using the deceptive phone number.

> Although the phone number was promptly dropped and the advertisements changed to explain that the product was not Unix, USL was still unhappy and filed suit to enjoin BSDI from selling their product.

> That was because the BSD systems were never released by Berkeley in a binary-only format; the distributions always contained the complete source to every part of the system.

- **考据注**：前两句＝BSDI 广告叙事（99% 折扣＋1-800-ITS-Unix 电话）；第三句＝电话成为诉讼焦点后广告改写；第四句＝BSD 从不以二进制形态发行、始终含全部源码（归属与署名迁移的制度底座）。落 V73 3.4.2／3.4.3／3.4.5／3.3.2。
- **考据日期**：2026-11-28（supp-V73-b007）


## supp-V73-b008 追加二句（2026-11-28，库内全文 txt ref3778 逐字）

> Under the auspices of this contract, Bob Fabry sets up an organization which was christened the Computer Systems Research Group, or CSRG for short.

> He immediately hired Laura Tong to handle the project administration.

- **考据注**：CSRG 建组句（DARPA 合同名义下 Fabry 建组命名）与行政职员雇用句；落 V73 3.9.1 大学任职与项目声名两块。
- **考据日期**：2026-11-28（supp-V73-b008）

