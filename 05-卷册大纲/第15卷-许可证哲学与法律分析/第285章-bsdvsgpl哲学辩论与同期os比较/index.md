---
chapter: 第 285 章
id: CH285
volume: 第15卷-许可证哲学与法律分析
---

# 第 285 章 bsdvsgpl哲学辩论与同期os比较

## 要点

- 许可哲学光谱：“义务自由（GPL）←→ 信任自由（BSD/宽松）←→ 闭源保护（Windows）”；BSD vs GPL 辩论的本质是“自由如何保障”的分歧，BSD 以信任、GPL 以约束，二者共同定义开源运动的哲学边界。
- Committer’s Big List of Rules 的沉默反映分层设计——治理程序处理“谁有权提交”，许可证哲学通过社区讨论与工程实践处理“提交什么”。BSD 化工程未通过修订 committer 规则实现，而是通过构建 BSD 许可证替代品逐步完成，证明规则的程序中立未阻碍许可证纯化，反而为工程替代争取了时间——若规则在早期强制禁绝 GPL 代码，FreeBSD 将因缺乏可用编译器而无法
- Committer’s Big List of Rules 争议映射出革命与改革的方法论分歧。革命路径主张直接修订规则——禁止 GPL 代码进入 base 系统、强制许可证审查、将 BSD 化写入治理章程；改革路径则在不修订规则的前提下，通过工程替代（Clang、LibreSSL、mandoc）逐步实现许可证纯化。FreeBSD 选择了改革路径，其困难远高于革命——须先构建功能对等的 BSD 替代
- 中文技术圈普遍以“病毒/传染”描述 GPL copyleft 机制，此隐喻**在法律意义上具有系统性误导**。词源可考：1990 年即出现 "General Public Virus"（GPV）贬称；2001 年 Microsoft 高管 Craig Mundie 称 GPL "viral aspect"，Steve Ballmer 更称 GPL 代码是 "a cancer that attach
- GPL 义务的触发条件是**分发（distribute，GPLv2）/传播（convey，GPLv3）**，而非“使用”或“修改”。中文圈“只要用了 GPL 代码就必须开源”的表述是核心误读之一。FSF GPL FAQ 明确：①**内部使用修改版不触发开源义务**——“GPL 不要求你发布修改版……你有自由修改并自用，而不必发布。这个规则也适用于机构（包括公司）”；②**运行修改版提供服务（Saa

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10483] BSD Now 第 665 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10547] BSD Now 第 654 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10584] BSD Now 第 646 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10645] BSD Now 第 637 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10778] BSD Now 第 617 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11152] BSD Now 第 571 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11215] BSD Now 第 563 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11366] BSD Now 第 546 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11444] BSD Now 第 536 期，匹配 CH285 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11544] BSD Now 第 526 期，匹配 CH285 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 辩论无终局——两种自由观各服务不同目标，BSD 的务实人文在光谱中独特定位。
- 【查证来源】FreeBSD Committer’s Guide 第 20 章经 docs.freebsd.org/en/articles/committers-guide/#rules WebFetch 一手核验目录条目存在；FreeBSD Core Bylaws 2000.8.28 版经 freebsd.org/internal/bylaws/ WebFetch 一手核验，规定 active c
- 【查证来源】项目史观总纲第 21 条原文经 据原文第 25 章 第 25 行 Read 一手核验：“革命与改革是历史方法论的分歧。Linux 靠革命，BSD 靠改革。改革的困难远高于革命。破山中贼易，破心中贼难”；BSD 化工程时间线经 135.8 节史料（OpenBSD LibreSSL 公告、FreeBSD LLVM 迁移文档、openbsd.db L3.6.1 查询报告）交叉核验；FreeB
- 【查证来源】GPLv2 §5 原文：“如果可识别的作品部分不是派生自本程序，且可合理视为独立的分离作品，则本许可证及其条款不适用于那些部分”（WebFetch gnu.org/licenses/old-licenses/gpl-2.0.txt 一手核验）；GPLv3 §5 聚合定义"aggregate"（WebFetch gnu.org/licenses/gpl-3.0.txt 一手核验）；Sta
- 【查证来源】FSF GPL FAQ 中文版（gnu.org/licenses/old-licenses/gpl-2.0-faq.zh-cn.html）WebFetch 一手核验上述问答原文；GPLv3 §0 “传播”（to convey）定义（gnu.org/licenses/gpl-3.0.txt）一手核验  【交叉验证方法】（1）FSF FAQ 内部一致性核验：修改版自用问答与 SaaS 问答

