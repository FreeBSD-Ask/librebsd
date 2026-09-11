---
chapter: 第 101 章
id: CH101
volume: 第05卷-freebsd的工程化奠基
---

# 第101章 freebsd6x回归稳定

## 要点

- FreeBSD 6.0(2005.11.3，release/6.0.0 tagger_date = 2005-11-03T00:35:26Z，tagger = cvs2svn) 回归稳定设计哲学：放弃 5.x 的激进改造，专注性能调优与 bug 修复；目标 “5.x 适合生产环境”; 6.0 是 5.x 的 “稳定化版本”
- 6.0 发布过程：2005.4 6.0-BETA1、2005.8 6.0-BETA4、2005.10 6.0-RC1、2005.11.3 6.0-RELEASE（release/6.0.0 tagger_date = 2005-11-03T00:35:26Z，tagger = cvs2svn）；Release Engineering 团队由 Scott Long 主导
- 设计哲学辨析：(1) 6.x 是 5.x 的稳定化还是新方向；(2) 渐进改造 vs 激进改造；(3) 与 Linux 2.6 渐进对比
- 6.0 史料疑点：(1) 6.0 是否真 “稳定”;(2) 6.0 发布日期是否延期；(3) 6.0 是否完全抛弃 5.x 遗产
- 6.x 时期无名贡献者：(1) 测试与 bug 报告志愿者；(2) 文档翻译志愿者；(3) Port 维护者；(4) 邮件列表回答者

## 史观

- 总纲第 5 条——技术债务与代码考古，6.x 是 5.x 债务的偿还
  - 辨析：经 freebsd.duckdb tags 表验证，6.0-RELEASE 的 tagger_date 为 2005-11-03T00:35:26Z（非旧叙事 2005.11.4，误差 1 天，可能为公告日期与 tag 日期差异）；6.x 是否真稳定，需查早期 bug 报告；〔待核：原文截断，后文待回源〕
- 总纲第 13 条——边缘者的作用
  - 辨析：贡献者是否被记录，需查
  - 文献：作者不详. FreeBSD commit log[Z]. 年份不详；作者不详. FreeBSD 邮件列表[EB/OL]. 年份不详 ［A］

## 100.10.2 边缘贡献者辨析

- 要点：边缘贡献者辨析：(1) 边缘标准；(2) 是否被承认；(3) 边缘贡献对 6.x 稳定性的作用
- 史料：contr
- 总纲第 11 条——历史书写的可错性
  - 辨析：判决对开源的实际影响，需独立判断
  - 文献：545 U.S. 913；Lessig 评论［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

## 100.11.2 2007.8.10 Judge Kimball 即决判决 Nove

- 总纲第 6 条——技术选择的代价：Giant 锁分解付出工程复杂度代价（细粒度锁设计与验证困难），但获得多核扩展性；总纲第 17 条——形式与内容：锁粒度作为 “形式” 改变 “内容”（内核并发执行能力）
  - 辨析：经 bsd_commits.duckdb tags 表验证，6.0-RELEASE 的 tagger_date 为 2005-11-03T00:35:26Z（非旧叙事 2005.11.4）
- 总纲第 7 条——BSD 与 UNIX 谱系的连续性
  - 辨析：Linux 2.6 成熟对 FreeBSD 影响，需查市场份额
  - 文献：Release Notes；Distrowatch［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

## 100.13.2 Windows

## 辨析

- 经 freebsd.duckdb tags 表验证，6.0-RELEASE 的 tagger_date 为 2005-11-03T00:35:26Z（非旧叙事 2005.11.4，误差 1 天，可能为公告日期与 tag 日期差异）；6.x 是否真稳定，需查早期 bug 报告；0 信任原则适用说明：L1.1.1 年度 commit 量基于 author_date 聚合，FreeBSD SVN-to-Git
- 贡献者是否被记录，需查
  - 文献：作者不详. FreeBSD commit log[Z]. 年份不详；作者不详. FreeBSD 邮件列表[EB/OL]. 年份不详 ［A］

## 100.10.2 边缘贡献者辨析

