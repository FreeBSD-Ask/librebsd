# DOC_MINE 补证块格式规则（2026-11-10 立）

> **性质**：本规则是 `05-卷册大纲/` 树内**非邮件来源补证块**的唯一格式判据源，约束联网补证产出的块体结构、抬头词表、证据等级取真值与写入链。
> **适用对象**：`05-卷册大纲/**/*.md` 中以 `<!-- DOC_MINE: ... -->` 标记开头、来源为 `references_fulltext.duckdb` 已登记文献或网页条目的补证块。
> **与 ROW_MINE 规则的关系**：邮件列表来源块仍由《ROW_MINE块体格式规则》约束；两份抬头表**按块型分治，不得跨用**（划界见 §五）。冲突时以各自适用块型为准。
> **授权依据**：ykla 2026-11-10 三项裁定——① 新立 `DOC_MINE` 与 `ROW_MINE` 并列；② 等级承库内 L1–L5 口径并为补证块新立抬头表；③ 先落规程、规则与门禁，再以三卷试点后按卷铺开。

## 一、适用范围

1. 本规则适用于**补证块**：小节论题成立而旧树与既有语料无同类块，经联网查证、已入 claim 库后写入大纲的证据块。
2. 补证块的来源**只限** `references_fulltext.duckdb` 的 `references` 表已登记条目（含网页条目、网页快照、存档件）。
3. 不适用：`ROW_MINE` 邮件块（见《ROW_MINE块体格式规则》）、A 型叙述锚（锚点后无块体者，见该规则 §二·补）、`MAIL_INSIGHT` 块。
4. 同一小节内 `ROW_MINE` 与 `DOC_MINE` 可并存；每块各按其型校验，不得混用抬头或纪律串。

## 二、块体结构

补证块恒为 **5 行**，不得增减；紧邻其前一个同级块之后插入，同段块相邻。按文献是否已入全文库分两子型。

### 2.1 D1 型（全文块，文献已入 `fulltext`）

```text
1  <!-- DOC_MINE: ref<REF_ID>#<BLOCK_INDEX> -->
2  **<抬头>**（证据等级：<LV>，来源：`historical_claims.duckdb.claim.<CID>`；<采纳批次>）
3  （空行）
4  [<YYYY 年 M 月 D 日，>]<摘要 30–80 字>引文出处：<著录简式>；引文按 <LV> 纪律：<等级中段>，具体结论仍须回核原文与同期一手材料，不得单独引为定论。
5  （空行）
```

### 2.2 D2 型（条目块，文献仅有条目或网页快照，未入 `fulltext`）

```text
1  <!-- DOC_MINE: ref<REF_ID>#url -->
2  **<抬头>**（证据等级：<LV>，来源：`historical_claims.duckdb.claim.<CID>`；<采纳批次>）
3  （空行）
4  [<YYYY 年 M 月 D 日，>]<摘要 30–80 字>引文出处：<著录简式＋访问日>；引文按 <LV> 纪律：<等级中段>，具体结论仍须回核原文与同期一手材料，不得单独引为定论。
5  （空行）
```

**子型选择硬判据**：该文献在 `fulltext` 表有 `reference_id` 对应行者**必须**用 D1；无全文者方可用 D2。已有全文而用 D2，判 D2 FAIL。

## 三、字段定义

| 字段 | 取值规则 |
| ---- | -------- |
| `REF_ID` | `references.id`，逐字取自库，不得手写近似值 |
| `BLOCK_INDEX` | `fulltext_blocks.block_index`（该文献内块序），须能在库内按 `reference_id` 命中 |
| `LV` | `claim.evidence_level` **真值**，取值 `L1`–`L5`；严禁写死字面或凭印象定级 |
| `CID` | `claim.claim_id`，须在库内存在且 `status='supported'` |
| `采纳批次` | 形如 `2026-11-12 V37 补证批 b003`；批次号与补证台账一致 |
| 摘要 | 30–80 字，忠实原文；不得删改原意，不得夹带判词与元评论 |
| 著录简式 | 作者. 题名. 年份.，与 `references.bibliography_entry` 一致；D2 另附 `访问日` |

