# Introduction to IBM System Storage N series Data ONTAP 8.0（IBM Redpaper）引用卡

> 用途：V71.2.2.2／2.2.5／2.3.2 内容补证（G8-S2 V71 b017 起）。

## 一、著录

IBM Redbooks. Introduction to IBM System Storage N series Data ONTAP 8.0（IBM Redpaper redp4671）[R/OL]. IBM, 2010[2026-11-13]. https://www.redbooks.ibm.com/redpapers/pdfs/redp4671.pdf.

- 责任者：IBM Redbooks（厂商技术出版物，围绕 NetApp 提供技术支持的 N series 产品）
- 载体：PDF 技术红皮书（36 页）；`source_tier=primary`（厂商技术文档，机构自述）
- 出版年：2010（PDF 页脚“© Copyright IBM Corp. 2010”）
- 访问日：2026-11-13
- 说明：红皮书讲述 Data ONTAP 8.0 的系统结构、7-mode 与 cluster-mode、术语定义；引文照录。

## 二、逐字引文（英文，未翻译）

WAFL 与 FreeBSD 的组合来源：

> Data ONTAP GX was created as a combination of the WAFL® file system and SpinFS running in a FreeBSD environment.

系统与文件系统的分离式创新：

> the clean separation of the operating system from the file system allows for focused innovation within the file system itself

8.0 的平台归一：

> Data ONTAP 8.0 brings Data ONTAP 7G and Data ONTAP GX together into a single storage operating system, also running on FreeBSD.

术语表对 FreeBSD 的定位：

> FreeBSD: FreeBSD is now the Data ONTAP foundation.

以 FreeBSD 为操作系统的收益句（b029 补录）：

> The use of FreeBSD as the operating system for Data ONTAP 8.0 allows for some significant benefits. Besides the fact that Data ONTAP will continuously benefit from the third-party work taking place within the FreeBSD community

## 三、考据说明

- “combination of the WAFL file system and SpinFS running in a FreeBSD environment”是 2.3.2“WAFL 与 BSD 内核并置而非派生”的直接原文：组合体由两个来源拼成，WAFL 不是 BSD 内核演化的产物。
- “clean separation of the operating system from the file system”说明并置关系为何能维持：两套维护线各自演进，这是 2.2.2／2.3.2 的机制句。
- 术语表条目“FreeBSD is now the Data ONTAP foundation”是技术文档公开承认基础层的强形式（定义性陈述），支撑 2.2.5。
- 按 L3 采信；IBM 技术红皮书，所述对象为 NetApp 产品，属转述而非 NetApp 自述，引用时注明文书主体。
