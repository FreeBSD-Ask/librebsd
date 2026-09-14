---
chapter: 第 277 章
id: CH277
volume: 第14卷-商业生态与企业案例
---

# 第277章 基金会争议与企业治理

## 要点

- **FreeBSD Foundation** 的收入主要来自企业捐赠，**Juniper** 长期占据显著比例。收入结构的集中度引发对基金会独立性的担忧。
- **FreeBSD Foundation** 的个人捐赠低迷，曾出现 **Core Team** 成员在 Twitter 催款的尴尬事件。个人捐赠的低迷反映 BSD 社区的商业闭环缺失。
- **Linux Foundation** 的资金规模远超 **FreeBSD Foundation**，2020 年代年收入已达数亿美元。**Linux Foundation** 的商业模式包括会员费与认证服务。
- **FreeBSD Foundation** 的年报与 IRS 990 表是财务分析的主要史料，需逐年核查。
- **TrueNAS 25.04**（**Fangtooth**）于 2025 年 4 月 22 日正式发布，基于 **Linux Kernel 6.12**（底层发行版为 **Debian 12 bookworm**），用 **Incus** 替代 **jails**，支持 **Secure Boot** 与 **TPM**。转向 **Linux** 是 **iXsystems** 的重大战略调整。**iXsystems** 官方公告位于 `truenas.com/blog` 或 `ixsystems.com/blog`（具体公告 URL 须以 **iXsystems** 官网实时检索为准）[考据完成：2026-07-30 TrueNAS 25.04 发布日期为 2025 年 4 月 22 日，Debian 12 bookworm 为 TrueNAS SCALE 系列的底层发行版，25.04 统一后延续此底层；iXsystems 官方公告 URL 须以官网实时检索为准]

## 史观

- 总纲第 13 条——法律与道德是利益分配：基金会收入结构的法律披露（原挂“总纲第 12 条——法律结构”，权威表第 12 条为“科学是形式主义”，主题不符，按 R2140 先例改挂）
  - 辨析：**Juniper** 占比的确切数字需核查 IRS 990 表
  - 文献：FreeBSD Foundation IRS 990；年报；FreeBSD Foundation 官方财务页面 <https://freebsdfoundation.org/about-us/about-the-foundation/financials/>
- 专题语（不设条号）：资金治理与社区参与（原挂“总纲第 23 条——社区治理”，权威表第 23 条为“一切历史写作都是基于哲学设定的历史小说”，主题不符，改专题语）
  - 辨析：个人捐赠低迷的原因需多角度分析
  - 文献：Twitter 存档；Foundation 筹款记录 ［A］

## 277.10.2 个人捐赠低迷与 Twitter 催款事件

- 要点：**FreeBSD Foundation** 的个人捐赠低迷，曾出现 **Core Team** 成员在 Twitter 催款的尴尬事件。个人捐赠的低迷反映 BSD 社区的商业闭环缺失。
- Twitter 存档；Foundation 筹款记录 ［A］

## 277.10.3 与 Linux Foundation 资金规模的比较

- 要点：**Linux Foundation** 的资金规模远超 **FreeBSD Foundation**，2020 年代年收入已达数亿美元。**Linux Foundation** 的商业模式包括会员费与认证服务。
- 总纲第 8 条——本体论上各方平等：两个 **Foundation** 的法律结构不同（501(c)(3) vs 501(c)(6)），治理模式与资金规模差异不构成优劣序（原挂“总纲第 16 条——经济周期”非基线条名，按权威表改挂）
  - 辨析：两个 **Foundation** 的法律结构不同（501(c)(3) vs 501(c)(6)），比较需注意
  - 文献：Linux Foundation 年报；IRS 990 ［B］

## 277.10.4 基金会年报与 IRS 990 表考据

