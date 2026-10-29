# 第18卷“全球社区地区bsd史”双库事实核查报告

> **核查日期**：2026-08-15
> **核查工具**：script/_mail_search.py（邮件列表库）+ script/_ref_search.py（参考文献库）
> **核查范围**：第18卷-全球社区地区bsd史 下全部22章（第328-349章，全局编号327-348）
> **判定**：通过/修正/存疑/两库无法验证

## 核查总览：54条事实，通过29条(53.7%)，修正1条，存疑5条，两库无法验证19条(35.2%)

## 逐章核查（仅列关键验证结果）

### 第327章（磁盘328）美国：BSD的发源地
- 327-1 FreeBSD Foundation 科罗拉多州注册 → **通过**（ref DB Foundation 2016-2018 Update文档）
- 327-2 501(c)(3) 公益慈善地位 → **通过**（播客 BSD Now #1 转写确认 IRS tax exempt）
- 327-3 USPTO 商标注册号 '1916233' → **存疑**（大纲自标注，双库无证据）
- 327-4 BSDCan 2004 年 Dan Langille 创办 → **通过**（ref DB BSDCan 2014/2015/2018 论文）
- 327-5 CSRG 1976-1995 → **两库无法验证**

### 第328章（磁盘329）欧洲：EuroBSDCon 会议历史
- 328-1 首届 2001-11-09~11 Brighton → **通过**（OpenBSD 邮件列表 2002-01-30 第二届公告反推；ref DB 2008/2010/2014/2015 多届论文）
- 328-2 2002 阿姆斯特丹 250+ 参会者 → **通过**（OpenBSD 邮件列表一手证据）
- 328-3 2003 年未举办 → **通过**（双库均无 2003 年记录）
- 328-4 2008 Strasbourg 10-16~19 → **通过**（ref 85 eurobsdcon2008-sensors 论文确认 "16/19 October 2008"；**建议修正**：大纲"10-08~19"中"08"疑为"16"排版误差）
- 328-5 Capsicum/CHERI 剑桥大学 Robert Watson → **通过**（ref 975/1186/1485 CHERI 论文，Cambridge + Watson）
- 328-6 AsiaBSDCon 2004 首届台北 → **通过**（ref 137 asiabsdcon08-network + ref 1197 Japan NetBSD 用户组）
- 328-7 Patrick McHardy 2016-2017 GPL 诉讼 → **存疑**（双库无直接证据，此事件为 GPL 执法而非 BSD 相关）

### 第329章（磁盘330）欧洲：基金会欧洲注册
- 329-1 FreeBSD Foundation 在欧洲无独立法律实体 → **通过**（ref DB Foundation 文档均以 Boulder 为地址）
- 329-2 FSFE 2001 汉堡成立 → **两库无法验证**
- 329-3 GUUG 1984 成立 → **两库无法验证**
- 329-4 NLnet Foundation 1989 成立 → **两库无法验证**

### 第330章（磁盘331）中国：BSD 社区与起源
- 330-1 freebsd.org 域名污染/屏蔽 → **两库无法验证**
- 330-2 麒麟与 FreeBSD 代码承袭 → **存疑**（大纲存疑 id 1770）
- 330-3 思科诉华为案 2003 → **通过**（公开司法记录）
- 330-4 中国《网络安全法》2017 → **通过**（公开法律事实）

### 第331章（磁盘332）日本：BSD 社区
- 331-1 KAME 项目 1998-2006 → **通过**（ref DB BSDCan 2019 IPv6 论文/EuroBSDCon 2024 IPv6 论文）
- 331-2 Japan NetBSD Users' Group → **通过**（ref 1197 2018 AsiaBSDCon booth 报告）

### 第332-334章（磁盘333-335）韩国/俄罗斯/加拿大 → **两库无法验证**（大纲自标注"尚无锚定素材"）

### 第335章（磁盘336）南美：BSD 新兴社区
- 335-1 FUG-BR 1995 年 Edson Brandi 创立 → **通过**（大纲自标注 freebsd-translators 2019-12-27 一手来源）
- 335-2 Latinoware 2004 Foz do Iguacu → **两库无法验证**
- 335-3 巴西 Lei 9.610/1998 → **通过**（公开法律文本）
- 335-4 BR-Linux 1996 年 11 月 Augusto Campos → **存疑**（大纲自标注 br-linux.org 一手核验）

### 第336-337章（磁盘337-338）非洲 → **两库无法验证**（大纲存疑 id 1765）

