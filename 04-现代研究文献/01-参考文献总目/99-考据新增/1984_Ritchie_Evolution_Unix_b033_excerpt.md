# The Evolution of the Unix Time-sharing System（Ritchie 1984）——b033 专用摘录卡

- 来源：https://www.read.seas.harvard.edu/~kohler/class/aosref/ritchie84evolution.pdf
- 库内本体：ref878（`fulltext_blocks` 已入库、ocr verified），复用既有 ref id，不新建文献行
- 作者：Dennis M. Ritchie
- 出处：AT&T Bell Laboratories Technical Journal, Vol. 63, No. 6, Part 2, pp. 1577-1593（1984）
- 访问日：2026-11-17
- 用途：Task 8.2 V01-S2 b033，V01.7.7 节六题（D1 全文库块，当事人一手追述）
- 摘录说明：逐字取自库内 `references_fulltext.fulltext_blocks`（ref878，block_index 1／9／17）。与 b032 摘录卡段落不重（本卡取比较史/交互服务/PDP-11 硬件到货段）。

## 正文摘录（逐字）

### 块 1（交互服务、技术社会史声明）

> More important, the convenient interactive computing service that Multics had promised to the entire community was in fact available to our limited group, at first under the CTSS system used to develop Multics, and later under Multics itself.

> This paper presents a technical and social history of the evolution of the system.

### 块 9（与同时代交互系统的结构对照、专用机制）

> The structure of this process control scheme, with one process per terminal, is similar to that of many interactive systems, for example CTSS, Multics, Honeywell TSS, and IBM TSS and TSO. In general such systems require special mechanisms to implement useful facilities such as detached computations and command files; Unix at that stage didn't bother to supply the special mechanisms.

### 块 17（PDP-11 到货与磁盘延迟）

> The processor arrived at the end of the summer, but the PDP-11 was so new a product that no disk was available until December. In the meantime, a rudimentary, core-only version of Unix was written using a cross-assembler on the PDP-7.

## 提要

Ritchie 1984 年追述中用于比较史的部分：Multics 承诺的便利交互服务先在 CTSS、后在 Multics 上向小组开放；早期 Unix 进程结构与 CTSS、Multics、Honeywell TSS、IBM TSS/TSO 相似，但当时 Unix 未提供后者所需的专用机制；PDP-11 太新，磁盘迟至 12 月到货，其间只能在 PDP-7 上写纯核心版 Unix。作者自陈兼写技术史与社会史。均为当事人一手追述，作过程性证据。