- 要点：**FreeBSD Foundation** 的年报与 IRS 990 表是财务分析的主要史料，需逐年核查。
- 史观：总纲第 13 条——法律与道德是利益分配：非营利组织的财务透明度属利益披露的法律与道德维度（原挂“总纲第 12 条——法律结构”非基线条名，改挂）
- 辨析：IRS 990 表的解读需会计专业知识
- 文献：FreeBSD Foundation IRS 990；年报 ［B］
- iXsystems 公告；TrueNAS 25.04 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 277.11.2 CORE 与 SCALE 并存时代的终结

- 要点：**TrueNAS CORE**（**FreeBSD**）与 **SCALE**（**Linux**）的并存局面在 25.04 终结，**iXsystems** 统一于 **Linux**。**CORE** 用户面临迁移压力。
- 史观：总纲第 22 条——知识注定过时：TrueNAS CORE（FreeBSD 基底）被 SCALE（Linux 基底）取代，反映存储 appliance 领域 FreeBSD 系知识栈的代际更替（原挂“总纲第 25 条——终结与延续”非基线条名，按报告建议改挂）
- 史料：**iXsystems** 迁移指南、社区论坛中的用户
- 辨析：转向 **Linux** 的技术动机是否为唯一原因需分析
- 文献：iXsystems 公告；TrueNAS 25.04 文档［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 277.12.2 企业与志愿者 committer 权限平等原则

- 要点：**FreeBSD** 的 committer 权限规则不区分企业 committer 与志愿者 committer，所有 committer 遵守相同规则。这是 **FreeBSD** 治理的核心原则之一。
- 史料：Committer's Big List of Rules 文本、**Core Team** 治理文档 ［A］
- 史观：总纲第 13 条——法律与道德是利益分配：权限规则以统一法律文本约束企业与志愿者两类主体（原挂“总纲第 12 条——法律结构”非基线条名，改挂）
- 辨析：平等原则的实施须以 Committer's Big List of Rules 与 **Core Team** 决议公开记录为据；未公开撤销不等于无争议，可能存在私下警告〔注：辨析句原文截断，按上下文收束〕
- 文献：Committer's Big List of Rules；Core Team 决议；Linux MAINTAINERS 文件；FreeBSD committer 文档 ［A］

## 277.12.4 Core Team 权限决议与邮件记录考据

- 要点：**Core Team** 的权限决议记录存于 `freebsd-hackers` 邮件列表与 **Core Team** 内部文档（部分公开）。
- 史料：`freebsd-hackers` 邮件列表、**Core Team** 公开决议 ［A］
- 史观：专题语（不设条号）：决议记录的透明度（原挂“总纲第 23 条——社区治理”非基线条名，改专题语）
- 辨析：内部决议的公开程度有限，史料重建不完整
- 文献：freebsd-hackers 邮件列表；**FreeBSD Committer's Guide**；**FreeBSD Foundation** 年报 ［A］〔注：原混入的内部脚本路径与查询编号（freebsd.duckdb commits 表、script/query_ch133_enterprise_commits.py、L3.2.1）已按可读来源著录规则移除，记录见 **04-现代研究文献/09-bsd仓库数据分析/**〕

## 277.13.2 重要企业 committer 历史档案

