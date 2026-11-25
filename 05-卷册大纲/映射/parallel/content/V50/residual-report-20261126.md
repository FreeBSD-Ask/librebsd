# V50 三道残余 open 题定向补源与穷尽判定报告（2026-11-26）

## 一、结论摘要

| 小节 | 现题 | 本次判定 | 一句话依据 |
| ---- | ---- | -------- | ---------- |
| V50.3.4.3 | 硬件捐赠由需求方直接接收 | unresolvable | 仅项目自述页一源；bsdmag 2016、dragonflybsd.com 镜像、MidnightBSD 抄用均非独立载体 |
| V50.4.1.1 | 提交量 2005 年见顶 | single_source | GitHub 检索 API 复算 3 967；项目自建库异管线同向（4 194），但同仓库不构成独立第二源 |
| V50.4.2.4 | 核心子系统维护者数年内接连淡出 | unresolvable | 未见任何成文更替记录；已附降格拟题“子系统活跃区以数周无提交为界”（单源 L2） |

三题均不足以判 `filled_candidate`：每题都缺一份与本项目无同源关系的第二载体。逐题证据行见 `residual-evidence-20261126.tsv`（4 行，第 4 行为 4.2.4 的改题拟稿行）。

## 二、逐题

### 一、V50.3.4.3 硬件捐赠由需求方直接接收

**目标**：为“需求方直接接收、项目不介入交易”这一政策面找一份非转载、可独立核验的载体。

**检索面**（2026-11-26）：

| 检索方式 | 目标 | 结果 |
| -------- | ---- | ---- |
| WebSearch：政策原句与 requestor 关键词组合 | 找同句在异域名出现 | 仅命中官方页、bsdmag 2016、dragonflybsd.com |
| WebFetch 官方 donations 页全文 | 取现行文本与页末日期 | 取得，页末 2026-10-13 |
| Wayback CDX（dragonflybsd.org/donations/） | 追溯政策句起始 | 最早存档 2010-11-14，此后逐年连续 |
| WebFetch wiki.dragonflybsd.org/docs/ 索引 | 查 wiki 侧是否有独立表述 | 仅有 Obsolete Documentation、Code Bounties 等入口，无捐赠流程页 |
| WebFetch handbook introduction | 查开发模型章是否述捐赠 | 无 |

**判据分析**：

1. bsdmag 2016-03-11 文本为 2016 年版页面的整体转载，属同源，独立性不成立（与 c3 批判读一致）。
2. dragonflybsd.com/donations 为同文镜像站，域名不同而文本同源，仍不成立。
3. MidnightBSD 捐款页沿用同一句式（Donors, please contact the requestor directly and CC the above address），系姊妹项目抄用 DragonFly 措辞；它证明该措辞在 BSD 圈内流传，但对 DragonFly 自身政策不构成独立记录。
4. 版本差异值得落块时写明：2016 年版尚有“需求方名录＋须有一次被接受贡献”一段；2026 年版只剩政策句，名录已空置，正文中“requestor”已无对应条目。

**判定**：`unresolvable`。政策面事实本身由官方页逐字支撑（L3 单源可读），但按“≥2 独立来源”门槛不成立；建议落块时以“项目自述”限定语表述，或按存疑处置。若主会话愿接受“官方页＋2016 存档页”为两版本文献（同域异文献），可参照 V47 批先例，但仍非异域名独立源。

### 二、V50.4.1.1 提交量 2005 年见顶

**目标**：找口径可比的第二独立年度序列，不硬凑 Open Hub 全期 45 386 与项目库 656 207 的差异。

**检索与复算**：

| 来源 | 性质 | 取数 | 可否作第二源 |
| ---- | ---- | ---- | ------------ |
| GitHub commit search API（committer-date 分年） | 主源，官方镜像 | 2005＝3 967（2026-11-26 复算同值） | 是（主） |
| 项目自建库 dragonfly.duckdb（dragonfly-src，49 379 提交） | 全量克隆后自建统计 | 2004＝3 366、2005＝4 194、2006＝1 873、2024＝349 | 否：同仓库异管线 |
| Open Hub 项目页 | 第三方统计 | 全期 45 386、12 个月 896 | 否：无分年序列 |
| RepositoryStats 项目页 | 第三方统计 | 全期 45 490；自 2010 起分年；自述 2022 年起 2 521 次 | 否：不覆盖 2005，且与本地口径不一致 |
| LFX Insights | 第三方统计 | 仅近期窗口（检索摘要作 826 对 485，未取全页） | 否：无 2005 数据 |

