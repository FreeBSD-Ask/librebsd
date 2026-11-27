# FreeBSD Handbook《Introduction》（新 ref）引用卡

- **性质**：FreeBSD 项目官方手册第 1 章导论源文件 `_index.adoc`（22,305 字节，Asciidoc 源，取自 cgit plain 视图），含项目自述沿革与 “History” 附录
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b018；查重：cgit.freebsd.org 域内本批此前只取 `src` 树文件，`doc` 树该路径库内无条目）
- **source_url**：<https://cgit.freebsd.org/doc/plain/documentation/content/en/books/handbook/introduction/_index.adoc>
- **计数（抓取正文实测）**：`BSD` 113 次、`Berkeley` 6 次、`4.4BSD` 4 次
- **quote（逐字，三处，分落三块）**：
  1. FreeBSD is based on the 4.4BSD-Lite release from Computer Systems Research Group (CSRG) at the University of California at Berkeley, and carries on the distinguished tradition of BSD systems development.
  2. The FreeBSD Project had its genesis in the early part of 1993, partially as the brainchild of the Unofficial 386BSDPatchkit's last 3 coordinators: Nate Williams, Rod Grimes and Jordan Hubbard. … The early working title for the project was 386BSD 0.5 or 386BSD Interim in reference to that fact. 386BSD was Bill Jolitz's operating system, which had been up to that point suffering rather severely from almost a year's worth of neglect.
  3. FreeBSD then set about the arduous task of literally re-inventing itself from a completely new and rather incomplete set of 4.4BSD-Lite bits. Although only three files having to do with System V shared memory and semaphores were removed, many other changes and bug fixes had been made to the BSD distribution, so it was a huge task to merge all the FreeBSD developments into 4.4BSD-Lite.
- **考据注**：第 1 处用于 **“BSD 技术”作为独立传统的立名条件**（1.4.3）：立名的两要件在自述中齐备——**有基线版本**（4.4BSD-Lite／CSRG／柏克莱加州大学）与**有传统语**（“carries on the distinguished tradition of BSD systems development”）。第 2 处用于**历史主体的认定标准与缺位**（1.8.1）：主体写作“补丁包最后三位协调者”，工作名仍挂 386BSD／Bill Jolitz，即项目**自认由维护者群体而非发明人发起**。第 3 处用于**交接节点中的叙事重置**（1.11.5）：Novell 与柏克莱和解（同页记和解条件为移除三个 Net/2 文件并宣布 4.4BSD-Lite 无涉）之后，手册写“照字面重新发明自己”，重置的幅度自陈为“巨大工程”。
- **立场披露（要紧）**：本文件是 **FreeBSD 项目自述**（现行手册源，随版本更新），其对渊源、幅度与动机的表述属自我叙事而非第三方核验；三处引文中 “distinguished”“arduous”“huge task” 皆为评价性用词，本批只用于证“该叙述如此写”，不据以断定实际改动行数或工作量。另：本卡未取 git 历史，手册源文件的**版本时点未核**（列待补），引文按抓取时点记录。
- **文本处理披露**：Asciidoc 源按行取用，块内引文将原文换行并为空格；第 2 处中间略去一句（以 `…` 标示），未落块；库内 quote 存整段连续文本（不含省略号）。
- **本批落点**：V35.1.4.3（第 1 处）、V35.1.8.1（第 2 处）、V35.1.11.5（第 3 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b018；official_doc／L3，retrospective=1）

## supp-V73-b003 追加引文（2026-11-27，docs.freebsd.org 现行页逐字；Tavily＋curl 实取）

> The first CD-ROM (and general net-wide) distribution was FreeBSD 1.0, released in December of 1993. This was based on the 4.3BSD-Lite ("Net/2") tape from U.C. Berkeley, with many components also provided by 386BSD and the Free Software Foundation.

- **考据注**：首 CD-ROM 发行起点句（A Brief History of 小节）；与卡内第 2 条创生叙事同节，支撑 V73 2.2.2 起点文本面。
- **考据日期**：2026-11-27（supp-V73-b003）

## supp-V73-b003 追加引二句（2026-11-27，docs.freebsd.org 现行页逐字）

> Those plans came to a rude halt when Bill Jolitz suddenly decided to withdraw his sanction from the project without any clear indication of what would be done instead.

> The trio thought that the goal remained worthwhile, even without Bill’s support, and so they adopted the name "FreeBSD" coined by David Greenman.

- **考据注**：Jolitz 撤回支持句与自立命名句（A Brief History of 小节连续两句），支撑 V73 2.2.4 分叉叙事的自我定位面。
- **考据日期**：2026-11-27（supp-V73-b003）

