# ;login: 标题治理与 figures OCR ── 交接任务书

- **编号**：login杂志交接任务书-20261005
- **日期**：2026-10-05
- **状态**：**全链闭环（2026-10-06）：T1–T7 七项任务全部完成并终检通过**
- **修订（2026-10-05 主理人复核反馈）**：执行架构定案——**全部 OCR/抽取/复核由 Python 引擎直调 API（≤120 路、KeyPool 轮替存储 key、复用既有 T1 线路），不派子代理**；spec v3「40 路子代理轮询池」作废（spec 已加 v3.1 注记）
- **修订（2026-10-06 执行实况）**：主理人令「不修 sensenova lib，复用旧线路」——实际采用**旧线路** `api.senseaudio.cn/v1 + glm-5.3-flash + 存储 key 池轮替`（`script\_glm_line_20261006.py`，两引擎各换 import 一行，sensenova lib 一字未动）；探针实测文本抽取 4.1s、视觉转写 200，56 枚存储 key 中 30 枚活；T2 全链当日闭环（详见 §三）
- **权威源**：`d:\librebsd\.trae\specs\execute-login-title-fix-and-figures-ocr\`（spec.md v3 已批准 / tasks.md / checklist.md）
- **本任务书性质**：磁盘实况快照 + 接手操作指引（2026-10-05 23:30 盘查）；与 spec 冲突时以 spec 为准，数字以本任务书核验值为准

---

## 〇、一句话交接

**T1–T7 全链闭环（2026-10-06），终检全绿**：
- **T2 标题治理**：5,680 篇 100% 终态（reviewed_ok 938 / unresolved 4,742 带原因），A/B 复核＋仲裁 468 全落库；
- **T4 figures OCR**：16,806 项 100% 终态（done 11,988 / skip 4,818＝幽灵 4,403＋无 colorspace 415），pending/failed 残留 0；
- **T5 双通道复核**：A/B 各 11,988/11,988，quality 均分 96，仲裁 679，done 项 reviewed 100%；
- **T6 入大纲**：938 篇 relevance v2 重判；outline_mappings v2（旧值标 superseded_by 4,439 行 + auto_keyword_v2 4,449 + model_confirmed_v2 279）；图文映射 13,976 行；87 卷《;login: 材料清单》→ `大纲映射/`；
- **T7 收尾**：update_log id=5 COMPLETION 登记；folder_db_registry 刷新（size 442,511,360 / sha256 c8f04d7f… / v1.1.0）；终局 manifest `script/_fig_ocr_final_manifest_20261005.json`；README 终局化。
- **终检全绿**：行数守恒（issues 419 / articles 6604 / chunks 41899 / relevance 6604 / figures 16806 / citations 662）、覆盖率 100%、二进制列 0、page 锚对位失配 0。
全程旧线路（glm-5.3-flash，Python 引擎 ≤120 路，未派子代理）。
**接手后续（可选）**：citations 662 行复核（status=auto）、修正文章引用抽查、按波提交材料清单与任务书。

---

## 一、任务目标（双臂）

| 臂 | 目标 | 规模（核验值） |
|---|---|---|
| **T2 标题治理**（优先） | eraB（1975–2000 OCR）低置信文章标题/作者/栏目修正，双通道复核+仲裁 | `needs_review` 文章 **5,680 篇**、队列 **236 期** |
| **T4–T5 figures OCR** | 16,806 项图片 LLM 视觉转写（禁本地模型、禁二进制入库）+ 100% 复核 | 队列 **16,806 项**（全 pending） |

**目的（为什么做这两臂）**：
- eraB 5,680 篇低置信标题多为 OCR 噪声（"Notice"/"Abstract"/大写乱码），不修正则文章**不可著录、不可引用**；
- figures 16,806 项（eraB 整页扫描 6,892 + eraA 嵌入图 9,914）是 djvu.txt 文字层之外的**唯一内容载体**，不转写则图表/表格/广告内容永久缺失；
- 两臂共同服务于 **T6 入大纲**（chapter_keywords 映射 + `outline_mappings_figures` 图文映射 + 分卷《;login: 材料清单》GB/T 7714 著录），终局供 05-卷册大纲 各卷引用 ;login: 素材。

**执行架构（主理人 2026-10-05 复核定案：单 Python 并发池，子代理退场）**：
1. **复用既有 OCR 线路**：全部 LLM/OCR 调用一律 import 已建成并冒烟验证的 T1 客户端（`script\_sensenova_lib_20261005.py`：KeyPool 轮替 + `chat()` 文本/图像 + `extract_json` + 共享日志），复用 T2 已验证的 staging/单写者模式；**不另建客户端、不另立 key 池文件**。
2. **Python 直跑，不派子代理**：OCR/抽取/复核全由 Python 引擎（ThreadPool 直调 API）执行，主会话只负责起停进程与排障；**禁止用子代理做任何 OCR/抽取/复核**（历史战役教训：子代理臆造页、误报自身处置、终止即丢工作）。spec v3「40 路子代理轮询池」作废。
3. **并发 ≤120 路**：全局并发上限 120 路（cfg `pools.global_max_routes=120`），期级/项级并发由引擎 `--workers` 控制，可自 40 起步视 429 频率上调。
4. **轮替存储的 key**：唯一 key 入口 = `KeyPool`（round-robin 轮替存储池 `script\_sensenova_keys_20261005.json` 11 枚 + 429 共享冷却文件 `script\_sensenova_cooldown_20261005.json`）；引擎禁止硬编码或旁路读取 key。限流吃紧时可切 cfg 接入既有存储池 `C:/Users/ykla/.sensenova/senseaudio_keys.json`（48 枚，api.senseaudio.cn/glm-5.3-flash 线路，须同步改 base_url/model），切换属线路级变更、先小批试点再全量。

> 注：spec 文本中「5,510 篇 / 221+ 期」为 eraB-print 口径笔误；实测全口径为 **5,680 篇 / 236 期**（含 unix_news 169 篇）。

---

## 二、已完成资产（接手无需重做）

### 2.1 数据库与原始载体
- **主库**：`d:\librebsd\03-原始史料库\15-login杂志史料\login-zazhi.duckdb`（已登记 `11-元数据接口/09-文件夹数据库索引/folder_db_registry.csv`）
  - issues 419 / articles 6,604 / chunks 41,899（FTS 可用）/ relevance 6,604 / outline_mappings 27,388 / citations 662 / figures 16,806
  - **零二进制列**（程序核验）
- **原始载体**：`d:\librebsd\login-db\`（PDF 267 + djvu.txt 149 + 文字层 txt 118 + online HTML 152 + online txt 152）

### 2.2 T1 ✓ 客户端基建（已验证）
- `script\_sensenova_keys_20261005.json`：11 枚 sk- key 轮替池（**不入 git，日志仅显尾 6 位**）
- `script\_sensenova_cfg_20261005.json`：`base_url=https://token.sensenova.cn/v1`，model=`sensenova-6.8-flash-lite`，超时/重试/冷却/池参数
- `script\_sensenova_lib_20261005.py`：`load_cfg/load_keys`、`KeyPool`（round-robin + 共享冷却，原子写）、`chat(prompt_or_messages, *, images, max_tokens, temperature, attempts, pool)`、`extract_json`、`log/mask_keys`
- 冒烟 `script\_sensenova_smoke_20261005.py`：**SMOKE_OK**（纯文本 1.5s；图像 base64 转写 16.2s）

