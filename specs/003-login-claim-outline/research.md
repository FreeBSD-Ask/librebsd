# research.md — Phase 0 决策记录（login 判定入藏战役）

**Feature**: specs/003-login-claim-outline | **Date**: 2026-10-06

Technical Context 无 NEEDS CLARIFICATION（技术路线沿用主理人既定案）。以下为本战役六项关键决策。

## D1: 判定对象＝articles 表 6,604 行（figures/chunks 不并入）

- **Decision**: 逐条遍历主对象为 login-zazhi.duckdb 的 articles 表全部 6,604 行（含 kind='ad'/'toc'/'frontmatter'/'unknown'）。
- **Rationale**: 主理人指令"每条数据，即使是广告，也必须逐条遍历"——广告即 articles 行（kind='ad'，经标题治理战役的形态识别）；既有邮件挖掘战役（rowmine，392,008 条 SRC-rowmine 注册）同以文章/邮件行为遍历单位。figures 12,403 项已有独立图文映射（outline_mappings_figures 13,976）与 review 体系（100% reviewed、quality 覆盖），chunks 为分块派生物。
- **Alternatives considered**: 把 figures/chunks 并入逐条判定——被拒：与既有独立处理线重复，且 figures 非文本条目（图片转写已有 quality 分体系）；如主理人另有指令可增量扩展。

## D2: 判定执行＝滚动 40 路子代理（缺 1 补 1）＋Python 判定引擎（主理人 2026-10-06 新增要求）

- **Decision**: 判定执行采用**滚动 40 路子代理（缺 1 补 1）**：40 个并行子代理各领取互斥分片（articles 分片）运行 Python 判定引擎 `_login_claim_engine_20261006.py --shard k`；分片完成即补领下一未完成分片直至 6,604 篇全量；子代理失败/超时/零产出即重派（缺 1 补 1）；主会话只派发与排障。判定引擎 import 既有 `_glm_line_20261006.py`（api.senseaudio.cn + glm-5.3-flash + 存储池 56 枚去重轮替 + 429 冷却 + billing/invalid 冻结 + extract_json strict=False 容错）。
- **Rationale**: 主理人 2026-10-06 新增要求（"滚动40路子代理，缺1补1。禁止抽查。逐条遍历，综合分析"）——**以最新指令为准，取代本战役此前沿用 10-05/10-06“不派子代理”定案的表述**（该定案仍适用于 OCR/转录类战役；本战役为判定工作，主理人指令子代理架构）。子代理角色＝运行 Python 判定脚本与监督（既有战役模式：不手工搬数据），LLM 调用仍经引擎的旧线路客户端（key 轮替＋冷却统一治理）。
- **Supersession note**: 本决策取代本 feature 内 D2 原文（Python 直跑不派子代理）；`.specify` 四件与 tasks 已同步更新。
- **Alternatives considered**: 单进程 Python 直跑 ≤120 路——被主理人最新指令取代；子代理自行调 LLM（不经引擎）——拒（key 轮替/冷却/断点统一治理被破坏，且子代理产出不可断言）。

### D2b: 综合分析（逐条，禁止抽查）

- **Decision**: 每条的判定为**综合分析**——不限关键词匹配，综合时代背景、当事人、技术/法律/社区/商业/文化五维关联、对本书各维度的证据价值后给出判定终态；**禁止任何形式的抽查**（含引擎内部降采样）。
- **Rationale**: 主理人 2026-10-06 新增要求"逐条遍历，综合分析。禁止抽查"。
- **Alternatives considered**: 按相关度抽样深判——拒（禁抽查）。

## D3: 判定的规则依据与输出契约