**关键发现**：

1. 两条管线在峰值年一致（2005 均为最高），数量差 5.7%（3 967 对 4 194），可用于说明 API 计数非孤例，但同仓库对象决定其不能充当独立源。
2. 谷值年两管线不一致：本地为 2022＝345，2024＝349（差 4 次）。原题“2024 年触底”不成立；c4 批改题已改为“提交量 2005 年见顶”，本次复核支持该改法，落块时不应回写“触底”。
3. 项目库 2026 年 1 127 次系截至 2026-08-18 增量更新，非全年值，不得与整年比较。

**判定**：`single_source`（维持）。若主会话认“异管线互证”可升 L2 以上，但仍不满足“两独立来源”。

### 三、V50.4.2.4 核心子系统维护者数年内接连淡出

**目标**：找成文维护者更替记录（新闻、访谈、官方公告、学术文献）。

**检索面**：

| 检索方式 | 目标 | 结果 |
| -------- | ---- | ---- |
| 官方 history 页全文 | 找去留叙述 | 只有“Major kernel subsystems were also scaled one after another”与 2012 年 Tigeot 接手 DRM，无卸任记录 |
| team 页 2014／2026 两版 | 名录进出 | 纯增列 52→58，无删名 |
| Wikipedia 英文版 wikitext | 社区规模与人事 | 仅“smaller developer base”，无更替 |
| Phoronix、OSNews、BSD Now、Digest、DistroWatch 关键词检索 | 新闻／访谈 | 未见“维护者卸任／淡出”成文报道；Digest 与播客按规不作块证据 |
| Open Hub 贡献者页 | 末次提交 | 只有窗口人数与末次提交，无子系统维度 |
| 项目库按作者×路径 | 提交时序 | 可出推断，非成文记录 |

**降格拟题（建议采用）**：

- 拟题：`子系统活跃区以数周无提交为界`
- 依据引文（committer(7)，2009-03-26）：This means that, generally, if you do not see a commit to an area of the source tree in the last few weeks, it isn't considered active and you don't really need to confer with the developer that made the commit, though you should still post to the kernel@ mailing list and, of course, confer with developers when their expertise is needed.
- 旁证（同向，不支撑人员去留）：官方 history 页“Major kernel subsystems were also scaled one after another.”
- 强度：单源 L2；若要求双源，目前无等价表述可补。

**判定**：原拟证 `unresolvable`；改题后可按 `single_source` 落块（拟稿行已在 TSV 第 4 行）。

## 三、口径与守恒

- 时点：全部访问日 2026-11-26；GitHub 检索 API 2005 年复算与 2026-11-25 首测同值 3 967，随后按 2022 年复查触发 403 频控，未再取数。
- 本地计数法：`repo_name='dragonfly-src'`，按 `committer_date` 前四位分组，总 49 379（另 1 行日期为空）；`dragonfly-dports` 606 813 与 `dragonfly-docs` 15 未并入本卷口径。
- 邮件列表、（DragonFly BSD）Digest、播客均未作块证据；本报告仅用于线索披露与判定。
- 本次只写本目录两件产物（`residual-evidence-20261126.tsv`、本报告），未改树、未改台账、未写库、未提交；`script/` 下探针脚本已删除。

## 四、需主会话裁定（3 件）

1. V50.3.4.3 是否按 `unresolvable` 转存疑（存疑库登记），抑或接受“官方页＋同域存档异版”作两版本文献并以限定语落块。
2. V50.4.1.1 是否认“GitHub API＋项目自建库异管线”为可接受的互证而升 L3，抑或维持 `single_source` 并在落块时写明计数管线。无论何者，“2024 触底”都不应恢复。
3. V50.4.2.4 采原题判 `unresolvable`，还是采纳降格拟题“子系统活跃区以数周无提交为界”按单源 L2 落块。
