# SenseAudio 重转任务书 3：精选与候选音频大转录（2026-10-05）

> 主理人令：对精选（curated）与探索候选（candidates）音频池进行 SenseAudio 大转录，逐字复核、按规则入库、按批入大纲，全链滚动收口。本任务书**取代任务书 2**（BSDTalk 与外部，已多轮打补丁、尽存历史档）；与任务书 1（BSD Now）各自独立：各自库、各自台账、各自收口。
> 落盘＝`_tmp/senseaudio_out/tb2/`；脚本＝`script/senseaudio_20260929/tb2/` ＋ `yt_subs/`。

## 一、范围

- **库**：只写 `03-原始史料库/14-播客史料/youtube.duckdb`（transcripts／segments／source_info）。
- **音频**：`14-播客史料/audio/` 的 `youtube_<vid>.mp3` 族。survey（`01_survey.py` 三步链重建＝01→13 候选补丁→15 curated 补丁）统计 **4,255 期有在盘音频**＝DB 匹配 13＋curated 4,191＋候选 44（去重后口径；curated 清单 `_tmp/yt_channels/curated_final.txt` 4,197）。
- **去重**：转录/入库前按 vid 去重；DB 已有 pass 级 transcripts 的期跳过；同 vid 多 JSON 取最新。
- **当前进度（2026-10-05 18:20 快照，随批更新见 §五）**：转录 **954／4,255**、复核 **915 份**（905 pass／10 fail 挂账）、入库 **senseaudio 行 950 全 `'reviewed'`**（youtube.duckdb transcripts 950／segments 103,279，含 45 期被删 json 历史期 segments 已知 artifact）、费用 ~1,019 元、剩余 **~3,301 期**（ETA 1.7–2.3 天@30 路）。

## 二、模型与 API（契约书 `_tmp/senseaudio_out/API_CONTRACT.md`）

- 模型：`senseaudio-asr-stream-1.5-260910`（主理人指定），走 **WS 流式端点** `wss://api.senseaudio.cn/ws/v1/realtime/transcriptions`。
- 参数：16k mono s16le PCM（ffmpeg 解码）、server_vad、句级＋字级时间戳 on、diarization on（degraded，speaker 留空）、**smart_edit off（verbatim 保真）**。
- **术语提交仍为撤销态**（提示词/热词会被流式模型回声泄漏并诱发臆造——任务书 1 §二 实证；本战役沿用纯净配置）。
- **PCM 流式读取**（2026-10-04 内存改造：`seek/read` 不整载，单进程 RSS 实测 44–55MB；备份 `02_transcribe.py.bak-20261004-preStream`）。
- 15 分钟分块（块偏移加时间戳）；~8x 实时节流；`1011 service unavailable` 为服务端全局并发上限信号（判别定案：全局上限 ≈30–40，与 key 池大小无关）。
- fallback：`senseaudio-asr-pro-1.5-260319`（HTTP file_id 直传）。

## 三、key

- `~/.sensenova/senseaudio_keys.json` 的**轮替池 49 把**（具名 `tb2_bsdtalk_external` 1＋`pool` 48）；两批新增（10-04 晚 10 把、10-05 晨 16 把）均**探针全 OPEN**；备份 `bak-20261004-preGL` / `-preNew10` / `-preNew16`。
- 新增 key 必须先探针（`_tmp/_test_new16.py` 口径：WS 连接 OPEN=有效；401/403=死 key）再导入；导入前备份。
- `_KEY_EXHAUSTED` 标记出现 → 探针逐把测池、剔死 key → 删标记重启。
- 计费 3.6 元/小时按音频时长（`usage.seconds` 累加）。

## 四、脚本

| 脚本 | 用途 |
| --- | --- |
| `tb2/01_survey.py` | episode↔文件映射＋时长清单（**重建＝01→13→15 三步链**） |
| `tb2/02_transcribe.py` | WS 转录（流式 PCM；`--num <db:vid>`／`--next N`／`--force`） |
| `tb2/03_ingest.py` | JSON → youtube.duckdb（**复核 pass 门禁内建**；幂等） |
| `tb2/04_outline_rewrite.py` | 05 大纲既有条目改写派发单（`--num <youtube:vid>`，须带 `youtube:` 前缀） |
| `tb2/05_audit.py` | 对账门禁（五项） |
| `tb2/06_review.py` | 全量逐篇复核（`--dispatch` 派发单／`--collect` 收集裁决；裁决件命名 `<vid>.json`） |
| `tb2/15_parallel_transcribe.py` | 并行转录启动器（nproc 参数；**2.5s 错峰启动**已内置） |
| `tb2/_pcm_gc.py` | PCM 滚动回收（默认干跑；`--apply` 删已完成期＋无 JSON 且 mtime>2h） |
| `yt_subs/09_subs_retry_lowconc.py` | 字幕滚动重试（已修：cookies/ejs flags；WORKERS 8） |
| `yt_subs/13_survey_candidates_audio.py` / `15_survey_curated.py` | survey 补丁（候选/curated 行） |
| `yt_subs/14_audio_curated.py` / `16_redownload_list.py` / `17_diag_fail.py` / `18_audit_mp3.py` | 下载/重下/诊断/审计 |
| `_review_transcripts.py`（script/senseaudio_20260929/） | 机械预筛（语速/覆盖/8-gram/乱码/旧转写对照） |

