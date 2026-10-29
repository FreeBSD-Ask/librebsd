# 联网完善中外人名表 考据记录

- 日期：2026-08-13
- 对象：`10-交叉索引/cross_indexes.db` `person_bio_research` 表（158 行）
- 依据：spec `enrich-person-name-table-web-2026-08-13`
- 备份：`script/_backup_20260813_person_name/cross_indexes.db`（sha256 `799142a0722314c984a4cf3d7eee0991af42c69d16461678ed0067fe99221105`，integrity_check=ok）

## 查证来源

本轮对全部 158 人（P0=26、P1=52、P2=71、遗留=9）逐人联网考据，采用来源按优先级：book.bsdcn.org（FreeBSD 从入门到跑路）、正式中文出版物（机械工业出版社、人民邮电出版社、清华大学出版社、外研社、中国电力出版社等，均查证 ISBN/译者署名/CIP 数据）、中央级权威媒体（人民日报海外版、新华网/新华社、人民网、环球网、观察者网等）、本人博客/GitHub/主页/演讲自署、高校官方报道（北京大学、哈佛大学、剑桥大学、普林斯顿、达特茅斯等）、ACM 图灵奖/NAS/CHM/Britannica/讣告等一手或权威二手来源。所有 `sources` 字段 URL 均为 WebSearch/WebFetch 真实访问所得，严禁编造。数据库回写共 1376 字段（158 人）。

## 交叉验证方法

1. **一手来源不豁免**：当事人主页/GitHub/提交记录须与其他独立来源（官方悼念页、ACM 页面、正式出版物、讣告）交叉印证后方采信。
2. **独立来源要求**：不同作者、不同载体、不同社区至少两项差异；如 Ken Thompson 图灵奖页 + 《UNIX 传奇》中文版交叉；Robert Watson 以 CHERI 项目页 + FreeBSD 提交记录 + TrustedBSD 论文交叉。
3. **人名翻译交叉验证**：`name_zh` 仅在有正式出版物/中央媒体/本人自署时填入，其余清空并记 `doubt_flags`；如“里奇”据《C程序设计语言》《UNIX传奇》两书确认为“丹尼斯·里奇”，“麦克罗伊”据《UNIX传奇》目录更正为“道格·麦基尔罗伊”。
4. **账户名独立归位**：FreeBSD/NetBSD/OpenBSD/DragonFly 账户名（如 delphij、lwhsu、phk、deraadt、agc、mycroft、cgd、bde、kib 等）从 `name_zh` 脏值中剥离，统一归入 `aliases` 字段，不翻译不改写。

## 存疑判定依据

1. **name_zh 无依据清空（107 人保持英文原名）**：BSD/UNIX 提交者多无正式中文译名，仅见维基/百科/CSDN/博客者一律清空，记 `doubt_flags` status=open。少数人物（如 Perlis、Eich、Cantrill、McVoy、Rosenblum）虽有网络流传译名但无正式出版物依据，同样清空待上级裁定。
2. **生卒/全名存疑**：出生月日、中间名、出生地多源矛盾者记 open（如 Kernighan 出生月日、Ritchie 博士年份 1967/1968 两说、Babaoglu 土耳其名正字法 ASCII 两形、Chuck Haley 全名疑为 Charles Haley、Van Vleck 中间名）。
3. **数据一致性风险**：`ozalp_babaoglu`（P2 slug 行）与 `legacy_person_research_29`（遗留行）为同一人两条记录，本轮分别补全，去重留待后续处理。

## 字段补齐结果

| 字段 | 补前空值 | 补后空值 | 说明 |
|---|---|---|---|
| aliases | 158 | 7 | 账户名/昵称/笔名归位 |
| works | 158 | 5 | 著作/论文/软件 |
| affiliations | 149 | 0 | 机构与任期 |
| sources | 21 | 0 | 全部含 type/ref/url/checked |
| doubt_flags | 80 | 0 | 存疑留痕 |
| alive_status | 18 | 0 | 生卒状态 |
| priority/research_round | 9 | 0 | 遗留行补入 |
| name_zh | 9 | 107 | 有依据 51 人填入，无依据 107 人清空 |
| academic_genealogy | 158 | 118 | 师承可确证者填入，余省略 |
| relationship_status/dei_support/social_background | 59/59/42 | 59/59/42 | P0 部分补入，P1/P2 未覆盖（按优先级尽量补齐，余未处理） |
| vol_ch | 9 | 9 | 遗留行章号未能确证，未填 |

## 遗留待办

- 9 条遗留行 `vol_ch`（全书章号）未能确证，待后续大纲梳理时回填。
- `ozalp_babaoglu` 与 `legacy_person_research_29` 重复记录去重。
- `relationship_status`/`dei_support`/`social_background` 三项次优先级字段仅 P0 部分补入，P1/P2 未覆盖。
