# The Magical Mystery Merge：Why we run FreeBSD-current at Netflix（OpenFest 2023，Drew Gallatin）引用卡

> 用途：V71.3.1／3.2／3.4／3.6／3.7 内容补证（G8-S2 V71 b020 起）。

## 一、著录

Gallatin, Drew. The Magical Mystery Merge, Or Why we run FreeBSD-current at Netflix[R/OL]. OpenFest, 2023-11[2026-11-13]. https://people.freebsd.org/~gallatin/talks/OpenFest2023.pdf.

- 责任者：Drew Gallatin（Netflix 工程师、FreeBSD committer）
- 载体：PDF 幻灯片（38 页）；`source_tier=primary`（当事人会议演讲，当事人一手材料）
- 访问日：2026-11-13
- 说明：演讲讲 OCA 的软件栈、OCA Dev 团队与上游合并节奏；引文照录，幻灯片分行按空白归一。

## 二、逐字引文（英文，未翻译）

CDN 与设备定位：

> Open Connect is Netflix’s CDN. It is global, efficient, and purpose-built for distributing Netflix’s content.

> Open Connect Appliances are Netflix’s CDN servers.

OCA 的系统与文件系统分工：

> Run FreeBSD-current

> UFS for content / ZFS for root

自建发行版：

> Netflix has an internal “distro”

工作负载特征：

> Video quality is of the utmost importance, so we don’t transcode on the server

> Greatly simplifies server workload

设备与软件栈团队（b021 补录）：

> Open Connect Appliances are Netflix’s CDN servers.

> Team within Netflix that maintains the software stack for our OCAs

故障与合并节奏（b021 补录）：

> Storage fails in place

> Merge upstream from FreeBSD-current every 3 weeks

> We notice & resolve new upstream bugs that impact us immediately

上游协作的收益（b022 补录）：

> Much easier to upstream code and collaborate with upstream developers

## 三、考据说明

- 两处 CDN／OCA 定义句支撑 3.1.1“操作系统退到服务层之下”：对外单位是 CDN 与设备，系统只作为设备内部条件出现。
- “internal distro”是 3.1.2“选型惯例”与 3.4“CURRENT 进生产”的关键：厂商不是直接采用发行版，而是在上游之上自建发行版。
- 工作负载句（不转码、只发静态媒体）解释为何压力点到内核 I/O 与网络路径，支撑 3.1.5。
- 演讲者为 Netflix 工程师兼 FreeBSD committer，属当事人一手材料，按 **L4** 采信（制作性与宣传性 slogan 不作事实引用）。
