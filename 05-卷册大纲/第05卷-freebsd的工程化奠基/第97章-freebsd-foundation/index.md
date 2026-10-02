---
chapter: 第 97 章
id: CH97
volume: 第05卷-freebsd的工程化奠基
---

# 第 97 章 freebsd-foundation

## 要点

- 成立史料疑点：(1) 创始人名单是否包括 McKusick 还是仅 Gibbs 等；(2) 注册动机是否仅为商标保护还是更广义的项目支持；(3) 早期资金来源
- 边界史料疑点：(1) Foundation 雇员名单是否公开；(2) 雇员是否参与 Core Team;(3) 雇员薪酬是否影响决策
- 生平史料疑点：(1) 各董事的 BSD 参与起点；(2) 董事提名过程是否透明；(3) 董事是否曾因争议离职
- 比较史料疑点：(1) 各基金会披露程度不同；(2) 治理结构的实际运作与文档差距；(3) 跨基金会对比是否公平
- 批评史料疑点：(1) 批评者是否客观；(2) 批评是否反映社区共识；(3) 批评是否促成治理改革

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3797] 卷“第05卷-freebsd的工程化奠基”第 97 章，匹配置信度 folder，原因：folder 第95章
- [DB:references_fulltext:chapter_matches:chmatch_1229] 卷“第05卷-freebsd的工程化奠基”第 97 章，匹配置信度 0.7，原因：无匹配
- [DB:bsdnow_podcast:outline_mappings:om_10420] BSD Now 第 676 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10440] BSD Now 第 674 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10477] BSD Now 第 665 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10490] BSD Now 第 664 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10509] BSD Now 第 661 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10520] BSD Now 第 659 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10539] BSD Now 第 654 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10588] BSD Now 第 645 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10598] BSD Now 第 644 期，匹配 CH97 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10616] BSD Now 第 641 期，匹配 CH97 章，关联度 1.0

## 史观

- 本章不设章级史观综合；史观映射详见各子节文件的“史观/辨析”字段（如 97.7 历年决议文档概览——治理留痕、97.8 社区争议——技术派与商业派的分歧）。

## 辨析

- 创始人名单在基金会不同文档中是否一致，需逐份核对；**统计局限性标注**——统计显著 ≠ 实际显著，C-12 变点 p < 0.001 仅反映 commit 时序存在结构性断点，不等于 Foundation 的成立 “导致” 了变点，变点为工程节律切换的统计表征而非 Foundation 成立的工程因果；C-12 双检验一致性（Pettitt 与 BUISHAND）降低单一方法偏差但不可消除方法学
- 不应神化基金会——FreeBSD 的成功仍依赖核心开发者与社区；基金会是赋能工具而非替代。
- Determination Letter 是否曾在 IRS EO Select Check 中可查，需核实
- 州务卿备案是否包含完整 By-Laws，需查科罗拉多州备案规则
- McKusick 为亲历者，其“deadwood”表述带有当事人视角；首届民选核心团队（2000）与 Foundation 成立（2000）同年，二者是否同一治理改革的组成部分须对照 Core Team 档案核验

## 文献

