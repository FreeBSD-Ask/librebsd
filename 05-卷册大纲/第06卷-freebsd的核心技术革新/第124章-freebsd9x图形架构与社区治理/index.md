---
chapter: 第 124 章
id: CH124
volume: 06
---

## 要点

- 9.1-RELEASE 新增 Intel GPU 驱动支持 GEM（Graphics Execution Manager）与 KMS（Kernel Mode Setting），这是 FreeBSD 图形栈现代化的重要一步；KMS 将显示模式设置从用户态 X 服务器移入内核，支持更快的 VT 切换、更稳定的图形性能和 suspend/resume；Radeon KMS 支持在 9.x 尚未完成，10.x 之后才引入
- 9.x 系列新增大量网卡驱动：9.0 新增 **bxe(4)**（Broadcom NetXtreme II 10GbE）、**cxgbe(4)**（Chelsio T4 10Gb/1Gb）、**vte(4)**（RDC R6040）、**vxge(4)**（Neterion X3100 10GbE）；**em(4)** 更新至 7.3.2、**igb(4)** 至 2.2.5、**ixgbe(4)** 至 2.3.8，新增 Intel I350 支持；9.1 新增 **oce(4)**（Emulex OneConnect 10GbE）、**sfxge(4)**（Solarflare SFC9000）、**hpt27xx(4)**（HighPoint RocketRAID 27xx SAS 6Gb/s）
- 9.0-RELEASE 中 FreeBSD/powerpc 支持 Sony PlayStation 3 主机的 OtherOS 功能（固件 3.15 及更早版本）；Nathan Whitehorn 是 PS3 支持的主要开发者，他同时也是 bsdinstall 作者和 powerpc64 release builder；Sony 于 2010-04-01 通过固件更新 3.21 移除 OtherOS 功能（2010-03-28/29 为公告日，2026-08-05 联网复核更正），因此该支持仅对未升级固件的旧款 PS3（“OtherOS 脂肪机”）有意义，PS3 Slim 出厂即无 OtherOS
- 9.0-RELEASE 支持架构：amd64、i386、ia64（Itanium）、powerpc、powerpc64、sparc64；9.1-RELEASE 初始仅发布 amd64、i386、powerpc64、sparc64（ia64/powerpc 因构建资源受限后补）；9.2/9.3 恢复支持 amd64、i386、ia64、powerpc、powerpc64、sparc64；FreeBSD/arm 在 9.x 时期持续改进但未列入 RELEASE Tier 1 架构；FreeBSD/mips 在 9.x 时期主要用于嵌入式场景，不发布标准安装镜像
- Sony 于 2013 年 11 月 15 日（北美）/11 月 29 日（欧洲）发布 PlayStation 4（PS4），其操作系统 Orbis OS 基于 **FreeBSD 9.0** 内核修改（原文件错误为 10.0——PS4 2013.11 发布时 10.0 尚未发布（10.0 2014.1.20 才发布），时间线上不可能基于 10.0）；PS4 选择 FreeBSD 而非 Linux 的核心原因是 BSD 许可证允许闭源修改——Sony 无需像 GPL 那样公开其内核修改；Orbis OS 在 FreeBSD 9.0 基础上新增了定制的图形栈（基于 AMD GCN GPU）、安全 hypervisor、定制系统服务等

## 史观

- 总纲第 10 条——边缘者贡献：FreeBSD 图形驱动开发长期依赖少数志愿者（如 Konstantin Belousov（康斯坦丁·别洛乌索夫）、Konrad Witaszczyk 等）从 Linux 移植 DRM/KMS 代码，是项目中资源相对匮乏但需求广泛的领域；图形栈的延迟成熟是 FreeBSD 桌面体验落后于 Linux 的重要原因
  - 辨析：9.1 Intel KMS 仅支持较旧的
- 总纲第 10 条——边缘者贡献：PS3 支持是 FreeBSD 支持游戏主机的罕见案例——它与 PS4 Orbis OS（见 79.12）形成有趣对照：前者是 hobbyist 级的非官方支持，后者是 Sony 官方基于 FreeBSD 的产品级派生；Sony 移除 OtherOS 的决定引发了集体诉讼，最终以赔偿和解告终
  - 辨析：PS3 OtherOS 支持仅在 3.15 及更早固件有效，
- 总纲第 24 条——许可证：PS4 是 BSD 许可证商业友好性的标志性案例——它与 Apple macOS/Darwin（基于 FreeBSD 5.x 时期）、Netflix Open Connect、Juniper Junos、pfSense/OPNsense、Blue Coat、NetApp 等共同构成 BSD 许可证商业模式的实证；GPL 许可证要求公开派生作品源代码，这使得商业公司在闭源
- 总纲第 23 条——社区治理：Security Officer 是 FreeBSD 最关键的角色之一，掌握安全公告发布、漏洞协调、基础设施安全等核心权力；Colin Percival 长达 7 年（2005-2012）的任期塑造了 FreeBSD 安全响应的文化与流程，其继任者延续了严格、保守、透明的安全公告风格
- 辨析：Security Officer 交接在 9.x 密集发生（9.0 cpe
- 总纲第 1 条——知识管理的制度化。
- 文献：安全团队报告 ［A］

## 辨析

