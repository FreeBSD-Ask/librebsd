---
chapter: 第 154 章
id: CH154
volume: 第07卷-freebsd的工程体系重构
---

# 第 154 章 freebsd14x技术淘汰与base精简

## 要点

- FreeBSD 14.0 从 base system 中 **完全移除了** **telnetd(8)**（Telnet 服务器守护进程），这是 base 系统精简的重要一步；Telnet 协议诞生于 1969 年（RFC 15），是互联网最早的应用层协议之一，但因其明文传输所有数据（包括密码）而被认为本质上不安全；FreeBSD 长期以来默认禁用 telnetd（需在 inetd.conf 中手动启用），但一直保留在 base 中；**telnet(1)** 客户端仍保留在 base 中（因为有时仍需用它调试纯文本协议如 SMTP/HTTP），但 telnetd 服务器已移除；这一移除延续了 FreeBSD 自 10.x/11.x/12.x/13.x 持续精简 base system 的趋势——先前已移除了旧版本 GCC、BSD games、GNU grep、许多老旧工具等
- 除 telnetd 外，14.x 周期内 base system 还有多项精简与组件退役：① 32 位平台 RELEASE 构建在 14.x 后终止（15.0 起不再发布 i386 安装镜像，见 85.8）；② 旧版本工具链组件进一步清理——GCC 早已从 base 移除（12.x/13.x 完成），14.x 完成纯 LLVM 工具链（clang、lld、libc++、libc++abi、libunwind）；③ 某些过时的用户态工具被标记为 deprecated 或在 14.x/15.x 过渡期规划移除；④ ports 中大量老旧无人维护的 port 被标记为 DEPRECATED 或移除，但这属于 ports 范畴而非 base；FreeBSD 14.0 还清理了一些旧的驱动与未维护的硬件支持
- 架构平台降级在 14.x 周期内持续进行：① i386（32 位 x86）在 14.x 中仍为 Tier 2 并提供 RELEASE 镜像，但已明确预告 15.0 起停止 RELEASE 构建；② armv6 在 14.0 前已降级为 Tier 3；③ armv7 在 14.x 中保持 Tier 2，但未来降级路径已在讨论；④ MIPS 架构在 13.5 为最后支持版本，14.0 起已从源码树移除 [考据脚注：经 FreeBSD 官方 platforms 页面（2026-05-08 更新）确认，MIPS 全系列（mips/mipsel/mipshf/mipselhf/mipsn32/mips64/mips64el/mips64hf/mips64elhf）最后支持版本均为 13.5，14.x 平台列表中已无 MIPS。]；⑤ powerpc（32 位）、powerpcspe 等老旧 PowerPC 架构逐步降级；⑥ riscv64 保持 Tier 2 并持续完善，升 Tier 1 条件尚未成熟；⑦ aarch64（arm64）作为 Tier 1 在 14.x 中持续成熟，支持越来越多的服务器与开发板硬件；架构 Tier 调整由 Core Team 与 re@ 团队根据活跃开发者数量、用户基数、企业赞助等因素综合评估决定，调整前会提前多个版本预告
- FreeBSD 的 base 精简哲学与 CSRG 传统一脉相承又有重要区别——4.2BSD/4.3BSD 时代（1980 年代）的 BSD 发行版包含完整的源代码与全套工具，“UNIX 即完整操作系统” 是当时的理念；而现代 FreeBSD 面对的生态环境完全不同——开源软件数量爆炸式增长，一个 OS 不可能在 base 中维护所有软件，通过 pkg 安装第三方软件是主流模式；FreeBSD 的精简不是 “功能缺失”，而是明确的职责划分：base 系统提供一个稳定、安全、自洽的最小基础环境，ports/pkg 提供应用生态；这一哲学与 BSD 许可证的自由度相结合，使 FreeBSD 既保持了内核与基本系统的高质量，又通过 ports 提供了海量软件（超过 40,000 个 port）
- 本时期 FreeBSD 核心仓库的贡献高度依赖受雇于企业的核心开发者——iXsystems、Netflix、Intel、Isilon/EMC 等公司将工程资源投入 FreeBSD 的网络、存储与虚拟化子系统，以换取基础设施稳定；这种 “有组织贡献” 与志愿者个人贡献性质不同，二者共同构成 BSD 生态韧性之源（参见本章史观映射总纲第 4/5/13 条）。

