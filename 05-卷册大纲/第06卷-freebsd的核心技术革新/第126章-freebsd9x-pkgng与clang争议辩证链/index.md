---
chapter: 第 126 章
id: CH126
volume: 第06卷-freebsd的核心技术革新
---

# 第 126 章 freebsd9x-pkgng与clang争议辩证链

## 要点

- Linux/GNU 阵营对 FreeBSD 反批评的再回应集中于两点。其一，“生态规模不可逆论”：pkgng 即便工程完善，其软件包仓库规模、社区贡献者数量、第三方镜像网络均无法追赶 apt/yum 逾十年积累的生态——Debian 软件包仓库含逾 50,000 软件包且全球镜像数百个，FreeBSD pkg 仓库虽经 ports 同步但镜像网络与用户基数远小，工程等价性不等于生态等价性。〔待核：原文截断，后文待回源〕
- GNU 阵营对 FreeBSD 反批评的再回应集中于两点。其一，“Apache 2.0 专利条款遮蔽论”：FreeBSD 反批评中 “GPLv3 §11 专利报复条款构成法律风险” 的论证，只证明 GPLv3 有专利条款，不证明 FreeBSD 拒绝所有含专利条款的许可证——LLVM 现用许可证为 Apache 2.0（2019 年从 LLVM Release License 迁移），Apache
- **统计分析印证**——`freebsd.duckdb` freebsd-src 仓库 1993-2026 年 commit 月度量 Mann-Kendall 趋势检验结果为显著上升趋势（Sen's slope =+1.40/月，p < 0.001，95% CI [1.11, 1.69]）（统计结论 C-03）；FreeBSD 9.x 时期（2012-01 至 2017-06）处于 freebsd

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3809] 卷“第06卷-freebsd的核心技术革新”第 126 章，匹配置信度 folder，原因：folder 第124章

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 按 0 信任原则考据。【查证来源】Debian 软件包仓库规模经 packages.debian.org 一手核实（2026-07-23，stable 版含逾 50,000 软件包）；FreeBSD ports 数量约 24,000 经文件 57.16.2 已考据（9.x 时期 ports 从约 22,000 增长至超过 24,000）；ports 维护成本与 pkg/ports 元数据同步问题的
- 按 0 信任原则考据。【查证来源】Apache License 2.0 §3 专利报复条款经 apache.org/licenses/LICENSE-2.0 一手核验（2026-07-23），原文确含专利报复条款；LLVM 2019 年许可证迁移至 Apache 2.0 经 LLVM 官方公告核实；FSF 官方许可证列表关于 Apache 2.0 的评论经 gnu.org/licenses/lic
- *统计局限性标注**——(1) 统计显著 ≠ 实际显著：Mann-Kendall 趋势检验 p < 0.001 表明 freebsd-src commit 量存在统计学显著上升趋势，但 9.x 时期实际工程演进须结合具体子系统（bsdinstall、Capsicum、Clang、pkgng）的版本化分析；(2) 9.x 贡献率未量化：commit 量统计不区分 9.x 时期特有 commit 与其

## 文献

- Debian Project. Debian Packages [EB/OL]. [2026-07-23]. <https://packages.debian.org/>; FreeBSD Project. Ports Collection [EB/OL]. [2026-07-23]. <https://www.freebsd.org/ports/>; FreeBSD 10.0-RELEASE Announcement [Z]. 2014-01-20.［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- Apache Software Foundation. Apache License, Version 2.0 [Z]. 2004-01（§3）; Free Software Foundation. Various Licenses and Comments about Them: Apache 2.0 [EB/OL]. [2026-07-23]. <https://www.gnu.org/licenses/license-list.html#apache2>; LLVM Project. LLVM License Change to Apache 2.0 [EB/OL]. 2019; GCC Steering Committee. GCC Governance [EB/OL]. [2026-07-23]. <https://gcc.gnu.org/>; LLVM Foundation. Governance [EB/OL].［考据注：2026-07-28 联网考据留痕，模板句式已按 0 信任原则精简（WO-004）；语义以正文与所引来源为准］. ［A］

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
- FreeBSD Project. freebsd.duckdb freebsd-src 仓库 commit 数据库 [DB/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/freebsd.duckdb**; Hibsd Project. 推断性统计.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md** Task 5; Hibsd Project. 卷章数据映射.md [R/OL]. 2026-07-27. **03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/卷章数据映射.md** 第五卷第 57 章映射。［A］### 史观映射> 9.x 不是什么 “新一代”，而是 8.x 到 10.x 之间一座漫长的桥。bsdinstall 在 9.0 替换了年迈的 sysinstall，但 sysinstall 还在；Clang 导入了 base，但 GCC 4.2.1 仍是默认；Capsicum 进了 GENERIC，但标记为实验性；bhyve 在 -CURRENT 里写着，但 10.0 才正式发布；pkgng 在 ports 里孵化，pkg_add 仍在统治世界。Sony 把 FreeBSD 9.0 塞进 PS4，不是因为 9.0 比 Linux 更好，而是因为 BSD 许可证允许闭源——在这个版本里，你能看到许可证纯洁化工程的序幕（BSD patch 替换 GNU patch）和安全灾难（2012 年入侵），能看到 丹尼斯·里奇 的献辞和从数据中心到游戏主机的版图扩张。9.3 被支持到 2017 年不是偶然——它是旧世界（GPL 工具、sysinstall、pkg_add、GCC 默认）的最后一个稳定坐标。---> ## 第 57.24 不同时期人员的采访录（详见 [采访录.md](采访录.md)）> ## 第 57.24 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 57.25 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）## 第 57.25 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。> 2010-2020 年间：488,947 次提交。> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。
