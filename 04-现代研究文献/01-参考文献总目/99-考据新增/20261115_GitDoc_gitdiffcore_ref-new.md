# Git 参考文档 `gitdiffcore`（新 ref）引用卡

- **性质**：git-scm.com 的 `gitdiffcore` 手册页（Git 官方参考文档，描述 diff-* 家族在输出前的变换链）；本机 Chrome UA curl 200、46,031 B（HTML），去标签后 15,650 字符
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b017；source_url 四键查重：库内 git-scm.com 现有 7 条，`docs/git-log`（ref10691）、`docs/git-merge-base`（ref10688）、Pro Git 四页与一条无 URL 的 git-cherry-pick 记录；`docs/gitdiffcore` 无重合）
- **source_url**：<https://git-scm.com/docs/gitdiffcore>
- **quote（逐字，两处；折行按单空格）**：
  1. The amount of deletion of original contents and insertion of new material are added together, and if it exceeds the "break score", the filepair is broken into two.
  2. In both rename and copy detection, the same "extent of changes" algorithm used in diffcore-break is used to determine if two files are "similar enough", and can be customized to use a similarity score different from the default of 50% by giving a number after the "-M" or "-C" option (e.g. "-M8" to tell it to use 8/10 = 80%).
- **考据注**：两句合看即“相似”在工具层的语义——第 1 句把删与增的量相加，超过 break score 即断为两个 filepair；第 2 句说重命名／复制判定的依据是同一套 extent-of-changes 算法，且相似度阈值可自定（默认 50%）。故工具给出的“相似”是一个可配置的分数档，不是同一性判定，也不指向表达的唯一性——用于 2.3.2“结构同构与表达唯一的区分”。原文第 1 句的 `"break score"` 与第 2 句的 `"extent of changes"`、`"similar enough"` 均带直引号，照录
- **本批落点**：V34.2.3.2 第 1 块（第 1 句）、第 2 块（第 2 句）
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b017；official_doc／L3）
