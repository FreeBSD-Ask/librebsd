# A Hardware Architecture for Implementing Protection Rings（Schroeder & Saltzer 1971）

- 来源：https://multicians.org/protection.html
- 作者：Michael D. Schroeder, Jerome H. Saltzer
- 出处：Third ACM Symposium on Operating System Principles, Palo Alto, 1971（multicians.org 转录本）
- 访问日：2026-11-13
- 用途：Task 8.2 V01-S2 b015，V01.1.7.2.3 保护环与访问控制（D2 网页条目，1971 年同时代论文）
- 摘录说明：curl 抓取 HTML 转录本后去标签转纯文本，逐字摘录

## 正文摘录（逐字）

"In a system which uses segmentation as a memory addressing scheme, protection can be achieved in part by associating concentric rings of decreasing access privilege with a computation."

"While containing special logic to support a segmented virtual memory, the 645 processor [10] provides only a limited set of access control mechanisms, forcing software intervention to implement protection rings."

"The new processor includes an improved set of access control mechanisms, described here, which implement rings almost completely in hardware."

"The role of protection in a computer utility is to control user interaction-guaranteeing total user separation when desired, allowing unrestricted user cooperation when desired, and providing as many intermediate degrees of control as will be useful."

## 提要

1971 年 Schroeder 与 Saltzer 记：在分段式内存寻址的系统中，保护可部分实现为“与计算关联的同心环、权限逐环递减”；GE-645 处理器虽含分段虚存逻辑，却只提供有限的访问控制机制，保护环须靠软件介入；新处理器改以硬件实现环式保护。该文并称，公用计算中保护的作用是控制用户交互：需要时完全隔离、需要时无限制协作，并提供尽可能多的中间控制层级。
