# SenseAudio 重转任务书 3：精选与候选音频大转录（2026-10-05）

> 主理人令：对精选（curated）与探索候选（candidates）音频池进行 SenseAudio 大转录，逐字复核、按规则入库、按批入大纲（**既有条目原地改写＋无引用期新增条目增补入纲**，2026-10-06 批准），全链滚动收口。本任务书**取代任务书 2**（BSDTalk 与外部，已多轮打补丁、尽存历史档）；与任务书 1（BSD Now）各自独立：各自库、各自台账、各自收口。
> 落盘＝`_tmp/senseaudio_out/tb2/`；脚本＝`script/senseaudio_20260929/tb2/` ＋ `yt_subs/`。

## 一、范围

- **库**：只写 `03-原始史料库/14-播客史料/youtube.duckdb`（transcripts／segments／source_info）。
- **音频**：`14-播客史料/audio/` 的 `youtube_<vid>.mp3` 族。survey（`01_survey.py` 三步链重建＝01→13 候选补丁→15 curated 补丁）统计 **4,255 期有在盘音频**＝DB 匹配 13＋curated 4,191＋候选 44（去重后口径；curated 清单 `_tmp/yt_channels/curated_final.txt` 4,197）。
- **去重**：转录/入库前按 vid 去重；DB 已有 pass 级 transcripts 的期跳过；同 vid 多 JSON 取最新。
- **当前进度（2026-10-05 23:40 快照，随批更新见 §五）**：转录 **1,102／4,255**（json 全 1,102、30 路滚动中）、复核 **1,085 份全清（未复核积压 0）**、入库 **senseaudio 行 1,126 全 `'reviewed'`**、费用 ~1,163 元、剩余 **3,153 期**（ETA ~1.6 天@30 路）；循环进入稳态：新完成即复核→入库。

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

