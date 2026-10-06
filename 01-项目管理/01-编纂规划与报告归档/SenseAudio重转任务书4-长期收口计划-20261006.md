# SenseAudio 重转任务书 4：长期收口计划（2026-10-06）

> 主理人令（1:1 比照任务书九节结构建立长期计划）：按本任务书循环本体机械执行，直至 4,255 期全链收口（转录＋复核＋入库＋入大纲既有改写＋新增条目＋引用期重锚全零）。本任务书**取代任务书3 §五 的长期续接位**（任务书3 尽存循环史与坑集）；与任务书 1（BSD Now）各自独立。

## 一、范围（剩余工作盘点，2026-10-06 18:3x 读 DB 实测）

- **库**：只写 `03-原始史料库/14-播客史料/youtube.duckdb`（本战役 senseaudio 模型行）。
- **当前进度**：转录 **1,495/4,255（35.1%）**；入库 DB **1,488 行全 `'reviewed'`**（积压随到随清）；46 引用期 **5/46 全链**（giceCouM3F8/vVpd34bWCJA/N-7xZB0afyA/rXmWXIDsxig/vC7GITOi1P0，含大纲原地改写）；新增条目 **110/1,380**（试点 10＋批 2–6 各 20，落 292.4 PODCAST_REVIEW 块）；费用 ~1,400 元。
- **剩余**：转录 **~2,760 期**（ETA 1.5–2 天@30 路 1.0–1.35 期/分；中途 worker 耗尽按 §五 重启接续）；复核随转录节奏；新增条目 **~1,270 期**（每批 ≤20 随批，约 64 批）；46 引用期 **41 期**随转录落地（每期 1–44 处引用重锚）；音频/pcm 清理随批。
- 挂账：**11 项 fail 期**（BOPeeLhZOsY、Rsk2YZPOpG0、Y0MYPEKKF0g 等空输出/话术注入）在 failbak，随批重启自动重转重审。

## 二、模型与 API（同任务书3）

- WS 流式端点 `wss://api.senseaudio.cn/ws/v1/realtime/transcriptions`，模型 `senseaudio-asr-stream-1.5-260910`，16k mono s16le、server_vad、smart_edit off（verbatim）、15 分钟分块（BLOCK_SECONDS=900）、~8x 实时；**术语热词已撤销**；PCM 流式读取（`02_transcribe.py` seek/read 增量，RSS 44–55MB/worker）。
- **服务端全局并发上限 ≈30–40**（32/48/80/120 路实测 1011 风暴），**30 路＝上限内最优**；零星 1011 走 worker 内部 retry 自愈，风暴则降并发。

## 三、key（同任务书3）

- 轮替池 **49 把**（具名 1＋pool 48；`~/.sensenova/senseaudio_keys.json`，0600 不入 git；备份 preGL/preNew10/preNew16）；`_next_key()` 轮替。
- 计费 3.6 元/小时；`completed.usage.seconds` 按段累加。
- `_KEY_EXHAUSTED` 标记在位即停转（退出码 2）——探针剔死 key 后重启。

## 四、脚本（任务书3 工具集＋新增条目通道）

| 脚本 | 用途 |
| --- | --- |
| `tb2/15_parallel_transcribe.py 30` | 30 路并行转录（2.5s 错峰；done JSON 自动跳过） |
| `tb2/02_transcribe.py` | WS 转录（--force/--num/--next；流式 PCM） |
| `tb2/03_ingest.py` | 入库（pass 门禁＋幂等；--dry-run） |
| `tb2/06_review.py` | 复核派发/收集（--dispatch/--collect） |
| `tb2/04_outline_rewrite.py --num youtube:<vid>` | 引用期改写派发单（慢，仅单期用；全量用单遍索引法） |
| `tb2/05_audit.py` | 对账门禁 |
| `tb2/_pcm_gc.py --apply` | PCM 回收（done＋stale>2h；in-flight 保留） |
| `yt_subs/46_outline_cited_audio.py` | 引用缺口期音频下载（audio-only 优先，坑⑧） |
| 单遍索引法 | 一次扫全大纲建 `_outline_yt_cites.json`（全量扫描弃用） |
| 新增条目通道 | 批选择（**须传已做集合排除清单**＝pilot map json 并集，坑⑫）→子代理提炼草稿→主代理自块注释起定位落盘（坑⑪）→门禁 |

落盘：`_tmp/senseaudio_out/tb2/`（json/逐期、ledger.jsonl、reviews/裁决件、failbak/挂账件、review_work/ 转储与草稿、audio_deleted_*.jsonl manifests）。

## 五、执行步骤（长期循环本体——任何会话收到「继续」即按本表机械执行）

