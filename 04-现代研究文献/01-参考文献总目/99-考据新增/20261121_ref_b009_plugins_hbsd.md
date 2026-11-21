# OPNsense plugins 与 HardenedBSD 引用卡（ref 新建四件）

- **性质**：OPNsense plugins 仓库 README、pfSense packages 官方文档、HardenedBSD 官网与仓库 README——4.2.4 插件包分置与 4.4 面的一手表述
- **取件**（2026-11-21）：https://api.github.com/repos/opnsense/plugins/contents/README.md（base64 12 005 B）＋https://docs.netgate.com/pfsense/en/latest/packages/index.html（39 054 B）＋https://hardenedbsd.org/（71 243 B，状态报告流）＋https://api.github.com/repos/HardenedBSD/hardenedBSD/contents/README.md（base64 77 590 B）
- **plugins README 句（V57.4.2.4 A 块）**：The plugins collection offers users and developers a way to quickly build additions for OPNsense that can be optionally installed. As soon as they are upstreamed they will become available to everyone through the firmware GUI pages.
- **pfSense packages 句（V57.4.2.4 B 块）**：the firewall fetches package information from the Netgate package repository servers before the page is rendered to provide the most up-to-date information
- **hbsd 首页句一（V57.4.4.2 A 块）**：HardenedBSD uses a merge-based workflow for bringing in changes from upstream.
- **HardenedBSD README 句一（V57.4.4.2 B 块；软换行逐行归一）**：Over time, as the process of upstreaming ASLR to FreeBSD became more difficult, HardenedBSD naturally became a fork.
- **HardenedBSD README 句二（V57.4.4.1 A 块）**：HardenedBSD is a fork of FreeBSD, founded in 2014, that implements exploit mitigations and security hardening technologies. The primary goal of HardenedBSD is to perform a clean-room re-implementation of the grsecurity patchset for Linux to HardenedBSD.
- **hbsd 首页句二（V57.4.4.1 B 块；引号内人名段规避、两段 … 分段）**：In src: Contributor … hardened the kernel crashdump interface. Opt zlib kernel module into -ftrivial-var-auto-init
- **备用句（后续批）**：README Verifying Build Artifacts 节全句（4.4.3 面——与官网文章同文异载体，J94 不互证、须另寻第二源）；README toggle 句（secadm／hbsdcontrol）。
- **口径**：两 GitHub README 为项目官方仓库文件（api.github base64 逐字节）；HardenedBSD 首页为项目状态报告流（Shawn Webb 署名帖）；HardenedBSD README 与官网文章 Verifying Build Artifacts 同文异载体，4.4.3 双源另寻（J94）。
- **考据日期**：2026-11-21