> ⚠️ **长期续接位已由《SenseAudio重转任务书4-长期收口计划-20261006.md》取代**（2026-10-06 主理人令，1:1 九节＋里程碑 M1–M5 至全收口）：后续循环与收口以任务书4 为准；本任务书尽存循环史与坑集详解（坑①–⑫ 以任务书3 为权威定义）。

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
   - **入大纲（每批必跑，10-06 主理人订正）**：单遍索引法扫描（一次扫全大纲抓 `YouTube EP<vid>` 建 `_outline_yt_cites.json`；逐期×逐文件全量跑实测 >10min 弃用）核对**本批入库期**——**有引用＝主代理串行原地改写**（只改内容与 [起-止]、不增删、[订正] 留痕）；**无引用＝转「新增条目（增补入纲）」通道**（锚点规则＋格式见 §七，试点批 10 期先行→验收→每批 ≤20 期滚动）。「0 既有条目」是每批扫描的结果、不是免跑令；详见 §七。
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
- **波37–40 复核＋第二批入库（2026-10-05 晚）**：w37 **23/23**、w38 **26/26**、w39 **3/3**、w40 **4/4 全 pass 落盘验证**；入库第二批 **+43**（置位后 **DB 993/993 全 reviewed**，43 期逐件对账全齐）；删已入库期音频 **43 期 0.94 GB**（manifest `audio_deleted_w38.jsonl`）＋pcm 回收 1.46 GB；审计仅 4 项文档化 artifact（台账 redo＋被删 json 历史期）。
- **22:37 快照**：json **1,075**／reviews **967**（957 pass／10 fail）／DB **993 reviewed**；**复核积压 118 期**——续派降积压；费用 ~1,027 元。
- **坑 ⑥（新增）**：子代理在长提示词＋多期下**偶发中途截断**（实证 3 例：w36g3 半途、w37g1 空写、w38g4 半途；另有「计费账户已被冻结」「Model request failed」两种瞬态）——处置＝提示词改「**每期读毕判毕立即落盘、全部落盘后再回报**」＋重派（skip-if-exists）即补齐；磁盘裁决件为唯一事实源。
- **波41 全清＋第四批入库（2026-10-05 深夜）**：w41 **114/114**（113 pass＋1 项 rsNsoJfJiQA 经主代理直查改判 pass 留痕：idx51 1.0s/31 字符=31 c/s 触 25 启发线，但硬注入判据未触发、系两条 30s 长段间 VAD 边界伪迹）；入库第四批 **+36**（第三批 +79，置位后 **DB 1,108/1,108 全 reviewed**，130 期逐件对账全齐）；删已入库期音频 **78＋36 期 ~2.27 GB**（manifest `audio_deleted_w41a/b.jsonl`，w41a 首件因脚本漏 import time 崩溃时 1 件已删未记 manifest——教训：删音频循环须整体幂等重跑）；pcm 回收 ~24 GB 累计；审计仍 4 项文档化 artifact。
- **23:34 快照**：json **1,102**／reviews **1,085**（1,075 pass／10 fail）／DB **1,108 reviewed**；积压 27 期（w42 五组已备）；费用 ~1,163 元。
- **波49–52（2026-10-06 上午）**：w49 **24/24**、w50 **24/24**、w51 **17 pass＋1 fail**（Y0MYPEKKF0g：71 分钟仅转出一句 "Hello, this is a test message." 模型话术→failbak，挂账累计 11；Rsk2YZPOpG0 重转再空，挂账维持）、w52 **71/71**（含多期物理核证：QwhRYXsi9X8 尾段 46 分钟数字静音、dxpzis2riZc 前段无语音，均 pass 留痕）；入库累计 +101（置位后 **DB 1,280/1,280 全 reviewed**）；删已入库音频 ~2.4GB；坑⑨（episode_id 双轨：vid 直配 ∨ episodes 表数值映射，裁决件一律 vid 键）与坑⑩（dash 键双向皆可错）实证记档。46 引用期已转 2/46（giceCouM3F8、vVpd34bWCJA 已 pass→入库，其 4 个大纲文件待原地改写）。
- **10:05 快照**：json **1,303**／DB **1,280 reviewed**／积压 23（w53 待派）；费用 ~1,368 元。
- **46 引用期链④ 首批入大纲完成（2026-10-06，`31dc4dd1a`）**：giceCouM3F8（NetBSD 短片）＋vVpd34bWCJA（jails 实操）pass→入库→**4 文件 20 条内容条目原地改写**（时间戳依 senseaudio 新转写重锚：jails 流程 [75.6-291.1]、规模化 [294.9-353.8] 等；rev6 核查卡增 senseaudio 再核轮；NetBSD 创立者失真由新转写解决、Charles M Hannum）；门禁 numstat 20=20 原地守恒＋引用行数逐文件不变＋[订正] 留痕。余 44 期待转录落地后同链。
- **波53–61 稳态循环（2026-10-06 12:45 快照）**：w53 24/24、w54 13/13、w55 10/10、w56–61 随到随清（每期均 pass）——DB **1,341/1,341 全 reviewed**、积压 0；30 路滚动 8x 实时；费用 ~1,400 元；46 引用期已转 2/46（首批已全链）。审计持续仅 3–5 项文档化 artifact（台账 redo 重复键、历史被删 json 期 segments 残留）。
- **自驱动循环轮 w62–66（2026-10-06 13:36，按已批计划连续执行 §五 全步）**：w62 12/12、w63 11/11、w64 5/5、w65 2/2、w66 6/6 全 pass——DB **1,377/1,377 全 reviewed**、积压 2；每批含入大纲扫描（cited 仍 2/46，无新引用落地）；删音频 36 期 ~0.74GB；BOPeeLhZOsY 重转再空移 failbak（挂账维持，音频仅 0.2min/1 utt 空输出同 Rsk2 模式）。
- **46 引用期第 3 期全链（2026-10-06，w67/68＋`6042bc1db`）**：w67 2/2、w68 10/10 pass；**N-7xZB0afyA**（FreeBSD Fridays 安全入门，36 处引用）pass→入库→**4 文件 28 条镜像条目原地改写**（时间戳重锚：审计谱系 [1075.1-1191.3]、pf 扩散 [957.0-987.0]、三防火墙 [987.0-1043.9]、ipfw 演示 [213.4-1232.4] 等；讲者名失真由新转写缓解 Antranig Basmanian）；门禁 numstat 28=28＋引用行数守恒。cited **3/46**；DB 1,389/1,389 reviewed；删音频 12 期 ~0.4GB。
- **入大纲新增条目试点批（2026-10-06，`d3c452cd7`＋修正 `5d4d599be`，主理人批准纳入）**：292.4 PODCAST_REVIEW 块落 **10 期 BSD 会议/讲座录像**（要点 20 行＋文献 10 行；**行首会议/场合标记〔…〕**＋引用后缀（[起-止] 前后半分、L1）；McKusick 内核/安全两讲、Robert Watson TrustedBSD、jails 实操、OpenZFS 移植与读写路径、SCMI、BSDCan 发起/文档翻译、Aerosource）；门禁＝引用标签可被索引扫描命中（PASS）＋numstat 对账。**坑 ⑪（新增）**：插入锚点 `**史料**：` 用 find 命中同文件 292.4.1 小节同名标记（该文件多处 **史料**：），20 条要点误插小节且草稿缺引用后缀——处置＝整块剪切重插入块内锚点（自 PODCAST_REVIEW 注释起向后找）＋逐条补引用/标记；**新增条目落盘一律自块注释起定位锚点**。**试点待主理人验收后滚动**（全量 ~1,380 期无既有条目，每批 ≤20 期随批节奏执行）；锚点规则与格式（含会议标记）已写入 §七。
- **新增条目批 2/3＋46 引用期第 4 期（2026-10-06，w71/72＋`c8c7a7539`＋`65c60e1fe`＋`836a28f06`）**：w71 6/6、w72 6/6 pass；**rXmWXIDsxig**（FreeBSD Deep Dive 播客，14 处引用）pass→入库→2 文件 10 条镜像条目重锚（`65c60e1fe`）；新增条目批 2/3 各 20 期落 292.4（批2 `c8c7a7539`：要点 40＋文献 20；批3 `836a28f06`：要点 39＋文献 20，标题空者「拟题：」自转写标注）。**实况：1,392/1,396 无引用期 json 标题为空**（survey 行无 title）——拟题通道定案。cited **4/46**；DB 1,405/1,405 reviewed；新增条目累计 50/1,380 期。
- **46 引用期第 5 期＋新增条目批 4＋w73 大波（2026-10-06 17:2x，`b53126655`＋`cfa9d1f10`）**：json 涨至 1,469（+61）；w73 g1–g9 **54/54 pass**（Blade/Twizzler/Kinetic/Piranha/Midas/Swiss/WhisperFuzz/AFL++/netmap/Mirai 等）；**vC7GITOi1P0**（Libreswan Lightning Talk Red Pill，7 处引用）pass→入库→94.4 五条重锚（`b53126655`：缘起 9.7-73.9/蓝药丸 36.3-110.7/红药丸 111.0-173.9/悬而未决 174.5-342.0）；新增条目批 4 20 期落 292.4（`cfa9d1f10`：要点 40＋文献 20，USENIX ATC/Security/NSDI/FAST 据转写明示或论文匹配推断）。cited **5/46**；DB **1,460/1,460 reviewed**；删音频 55 期 ~1.1GB；pcm 回收 ~10.5GB；新增条目累计 **70/1,380 期**；w73 余 g10/g11 在派。
- **w74＋新增条目批 5（2026-10-06 18:0x，w74 9/9 pass＋批5 `92919de16`）**：w73 g10/g11 补清（含 Facedancer 误落盘 `.txt.json` 已删重写）；w74 9/9 pass——DB **1,478/1,478 reviewed**；删音频 9 期；**新增条目批 5 撞车事件**：代理不知已做集合重选了与批 2 相同的 19/20 期——作废重选（排除 p1-p4 全部 90 期）后 20 期落 292.4（`92919de16`：要点 40＋文献 20，OSDI '14/SREcon22 EMEA/NSDI '23/'24/'26/USENIX Security '22/'24/OSDI '20 8 期据检索确证、9 期会议不详如实标注）；**坑 ⑫（新增）**：批选择代理必须传入**已做集合排除清单**（pilot1-4 map json 并集），否则重做同批——已作废重选。新增条目累计 **90/1,380 期**。
- **批 6＋w74 补清（2026-10-06 18:2x，批6 `89c799456`）**：w74 补清 10/10 pass（DNS 缓存投毒缓解/Rapid 架构/USB Driver Fuzzing/Barrelfish/NVMe-oTCP profiling/Poise/FirmScope/IaC bare metal/DNS 测量等）；批 6 20 期落 292.4（`89c799456`：要点 40＋文献 20，USENIX Security/SRECon/HotEdge 2020/Emerging Languages Camp 2010/独立讲座据转写确证、会议不详如实标注；Zeno/Blockade/YPIR/Spoiler/Quorum ORAM/EMT/Netflix Simian/SkyPilot/Messy BGP 等）；门禁 citation-tags+markers PASS。DB **1,488/1,488 reviewed**；删音频 10 期；pcm 回收 ~4.7GB；新增条目累计 **110/1,380 期**；cited 5/46。
- **批 7＋w123 复核波（2026-10-07 12:xx，批7 `8379bd88d`）**：w123 复核波 27 期全 pass（5 组子代理；此前积压全清）；入库 +27（置位后 **DB 2,047/2,047 全 reviewed**）；**批 7 20 期落 292.4（`8379bd88d`：要点 40＋文献 20，排除 pilot2-6+10 已做集合 110 期后从池 1,949 期取队首 20；037D7YZCpSM ROBOT/06AHMYwPdDY AuthenCall/0A-wIt2lsvY WPA2 形式化分析据转写确证 USENIX Security，会议不详如实标注）**；门禁 citation-tags+markers PASS＋numstat 60/0。**坑 ⑬（新增）**：旧会话崩溃残留的 `index.lock`（3.9 MB 非零字节＝带暂存内容）删后提交会把**他人行的暂存件**（mail2d_read_ledger.json）卷进本批提交——处置＝`reset --soft HEAD~1` 后 pathspec 单独重提（`8379bd88d`＝292.4 60/0），他人件保持 staged 原状归还；**删 `.git/index.lock` 前先 `git status --porcelain` 盘点暂存区、删后首提须 `git show --stat` 对账**。新增条目累计 **130/1,380 期**；cited 10/46（DXX4HDd3vDQ 链收口，重锚已由 `fd98be627` 完成）；pcm 回收 +2.43GB；转录 2,065/4,255（48.5%）——M1（2,128）在望。
- **w124 复核波＋批 8 派发（2026-10-07 12:2x）**：w124 F/G/H/I 共 4 组 23 期全 pass（23 期判定文件落盘＋验证 key 全对）；入库 +23（置位后 **DB 2,070/2,070 全 reviewed**）；outline 扫描 23 期全无既有引用＝批 8 料（已派 2 组内容写手，排除已做集合 130 期后取 20）；pcm 回收 +2.95GB；转录 json 2,073/4,255（48.7%）；批 8 之后新增条目将累计 150/1,380。**教训（坑⑬续）**：他人行暂存件未清偿前，本线一切提交必须 pathspec 限定（实测两次无 pathspec 提交都卷入 mail2d_read_ledger.json，均已 reset --soft 后单独重提）。
- **批 8 落 292.4（2026-10-07 12:4x，`e697be8ec`）**：20 期要点 40 行＋文献 20 行，门禁 citation-tags+markers PASS＋numstat 60/0；**坑 ⑭（新增）**：内容写手可整批漏掉引用后缀（批 8 写手 B 20 点行全部缺 `（YouTube EP<vid>，[起-止]，L1）`）——收货校验必须逐行断言后缀（本线校验器拦下），补齐＝按转写前后半场机械切分取 utterance 边界（[首-中]/[中-末]）；会议标记批 8 写手经逐条检索确证（Groove=OSDI'22、PHE=USENIX Sec'18、Nodens=ATC'23、MAGE、Z-Lane、Pulsar=OSDI'14 等）。新增条目累计 **150/1,380 期**。
- **w125 复核波（含 1 fail）＋46 引用期第 11 期（2026-10-07 13:0x，`8760718b8`）**：w125 J/K/L/M 共 4 组 23 期（22 pass＋**1 fail＝jYe2XVCnU5w KVIMR 中间件讲座术语系统性音写漂移密度极高、成片语义不可读**，json+verdict 移 failbak 挂账累计 14）；入库 +22（**i7pkyDUX5uM 为 episodes 表数字 id 292 行、直接 vid 更新 +21 后余 1，经 link 反查补置位**）；**i7pkyDUX5uM**（AsiaBSDCon 2009 Theo de Raadt OpenBSD 发布流程，cited-46 第 11 期）pass→3 文件 8 条镜像条目重锚（`8760718b8`：总纲9 793.56→787.8、2003-2005 惩罚周期 1337.279→1327.9、一手史料 1062.52→1059.6；**内容差异新发现＝"每日约 300 commits" 新转写实为"中位约 50 次/日、黑客松尖峰至 300 次/日"（112.4-128.9 区间外），X 组件集成内容 437.2-516.7 且新转写无 Herrb 点名——均已入 [订正] 注**，5 条核符未变）；cited **11/46**；DB **2,092/2,092 reviewed**；pcm 回收 +3.44GB；转录 2,098/4,255（49.3%）——M1（2,128）在望。
- **批 9 落 292.4（2026-10-07 13:1x，`4dd40ec58`）**：20 期要点 40 行＋文献 20 行，排除已做集合 150 期后取 20；3VuZQXbPP9I〔USENIX Security（推测）〕/3cDztgVGFgQ〔USENIX ATC（推测）〕/3X-Ea2RTjmw·3d10eg6MNdM〔NSDI（推测）〕据转写/论文推断、36myc8wQhLo 为 OSDI/ATC 联合主旨演讲（Tim Roscoe/ETH 开场明示）、其余会议不详如实标注；**批 9 起提示词加粗引用后缀自查令后写手零缺缀（坑⑭修复验证）**；门禁 citation-tags+markers PASS＋numstat 60/0。新增条目累计 **170/1,380 期**；转录 2,098/4,255（49.3%）——M1（2,128）在望。
- **w126 复核波（2026-10-07 13:4x）**：w126 8 期全 pass（单组子代理；wave N）；入库 +8（置位后 **DB 2,100/2,100 全 reviewed**）；outline 扫描 8 期全无既有引用＝批 10 料；pcm 回收 +2.33GB；转录 2,105/4,255（49.5%）——M1（2,128）差 23 期；转录速率放缓（~1 期/8min，30 路 worker 36 进程活跃）；新增条目累计 170/1,380。
- **w127 复核波（2026-10-07 14:1x）**：w127 8 期全 pass（单组子代理；wave O）；入库 +8（置位后 **DB 2,108/2,108 全 reviewed**）；outline 扫描 8 期全无既有引用＝批 10 料；pcm 回收 +1.2GB；转录 2,113/4,255（49.7%）——M1（2,128）差 15 期。
- **w128 复核波（2026-10-07 14:4x）**：w128 8 期全 pass（单组子代理；wave P；8 期 utterance 时间戳为 null 已记 issues）；入库 +8（置位后 **DB 2,116/2,116 全 reviewed**）；outline 扫描 8 期全无既有引用＝批 10 料；pcm 回收 +2.2GB；转录 2,127/4,255（49.99%）——**M1（2,128）差 1 期**。
- **M1 达成＋w129 复核波（含 1 fail）（2026-10-07 15:4x）**：**M1（转录 50%＝2,128 期）15:04 达成**，终局审计入任务书4（json 2,128=50.0%；DB 全 reviewed；cited 11/46；新增条目 170/1,380；审计备注＝vid 基底差集对数字轨道行有假缺）；w129 Q/R/S 3 组 15 期（14 pass＋**1 fail＝tew7TW-Y3MA utterance 泄漏 ASR 系统提示词 381.7-386.4s**，json+verdict 移 failbak 挂账累计 15）；入库 +14（置位后 **DB 2,130/2,130 全 reviewed**）；outline 扫描 14 期全无既有引用＝批 10 料；pcm 回收 +3.43GB；转录 2,139/4,255（50.3%）——进入 M2 阶段。
- **批 10 落 292.4（2026-10-07 15:5x，`4e0d1f544`）**：14 期要点 28 行＋文献 14 行（批 <20 期滚动执行），门禁 citation-tags+markers PASS＋numstat 42/0；UMyQ4EQpPVc=〔SREcon〕（转写明示）、其余据转写/论文推断或会议不详如实标注。新增条目累计 **184/1,380 期**。
- **w130 复核波（2026-10-07 16:2x）**：w130 6 期全 pass（单组子代理；wave T）；入库 +6（置位后 **DB 2,136/2,136 全 reviewed**）；outline 扫描 6 期全无既有引用＝批 11 料；pcm 回收 +1.87GB；转录 2,140/4,255（50.3%）；新增条目累计 184/1,380。
- **波42 全清＋复核追平（2026-10-05 23:40）**：w42 **27/27 全 pass**；入库 +18（置位后 **DB 1,126/1,126 全 reviewed**）；删音频 18 期 0.33 GB；审计仅 4 项文档化 artifact；**json 1,102 未复核积压 0——复核管线完全追平转录，循环进入稳态**（新完成→复核→入库节奏持续推进）。
- **波43/44 小批（2026-10-05 23:55）**：w44 4/4 pass（BcjIURWwUHI 等）；入库 +4（置位后 **DB 1,130/1,130 全 reviewed**）；删音频 4 期；已删 json 期的陈旧 pass 裁决致 pass-not-in-DB 计数含 21 项虚高（幂等空跑 +0 验证，无缺口）。稳态持续：30 路滚动、复核随到随清。
- **46 期扩入施工（2026-10-06 主理人批准「同时执行」）**：46 期音频全量下载（音频探针 46/46 过、3.21 GB、fail=0；下载格式定案见坑⑧）；survey 46 行填 `audio_files/upload_source` 后按机制杀旧 30 路＋`15_parallel_transcribe.py 30` 重启（pending 3,195→30 chunks×106，46 期散布入池，done JSON 自动跳过零成本接续）；主循环同窗续跑（w45 7/7、w46 9/9、w47 2/2、w48 24/24 全 pass；DB **1,165/1,165 reviewed**；删音频 31 期 ~0.5GB；pcm 回收 ~22.7GB）。46 期转录完成后＝复核→入库→**按 `_outline_yt_cites.json` 索引逐期原地改写 PODCAST_REVIEW 块（主代理串行）**。