1. **实况复核**：json 计数／最新 mtime／worker 数（`02_transcribe` 进程数；**worker=0 即重启** `15_parallel_transcribe.py 30`）／未复核积压／RAM／`_KEY_EXHAUSTED`。
2. **转录**：30 路滚动监控；done JSON 自动跳过；46 引用期在池内渐次落地。
3. **复核波**：积压 ≥1 即备转储分组 → 子代理 3–4 路（≤6 期/路；「计费账户已被冻结」「user concurrency limit exceeded」「Model request failed」三种瞬态→重试或降并发）→ 逐篇全文通读（防注入物理校验＋vid 原样键）→ 磁盘逐件核对 → fail 期移 failbak（挂账，下批重启自动重转）。
4. **按批节奏**：
   - **入库**：`03_ingest.py` → 置位 reviewed（**双路**：`episode_id=vid` 直配 ∨ episodes 表映射，坑⑨）→ 对账（新增 segments==utterances）。
   - **入大纲扫描（每批必跑）**：单遍索引核对本批入库期——有引用＝`04_outline_rewrite.py --num` 派发单**主代理串行原地改写**（只改内容与 [起-止]、[订正] 留痕、条目守恒、numstat 对账）；无引用＝转**新增条目通道**（每批 ≤20：批选择传已做集合排除清单 → 子代理提炼草稿（行首会议标记〔…〕＋拟题「拟题：」＋引用后缀）→ 主代理自块注释起定位落盘 → 门禁 citation-tags+markers+numstat）。
   - **清理**：删该批已入库期音频（manifest 留痕）→ `_pcm_gc --apply`。
   - **门禁**：`05_audit.py`（仅文档化 artifact 白名单残留为合格：台账 redo 重复键、被删 json 历史期 segments 残留）。
   - **记档**：本任务书 §一 进度＋git 提交（index.lock 竞争重试；约每 3–5 波一次，非每波）。
5. **等待窗**：积压 0 且 worker 正常时 sleep 5 分钟再查（秒级快查勿长 sleep）。

**里程碑（每达即跑终局审计：05_audit 全绿＋DB↔清单差集＋numstat 对账＋本任务书 §一 更新）**：
- **M1**：转录 50%（~2,128 期）。
- **M2**：转录 100%（4,255 期全落 json）。
- **M3**：复核/入库追平（DB 4,255 全 reviewed、积压 0）。
- **M4**：新增条目 50%（~690/1,380）。
- **M5**：全收口（转录+复核+入库+46 引用期改写 46/46+新增条目 1,380 全零）→ 终局审计＋交接书收尾更新＋通知主理人。

## 六、入库规则（03_ingest.py，同任务书3 §六）

- transcripts 新行（review_status='pending_review'）＋segments 全量段；旧转写行保留；pass 门禁＋幂等。
- 每批置位 reviewed（**双路 SQL**）＋行数对账（segments==utterances，逐件全齐）。

## 七、入大纲规则（同任务书3 §七）

- **每批必跑扫描**；「0 既有条目」是每批扫描的结果、不是免跑令。
- **有引用＝主代理串行原地改写**（只改内容与 [起-止]、[订正] 留痕、条目守恒）。
- **新增条目（增补入纲）**：锚点规则（BSD 主题→技术章；其余→292.4；不确定者挂账待裁）；格式（块内追加：**行首会议/场合标记〔…〕**＋引用后缀 `（YouTube EP<vid>，[起-止]，L1/L2）`＋文献 1 行 [EB/OL]；标题空者「拟题：」自转写标注）；批选择**必须传已做集合排除清单**（坑⑫）；落盘**自块注释起定位锚点**（坑⑪）。
- **坑①–⑫ 全集沿袭**（见任务书3 §九：youtube:<vid> 前缀、dash 键双向、单遍索引、组数核对、DB 读数、1011 单发婉拒、中途截断处置、下载格式、键型双轨、dash 清理判据、块内锚点、批选择排除清单）。

## 八、对账门禁（05_audit.py＋里程碑审计，全绿才收口）

1. transcripts 新增行数＝转写成功期数；segments＝utterances 合计（按批对账）。
2. 逐期 full_text 非空、时间戳单调。
3. 大纲条目数守恒＋numstat 对账（有改写/新增时）。
4. severe_repetition 检测。
5. 台账 usage 合计（费用与 key 监控）。
- **已知 artifacts 白名单**：复核门设计 DB⊂JSON、redo 重复台账、被删 json 历史期 segments 残留。
- **DB↔跟踪清单差集审计**：定期比对；累计数字一律读 DB 不手算。

## 九、纪律

- 转录一律 python 直跑 30 路；复核子代理 3–4 路、≤6 期/路、配额感知降级；并发动前先探针。
- 台账／磁盘 JSON／裁决件为唯一事实源；子代理回报仅作参考（按派发清单逐件核对）。
- 长作业跨会话：交接随批更新**本任务书 §一 进度数字**（权威续接位）；任务书3 尽存循环史与坑集详解。
- git 按波提交、不等全收口；index.lock 竞争重试或延后。
- 挂账 11 项 fail 期随批重转重审；仍 fail 维持挂账（不无限重转，服务侧故障另报主理人）。