---
chapter: 第 28 章
id: CH28
volume: 第02卷-伯克利的岁月
---

# 第 28 章 vi 与 C Shell 的诞生

## 要点

- **vi** 命名起源的通行说法是 “vi 代表 visual（可视模式）”，此说法有 2BSD 一手发布说明支持——1979 年 2BSD 发布说明（TUHS 归档 2bsd_announcement.pdf）将 vi 描述为 ex 编辑器的 “screen editing facilities”（屏幕编辑功能），且 2BSD 随附文档标题为 “An Introduction to Display Editing with vi”
- csh 的历史替换与作业控制功能影响了后续 shell 设计——tcsh（Ken Greer **1981 年 12 月** 将 TENEX 风格文件名补全合并入 csh）延续 csh 谱系（Arch Linux man **tcsh(1)** 原文 “Ken Greer, HP Labs, 1981. File name completion.”），bash（Brian Fox **1989 年**）吸收 csh 交互功能，zsh（Paul Falstad **1990 年** 在普林斯顿大学发布于 comp.sources.misc 新闻组）
- 2BSD 是 PDP-11 平台上最后的主要 BSD 版本，1980 年代 BSD 主力转向 VAX，PDP-11 上的 2BSD 进入维护模式，但 2BSD 的代码与工具持续影响后续版本
- vi 的模态设计影响了后续编辑器——vim（Bram Moolenaar **1988 年** 在 Amiga 上开始开发，**1991 年 11 月** 首次公开发布 Vim 1.14 于 Fred Fish Disk #591，最初名为 “Vi IMitation”，**1992 年** Vim 1.22 移植到 UNIX/MS-DOS 后更名为 “Vi IMproved”；vim 保留 vi 的模态编辑模型并扩展多级撤销、语法高亮等，其兼容性谱系为 28.3/29.8 节辨析的延续）
- **csh 手册页**首次出现于 **2BSD**（man page 内部日期 **1979-02-24**），由 Bill Joy 编写，对应 csh 1.0 版本；**1BSD**（1978.3.9，TUHS 归档 1BSD/man1/ 目录确认）不含 csh man page，1BSD/man1/ 仅含 cd.1、lib.1、login.1、sh.1（Bourne Shell）、su.8、wait.1 共 6 个 man page

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3811] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3812] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3890] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3891] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3914] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3919] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3934] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_3958] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 folder，原因：folder 第28章
- [DB:references_fulltext:chapter_matches:chmatch_1551] 卷“第02卷-伯克利的岁月”第 28 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

总纲第 5 条——没有必然性，只有偶然性：vi 与 csh 诞生于 300 波特调制解调器与 PDP-11 硬件约束的偶然条件（与 28.1 映射一致）；总纲第 9 条——经验优先：Joy 的设计取舍以当事人一手叙述与源码为据（与 28.1/28.5 映射一致）；总纲第 4 条——分离聚合是永恒规律：csh 与 sh 谱系分化、tcsh/bash 对 csh 功能的吸收聚合（与 28.5 映射一致）；总纲第 2 条——历史是形式主义化的非存在：vi/csh 的“起源神话”为事后建构（与 28.1 辨析映射一致）；总纲第 15 条——文化即形式主义：模态编辑与 shell 语法成为技术文化的形式化遗产（与 28.3 映射一致）。子节级映射详见 28.1-28.5 各节史观字段

## 辨析

- ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ vi 命名起源在三个一手访谈来源中的具体陈述差异本节未能完整比对，原因如下：(1) Joy 2011 CHM 口述史 PDF 共 27 页，本节仅获取到前 6 页（至 BSD 与 VAX 引入部分），尚未触及 vi 命名讨论的具体段落，需后续获取完整 PDF 查阅 vi 命名相关段落；(2) McKusick BSD Now 278 期为音频格式访谈，无公开文字记录，需后续通过音频转录或人工听写获取 McKusick 对 vi 命名的具体陈述；(3) Kernighan 的 TUHS 访谈具体内容未能获取，需后续查找 TUHS 邮件列表归档中 Kernighan 相关访谈记录
- bash 对 csh 功能的吸收程度在不同 GNU 文档中表述不一，需核对 bash 源代码注释；Ken Greer 1981 年合并 tcsh 至 csh 工作的所属机构在不同来源中表述存在分歧——Arch Linux man tcsh 原文标注 “HP Labs, 1981”（机构为 HP Labs），另有来源记 Carnegie Mellon University 时期；两说并存 [存疑脚注：Greer 履历以 29.7/32.6 节考据为准，须以 tcsh 源码注释与当事人自述复核]
- PDP-11 上 2BSD 的最后维护版本号在不同史料中不一致，需核对伯克利发布记录
- vim 与 vi 的兼容性程度在不同版本中存在差异，需核对 vim 兼容性文档；vim 首次公开发布时间为 1991 年 11 月（Fred Fish Disk #591），1988 年仅为 Moolenaar 在 Amiga 上的个人开发起点；nvi 为 4.4BSD-Lite（1994 年春发布）而开发，~~先前叙述 “nvi（Keith Bostic 1992 年）” 系年份错误~~（修正：1992 年 elvis 被引入 BSD 用作临时 vi 替代，nvi 则是 Bostic 在 **1994 年** 为 4.4BSD-Lite 重写的版本）
- [考据完成：2026-07-29 经 TUHS utree 各版本 csh man page 直接访问核查，原 “具体版本号对照需后续从 TUHS 归档 tar.gz 包中提取比对” 的存疑标注现予以撤销并改为确证] csh man page 各版本 TH 行与内部日期已通过 TUHS utree 直接访问逐一核查确认：(1) **2BSD csh.u**（1979-02-24，TH 行 `.TH CSH UCB 2/24/79 UCB`，csh 1.0，Joy 编写，文件位于 `man/csh.u`，使用 `.u` 后缀——伯克利本地 man page 卷，非标准 `csh.1`）；其后 3BSD（1979-11-07）、4BSD（1980-09-28）、4.1cBSD（1983-02-09）、4.2BSD（1983-07-18）、4.3BSD（1986-06-05）、4.3BSD-Reno（1990）、4.4BSD（1994）各版本 TH 行与内部日期亦逐一核查确认，详见 28.5 节辨析

## 文献

