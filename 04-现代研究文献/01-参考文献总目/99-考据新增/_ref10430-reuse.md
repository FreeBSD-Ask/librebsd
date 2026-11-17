# jail(2) 手册页（复用卡，ref10430）

- **性质**：复用既有 ref10430（他线建，`man.freebsd.org/cgi/man.cgi?query=jail&sektion=2`，raw_source 表定 official_doc／L3），本卡只登记本批新取的引文段
- **source_url**：<https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=2>
- **本批取句（逐字，一处，整句原文无断行）**：

  > The jail() system call sets up a jail and locks the current process in it.

- **与前批的关系**：ref10430 原卡（他线）引 jail(2) 的 API 结构面；本批取 **DESCRIPTION 总述句**——“设立 jail 并把当前进程锁入其中”正是隔离视图语义的最短官方表述：监禁＝进程可见与可达范围的裁剪。
- **通道披露**：`format=ascii` 变体（与登记 URL 同文档，J48 通道）；该句原文整行无断行、无断词，空白未动。
- **限度**：①本句证监禁动作与语义，不证隔离强度分级；②“视图决定隔离强度”的展开属编纂论旨。
- **本批落点**：V37.3.2.1
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b026；复用 ref10430，official_doc／L3）