## 四、抬头与纪律串

补证块的抬头由**来源类型**决定，纪律串中段由**证据等级**决定；两维独立合成第 4 行。此结构与《ROW_MINE块体格式规则》§四 的“四档一对一”不同，原因是文献来源的类型与等级不再一一对应（同一 `official_doc` 可因内容性质不同而取 L4 或 L5）。

### 4.1 抬头 ↔ 来源类型（`raw_source.source_type`，取值承 `controlled_vocab`）

| 来源类型 | 抬头 |
| -------- | ---- |
| `official_doc` | 官方文档 |
| `academic_work` | 学术记载 |
| `magazine-article` | 同时代报道 |
| `news` | 新闻报道 |
| `web_archive` | 网页存档 |
| `reference_book` | 工具书记载 |
| `talk_interview` | 事后追述 |

表外来源类型不得写块；先按 `controlled_vocab` 归型，归型不能者进例外。

### 4.2 纪律串中段 ↔ 证据等级（承 `historical_claims.schema_meta.evidence_level_convention`）

| 等级 | 纪律串中段 |
| ---- | ---------- |
| `L5` | 以上为直接来源记载，可作定论依据但仍须核对版本与上下文 |
| `L4` | 以上为当事人一手记载，属过程性证据 |
| `L3` | 以上为公开文献记载（官方文档或同时代报道），非当事人直接证词 |
| `L2` | 以上为背景性材料或学术二手，须与一手交叉验证 |
| `L1` | 以上为仅具相关性的线索，采信前须另行考据 |

**L3 措辞说明**：库内 `official_doc` 的 claim 主为 `L3`（实测 18 条，`wording_gate` 为“技术文档／论文明确说明”），故本文 L3 中段取中性表述“公开文献记载”；**禁写“二手转述”**——该词只属《ROW_MINE块体格式规则》§四 的邮件语境，用于文献块即错标。

### 4.3 三条一致性要求（缺一不可）

1. 第 2 行抬头 ↔ `raw_source.source_type` 按 §4.1 相符。
2. 第 2 行等级 ↔ 第 4 行纪律串等级相符。
3. 第 4 行纪律串中段 ↔ 第 2 行等级按 §4.2 相符。

## 五、与 ROW_MINE §四 的分治声明

1. 《ROW_MINE块体格式规则》§四 的抬头表（当事人自述／二手转述／背景性材料／存疑材料）**只约束邮件来源块**，其 `L1` 措辞（存疑材料）与库内 `evidence_level_convention`（L1 最弱→L5 最强）不一致，属历史遗留；存量约 47 万块**不订正、不扩用**。
2. 补证块一律按库内 convention 定级与取纪律串，**禁止**套用邮件抬头：不得出现“当事人自述”“二手转述”等词，也不得出现“以上为邮件列表……”句式。
3. 反向亦禁：邮件块不得套用本规则抬头表。
4. 违反第 2、3 条者，由 `audit_supplement_chain.py` 的 D2 判 FAIL。此条针对 2026-08-31“16,618 块抬头全量错标”事故的同类风险面，不设人工豁免。

## 六、补证链（S0–S5）

本节是补证作业的**唯一流程正文**；《小节建制与题名规则》只写触发条件与本节点指针，不复制判据。

### S0 取号与占位

从 `映射/design/exceptions/V{NN}.tsv` 取 `status=open` 且 `kind=corpus_gap` 的行；在 `映射/design/supplement/V{NN}.tsv` 建行，字段：`subsection_id`、`kind`、`ref_id`、`claim_id`、`source_type`、`tier`、`block_type`（D1／D2）、`batch`、`status`（`claimed`）、`note`。

判据：该小节 `approved/V{NN}.title.ok` 与 `land.ok` 齐备；同一 `subsection_id` 不得被两批同时 `claimed`（占位冲突即停）。

