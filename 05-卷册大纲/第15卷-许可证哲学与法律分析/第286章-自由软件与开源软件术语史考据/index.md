---
chapter: 第 286 章
id: CH286
volume: 第15卷-许可证哲学与法律分析
---

# 第286章 自由软件与开源软件术语史考据

## 史料

- [DB:research_notes:blocks:480177] 关键词“开源软件术语史考据”命中：第十一卷第 135 章 BSD vs GPL 哲学辩论（在 135.10 节“许可哲学光谱”前增补 135.10.0 子…

## 要点

- 自由软件基金会（Free Software Foundation，FSF）成立于 1985 年 10 月，初期宗旨是为 GNU 工程筹集资金。理查德·斯托曼（Richard Stallman）撰写的《GNU 宣言》（GNU Manifesto）于 1985 年首次发布，正文中多次使用“free”一词描述软件，例如“complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it”以及“to put together a sufficient body of free software so that I will be able to get along without any software that is not free”。但《GNU 宣言》中的“free”一词并未严格区分“自由”与“免费”两层含义，斯托曼本人在 1983 年 9 月 27 日 GNU 初始公告脚注中明确承认“当时的用词并不是特别小心……后来，我意识到要在‘free’的自由之意和‘free’的价格之意间做认真的区分”。因此从一手文献角度，“free software”作为术语在 1985 年《GNU 宣言》中已有正式使用，但其语义在该时期尚未严格化为后世 FSF 定义的标准定义。
- FSF 官方“The Free Software Definition”页面（gnu.org/philosophy/free-sw.html）脚注 1 明确记载四项自由编号的历史：“使用 0、1、2 和 3 排列这些自由有历史的原因。在 1990 年左右，列出来的自由是 1、2 和 3。然后，我们意识到运行软件的自由也应该明确列出来。这个自由显然比另外 3 个自由更基本，所以应该列在前面。我们没有修改其他 3 个自由的序号，而是将运行软件的自由列为 0。”据此可确证：1990 年左右自由软件定义列出三项自由（编号 1、2、3），后增加“运行程序的自由”为 freedom 0，形成 freedom 0/1/2/3 的格局，该编号方式延续至今。现行四项自由的官方表述为：freedom 0 运行程序的自由、freedom 1 学习并修改源代码的自由、freedom 2 再分发拷贝的自由、freedom 3 分发修改版的自由。
- FSF 官方“What is Free Software?”文档中出现的“think of 'free' as in 'free speech,' not as in 'free beer'”口号是当代自由软件运动的标志性表述。但 FSF 官方文档并未明确标注该口号首次提出的具体时间与场合。GPL v1（1989 年 2 月）前言中已包含相关表述：“When we speak of free software, we are referring to freedom, not price.”GPL v2（1991 年 6 月）前言同样保留该表述。据此可确证：至晚在 1989 年 2 月 GPL v1 发布时，“free software 指自由而非价格”的核心表述已经形成。但“free speech, not free beer”这一具体口号化的表述首次提出时间与提出者，在公开的一手文献中无法精确考证。
- GNU 通用公共许可证第 1 版（GPL v1）发布于 1989 年 2 月，前言中阐述了“自由软件”的核心定义并通过版权（copyright）与许可证（license）两步保护用户自由。关键考据发现：GPL v1（1989 年 2 月）全文未出现“copyleft”一词，GPL v2（1991 年 6 月）全文同样未出现“copyleft”一词。即“copyleft”一词并非 GPL 文本本身的术语，而是斯托曼在 GNU 工程文档中独立阐述的概念。斯托曼在《The GNU Project》一文中明确阐述：“GNU 的宗旨是给用户自由，而不只是变得流行。所以我们需要使用禁止让 GNU 软件变成专属软件的发布条款。我们所用的方法叫做‘copyleft’。”FSF 官方“What is Copyleft?”页面（gnu.org/licenses/copyleft.en.html）系统阐述了 copyleft 的词源与机制："Proprietary software developers use copyright to take away the users' freedom; we use copyright to guarantee their freedom. That's why we reverse the name, changing‘copyright’into‘copyleft.’“关于”left"一词的含义，FSF 官方文档明确指出“The‘left’in‘copyleft’is not a reference to the verb‘to leave’—only to the direction which is the mirror image of‘right.’”即“left”并非动词“留下”之意，而是与“right”（右）镜像对应的“左”。
- OSI 官方历史页面（opensource.org/about/history-of-the-open-source-initiative）记载："The’open source'label was created at a strategy session held on February 3rd, 1998 in Palo Alto, California, shortly after the announcement of the release of the Netscape source code.“即”open source"标签于 1998 年 2 月 3 日在加州 Palo Alto 的战略会议上创建，时值 Netscape 宣布发布其浏览器源代码之后不久。OSI 官方历史继续陈述："Brainstorming for this new label eventually converged on the term’open source', originally suggested by Christine Peterson.“即与会者认为需要一个统一标签来区别于哲学与政治色彩浓厚的”free software“标签，头脑风暴最终汇聚到”open source"一词，由 Christine Peterson 最初提议。Foresight Institute 官方页面（foresight.org/1998-the-two-words-that-changed-software/）提供了更为详尽的会议经过叙述：1998 年 2 月 2 日晚 Foresight 在 Los Altos 办公室主持了一次会议，与会者包括 Brian Behlendorf（布莱恩·贝伦多夫）、Michael Tiemann、Todd Anderson、Mark S. Miller、Ka-Ping Yee 以及 Eric Raymond；1998 年 2 月 5 日在 VA Research 举行更大会议商讨推广策略，Todd Anderson 在无关话题的对话中悄然插入该词，会议末期术语问题被正式提出，候选词包括“freely distributable”“cooperatively developed”“free software”“sourceware”，Todd 正式倡导“open source”，Eric Raymond 表示赞同。ESR 于 1998 年 2 月 8 日发布“Goodbye, ’free software'; hello, ’open source‘”一文向社区正式推广。

