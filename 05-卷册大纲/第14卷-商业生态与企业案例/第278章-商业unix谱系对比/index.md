---
chapter: 第 278 章
id: CH278
volume: 第14卷-商业生态与企业案例
---

# 第 278 章 商业unix谱系对比

## 要点

- **IBM** 的公开文档与收购记录是分析其商业策略的主要史料。
- **DEC**/**Compaq**/**HP** 的公开文档与 **EOL** 记录是追溯 **Tru64** 演变的主要史料。
- **SGI** 2009 年破产，**IRIX** 随之 **EOL**。破产记录与 **EOL** 公告是分析 **SGI** 终结的主要史料。
- **Sun** 的公开文档与 **Oracle** 2010 年收购记录是分析 **Sun** Unix 谱系的主要史料。
- **Oracle** 通过官方公告、**Solaris** 路线图文档阐述未来方向，但这些文档多被删除或归档后需依赖 `archive.org` 检索。

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10437] BSD Now 第 675 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10453] BSD Now 第 671 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10480] BSD Now 第 665 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10500] BSD Now 第 663 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10514] BSD Now 第 661 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10521] BSD Now 第 659 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10536] BSD Now 第 655 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10574] BSD Now 第 648 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10600] BSD Now 第 644 期，匹配 CH278 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10617] BSD Now 第 641 期，匹配 CH278 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- **DEC** 文档的获取难度较大，需依赖 `archive.org`
- **Oracle** 收购后 **Sun** 文档的获取需依赖 `archive.org`
- **Oracle** 路线图的变更时点难以精确还原，可从 **SEC** 文件与新闻稿交叉验证
- **SFU** 与 **Interix** 的版本对应关系可从 **Windows** 版本号核对
- **Google** 倾向 **Apache 2.0** 是否包含专利防御考量

## 文献

- IBM 10-K；SEC 文件［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- HP EOL 公告；archive.org DEC 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- SGI 破产文件；IRIX EOL 公告［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Oracle 收购公告；archive.org Sun 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Oracle 2018 10-K；archive.org Solaris 路线图快照［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Microsoft SFU 3.5 文档；archive.org MSDN 快照［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Google 2017 开源年度报告；GitHub License 统计 ［B］
- Percival 个人博客；AWS EC2 FreeBSD User Guide ［C］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 1978-2026 年间：1,294,851 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- opensource.fb.com；GitHub Meta 组织提交历史［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Cisco 2010 年代 10-K；archive.org Cisco 白皮书［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP51、BSD Now EP591（共 2 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Eric LeBlanc 自述 Xinuos 在约十八个月调研后选择 FreeBSD 作为新增支持的开源操作系统，理由包括与 OpenServer 相近的代码树、BSD 许可证及 FreeBSD Foundation 的存在。（BSD Now EP51，[1014.92-1082.10]，L1）
- Xinuos 以 BSD 许可证允许转售商与客户开发专有环境为关键考量，并计划对 FreeBSD 稳定分支提供最长十五年的支持与回溯移植。（BSD Now EP51，[1163.86-1335.46]，L1）
- Xinuos 计划将 OpenServer 与 UnixWare 等遗留应用运行于 bhyve 虚拟化之上，以迁移无源码的旧应用。（BSD Now EP51，[1465.72-1508.64]，L1）
- 主持人讨论 Apple 在 1990 年代中后期濒临破产的处境：旧版 Mac OS 的 Copland 项目曾缩减至约三名开发者，BeOS 虽被视作备选平台，但事后被评价为尚非稳定的 Unix 系统。（BSD Now EP591，[426.6-493.8]，L2）[订正：原 [429.12-479.48]，2026-10-01 SenseAudio 重转核对]
- 主持人认为 Apple 通过收购 NeXT 继承了 Mach 与 BSD 的既有成果，从而以较低成本获得 Unix 平台的稳定性；并由此讨论若 NeXT 独立成功或 Apple 破产，个人计算机与开源生态的历史可能完全改写。　[存疑脚注] Apple 收购 NeXT 继承 Mach/BSD 成果并降低成本的因果概括系主持人单方推断，未经 Apple/NeXT 财务与工程档案核实。（BSD Now EP591，[477.6-522.5]，L4）[订正：原 [479.48-518.82]，2026-09-30 SenseAudio 重转核对]
- 主持人就专有 Unix 的衰落展开讨论：昂贵的专有 Unix 平台因创新迟缓与封闭生态而让位于廉价开放架构，PC 以低价与现成部件取胜，ARM 亦因低价而崛起。（BSD Now EP591，[561.6-672.6]，L2）[订正：原 [562.28-665.06]，2026-10-01 SenseAudio 重转核对]
- 三位主持人自述各自的 BSD 入门史：Benedikt 以 FreeBSD 5.2.1 入门，Jason 经 OpenBSD 2.8 与 OpenBSD 文档接触 BSD，Tom 在 PowerPC iBook G4 上尝试 OpenBSD 4.1 与 FreeBSD 7-current。（BSD Now EP591，[2101.6-2502.2]，L1）[订正：原 [2115.96-2492.78]，2026-10-01 SenseAudio 重转核对]

