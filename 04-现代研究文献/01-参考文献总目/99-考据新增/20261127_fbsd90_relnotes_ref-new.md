# ref-new 考据登记（2026-11-27，V36 W1-5.4 研究稿）

- **标题**：FreeBSD 9.0-RELEASE Release Notes
- **作者**：The FreeBSD Project
- **年份**：2012
- **来源 URL**：https://www.freebsd.org/releases/9.0R/relnotes/
- **抓取日期**：2026-11-27（快照见 dossier verification.snapshot）
- **用途**：V36.5.4.3（V36 补证）
- **源类型／等级**：official_doc／L3（FreeBSD 官方发行说明）
- **查重披露**：refdedup 预检后未见同 URL／同标题命中，本条新建。发行说明页为 9.0 版通用页；Capsicum 条目带提交号 [r219129]。

## 关键原文（逐字）

> The FreeBSD kernel now supports Capsicum Capability Mode. Capsicum is a set of features for sandboxing support, using a capability model in which the capabilities are file descriptors. Two new kernel options CAPABILITIES and CAPABILITY_MODE have been added to the GENERIC kernel.

## 中文提要

FreeBSD 9.0 内核支持 Capsicum 能力模式，以文件描述符承载能力并提供沙箱特性，CAPABILITIES 与 CAPABILITY_MODE 加入 GENERIC。
