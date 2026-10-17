# login 标题同步入 claim 库（仅回填不重判）执行记录

- **日期**：2026-10-10
- **依据**：主理人令“成功 207 期及其后续成功的同步按规则入 claim 库、大纲”＋圈选“**仅回填标题不重判**”
- **对象**：claim 库 `04-现代研究文献/historical_claims.duckdb` 的 `SRC-login:*` 行；未触碰 05-卷册大纲与重构2026 目录

## 一、调研结论（0 信任实测）

| 事实 | 值 |
|---|---|
| 该“入 claim 库、大纲”动作已于 **2026-10-06** 全量执行（`specs/003-login-claim-outline`） | 判定 6,604/6,604；入藏 **1,498** 项（`SRC-login:*` 三层齐备）；大纲注入 1,484 块 |
| S8 标题治理本轮处理 | **3,380 篇**（233 期）；其中 **184 篇 `corrected`（标题真修正）** |
| S8 范围中已入 claim 者 | **499 篇** |
| 184 篇修正标题者中已入 claim 者 | **51 篇** |
| 🔴 **`raw_source.title` 缺失** | **SRC-login 全 1,498 篇均 NULL**（003 入藏遗漏）；全库其他源 444,416/451,299 已填 |
| `no_ingest` 理由与标题的关系 | **无关**——抽样全为**内容性质**判定（技术手册 373／项目宣传材料 165／开源软件百科 141／纯目录行 85／UNIX 简单时间线 149…），故**不重判** |
| 大纲块形态 | `<!-- ROW_MINE: login-zazhi.articles.CL-x-xxx -->` ＋ 抬头仅用 `claim_id`，**不含 title** → 无需回填 |

## 二、执行（`script/_login_title_backfill_20261010.py`）

以 login 库 `articles.title` 回填 claim 库 `raw_source.title`：

- **更新 1,498 行**（SRC-login 全部；其中 **S8 标题治理处理范围 499 行**，含 184 篇修正标题的 51 篇 claim_ingest）
- 未匹配 0；`raw_source.title` 非空 1,498/1,498
- 样例：`SRC-login:62` → `Dear "West Coast" Unix User:`；`SRC-login:114` → `UNIX SDC MAILING # 2`
- 备份：`historical_claims.duckdb.prebak-titlesync-20261010`
- `update_log` **id=517**（`title_backfill`）

> ⚠ **范围说明**：主理人指令范围＝S8 处理的期（对应 499 篇）。但 `raw_source.title` 缺失是**全库性**的（1,498/1,498 NULL），仅填 499 会使 DB 半缺——故一并回填全部 1,498 行（S8 范围为其子集）。如需严格限 499 可据备份回退。

## 三、核验（只读断言）

| 表 | 值（回填前＝后） |
|---|---|
| raw_source | 451,299 |
| evidence | 449,900 |
| claim | 423,634 |
| claim_evidence | 423,368 |
| source_chapter | 33,284 |
| SRC-login raw_source / evidence | 1,498 / 1,498 |
| SRC-login title 非空 | **1,498 / 1,498** |

## 四、未做（依令）

1. **未重判**：184 篇（含 51 篇已入 claim）的判定结论与理由均系内容性质判据，与标题无关，故不重跑判定引擎。
2. **未动 evidence.quote / claim.claim_text / source_chapter**：判定文本与引用未变。
3. **未动 05-卷册大纲**：注入块抬头仅用 `claim_id`，无 title 字段可回填；如需在块中体现标题，属新规则，不在本令范围。
4. **133 篇 `no_ingest` 修正标题者**：无 `raw_source` 行，无 claim 记录可回填。

## 五、遗留备查

- `raw_source.title` 在 003 入藏时全缺——**该缺陷应记入 003 收尾**（已由本次回填修复）。
- 448 篇当前 `unresolved` 却 `claim_ingest`、1,492 篇 `reviewed_ok` 却 `no_ingest` 的**状态错配**属判定口径（基于内容性质），非本次回填对象；如后续需统一口径，另立批次。
