---
chapter: 第 197 章
id: CH197
volume: 第10卷-openbsd的历史
---

# 第 197 章 openbsd-5x的发布周期文化

## 要点

- OpenBSD 提交高峰期：2015年(22014次)，对应 5.x 发布周期文化确立期

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4013] 卷“第10卷-openbsd的历史”第 197 章，匹配置信度 1.0，原因：任务4 衍生组官方文档采集

- [DB:code_repos:openbsd.duckdb] OpenBSD 提交高峰期：2015年(22014次)，对应 5.x 发布周期文化确立期

## 史观

- 循环而非进步：OpenBSD 5.x 的发布周期文化不是进步，而是对'稳定发布'这一承诺的循环性履行

## 辨析

- Release Notes 的完整性以 plus.html 页面为准——该页面仅记录“重要的和用户可见的变更”，部分内部代码重构（如 guenther 的 NOLOCK 标记）可能未在 Release Notes 中记录但可在 commit log 中定位；OpenBSD 仓库无 release tag（OpenBSD 使用 CVS 而非 git tag 标记 release），故 release
- de Raadt 发言的语义以 marc.info 存档原始帖子为准——部分帖子被社区解读为“粗暴”，但原始语境中多为技术论证；邮件列表档案的完整性以 marc.info 与 OpenBSD 官方存档为准——早期档案（1995-2000）可能存在缺失 [考据完成：2026-07-28 OpenBSD 邮件列表 1995-2000 年存档的完整性未经验证，marc.info 的 openbsd-mi
- 邮件列表档案的完整性以 marc.info 存档为准——部分权限撤销讨论可能在私有列表进行，公开档案无法覆盖全部讨论；个别权限撤销事件的具体细节以多源交叉验证为准——邮件列表、hackathons 记录、contributors 表三者交叉
- 批评的具体语境以原始邮件列表帖子为准——OSNews、Slashdot 等技术媒体的报道常简化邮件列表讨论的完整语境；de Raadt 回应的语义以 marc.info 存档原始帖子为准——部分回应被解读为“粗暴”但在原始语境中多为技术论证
- commit 记录的归属以 bsd_commits.db openbsd-src 仓库 commits 表 author_name 与 commit_files 表 file_path 交叉验证为准——部分 patch 由多人协作但仅一人 commit，commit_files 表可定位实际代码变更者；邮件列表档案的完整性以 marc.info 存档为准

## 文献

- [DB:references_fulltext] 参考文献全文数据库（4077 篇全文，27138 条时间线事件）—— 对应 openbsd.duckdb

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP166、BSD Now EP53、BSD Now EP52、BSD Now EP32、BSD Now EP18、BSD Now EP10（共 6 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 管道概念由 Doug McIlroy 在 Unix 早期提出，1969 年 Ritchie、Thompson 等人围绕文件系统设想时已在黑板讨论，但因当时被认为缺乏想象力而搁置，直到 1972 年才实际实现。（BSD Now EP166，[233.7-308.86]，L2）
- McIlroy 将管道与过滤器描述为连接程序与数据、消解组合程序时“意外困难”的概念结构，使可互相调用的程序在实践上能够真正连接。（BSD Now EP166，[398.14-414.98]，L2）
- NCC Group 以 AFL 加 QEMU 组成 TriforceAFL，并借助 flashrd 生成的 OpenBSD 系统对系统调用进行模糊测试，工具已开源，节目主持人提出可将同类方法转向 FreeBSD 系统调用。（BSD Now EP166，[122.62-224.46]，L2）
- Mark Schilder 的 FreeBSD MySQL 导入记录显示，通过关闭 sync_binlog、InnoDB flush log at commit 与 doublewrite，并将 ZFS sync 设为 disabled，导入速度从每分钟数十 MB 提升至数 GB。（BSD Now EP166，[566.72-824.56]，L2）
- MySQL 数据库在 ZFS 上宜将 record size 设为 16K 以匹配 InnoDB 页大小、减少写放大，并可设 redundant_metadata=most 与 logbias=throughput 降低元数据写与 ZIL 开销。（BSD Now EP166，[838.88-1004.52]，L2）
- OpenBSD VMM 的 vmctl 命令行与配置文件风格接近 bhyve 管理框架，配置可被 UCL 解析，但当时仅支持运行 OpenBSD 客户机，且只在 2016 年 10 月 22 日以后的最新 snapshot 中提供。（BSD Now EP166，[1128.68-1256.52]，L2）
- Adhoku 以 Ansible 和 FreeBSD Jails 复刻 Docker 式部署，每个应用创建独立 jail 并由宿主机 nginx 反向代理按域名分发，使单个 IP 可承载多站点，宣称无需 FreeBSD 专门知识。（BSD Now EP166，[1636.04-1775.64]，L2）
- FreeBSD Foundation 2016 年 10 月更新预告 developer summit 与 MeetBSD，并强调年末小额捐赠的数量关系到基金会维持公共慈善地位，而非仅依赖少数大额捐赠。（BSD Now EP166，[1259.92-1293.08]，L2）
- NetBSD 7.0.2 为小型安全更新，修复 mail.local 竞态、更新 OpenSSL 与 NTP/BIND，并修复 UFS1 外来文件系统、MIPS pmap 与 SPARC64 问题。（BSD Now EP166，[2064.56-2101.88]，L2）
- Matthew Dillon 修复 DragonFly 内核 MMC/SD 读写的 AB_RID 未清零导致的短读写，并将首次超时后的等待从 10 秒降为 1 秒，减少死端口引导延迟。（BSD Now EP166，[2108.32-2152.92]，L2）
- HAMMER 是 Matthew Dillon 为 DragonFly BSD 设计的 64 位文件系统，以事务组实现逐文件历史、快照、镜像流与删除后恢复。（BSD Now EP53，[3556.02-3609.18]，L2）
- HAMMER 的镜像流模式类似持续运行的 ZFS send，可不断向备份目标复制数据；其快照被视为可访问的实时数据而非只读副本。（BSD Now EP53，[3978.66-4095.18]，L2）
- Reyk Floeter 在卢布尔雅那 OpenBSD hackathon 当天以 relayd 源码为基础拆出基本可用的 httpd，随后在 Bob Beck 与 Theo de Raadt 推动下提交进树，十四天后达到可接受状态。（BSD Now EP53，[945.18-1035.58]，L1）
- OpenBSD httpd 默认运行于 chroot、采用特权分离与 pre-fork 模型，并吸收 LibreSSL 对私有内存分配器遮蔽安全机制的教训，保持代码基精简。（BSD Now EP53，[866.38-958.10]，L1）
- Sean Webb 与 Oliver Pinter 在 HardenedBSD 项目内推进 ASLR/PIE，并将其作为补丁提交上游 FreeBSD，目标是进入 11 版本。（BSD Now EP52，[1110.02-1421.06]，L1）
- ASLR 使程序可加载到任意内存地址，PIE 进一步支持应用级随机化，用于提高缓冲区溢出与信息泄露攻击的门槛；该实现默认关闭，需编译内核选项并可通过 sysctl 控制。（BSD Now EP52，[1110.02-1183.22]，L1）
- 该 ASLR 实现借鉴 PaX 与 NetBSD 的实现谱系，并在除 ARM 外的 FreeBSD 支持架构上工作，包括 32 位 Linux 兼容层。（BSD Now EP52，[1351.34-1501.26]，L1）
- OpenBSD 以 nginx 在基础系统中难以维护、且其自定义内存分配器遮蔽安全缓解机制为由，将其移出基础系统改由 ports 提供。（BSD Now EP52，[400.96-426.04]，L2）
- 自OpenBSD 5.5起，安装器支持autoinstall功能，可通过DHCP与PXE下载答案文件，使安装器按预设选项完成完全自动的无人值守安装。（BSD Now EP32，[1978.08-1988.48]，L2）
- 自动化安装流程需要配置DHCP的filename与next-server选项，经TFTP加载pxeboot与bsd.rd，再由OpenBSD内置的nginx提供安装集与install.conf答案文件。（BSD Now EP32，[2039.88-2285.80]，L2）
- install.conf中的答案变量对应安装器实际提示的问题，可预填主机名、密码、网络接口、用户、时区及HTTP安装集来源等参数。（BSD Now EP32，[2285.80-2347.94]，L2）
- 即使配置了autoinstall，系统仍要求用户选择进行自动安装，以避免误插网线导致空白机器被意外覆盖。（BSD Now EP32，[2545.76-2558.20]，L2）
- 当期问答指出Cisco的IronPort安全设备实际上以FreeBSD为基础，主持人认为其版本已较旧，显示FreeBSD在商用安全设备中的隐性基底。（BSD Now EP32，[3897.90-3907.06]，L2）
- 当期问答建议以zfs send与receive在本地管道中迁移FreeNAS的插件jail及其ZFS池，可逐位保留ZFS属性并可在转换中调整压缩等参数。（BSD Now EP32，[3987.06-4053.16]，L2）
- 主持人转述 Justin Sherrill 的观点：PF 已被 FreeBSD、NetBSD、macOS 等吸收，但各实现基于不同时期的 OpenBSD 版本且无版本号，导致规则语法与功能分化。（BSD Now EP18，[346.52-362.32]，L2）
- 节目讨论以 OpenSSH portable 或 OpenZFS 共同核心为参照，为 PF 建立可移植层（被称为 PPL 或 OpenPF 构想）；Henning Brauer 表示愿意协助，但该项目当时尚未落地。（BSD Now EP18，[454.58-557.28]，L2）
- Baptiste Daroussin 自述因厌倦反复源码编译而设计 PackageNG，后在 BSDCan 演讲并取得 ports commit bit，成为 portmgr 成员。（BSD Now EP18，[993.58-1029.66]，L1）
- PackageNG 方向为将 poudriere 由面向最终用户的安装工具转为基础设施构建工具，并引入 staging、autoplist、子包、flavors/providers 及基于 fingerprint 的仓库签名，以解决冲突、改名与多版本包问题。（BSD Now EP18，[1049.62-1253.12]，L1）
- OpenBSD 长期缺乏官方跨版本升级工具，第三方 ksh 脚本 OpenBSD Binary Upgrade 可完成 5.3 到 5.4 的二进制升级与旧文件清理，但仅校验 SHA256 而不提供签名。（BSD Now EP18，[2198.60-2266.36]，L2）
- Michael W. Lucas 自述 1995 年因所在国家主干网公司的 DNS 管理员离职而被指派接管，用 FreeBSD 2.0.x 替换老旧的 SunOS 与 Ultrix 服务器后稳定运行，由此进入 BSD 世界。（BSD Now EP10，[679.1-830.6]，L1）
- 他介绍 sudo 是分割 root 权限的访问控制工具，写作 Sudo Mastery 源于用户普遍误用 sudo，且大量教程推荐了可被突破权限限制的不安全配置。（BSD Now EP10，[956.9-1167.1]，L1）
- 他回顾 sudo 具备入侵检测能力，可按 SHA-256 等算法校验待执行文件的校验和，防止用户通过复制 shell 绕过限制，并主张采用白名单式授权而非黑名单式排除。（BSD Now EP10，[1491.9-1654.3]，L1）
- 新闻部分报道 OpenBSD 5.4 于 2013 年 11 月 1 日发布，并提及 DragonFly BSD 3.6 分支加入 SMP 改进、GCC 4.7 默认与 dports 成为默认。（BSD Now EP10，[85.1-96.2]，L2）

**史料**：

- Rhonda Hauben 撰写的 Unix 管道历史文章，引用 Doug McIlroy、Dennis Ritchie 与 Ken Thompson 的记述，主持人逐段转述。（BSD Now EP166，[233.7-422.96]，L2）
- NCC Group 开源的 TriforceAFL 与 flashrd 工具链（GitHub 仓库），用于 OpenBSD 系统调用模糊测试。（BSD Now EP166，[122.62-224.46]，L2）
- Mark Schilder 关于在 FreeBSD 上加速 MySQL 导入的博客文章，列出 InnoDB 与 ZFS 调优清单。（BSD Now EP166，[566.72-1010.56]，L2）
- Keith Burnett 的 OpenBSD 6.0 笔记本安装教程（ThinkPad X60 上配置 XFCE、doas 与 USB 挂载）。（BSD Now EP166，[1802.96-1947.44]，L2）
- Reyk Floeter 访谈（OpenBSD httpd 作者当事人自述）。（BSD Now EP53，[540.14-1854.84]，L1）
- Sean Webb（Laddera）访谈（ASLR/PIE 实现者当事人自述）。（BSD Now EP52，[933.90-2162.30]，L1）
- 当期教程演示了OpenBSD 5.5的autoinstall配置过程，包括DHCP、TFTP、pxeboot、bsd.rd、nginx与install.conf的完整步骤。（BSD Now EP32，[1978.08-2602.24]，L2）
- 当期问答提及Cisco IronPort设备以FreeBSD为基础，以及FreeNAS ZFS池迁移采用zfs send与receive的方法。（BSD Now EP32，[3897.90-4053.16]，L2）
- 本期史料包括 Justin Sherrill 博客观点、Henning Brauer 对 PF 可移植层的表态、Baptiste Daroussin 访谈（当事人自述）以及 OpenBSD Binary Upgrade 第三方脚本。（BSD Now EP18，[346.52-557.28]，L1）
- 当事人列出自著书籍：Absolute OpenBSD、Absolute FreeBSD、SSH、DNSSEC、Network Flow Analysis 与 Sudo Mastery；较大体量的书经 No Starch Press 出版，自出版书经 Tilted Windmill Press 发行。（BSD Now EP10，[1696.3-1835.4]，L1）

**史观**：

- 总纲5 没有必然性，只有偶然性：管道从 1969 年提议到 1972 年实现，其间经历了被质疑“缺乏想象”的搁置，具体技术路径由当时的人与偶然条件决定，而非线性必然。（BSD Now EP166，[233.7-308.86]，L3）
- 总纲9 经验优先：McIlroy 以“简单管线连接程序与数据”的经验表述总结工程实践，Unix 的哲学原则从具体动手经验中凝结而成。（BSD Now EP166，[398.14-414.98]，L3）
- 总纲1 一切真历史都是古代史：主持人感叹管道今日被当作理所当然，而忽略其曾有“没有管道的时代”，历史书写把建构产物自然化为恒常存在。（BSD Now EP166，[239.06-247.66]，L3）
- 总纲4 分离聚合是永恒规律：Adhoku 以 jail 做应用级分离、以反向代理做流量聚合，呈现分离与聚合的交替结构，而非单一集中或单一分散。（BSD Now EP166，[1636.04-1775.64]，L3）
- 总纲10 动手者创造历史：MySQL 与 ZFS 的优化均来自动手部署者的具体记录，性能改进由实际操作者而非抽象方案推动。（BSD Now EP166，[566.72-1010.56]，L3）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Reyk Floeter 以一天内动手拆出 httpd 并持续迭代的方式直接塑造 OpenBSD 基础系统工具。（BSD Now EP53，[945.18-1035.58]，L1）
- 总纲22 知识注定过时：总纲22 知识注定过时：OpenBSD 以更简单、更贴合自身安全模型的新工具替换日益膨胀的 nginx，体现既有技术方案的持续失效与重写。（BSD Now EP53，[837.46-945.18]，L1）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：httpd 自 relayd 分离、其协议改进又回流 relayd，展示 BSD 工程中持续的分离与聚合循环。（BSD Now EP53，[1169.46-1196.62]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Sean Webb 以动手实现并上游 ASLR/PIE 的方式直接改变 FreeBSD 安全能力。（BSD Now EP52，[1110.02-1421.06]，L1）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：ASLR 采用 PaX 模型而非 OpenBSD 模型，源于实现者个人偏好与 HardenedBSD 协作的偶然路径。（BSD Now EP52，[1381.32-1435.42]，L1）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：FreeBSD、OpenBSD 与 HardenedBSD 在 ASLR 实现上各有路径，被置于对等比较而非优劣判定。（BSD Now EP52，[1381.32-1449.58]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：autoinstall把重复的交互安装劳动转化为可复用的答案文件，体现了动手者对运维效率的持续改造。（BSD Now EP32，[2285.80-2347.94]，L3）
- 总纲3 不存在进步，只有权力再分配：总纲3 不存在进步，只有权力再分配：autoinstall并非单纯的技术先进，而是把安装决策权从现场交互重新分配给预先编写的配置与网络服务。（BSD Now EP32，[1983.08-1998.48]，L3）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：当期对Cisco IronPort FreeBSD基底的提及，把商业设备与开源系统置于同一技术谱系中考察，而非以品牌叙事先行。（BSD Now EP32，[3897.90-3907.06]，L3）
- 总纲4 分离聚合是永恒规律：总纲4 分离聚合是永恒规律：PF 随各 BSD 分支而分离，又出现以共同核心重新聚合的讨论，呈现分离与聚合的循环。（BSD Now EP18，[359.44-413.44]，L2）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：Baptiste Daroussin 因个人反复编译的痛点动手重写包系统，改变 FreeBSD 软件分发方式。（BSD Now EP18，[993.58-1029.66]，L1）
- 总纲18 时间是一种形式主义：总纲18 时间是一种形式主义：PF 缺乏版本号使各实现难以按时间锚定演进，说明版本命名是形式化的时间标记。（BSD Now EP18，[425.34-439.46]，L2）
- 总纲9 经验优先：Lucas 认为技术图书的价值在于说明知识如何与读者的实际工作相关，而非仅做信息堆砌，体现以经验与实用为重的取向。（BSD Now EP10，[1848.3-1998.2]，L1）
- 总纲10 动手者创造历史：他以自出版书籍收益赞助 BSDCan 等社区活动，把写作视为服务社区并推动社区建设的动手实践。（BSD Now EP10，[2143.1-2227.3]，L1）

**辨析**：

- [存疑脚注] 转写将管道历史中的参与者记作“Thompson and Kennedy”，疑为 Ritchie、Thompson 与 Rudd Canaday 的误转；管道提议与实现时间线须以 McIlroy 原文及 Unix 一手文献复核。　[存疑脚注] 人名与时间线须核验一手文献。（BSD Now EP166，[279.9-308.86]，L4）
- [存疑脚注] 转写将 Hauben 文章托管地记作“farther dot edu”，实际域名无法据此确认，引用时须核验文章来源。　[存疑脚注] 文章来源域名存疑。（BSD Now EP166，[417.88-422.96]，L4）
- HAMMER 在转录中被转写为多处以 ZFS 类比，其最大容量等参数属主持人转述，未能直接核对 DragonFly 官方文档。　[存疑脚注] HAMMER 技术参数为二手转述，未经官方手册交叉核验（BSD Now EP53，[3556.02-3609.18]，L4）
- Sean Webb 坦言上游化过程中存在私下邮件列表讨论与政治博弈，其本人一度无法参与辩护，具体争议内容未在本期披露。　[存疑脚注] 上游化受阻的具体技术或治理争议仅凭当事人单方叙述（BSD Now EP52，[1880.06-1929.90]，L4）
- 关于IronPort设备的FreeBSD版本已较旧的说法，主持人明确表示不十分确定，属于口头估计而非可核验的版本信息。　[存疑脚注] Cisco IronPort设备所采用的FreeBSD版本属主持人口头估计，需以设备文档或官方信息核实。（BSD Now EP32，[3903.66-3907.06]，L4）
- 主持人将 DragonFly 的 PF 对应 OpenBSD 4.4、FreeBSD 对应 4.5 等版本关系为口头转述，需与各项目代码核对；OpenPF 项目在 2014 年成立属对未来的期许而非既成事实。　[存疑脚注] 各 BSD 的 PF 版本对应与 OpenPF 立项状态需以源码与邮件列表原始记录复核。（BSD Now EP18，[386.32-439.46]，L4）

**文献**：

- [BSD Now EP166] Pennington J. BSD Now: 166: Pass that UNIX Pipe[EB/OL]. (2016-11-02)[2026-08-15]. https://www.bsdnow.tv/166.
- [BSD Now EP53] Pennington J. BSD Now: 53: It's HAMMER Time[EB/OL]. (2014-09-03)[2026-08-15]. https://www.bsdnow.tv/53.
- [BSD Now EP52] Pennington J. BSD Now: 52: Reverse Takeover[EB/OL]. (2014-08-27)[2026-08-15]. https://www.bsdnow.tv/52.
- [BSD Now EP32] Pennington J. BSD Now: 32: PXE Dust[EB/OL]. (2014-04-09)[2026-08-15]. https://www.bsdnow.tv/32.
- [BSD Now EP18] Pennington J. BSD Now: 18: Eclipsing Binaries[EB/OL]. (2014-01-01)[2026-08-15]. https://www.bsdnow.tv/18.
- [BSD Now EP10] Pennington J. BSD Now: 10: Year of the BSD Desktop[EB/OL]. (2013-11-06)[2026-08-15]. https://www.bsdnow.tv/10.

<!-- /PODCAST_REVIEW -->