## 史观

- 总纲第 4 条——分离聚合是永恒规律：telnetd 的移除标志着过时协议与 FreeBSD base 的分离、一个互联网时代的终结——1980-1990 年代 Telnet 是远程登录 UNIX 主机的标准方式，SSH（Secure Shell）自 1995 年 Tatu Ylönen 发明后逐步取代 Telnet，到 2020 年代 Telnet 已完全退出实际生产使用（仅作为调试工具偶尔使用 telnet 客户端）；FreeBSD 保留 telnet(1) 客户端于 base 中以备调试之需，仅将 telnetd 服务器移除出 base。
- 总纲第 13 条——法律与道德是利益分配：企业赞助方向直接塑造 FreeBSD 在该时期的子系统优先级（如 Netflix 推动内核 TLS 卸载与网络栈高性能化）。
  - 辨析：企业提交多属受雇工作期间的 “有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验。
  - 文献：freebsd.duckdb（freebsd-src contributors 表，窗口 2021–2023，检索 2026-07-21）
- 总纲第 4 条——分离聚合是永恒规律：30 年在 OS 历史中是一段不短的时间——GNU 项目始于 1983 年（40 年）、Linux 始于 1991 年（35 年）、386BSD 始于 1992 年、FreeBSD 始于 1993 年、OpenBSD 始于 1995 年、NetBSD 始于 1993 年；FreeBSD 30 年的历史见证了 UNIX 从实验室到互联网再到云时代的全过程，CSRG BSD 一脉的工程传统仍在延续。
- 专题语——工程文化与技术采用（不设总纲条号）：LLM 辅助编程是软件工程自编译器、IDE、开源协作以来最新的范式转变之一，但 FreeBSD 保守的工程文化决定了其采用速度会慢于商业公司与新兴项目；这不是 “拒绝进步”，而是内核级代码的高风险属性要求——一个驱动 bug 最多导致硬件不工作，一个文件系统或 VM 子系统 bug 可能导致数据损坏；FreeBSD 社区 “代码必须被人理解” 的传统是安全的最后一道防线。
- 总纲第 5 条——没有必然性，只有偶然性：14.x 不是某一个 “革命性” 时刻，而是一系列渐进改进汇聚成的一刻——sendmail 默认地位的终结、32 位平台时代的落幕、纯 LLVM 工具链的完成、后量子密码的首次默认启用、WireGuard 争议的解决，每一个单独看都是渐进演化，但它们汇聚在 14.x 周期，标志着 FreeBSD 从 “20 世纪 UNIX 继承者” 完成向 “21 世纪现代 OS” 的转型。

## 辨析

- 需要区分 “完全移除” 与 “默认禁用”——telnetd 是完全移除（源码树与安装镜像中都不再包含），而非仅仅默认禁用；用户若仍需要 telnetd 可从 ports 安装（telnetd 存在于 ports 中，或使用 net/telnetd 等替代实现）；OpenSSH 自 FreeBSD 4.0（2000 年）起即已在 base 中作为默认远程登录方式，telnetd 的移除在此后 23
- 企业提交多属受雇工作期间的 “有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验。
  - 文献：freebsd.duckdb（freebsd-src contributors 表，窗口 2021–2023，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<https://docs.freebsd.org/en/articles/contributing/>）
