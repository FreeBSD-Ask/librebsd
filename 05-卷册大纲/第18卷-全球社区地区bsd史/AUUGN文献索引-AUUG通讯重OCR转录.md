# AUUGN 文献索引——AUUG 通讯重 OCR 转录

> **转录批次**：TB2（任务书 2，即 OCR2，ref 3424–3665 段）重 OCR 首批接线，2026-09-29
> **覆盖范围**：AUUGN-V22.1（ref 3424），1 件、62 页
> **转录方法**：GLM-4.6V 视觉逐页转录，替代原 rapidocr_onnx
> **数据库状态**：已入库，`fulltext.extraction_method='glm_vision_20260924'`
> **key_facts**：30 条（`fact_category='periodical_primary'`、`confidence='2'`）
>
> **2026-09-29 增补（OCR1／任务书 1）**：本文件范围自 1 件扩至 3 件 152 页——新增 AUUGN-V02.5（ref 3334，28 页）与 AUUGN-V21.4（ref 3423，62 页），均为 GLM 视觉逐页转录、`extraction_method='glm_vision_20260924'`。
> 上方「覆盖范围」「key_facts」两行为接线时（仅 ref 3424）所记，现况以下文「数据库留痕补记」为准；3424 那行所记 `periodical_primary` 30 条经 2026-09-29 复核**与库内实况不符**，已就地标注，未改动 3424 的任何既有行。


本文件为**卷级文献索引**，按 TB4 先例（`第01卷-unix的起源/TB4文献索引-早期UNIX文档与工具.md`）体例。
不改动任何章节正文、不引入新锚点格式、不修改 `SUMMARY.md` 与 `chapter_keywords.json`。
「说明」依转录原文逐页核读后撰写。

AUUGN 全集（V01.1 至 V22.x，约 228 件）已整体登记在本卷卷末书目述评
「附：SFU PUPS 存档增补清单（待迁移）」附录中，该件为清单第 **213** 项。
本附录的整改说明要求「正式归置应依《镜像站挖掘与 OCR 流水线规则》迁往镜像站挖掘指向的正式目录，迁移时整节移出」——**本文件即该迁出动作的第一步**，仅覆盖已重 OCR 入库的部分，未入库件不在此列。

## 文献清单

