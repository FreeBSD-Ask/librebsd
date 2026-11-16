# Debian `openssh-server`（bookworm）包页（新 ref）引用卡

- **性质**：Debian 官方软件包页 `packages.debian.org/bookworm/openssh-server`（24,208 字节；包版本 `1:9.2p1-2+deb12u10`），含包说明、维护者名单与外部资源链接
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b011；`packages.debian.org` 库内无同 URL 条目）
- **source_url**：<https://packages.debian.org/bookworm/openssh-server>
- **quote（逐字，一处）**：

  > This is the portable version of OpenSSH, a free implementation of the Secure Shell protocol as specified by the IETF secsh working group.

- **考据注**：本页用于**远程访问栈中的署名缺失位置**（2.1.3）。可证者：包说明只把来源系于“OpenSSH 的可移植版”与 IETF secsh 协议规范；**整页 `OpenBSD` 出现 0 次**（抓取文本实测计数），`OpenSSH` 出现 2 次，`upstream` 0 次，`portable` 1 次。同时页内确有“External Resources: Homepage [www.openssh.com]”与源包链接 `openssh_9.2p1.orig.tar.gz`——即**线索以链接形式存在，而以文字形式缺席**。**限度（要紧）**：题面问“缺失位置与**频率**”，本卡只是一件取样（Debian bookworm 一个包页），不足以立频率判断；频率须跨发行版（Ubuntu／Fedora／openSUSE）、跨文档层（包页／手册页／安全公告）抽样后另批处理，列待补。另不可据此断言“Debian 有意抹去 OpenBSD”——缺载不等于反证。
- **文本处理披露**：HTML 抽取后连续空白并作单空格；引文取自页内说明段，逐字未改。
- **本批落点**：V35.2.1.3
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b011；official_doc／L3）
