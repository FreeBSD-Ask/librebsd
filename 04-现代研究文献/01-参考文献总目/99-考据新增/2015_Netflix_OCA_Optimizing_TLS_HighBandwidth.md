# Optimizing TLS for High–Bandwidth Applications（Netflix OCA，AsiaBSDCon 2015）引用卡

> 用途：V71.3.1／3.2／3.6 内容补证（G8-S2 V71 b020 起）。

## 一、著录

Netflix Open Connect. Optimizing TLS for High–Bandwidth Applications[R/OL]. AsiaBSDCon 2015[2026-11-13]. https://openconnect.netflix.com/publications/asiabsd_2015_tls.pdf.

- 责任者：Netflix Open Connect（厂商公开技术论文）
- 载体：PDF 会议论文（6 页）；`source_tier=primary`（厂商公开技术出版物）
- 访问日：2026-11-13
- 说明：论文描述 OCA 的硬件规格、并发会话规模与 TLS 数据路径改造；引文照录。

## 二、逐字引文（英文，未翻译）

OCA 的规格与并发规模：

> Each server is designed to hold between 10TB and 120TB of multimedia objects, and can accommodate anywhere from 10,000 to 40,000 simultaneous long-lived TCP sessions with customer client systems.

软件环境：

> running FreeBSD 10.1 and Nginx 1.5

## 三、考据说明

- 规格句给出“服务规模”的可核对口径（容量区间、并发会话区间、带宽区间），是 3.1.5“规模对内核的压力”的量化依据；区间值照录，不取中点外推。
- “FreeBSD 10.1 and Nginx 1.5”是 2015 年论文写作时的版本现场，只作时代快照引用，不代表后续版本。
- 论文为厂商公开出版物，按 L3 采信。
