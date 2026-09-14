---
chapter: 第 123 章
id: CH123
volume: 第06卷-freebsd的核心技术革新
---

# 第 123 章 freebsd9x版本基础与内核子系统


## 史料

- [DB:research_notes:blocks:534] 关键词“内核子系统”命中：史实考据：Antti Kantee 的 Aalto 大学 2012 年博士学位论文，系统阐述 anykernel 与 r…
- [DB:research_notes:blocks:1085] 关键词“内核子系统”命中：史实考据：DragonFly BSD 项目在 USENIX 2005 Annual Technical Conferen…
- [DB:research_notes:blocks:5483] 关键词“内核子系统”命中：史实考据：NetBSD 1.3 官方发布说明，确认发布日期为 1998 年 1 月 9 日；二进制发布支持 14 个平台…

## 要点

- FreeBSD 9.0 开发始于 stable/8 分支冻结后，历时近两年（2010 年中至 2012.1.12 正式发布），是 FreeBSD 历史上开发周期最长的大版本之一；9.x 系列包含四个 RELEASE：9.0（2012.1.12）、9.1（2012.12.30）、9.2（2013.9.30）、9.3（2014.7.16），无 9.4-RELEASE；9.3 作为 9.x 系列终章获得超长支持周期至 2017.1.1，是生产环境长期部署的 “企业级稳定版”
- Dennis M. Ritchie 于 2011 年 10 月 12 日逝世，距 9.0-RELEASE 发布恰好三个月；FreeBSD 项目在官方公告中明确将 9.0-RELEASE 献给 Ritchie："The FreeBSD Project dedicates the FreeBSD 9.0-RELEASE to the memory of Dennis M. Ritchie, one of the founding fathers of the UNIX operating system“；献辞指出 ”the fact that his work of so many years ago continues to influence new design decisions to this very day speaks for the brilliant engineer that he was"
- 2012 年 11 月 11 日，FreeBSD 基础设施中两台机器被检测到入侵——受影响的是旧版第三方包构建基础设施头节点（“pointyhat”）；入侵原因是某位开发者的 SSH 密钥泄露，而非 FreeBSD 代码本身存在漏洞；入侵者最早可能于 2012 年 9 月 19 日即获得访问权限；项目于 11 月 17 日公开通报，大量基础设施机器下线审计，导致 9.1-RELEASE 发布延迟且初始仅含 GNOME/KDE 最小包集，完整包集直至 2013 年 4 月 30 日才恢复；Subversion 源码仓库、base 系统均未被篡改
- 9.0-RELEASE 安全支持原计划至 2013.1.31，因 9.1 发布延迟顺延至 2013.3.31；9.1-RELEASE 作为延长支持版本 EOL 为 2014.12.31；9.2-RELEASE 支持至 2014.9.30；9.3-RELEASE 支持至 2017.1.1——这一超长支持周期使 9.3 成为 FreeBSD 历史上支持时间最长的 .0 大版本系列之一，被众多企业和托管服务商长期部署。9.x 系列版本发布与支持周期关键数据（tagger_date、target_commit_hash 经 **freebsd.duckdb** `tags` 表验证）汇总见下表。
- **bsdinstall(8)** 由 Nathan Whitehorn（nwhitehorn@）主导开发，在 9.0-RELEASE 中正式取代使用了近 20 年的 **sysinstall(8)**；bsdinstall 采用 shell 脚本与分布式模块化设计，而非 sysinstall 的单体 C 程序架构；核心设计目标是可扩展性——sysinstall 因硬编码逻辑难以支持新特性（如 ZFS、GPT、UEFI），bsdinstall 通过脚本化架构解决此问题；9.0-RELEASE 的 ISO 镜像默认使用 bsdinstall，但 sysinstall 仍存在于系统中以兼容旧脚本

## 史观