落盘：`_tmp/senseaudio_out/tb2/`（`json/` 逐期、`ledger.jsonl` 台账、`reviews/` 裁决、`pcm/` 缓存、`mp3_audit.*`、`audio_deleted_*.jsonl` 删件留痕）。

## 五、执行步骤（循环本体——任何会话收到「继续」即按本表机械执行）

1. ~~勘察~~（完成：4,255 期有音频）。
2. ~~API 契约实测~~（完成）。
3. ~~试点批~~（完成）。
4. **转录：30 路 python 直跑**。命令 `python script/senseaudio_20260929/tb2/15_parallel_transcribe.py 30`（run_in_background 直启，勿用 `&`；2.5s 错峰已内置）。
   - 150 路判别定案：本机内存可承载（流式读），但**服务端全局并发上限 ≈30–40**——32/48/80/120 路均触发 1011 风暴（实测记档），**30 路＝上限内最优**；上探唯一前提＝服务方提高配额。
   - worker 随会话结束被回收（已知）；新会话按本步重启，done JSON 自动跳过、零成本接续。
   - 每完成一批即出 JSON（`tb2/json/youtube__<vid>.json`）＋台账追加（`tb2/ledger.jsonl`）。
5. **复核波（逐篇通读，禁抽查）**：
   - `06_review.py --dispatch` 生成派发单（含预计算统计）→ `_review_transcripts.py` 机械预筛；
   - **子代理 4–8 路（≤6 期/路）** 逐篇通读（配额受限时降级 2–3 路或主代理内联机械复核 fallback）；
   - 复核口径：pass＝逻辑连贯成文／无大段乱码复读／无臆造（含**单条 utterance 时长→字数物理校验**，如 1.6s 含数百字＝臆造注入判 fail）／开头结尾与学术演讲格式自洽／专名拼写可还原＋QC 三项（leakage=false、order 单调、truncation 覆盖≥90%且末段缺口<60s）；fail 判据＝大段乱码、复读循环、内容无关、覆盖率<90%、提示词泄漏／模型自述、full_text<200 字符；
   - 裁决写 `tb2/reviews/<vid>.json`（key 须**逐字符含 vid 前导连字符**；python json.dump ensure_ascii=False）；
   - `--collect` 收集；**磁盘按派发清单逐件核对裁决件**（子代理回报仅作参考——已两度实证其可改写 vid／评审未派发期）；
   - fail 期：删 JSON → `--force` 重转（音频坏则先重下）→ 再审；重转一轮仍 fail → 回挂账（fail 裁决挡门禁）。
6. **按批节奏（完成一批→复核一批→入库一批→入大纲一批→清理→门禁→记档）**：
   - **入库**：`03_ingest.py` 干跑→正式（pass 门禁）→**对账**（segments 增量==utterances 合计）→新行置位 `'reviewed'`；
   - **入大纲**：`04_outline_rewrite.py --num …` 派发→**主代理串行原地改写**（只改内容与 [起-止]、不增删、[订正] 留痕）；**本战役新增期均无既有条目**（已逐批核验 0）——入纲归独立增补 campaign（勿抢）；
   - **清理**：删该批已入库期音频（manifest `audio_deleted_*.jsonl` 留痕）→ `_pcm_gc.py --apply`；
   - **门禁**：`05_audit.py`（已知 artifacts 白名单：复核门设计 DB⊂JSON、redo 重复台账、挂账件空正文）；
   - **记档**：本任务书 §一/§五 进度数字＋交接书 §十三＋git 提交（index.lock 竞争重试或延后；陈旧锁先核锁龄）。
7. **触发机制（无定期任务）**：任何会话收到「继续」→ 先**实况复核**（worker 数／ledger 尾项／json 计数／未复核积压／RAM／`_KEY_EXHAUSTED`）→ 自第 4 步续跑；worker=0 或积压>0 均按本表处置；两者皆正常则等积压或小批推进。

