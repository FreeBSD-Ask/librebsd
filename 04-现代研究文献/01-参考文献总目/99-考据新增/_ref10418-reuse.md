# jail(8) 手册页（复用卡，ref10418）

- **性质**：复用既有 ref10418（他线建，`man.freebsd.org/cgi/man.cgi?query=jail&sektion=8`，raw_source 表定 official_doc／L3），本卡只登记本批新取的引文段
- **source_url**：<https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=8>
- **本批取句（逐字，一处；原文 "only\n" 处为词间换行，空白归一为单空格连读）**：

  > When set to 1, only mount points below the jail's chroot directory are visible.

- **与前批的关系**：ref10418 原卡（他线）引 jail(8) 的操作参数面；本批取 **enforce_statfs=1 的可见性句**——文件系统命名空间的挂载点封闭（chroot 目录以下才可见）正是“以挂载点封闭命名空间”的官方分级表述（0＝全部可见／1＝子树可见／2＝仅挂载点本身，本批引 1 档句）。
- **通道披露**：`format=ascii` 变体；断行在词界（only｜mount）无断词，空白归一后连读。
- **限度**：①引文只取 1 档（0／2 档原文在页，本批未引）；②“封闭程度决定越界风险”的展开属编纂论旨。
- **本批落点**：V37.3.2.2
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b026；复用 ref10418，official_doc／L3）
