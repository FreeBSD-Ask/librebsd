# ref-new 考据登记（2026-11-26，V36 W1-4.5 研究稿）

- **标题**：FreeBSD 6.0-RELEASE Release Notes
- **作者**：The FreeBSD Project
- **年份**：2005
- **来源 URL**：http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/i386/6.0-RELEASE/RELNOTES.TXT
- **抓取日期**：2026-11-26（快照见 dossier verification.snapshot）
- **用途**：V36.4.5.3（V36 补证）
- **源类型／等级**：official_doc／L3
- **查重披露**：refdedup 预检后未见同 URL／同标题命中，本条新建。

## 关键原文（逐字）

> struct ifnet and the network interface API have been changed. Due to ABI incompatibility, all drivers not in the FreeBSD base system need to be updated to use the new API and recompiled.

> Due to these changes, the ABI on 64-bit platforms is incompatible with previous releases of FreeBSD and the major version number of the libpcap shared library has been bumped.

## 中文提要

6.0 注记：struct ifnet 与网络接口 API 变更造成 ABI 不兼容，树外驱动须更新并重编。