### 2.3 T3 ✓ schema v2 增量（已验证）
- figures +5 列：`review_status / review_engine / reviewed_at / review_notes / ocr_quality`
- articles +2 列：`seg_review_status / seg_review_notes`
- outline_mappings +2 列：`superseded_by / key_points`
- 新表 `outline_mappings_figures`（0 行）
- `update_log` id=4 已登记 SCHEMA_V2；行数断言通过（6,604 / 16,806 / 27,388 不变）；二进制列 = 0

---

## 三、T2 进度快照（2026-10-06 全链闭环实况）

| 项 | 状态 | 证据 / 实况 |
|---|---|---|
| 队列 236 期 | ✅ 全闭环 | 引擎完成 232 期 + 重试 2 期（199/222）+ 试点 2 期；断点 236 行 |
| 治理覆盖 | ✅ 100% | needs_review 5,680 → **reviewed_ok 938 / unresolved 4,742**（终态外残留 0） |
| 复核 A | ✅ 938/938 | 1 单元（937）模型输出未转义引号，按模型原判解析恢复落盘 |
| 复核 B | ✅ 146 期 | 有 corrected 行的期全部复核 |
| 仲裁 | ✅ 468 篇 | A 判不一致 265 ∪ B 报问题 327，全部终裁 |
| writer | ✅ 实跑收口 | staging 全清偿（offset=EOF）；applied/cycle/review 全部入库；隔离 2 行（历史，已重放成功） |
| 数据库 | ✅ 守恒 | articles 6604 / figures 16806 / chunks 41899 / relevance 6604 / outline_mappings 27388 / citations 662 不变；二进制列 0 |
| 报告 | ✅ | `script\_title_fix_report_20261005.json` |

