# A 类存疑本地库核验报告（2026-08-04）

> 核验方式：本地 11 个 git 仓库库（dragonfly/freebsd/netbsd/openbsd 等 commits/tags/contributors/commit_files 表）+ 资料数据库 freebsd_sa 表 + references_fulltext chapter_matches
> 核验日期：2026-08-04 14:30｜结果文件：script/_verify_a_class_result_20260804.json / _verify_a2_result_20260804.json / _verify_a3_result_20260804.json

## 一、核验通过（可 resolved）11 项

| 存疑 id | 章节 | 大纲主张 | 本地实证 | 结论 |
|---------|------|---------|---------|------|
| 1658 | ch214.1 Hsu 评价 | Hsu 280 条 commit 集中在 2003-2007 | contributors 表：Jeffrey Hsu commits=280，first=2003-07-24，last=2007-11-06 | **完全一致** |
| 1674 | ch225.1 4.2.2 错误 tag | 4.2.2 为错误 tag | tags 表 v4.x 系列 131 个：v4.2.1(2015-07-01)→**v4.2.3(2015-07-13)** 跳号，无 v4.2.2 | **实证确认 4.2.2 缺失** |
| 1681 | ch230.1 DRM 回移 | DRM 从 Linux 回移 | sys/dev/drm/ 时间窗 2003-06-17~2026-05-16（n=1406）；年度峰值 2014(197)/2015(310)，2021 起骤降 | **佐证回移+后期维护** |
| 1682 | ch230.1 netif vs drm | 目录活跃度比较 | netif=3053 vs drm=1406（DISTINCT commit） | **netif 更活跃，实证** |
| 1683/1685 | ch230.3/231.4 vkernel 移除 | commit 770134 + Digest 2021.1.8 | sys/platform/vkernel/ 时间窗 2003-06-17~2015-06-23（n=502），之后无提交；hash 770134 无精确匹配（两误匹配） | **佐证 vkernel 2015 后移除/缺席** |
| 1684 | ch230.4 现状 2026 | 两人 1318/1738≈75.8% | dragonfly-src 2024-2026：两人 1322/1754=**75.4%**（2024:71.5%、2025:64.3%、2026:83.3%） | **口径吻合（差异 0.4pp 系 dports/docs 含入差异）** |
| 1717 | ch214 概述 Dillon 首 commit | 1998-08-26 | freebsd contributors：Matthew Dillon(1027 commits) first=1998-08-26T01:58:39Z，last=2003-01-28 | **实证确认**（last 亦佐证 2003-02-03 撤权） |
| 1719 | ch231 概述 TOP 贡献者 | Aaron LI/Huete/Kusumi/zrj 排名 | Aaron LI 1830、Kusumi 1582+502=2084、zrj 1205+20=1225、Huete 1170+13+5=1188 | **排序与分期实证确认** |
| 1879 | ch149.14 13.x 39 SA | 39 个 SA（2021-04-01~2023-11-01） | freebsd_sa 表同口径计数 = **39** | **完全一致** |
| 1880 | ch154.20 14.x 80 SA | 80 个 SA（2024 19/2025 12/2026 49） | freebsd_sa 表按 SA 编号年度：2024=19、2025=12、2026=49 = **80** | **完全一致**（日期口径 85 系含 2026-07 后公告，非错误） |
| 1760 | ch313 概述 chapter_matches '32' | 20 条匹配待核 | 20 条 ref（FFS/McKusick/CSRG TR/DTIC 4.2BSD）与第32章“4.2BSD 革命与三件套”主题吻合 | **匹配合理** |

## 二、部分核验（佐证成立，但存疑原始关切超出本地库能力）

| 存疑 id | 大纲主张 | 本地实证 | 剩余待核 |
|---------|---------|---------|---------|
| 1672/1678/1680 | HAMMER vs ZFS 设计哲学（B+Tree vs merkle） | hammer2 目录时间窗 2012-02-08~2026-06-27（n=826），年度 2012(101) 启动、2019 后持续 55-99 | 设计哲学差异须源码逐文件对比（超出 commit 元数据能力） |
| 1675 | OpenSSL 1.0.x 漏洞对三项目 commit 量 | dragonfly openssl 路径 2010-2014 月度 commit 密集（300+ 条），Import 0.9.8m/1.0.0a/1.0.0b 清晰可见 | FreeBSD/NetBSD/OpenBSD 同期 commit 量（可再补查） |
| 1720 | vkernel 移除时点 | sys/platform/vkernel/ 最后 commit 2015-06-23 | 精确移除 commit 770134 未在库中定位（可能为 CVS 时期 hash 或 Digest 表述） |

## 三、未核验（超出本地库能力，维持登记）

- 1670（DragonFly 2.x 安全机制继承范围）：sys/security/ 2006-2010 无匹配路径（DragonFly 该路径结构不同），须 commit log 逐条人工核验
- 1641/1656/1657/1658(代表性问题)/1666/1667/1668/1669/1690/1691：邮件列表存档/官方档案/LKML 索引——非本地库可核

## 四、方法学备注

- 计数均走索引（idx_commits_repo_author_date / idx_contributors_repo_count / idx_commit_files_path / idx_tags_repo_date），无全表扫描
- contributor 同名多行（不同 email）需合并统计；dragonfly 库含 3 个 repo（dragonfly-src/dports/docs），repo 过滤后计数更准
- vkernel 路径 LIKE '%vkernel%' 会匹配 fork 初始导入（FreeBSD RELENG_4 含 vkernel 路径残留），时间窗上限以 MAX(author_date) 为准