### S1 先库后网（去重前置）

**顺序强制：先查库内，再联网。** 四键查重，任一命中即复用其 `ref_id`，不得重复采集或重复入库；**联网核验为全 76 卷每题必经工序（2026-11-12 裁定），库内命中只作复用来源，不替代联网**：

1. `sha256`：文件级精确比对 `references.sha256`。
2. `isbn_doi`：DOI／ISBN 归一（小写、去 `https://doi.org/` 前缀）后比对。
3. `source_url`：URL 归一（去 scheme、去尾斜杠、去 `utm_*` 查询参数、host 小写）后比对。
4. 三元组：标题归一（去空格与标点、统一大小写）＋第一作者姓氏＋年份，三者全同即判重。

命中处置：复用既有 `ref_id`，在补证台账记 `dedup_hit=<键名>`；**不新建 `references` 行、不重复存全文**；仍须联网对题面事实独立核验并留检索记录（日期、人名、版次、合同号、案号等硬事实逐项复核）。四键均未命中方进入 S2。

判据正文另见《流程规则/09-材料、文献与入库》“去重执行要求”（SHA-256 精确＋三元组模糊＋`reference_duplicates` 登记），本节只规定补证场景的执行顺序。

### S2 文献登记

未命中者写入 `references`：`title`、`author`、`year`、`format`、`file_path`、`filename`、`sha256`、`file_size` 八字段必填；`bibliography_entry` 按 GB/T 7714-2015；`source_url` 须真实可访并留访问日；`source_tier` **必填**（`primary`／`secondary_authoritative`／`secondary_nonauthoritative`）；`status` 取 `kaoju_new`。

禁引来源（维基百科／百度百科／CSDN／百家号／HandWiki／阮一峰及其镜像等，清单见《考据规则》“其他不可信来源”与“禁引来源的镜像与变体识别”）一律 `source_tier='banned_repost'`、`status='banned_source'`，不得进入 S3。

需全文者落 `04-现代研究文献/03-文献下载/` 后按既有自动检测流程入 `fulltext` 与 `fulltext_blocks`；不重复入库的判定同 S1 四键。

### S3 claim 登记

三段写库，顺序不可颠倒：

1. `raw_source`：`source_id='SRC-ref:<REF_ID>'`、`namespace='ref'`、`local_pk='<REF_ID>'`、`source_db='04-现代研究文献/05-参考文献全文数据库/references_fulltext.duckdb'`、`source_table='references'`、`source_layer` 按 `controlled_vocab` 的层号取值（`official_doc`=3、`academic_work`=5、`talk_interview`／`memoir_blog`=4、`code_artifact`=1，表外类型按词表定义）、`source_type`（承 `controlled_vocab`）、`title`、`provenance_url` 或经 `references.file_path` 承担溯源（本地文献可空）、`source_date`、`tier_basis`、`reliability_grade`、`banned_source=0`、`acquisition_method='web_supplement'`、`acquired_at`。**标识口径承库内既有约定**（`SRC-ref:<id>` ＋ `namespace='ref'`），不得自造 `namespace='ref:<id>'`。
2. `evidence`：`source_id` 指向上行、`evidence_id` 用 `EV-SUP-<六位>` 号段（与 `EV-KF-` 分开，免混入既有 KF 统计）、`anchor` 记 `url:<去 scheme 的 URL>#<BLOCK_INDEX 或片段锚>`、`quote` **逐字**取自原文、`fact_text` 为可独立成立的事实陈述、`evidence_kind`（`quote`／`article_text`／`fact`）、`quote_lang`、`event_date`、`event_date_precision`（`day`／`month`／`year`）、`confidence`。
3. `claim`：`claim_id` 续 `CL-RM-` 号段（不新立前缀，以复用既有水位锁与全部下游正则）、`claim_text`、`evidence_level` 按 §4.2 定级、`status='supported'`、`created_by='supplement:<卷>-<批号>'`。

