---
chapter: 第 306 章
id: CH306
volume: 16
---

# 第306章 freebsd社区演进史-治理结构

## 要点

- FreeBSD 项目 1994-1995 年起使用 majordomo 邮件列表软件，freebsd-hackers、freebsd-current、freebsd-questions 等列表在 1990 年代通过 hub.freebsd.org 分发，后迁移至 mailman
- FreeBSD 治理结构从 1993 年创始人小组到 2000 年首次 Core Team 直选，再到 2000 年 Foundation 成立形成“Core Team 共识 + Foundation 商业托管”双轨治理
- FreeBSD 邮件列表既是技术讨论场所也是治理决策的非正式平台，与 Linux LKML 的高流量补丁讨论模式形成对比
- FreeBSD 邮件列表存档由 freebsd.org 官方与 The Mail Archive、Weren't archive 等第三方备份，部分早期邮件已遗失
- Jordan Hubbard 2001 年 6 月 25 日宣布加入 Apple 担任 BSD Technologies Manager（Darwin 邮件列表公告），2002 年 5 月 1 日正式从 FreeBSD Core Team 辞职，辞职信提到 Core Team 凝聚力下降与“痛苦的经历”

## 史观

- 总纲第 8 条——物理空间影响技术，邮件列表架构塑造了 FreeBSD 的去中心化协作模式
  - 辨析：FreeBSD 邮件列表从 majordomo 迁移至 mailman 的具体时间需查 freebsd-hackers archive；hub.freebsd.org 的硬件配置历史需考据
  - 文献：FreeBSD List Archives 1995-2000；majordomo doc
