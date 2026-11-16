# Vim 官方 About 页（新 ref）引用卡

- **性质**：Vim 项目官方 About 页 `vim.org/about.php`（15,784 字节），含 “What Vim Can Do”“What Is Vim?” 两节与 vi 谱系自述
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b022；查重：库内 `vim` 相关为 ref5799（1991 年 Vim 1.14 首发，无 URL）与 ref5820（Neovim 0.1.0），`vim.org/about.php` 无条目）
- **source_url**：<https://www.vim.org/about.php>
- **quote（逐字，两处，分落两块）**：
  1. Vim is an advanced text editor that seeks to provide the power of the de-facto Unix editor 'Vi', with a more complete feature set.
  2. It is an improved version of the vi editor distributed with most UNIX systems.
- **计数（抓取正文实测）**：`BSD` 0 次、`Berkeley` 0 次、`UNIX` 多次出现
- **考据注**：第 1 处用于**编辑器归属的通行误记**（3.2.2）：页内称 vi 为“事实上的 Unix 编辑器”（de-facto Unix editor），**柏克莱之名全页 0 次**——归属被泛化到 Unix 层，作者与项目层不见。第 2 处用于**误记在手册中的复制链**（3.2.4）：以“随多数 UNIX 系统分发的 vi 编辑器”交代谱系，即以**发行事实**代替**来源记载**；该句随 vim 文档、镜像与各发行版说明层层复制，构成复制链末端的实例。
- **限度（要紧）**：①vim.org 是**衍生物（vi improved）的官方页**，不是教材，故 3.2.4 只把它当“复制链的一个环节”，不作教材样本；教材层面的复制链须另取（列待补）。②“de-facto”是 vim 项目的自我定位语，属评价而非统计；本批只证“该页如此写”，不据以断定 vi 的实际普及度。③本页未记 vim 与 vi 的版权关系，许可与代码谱系须另核 vim 的 `:help uganda`／LICENCE（未取，列待补）。
- **文本处理披露**：HTML 抽取后连续空白并作单空格；原文 `'Vi'` 为单引号，按原样保留（未改弯引号）。
- **本批落点**：V35.3.2.2（第 1 处）、V35.3.2.4（第 2 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b022；official_doc／L3）
