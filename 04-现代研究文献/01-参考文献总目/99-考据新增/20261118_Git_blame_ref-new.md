# Git《git-blame(1)》官方文档（新 ref）引用卡

- **性质**：Git 官方文档 git-blame 页（git-scm.com/docs/git-blame，curl 直取 82,816 字节，逐字可靠）
- **数据库**：新建 ref（2026-11-18 V35 P2 联网补证批 b033；git-scm.com 域内既有 ref10674—10688 为 Pro Git 章节与 git-merge-base 条，本 URL 无条目）
- **source_url**：<https://git-scm.com/docs/git-blame>
- **quote（逐字，一处）**：

  > git-blame - Show what revision and author last modified each line of a file

- **考据注**：用于**实施工具署名的交叉核对流程并记录结果**（3.7.5）。该句是行级署名取证的标准工具定义：git-blame 逐行显示最后修改的修订与作者——工具署名的交叉核对由此可落为**行级历史取证程序**（以行级提交与作者记录为证源、逐行回查归属、结果随批留痕），而非凭 README 或发行说明的自述署名。同页含 `-e`／`--show-email` 等选项面，本批未引。
- **限度**：①git-blame 显示的是“最后修改每行”的提交——跨版本历史需配合 git-log／git-blame -C 追溯，单命令不足以完成全部署名考古；②工具面只证程序可行性与定义，不证任何具体署名结论。
- **本批落点**：V35.3.7.5
- **考据日期**：2026-11-18（Task 8.2 G4 V35 P2 批 b033；official_doc／L3）