- 总纲第 23 条——社区治理形式主义化的渐进过程；统计结论印证：统计结论 [C-24] FreeBSD freebsd-src 仓库贡献者 Gini 系数 0.9188（Bootstrap 95% CI [0.9093, 0.9270]）、统计结论 [C-25] DragonFly BSD dragonfly-src Gini 0.8972（[0.8517, 0.9187]）、统计结论 [C-26
- 总纲第 25 条——延续与终结，关键人物离场
- 辨析：【双库核查 2026-08-15】邮件列表库 freebsd-hackers 2000-2002 年查询 'Jordan Hubbard' 命中 5 条（Jordan Hubbard 本人 2000 年活跃参与），参考文献库 'Jordan Hubbard' 命中 5 条（lisa08、bsdcan 2015/2016、coscup 2019
- 总纲第 23 条——社区治理的共识模式效率局限
  - 辨析：Rice 演讲的具体原文需查 AsiaBSDCon proceedings；2008 年前讨论的具体提案需考据
  - 文献：Benno Rice 2018 AsiaBSDCon"A Tale of Two Repositories"；LWN 2018 FreeBSD coverage[考据完成：2026-07-28 经穷尽联网考据，上
- 总纲第 15 条——社会运动影响社区治理
  - 辨析：【双库核查 2026-08-15】邮件列表库 freebsd 查询 'Gamergate Randi Harper' 命中 4 条——关键一手证据：Randi Harper（<randi@freebsdgirl.com>）2015 年发出 'Concerning our new Code of Conduct...' 邮件，为 Gamergate

## 辨析

- FreeBSD 邮件列表从 majordomo 迁移至 mailman 的具体时间需查 freebsd-hackers archive；hub.freebsd.org 的硬件配置历史需考据
  - 文献：FreeBSD List Archives 1995-2000；majordomo documentation[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分
- 【双库核查 2026-08-15】邮件列表库 freebsd-announce 1999-2001 年查询 'FreeBSD Foundation' 命中 3 条（含 1999 年垃圾邮件干扰），参考文献库 'FreeBSD Foundation' 命中 5 条（Handbook、UNIX 传奇）——双库间接验证；2000-03-19 精确日期需 IRS Determination Letter
- 【双库核查 2026-08-15】邮件列表库 freebsd-hackers 2000-2002 年查询 'Jordan Hubbard' 命中 5 条（Jordan Hubbard 本人 2000 年活跃参与），参考文献库 'Jordan Hubbard' 命中 5 条（lisa08、bsdcan 2015/2016、coscup 2019）——双库验证 Jordan Hubbard 活跃存在；
- Rice 演讲的具体原文需查 AsiaBSDCon proceedings；2008 年前讨论的具体提案需考据
  - 文献：Benno Rice 2018 AsiaBSDCon"A Tale of Two Repositories"；LWN 2018 FreeBSD coverage[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费
- 【双库核查 2026-08-15】邮件列表库 freebsd 查询 'Gamergate Randi Harper' 命中 4 条——关键一手证据：Randi Harper（<randi@freebsdgirl.com>）2015 年发出 'Concerning our new Code of Conduct...' 邮件，为 Gamergate 事件在 FreeBSD 社区的直接一手证据；参考文献库

## 文献

- FreeBSD List Archives 1995-2000；majordomo documentation[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 306.1.2 治理结构演变历程

- 要点：FreeBSD 治理结构从 1993 年创始人小组到 2000 年首次 Core Team 直选，再到 2000 年 Foundation 成立形成“Core Team 共识 + Foundation 商业托管”双轨治理
- FreeBSD Core Team Election Rules 2000；FreeBSD Foundation 2000 Annual Report ［A］；freebsd.db 查询 L1.2.1（每年新增贡献者数演化，1993-2026，38 行结果）、L1.2.2（每年活跃贡献者数演化，1993-2026，34 行结果），见 `原材料/研究/bsd仓库分析/数据分析/宏观趋势统计.md` §L1.2.1、§L1.2.2

## 306.1.3 邮件列表与治理模式辨析

- 要点：FreeBSD 邮件列表既是技术讨论场所也是治理决策的非正式平台，与 Linux LKML 的高流量补丁讨论
- Hubbard 2001-06-25 Apple Announcement；Hubbard 2002-05-01 Resignation Letter；Linux.com 2002 Jordan Hubbard Resigns[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 306.10.2 离开对社区凝聚力的效应

- 要点：Hubbard 离开削弱 FreeBSD 早期创始团队的凝聚力，象征“创始时代”终结
- 史料：freebsd-hackers 2001-20
- Benno Rice 2018 AsiaBSDCon"A Tale of Two Repositories"；LWN 2018 FreeBSD coverage[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 306.11.2 CVS 到 SVN 到 Git 迁移迟缓

- 要点：FreeBSD 1993-2008 年使用 CVS，2008-2020 年使用 SVN，2020 年迁移至 Git，相比 Linux（2002 即采用 BitKeeper 后转 Git）迟缓约
- Core Team 2015 Statement；ARS Technica FreeBSD Gamergate coverage ［A］

## 306.12.2 Randi Harper 贡献与离开过程

- 要点：Randi Harper（freebsdgirl）作为 FreeBSD committer 与 Gamergate 反骚扰倡导者，因社区反应态度最终离开 FreeBSD 项目
- 史料：Harper 个人博客与 Twitter、freebsd-hackers 关于 Harper 离开的讨论 ［A］
- 史观：总纲第 25 条——延续与终结，关键人物离场
- 辨析：Ha
- FreeBSD CI Documentation；BSDCan 2017 CI talks[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 306.13.2 2017 年后测试建设过程

- 要点：2017 年后 FreeBSD 引入 Jenkins CI、kyua 测试框架、GitHub Actions 等逐步建立测试基础设施
- 史料：FreeBSD src/tests/ 目录 commit log、freebsd-testing 邮件列表、Jenkins CI
- FreeBSD Core Team Election Rules；Core Team Roster 历史 ［A］

## 306.2.2 历届选举争议与演变

- 要点：Core Team 选举 2000-2024 年共举行 10+ 届，2020 年选举因 CoC 争议 voter turnout 下降，2022 年选举引入电子投票系统
- 史料：freebsd-hackers 与 freebsd-core 邮件列表选举讨论、Core Team 选举结果公告；2022 年 Core.12 选举结果公告（FreeBSD Core Team Secretary 2022-06-18 发布，fr
- FreeBSD Committer's Guide；FreeBSD src/ repository ACL ［A］

## 306.3.2 文档贡献者与 committer 关系演变

- 要点：FreeBSD Documentation Engineering Team 与代码 committer 关系复杂，文档贡献者需通过文档 committer 审查提交，存在“二等公民”感受
- 史料：freebsd-doc 邮件列表、Documentation Engineering Team 章程 ［A］
- 史观：总纲第 10 条——边缘者贡献塑造社区知识结构
- 辨析：文档 comm

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP373、BSD Now EP360、BSD Now EP354、BSD Now EP278、BSD Now EP145、BSD Now EP579（共 6 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 访谈对象 Kyle Evans 因课程同学使用 FreeBSD 而入坑，从 bsdgrep 的 GSoC 项目开始参与 FreeBSD 开发，后当选 Core 团队成员。（BSD Now EP373，[163.48-233.53]，L1）
- bsdgrep 源自 2011 年前后的 GSoC 项目，旨在替换 base 中的 GNU grep；其难点在于需保持与 GNU 扩展及既有脚本依赖的 bug 兼容。（BSD Now EP373，[216.33-426.70]，L1）
- flua 是 base 中专用的 Lua 解释器，避免与 ports 中的 Lua 冲突；引导装载器由 Forth 转 Lua 后，boot 环境菜单等逻辑更易维护。（BSD Now EP373，[517.11-657.27]，L1）
- bectl 源自 GSoC 项目，用于管理 ZFS 引导环境；ZFS Boot CFG 进入上游 OpenZFS 后成为一等特性，可在 UEFI 下工作。（BSD Now EP373，[828.43-1009.87]，L1）
- certctl 将 Mozilla 根证书束纳入 base，使 FreeBSD 12.2 的新装系统默认具备 SSL 信任库，并可增删或拉黑证书。（BSD Now EP373，[1208.75-1317.09]，L1）
- 追查坏提交的文章介绍用 git bisect 二分定位引入回归的提交，并指出破坏可能来自非直观的依赖变更。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 完成 2020 年第十一届 Core 团队选举，Baptiste Daroussin、Ed Maste、George Neville-Neil、Hiroki Sato、Kyle Evans、Mark Johnston、Scott Long、Sean Chittenden、Warner Losh 当选。（BSD Now EP360，[460.69-614.65]，L2）
- NetBSD 在 Pinebook Pro 上以 NetBSD 9 用户态搭配 Current 内核运行，以兼顾二进制包与更好的硬件支持。（BSD Now EP360，[624.57-842.58]，L2）
- pf 状态表存在默认大小限制，FreeBSD 另有 `net.pf.request_maxcount` sysctl 控制单次 ioctl 载入表项数；DragonFly 侧限制为静态内核值。（BSD Now EP360，[1199.40-1404.41]，L2）
- FreeBSD 11.4 进入 RC2，camcontrol、freebsd-update、ZFS 书签重命名、certctl 等更新随 11.4 与 12.2 推出。（BSD Now EP354，[66.04-186.90]，L2）
- Jim Salter 的 Ars Technica 文章以 1.9TB 虚拟机镜像为例比较 ZFS 复制与 rsync：ZFS 靠块出生时间与快照可在 8 秒内完成，而 rsync 需约 2.5 小时。（BSD Now EP354，[474.62-667.52]，L2）
- Colin Percival 自 2008 年起主导 FreeBSD 移植至 Amazon EC2，并持续维护至今。（BSD Now EP354，[674.30-747.26]，L2）
- FreeBSD 项目发起 2020 年社区调查，以量化数据引导项目优先事项与努力方向。（BSD Now EP354，[756.54-846.94]，L2）
- McKusick 亲述伯克利早期四张桌四人同处一室、与 Bill Joy 为办公室同僚，办公室仅一部电话且十之八九是找 Bill Joy；他形容 Bill Joy 更像营销者，四处演讲、散发磁带、动员他人贡献。（BSD Now EP278，[176.66-198.66]，L1）
- McKusick 认为 FreeBSD 二十五年来最大的成就是形成一套能持续吸纳新人并让其上升的治理机制：文档 committer 与源码 committer 同样有权选举 core，营销背景者也能当选。（BSD Now EP278，[533.12-611.68]，L1）
- McKusick 援引 MIT 与法国南部高校的社会学研究，称多数开源项目约五年内沉寂，只有 Apache 与 FreeBSD 等项目完成三次以上成功的领导层更替，FreeBSD 已历约五代。（BSD Now EP278，[725.94-848.56]，L1）
- McKusick 亲述 FreeBSD 基金会起源：早期发行由 Walnut Creek CD-ROM 支撑，后依赖 Yahoo 提供基础设施十余年，Justin Gibbs 因担忧单一公司退出而发起基金会。（BSD Now EP278，[1883.72-1965.34]，L1）
- McKusick 亲述 UFS 三十年：其保存的 1982 年磁盘镜像在当代仍可读写，UFS 适合资源受限的嵌入式设备，ZFS 适合大资源环境，二者各解决不同问题。（BSD Now EP278，[1093.34-1174.26]，L1）
- McKusick 判断容器概念发明于 FreeBSD 却在他处获得成功，FreeBSD 常把项目推进到九成而缺最后一成产品化，恰如“先驱挨箭、定居者得地”。（BSD Now EP278，[2596.78-2625.54]，L1）
- Benno Rice（EMC Isilon 的 OS 与网络经理）竞选 FreeBSD Core Team，主张改进社区治理：引入并落实 Code of Conduct、修复非 committer 贡献路径、改善 Bugzilla 补丁响应。（BSD Now EP145，[448.00-676.00]，L1）
- Rice 指出 FreeBSD 测试自动化不足、新贡献者入门困难、Bugzilla 中补丁积压多年，并认为每一个被冷落的补丁都意味着失去一位潜在贡献者。（BSD Now EP145，[643.00-971.00]，L1）
- Rice 讨论 GitHub 与 Bugzilla/Fabricator 的取舍，认为 GitHub 是当下最低摩擦的贡献入口，但并非唯一解；项目目前“半上 GitHub”的状态造成补丁滞留。（BSD Now EP145，[1339.00-1524.00]，L1）
- Colin Percival 优化 FreeBSD 的 SHA-256/512 实现，在 2013-2015 年处理器上提速 20-25%，该工作由 Tarsnap 赞助；同期 OpenBSD 增加 ARMv7 引导加载器，ifconfig 新增 `-f` 输出格式。（BSD Now EP145，[2346.00-2480.00]，L2）
- pkgsrc 第 50 次发布访谈 Jörg Sonnenberger，强调跨平台一致包仓库的价值；另报道 Cavium ThunderX ARM 服务器发往 FreeBSD Foundation。（BSD Now EP145，[2481.00-2655.00]，L2）
- Stefano Marinelli 自述 2002 年因大学同学提及教授 Özal Babaoğlu 是伯克利原始 BSD 的创建者之一而开始研究 BSD，随后在笔记本电脑上安装 FreeBSD 并长期使用。（BSD Now EP579，[843.16-910.40]，L1）
- Stefano 创办 BSD Cafe：因 Fediverse 上缺少 BSD 爱好者的开放交流空间，创建实例后 24 小时内即吸引逾百名用户，后扩展出 Matrix 频道与 RSS 等服务，并推动意大利中小企业与医疗行业采用 BSD。（BSD Now EP579，[942.26-1072.78]，L1）
- Dave Cottlehuber 追述 FreeBSD core 团队史：早期 core 即所有持有源码提交权限者，后经诉讼尾声与治理需要而结构化，约二十年前基金会成立；近年 core 将源码提交权限的决策下放给新设的 source manager team。（BSD Now EP579，[1898.98-2186.62]，L1）
- Dave 说明 FreeBSD Core 13 的目标包括完成 source manager team 的设立、改善软件包仓库的 CDN 分发、加强与 Dell、Sony、Apple 等下游伙伴的协作，并推进由基金会资助的 CI 工作流。（BSD Now EP579，[2207.24-2461.08]，L1）
- Christos Margiolis 自述因 Linux 代码库过于庞大而选择 FreeBSD 作为贡献对象，从事声音子系统与音乐制作工具的维护与改进。（BSD Now EP579，[2721.16-2774.92]，L1）

**史料**：

- Kyle Evans 本人口述其参与 bsdgrep、flua、bectl、certctl 与 Core 团队的经过。（BSD Now EP373，[163.48-1933.73]，L1）
- 访谈提及 Warner Losh 引入 Lua 脚本、Alan Jude 作为 GSoC 导师等当事人协作细节。（BSD Now EP373，[522.88-867.89]，L1）
- 追查坏提交博文与 git bisect 说明。（BSD Now EP360，[65.19-460.69]，L2）
- FreeBSD 2020 年 Core 团队选举公告，由主持人转述当选名单。（BSD Now EP360，[460.69-614.65]，L2）
- Jim Salter 在 Ars Technica 的 OpenZFS 指南及 syncoid 工具说明。（BSD Now EP354，[474.62-597.86]，L2）
- 关于 Colin Percival 的播客访谈，介绍其 Tarsnap 创立、AWS 使用经验与 FreeBSD 安全官经历。（BSD Now EP354，[674.30-747.26]，L2）
- McKusick 提及 FAST 大会关于文件系统三十年演进的 keynote、BSDCan 2018 的采访背景，以及 CSRG 重写 AT&T 程序时 Keith Bostic 主张将署名归于他人以自保的细节。（BSD Now EP278，[339.18-390.46]，L1）
- McKusick 提及 TeachBSD 项目，主张以真实操作系统而非玩具系统教授计算机科学，并认为 DTrace/DWatch 等工具是“玻璃制”可观测系统的重要组成部分。（BSD Now EP278，[2723.00-2781.38]，L1）
- Benno Rice 的 Core Team 竞选主张与其在 Linux.conf.au 听到的 Rust 社区 Emily Dunham 演讲。（BSD Now EP145，[534.00-570.00]，L1）
- Colin Percival 的 SHA-256/512 优化 commit 与跨硬件基准数据，作为加密哈希性能演进的一手材料。（BSD Now EP145，[2350.00-2478.00]，L2）
- 本期为 EuroBSDcon 2024 现场采访，Stefano Marinelli、Dave Cottlehuber 与 Christos Margiolis 均为当事人自述；Özal Babaoğlu 的身份信息为 Stefano 转述的同学说法。（BSD Now EP579，[745.78-2774.92]，L1）

**史观**：

- 总纲10 动手者创造历史：Kyle 以“找让自己不舒服的问题”为切入点，从具体缺陷入手参与系统开发，体现动手者以具体工程推动项目。（BSD Now EP373，[1604.00-1770.17]，L1）
- 总纲9 经验优先：访谈强调通过实际项目学习并建立人际网络以获取经验，而非单纯阅读文档。（BSD Now EP373，[1639.55-1710.47]，L1）
- 总纲10 动手者创造历史：FreeBSD 决策由“到场者”作出，主持人与提问者强调社区参与决定项目走向。（BSD Now EP360，[2452.99-2456.55]，L2）
- 总纲4 分离聚合是永恒规律：Core 团队成员更替体现治理层的分离与再聚合。（BSD Now EP360，[460.69-614.65]，L2）
- 总纲9 经验优先：ZFS 复制对 rsync 的优势来自块级快照的实际经验，而非理论推断。（BSD Now EP354，[560.26-667.52]，L2）
- 总纲3 不存在进步，只有权力再分配：社区调查旨在重新分配开发优先级，体现技术方向由使用数据而非线性进步主导。（BSD Now EP354，[756.54-846.94]，L2）
- 总纲10 动手者创造历史：McKusick 强调软件与项目的持续“养护”远非社区驱动项目所长，人们倾向做新奇有趣之事；文档与基础设施的默默维护恰是系统得以存活的关键。（BSD Now EP278，[451.46-489.68]，L1）
- 总纲3 不存在进步，只有权力再分配：McKusick 指出历史上 IBM、微软各自占据过绝对支配地位又相继让位，Linux 今日的支配地位同样不会永远持续，FreeBSD 甘居雷达之下反而得以延续。（BSD Now EP278，[2247.34-2342.26]，L1）
- 总纲5 没有必然性，只有偶然性：McKusick 以“容器发明于 FreeBSD 却成功于他处”为例，指出技术领先与市场成功之间并无必然因果，成功更多依赖偶然的产品化时机。（BSD Now EP278，[2596.78-2625.54]，L1）
- 总纲7 理论必须自反：Rice 反思 FreeBSD“开源早于开源”带来的陈旧社区模型，主张挑战既有的贡献与治理假设。（BSD Now EP145，[575.00-595.00]，L1）
- 总纲8 本体论上各方平等：Rice 主张把非 committer 贡献者与文档、测试、运维者平等纳入社区，落实尊重与 Code of Conduct。（BSD Now EP145，[612.00-689.00]，L1）
- 总纲9 经验优先：Rice 从 Randy Harper 事件与 Python 社区经验中提炼治理改进，以既往经验反推未来制度。（BSD Now EP145，[482.00-569.00]，L1）
- 总纲10 动手者创造历史：Stefano 以运维者身份推动客户迁移 BSD 并创办社区服务，Dave 以志愿者身份参与治理，均体现动手者在社区运行中的基础作用。（BSD Now EP579，[942.26-1072.78]，L1）
- 总纲3 不存在进步，只有权力再分配：core 团队将源码提交权限决策下放给 source manager team 的过程，是 FreeBSD 治理权力在团队间的重新配置。（BSD Now EP579，[2081.44-2186.62]，L1）
- 总纲8 本体论上各方平等：Dave 强调 FreeBSD 与 OpenBSD、NetBSD、DragonFly BSD 乃至 Linux 社区之间存在持续的跨项目交流，各方在面对共同工程问题时彼此平等。（BSD Now EP579，[2560.00-2607.04]，L1）

**辨析**：

- bsdgrep 尚未完整支持 GNU 扩展，替换 base 中 GNU grep 的时机与兼容性范围仍待评估。　[存疑脚注] GNU 扩展兼容范围待核实（BSD Now EP373，[394.32-426.70]，L4）
- DragonFly 的 pf 表限制是静态内核值且未暴露为可调 sysctl，是否需要仿照 FreeBSD 改造仍待确认。　[存疑脚注] DragonFly 侧改造计划待核实（BSD Now EP360，[1360.80-1390.40]，L4）
- 转写中“8 秒对 2.5 小时、1150 倍”为作者特定场景的实测数据，主持人亦提示学术上此类极端比值需谨慎看待。　[存疑脚注] 极端比值需结合具体场景理解（BSD Now EP354，[615.14-641.14]，L4）
- McKusick 关于“文档 committer 与源码 committer 同等投票”的叙述属当事人视角，须与 FreeBSD 选举规则文件与历届 core 名单交叉核验；其对自己“不再关键”的自评也属谦辞。　[存疑脚注] 选举资格细节须以 FreeBSD Core Team 规则文件核实。（BSD Now EP278，[533.12-611.68]，L3）
- McKusick 提及的研究（MIT 与法国高校基于 commit log 分析领导层）未给出具体出处，其“只有 Apache 与 FreeBSD 等少数项目完成多次更替”的结论需核对原始研究。　[存疑脚注] 所援引研究未具名，结论无法直接追溯。（BSD Now EP278，[725.94-799.70]，L4）
- GitHub 是否应取代 Bugzilla/Fabricator 存在分歧：Rice 认为 GitHub 是最低摩擦路径但非唯一答案，需要社区就是否“全上 GitHub 或完全不用”作出决断。（BSD Now EP145，[1390.00-1524.00]，L1）
- Stefano 所称 Özal Babaoğlu 为“原始 BSD 的创建者之一”系同学转述，其具体贡献范围须以 CSRG 档案核实。　[存疑脚注] Babaoğlu 在伯克利 BSD 中的具体贡献与角色未经 CSRG 一手档案核实。（BSD Now EP579，[843.16-869.18]，L4）
- Dave 所述“早期 core 即全体源码 commit 持有者”为其个人追述，具体历史节点须以 FreeBSD 项目档案核实。　[存疑脚注] core 早期构成说法为个人追述，未经项目治理档案核实。（BSD Now EP579，[1898.98-1948.24]，L4）

**文献**：

- [BSD Now EP373] Pennington J. BSD Now: 373: Kyle Evans Interview[EB/OL]. (2020-10-22)[2026-08-15]. https://www.bsdnow.tv/373.
- [BSD Now EP360] Pennington J. BSD Now: 360: Full circle[EB/OL]. (2020-07-23)[2026-08-15]. https://www.bsdnow.tv/360.
- [BSD Now EP354] Pennington J. BSD Now: 354: ZFS safekeeps data[EB/OL]. (2020-06-11)[2026-08-15]. https://www.bsdnow.tv/354.
- [BSD Now EP278] Pennington J. BSD Now: Episode 278: The Real McCoy | BSD Now 278[EB/OL]. (2018-12-27)[2026-08-15]. https://www.bsdnow.tv/278.
- [BSD Now EP145] Pennington J. BSD Now: 145: At the Core of it all[EB/OL]. (2016-06-08)[2026-08-15]. https://www.bsdnow.tv/145.
- [BSD Now EP579] Pennington J. BSD Now: 579: EuroBSDcon 2024[EB/OL]. (2024-10-03)[2026-08-15]. https://www.bsdnow.tv/579.

<!-- /PODCAST_REVIEW -->
