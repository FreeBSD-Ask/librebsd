# How to check the version of FreeBSD on NetScaler（CTX495617）引用卡

> 用途：V71.1.4.1“NetScaler 设备的 FreeBSD 基底”内容补证（G8-S2 V71 b002）；b008 补录完整输出（含构建路径）。

## 一、著录

Citrix Systems. How to check the version of FreeBSD on NetScaler (Article ID: CTX495617)[EB/OL]. Citrix Support, （日期不详）[2026-11-12]. https://support.citrix.com/external/article?articleUrl=CTX495617-how-to-check-the-version-of-freebsd-on-netscaler.

- 责任者：Citrix Systems（厂商支持知识库）
- 载体：HTML 支持文章；`source_tier=primary`（厂商支持文档，含设备 shell 实测输出示例）
- 访问日：2026-11-12
- 说明：文章给出登录设备 shell、执行 `uname -a` 的步骤与输出示例；引文照录，输出中的编译时戳与路径为原文所有。

## 二、逐字引文（英文，未翻译）

操作步骤与内核标识示例：

> 1. Login to Putty 2. Type "shell" 3. Type command "uname -a" e.g. root@NS# uname -a FreeBSD NS 11.4-NETSCALER-13.1 FreeBSD 11.4-NETSCALER-13.1 #0 186b96821582(heads/artesa_37_38)-dirty: Wed Nov 23 04:42:52 PST 2022

完整输出含构建路径（b008 补录）：

> root@NS# uname -a FreeBSD NS 11.4-NETSCALER-13.1 FreeBSD 11.4-NETSCALER-13.1 #0 186b96821582(heads/artesa_37_38)-dirty: Wed Nov 23 04:42:52 PST 2022 root@sjc-bld-bsd114-215:/usr/obj/usr/home/build/adc/usr.src/sys/NS64 amd64

## 三、考据说明

- 该文是厂商支持库中直接以 FreeBSD 为题的文章，输出示例含 `FreeBSD NS 11.4-NETSCALER-13.1`，可作为“设备底层为 FreeBSD”的厂商自述证据。
- 属示例性输出（e.g.），claim 须写成“官方支持文章以示例形式给出”，不得据此断言所有版本与机型。
- 按 L3 采信：厂商文档，非独立第三方。
- b008 补录：完整输出末尾的构建路径 `usr/home/build/adc/usr.src/sys/NS64` 表明厂商以自有源码树的 `sys/NS64` 平台目录构建内核，可作 1.5.3“封闭范围叠加于内核本体”的厂商自述证据；仍属示例输出，不得外推。
