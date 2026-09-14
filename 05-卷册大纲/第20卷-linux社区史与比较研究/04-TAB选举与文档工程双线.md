# 04 【Linux社区】TAB选举与文档工程双线

> **性质**：13-deepseek-linux 战线 P4 大纲增补（ksummit-discuss 主题审读产物）
> **来源**：ksummit-discuss p69（2016-11 会后一周线程 + KS2014 混档 6 封，pk 347656–347705）
> **建立**：2026-09-11（p69 审读当页新增，新节奏“当页入库+当页入大纲”）
> **关联**：claim DSLXC-3913..3946（34 条）均已入 `dslinux_claims.duckdb`

## 【Linux社区】零、自反性声明

本块系对 KS2016 会后一周邮件的形式化提取，两条主线（TAB 选举、Sphinx 图像管线）均为组织史/工程史一手语料；KS2014 混档 6 封单独归块。邮件多为事务性协调，史家判断仅在“辨析”中给出。

---

## 4.1 【Linux社区】TAB 2016 选举全程（Rostedt / Mason / Anvin / Pinchart）

- **要点**：Steven Rostedt 主持 Linux Foundation 技术顾问委员会（TAB）选举——8 候选人（Triplett/Riel/Taht/Mason/Williams/Starovoitov/Petersen/Johansson），LPC+KS 全体与会者可投；结果 108 票：Chris Mason 81、Olof Johansson 72、H. Peter Anvin 61、Dan Williams 59、Rik van Riel 55（第六名 44）；Laurent Pinchart 质询“为何不公布完整票数”，Mason 披露全程：Grant/Steve/Shuah 三人手工计票互验，SDAPS 光学扫描 108 票仅漏 1 误 0、GUI 逐票核验，扫描仪按“能塞进行李箱的最快型号”选购。
- **史料**：DSLXC-3915/3918/3920/3921/3922（347658/347661/347663/347664/347665）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347658 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347661 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347663 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347664 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347665 -->`
- **史观**：多方平等（总纲 8：质询与被质询并录）；动手者叙事（总纲 10：选票扫描仪的行李箱细节）；偶然性优先（总纲 5：SDAPS 系 hpa 个人提议）
- **辨析**：这是 TAB 选举机制从纯手工向机读过渡的孤本记录——SDAPS 开源包（hpa 自荐实现选票系统，见 347658 自荐信“I also implemented the system for handling the ballots for this year's election”）；“不公布全票”的解释（保护落选者再次参选意愿）是社区政治的微妙样本
- **文献**：DSLXC-3915/3918/3920/3921/3922（`ksummit-discuss.messages.347658/347661/347663/347664/347665`，2016-11-01/03 TAB 2016 选举线程），全文见 `raw_source.raw_json`
- **落点**：卷 4“Linux 治理”或“技术委员会选举机制”（原记“第 24 卷”不存在，卷位待定并登记挂账）

## 4.2 【Linux社区】H. Peter Anvin 的 TAB 自荐陈述（1992-2016 履历自述）

- **要点**：hpa 自述：1992 年初入 Linux；Intel Senior Principal Engineer 8 年；tip tree 与 x86 架构共同维护者近 10 年；实现过内核、用户态与引导层（Syslinux）多个子系统；在 Intel 的使命是“与 CPU/固件设计师对接使硬件对 Linux 更友好”；近年自任 gcc/llvm 社区非正式联络人，“接口摩擦的减少与此有关”；1997 年创建 kernel.org。
- **史料**：DSLXC-3917（347660）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347660 -->`
- **史观**：动手者创造历史（总纲 10）；经验优先（总纲 9：第一人称履历）
- **辨析**：此为 hpa 唯一一份完整的自我定位陈述——“infrastructure 是被忽视的、对后续开发征收长期税（technical debt）的方面”是其技术哲学核心句；与 McKusick 式 BSD 老将履历对勘有结构史价值；自荐信亦坦承“我有过度工程化的倾向”
- **文献**：DSLXC-3917（`ksummit-discuss.messages.347660`，2016-11-02 hpa 自荐陈述），全文见 `raw_source.raw_json`
- **落点**：人物志（hpa 条目）/“开发者自述史料”（原记“第 24 卷”不存在，卷位待定并登记挂账）

## 4.3 【Linux社区】复杂依赖会议纪要（Luis R. Rodriguez 长文）

