---
chapter: 第 206 章
id: CH206
volume: 第10卷-openbsd的历史
---

# 第 206 章 openssh的诞生与早期发展

## 要点

- OpenSSH 诞生于 1999-12：OpenBSD 2.6（1999-12-01）内置 OpenSSH 1.2.2，portable 版本随后首次单独发布，现已覆盖全球绝大多数 UNIX/Linux 发行版
- 四项纯洁化工作在 fork 数周内完成——de Raadt 移除非可移植代码、Provos 前往加拿大移除加密与 GPL 组件、Friedl 以 SSH 1.5 替换 SSH 1.3、Beck 改写 Makefile 规避 RSA 专利
- SSH1 弃用贯穿全史：2015-03 编译期默认禁用，7.4（2016-12-19）移除服务端支持，7.6（2017-10-03）完全删除客户端代码；OpenSSH 仓库共 14372 次提交（1999-10-27 至 2026-08-20），173 位贡献者

## 史料

- OpenSSH 官方文档与发布说明（openssh.com 一手官方来源，衍生组官方文档采集所得）

- OpenSSH 代码仓库统计（openssh.duckdb）：共 14372 次提交、173 位贡献者（1999-10-27 至 2026-08-20）

## 史观

- 总纲第 10 条——动手者创造历史：OpenSSH 的全球采纳是无数系统管理员默默部署的结果，非营销之功

## 辨析

- fork 日期在不同叙事中存在差异——部分来源称“1999 年 9 月（随 OpenBSD 2.6 于 1999-12-01 正式发布）”（以 OpenSSH-1.0 commit 日期 1999-10-01 为准），部分称“1999 年 9 月”（以初始导入 commit 84959968510b 日期 1999-09-26 为准）；经 openbsd.duckdb 核查，初始导入为 1999-09-26（口径注：1999-09-26 系 openbsd-src 树内初始导入日，而要点所载“1999-10-27 至 2026-08-20”统计窗出自独立的 OpenSSH portable 仓库，二者口径不同，非矛盾）
- 考据过程留痕——【查证来源】合图“成功”判定的各项事实经以下一手史料核验：SSH1 移除时间线，经 OpenSSH 7.4 Release Notes（<https://www.openssh.com/txt/release-7.4>，2026-07-23 WebFetch 一手核验）确认原文“This release removes server support for the SSH v.1 protocol.”
- 纯洁化工作的具体范围经 OpenSSH 官方历史页面确认涵盖四项——de Raadt 的非可移植代码移除、Provos 的加密与 GPL 组件移除、Friedl 的 SSH 1.3→1.5 协议替换、Beck 的 RSA 专利规避 Makefile；纯洁化完成时间节点为 OpenSSH 1.2.2 随 OpenBSD 2.6 发布日 1999-12-01，因 1.2.2 是首个随 OpenBSD 正式发布的 OpenSSH 版本。
- FreeBSD 4.0（2000-03-14）包含 OpenSSH 但 sshd 未默认启用——vendor import 在 2000-02-24，MFC 至 4-STABLE 在 2000-03-13，但“sshd enabled by default”MFC 在 2000-09-07（commit 94e00feef2e1），故 FreeBSD 4.0 用户需手动启用 sshd，FreeBSD 4-STABLE 直至 2000-09-07 MFC 后才默认启用 sshd。
- SSH1 移除时间线经 OpenSSH 官方 Release Notes 与 openbsd.duckdb 双重核实——7.4（2016-12-19）移除服务端 SSH1，7.6（2017-10-03）完全删除客户端 SSH1（含配置选项与文档），部分二手资料将“OpenSSH 8.2（2020-02-14）”误记为 SSH1 移除版本，但 8.2 Release Notes 实际记载的是 FIDO/U2F 支持。

## 文献

