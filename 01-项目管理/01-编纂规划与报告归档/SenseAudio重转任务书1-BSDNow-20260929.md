# SenseAudio 重转任务书 1：BSD Now（2026-09-29）

> 主理人令：使用高质量 LLM（SenseAudio ASR）重新转录音频源文件，重新按规则入库、入大纲（既有条目直接原地改写）。本任务书与任务书 2（BSDTalk＋非播客内容）**完全独立**：各自 key、各自滚动池、各自台账与落盘、各自收口。

## 一、范围

- **库**：只写 `03-原始史料库/14-播客史料/bsd-now.duckdb`。
- **音频**：`14-播客史料/audio/` 中 BSD Now 期（命名族 `bsdnow_<n>` 旧代＋`bsd-now_<n>` 新代＋`bsdnow/` 子目录裸号），去重后 **228 期有在盘音频，合计 314.84h**（两代重复 21 期按音源优先级 mp3>ogg>16k.wav 取一）。
- 文件号＝episode_number（已实证：16k wav 字节数/32000 与 duration_seconds 偏差 0.0%）。

## 二、模型与 API（契约书 `_tmp/senseaudio_out/API_CONTRACT.md`）

- 模型：`senseaudio-asr-stream-1.5-260910`（主理人指定），走 **WS 流式端点** `wss://api.senseaudio.cn/ws/v1/realtime/transcriptions`（HTTP 转写端点不收此模型，实测 500）。
- 参数：16k mono s16le PCM（ffmpeg 9.0 解码），server_vad，`x_sense_asr`＝句级＋字级时间戳 on、diarization on（离线模式 degraded，speaker 留空）、**smart_edit off（verbatim 保真）**。
- **术语提交（主理人令，参见在线文档）**：`session.update` 的 `transcription.keywords` 热词数组提交领域术语（FreeBSD/OpenBSD/ZFS/jails/Poudriere/McKusick 等 ~44 词）＋ `transcription.prompt` 识别提示词，提升专名转写准确度。wave1 之前的已转期不带热词，复核不过才用 `--force` 重转。
- 实测 7.5–8 倍实时；单会话 30 分钟 PCM 分块，utterance 时间戳加块偏移。
- fallback：`senseaudio-asr-pro-1.5-260319`（HTTP file_id 直传）。

## 三、key

- `~/.sensenova/senseaudio_keys.json` 的 `tb1_bsdnow`（0600，不入 git）。本任务书**只准用这一把**，与任务书 2 的 key 严格隔离。
- 计费 3.6 元/小时按音频时长；`completed.usage.seconds` 按段累加即计费时长。
- **key 余额耗尽或计费/鉴权错误连续出现 → 立即停止本任务书并通知主理人**（脚本写 `_KEY_EXHAUSTED` 标记、退出码 2）。

## 四、脚本（`script/senseaudio_20260929/tb1/`）

| 脚本 | 用途 |
| --- | --- |
| `01_survey.py` | episode↔文件映射＋时长清单（已完成，`_tmp/senseaudio_out/tb1/survey.json`） |
| `02_transcribe.py` | WS 转录：`--num <epnum>…` / `--next N` / `--all-pending`；逐期 JSON＋台账断点续跑 |
| `03_ingest.py` | JSON → bsd-now.duckdb（transcripts 新行＋segments 全量段；旧转写行保留） |
| `04_outline_rewrite.py` | 05 大纲既有条目原地改写（只碰 BSD Now 期条目） |
| `05_audit.py` | 对账门禁 |
| `06_review.py` | 全量逐篇复核（--dispatch 派发单／--collect 收集裁决） |

落盘：`_tmp/senseaudio_out/tb1/`（json/ 逐期、ledger.jsonl 台账、pcm/ 缓存）。

## 五、执行步骤

1. ~~勘察~~（完成：228 期／314.84h／费用预估 1,133 元）。
2. ~~API 契约实测~~（完成：见契约书实测结论节）。
3. 试点批（期 34＋505）→ 门禁抽查全绿。
4. **8 路子代理滚动**：子代理只领批次（按台账/磁盘 JSON 游标）→ 跑 `02_transcribe.py --num …` → 逐期 JSON 落盘验证 → 回报。**不碰 DB／大纲**（主代理统一入库）。批次完成即补位下一批；429/限速全池退避；子代理回报不作事实源，磁盘 JSON＋台账为唯一事实源；重派前先读盘防双写。
5. **复核波（主理人令：转译完必须逐个复核质量，全量通读非抽查非收尾）**：每波转录完成后，8 路复核子代理逐篇**通读全文**（`06_review.py --dispatch` 生成派发单＋统计，复核口径＝逻辑连贯／无大段乱码复读／无臆造／开头结尾与节目格式自洽／专名拼写合理），逐期写裁决 `reviews/<ep>.json`；`--collect` 收集，**fail 期用 `--force` 重转（带术语热词）→ 再复核**，全部 pass 才入下一步。
6. 复核全过＋全部落盘后主代理统一入库＋大纲原地改写＋对账收口。

## 六、入库规则（03_ingest.py）

- `transcripts` 新行：`id`=新编号、`episode_id`、`full_text`、`model='senseaudio-asr-stream-1.5-260910'`、`language='en'`、`transcribed_at`、`review_status='pending_review'`、`quality_score/flags`（05_audit 回填）。
- `segments` 全量段：utterance 级 `start/end`（秒）、`speaker`（diarization degraded 留空）、`text`；字级 words 留档逐期 JSON（不进 DB）。
- 旧转写行**保留不动**（多模型并存为既有模式）。
- `source_info`：音频 sha256/size/格式。

## 七、入大纲规则（04_outline_rewrite.py）

- 范围：`05-卷册大纲` 中已引用 BSD Now 期的既有条目（`PODCAST_REVIEW` 块内，逐期要点＋`[起-止秒]`＋L1/L2）。
- **既有条目直接原地改写**：按新转写逐条核对文本与时间戳后只改内容与 `[起-止]` 区间；不增删条目、不动其他期条目；新转写与旧引用文本不一致处依新转写订正并留 `[订正]` 痕。
- 改写由主代理串行执行（防并发写文件）。

## 八、对账门禁（05_audit.py，全绿才收口）

1. transcripts 新增行数＝转写成功期数；segments 行数＝utterances 合计。
2. 逐期 full_text 非空、utterances 时间戳单调不倒序。
3. 大纲改写：条目数改写前后守恒、`git diff --numstat` 对账。
4. 重复/空文本检测（复用既有质量口径：severe_repetition 等）。
5. 台账 usage 合计与 records 端点对账（key 余额监控）。

## 九、纪律

- 并发：8 子代理滚动为上限；子代理 25 分钟时间盒；批次 ≤6 期/子代理。
- 长作业跨会话：交接随批更新本文件 §五 进度。
- 台账/磁盘 JSON 为唯一事实源；子代理回报仅作参考。
