---
chapter: 第 127 章
id: CH127
volume: 第06卷-freebsd的核心技术革新
---

# 第 127 章 FreeBSD 10.0 的发布与大整合开端

## 要点

- FreeBSD 提交高峰期出现在 2024 年（63750 次）；10.x 的大整合与 pkg 迁移时期则对应 2013-2014 年（10.0-RELEASE 于 2014 年 1 月 20 日发布）——两者分属不同时期，不得混为一谈。

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3699] 卷“第06卷-freebsd的核心技术革新”第 127 章，匹配置信度 folder，原因：folder 第125章

- [DB:code_repos:freebsd.duckdb] FreeBSD 提交高峰期：2024 年（63750 次）；10.x 大整合与 pkg 迁移期为 2013-2014 年，两时点须区分表述。

## 史观

- 总纲第 5 条——没有必然性，只有偶然性：FreeBSD 10.0 的大整合是多项技术路线偶然交汇的结果

## 辨析

- 10.0 支持周期（原计划至 2015.1.31）实际因后续 10.1/10.2 等版本发布而延长——单个 RELEASE 版本支持周期通常为至下一个次版本发布后一个月，stable/10 分支整体支持至 2018.10.31。
- bhyve 客户机多 vCPU（SMP）能力自 10.0 合入 base 即具备，实际可用性受 CPU 的 UG（Unrestricted Guest）硬件特性约束——原稿“SMP 客户机支持在 10.3 才加入”无官方公告依据　[存疑脚注] 多 vCPU 客户机的版本归属表述以 bhyve(8) 现行手册与 10.x/11.0 官方公告复核为准；bhyve 在 10.1 仍无 UEFI 固件支持——uefi-edk2-bhyve 端口在 10.x 后期才成熟。
- 原文件提到 “pkg 1.10.1 升级后整个 pkg 环境无法使用、从 1.x 升级到 2.10 时大量包被意外安装、jail 环境中 pkg 命令陷入无限循环”——这些问题发生在 pkg 1.x 早期版本（约 2014-2015 年），属迁移期真实问题但多数在 10.2 时期已修复；pkg 2.x 系列实际是在更晚版本中出现，10.x 携带的是 pkg 1.x 系列。
- 10.3 中 Hyper-V 集成持续改进但 Azure 镜像在 10.3 Announcement 中仍链接 VMDepot 而非 Azure Marketplace——FreeBSD 10.3 镜像于 2016 年 6 月 8 日宣布上架 Azure Marketplace（早于 10.4-RELEASE）。
- 不应将 10.x 神化为 “最好的 FreeBSD 版本”——10.0-10.2 时期存在大量迁移期 bug，10.3/10.4 才趋于稳定；但 10.x 时期完成的基础架构转型规模与深度在 FreeBSD 历史上前所未有，其工程价值在后续版本中得到充分体现。

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 **freebsd.duckdb**

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP21、BSD Now EP19、BSD Now EP9、BSD Now EP2（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 10.0 于 2014 年 1 月发布，此前经历 Alpha、Beta 与多个 RC；主持人强调 10.0 经过大量测试，以降低“.0 版本”的历史风险。（BSD Now EP21，[5624.00-5655.20]，L2）
- 采访 FreeBSD 安全官 Colin Percival：SSH 私钥加密由基于 MD5 的 crypt 改为 bcrypt 作为密钥派生函数，显著提高抵御暴力破解的难度；iSCSI target 在 10.0 中被认为可用于生产。（BSD Now EP21，[531.18-545.14]，L1）
- m0n0wall 1.81 发布，为面向嵌入式设备的 BSD 防火墙发行版；pfSense 于 2004 年自 m0n0wall 分叉，面向普通 PC 且开发更活跃。（BSD Now EP21，[4455.30-4530.00]，L2）[订正：原 [4458.98-4516.38]，2026-09-30 SenseAudio 重转核对]
- NTPD 被发现可利用欺骗 UDP 包返回放大响应而充当 DDoS 放大器，FreeBSD 与 pfSense 均通过安全公告与配置更新进行缓解。（BSD Now EP21，[4540.34-4636.46]，L2）
- PC-BSD 10.0 随 FreeBSD 10 发布，RC4 支持 Wine 与 9.2 升级保留 PBI；因 FreeBSD 10 的 ABI 变化，升级需重建或重装全部包。（BSD Now EP21，[4751.26-4801.10]，L2）
- 本期以 installfest 形式逐项演示 FreeBSD 10.0、OpenBSD 5.4、NetBSD 6.1.2、DragonFly BSD 3.6 与 PC-BSD 10.0 的安装流程，比较文本式、引导式与图形式安装器的交互差异。（BSD Now EP19，[1011.60-1046.72]，L2）
- FreeBSD 10 安装器新增键位测试、自动 root-on-ZFS、GELI 磁盘加密与 shell 安装模式，改进主要由 Devin Teske 与 Warren Block 等完成。（BSD Now EP19，[1069.32-1330.48]，L2）
- OpenBSD 在 5.4 前后提交 signify，用于签名基础发行集与第三方包，以解决此前 SHA256 校验在 X 集同步时因多机多时构建而出现的时序错配。（BSD Now EP19，[321.52-347.64]，L2）
- PC-BSD 使用 pc-sysinstall 脚本化安装器，图形安装可保存配置用于批量部署；TrueOS 为无 GUI 的服务器版本，内置 PEFS 与 Life Preserver 等命令行组件。（BSD Now EP19，[2244.04-2352.08]，L2）
- NetBSD 社区发布 pkgsrc 2013Q4；FreeBSD 侧由 Julio Merino 自 NetBSD 带入 Kyua 测试框架并搭建持续测试基础设施，以替代旧 Tinderbox 思路。（BSD Now EP19，[91.48-144.40]，L2）
- OpenBSD 3.0 引入 PF 后，Henning Brauer 将运行 IPF 的防火墙机器迁移至 PF，并与 Daniel Hartmeier 共同调试初期崩溃问题；修复后同一批机器以约 10% 的 CPU 负载处理原先满载的流量。（BSD Now EP9，[1015.4-1088.7]，L1）
- Henning Brauer 因向 misc@openbsd 报告 PF 迁移效果而收到 Theo de Raadt 的 hackathon 邀请，2002 年参加后获得提交权限，此后约十一年主要工作在 PF 与网络栈。（BSD Now EP9，[1090.3-1119.2]，L1）
- 他回顾早期 PF 黑客倾向在 PF 内解决一切问题，后转向以整个网络栈为对象的处理方式；并先后参与 bgpd、ntpd 与校验和处理，新排队系统计划替代 ALTQ。（BSD Now EP9，[1138.7-1640.5]，L1）
- FreeBSD 发行工程团队在代码冻结后审批所有针对该分支的变更，目标是在已知良好状态上修复既有问题而非引入新特性，以降低升级回归风险。（BSD Now EP2，[2347.62-2437.94]，L1）
- Glen Barber 加入 FreeBSD 基金会后获得专职时间协调发布流程，并兼管集群管理团队与项目资源维护，使发布节奏不再完全依赖志愿者的时间。（BSD Now EP2，[4398.47-4558.76]，L1）
- FreeBSD 10-CURRENT 自 2013 年 9 月起不再默认构建 GCC，基础系统改以 Clang 为默认编译器；需要 GCC 的场景改由 ports 提供现代版本。（BSD Now EP2，[543.86-622.62]，L2）
- LDNS 与 Unbound 正被移植入 FreeBSD 基础系统，计划在 10.0 前移除 BIND；主持人预期此举可减少约三分之一的安全公告负担。（BSD Now EP2，[4075.30-4225.94]，L1）
- Poudriere 以 jail 隔离并发构建二进制包，可在一台机器上按 FreeBSD 版本与架构分 jail 编译，并以增量重建与摘要签名支撑自有 pkg 仓库分发。（BSD Now EP2，[865.40-904.68]，L2）
- 该期头条报道 OpenBSD 已实现 64 位 time_t，以避免 2038 年 32 位时间戳溢出；该改动使 32 位平台也能跨越 Y2038 时间曲线。（BSD Now EP2，[71.70-150.60]，L2）

