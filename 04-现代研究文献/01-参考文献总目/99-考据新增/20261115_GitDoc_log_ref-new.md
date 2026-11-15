# Git 文档 `git-log`（新 ref）引用卡

- **性质**：git-scm.com 的 `git log` 命令手册页（官方参考文档）；本机 Chrome UA curl 200、376,281 B（单页手册，体积较大）
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b011；source_url 四键查重：库内 git-scm.com 已有书籍三页与 git-merge-base，本手册页无重合）
- **source_url**：https://git-scm.com/docs/git-log
- **quote（逐字，一处）**：
  1. -S<string> Look for differences that change the number of occurrences of the specified <string> (i.e. addition/deletion) in a file. Intended for the scripter’s use. It is useful when you’re looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the feature iteratively to feed the interesting block in the preimage back into -S, and keep going until you get the very first version of the block.
- **考据注**：该段说明 `-S`（俗称 pickaxe）的用法——按某字符串出现次数的增减找差异，并建议**迭代**：把上一版里的目标块再喂回 `-S`，直到追到该块的最早版本。用于 2.3.3“注释与标识符的指纹作用”：指纹之所以有用，是因为它是“精确字符串”而非模糊相似。**照录项**：`-S<string>` 的尖括号形态、`scripter’s`／`you’re` 的弯撇号均为原文所有；段末关于二进制文件的句子未取
- **本批落点**：V34.2.3.3 第 1 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b011；official_doc／L3）