写前门禁：`claimdb_guard.py --db historical_claims` 须 PASS；`register_waterlock.py probe → acquire → register → release` 全程留槽。写后对账：`raw_source`／`evidence`／`claim` 三表新增行数与台账行数相等，`banned_source` 全为 0。**复核分层（2026-11-12 裁定）**：常规题出三份清单（初稿→独立复核→修复后复验）；涉日期、人名、版次、合同号、案号等硬事实者，另加严格复查一轮并出第四份清单，递归至无问题；各轮清单入批记。

### S4 入纲

按 §二 写块至目标小节 `.md`；块头 `CID` 与 `LV` 取自库内真值（禁写死）；同批同步补证台账 `block_type`、`claim_id`、`batch`、`status` 与 `note`（块锚 `ref<ID>#<块序或 url>` 可按需记入 `note`；台账表头以 162 号文 §11.2 十列为准）。写盘走 `write_guard()` 或显式 LF，UTF-8 无 BOM。

体量：每小节 `ROW_MINE`＋`DOC_MINE` 合计 ≤12 块且 ≤16,797 B（承《小节建制与题名规则》J2）；超者按 J4 阶梯处置，不得以补证为名突破。

### S5 回填与收口

1. `exceptions/V{NN}.tsv` 该行 `status` 由 `open` 改为 `supplemented`（补证成功）或 `unresolvable`（穷尽查证无果，须同时在 `doubts_standalone.duckdb` 登记 `resolution_status=open`）；并填 `resolution_kind`／`resolution_ref`／`resolution_claim_id`：doc_mine 记 `ref:<REF_ID>` 与 claim 号，row_mine 记块锚，exhausted 记 `doubts:<id>`，structure 记 approval 文号。
2. 小节 YAML `status`：有块即 `filled`；穷尽无果改 `closed`＋`resolution_reason: unresolvable`；合并／退役改 `closed`＋`resolution_reason: merged`／`retired`（须结构工单）。不得把已决题留在 `skeleton`。
3. 门禁：`audit_supplement_chain.py` D1–D6 全绿；`audit_outline_landing.py` L1–L19；`audit_subsection_design.py`；`audit_title_consistency.py`；卷级回归 `tests/volume_regression.mjs --vol V{NN}`。
4. 台账守恒：`exceptions` 行数批前批后相等（结构处置除外）；`open + claimed + supplemented + unresolvable = 原 open 总数`。

## 七、禁止项

1. 禁止未入 `references` 的网页或文献直接写块。
2. 禁止越过 claim 库把联网结论直接写入小节（先 claim 后大纲，顺序不可颠倒）。
3. 禁止在 S1 四键命中后仍新建 `references` 行或重复存全文。
4. 禁止以禁引来源作补证证据，或以其镜像、转储、缓存片段替代原文。
5. 禁止已有全文的文献改用 D2 型。
6. 禁止撰写导语、过渡、结论（红线 1）；补证块只承载证据与事实条目。
7. 禁止改块形、增删行、跨型套用抬头。
8. 禁止以补证为名突破 J2 体量与 J3 小节数上限。

## 八、写入与校验

- **写入**：补证块一律由脚本生成（台账 → 块文本），不得手工拼串；抬头与纪律串按 §4.1／§4.2 由 `source_type` 与 `LV` 两列查表生成，禁止硬编码单串。
- **门禁**：`脚本与命令/audit_supplement_chain.py`（第四十三件，2026-11-10 立），六项判据：

