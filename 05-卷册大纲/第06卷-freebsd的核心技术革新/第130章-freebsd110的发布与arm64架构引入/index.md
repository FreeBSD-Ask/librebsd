---
chapter: 第 130 章
id: CH130
volume: 第06卷-freebsd的核心技术革新
---

# 第 130 章 freebsd110的发布与arm64架构引入

## 要点

- 11.0 引入多个重要用户空间组件：① **libxo(3)**——由 Juniper Networks 赞助、Phil Shafer 开发的通用输出库，使系统工具可同时生成人类可读文本、XML、JSON、HTML 等多种格式输出，**netstat(1)**（r279122，Juniper 赞助；Glen Barber 于 2015-04-28T18:10:35Z 在 commit `d1e25
- FreeBSD 11.4-RELEASE 于 2020 年 6 月 23 日发布，是 stable/11 分支第五个也是最后一个版本（"fifth and final release"）。核心更新：Clang/LLVM/LLD/LLDB/compiler-rt/libc++ 升级至 10.0.0；OpenSSL 1.0.2u（OpenSSL 1.0.2 系列最终版本）；Unbound 更新至 1.
- 11.x 时期 Linux 兼容层（Linuxulator）持续改进：①CentOS 7 兼容层 ports（emulators/linux-c7）在 11.x 时期成熟（10.3 引入 64 位 Linux 支持后持续完善）；②1:1 线程模型与 **epoll(7)** 子集实现在 10.3 基础上持续改进，可运行更多 Linux 商业软件；③ **jail(8)** 内支持挂载 **linp

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10423] BSD Now 第 676 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10510] BSD Now 第 661 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10526] BSD Now 第 656 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10533] BSD Now 第 655 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10540] BSD Now 第 654 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10556] BSD Now 第 652 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10566] BSD Now 第 651 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10589] BSD Now 第 645 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10606] BSD Now 第 642 期，匹配 CH130 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10630] BSD Now 第 638 期，匹配 CH130 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 部分资料称“blacklistd 在 11.0 已集成到 OpenSSH”——经 11.0 与 11.1 Release Notes 交叉验证，11.0 仅导入 libblacklist 与 blacklistd 守护进程本身，OpenSSH 的 blacklistd 集成在 11.1-RELEASE 才完成（11.1 Announcement 明确列出"Support for **blackli
- 部分资料误称“11.4 是最后一个使用 GCC 4.2.1 的版本”——GCC 4.2.1 在 11.x 仍用于 powerpc/sparc64/mips 等非 x86 架构的构建，但 x86 早已默认 Clang；GCC 4.2.1 从 base 中完全移除发生在 FreeBSD 13.0 时期，非 11.4。11.4 携带的 OpenSSL 1.0.2u 是 OpenSSL 1.0.2 系列的
- Linux 兼容层在 11.x 仍不能运行 Docker——Docker 依赖大量 Linux 特定内核特性（cgroups v2、namespaces 完整集合、systemd socket 等），Linuxulator 实现的系统调用子集不足以支持 Docker；Docker on FreeBSD 在 11.x 时期需通过 bhyve 虚拟机运行 Linux 间接实现。WireGuard 在

## 文献

- Shafer P. libxo: A Library for Generating Text, XML, JSON, and HTML Output [EB/OL]. juniper.github.io/libxo/；FreeBSD libxo(3)/blacklistd(8) Manual Pages [Z]；FreeBSD 11.0/11.1-RELEASE Release Notes [Z]. 2016/2017；Barber G. Document r279122, netstat(1) updated to use libxo(3). freebsd-src [DB/OL]. 2015-04-28T18:10:35Z. d1e2507b7f2a645e09676d1c005713f39968e718; Barber G. Document r275680, fstyp(8) addition. freebsd-src [DB/OL]. 2015-01-11T19:01:04Z. 7ddc205dac1e7b03d4a31b9496d9c263ac1c35b6; Barber G. Document r278320, devctl(3) and devctl(8) added. freebsd-src [DB/OL]. 2015-02-20T17:46:10Z. 742355ae61376053156d0875685c04f8cc7d59c3; Barber G. Document r279315, uefisign(8) addition. freebsd-src [DB/OL]. 2015-03-16T15:54:41Z. ac2456f1bd0ee0b03a7a7e7e2742f5fbed7b42ac; Barber G. Document r287473, sesutil(8) addition. Add Gandi.net to sponsor.ent. freebsd-src [DB/OL]. 2015-10-05T20:13:30Z. c4af256e4867cf90b7b1743a08cbb1cf8371f3ed ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2016-2016 年间：44,329 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD Release Engineering Team. FreeBSD 11.4-RELEASE Announcement [Z]. 2020-06-23；FreeBSD Project. In Memoriam: Bruce Evans [Z]. 2020；FreeBSD 11.4-RELEASE Release Notes [Z]. 2020；FreeBSD Project. release/11.4.0. freebsd-src 仓库 tag [DB/OL]. 2020-06-16T13:59:51Z. tag: release/11.4.0; commit: 8c639945a44588f6cfdddfb057bb5aad88735da0 ［A］<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。
- FreeBSD linux(4)/capsicum(4) Manual Pages [Z]；Watson R N M. Capsicum: Practical Capabilities for UNIX [C]//USENIX Security 2010；FreeBSD 11.x Release Notes Security chapters [Z].<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，13,875 位贡献者，1993-06-12 至 2026-08-25。

<!-- PODCAST_MINE v20260827 -->
<!-- 章节主题过滤：第130章-freebsd110的发布与arm64架构引入 第 130 章 freebsd110的发布与arm64架构引入（实体评分 ≥2 命中才入选） -->
<!-- 匹配期数：15 期，扫描 segments：13911 条 -->

### 要点（播客口述史提取）
- upgrading the craft referencing and search tools that are built into FreeBSD.（BSD Now EP1 @ 1858.719）
- And I guess the other one was OpenBSD changed the syntax of the rules and FreeBSD didn't（BSD Now EP16 @ 5602.939）
- always be his first choice. He knows FreeBSD as well, but he cannot answer questions about（BSD Now EP21 @ 5077.540）
- First up we got some information about getting started with FreeBSD.（BSD Now EP23 @ 3251.319）
- We got a new video and blog series about getting started of course with FreeBSD.（BSD Now EP23 @ 3256.119）

### 史料（播客当事人陈述）
- But it looks like they're going to be having presentations on ARM on NetBSD and FreeBSD.（BSD Now EP26 @ 328.0999）
- where they were talking about how FreeBSD was dying because they hadn't met their donation goal yet,（BSD Now EP1 @ 1178.880）
- Yeah, just about every GUI we have, there's some kind of shell or back end behind it that's just running standard FreeBSD commands.（BSD Now EP1 @ 1574.040）
- and actually just have them be put into as articles in not the handbook, but in the FreeBSD documentation tree.（BSD Now EP1 @ 1785.939）

### 史观（播客当事人观点与总纲映射）
- （该章节匹配播客中未提取到当事人观点性陈述）

### 辨析（播客争议与存疑点）
- [存疑脚注] FreeBSD10, it's likely that FreeBSDPF will be a fork from this point, not brought up to date with（BSD Now EP25 @ 1421.520）
- [存疑脚注] And if you're using FreeBSD secure levels, you can actually make it so the flag can't be removed（BSD Now EP39 @ 3676.899）

### 文献（播客参考条目）
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.
- [BSD Now EP16] Pennington J. BSD Now: 16: Cryptocrystalline[EB/OL]. (2013-12-18)[2026-08-15]. https://www.bsdnow.tv/16.
- [BSD Now EP21] Pennington J. BSD Now: 21: Tendresse for Ten[EB/OL]. (2014-01-22)[2026-08-15]. https://www.bsdnow.tv/21.
- [BSD Now EP22] Pennington J. BSD Now: 22: Journaled News-Updates[EB/OL]. (2014-01-29)[2026-08-15]. https://www.bsdnow.tv/22.
- [BSD Now EP23] Pennington J. BSD Now: 23: Time Signatures[EB/OL]. (2014-02-05)[2026-08-15]. https://www.bsdnow.tv/23.
- [BSD Now EP25] Pennington J. BSD Now: 25: A Sixth pfSense[EB/OL]. (2014-02-19)[2026-08-15]. https://www.bsdnow.tv/25.
- [BSD Now EP26] Pennington J. BSD Now: 26: Port Authority[EB/OL]. (2014-02-26)[2026-08-15]. https://www.bsdnow.tv/26.
- [BSD Now EP32] Pennington J. BSD Now: 32: PXE Dust[EB/OL]. (2014-04-09)[2026-08-15]. https://www.bsdnow.tv/32.

<!-- /PODCAST_MINE -->