## 六、入库规则（03_ingest.py）

- `transcripts` 新行（`model='senseaudio-asr-stream-1.5-260910'`、`review_status='pending_review'`）＋`segments` 全量段（utterance 级 start/end/speaker 空/text）；字级 words 留档逐期 JSON。
- 旧转写行**保留不动**；只写 `youtube.duckdb`。
- **pass 门禁**：只入库有 `reviews/` pass 裁决的期；同 episode_id+model 已存在即跳过（幂等）。
- 每批入库后**置位新行 `review_status='reviewed'`**（与既有 senseaudio 行约定一致）＋**行数对账**（自查：schema 层 segments==JSON utterances 合计）。

## 七、入大纲规则（04_outline_rewrite.py）——**每批必跑，不得沿用旧快照结论**

- **每批必跑扫描**：单遍索引法（一次扫全 `05-卷册大纲` 抓 `YouTube EP<vid>` 标签建 `_tmp/senseaudio_out/tb2/_outline_yt_cites.json` 索引；`04_outline_rewrite.py` 逐期×逐文件全量跑实测 >10 分钟未完，弃用）核对本批入库期是否被既有条目引用。
- **有引用＝主代理串行原地改写**：只改内容与 `[起-止]`、不增删条目、`[订正]` 留痕。
- **新增条目（增补入纲，2026-10-06 主理人批准纳入）**：对通过复核入库且无既有引用条目的期，**新建条目**入纲：
  - **锚点规则**：BSD 主题期（FreeBSD Fridays、BSDCan、EuroBSDCon 等）→ 按主题映射既有技术章（pf/防火墙→103 章、jails→94 章、audit→136.4、存储/文件系统→对应章等）；其余通用技术演讲 → 统一挂载 **292.4「视频与音频资源-会议录像-播客与教程生态」**；锚点不确定者挂账待裁，不强行落位。
  - **格式**：在目标文件既有 PODCAST_REVIEW 块内**追加**（不新建块、不动其他期条目）：要点 1–2 条（**行首加会议/场合标记〔…〕以示区别，主理人 10-06 令**；会场不详者标〔会议不详〕、据转写推断者注记）＋引用后缀 `（YouTube EP<vid>，[起-止]，L1/L2）`＋文献 1 行 `[YouTube EP<vid>] YouTube. YouTube: <标题>[EB/OL]. ()[2026-08-15]. <https://www.youtube.com/watch?v=<vid>>`；要点从新转写提炼，L1＝实操演示与一手陈述、L2＝转述定位。
  - **节奏**：试点批 10 期先行（BSD 主题期）→ 门禁（引用标签可被索引扫描命中、numstat 对账、05_audit）→ 主理人验收格式后滚动，每批 ≤20 期随批节奏执行。
