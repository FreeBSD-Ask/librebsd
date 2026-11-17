# The UNIX Time-Sharing System（Ritchie & Thompson 1974）b032 专用摘录卡

- 来源：https://www.read.seas.harvard.edu/~kohler/class/aosref/ritchie84evolution.pdf （CACM 1974 电子版，Eric A. Brewer 重制）
- 库内本体：ref869（`fulltext_blocks` 已入库），复用既有 ref id，不新建文献行
- 作者：Dennis M. Ritchie; Ken Thompson
- 出处：Communications of the ACM, 1974, 17(7): 365-375
- 访问日：2026-11-17
- 用途：Task 8.2 V01-S2 b032，V01.7.6.1（D1 全文库块，同期系统论文）
- 摘录说明：逐字取自库内 `references_fulltext.fulltext_blocks`（ref869，block_index 9）；原文含 1974 年排字连字符，摘录按语义连写，英文词形未改。

## 正文摘录（逐字）

### 块 9（文件系统三类）

> The most important job of UNIX is to provide a file system. From the point of view of the user, there are three kinds of files: ordinary disk files, directories, and special files.

## 提要

Ritchie 与 Thompson 1974 年 CACM 论文明确：UNIX 最重要的工作是提供文件系统，用户视角下有普通磁盘文件、目录与特殊文件三类。此为用户接口层的原始设计陈述（同期一手系统论文），可与 Ritchie 1984 年追述对照。
