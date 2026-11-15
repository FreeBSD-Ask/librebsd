# Pro Git“Git Branching — Branches in a Nutshell”页（新 ref）引用卡

- **性质**：git-scm.com 上 Pro Git（第 2 版）第 3 章第 1 节；本机 Chrome UA curl 200、136,157 B
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b009；source_url 四键查重：库内 git-scm.com 已有 3 条（Short-History／What-is-Git／Git-Objects），本页无重合）
- **source_url**：https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
- **quote（逐字，两处）**：
  1. If you make some changes and commit again, the next commit stores a pointer to the commit that came immediately before it.
  2. A branch in Git is simply a lightweight movable pointer to one of these commits.
- **考据注**：第 1 句给节点构造（提交存“紧前一次提交”的指针，故历史是有向图而非带时间戳的清单）；第 2 句给分支构造（指向某提交的可移动轻量指针，分叉不复制内容）。两句合起来正好回答 2.2.3 题面的“节点与分支如何构造”。**未取**：同页对默认分支名 `master` 的注释（含历史遗留讨论）与“detached HEAD”一段，留给需要时再引
- **本批落点**：V34.2.2.3 第 1、2 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b009；official_doc／L3）