- OpenSSH 官方项目历史 [EB/OL]. <https://www.openssh.com/history.html>
- OpenSSH 7.4 Release Notes [EB/OL]. <https://www.openssh.com/txt/release-7.4>
- OpenSSH 7.6 Release Notes [EB/OL]. <https://www.openssh.com/txt/release-7.6>

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP194、BSD Now EP192、BSD Now EP191、BSD Now EP190（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 2017 年第一季度状态报告记录 core team、基金会、ports（接近三万端口）、release engineering（11.1 排期）等团队动态，基金会赞助 168 个提交并资助多个项目。（BSD Now EP194，[98.3-164.34]，L2）
- Colin Percival 提出一种介于 Patreon 与 Bugzilla 之间的开源维护资助模型，主张以持续收入支持软件维护而非一次性赏金，从而缓解开源软件维护不足的问题。（BSD Now EP194，[878.98-1386.52]，L2）
- Chris Siebenmann 追溯 FreeBSD 目录组继承行为至 4.1cBSD 引入 mkdir 系统调用与多组进程的时期，指出新对象继承父目录组是传统 BSD 行为而非 FreeBSD 的新发明。（BSD Now EP194，[2332.28-2964.74]，L2）
- OpenBSD 变更集移除 SSHv1 协议代码，从 FreeBSD 移植 witness 锁顺序校验工具，并引入 BearSSL 常数时间 AES 实现。（BSD Now EP194，[1925.44-2328.28]，L2）
- OpenSSH 彻底移除 SSHv1 全部代码，简化协议处理；此前该协议已默认禁用多年。（BSD Now EP192，[65.54-183.18]，L2）
- FreeBSD 基金会 4 月更新记录授予 Edward Napierala 项目资助，以 CTL 为后端开发 USB 大容量存储目标驱动，使 BeagleBone Black、Raspberry Pi Zero 等嵌入式平台可模拟 U 盘。（BSD Now EP192，[210.02-300.24]，L2）
- Patrick M. Hausen 回忆 1994 年与 Jordan Hubbard 会面，获 Walnut Creek 全套 CD-ROM 与 50 张 FreeBSD 1.1 光盘回德国推广，其后公司以 FreeBSD 3/4 运行服务器。（BSD Now EP192，[1270.68-1320.66]，L1）
- Rick Macklem 发布 pNFS 服务器首个测试征集，架构为单个元数据服务器加多个数据服务器，纯 FreeBSD 实现，当前尚不支持冗余。（BSD Now EP192，[5241.34-5535.38]，L2）
- FreeBSD 长期使用 32 位 inode，单文件系统与 NFS 导出受约四十亿对象上限制约；ino64 分支源自 Gleb Kurtsou 的 GSoC 项目，后由 Kirk McKusick 接手，征集新旧内核与用户态混搭测试。（BSD Now EP191，[2826.6-3145.38]，L2）
- OpenBSD 在 amd64 与 i386 将 Clang 加入 base 作为非默认编译器，动因是 GCC 转向 GPLv3 以及支持 arm64 新硬件的需求。（BSD Now EP191，[5192.9-5287.82]，L2）
- Tatu Ylönen 于 1995 年向 IANA 申请端口 22，因 SSH 拟取代 FTP（20/21）与 Telnet（23），次日获 Joyce Reynolds 分配该端口。（BSD Now EP191，[5570.38-5905.62]，L2）
- 德国高校与 AV-TEST 合作研究扫描 64,415 个 GitHub PHP 代码库，发现 117 处与教程漏洞同源的安全缺陷，其中约八成是 SQL 注入。（BSD Now EP191，[4149.76-4709.4]，L2）
- OpenBSD 6.1 如期发布，为项目第 42 个版本；SSH 特权分离不再可配置关闭，并去除随机化与校验检查以支持 AFL fuzzing。（BSD Now EP190，[409.46-563.58]，L2）
- ZFS 压缩 send/receive 依赖压缩 ARC 特性，可跨网络直接传输压缩块，避免发送前解压、接收后再压缩的低效流程。（BSD Now EP190，[3892.42-4264.2]，L2）
- Kris Moore 披露 FreeNAS 11 将采用 jail 插件、从 GRUB 切换 BSD loader，并计划引入持久 L2ARC 等 ZFS 特性。（BSD Now EP190，[3280.58-3598.7]，L1）
- Mike Muuss 于 1983 年受 Dave Mills 言论启发，一夜写出 ping 并为 4.2a BSD 补充内核 ICMP 支持；ping 命名来自声呐回响，而非“Packet Internet Groper”缩写。（BSD Now EP190，[4653.46-4908.5]，L2）

