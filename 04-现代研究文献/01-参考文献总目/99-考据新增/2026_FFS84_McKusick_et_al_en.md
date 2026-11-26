# A Fast File System for UNIX（FFS84）引用卡

> 用途：V12.5.3 节（文件系统与 I/O 改进）六题内容补证（V12 补证批 b063）。学术论文（一手技术文献，L3）。

## 一、著录

McKusick, Marshall K.; Joy, William N.; Leffler, Samuel J.; Fabry, Robert S. A Fast File System for UNIX[J/OL]. ACM Transactions on Computer Systems, 1984, 2(3): 181-197[2026-11-27]. 课程镜像 PDF: http://people.eecs.berkeley.edu/~kubitron/courses/cs162-S15/sp15/static/readings/FFS84.pdf.

- 责任者：CSRG 四人（McKusick／Joy／Leffler／Fabry）
- 载体：PDF（1,311,515 B；pdftotext -layout 抽文 62,760 字符，存 `script/_g2_ffs84.txt`）
- `source_tier=primary`（技术论文，一手技术文献；L3 公开文献记载）
- 访问日：2026-11-27（curl 直取）
- 说明：论文第二节 “OLD FILE SYSTEM” 完整记述 4.1BSD 时期的文件系统改进（512→1024 字节块、staging 修改提高可靠性），是 V12.5.3 六题的直接技术史料。

## 二、逐字引文（英文，未翻译）

性能诉求（5.3.1A，VAX 应用需要吞吐）：

> When used on the VAX-11 together with other UNIX enhancements, the original 512-byte UNIX file system is incapable of providing the data throughput rates that many applications require. For example, applications such as very-large-scale integration (VLSI) design and image processing involve a small amount of processing on large quantities of data and need to have a high throughput from the file system.

块大小与带宽利用（5.3.2A，512→1024 翻倍但仍仅约 4%）：

> The file system performance was improved by a factor of more than two by changing the basic block size from 512 to 1024 bytes. There were two reasons for the increase: each disk transfer accessed twice as much data, and most files could be described without need to access indirect blocks since the direct blocks contained twice as much data. The file system with these changes will henceforth be referred to as the old file system.

磁盘组织次优（5.3.3A，512 字节传输与跨柱面 seek）：

> The allocation of data blocks to files is also suboptimum. The traditional file system never transfers more than 512 bytes per disk transaction and often finds that the next sequential data block is not on the same cylinder, forcing seeks between 512-byte transfers.

吞吐瓶颈诊断（5.3.4A，小块＋有限预读＋多 seek）：

> The combination of the small block size, limited read-ahead in the system, and many seeks severely limits file system throughput.

方案取舍（5.3.5A，块大小与间接块的双重理由）：

> The reliability was improved by staging modifications to critical file system information so that they could either be completed or repaired cleanly by a program after a crash.

实测支点（5.3.6A，仅约 2% 带宽／每臂约 20 KB/s）：

> This requires a file system providing higher bandwidth than the original 512-byte UNIX one that provides only about two percent of the maximum disk bandwidth or about 20 kilobytes per second per arm.

## 三、考据说明

1. 本论文由 CSRG 四人署名（1984），其第二节对“传统文件系统”（512 字节块）与“旧文件系统”（1024 字节块，4.1BSD 时期）的记述，是 4.1BSD 文件系统改进的**当事人技术文献**——对 V12.5.3 六题（性能诉求／通道改进／磁盘组织／瓶颈诊断／取舍留档／实测支点）逐题对应。
2. 论文的“old file system”指 4.1BSD 的 1024 字节块版本；“traditional file system”指 V7 的 512 字节块版本——引文措辞须区分两术语。
3. L3 纪律：技术论文为一手技术文献，但涉及动机与决策的判断须与当事人回忆（ref1575）交叉。
4. 禁引核查：课程镜像公开 PDF（原文 ACM TOCS），`banned_source=0`。
