---
chapter: 第 201 章
id: CH201
volume: 第10卷-openbsd的历史
---

# 第 201 章 openbsd-6x的安全机制综合演进

## 要点

- 2017-2021 应用沙箱：OpenBSD 6.x 的 pledge/unveil 以极简声明引领，FreeBSD Capsicum 以能力句柄深入，Linux seccomp 以 BPF 灵活，Windows AppContainer 与 macOS Sandbox 闭源/半开源；OpenBSD 6.x 的极简沙箱影响行业（如部分思路入 Linux）  **2017-2021 同期应用沙箱机制**
- 6.x 周期是 OpenBSD“主动审计—快速修复—加固重构”循环的形成期——**主动审计** 体现于 6.0 errata 中 8 月 3 日单日发布 029-039 共 11 个 patch（含 9 个 SECURITY FIX），反映一次系统性的内核安全审计；**快速修复** 体现于 Spectre v2 披露后 14 天内提交修复 commit（kettenis `d855ec95cfe6
- 从项目史观总纲第 5 条“没有必然性，只有偶然性”与总纲第 13 条“法律与道德是利益分配”审视，LibreSSL fork 与 RETGUARD 皆非“安全必然性”的产物，亦非纯粹的工程道德选择，而是偶然事件与利益分配的交汇。总纲第 5 条指出，每一次 fork、每一个技术决定都是不可替代的偶然——Heartbleed 于 2014 年 4 月 7 日披露是偶然事件，OpenBSD 团队当日即由
- OpenBSD 6.4（2018-10-18）引入 **unveil(2)** 系统调用用于文件系统路径访问限制——unveil(2) 允许进程在启动时声明所需访问的文件系统路径（如 `unveil("/var/www", "r")`），内核据此限制进程的文件系统访问范围，未声明的路径对进程不可见；〔订正：原稿误作 6.2（2017-10-09）引入 unveil(2)，实系 OpenBSD 6.4 引入，6.2 仅含 pledge 改进、RETGUARD、KARL 等，依核查报告订正〕〔待核：原文截断，后文待回源〕

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3900] 卷“第10卷-openbsd的历史”第 201 章，匹配置信度 folder，原因：folder 第199章
- [DB:references_fulltext:chapter_matches:chmatch_4015] 卷“第10卷-openbsd的历史”第 201 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

## 史观

- 章级史观汇总（子节映射摘要，详见子节文件史观/辨析字段）：6.x 时期安全机制的演进呈现多重总纲映射——pledge/unveil 极简沙箱路线与 LibreSSL fork 均非必然产物，系 Heartbleed 等偶然事件与许可证利益分配的交汇（总纲第 5 条“没有必然性，只有偶然性”；总纲第 13 条“法律与道德是利益分配”）；主动审计—快速修复—加固重构循环由开发者逐项动手推进（总纲第 10 条“动手者创造历史”）；沙箱机制在 pledge/unveil、Capsicum、seccomp 等路线间并存互鉴（总纲第 8 条“本体论上各方平等”）。

(原占位“(待人工回填——详见子节文件史观/辨析字段)”已按子节映射摘要回填，依核查报告订正)

## 辨析

- 沙箱“简洁 vs 灵活”是设计权衡——pledge 的采用门槛最低（一行 `pledge()` 调用），seccomp 的表达力最强（BPF 过滤器可定义任意系统调用过滤规则），Capsicum 的粒度最细（能力句柄可绑定至单个文件描述符）
- **须精确说明 6.0 errata 8 月 3 日单日 11 个 patch 的性质**：029_sigio（RELIABILITY）、030_sendsyslog（RELIABILITY）、031_fuse（SECURITY）、032_recv（SECURITY）、033_tcp_usrreq（SECURITY）、034_sockaddr（SECURITY）〔待核：原文截断，后文待回源〕
- 考据过程留痕——【查证来源】总纲第 5 条与第 13 条原文经 据原文第 25 章 一手核验，第 5 条明确“每一次 fork、每一个技术决定，都是不可替代的偶然”，第 13 条明确“任何道德问题本质上是利益问题”；LibreSSL fork 的 commit 时间线经 openbsd.duckdb openbsd-src 仓库 commits 表一手核验（djm `af0b15b8442f` 2
- unveil(2) 引入的考据须遵循 0 信任原则——【查证来源】（1）OpenBSD 6.4 release 页面（<https://www.openbsd.org/64.html>）经检索，记载发布日期 2018-10-18 与 unveil(2) 引入〔订正：原稿误引 6.2 release 页面（62.html），62.html 不记载 unveil(2)〕；（2）**unveil(2)** 手册页记载 unveil(2) 系统调用的设计与约束机制；（3）bsd_commi

## 文献

- OpenBSD 6.x Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；各系统沙箱文档 ［B］

---

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD Project. OpenBSD 6.0 Errata [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata60.html>; OpenBSD Project. OpenBSD 6.4 Errata [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata64.html>; OpenBSD Project. pledge(2) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/pledge.2>; OpenBSD Project. unveil(2) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/unveil.2>; OpenBSD Project. syspatch(8) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/syspatch.8>; OpenBSD Project. signify(1) Manual Page [EB/OL]. [2026-07-22]. <https://man.openbsd.org/signify.1>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. [2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. openbsd.duckdb — openbsd-src 6.x security commits [DB/OL]. 2026-07-22. SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name =‘openbsd-src’ AND author_date >=‘2016-09-01’ AND author_date <‘2019-10-01’ AND (message_subject LIKE ‘%CVE-%’ OR message_body LIKE ’%CVE-%’ OR message_subject LIKE ‘%security%’ OR message_subject LIKE ’%spectre%’ OR message_subject LIKE '%meltdown%’) ORDER BY author_date ASC ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- 项目史观总纲第 5 条、第 13 条。见：据原文第 25 章；项目史观总纲第 5 章偶然性论述。见：据原文第 5 章；openbsd.duckdb openbsd-src 仓库 LibreSSL/RETGUARD 相关 commit（af0b15b8442f、b6553af36068、e688c2b0648a）；LibreSSL 官方公告 [EB/OL]. <https://www.libressl.org/>；OpenSSL Apache 许可证文本；LibreSSL ISC 许可证文本 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。
- OpenBSD 6.2 release 页面 ［EB/OL］. <https://www.openbsd.org/62.html>；**unveil(2)** 手册页；OpenBSD 邮件列表存档；undeadly.org 报道；03-原始史料库/06-考据记录/（20260723_announcements-openbsd.md，〔存疑：原件未入库，待迁移〕） § 二.4.3；openbsd.duckdb openbsd-src 仓库 ［A］
- FreeBSD 社区论文：[FP-2022-001] Refining FreeBSD's Kernel Crypto Framework（John Baldwin（约翰·鲍德温），2022）<https://papers.freebsd.org/2022/bsdcan/baldwin-refining_freebsds_kernel_crypto_framework/>
- FreeBSD 社区论文：[FP-2021-008] smart(8) Update: A Permissively-Licensed Alternative to smartctl(8)（Michael Dexter（迈克尔·德克斯特）; Chuck Tuffli，2021）<https://papers.freebsd.org/2021/eurobsdcon/dexter-tuffli-update_on_smart/>
- FreeBSD 社区论文：[FP-2019-076] FreeBSD at Work: Building Network and Storage Infrastructure with pfSense and FreeNAS（Conor Beh，2019）<https://papers.freebsd.org/2019/vbsdcon/beh-freebsd_at_work/>
- FreeBSD 社区论文：[FP-2019-002] BSD Unix Solutions in the Australian NFP/NGO Health Sector（Jason Tubnor，2019）<https://papers.freebsd.org/2019/asiabsdcon/tubnor-bsd_unix_solutions_in_the_australian_nfp_ngo_health_sector/>
- FreeBSD 社区论文：[FP-2019-014] LLVM and the state of sanitizers on BSD（David Carlier，2019）<https://papers.freebsd.org/2019/asiabsdcon/carlier-llvm_and_the_state_of_sanitizers_on_bsd/>
- FreeBSD 社区论文：[FP-2018-010] Preparing your home router(s) for the future: A journey through Homenet and interconnected objects（Massimiliano Stucchi，2018）<https://papers.freebsd.org/2018/bsdcan/stucchi-preparing_your_home_routers_for_the_future/>
- FreeBSD 社区论文：[FP-2017-014] Isolated BSD build environments using virtual and hardware machines（Michael Dexter，2017）<https://papers.freebsd.org/2017/vbsdcon/dexter-isolated_bsd_build_environments_using_virtual_and_hardware_machines/>
- FreeBSD 社区论文：[FP-2017-009] My BSD sucks less than yours（Baptiste Daroussin（巴蒂斯特·达鲁桑） Antoine Jacoutot（安托万·雅库托），2017）<https://papers.freebsd.org/2017/fosdem/bapt-my_bsd_suck_less_than_yours/>

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP374、BSD Now EP351、BSD Now EP325、BSD Now EP322、BSD Now EP203（共 5 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- OpenBSD 于 2020 年 10 月 18 日发布 6.8 版，正值项目创立二十五周年；该版引入由引导装载器向内核传递的随机种子置信度标记、在支持的 arm64 处理器上启用 PAN，并改进 FFS、安装镜像与多架构安装引导。（BSD Now EP374，[0.0-10.72]，L2）
- NetBSD 于 2020 年 10 月 18 日发布 9.1，新增并行磁盘加密、C.UTF-8 区域设置、ZFS 支持增强、NVMM 虚拟机监控器更新以及 PowerPC64 PowerNV 支持。（BSD Now EP374，[590.42-796.96]，L2）
- OpenZFS 开发者峰会 2020 因疫情改以 Zoom 举办，采用 webinar 演讲与虚拟走廊并行的组织方式；峰会自 2013 年起规模持续扩大，本年取消人数上限后允许更多人参加。（BSD Now EP374，[847.32-970.56]，L1）
- BastilleBSD 相关文章将容器技术谱系上溯至 1979 年 Unix 第七版 chroot，指出 jail 术语最早见于 1991 年 4.3BSD，FreeBSD 4.0 于 2000 年提供 jail 命令，Linux 迟至 2008 年才有 LXC、2013 年才有 Docker。（BSD Now EP374，[1848.72-2116.32]，L2）
- OpenBSD 6.7 于 2020 年 5 月 19 日如期发布，延续其固定发布周期；本期逐项梳理 FFS2 默认、软 RAID 加密、PowerPC 默认编译器切换等改动。（BSD Now EP351，[426.2-433.64]，L2）
- 安全方面，OpenBSD 6.7 将 unveil 用于 82 个用户态程序，把 dig、host、nslookup 从 BIND 源码中剥离并以 pledge 收紧，体现 6.x 安全机制的持续扩散。（BSD Now EP351，[729.32-749.88]，L2）
- Chris Siebenmann 的文章考据 chown 语义的 Unix 分野：V7 与 4.2BSD 限制普通用户转让文件所有权，System III/System V 放开，POSIX 允许两种行为并存，现代系统多采 BSD 一侧。（BSD Now EP351，[1344.98-1550.98]，L2）
- FreeBSD 12.1 是首个以 open ZFS 端口支撑原生 ZFS 加密所需密码学原语的版本，同时导入 BearSSL 为 Juniper 的验证引导装载器提供轻量 TLS，并纳入 MLX5 固件更新工具与 FUSE 驱动重写。（BSD Now EP325，[63.84-68.92]，L2）
- 12.1 预告 i386 默认 CPU 类型将由 486 升至 686（自 13 起），因 486 缺 64 位原子操作且用户态无法模拟；CTM 与 timed 等工具被标记废弃。（BSD Now EP325，[543.78-594.94]，L2）
- 重刊的《Unix Evolution 1975–1984》一文梳理 research Unix v6/v7/v8 的文本格式化、编译器与开发工具流变，并记述 Ritchie 关于 man page BUGS 节以公开羞辱促修复的自述。（BSD Now EP325，[723.74-1018.28]，L2）
- OpenBSD 在 base unbound 默认启用 DNSSEC 验证，并以 Quad9 的 9.9.9.9 做约束验证绕开 NTP 与 DNSSEC 的时钟引导死锁；2018 年曾因时钟问题回滚后于此次重开。（BSD Now EP325，[2062.14-2169.84]，L2）
- Rainbow Crack 的 OpenBSD 编译补丁引出彩虹表原理：加盐与多轮散列（bcrypt 可至百万轮、SHA-512 crypt 默认万轮）使针对字典的预计算表失效，凸显密码存储需抗彩虹表算法。（BSD Now EP325，[2632.88-2909.48]，L2）
- Warner Losh 通过 Bell Labs 1968 年影片《The Incredible Machine》比对 DEC 目录与现场服务清单，论证片中 PDP-7 即 Ken Thompson 所用序列号 34：具备 340 显示器与 444B 纸带机、无 DECtape。（BSD Now EP322，[407.26-941.24]，L2）
- 影片中机器生成音乐、与视觉声学部门来源吻合，配置、日期、无磁带三条证据链共同支持其“Unix 之母机”身份，但 Warner 仍以弱证据与强证据区分，未作绝对断言。（BSD Now EP322，[936.56-977.82]，L2）
- OpenBSD 6.6 为第 47 个发布，unveil 已用于 77 个用户态程序，移除 bridge 输出快速路径内核锁，加入 Intel MDS 缓解与 malloc 隐蔽/清零 API，并更新 VMM 以透传 MSR 缓解位。（BSD Now EP322，[1059.96-1598.48]，L2）
- OpenSSH 8.1 修复 XMSS 私钥解析整数溢出，并在 RAM 中加密静态私钥以防 Spectre/Meltdown 类侧信道；RSA 证书签名默认改用 SHA2-512，不兼容 7.2 之前的客户端。（BSD Now EP322，[2107.02-2265.46]，L2）
- GhostBSD 澄清其基于 TrueOS/FreeBSD 12 stable，官方桌面为 MATE，其他桌面以社区版本维护，项目提供构建与托管支持并欢迎贡献。（BSD Now EP322，[1778.00-1862.98]，L2）
- 该期以“ZFS 是否还是最佳文件系统”为引，反驳一篇称 ZFS 陷于过去的博文：指出异步销毁、透明压缩、分配类、vdev 移除等大量特性均为近十年新增，ZFS 并未停滞。（BSD Now EP203，[377.50-720.00]，L2）
- 主持人梳理 ZFS 法律史：2007 年 NetApp 诉 Sun 侵犯 WAFL 专利，Sun 反诉，最终互不侵权；Oracle 收购 Sun 后关闭 OpenSolaris 源码，OpenZFS 项目从最后的开源版本分叉并延续至今。（BSD Now EP203，[148.62-241.44]，L2）
- 技术反驳包括：去重收益常被压缩抵消，Intel 的分配类（allocation classes）与元数据分层可实现混合存储；George Wilson 与 Matt Ahrens 的 2014/2016 空间分配改进缓解了大而碎池的性能悬崖。（BSD Now EP203，[522.88-800.00]，L2）
- Theo de Raadt 在 OpenBSD 技术邮件列表报告内核随机重链接（KARL）进展：安装、升级与每次开机都会以随机顺序与偏移重链接生成唯一内核，使单个指针泄露无法推断其他地址，并要求用户测试 6.2 快照。（BSD Now EP203，[4432.62-4690.58]，L2）
- Jörg Sonnenberg 公告 NetBSD 仓库 CVS→Fossil→Git 转换迁至新家，改用 SHA-512 校验；同期 LibreSSL 2.5.5 与 2.6.0 发布，后者将成为 OpenBSD 6.2 的一部分。（BSD Now EP203，[5080.48-5480.00]，L2）

**史料**：

- OpenBSD 6.8 官方变更日志与发行公告，涵盖 OpenSSH 8.4、LibreSSL 3.2.2、OpenSMTPD 与 VMM/VMD 更新，由主持人转述。（BSD Now EP374，[357.24-391.04]，L2）
- NetBSD 9.1 官方发布公告，涵盖 cgd 并行磁盘加密、ZFS、NVMM、NPF、X11 默认窗口管理器切换等内容，由主持人转述。（BSD Now EP374，[590.42-823.44]，L2）
- OpenZFS 开发者峰会 2020 议题，包括 Matt Ahrens 论 OpenZFS 状态与版本化、George Wilson 论 ARC 与操作系统内存协作、持久 L2ARC、ZIL 并行化、顺序重建与 send/recv 性能提升，由 Alan Jude 亲历转述。（BSD Now EP374，[974.72-1777.74]，L1）
- OpenBSD 6.7 变更日志与发布公告，含 FFS2、softraid 加密、PowerPC Clang、SMP 与硬件驱动改进。（BSD Now EP351，[476.52-480.64]，L2）
- V7 与 4.2BSD 的 chown 手册页及源码，以及 POSIX chown 规范的 rationale 章节（节目引述）。（BSD Now EP351，[1373.9-1542.98]，L2）
- LibreSSL 3.1.1 与 OpenSSH 8.3 随 6.7 更新，OpenSSH 移除 SHA-1 证书签名算法支持。（BSD Now EP351，[816.68-855.76]，L2）
- FreeBSD 12.1 发布公告与 releng 说明，列明 open ZFS、BearSSL、MLX5、FUSE 重写及废弃项。（BSD Now EP325，[128.32-148.56]，L2）
- Microsystems Magazine 1984 年 11 月号《Unix Evolution》文章（Daemon News 1999 重刊），为节目重读的历史文本。（BSD Now EP325，[740.14-756.02]，L2）
- Dennis Ritchie 关于 man page BUGS 节政策的引文，属当事人一手表述。（BSD Now EP325，[1012.82-1027.82]，L1）
- OpenBSD unbound.conf 默认 DNSSEC 与 aggressive NSEC 的提交说明，及与 Quad9 的约束验证讨论。（BSD Now EP325，[2077.00-2124.28]，L2）
- Warner Losh 博客《Hunting Down Ken's PDP-7》及 Bell Labs《The Incredible Machine》1968 年影片。（BSD Now EP322，[400.18-979.3]，L2）[订正：原 [400.18-402.92]，2026-09-30 SenseAudio 重转核对]
- DEC PDP-7 销售目录与 Bitsavers 现场服务清单（序列号 34/149 的选件记录）。（BSD Now EP322，[545.0-707.24]，L2）[订正：原 [685.26-707.24]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 6.6 发布页与升级说明（unveil、MDS 缓解、预编译包数量等）。（BSD Now EP322，[1063.56-1528.5]，L2）[订正：原 [1063.56-1068.82]，2026-09-30 SenseAudio 重转核对]
- OpenSSH 8.1 发布公告，含 Adam Zabrocki 报告的 XMSS 私钥解析漏洞。（BSD Now EP322，[2125.36-2172.60]，L2）
- OpenZFS wiki 公司列表与 Dev Summit 材料；OpenBSD 技术邮件列表 KARL 状态帖；NetBSD announce 仓库转换公告；LibreSSL 发布说明。（BSD Now EP203，[148.62-5480.00]，L2）

**史观**：

- 总纲10 动手者创造历史：OpenZFS 峰会的进展来自各平台维护者在 ARC 内存协作、持久 L2ARC、顺序重建等具体工程上的改进，而非单一权威的主导。（BSD Now EP374，[1024.98-1169.92]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 代码在 FreeBSD、Linux、illumos、macOS、Windows 之间聚合，jail 则在 chroot 基础上分离出独立的隔离模型，两者皆呈现分离聚合的循环。（BSD Now EP374，[1848.72-2116.32]，L2）
- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：chown 与配额语义的分野最终服务于磁盘空间这一稀缺资源的分配与控制，POSIX 以允许差异化的方式调和各方。（BSD Now EP351，[1505.46-1542.98]，L2）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：BSD 与 System V 从共同 V7 祖先分离出相反的 chown 语义，再由 POSIX 规范聚合为可共存的行为。（BSD Now EP351，[1344.98-1550.98]，L2）
- 总纲3 不存在进步，只有权力再分配：总纲3 不存在进步，只有权力再分配：i386 486→686、GCC 4.2 弃用、CTM 与 timed 废弃不是进步，而是支持资源在不同架构间的再分配。（BSD Now EP325，[567.10-625.50]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：FreeBSD、OpenBSD、HardenedBSD、OPNsense 同屏报道，各分支地位平等，不以体量定优劣。（BSD Now EP325，[1698.58-1805.42]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Tom Jones 以 git worktree、tmux、cscope、bhyve 的动手流程呈现 FreeBSD 开发者的真实工作方式。（BSD Now EP325，[1317.46-1484.78]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：1984 年文章自承需源许可并签血誓方可读源码，而 V7 源码迟至 2002 年由 Caldera 释放，知识条件随时间失效。（BSD Now EP325，[923.02-977.30]，L2）
- 总纲12 科学是形式主义：总纲12 科学是形式主义：密码学的“安全”依赖加盐与轮数的形式约定，彩虹表攻击揭示其相对性而非绝对真理。（BSD Now EP325，[2864.92-2909.48]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：OpenBSD 2018 年曾默认开 DNSSEC 后回滚、2019 年再启用，取决于时钟引导问题被偶然解决。（BSD Now EP325，[2124.78-2143.00]，L2）
- 总纲1 一切真历史都是古代史：总纲1 一切真历史都是古代史：50 年前的机器被当作文物考据，当下的档案即未来的历史。（BSD Now EP322，[985.90-1007.10]，L2）
- 总纲17 证明世界先于解释和改造世界：总纲17 证明世界先于解释和改造世界：先有 PDP-7 实物与影片证据，再谈 Unix 起源解释。（BSD Now EP322，[461.82-466.08]，L2）
- 总纲19 解释学循环是历史认识的根本条件：总纲19 解释学循环是历史认识的根本条件：影片截图与目录照片互为印证，逐项比对构成循环解释。（BSD Now EP322，[558.72-631.14]，L2）
- 总纲22 知识注定过时：总纲22 知识注定过时：SSH 旧客户端与 RSA-SHA1 证书兼容性被新默认淘汰，知识随版本更替失效。（BSD Now EP322，[2236.64-2265.46]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：OpenBSD 6.6 与 OPNsense、GhostBSD 同屏，各项目如实呈现。（BSD Now EP322，[1608.32-1905.7]，L2）[订正：原 [1608.32-1616.96]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Warner Losh 逐帧考证、OpenBSD 开发者逐锁解锁，动手者推动认识与系统演进。（BSD Now EP322，[982.99-1165.6]，L2）[订正：原 [982.99-1036.46]，2026-09-30 SenseAudio 重转核对]
- 总纲5 没有必然性，只有偶然性：ZFS 从 Sun 内部项目到 OpenZFS 社区的转折由诉讼、收购等偶然事件驱动，社区分叉后反而延续了技术生命，体现分离聚合与偶然性在文件系统史中的塑造。（BSD Now EP203，[148.62-241.44]，L2）
- 总纲10 动手者创造历史：KARL 把安全机制落实为每次开机的具体重构，由 Theo 与协助者在 hackathon 上动手实现，显示安全演进来自动手者的直接推进而非抽象原则。（BSD Now EP203，[4432.62-4690.58]，L2）

**辨析**：

- 转写中 OpenBSD 6.8 随机种子置信度标记被表述为“RB_GOODRANDOM”，其具体宏名与语义应以 OpenBSD 6.8 发布说明及源码为准。 [存疑脚注] 具体宏名待官方变更日志核对（BSD Now EP374，[397.32-447.44]，L4）
- 转写对‘软件 RAID 加密卷’等术语有拼写漂移（如‘software aid crypto volumes’），引用时须回查 OpenBSD 6.7 官方变更日志。 [存疑脚注] 转写术语拼写漂移（BSD Now EP351，[514.16-524.0]，L4）
- Rainbow Crack 网站自 2007 年后基本未更新，教程提及的某域名已被劫持为垃圾页，该工具的可用性与教程安全性存疑。 [考据脚注] 站点域名易主，链接与补丁来源需重新核实（BSD Now EP325，[2683.40-2706.96]，L4）
- 12.1 的 open ZFS 与原生加密支持为发布说明转述，具体实现路径与加密原语宜以 FreeBSD 源码树核对。 [存疑脚注] 转写对“首个支持 open ZFS 端口的正式版”表述较口语化（BSD Now EP325，[68.92-90.80]，L4）
- PDP-7 影片鉴定为“强烈支持而非确证”，Warner 本人承认对序列号 149 的排除仅属弱证据。 [存疑脚注] 三线证据均非决定性，结论保持开放（BSD Now EP322，[770.24-808.78]，L3）
- GhostBSD 路线为项目方单方声明，TrueOS 后续变动可能使其再调整，不宜作长期定论。 [考据脚注] 上游 TrueOS 路线变动风险未计入（BSD Now EP322，[1802.90-1822.78]，L4）

**文献**：

- [BSD Now EP374] Pennington J. BSD Now: 374: OpenBSD’s 25th anniversary[EB/OL]. (2020-10-29)[2026-08-15]. <https://www.bsdnow.tv/374>.
- [BSD Now EP351] Pennington J. BSD Now: 351: Heaven: OpenBSD 6.7[EB/OL]. (2020-05-21)[2026-08-15]. <https://www.bsdnow.tv/351>.
- [BSD Now EP325] Pennington J. BSD Now: 325: Cracking Rainbows[EB/OL]. (2019-11-21)[2026-08-15]. <https://www.bsdnow.tv/325>.
- [BSD Now EP322] Pennington J. BSD Now: 322: Happy Birthday, Unix[EB/OL]. (2019-10-31)[2026-08-15]. <https://www.bsdnow.tv/322>.
- [BSD Now EP203] Pennington J. BSD Now: 203: For the love of ZFS[EB/OL]. (2017-07-19)[2026-08-15]. <https://www.bsdnow.tv/203>.

<!-- /PODCAST_REVIEW -->

<!-- W172-YT-ROUTE:BEGIN 2026-10-15 YouTube 章节路由注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-272 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-272`；w172 YouTube 章节路由采纳）