## 史观

- 总纲第 12 条科学是形式主义：自由软件运动的术语原初形态承载“free”双义，自由软件运动的道德命令传统尚未严格化
- 辨析：
  【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 1.1 节考据结论经 GNU 工程官方页面（gnu.org/gnu/manifesto.en.html）WebFetch 一手核验，《GNU 宣言》正文确含"give it away
- 总纲第 12 条科学是形式主义：四项自由的编号演化反映自由软件运动从“修改-分发”两维向“运行-研究-分发-改进”四维的本体论扩展
- 辨析：
  【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 2.3 节考据结论经 gnu.org/philosophy/free-sw.html WebFetch 一手核验，脚注 1 一手陈述“1990 年左右，列出来的自由是 1
- 总纲第 15 条文化即形式主义：“free as in freedom, not free as in beer”口号是自由软件运动对“free”双义歧义性的显式消歧，标志自由软件运动从术语原初形态向严格定义的过渡
- 辨析：
  【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 1.4 节考据结论经 GPL v1 全文（gnu.org/licenses/gpl-1
- 总纲第 15 条文化即形式主义：copyleft 是斯托曼在 GNU 哲学层面对 GPL 法律机制的概括性命名，是对 copyright 的戏仿，标志自由软件运动从法律机制到哲学概念的层次跃升
- 辨析：
  【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 3.1、3.2 节考据结论经 GPL v1 全文（gnu.org/licenses/gpl-1.0.html
- 总纲第 4 条——分离聚合是永恒规律：1998 年 2 月 Palo Alto 峰会标志“open source”从“free software”阵营的分离起点
- 辨析：
  【查证来源】`原材料/研究/自由软件词源考察/04-开源软件运动术语史.md` 第 1.1、1.2 节考据结论经 OSI 官方历史页面 WebFetch 一手核验“open source”标签于 1998 年 2 月 3

## 辨析

