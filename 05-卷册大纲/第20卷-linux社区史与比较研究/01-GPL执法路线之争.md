# 01 【Linux社区】GPL执法路线之争

> **性质**：13-deepseek-linux 战线 P4 大纲增补（ksummit-discuss 主题审读产物）
> **来源线程**：[CORE TOPIC] GPL enforcement（ksummit-discuss 2016-08，p57-p60，pk 347063–347165 区间）
> **建立**：2026-09-10 首建（P4 首次增补）；2026-09-11 依 claim 库重建（原文件丢失，以 `dslinux_claims.duckdb` 为唯一反查源）
> **关联**：claim 均坐落在 `dslinux_claims.duckdb` claim 表（`source_ref=ksummit-discuss.messages.<pk>`），每条以 `<!-- ROW_MINE: ... -->` 锚定

## 【Linux社区】零、自反性声明

本增补块为按编纂方法论对 ksummit-discuss 邮件的一手提取，非对“GPL 执法史”的总体裁断；所书系对讨论的形式化重构，直线式叙事不声称呈现“真实的 Linux 历史”。引用一律保留当事人原句，史家判断与当事人自述以“辨析”区分。

---

## 1.1 【Linux社区】GPL 执法的历史形态（SFC 与 Kuhn 视角）

- **要点**：2016 年 8 月 LinuxCon 上，SFC 执行总监 Karen Sandler 迟期提出 GPL 执法议题：“近来新闻很多（Patrick McHardy 执法、社区导向执法原则、VMware 驳回/上诉），引发相当多猜测”。Bradley M. Kuhn 随后给出 0.57% 量化：约 3,000 起 GPL 违规报告仅 17 名被告，并把“把 Linux 变成 GPL 测试案例”的指责反推为“一系列外部事件的汇合在没有我帮助的情况下已经那样做了”。
- **史料**：`ksummit-discuss.messages.347063`（Sandler 提案）、`347085/347095`（Kuhn 两封）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347063 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347085 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347095 -->`
- **史观**：偶然性优先（总纲 5：外部事件汇合而非必然进程）；多方平等（总纲 8：SFC 与内核社区的两种执法观并列呈现）
- **辨析**：本案量化口径（3,000 报告/17 被告）系 Kuhn 现场表述，非官方统计，须与 SFC 年报对勘；“Patrick McHardy 执法”指 2014 年起个人执法、多庭和解，属本讨论此前背景
- **文献**：SFC 官网 enforcement 历史页（2016 版快照见 raw_source）

## 1.2 【Linux社区】程序性否决与“律师在场即风险”机理

- **要点**：Greg KH 以程序理由否决并给出风险机理——“在有些国家/法域，牵涉诉讼的人与别人谈论时，那些别人随后可能被诉讼另一方传唤”“我尽最大努力永远不必在任何事里被质证”；Jiri Kosina 反诘“如果一个人其实并不介意参与，因为他真的相信那场诉讼想达成的东西，并且乐意在需要时作证呢”。
- **史料**：`347065/347082/347084`（Greg 三封）、`347086/347089`（Kosina 两封）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347065 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347082 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347084 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347086 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347089 -->`
- **史观**：动手者叙事（总纲 10：以开发者个体法律风险为分析单位）、经验优先（总纲 9：大陪审团与法域经验）
- **辨析**：Greg 的“律师在场即风险”是内核峰会史上关键的“该不该谈 GPL 执法”程序性争论，直接决定该议题能否获得正式时段；其本人 2016 现场缺席系自主决定（见 347083，不在候选）
- **文献**：本组全部依 `raw_source.raw_json` 全行反查（一线邮件原文为唯一证据源）

## 1.3 【Linux社区】议程筛选与“诉讼 vs 保护”的价值争论

- **要点**：Linus Torvalds 亲自下场十余封，核心判断：“诉讼是毁灭不是保护”“我真正在乎的是把代码贡献收回来——那差不多就是 GPLv2 的全部要点”；以“伤寒玛丽”类比反对把 Linux 做成 GPL 测试案例；区分“公开羞辱”与“法律威胁”两种施压手段，支持前者。
- **史料**：`347105/347107/347109/347130/347139/347141/347147/347155`（Linus 序列）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347105 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347107 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347109 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347130 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347139 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347141 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347147 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347155 -->`
- **史观**：拒绝进步叙事（总纲 3：Linus 认为“现在比 15 年前好得多”非必然）、动手者创造历史（总纲 10：把镜头对准日常合规谈判）
- **辨析**：Linus 与 Matthew Garrett 的“编码贡献 vs 代码可得性”之争（347156 Garrett）是全线程哲学分歧点，须同时呈现两造原句
- **文献**：本组 claim 为一线邮件，直接著录 `raw_source`

## 1.4 【Linux社区】反方证据：诉讼作为协商的底线

- **要点**：David Woodhouse“没有诉讼这个选项，就没有协商”“如果 GPL 没有法律支撑，你不如用 BSD 许可证”（347158）；Jeremy Allison（Samba 核心、SFC 董事）以 Samba 与微软反垄断案举证“成功诉讼完全无益”，并谴责“引文脱离语境”的媒体报道。
- **史料**：`347158/347156/347159` 三封
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347158 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347156 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347159 -->`
- **史观**：经验优先（总纲 9：一手诉讼经历）、多方平等（总纲 8：Samba/FSFE 与 Linux 内核两种执法传统）
- **辨析**：Woodhouse 的“BSD 许可证”悬崖论证是理解本社区为何不放弃 GPL 的关键句，但须注意其目标受众是“主张放任者”而非贬低 BSD；时间与授权均须以 raw_source 原文为准。
- **文献**：本组 claim 为一线邮件（347158/347156/347159），直接著录 `raw_source`；The Register 2016-08 报道为二手参照，仅作语境