**进度批次记录（2026-10-05，跨会话续接位）**：
- **波36 复核**：派 16 组 92 期；**10 组完成、59 期 pass 全落盘验证**（g1–g10；g3 半途重跑一次；防注入物理校验逐期过、无注入）；**1 fail＝Rsk2YZPOpG0**（44.5min 音频空输出 usage=0，已移 failbak，挂账累计 10）。
- **入库本批 +67**（dry→实跑 pass 门禁；segments +5,584，逐件对账全齐；置位 reviewed）→ **DB 950/950 全 reviewed**；本批**无重复 transcript**（dup=0 实证）。
- **清理**：删已入库期音频 **67 期 1.39 GB**（manifest `audio_deleted_w36b.jsonl`）；`_pcm_gc --apply` 回收 done 152（5.34 GB）＋stale 353（18.04 GB），in-flight 148 保留、in-use 273 跳过。
- **审计 05_audit**：仅 3 项**文档化 artifact** 残留（台账 redo 重复键 4、历史被删 json 期 DB segments 残留 45 期），非回归。
- **待续**：复核积压 ~40 期（g11/g12＋w37 四组）；**子代理侧 18 时起瞬态失败**（「计费账户已被冻结」多路→单路试跑成功→再「Model request failed」）——重试或内联 fallback；转录 30 路滚动（最新 18:03:52 起持续推进）。

## 六、入库规则（03_ingest.py）

- `transcripts` 新行（`model='senseaudio-asr-stream-1.5-260910'`、`review_status='pending_review'`）＋`segments` 全量段（utterance 级 start/end/speaker 空/text）；字级 words 留档逐期 JSON。
- 旧转写行**保留不动**；只写 `youtube.duckdb`。
- **pass 门禁**：只入库有 `reviews/` pass 裁决的期；同 episode_id+model 已存在即跳过（幂等）。
- 每批入库后**置位新行 `review_status='reviewed'`**（与既有 senseaudio 行约定一致）＋**行数对账**（自查：schema 层 segments==JSON utterances 合计）。

## 七、入大纲规则（04_outline_rewrite.py）

- 范围：`05-卷册大纲` 中已引用 `YouTube EP<vid>` 的既有条目；**既有条目直接原地改写**（只改内容与 [起-止]、不增删、[订正] 留痕），**主代理串行执行**。
- 本战役为**新增未引用期**：逐批派发结果若为 0 既有条目即记录在案，不再动作；其「增补入纲」属独立 campaign（锚点缺口审计，并行会话在管）。

## 八、对账门禁（05_audit.py，全绿才收口）

1. transcripts 新增行数＝转写成功期数；segments 行数＝utterances 合计（按批对账）。
2. 逐期 full_text 非空、utterances 时间戳单调不倒序。
3. 大纲条目数守恒＋`git diff --numstat` 对账（有改写时）。
4. severe_repetition 检测。
5. 台账 usage 合计（费用与 key 监控）。
- **已知 artifacts 白名单**（非新问题）：复核门设计致 DB⊂JSON、redo 重复台账行、挂账件空 full_text。
- **DB↔跟踪清单差集审计**：定期比对 DB senseaudio episode_id 与全部 passkeys 清单并集，零真实缺口为合格；**累计数字一律读 DB 不手算**。

## 九、纪律

- **并发**：转录一律 python 直跑（30 路，见 §五.4）；复核子代理 4–8 路、**批次 ≤6 期/子代理**、25 分钟时间盒；配额受限时降级（2–3 路）或主代理内联 fallback；并发动前先探针。
- **事实源**：台账／磁盘 JSON／裁决件为唯一事实源；**子代理回报仅作参考**（可改写 vid、可评审未派发期——按派发清单逐件核对）；进度只认磁盘行数。
- **长作业跨会话**：交接随批更新**本任务书 §五＋§一 进度数字**（权威续接位）＋交接书 §十三。
- **git**：按波提交、不等全收口；并行会话高频提交致 index.lock 竞争——重试或延后，陈旧锁（0 字节且锁龄>60s）核实后可清。
- **坑集**（每条实付代价）：① 04_outline `--num` 须 `youtube:<vid>` 前缀（裸 vid 静默 0 匹配）；② 裁决 key 须逐字符含前导连字符（`-qd-Xjkdb2k` 曾丢横杠漏入库）；③ 分片派发后核对「组数×6＝全量」（曾漏派 E 组 6 期）；④ 累计数字读 DB（曾手算错两次）；⑤ 含 `1011` 的一次性单发重转会被 30 路占满服务端婉拒——挂回下批重启时自动重转。
