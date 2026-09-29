# SenseAudio 重转任务书 2：BSDTalk＋非播客内容（2026-09-29）

> 主理人令：使用高质量 LLM（SenseAudio ASR）重新转录音频源文件，重新按规则入库、入大纲（既有条目直接原地改写）。本任务书与任务书 1（BSD Now）**完全独立**：各自 key、各自滚动池、各自台账与落盘、各自收口。**非播客内容（YouTube 等非播客音频）归本任务书。**

## 一、范围

- **库**：`03-原始史料库/14-播客史料/bsdtalk.duckdb`（BSDTalk）＋`youtube.duckdb`（非播客视频）。
- **音频**：`14-播客史料/audio/` 中 BSDTalk 期（命名族 `external_<n>` 旧代＋`bsdtalk_<n>` 新代＋`bsdtalk/` 子目录＋`external/` 子目录裸号）＋YouTube 期（`youtube_<videoId>`）。
- 去重后 **177 期有在盘音频，合计 57.65h**（BSDTalk 169 期＋YouTube 8 期）。
- ⚠️ 小库 5 期（the-changelog／software-engineering-daily／floss-weekly／nerding-out）**无在盘音频**（已删，未重下载），本轮不在范围。
- 文件号＝episode_number（已实证）；**eid 严禁同用做匹配键**（bsdtalk 期 132 的 eid=133 曾错转 133 期音频，已删件重转）。

## 二、模型与 API（契约书 `_tmp/senseaudio_out/API_CONTRACT.md`）

- 模型：`senseaudio-asr-stream-1.5-260910`（主理人指定），走 **WS 流式端点**（HTTP 转写端点不收此模型，实测 500）。
- 参数：16k mono s16le PCM（ffmpeg 9.0 解码，YouTube 期 16k.wav 全部 0 字节假文件、须由 mp3 现解码），server_vad，句级＋字级时间戳 on、diarization on（degraded，speaker 留空）、**smart_edit off（verbatim 保真）**。
- **术语提交（主理人令，参见在线文档）**：`session.update` 的 `transcription.keywords` 热词数组提交领域术语（~44 词）＋ `transcription.prompt` 识别提示词。wave1 之前的已转期不带热词，复核不过才用 `--force` 重转。
- 实测 7.5–8 倍实时；单会话 30 分钟 PCM 分块，utterance 时间戳加块偏移。
- fallback：`senseaudio-asr-pro-1.5-260319`（HTTP file_id 直传）。

## 三、key

- `~/.sensenova/senseaudio_keys.json` 的 `tb2_bsdtalk_external`（0600，不入 git）。本任务书**只准用这一把**。
- 计费 3.6 元/小时按音频时长。
- **key 余额耗尽或计费/鉴权错误连续出现 → 立即停止本任务书并通知主理人**（脚本写 `_KEY_EXHAUSTED` 标记、退出码 2）。

## 四、脚本（`script/senseaudio_20260929/tb2/`）

| 脚本 | 用途 |
| --- | --- |
| `01_survey.py` | episode↔文件映射＋时长清单（已完成，`_tmp/senseaudio_out/tb2/survey.json`） |
| `02_transcribe.py` | WS 转录：`--num <db:epnum>…` / `--next N` / `--all-pending` |
| `03_ingest.py` | JSON → bsdtalk/youtube.duckdb（transcripts 新行＋segments 全量段） |
| `04_outline_rewrite.py` | 05 大纲既有条目原地改写（只碰 BSDTalk/YouTube 期条目） |
| `05_audit.py` | 对账门禁 |
| `06_review.py` | 全量逐篇复核（--dispatch 派发单／--collect 收集裁决） |

落盘：`_tmp/senseaudio_out/tb2/`（json/、ledger.jsonl、pcm/）。

## 五、执行步骤

1. ~~勘察~~（完成：177 期／57.65h／费用预估 208 元）。
2. ~~API 契约实测~~（与任务书 1 共用；bsdtalk:132 冒烟已通过）。
3. 试点批（bsdtalk:132＋bsdtalk:178 三块长文件）→ 门禁抽查全绿。
4. **8 路子代理滚动**：子代理只领批次 → 跑 `02_transcribe.py --num …` → JSON 落盘验证 → 回报。不碰 DB／大纲。滚动与防双写纪律同任务书 1。
5. **复核波（主理人令：转译完必须逐个复核质量，全量通读非抽查非收尾）**：每波转录完成后 8 路复核子代理逐篇**通读全文**（`06_review.py --dispatch/--collect`，裁决 `reviews/<ep>.json`），**fail 期用 `--force` 重转（带术语热词）→ 再复核**，全部 pass 才入下一步。
6. 复核全过＋全部落盘后主代理统一入库＋大纲原地改写＋对账收口。

## 六、入库规则（03_ingest.py）

- `transcripts` 新行（model=`senseaudio-asr-stream-1.5-260910`、review_status='pending_review'）＋`segments` 全量段（utterance 级 start/end/speaker/text）；字级 words 留档逐期 JSON。
- 旧转写行**保留不动**；各库写各自文件（bsdtalk.duckdb／youtube.duckdb）。

## 七、入大纲规则（04_outline_rewrite.py）

- 范围：`05-卷册大纲` 中已引用 BSDTalk／YouTube 期的既有条目。
- **既有条目直接原地改写**：只改内容与 `[起-止]` 区间，不增删条目，订正留痕；主代理串行执行。

## 八、对账门禁（05_audit.py，全绿才收口）

1. transcripts/segments 行数守恒；2. full_text 非空＋时间戳单调；3. 大纲条目数守恒＋numstat；4. 重复/空文本检测；5. 台账 usage 与 records 对账。

## 九、纪律

- 并发：8 子代理滚动为上限；子代理 25 分钟时间盒；批次 ≤6 期/子代理。
- 长作业跨会话：交接随批更新本文件 §五 进度。
- 台账/磁盘 JSON 为唯一事实源；子代理回报仅作参考。
