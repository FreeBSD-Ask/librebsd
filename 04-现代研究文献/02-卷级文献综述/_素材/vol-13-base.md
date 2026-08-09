# 第 13 卷综述素材（T1 三源合一，2026-08-04 自动生成）

> 卷目录：第13卷-bsd衍生操作系统｜章范围：ch253-ch269

## ① 现有研究（references_fulltext，36 条）

- [1677] Goodkin D, Gurkowski D. FreeBSD Workshop[C]. FOSSY 2023, Portland, OR, July 13–1（，）
- [1812] FreeBSD Foundation. FreeBSD Journal. Nov/Dec 2020.（，）
- [1814] FreeBSD Foundation. FreeBSD Journal. Sep/Oct 2020.（，）
- [1986] freecall using yate（freecall，）
- [2260] FreeBSD Handbook: Commercial users (Juniper/Netflix/Sony etc.)（The FreeBSD Project，2024）
- [2261] FreeBSD in Production: Who Uses It and Why（freebsdsoftware.org，2024）
- [2262] TrueNAS (based on FreeBSD)（iXsystems，2024）
- [2263] pfSense (FreeBSD-based firewall)（Netgate，2024）
- [2264] OPNsense (FreeBSD-based firewall)（OPNsense Project，2024）
- [2265] GhostBSD (FreeBSD-derived desktop)（GhostBSD Project，2024）
- [2266] MidnightBSD (FreeBSD-derived desktop)（MidnightBSD Project，2024）
- [2267] NomadBSD (persistent live system)（NomadBSD Project，2024）
- [2268] FreeNAS (network storage appliance)（iXsystems，2024）
- [2269] Junos OS (based on FreeBSD)（Juniper Networks，2024）
- [2270] PlayStation 4 OS (modified FreeBSD)（Sony Interactive Entertainment，2024）
- [2271] Netflix OpenConnect appliance (FreeBSD-based)（Netflix，2024）
- [2272] Orbis OS (PS5, FreeBSD 11 base)（Sony Interactive Entertainment，2024）
- [2273] WhatsApp (FreeBSD infrastructure)（Meta，2024）
- [2274] mfsBSD (memory-based FreeBSD toolkit)（mfsBSD Project，2024）
- [2275] BSD Router Project (FreeBSD-based)（BSD Router Project，2024）
- [2322] FreeBSD derivatives: failures and governance（The FreeBSD Project，2024）
- [2323] TrueNAS Open Storage platform（iXsystems，2024）
- [2324] TrueNAS CORE (FreeNAS successor) documentation（iXsystems，2024）
- [2325] pfSense Plus and CE documentation（Netgate，2024）
- [2326] OPNsense firewall documentation（OPNsense Project，2024）
- [2327] GhostBSD project documentation（GhostBSD Project，2024）
- [2328] MidnightBSD documentation（MidnightBSD Project，2024）
- [2329] Juniper Junos OS platform documentation（Juniper Networks，2024）
- [2330] PlayStation 4 system software (FreeBSD-based)（Sony Interactive Entertainment，2024）
- [2331] PlayStation 5 Orbis OS (FreeBSD 11 base)（Sony Interactive Entertainment，2024）
- [2332] Netflix Open Connect Appliance (FreeBSD)（Netflix，2024）
- [2333] Netflix and FreeBSD: 32% of North American traffic（The FreeBSD Project，2024）
- [2334] FreeBSD silent commercial users (Isilon/Verisign/WhatsApp)（The FreeBSD Project，2024）
- [2335] FreeBSD silent users: historical perspective（freebsdsoftware.org，2024）
- [2336] PC-BSD and TrueOS history（Wikipedia，2024）
- [2337] TrueOS (formerly PC-BSD) project documentation（iXsystems，2024）

## ② 研究缺口（doubts_to_resolve，51 条）