### 用户通讯（AUUG Newsletter）

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3424 | AUUGN-V22.1（AUUG Newsletter） | 62 | 2001 | 澳大利亚 UNIX 用户组（Australian UNIX User Group）通讯第 22 卷第 1 期。卷首为 AUUG 会员与总务联络块：The AUUG Secretary，PO Box 366, Kensington NSW 2033，电话 02 8824 9511／免拨长途 1800 625 655，传真 02 8824 9522，邮箱 auug@auug.org.au；管理委员会议事邮箱 auugctee@auug.org.au；**主席 David Purdue**（iPlanet e-commerce solutions，South Melbourne VIC 3205）、**副主席 Malcolm Caldwell**（Northern Territory University）。并载明 2001 年各期截稿期：Vol 22 No 2（2001 年 6 月号，截稿 5 月 17 日）、No 3（9 月号，8 月 17 日）、No 4（12 月号，11 月 17 日）；编委会邮箱 auugn@auug.org.au，**主编 Con Zymaros**。**件号 V22.1 与正文所载 V22.2–V22.4 截稿期并存，故本件为第 22 卷第 1 期，即 2001 年初刊** |
| 3423 | AUUGN-V21.4（AUUG Newsletter，2000 年 12 月号） | 62 | 2000 | 澳大利亚 UNIX 用户组通讯第 21 卷第 4 期，本年最后一期，新任主编的第一期，接替担任主编逾四年的前任。卷首为 AUUG 总务与管理委员会名单——主席 David Purdue（iPlanet e-commerce solutions，South Melbourne VIC 3205）、副主席 Malcolm Caldwell（Northern Territory University，Casuarina 校区）、秘书 Michael Paddon（eSec Ltd）、司库 Luigi Cantoni（STM）。实质篇目：①FreeBSD 官方 i386 安装手册全文连载（署名 Jordan K. Hubbard，第 13–17 页；载明 386 以上处理器、安装需 5MB／运行需 4MB RAM、最小 100MB 磁盘、El Torrito 可启动 CD 标准与 boot.flp 网络安装路径、FreeBSD 安装 CD 由 Walnut Creek CDROM 提供）；②NetBSD 专栏（「thirty different system architectures featuring eleven distinct families of CPUs」，平台跨度自 64 位 AlphaServer 至手持设备）；③linux.conf.au 讲题清单（Keynote Speakers：Alan Cox、Dave Miller、Tridge）；④AUUG 开源研讨会讲题纪要，含 **Greg Lehey: Revamping the FreeBSD SMP implementation**；⑤AusCERT（澳大利亚计算机紧急响应小组）入侵恢复步骤指南，第 47–54 页；⑥87 家公司会员名录（截至 2000-12-01），覆盖政府统计机构、国家研究体系、十一所大学与数十家企业（含 SCO、BHP、CSIRO、C.I.S.R.A.、ADFA、Motorola Australia、Nokia Australia、Qantas Information Technology）；⑦2000 年 11 月连办 AUUG Security Symposium 与 Australian Open Source Symposium，两者均为第二届；⑧红帽 Linux 7 广告页 |
| 3334 | AUUGN-V02.5（AUUG Newsletter，1980 年 6–7 月号） | 28 | 1980 | 澳大利亚 UNIX 用户组通讯第 2 卷第 5 期，编者 Peter Ivanov（University of New South Wales）。卷首为 Western Electric 许可限制声明框（「Circulation of this document is restricted to holders of a license for the UNIX software system from Western Electric」）。实质篇目：①1980-07-02 悉尼 AUUG 会议议程，Ken McDonell（Monash）在会上发起「VMS vs UNIX」讨论，CSIRO 一组人报告数据处治／排版／CSIRONET 通信／回归与离群检验统计的 UNIX 化；②Alan Mason（UKUUG）记录的 Stephen Johnson（Bell Labs）1980 年 3 月阿姆斯特丹 Vrije Universiteit 三讲——可移植 C 编译器（Sethi-Ullman 编号、树式代码生成与模板重写）、系统软件可移植性改造（含 Lint 的职责分离理由）、语言驱动的机器设计（为 C 定制的 32 位机与专用零寄存器 Z）；③UKUUG 的 V7 精简发行（McKie／Heriot-Watt、Rosenthal／Edinburgh、Prosser／SRC Rutherford，取消 I&D 分离要求，已在 11/34、11/40、11/45、11/60 测试）；④Dave Rosenthal 的 makefile 增量更新库写法；⑤Bruce Anderson 的 RESET/SETEXTIT 改良（Peter Landin 的 CATCH/THROW，PDP-11 汇编实现）；⑥爱丁堡人工智能系 POP-2 与 Prolog 在 PDP-11／UNIX V6 上的发行（32K 用户地址空间、紧凑垃圾收集器）；⑦ETH 苏黎世 Niklaus Wirth 1980-04-11 预告 Modula-2 的 PDP-11（RT-11）实现将于 1980 年 6 月发布，自注「exactly 10 years after our first release of Pascal」；⑧Vrije Universiteit Tanenbaum 组 1980 年 5 月发布的符合 ISO 标准的可移植 Pascal 编译器（EM-1 中间码，PDP-11／UNIX V6 与 V7 两条发行带）；⑨VAX SPITBOL 的 UNIX 版 1980-06-06 完成；⑩Ian R. Perry 谈 L.E.R.S.（Synthelabo）——自称当时欧洲唯一商业 UNIX 许可持有者，1976 年底起，PDP 11/70 配重改造带实时分区的 V6；⑪grep 方括号竞答与 SP380A 总线占用率表头电路；⑫末页列出悉尼／科尔切斯特／维也纳／多伦多四地 UNIX 通讯编辑人名单，显示用户组通讯已跨境共享编辑责任 |

## 章节关联

