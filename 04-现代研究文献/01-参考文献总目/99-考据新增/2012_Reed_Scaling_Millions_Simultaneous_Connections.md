# Scaling to Millions of Simultaneous Connections（Rick Reed，Erlang Factory SF 2012）引用卡

> 用途：V71.3.5.2／3.5.3／3.5.4 内容补证（G8-S2 V71 b023 起）。

## 一、著录

Reed, Rick. Scaling to Millions of Simultaneous Connections[R/OL]. Erlang Factory SF, 2012-03-30[2026-11-13]. https://www.erlang-factory.com/upload/presentations/558/efsf2012-whatsapp-scaling.pdf.

- 责任者：Rick Reed（WhatsApp 工程师，曾任 Yahoo! Distinguished Engineer）
- 载体：PDF 幻灯片（31 页）；`source_tier=primary`（当事人会议演讲）
- 访问日：2026-11-13
- 说明：演讲记单机连接数的爬升过程、瓶颈定位与 Erlang／FreeBSD 两侧调优；引文照录。

## 二、逐字引文（英文，未翻译）

两侧的扩展性：

> Erlang has awesome SMP scalability >85% cpu utilization across 24 logical cpus FreeBSD shines as well

（幻灯片原为三行，此处合为一段以便逐字比对。）

连接数的爬升与峰值：

> Achieved 2M conns about a month later

> Peaked at 2.8M conns before we intervened

标准配置与首段瓶颈（b024 补录）：

> Our standard configuration Dual Westmere Hex-core (24 logical CPUs) 100GB RAM, SSD Dual NIC

> Initial bottlenecks appeared around 425k

> First round of fixes got us to 1M conns

## 三、考据说明

- “Erlang has awesome SMP scalability … FreeBSD shines as well”是 3.5.2“组合分工在语言层与系统层”的当事人表述：两侧各自贡献扩展性，而非一方独任。
- “2M … a month later”“Peaked at 2.8M conns before we intervened”给出爬升序列与“介入前峰值”，是 3.5.3“公开口径”的第二来源（与博客的 227 万并列，但为演讲口径）。
- 按 **L4** 采信（当事人一手）；峰值数字属实验性尝试，不写作常态容量。
