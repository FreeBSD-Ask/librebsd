# 实体映射（首批）——机构规范化备忘

- 日期：2026-09-11（阶段B 首批产物）
- 数据源：`data/catalog.json`（persons.affiliations，2238 人）
- 用途：为三域语义中枢的“实体域·机构子域”提供规范化映射基线；不改变任何交付物文面。

## 1 映射规则

机构字符串按下列顺序归并：

1. 大小写变体（`OpenBSD project` → `OpenBSD Project`）；
2. 中英同义（`FreeBSD 项目` ↔ `FreeBSD Project`）；
3. 下属与母体分离标识（`FreeBSD Foundation` 为独立法人，不并入 `FreeBSD Project`；本批暂不合并，后续考据后另案处理）；
4. 短期项目名（`386BSD 项目` → `386BSD`）；
5. 职务后缀从机构名剥离（`FreeBSD Project（联合创始人）` → 机构 `FreeBSD Project`，职务信息保 person.role）。

## 2 首批归并组（8 组，制度化示例）

| 规范名 | 别名（归并前） |
| --- | --- |
| FreeBSD Project | FreeBSD Project、FreeBSD 项目、FreeBSD Project（联合创始人）、FreeBSD Project（联合创始人，Core Team 1992-1995） |
| OpenBSD Project | OpenBSD Project、OpenBSD、OpenBSD 项目、OpenBSD project |
| NetBSD Project | NetBSD Project、The NetBSD Project、NetBSD |
| UC Berkeley/CSRG | University of California, Berkeley |
| Bell Labs | Bell Labs、AT&T Bell Laboratories、Bell Laboratories |
| IBM | IBM Corporation、IBM |
| DragonFly BSD | DragonFly BSD 项目 |
| 386BSD | 386BSD 项目 |

## 3 频次基线（归并后 TOP）

OpenBSD Project 26、FreeBSD Project 18、Bell Labs 11、NetBSD Project 8、UC Berkeley/CSRG 7、Carnegie Mellon University 6、Sun Microsystems 5、IBM 5、Stanford University 3。

## 4 后续动作

- 归并组落地为 `org-map.json`（阶段B 正式产物），供 catalog 与 schema 引用；
- FreeBSD Foundation 与 FreeBSD Project 的机构关系需逐个考据（271 个邮箱/账户条目可交叉证）；
- 中文机构名（如“FreeBSD 项目”）与英文规范名互链，避免同一机构中英重复计数。