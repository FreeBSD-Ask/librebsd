# FreeBSD 5.x Release Engineering Roadmap“Major issues”引文卡

- **著录（GB/T 7714-2015）**：THE FREEBSD PROJECT. 5-roadmap: Major issues（FreeBSD 4.8-RELEASE 文档存档）[EB/OL]. The FreeBSD Project, 2003[2026-11-25]. https://docs-archive.freebsd.org/doc/4.8-RELEASE/usr/share/doc/en/articles/5-roadmap/major-issues.html.
- **来源 URL**：https://docs-archive.freebsd.org/doc/4.8-RELEASE/usr/share/doc/en/articles/5-roadmap/major-issues.html
- **访问日期**：2026-11-25（WebSearch 抓取官方存档页正文）
- **用途**：Task 8.2 G3 全责线 V27 b014（4.2.2B 既有锁模型不可扩展面）
- **tier 依据**：source_type=official_doc、source_tier=primary（发行工程团队正式路线文件，2003 年同时代）
- **披露**：原页以双反引号标 ``Giant``，引文照录并保留双反引号；同页另有 4.8-RELEASE 版与 AUUGN 转载，取官方存档页为准

## 逐字引文

Q1（4.2.2B 源，SMPng 与 Giant 全局锁为五版最大隐患）:
The state of SMPng and kernel lockdown is the biggest concern for 5.X. To date, few major systems have come out from under the kernel-wide mutex known as ``Giant''.

Q2（4.2.2B 源，Giant 争用反伤性能）:
However, contention due to Giant covering much of the kernel and most of the device driver interrupt routines causes excessive context switches and might actually be hurting performance.

## b014-r3 追加引文（2026-11-25 快照复取核证）

- **追加用途**：b014-r3（4.1.4A／4.4.3B）
- **披露**：链接后空格标点归一；roadmap“5. X .”空格形与 ``Giant'' 双反引号、rel53 ``skipping'' 双反引号照录

A1（rdA）:
The state of SMPng and kernel lockdown is the biggest concern for 5. X . To date, few major systems have come out from under the kernel-wide mutex known as ``Giant''.
