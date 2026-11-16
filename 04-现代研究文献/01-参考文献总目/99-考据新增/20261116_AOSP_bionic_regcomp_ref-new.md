# bionic `libc/upstream-netbsd` `regcomp.c`（新 ref）引用卡

- **性质**：Android C 库 bionic 树内 `libc/upstream-netbsd/lib/libc/regex/regcomp.c`（57,085 字节），即 NetBSD 正则实现原样带入 Android 树的上游副本；文件头保留 NetBSD 修订戳、SPDX 标识与原始版权行
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b008；source_url 查重＋规范化 URL：库内无该文件，亦无 `regcomp` 同名条目）
- **source_url**：<https://cdn.jsdelivr.net/gh/aosp-mirror/platform_bionic@master/libc/upstream-netbsd/lib/libc/regex/regcomp.c>
- **quote（逐字，文件头九行）**：

  ```text
  /*	$NetBSD: regcomp.c,v 1.49 2025/01/01 18:19:50 christos Exp $	*/

  /*-
   * SPDX-License-Identifier: BSD-3-Clause
   *
   * Copyright (c) 1992, 1993, 1994 Henry Spencer.
   * Copyright (c) 1992, 1993, 1994
   *	The Regents of the University of California.  All rights reserved.
  ```

- **考据注**：本卡只用于一题——**BSD 版权声明在 bionic 源码中的保留惯例**（2.2.4）。可证者三：①`$NetBSD: regcomp.c,v 1.49 …$` 修订戳未被剥除；②SPDX 标识 `BSD-3-Clause` 与原始版权行并列，未替换为项目自有声明；③版权人链（Henry Spencer 1992—1994／加州大学柏克莱 1992—1994）按原文年份逐行保留。**不可证者**：本条不证 bionic 的许可隔离制度设计（2.2.3 另题，该题本轮仍未取到 NOTICE 与构建规则文件，列待补）；亦不证全部 bionic 文件的普遍惯例，本卡只是**单文件取样**，普遍性须另做抽样。
- **载体披露（要紧）**：原生 `android.googlesource.com` 本机不可达（连接超时），`raw.githubusercontent.com` 本机连接被重置；本卡经 **jsDelivr CDN** 取 AOSP 镜像 `aosp-mirror/platform_bionic` 的同路径文件。镜像与原生若有版本差，须以提交哈希另核（本轮未取哈希，列待补）。
- **本批落点**：V35.2.2.4（第 4 行 SPDX／第 6—9 行版权行）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b008；official_doc／L3）