据〔Never lose a Syslog Message 演讲〕讲者口述：讲者称开始改进 syslog 时只有 IPv4，如今 IPv4 与 IPv6 两侧都能承载 UDP、TCP 与 TLS。（YouTube EP8p6lnxClMak，[1498.26-1508.36]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-704 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-704`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者表示将来还会增加一项支持能力（转写音作 SSV SS SMP，讲者当场未展开缩写），服务于 secure nested paging 安全嵌套分页。（YouTube EPKpPY0wKSURM，[1180.16-1189.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-703 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-703`；w172 YouTube 章节路由采纳）

据〔来源不详〕讲者口述：讲者说他已经在做的事之一，是让 OpenBSD 作为客户机跑在 Linux KVM 宿主机上，并且这个配置可以启用 SMP。（YouTube EPKpPY0wKSURM，[3046.88-3055.75]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-1290 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-1290`；w172 YouTube 章节路由采纳）

据〔Developing Software in a Hostile Environment（Ted Unangst 讲）〕讲者口述：讲者（Ted Unangst）称他们的工作是在开放 BSD 内核里完成的。（YouTube EP_q8zzWHj15Q，[2451.5-2454.4]）引用时按 L1 纪律：以上为视频或播客转写存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- W172-YT-ROUTE:END -->

<!-- GAP-A-YT:BEGIN 2026-10-18 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2616 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2616`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔DCBSDCon 2009 Kurt Miller 报告〕讲者口述：PIE 即 position independent executable，把可执行文件本身编译成位置无关，再配合内核支持即可整体搬移，因而是一种地址空间随机化（ASLR）技术；讲者紧接称其为漏洞利用缓解特性。（YouTube EPSPMWH367u6I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2617 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2617`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔DCBSDCon 2009 Kurt Miller 报告〕讲者口述：OpenBSD 当时已有基于地址的布局随机化——内核随机加载运行时链接器，并把所链接的共享库加载到随机位置，使共享库每次执行都移动，从而挡住最常见的 return-to-libc 攻击（原文转写作 return to Li／return to LIC）。（YouTube EPSPMWH367u6I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2618 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2618`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔DCBSDCon 2009 Kurt Miller 报告〕讲者口述：PIE 工作在上一个版本之前就已启动，OpenBSD 4.5 将让所有动态程序都能使用 PIE，但当时还不会默认开启，最终目标是默认启用。（YouTube EPSPMWH367u6I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2619 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2619`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔DCBSDCon 2009 Kurt Miller 报告〕讲者口述：PIE 并非对所有场景都有效，以 Apache 1.3 为例，守护进程 fork 出的子进程是初始程序的精确副本，随机化只对初始进程生效，攻击者可反复暴力猜测地址。（YouTube EPSPMWH367u6I，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
