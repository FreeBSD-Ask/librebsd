---
chapter: 第 199 章
id: CH199
volume: 第10卷-openbsd的历史
---

# 第 199 章 OpenBSD 6.x 的 pledge 安全机制

## 要点

- pledge 的 CVS commit log 与 **pledge(2)** 手册页历次版本是研究 pledge 演进的核心史料；openbsd.duckdb openbsd-src 仓库中 pledge 相关 commit 自 2015-10-09 起（deraadt“Rename tame() to pledge()”），后续 semarie、benno、millert 等 committer 持续扩展 pledge 覆盖面（时序与覆盖清单以 Release Notes 与 commit log 交叉验证为准）。
- LibreSSL fork 的辩证合图——fork 既是 OpenBSD 对 OpenSSL 工程失败的必要回应（反批评层）也是 TLS 库碎片化的加剧因素（批评层与再批评层），二者并非非此即彼；LibreSSL 在 OpenBSD 生态内具有工程合理性（代码精简、攻击面缩减、ISC 许可证纯洁性、年均低 CVE 频率），但在全球 TLS 生态内具有外部性（碎片化、API 不兼容、维护成本由生态承担）。
- pledge/unveil 设计争议的项目统摄史观审视须从总纲三条切入——其一，总纲第 13 条“法律与道德是利益分配”映射：pledge/unveil 的“简洁正确性”叙事不仅是技术论证也是 OpenBSD 项目身份建构的政治产物，社区对 pledge 的辩护中混合了技术判断（粗粒度降低配置错误）与道德判断（“正确使用简单机制优于错误使用复杂机制”），后者本质是将 OpenBSD 工程哲学包装为普适道德律令的修辞（此判断属形式分析，须以 misc@ 辩护原文为据方可成立，见辨析的道德包装论证辨析）。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4014] 卷“第10卷-openbsd的历史”第 199 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集
- [DB:bsdnow_podcast:outline_mappings:om_11196] BSD Now 第 565 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11238] BSD Now 第 561 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11308] BSD Now 第 553 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11387] BSD Now 第 543 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11396] BSD Now 第 542 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11415] BSD Now 第 539 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11432] BSD Now 第 537 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11462] BSD Now 第 534 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11471] BSD Now 第 533 期，匹配 CH199 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11540] BSD Now 第 526 期，匹配 CH199 章，关联度 1.0

## 史观

- 总纲 9“经验优先”：pledge 由 systrace 难用、file 沙箱半年即弃的实践挫败催生，设计取舍以真实程序的可用性经验为准。
- 总纲 5“没有必然性，只有偶然性”：pledge 的诞生是偶然挫败的产物，而非预先规划的安全路线图。
- 总纲 10“动手者创造历史”：pledge 覆盖面由开发者逐程序审计与需求归类累积而成，非一次性顶层设计。
- 总纲 13“法律与道德是利益分配”：pledge/unveil 的“简洁正确性”叙事既是技术论证亦含项目身份建构的成分，辩护中技术判断与道德判断的配比须以 misc@ 原文为据。

## 辨析

- pledge 演进的具体里程碑以 Release Notes 与 commit log 交叉验证为准——Release Notes 记录用户可见的 pledge 覆盖扩展，commit log 记录具体代码变更；commit log 中的 pledge 相关 commit 以 file_path 含“pledge”或 message_subject 含“pledge”为筛选条件，在 **openbsd.duckdb** openbsd-src 仓库（旧名 **bsd_commits.db**，已拆分为现行 *.duckdb）中筛取相关 commit 后与 Release Notes 逐条对照。
- 合图不寻求消除张力而寻求呈现张力——LibreSSL 的“自主”与“孤立”是同一决策的共生效应，不可分割；【0 信任原则·合图的非终结性】合图并非辩证链的终结而是阶段性综合，随 LibreSSL 与 OpenSSL 演进（如 OpenSSL 3.0 与 LibreSSL 的进一步分化）须重新展开；【0 信任原则·合图的非折中主义】合图不是“LibreSSL 在 OpenBSD 内合理、在生态外不合
- 哲学审视的合理性须以三个层面交叉验证——【0 信任原则·道德包装论证的辨析】“pledge 辩护混合技术判断与道德判断”论证须对照 misc@ 邮件列表原文核实——若辩护文本仅含技术论证（如“粗粒度降低配置错误率”），不得人为添加道德判断成分，须以具体文本为据；【0 信任原则·权力-知识共谋的可证伪性】“pledge 被塑造为正确方向、seccomp 被叙述为包袱”论证须对照 OpenBSD 官方

