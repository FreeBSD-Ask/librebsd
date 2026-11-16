# Apple XNU `README.md`（新 ref）引用卡

- **性质**：Apple 开源内核 XNU 的 `README.md`（22,122 字节），含 “What is XNU?”、“The XNU Source Tree” 目录清单与构建宏说明
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b026；查重：库内无 `apple-oss-distributions/xnu` 条目）
- **source_url**：<https://cdn.jsdelivr.net/gh/apple-oss-distributions/xnu@main/README.md>
- **计数（抓取正文实测）**：`BSD` 3 次、`Berkeley` 0 次、`FreeBSD` 1 次
- **quote（逐字，三处，分落三块）**：
  1. XNU is a hybrid kernel combining the Mach kernel developed at Carnegie Mellon University with components from FreeBSD and a C++ API for writing drivers called IOKit.
  2. （同段）XNU is an acronym for X is Not Unix.
  3. * `BSD_KERNEL_PRIVATE` : If defined, enclosed code is visible exclusively within the xnu/bsd module.
  4. * `bsd` - BSD subsystems code
- **考据注**：第 1／4 处用于 **BSD 层在内核文档中的自述**（1.13.1）与**再解释与再分类的区分**（3.9.5）：README 一面把 FreeBSD 组件与 Mach 并列为来源（血统陈述），一面在源码树清单里把 `bsd` 列为与 `osfmk`、`libkern` 并列的**一类子系统**（分类陈述）——同一文档同时给出两种陈述，正是“再解释”与“再分类”可分离的实证。第 3 处补出可见性边界（`BSD_KERNEL_PRIVATE` 只在 xnu/bsd 模块内可见）。
- **名与实的对照（要紧）**：同段解名 “XNU is an acronym for X is Not Unix”——名称自述“非 Unix”，而组成自述含 FreeBSD 组件；这一**名实反差**是本卷归名论题的直接文本证据，但 README 本身并无否认 BSD 渊源的意图（它只是递归式命名玩笑），不可写成“Apple 否认 Unix”。
- **限度**：①`Berkeley` 在本 README 出现 0 次——README 只到 “FreeBSD” 一层为止，更上游（BSD 血统的柏克莱段）须另取 Apple 的 copyright 文件与 `bsd/` 目录内文件头（本批未取，列待补）。②README 为**现行 main 分支文本**，与 macOS 发布版本的对应关系未核。③本卡引文经 jsDelivr CDN 取 `apple-oss-distributions/xnu` 镜像（Apple 原生 `opensource.apple.com` 未取），镜像与原生若有版本差，须以提交哈希另核（列待补）。
- **文本处理披露**：Markdown 源按行取用；列表项前的 `* ` 记号保留在引文中，正文空白归一。
- **本批落点**：V35.1.13.1（第 1、3 处）、V35.3.9.5（第 4 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b026；official_doc／L3）
