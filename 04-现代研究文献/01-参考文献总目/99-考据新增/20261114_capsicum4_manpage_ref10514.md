# capsicum(4) — FreeBSD 内核接口手册页（ref10514）引用卡

- **性质**：FreeBSD 官方手册页（Kernel Interfaces Manual，CAPSICUM(4)，FreeBSD 15.1，2026-01-23 更新）
- **数据库**：ref 10514（references_fulltext.duckdb，kaoju_new，0 全文块＝D2 条目型）
- **source_url**：https://man.freebsd.org/cgi/man.cgi?query=capsicum&sektion=4
- **抓取**：2026-11-14 curl 直取（65,684 B HTML），剥标签取正文（script/_capsicum4.txt 工作件）
- **quote（逐字）**：
  1. "Capsicum is a lightweight OS capability and sandbox framework implementing a hybrid capability system model."
  2. "Capsicum provides two core kernel primitives: capability mode — A process mode, entered by invoking cap_enter(2), in which access to global OS namespaces (such as the file system and PID namespaces) is restricted; only explicitly delegated rights, referenced by memory mappings or file descriptors, may be used. Once set, the flag is inherited by future children processes, and may not be cleared."
- **关联 claim**：CL-RM-495047（L3，supported）——"官方文档记载"（手册页＝官方文档抬头）
- **本批落点**：V36.9.6.1（能力模式的系统位置）D2 块 `ref10514#url`
- **考据日期**：2026-11-14（Task 8.2 G4 P2 留题解决批；四键查重：source_url 与题名+首作者+年份均无重合）
