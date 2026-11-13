# A General-Purpose File System for Secondary Storage（Daley & Neumann 1965）

- 来源：https://multicians.org/fjcc4.html
- 作者：Robert C. Daley, Peter G. Neumann
- 出处：1965 Fall Joint Computer Conference（multicians.org 转录本）
- 访问日：2026-11-13
- 用途：Task 8.2 V01-S2 b015，V01.1.7.2.4 文件系统的层次结构（D2 网页条目，1965 年同时代论文）
- 摘录说明：curl 抓取 HTML 转录本后去标签转纯文本，逐字摘录

## 正文摘录（逐字）

"This formulation provides the user with a simple means of addressing an essentially infinite amount of secondary storage in a machine-independent and device independent fashion."

"The basic structure of the file system is independent of machine considerations. Within a hierarchy of files, the user is aware only of symbolic addresses. All physical addressing of a multilevel complex of secondary storage devices is done by the file system, and is not seen by the user."

"The file structure consists of a basic tree hierarchy of files, across which links may be added to facilitate simple access to files elsewhere in the hierarchy. Each file has an independent means for controlling the way in which it may be used."

## 提要

1965 年 Daley 与 Neumann 记：该文件系统方案使用户得以机器无关、设备无关地寻址“近乎无限”的二级存储；文件系统的基本结构不依赖具体机器，在文件层次中用户只见符号地址，多级存储设备的物理寻址全由文件系统承担；文件结构为基本树形层次，可在其上加链接以便访问别处文件，且每个文件各有独立的“可如何使用”控制方式。