**史料**：

- 本期史料包括 Colin Percival 访谈（当事人自述）、FreeBSD 10.0 发布与安全公告、m0n0wall 1.81 与 pfSense 谱系记录及 RUBSD 会议录像。（BSD Now EP21，[531.18-545.14]，L1）
- 本期史料包括 Devin Teske 与 Warren Block 的安装器改动、OpenBSD signify 提交与测试密钥、Julio Merino 的 Kyua 测试框架、pc-sysinstall 脚本化安装器及 pkgsrc 2013Q4 分支。（BSD Now EP19，[91.48-1330.48]，L2）
- 当事人自述因 Linux 服务器受攻击而转向 BSD，OpenBSD 光盘先于 FreeBSD 光盘寄达从而成为其入门版本；早期 PF 初版由 Daniel Hartmeier 完成，bgpd 与 Claudio Jeker 合作约三个月做出可用版本，imsg 进程间通信框架成为其后多数 OpenBSD 守护进程的基础。（BSD Now EP9，[924.1-1365.8]，L1）
- 当事人 Glen Barber 自述约 2007 年以爱好者身份接触 FreeBSD，2010 年获 commit bit，先后加入文档工程、集群管理与发行工程团队；其参与发行工程的起点是为解决快照缺失问题。（BSD Now EP2，[2101.06-2165.46]，L1）
- 该期提及 OpenBSD 通过预售与销售 CD 套装筹集开发资金，并随每次发布推出歌曲与包装设计。（BSD Now EP2，[480.02-515.68]，L2）

**史观**：