- Foundation 官方文档；Gibbs BSDCon 2001 演讲 ［B］；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md**；统计分析报告：推断性统计.md Task 6 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md**；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. freebsd.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase2_inferential.py`. Task 6 变点检测（Pettitt + BUISHAND）. 执行日期：2026-07-27 [考据脚注：C-03 freebsd-src 444,203 commits 与 C-12 变点 1999-08 经 `script/phase2_inferential.py` 执行结果与 `phase2_results.json` 结构化结果交叉验证；变点判定非迁移伪变点已通过距 2020-01 SVN-to-Git 迁移 245 个月的时间间距排除。]

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2000-2000 年间：29,754 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Foundation 990 表；Core Team 名单 ［A］

## 史料考据补充（2026-08-04 任务3 联网核验）

> 主题：staff developer 与志愿者的张力
- 作者不详. FreeBSD Foundation 董事会名单[Z]. 年份不详；作者不详. freebsd-hackers 邮件列表[EB/OL]. 年份不详 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 各基金会 990 表［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 作者不详. 批评博客[EB/OL]. 年份不详；作者不详. FreeBSD Foundation 改革记录[Z]. 年份不详 ［C］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Foundation 档案［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
FreeBSD 社区论文：[FP-2020-014] FreeBSD Around the World!（Deb Goodkin（德布·古德金），2020）<https://papers.freebsd.org/2020/fosdem/goodkin-freebsd_around_the_world/>
FreeBSD 社区论文：[FP-2018-002] Flexible Disk Use in OpenZFS（Matt Ahrens，2018）<https://papers.freebsd.org/2018/bsdcan/ahrens-flexible_disk_use_in_openzfs/>
FreeBSD 社区论文：[FP-2018-043] The FreeBSD Foundation and How We Are Changing the World（Deb Goodkin，2018）<https://papers.freebsd.org/2018/fosdem/deb-the_freebsd_foundation_and_how-we_are_changing_the_world/>
FreeBSD 社区论文：[FP-2015-008] Supporting a BSD Project（Ed Maste（埃德·马斯特），2015）<https://papers.freebsd.org/2015/vbsdcon/maste-supporting_a_bsd_project/>
FreeBSD 社区论文：[FP-2010-002] Software Tools - Mission Accomplished or Mission Failure ?（Poul-Henning Kamp（波尔-亨宁·坎普），2010）<https://papers.freebsd.org/2010/phk-software-tools/>
FreeBSD 社区论文：[FP-2007-003] Lousy virtualization, Happy users: FreeBSD's jail(2) facility（Poul-Henning Kamp，2007）<https://papers.freebsd.org/2007/euug/phk-jail/>
FreeBSD 社区论文：[FP-2005-001] Building a FreeBSD Appliance With NanoBSD（Poul-Henning Kamp，2005）<https://papers.freebsd.org/2005/phk-nanobsd/>
FreeBSD 社区论文：[FP-2005-004] Ioctl(2) is so 1980ies（Poul-Henning Kamp，2005）<https://papers.freebsd.org/2005/phk-ioctl/>
FreeBSD 社区论文：[FP-2004-003] GEOM（Poul-Henning Kamp，2004）<https://papers.freebsd.org/2004/phk-geom/>
FreeBSD 社区论文：[FP-2004-004] GEOM Tutorial（Poul-Henning Kamp，2004）<https://papers.freebsd.org/2004/phk-geom-tutorial/>
FreeBSD 社区论文：[FP-2004-005] Making sure data is lost（Poul-Henning Kamp，2004）<https://papers.freebsd.org/2004/phk-gbde/>
FreeBSD 社区论文：[FP-2003-001] GBDE - GEOM Based Disk Encryption（Poul-Henning Kamp，2003）<https://papers.freebsd.org/2003/bsdcon/phk-gbde-paper/>
FreeBSD 社区论文：[FP-2003-002] GEOM tutorial（Poul-Henning Kamp，2003）<https://papers.freebsd.org/2003/bsdcon/phk-geom-tutorial/>
FreeBSD 社区论文：[FP-2003-003] Making sure data is lost（Poul-Henning Kamp，2003）<https://papers.freebsd.org/2003/bsdcon/phk-gbde-slides/>
FreeBSD 社区论文：[FP-2002-004] Rethinking /dev and devices in the UNIX kernel（Poul-Henning Kamp，2002）<https://papers.freebsd.org/2002/bsdcon/phk-devfs/>
FreeBSD 社区论文：[FP-2002-009] Timecounters: Efficient and precise timekeeping in SMP kernels（Poul-Henning Kamp，2002）<https://papers.freebsd.org/2002/phk-timecounters/>
FreeBSD 社区论文：[FP-2000-001] Jails: Confining the omnipotent root（Poul-Henning Kamp; Robert N. M. Watson（罗伯特·N·M·沃森），2000）<https://papers.freebsd.org/2000/phk-jails/>
FreeBSD 社区论文：[FP-2000-003] The Nanokernel（Dave L. Mills; Poul-Henning Kamp，2000）<https://papers.freebsd.org/2000/phk-nanokernel/>
FreeBSD 社区论文：[FP-1998-001] Raw data: Interrupt latency measurements（Poul-Henning Kamp，1998）<https://papers.freebsd.org/1998/phk-interrupts/>
FreeBSD 社区论文：[FP-1998-002] Malloc(3) revisited（Poul-Henning Kamp，1998）<https://papers.freebsd.org/1998/phk-malloc/>

### 史观映射

> 基金会的诞生把一个松散的黑客共同体推入了法律实体的模具——科罗拉多州注册、IRS 501(c)(3) 裁定、By-Laws 条款、officer 职责分工，每一份表格都在把 “谁有权做什么” 从默契变成条文。形式主义化不一定是堕落——没有基金会，Jan Koum（简·库姆） 的支票无处可签；但形式主义化也不一定是进步——当执行总监与董事会争夺日常运营权，当技术派与商业派在预算表上对峙，当员工开发者因有薪酬而比志愿者更有话语权，治理就不再是服务社区的工具，而是社区必须服从的结构

---

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD 相关记录（详情见存疑库；本条为自动抽取块，未经人工核验，引用前须逐条验证）。文献 (Code, 2024) 提及 Tetlow, Gordon〔存疑：原文记作“FreeBSD Foundation 执行董事”，与 97.11 报告（Goodkin 任执行总监）及 EP616 口述冲突，Gordon Tetlow 系开发者，职务归属待核〕，在基金会治理和项目战略规划中发挥关键作用。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 提及 Neville-Neil, George，作为 FreeBSD Core Team 成员，在存储系统方面做出了重要贡献。文献 (FreeBSD-Foundation-August-2016-Update, 2016) 提及 Baldwin, John，作为 FreeBSD 核心开发者，在内核修复和架构支持方面做出了重要贡献。文献 (FreeBSD-Foundation-December-2016-Update, 2016) 提及 Watson, Robert N. M.，以基金会董事会成员身份在上海 BSD 聚会中发表了演讲。文献 (FreeBSD-Foundation-January-2018-Update, 2018) 提及 Percival, Colin，作为 Tarsnap 总裁，对 FreeBSD 安全更新基础设施做出了重要贡献。**新增技术**文献 (Code, 2024) 讨论 bhyve，该安全审计报告对 Capsicum 和 bhyve 子系统进行了全面的安全审查。文献 (Code, 2024) 讨论 FreeBSD，该报告由 FreeBSD Foundation 于 2024 年 11 月发布。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 讨论 Ports Collection，FreeBSD 社区贡献者持续将改进和错误修复贡献回上游项目。文献 (FreeBSD-Foundation-December-2016-Update, 2016) 讨论 DTrace，社区成员对 Jails、DTrace 和 ZFS 等主题表现出浓厚兴趣。文献 (FreeBSD-Foundation-February-2018-Update, 2018) 讨论 lld，FreeBSD 工具链现代化项目将 LLVM 的 LLD 链接器引入基本系统。文献 (FreeBSD-Foundation-January-2018-Update, 2018) 讨论 clang，FreeBSD 在基本系统中采用 Clang 编译器作为默认编译器。**新增时间线事件**文献 (Code, 2024) 记录 2019：FreeBSD 安全公告涉及 CVE-2019-5607 漏洞。文献 (Code, 2024) 记录 2019：该安全公告涉及的漏洞模式分析。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 记录 2012：FreeBSD 项目在 NYI 数据中心部署了东海岸镜像站点。文献 (FreeBSD-Foundation-April-2016-Update, 2016) 记录 2015：FreeBSD 测试集群在 2015 年底进行了重大升级。文献 (FreeBSD-Foundation-April-2018-Update, 2018) 记录 2018：FreeBSD 基金会参加了 Rootconf 2018 和 BSDCan 2018 等社区活动。文献 (FreeBSD-Foundation-April-2018-Update, 2018) 记录 2018：FreeBSD 基金会 2018 年 4 月更新，涵盖 Rootconf 2018 和 BSDCan 2018 
<!-- DB_REF:freebsd.duckdb -->> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2000-2000 年间：29,754 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

- IRS EO Select Check；Foundation 历年 990 表［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- 科罗拉多州务卿档案；Foundation By-Laws ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- McKusick & Rice. The Evolution of FreeBSD Governance [J]. FreeBSD Journal, 2017, 4(5): 26-31 ［A］；McKusick. The Evolution of FreeBSD Governance [C]//BSDCan 2018. Ottawa, 2018 ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1996-2010 年间：482,545 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP566、BSD Now EP648、BSD Now EP333、BSD Now EP278、BSD Now EP269、BSD Now EP258、BSD Now EP198、BSD Now EP194、BSD Now EP192、BSD Now EP189、BSD Now EP166、BSD Now EP138、BSD Now EP622、BSD Now EP616、BSD Now EP59、BSD Now EP56、BSD Now EP51、BSD Now EP23、BSD Now EP2、BSD Now EP1、BSDTalk EP169、BSDTalk EP237（共 22 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 主持人介绍 FreeBSD Day 的 31 周年庆祝，并转述一篇综述文章对 FreeBSD 历史的阶段划分：1993 年 1.0 首发，2.0 与 2.1 引入 ports 集合，3.0 引入 GEOM 框架与对称多处理改进，4.x 以稳定著称，6.x 引入 jails，8.x 与 9.x 引入 ZFS 与 DTrace，后续版本扩展 ARM 架构支持。（BSD Now EP566，[367.60-589.20]，L2）
- Tom Jones 自述受 FreeBSD 基金会与 RG Nets 共同资助，将基于 DPDK 的高性能用户态转发框架 VPP 移植到 FreeBSD 并回馈上游，产生逾百项变更，约 20% 已合并，移植工作还促使 VPP 核心基础设施变得更灵活。（BSD Now EP566，[1513.74-1930.24]，L1）
- 主持人评述 Rust 的 crates.io 依赖注册表存在供应链安全隐患，并对比 OpenBSD 与 FreeBSD 基本系统自带经审查工具、无需海量外部依赖的路径。（BSD Now EP566，[2342.36-2831.24]，L2）
- FreeBSD Foundation 2026 募款文显示资金约三分之二用于软件开发，其余用于宣传教育、基础设施与筹款管理，强调捐赠直接支撑笔记本电脑、构建测试与持续集成。（BSD Now EP648，[103.42-208.70]，L2）
- Peter N. M. Hansteen 自述 2007 年起运行 spamd 灰度陷阱，截至 2025 年 8 月陷阱条目超过 562 万、超过挪威人口，数据显示垃圾邮件活动呈下降趋势但伴随突发峰值。（BSD Now EP648，[257.02-1152.28]，L1）
- BSDCan 组织委员会回顾会议由 Dan Langille 在渥太华大学创办并连续举办 22 年，领导权经 Dan Langille、Michael W. Lucas 逐代交接，规划委员会维持约 12 人。（BSD Now EP648，[1246.88-1475.48]，L1）
- BSDCan 2026 延续教程加两天会议的形式，AV 团队与 ScaleEngine 合作向 YouTube 与 PeerTube 同步直播，并计划提高分辨率与音频质量。（BSD Now EP648，[2144.22-2315.56]，L1）
- Chris Siebenmann 以 400 余行既有 PF 规则、本地运维工具与团队知识三个理由说明从 OpenBSD PF 迁往 Linux nftables 的代价高于收益。（BSD Now EP648，[3328.02-3441.68]，L1）
- FreeBSD Foundation 回顾 2019 年：参与 38 场会议、资助 Wi-Fi 支持与安全团队，并强调捐款直接支撑项目。（BSD Now EP333，[73.4-189.2]，L2）[订正：原 [69.24-169.04]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 6.6 路由器上的 WireGuard 配置教程，通过 PF 与 MTU/MSS 调整实现 VPN 出口。（BSD Now EP333，[430.3-658.3]，L2）[订正：原 [420.78-653.64]，2026-09-30 SenseAudio 重转核对]
- Amazon 推出基于 Graviton2 的 ARM 实例并支持 FreeBSD 12.1，宣称较 x86 有 40% 更优性价比。（BSD Now EP333，[703.6-810.4]，L2）[订正：原 [704.98-810.16]，2026-09-30 SenseAudio 重转核对]
- McKusick 亲述伯克利早期四张桌四人同处一室、与 Bill Joy 为办公室同僚，办公室仅一部电话且十之八九是找 Bill Joy；他形容 Bill Joy 更像营销者，四处演讲、散发磁带、动员他人贡献。（BSD Now EP278，[173.80-287.60]，L1）[订正：原 [176.66-198.66]，2026-09-30 SenseAudio 重转核对]
- McKusick 认为 FreeBSD 二十五年来最大的成就是形成一套能持续吸纳新人并让其上升的治理机制：文档 committer 与源码 committer 同样有权选举 core，营销背景者也能当选。（BSD Now EP278，[533.12-611.68]，L1）
- McKusick 援引 MIT 与法国南部高校的社会学研究，称多数开源项目约五年内沉寂，只有 Apache 与 FreeBSD 等项目完成三次以上成功的领导层更替，FreeBSD 已历约五代。（BSD Now EP278，[725.94-848.56]，L1）
- McKusick 亲述 FreeBSD 基金会起源：早期发行由 Walnut Creek CD-ROM 支撑，后依赖 Yahoo 提供基础设施十余年，Justin Gibbs 因担忧单一公司退出而发起基金会。（BSD Now EP278，[1883.72-1965.34]，L1）
- McKusick 亲述 UFS 三十年：其保存的 1982 年磁盘镜像在当代仍可读写，UFS 适合资源受限的嵌入式设备，ZFS 适合大资源环境，二者各解决不同问题。（BSD Now EP278，[1093.34-1174.26]，L1）
- McKusick 判断容器概念发明于 FreeBSD 却在他处获得成功，FreeBSD 常把项目推进到九成而缺最后一成产品化，恰如“先驱挨箭、定居者得地”。（BSD Now EP278，[2596.78-2625.54]，L1）
- FreeBSD 基金会 2018 年 9 月更新报告全年筹款目标为 125 万美元，Verisign 成为银级赞助商，基金会资助 CI 系统、发布工程与安全团队以支持 12.0 发布。（BSD Now EP269，[435.64-611.40]，L2）[订正：原 [435.64-528.72]，2026-09-30 SenseAudio 重转核对]
- 文章介绍 daemonize 微型 C 库：System V 式守护进程初始化步骤繁多，而 BSD 自 4.4BSD 起提供的 daemon() 函数不完整遵循这些步骤，作者遂编写仅两个文件的小型库。（BSD Now EP269，[1440.68-1771.96]，L2）
- 微软将 DTrace 从 FreeBSD 移植到 Windows 10，D 脚本基本一致，仅系统调用名改为 NT 前缀的驼峰形式；DTrace 谱系为 illumos 发明、移植 FreeBSD、再传 macOS 与 Windows。（BSD Now EP269，[3414.48-3586.48]，L2）
- 波兰 BSD 用户组由 Mariusz Zaborski 等人在访问湾区 FreeBSD 用户组后创立，定位为促进波兰全部 BSD 的社区，会议以网络交流为主、演讲不超过十五分钟。（BSD Now EP269，[2943.52-3137.00]，L2）
- 节目朗读 FreeBSD 基金会 2018 年 7 月通讯：商业与个人捐赠用于质量保证、持续集成与自动化测试的全职软件工程师，以及安全团队与发布工程团队的关键岗位，并赞助和参加开源会议以推广 FreeBSD。（BSD Now EP258，[321.10-419.90]，L1）[订正：原 [315.56-412.50]，2026-09-30 SenseAudio 重转核对]
- HardenedBSD 基金会于 7 月 9 日举行董事会 kickoff 会议，计划申请 501c3 免税地位；在马里兰州注册免税非股份公司、取得联邦税号，并增补 Emerald Onion 董事 Christian Severt 为顾问，预计年底前获批。（BSD Now EP258，[3362.40-3523.30]，L2）
- OpenBSD 的 Philip Guenther 与 Brian Steele 为 AMD64 增加 Spectre RSB 等推测执行缓解，在进入内核与返回用户空间时填充返回栈缓冲区，并将该缓解扩展到 VMM 虚拟机退出路径。（BSD Now EP258，[3532.28-3667.74]，L2）[订正：原 Philippe Gontier，2026-09-30 SenseAudio 重转核对]
- 该期回顾 BSDCan 2017：开发者峰会、教程与正式会议四轨并行，列举大量演讲（SSH 滥用做 ZFS 复制、packet drill、FreeBSD ARM 启动、OpenBSD VMM、bhyve 安全恢复、Netflix 大 mbuf、Capsicum 沙箱等）。（BSD Now EP198，[4352.30-5412.26]，L2）
- 渥太华大学法学教授 Michael Geist 发表主旨演讲，讨论技术社群面对电信巨头与政策游说的挑战，主张技术人员通过联系议员、提供专家证词等方式介入政策制定，避免政府只听到游说一方。（BSD Now EP198，[4152.78-4309.98]，L2）
- FreeBSD 基金会与滑铁卢大学合作启动 co-op 实习生计划，学生在 Ed Maste 指导下参与项目，并在 BSDCan 展示构建状态仪表盘等成果。（BSD Now EP198，[479.90-573.74]，L2）
- FreeBSD 2017 年第一季度状态报告记录 core team、基金会、ports（接近三万端口）、release engineering（11.1 排期）等团队动态，基金会赞助 168 个提交并资助多个项目。（BSD Now EP194，[98.3-164.34]，L2）
- Colin Percival 提出一种介于 Patreon 与 Bugzilla 之间的开源维护资助模型，主张以持续收入支持软件维护而非一次性赏金，从而缓解开源软件维护不足的问题。（BSD Now EP194，[878.98-1386.52]，L2）
- Chris Siebenmann 追溯 FreeBSD 目录组继承行为至 4.1cBSD 引入 mkdir 系统调用与多组进程的时期，指出新对象继承父目录组是传统 BSD 行为而非 FreeBSD 的新发明。（BSD Now EP194，[2332.28-2964.74]，L2）
- OpenBSD 变更集移除 SSHv1 协议代码，从 FreeBSD 移植 witness 锁顺序校验工具，并引入 BearSSL 常数时间 AES 实现。（BSD Now EP194，[1925.44-2328.28]，L2）
- OpenSSH 彻底移除 SSHv1 全部代码，简化协议处理；此前该协议已默认禁用多年。（BSD Now EP192，[65.54-183.18]，L2）
- FreeBSD 基金会 4 月更新记录授予 Edward Napierala 项目资助，以 CTL 为后端开发 USB 大容量存储目标驱动，使 BeagleBone Black、Raspberry Pi Zero 等嵌入式平台可模拟 U 盘。（BSD Now EP192，[210.02-300.24]，L2）
- Patrick M. Hausen 回忆 1994 年与 Jordan Hubbard 会面，获 Walnut Creek 全套 CD-ROM 与 50 张 FreeBSD 1.1 光盘回德国推广，其后公司以 FreeBSD 3/4 运行服务器。（BSD Now EP192，[1270.68-1320.66]，L1）
- Rick Macklem 发布 pNFS 服务器首个测试征集，架构为单个元数据服务器加多个数据服务器，纯 FreeBSD 实现，当前尚不支持冗余。（BSD Now EP192，[5241.34-5535.38]，L2）
- NetBSD 在其 wiki 列出 GSoC 内核级与用户态项目并标注难度；FreeBSD 的项目含 Lua bootloader、POSIX 合规测试框架、.NET Core CLR 移植等。（BSD Now EP189，[585.22-733.18]，L2）
- 受访者 Wendell 回忆 ZFS 可从多盘硬件故障且池满的状态恢复数据，并支持池在 SPARC 与 amd64 架构间跨字节序移植。（BSD Now EP189，[4340.92-4558.02]，L1）
- Wendell 用退役的 IBM NetApp 磁盘柜与 Google Search Appliance（Dell R710）搭建 10GbE 视频存储，ZFS 压缩使八百万文件遍历缩短到八分钟。（BSD Now EP189，[4702.86-5620.86]，L1）
- Ted Unangst 撰文记录在网站登录、系统登录等场景使用 YubiKey 的体验，以帮助他人少走弯路。（BSD Now EP189，[6182.44-6225.48]，L2）
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
- Benedict Reushling 自述其入会路径：EuroBSDCon Sofia（2014）会后被 Erwin Lansing 略带神秘地接洽，受邀加入 FreeBSD Foundation 董事会，动因是董事会欲在德语区（德、奥、瑞士）扩展席位；2015 年 1 月前后经正式电话面试，面试中他自陈“我是文档人，不熟悉内核”，有董事随即打断并表态“源码提交者已经够多，董事会需要多样性”（1664-1688 秒）；同年 BSDCan 前的年度董事会完成履新，受访时（AsiaBSDCon 2016 东京现场）入会约一年，其定位始终是文档与欧洲拓展而非内核开发。　[存疑脚注] 受访人姓氏在转写中作 Russeling/Herschling，按 FreeBSD Foundation 董事名录判定为 Benedict Reushling；电话面试中另一表态董事姓名转写失真（音似 Qsync），仅 Kirk 一名可辨。（BSD Now EP138，[1596.68-1694.12]，L1）
- 基金会职能被受访者概括为“支持位”而非治理位：不向项目推送任何政策、不指定开发何种驱动，而是以资金资助开发者与发布工程师等职员、以法人实体身份签署 NDA 等法律文书、维护 FreeBSD 注册商标——freebsd.foundation 新顶级域名遭抢注者索价 8000 美元，董事会曾在付款、无视与诉诸律师之间权衡——并走访 iXsystems、Netflix 等大赞助商，维系捐赠并对接其技术需求，同时开拓欧洲赞助方与 Linux 系会议之外的布道场合（1791-1990 秒）。（BSD Now EP138，[1782.6-1992.4]，L1）[订正：原 [1789.80-1989.86]，2026-09-30 SenseAudio 重转核对]
- Mark Phillips 自述 2014 年入职仅约 18 个月的 Ansible，次年公司被 Red Hat 收购；此后在 Red Hat 与多家创业公司间辗转，2025 年初加入 FreeBSD Foundation 任技术营销经理。（BSD Now EP622，[407.42-944.24]，L1）
- Mark Phillips 主张营销的本质是对好产品讲好故事，把营销替换为讲故事即可理解其工作，并强调技术与营销互为表里、工程师需要被反馈其工作价值。（BSD Now EP622，[944.24-1506.38]，L1）
- Mark Phillips 认为 ZFS 是 FreeBSD 的杀手特性，Solaris 系统管理员因 ZFS 与 DTrace 的继承而转向 FreeBSD，FreeNAS 等产品也以此为基础。（BSD Now EP622，[1051.38-1238.66]，L1）
- Mark Phillips 曾帮助测试 Colin Percival 的 EC2 ZFS 根镜像工作，并从 Lightsail 迁往 EC2 以获得 ZFS 根文件系统。（BSD Now EP622，[1205.98-1244.40]，L1）
- Mark Phillips 建议开发者讲故事时不要试图改变他人想法，而是热情讲述自己相信并亲历的解决过程；他推荐 John York 的《Into the Woods》、Seth Godin、Kahneman 与 Nancy Duarte 等读物。（BSD Now EP622，[2825.06-3030.52]，L1）
- FreeBSD 基金会于 2000 年前后创立，直接动因是让项目拥有可持有注册商标并募集资金的法律实体；首任团队由 Justin Gibbs、John Polstra 与 John Bresler 等志愿者组成，早期由 Gibbs 个人垫资起步。（BSD Now EP616，[248.88-257.34]，L1）
- 基金会选择 501(c)(3) 公共慈善结构，而非 Linux 基金会式的 501(c)(6) 会员制；前者的资金来源以公众捐赠为主，且须证明其服务于公共目的，这一法律结构差异决定了二者的治理取向。（BSD Now EP616，[289.12-311.36]，L1）
- 基金会由最初亲力亲为的三名志愿者董事会，发展为拥有约七名员工与二十名承包商的职业化机构，预算规模约二百七十万至二百九十万美元。（BSD Now EP616，[549.7-586.06]，L1）
- core team 每两年改选并越来越多地承担技术路线图职责，基金会作为持久实体提供连续性与支持，二者通过季度报告、会议记录与共同培训保持对齐。（BSD Now EP616，[1844.08-2006.00]，L1）
- 受访者将 Jails 追认为容器化的先驱之一，但认为 FreeBSD 社区的“黑客伦理”与“用代码说话”传统使其长期缺乏面向市场的叙事能力。（BSD Now EP616，[1186.70-1252.80]，L2）
- 斋藤博纪自述入道经历：入大学前使用 PC-98（日本特有规格的 IBM 兼容机）加 MS-DOS，经电话线拨号与他人通信；进大学后接触 Sun 工作站与 IBM AIX，深受震撼，遂想在自家机器上运行 UNIX。因 PC-98 规格特殊需要移植版 PC UNIX，当时 Linux 与 FreeBSD 均有移植而只有 FreeBSD 能在其机器上运行；版本约 2.2.5，机器仅 8MB 内存与 180MB 硬盘，编译 X 花了两天。直接动机是在原生 UNIX 环境使用正宗 TeX 实现撰写论文——MS-DOS 上须借 DOS 扩展器才能用扩展内存——此后学习网络配置接入互联网。（BSD Now EP59，[1743.93-2004.19]，L1）
- 日本 BSD 生态的转折点（当事人一手叙述）：1994—1995 年日本 FreeBSD 用户众多；NetBSD 引入 newconfig 配置框架后，日本许多能读内核代码的高手认为应基于 config 实用工具另建配置框架并写出自有代码，但美方多数人不知该代码存在；这些日本开发者相信自己代码技术上更优，却不参与英文邮件列表讨论，仅投递超长行数的补丁且不说明理由，补丁因难读难懂而被忽略。结果是多数日本 FreeBSD 开发者转投 NetBSD，部分人随后创立公司；IIJ 作为主要 ISP 因熟悉内核而在服务与产品中大量采用 NetBSD。日本 FreeBSD 拥趸的这次集体转向，塑造了此后亚洲 BSD 大会浓厚的 NetBSD 色彩，而日本其他开源会议多面向爱好者而非开发者。（BSD Now EP59，[2227.32-2511.23]，L1）
- 当代工作与组织改革设想：斋藤近期积极改进 FreeBSD 的 IPv6 栈——KAME 项目结束后该栈实际无人维护，而 IETF 与 RFC 持续发布新规范需跟进实现。作为 core team 成员，他拟提交 Quality Assurance 团队提案：汇集分散的测试基础设施努力，以统一 web 界面保存各分支的质量评估并供开发者共享，纠正对个人努力的依赖（此前的性能分析者离开后工作即中断），并为 core team 的方向决策提供咨询。作为 Foundation 董事，他运营 AsiaBSDCon、走访企业与洽谈镜像站点；另设立本地非营利组织作为与企业谈判的凭据，因其直言日本人只信任有机构背景者而非热情个人：NEC 的 UNIX 服务器软件销量居日本之首、大量客户想用 FreeBSD 却不知如何获得支持，他已向 NEC 提供信息并获积极回应；Sony 则因保密文化几无信息可获——曾谈成的开发者采访在 Sony 要求预审问题清单后杳无音信，且公司内部必须经经理层许可，开发者本人无对外联络的决策权。（BSD Now EP59，[2011.63-2783.80]，L1）
- IPFW 十余年来最大更新的要点：表可命名（至多 65000 个表、每个名称 63 字符）、表感知规则集可实现原子切换、批量增删、新增 flow 表类型与按 CIDR 哈希/接口/数字/流等多种查找算法、表值可承载多数据字段；主锁改为 RM lock，规则计数器与规则本体分离并按 CPU 分配以降低锁争用；旧命令行工具对新内核接口保持 ABI 兼容但无法识别表名、一律显示为表 65535。BSD Router Project 维护者 Olivier 的基准测试（4 核 Xeon 2.13GHz 配 Intel X540 双口万兆网卡、2000 条状态）显示改动前后吞吐提升约每秒 10 万包，其本人表示期待出现 pfsync 的 IPFW 等价物。（BSD Now EP59，[1391.89-1594.26]，L2）
- FreeBSD.org 集群由约一百三十台机器分布于全球六个地理位置，并运行一百一十多个 jail，广泛使用 ZFS、PF、VLAN 与 GeoDNS。（BSD Now EP56，[582.9-657.04]，L1）[订正：原 [574.76-657.04]，2026-09-30 SenseAudio 重转核对]
- 集群长期在开发分支 head 上运行以对最新代码进行真实负载压力测试，并已转向统一二进制构建以替代逐机 make world。（BSD Now EP56，[855.6-1043.1]，L1）[订正：原 [1126.38-1225.00]，2026-09-30 SenseAudio 重转核对]
- 2012 年安全事件源于开发者经被攻破的大学网络跳板泄露 SSH 密钥，攻击者抓取连接关系并回连个人主机；David Wolfskill 因发现异常登录而触发追踪。（BSD Now EP56，[2112.8-2305.54]，L1）[订正：原 [2102.38-2305.54]，2026-09-30 SenseAudio 重转核对]
- 事件后集群改为机器间互不信任、拉取而非推送、审计记录入密封存储，并尽量以 JBOD 取代不可靠的硬件 RAID 控制器。（BSD Now EP56，[2022.30-2423.84]，L1）
- Eric LeBlanc 自述 Xinuos 在约十八个月调研后选择 FreeBSD 作为新增支持的开源操作系统，理由包括与 OpenServer 相近的代码树、BSD 许可证及 FreeBSD Foundation 的存在。（BSD Now EP51，[1014.92-1082.10]，L1）
- Xinuos 以 BSD 许可证允许转售商与客户开发专有环境为关键考量，并计划对 FreeBSD 稳定分支提供最长十五年的支持与回溯移植。（BSD Now EP51，[1163.86-1335.46]，L1）
- Xinuos 计划将 OpenServer 与 UnixWare 等遗留应用运行于 bhyve 虚拟化之上，以迁移无源码的旧应用。（BSD Now EP51，[1465.72-1508.64]，L1）
- Ted Unangst 自述约 2000 年接触 OpenBSD 并因其稳定性成为用户，此后 11 年担任 OpenBSD 开发者，因提交大规模 VFS 锁修复 diff 而获得 commit 权限。（BSD Now EP23，[728.56-800.12]，L1）
- signify 是仅用于密码学签名与校验的简单工具，不含加密功能；自 2013 年 12 月 21 日开发，Ted Unangst 为主要作者，Marc Espie 编写包工具集成，Alexander Hall 编写安装器部分。（BSD Now EP23，[898.44-991.80]，L1） [订正：原 [898.44-1006.76]，2026-09-30 SenseAudio 重转核对]
- OpenBSD 自 5.5 起以 signify 签名基础发行集与第三方包，采用 SHA256.sig 签名校验和清单；使用单一密钥而非 PKI 信任链，公钥检入源码库并经邮件列表扩散。（BSD Now EP23，[934.36-1387.66]，L1）
- FreeBSD Foundation 2013 年筹款总额为 768,562 美元，来自约 1,659 名捐赠者，并已启动 2014 年百万美元目标。（BSD Now EP23，[76.32-139.56]，L2）
- 教程演示自建 NTP 服务器，并报道 OpenBSD 在 BeagleBone Black 上的 ARMv7 移植经验，涉及不同存储选项与已知问题的规避。（BSD Now EP23，[428.10-474.86]，L2）
- FreeBSD 发行工程团队在代码冻结后审批所有针对该分支的变更，目标是在已知良好状态上修复既有问题而非引入新特性，以降低升级回归风险。（BSD Now EP2，[2347.62-2437.94]，L1）
- Glen Barber 加入 FreeBSD 基金会后获得专职时间协调发布流程，并兼管集群管理团队与项目资源维护，使发布节奏不再完全依赖志愿者的时间。（BSD Now EP2，[4398.47-4558.76]，L1）
- FreeBSD 10-CURRENT 自 2013 年 9 月起不再默认构建 GCC，基本系统改以 Clang 为默认编译器；需要 GCC 的场景改由 ports 提供现代版本。（BSD Now EP2，[543.86-622.62]，L2）
- LDNS 与 Unbound 正被移植入 FreeBSD 基本系统，计划在 10.0 前移除 BIND；主持人预期此举可减少约三分之一的安全公告负担。（BSD Now EP2，[4075.30-4225.94]，L1）
- Poudriere 以 jail 隔离并发构建二进制包，可在一台机器上按 FreeBSD 版本与架构分 jail 编译，并以增量重建与摘要签名支撑自有 pkg 仓库分发。（BSD Now EP2，[865.40-904.68]，L2）
- 该期头条报道 OpenBSD 已实现 64 位 time_t，以避免 2038 年 32 位时间戳溢出；该改动使 32 位平台也能跨越 Y2038 时间曲线。（BSD Now EP2，[71.70-150.60]，L2）
- 该期头条报道 FreeBSD 10-CURRENT 合入 Radeon KMS 内核图形驱动，标志 FreeBSD 桌面图形栈由传统驱动模式向内核模式设置过渡，并为 10.0 发布前的驱动测试提供基础。（BSD Now EP1，[70.30-125.02]，L2）
- VeriSign 公开拥抱 FreeBSD，以之支撑 .com、.net 等顶级域名的 DNS 根服务器；主持人归纳其选择理由为平台稳定、高并发查询处理能力与社区可回馈性。（BSD Now EP1，[281.60-311.04]，L2）
- Peter Hessler 的 BGP SpamD 以 BGP 协议实时分发垃圾邮件黑名单与白名单：黑名单社区属性为 666、白名单为 42，运营于私有自治系统 AS65066，并以 OpenBGPD 为基础。（BSD Now EP1，[4554.19-4919.96]，L1）
- FreeBSD 基金会 2013 年春季筹款募集 219806 美元，来自 12 家企业与 365 名个人捐赠者；为维持 501(c)(3) 免税地位，个体小额捐赠被视为关键支撑。（BSD Now EP1，[1879.13-1939.54]，L2）
- DragonFly BSD Digest 的起源由当事人自述：2003 年 Matt Dillon 自 FreeBSD 4 分叉出 DragonFly 时他注意到项目启动，想贡献却不愿以写 C 为业，而 BSD 项目几乎所有互动都在邮件列表上进行，遂决定做一份摘编网站替人筛选要闻；他先默默试运行约一周确认能坚持，再公开宣布，至访谈时已持续约五年。（BSDTalk EP169，[91.60-158.72]，L1）
- Digest 之外的社区建设包括：将 FreeBSD Handbook 转换为 DragonFly 版并自 SGML 体系迁移至今日的 wiki、搭建 DragonFly 网站的邮件列表存档、推动 wiki 与主站整合；计划次年为 DragonFly 设立非营利法人，以摆脱互联网散兵游勇状态——法人实体便于美国捐赠者移交硬件、也能提供章程焦点。他盛赞 FreeBSD Foundation 的示范：送开发者赴会、推动项目完成，年度 30 万美元募款目标接近达成。关于社区健康度，他坦承 DragonFly 仍然很小，愿意做操作系统的人数增长远不及互联网，热点在 Twitter、WordPress 式应用开发；DragonFly 的吸引力恰在人少而无既有结构，可以说事情可以这样办、没有必须沿袭的包袱，代价是谁发声谁干活。（BSDTalk EP169，[158.72-402.22]，L1）
- 他长期以 DragonFly 自用：Digest 网站本身运行于 DragonFly 机器多年；系统应用以 pkgsrc 安装，pkgsrc 对频繁升级不友好但可忍受；他在 packagebox.dragonflybsd.org 上对 pkgsrc 季度发布做约 8000 个包的 bulk build，实测这是给文件系统施压的极好方式，该机器当前即运行 HAMMER 文件系统，尽管他个人并未在其他场合使用 HAMMER。（BSDTalk EP169，[402.22-476.42]，L1）
- 他对 BSD 哲学的被吸引点做了非宗教式表述：1998 至 1999 年在旧东家因同事偶语而装上 FreeBSD 4 尝试，相较 Linux，吸引他的不是许可证立场，而是一种以质量为本的做事方式——写代码因为它是该做的对事、是高质量的做法，而非软件必须自由的信仰宣示；他认为这种 quality-based 的取向让工作本身更有趣。（BSDTalk EP169，[493.30-573.38]，L1）
- Digest 的编辑理念被他上升为氧气论：一个操作系统需要其周围的气氛，胜过其他一切。主流科技博客以轻快语调追逐硬件与游戏，不追问计算机史从何而来、BSD 为何重要；而每个计算机系三年级学生都能写一个操作系统，写完却会发现无事可做，因为操作系统真正需要的是周边生态与身份氛围。他引述某个他记不清归属者的说法，认为 FreeBSD Diary、BSD Talk 与 Digest 的工作正是定义“说自己是 BSD 用户意味着什么”，这也是 advocacy 的实质。（BSDTalk EP169，[573.38-789.40]，L1）
- 关于志愿项目的维持机制，他将 BSD 项目与其他全志愿非营利事业（教育、食物、住所）视为同构：发不出工资，奖赏只能是公开庆祝成就——提交日志无人翻检，必须有人明说这块硬件能用了多亏某人，哪怕回报只是日后会议上一杯致谢的酒。会议被他视为提交活动的催化剂：会议数量增长是生态健康迹象，每次会议后都有活动爆发，第 25 届混沌通信大会收官当天 Simon Schubert 即因与会交流而向 DragonFly 集中提交；面对面接触带来的即时反馈远胜邮件。（BSDTalk EP169，[794.44-1008.94]，L1）
- Neville-Neil 自述创刊缘起：大约一年前他意识到其他开源操作系统都有 plenty 的期刊杂志，而当时全部 BSD 共用一份刊物、更没有专属 FreeBSD 的杂志，于是决定筹办；他此前十年参与 ACM Queue 杂志的经验使出版流程可行，经数月与 FreeBSD Foundation 的合作开发并组建编辑部，杂志定于 2014 年 1 月底面世。（BSDTalk EP237，[68.82-115.72]，L1）
- 编辑委员会按字母序包括 John Baldwin、Daichi Goto、Joseph Kong、Drew Levine、Michael Lucas、Kirk McKusick、Hiroki Sato 与 Robert Watson，覆盖内核、网络安全、出版与基金会等面向；编辑会的职能是主动发掘内容——开发者提交代码后通常不会想到写文章，编辑会负责找到做出有趣工作的人、请他们动笔，再由职业编辑把“信封背面”式的草稿变成可读的正式文章。（BSDTalk EP237，[141.44-278.96]，L1）
- 2014 年全年六期均设主题，继 FreeBSD 10 专号之后依次为网络、虚拟化、开发工具与新硬件特性；创刊号即 FreeBSD 10 专辑：David Chisnall 论成为 10 默认编译套件的 Clang 与 LLVM、Allan Jude 论源自 Solaris 与 illumos 而在 FreeBSD 被采纳扩展的 ZFS、一篇在 BeagleBone Black 上运行 FreeBSD 的入门文章呼应 ARM 热潮、John Baldwin 的内核向文章讲如何实现 sysctl 节点、另有 Joseph Kong 与重度 FreeBSD 用户 NYI 合写的托管服务部署白皮书；常设专栏包括发布工程师 Glenn Barber 的 SVN Update、Thomas Abthorpe 的 Ports Report 与 Drew Levine 的活动日历加“BSD 历史上的今天”。（BSDTalk EP237，[1125.94-1326.38]，L1）
- 发行走纯电子路线：应用本身免费、内容订阅制，全年六期 19.99 美元、单期 6.99 美元，双月刊一次下载；应用内置链接可直接跳转 diff 或外部网页，且内容离线可用——地铁隧道与航班上仍可阅读；应用商店代管分发并抽成，但免去了传统杂志“印刷多少卖不掉就销毁多少”的重负，Neville-Neil 认为这正是大型杂志纷纷转向电子发行的原因。（BSDTalk EP237，[391.66-543.34]，L1）
- 资金安排上 FreeBSD Journal 由 FreeBSD Foundation 出资承担首年出版成本，这是一笔不菲的投入，向基金会董事会立项时的前提就是必须以一年为期检验成败；预期靠订阅与广告收回成本，目标仅是收支平衡以维持为社区持续产出高质量刊物，首批已有若干广告主签约整年；他预计订阅基础要经数期积累，而非一期爆红。（BSDTalk EP237，[937.54-981.44]，L1）
- 生产流程上投稿几乎不限格式、偏好纯文本加随意画的图，交由合作的专业出版商 S&W Publishing 编辑排版，成稿经编辑返回作者确认的数轮往返；平台方面短期内只覆盖 Apple、Google 与 Amazon Kindle 三家应用商店，头六个月不计划做 FreeBSD 本机的阅读应用；应用内不可打印，但将为亚洲 BSDCon、BSDCan、EuroBSDCon 等会议制作限量印刷版，甚至设想由编辑部签名拍卖。（BSDTalk EP237，[828.84-1098.90]，L1）

**史料**：

- 本期核心史料为 hemradio.mi 的 FreeBSD 历史综述文章与 Tom Jones 的 VPP 移植技术文章；后者为当事人一手工程记录。（BSD Now EP566，[367.60-589.20]，L2）
- Peter N. M. Hansteen 博客《18 years of grey trapping》及历年陷阱数据文件。（BSD Now EP648，[257.02-1152.28]，L1）
- FreeBSD Foundation 由 Deb Goodkin 署名的年度募款文章 Powering the Future of BSD。（BSD Now EP648，[103.42-208.70]，L2）
- BSDCan 2026 组织委员会 Pat、Peter、Michael 访谈。（BSD Now EP648，[1226.50-2782.18]，L1）
- FreeBSD Foundation 2019 年度影响报告。（BSD Now EP333，[73.4-103.4]，L2）[订正：原 [69.24-90.64]，2026-09-30 SenseAudio 重转核对]
- Theo de Raadt 访谈视频（Tom Smythe 录制，2019 年 Ottawa hackathon 与 BSDCan 之间）。（BSD Now EP333，[1554.2-1626.5]，L2）[订正：原 [1554.58-1616.68]，2026-09-30 SenseAudio 重转核对]
- multicians.org 的 Multics 历史站点与《The Design of the UNIX Operating System》读书笔记。（BSD Now EP333，[1703.8-1897.8]，L3）[订正：原 [1801.42-1895.64]，2026-09-30 SenseAudio 重转核对]
- McKusick 提及 FAST 大会关于文件系统三十年演进的 keynote、BSDCan 2018 的采访背景，以及 CSRG 重写 AT&T 程序时 Keith Bostic 主张将署名归于他人以自保的细节。（BSD Now EP278，[339.18-390.46]，L1）
- McKusick 提及 TeachBSD 项目，主张以真实操作系统而非玩具系统教授计算机科学，并认为 DTrace/DWatch 等工具是“玻璃制”可观测系统的重要组成部分。（BSD Now EP278，[2723.00-2781.38]，L1）
- 基金会更新提及 OpenSSL 基础版本由 1.0.2 升级至 1.1.1 长期支持版，以及为 12.0 清理内核 bug 报告、修复 Unix 域套接字与 ZFS 回归的进展。（BSD Now EP269，[131.20-822.54]，L2）[订正：原 [721.88-822.54]，2026-09-30 SenseAudio 重转核对]
- 提及 Doug Engelbart 1968 年“所有演示之母”五十周年，以及 EuroBSDCon 2018 在布加勒斯特举行的游记与 Kamil Rytarowski 的 NetBSD sanitizers 演讲。（BSD Now EP269，[1889.60-3400.80]，L2）[订正：原 [2603.40-2648.68]，2026-09-30 SenseAudio 重转核对]
- 一手史料：FreeBSD 基金会 2018 年 7 月通讯（官方文本）；HardenedBSD.org 关于基金会组建的公告；openbsd-tech 邮件中 Philip Guenther 与 Brian Steele 的推测执行缓解提交说明。（BSD Now EP258，[3532.28-3667.74]，L1）[订正：原 Philippe Gontier，2026-09-30 SenseAudio 重转核对]
- 二手史料：NetBSD 博客的 Google Summer of Code libfuzzer 集成报告（第二部分），对 expr、zsh、file、ping 等用户态程序进行模糊测试。（BSD Now EP258，[3732.42-3797.80]，L2）
- BSDCan 2017 网站与演讲幻灯片；Michael Geist 主旨演讲；FreeBSD 基金会 co-op 计划博客。（BSD Now EP198，[4152.78-573.74]，L2）
- FreeBSD Quarterly Status Report（2017 年第一季度，官网发布）（BSD Now EP194，[67.52-222.56]，L1）
- Colin Percival 于 daemonology.net 发表的开源软件维护方案博客原文（BSD Now EP194，[872.66-1467.2]，L1）
- Chris Siebenmann（University of Toronto）关于 BSD 目录组继承语义的考据博客（BSD Now EP194，[2332.28-2964.74]，L1）
- OpenBSD changes of note 621（tedu 发布的变更综述）（BSD Now EP194，[1925.44-2332.28]，L1）
- OpenBSD OpenSSH 删除 SSHv1 代码的提交记录（BSD Now EP192，[65.54-183.18]，L1）
- FreeBSD Foundation 2017 年 4 月开发者更新（BSD Now EP192，[210.02-300.24]，L1）
- Patrick M. Hausen 访谈自述（BSD Now EP192，[1066.4-2279.84]，L1）
- Rick Macklem 的 pNFS call for testing 邮件（BSD Now EP192，[5241.34-5535.38]，L1）
- NetBSD GSoC wiki 项目列表（BSD Now EP189，[670.66-741.64]，L1）
- FreeBSD GSoC 项目列表（BSD Now EP189，[585.22-667.7]，L1）
- Wendell 访谈自述（BSD Now EP189，[4340.92-6064.62]，L1）
- Ted Unangst 的 YubiKey 使用博客（BSD Now EP189，[6182.44-6225.48]，L1）
- Rhonda Hauben 撰写的 Unix 管道历史文章，引用 Doug McIlroy、Dennis Ritchie 与 Ken Thompson 的记述，主持人逐段转述。（BSD Now EP166，[233.7-422.96]，L2）
- NCC Group 开源的 TriforceAFL 与 flashrd 工具链（GitHub 仓库），用于 OpenBSD 系统调用模糊测试。（BSD Now EP166，[122.62-224.46]，L2）
- Mark Schilder 关于在 FreeBSD 上加速 MySQL 导入的博客文章，列出 InnoDB 与 ZFS 调优清单。（BSD Now EP166，[566.72-1010.56]，L2）
- Keith Burnett 的 OpenBSD 6.0 笔记本安装教程（ThinkPad X60 上配置 XFCE、doas 与 USB 挂载）。（BSD Now EP166，[1802.96-1947.44]，L2）
- 本期新闻与访谈段落提及的一手史料：Colin Percival 论 opinionated workarounds 的博文（只在需要的系统上打补丁并大声报错）；Andrew Tanenbaum 复盘 Minix 三十年经验的视频报道（324-390 秒）；NetBSD 官方安全公告（calendar(1) 以 root 执行外部命令前未剥离特权，波及几乎所有历史版本）；OpenBSD pledge 多语言绑定仓库（node、Python、Rust、Go、Lua、Erlang、Nim 等）；Michael W. Lucas《FreeBSD Mastery: Advanced ZFS》出版信息；PGCon 2016（渥太华）、EuroBSDCon 2016（贝尔格莱德）、pkgsrcCon 2016（克拉科夫）征稿公告；FreeBSD wiki 的 ARM 交叉编译指南；AsiaBSDCon 2016 现场三小时文档与翻译教程，成果为将 LeapSeconds 一文译入日语（2663-2805 秒）。（BSD Now EP138，[3326.48-4582.82]，L2）
- Mark Phillips 访谈（2025 年 7 月柏林 Hackathon 现场）。（BSD Now EP622，[66.14-3216.34]，L1）
- FreeBSD Foundation 关于页面与 YouTube 频道内容。（BSD Now EP622，[2688.00-2695.60]，L2）
- 本期为 FreeBSD 基金会执行董事 Deb Goodkin 与早期创始人 Justin Gibbs 的口述访谈，属当事人一手自述；访谈提及早期商标转让与基金会自筹资金的历史细节。　[存疑脚注] 转写将商标原持有人写作 Gwyn River，疑为 Walnut Creek 的语音识别讹误，须以基金会档案核实。（BSD Now EP616，[420.22-528.70]，L1）
- FreeBSD 2014 年第三季度状态报告（7—9 月）所载一手进展：core team 报告含 git.freebsd.org 提升为官方服务、与 Foundation 协商取得 ZenForo 论坛软件许可、与 Oracle 谈成 Java 7/8 官方支持（开放 OpenJDK 代码双向流动并提供 TCK 测试框架签署认证）、在贡献者与 committer 之间居中调解；UEFI 状态报告确认 10.1 采用常规镜像加单独 UEFI 镜像、11 快照为混合镜像、boot1.efi 的 ZFS 驱动列为待实现、作者笔记本在 Optimus 独显模式下 UEFI 无法定位显卡的调试案例；VT 控制台驱动补齐 vidcontrol 特性、CJK 字体进行中并在 11 默认启用；John-Mark Gurney 向 OpenCrypto 框架加入 AES-GCM 与 AES-CTR 模式；Chelsio T4/T5 网卡的 iSCSI offload 以硬件无关方式同时支持 target 与 initiator，并实现 VMware VAAI 与 Hyper-V ODX 加速（write same、extended copy、unmap 空间回收，相当于 Zvol 的 trim 支持）；Debian/kFreeBSD 状态报告称其工作过程发现了两个月前安全公告中的内核 bug；PXE 自动化安装为 GSoC 项目，bsdinstall 增加按 MAC 地址取配置的脚本化能力；另有 ARM 板卡与 ARM64 的 LLDB 调试器移植。（BSD Now EP59，[580.29-1284.73]，L2）
- Foundation 季度更新的一手清单：资助 Postgres 性能优化、AutoFS 自动挂载器、iSCSI 系列工作与 Ed Maste 的 UEFI/VT 项目——主持人点评这些久拖不决的项目“因无人想做”而由基金会出资促成；Secure Boot 方案已定待执行；购置硬件强化 New York Internet 与 Sentex 共置机房，前者成为加州全部内容的完整镜像；宣布与 Cavium 合作支持 ARMv8 服务器；赞助 Robert Watson 组织剑桥开发者峰会、资助开发者组织阿根廷 BSD Day、以金牌赞助身份出席 EuroBSDCon 2014 并在该会募得逾 2000 美元捐款；Kirk McKusick、Robert Watson 与 George Neville-Neil 合著的《The Design and Implementation of the FreeBSD Operating System》由基金会出版，McKusick 在 EuroBSDCon 的 ZFS 报告之外另授两日 FreeBSD 内核教程。（BSD Now EP59，[1148.02-1274.02]，L2）
- Peter Wemm 访谈（FreeBSD.org 集群管理员当事人自述）。（BSD Now EP56，[226.16-2846.68]，L1）
- Eric LeBlanc 访谈（Xinuos 董事长兼 CEO 当事人自述）。（BSD Now EP51，[992.22-1870.22]，L1）
- 本期史料包括 Ted Unangst 访谈（当事人自述）、OpenBSD signify 工具与测试密钥、FreeBSD Foundation 2013 年筹款报告、NTP 教程及 OpenBSD BeagleBone Black 移植博客。（BSD Now EP23，[61.30-3246.40]，L1） [订正：原 [713.64-1387.66]，2026-09-30 SenseAudio 重转核对]
- 当事人 Glen Barber 自述约 2007 年以爱好者身份接触 FreeBSD，2010 年获 commit bit，先后加入文档工程、集群管理与发行工程团队；其参与发行工程的起点是为解决快照缺失问题。（BSD Now EP2，[2101.06-2165.46]，L1）
- 该期提及 OpenBSD 通过预售与销售 CD 套装筹集开发资金，并随每次发布推出歌曲与包装设计。（BSD Now EP2，[480.02-515.68]，L2）
- 当事人 Peter Hessler 自述其为 OpenBSD 用户与开发者：2000 年起使用、2008 年起成为开发者，早期从事 ports 移植，后加入 Vantronics 从事 OpenBSD 防火墙与路由器相关工作，并曾运行约 50 个路由域。（BSD Now EP1，[2946.18-3109.14]，L1）
- 当事人自述其 BGP SpamD 聚合阿尔伯塔大学与《The Book of PF》作者 Peter Hanstein 的 SpamD 黑名单，并以 24 小时内命中蜜罐邮箱地址作为黑名单收录口径。（BSD Now EP1，[3984.50-4100.90]，L1）

**史观**：

- 总纲10 动手者创造历史：Tom Jones 以受资助的工程工作完成 VPP 移植并推动上游改进，体现动手者通过具体技术贡献塑造系统生态。（BSD Now EP566，[1513.74-1930.24]，L1）
- 总纲13 法律与道德是利益分配：VPP 移植由基金会与商业公司共同出资，显示开源工程背后持续存在的资金与利益安排。（BSD Now EP566，[1557.02-1567.42]，L1）
- 总纲10 动手者创造历史：Hansteen 以十八年持续运维累积的灰度陷阱数据，记录的是不被聚光灯照到的反垃圾邮件一线工作。（BSD Now EP648，[257.02-1152.28]，L1）
- 总纲4 分离聚合是永恒规律：BSDCan 领导权在代际之间交接、规划委员会持续吸纳新人，体现社区组织的聚合与再分配。（BSD Now EP648，[1382.64-1467.34]，L1）
- 总纲9 经验优先：Siebenmann 从自身运维规则集与工具链出发评估防火墙迁移，而非依赖抽象性能宣传。（BSD Now EP648，[3368.44-3441.68]，L1）
- 总纲10 动手者创造历史：FreeBSD Foundation 报告将捐款落到 Wi-Fi 支持、安全响应等具体工程，而非口号。（BSD Now EP333，[131.1-155.6]，L2）[订正：原 [136.72-161.1]，2026-09-30 SenseAudio 重转核对]
- 总纲9 经验优先：multicians.org 以当事人回忆与一手技术文档保存 Multics 经验，体现经验优先。（BSD Now EP333，[1822.2-1882.2]，L2）[订正：原 [1837.68-1883.14]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：McKusick 强调软件与项目的持续“养护”远非社区驱动项目所长，人们倾向做新奇有趣之事；文档与基础设施的默默维护恰是系统得以存活的关键。（BSD Now EP278，[451.46-489.68]，L1）
- 总纲3 不存在进步，只有权力再分配：McKusick 指出历史上 IBM、微软各自占据过绝对支配地位又相继让位，Linux 今日的支配地位同样不会永远持续，FreeBSD 甘居雷达之下反而得以延续。（BSD Now EP278，[2247.34-2342.26]，L1）
- 总纲5 没有必然性，只有偶然性：McKusick 以“容器发明于 FreeBSD 却成功于他处”为例，指出技术领先与市场成功之间并无必然因果，成功更多依赖偶然的产品化时机。（BSD Now EP278，[2596.78-2625.54]，L1）
- 总纲4 分离聚合是永恒规律：DTrace 从 Solaris 发明、经 FreeBSD 移植、再由微软带入 Windows，追踪工具的跨系统传承显示技术思想的流动并不以许可证或阵营为边界。（BSD Now EP269，[3441.20-3510.40]，L2）
- 总纲10 动手者创造历史：波兰 BSD 用户组以“先做起来、控制在十五分钟演讲、保持低成本”的方式维系社区，说明地方社区依靠组织者的持续投入而非宏大规划得以存续。（BSD Now EP269，[3019.68-3177.30]，L2）
- 总纲10 动手者创造历史：基金会以受雇工程师和会议赞助支持实际写代码与发布的人，捐赠最终落到动手者手中。（BSD Now EP258，[321.10-419.90]，L1）[订正：原 [323.00-412.50]，2026-09-30 SenseAudio 重转核对]
- 总纲13 法律与道德是利益分配：HardenedBSD 基金会申请 501c3 免税地位、设置董事与顾问，是把社区劳动组织化并纳入法律利益分配框架的过程。（BSD Now EP258，[3394.50-3523.30]，L2）[订正：原 [3399.98-3523.30]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：会议通过 hallway track、工作进展分享与拍卖等非正式互动促成协作，社区的推进依赖动手者聚集与偶然交流，而非仅靠正式议程。（BSD Now EP198，[4352.30-5412.26]，L2）
- 总纲10 动手者创造历史：状态报告显示基金会资助与普通提交者的日常维护共同推进系统细节，历史由大量默默动手者累积而成。（BSD Now EP194，[98.3-164.34]，L2）
- 总纲13 法律与道德是利益分配：开源维护资助之争的实质是贡献者劳动如何获得回报的利益分配问题，而非单纯的技术或道德问题。（BSD Now EP194，[907.04-1249.4]，L2）
- 总纲5 没有必然性，只有偶然性：BSD 目录组继承语义是 4.1cBSD 多组进程引入时的偶然工程选择，随后沉淀为传统，并非预先设计的必然。（BSD Now EP194，[2486.68-2686.36]，L2）
- 总纲10 动手者创造历史：Patrick Hausen 从组装 PC、接触 Xenix 到部署 FreeBSD 的历程表明，历史由持续动手运维的人塑造。（BSD Now EP192，[1068.62-1274.52]，L1）
- 总纲9 经验优先：主持人与其访谈对象依据长期实际部署经验判断 BSD 相对 Linux 的稳定性与文档质量，经验先于抽象理论。（BSD Now EP192，[1425.04-1488.94]，L1）
- 总纲4 分离聚合是永恒规律：pNFS 把单一 NFS 服务拆分为元数据节点与数据节点，再聚合为统一文件系统，体现分离聚合的循环。（BSD Now EP192，[5241.34-5535.38]，L2）
- 总纲10 动手者创造历史：受访者以退役硬件自建存储系统并迁移海量文件，历史由动手实践者推动。（BSD Now EP189，[4702.86-5620.86]，L1）
- 总纲9 经验优先：对 ZFS 健壮性的判断来自亲身数据恢复与迁移经历，经验先于宣传。（BSD Now EP189，[4462.78-4558.02]，L1）
- 总纲12 科学是形式主义：存储性能与可靠性认知源于可复现的实验、工具与度量，而非主观印象。（BSD Now EP189，[5085.26-5282.2]，L1）
- 总纲5 没有必然性，只有偶然性：管道从 1969 年提议到 1972 年实现，其间经历了被质疑“缺乏想象”的搁置，具体技术路径由当时的人与偶然条件决定，而非线性必然。（BSD Now EP166，[233.7-308.86]，L3）
- 总纲9 经验优先：McIlroy 以“简单管线连接程序与数据”的经验表述总结工程实践，Unix 的哲学原则从具体动手经验中凝结而成。（BSD Now EP166，[398.14-414.98]，L3）
- 总纲1 一切真历史都是古代史：主持人感叹管道今日被当作理所当然，而忽略其曾有“没有管道的时代”，历史书写把建构产物自然化为恒常存在。（BSD Now EP166，[239.06-247.66]，L3）
- 总纲4 分离聚合是永恒规律：Adhoku 以 jail 做应用级分离、以反向代理做流量聚合，呈现分离与聚合的交替结构，而非单一集中或单一分散。（BSD Now EP166，[1636.04-1775.64]，L3）
- 总纲10 动手者创造历史：MySQL 与 ZFS 的优化均来自动手部署者的具体记录，性能改进由实际操作者而非抽象方案推动。（BSD Now EP166，[566.72-1010.56]，L3）
- 总纲10 动手者创造历史：“我是文档人”的自谦与“源码提交者已经够多”的回应，使这次董事补选成为对何种劳动被计入治理的再定义：文档、翻译、法务、布道与组织工作在基金会层面获得与内核开发同等的代表权——书写 BSD 史时，维持项目运转的动手者与提交代码的动手者同为历史的创造者（1664-1688 秒）。（BSD Now EP138，[1659.1-1689.1]，L1）[订正：原 [1664.16-1687.68]，2026-09-30 SenseAudio 重转核对]
- 总纲1 一切真历史都是古代史：calendar(1) 漏洞是“古代制度活在当代”的活标本：主持人的解释是，该工具为全校共用一台主机、每人维护日历文件的时代而设计，以 root 身份遍历所有用户日历并邮寄提醒在当时合理；2016 年它仍以 root 日任务存续，特权未剥离的旧设计在新语境中变成提权漏洞——理解这一漏洞必须回到其诞生的分时主机时代而非仅看当代代码（3666-3696 秒）。（BSD Now EP138，[3660.0-3711.6]，L2）[订正：原 [3666.52-3695.82]，2026-09-30 SenseAudio 重转核对]
- 总纲15 文化即形式主义：Mark Phillips 把营销还原为讲故事的形式，提示技术传播中的品牌叙事同样是形式化构造。（BSD Now EP622，[2702.70-2727.46]，L1）
- 总纲10 动手者创造历史：他以工程师背景亲手测试 ZFS 根镜像并反馈给 Colin Percival，体现使用者参与塑造云镜像。（BSD Now EP622，[1215.20-1244.40]，L1）
- 总纲9 经验优先：其讲故事方法论基于多年创业与营销一线经验，而非抽象理论推演。（BSD Now EP622，[2553.94-2822.94]，L1）
- 总纲10 动手者创造历史：Justin Gibbs 自述大学二年级即因 FreeBSD 社区的信任而获得为大型 FTP 站点编写设备驱动的机会，体现技术史中默默动手者借社区空间成长的路径。（BSD Now EP616，[2482.00-2531.14]，L1）
- 总纲3 不存在进步，只有权力再分配：基金会与 core team 在技术方向上的权责随选举制与职业化进程持续再分配，呈现治理权力的流动与重新配置，而非线性进步叙事。（BSD Now EP616，[1876.88-1997.64]，L1）
- 总纲20 历史地理塑造思想土壤：日本 BSD 社区轨迹的地域性：PC-98 这一日本特有硬件生态决定了斋藤只能在 FreeBSD 与 Linux 的本地移植中择路；语言与文化边界使技术上占优的日本补丁因拒绝进入英文邮件列表的讨论形式而被系统性忽略，进而引发整个开发者群体向 NetBSD 的迁移。硬件土壤与沟通文化共同塑造了日本 BSD 版图从 FreeBSD 倾向转为 NetBSD 倾向的历史路径，而非任何技术必然性。（BSD Now EP59，[2227.32-2483.87]，L1）
- 总纲7 理论必须自反：Peter Wemm 反复以事故教训反观并修正基础设施设计，而非固守既有运维惯例。（BSD Now EP56，[1982.06-2022.30]，L1）
- 总纲5 没有必然性，只有偶然性：2012 年事件由跳板主机、共享 NFS home 与可写 authorized_keys 等偶然叠加而成，并非必然发生。（BSD Now EP56，[2112.8-2192.90]，L1）[订正：原 [2102.38-2192.90]，2026-09-30 SenseAudio 重转核对]
- 总纲10 动手者创造历史：集群由 Peter Wemm、Glen Barber、Sean Bruno 等动手维护者在长周期中持续改造。（BSD Now EP56，[666.00-748.68]，L1）
- 总纲13 法律与道德是利益分配：Xinuos 选择 BSD 许可证的本质是转售商与专有业务利益的分配安排。（BSD Now EP51，[1163.86-1179.76]，L1）
- 总纲3 不存在进步，只有权力再分配：Xinuos 由专有 System V 转向参与 FreeBSD，是商业权力格局的再分配而非线性技术进步。（BSD Now EP51，[1014.92-1128.06]，L1）
- 总纲11 商品是形式主义：访谈将操作系统视为可支持、可转售的商品，并以支持周期与许可证作为商品属性展开叙述。（BSD Now EP51，[1322.60-1363.72]，L1）
- 总纲10 动手者创造历史：Ted Unangst、Marc Espie 与 Alexander Hall 以具体工具开发补齐 OpenBSD 发布签名空白。（BSD Now EP23，[949.00-991.80]，L1） [订正：原 [949.00-1006.76]，2026-09-30 SenseAudio 重转核对]
- 总纲5 没有必然性，只有偶然性：Theo 的一封邮件触发 signify 开发，当事人明确不知动机，说明安全工程由具体事件偶然推动。（BSD Now EP23，[1615.30-1651.60]，L1）
- 总纲22 知识注定过时：signify 以极简设计替代 GPG 的部分用途，体现工具随需求演进而更替。（BSD Now EP23，[898.44-930.08]，L1）
- 总纲9 经验优先：发行工程对稳定分支宁可关闭新特性也不愿引入回归，体现以既有用户升级经验为优先的保守取向，而非功能扩张优先的进步叙事。（BSD Now EP2，[3189.04-3237.52]，L1）
- 总纲13 法律与道德是利益分配：GCC 退出基本系统与 BIND 替换是许可证与维护成本共同驱动的工具替换，属利益与负担在工具链层面的重新分配。（BSD Now EP2，[543.86-645.78]，L2）
- 总纲4 分离聚合是永恒规律：Poudriere 以 jail 将单一构建任务分离为按版本、架构与选项隔离的并发构建，并以增量重建聚合为统一二进制仓库，是分离与聚合的工程实践。（BSD Now EP2，[865.40-1801.56]，L2）
- 总纲4 分离聚合是永恒规律：BGP SpamD 将阿尔伯塔大学与 Peter Hanstein 各自维护的黑名单聚合为统一的 BGP 分发列表，以本地复制取代中心网站下载与实时 DNS 查询，是分散源向聚合结构流转的具体实践。（BSD Now EP1，[4411.69-4474.51]，L1）
- 总纲8 本体论上各方平等：该期将 FreeBSD 图形驱动、OpenBSD BGP SpamD、NetBSD 6.1.1 等并列报道，未以单一分支为中心，呈现多方平等的叙事格局。（BSD Now EP1，[0.00-125.02]，L2）
- 总纲10 动手者创造历史：BGP SpamD 由 Peter Hessler 个人搭建并维护，访谈记录的是具体动手者对垃圾邮件防御工具的工程选择，而非抽象的项目叙事。（BSD Now EP1，[2946.18-3109.14]，L1）
- 总纲10 动手者创造历史：Digest 的五年自身即是历史由默默动手者写就的例证：一个不愿以写 C 为业、白天在墨盒制造厂维护老旧 Debian 系统的普通人，以每日筛读邮件列表、转换手册、搭建存档的琐碎劳动，为一个分叉项目保住了公共记忆与氧气。操作系统的存续不只在提交日志里，也在这些无名整理者的持续劳作中。（BSDTalk EP169，[91.60-158.72]，L1）
- 总纲10 动手者创造历史：Neville-Neil 说 FreeBSD 一贯吸引他的，是这里的人既能开发软件、也能在纸上解释自己做了什么——这是科学与工程常被忽略的另一半；但开发者提交代码后并不会自发地书写，于是需要编辑委员会去主动发现动手者、需要职业编辑把草稿转成可读文本。动手者创造了系统，而把这份工作写成历史性记录，需要专门的转译机制。（BSDTalk EP237，[597.56-613.70]，L1）

**辨析**：

- 综述文章对 FreeBSD 各版本与特性年份的归属存在简化乃至偏差，例如将 APT 误作 FreeBSD 包工具，具体里程碑须以官方发布说明核实。　[存疑脚注] 综述文章的版本与特性对应关系存在简化或偏差，未经官方发布说明逐项核实。（BSD Now EP566，[468.76-493.60]，L4）
- 转录将 Peter N. M. Hansteen 误记为 Peter N.M. Hanstein，且陷阱总数 17,8238 的数字断词存疑，须对照原文与数据文件。　[存疑脚注] 人名与统计数字存在语音转写歧义，须以原文与数据文件核验（BSD Now EP648，[997.58-1005.20]，L4）
- Theo de Raadt 访谈为第三方转述与视频链接，其具体言论需回看原视频核验。　[存疑脚注] 访谈内容未在转写中完整呈现（BSD Now EP333，[1576.5-1626.5]，L4）[订正：原 [1577.94-1616.68]，2026-09-30 SenseAudio 重转核对]
- McKusick 关于“文档 committer 与源码 committer 同等投票”的叙述属当事人视角，须与 FreeBSD 选举规则文件与历届 core 名单交叉核验；其对自己“不再关键”的自评也属谦辞。　[存疑脚注] 选举资格细节须以 FreeBSD Core Team 规则文件核实。（BSD Now EP278，[533.12-611.68]，L3）
- McKusick 提及的研究（MIT 与法国高校基于 commit log 分析领导层）未给出具体出处，其“只有 Apache 与 FreeBSD 等少数项目完成多次更替”的结论需核对原始研究。　[存疑脚注] 所援引研究未具名，结论无法直接追溯。（BSD Now EP278，[725.94-799.70]，L4）
- 主持人称微软的 DTrace 移植“未从 illumos 上游起步而是自 FreeBSD 版本开始”，此谱系判断须以微软官方实现与代码署名核实。　[存疑脚注] DTrace Windows 移植的具体代码来源未经一手仓库核对。（BSD Now EP269，[3451.40-3460.96]，L4）
- [存疑脚注] HardenedBSD 基金会预计年底前获批 501c3 系公告中的预期表述而非既成事实，须以其后续公告核实实际获批时间。　[存疑脚注] 501c3 获批时间为预期而非既成事实。（BSD Now EP258，[3506.20-3524.90]，L4）[订正：原 [3506.99-3515.60]，2026-09-30 SenseAudio 重转核对]
- [考据脚注] 基金会通讯中的支出与人员细目为选择性朗读，完整内容须与 FreeBSD 基金会年度报告及官方通讯原文核对。　[考据脚注] 支出细目须与基金会年度报告核对。（BSD Now EP258，[321.10-419.90]，L4）[订正：原 [315.56-412.50]，2026-09-30 SenseAudio 重转核对]
- [存疑脚注] Colin Percival 的开源资助方案当时仅为其个人提案，尚未落地实施，能否被社区采纳与商业化可行仍待验证。　[存疑脚注] 该方案属单一来源的个人设想，未形成实施记录。（BSD Now EP194，[1367.52-1440.28]，L4）
- [存疑脚注] Patrick Hausen 所忆 1994 年与 Jordan Hubbard 会面、Walnut Creek 光盘数量等细节系当事人多年后回忆，需与 Walnut Creek 档案交叉核验。　[存疑脚注] 当事人回忆性细节，缺乏独立一手档案印证。（BSD Now EP192，[1279.84-1320.66]，L4）
- [存疑脚注] GSoC 项目名单为 2017 年计划，最终是否全部完成须以后续项目报告为准。　[存疑脚注] 计划性名单，验收结果待后续报告。（BSD Now EP189，[585.22-733.18]，L4）
- [存疑脚注] 转写将管道历史中的参与者记作“Thompson and Kennedy”，疑为 Ritchie、Thompson 与 Rudd Canaday 的误转；管道提议与实现时间线须以 McIlroy 原文及 Unix 一手文献复核。　[存疑脚注] 人名与时间线须核验一手文献。（BSD Now EP166，[279.9-308.86]，L4）
- [存疑脚注] 转写将 Hauben 文章托管地记作“farther dot edu”，实际域名无法据此确认，引用时须核验文章来源。　[存疑脚注] 文章来源域名存疑。（BSD Now EP166，[417.88-422.96]，L4）
- 主持人在评述 Percival 博文时即兴将 OpenSSL Heartbleed 归因于“为个别系统的慢 malloc 自建内存管理层却全局启用”，以此反证“补丁只打在需要的系统上”的局部性原则；但此归因系主持人现场发挥而非博文原文，Heartbleed 的直接根因是心跳报文边界检查缺失，与自定义内存管理器的关系须经代码与事后审计多源核对，不可直接采信。　[存疑脚注] Heartbleed 与 OpenSSL 自定义内存管理层的因果链为主持人单源现场推断，节目未给出出处，属待验证命题。（BSD Now EP138，[3530.1-3596.6]，L4）[订正：原 [3534.72-3578.44]，2026-09-30 SenseAudio 重转核对]
- 受访者供职的达姆施塔特应用技术大学把 26 节点 Dell C6220 集群从 Ubuntu 渐进迁往 FreeBSD：以 bhyve 为教学虚拟机宿主、以 ZFS 快照回滚兜底学生 root 误操作、自写 shell 脚本把重装时长从 FI 全自动安装的 25 分钟压缩到约 10 分钟，是 2016 年 bhyve 与 ZFS 进入真实教学负载的自述个案；但其自承性能验证尚未完成，属单一当事人陈述，可作 bhyve 成熟度的孤证线索而非生态级结论。　[存疑脚注] 单源自述；“学生不会察觉运行于虚拟机”的性能判断未附数据，待其承诺的后续文章或演讲验证。（BSD Now EP138，[2437.2-2657.4]，L4）[订正：原 [2437.50-2649.70]，2026-09-30 SenseAudio 重转核对]
- 访谈为 Mark Phillips 单方自述，其职业时间线与 FreeBSD Foundation 任职细节为单一来源，关键节点须以基金会公告交叉验证。　[存疑脚注] 职业履历为当事人单一来源自述，未与其他公开资料交叉验证（BSD Now EP622，[407.42-944.24]，L4）
- 访谈中的预算（约 270 万至 290 万美元）与募资（约 550 万美元）数字为当事人口述的单一来源，须与基金会年度报告交叉核对。　[存疑脚注] 预算与募资金额为当事人口述，未经年报交叉验证。（BSD Now EP616，[570.70-586.06]，L4）
- commit 日志作为史料样本与媒体误读现象：本期新设邮件列表集锦段所引三例——Julian Assange 于 1990 年代中期致信 FreeBSD 邮件列表建议放弃 CVS（表明其曾是 FreeBSD 用户）；Ted Unangst 修复 head(1) 的提交日志戏称“修复 head 中严重的分布式拒绝服务”，被技术媒体当真演绎为 OpenBSD 出现严重漏洞；另一提交日志自述“修复 Bill Joy 于 1977 年 8 月 24 日引入、已存在于 1978 年 3 月 9 日 1BSD 发布中的 37 年老 bug，方式是合并 Keith Bostic 来自 4.4BSD 的 22 年前修复”。前者展示技术幽默在跨语境传播中的失真，后者则将 1BSD—4.4BSD—当代的代码谱系凝缩于一条提交日志，可作版本演化叙事的直接引证。（BSD Now EP59，[4501.43-4646.07]，L2）
- 2012 年事件中患者零号的初始入侵路径仅存候选推断，Peter Wemm 自述只有短名单而无确定结论。　[存疑脚注] 初始入侵路径未获确证，属当事人事后推断（BSD Now EP56，[2224.94-2233.42]，L4）
- Xinuos 与 SCO 的历史关联及其 UNIX 版权诉讼前史在本期仅被一带而过，其与 FreeBSD 关系的长期后果未在本期展开。　[存疑脚注] SCO 前史仅凭主持人转述与当事人简短开场，未经多源交叉核验（BSD Now EP51，[1015.90-1019.40]，L4）
- 当事人明确表示不知 Theo 启动签名项目的动机，且 5.5 正式签名密钥当时尚未生成；发行集签名覆盖范围（源集、ports tarball 是否签名）仍属待定。　[存疑脚注] 签名动机与最终覆盖范围以 OpenBSD 官方发布说明为准，需后续考据。（BSD Now EP23，[1312.30-1659.90]，L4） [订正：原 [1615.30-1651.60]，2026-09-30 SenseAudio 重转核对]
- FreeBSD 10.0 是否彻底移除 BIND、以及 resolv.conf 与 DHCP 切换的具体方案在本期仍属进行中的计划，须以 10.0 最终发布说明为准。　[存疑脚注] BIND 移除与解析配置迁移为当时未定稿规划，播客转述不等同于正式发布决策。（BSD Now EP2，[4181.74-4227.38]，L4）
- VeriSign 同时使用 BSD、Linux、Solaris 等操作系统作多样性冗余的说法为主持人转述，其根服务器内部各系统的具体比例未获官方资料核验。　[存疑脚注] VeriSign 各操作系统在根服务器中的具体占比属单一播客转述，须以官方资料交叉验证。（BSD Now EP1，[460.01-478.53]，L4）
- 转写误植须考订：Matt Bill 应为 Matt Dillon、grag-and-fly-vsd.org 应为 dragonflybsd.org、package source 应为 pkgsrc、a cabotette for humanity 应为 Habitat for Humanity、previous D-year 应为 FreeBSD；氧气说归属者转写为 Jordan Hubbard 或 John Louis Gasey，后者拼写无法确证，当事人自承记不清出处，Package Manager 这一 pkgsrc 图形工具的活动状态亦不明。[存疑脚注] 氧气名言的原始出处与精确措辞无从自转写确证，须以邮件列表与早期演讲存档复核。　[存疑脚注] 氧气说归属与措辞为单一来源模糊回忆，引用须先经外部文献核验。（BSDTalk EP169，[685.46-706.46]，L4）

**文献**：

- [BSD Now EP566] Pennington J. BSD Now: 566: Open Source Excellence[EB/OL]. (2024-07-04)[2026-08-15]. <https://www.bsdnow.tv/566>.
- [BSD Now EP648] Pennington J. BSD Now: 648: Greytrapping for years[EB/OL]. (2026-01-29)[2026-08-15]. <https://www.bsdnow.tv/648>.
- [BSD Now EP333] Pennington J. BSD Now: 333: Unix Keyboard Joy[EB/OL]. (2020-01-16)[2026-08-15]. <https://www.bsdnow.tv/333>.
- [BSD Now EP278] Pennington J. BSD Now: Episode 278: The Real McCoy | BSD Now 278[EB/OL]. (2018-12-27)[2026-08-15]. <https://www.bsdnow.tv/278>.
- [BSD Now EP269] Pennington J. BSD Now: Episode 269: Tiny Daemon Lib | BSD Now 269[EB/OL]. (2018-10-24)[2026-08-15]. <https://www.bsdnow.tv/269>.
- [BSD Now EP258] Pennington J. BSD Now: Episode 258: OS Foundations | BSD Now 258[EB/OL]. (2018-08-08)[2026-08-15]. <https://www.bsdnow.tv/258>.
- [BSD Now EP198] Pennington J. BSD Now: 198: BSDNorth or You can’t handle the libtruth[EB/OL]. (2017-06-14)[2026-08-15]. <https://www.bsdnow.tv/198>.
- [BSD Now EP194] Pennington J. BSD Now: 194: Daemonic plans[EB/OL]. (2017-05-17)[2026-08-15]. <https://www.bsdnow.tv/194>.
- [BSD Now EP192] Pennington J. BSD Now: 192: SSHv1 Be Gone[EB/OL]. (2017-05-03)[2026-08-15]. <https://www.bsdnow.tv/192>.
- [BSD Now EP189] Pennington J. BSD Now: 189: Codified Summer[EB/OL]. (2017-04-12)[2026-08-15]. <https://www.bsdnow.tv/189>.
- [BSD Now EP166] Pennington J. BSD Now: 166: Pass that UNIX Pipe[EB/OL]. (2016-11-02)[2026-08-15]. <https://www.bsdnow.tv/166>.
- [BSD Now EP138] Pennington J. BSD Now: 138: Rushing into BSD[EB/OL]. (2016-04-20)[2026-08-15]. <https://www.bsdnow.tv/138>.
- [BSD Now EP622] Pennington J. BSD Now: 622: Interview with Mark Phillips - Technical Marketing Manager at the FreeBSD Foundation[EB/OL]. (2025-07-31)[2026-08-15]. <https://www.bsdnow.tv/622>.
- [BSD Now EP616] Pennington J. BSD Now: 616: FreeBSD Foundation Interview[EB/OL]. (2025-06-19)[2026-08-15]. <https://www.bsdnow.tv/616>.
- [BSD Now EP59] Pennington J. BSD Now: 59: BSDって聞いたことある？[EB/OL]. (2014-10-15)[2026-08-15]. <https://www.bsdnow.tv/59>.
- [BSD Now EP56] Pennington J. BSD Now: 56: Beastly Infrastructure[EB/OL]. (2014-09-24)[2026-08-15]. <https://www.bsdnow.tv/56>.
- [BSD Now EP51] Pennington J. BSD Now: 51: Engineering Nginx[EB/OL]. (2014-08-20)[2026-08-15]. <https://www.bsdnow.tv/51>.
- [BSD Now EP23] Pennington J. BSD Now: 23: Time Signatures[EB/OL]. (2014-02-05)[2026-08-15]. <https://www.bsdnow.tv/23>.
- [BSD Now EP2] Pennington J. BSD Now: 2: Engineering and Powder Kegs[EB/OL]. (2013-09-11)[2026-08-15]. <https://www.bsdnow.tv/2>.
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. <https://www.bsdnow.tv/1>.
- [BSDTalk EP169] Backman W. BSDTalk: 169: bsdtalk169 - Justin Sherrill of the DragonFlyBSD Digest[EB/OL]. (2009-01-04)[2026-08-27]. <https://bsdtalk.blogspot.com/2009/01/bsdtalk169-justin-sherrill-of.html>.
- [BSDTalk EP237] Backman W. BSDTalk: 237: bsdtalk237 - The FreeBSD Journal with George Neville-Neil[EB/OL]. (2014-01-08)[2026-08-27]. <https://bsdtalk.blogspot.com/2014/01/bsdtalk237-freebsd-journal-with-george.html>.

<!-- /PODCAST_REVIEW -->