- 要点：基于 277.12 节核验脉络（原稿称“133.12.7 节”系拆分前旧章号）的 freebsd.duckdb 查询结论，**freebsd-src** 仓库中企业 committer 的 commit 分布为：**iXsystems** 530 commit（最高，反映 iXsystems 作为企业 committer 的贡献集中度）〔原文截断，后续分布数据待回源〕

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP75（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Ed Maste 首次接触 BSD 并非经由三大发行版本体，而是在滑铁卢一家视频流硬件初创公司实习时接触采用 BSD 网络栈的 VxWorks；2000 年代初其新公司需同时维持大量并发 TCP 连接，因 FreeBSD 的 kqueue 已可用而 Linux 的 epoll 尚未成熟而选定 FreeBSD，此后在公司 FreeBSD 衍生系统中负责推动修改回流上游，2012 年前后因其社区工作受基金会董事会注意而入会任项目开发总监。（BSD Now EP75，[973.16-1139.82]，L1）
- 基金会资助的自我定位是填补社区无人承担的空白：每年董事会会议基于用户、大型企业与个人支持者的反馈确定高优先主题，当年度定为安全、性能与开发者工具三项，典型如人人需要却无人愿独自投入的工具链；资助形式分面向个人的定点项目资助与全职员工承担的长期项目两类，最终取舍由董事会裁量。（BSD Now EP75，[1144.06-1294.33]，L1）
- 主持人 Kris Moore 以 PC-BSD 开发者身份宣布 10.1.1 季度版：底层仍为 FreeBSD 10.1，新增基于 boot environments 与 chroot 技巧的后台自动更新（使用中系统不被改动，重启即进入新环境）、全套工具迁移至 Qt5、提供 OVA 虚拟机镜像，并以 GELI v7 配合 GRUB 实现单加密 zpool 的全盘加密启动，不再留未加密的引导分区。（BSD Now EP75，[3292.72-3389.12]，L1）

**史料**：

- 访谈提及的基金会一手文件包括新近上线的项目资助提案指南（约十至十一页并附样例提案），其要点为提案须绑定明确范围、具名开发者与预算金额，并须清晰论证对 FreeBSD 社区的收益；年度直接项目资助预算数字由基金会工作人员提供并经 Ed Maste 在访谈中复述。（BSD Now EP75，[1600.02-1703.84]，L1）
- 本期新闻段援引的一手材料包括 Damien Miller 介绍 OpenSSH 6.8 密钥轮换机制的博客文章、Adam Wolk 记述 OpenBSD 二进制快照滚动跟进体验的博文、详述新旧支持模型利弊的 FreeBSD 邮件列表帖子，以及 Josh Paetzel 执笔的 FreeNAS 硬件选型指南；各件均以链接形式收入节目注释。（BSD Now EP75，[2776.48-3071.16]，L2）

**史观**：

- 总纲4 分离聚合是永恒规律：Ed Maste 断言 FreeBSD 在部分第三方组件上只维护树内副本而不与上游沟通，是通往长期分叉灾难的路径，主张从做完再回推上游转向与上游同体工作，并举其作为 LLVM 上游 committer、FreeBSD 移植工作先在上游仓库进行为例；主持人补充 OpenZFS 亦在重构类似协作通道——分叉与回流在开源工程组织中反复重演，构成又一轮聚合循环。（BSD Now EP75，[2117.84-2313.04]，L1）
- 总纲5 没有必然性，只有偶然性：面对 2014 年使筹款近乎翻倍的一笔事先不知情的巨额捐赠，基金会将其中百分之十直接注入项目资助池，其余设立捐赠基金分年支用，以备歉收之年，并将直接项目资助预算自 2014 年的十二万二千美元提至 2015 年的三十万美元——一次性偶然馈赠不可充作长期依赖，须经制度安排转化为可持续的资金秩序，恰见组织存续对偶然性的驯化。（BSD Now EP75，[1877.28-1971.32]，L1）

**辨析**：

- Ed Maste 对基金会已结项目的内部评估并不齐一：autofs 自动挂载守护进程与内核态 iSCSI 栈被引为部署反馈良好的成功案例，而 vt 控制台更新虽早已是 current 默认、其本人亦使用年余，却自认远未达预期，项目体量超出当初预估而仍在收尾——同为基金会出资，工程完成度因项目而异，资金投入与成果兑现并无必然对应。（BSD Now EP75，[1484.46-1590.74]，L1）

**文献**：

- [BSD Now EP75] Pennington J. BSD Now: 75: From the Foundation (Part 1)[EB/OL]. (2015-02-04)[2026-08-15]. <https://www.bsdnow.tv/75>.

<!-- /PODCAST_REVIEW -->