- 总纲第 21 条——革命与改革是历史方法论的分歧：9.x 是 8.x 时代的“终结”与 10.x 时代的“延续”之间的过渡——它既完成了 bsdinstall、SUJ、ZFS v28、Capsicum 等 10.x 时代核心特性的落地与验证，又保持了 GCC 4.2.1、pkg_install 等旧栈作为默认，为许可证纯洁化大迁移（GCC→Clang、pkg_install→pkg、BIND→Unbound）铺平了道路——以改革而非革命的节奏完成代际更替。
- 专题语（不设总纲条号）——支持周期与用户采用模式：9.3 获得超长支持，是因为 10.x 系列引入 Clang 默认、pkg 取代 pkg_install 等重大变化导致许多生产环境不愿升级，9.3 成为“旧世界”的最后堡垒；这种“LTS 式”社区自发延长支持的模式，与 Linux 发行版商业驱动的 LTS 形成对照
- 辨析：FreeBSD 官方从未使用 “LTS”
- 专题语（不设总纲条号）——安装器的工程范式迁移：sysinstall 到 bsdinstall 的更替体现了“单体 → 模块化”、“C 硬编码 → 脚本化组合”的迁移；sysinstall 是 1990 年代 BSD 安装器的典型（类 sysconfig 界面、静态菜单），bsdinstall 则面向 ZFS、虚拟化、云部署等 2010 年代新需求设计
- 总纲第 10 条——动手者创造历史：SUJ 是 McKusick 作为 UFS/FFS 原始设计者对其作品的“晚年修订”——soft updates 本身是 Ganger & Patt 于 1990 年代提出的元数据一致性方案，McKusick 在 FreeBSD 中实现并维护 15 年后，通过 SUJ 解决了其最后的痛点（崩溃后 fsck 时间）；这体现了核心系统软件“作者终身维护”的 BSD 传统（soft updates 自 1990 年代方案到 SUJ 的 15 年演进即此传统的实例）。
- 总纲第 13 条——法律与道德是利益分配：ZFS v28 成为 FreeBSD（以及后来整个开源社区）ZFS 演进的基础版本具有历史决定性——Oracle 闭源后，illumos 成为 ZFS 开源开发的主力，FreeBSD 从 illumos 持续移植改进；v28 作为 CDDL 许可的最后共同祖先版本，奠定了 BSD/Linux/macOS ZFS 生态的技术基础

## 辨析

- 9.x 常被叙事为 “新一代”（标题中 “新一代” 标签），但技术上多数核心特性在 8-CURRENT 已开始开发（如 USB 栈重写始于 8.0），9.0 是集成与稳定化而非全新革命；9.3 的超长支持周期（至 2017）与 10.x 系列较短的支持周期（10.0 至 2015.1.31）形成对比，表明生产用户对 9.x 稳定性的认可；**数据库验证结论**：9.x 四个 RELEASE 的 tagger_date 与 target_commit_hash 均经 tags 表逐项验证，与官方公告日期一致。
- FreeBSD 官方从未使用 “LTS” 术语，但 9.3 的实际支持周期（2014.7-2017.1，约 2.5 年）远超常规 RELEASE 支持周期（通常约 1 年）；这表明支持周期由用户需求与安全团队资源共同决定，而非硬性政策
- 文献：FreeBSD Security Team. FreeBSD Security Support [Z]. security.freebsd.org；各版本

- bsdinstall 的 “shell 脚本驱动” 常被误解为 “用 Lua 驱动”——bsdinstall 实际主要使用 POSIX shell 脚本配合 **dialog(1)** 提供文本界面，Lua 是在更晚版本（10.x 之后）才逐步引入部分组件；9.0 的 bsdinstall 尚不支持 ZFS root 自动安装（需手动配置），ZFS 引导的官方安装支持在 10.x 才完善

- SUJ 不是 “日志文件系统”（journaling filesystem）的完整实现——它仅对 soft updates 元数据更新增加意向日志以加速恢复，而非像 ext3/ext4、XFS 那样对元数据甚至数据进行完整日志记录；这一设计选择保持了 soft updates 的性能优势，同时消除了其最显著的运维缺陷（服务器异常断电后 fsck 时间与文件系统大小成正比）
  - 文献：McKus
- ZFS v28 在 FreeBSD 9.0 中状态为 “Production 但非默认根文件系统”——作为数据存储卷使用已相当稳定，但作为 root 文件系统仍需大量手动调整，不适合普通用户；10.0 时期 bsdinstall 才逐步加入自动 ZFS root 配置
  - 文献：svn commit r219089；FreeBSD 9.0-RELEASE Release Notes（ZFS 章节）。

## 文献

- FreeBSD Release Engineering Team. FreeBSD 9.0-RELEASE Announcement [Z]. 2012-01-12；FreeBSD Release Engineering Team. FreeBSD 9.3-RELEASE Announcement [Z]. 2014-07-16；Lucas M W. FreeBSD Mastery: Specialty Filesystems [M]. Tilton: Tilted Windmill Press, 2016；FreeBSD Project. release/9.0.0. freebsd-src
- FreeBSD Security Team. FreeBSD Security Support [Z]. security.freebsd.org；各版本 Release Announcement Support 章节［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD 9.0-RELEASE Release Notes [Z]. docs.freebsd.org；Whitehorn N. bsdinstall: A New Installation System for FreeBSD [C]//BSDCan 2011. Ottawa, 2011；**bsdinstall(8)** man page

## 存目（原 122.2.2/122.3.2/122.4.2/122.5.2/122.6.2 抢救残片）

- 上述五节为本 123 章主题（9.x 子系统史）的旧章号抢救残片，其正本体对应磁盘节文件 123.2（bsdinstall）、123.4（ZFS v28/TRIM/lz4）、123.5（CAM/ATA 与 USB 栈）、123.6（网络栈改进含 NFSv4）——残片均截断且含错位文献行，已按正本体删除；其中“122.3.2 UFS2 TRIM”题名与所引文献（实为 ZFS TRIM）错位，一并归档处理。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。