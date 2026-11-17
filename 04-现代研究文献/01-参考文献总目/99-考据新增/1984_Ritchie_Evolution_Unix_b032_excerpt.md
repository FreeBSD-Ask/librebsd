# The Evolution of the Unix Time-sharing System（Ritchie 1984）——b032 专用摘录卡

- 来源：https://www.read.seas.harvard.edu/~kohler/class/aosref/ritchie84evolution.pdf
- 库内本体：ref878（`fulltext_blocks` 已入库、ocr verified），复用既有 ref id，不新建文献行
- 作者：Dennis M. Ritchie
- 出处：AT&T Bell Laboratories Technical Journal, Vol. 63, No. 6, Part 2, pp. 1577-1593（1984）
- 访问日：2026-11-17
- 用途：Task 8.2 V01-S2 b032，V01.7.6 节六题（D1 全文库块，当事人一手追述）
- 摘录说明：逐字取自库内 `references_fulltext.fulltext_blocks`（ref878，block_index 3／9／19）。英文原文含 1979/1984 年拼写与排字，逐字照录。

## 正文摘录（逐字）

### 块 3（寻找替代品、文件系统的诞生、Ritchie 论设备文件）

> Throughout 1969 we (mainly Ossanna, Thompson, Ritchie) lobbied intensively for the purchase of a medium-scale machine for which we promised to write an operating system; the machines we suggested were the DEC PDP-10 and the SDS (later Xerox) Sigma 7.

> We knew from experience that the essence of communal computing, as supplied by remote-access, time-shared machines, is not just to type programs into a terminal instead of a keypunch, but to encourage close communication.

> Thompson, R. H. Canaday, and Ritchie developed, on blackboards and scribbled notes, the basic design of a file system that was later to become the heart of Unix. Most of the design was Thompson's, as was the impulse to think about file systems at all, but I believe I contributed the idea of device files.

### 块 9（进程控制与文件系统对照、shell 的用户级实现）

> By 'process control,' I mean the mechanisms by which processes are created and used; today the system calls fork, exec, wait, and exit implement these mechanisms. Unlike the file system, which existed in nearly its present form from the earliest days, the process control scheme underwent considerable mutation after PDP-7 Unix was already in use.

> Crucial to subsequent development was the implementation of the shell as a user-level program stored in a file, rather than a part of the operating system.

### 块 19（管道思想非全新、Dartmouth communication files、1972 年）

> One of the most widely admired contributions of Unix to the culture of operating systems and command languages is the pipe, as used in a pipeline of commands. Of course, the fundamental idea was by no means new; the pipeline is merely a specific form of coroutine. Even the implementation was not unprecedented, although we didn't know it at the time; the 'communication files' of the Dartmouth Time-Sharing System [10] did very nearly what Unix pipes do, though they seem not to have been exploited so fully.

> Pipes appeared in Unix in 1972, well after the PDP-11 version of the system was in operation, at the suggestion (or perhaps insistence) of M. D. McIlroy, a long-time advocate of the non-hierarchical control flow that characterizes coroutines.

## 提要

Ritchie 1984 年追述 UNIX 早期设计与 Multics 影响的复杂关系：1969 年小组游说购买中型机（PDP-10／Sigma 7）以替代 Multics；文件系统自早期即近今貌而进程控制几经变化，shell 作为用户级程序的实现至为关键；管道思想并非 UNIX 首创，Dartmouth 分时系统的“通信文件”已近其事，管线 1972 年才在 McIlroy 倡议下进入 UNIX。均为当事人一手追述，作过程性证据。
