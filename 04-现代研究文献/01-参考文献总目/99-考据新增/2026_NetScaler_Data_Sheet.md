# NetScaler Data Sheet（官方产品数据表）引用卡

> 用途：V71.1.4.3“BLX 形态的 Linux 原生进程”内容补证（G8-S2 V71 b002）；b010 补录形态与能力表述（供 1.7.1／1.7.2／1.7.5）。

## 一、著录

Citrix Systems. NetScaler Data Sheet[R/OL]. Citrix Systems, （日期不详）[2026-11-12]. https://www.citrix.com/content/dam/netscaler/documents/data-sheet/netscaler-data-sheet.pdf.

- 责任者：Citrix Systems（厂商产品数据表）
- 载体：PDF（数据表）；`source_tier=primary`（厂商官方产品材料）
- 访问日：2026-11-12
- 说明：数据表列各形态定位；引文照录英文原文。

## 二、逐字引文（英文，未翻译）

BLX 的进程形态：

> NetScaler BLX for bare metal runs as a Linux process on your hardware of choice. Because NetScaler BLX is a lightweight software package with no hypervisor or container overhead, you get extraordinarily fast performance.

形态与能力为中心的表述（b010 补录）：

> NetScaler MPX is a physical form factor that provides powerful hardware-based application delivery and load balancing with options for high performance web application security and SSL offload support.

> NetScaler SDX introduces fully isolated multi-tenant support on a single appliance for application workloads and groups.

## 三、考据说明

- “runs as a Linux process”是 1.4.3 题面的直接表述；与 FAQ 的“native application”互为两文献。
- 数据表另称 NetScaler“built on a single operating system”，指管理面统一，不等于各形态内核底座相同；与 1.4.4“底座随形态而分”并存，落块时不作“底座统一”解读。
- 按 L3 采信；产品宣传材料，性能类形容不入 claim。
- b010 补录：数据表以“形态（MPX／SDX／VPX／CPX／BLX）＋能力＋许可”组织全文，MPX／SDX 两段通篇讲硬件与多租户能力、未出现底层操作系统名称；“产品介绍层不见系统之名”的判读据此段与全文通读得出（详见批记 b010 考据说明），不作为单句引文的字面结论。