## 文献

- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］------## 史料登记与辩证校准（2026-08-08 追加）> **本卷命题**：24.2 劣币驱逐良币（详见本卷 00-总览“编纂指导思想叙事参照”）### 史料文献
- Committer’s Big List of Rules（docs.freebsd.org/en/articles/committers-guide/#rules）；FreeBSD Core Bylaws 2000.8.28 版（freebsd.org/internal/bylaws/）；BSD 化 commit log；Core Team 选举记录（freebsd.org/administration/）［A］
- 项目史观总纲第 21 条（据原文第 25 章 第 25 行）；BSD 化工程时间线（详见 135.8 节）；FreeBSD Core Bylaws 2000.8.28 版第 9 条（freebsd.org/internal/bylaws/）［A］
- GPLv2/GPLv3 全文（gnu.org）；FSF GPL FAQ（gnu.org/licenses/gpl-faq.html）；Copyleft 词条（Wikimedia）；中文自媒体《开源许可证教程》（ref 2377，kaoju_unreliable 系列，被考据对象——仅作“个人观点”元引用，其史实断言须独立核验）## 284.13.2 传染触发条件的法律边界——“分发/传播”而非“使用”
- FSF GPL FAQ 中文版；GPLv2/GPLv3 全文；AGPL 文本［A］## 284.13.3 传染性边界：演绎作品 vs 聚合（aggregation）
- GPLv2/GPLv3 全文；FSF GPL FAQ；最高法（2021）最高法知民终51号判决；HBuilder 案判决；康达律师事务所开源协议分析文 ［A］## 284.13.4 GPL 的法律性质：许可条件（conditions）而非单纯合同承诺（covenants）
- Jacobsen v. Katzer（535 F.3d 1373, Fed. Cir. 2008）；Creative Commons 声明；Artifex v. Hancom（2017）；济宁网络科技案；广州知识产权法院典型案例；最高法（2021）最高法知民终51号 ［A］## 284.13.5 违约救济误读：从“最坏不过被起诉”到司法实践的多元救济
- 南京中院（2021）苏01民初3229号；FSF v. Cisco 记录；广州知识产权法院典型案例；济宁网络科技案（2021）；中文自媒体《开源许可证教程》（ref 2377，kaoju_unreliable 系列，被考据对象——其“GPL 病毒”与“法官只会判停止使用”断言已按判例逐条纠正，结论以 FSF 官方 + 判例原文为准）［A］## 284.13.6 中文圈 GPL 理解偏差总表（法律意义维度）| # | 中文圈常见表述 | 法律事实 | 偏差类型 ||---|---|---|---|| 1 | “GPL 是病毒，用了就传染” | 传染仅限演绎作品；聚合/独立程序豁免（GPLv2 §5/GPLv3 §5） | 隐喻误导 || 2 | “只要用了 GPL 代码就必须开源” | 义务触发条件是分发/传播，内部使用与 SaaS（GPLv2）不触发 | 触发条件误读 || 3 | “违反 GPL 只是违约，不构成侵权” | Jacobsen（2008）：许可条件是 copyright conditions，违反=侵权；中国广州案：合同性质+授权终止=侵权 | 法律性质误读 || 4 | “最坏情况就是被起诉、判停止使用” | 南京案 300 万惩罚性赔偿；济宁/广州案授权终止；FSF v. Cisco 合规导向 | 救济范围误读 || 5 | “GPL 是免费午餐/自由软件=免费” | GPL 允许商业收费（GPL FAQ：可销售拷贝赚钱）；"free" 指自由非价格 | 概念混淆（freedom vs gratis） || 6 | “GPL 软件不能商用” | GPL 明确允许商业使用/销售（FSF 商业例外策略） | 商用限制误读 || 7 | “GPLv3 与 GPLv2 区别不大” | v3 增加专利授权、反 Tivoization、与 Apache 2.0 兼容；Linux 内核固守 v2-only | 版本差异误读 || 8 | “违反 GPL 后权利人不享有著作权” | 最高法 51 号案：违反 GPL 与著作权独立——开发者基于独创贡献仍享有著作权（演绎作品保护） | 权利关联误读 |> 本表为法律意义维度的系统性梳理，供正文写作与编辑引用；每条均有判例/FSF 官方来源支撑（详见 284.13.1-284.13.5 各小节辨析字段）。---## 附录：判例一手原件清单（2026-08-04 依据“判例与法律文件一手原件入库规则”采集）> 全部一手原件已下载存档于 `04-现代研究文献/03-文献下载/01-判决书案例/`，并在 references_fulltext.db 入库（ref id），大纲概述以 `<!-- NEWREF:ID -->` 标记引用。案件总清单：`03-原始史料库/06-考据记录/20260804_gpl_cases_inventory.md`。| 案件 | 一手原件 | ref id | 本地存档 ||------|---------|--------|---------|| Jacobsen v. Katzer（CAFC 2008） | CAFC 判决书 PDF（535 F.3d 1373） | 2417 | `Jacobsen_v_Katzer/` || Jacobsen 上诉卷宗 | appellant/appellee brief、CC amicus brief（445KB）、oral argument order 等 10 份 | 2418 | `Jacobsen_v_Katzer/` || Artifex v. Hancom（N.D. Cal. 2017） | MSJ 裁定（govinfo 官方 PDF 491KB）、MTD 裁定（CMU 370KB）、Hancom 动议（archive.org 181KB） | 2423/2424/2425 | `Artifex_v_Hancom/` || FSF v. Cisco（S.D.N.Y. 2008） | 起诉状公告+背景说明（FSF 官方页，案号 08-CV-10764） | 2426/2427 | `FSF_v_Cisco/` || SCO v. Novell（10th Cir. 2011） | 上诉判决 PDF（62KB，确认 Novell 拥有 Unix 版权） | 2428 | `SCO_v_Novell/` || USL v. BSDi / USL v. UC（1993-1994） | 1993-03-03 判决、920420/920724 起诉状、**McKusick 法庭声明**（930119.mckusick.decl，证人证词一手）、1986 UC-AT&T 许可协议 | 2422 | `USL_v_BSDi_USL_v_UC/` || 最高法（2021）知民终51号（OpenWRT/GPLv2） | 判决书全文（官网 HTML 98KB + wikisource 149KB）；一审案号（2018）苏05民初845号 | 2419 | `最高法2021知民终51号_OpenWRT/` || 南京中院（2021）苏01民初3229号（GPL 抗辩） | **判决书全文（2022-09-19，华宇元典 2026-08-04 获取）**+“密切通信”传染规则+300 万惩罚性赔偿；汉坤律所技术+法律分析 | 2468/2420/2421 | `南京苏01民初3229号_GPL抗辩/` || 广州知产法院（2019）粤73知民初207号（GPLv3 合同性质） | 判决书全文（45K 字，2021-09-29） | 2429 | `广州粤73知民初207号_GPLv3罗盒/` || 深圳中院（2019）粤03民初3928号（罗盒 v. 风灵/腾讯） | 判决书全文（43K 字，2021-04-30） | 2430 | `深圳粤03民初3928号_GPLv3罗盒/` || 北京高院（2018）京民终471号（HBuilder 案二审） | **二审判决书全文（2019-11-06，知产宝 2026-08-04 获取）**——三插件独立文件夹无 GPL 协议不受约束；聚合体认定；改判 50 万 | 2476 | `北京HBuilder案_GPL第一案/` |**说明**：

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP335、BSD Now EP27、BSDTalk EP7、BSDTalk EP9（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Deb Goodkin 与 FreeBSD Foundation 在 Linux Conf AU 内组织首个 FreeBSD mini-conf，Ben Woods、Peter Grehan 等演讲者出席。（BSD Now EP335，[1272.54-1399.32]，L2）
- Hyperbola 联合创始人 Andre 解释弃 Linux 内核的原因：HDCP 等 DRM、GRSecurity 停止公开补丁、Rust 商标限制，并计划 fork OpenBSD 内核。（BSD Now EP335，[419.28-605.24]，L2）
- JT 对‘从 Linux 迁移到 BSD’一文四个论点逐条反驳：Linux 碎片化被高估、商业介入非坏事、社区优劣是比例问题、许可证争论难有定论。（BSD Now EP335，[1941.52-2505.94]，L2）
- Will Backman作为早期BSD播客BSDTalk的主持人，在访谈中表示BSD Now等新音频资源分担了BSD社区的声音传播压力，使更多人以音频形式接触BSD。（BSD Now EP27，[3735.70-3797.78]，L1）
- Backman认为GPL3的转向曾让包括Apple在内的公司产生顾虑，而BSD许可虽早已存在，却在人们观念中重新浮现，Android等平台内核之上亦采用BSD式许可。（BSD Now EP27，[3572.44-3610.86]，L1）
- 访谈双方以ZFS进入FreeBSD安装器、bhyve即将可用等标志，表达2014年前后BSD社区从追赶Linux转向出现自身新特性的感知。（BSD Now EP27，[3613.56-3645.20]，L1）
- Alan Jude与TJ曾邀请Will Backman共同主持BSD Now，因其无法投入固定时间而未成行，这段口述记录了BSD Now节目创建初期的主持人选过程。（BSD Now EP27，[3835.86-3858.86]，L1）
- 当期教程展示NetBSD可通过build.sh在几乎任何支持编译器的系统上交叉编译，且可用非root用户完成构建，适合在快速服务器上为嵌入式平台生成系统与ISO镜像。（BSD Now EP27，[3927.86-4385.62]，L2）
- DragonFly BSD 1.4 于 2006 年 1 月 7 日发布；主持人补记此前遗漏，并说明该项目由一群围绕 FreeBSD 5 系内核希望作出重大改动的人分叉而来，旨在验证其在多处理性能上的理论，若理论成立则成果可惠及全部 BSD。（BSDTalk EP7，[20.38-79.16]，L2）
- GPL 正酝酿第三版：Richard Stallman 主导的修订拟纳入争议性反 DRM 条款，即 GPLv3 软件不得被改造用于对不自愿用户强制数字版权管理（如 TiVo 式设备限制用户复制与媒介转移的合理使用）。因 BSD 生态大量依赖 GNU 工具、尤其 GCC 编译器（Apple 亦曾长期为 PowerPC 改进 GCC），主持人推演其后果：并非所有软件都会升级到 v3，若 GCC 随 v3 发布可能出现以 v2 末版为基的分叉编译器，商业公司转向 Intel 平台后也可能改用 Intel 编译器；而 BSD 许可证仅有数行、几乎无限制（只要求署名与免于诉讼），GPLv3 的争议或促使商业公司重新审视 BSD 许可证与 BSD 系统，成为 BSD 的转折点。（BSDTalk EP7，[84.90-361.82]，L2）
- 主持人选取五款 BSD live CD 实测：FreeSBIE（FreeBSD 基）、Anonymous（OpenBSD 基）、DragonFly 安装盘（自述兼作 live CD 但极简）、NetBSD 官方 live CD（定位救援盘兼 KDE 桌面）、Newbee（NetBSD 基，主打全功能图形桌面）；测试硬件为 233 MHz/128 MB 旧笔记本、自制 AMD 2600 台式机、仅 USB 外设的 Dell GX280 与新款 Centrino 笔记本 Dell Latitude D610。（BSDTalk EP7，[376.02-517.04]，L1）
- 实测结果：除 Dell GX280 上 NetBSD live CD 不识别 USB 键盘致无法继续外，其余组合均可启动联网；DragonFly 盘仅文本模式、实用价值低但足以验证硬件支持；NetBSD 盘因缺 libqt 而无法启动 KDE，但 X 与轻量窗口管理器可用；Newbee 启动 Fluxbox 或 Blackbox 并预装浏览器邮件聊天工具；FreeSBIE 允许启动时选择轻量或重量级图形界面，基于 FreeBSD 5.3（2004 年 12 月发布），虽技术偏旧仍被主持人评为最佳 BSD live CD 桌面。横向对照：BSD live CD 资源占用普遍不高，但与 Linux 系 live CD 参照物（转写作 Canopix）相比浏览器启动明显偏慢，当事人将差距归因于后者更成熟、优化投入更多。（BSDTalk EP7，[549.84-843.56]，L1）
- Webmin 起源于作者任系统管理员时解决自身痛点的受限 Web 界面：为让非管理员安全变更 DNS 记录、避免手改配置文件破坏服务而写，随后逐步扩展出用户与组、Samba、Apache、NFS 导出等模块，长成覆盖多数类 UNIX 系统的管理框架。项目赞助历经多家公司：Caldera 于 2000 年赞助约一年，此后有 MSC Software，访谈时由 OpenCountry 赞助，但作者强调项目始终是自由软件、未被任何公司接管。（BSDTalk EP9，[277.26-383.38]，L1）
- 跨平台支持是 Webmin 的立项目标也是最重负担：各 UNIX 的基本概念（用户、组、文件）一致，但 NFS、cron 等服务的配置方式差异大，Apache 等常见软件在不同发行版中安装位置各异，Webmin 必须逐一掌握安装路径与版本。当事人的分化判断是：UNIX 家族之间未见进一步分化或收敛、大体稳定，而 Linux 发行版数量爆炸且各自发明打包方法与配置文件布局，未测试的发行版上不能贸然安装；支持最好的平台为 Red Hat/Fedora、Debian、Solaris、FreeBSD，即作者本人常用的系统，其中他偏好 Debian 的 apt 包管理之无痛安装，Red Hat/Fedora 的优势则在第三方商业软件商支持。（BSDTalk EP9，[392.60-560.38]，L1）
- 当事人解释弃 GPL 取 BSD 许可证的理由：GPL 虽好，但其源码共享义务限制了将 Webmin 改造进商业产品或设备（appliance）的用途；BSD 许可证允许任何人以任意方式使用与改造，在其看来才是真正的更自由。（BSDTalk EP9，[560.38-620.12]，L1）
- 衍生项目 Virtualmin 是 Webmin 的虚拟主机模块，对标 cPanel 与 Plesk，用于单机托管多虚拟网站、邮件域、DNS 域与 FTP；采用双版本策略：GPL 许可的免费版与功能增强的商业版并行，呈现了开源基础加商业增值的典型商业模式。（BSDTalk EP9，[775.82-811.34]，L1）

