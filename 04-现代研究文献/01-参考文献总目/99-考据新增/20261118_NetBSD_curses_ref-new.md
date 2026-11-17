# NetBSD curses(3) 手册页（新 ref）引用卡

- **性质**：NetBSD 官方手册 curses(3)（man.netbsd.org，curl 直取 38,132 字节，逐字可靠；HISTORY 段）
- **数据库**：新建 ref（2026-11-18 V35 P2 联网补证批 b032；`man.netbsd.org` 域内既有 ref1699／10448—10451 为其他手册页，本 URL 无条目）
- **source_url**：<https://man.netbsd.org/curses.3>
- **quote（逐字，一处）**：

  > The Curses package appeared in 4.0BSD.

- **考据注**：用于**终端库来源混淆的判定要点清单**（3.5.6）。该句是终端库谱系判定的一个标准锚点示例：NetBSD 现行 curses 实现的文档 HISTORY 段自述其包出现于 4.0BSD——**终端库出身应以实现自身文档的 HISTORY／谱系段为锚**（Berkeley 出身有现行实现自述可核），而非以宿主系统、接口同名或“常见于某系”的印象推断。终端库三族（termcap／terminfo／curses）各有独立谱系，判定清单的核心动作即回实现谱系逐库核。
- **限度**：①本句只证 curses 的 Berkeley 起点，不证 termcap／terminfo 的分野（该两族另有出处面，本批未引）；②NetBSD 实现是历史 curses 的后裔，其自述谱系与原始 Berkeley 包之间是传承关系而非逐字同一；③“判定要点”的清单化属编纂论旨。
- **本批落点**：V35.3.5.6
- **考据日期**：2026-11-18（Task 8.2 G4 V35 P2 批 b032；official_doc／L3）
