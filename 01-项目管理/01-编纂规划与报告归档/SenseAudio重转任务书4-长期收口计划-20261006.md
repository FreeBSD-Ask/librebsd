# SenseAudio 重转任务书 4：长期收口计划（2026-10-06）

> 主理人令（1:1 比照任务书九节结构建立长期计划）：按本任务书循环本体机械执行，直至 4,255 期全链收口（转录＋复核＋入库＋入大纲既有改写＋新增条目＋引用期重锚全零）。本任务书**取代任务书3 §五 的长期续接位**（任务书3 尽存循环史与坑集）；与任务书 1（BSD Now）各自独立。

## 一、范围（剩余工作盘点，2026-10-06 18:3x 读 DB 实测）

- **库**：只写 `03-原始史料库/14-播客史料/youtube.duckdb`（本战役 senseaudio 模型行）。
- **当前进度**：转录 **1,495/4,255（35.1%）**；入库 DB **1,488 行全 `'reviewed'`**（积压随到随清）；46 引用期 **5/46 全链**（giceCouM3F8/vVpd34bWCJA/N-7xZB0afyA/rXmWXIDsxig/vC7GITOi1P0，含大纲原地改写）；新增条目 **110/1,380**（试点 10＋批 2–6 各 20，落 292.4 PODCAST_REVIEW 块）；费用 ~1,400 元。
- **剩余**：转录 **~2,760 期**（ETA 1.5–2 天@30 路 1.0–1.35 期/分；中途 worker 耗尽按 §五 重启接续）；复核随转录节奏；新增条目 **~1,270 期**（每批 ≤20 随批，约 64 批）；46 引用期 **41 期**随转录落地（每期 1–44 处引用重锚）；音频/pcm 清理随批。
- 挂账：**11 项 fail 期**（BOPeeLhZOsY、Rsk2YZPOpG0、Y0MYPEKKF0g 等空输出/话术注入）在 failbak，随批重启自动重转重审。
- **循环记录（2026-10-06 18:4x，任务书4 首轮）**：w75 15/15 pass（Dual EC DRBG/ZLFS/SMM 综述/PQXDH/OblivP2P/SEAL 等）；入库 +15（置位后 **DB 1,503/1,503 全 reviewed**）；删音频 15 期；pcm 回收 ~2.2GB；审计仅 4 项文档化 artifact；json 1,504（35.3%）。
- **持续串接轮 w76–99（2026-10-06 23:2x，主理人批评中断后修正——同一回合内连续串接循环）**：w76–w99 共 24 波全清（每波随到随清全 pass，含 46 引用期 ieLN_5j7G1g 的 3 块新增条目落盘 `2acb66591`）；DB **1,589/1,589 全 reviewed**、积压 0；30 路滚动（json 1,590=37.3%）；删音频 22 期 ~0.4GB；pcm 回收 ~19GB；新增条目累计 110/1,380（批 7 起随批续排）；cited **6/46**（前 6 期全链含大纲落地）。
- **46 引用期第 7 期＋w100/101/102（2026-10-07 0:0x，`44200e365`）**：**tuI2wX3ol2o**（DevNotes《The Making of BSD》纪录片，40 处引用）pass→入库→**4 文件 28 条镜像条目重锚**（BSD 起点 84.0-174.0/1BSD-3BSD 174.0-264.0/Tahoe 264.0-324.0/net1-net2 354.0-438.9/诉讼-和解 435.9-617.3/史料节点 354.0-561.1/总纲5 627.2-641.2；新转写前段含 Watergate 引子约 30s 时间轴后移，[订正] 留痕）；w100 1/1、w101 5/5、w102 3/3 pass。cited **7/46**；DB **1,597/1,597 reviewed**；json 1,598（37.5%）；新增条目累计 110/1,380（批 7 起随批续排）。
- **持续串接轮 w103–120（2026-10-07 4:1x，夜班连续滚动）**：w103–w120 共 31 波全清（每波随到随清全 pass，含 1 项新增 fail＝jfe43i0rz5g FreeBSD 安全官演讲 ASR 话术泄漏 1.6s/41 字符→failbak 挂账累计 12）；DB **1,719/1,719 全 reviewed**、积压 1；30 路滚动（json 1,721=40.4%）；删音频 ~60 期 ~1.5GB；pcm 回收累计 ~35GB；cited **7/46**；新增条目 110/1,380（批 7 起随批续排）。M1 里程碑（转录 50%＝2,128 期）预计今日内到达。
- **w121 大波（json 1,954→1,980，隔夜 +233 期）＋46 引用期第 8/9 期（2026-10-07 上午，`0a772872b`）**：w121 g1-g45 共 45 组全清（265 期 pass＋2 新增 fail＝YsF9_D2QH4U 工具话术泄漏→挂账累计 13；中途 2 次配额瞬态作废重派成功）；**SGC0191nDp0**（McKusick BSD Daemon 图像史，33 处引用）与 **uj1Ricrq0bs**（Warner Losh Git 迁移讲解，33 处引用）pass→入库→6 文件 45 条重锚（`0a772872b`）；cited **9/46**；DB **1,979/1,979 reviewed**；删音频 ~130 期 ~3.5GB；pcm 回收 ~40GB；转录 1,980/4,255（46.5%）——**M1 里程碑（50%＝2,128 期）在望**；新增条目 110/1,380。
- **w122 收尾＋第 10 期链闭环（2026-10-07 下午，续接自上下文压缩）**：**DXX4HDd3vDQ**（Allan Jude/Klara "用 FreeBSD 构建设备"，EuroBSDCon 2024，30 处引用）链全闭环——复核 pass（Poudriere appliance 镜像/邮件服务器客户转型/EFI 固件供应链安全启动/MAC 模块族 mac_ntpd·portacl·bsdextended·do/升级"绝不留在坏状态"/fork 上游化之道）→入库 +18 → **重锚已由先前收口提交 `fd98be627` 完成（约 300 处行级订正）**，8 段时间戳对新转写逐段核验全符；**cited 10/46**；DB **2,020/2,020 reviewed**；转录 json **2,048/4,255（48.1%）**；积压复核波 27 期已派 5 组子代理（w123）。

