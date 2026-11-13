# Yahoo! and FreeBSD（David Filo，Yahoo! 联合创始人）引用卡

> 用途：V71.3.3.1／3.3.2／3.3.3／3.3.5 内容补证（G8-S2 V71 b025 起）。

## 一、著录

Filo, David. Yahoo! and FreeBSD[EB/OL]. zer0.org（原载 FreeBSD News）, （日期不详）[2026-11-13]. https://zer0.org/daemons/yahoobsd.html.

- 责任者：David Filo（Yahoo! 联合创始人，当事人）
- 载体：HTML 转载页（原载 FreeBSD News）；`source_tier=primary`（当事人自述）
- 访问日：2026-11-13
- 抓取通道：本机直连 zer0.org 失败，经 exa 服务端抓取落盘（`yh_filo.txt`），引文以落盘文本为准
- 撰期：**〔存疑〕** 原文无日期；据文内“FreeBSD 2.0.5 起步、现用 2.1 STABLE、测试 2.2 STABLE、发现 FreeBSD 两年后”推定约 1996–1997 年，**不据推定为文内事实**，落块只用事件序列与数量表述

## 二、逐字引文（英文，未翻译）

加一台 FreeBSD 机器进 Web 服务器集群：

> A couple of days later we added a FreeBSD box to our cluster of Web servers. Not only did it out-perform the rest of our machines, but it was more stable.

选型所因：

> it was the stability, performance, and access to the sourcode that sold us

早期规模：

> We started with a single Pentium 100 box running FreeBSD 2.0.5. We eventually migrated the rest of our production servers to FreeBSD and today we have over 50 servers running various versions of 2.1 STABLE.

单机服务量与稳定性：

> We've seen over 180 days of uptime on a machine serving over 4 million HTTP requests per day.

磁盘条带化后的单机吞吐：

> we've been able to serve over 12 million HTTP requests per day on a PPro200 with 128MB of memory

无更换理由：

> Two years after discovering FreeBSD, we have yet to find a reason why we should switch to anything else.

## 三、考据说明

- “added a FreeBSD box to our cluster of Web servers”是 3.3.1“前端服务以集群承载”的起点叙述：集群先存在，FreeBSD 是加进去的一台。
- “over 50 servers”与单机“4 million／12 million HTTP requests per day”是 3.3.2 规模的原始量级（数十台×百万级日请求），**不是**后来的数千台／十万台量级，两者不可混用。
- “stability, performance, and access to the sourcode”是 3.3.3“商业证明”的内容层：选型理由来自生产运行而非技术论证；注意原文拼写为 `sourcode`，引文照录。
- 按 **L4** 采信（联合创始人自述）；数量与吞吐为当事人自述，非审计口径。
