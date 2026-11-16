<!-- 网页条目卡｜Marc J. Rochkind, The Source Code Control System, IEEE TSE 1975｜本卡为 Task 8.2 G1 V05 b005 联网补证批引文载体 -->

# The Source Code Control System（Rochkind，1975）

作者原站 PDF（`https://www.mrochkind.com/aup/talks/SCCS-Slideshow.pdf`）在本机 TLS 握手失败、WebFetch 通道亦不可达；引文取自搜索引擎对该 PDF 的文本转录，并与 ACM Digital Library 记录（`https://dl.acm.org/doi/abs/10.1109/TSE.1975.6312866`）的摘要逐句核对一致。出版项：IEEE Transactions on Software Engineering, 1975, SE-1(4):364–370, DOI 10.1109/TSE.1975.6312866。

## 逐字原文（摘要）

The Source Code Control System (SCCS) is a software tool designed to help programming projects control changes to source code. It provides facilities for storing, updating, and retrieving all versions of modules, for controlling updating privileges, for identifying load modules by version number, and for recording who made each software change, when and where it was made, and why.

There are two implementations of SCCS: one for the IBM 370 under the OS and one for the PDP 11 under UNIX.

## 逐字原文（引言，问题清单）

COMPUTER programs are always changing. There are bugs to fix, enhancements to add, and optimizations to make. … The most serious are the following.

1) The amount of space to store the source code (whether on disk, tape or cards) may be several times that needed for any particular version. For example, there might be “customer,” “system test,” and “development” source libraries, with most modules represented by a different version in each.

2) Fixes made to one version of a module sometimes fail to get made to other versions.

3) When changes occur it is difficult to tell exactly what changed and when.

4) When a customer has a problem it is hard to figure out what version he has.

## 逐字原文（特性清单）

Storage: All versions of a module are stored together in the same file. Source code common to more than one version is not duplicated. All versions are accessible.

Protection: A programmer may be restricted to updating only designated modules, and only designated versions of those. The only access to a module is through SCCS.

Identification: The system automatically stamps load modules with information such as version number, date, time, etc.

Documentation: The system automatically records who made each change, what it was, where it was made, when it was made and why.

## 著录

Marc J. Rochkind. The Source Code Control System[J]. IEEE Transactions on Software Engineering, 1975, SE-1(4): 364–370. DOI: 10.1109/TSE.1975.6312866.（引文取自原站 PDF 的检索转录，ACM 摘要交叉核对；访问日 2026-11-16。）