**史料**：

- Ruben 撰写的澳大利亚 FreeBSD mini-conf 回顾，含演讲者名单与议题。（BSD Now EP335，[1272.54-1438.44]，L2）
- It's FOSS 的 John Paul 对 Hyperbola 联合创始人 Andre 的访谈。（BSD Now EP335，[419.28-426.72]，L2）
- Kamil Rytarowski 的 NetBSD 博客：改进 ptrace API 并为 LLVM 10 做准备。（BSD Now EP335，[935.22-964.18]，L2）
- 当事人Will Backman自述其BSD播客经历、对BSD Now的评价，以及BSD Now主持团队最初向其发出的联合主持邀请。（BSD Now EP27，[3735.70-3858.86]，L1）
- 当期新闻与教程覆盖OpenBSD X server无需root运行的改进、OpenSSH 6.6测试呼吁、NetBSD build.sh交叉编译流程及PC-BSD的Life Preserver备份工具更新。（BSD Now EP27，[4417.34-4990.40]，L2）
- 当事人一手实测记录：五款 BSD live CD 在四类硬件上的启动、网卡与键盘图形检测、失败案例（GX280 USB 键盘不识别、NetBSD 盘 libqt 缺失）与逐盘评述，为 2006 年初 BSD 桌面化程度的一手横截面；另含经主持人转述的 DragonFly 1.4 发布公告及其分叉动机表述、GPLv3 起草阶段 FSF 与 Stallman 反 DRM 立场的公开信息。（BSDTalk EP7，[20.38-843.56]，L1）
- Webmin 作者 Jamie Cameron 的一手访谈自述：项目起源、模块化扩展过程、Caldera、MSC Software、OpenCountry 的赞助史、跨平台适配经验、对 Linux 发行版碎片化的判断、BSD 许可证选择理由与 Virtualmin 双许可模式；另涉及其 Prentice Hall 出版的著作《Managing Linux Systems with Webmin》——为 Webmin 1.0 而写，此后变化多为新增功能、书中内容仍有效，可免费下载亦可购买。（BSDTalk EP9，[277.26-811.34]，L1）
- BSD daemon 吉祥物的口述史材料（经主持人转述）：daemon 拼写区别于 demon、义为后台无人值守进程，源自古希腊语中守护精灵之义而无撒旦关联；现有形象由 John Lasseter 绘制；版权由 Marshall Kirk McKusick 持有，以确保该形象仅用于代表 BSD 软件及相关服务。（BSDTalk EP9，[78.52-150.64]，L2）

