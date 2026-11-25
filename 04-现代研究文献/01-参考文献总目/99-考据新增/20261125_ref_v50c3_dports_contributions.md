# DPortsContributions（V50-c3 新登记）（V50-c3 批引文卡，2026-11-25）

- **来源**：DragonFly BSD. DPortsContributions[EB/OL]. https://wiki.dragonflybsd.org/docs/howtos/DPortsContributions/ [2026-11-25].
- **性质**：DragonFly BSD 官方文档或仓库页的成文记录；本卡供 V50 第 3 章证据块逐字取用。
- **取文途径**：2026-11-25 直连实抓（gitweb 以 curl UA 过 Anubis；script/_g5_v50c3_src/）。
- **四键查重**：新登记（URL／三元组／sha 待库内预检）。
- **tier 依据**：官方文档，source_tier=primary；claim 取 L3。
- **用途**：V50-c3（V50.3.2.1, V50.3.2.2, V50.3.2.3, V50.3.2.4）。

## 逐字引文池

- Around the 15th of each month a monthly branch is created in a local clone of the freebsd ports repository. This is taken as the base for the sync between freebsd ports and dports.
- In the staged build box a full build of the potential tree is built. Every package that builds will go to ports/staged branch and will also leave a trace of the build outcome in deltaports master branch (STATUS file in each port's folder).
- Sometimes people notice that a built port has a broken behaviour and open a PR on Github in order to fix that.
- The easiest thing you can do is to try to use the ports yourself and reports any issues, either by opening a Github issue, or through our bugtracker, where there's a specific DPorts category.