| 判据 | 内容 |
| ---- | ---- |
| D1 | `exceptions` 每行 `status` ∈ 四态、`resolution_kind` ∈ `none`／`doc_mine`／`row_mine`／`exhausted`／`structure`；`supplemented` 分轨：doc_mine 须在 `supplement/V{NN}.tsv` 有记录且 `ref_id`／`claim_id` 非空，row_mine／structure 须 `resolution_ref` 非空；`unresolvable` 须 `resolution_kind=exhausted` |
| D2 | 每个 `DOC_MINE` 锚的 `CID` 在 `claim` 存在、`status='supported'`、`LV` 与库内 `evidence_level` 一致；抬头与 `source_type` 按 §4.1 相符；不得出现邮件抬头 |
| D3 | 对应 `raw_source.source_id='SRC-ref:<REF_ID>'`、`namespace='ref'`、`local_pk` 指向该 ref、`banned_source=0`，且 `provenance_url` 与 `references.file_path` **至少一项非空**（本地 PDF／全文文献无网络 URL 属常态，溯源由 `file_path`＋`sha256` 承担），该 `ref_id` 在 `references` 存在 |
| D4 | 新入 `references` 的四键（`sha256`／`isbn_doi`／`source_url`／三元组）在库内唯一，或已在 `reference_duplicates` 登记。**重合判定以 `sha256`／`isbn_doi`／三元组为强证据（FAIL）**；`source_url` 单键重合而 `sha256`／三元组均不重合者，视为系列丛书共享集合页 URL（如贝尔官史六卷共用同一 archive.org collection），降 WARN 交人工判读，不自动判重 |
| D5 | 含 `DOC_MINE` 的小节合计块数 ≤12、字节数 ≤16,797 |
| D6 | 树内 YAML `status` 与例外台账双向一致：`skeleton`↔`open`／`claimed`；`filled`↔`supplemented`；`closed/unresolvable`↔`unresolvable`；`closed` 须 `resolution_reason` ∈ `unresolvable`／`merged`／`retired` 且 `closed_at`／`closed_ref` 非空；structure 轨允许树件已删，但须 approval 文号 |

- **自检**：`--selftest` 须含正例与反例（错级、伪 CID、禁引来源、重复键、超体量、skeleton 无台账、closed 无台账各一），判据为空即视为未立规。

## 九、变更流程

本规则的块形、抬头表、纪律串、链路顺序与门禁判据的任何变更，须经 ykla 裁定并留痕；变更后须同步：`audit_supplement_chain.py`、补证写入脚本、已落盘块（存量按批次评估，不静默订正）。

**2026-11-12 修订**：依 ykla 裁定统一联网口径（全 76 卷每题必经、库内命中不豁免）与复核分层；`raw_source` 标识口径统一为 `source_id='SRC-ref:<ID>'`／`namespace='ref'`／`local_pk='<ID>'`（与第四十三件 D3 实现一致）；`supplement` 台账列名以 162 号文 §11.2 十列为准。门禁判据逻辑未变。

## 十、立规依据

1. **现状**：`映射/design/exceptions/` 全 76 卷 **16,017 条** `corpus_gap`、`status` 全 `open`、`proposal` 逐条写“内容批前联网补证”；Task 8 内容面 filled 3,110／19,461（15.98%），skeleton 16,351。补证是已承诺未执行的工序，此前无格式、无链路、无门禁。
2. **格式缺口**：《ROW_MINE块体格式规则》只覆盖邮件来源块（锚 `lib.messages.<pk>`、四档邮件抬头），网页与文献来源无块可落。
3. **等级冲突**：库内 `schema_meta.evidence_level_convention` 为“L1 最弱→L5 最强”，与《ROW_MINE块体格式规则》§四 的 `L1=存疑` 措辞不一致；库内实测 `academic_work` 的 claim 主为 L2（584 条）、`magazine-article` 主为 L1（2,271 条）。不先划界即补证，必然重演 2026-08-31 错标事故。
4. **去重口径既有**：《流程规则/09-材料、文献与入库》“去重执行要求”与《考据规则》“文献分级 source_tier”的补主源优先级（库内复用 → 联网注册 → 降级存疑）已足；本规则只把顺序前移为“先库后网”，不新立去重判据。
5. **授权**：ykla 2026-11-10 三项裁定（块型、等级口径、落盘范围与节奏）。