**史观**：

- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：Hyperbola 的 fork 决策围绕 GPL、四条款 BSD 与 CDDL 的兼容性展开，许可证成为利益与自由的分配工具。（BSD Now EP335，[672.14-806.78]，L2）
- 总纲6 和解优于斗争：总纲6 和解优于斗争：JT 主张以正面理由论证 BSD 而非贬低 Linux，正面论证优于负面论证。（BSD Now EP335，[1971.68-1991.92]，L2）
- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：BSD许可与GPL的此消彼长被当事人置于企业采纳与规避风险的框架中解释，许可首先表现为利益分配工具。（BSD Now EP27，[3572.44-3610.86]，L3）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：访谈以BSD许可重新浮现而非线性胜利的视角，同时呈现Linux技术优势与BSD许可吸引力，避免把某一方置于本体论优先位置。（BSD Now EP27，[3552.14-3645.20]，L3）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：播客主持、教程制作与NetBSD交叉编译的演示都强调实际操作者对知识传播与技术工具的推动。（BSD Now EP27，[3927.86-4385.62]，L3）
- 总纲13 法律与道德是利益分配：主持人对 GPLv3 反 DRM 条款的解读呈现了许可证作为利益分配机制的本质：Stallman 试图以许可证条款强制商业公司放弃对用户设备的 DRM 控制，将权利再分配给终端用户，而商业公司是否愿意接受尚属疑问；与之相对，BSD 许可证以近乎零限制的条款把选择权交还使用者和商业方，两种许可证哲学在 DRM 议题上正面相遇。（BSDTalk EP7，[132.54-355.32]，L2）
- 总纲4 分离聚合是永恒规律：主持人预测若 GCC 随 GPLv3 发布，可能出现以 v2 末版为基的分叉编译器：许可证条款变更触发项目分叉，正是开源谱系以分离应对分歧、以聚合延续成果的常态机制。（BSDTalk EP7，[314.34-334.28]，L2）
- 总纲10 动手者创造历史：Webmin 由一线系统管理员解决自己日常痛点的脚本生长为跨平台管理框架，再借企业赞助与社区协作扩张——项目的形态由动手者面临的实际运维问题而非顶层设计决定，体现了动手者在日常实践中创造技术历史。（BSDTalk EP9，[277.26-346.42]，L1）