- 9.1 Intel KMS 仅支持较旧的 Intel GPU（Ironlake/Sandy Bridge 时期），Ivy Bridge 及更新 GPU 支持在后续版本添加；Radeon/NVIDIA KMS 在 9.x 不可用
  - 文献：FreeBSD 9.1-RELEASE Release Notes（Graphics Drivers 章节）；**drm(4)**、**i915kms(4)*
- PS3 OtherOS 支持仅在 3.15 及更早固件有效，绝大多数 PS3 用户因在线游戏和 PSN 需求早已升级固件，因此该支持的实用价值有限，但作为 FreeBSD 支持非传统硬件平台的案例具有历史意义
  - 辨析（2026-08-05 一手原件补充，ref 2632-2637/2647）：**In re Sony PS3 "OtherOS" Litigation**（N.D. Cal.,
- **重要事实纠正——Orbis OS 基于 FreeBSD 9.0 而非 10.0**：时间线证据是决定性的——PS4 2013.11.15 发售，FreeBSD 10.0 2014.1.20 才发布；PS4 开发周期中 10.0 尚未发布，Sony 不可能基于未发布的版本；CTurt 等 PS4 越狱者的逆向分析也确认内核基于 9.0；部分媒体可能因 PS4 生命周期中后续升级包含 10.x 代
- Security Officer 交接在 9.x 密集发生（9.0 cperciva→9.1 simon→9.2 des，9.3 新增 delphij），部分源于 Colin Percival 在 Tarsnap 等商业项目上的精力分配，也与 2012 年入侵事件后安全团队扩充有关；从 9.2 开始采用 "Security Officer + Emeritus" 双轨制，保留前任经验；这种有序的权
- 谱系叙述中须区分两个层次——技术源头是 Larry Wall 原始 **patch(1)**，许可证源头是 OpenBSD 替换 GPL 文件为 PD/无限制版本；DragonFly 的 “进一步增强” 具体内容须对照 DragonFly commit log 核实；pfg “反向移植 FreeBSD 原有增强” 表明 FreeBSD 版本与 DragonFly 版本并非简单复制关系，而是双向融合

## 文献

- FreeBSD 9.1-RELEASE Release Notes（Graphics Drivers 章节）；**drm(4)**、**i915kms(4)** man pages（9.1 版本） ［B］

## 123.10.2 网络驱动更新

- 要点：9.x 系列新增大量网卡驱动：9.0 新增 **bxe(4)**（Broadcom NetXtreme II 10GbE）、**cxgbe(4)**（Chelsio T4 10Gb/1Gb）、**vte(4)**（RDC R6040）、**vxge(4)**（Neterion X3100 10GbE）；**em(4)** 更新至 7.3.2
- FreeBSD 9.0-RELEASE Release Notes（Architectures 章节）；svn commit r217044；Sony Computer Entertainment. PS3 System Software Update 3.21 [Z]. 2010-03-28 ［A］

## 123.11.2 9.x 支持架构与状态

- 要点：9.0-RELEASE 支持架构：amd64、i386、ia64（Itanium）、powerpc、powerpc64、sparc64；9.1-RELEASE 初始仅发布 amd64、i386、powerpc64、sparc64（ia
- Sony Computer Entertainment. PlayStation 4 Developer Documentation（Orbis OS 章节）；CTurt. PS4 Kernel Exploitation Analysis [Z]. 2015-2017；多家技术媒体 2013.6 E3 报道（确认 Orbis OS 基于 FreeBSD 9.0）；Rosen L. Open Source Licensing: Software Freedom and Intellectual Property Law [M]. Upper Saddle River: Prentice Hall
- FreeBSD 9.0/9.1/9.2/9.3-RELEASE Announcement Acknowledgments 章节 [Z]. 2012-2014；FreeBSD Security Team 页面（security.freebsd.org）[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 123.13.2 Release Engineering 团队构成

- 要点：9.0 Release Engineering Team 由 Ken Smith（kensmit
- 安全团队报告 ［A］
- Pedro Giffuni 2013.1.29 [CFT] WITH_BSD_PATCH（freebsd-current 邮件列表 archives/2013-January/039367.html）；FreeBSD Bugzilla PR 99173（bugs.freebsd.org/bugzilla/show_bug.cgi?id = 99173）；Kohn A. 2006.6.19 lwpatch 提案附件 ［A］

## 123.15.2 r246074 首次导入与 WITH_BSD_PATCH 构建选项

- 要点：2013 年 1 月 29 日 17:03 由 Gabor Kove
- Pedro Giffuni. [CFT] WITH_BSD_PATCH [EB/OL]. freebsd-current mailing list, 2013-01-29; Free Software Foundation. Various Licenses and Comments about Them [EB/OL]. gnu.org/licenses/license-list.html（#ModifiedBSD、#FreeBSD 条目，2026-07-22 核实）.[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史
- Phoronix FreeBSD 9.0 vs Linux benchmarks（2012 年系列）；freebsd-advocacy 邮件列表档案 ［A］

## 123.16.2 被忽视的边缘贡献者

- 要点：9.x 时期核心技术的知名贡献者（McKusick、Watson、Motin、Selasky、Grehan、Percival、Whitehorn、Dawidek 等）常被历史记录，但大量 ports 维护者、文档翻译者、bug 报告者、测试者的贡献被主流叙事忽视；FreeBSD 9.x 时期 ports 数量从约 22,000 增长至超过 24,000，背后是数百名 ports c

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