**史料**：

- Eric LeBlanc 访谈（Xinuos 董事长兼 CEO 当事人自述）。（BSD Now EP51，[992.22-1870.22]，L1）
- 本期为主持人自访的口述史料；其中 Copland 开发者数量、Jean-Louis Gassée 对 BeOS 的评价及 IBM 与 Sun 收购细节均为主持人转述的二手信息。（BSD Now EP591，[426.6-475.7]，L2）[订正：原 [429.12-471.38]，2026-09-30 SenseAudio 重转核对]

**史观**：

- 总纲13 法律与道德是利益分配：总纲13 法律与道德是利益分配：Xinuos 选择 BSD 许可证的本质是转售商与专有业务利益的分配安排。（BSD Now EP51，[1163.86-1179.76]，L1）
- 总纲3 不存在进步，只有权力再分配：总纲3 不存在进步，只有权力再分配：Xinuos 由专有 System V 转向参与 FreeBSD，是商业权力格局的再分配而非线性技术进步。（BSD Now EP51，[1014.92-1128.06]，L1）
- 总纲11 商品是形式主义：总纲11 商品是形式主义：访谈将操作系统视为可支持、可转售的商品，并以支持周期与许可证作为商品属性展开叙述。（BSD Now EP51，[1322.60-1363.72]，L1）
- 总纲5 没有必然性，只有偶然性：主持人关于 Apple 破产、NeXT 成功、IBM 收购 Sun 的反事实讨论，强调技术史由具体事件与偶然条件塑造，而非某种必然规律。　[存疑脚注] Apple 破产、NeXT 成功、IBM 收购 Sun 等反事实讨论为主持人现场发挥，无一手文献支撑，仅作口述史观点记录。（BSD Now EP591，[361.1-522.5]，L4）[订正：原 [373.70-518.82]，2026-10-01 SenseAudio 重转核对]
- 总纲22 知识注定过时：主持人从 Amiga、286、Z80 到专有 Unix 的淘汰中，呈现旧技术平台与其知识的持续更替，而非单纯的代际进步。（BSD Now EP591，[561.6-672.6]，L2）[订正：原 [562.28-665.06]，2026-10-01 SenseAudio 重转核对]

**辨析**：

- Xinuos 与 SCO 的历史关联及其 UNIX 版权诉讼前史在本期仅被一带而过，其与 FreeBSD 关系的长期后果未在本期展开。　[存疑脚注] SCO 前史仅凭主持人转述与当事人简短开场，未经多源交叉核验（BSD Now EP51，[1015.90-1019.40]，L4）
- Copland 缩减至约三名开发者、Gassée 对 BeOS 的评价等说法均为主持人转述，缺乏当期一手档案佐证，应作存疑处理。　[存疑脚注] 相关数字与评价为主持人转述，未经 Apple 或计算机历史博物馆一手档案核实。（BSD Now EP591，[426.6-475.7]，L4）[订正：原 [429.12-471.38]，2026-09-30 SenseAudio 重转核对]

**文献**：

- [BSD Now EP51] Pennington J. BSD Now: 51: Engineering Nginx[EB/OL]. (2014-08-20)[2026-08-15]. <https://www.bsdnow.tv/51>.
- [BSD Now EP591] Pennington J. BSD Now: 591: The Three Wise Men (hosts)[EB/OL]. (2024-12-26)[2026-08-15]. <https://www.bsdnow.tv/591>.

<!-- /PODCAST_REVIEW -->