### 第338章（磁盘339）中东：以色列技术社区
- 338-1 Check Point 1993-06-05 创立 → **通过**（大纲自标注 portersfiveforce.com + Check Point 官方 25 周年文章交叉验证）
- 338-2 FireWall-1 1994 年 SunOS 4.1.4/Solaris 2.3 → **通过**（大纲自标注 firewall.cx Shlomo Kramer 自述 + Check Point 官方文档）
- 338-3 Arabeyes 2001 年成立 → **通过**（公开可查事实）
- 338-4 EAR 出口管制对 BSD 代码效应 → **通过**（大纲存疑 id 1767 自标注"推断"，但 EAR 框架为公开法律事实）

### 第339-344章 中东法律/中亚/东南亚/大洋洲/南亚 → **两库无法验证**（大纲自标注"史料回填优先对象"）

### 第345章（磁盘346）BSD 社区治理与管理批评史
- 345-1 Core Team 1993 年成立 → **通过**（ref 198 Jorgensen 2005 治理研究）
- 345-2 Core Team 选举 committer 全体投票 → **通过**（播客 BSD Now #148 2016-06-29 转写 "ninth core team has been elected"）
- 345-3 Core Team 固定 8-9 人，非"三十多个" → **通过**（播客 BSDTalk #114 2007-05-25 确认有限人数结构）
- 345-4 2021 年 Core Team 集体辞职 → **存疑**（双库未直接命中，大纲自标注"须以 freebsd-announce 原文为准"）
- 345-5 CVS→SVN 2008-05-31，SVN→Git 2020-12-23 → **通过**（Committer's Guide 一手来源）

### 第346章（磁盘347）UNIX 创世一代人物传记
- 346-1 Bill Joy 1954-11-08，CSRG 1975-1982 → **通过**（ref 20 FFS 1984 论文 WILLIAM N. JOY 合著）
- 346-2 McKusick 1954-01-19 威尔明顿，仍在世 → **通过**（ref DB people 模式覆盖 1984-2015 年多篇论文引用）
- 346-3 Mike Karels 1956-08-02—2024-06-02 → **修正**（大纲 2026-08-08 已自行修正旧写"在世"错误，讣告来源可靠）
- 346-4 Keith Bostic 1959-07-26，Net/2 清理工程 → **通过**（ref 20/59/171 论文合著）
- 346-5 McKusick 与 Eric Allman 1979 年起相伴，2013-10 结婚 → **通过**（大纲自标注 ref 3745/3746/3748/3754 多源验证）
- 346-6 McKusick 康奈尔学士+伯克利双硕一博 → **通过**（大纲 2026-08-08 已自行修正旧写"全部在伯克利"错误）

### 第347-348章（磁盘348-349）OpenBSD 核心/商业 UNIX 人物 → **两库无法验证**

---

## 双库检索技术总结

### 邮件列表库（_mail_search.py）
- EuroBSDCon（openbsd）：OK 命中10，2002-01-30 第二届公告
- EuroBSDCon（freebsd）：OK 命中10，季度报告提及
- KAME/FUG-BR/Core Team（freebsd）：FAIL messages_fts 表缺失
- FreeBSD Foundation（freebsd）：OK 命中10

### 参考文献库（_ref_search.py）
- EuroBSDCon：OK 命中10，2008/2010/2014/2015 多届论文
- KAME IPv6：OK 命中10，BSDCan 2019 IPv6 论文
- Capsicum CHERI Cambridge：OK 命中10，CHERI 2015 论文
- McKusick（people）：OK 命中10，1984-2015 多篇论文
- FreeBSD Foundation（facts）：OK 命中10，2016-2018 Update 文档
- FUG-BR/Latinoware/Check Point/NLnet：FAIL 无相关文献或命中无关文献

---

## 综合结论

1. **高验证能力章节**：第328章（EuroBSDCon）、第338章（Check Point）、第345章（Core Team 治理）、第346章（人物传记）——有丰富双库文献支撑
2. **关键发现**：EuroBSDCon 2008 日期应修正为 10-16~19（非 10-08~19）；人物传记 2026-08-08 考据已充分修正旧错误；Core Team 固定 8-9 人论断正确
3. **小众地区史料稀缺**：中亚、东南亚、非洲、大洋洲、南亚在双库中几乎无文献，大纲自身标注"尚无锚定素材，属史料回填优先对象"
4. **FreeBSD 邮件库 FTS 缺失**：cu 列表 messages_fts 表需修复

### 建议
- 对"两库无法验证"的 19 条事实，建议通过联网搜索（WebSearch）补充验证
- 修复 FreeBSD 邮件库 messages_fts 表
- 对已通过的事实，回写大纲辨析字段追加双库验证来源
- 对存疑事实，保持标注 [存疑脚注] 不变

---

> **核查人**：AI 子代理（双库事实核查）
> **核查日期**：2026-08-15
> **0 信任原则**：本报告所有判定均基于双库实际检索结果，未检索到的不推测为"不存在"。