- **要点**：Luis 发布 KS2016 complex dependencies 两场会议+走廊追踪纪要——原目标：找出哪些子系统用图表达依赖并做拓扑排序、能否抽象共享；七子系统盘点：DAPM（TBD）、component（DRM/ALSA，commit 2a41e6070dd7e）、v4l2-async、x86 PCI IOMMU（memmove 简单排序+ELF 特殊节）、ACPI（隐式序，无显式拓扑排序）、media controller（图导出用户态）、linker tables（开发中）；依赖环最坏 NP 完全否则线性；共识“按操作/设备类型用图表示设备”；Rafael 补丁不排序、依赖 ACPI 隐式序；DT 依赖注记于节点而 struct device 不存在——框架复用受限。
- **史料**：DSLXC-3932（347685）、DSLXC-3925/3926（347670/347672）、DSLXC-3916/3913（347659/347656）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347685 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347670 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347672 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347659 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347656 -->`
- **史观**：动手者叙事（总纲 10：纪要即工作）；循环结构呈现（总纲 4：与 p62-64 设备探测讨论同题回归）
- **辨析**：纪要中“Andrzej Hajda 缺席、无人熟悉其补丁，故评审全依 Rafael 补丁”是会议知识的偶然性实证；Marek 的 Exynos IOMMU of_xlate 建 links 实作（347672）是“补丁先行于框架”样本；本块与 03 文件 3.1（generic drivers）同属“设备层依赖”支线
- **文献**：DSLXC-3913/3916/3925/3926/3932（`ksummit-discuss.messages.347656/347659/347670/347672/347685`，2016-11-01/07），全文见 `raw_source.raw_json`
- **落点**：设备层对照（原记“卷 20/22”有误：卷 20 即本卷，卷位待定并登记挂账）；“deferred probe 之史”一节

## 4.4 【Linux社区】Sphinx 图像管线之争（Mauro / Jani / Markus / Corbet 四方）

- **要点**：KS 后 Mauro 传达两决定（不加通用命令扩展；PDF 图像运行时生成）并求方案——三条路：复制 rst 到输出目录/扩展调 ImageMagick/骗 Sphinx 把输出目录当源目录；Jani 提 svg 直通双案（raw latex/指令扩展）并反对复制（“我们是来解决问题的不是制造新问题”：时间戳、依赖分析、in-tree 一致性）；Markus Heiser 主张 sourcedir 置 O= 目录并发 POC 补丁（cp -sa sync）；Jani 拒绝参与（“Sorry, I do not wish to be part of this.”次日道歉，自称“unsubstantiated gut feel from experience”）；Mauro 与 Jani 合流：复制致全量重建，扩展才是正解但须有人写；Corbet 终裁方案 2，并点出 \write18（shell 执行）混入构建的安全疑点。
- **史料**：DSLXC-3929/3930/3931（347681/347682/347684）、DSLXC-3934/3935/3939（347688/347692/347697）、DSLXC-3940/3941/3942（347698/347699/347700）、DSLXC-3944/3945/3946（347703/347704/347705）
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347681 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347682 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347684 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347688 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347692 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347697 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347698 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347699 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347700 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347703 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347704 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347705 -->`
- **史观**：多方平等（总纲 8：四方立场全录）；经验优先（总纲 9：“凭经验的直觉”）；动手者创造历史（总纲 10：Markus 的 POC 当日即发）
- **辨析**：①本线程是“内核弃 DocBook 迁 Sphinx（2016）”阵痛的完整切片——PNG 都渲染失败、texlive 的 SVG 支持本质是调 inkscape；②Jani 的道歉与 Markus 的接受（“建一堆符号链接确实 smells”但 O= 与 sourcedir 冲突无他解）是社区摩擦修复的一手样本；③Corbet 对 Mauro 补丁有效性的当面对质（“确定这补丁真修好了你的问题？”——移除图仍复现）是技术纠错的范式；④\write18 安全疑点悬置（Mauro 疑 adjustbox），本书不写“必然解决”，只记时间坐标
- **文献**：DSLXC-3929/3930/3931/3934/3935/3939/3940/3941/3942/3944/3945/3946（`ksummit-discuss.messages.347681/347682/347684/347688/347692/347697/347698/347699/347700/347703/347704/347705`，2016-11-07/14），全文见 `raw_source.raw_json`
- **落点**：“文档工程”/“内核文档体系（Sphinx 迁移 2016-2019）”节（原记“第 27 卷”不存在，卷位待定并登记挂账）

## 4.5 【Linux社区】KS2014 混档档案信实录（本页 6 封）

- **要点**：p69 夹带 6 封 2014 年历史信：Jason Cooper QR oops“cut here”陷阱修复补丁（panic.c/lib/bug.c，改“cut 10 lines above here”，×2）；Jason Cooper QR 容量仅容一 oops；Joerg Roedel IOMMU 隔离（bus master 非 PCI 通用、legacy 32 位 PCI 连坐）；Joerg Roedel 故障上报禁用语义（DMA-API 在用 IOMMU 不能运行时禁用）；Levente Kurusa 附和不强制 app（NV）；Josh Boyer secure boot trusted_kernel 搁浅（LPC 2013 共识再度脱轨，2014-05-02）。
- **史料**：DSLXC-3914（347657）、DSLXC-3924（347668）、DSLXC-3927（347679）、DSLXC-3943（347701）；另 `347690`/`347702` 两封未入候选库〔存疑：无对应 claim 编号，待回源核定〕
- 【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347657 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347668 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347679 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347690 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347702 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347701 -->`
- **史观**：动手者叙事（总纲 10）——归档杂讯本身即史料，列表归档形态
- **辨析**：KS2014 档案混挂在 2015/2016 序列中——落书引用须以 `date` 字段判年，勿按 pk 顺序断代；347701（secure boot 搁浅）与 2016 年后的 secure boot 讨论可成对呈现
- **文献**：DSLXC-3914/3924/3927/3943（`ksummit-discuss.messages.347657/347668/347679/347701`，2014-05-02/12 KS2014 档案信），全文见 `raw_source.raw_json`
- **落点**：KS2014 会议史（QR oops、IOMMU 隔离、secure boot）

## 【Linux社区】五、本页入大纲建议落点

- **主落点**：TAB 选举机制（4.1/4.2）→ 卷 4“Linux 治理”或“技术委员会选举”；Sphinx 文档工程（4.4）→“文档工程”（原记“第 24 卷”“第 27 卷”均不存在，卷位待定并登记挂账）
- **次落点**：复杂依赖纪要（4.3）→ 设备层（原记“卷 20/22”有误：卷 20 即本卷，卷位待定并登记挂账）；KS2014 档案（4.5）→ 历届议题史
- **勿用**：Carpool 5 封纯后勤不入选；本页 34 条为组织史/工程史素材，非技术史主线年表
