# Git 文档 `git-merge-base`（新 ref）引用卡

- **性质**：git-scm.com 的 `git-merge-base` 命令手册页（官方参考文档）；本机 Chrome UA curl 200、41,269 B
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b009；source_url 四键查重：库内 git-scm.com 已有 3 条书籍页，本手册页无重合）
- **source_url**：https://git-scm.com/docs/git-merge-base
- **quote（逐字，一处）**：
  1. git merge-base finds the best common ancestor(s) between two commits to use in a three-way merge. One common ancestor is better than another common ancestor if the latter is an ancestor of the former. A common ancestor that does not have any better common ancestor is a best common ancestor, i.e. a merge base.
- **考据注**：该段把“共同祖本”写成可判定关系——最佳共同祖先的定义是“不存在更佳共同祖先者”，而“更佳”的判准是祖先关系（后者是前者的祖先则前者更佳）。这正是 2.2.4 题面要的“推定方法”：不是凭相似度猜，而是按图上的祖先关系定。**未取**：同页 `--fork-point` 模式与 `--independent` 的讨论（涉及 reflog，与本卷方法层面无关）。**注意**：段末 “i.e. a merge base” 为原文缩写形态，照录
- **本批落点**：V34.2.2.4 第 1 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b009；official_doc／L3）
