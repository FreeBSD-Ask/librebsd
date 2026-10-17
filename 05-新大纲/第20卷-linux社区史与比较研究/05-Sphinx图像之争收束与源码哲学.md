# 05 【Linux社区】Sphinx图像之争收束与源码哲学

> 本文件衔接 p69 增补文件（03-KS2016会前议题与组织机制史.md）“Sphinx 图像管线之争”主题，记录 2016-11-14 至 11-21 执行落定：Mauro 认错、Linus 定义“源代码”、graphviz+SVG 定调、Corbet 批准进 4.10。
> 本页史料范围 pk 347706–347755（ksummit-discuss 2016-11 线程），全部已入 claim 库（DSLXC-3947..3988）。
> 每块末尾“史料锚”为可反查去重的 ROW_MINE 定位（claim 库 source_ref 一致）。

## 【Linux社区】零、自反性声明

本增补块系对 ksummit-discuss 2016-11-14 至 11-21 文档工程执行线程的一手提取；所书为当事人原话的转述与节选，史家判断仅在“辨析”中给出，不声称该线程即“内核文档史”全貌。本页另混入 4 封 KS2014（2014-05-12）档案信，单独归块并显式划界。

---

## 5.1 【Linux社区】认错与技术对质：PNG 并未损坏

**要点**：Mauro 于 11-14 公开认错——此前 Sphinx 图像之争中“PNG 有问题”诊断有误，实为 Sphinx 1.4.5→1.4.8 版本行为差异；认错附带“让 Sphinx 处理 PNG”补丁全文，是可查的公开技术纠错记录。

**史料**：`347706`

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347706 -->`

**史观**：经验优先（总纲 9：以版本差异与补丁实证纠正既有判断）；动手者叙事（总纲 10：纠错由当事人公开完成）
**辨析**：原“PNG 有问题”诊断实为 Sphinx 1.4.5→1.4.8 版本行为差异，非图像格式缺陷；落书引用须注明 Sphinx 版本口径。
**文献**：DSLXC-3947（`ksummit-discuss.messages.347706`，2016-11-14），全文见 `raw_source.raw_json`

---

## 5.2 【Linux社区】规模盘点与邮件系统约束

**要点**：Arnd 指出 gif 与 png 同病，全树二进制除企鹅 logo 外集中在 Documentation/media；Mauro 补史实：4.8 前图像以 uuencode 提交，VGER 邮件列表静默拒收超长行补丁（SVG 998 列，RFC 2821 行宽约束）——“邮件列表物理层约束源码提交”实证；Arnd 测 pnm 可 patch 化（+25MB）拉 Linus 裁决；Jani 实测 kernel.org 二进制补丁不可 apply。

**史料**：`347707`（盘点）、`347708`（uuencode/998 列）、`347709`（pnm 测损）、`347710`（二进制补丁不可 apply）

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347707 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347708 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347709 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347710 -->`

**史观**：经验优先（总纲 9：以补丁实测与列表拒收记录为据）；动手者叙事（总纲 10：约束由一线提交者亲历揭示）
**辨析**：VGER 静默拒收超长行（SVG 998 列、RFC 2821 行宽约束）是“邮件列表物理层约束源码提交”的直接证据；pnm 化代价 +25MB 系 Arnd 实测口径。
**文献**：DSLXC-3948/3949/3950/3951（`ksummit-discuss.messages.347707/347708/347709/347710`，2016-11-16/17），全文见 `raw_source.raw_json`

---

## 5.3 【Linux社区】“源码”定义之争（Linus 定调）

**要点**：Ts'o 引入生成文件哲学（“preferred form for modification”=svg，autoconf 例外）；Linus 亲自定义：**“用十六进制编辑器也能‘编辑’vmlinux 但那不叫 source code”；“I don't want to see generated binary crap”——png/gif/pdf 皆然**；修 Sphinx 处理方式优于 Makefile 生成游戏；并澄清发布补丁已带 `--binary + -M` 是 git apply 时代机制，与“源码”定义是两个问题——两层语义明确拆开。

**史料**：`347712`（Ts'o）、`347717`（Linus 定义）、`347718`（Linus 澄清）

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347712 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347717 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347718 -->`

**史观**：多方平等（总纲 8：Ts'o 的生成文件哲学与 Linus 的源码定义并列）；动手者叙事（总纲 10：定义由维护者一手给出）
**辨析**：Linus 的“源码”定义与 git apply 的 `--binary + -M` 发布机制属两层语义，本块已明确拆开；Ts'o 的“preferred form for modification”系生成文件哲学之通行表述。
**文献**：DSLXC-3953/3957/3958（`ksummit-discuss.messages.347712/347717/347718`，2016-11-17），全文见 `raw_source.raw_json`

---

## 5.4 【Linux社区】技术路线拉锯：graphviz 语言 vs TeX 怀旧 vs xfig 考古

**要点**：Bottomley 提 SVG data-uri 包裹位图旁路；Bart 提 graphviz 语言（版本控制友好）；Lunn 演示 Sphinx 内置 dot 插件实战；Woodhouse 怀旧“TeX 一直擅长”被 Linus 驳斥（“Christ, I get flashbacks”——epsfig/xfig/fig2dev 创伤），定调“现代格式=graphviz+svg”；Mauro 考古最老图为 PDF 源、Linus 纠正为 xfig、Woodhouse 认账（回忆梗）。

**史料**：`347719`（data-uri）、`347723`（graphviz 语言）、`347726`（dot 实战）、`347725`（TeX 怀旧）、`347727`（Linus 定调）、`347728`（考古）、`347729`（xfig 纠正）、`347730`（认账）

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347719 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347723 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347726 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347725 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347727 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347728 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347729 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347730 -->`

