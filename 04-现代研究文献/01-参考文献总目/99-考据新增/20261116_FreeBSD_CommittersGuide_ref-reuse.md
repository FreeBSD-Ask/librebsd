# FreeBSD Committer's Guide（复用件 ref10664）引用卡

- **性质**：ref10664（docs.freebsd.org/en/articles/committers-guide/，官方文档）的本批新取引文卡；原卡引文面（提交位／许可留档／非 BSD 许可安置）与本批不重叠
- **数据库**：复用 ref10664（2026-11-16 supp-V75-b003；文档页为现势版，钩子章节为 Git 迁移后规程）
- **source_url**：<https://docs.freebsd.org/en/articles/committers-guide/>
- **quote（逐字两处；折行按单空格归一）**：
  1. The commit hook in repo.freebsd.org checks the "Commit" field matches the committer’s information in FreeBSD.org.
  2. Install commit message template hook: For doc repository: % cd .git/hooks % ln -s ../../.hooks/prepare-commit-msg For ports repository: % git config --add core.hooksPath .hooks For src repository: % cd .git/hooks % ln -s ../../tools/tools/git/hooks/prepare-commit-msg
- **考据注**：第 1 处为服务器端钩子（repo.freebsd.org 校验 Commit 字段与 committer 信息）；第 2 处为三库客户端钩子安装规程（doc 软链 .hooks/prepare-commit-msg、ports 用 core.hooksPath .hooks、src 软链 tools/tools/git/hooks/prepare-commit-msg）。两处均为 Git 迁移后基础设施自动化面的可考痕迹
- **本批落点**：V75.1.2.3 第 1 块（D2 ref10664#url）与第 2 块（D2 ref10664#2）
- **考据日期**：2026-11-16（supp-V75-b003；official_doc／L3）

## supp-V75-b004 追加引文（2026-11-16）

- **quote 3（逐字；折行按单空格归一）**：For changes beyond those described here, committers should seek review from committers with the appropriate bit in the target repository. When in doubt, seek review, even if you have a commit bit in the repo.
- **quote 4（逐字）**：Committers are encouraged to seek review for their work as part of the normal development process, regardless of the area of the tree where the work is occurring.
- **考据注**：第 3 处为 4.1.2 非显然改动送审规则＋存疑即送审句（Pre-Commit Review 面）；第 4 处为送审文化句（常规开发过程组成部分、不限区域）。本段引文与原卡（提交位／许可留档／非 BSD 安置）及 b003 引文面（commit hook／钩子安装）不重叠
- **本批落点**：V75.1.2.4 两块（D2 ref10664#url／#2）

## supp-V75-b005 追加引文（2026-11-16）

- **quote 5（逐字；折行按单空格归一）**：The access and mentors files are stored in an orphan branch, internal/admin , in each repository.
- **考据注**：access 与 mentors 名册存于孤儿分支 internal/admin——行政记录与源码树分列，开发态与行政态的边界由分支机制承载。与前四段引文面（提交位／许可留档／非 BSD 安置／commit hook 与钩子安装／送审规则）不重叠
- **本批落点**：V75.1.3.4 第 2 块（D2 ref10664#url）