## 文献

- openbsd.duckdb openbsd-src 仓库 pledge 相关 commit；OpenBSD **pledge(2)** 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；openbsd.duckdb 查询 L1.1.1 与 L1.1.2（原引来源 宏观趋势统计.md §L1.1.1、§L1.1.2〔存疑：原路径 原材料/研究/bsd 仓库分析/ 为树外断链，库内实测未入库〕）；openbsd.duckdb 查询 L2.3.1.pledge 与 L2.3.1.unveil（原引来源 中观模式挖掘.md §L2.3.1〔存疑：同为树外断链路径〕，数据缺口）；统计分析报告：时间序列分析.md Task 14 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/时间序列分析.md**；Python 统计脚本：`script/phase4_time_series.py`. Task 14 ARIMA 建模 + Task 15 MAPE/RMSE 预测精度。执行日期：2026-07-27 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2015-2016 年间：41,347 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- LibreSSL 与 OpenSSL 综合对比研究；TLS 库生态演进史；openbsd.duckdb openbsd-src 仓库 LibreSSL/OpenSSL CVE commit 对比 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2014-2014 年间：20,651 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- 项目史观总纲第 13、19、21 条原文；de Raadt 邮件列表发言 [EB/OL]. <https://marc.info/?laccopenbsd-misc>；OpenBSD **pledge(2)** 手册页 [EB/OL]. <https://man.openbsd.org/pledge.2>；Linux seccomp-bpf 文档 [EB/OL]. <https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html>；Linux landlock 文档 [EB/OL]. <https://docs.kernel.org/userspace-api/landlock.html>；openbsd.duckdb openbsd-src 仓库 pledge 覆盖扩展 commit ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 2018-2018 年间：16,734 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP498、BSD Now EP144、BSD Now EP140（共 3 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Florian Obser 阐述 OpenBSD 三类利用缓解：降权、权限分离与受限服务操作模式，作为攻击者达成任意代码执行后的最后防线；降权是最弱但最古老的缓解，权限分离将不可信数据解析移入低权限进程，受限模式则以 pledge 限制进程能力。（BSD Now EP498，[514.74-603.96]，L2）
- Obser 回溯 ping 降权的历史：Theo de Raadt 逾 26 年前重构 ping，使其先打开原始套接字再丢弃 root 权限，以防本地用户借 ping 缺陷提权；二十年后又发现以 root 调用 ping 时只是从 root 降到 root，遂改为降级到专用用户。（BSD Now EP498，[598.70-632.26]，L2）
- Obser 叙述 pledge 的由来：systrace 由 Niels Provos 开发但因基于系统调用参数而难用，OpenBSD 基础系统中长期仅 sshd 使用；2015 年 Theo 诱使 Nicholas Marriott 用 systrace 沙箱 file 却只坚持半年，成为压垮性体验，Theo 遂开发 tame（后改名 pledge）。（BSD Now EP498，[784.74-861.42]，L2）
- pledge 通过对 OpenBSD 基础程序的需求归类而成，程序违规即被内核以不可捕获的 SIGABRT 终止；当约 50 个程序加入 pledge 后被认为成熟并合入主线，半年内几乎所有基础程序均使用 pledge。（BSD Now EP498，[861.42-931.54]，L2）
- 其余新闻包括 OPNsense 23.1.1 发布、Ansible Clone 工具、NetBSD 在 FOSDEM 2023 的 BSD dev room 报告、FreeBSD Foundation 的 BSDCan 旅行资助，以及 Game of Trees 0.81 与 x-only PKU、pinsyscall 等 OpenBSD 新进展。（BSD Now EP498，[1156.64-2330.00]，L2）
- Provost 论证 FreeBSD PF 的 IPv6 分片处理缺陷：PF 重组分片并做出过滤决策后，IPv4 下可交回协议栈重新分片，而 IPv6 为保住路径 MTU 发现必须把分片集合原样送出，netpfil 接口却只支持一包进一包出；PF 目前自行调用 ip6_output 或 ip6_forward，既构成层级违例又存在输出/转发判断错误，特定情形下导致 panic 或丢包；OpenBSD 由协议栈告知 PF 数据包方向的做法可资借鉴，计划中的改造是让 netpfil 支持一包进一堆出，并预期 IPFW 处理 IPv6 分片时同样受益。（BSD Now EP144，[1579.66-1853.0]，L1）[订正：原 [1579.66-1794.88]，2026-09-30 SenseAudio 重转核对]
- Theo de Raadt 提交使 OpenBSD 的 W^X 违例默认不再允许：违例时内核生成日志，mprotect 与 mmap 返回 ENOTSUP，可经 sysctl 改为 SIGABRT 以便调试与取核转储；同时引入 wxallowed 挂载选项按文件系统豁免，commit 原文断言上游开发者终将理解 W^X 违例是极高风险的编程风格并终被彻底禁绝，此前建议在 /usr/local 文件系统使用该选项；主持人评价这使用户得以审计 ports 与自装程序并向上游施压推动修复。（BSD Now EP144，[975.68-1114.66]，L2）
- Theo de Raadt 的 Pledge 演讲经主持人转述：pledge 在系统调用层约束进程能力，OpenBSD 的 NTP 守护进程已在内部使用；演讲披露迄今约 10% 被 pledge 的程序被发现试图执行安全范围之外的动作；未来方向包括回头检视 2003 年前后引入的 OpenSSH 特权分离，以及向其他操作系统输出 pledge 类机制的意愿。（BSD Now EP144，[130.44-250.50]，L2）
- FreeBSD 11.0 发布前夜的两项工程经主持人详述：bhyve 在项目分支 projects/bhyve-graphics 获得 UEFI GOP 支持，用户态虚拟显卡把画面送进内建 VNC 服务器，辅以 XHCI（USB 3 仿真）与平板定位实现精准鼠标、PS2 键鼠兜底、可选等待连接后再启动，并已在 Windows 7/8/8.1/10、Server 2012/2016、Ubuntu 15.10、FreeBSD 10.3/11 上验证，grub-bhyve 被定性为权宜之计、单命令 EFI 启动才是长期目标；zfsd 则补齐内核之外的 ZFS 故障管理，监听 devctl 事件自动激活热备，按 zfs 标签与物理路径处置盘位插拔，60 秒内 50 次 IO 或校验和错误即标记故障并换盘，管理员仅经池属性 autoreplace 间接控制，默认未启用。（BSD Now EP144，[243.24-975.32]，L2）
- FreeBSD 图形栈跟进：Linux 4.6 DRM 更新需要用户测试，bsddesktop.com/images 提供 USB 启动测试镜像，非安装器、不改动既有系统；开发者 Matt Macy 经 IRC 转达 AMD/ATI 支持将至，且此项工作主要目标本是 AMD 而非 Intel，Intel 只是副产品；同期 head 的 C++ 变更致 VLC 等断裂，使 11 中 KDE、GNOME 3、XFCE、MATE 的桌面包暂缺——约 300 个包失败、600 个被阻断，占 26000 个包不足 2%，却几乎覆盖桌面所需，Warren Block 的 notebook-stats 脚本用于收集硬件细节以定位问题配置；主持人计划携镜像赴 BSDCan 分发。（BSD Now EP144，[2932.90-3198.18]，L2）
- OpenBSD 6.0 移除 systrace 的论证被归纳为模型错位：程序常需在启动期执行特殊系统调用而后不再需要，静态全局限制要么过松要么令程序失效，而 pledge 与 Capsicum 式“启动完成后降权”更贴合实际故而更严格；主持人并以旁证收束——NetBSD 早在 2007 年移除，Linux 最后版本止于 2.6.1，保留旧有冗余已无意义。（BSD Now EP140，[3242.2-3317.7]，L2）[订正：原 [3249.92-3322.20]，2026-09-30 SenseAudio 重转核对]
- Backtrace 创始人 Samy Al Bahra（转写作 Sammy）主张符号调试自 Steve Bourne 的 adb 以来停滞约二十年，其平台以高性能调试器提取故障时刻状态、以调用栈签名聚合同类故障入集中对象存储并自动分派（建 JIRA 工单、通报安全团队），并与 FreeBSD 内核 UMA 分配器集成以自动标注悬空指针与双重释放；其宣称 libkvm 优化使简单回溯从两分钟级降至一秒内，GDB 在五万线程、500GB RSS 的客户负载上二十分钟的回溯缩至二至三秒。　[存疑脚注] 全部性能数字与产品能力均为创始人单方陈述，未经独立验证；专名 PT Malak（2191.54-2199.06）疑为 ptmalloc 之转写失真（BSD Now EP140，[2012.7-2098.1]，L1）[订正：原 [2012.24-2062.24]，2026-09-30 SenseAudio 重转核对]
- Ted Unangst 的程序命名考揭示 argv[0] 的多重身份——文件系统名、调用名与程序自认名可彼此背离，grep/egrep、md5/sha2 家族与 test/[ 均有意利用之；但 syslog 默认采用 progname，使特权工具可被改名以规避日志监控，doas 已修复此面而 sudo 的部分配置仍受其扰，作者由此提出 progname 是有用的抽象、却正缓慢退化为货物崇拜式惯例。（BSD Now EP140，[817.4-1239.7]，L2）[订正：原 [849.42-1226.70]，2026-09-30 SenseAudio 重转核对]

**史料**：

- Florian Obser《Privilege drop, privilege separation and restricted service operating mode in OpenBSD》（sha256.net 博客），为 OpenBSD 开发者本人的一手技术文章，经节目转述。（BSD Now EP498，[508.82-1144.64]，L1）
- OpenBSD tech 邮件列表中 Theo de Raadt 关于 pinsyscall 的帖子，涉及 ExecVE 与 ROP pivot，为当事人一手陈述，经节目转述。（BSD Now EP498，[2272.22-2304.38]，L1）
- Game of Trees 0.81 发布与 Stefan Sperling 在 FOSDEM 2023 的演讲及幻灯片，为官方发布线索，经节目转述。（BSD Now EP498，[1823.68-1923.94]，L2）
- 一手材料密集：Kristof Provost 在 AsiaBSDCon 的现场访谈自述（入坑经历、补丁被批评被测试再合并的流程、搞崩共同主持人 Alan 路由器的复盘）；Theo de Raadt 的 Pledge 主题演讲视频与幻灯片；Eric McCorkle 谈 EFI 启动重构与 GELI 支持的博客（附 GitHub 代码链接与成段引文）；Sean Chittenden 的 Postgres 多数据中心高可用演讲；Michael W. Lucas 的 Faces of FreeBSD 入行自述；Netgate UFO 板卡的 dmesg 启动日志与 openssl speed 实测数据。　[存疑脚注] 转写专名多处音转失真（Kristof Provost 转作 Christophe、bhyve 转作 beehive、GELI 转作 Jelly、Consul 转作 console、W^X 转作 WXRX、Netgate UFO 转作 NetGate UFW），语义均可由上下文复原；唯 Theo de Raadt 演讲场合转写作“Dot Security 2016”无法与 2016 年已知公开演讲日程对确。（BSD Now EP144，[1277.04-2311.52]，L1）
- 该期可辨识的一手与当事人材料包括：FreeBSD 2016 年第一季度核心团队季度报告（ASLR 进展、Ceph 移植与 pNFS 支持为要点）、FreeBSD 10.3 的 errata notice（解释 PKG 1.7.0 性能回退根因）、Ted Unangst 关于程序命名的技术文章、LibreSSL 路线讨论文章、Backtrace 创始人调取客户生产故障数据的现场演示、Allan Jude 对欧洲黑客松与开源数据中心会议的亲历叙述，以及 Linux Fest Northwest 演讲视频存档；主持人转述 Ceph 移植动机时引述“Ceph has this concept called like RDB, which is kind of Ceph's version of a Zvol”（386.00-391.20）。（BSD Now EP140，[338.5-452.6]，L2）[订正：原 [347.76-445.20]，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲10 动手者创造历史：安全机制由开发者逐个程序地审计与归类累积而成，而非一次性顶层设计。：Theo 与 Obser 等通过逐个程序的重构与需求归类塑造 OpenBSD 安全机制。（BSD Now EP498，[861.42-931.54]，L2）
- 总纲9 经验优先：以基础系统中真实程序的可用性经验为标准，淘汰难以使用的 systrace。：systrace 因难用而被 pledge 取代，设计取舍来自真实程序的实践经验。（BSD Now EP498，[784.74-861.42]，L2）
- 总纲5 没有必然性，只有偶然性：pledge 的诞生由 systrace 实践中的偶然挫败触发，而非预先规划。：file 沙箱半年即弃的偶然失败促成 tame 与 pledge 的诞生。（BSD Now EP498，[784.74-861.42]，L2）
- 总纲10 动手者创造历史：本期是动手者创造历史的微观样本：Kristof Provost 的入坑起因只是“因为它跑不起来”，为修一块 Marvell 板卡上的问题从此一直在找 bug，补丁经批评、测试、合并的循环把他卷成 committer；Michael W. Lucas 因深夜 DNS 管理员离职被顶上岗位、为睡安稳觉换掉 Unixware 与 Solaris 转向 BSD；系统的演进正由这类具体修补与无名测试者的反馈累积而成。（BSD Now EP144，[1306.72-1354.34]，L1）
- 总纲22 知识注定过时：工程知识的过时性在本期反复显形：grub-bhyve 被当事人定性为“一直只是权宜之计”，单命令 EFI 启动才是长期目标；McCorkle 判定自建的 boot1 非 EFI 提供者框架与 EFI 框架既有功能重复、接口别扭且无法向内核传递密钥，重构后 boot1 缩为一个很小的源文件并与 loader 共享全部后端驱动，bcache 成为通向 EFI 驱动模型与热插拔支持的唯一阻碍——每一代被视为完成的方案，都会成为下一代重构的对象。（BSD Now EP144，[2619.86-2734.50]，L2）
- 22 知识注定过时：systrace 的生灭是知识注定过时的标本：OpenBSD 首创、并曾被多系统跟进的安全机制，因承诺与真实使用模式脱节而被 pledge 接替，最终在多系统中殊途同归地清退——首创性并不赋予技术方案永续的正当性，其存续取决于能否在实际使用中维持解释力，形式一俟失效即被新形式重构取代。（BSD Now EP140，[3242.2-3317.7]，L2）[订正：原 [3257.52-3319.04]，2026-09-30 SenseAudio 重转核对]
- 6 和解优于斗争：Backtrace 与 FreeBSD 社区的关系呈现和解式嵌入的形态：公司以“FreeBSD developers care about stability and care about quality”（2775.36-2781.76）为优先 FreeBSD 的理由，经由赞助 BSDCan、与 Jenkins 测试集群集成、向 freebsd.org 开发者免费开放平台进入社区网络，商业基础设施与志愿者社区的利益由此耦合，对抗性让位于协作性。（BSD Now EP140，[2772.76-2801.00]，L2）

**辨析**：

- Obser 所述 Theo 逾 26 年前重构 ping 的具体年份需与 OpenBSD 提交史核验，节目转述未给出提交编号。　[存疑脚注] ping 重构年份为口述概数，须以 OpenBSD 提交记录与变更日志核验。（BSD Now EP498，[598.70-632.26]，L4）
- pledge 从 tame 更名的具体时间与 5.8、5.9 版本对应关系为概略叙述，需以 OpenBSD 发布说明与 man 页核验。　[存疑脚注] tame 更名 pledge 及对应版本为概略叙述，需以 pledge(2) 手册与发布说明确认。（BSD Now EP498，[861.42-931.54]，L4）
- 听众 Bill 的安装失败归因存在可考辨的争议：其归咎 ZFS 默认文件系统与 legacy MS-DOS 分区不兼容，主持人则把故障机制改判为 GPT 分区表使部分主板（Lenovo）拒绝引导，且 PC-BSD/GhostBSD 强制 ZFS 属发行版选择而非 ZFS 缺陷；主持人“ZFS will change your life”（5271.86-5275.90）式的布道话语亦应视为社区推广文化的一部分，而非中立技术评估。（BSD Now EP140，[5140.0-5302.6]，L2）[订正：原 [5155.90-5303.58]，2026-09-30 SenseAudio 重转核对]
- 本期标题所示“DDoS for the People”文章在转写中并无对应讨论段落，其内容无法由本转写证实；转写为双音轨交错、时间戳乱序且专名失真频发——Olivier Cognet、Larry Kofiro、ZX Backup、AfriBIC 等均未经核对，涉及具体人名与工具名的引用前必须核对原始 show notes。　[存疑脚注] 标题文章内容未见于转写；Olivier Cognet、Larry Kofiro、ZX Backup、AfriBIC、PT Malak 疑为转写失真，待核 show notes（BSD Now EP140，[2191.54-2199.06]，L4）

**文献**：

- [BSD Now EP498] Pennington J. BSD Now: 498: Dropping Privileges[EB/OL]. (2023-03-16)[2026-08-15]. <https://www.bsdnow.tv/498>.
- [BSD Now EP144] Pennington J. BSD Now: 144: The PF life[EB/OL]. (2016-06-01)[2026-08-15]. <https://www.bsdnow.tv/144>.
- [BSD Now EP140] Pennington J. BSD Now: 140: Tracing it back to BSD[EB/OL]. (2016-05-04)[2026-08-15]. <https://www.bsdnow.tv/140>.

<!-- /PODCAST_REVIEW -->
