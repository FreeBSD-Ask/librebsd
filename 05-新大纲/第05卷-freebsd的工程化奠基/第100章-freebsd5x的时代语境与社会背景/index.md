---
chapter: 第 100 章
id: CH100
volume: 第05卷-freebsd的工程化奠基
---

# 第 100 章 freebsd5x的时代语境与社会背景

## 要点

- 1996-2010 美国总统科技政策：Clinton 第二任期 (Telecom Act 1996.2.8、DMCA 1998.10.28、Sonny Bono CTEA 1998.10.27、US v. Microsoft 1998.5.18、Bush v. Gore 2000.12.12)、Bush 43 任期 (9/11 2001.9.11、USA PATRIOT Act 2001.10.26、No Child Left Behind 2002.1.8、Iraq War 2003.3.20、Lehman 破产 2008.9.15、TARP 2008.10.3)、Obama 任期 2009-2010(ARRA 2009.2.17、ACA 2010.3.23、Citizens United v. FEC 2010.1.21)
- 1996-2010 伯克利校长：Chang-Lin Tien(1990-1997)、Robert M. Berdahl(1997-2004)、Robert J. Birgeneau(2004-2013)；三人对 CSRG 遗产与 BSD 项目的态度不同
- 1996-2010 集成电路发展：Intel Pentium II 至 Core 系列、AMD Athlon/Opteron/AMD64 复兴 (2003 AMD64 为 FreeBSD 提供首批 64 位平台)、ARM Holdings 崛起与嵌入式革命、Apple 2005 从 PowerPC 向 Intel 转型
- 硬件厂商谱系：Intel Pentium II(1997)/III(1999)/4(2000)/Core(2006); AMD K6(1997)/Athlon(1999)/Opteron(2003, AMD64)/Phenom(2007); ARM ARM7(1994)/ARM9(1997)/ARM11(2002)/Cortex(2005); Apple 2005.6 Intel 转型
- 物理与工艺：250nm(1997)→180nm(1999)→130nm(2001)→90nm(2004)→65nm(2005)→45nm(2007)→32nm(2009)；多核时代 (Pentium D 2005、Core 2 Duo 2006)；SoC 集成；功耗墙约 2005 显现
- 多元群体贡献（100.18）：除企业核心外，FreeBSD 贡献者横跨多国——德国、法国、俄罗斯等地域 ccTLD 与多所大学（如 Stony Brook）的学术贡献显著；区域志愿者填补本地化与硬件移植空白，学术研究者将 BSD 作为操作系统研究的活体平台
- 与同时期操作系统比较（100.19）：Microsoft Windows XP（2001.10）统一了消费与商业桌面，Windows Server 2003（2003.4）强化了服务器能力
- 其余子节要点详见对应子节文件：100.16（FreeBSD 5.x 时期的技术淘汰：GEOM、UFS2、rcNG 与 ULE）、100.17（第三方软件变更：PF 防火墙引入与 MTA 格局）、100.20（漏洞与安全响应：FreeBSD 5.x 时期的 mksnap_ffs 权限缺陷）

## 史观

- 总纲第 3 条——不存在进步，只有权力再分配，制程演进（250nm→32nm）与厂商兴衰（AMD 复兴、Apple 转型 Intel）呈现为权力再分配而非线性进步
- 总纲第 4 条——分离聚合是永恒规律，5.x 相对 4.x 的架构分离及其后向 6.x/7.x 的重新聚合
- 总纲第 5 条——没有必然性，只有偶然性，Telecom Act 1996、9/11、USA PATRIOT Act 与 2008 金融危机等偶然事件构成 5.x 的时代约束
- 总纲第 7 条——理论必须自反，本章自反性声明即该条在编纂层的落实
- 总纲第 8 条——本体论上各方平等，企业贡献者与区域志愿者、FreeBSD 与同期操作系统在本章并置而不预设高下
- 总纲第 10 条——动手者创造历史，区域志愿者填补本地化与硬件移植空白，学术研究者将 BSD 作为活体研究平台
- 总纲第 13 条——法律与道德是利益分配，Telecom Act 1996、DMCA、Sonny Bono CTEA 与 US v. Microsoft 案即利益分配的场域
- 总纲第 20 条——历史地理塑造思想土壤，伯克利校长谱系（Tien、Berdahl、Birgeneau）对 CSRG 遗产与 BSD 项目的地缘延续

## 辨析

- 政策对 BSD 的实际影响，需独立判断
- 经 bsd_commits.duckdb tags 表验证，5.0-RELEASE 的 tagger_date 为 2003-01-16（非旧叙事 2003.1.19，误差 3 天，可能为公告日期与 tag 日期差异）；GEOM 是否真正“取代”旧 disk 子系统需考据——5.0 引入但 4.x 的 disk 子系统仍保留兼容直至 7.x
- 经 bsd_commits.duckdb tags 表验证，5.3-RELEASE 的 tagger_date 为 2004-11-04T19:12:42Z（非旧叙事 2004.11.6，误差 2 天，可能为公告日期与 tag 日期差异）；经 bsd_commits.duckdb commits 表验证，PF 导入 commit 为 2004-06-16T23:03:14Z Max Laier “Import pf from OpenBSD 3.5 (OPENBSD_3_5_BASE)”
- 企业提交多属受雇工作期间的“有组织贡献”，不宜与志愿者个人贡献混同；corp 名单随年份变动，须以 contributors 表逐期核验
- 将 5.x 早期性能问题等同于“FreeBSD 衰落”是片面——5.x 的架构债务清理为 6.x/7.x 的性能回升奠定基础；Linux 2.5 同样经历开发期不稳定

## 文献

- Federal Register；法案全文［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- FreeBSD 5.0-RELEASE Release Notes (2003.1)；Kamp, P.-H. 2002 BSDCon “GEOM—Modular Disk Framework”；geom(4) 手册页；FreeBSD Handbook “GEOM” Chapter；release/5.0.0. freebsd-src 仓库 tag [DB/OL]. 2003-01-16T16:56:23Z. tag: release/5.0.0; commit: 47227ef0ef663b7abb81ab5a60a450da9a93d24b ［A］
- FreeBSD 5.3-RELEASE Announcement [Z]. 2004-11-04；Hartmeier D. The Design and Implementation of the OpenBSD Packet Filter (PF)[C]//BSDCon 2002. San Francisco, 2002；OpenBSD 3.0 Release Notes [Z]. 2001-12-01；Max Laier. Import pf from OpenBSD 3.5 (OPENBSD_3_5_BASE). freebsd-src [DB/OL]. 2004-06-16T23:03 ［A］
- freebsd.duckdb（freebsd-src contributors 表，窗口 2002–2005，检索 2026-07-21）［A］；FreeBSD 项目贡献者指南（<https://docs.freebsd.org/en/articles/contributing/>）［B］
- Torvalds L. Linux 2.6 ChangeLog [EB/OL]. 2003；McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. Addison-Wesley, 2004. ［B］
- FreeBSD-SA-04:01.mksnap_ffs [Z/OL]. 2004-01-30. <https://www.freebsd.org/security/advisories/FreeBSD-SA-04:01.mksnap_ffs.asc>；CAN-2004-0099. NVD [DB/OL]. <https://nvd.nist.gov/vuln/detail/CAN-2004-0099>；**原材料/研究/bsd 漏洞史/早期漏洞补遗/freebsd-早期漏洞.md** ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
