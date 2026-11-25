# ref-new 考据登记（2026-11-25，supp-V36-p2-b017）

- **标题**：MS Windows NT Kernel-mode User and GDI White Paper（Windows NT 4.0 内核态 User／GDI 白皮书）
- **作者**：Microsoft Corporation
- **年份**：1996（TechNet 归档件）
- **来源 URL**：https://learn.microsoft.com/en-us/previous-versions/cc750820(v=technet.10)
- **抓取日期**：2026-11-25（curl 实取 HTML，正文见下）
- **用途**：supp-V36-p2-b017／V36.2.9.2（NT 4.0 内核态图形子系统与服务器定位）
- **查重披露**：source_url 四键预检无命中；本条为微软官方白皮书归档，非第三方转述。

## 关键原文（逐字）

> With this new release, the Window Manager, GDI, and related graphics device drivers have been moved to the Windows NT Executive running in kernel mode. Both Window Manager and GDI now exist as Windows NT Executive system services.

> It is both incredibly robust and stable as an application server and workstation platform, yet fast and nimble from the perspective of core operating system services, such as virtual memory management, file I/O, networking, and file and print sharing.

> The objective of any high-end operating system, such as Windows NT, is to protect the system and other applications from errant applications.

## 中文提要

微软白皮书自述 NT 4.0 把 Window Manager、GDI 与图形驱动移入内核态 Executive，并以“application server and workstation platform”与“high-end operating system”自我定位；同页承认驱动整体入内核后缺陷可波及全系统——统一内核路线的收益与代价由厂商文档自陈。
