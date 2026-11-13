# Installing and Operating 4.4BSD（CSRG 1993 安装操作手册）引文卡

- **著录（GB/T 7714-2015）**：MCKUSICK M K, BOSTIC K, KARELS M J, LEFFLER S J, HIBLER M. Installing and Operating 4.4BSD UNIX[R]. Berkeley: University of California, Berkeley, 1993-07-27.
- **库内 ref**：1615（PDF 本体在库，fulltext 129 块）
- **访问日期**：2026-11-14（引文取自库内全文块）
- **用途**：Task 8.2 G3-V24 P2 b004（发行物清单著录／源码树约定／完整性核验）

## 逐字引文

Q1（blk37，X11R5 发行带文件落位）:
it contains the sources for X11R5 in tar(1) format. As
distributed, X11R5 should be placed in/usr/src/X11R5.

Q2（blk37，安装规程以 /usr/src 为源码树根）:
# cd /usr/src
# mt -f /dev/nrmt0 fsf (space to end of previous tape file)
# tar xpbf 20 /dev/nrmt0 (extract the X11R5 source)

Q3（blk37，抽取后 fsck 核验指引）:
Having now completed the extraction of the sources, you may want to verify that your /usr/src
filesystem is consistent. To do so, you must unmount it, and run fsck(8);