- 总纲22 知识注定过时：SSH 旧密钥派生函数因安全进展被 bcrypt 取代，既有加密方法随攻防演进而过时。（BSD Now EP21，[531.18-545.14]，L1）
- 总纲10 动手者创造历史：Colin Percival 等安全工程师以具体维护与发布工作维持 FreeBSD 的安全响应体系。（BSD Now EP21，[5585.30-5655.60]，L1）[订正：原 [5597.60-5655.20]，2026-09-30 SenseAudio 重转核对]
- 总纲3 不存在进步，只有权力再分配：安全机制的替换体现攻防双方能力的再分配，而非简单的线性安全进步。（BSD Now EP21，[4540.34-4636.46]，L2）
- 总纲10 动手者创造历史：Devin Teske、Warren Block、Julio Merino 等以具体工程改进安装器与测试基础设施，推动发行流程演进。（BSD Now EP19，[1071.50-1290.20]，L2）[订正：原 [1069.32-1300.48]，2026-09-30 SenseAudio 重转核对]
- 总纲22 知识注定过时：sysinstall 被 bsdconfig 与脚本化安装器取代，旧安装方式随版本演进而淘汰。（BSD Now EP19，[2238.16-2399.96]，L2）
- 总纲8 本体论上各方平等：installfest 将五大 BSD 并置演示，体现多分支在本体论上平等对待的叙述方式。（BSD Now EP19，[1011.60-1046.72]，L2）
- 总纲5 没有必然性，只有偶然性：Henning Brauer 的入门路径由一次服务器受攻击后的偶然选择与一张先寄到的光盘共同决定，而非预先规划。（BSD Now EP9，[924.1-1003.4]，L1）
- 总纲10 动手者创造历史：他从 ISP 运维者转为直接修补 PF、编写 bgpd 与网络栈，以具体动手推动 OpenBSD 演进。（BSD Now EP9，[1005.4-1356.0]，L1）
- 总纲9 经验优先：发行工程对稳定分支宁可关闭新特性也不愿引入回归，体现以既有用户升级经验为优先的保守取向，而非功能扩张优先的进步叙事。（BSD Now EP2，[3189.04-3237.52]，L1）
- 总纲13 法律与道德是利益分配：GCC 退出基础系统与 BIND 替换是许可证与维护成本共同驱动的工具替换，属利益与负担在工具链层面的重新分配。（BSD Now EP2，[543.86-645.78]，L2）
- 总纲4 分离聚合是永恒规律：Poudriere 以 jail 将单一构建任务分离为按版本、架构与选项隔离的并发构建，并以增量重建聚合为统一二进制仓库，是分离与聚合的工程实践。（BSD Now EP2，[865.40-1801.56]，L2）

**辨析**：

- bcrypt 较 MD5 安全五亿倍为主持人粗略换算，需以密码学文献为准；m0n0wall 与 pfSense 的分叉年份及 iSCSI target 的生产就绪判断均为访谈与主持人口径。　[存疑脚注] 分叉年份与安全倍数表述需以项目发布记录和密码学原始文献复核。（BSD Now EP21，[536.90-552.02]，L4）
- OpenBSD 5.4 时期 signify 仍为测试密钥，正式签名需待 5.5；各 BSD 安装器细节为主持人实操演示，与官方手册的一致性需逐项复核。　[存疑脚注] 安装器细节与 signify 状态以官方发布说明为准，需交叉验证。（BSD Now EP19，[321.52-347.64]，L4）
- 转写对当事人姓名的识别：新转写将 Henning Brauer 一致写作正确原名，Daniel Hartmeier 仍被误写作 Daniel Hakmaier；引用时以英文原名 Henning Brauer、Daniel Hartmeier、Claudio Jeker、Theo de Raadt 为准，不自行音译。（BSD Now EP9，[892.0-1882.7]，L2）[订正：原 Henning Brauer 被写作多种变体且 [888.4-1895.7]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 10.0 是否彻底移除 BIND、以及 resolv.conf 与 DHCP 切换的具体方案在本期仍属进行中的计划，须以 10.0 最终发布说明为准。　[存疑脚注] BIND 移除与解析配置迁移为当时未定稿规划，播客转述不等同于正式发布决策。（BSD Now EP2，[4181.74-4227.38]，L4）

**文献**：

- [BSD Now EP21] Pennington J. BSD Now: 21: Tendresse for Ten[EB/OL]. (2014-01-22)[2026-08-15]. <https://www.bsdnow.tv/21>.
- [BSD Now EP19] Pennington J. BSD Now: 19: The Installfest[EB/OL]. (2014-01-08)[2026-08-15]. <https://www.bsdnow.tv/19>.
- [BSD Now EP9] Pennington J. BSD Now: 9: CURRENT Events[EB/OL]. (2013-10-30)[2026-08-15]. <https://www.bsdnow.tv/9>.
- [BSD Now EP2] Pennington J. BSD Now: 2: Engineering and Powder Kegs[EB/OL]. (2013-09-11)[2026-08-15]. <https://www.bsdnow.tv/2>.

<!-- /PODCAST_REVIEW -->
