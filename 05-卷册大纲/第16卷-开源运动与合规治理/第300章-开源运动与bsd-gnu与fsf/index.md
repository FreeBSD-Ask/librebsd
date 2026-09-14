---
chapter: 第 300 章
id: CH300
volume: 第16卷-开源运动与合规治理
---

# 第300章 开源运动与bsd-gnu与fsf

## 要点

- Richard Stallman 于 1983 年 9 月 27 日在 net.unix-wizards 新闻组发布 GNU 宣言，宣告 GNU（GNU's Not UNIX）项目启动；1985 年完善为完整 GNU 宣言文档，已含运行、研究、再分发与改进的自由主张（“四项自由”的系统表述于 1990 年代定型）；Stallman 哲学核心是 “软件共享是道德义务” 而非 “代码开放是实用策略”
- 自由软件基金会（FSF）于 1985 年 10 月 4 日成立，由 Stallman 创立，注册为 501(c)(3) 非营利组织；FSF 早期通过销售 GNU 软件磁带筹集资金；组织架构包括董事会、执行董事、雇员开发者；FSF 是 GPL 许可证的版权持有者
- GNU 项目与 BSD 的早期交集：(1) GNU 工具链（gcc、gdb、make、bash）长期与 BSD 系统协同；(2) FreeBSD 用户空间大量使用 GNU 工具；(3) 1990 年代起 GNU 与 BSD 在许可证哲学上分歧加深；(4) GNU C Library 与 BSD libc 的长期竞争
- GPL 与 BSDL 两种自由观的张力：(1) GPL 强调 “用户自由” 通过 copyleft 强制回馈；(2) BSDL 强调 “开发者自由” 允许任意使用；(3) Stallman 批评 BSDL “允许专有化” 为缺陷；(4) BSD 社区认为 BSDL 才是真正的自由，因不强制任何行为；GPL 的强制执行在 2008 年 FSF v. Cisco 案中有具体体现——FSF 起诉 Cisco 的 Linksys 产品违反 GPL（含 GCC、binutils、GNU C Library 等代码），案件于 2009.5.20 和解、历时约 5.3 个月（2008.12.11 起诉；据 FSF 2009-05-20 和解公告），Cisco 同意为 Linksys 任命自由软件总监（Free Software Director for Linksys）并建立合规流程，“compliance officer”系媒体转称，BSD 许可证因不强制回馈而无类似执行案例
- GNU/FSF 阵营对 BSD 在 GNU 生态中角色的批评集中在三个维度。(1) 许可证维度：Stallman 在 GNU Manifesto（1985，**gnu.org/gnu/manifesto.en.html** 确认，2026-07-24 联网核查）中明确提出 “proprietary modifications will not be allowed”（不允许专有化修改），此即 copyleft 原则的最早表述，BSD 许可证因允许专有化修改而被 FSF 视为缺陷；FSF 官方页面 “What is Copyleft?”（**gnu.org/licenses/copyleft.en.html**）明确表述 "the GPL gives users freedom to distribute and modify free software, and to charge for it, while ensuring that all modified versions remain free"，BSD 许可证不保障修改版本保持自由，故被 FSF 划入 “非 copyleft” 许可证范畴。(2) 协作维度：GNU 项目长期为 BSD 系统提供工具链（GCC 编译器、GDB 调试器、Bash shell、groff 排版系统、GNU coreutils），但 BSD 社区未对等回馈 GNU 工程——FreeBSD 用户空间长期依赖 GNU 工具链直至 2014 年 FreeBSD 10.0 以 Clang 替换 GCC（**freebsd.org/releases/10.0R/announce/** 确认，2026-07-24 联网核查，原文 "GCC is no longer installed by default on architectures where clang(1) is the default compiler"）与 2021 年 FreeBSD 13.0 移除 GNU grep（**freebsd.org/releases/13.0R/relnotes/** 确认），此长期依赖被 FSF 视为 BSD 对 GNU 工程的实质性受惠。(3) 哲学维度：FSF 认为 BSD 的 “消极自由” 哲学（不强制回馈、不强制开源）削弱了自由软件运动的道德立场——Stallman 在 GNU “Why Open Source misses the point of Free Software”（**gnu.org/philosophy/open-source-misses-the-point.html**）中明确表述 "the values of open source are not the values of free software"，BSD 社区因接受 “开放” 而非 “自由” 话语而被 FSF 视为运动中的妥协派

## 史观

- 0 信任原则（考据规则，非总纲条目）：对 Stallman 自述须独立考据
- 总纲第 15 条——文化即形式主义：FSF 组织形式主义是否过度
- 总纲第 13 条——法律与道德是利益分配：Stallman 对 BSD 许可证的批评表面为道德判断（“专有化是缺陷”），实质为利益分配之争——copyleft 通过法律强制保障修改版本回馈社区，BSD 许可证不强制回馈即放弃此利益再分配工具
- 总纲第 5 条——没有必然性，只有偶然性：Peterson 的命名偶然改变开源运动话语

（2026-09-12 整改：史观段原混入的辨析/文献子字段移归辨析段；空二级标题“##”删除；截断待核标记随重建消除——批次 C241 问题 3/4/5/6/8/9/7）

## 辨析

- GNU 宣言具体发布日期与平台，须查 Usenet 存档；宣言是否真影响 BSD 社区；【双库核查 2026-08-15】邮件列表库 freebsd 查询 Stallman GNU 命中 5 条（1998 年 Phillip Salzman 等提及），参考文献库 Stallman 命中 5 条（Meeker 2008、Salus 1994、开源许可证合规性研究 2022）——双库间接验证
- FSF 成立日期与 BSD 基金会对比（FSF 1985 vs FreeBSD Foundation 2000）；文献：FSF 官方历史
- 两种自由观无对错，需独立判断；是否实际影响技术演进；freebsd.duckdb freebsd-src 仓库的 license 主题 commit 显示 BSD 社区不仅在哲学上反对 GPL，更在工程实践上持续清理 GPL 代码——“GPL infected” 措辞与 “reduce whining” 措辞反映 BSD 社区对 GPL 的明确态度；FreeBSD 10.0 起 Clang 替换 GCC、13.0 移除 GNU grep 系工程清理的节点性事件〔2026-09-12 整改：截断收束〕
- 考据过程留痕——【查证来源】GNU Manifesto、What is Copyleft?、Why Open Source misses the point 三份文献均经 **gnu.org** 官方页面一手核验（2026-07-24 联网核查），原文引述准确；FreeBSD 10.0-RELEASE Announcement 经 **freebsd.org** 官方页面一手核验〔2026-09-12 整改：截断收束〕
- 【双库核查 2026-08-15】邮件列表库 freebsd 1997-1999 年查询 ‘open source’ 命中 5 条，参考文献库 ‘open source’ 命中 5 条（simsong 1994、Brooks 1987、Exokernel 1995）——双库间接验证 1998 年前后 ‘open source’ 术语在 BSD 社区的讨论（与 300.1.3 节双库核查一致）〔2026-09-12 整改：截断收束〕

（2026-09-12 整改：辨析段并入原史观段嵌套的辨析/文献子字段并完成收束——批次 C241 问题 1/9）

## 文献

- Stallman “GNU Manifesto”；Williams《Free as in Freedom》［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 300.1.2 FSF 1985 年成立与组织架构

- 要点：自由软件基金会（FSF）于 1985 年 10 月 4 日成立，由 Stallman 创立，注册为 501(c)(3) 非营利组织；FSF 早期通过销售 GNU 软件磁带筹集资金；组织架构包括董事会、执行董事、雇员开发者；FSF 是 GPL 许可证的版权持
- FSF 官方历史［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 300.1.3 GNU 项目与 BSD 的早期交集与分歧

- 要点：GNU 项目与 BSD 的早期交集：(1) GNU 工具链（gcc、gdb、make、bash）长期与 BSD 系统协同；(2) FreeBSD 用户空间大量使用 GNU 工具；(3) 1990 年代起 GNU 与 BSD 在许可证哲学上分歧加深；(4) GNU C Library 与 BSD libc 的长期竞争
- 史料：GNU 官方文献（Manifesto、What is Copyleft?、Why Open Source misses the point，均经 gnu.org 一手核验）与 freebsd.duckdb license 主题 commit 证据〔2026-09-12 整改：截断收束〕
- Stallman 论 BSD；McKusick 论许可证；freebsd.duckdb commits 表 freebsd-src Robert Watson commit `bf139e9706ee`（2002-11-04T18:11:17Z，"License: update, remove clause three of BSD license per approval of NAI."）；freebsd.duckdb commits 表 freebsd-src Poul-Henning Kamp commit `3b1746df8b34`（2003-01-18T10:08:27Z，"Sanitize the copyright section a bit: We do not need two copies of the four-clause BSD license in the file, one will do."〔2026-09-12 整改：截断按库内 commit 原文补全〕
- Stallman, R. The GNU Manifesto [EB/OL]. (1985). <https://www.gnu.org/gnu/manifesto.en.html> [2026-07-24]；Free Software Foundation. What is Copyleft? [EB/OL]. <https://www.gnu.org/licenses/copyleft.en.html> [2026-07-24]；Stallman, R. Why Open Source misses the point of Free Software [EB/OL]. <https://www.gnu.org/philosophy/open-source-misses-the-point.html> [2026-07-24]〔2026-09-12 整改：截断补全〕
- Peterson 开源 20 周年回顾文（2018；联网检索未能确证其 2006 年以“Open Source: Where It Started”为题发表之文〔存疑：2006 年出处待回源，确证前不采〕）［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 300.2.2 Netscape 开源 Navigator 的催化作用

- 要点：Netscape 于 1998 年 1 月 22 日宣布将 Navigator 浏览器源代码开源（mozilla.org），是商业大型软件首次主动开源；Netscape 决策受 Raymond《大教堂与集市》的启发（1998-01-22 宣布开源，mozilla.org 上线）〔2026-09-12 整改：截断收束〕
- OSI 官方历史［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 300.3.2 开源定义的十项标准与 BSD 许可证

- 要点：开源定义（OSD）十项标准由 Perens 基于 Debian 自由软件指南（DFSG）改写，1998 年由 OSI 采纳；OSD 包括自由再分发、源代码开放、派生作品、作者源代码完整性、无歧视、许可证传播、许可证不得特定于产品、不得限制其他软件、技术中立；BSD 许可证（两条款与三条款）作为 OSD 认证的原型许可证
- 史料：OSD 十项标准原文（opensource.org/docs/osd）与 BSD-2/3-Clause 许可证文本〔2026-09-12 整改：截断收束〕

> （2026-09-12 整改：本索引子节按 300.1.2→300.1.3→300.2.2→300.3.2 正序排列；300.1.1/300.2.1/300.3.1 未在本文件重复堆叠，内容见各节文件（同 336 章处置）；第一块残片版 300.1.3 已删除、保留完整版——批次 C241 问题 2/9。）

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP478（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Rob Pike 在一封 TUHS 邮件中自述，1977 年前后在多伦多大学动态图形实验室为 nroff 编写绘图仪输出程序，被 Dennis Ritchie 面试时问及为何重复 Berkeley 已做的工作，Pike 答曰自己先写而 Berkeley 后来才署名，Ritchie 相信了他，这一经历可能助其获得贝尔实验室职位。（BSD Now EP478，[1016.14-1237.96]，L1）
- FreeBSD rc 系统谱系可追溯至 4.0BSD（1980 年）的 rc 工具，NetBSD 于 2000 年引入 rc.d 目录与 rcorder 以现代化启动子系统，FreeBSD 5.0 三年后导入这一改进。（BSD Now EP478，[808.44-873.12]，L2）
- Peter Hansteen 以 SolarWinds 供应链攻击与 node-ipc 组件事件为例，破除开源软件天然更安全、足够多眼球即无深缺陷两类断言，强调安全取决于实际审查者的能力与投入。（BSD Now EP478，[423.52-644.98]，L2）

**史料**：

- Rob Pike 的 TUHS 邮件为当事人一手史料，记录 Toronto 排版系统、Regents 注释替换原作者署名以及被 Ritchie 雇佣的经过。（BSD Now EP478，[1167.76-1232.8]，L1）
- FreeBSD 手册页与 Clare Systems 文章共同呈现 rc 系统自 4.0BSD 起源、经 NetBSD 现代化再导入 FreeBSD 5.0 的时间线，属可交叉验证的技术史叙述。（BSD Now EP478，[808.44-873.12]，L2）

**史观**：

- 总纲6 和解优于斗争：Rob Pike 对 Berkeley 署名更替虽有不满，但最终以 Dennis Ritchie 相信自己收束，未演变为对立，体现和解优于斗争的处理方式。（BSD Now EP478，[1198.8-1232.8]，L1）
- 总纲8 本体论上各方平等：开源安全神话的辨析表明，安全性取决于实际审查能力而非许可证形式，不应预设某一阵营在本体论上更优越，呼应各方平等的判断。（BSD Now EP478，[423.52-620.84]，L2）

**辨析**：

- Rob Pike 所述 Berkeley 夺走功劳属单方回忆，Regents 注释替换的时间与动机需与 Berkeley 侧史料交叉验证。　[存疑脚注] 该段为 Rob Pike 单方自述，需比对伯克利 CSRG 源码与邮件记录。（BSD Now EP478，[1175.84-1203.44]，L4）
- 转写称 rc 工具首现于 4.0BSD（1980 年），具体出处与版本沿革需查证 FreeBSD 手册页原文。　[考据脚注] rc 首现版本与 4.0BSD 对应关系需查手册页 HISTORY 节与 4BSD 源码。（BSD Now EP478，[808.44-815.08]，L4）

**文献**：

- [BSD Now EP478] Pennington J. BSD Now: 478: Debunking sudo myths[EB/OL]. (2022-10-27)[2026-08-15]. <https://www.bsdnow.tv/478>.

<!-- /PODCAST_REVIEW -->