## 1.5 【Linux社区】三方的治理追问（Conservancy vs Linus vs Ted）

- **要点**：Theodore Ts'o 把问题提升为治理问题：“归根到底这真的是一个治理问题”，并追问“哪些开发者”、“Conservancy 能否自行挑选它愿听的开发者”；Josh Triplett 把“无问题可辩”逆转为六条可表决清单；Rik van Riel 提“合规设备清单”正向激励（Linksys 案例被 Garrett 反驳，见 347142）。
- **史料**：`347160/347163/347165`（Ts'o）、`347133/347150`（Rik）、`347108/347144`（Linksys 争议）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347160 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347163 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347165 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347133 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347150 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347108 -->`
- **史观**：多方平等（总纲 8：给 SFC、内核核心、第三方辩护权）、偶然性（总纲 5：治理方案由本线程偶然成型）
- **辨析**：Linksys 2008 年诉讼时间线在 Garrett（347142）与 Kuhn（347128）两方叙述中略有出入，须以原始法律文件核对后再入书
- **文献**：The Register 2016-08 报道（347158 引）为二手参照，仅作语境

## 1.6 【Linux社区】版权归属新议题（雇主付费代码的保留态度）

- **要点**：Greg KH 叙事中指出“我们中许多人完完全全为雇主工作”的现实，引出“开发者是否真能关心 GPL 执法”的存在论问题（Luis Rodriguez 提出：“受雇开发者真的能关心 GPL 执法吗？还是这项权利已被许多公司夺走？”），Kosina 则坚持个人/雇主关系“首先要在个人与其雇主之间解决”。
- **史料**：`347078`（Rodriguez）、`347071/347073`（Greg/Kosina）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347078 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347071 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347073 -->`
- **史观**：动手者叙事（总纲 10）——真正关心执法的是个人而非机构；经验优先（总纲 9）
- **辨析**：雇主付费代码的保留态度（Rostedt 立场）在本线程末（非候选）另有展开，本节只在主线程口径收录
- **文献**：本组 claim 为一线邮件（347078/347071/347073），直接著录 `raw_source`

## 1.7 【Linux社区】会议机制史：LLW 与“律师在场”先例

- **要点**：Greg KH 称（2020 年）“律师参与 GPL 辩护会让社区负上法域风险至今无人敢承接讨论”；Sandler 反诘“会议有录音吗？出席会被记录吗？”，并指对方公开自己邮件列表（“你引 LWN 评论原文”）本身即示范“公开讨论可以无风险”。
- **史料**：`347070`（Woodhouse 反诘）、`347072`（Sandler 录音/出席留痕追问）、`347093`（Greg 程序性处理）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347070 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347072 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347093 -->`
- **史观**：权力再分配（总纲 3）；法律与道德是利益分配（总纲 13）
- **辨析**：此“先例”是理解 2020-2025 年 Linux 基金会 GPL 执法沉默的关键背景，可作为第 19 卷 BSD 史编纂学（第 350-352 章）“GPL 执法史”节素材
- **文献**：`raw_source` 全行可反查

## 【Linux社区】七、本线程入大纲建议落点

- **主题**：GPL 执法与开源许可证政治（对应 `05-卷册大纲` 第 08 卷诉讼讲述、第 15/16 卷“许可证哲学与法律分析／开源运动与合规治理”重构卷位（卷位待定，登记挂账））
- **建议节**：Linux 社区 GPL 执法的内部争论（2016）一节，含“名额、执法论证的两种路线”〔存疑：“Comunicação vs 治理”“SFC 的 Corner 历史角色”二语未能在本线程原始邮件（p57-p60）及候选库中复核，疑为转写讹误，待回源核定〕
- **考量**：本线程是内核社区“社区- 机构- 公司”三方张力的一次完整实况记录，且**Linus 亲自下场**（罕见），对“Linux 文化挪用研究”“BSD 与 Linux 执法对比”均有对照价值（BSD 侧无此类 SFC 类机构，见 04-现代研究文献/08-linux文化挪用研究）