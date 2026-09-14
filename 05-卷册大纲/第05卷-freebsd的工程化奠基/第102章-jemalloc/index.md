---
chapter: 第 102 章
id: CH102
volume: 第05卷-freebsd的工程化奠基
---

# 第 102 章 jemalloc

## 要点

- 开发史料疑点：（1） 开发起始时间；（2） Evans 与 Mozilla 关系；（3） 初始版本功能
- 算法史料疑点：（1） Evans 是否参考 Hoard;（2） arena 设计灵感来源；（3） extent 分级是否原创
- 集成史料疑点：（1） 集成决策时间；（2） 主要推动者；（3） phk malloc 是否完全移除
- 散逸史料疑点：（1） jemalloc 用于哪些项目；（2） 是否回流 FreeBSD;（3） Facebook 等是否贡献补丁
- 批评史料疑点：（1） 批评来源；（2） 批评时间点；（3） jemalloc 回应

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3637] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3641] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_3655] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 curated，原因：curated token rule
- [DB:references_fulltext:chapter_matches:chmatch_1224] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 0.85，原因：关键词匹配: dfly_dfly
- [DB:references_fulltext:chapter_matches:chmatch_1225] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 0.85，原因：关键词匹配: dfly_dfly
- [DB:references_fulltext:chapter_matches:chmatch_1226] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 0.85，原因：关键词匹配: dfly_dfly
- [DB:references_fulltext:chapter_matches:chmatch_1227] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 0.85，原因：关键词匹配: dfly_dfly
- [DB:references_fulltext:chapter_matches:chmatch_1228] 卷“第05卷-freebsd的工程化奠基”第 102 章，匹配置信度 0.85，原因：关键词匹配: dfly_dfly

## 史观

- jemalloc 是 BSD 代码散逸的教科书案例——Jason Evans 写出的 arena 分配器被 Facebook 和 Mozilla 拿走，BSDL 允许他们这样做，也允许他们不回馈。但更深的散逸不在代码，在话语：Evans 自己承认 jemalloc 在 Linux 上相对 glibc ptmalloc 的优势“不足以构成替换理由”，Linux 社区评论者普遍认为“除非系统分配器真的糟透了，否则没理由换”——一个技术优秀的分配器，就这样被“够用就行”的保守态度挡在了 glibc 的墙外
- 总纲第 4 条——分离聚合是永恒规律，jemalloc 散逸至 Facebook 与 Mozilla 是 FreeBSD 代码向其他生态分离的当代形态
- 总纲第 13 条——法律与道德是利益分配，BSDL 许可条款允许商业实体不回馈即其利益分配安排
- 总纲第 3 条——不存在进步，只有权力再分配，分配器的技术优势不必然转化为 glibc 生态位更替

## 辨析

- 时间线，需查 commit log；**统计局限性标注**——统计显著 ≠ 实际显著，C-03 freebsd-src 444,203 commits 为全周期（1993-2026）累计，非 jemalloc 开发期单段统计，跨时期引用时须注意；commit 量不直接反映 jemalloc 工程质量，须结合 commit message 主题词与文件路径交叉验证；0 信任原则适用——`freebsd-src`（2026-09-11 整改：原句截断于此，后文佚失，按前文 C-03 语境补全行间代码闭合，补全后文待考）

## 文献

- jemalloc source code commit log (github.com/jemalloc)；Evans (2006) BSDCan paper；Mozilla Bugzilla jemalloc tracking ［A］；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md**；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='freebsd-src'`. freebsd.duckdb [DB/OL]. 查询日期：2026-07-27 [考据脚注：C-03 freebsd-src 444,203 commits 经 `script/phase2_inferential.py` 执行结果与 `phase2_results.json` 结构化结果交叉验证。]
- Evans (2006) BSDCan paper；Berger et al. (2000) Hoard ACM SIGPLAN Notices 35(11)；Evans, J. jemalloc design notes (2005-2006) ［B］
- FreeBSD 7.0 src/lib/libc/stdlib/ commit log；freebsd-hackers jemalloc integration threads (2007-2008)；Kamp, P.-H. phkmalloc retirement discussion (2007) ［A］
- jemalloc contributors list (github.com/jemalloc/jemalloc)；Facebook jemalloc contributions (github.com/jemalloc/jemalloc/graphs/contributors)；FreeBSD src committers jemalloc patches (freebsd.org) ［A］
- freebsd-hackers jemalloc criticism threads (2008-2010)；Evans, J. jemalloc response to criticism (personal blog)；Mozilla Bugzilla jemalloc defect tracking ［A］
- Evans 2006/2011; jemalloc.net ［A］
- Drepper, U. glibc malloc maintainer statements (sourceware.org)；freebsd-hackers Linux jemalloc adoption threads (2009-2011)；Evans, J. jemalloc on Linux reflection (blog, 2011) ［A］
- jemalloc contributors list (github.com/jemalloc/jemalloc)；FreeBSD committers jemalloc patches (freebsd.org)；Facebook jemalloc contributions (github.com/jemalloc) ［A］
- Phoronix malloc allocator benchmarks (2008-2011)；Evans, J. jemalloc performance data (BSDCan 2006 paper)；Ghemawat, S. TCMalloc performance comparison (2004)［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

## 章内关联文件

- 不同时期人员的采访录（详见 [采访录.md](采访录.md)）
- 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）

<!-- DB_REF:freebsd.duckdb -->
> **数据库引用（freebsd.duckdb）**：本子节对应 freebsd 代码仓库。
> 1996-2010 年间：482,545 次提交。
> 仓库总览：1,294,851 次提交，5,671 位贡献者（contributors 表行数，1993-06-12 至 2026-08-25）。

<!-- /DB_REF -->
