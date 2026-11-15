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
