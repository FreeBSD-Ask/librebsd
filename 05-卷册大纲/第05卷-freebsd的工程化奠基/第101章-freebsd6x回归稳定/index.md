---
chapter: 第 101 章
id: CH101
volume: 第05卷-freebsd的工程化奠基
---

# 第101章 freebsd6x回归稳定

> 本章前部五字段为全章要点的摘要，子节详目见 [概述.md](概述.md)；编纂立场与局限详见文末〈自反性声明〉。

## 要点

- FreeBSD 6.0(2005.11.3，release/6.0.0 tagger_date = 2005-11-03T00:35:26Z，tagger = cvs2svn) 回归稳定设计哲学：放弃 5.x 的激进改造，专注性能调优与 bug 修复；目标 “5.x 适合生产环境”；6.0 是 5.x 的 “稳定化版本”
- 6.0 发布过程：2005.4 6.0-BETA1、2005.8 6.0-BETA4、2005.10 6.0-RC1、2005.11.3 6.0-RELEASE（release/6.0.0 tagger_date = 2005-11-03T00:35:26Z，tagger = cvs2svn）；Release Engineering 团队由 Scott Long 主导
- 6.x 稳定化是渐进路线而非新方向：6.0 起 libthr 1:1 取代失败的 KSE M: N 成为默认线程模型，ULE 调度器仅为实验性选项而 4BSD 保持默认；发布工程自 2005 年起拉开发布间隔并终结 4.x/5.x 双发布周期并行，发布分支内只进 bug 修复与少量驱动更新（据 101.1、101.2、101.12）
- 6.0 发布日期以 release/6.0.0 tagger_date = 2005-11-03T00:35:26Z 为准，与旧叙事 2005.11.4 的 1 天误差属公告日期与 tag 日期差异；6.x 稳定与否须结合早期 bug 报告与 bug tracker、release engineering 数据综合判断，commit 量升降不直接等同于稳定性（据 101.1.1、101.1.4 辨析）
- 6.x 时期无名贡献者：(1) 测试与 bug 报告志愿者；(2) 文档翻译志愿者；(3) Port 维护者；(4) 邮件列表回答者
- 与同时期操作系统相比：Linux 2.6（2003-2010）进入成熟期、市场份额持续增长，Windows Vista（2006.11, NT 6.0）失败促使企业重新评估 Linux/BSD，Solaris 10（2005.1 起，Update 1-8 至 2008）持续更新；同期 BIND DNS 拒绝服务漏洞群、OpenSSL DTLS 整数溢出与 tcpdump 缓冲区溢出等安全响应贯穿 6.x 版本周期（据 101.13、101.14）

## 史观

- 总纲第 22 条——知识注定过时：6.x 是 5.x 债务的偿还——5.x 寄望的 KSE M: N 线程模型被证实实现复杂、性能不及预期，由更简单的 libthr 1:1 取代；曾被当作方向的激进改造让位于稳定化（据 101.1、101.2、101.12）
- 总纲第 10 条——动手者创造历史：6.x 的稳定性由测试与 bug 报告志愿者、文档翻译志愿者、Port 维护者与邮件列表回答者等无名贡献者支撑，其劳动多未被既有记录完整留存（据 101.10）
- 否定之否定的回归稳定：6.x 不是革命，而是对 5.x 一厢情愿的否定之否定——KSE M: N 死了，libthr 1:1 接班；SMPng 还在抖，那就再稳一版；用户被 5.x 吓跑了，就把他们叫回来；回归稳定不是倒退（本章史观映射，见概述）

## 辨析

- 经 freebsd.duckdb tags 表验证，6.0-RELEASE 的 tagger_date 为 2005-11-03T00:35:26Z（非旧叙事 2005.11.4，误差 1 天，可能为公告日期与 tag 日期差异）；6.x 是否真稳定，需查早期 bug 报告；0 信任原则适用说明：L1.1.1 年度 commit 量基于 author_date 聚合，FreeBSD SVN-to-Git 2020 迁移可能引入日期偏差；L1.1.1/L1.1.2 报告截断（仅显示前 30 行）导致 2004-2008 年 freebsd-src 数据不可直接获取，须直接查询 freebsd.duckdb 验证；L1.3.2 文件修改数为替代指标，不等于 commit 量（单个 commit 可修改多文件）；L1.4.1/L1.4.2 release tag 间隔报告同样截断，部分 tag 为 svn2git 重构标签须排除 _cvs 后缀（据 101.1.1）
- MPSAFE VFS 在 6.0 的具体完成度在不同叙事中存在差异——部分资料称 6.0 完成 MPSAFE VFS，部分称 6.1 才完整，经 freebsd.duckdb 查询未得明确证据（MPSAFE 为代码级概念，无单一 commit/tag 标记完成时间），需对照 6.0 Release Notes 与 commit log 核验；Giant 锁在 6.x 时期残余的具体范围需考据（据 101.12.1）
- 边缘贡献者的界定标准、承认机制及其对 6.x 稳定性的作用需独立判断；贡献者是否被记录，需查 contributors 列表与邮件列表（据 101.10.2）
- Linux 2.6 成熟对 FreeBSD 的影响需查市场份额；Vista 失败是否真使企业转向 BSD，需独立判断（据 101.13）
- 范围注：2007.8.10 Judge Kimball 即决判决 Novell 持有 UNIX 版权与 MGM v. Grokster（545 U.S. 913）属 SCO 诉讼法律语境，见本章 [101.11](101.11-法律语境-SCO-诉讼与-MGM-v-Grokster.md)（其中 Novell v. SCO 即决判决属第 15 卷 295.3 章范围），本章不再展开

## 文献

- 6.0 Release Notes；freebsd-stable 邮件；6.0 Release Schedule；Scott Long 发布公告；release/6.0.0. freebsd-src 仓库 tag [DB/OL]. 2005-11-03T00:35:26Z. tag: release/6.0.0; commit: 3d215489fe03c6c5cecc3b5ed9ea39118e6ce379 ［A］；freebsd.duckdb L1.1.1 查询结果（freebsd-src 年度 commit 量 2005-2008）[DB/OL]；freebsd.duckdb L1.4.1 查询结果（freebsd-src release tag 间隔 6.x 系列）[DB/OL]；freebsd.duckdb L1.3.2 查询结果（freebsd-src 年度文件操作数 2005-2008）[DB/OL] ［A］
- Robert Watson “FreeBSD SMPng Project” 演讲；Michael W. Lucas “FreeBSD 5 SMPng”（; login: vol. 30 no. 5, 2005）；freebsd-threads 邮件；libthr(3) 手册页 ［A］
- 作者不详. FreeBSD commit log[Z]. 年份不详；作者不详. FreeBSD 邮件列表[EB/OL]. 年份不详；contributors 列表；FreeBSD 6.0-RELEASE src/sys/ commit log；McKusick & Neville-Neil (2014), Chapter 4 ［A］
- Linux 2.6 Release Notes；Vista Release Notes；Solaris 10 Update Notes；Distrowatch［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
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