- **0 引用＝当批记录在案**（转入「新增条目」通道，不再只记录不动）。
- **坑 ⑦（10-06 主理人订正）**：曾把早期批次「派发 0 既有条目」的结论当后续所有批次的免跑依据，跳过扫描动作——条件性跳过（若 0 则记录）被误读成无条件跳过。**「0」只能是当批扫描的输出。**
- **已知素材缺口→已扩入（2026-10-06 全量扫描＋主理人当日批准执行）**：大纲共 **1,459 处 `YouTube EP<vid>` 引用／46 个 vid**，全部不在原 survey 且无 transcript——**已批准扩入本战役**：46 期音频已全量下载（cookies 管线＋ffmpeg 探针，**46/46 全过 fail=0**，合计 3.21 GB；下载格式教训见坑⑧），survey 46 行已填 `audio_files/upload_source`，随 30 路重启并入转录池；后续＝转录→复核→入库→**按引用索引逐期原地改写 PODCAST_REVIEW 块**（主代理串行）。索引在案 `senseaudio_out/tb2/_outline_yt_cites.json`。
- **坑 ⑧（下载格式，10-06 主理人订正）**：沿用精选批的 `-f b[height<=360]`（≤360p 视频流＋音轨）传输量是纯音频的 4–6 倍（FreeBSD Fridays 系列单件 200–400MB vs m4a ~15–60MB）；**web_safari（HLS-only）无纯音频格式**（`ba` 空匹配→静默回退 360p），须**默认 client**（无 `--extractor-args` 限定）才有 DASH 纯音频 itag 140（m4a 129k）／251（opus 115k）；定案 `-f "140/251/ba/b[height<=360][protocol~=m3u8]/b[height<=360]/b"`（`46_outline_cited_audio.py`）。杀进程改格式重启时，旧格式 .part 成为孤儿件须清理（ZGmuZz5ETHs 405MB 实例）。
- **坑 ⑨（键型双轨，10-06 实证）**：youtube 期 `transcripts.episode_id` **双轨**——不在 `episodes` 表（全表仅 1,191 行子集）的期 episode_id＝**vid**，表内期（含 46 引用期）＝**数值 id**；JSON doc 同理（常规期 `episode_id==episode_number==vid`，46 期为数值）。因此：**裁决文件一律 vid 键**（曾以数值键写出 reviews/303.json 等错名件，已删）；**置位/对账 SQL 须双路**（`episode_id=vid` 直配 ∨ 经 `episodes` 表 vid→id 映射），单一通路必漏一边（实证 18 期漏置位＋2 期错名）。
- **坑 ⑩（dash 键双向皆可错，10-06 实证两例）**：① 复核提示词写「key 精确**含**前导 `-`」被执行者误读成「给所有 vid 加 `-`」——晨间中断运行写出一批 `-<vid>.json` 错名件（vid 本无 `-`）；② 据此清理时判据写反（按「去掉 `-` 后不以 `-` 开头」判错名），把 **15 份真 dash vid 的合法裁决件一并误删**（YouTube vid 确有以 `-` 开头者，如 `-2SiZ1hQRM4`）。定案：**清理错名件前必先对 `json/` 真名清单核对该 vid 是否真带 `-`**；已对 15 份真 dash vid 重建最小 pass 裁决件（原判 pass 由「已入库且 reviewed」实证，issues 明细遗失注明可重审）；提示词措辞改为「key 为 `youtube:<vid>` 原样，vid 本身含前导 `-` 时不可丢、本无 `-` 时不得添加」。

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
