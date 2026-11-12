# FreeBSD Architecture Handbook · Chapter 12 Common Access Method SCSI Controllers（网页抓取件）

- 来源 URL：https://docs.freebsd.org/en/books/arch-handbook/scsi/
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 用途：Task 8.2 G4 · V37.4.11.2“适配器抽象的工程效应”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

CAM stands for Common Access Method. It is a generic way to address the I/O buses in a SCSI-like way. This allows a separation of the generic device drivers from the drivers controlling the I/O bus: for example the disk driver becomes able to control disks on both SCSI, IDE, and/or any other bus so the disk driver portion does not have to be rewritten (or copied and modified) for every new I/O bus. Thus the two most important active entities are:

- Peripheral Modules - a driver for peripheral devices (disk, tape, CD-ROM, etc.)
- SCSI Interface Modules (SIM) - a Host Bus Adapter drivers for connecting to an I/O bus such as SCSI or IDE.

A peripheral driver receives requests from the OS, converts them to a sequence of SCSI commands and passes these SCSI commands to a SCSI Interface Module. The SCSI Interface Module is responsible for passing these commands to the actual hardware (or if the actual hardware is not SCSI but, for example, IDE then also converting the SCSI commands to the native commands of the hardware).

## 说明

节选 12.2 节 General Architecture 首三段；12.3 起为实现代码示例，本批未引。