- **第 344 章 大洋洲 BSD 社区**：AUUGN-V22.1（3424）——大洋洲（澳大利亚）BSD／UNIX 社区的组织一手资料，含该卷期号的主席／副主席任职、iPlanet 与北领地大学两个机构落点、编委会与截稿期等运作细节。AUUG 是澳大利亚 UNIX 用户组，本件为其 2001 年年度的通讯首期，属「大洋洲 BSD 社区」范畴内的一手组织文献
- **第 344 章 大洋洲 BSD 社区（3423 增补）**：AUUGN-V21.4（3423）——大洋洲 BSD 用户在 2000 年末的入口一手资料：本期是 AUUG 从「UNIX 用户组通讯」转向开放系统综合刊物的转折期（卷首明言「We mix big-vendor Unix platforms, as well as Open Source OSEs and tools」），同期转载 FreeBSD 官方安装手册、报道 FreeBSD SMP 重构与 NetBSD 的移植规模，并连载本地 CERT 的入侵恢复指南。对「344.2 澳大利亚 BSD 用户组与会议」与「344.6 澳大利亚新西兰的 freebsd 部署」两节均有直接支撑 |
- **第 344 章 大洋洲 BSD 社区（3334 增补）**：AUUGN-V02.5（3334）——大洋洲 UNIX 用户组 1980 年的组织一手资料，是本卷「大洋洲 BSD 社区」时序的起点锚：AUUG 与 UKUUG／加拿大 UNIX SIG／美国各通讯同期互编（末页四地编辑人名单），Ken McDonell 在悉尼会议发起 VMS vs UNIX 之争；同期 AUUG 正筹备 1980 年 10 月墨尔本的 World UNIX Conference 并启动 Software Catalogue 工程。对「344.2 澳大利亚 BSD 用户组与会议」的起点时段、以及「344.1 澳大利亚 BSD 社区的历史」中 1980 年代的 UNIX 用户组脉络有直接支撑 |
- **本卷「待迁移」附录**：本件（清单第 213 项）自 `卷末书目述评.md` 的 SFU PUPS 增补清单迁出至此；同段内 AUUGN-V01.5／V02.3／V02.4／V03.1–V03.6（ref 3712–3718）及 V03.4–V03.6（ref 3719–3721，已归第01卷 TB4 索引）等件为重 OCR 后续批次的候选，**尚未重 OCR 者不列入本文件**

## 转录质量说明

- 62 页经 GLM-4.6V 视觉逐页转录，`extraction_method` 为 `glm_vision_20260924`
- 本件为网页打印型 PDF 的转录：每页页眉含抓取时间戳（形如 `2026/8/6 14:41`）与源网址 `theos.com/deraadt/coremail.html`，属转录源的载体信息而非原刊内容，正文引用时应剔除
- 第 2 页起为纯序号列（`#      44` 至 `#      68`），是原刊的页码索引桩，无正文信息

## 数据库留痕

- `fulltext`：1 件更新，`extraction_method='glm_vision_20260924'`
- `fulltext_blocks`：62 块（`block_type='ocr_glm_vision'`）
- `key_facts`：30 条，`fact_category='periodical_primary'`、`confidence='2'`
- `references.year` 本件为 NULL（通讯内无单一年份标示，年代 2001 取自卷号 V22 与正文载明的 2001 年各期截稿期）
- 本文件**未改动** `chapter_matches`、`chapter_reviews`、`SUMMARY.md`、`chapter_keywords.json` 与任何章节正文
### 数据库留痕补记（2026-09-29 复核与增补）

- 新增 3334 与 3423 的 `fulltext` 更新与 `fulltext_blocks` 块（`block_type='ocr_glm_vision'`、`block_page` 为 1..28 与 1..62 的连续字符串、`block_index` 为 0..N-1）；`extraction_method='glm_vision_20260924'`、`extraction_notes='GLM 视觉逐页转录（原 rapidocr/扫描件替换）'`。
- `key_facts` 新增 17 条：`kf-tb1-3334-000..008`（9 条）、`kf-tb1-3423-000..007`（8 条），`fact_category='periodical_primary'`、`confidence='2'`、`related_chapter='第18卷-全球社区地区bsd史'`；每条 `source_quote` 均断言为不含换行、且逐字出现在该件某页单行内的片段。
- `id` 采用 `kf-tb1-` 字符串前缀（与 `kf-tb3-`／`kf-tb4-` 同族），按构造避免与并发会话争抢数值号段；本件不占用数值 id。
- **复核发现（未改动 3424 的任何行）**：上方「`key_facts`：30 条（`fact_category='periodical_primary'`、`confidence='2'`）」经 2026-09-29 实测**与库内实况不符**——ref 3424 的 30 条实为 `kf-batch-3424-000..029`，`fact_category` 为 `technology` 27 条与 `person` 3 条，`confidence` 为 `0.7`，`fact_text` 形如「unix mentioned (93 times)」，属词频统计行而非逐字一手引文。该 30 条属 TB2（任务书 2）范围，本文件仅如实标注、不作修改，是否回滚为逐字引文版待 TB2 线裁定。
- 3424 在本文件中仍记 62 页、1 件；增补后本文件覆盖 3 件 152 页（28 + 62 + 62）。


---

**生成日期**：2026-09-29
**2026-09-29 增补后**：总页数 152，总件数 3（3334 28 页 + 3423 62 页 + 3424 62 页）

**转录批次**：TB2（任务书 2 / OCR2）首批接线
**总页数**：62
**总件数**：1