- FreeBSD 历史起点的界定存在多种说法：项目最初源于 1992 年的 386BSD 补丁集、FreeBSD 1.0 于 1993.6.19 发布、FreeBSD 2.0（1994.11）是首个相对成熟的版本；30 周年选择以 1.0 发布日期为起点是符合历史惯例的；Jordan Hubbard、Rodney Grimes、Nate Williams 三位创始人中，Jordan Hubbard
- NetBSD 在 2024 年 5 月修订了 commit guidelines，明确将 LLM 生成代码标记为 “tainted code”（受污染代码），需要 Core Team 书面批准才能合入；相比之下，FreeBSD 截至 2026 年 7 月尚无正式政策，更多依赖 committer 个人判断与代码评审流程；两者的差异反映了不同项目的风险偏好——NetBSD 的正式政策更保守，Free
- 关于 “哪个 FreeBSD 版本是最好的” 是社区长期争论的话题——老用户可能怀念 4.x/5.x 时代的简单、7.x/8.x 的稳定、9.x/10.x 的 ZFS 成熟；但客观地说，14.x 是 FreeBSD 历史上功能最完善、安全默认最好、硬件支持最广、工具链最现代的版本；“更好” 是主观判断，但 “更现代、更安全默认” 是客观事实
  - 文献：FreeBSD Project. Rele

## 文献

- FreeBSD Project. FreeBSD 14.0-RELEASE Release Notes — Removed Features [EB/OL]. (2023-11-20)[2026-07-19]. <https://www.freebsd.org/releases/14.0R/relnotes/>; Ylönen T. SSH — Secure Login Connections over the Internet [C]. USENIX Security Symposium, 1996; FreeBSD Project. telnet(1) Manual Page [EB/OL
- freebsd.duckdb（freebsd-src contributors 表，窗口 2021–2023，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<https://docs.freebsd.org/en/articles/contributing/>）［B］


<!-- dangan-20260908 消解回写 -->
- NVIDIA.. Open GPU Kernel Modules [EB/OL]. [2026-07-19]. <https://github.com/NVIDIA/open-gpu-kernel-modules>[EB/OL]. 2026. ［DKC-2274→fulltext:6139］
<!-- /dangan-20260908 -->

<!-- 迁移说明：以下 153.14.2 节系第 153 章内容误植于本章，待跨文件迁移处置（登记 DEFERRED，暂保留存目）。 -->
## 153.14.2 地域与学术的志愿者多样性

- 要点：除企业核心外，FreeBSD 贡献者横跨多国——德国、法国、俄罗斯等地域 ccTLD 与多所大学（如 Stony Brook）的学术贡献显著；区域志愿者填补本地化与硬件移植空白，学术研究者将 BSD 作为操作系统研究的活体平台。
- 史料：
- FreeBSD Foundation. FreeBSD at 30 — Timeline [EB/OL]. (2023-06)[2026-07-19]. <https://freebsdfoundation.org/wp-content/uploads/2023/06/FreeBSD_timeline.pdf>; Hubbard J, Grimes R W, Williams N. FreeBSD 1.0 Release Announcement [EB/OL]. (1993-06-19)[2026-07-19]. comp.unix.bsd Usenet archives; Salus P
- NetBSD Project. Commit Guidelines — LLM-Generated Code Policy [EB/OL]. (2024-05)[2026-07-19]. NetBSD Developer Documentation; U.S. Copyright Office. Copyright Registration Guidance: Works Containing Material Generated by Artificial Intelligence [EB/OL]. (2023-03)[2026-07-19]. <https://www.copyright.gov/ai/ai_policy_guidance.pdf>.
- FreeBSD Project. Release Information for all FreeBSD Releases [EB/OL]. [2026-07-19]. <https://www.freebsd.org/releases/>; McKusick M K, Neville-Neil G V, Watson R N M. The Design and Implementation of the FreeBSD Operating System, 2nd Edition [M]. Boston: Addison-Wesley, 2014. ISBN 978-0-321-96897-5. ［B］　[存疑脚注] 原条目误记为第 3 版（2024 年 expected、ISBN 待确认）；经出版方 Pearson/InformIT 页面核验，现行最新版为第 2 版（2014 年 9 月出版），3rd Edition 截至核验日（2026-09-13）无出版记录，故按第 2 版著录。

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。