**史料**：

- FreeBSD Quarterly Status Report（2017 年第一季度，官网发布）（BSD Now EP194，[67.52-222.56]，L1）
- Colin Percival 于 daemonology.net 发表的开源软件维护方案博客原文（BSD Now EP194，[872.66-1467.2]，L1）
- Chris Siebenmann（University of Toronto）关于 BSD 目录组继承语义的考据博客（BSD Now EP194，[2332.28-2964.74]，L1）
- OpenBSD changes of note 621（tedu 发布的变更综述）（BSD Now EP194，[1925.44-2332.28]，L1）
- OpenBSD OpenSSH 删除 SSHv1 代码的提交记录（BSD Now EP192，[65.54-183.18]，L1）
- FreeBSD Foundation 2017 年 4 月开发者更新（BSD Now EP192，[210.02-300.24]，L1）
- Patrick M. Hausen 访谈自述（BSD Now EP192，[1066.4-2279.84]，L1）
- Rick Macklem 的 pNFS call for testing 邮件（BSD Now EP192，[5241.34-5535.38]，L1）
- Constantine Belousov 的 ino64 测试征集邮件（BSD Now EP191，[2826.6-3145.38]，L1）
- OpenBSD Clang 使用 FAQ（BSD Now EP191，[5192.9-5287.82]，L1）
- SSH.com 发表的“How SSH got port 22”历史文章（BSD Now EP191，[5570.38-5905.62]，L1）
- TU Berlin、Saarland University、TU Braunschweig 与 AV-TEST 合作的教程安全缺陷论文（BSD Now EP191，[4149.76-4709.4]，L1）
- OpenBSD 6.1 发布公告（BSD Now EP190，[72.92-87.54]，L1）
- FreeBSD ZFS vendor 分支导入提交（BSD Now EP190，[3892.42-4264.2]，L1）
- Kris Moore 访谈自述（BSD Now EP190，[3280.58-3714.9]，L1）
- Mike Muuss 的 ping 主页自述（BSD Now EP190，[4653.46-4908.5]，L1）
- Dennis Ritchie《The Evolution of the Unix Time-sharing System》（BSD Now EP190，[8.0-13.36]，L1）

**史观**：

