# FreeBSD src sys/netinet/tcp_input.c 文件头（新 ref）引用卡

- **性质**：FreeBSD 官方源码树 freebsd-src 的 TCP/IP 实现文件头部（经 api.github.com 字节级取回 121,729 B，SPDX-License-Identifier: BSD-3-Clause）
- **数据库**：新建 ref（2026-11-18 G4-P2 批 b025；freebsd-src 域内既有 ref10338／10366 为其他文件，本 URL 无条目）
- **source_url**：<https://github.com/freebsd/freebsd-src/blob/main/sys/netinet/tcp_input.c>
- **quote（逐字，一处；源内两行（换行＋制表缩进）与“California.  All”双空格均归一为单空格）**：

  > Copyright (c) 1982, 1986, 1988, 1990, 1993, 1994, 1995 The Regents of the University of California. All rights reserved.

- **考据注**：用于**FreeBSD 网络栈承自 4.2BSD 的协议实现**（2.1.1）。现行 TCP 实现文件头承加州大学 Regents 版权行，最早年份 **1982**——正是 Berkeley TCP/IP 实现（1983 年随 4.2BSD 发行）的写作年代；1986／1988 等续年对应 4.3BSD 时代演进。网络栈的谱系由此**以源内版权行自证**，接口与语义的承袭定型有源码面直接凭据。头部另载 Swinburne／FreeBSD Foundation／Juniper 等后继版权段，本批未整段引。
- **限度**：①版权年份证的是实现谱系存在与起点年代，不证逐行代码未改；②“接口与语义定型”的判读属编纂论旨；③1982 年份与 4.2BSD 发行（1983-08）的关系是年代对应，发行注面的直接表述另有出处面。
- **本批落点**：V37.2.1.1
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b025；official_doc／L3）
