# kqueue 论文 PDF 卡：引言的问题起点表述（版本记录载体）

> 用途：V67.2.3.2“事件通知设施的问题起点”内容补证（V67 补证批 b018）。

## 一、著录

Jonathan Lemon. Kqueue: A generic and scalable event notification facility (full paper, PDF)[EB/OL]. 2001[2026-11-14]. https://www.usenix.org/legacy/events/usenix01/freenix01/full_papers/lemon/lemon.pdf.

- 责任者：Jonathan Lemon（FreeBSD Project）
- 载体：USENIX 2001 FREENIX 轨道论文全文 PDF（curl 直取 104,951 B；pdftotext 提取）
- `source_tier=primary`（学会官方存档件，一手）
- 访问日：2026-11-14
- 提取说明：PDF 排印连字（ﬁ／ﬂ，U+FB01 等）已归一为普通字母 fi／fl——属排印形态归一，非文字改动；跨行断词处已合并。

## 二、逐字引文（英文，未翻译；连字已归一）

1 Introduction（问题起点段）：

> FreeBSD provides two system calls for detecting activity on file descriptors, these are poll() and select(). However, neither of these calls scale very well as the number of descriptors being monitored for events becomes large. A high volume server that intends to handle several thousand descriptors quickly finds these calls becoming a bottleneck, leading to poor performance [1] [2] [10].

2 Problem（无状态设计根源）：

> These problems stem from the fact that poll() and select() are stateless by design; that is, the kernel does not keep any record of what the application is interested in between system calls and must recalculate it every time.

## 三、核对记录

- 本卡与 ref 10559（论文摘要页）为**同一论文的两种载体**（会序摘要页／全文 PDF）：题面“论文以 select 与 poll 在描述符增多时不可扩展作为问题起点”本即关于该论文自身表述，两载体分别证摘要与引言两处行文；独立性限度如实披露——第三方独立佐证（论文引用标注 [1][2][10]，含 Banga／Mogul 1998 一类先行工作）留扩展批。
- 摘要与引言措辞不同（“does not scale well with an increasing number of descriptors” vs “neither of these calls scale very well as the number of descriptors being monitored for events becomes large”），照录不合并。
- 第 2 节（Problem）的无状态根源句为 2.3.x 后续题面候选，本批未取。
- 文首版权行载 “Proceedings of the FREENIX Track: 2001 USENIX Annual Technical Conference, Boston, Massachusetts, USA June 25–30, 2001”。
