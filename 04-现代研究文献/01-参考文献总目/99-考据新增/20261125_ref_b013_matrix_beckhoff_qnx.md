# supp-V57-b013 引文卡（Matrix 新闻稿／Beckhoff 案例／QNX io-sock／基金会案例总目）

- **批次**：Task 8.2 G6 全责线 V57 b013（5.2.1—5.2.5）
- **取证日期**：2026-11-25
- **用途**：V57 第 5 章 5.2 节五题 D2 块；Matrix 新闻稿与 QNX 文档为新 ref，Beckhoff（ref 992）与 Netflix（ref 10479）为库内复用。
- **披露**：英文引文逐字照录，弯撇号与连字符保持原样；ref 992 库内著录题名过简（Beckhoff-CASE-STUDY-5），块内改按实际题名与基金会 URL 著录，ref 身份不变；QNX 页更新日期 2026-11-05，抓取日 2026-11-25。

## 一、FreeBSD 新闻稿（1999-04-22）

- **著录**：FREEBSD PROJECT. FreeBSD Used to Generate Spectacular Special Effects[EB/OL]. (1999-04-22)[2026-11-25]. https://www.freebsd.org/press/press-rel-1.
- **URL**：https://www.freebsd.org/press/press-rel-1
- **tier**：primary（FreeBSD 项目官方新闻稿，含当事人直接引语）
- **引文 P1**：

> We came to a point in the production where we realized we just did not have enough computing power on our existing SGI infrastructure to get through the 3-D intensive sequences. It was at that point we decided on going with a FreeBSD based solution, due to the ability to get the hardware quickly as well as the reliability and ease of administration that FreeBSD provides us.

- **引文 P2**：

> Working with Dell, we purchased 32 of these systems on a Wednesday, and had them rendering in production by Saturday afternoon.

- **引文 P3**：

> 32 Dual-Processor FreeBSD systems were used to generate a large number of special effects in the cutting edge Warner Brothers film, The Matrix.

- **引文 P4**：

> Manex Visual Effects used 32 Dell Precision 410 Dual P-II/450 Processor systems running FreeBSD as the core CG Render Farm.

## 二、Beckhoff 案例（ref 992，库内复用）

- **著录**：FREEBSD FOUNDATION. Beckhoff Achieves a Smaller Footprint by Switching from Windows CE to FreeBSD[EB/OL]. [2026-11-25]. https://freebsdfoundation.org/end-user-stories/beckhoff-case-study-2/.
- **库内 ref**：992（原题名 Beckhoff-CASE-STUDY-5；块内按实际题名著录，身份不变）
- **引文 B1**：

> With end-of-life for Windows CE on the horizon, Beckhoff needed a non-GPL, stable, secure, and high-performance OS that supports the full range of hardware in their line from ARM to Xeon.

- **引文 B2**：

> Beckhoff implemented TwinCAT/BSD across all its industrial appliances, offering a best-of-both-world solution between its proprietary TwinCAT real-time and an industrially proven OS in FreeBSD.

- **引文 B3**：

> Beckhoff was able to decrease its operating system footprint by almost seven times – from 1.5 gigabytes to 500 megabytes.

- **引文 B4**：

> Because FreeBSD doesn’t include processes that aren’t needed, Beckhoff can reduce its use to about 200 megabytes of RAM usage, according to Heiko Wilke, leaving much more room for...

## 三、QNX io-sock 文档（两页，新 ref）

- **著录 Q1**：QNX SOFTWARE SYSTEMS. High-Performance Networking Stack (io-sock) User's Guide — Overview[EB/OL]. (2026-11-05)[2026-11-25]. https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.io_sock/topic/overview.html.
- **著录 Q2**：QNX SOFTWARE SYSTEMS. Networking APIs — High-Performance Networking Stack (io-sock) User's Guide[EB/OL]. (2026-11-05)[2026-11-25]. https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.io_sock/topic/socket_api.html.
- **tier**：primary（厂商官方文档）

- **引文 Q1**：

> The io-sock networking stack is designed to follow the FreeBSD networking stack code base and architecture as closely as possible.

- **引文 Q2**：

> The io-sock networking stack provides socket functions ported from FreeBSD as well as io-sock-specific ones.

## 四、FreeBSD 基金会 end-user-stories 与 Netflix 案例

- **著录 F**：FREEBSD FOUNDATION. End User Stories[EB/OL]. [2026-11-25]. https://freebsdfoundation.org/end-user-stories/.
- **引文 F1**：

> Read how organisations are using FreeBSD across the globe

- **引文 F2**：

> From enterprise to individuals. From mission-critical to servers to laptops. See how users are leveraging the power of FreeBSD for security, performance, and scalability.

- **著录 N**：FREEBSD FOUNDATION. Maintaining the World’s Fastest Content Delivery Network at Netflix on FreeBSD[EB/OL]. (2024-11-01)[2026-11-25]. https://freebsdfoundation.org/end-user-stories/netflix-case-study/.
- **库内 ref**：10479（复用）
- **引文 N1**：

> Netflix adopted FreeBSD-CURRENT for its Open Connect CDN, aligning closely with the FreeBSD community and staying at the forefront of system development. This strategic decision allowed Netflix to develop and maintain a customized FreeBSD implementation, enabling deep system-level optimizations and continuous enhancements tailored to their CDN’s needs.

> **自反性声明**：本卡是引文的形式化载体，不声称穷尽上述页面；引文逐字照录，断句与外文拼写以原页为准，落块时不得改写。