- 要点：边缘贡献者辨析：(1) 边缘标准；(2) 是否被承认；(3) 边缘贡献对 6.x 稳定性的作用
- 史料：contributors 列表、邮件[考据完成：2026-
- 判决对开源的实际影响，需独立判断
  - 文献：545 U.S. 913；Lessig 评论［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

## 100.11.2 2007.8.10 Judge Kimball 即决判决 Novell 持有 UNIX 版权

- 要点：2007.
- 经 bsd_commits.duckdb tags 表验证，6.0-RELEASE 的 tagger_date 为 2005-11-03T00:35:26Z（非旧叙事 2005.11.4）；［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］ MPSAFE VFS 在 6.0 的具体完成度在不同叙事中存在差异——部分资料称 6.0 完成 MPSAFE VFS，部分称
- Linux 2.6 成熟对 FreeBSD 影响，需查市场份额
  - 文献：Release Notes；Distrowatch［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

## 100.13.2 Windows Vista 与 Solaris 10

- 要点：Windows

## 文献

- 6.0 Release Notes；freebsd-stable 邮件；release/6.0.0. freebsd-src 仓库 tag [DB/OL]. 2005-11-03T00:35:26Z. tag: release/6.0.0; commit: 3d215489fe03c6c5cecc3b5ed9ea39118e6ce379 ［A］；freebsd.duckdb L1.1.1 查询结果（freebsd-src 年度 commit 量 2005-2008，报告截断）[DB/OL]；freebsd.duckdb L1.4.1 查询结果（freebsd-src release tag 间隔 6.x 系列
- 作者不详. FreeBSD commit log[Z]. 年份不详；作者不详. FreeBSD 邮件列表[EB/OL]. 年份不详 ［A］

## 100.10.2 边缘贡献者辨析

- 要点：边缘贡献者辨析：(1) 边缘标准；(2) 是否被承认；(3) 边缘贡献对 6.x 稳定性的作用
- 史料：contributors 列表、邮件［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］
- 史观：总纲第 13 条——边缘者的作用
- 辨析：边缘贡献者作用，需独立
- 545 U.S. 913；Lessig 评论［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

## 100.11.2 2007.8.10 Judge Kimball 即决判决 Novell 持有 UNIX 版权

- 要点：2007.8.10 犹他联邦法院 Judge Dale Kimball 即决判决 Novell（而非 SCO）持有 UNIX 版权，初步终结 SCO v. IBM 案件的法律基础；SCO 随后于 2007.9 申请 Chapter 11 破产保护；但该即决判
- FreeBSD 6.0-RELEASE Release Notes；Robert Watson “FreeBSD SMPng Project” 演讲；Michael W. Lucas “FreeBSD 5 SMPng”（; login: vol. 30 no. 5, 2005）；release/6.0.0. freebsd-src 仓库 tag [DB/OL]. 2005-11-03T00:35:26Z. tag: release/6.0.0; commit: 3d215489fe03c6c5cecc3b5ed9ea39118e6ce379 ［A］

## 100.12.2 KSE M: N 线

- Release Notes；Distrowatch［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

## 100.13.2 Windows Vista 与 Solaris 10

- 要点：Windows Vista(2006.11, NT 6.0) 与 Solaris 10(2005.1, Update 1-8 至 2008) 同期；Vista 失败使企业重新评估 Linux/BSD; Solaris 10 持续更新
- 史料：Vista Release Notes、So
- ISC BIND Security Advisories（isc.org/ops/advisories）；FreeBSD-SA-07:07.bind；freebsd.duckdb freebsd-src 仓库 BIND 相关 commit（2006-11 至 2007-07） ［A］
- OpenSSL Security Advisory（2007-10）；tcpdump ChangeLog（2007-08）；FreeBSD-SA-07:06.tcpdump；FreeBSD-SA-07:08.openssl；freebsd.duckdb freebsd-src 仓库 OpenSSL/tcpdump 相关 commit（2007-07 至 2007-10） ［A］
- freebsd.duckdb freebsd-src 仓库 6.x 版本周期 security fix commit 清单（2006-01 至 2008-01）；TrustedBSD 项目页面；OpenBSM 1.0 alpha 10 Release Notes ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP122（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 嵌入与安装有三重本质差异：嵌入以母镜像批量部署到多台设备而安装逐机定制并依赖发布工程或第三方项目产出镜像；嵌入要求一个跨版本可以精确重建的系统子集；嵌入面对的设备驱动需求不同，典型设备低功耗、无移动部件、全闪存运行并周期休眠，但亦有需风扇散热的路由器与文件服务器等接近普通 PC 的大型嵌入场景。（BSDTalk EP122，[82.04-181.52]，L1）
- 其十年嵌入式实践集中在两类平台：其一为 Intel 单板计算机从 Compact Flash 运行，需与大量自定义设备通信取状态与测量，构建时将闪存当普通盘但严格限制写入并深度子集化系统，产品镜像从约 14MB 到 96MB 不等；其二为基于 Atmel AT91RM9200 片上系统的低成本 ARM 平台，以 I2C 标记部件身份、SPI 承载引导 ROM、SD 卡存放系统，内存足迹更小且须更谨慎对待文件系统写入。（BSDTalk EP122，[184.52-288.32]，L1）
- 构建方法上从 FreeBSD 源码树取发布前后的快照，树本身几乎不加修改，配以自研软件、若干 ports 与 chroot 环境中的构建胶水，使镜像跨构建机器可再现且具有相同 MD5 签名；除特定自定义硬件外，全部平台支持都直接集成进 FreeBSD 树并进入受支持设备与处理器列表，所修缺陷与 ports 问题一律回馈原作者并滚动进后续版本。（BSDTalk EP122，[288.32-433.36]，L1）
- 闪存工程经验表明 SD 卡与 Compact Flash 的耐磨性已足够，只需多数系统只读挂载、不更新访问时间、日志先写入内存文件系统再刷回永久存储等简单预防，即可在除需与 MS-DOS 格式 U 盘互操作外的全部场景沿用 FFS；实时需求则完全下沉到硬件层，由操作系统定时调度、硬件执行测量后排队回传，产品无需任何实时增强。（BSDTalk EP122，[436.04-512.36]，L1）
- 当时嵌入式生态图景：x86 上已有 pfSense、m0n0wall 与 FreeNAS 等可下载镜像即装即得防火墙或网络存储；Linksys NSLU2（XScale ARM）与 WRT 系列路由器（MIPS）上均有移植努力，后者代码存于 Perforce 仓库但受 Linksys 持续削减闪存与 RAM 的成本策略阻碍；大量 MIPS 代码等待合入主树并期望赶上 7.0，ARM 与 PowerPC 的现成镜像仍然薄弱。　[存疑脚注] MIPS 移植赶在 7.0 之前合入属受访者当时的预期且自认存在后勤变数，实际合入时点须与发布工程记录核实。（BSDTalk EP122，[512.36-683.88]，L1）
- 他认为 FreeBSD 作为嵌入式系统的竞争力来自三点：多年专注服务器积累的强大网络与并行能力正日益成为嵌入设备的关键；集成源码树使构建与交叉构建所需一切都在仓库内，无须自行卷制发行版；BSD 许可证允许公司自由利用软件，随着其他开源许可证新限制出现，商业方正在重新审视 BSD 许可软件的价值。（BSDTalk EP122，[683.88-913.4]，L1）

**史料**：

- 本期提及的一手材料包括 embedded@freebsd.org 嵌入式开发者邮件列表、arm@、powerpc@ 与 mips@freebsd.org 各架构移植列表、BSDCan 年会上的嵌入式产品演讲与走廊交流、存放 WRT 路由器移植代码的 Perforce 仓库，以及计划在 7.0 发布说明中扩充的嵌入式能力文档。（BSDTalk EP122，[755.44-856.52]，L1）

**史观**：

- 总纲13 法律与道德是利益分配：许可证在本期叙述中呈现为一种利益分配的制度形式：BSD 许可证的宽松条款使企业得以将 FreeBSD 转化为商业产品并愿意投入，而其他开源许可证新增的限制则改变企业侧的利益计算，驱使其重新分配对 BSD 的注意力；技术采用格局随许可证条款这一利益边界的变化而移动。（BSDTalk EP122，[713.92-913.4]，L1）

**文献**：

- [BSDTalk EP122] Backman W. BSDTalk: 122: bsdtalk122 - Embedding FreeBSD with M. Warner Losh[EB/OL]. (2007-07-27)[2026-08-27]. <https://bsdtalk.blogspot.com/2007/07/bsdtalk122-embedding-freebsd-with-m.html>.

<!-- /PODCAST_REVIEW -->