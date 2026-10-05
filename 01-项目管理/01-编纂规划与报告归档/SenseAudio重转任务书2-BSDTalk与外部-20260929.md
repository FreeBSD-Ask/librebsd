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
- **术语提交（已撤销，2026-09-29 复核实证）**：曾按主理人令提交 `keywords`＋`prompt`；复核发现流式模型会回声泄漏提示词块并诱发臆造模板段（tb1 期 25-31 六期 fail 实证），故撤销、回归纯净配置；fail 期 `--force` 重转。
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
6. **按批节奏（主理人令 2026-09-29：完成一批→逐字逐段完整复核一批→解读一批并与既有转写比较确认→入库一批→按规则入大纲一批，不计成本、加快频次、先补遗）**：入库脚本已加复核门（只入库有 pass 裁决的期）；大纲改写按派发单逐期原地改写；每批完成即入库＋派大纲改写。

**执行进度（2026-10-04 22:2x，随批更新——跨会话续接权威位）**：
- 转录：30 路 python 直跑滚动（`15_parallel_transcribe.py 30`；json 29x/待转 ~3,9xx，30 路实测 1.0–1.35 期/分，全程约 2.1–2.8 天）。§五.4「8 路子代理转录」已被 handoff §九.7 主理人令**取代＝python 直跑**；§五.5「带术语热词」已被 §二.17 撤销条款取代；§三 单把 key 已被主理人池扩展（49 把轮替）取代。
- 复核波1＝48 期（8 路×6 期子代理）：**47 pass／1 fail**（`luPViknmoXc` 泄漏重转一轮仍复现→挂账；另有 BOPee、pynpY7Isbxs 挂账）。裁决件已对齐本任务书命名 `<epnum>.json`（原 `youtube__<vid>.json` 74 份已改名）。
- 复核波2＝48 期（8 路×6 期）：**48/48 全 pass**（0 fail；ASR 专名漂移 issues 留档）；机械预筛 307 期 13 标记（12 临界 wpm＋BOPee）。
- 复核波3＝48 期（8 路×6 期）：**48/48 全 pass**。
- 复核波4＝48 期（8 路×6 期）：**47 pass／1 fail**（`yzv9lcjxhAg` 臆造拒绝话术泄漏，一次性重转被 30 路占满的 1011 拒→挂回待转下批重转重审）。挂账累计 4：BOPee／pynpY7Isbxs／luPViknmoXc／yzv9lcjxhAg。
- 复核波5＝48 期（8 路×6 期）：**47 pass／1 fail**（`e5g9blIkp0g` 泄漏 "Please provide the audio input"，一次性重转被 1011 拒→挂回待转）。**挂账累计 5**：BOPee／pynpY7Isbxs／luPViknmoXc／yzv9lcjxhAg／e5g9blIkp0g（均 fail 裁决挡门禁，下批 15_parallel 启动时自动重转重审）。
- 复核波6＝15 期（3 路×5 期小批）：**15/15 全 pass**。
- 复核波7＝12 期（2 路×6 期）：**11 pass／1 fail**（`XT7soOM_YuM` 大段乱码→--force 重转成功→再审 **pass**→入库，全链闭环）。
- 复核波8＝17 期（3 路 6+6+5）：**16 pass／1 fail**（`nyNCSM4vGF4` 泄漏 "What every good ASR engine does, back off and jitter"，一次性重转被 1011 拒→挂回待转）。**挂账累计 6**：BOPee／pynpY7Isbxs／luPViknmoXc／yzv9lcjxhAg／e5g9blIkp0g／nyNCSM4vGF4（fail 裁决挡门禁，下批 15_parallel 启动时自动重转重审）。
- 复核波9＝4 期（1 路）：**4/4 全 pass**；复核波10＝6 期（1 路）：**6/6 全 pass**；复核波11＝9 期（2 路 6+3）：**9/9 全 pass**；复核波12＝13 期（3 路 6+6+1）：**12 pass／1 fail**（`X2rx9H5Aw20` 泄漏模板回声→挂账）。
- 复核波13＝30 期（5 路×6 期，其中 2 路撞「user concurrency limit exceeded」后降 2 路重派成功）：**30/30 全 pass**。
- 复核波14＝17 期（3 路 6+6+5）：**17/17 全 pass**；复核波15＝34 期（6 路分段 4+1+2 重派规避并发上限）：**34/34 全 pass**。⚠️ 并发上限坑两度出现（5 路并行即可能触发 user concurrency limit exceeded），处置＝降路数重派（已两次实证）。
- 复核波16＝18 期（3 路×6 期）：**18/18 全 pass**。
- 复核波18补＝6 期（E 组首派撞并发限额漏派，单路补派）：**6/6 全 pass**；复核波20＝48 期（8 路首派 4 组撞限额，4 组降级重派）：**48/48 全 pass**。⚠️ 并发限额坑累计四次实证；⚠️ 流程坑新记：**分片派发后必须核对「组数×6＝全量」再收口**（波20 曾漏派 E 组 6 期，靠收口验证抓回）。
- 复核波17＝4 期（1 路）：**4/4 全 pass**。
- 复核波18＝9 期（2 路 6+3）：**9/9 全 pass**。⚠️ 新坑：并行子代理派发撞账号并发上限（user concurrency limit exceeded），处置＝降低并行路数重派。
- 复核波19＝48 期（8 路×6 期派发，3 路撞并发上限降级重派）：**47 pass／1 fail**（`Qc0QRdxVv3g` 空转录 full_text=0 字符→**挂账累计 8**：前 7 项＋Qc0QRdxVv3g；fail 裁决挡门禁，下批 15_parallel 启动时自动重转重审）。⚠️ 新坑：`-qd-Xjkdb2k`（vid 带前导横杠）裁决文件 key 被写成 `youtube:qd-Xjkdb2k`（丢横杠）→门禁按 key 匹配漏入库；修正 key 后补入库对账一致——**裁决文件 key 必须逐字符含 vid 前导连字符**。
- 入库累计 **+590 transcripts**（…＋波20 42＋波20E补 6＋XT7soOM_YuM 1，每批对账 segments==utterances 逐件一致；DB↔跟踪清单差集审计＝零真实缺口，635＝45 旧战役＋590 本战役）；senseaudio 行 **635 全 `'reviewed'`**；删已入库音频累计 ~11.5GB（manifest×28）。
- 入大纲：119 期 pass 件派发＝**全部 0 既有条目**（本战役为新增未引用期；入纲=独立增补 campaign）。
- 清理：删已入库期音频 119 件（manifest×2 留痕）；`_pcm_gc.py` 多轮回收（含「无JSON且mtime>2h」规则，主理人已批）。
- `05_audit.py` 门禁 5 FAIL 全为已知 artifacts（复核门设计致 DB⊂JSON、redo 重复台账 3、BOPee 挂账件空正文），非新问题。
- 长期计划手册＝交接书 §十四（严格本任务书流程循环）。

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