## 二、模型与 API（同任务书3）

- WS 流式端点 `wss://api.senseaudio.cn/ws/v1/realtime/transcriptions`，模型 `senseaudio-asr-stream-1.5-260910`，16k mono s16le、server_vad、smart_edit off（verbatim）、15 分钟分块（BLOCK_SECONDS=900）、~8x 实时；**术语热词已撤销**；PCM 流式读取（`02_transcribe.py` seek/read 增量，RSS 44–55MB/worker）。
- **服务端全局并发上限 ≈30–40**（32/48/80/120 路实测 1011 风暴），**30 路＝上限内最优**；零星 1011 走 worker 内部 retry 自愈，风暴则降并发。
- **120 路实测定案（2026-10-07 18:0x-18:13，主理人令测试）**：120 路重启后 ~113 路起**大量 1011 "realtime transcribe service unavailable"**（新 worker 日志 18 分钟内 1,652 条、重试风暴拖慢实际吞吐），本机 **RAM load 93%、可用 1.0 GB**（15.8 GB 机；30 路时 74%/4.0 GB）；**吞吐实测 120 路＝4 期/8min（30 期/h），低于 30 路基线 ~49 期/h**。结论＝**120 路双重约束不可行（服务器 1011 拒绝＋本机内存近枯），30 路仍为最优**；已按机制回落 30 路（杀旧＋重启，RAM 回升 4.0 GB/74%）。附带：120 路期间 giceCouM3F8 ffmpeg 解码探针失败（rc=4294967294）——该期已完整 reviewed（episodes 表数字 id 319），无数据损失。

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
- **M1：转录 50%（~2,128 期）——✅ 已达成（2026-10-07 15:0x）**：终局审计＝json **2,128/4,255（50.0%）**；DB **2,116/2,116 全 reviewed**（pending ~9-11 为新转录在复核管线）；复核管线完全追平；cited **11/46**（DXX4HDd3vDQ/SGC0191nDp0/uj1Ricrq0bs/i7pkyDUX5uM 等 11 期全链收口）；新增条目 **170/1,380**（批 1-9）；fail 挂账 14；pcm 回收累计 ~50GB。**审计备注**：vid 基底对账有假象——cited-46 数字轨道行（episodes 表行如 292）DB episode_id 非视频 vid，vid 基底差集含 ~56 项假缺，须经 episodes.link 反查后对账。下一手＝M2（转录 100%）。
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
- **工作区归档豁免（2026-10-07 主理人批准）**：`_tmp/senseaudio_out/tb2/` 虽属 gitignored 工作区，但 json/ 逐期原件（字级时间戳唯一留档）、ledger.jsonl 台账、reviews/ 裁决件、manifests 为战役真值与史料凭证——**清理作业一律豁免该目录**；战役收口后将其归档至正式史料目录（或明确豁免规则入 .gitignore 策略），避免历轮清理误伤。