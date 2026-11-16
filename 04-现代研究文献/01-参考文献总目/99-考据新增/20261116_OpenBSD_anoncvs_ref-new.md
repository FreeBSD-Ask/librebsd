# OpenBSD Anonymous CVS（官方 AnonCVS 说明页）（新 ref）引用卡

- **性质**：openbsd.org AnonCVS 页；curl 实抓 2026-11-16（HTTP 200，19 355 B）
- **数据库**：新建 ref（supp-V75-b013；四键查重：库内该 URL 0 条）
- **source_url**：<https://www.openbsd.org/anoncvs.html>
- **quote（逐字两处）**：
  1. The OpenBSD Project currently has four active source repositories: src - source code for the base system ports - the ports tree www - web pages xenocara - xenocara
  2. There are two levels of source tree access: Read-write access for developers Read-only access for everyone
- **考据注**：第 1 处为仓库构成全表（src／ports／www／xenocara 四库，各附一句职责），第 2 处为访问权限两层（开发者读写、他人只读）。同页另述 AnonCVS 可追 errata 补丁、中央仓库支持 diff 与变更史查询，并以源码 tarball 预载减少流量——取史者可由四库与两权限界定期望边界。
- **本批落点**：V75.2.2.4 两块（D2 ref-new#url／#2）
- **考据日期**：2026-11-16（supp-V75-b013；official_doc／L3）

## supp-V75-b014 追加（2.3.3 两块）

- **追加引文（逐字两处）**：
  1. Anonymous CVS is a method of keeping your local copy of the OpenBSD source tree up to date with respect to changes made to current OpenBSD sources.
  2. Anonymous CVS works directly against a central source code repository. … This means that you have the full set of CVS commands available to control merging and updating your changes with other source changes, performing diffs, change histories and other queries against the central repository.
- **追加考据注**：第 1 处为取码目标（本地树与现行源同步，并可追发行勘误）；第 2—3 处为直连中央仓库句与全套 CVS 命令句——与 b013 已引的四库全表、两级权限分属构成面与操作面。
- **本批落点**：V75.2.3.3 两块（#url／#2）
- **考据日期**：2026-11-16（supp-V75-b014）