- **Decision**: 每条的判定 prompt 内嵌本书既有规则的**可执行判据集**（非全文）：八项操作原则 R1-R12（约束矩阵压缩集）、七类不写排查（BSD 版本列表项已放开）、十二项阈值中的判定相关项、R11 利益分配分析（广告的价值判据）；输出结构化判定（应入/不入＋理由＋所引原则编号＋拟挂大纲章）。
- **Rationale**: 62 条原则全文过长（1,136 行）不宜整文入 prompt；约束矩阵 §0.2 的 R1-R12 压缩集即其"汇聚形态"，配七类不写与 R11 广告判据构成逐条判定的最小充分判据集。判定理由可回溯原则编号（FR-002）。
- **Alternatives considered**: 仅按 relevance v2 关键词分——拒（关键词分不等于历史意义判定，主理人指令要求"判断分析其历史意义，价值"）；全文规则入 prompt——拒（成本与噪声）。

## D4: claim 入藏＝既有库 schema 续排（SRC-login 命名空间）

- **Decision**: historical_claims.duckdb 纯增量入藏：raw_source（source_id=`SRC-login:<article_id>`、source_db='login-zazhi'、local_pk、content_hash）、evidence（quote＝body_text 原文照录零改写）、claim（claim_id 沿用 `CL-<卷>-<序号>` 按所映射卷续排、claim_type 十值、evidence_level、wording_gate、status）、claim_evidence（role）、source_chapter（挂钩）。
- **Rationale**: 库内既有约定即权威（claim 393,153 行全 CL- 前缀；raw_source 420,818 行按命名空间注册：rowmine/mat/ref/commit/mail）；06 号 schema 设计为库的建库文本；"注册制不搬正文"（§2.3）。
- **Alternatives considered**: 新建独立库——拒（06 号 §8.2 拍板主张库为主数据单库；login 属史料入库非新体系）；复制正文进 claim 库——拒（注册制红线）。

## D5: 05-大纲同步＝source_chapter 挂钩＋ROW_MINE 注入块双面

- **Decision**: 入 claim 者**同时**：(a) claim 库侧 source_chapter 行（vol/ch/sec、link_type used/mentioned/background）；(b) 05-卷册大纲磁盘侧宿主章文件写入 ROW_MINE 注入块（块体按 ROW_MINE 块体格式规则：块头结构、当事人自述抬头、证据等级标注真值来源、引用纪律句），写盘走 WO-007（has_block + write_guard），写后跑 audit_evidence_level_labels 全绿。
- **Rationale**: 主理人指令"必须同时按规则入05-大纲"；既有邮件挖掘战役即此双面结构（source_chapter 31,786 行＋大纲注入块）；块体格式规则为 2026-09-17 立规的正式契约。
- **Alternatives considered**: 仅 DB 侧挂钩不动磁盘大纲——拒（主理人指令明写"入05-大纲"）；写入重构2026 目录——拒（只读红线）。

## D6: 新建大纲章＝CLAUDE.md 扩展接口三步，从严触发

- **Decision**: 仅当判定应入且既有 54 卷 454 章确无承载章时，按“新增章节”接口新建：卷 00-总览.md 登记章号标题→章文件夹与 index.md→sync_gitbook_summary.py --write；子节五字段＋史观映射 ≥5 条总纲；插入章号递归重排。
- **Rationale**: 主理人指令"应入本书而大纲不足以满足归类的，允许按规则新建大纲文件"；CLAUDE.md 新增章节接口为唯一正规路径。
- **Alternatives considered**: 大批量预建"login 专卷"——拒（无判定证据支撑先建结构，违反判定先行）；放宽触发——拒（滥建违反既有结构纪律）。

## D7: 重构2026 只读的实现与终检

- **Decision**: 战役启动前采集 `08-核查报告与多轮复核/重构2026/` 全目录文件清单＋SHA-256 基线（script/ 下 JSON）；终检重采比对，零变更 exit 0；全程任何写入路径不含该目录。
- **Rationale**: 主理人指令"过程中不得涉及任何重构2026文件夹（只读）"；哈希比对是唯一可机器断言的"零涉及"。
- **Alternatives considered**: 仅声明不写——拒（不可断言）；mtime 比对——拒（mtime 弱于内容哈希）。
