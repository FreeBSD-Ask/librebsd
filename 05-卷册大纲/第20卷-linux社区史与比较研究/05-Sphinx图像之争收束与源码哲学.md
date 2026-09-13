# KS2016 会期文档工程收束：Sphinx 图像格式之争的执行层

> 本文件衔接 p69 增补文件（03-KS2016会前议题与组织机制史.md）「Sphinx 图像管线之争」主题，记录 2016-11-14 至 11-21 执行落定：Mauro 认错、Linus 定义「源代码」、graphviz+SVG 定调、Corbet 批准进 4.10。
> 本页史料范围 pk 347706–347755（ksummit-discuss 2016-11 线程），全部已入 claim 库（DSLXC-3947..3988）。
> 每块末尾「史料锚」为可反查去重的 ROW_MINE 定位（claim 库 source_ref 一致）。

---

## 5.1 认错与技术对质：PNG 并未损坏

**要点**：Mauro 于 11-14 公开认错——此前 Sphinx 图像之争中「PNG 有问题」诊断有误，实为 Sphinx 1.4.5→1.4.8 版本行为差异；认错附带「让 Sphinx 处理 PNG」补丁全文，是可查的公开技术纠错记录。

**史料**：`347706`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347706 -->`

---

## 5.2 规模盘点与邮件系统约束

**要点**：Arnd 指出 gif 与 png 同病，全树二进制除企鹅 logo 外集中在 Documentation/media；Mauro 补史实：4.8 前图像以 uuencode 提交，VGER 邮件列表静默拒收超长行补丁（SVG 998 列，RFC 2821 行宽约束）——「邮件列表物理层约束源码提交」实证；Arnd 测 pnm 可 patch 化（+25MB）拉 Linus 裁决；Jani 实测 kernel.org 二进制补丁不可 apply。

**史料**：`347707`（盘点）、`347708`（uuencode/998 列）、`347709`（pnm 测损）、`347710`（二进制补丁不可 apply）

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347707 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347708 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347709 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347710 -->`

---

## 5.3 「源码」定义之争（Linus 定调）

**要点**：Ts'o 引入生成文件哲学（「preferred form for modification」=svg，autoconf 例外）；Linus 亲自定义：**「用十六进制编辑器也能『编辑』vmlinux 但那不叫 source code」；「I don't want to see generated binary crap」——png/gif/pdf 皆然**；修 Sphinx 处理方式优于 Makefile 生成游戏；并澄清发布补丁已带 `--binary + -M` 是 git apply 时代机制，与「源码」定义是两个问题——两层语义明确拆开。

**史料**：`347712`（Ts'o）、`347717`（Linus 定义）、`347718`（Linus 澄清）

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347712 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347717 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347718 -->`

---

## 5.4 技术路线拉锯：graphviz 语言 vs TeX 怀旧 vs xfig 考古

**要点**：Bottomley 提 SVG data-uri 包裹位图旁路；Bart 提 graphviz 语言（版本控制友好）；Lunn 演示 Sphinx 内置 dot 插件实战；Woodhouse 怀旧「TeX 一直擅长」被 Linus 驳斥（「Christ, I get flashbacks」——epsfig/xfig/fig2dev 创伤），定调「现代格式=graphviz+svg」；Mauro 考古最老图为 PDF 源、Linus 纠正为 xfig、Woodhouse 认账（回忆梗）。

**史料**：`347719`（data-uri）、`347723`（graphviz 语言）、`347726`（dot 实战）、`347725`（TeX 怀旧）、`347727`（Linus 定调）、`347728`（考古）、`347729`（xfig 纠正）、`347730`（认账）

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347719 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347723 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347726 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347725 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347727 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347728 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347729 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347730 -->`

---

## 5.5 执行：9 连 PATCH 系列与 svg-images 分支

**要点**：Mauro 11-20 连发 PATCH 0/9..9/9 完整转换：xfig→SVG、pipeline 重建为 dot（12 行源）、Makefile.sphinx 重组、cleandocs 修复；Tuz 图 crop 演示（PNG 11K→SVG 563K）；[RFC] 规则上移通用化（任意子目录 DOTS/IMAGES）；Vetter 求分支（GPU 文档）；Johannes 提「源已失传不碍事」+graphviz 内置插件。

**史料**：`347731`（已全去位）、`347732`（PATCH 8/9）、`347733`（PATCH 9/9）、`347734`（PATCH 7/9）、`347736`（PATCH 0/9 封面）、`347737`（PATCH 4/9）、`347743`（RFC 上移）、`347744`（求分支）、`347745`（源已失传）

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347731 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347732 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347733 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347734 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347736 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347737 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347743 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347744 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347745 -->`

---

## 5.6 收尾：caption 缺位、ASCII art 底线与 Corbet 批准

**要点**：Mauro 列出 Sphinx 插件功能差距（caption/图表索引）；Bottomley 坚持 ASCII art 纯文本保护（「if it ain't broke, don't fix it」）；Johannes 同意并给「缺插件回退纯文本」设计；Johannes 同意并给「缺插件回退纯文本」设计；Jani 指外溢价值；Corbet 拍板「Should I apply these?」批 4.10（SVG 拆行实验+emacs 渲染轶事）；Mauro 请立即应用并坦承拆行风险存疑。

**史料**：`347748`（差距）、`347749`（ASCII 底线）、`347750`（同意）、`347751`（外溢）、`347753`（批准 4.10）、`347754`（请应用+风险）

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347748 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347749 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347750 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347751 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347753 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347754 -->`

---

## 5.7 本页 KS2014 档案信标注（主题外）

**要点**：本页混入 4 封 KS2014（2014-05-12）档案信：347713（Jason Cooper：staging 树入口+反游戏化）、347724（HPA：QR oops cut-here 容量）、347735（HPA：去掉 cut、here）、347746（Preeti：Energy bias governor 节能之辩）——与 2016 线程无关，已读入 claim，历史归卷需另处。

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347713 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347724 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347735 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347746 -->`

---

> 页面统计：50 封 / CAND 42 / NV 8 / recheck 0。评定表：review/ksd70_verdicts.md（逐行一致）。