- 【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 1.1 节考据结论经 GNU 工程官方页面（gnu.org/gnu/manifesto.en.html）WebFetch 一手核验，《GNU 宣言》正文确含“give it away free”与“free software”表述；1983 年初始公告（gnu.org/gnu/initial-announcemen
- 【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 2.3 节考据结论经 gnu.org/philosophy/free-sw.html WebFetch 一手核验，脚注 1 一手陈述“1990 年左右，列出来的自由是 1、2 和 3”，“我们没有修改其他 3 个自由的序号，而是将运行软件的自由列为 0”；现行四项自由表述经同一页面一手核验
  【交叉验证方法】两层
- 【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 1.4 节考据结论经 GPL v1 全文（gnu.org/licenses/gpl-1.0.html）WebFetch 一手核验，前言确含"When we speak of free software, we are referring to freedom, not price"；GPL v2（1991 年 6 月）前言同样保留该表述（经 286.1 子节同源考据核验），原截断部分已据此补全。
- 【查证来源】`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 3.1、3.2 节考据结论经 GPL v1 全文（gnu.org/licenses/gpl-1.0.html）与 GPL v2 全文（gnu.org/licenses/old-licenses/gpl-2.0.html）WebFetch 一手核验，两版全文均未出现“copyleft”一词；斯托曼自述《The GNU Project》
- 【查证来源】`原材料/研究/自由软件词源考察/04-开源软件运动术语史.md` 第 1.1、1.2 节考据结论经 OSI 官方历史页面 WebFetch 一手核验“open source”标签于 1998 年 2 月 3 日在 Palo Alto 创建；Foresight 官方叙述 WebFetch 一手核验 1998 年 2 月 2 日晚 Los Altos 会议与 2 月 5 日 VA Res

## 文献

- 斯托曼《GNU 宣言》（1985）［A］；斯托曼 1983-09-27 GNU 初始公告 ［A］；斯托曼《The GNU Project》［A］；GNU 工程概述页 ［A］；`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 1.1、1.3 节
- FSF“The Free Software Definition”［A］；FSF“Categories of Free and Nonfree Software”［A］；斯托曼《The GNU Project》［A］；`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 2.1、2.3 节
- GPL v1（1989-02）前言 ［A］；GPL v2（1991-06）前言 ［A］；FSF“What is Free Software?”［A］；`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 1.4 节
- GPL v1（1989-02）全文 ［A］；GPL v2（1991-06）全文 ［A］；斯托曼《The GNU Project》［A］；FSF“What is Copyleft?”［A］；FSF“Categories of Free and Nonfree Software”［A］；`原材料/研究/自由软件词源考察/03-自由软件运动术语史.md` 第 3.1、3.2 节
- OSI 官方历史页面 ［A］；Foresight Institute 官方页面 ［A］；ESR“Goodbye, ’free software'; hello, ’open source‘”（1998-02-08）［A］；Christine Peterson 自述 ［A］；`原材料/研究/自由软件词源考察/04-开源软件运动术语史.md` 第 1.1、1.2、1.4 节
- OSI 官方历史页面 ［A］；OSD 现行版本 ［A］；Debian 社会契约 ［A］；OSI 官方许可证列表 ［A］；`原材料/研究/自由软件词源考察/04-开源软件运动术语史.md` 第 1.5、3.1 节
- 斯托曼“Why Open Source Misses the Point of Free Software”［A］；GNU 哲学页面“Free Software for Freedom”［A］；ESR“Goodbye, ’free software'; hello, ’open source‘”［A］；`原材料/研究/自由软件词源考察/04-开源软件运动术语史.md` 第 2.1、2.2 节
- ESR“Goodbye, ’free software'; hello, ’open source‘”（1998-02-08）［A］；Foresight Institute 官方页面 ［A］；OSI 官方历史页面 ［A］；斯托曼“Why Open Source Misses the Point of Free Software”［A］；`原材料/研究/自由软件词源考察/04-开源软件运动术语史.md` 第 1.3 节

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