**辨析**：

- Hyperbola 拟 fork OpenBSD 内核的计划被主持人质疑为工作量巨大、可持续性存疑，属开放性争议而非定论。　[存疑脚注] Hyperbola BSD 计划可行性存疑（BSD Now EP335，[829.34-903.78]，L3）
- 转写文本将嘉宾姓名拼写为Will Vokman、Will Bachman等多种形式，据语境应指BSD播客BSDTalk主持人Will Backman，引用时需以BSDTalk主持人的正式姓名为准。　[存疑脚注] 语音转写对嘉宾姓名拼写不一致，需以BSDTalk主持人的正式姓名Will Backman交叉核对。（BSD Now EP27，[0.0-12.52]，L5）
- 当事人自我限定：其四台测试机不代表全部硬件生态，个别失败可能只是特定硬件组合的偶然不兼容，不能据此否定某张 live CD 的整体质量，引用本期的硬件兼容性结论时须保留这一适用范围限定。另转写将 Linux 参照 live CD 记作 Canopix 或 Nopix，所指发行版名称待考，引用其性能对比前须核实项目实名。[存疑脚注] 转写中的项目名 Canopix/Nopix 无法确证，待与 2006 年 live CD 发行版名录核对。　[存疑脚注] 转写中的 Linux live CD 项目名 Canopix/Nopix 无法确证，待与 2006 年 live CD 发行版名录核对。（BSDTalk EP7，[392.64-843.56]，L5）
- BSD daemon 图像出自 John Lasseter、版权由 Marshall Kirk McKusick 持有之说在本期为主持人转述，与公开记录相符，但节目本身未给出处；引用时应回溯 McKusick 的官方表述与相关版权页面核实。[考据脚注] 转述内容与已知公开记录一致，仍需一手来源复核。　[考据脚注] 图像作者与版权持有人信息需与 McKusick 官方版权声明核对。（BSDTalk EP9，[125.04-150.64]，L2）

**文献**：

- [BSD Now EP335] Pennington J. BSD Now: 335: FreeBSD Down Under[EB/OL]. (2020-01-30)[2026-08-15]. https://www.bsdnow.tv/335.
- [BSD Now EP27] Pennington J. BSD Now: 27: BSD Now vs. BSDTalk[EB/OL]. (2014-03-05)[2026-08-15]. https://www.bsdnow.tv/27.
- [BSDTalk EP7] Backman W. BSDTalk: Live BSD CDs[EB/OL]. (2006-01-18)[2026-08-15]. https://archive.org/download/bsdtalk007/bsdtalk007.ogg.
- [BSDTalk EP9] Backman W. BSDTalk: Interview with Webmin Author Jamie Cameron[EB/OL]. (2006-01-24)[2026-08-15]. https://archive.org/download/bsdtalk009/bsdtalk009.ogg.

<!-- /PODCAST_REVIEW -->
