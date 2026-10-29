# 联网扩充中外人名表 考据记录（续）

- 日期：2026-08-13
- 对象：`10-交叉索引/cross_indexes.db` `person_bio_research` 表（158 → 276 行）
- 依据：spec `enrich-person-name-table-web-2026-08-13` 的扩充阶段（用户指示“联网复核，扩展更多人名；同步更新大纲中的交叉引用”）

## 查证来源

在首轮 158 人基础上，从 `person_records` 表（`knowledge_graph_extract` 类型，去重 1134 条）中经程序去噪（首名命中常见西方名表 + 逗号“姓,名”格式识别 + 噪声词表排除组织/产品/术语/地名/书名/AI 模型名/截断），筛出 142 名候选，委派 6 个子代理逐人 WebSearch 联网核实，剔除噪声与主题无关者、去重已入表者，最终新增 118 名真实相关人物入表。所有 `sources` URL 均为 WebSearch/WebFetch 真实访问所得，严禁编造。

## 交叉验证方法

1. **程序预筛**：`final_filter_candidates2.py` 以“首词命中常见西方名表（含 Vint/Bjarne/Blaise/Moses/Marsilio/Thorstein/Erwin 等历史人物名）+ 去重（同姓+同首字母、全名/子串匹配）”过滤，将 704 候选缩至 142，再交人工联网核实。
2. **逐人联网核实**：6 批子代理对每个候选判断“真实人名 vs 噪声/组织/产品/术语/地点/AI 模型/乱码/截断”，真实人名再核对与本书主题（BSD/UNIX/计算机史、自由软件/开源、科学哲学与观念史）的相关性。
3. **同名区分**：Robert Morris 区分 Sr.（Bell Labs 密码学家，P1）与 Tappan（Morris worm 作者，P2）；Martin Zobel 截断补全为 Martin Zobel-Helas；Van Horn 补全为 Earl C. Van Horn（capability 模型）；Simon Andreas Frimann 截断补全为 Simon Andreas Frimann Lund。
4. **name_zh 交叉验证**：仅在有正式中文出版物/中央级媒体/本人自署依据时填（如罗伯特·卡恩、托马斯·阿奎那、威廉·詹姆斯、亚当·斯密、高德纳、图灵、克里斯坦森等），无依据者一律留空保持英文原名。

## 存疑判定依据

1. **截断/乱码剔除**：Andrew Hewus Fresh、Alfred North（疑 Alfred North Whitehead 截断）、Jan Stary Ehans、Van Deerlin 等截断名不臆断、直接剔除。
2. **同名歧义剔除**：Thomas Williams、Ian Evans、Isaac David、William Stern、Xavier Torrent、Elmer Carlson、Ethel Power、Forrest Fleming 等同名/无关者剔除。
3. **主题弱相关**：Max Weber、Paul Guyer、Michael Rossman、Jack Weinberg、Lennart Poettering、Luc Houweling、Martin Grenouilloux 等观念史/弱关联者在 doubt_flags 标注 relevance 存疑（open），供上游裁量。
4. **生年存疑**：Moses Maimonides 生年 1135（Britannica）/1138（Stanford）两说并存记 open；Evi Nemeth 出生年未确证留空。

## 扩充结果

| 指标 | 首轮 | 本轮后 |
|---|---|---|
| 总人数 | 158 | 276 |
| P0 | 26 | 26 |
| P1 | 52 | 75 |
| P2 | 71 | 175 |
| 有中文名(name_zh) | 51 | 59 |
| 无中文名(保持英文) | 107 | 217 |
| 有来源(sources) | 158 | 276 |

本轮新增 118 人（research_round=R1），其中 P1 新增 23 人（Vint Cerf、Bjarne Stroustrup、Evi Nemeth、Audris Mockus、Eugene Wong、Paul Baran、Martin Richards、Mike Accetta、Peter Denning、Larry Roberts、Lawrence Lessig、Richard Rashid、Robert Kahn、Robert Morris Sr.、Donald Knuth、Alan Turing、Adam Smith 等），P2 新增 95 人。

## 数据一致性修正

- **person_name 规范化**：统一 `person_name` = `name_zh`（有中文名）否则 `name_en`，修复 145 行残留脏值（混入账户名/注释，如“安德鲁·多兰，ad@NetBSD.org”“wiz”“sthen，斯图尔特·亨德森”“海老原 纯，えびはら じゅん”等），最终残留脏值 0。
- **抽样复核更正 2 处**：mike_karels 中间名由缩写 J. 补全为 John（家庭讣告 gearty-delmore.com）；stuart_henderson 的 name_zh“斯图尔特·亨德森”无依据清空。

## 遗留待办

- 9 条遗留行 `vol_ch`（全书章号）仍待大纲梳理时回填。
- `ozalp_babaoglu`（P2 slug 行）与 `legacy_person_research_29`（遗留行）为同一人两条记录，待去重。
- `relationship_status`/`dei_support`/`social_background` 三项次优先级字段仅部分补入。
- 大纲交叉引用标注（首次出现中文名后括注英文全名）为后续独立任务。