**执行实况（关键经验，T4 直接复用）**：
1. **旧线路**＝`script\_glm_line_20261006.py`（api.senseaudio.cn + glm-5.3-flash + 存储 key 池轮替 + 429 冷却 + billing/invalid 冻结 24h + `extract_json` 含 `strict=False` 容错）；key 池 56 枚存储、30 枚活（`_glm_line_alive_keys_20261006.txt`）；**sensenova lib 未修未用**。
2. **DuckDB 1.5.5 FK 限制（联网证实：duckdb#20246/#8988/#13819，无修复版）**：articles 被 4 表 FK 引用，对被引用行 UPDATE 含 LIST 列（authors）触发行重写并按**已提交状态**重查 FK——同事务删子行不可见、DROP CONSTRAINT 未实现。writer 已改造为**差量 UPDATE（未变字段剔除）＋ authors 变更走「子表存档落盘→删→改→回插」autocommit 三步回路 + 启动恢复协议**（`_title_fix_childcycle_20261006.jsonl`）；标量列 UPDATE 不触发、T4 的 figures 更新（无子表引用、ocr_text 为标量）**不受影响**。
3. Windows 下 `os.replace` 游标文件会被并发读取占用——writer save_cursor 已带 5 次重试；监控时**勿在读游标的同时跑写者**。
4. glm-5.3-flash 抽取大期时串值可能含裸换行（strict=False 解决）与未转义内嵌引号（偶发，重试或按原判恢复）。

---

## 四、T2 管线契约（字段级）

### 4.1 脚本清单（均在 `d:\librebsd\script\`）

| 脚本 | 作用 | 关键参数 | 库权限 |
|---|---|---|---|
| `_title_queue_build_20261005.py` | 生成期级队列（含 shard 分配） | 无 | read_only |
| `_title_fix_engine_20261005.py` | 分片引擎：窗口切分（12,000 字符 / 1,000 重叠）→ 抽取 prompt → 锚点匹配（difflib ≥0.55）→ 写 staging | `--shard 0,5,10` / `--issue 25` / `--workers ≤120` | read_only |
| `_title_fix_writer_20261005.py` | **唯一写者**：staging → DB，事务批 200 + 行数断言 + quarantine | `--drain` / `--max-seconds N` / `--reset-cursor` | **可写** |
| `_title_review_engine_20261005.py` | 双通道复核 + 仲裁，写 staging | `--channel A --shard 0,8,16` / `--channel B` / `--arbitrate` / `--workers ≤120` | read_only |
| `_title_report_20261005.py` | Task 2.5 汇总报告（读库 + 读 JSONL → JSON + stdout） | 无 | read_only |
| `_title_fix_report_20261005.py` | 另一版统计报告（read_only 统计 + 分布） | 无 | read_only |

### 4.2 文件契约（断点/游标/隔离）

| 文件 | 用途 |
|---|---|
| `_task_queue_title_20261005.jsonl` | 期级队列（236 行；`shard/issue_id/identifier/txt_file/n_articles`） |
| `_title_fix_staging_20261005.jsonl` | **唯一先行载体**（append-only；writer 投影回放） |
| `_title_fix_done_20261005.jsonl` | 引擎断点（已完成期；**重跑试点须先删对应行**，否则被跳过） |
| `_title_fix_writer_cursor_20261005.json` | writer 字节游标（尚未生成） |
| `_title_fix_quarantine_20261005.jsonl` | 校验失败/断言违例隔离（尚未生成） |
| `_title_review_done_20261005.jsonl` | 复核断点（`{"channel": "A"/"B"/"ARB", "id": ...}`） |
| `_sensenova_lib_20261005.log` | 共享日志（引擎/复核/API 调用同写此文件；key 已脱敏） |

### 4.3 staging 行类型（字段级）

```jsonc
// 修正/未决（writer 幂等：行值==pre → 应用 post；==post → skip；否则 quarantine）
{"type":"article_update","article_id":336,"issue_id":25,
 "pre":{"title","authors","section","seg_method","seg_confidence","needs_review","seg_review_status","seg_review_notes"},
 "post":{"title","authors","section","seg_method":"<旧>+llm_review","seg_confidence":"llm_review","needs_review":false,
         "seg_review_status":"corrected","seg_review_notes":"engine: match=0.87 kind=article"}}
{"type":"unmatched_model_article","issue_id":1,"entry":{...}}          // 仅报告
{"type":"issue_done","issue_id":25,"identifier":"...","n_rows":1,"n_corrected":0,"n_unresolved":1}
{"type":"issue_failed","issue_id":1,"error":"..."}
{"type":"review_a","article_id":N,"verdict":{"consistent":true/false,"corrected_title":"","corrected_authors":[],"reason":""}}
{"type":"review_b","issue_id":N,"problems":[{"article_id":N,"problem":"..."}]}
{"type":"arbitration","article_id":N,"final":{"final_title":"","final_authors":[],"final_section":"","reason":""}}
```