- id=1320 [resolved] - 辨析：stack protector 对栈缓冲区溢出有效但对堆溢出无效，须区分漏洞类型与缓解机制的对应关系；hardenedbsd-src 的 627 个去
- id=1321 [resolved] - 辨析：ASLR 对 Spectre 的 "有限缓解" 判断须以 HardenedBSD 官方安全公告或技术分析为据，不得仅凭理论推断；CVE-2017-57
- id=1322 [resolved] - 辨析：flashpowder 的具体技术机制（运行时随机化、陷阱检测）须以 HardenedBSD 官方文档与源码为据，本节基于公开信息的概括性描述可能存在
- id=1323 [resolved] - 辨析：NomadBSD 的 Live 系统技术栈（OpenBox、lxpanel、ZFS 快照持久化）须以项目官方文档核实，本节基于公开信息的概括性描述可能
- id=1324 [resolved] - 辨析：考据过程留痕——【查证来源】JunOS 基于 FreeBSD 用户空间经 Juniper 官方架构文档可验证；bsd_commits.db L7.2.
- id=1325 [resolved] - 辨析：考据过程留痕——【查证来源】JunOS 的控制平面与转发平面分离架构经 Juniper 官方架构文档可验证；Juniper 在转发平面的 R&D 投入
- id=1326 [resolved] - 辨析：考据过程留痕——【查证来源】JunOS 内部 fork 维护模式经 Juniper 官方架构文档可验证；Linux 兼容层引入经 JunOS 版本发布
- id=1327 [resolved] - 辨析：考据过程留痕——【查证来源】JunOS 自 1998 年起即基于 FreeBSD，至 2026 年已延续 28 年经 Juniper 官方架构文档与 
- id=1328 [resolved] - 辨析：考据过程留痕——【查证来源】项目史观总纲第 11、13、19 条原文经 **c:\Users\ykla\Documents\hibsd\原材料\哲学\
- id=1329 [resolved] - 辨析：【查证来源】PlayStation.Blog 2010.3.28 PS3 Firmware v3.21 Update 公告原文经 WebFetch 核
- id=1330 [resolved] - 辨析：【查证来源】PS3 用户协议（PlayStation Network User Agreement）保留 Sony 修改系统软件权利的条款经 Sony
- id=1331 [resolved] - 辨析：【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 11、13、19 条原文经 Read 一手核验；PlayStation.Blog 
- id=1332 [resolved] - 辨析：【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 11、13、19 条原文经 Read 一手核验；Ventura v. SCEA 案
- id=1333 [resolved] - 辨析：【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 11 条原文经 Read 一手核验；原材料/哲学/项目统摄史观/第 08 章.md
- id=1334 [resolved] - 辨析：【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 13 条原文经 Read 一手核验；PlayStation.Blog 2010.3
- id=1335 [resolved] - 辨析：【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 19 条原文经 Read 一手核验；原材料/哲学/项目统摄史观/第 19 章.md
- id=1336 [resolved] - 辨析：【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、11、13、19、23、25 条原文经 Read 一手核验；本节 12
- id=1337 [resolved] - 辨析：【查证来源】Sony PS4/PS5 基于 FreeBSD 的事实经 FreeBSD Handbook 官方页面（freebsd.org.cn/fre
- id=1338 [resolved] - 辨析：【查证来源】BSD 许可证原文经 FreeBSD 官方页面一手核验，确认 "再分发与使用" 条款允许商业实体封闭化使用衍生作品；Sony 工程师在 l
- id=1339 [resolved] - 辨析：【查证来源】总纲第 8、11、21 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 11、14、25 行 Read 一手核验（第 8 条 "
- id=1340 [resolved] - 辨析：【查证来源】合图层所依据的总纲第 8、11、19、21 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 11、14、19、25 行 Read
- id=1341 [resolved] - 辨析：【查证来源】总纲第 11 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 14 行 Read 一手核验，原文为 "商品是形式主义。技术市场的
- id=1342 [resolved] - 辨析：【查证来源】总纲第 8 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 11 行 Read 一手核验，原文为 "本体论上各方平等。FreeB
- id=1343 [resolved] - 辨析：【查证来源】总纲第 21 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 25 行 Read 一手核验，原文为 "革命与改革是历史方法论的分
- id=1344 [resolved] - 辨析：【查证来源】本节所引用的总纲第 1、2、7、8、11、21、23、25 条原文均经 `原材料/哲学/一刻哲学/第25章.md` Read 一手核验；【
- id=1345 [resolved] - 辨析：【查证来源】总纲第 13 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 17 行 Read 一手核验，原文为“法律与道德是利益分配。任何道
- id=1346 [resolved] - 辨析：【查证来源】总纲第 19 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 23 行 Read 一手核验，原文为“解释学循环是历史认识的根本条
- id=1347 [resolved] - 辨析：【查证来源】总纲第 21 条原文经 `原材料/哲学/一刻哲学/第25章.md` 第 25 行 Read 一手核验，原文为“革命与改革是历史方法论的分歧
- id=1348 [resolved] - 辨析：【查证来源】本节所引用的总纲第 8、13、19、21 条原文均经 `原材料/哲学/一刻哲学/第25章.md` Read 一手核验；Ventura v.
- id=1349 [resolved] 需要说明的是，文件名为“2004_Rosen_rosen-l-2004-open-source-licensing-software-freedom-and_e
- id=1350 [resolved] 5 篇文献中 Bonaccorsi 与 Rossi、Weber、Meeker、Tsatsaronis 四篇围绕开源软件的成功机制、法律风险与质量度量展开，为本章
- id=1351 [resolved] - 辨析：考据过程留痕——【查证来源】FreeBSD 官方手册（**<https://www.freebsd.org.cn/freebsdhandbook/nu
- id=1352 [resolved] - 辨析：考据过程留痕——【查证来源】BSD-3-Clause 许可证文本经 Open Source Initiative（**<https://opensou
- id=1353 [resolved] - 辨析：考据过程留痕——【查证来源】IDC 2012 年将 NetApp Data ONTAP 评为“2012 年度开放式网络磁盘存储系统市场第一品牌存储操作
- id=1354 [resolved] - 辨析：考据过程留痕——【查证来源】BSD-3-Clause 许可证文本经 Open Source Initiative（**<https://opensou
- id=1355 [resolved] - 辨析：考据过程留痕——【查证来源】IDC 2012 年将 NetApp Data ONTAP 评为“2012 年度开放式网络磁盘存储系统市场第一品牌存储操作
- id=1356 [resolved] - 辨析：考据过程留痕——【查证来源】BSD-3-Clause 许可证文本经 Open Source Initiative（**<https://opensou
- id=1357 [resolved] - 辨析：考据过程留痕——【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 19 条原文与原材料/哲学/项目统摄史观/第 19 章.md 解释
- id=1358 [resolved] - 辨析：考据过程留痕——【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 21 条原文与原材料/哲学/项目统摄史观/第 21 章.md“革命
- id=1359 [resolved] - 辨析：考据过程留痕——【查证来源】原材料/哲学/项目统摄史观/第 25 章.md 总纲第 1、2、7、11、13、19、23、25 条原文经本项目哲学源材料
- id=1360 [resolved] - 史观：总纲第 25 条——终结中的延续，桌面 BSD 实验的 "终结" 是形式而非实质（思想延续至 GhostBSD 等）；统计结论印证：C-28（vol-
- id=1361 [resolved] - 辨析：PC-BSD 时期 "安全维护投入高于纯社区 fork" 的判断须以 iXsystems 员工 commit 量、安全公告频率等量化指标为据，不得仅凭
- id=1648 [resolved] IBM 公告 URL 与 SEC 8-K 文件编号须以 IBM 官网与 SEC EDGAR 数据库一手核实，详见考据记录 20260730_jianyi缺口补全
- id=1649 [resolved] GitHub 收购完成日期 2018-10-26 与 Microsoft 加入 OIN 2018 年 10 月为多份二手来源一致表述，但 Microsoft 官
- id=1650 [open] MAINTAINERS 文件中 Red Hat 员工比例统计存在口径差异——以雇佣关系统计（含 Red Hat 直接雇佣与前员工）与以 @redhat.com/
- id=1651 [resolved] 具体每位技术委员会成员的偏好排序须以 debian-ctte 邮件列表存档（**lists.debian.org/debian-ctte/2014/02/**，
- id=1652 [resolved] VUAs 集体声明未列具名成员名单，jianyi.md 中“Vincenzo ‘KatolaZ’ Nicosia 等”须以 DNG 邮件列表后续发帖核实具体核心
- id=1729 [open] 第 258.4 节（第 45、59 行）称存在名为 'flashpowder' 的 HardenedBSD '漏洞缓解框架'，机制为运行时随机化/陷阱检测。穷尽
- id=1730 [resolved] NEWREF:1986 主库 title 为 'freecall using yate'（author 'freecall'，year 空），bibliogra
- id=1731 [open] 第 263 章主张 'PS4 Orbis OS 基于 FreeBSD 9'。'基于 FreeBSD' 主线有广泛二手技术报道支持，但具体版本号 'FreeBSD
- id=1732 [open] 第 264 章涉及 'PS5 Prospero OS' 的 FreeBSD 基底，但其具体 FreeBSD 版本号 Sony 未公开。任何具体版本号断言均不可考

## ③ 一手史料（original_sources.kaoju_records，0 条）

（无）