**史观**：多方平等（总纲 8：graphviz／TeX／xfig 三路线立场全录）；循环结构呈现（总纲 4：TeX 工具链旧创在 2016 年再度成为议题）
**辨析**：Linus 对 TeX 的驳斥（epsfig/xfig/fig2dev 创伤）与其后“原图格式几乎肯定是 xfig”之纠正互为印证；“现代格式=graphviz+svg”系 Linus 定调而非会议决议。
**文献**：DSLXC-3959/3963/3966/3965/3967/3968/3969/3970（`ksummit-discuss.messages.347719/347723/347726/347725/347727/347728/347729/347730`，2016-11-19），全文见 `raw_source.raw_json`

---

## 5.5 【Linux社区】执行：9 连 PATCH 系列与 svg-images 分支

**要点**：Mauro 11-20 连发 PATCH 0/9..9/9 完整转换：xfig→SVG、pipeline 重建为 dot（12 行源）、Makefile.sphinx 重组、cleandocs 修复；Tuz 图 crop 演示（PNG 11K→SVG 563K）；[RFC] 规则上移通用化（任意子目录 DOTS/IMAGES）；Vetter 求分支（GPU 文档）；Johannes 提“源已失传不碍事”+graphviz 内置插件。

**史料**：`347731`（已全去位）、`347732`（PATCH 8/9）、`347733`（PATCH 9/9）、`347734`（PATCH 7/9）、`347736`（PATCH 0/9 封面）、`347737`（PATCH 4/9）、`347743`（RFC 上移）、`347744`（求分支）、`347745`（源已失传）

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347731 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347732 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347733 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347734 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347736 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347737 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347743 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347744 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347745 -->`

**史观**：动手者叙事（总纲 10：9 连 PATCH 与分支即工作本身）；经验优先（总纲 9：图档体积与重建结果均为实测）
**辨析**：9 连 PATCH 为执行层完整序列（含封面信与 cleandocs 修复），可作“文档工程执行范式”标本；PNG 11K→SVG 563K 系以体积换可编辑性之代价，须与 5.2 的 pnm 测损并读。
**文献**：DSLXC-3971/3972/3973/3974/3976/3977/3978/3979/3980（`ksummit-discuss.messages.347731/347732/347733/347734/347736/347737/347743/347744/347745`，2016-11-20/21），全文见 `raw_source.raw_json`

---

## 5.6 【Linux社区】收尾：caption 缺位、ASCII art 底线与 Corbet 批准

**要点**：Mauro 列出 Sphinx 插件功能差距（caption/图表索引）；Bottomley 坚持 ASCII art 纯文本保护（“if it ain't broke, don't fix it”）；Johannes 同意并给“缺插件回退纯文本”设计；Jani 指外溢价值；Corbet 拍板“Should I apply these?”批 4.10（SVG 拆行实验+emacs 渲染轶事）；Mauro 请立即应用并坦承拆行风险存疑。

**史料**：`347748`（差距）、`347749`（ASCII 底线）、`347750`（同意）、`347751`（外溢）、`347753`（批准 4.10）、`347754`（请应用+风险）

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347748 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347749 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347750 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347751 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347753 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347754 -->`

**史观**：多方平等（总纲 8：插件功能、ASCII art 底线与批准权三方并置）；动手者叙事（总纲 10：批准与风险自陈皆当事人一手）
**辨析**：Corbet 的“Should I apply these?”系文档子系统裁决权的一手表达；Mauro 自陈拆行风险存疑，说明 4.10 采纳时风险未完全收敛。
**文献**：DSLXC-3982/3983/3984/3985/3986/3987（`ksummit-discuss.messages.347748/347749/347750/347751/347753/347754`，2016-11-21），全文见 `raw_source.raw_json`

---

## 5.7 【Linux社区】本页 KS2014 档案信标注（主题外）

**要点**：本页混入 4 封 KS2014（2014-05-12）档案信：347713（Jason Cooper：staging 树入口+反游戏化）、347724（HPA：QR oops cut-here 容量）、347735（HPA：去掉 cut、here）、347746（Preeti：Energy bias governor 节能之辩）——与 2016 线程无关，已读入 claim，历史归卷需另处。

**史料**：`347713`（Jason Cooper，DSLXC-3954）、`347724`（HPA，DSLXC-3964）、`347735`（HPA，DSLXC-3975）、`347746`（Preeti，DSLXC-3981）

【Linux社区】**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347713 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347724 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347735 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347746 -->`

**史观**：多方平等（总纲 8：2014 档案与 2016 线程并列呈现）；动手者叙事（总纲 10：归档杂讯本身即史料）
**辨析**：本页 4 封 KS2014 档案信（2014-05-12）与 2016 线程无关，已读入 claim，历史归卷须另处；引用须以 `date` 字段判年，勿按 pk 顺序断代。
**文献**：DSLXC-3954/3964/3975/3981（`ksummit-discuss.messages.347713/347724/347735/347746`，2014-05-12 KS2014 档案信），全文见 `raw_source.raw_json`

---

> 页面统计：50 封 / CAND 42 / NV 8 / recheck 0。评定表：review/ksd70_verdicts.md（逐行一致）。