- 总纲10 动手者创造历史：状态报告显示基金会资助与普通提交者的日常维护共同推进系统细节，历史由大量默默动手者累积而成。（BSD Now EP194，[98.3-164.34]，L2）
- 总纲13 法律与道德是利益分配：开源维护资助之争的实质是贡献者劳动如何获得回报的利益分配问题，而非单纯的技术或道德问题。（BSD Now EP194，[907.04-1249.4]，L2）
- 总纲5 没有必然性，只有偶然性：BSD 目录组继承语义是 4.1cBSD 多组进程引入时的偶然工程选择，随后沉淀为传统，并非预先设计的必然。（BSD Now EP194，[2486.68-2686.36]，L2）
- 总纲10 动手者创造历史：Patrick Hausen 从组装 PC、接触 Xenix 到部署 FreeBSD 的历程表明，历史由持续动手运维的人塑造。（BSD Now EP192，[1068.62-1274.52]，L1）
- 总纲9 经验优先：主持人与其访谈对象依据长期实际部署经验判断 BSD 相对 Linux 的稳定性与文档质量，经验先于抽象理论。（BSD Now EP192，[1425.04-1488.94]，L1）
- 总纲4 分离聚合是永恒规律：pNFS 把单一 NFS 服务拆分为元数据节点与数据节点，再聚合为统一文件系统，体现分离聚合的循环。（BSD Now EP192，[5241.34-5535.38]，L2）
- 总纲22 知识注定过时：32 位 inode 等既有设计随时间成为瓶颈，知识注定在演进中过时。（BSD Now EP191，[2826.6-3145.38]，L2）
- 总纲13 法律与道德是利益分配：OpenBSD 弃 GCC 选 Clang 是许可证约束与架构支持之间的利益权衡。（BSD Now EP191，[5234.94-5283.66]，L2）
- 总纲10 动手者创造历史：ino64 从 GSoC 学生项目经多人接力维护到主线，体现动手者持续积累的历史过程。（BSD Now EP191，[2993.42-3046.66]，L2）
- 总纲10 动手者创造历史：Mike Muuss 一夜写就 ping 并补齐内核支持，说明关键工具常由具体动手者直接造就。（BSD Now EP190，[4653.46-4908.5]，L2）
- 总纲9 经验优先：OpenZFS 以特性在生产环境运行六个月作为接纳前提，经验验证先于理论采纳。（BSD Now EP190，[3415.94-3437.3]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 特性先在 FreeBSD、illumos 等系统落地测试，再聚合回上游，体现分离聚合循环。（BSD Now EP190，[3396.02-3430.0]，L2）

**辨析**：

- [存疑脚注] Colin Percival 的开源资助方案当时仅为其个人提案，尚未落地实施，能否被社区采纳与商业化可行仍待验证。 [存疑脚注] 该方案属单一来源的个人设想，未形成实施记录。（BSD Now EP194，[1367.52-1440.28]，L4）
- [存疑脚注] Patrick Hausen 所忆 1994 年与 Jordan Hubbard 会面、Walnut Creek 光盘数量等细节系当事人多年后回忆，需与 Walnut Creek 档案交叉核验。 [存疑脚注] 当事人回忆性细节，缺乏独立一手档案印证。（BSD Now EP192，[1279.84-1320.66]，L4）
- [存疑脚注] ino64 的 2007 年起始点与十年开发时长系播客转述，需对照 FreeBSD 提交历史核验。 [存疑脚注] 单一来源转述的时间线，缺提交记录印证。（BSD Now EP191，[2889.64-2908.0]，L4）
- [存疑脚注] 教程安全缺陷研究数据为 2017 年快照，117 处漏洞发现不能代表当时 PHP 生态全貌。 [存疑脚注] 研究样本受 GitHub API 限制，覆盖范围有限。（BSD Now EP191，[4334.74-4354.04]，L4）
- [存疑脚注] ping“一晚写成”与 4.2a BSD 内核 ICMP 支持的时间线系作者自述，需与 4.2BSD 源码与 DARPA 会议记录交叉核验。 [存疑脚注] 单一来源自述，缺少独立档案印证。（BSD Now EP190，[4708.38-4780.22]，L4）

**文献**：

- [BSD Now EP194] Pennington J. BSD Now: 194: Daemonic plans[EB/OL]. (2017-05-17)[2026-08-15]. <https://www.bsdnow.tv/194>.
- [BSD Now EP192] Pennington J. BSD Now: 192: SSHv1 Be Gone[EB/OL]. (2017-05-03)[2026-08-15]. <https://www.bsdnow.tv/192>.
- [BSD Now EP191] Pennington J. BSD Now: 191: I Know 64 & A Bunch More[EB/OL]. (2017-04-26)[2026-08-15]. <https://www.bsdnow.tv/191>.
- [BSD Now EP190] Pennington J. BSD Now: 190: The Moore You Know[EB/OL]. (2017-04-19)[2026-08-15]. <https://www.bsdnow.tv/190>.

<!-- /PODCAST_REVIEW -->

<!-- dangan-20260908 消解回写 -->
- SSH Communications Security 1999 商业许可证声明 [EB/OL]. 1999. <https://www.ssh.com/>
<!-- /dangan-20260908 -->
