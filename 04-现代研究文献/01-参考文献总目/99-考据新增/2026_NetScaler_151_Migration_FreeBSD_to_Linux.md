# Migrate NetScaler VPX from 14.1 (FreeBSD) to 15.1 (Linux)（官方迁移文档）引用卡

> 用途：V71.1.4.1／1.4.4 内容补证（G8-S2 V71 b002）。

## 一、著录

NetScaler (Cloud Software Group). Migrate NetScaler VPX from 14.1 (FreeBSD) to 15.1 Tech Preview (Linux)[EB/OL]. NetScaler Docs, 2026-09-30[2026-11-12]. https://docs.netscaler.com/us/en/preview/netscaler-15-1/netscaler-vpx-15-1/migration-to-15-1-linux.html.

- 责任者：NetScaler（Cloud Software Group 产品文档）
- 载体：HTML 技术预览文档；`source_tier=primary`（厂商官方文档）
- 访问日：2026-11-12
- 说明：文档标题与正文均以 FreeBSD／Linux 标注两代 VPX；引文照录英文原文。

## 二、逐字引文（英文，未翻译）

两代底座的更替：

> NetScaler® 15.1 introduces a Linux-based VPX, replacing the FreeBSD-based VPX available in release 14.1 and earlier.

迁移前置与回退路径：

> The VPX must be running NetScaler 14.1 build 56.x or later. If it is on an earlier 14.1 build, upgrade to 14.1-56.x or later with the standard FreeBSD bundle first.

> Rollback or downgrade to 14.1 (FreeBSD)

## 三、考据说明

- 该文以官方口径把“形态（VPX）—版本（14.1／15.1）—底座（FreeBSD／Linux）”三者绑定，是 1.4.4“形态分野落在交付方式而非功能集合”的底座侧证据。
- 亦为 1.4.1“设备／虚拟设备版以 FreeBSD 为底层”的第二来源（与 CTX495617 的 uname 示例互证）。
- 按 L3 采信；属技术预览文档，适用范围以其自述为限。