### 4.4 硬约束（违反即破坏任务）
1. **引擎/复核一律 `read_only` 打开 DuckDB；只有 writer 一个进程可写库**（DuckDB 单写锁）。
2. 全量执行时 writer 须常驻（`--drain`），与 Python 引擎并行；staging 是唯一信息通道。
3. 密钥只在 script/，不入 git；任何输出不得出现完整 key。
4. 库内禁二进制；所有中间产物只落 script/。
5. 试点期选**队列中 n_articles 最小期**，省 API 调用。
6. 全量执行：**单进程 Python 引擎直跑**（`--shard 0,1,…,39 --workers ≤120`），不派子代理；`--shard` 互斥语义保留，禁止同一期被两个分片/进程处理。
7. **一律复用既有线路**：引擎/复核 import `_sensenova_lib_20261005.py`，key 只经 KeyPool 轮替；禁止另建客户端或旁路读 key。

---

## 五、已知问题（阻塞级在前）

### 5.1 【阻塞】模型响应解析失败：推理链占满输出、无 `content` 键
- **现象**：issue 1 两窗 × 3 次全败；错误 `chat 响应解析失败（'content'）`。
- **根因（原始响应为证，已脱敏）**：
  ```json
  {"model":"sensenova-6.8-flash-lite","object":"chat.completion",
   "choices":[{"index":0,"message":{"role":"assistant",
     "reasoning":"Let me analyze this OCR text fragment from what appears to be a UNIX newsletter..."}}]}
  ```
  message 中**只有 `reasoning`（推理链），没有 `content` 键**——该模型为推理模型，抽取任务（max_tokens=6000）的**输出预算被推理过程耗尽**，最终 JSON 未产出。lib 的 `_content_to_str` 直接取 `[…] ["content"]` 故抛 KeyError。
- **修复指引（下一会话必做，改 `_sensenova_lib_20261005.py` + `_title_fix_engine_20261005.py`）**：
  1. lib 解析改 `.get()`：`content` 缺失/None 且存在 `reasoning` 时，读取并记录 `finish_reason`，抛出带上下文的**可重试**异常（如 `ReasoningOnlyError`）。
  2. 抽取 `max_tokens` 6000 → **24,000–32,000**（文档上限 65,536），保证“推理 + 正式输出”都装得下。
  3. prompt 末尾追加：**“不要输出推理过程，只输出 JSON 数组”**；并按官方文档启用 `response_format={"type":"json_object"}`（文档确认支持 `text`、`json_object`）。
  4. 若仍失败：窗口 12,000 → 6,000–8,000 字符降推理负担；必要时探索文档中的思考开关参数（以 platform.sensenova.cn/docs 现行版为准）。
- **附带证据**：另有一次 `RemoteDisconnected` 连接错误 + 429 冷却（`qbyr1Z`，已按机制换 key），属网络偶发，机制已覆盖，无需改。

### 5.2 issue 25「窗口成功但条目 0」待判定
- 可能与 5.1 同因（空 content 被“成功解析为空数组”），也可能该期确实无正文条目。**修复后重跑即可判定**。

### 5.3 重复行（无害）
- staging 中 `article_id=336` 出现 2 行（两次运行所致）；writer 幂等语义（==post → skip）可容忍，无需清理。

### 5.4 陈旧冷却条目
- `_sensenova_cooldown_20261005.json` 内时间戳已过期，lib 读取时自动忽略；保留原样即可。

---

## 六、后续任务（依赖顺序）

```
【T2.6 修复解析】──► 重跑试点（issue 25 + issue 1/30，writer --drain，断言修正生效）
        │
        ▼
【T2.3 全量（Python 引擎 ≤120 跑全 236 期）】──►【T2.4 复核 A/B + 仲裁（Python）】──►【T2.5 报告】
        │
        ▼
【T4 渲染 + OCR 引擎（复用 lib，≤120 路）】──► 试点 50 张 ──► 全量 16,806 ──►【T5 复核（Python 引擎）】
        │
        ▼
【T6 入大纲：v2 重判 + model_confirmed_v2 + 图文映射表 + 分卷材料清单】
        │
        ▼
【T7 失败清算 + README/注册表/update_log + 终检（覆盖率 100% 断言）】
```