- Joy, W. (1979) “2BSD Release Announcement”（TUHS 归档 2bsd_announcement.pdf，<https://www.tuhs.org/Archive/Distributions/UCB/Documentation/2bsd_announcement.pdf>）；Joy, W. (1978) “An Introduction to Display Editing with vi”（2BSD 随附手册）；Joy, Bill. Oral History [EB/OL]. Computer History Museum, 2011-03-30. Catalog Number 102743073. <https://www.computerhistory.org/collections/catalog/102743073/>；BSD Now. Episode 278: The Real McCoy [audio podcast]. 2018-12-27. <https://www.bsdnow.tv/278> ［A］
- Arch Linux man **tcsh(1)** “AUTHORS” 节（HP Labs 1981 标注）；Fox, B. (1989) “Bash Reference Manual”；Loukides, M. (1990) “Programming with GNU Software”；Falstad, P. (1990) zsh 0.1 发布公告，comp.sources.misc 新闻组（zsh.sourceforge.io 项目历史存档） ［A］
- DEC (1990) “PDP-11 End of Life Announcement”；伯克利 CSRG 维护日志［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Moolenaar, B. (1991) Vim 1.14 首次公开发布（Fred Fish Disk #591）；Moolenaar, B. (1992) Vim 1.22 移植到 UNIX 并更名 “Vi IMproved”；Bostic, K. (1994) nvi for 4.4BSD-Lite；Joy, W. (1978) “vi User's Manual”；Kirkendall, S. (1990) elvis editor［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］
- Joy, W. (1978) “An Introduction to the C Shell”（2BSD 随附手册，TUHS 归档 2bsd.tar.gz）；**TUHS utree 各版本 csh man page 直接链接**（2026-07-29 联网核查确认均可访问）：2BSD csh.u（<https://www.tuhs.org/cgi-bin/utree.pl?file=2BSD/man/csh.u>）；3BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=3BSD/usr/man/man1/csh.1>）；4BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4BSD/usr/man/man1/csh.1>）；4.1cBSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.1cBSD/usr/man/man1/csh.1>）；4.2BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/man/man1/csh.1>）；4.3BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD/usr/man/man1/csh.1>）；4.3BSD-Reno csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD-Reno/src/bin/csh/csh.1>）；4.4BSD csh.1（<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/src/bin/csh/csh.1>）；1BSD/man1/ 目录（<https://www.tuhs.org/cgi-bin/utree.pl?file=1BSD/man1>，确认 1BSD 不含 csh man page）；2BSD/man/ 目录（<https://www.tuhs.org/cgi-bin/utree.pl?file=2BSD/man>，确认 2BSD man page 均使用 `.u` 后缀）；TUHS 归档 tar.gz 包：2bsd.tar.gz（<https://www.tuhs.org/Archive/Distributions/UCB/2bsd.tar.gz>）、3bsd.tar.gz（<https://www.tuhs.org/Archive/Distributions/UCB/3bsd.tar.gz>）、4.2BSD/（<https://www.tuhs.org/Archive/Distributions/UCB/4.2BSD/>）；项目本地 `03-原始史料库/02-man源与posix仓库/01-repos/openbsd-src/bin/csh/csh.1`（OpenBSD 现代 csh man page） ［A］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP352（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 本期主话题是 NetBSD 内核对随机数生成机制的重写，目标是把熵池升级到满足 256 位不可预测性等新期望。（BSD Now EP352，[182.96-190.12]，L2）
- 主持人的核心判断是：随机数在操作系统中多处不可或缺，现代系统通常把 RD-RAND、RD-SEED 等硬件输出与哈希混合，单一熵源失效不应击穿整个系统。（BSD Now EP352，[159.08-178.48]，L2）
- 新闻部分记载 NetBSD core team 人事变动：Matt Thomas 在服务十余年后卸任，Robert Elz 受邀加入；同期 FreeBSD core team 进行两年一度的民主选举。（BSD Now EP352，[764.8-901.42]，L2）

**史料**：

- NetBSD rnd(4) 手册页及其引用的随机性论文，节目提示可阅读 rnd(4) 了解熵源设计。（BSD Now EP352，[448.56-454.56]，L2）
- NetBSD 公告邮件列表中 Alistair Crooks 发布的 core team 变更公告，记载 Matt Thomas 的 ELF、VAX 维护与 GCC 贡献。（BSD Now EP352，[764.8-788.16]，L2）
- Bill Joy 1999 年 Linux Magazine 采访与 2003 年离任 Sun 时的报道，提及 BSD Unix、NFS、UltraSPARC、Java 与 1976 年创作的 vi。（BSD Now EP352，[1860.4-1891.92]，L3）

**史观**：

- 总纲10 动手者创造历史：Matt Thomas、Robert Elz 等长期维护 ELF、VAX、shell 与 POSIX 的动手者构成社区治理的实质基础。（BSD Now EP352，[764.8-810.32]，L2）
- 总纲9 经验优先：开发者对 Allwinner ARM 真随机数设备实测统计测试，发现输出高度偏置，遂以经验判定不能仅依赖该硬件熵源。（BSD Now EP352，[366.88-377.24]，L2）

**辨析**：

- 转写中‘Robert Ells’ 疑为 Robert Elz，写作时须以 cross_indexes.duckdb 译名表校正，不宜直接照搬语音转写。　[存疑脚注] 转写人名拼写存疑（BSD Now EP352，[764.8-800.48]，L4）
- 转写中‘Rastrad’ 等拼写疑指 NetBSD 开发者 Riastradh（Taylor R Campbell），其 Allwinner RNG 驱动与统计测试的准确姓名需另核。　[存疑脚注] 转写人名拼写存疑（BSD Now EP352，[366.88-377.24]，L4）

**文献**：

- [BSD Now EP352] Pennington J. BSD Now: 352: Introducing Randomness[EB/OL]. (2020-05-28)[2026-08-15]. <https://www.bsdnow.tv/352>.

<!-- /PODCAST_REVIEW -->
