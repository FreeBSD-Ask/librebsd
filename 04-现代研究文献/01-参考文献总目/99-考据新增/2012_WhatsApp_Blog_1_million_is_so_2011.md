# 1 million is so 2011（WhatsApp 官方博客）引用卡

> 用途：V71.3.5.2／3.5.3 内容补证（G8-S2 V71 b023）。

## 一、著录

WhatsApp. 1 million is so 2011[EB/OL]. WhatsApp Blog, 2012-01-06[2026-11-13]. https://blog.whatsapp.com/1-million-is-so-2011.

- 责任者：WhatsApp（运营者官方博客）
- 载体：HTML 博客（含 sysctl／uname 命令输出）；`source_tier=primary`（运营者自述，机构官方）
- 访问日：2026-11-13
- 抓取通道：本机直连 blog.whatsapp.com 超时，经 exa 服务端抓取取回正文后落盘（`wa_blog.txt`），引文以落盘文本为准
- 说明：博客公布单机 TCP 连接数、硬件配置、系统版本与 Erlang 版本；引文照录（代码块内的键值对按原样引用）。

## 二、逐字引文（英文，未翻译）

单机连接数的公开表述：

> we are now able to easily push our systems to over 2 million tcp connections

连接计数的实测输出：

> kern.ipc.numopensockets: 2277845

系统与运行时版本：

> FreeBSD 8.2-STABLE amd64

> Erlang R14B03 (erts-5.8.4) [source] [64-bit] [smp:24:24] [rq:24] [async-threads:0] [kernel-poll:false]

## 三、考据说明

- “over 2 million tcp connections”与 sysctl 实测 2,277,845 并列，是 3.5.3“运营者自述口径”的直接材料：数字由运营者自行公布，附硬件与内核参数，但非第三方基准测试，也无审计。
- 同页并列 `FreeBSD 8.2-STABLE` 与 `Erlang R14B03`，是 3.5.2“语言层与系统层分工”的版本现场。
- 按 L3 采信（运营者机构自述）；`kern.ipc.maxsockets=2400000` 等调参项只作背景，不据此推断默认上限。