### 6.1 试点重跑（T2.6 验证，命令模板）
```bat
:: 1) 先删断点中 issue 25 行，否则重跑会被跳过
::    编辑 script\_title_fix_done_20261005.jsonl 移除 {"issue_id": 25, ...} 行
python script\_title_fix_engine_20261005.py --issue 25 --workers 1
python script\_title_fix_engine_20261005.py --issue 1  --workers 1
python script\_title_fix_writer_20261005.py --drain
```

### 6.2 全量（T2.3，Python 单进程 ≤120 路）
```bat
:: writer 常驻（唯一写者）
python script\_title_fix_writer_20261005.py --drain
:: 单进程 Python 引擎直跑全部 236 期（--workers 即并发路数，≤120，可自 40 起步视 429 频率上调）
python script\_title_fix_engine_20261005.py --shard 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39 --workers 120
```
> 吞吐不足时可拆为少数几个引擎进程各领互斥分片（如 4 进程 × 10 片、每进程 `--workers 30`），仍不派子代理；staging 为 append-only，多进程追加须谨慎（单进程为上）。引擎每期各开一个 read_only 连接，120 路并发连接 DuckDB 内存占用可观（16GB 机建议先 40 路试跑观察 RSS 再上调）。

### 6.3 复核（T2.4）
```bat
python script\_title_review_engine_20261005.py --channel A --workers 120
python script\_title_review_engine_20261005.py --channel B --workers 120
python script\_title_review_engine_20261005.py --arbitrate --workers 120
python script\_title_fix_writer_20261005.py --drain
```

### 6.4 T4 起（要点，详见 spec）
- T4.1 渲染器：page_scan→150dpi 灰度 JPEG 长边 ≤2000px；embedded→xref 原图（<8KB skip）；文件名=`{figure_id}.jpg` → `script\_fig_ocr_images_20261005\`
- T4.2 引擎：**复用既有线路（import `_sensenova_lib_20261005.py`，KeyPool 轮替存储 key）**、三重对位校验（figure_id ↔ 文件 ↔ raw_path/page）、≤120 线程、相关性优先序、JSONL（figure_id 主键 + pre-image）、**按 figure_id 精确 UPDATE**、page/seq 断言、断点续传
- T5：复核（Python 引擎，通道 A 忠实性 + 通道 B 数字/人名/代码/表格专项 + 仲裁；quality 分入 `review_notes`）
- T6：`outline_mappings` 旧值标 `superseded_by='v2'`；`outline_mappings_figures` 落映射；分卷《;login: 材料清单》→ `15-login杂志史料\大纲映射\`
- T7：`_fig_ocr_final_manifest_20261005.json`；README/关联性普查报告/folder_db_registry 刷新；终检

---

## 七、验收断言（只读 SQL）

```sql
-- 行数不变断言（任何阶段）
select count(*) from articles;   -- 必须 = 6604
select count(*) from figures;    -- 必须 = 16806
-- 二进制合规
select count(*) from information_schema.columns
 where data_type in ('BLOB','VARBINARY','BYTEA');   -- 必须 = 0
-- T2 收口口径（全量+复核后）
select coalesce(seg_review_status,'NULL') s, count(*) from articles group by 1 order by 2 desc;
-- T4/T5 收口口径
select ocr_status, count(*) from figures group by 1;              -- 无 pending/in_progress 残留
select review_status, count(*) from figures group by 1;           -- done 项 reviewed 100%
-- 图位对位抽查
select figure_id, page, kind, raw_path from figures where ocr_status='failed' limit 50;
```

---

## 八、接手指引（按序执行）

1. 读 spec（`.trae\specs\execute-login-title-fix-and-figures-ocr\`）与本任务书；再读 `tasks.md` 中 **Task 2.6（新增阻塞项）**。
2. 修 `_sensenova_lib_20261005.py` 响应解析（见 §5.1 指引 1–3），最小复现：直接重跑 issue 1 窗口即可验证。
3. 按 §6.1 重跑试点 → 断言 `issue 25/1` 出现 `corrected`（或明确 unresolved 原因）且 `quarantine` 为空。
4. 通过后按 §6.2 单进程 Python 引擎全量（≤120 路，writer 常驻，不派子代理），再走 §6.3 复核。
5. T2 收口后按 §6.4 进入 T4（OCR 引擎），最后 T6 入大纲、T7 收尾。

**全程红线**：只读/单写者约束（§4.4）、密钥脱敏、禁二进制、不触碰 `05-卷册大纲` 正文与书稿文件（大纲仅接收结构化映射与报告）。

---

## 附：机读摘要

`script\_t2_handoff_summary_20261005.json`（脚本路径 / 队列 / 断点 / 游标 / 待办 / 阻塞项 / 执行架构，供程序化读取）