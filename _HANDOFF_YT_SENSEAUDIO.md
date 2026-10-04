# 交接书：BSD/Unix 会议视频字幕与音频转录战役（2026-10-02 ～ 10-04）

> 接手必读。本文件覆盖三条主线：**youtube.duckdb 音频转录战役**（BSD 会议/关键人物/USENIX 精选）、
> **精选 USENIX 大转录战役**（3,631 期，进行中）、**大纲引用改写与全库判断**（已闭环）。
> 库= `03-原始史料库/14-播客史料/youtube.duckdb`；相关工作目录 `D:/librebsd/_tmp/senseaudio_out/tb2/`。
> 配套记忆卡：`yt-fail-retranscribe-closeout-20261002`（MEMORY.md 已索引）。
>
> 🔴 **用户发「继续」＝假定所有程序/子代理任务已终止，先实况复核再恢复或按用户要求执行（§九.8，优先级最高）。**

---

## 一、当前库与磁盘状态（2026-10-04 16:30 复核；17:45 接手复核维持，转录线已重启）

| 项 | 值 |
|---|---|
| DB episodes | 1,191 期 |
| DB segments | 1,502,748 段 |
| transcripts 分布 | youtube_subs_20261001=1,123 / youtube_auto_subs=52 / senseaudio-asr-stream-1.5-260910=~45（总 1,220） |
| audio 库 | **curated 4,197/4,197 音频 100% 到手**（16:20 终态；全库 5,4xx mp3，约 175G），路径 `03-原始史料库/14-播客史料/audio/` |
| 磁盘 | D: 531G，可用约 180G（66%） |
| key 池 | `C:/Users/ykla/.sensenova/senseaudio_keys.json`：pool 22 把（含 GL* 导入 18 把），备份 `senseaudio_keys.json.bak-20261004-preGL` |
| 大纲 git | `db2743a5b`（46 期内容复核波）；其后大纲无新提交 |
| 下载线 | 🟢 D1 curated 4,197/4,197＋D2 重下 14/14 全部到手；cookies 管线定型（见 §十）；全库解码审计**已收口：4,197 件全验毕（4,196 ok＋1 瞬时误报复验有效）**；310 个冗余 mp4 已清（释放 23.08 GB）；D3 字幕见 §三.3 |
| 复核线 | 🟢 **54/54 全部复核完毕：53 pass / 1 fail**（fail＝BOPeeLhZOsY 空正文，待回炉）；裁决件在 `tb2/reviews/`，pass 中 QC 无 suspect |
| 转录线 | 🟢 17:50 重启：survey 三步链已重建，pending **4,201**；`15_parallel_transcribe.py 32` 在跑（150 路内存不可行，实测依据见 §三.1）；JSON 55 件（含 BOPee 回炉件） |
| 大规模清理事故 | 10-04 11:40 `_tmp` 被清（113G 释放）；audio 库与 DB **幸存**；tb2 的 json/reviews/裁决件丢失（可再生产物） |

---

## 二、已完成（零剩余）

1. **rev6 严格逐字复审**：809 期（yt_rev6_chunk_00-40）全量收口，fail 终态 34 期（裁决件原在
   `tb2/reviews/yts__<id>.json`，⚠️ 已随清理事故丢失，可从 DB quality_flags 与本文件 §五 恢复清单）。
2. **34 期 fail 落库**：`transcripts.quality_flags=['asr_quality_fail']`（库内 fail 标记总 54），
   DB 备份 `youtube.duckdb.bak-20261002-failflags`。
3. **重转链两波**：14 期＋27 期 fail 期音频下载→SenseAudio 多 key 重转→逐字复核→
   **18 期 pass 入库**（+4,066＋+8,504 段）＋reviewed 置位（备份 `bak-20261002-saingest`）。
   j83_Ufhijso/frwMWeyau_o/TJLOBLSRoHE 等 youtube_subs 侧 fail 期现已有 pass 级 SenseAudio 转录在库。
4. **163 期探索候选**（6 官方频道：BSDCan 17/BSDTV 42/EuroBSDCon 31/FreeBSD Foundation 15/
   FreeBSD project 12/OpenZFS 21/@BSDConferences 漏网 25）：16 期字幕全链入库＋16 路逐字复核全 pass。
5. **46 期大纲引用改写全链**：改写（~370 条核对）＋第三方内容复核（约 300 处行级订正）＋
   ieLN_5j7G1g 24 条错配重归属 EPi7pkyDUX5uM，提交 `db2743a5b`（159 文件 +3245/-3229）。
6. **USENIX 全库 7,273 期逐个判断**：40 片子代理按"本书目录主题"口径逐条判断，
   **纳入 3,660／排除 3,106**；判断产物原在 `_tmp/yt_judge/v01-40.txt`（⚠️ 已随清理丢失，
   纳入结果已固化在 `_tmp/yt_channels/curated_final.txt` 4,197 期清单）。
7. **GL* key 鉴权与导入**：`_test_gl_enabled.py` 实测 25 把中 **18 把通过 SenseAudio 鉴权**
   （GL1/GL2/GL4/GL7-GL17/GL19/GL21/GL22＋"我自己senseaudio"），池 4→22；
   无效 7 把＝大旺AI/1517/GL3/GL5/GL6/GL18/GL20。
8. **精选音频下载**：🟢 **4,197/4,197 = 100% 到手**（10-04 16:20 终态）——经 cookies＋solver 管线
   拿下全部残余（含末 4 期逐件解码验证）；D2 损坏/幻觉期重下 14/14；全库解码审计收口（见 §十一 QC）。
   任务书与教训详见 `script/senseaudio_20260929/yt_subs/_DOWNLOAD_TASKS.md`。
9. **youtube 候选字幕/音频战役**：71 期无字幕候选音频 68 到手；63 期转录 JSON 完成；
   2 期不适宜视频已删（`_tmp/yt_excluded_inappropriate.txt`：UITF03xeQhw、mMmbjJI5su0）。

---

## 三、暂停中的在途任务（接手即重启）

### 3.1 精选 USENIX 大转录战役（最高优先）
- **范围**：3,631 期（survey youtube db 中有 upload_source 且无 JSON 件者）。
- **10-04 13:15 复核实况**：大转录已于 11:41 重启，**54 期 JSON 完成**（ledger.jsonl 54 条全 ok、
  JSON 件 54/54 抽验全合法），随后 24 进程**随会话结束被连带回收**（§六 已知坑，本次实跑踩中）；
  现在无任何转录进程在跑（仅剩 2 个 mcp-server-fetch）。pt_10 尾部最后一次是 block2 退避重试中被打断，非脚本崩。
- ⚠️ **survey.json 已丢失**（11:40 清理与 11:41 重启赛跑所致；`15_parallel_transcribe.py` 启动即读它）——
  **重启前必须先跑 `01_survey.py` 重建**，否则启动即崩。已有 54 期 JSON 自动跳过，重跑零重复成本。
- **重启命令**（run_in_background 直启，勿用 `&`）：
  1. `python script/senseaudio_20260929/tb2/01_survey.py`（重建 survey.json）
  2. `python script/senseaudio_20260929/tb2/15_parallel_transcribe.py 150`
     （§九 修订：不低于 150 路；key 池 22 把现状，须实测 block0 no-close-frame／1011 退避频率，
     服务端并发限制过密则回退 24–64 路并加钥，实测数字记回本节）
- **量级**：每进程完成分片即出 JSON（`tb2/json/youtube__<vid>.json`）＋`tb2/ledger.jsonl` 追加顺序台账。
- **后链**（每批判 ~20 期滚动）：逐字复核（SenseAudio 口径，禁抽查）→ 03_ingest.py 入库 →
  reviewed 置位 → 删该批音频（链接留 DB，纪律见 §六）。
- **🔴 2026-10-04 17:50 接手重启实录（实测数字）**：survey 三步链重建
  （`01_survey.py`→`13_survey_candidates_audio.py`→`15_survey_curated.py`；youtube 行 5,432＝
  DB 1,191＋curated 4,197＋候选 44，BOPee 手工补行）→ **pending 实测 4,201**（「3,631」系 11:41 时点旧口径：
  D1 补漏到齐后此数增大；54 期已转期不计）→ 启动 `15_parallel_transcribe.py 32`（17:50）。
  🔴 **32 路实测遭服务侧 1011 风暴**：前 17 分钟仅成 2 期；日志实证大量
  `received 1011 realtime transcribe service unavailable`＋`no close frame`（4 连退避 30/60/120/240s 耗尽即弃期，
  弃期不计 JSON、自动回 pending；key 轮替无竞态，`_key_rotate`=33 正常分发）。全窗口 30 分钟约成 30 期（后段回暖），
  判定＝32 路超服务端当前容忍度（10-04 傍晚时段）。
  → **18:20 全量 taskkill（32/32 确认终止）→ 18:22 起改 16 路**：`15_parallel_transcribe.py` 本版加 2.5s
  错峰启动（防 `_key_rotate` 读改写竞态与建连风暴）。**16 路实测（18:22–18:40）**：稳定产出约 22 期/18 分钟
  （≈1.2 期/分）；仍可见偶发 1011/退避（尾部窗口 16 片合计：退避 45 次／1011 40 条／弃期 4 次＝远低于
  32 路密度，弃期自动重排）；内存 free 由 2.7GB 回到 4.9GB。**两窗口完成速率接近（≈1.0 vs ≈1.2 期/分），
  16 路稳定性与内存余量更优；上探 20–24 路须留待非高峰时段另测**。
  ⚠️ **150 路「双约束」**：① 内存——02_transcribe 每期全量载入 PCM（实测 p50≈36MB／p90≈78MB／max≈163MB），
  150 路理论峰值 >16GB（本机 16GB）；② 服务端——32 路即触 1011。放宽前置＝流式读 PCM（或加内存）＋与服务方
  确认并发上限——待裁。快照（18:40 前后）：json 107／ledger 108（重启后 +53；BOPee 回炉另计）。

### 3.2 残 19 期精选音频 —— 🟢 已闭环（10-04 16:20）

- 全部到手：curated **4,197/4,197**（含末 4 期逐件解码验证：5zmsPhLNhAM/I9WrwbNS6pM/idkopV6LR5U/9hOY08UOD20）。
- 打通路径＝**cookies 管线**（Chrome 导出 cookies→Netscape＋node solver＋HLS 原声轨），
  细节与全部教训见 §十 与 `_DOWNLOAD_TASKS.md`；清单 `download_pending_audio.txt` 已清零。
- 全库解码审计（§十一 QC）收口后如有坏件，用 `16_redownload_list.py N <坏件清单>` 重下。

### 3.3 字幕滚动（低优先，可选）——🟢 17:4x 管线修复，17:48–17:55 批跑 ok=1/fail=68
- 修复（采用修法①）：`09_subs_retry_lowconc.py` 补 `--js-runtimes node --remote-components ejs:github
  --cookies _tmp/yt_cookies.txt`（修 bgutil 2.0.1 脚本模式 15s 探测超时）＋WORKERS 240→8。
- 单发探针 2/2 管线全通（PO token 生成＋node 解 JS 挑战＋m3u8 取到），均报「无字幕轨道」。
- **批跑终态 17:55:10：ok=1（`Y5cx9hEhxfE` 实取到 127,759B `.en.vtt`——旧管线假性失败件）、
  fail=68（rc=0「无字幕轨道」确定性回复）**。路由：新字幕件走 `03_ingest_subs.py` 入库链；
  68 期无字幕者既定＝音频链替代（44 期已在候选补丁链，详见 `_DOWNLOAD_TASKS.md` D3）。
- 实证（仍有效）：timedtext 限流与并发无关（1/3/8/16/40/240 路得数相同 2-6 份/轮）。

---

## 四、挂账（无法自动修复，需裁定或人工）

| 项 | 明细 |
|---|---|
| 转录幻觉挂死 5 期 | -AKdvHriBuE / 5235CsD1QwQ / 8XCNtBzmEZ0 / 9hOY08UOD20 / AblGHmmGmho——旧判「勿再重转勿入库」，按 §九.9 已改为**重下音频后重转一轮**；🟢 音频已全部重下到位（D2），待转录线接续 |
| 转录幻觉/过短 4 期 | jfe43i0rz5g / ZhPvCc3wpvE / qewI1oWlxBY / UtlGt3ag0o0 / RSqs6NAsmiY / xkV1Jey0f_o——同上，音频已重下到位（D2 14/14），重转后按 §十一 QC 判 |
| 音频损坏 3 期 | 5Cni50vnlto / c1LKeyP1mos / 1de-pxqHKkU——🟢 已重下（D2 14/14 含此 3 期），待重转 |
| 不适宜已删 2 期 | UITF03xeQhw / mMmbjJI5su0（年龄限制，清单已移除） |
| 无英文候选 2 期 | A2B6N5HGfy4 / 1W7ir3TKK6k（字幕轨不存在） |
| 残 id 教训 | `9hOY08UOD20` 曾因抄写为 `9hY08UOD20`（O→Y）假性失败多轮——**清单 vid 必须原样复制，禁凭记忆转写** |
| 复核 fail（已回炉，待裁） | `BOPeeLhZOsY`＝**EuroBSDCon Dublin Promo（15 秒无语音宣传片）**：17:40 重下新编码音频＋17:46 重转，仍空正文（唯一 utterance 无文字、usage 1.1s；字幕轨亦近空 219B）——**非管线故障**，建议标 non-speech／弃，待主理人裁 |
| D3 字幕阻塞 | bgutil 2.0.1 脚本模式 15s 版本探测超时（09_subs 未带 new flags 仍自动加载插件）——修法见 §三.3／`_DOWNLOAD_TASKS.md` D3 |
| DB 待修 | 无（ep292/293"跨期错配"为复核代理误读，**勿修**） |
| 入大纲增补链路 | 新入库 youtube 期未被大纲引用；属独立 campaign（锚点缺口审计），有并行会话在相邻队列，**勿抢** |

---

## 五、关键恢复清单（清理事故后需重建的产物）

| 产物 | 重建方式 |
|---|---|
| 34 期 fail 裁决件 | DB `quality_flags` 仍完整（asr_quality_fail 54）；如需逐字证据可按 §四 清单重审 |
| survey.json | 🟢 已重建（10-04 17:45；三步链 `01_survey.py`→`13_survey_candidates_audio.py`→`15_survey_curated.py`；重建后计数与口径订正见 §十三） |
| 31 期精选转录 JSON | 已过时——10-04 11:41 重启后已新出 54 期（audio 幸存，零下载成本） |
| USENIX 判断产物 v01-40 | 纳入结果已固化于 `curated_final.txt`（4,197 期）；如需理由词需重判 |
| pt_N.log / 各战役日志 | 重跑自动重建 |
| 字幕滚动清单 | `_tmp/yt_new_list.txt`（161 候选）＋ `_tmp/yt_subset/w1-w4.txt`（71 期互斥子集）幸存 |

---

## 六、纪律与坑（每条都实测付出过代价）

**DB 层**
- `transcripts.episode_id` 是内部数字 id；**视频 id 必须经 `episodes.link`（`?v=<vid>`）JOIN**。
- `quality_flags` 是 VARCHAR[]：DuckDB 里 `["x"]` 双引号＝标识符报错，**必须单引号字面量**。
- survey（`_tmp/senseaudio_out/tb2/survey.json`）youtube db 的 `episode_number`＝**视频 id**；
  `02_transcribe.py --num` 按它选期——**传内部 id 会静默空转**。
- ingest 对 survey `episode_id=vid` 回退的期**不注册 episode 行**（transcript 挂 vid 字符串 id）——
  需手工补注册（ep1458-1460 案例）。
- 删除期前先查 DB 行；"ep292/293 跨期错配"是复核代理混淆 transcript_id/episode_id 的误读，**勿修**。

**转录层**
- `02_transcribe.py --num` 对**带前导横杠的 vid** 须传完整 key 形式（`youtube:-AK...`），
  裸 `--num -AK...` 被 argparse 吃掉静默空转。
- `15_parallel_transcribe.py N`＝N 进程并行（各分片互斥、独立日志 pt_N）；key 池 22 把支撑 24 路实测正常。
- block0 "no close frame"＝多 key 同时建连触发服务端并发限制，脚本自带 4 次退避重试，成功即续——**勿盲目重启**。
- 转录 stdout 路径按 chatcmpl-tool id 变化（`.zcode/cli/exec/sess_*/<id>-stdout.log`）；
  监控器 `script/tools/yt_chain_monitor.py` 的 `TRANS_STDOUT` 硬编码，**换跑须改**。

**下载层**
- timedtext（字幕）限流与并发无关（1/3/8/16/40/240 路实证得数相同 2-6 份/轮）；
  音频端点行为独立（曾全放行也全拦）——**两 IP 实证：限流跟随账号/设备指纹，非 IP**。
- bgutil-ytdlp-pot-provider 插件会以脚本模式 15s 超时**拖死每次 yt-dlp 调用**——已卸载，勿重装。
- yt-dlp 在 PATH 外，一律 `python -m yt_dlp`；--extractor-args `"youtube:player_client=android,web_safari"`。
- 残 23 期 bot 窗口：代理切换曾解除（575→33），再复发则滚动重试等窗口。

**磁盘与进程**
- **PCM 缓存是最大空间杀手**（单轮 16-67G）：转录/复核批次收口必清 `tb2/pcm`、`tb1/pcm`；
  **清理白名单＝PCM/work/日志可清，json/reviews/裁决件保留**（10-04 清理事故曾连裁决件清掉）。
- 磁盘满（Errno 28）会产生**截断 mp3**（"Header missing"，ffmpeg rc=-22）——按大小+解码探针筛删重下。
- 后台任务：**`&` 方式启动会被 Bash 任务结束连带回收**，必须 run_in_background 直启；
  TaskStop 不杀 python 子进程，须按命令行 taskkill；被取消的前台 Bash 会杀整个进程树。

**复核层**
- SenseAudio 口径：pass=逐句可读/无提示词泄漏（subscribe/transcribe/模型自述）/无成段乱码/无臆造/专名可还原；
  fail 阈值=提示词泄漏话术、成段词拼贴、核心专名全毁、正文过短（<200 字符）。
- 裁决写 `tb2/reviews/youtube__<vid>.json`：`{"key":"youtube:<id>","verdict","issues","garbled_passages","reviewed_at"}`，
  用 python json.dump 保证合法（**单引号勿写成 \'**）。
- 复核临时目录用完即清（`_tmp/work/sa_*` 等）。

---

## 七、下一步（接手即做，按序；顺序已按 §九.9 修订）

1. **下载线收口**（🟢 D1/D2 已 100% 到手）：等全库解码审计（`18_audit_mp3.py`）收口 →
   坏件按 `mp3_audit_bad.txt` 重下（`python 16_redownload_list.py 8 <坏件清单>`）→
   **清冗余 mp4**（310 个双存中间件，审计确认对应 mp3 有效后删除）。详见 §十。
2. **重启大转录**：先 `01_survey.py` 重建 survey.json → `15_parallel_transcribe.py 150`
   （§九.2；python 直跑勿走子代理，run_in_background 直启）。
3. **首批判复核（QC 全过才入库）**：json 齐 ~20 期 → 子代理逐字复核（§六 口径）
   → **§十一 六项 QC** → `03_ingest.py` 入库 → reviewed 置位 → 删该批音频（纪律 §六）。
4. **转录全量收口后**：库终态统计 → 交接书/记忆卡更新 →（可选）入大纲增补链路另立项。
5. **key 池维护**：新 SenseAudio key 提供后即刻导入池并扩并行（`_test_gl_enabled.py` 探针先行）。

## 八、相关文件索引

- 脚本：`script/senseaudio_20260929/tb2/`（02_transcribe/03_ingest/04_download_fail_audio/
  15_parallel_transcribe）；`script/senseaudio_20260929/yt_subs/`（01-14 各波＋**16_redownload_list /
  17_diag_fail / 18_audit_mp3**＋`_DOWNLOAD_TASKS.md`）。
- 数据：`_tmp/senseaudio_out/tb2/`（survey.json＋json/＋reviews/＋pt_N.log＋
  **mp3_audit.jsonl／mp3_audit_bad.txt**）；`_tmp/yt_channels/curated_final.txt`（4,197 纳入清单）；
  `_tmp/yt_new_list.txt`（161 探索候选）；下载线清单已清零（`download_pending_audio.txt` 0 行）；
  **cookies：`_tmp/yt_cookies.txt`**（Chrome 导出 JSON 转制；含账号会话，**勿入 git、勿外传**，失效重导）。
- DB 备份：**仅 `-preroll` 幸存**（10-04 13:15 实测；-failflags / -saingest / -pre292 / -pre3ep 已不在盘上，
  去向待核实——清理误删或轮换删除）；重要写库节点前先补一个当前态备份；
  key 备份：`senseaudio_keys.json.bak-20261004-preGL`。
- 交接前暂停动作：全部转录/下载 worker 已 taskkill（会话内 MCP 进程未动）。
  ⚠️ 10-04 13:15 复核此条与实况不符：11:41 重启的 worker 一直跑到 13:08 后随会话回收，
  交接书写于 13:06 期间 worker 仍在跑——「已 taskkill」当时未生效，接手仍须按 §三.1 重启。

## 九、任务书修订（2026-10-04 主理人指令，随即生效）

1. **加强入库、入大纲的复核流程**：入库前逐字复核（禁抽查）之外，入库后追加**行数对账**
   （segments 增量 vs ledger utterances）＋入大纲后 grep 锚点对账；对账不过不删该批音频。
2. **转录并行 ≥150 路＋key 轮替最大化**：轮替 key 数与并发数都不低于 150
   （key 池 22 把现状支撑有限——扩钥后逐级提路，每级实测 no-close-frame／1011 退避率，
   退避率过密则回落并记录）；顺序监控复核＝ledger.jsonl 台账对账（条数==JSON 数、无重复 vid）
   ＋pt_N.log 尾部巡检。
3. **临时文件及时＋周期性清理**：批收口即清 `tb2/pcm`、`tb1/pcm`（当前 tb2/pcm 6.0G）＋`_tmp/work/*`；
   每日一轮周期巡检；**转录完成的 mp3 属非源文件，入库后一律删除**（链接留 DB，§六 白名单扩展）。
4. **下载并发 64 路**：yt-dlp 侧下载（14_audio_curated.py 等）统一并发 64 路（10-04 裁定，取代 40 路）；
   **本会话范围收窄为只负责下载＋复核两线**（转录/入库/入大纲不归本线）。
5. **下载流与入库/入大纲流并行分记**：两条流水线各自独立 ledger／日志目录，互不混写、互不阻塞，
   收口时按 §五 对账合并。
6. （第六点未随指令传到，待主理人补发；先按前五点执行。）
7. **分工定则（10-04 补充指令）**：**转录一律用 python 程序直跑（15_parallel_transcribe.py 等），不走子代理**；
   **子代理用于下载、入库、复核、入大纲**四环节（可并行多路派发）。转录层的监控与终止仍按 §六 进程纪律
   （python 直跑、taskkill 按命令行、勿用子代理转录）。
8. **「继续」触发定则（10-04 补充指令，优先级最高）**：**每次用户发「继续」时，必须假定所有程序与
   子代理任务均已终止**——不复述旧状态、不盲信交接书数字，先做实况复核（进程清单、ledger/JSON 件数、
   磁盘与 DB 对账），再据复核结果**恢复在途任务**或**按用户本次要求执行**；两者冲突时以用户要求优先。
9. **10-04 补充指令三则**：
   - **顺序修订**：接手先跑 **3.2 残 19 期精选音频**（bot 窗口滚动）＋**3.3 字幕滚动**（低优先），
     然后重启 3.1 大转录（§七 顺序已同步更新）。
   - **加强幻觉监控**：复核发现幻觉（提示词泄漏/成段乱码/臆造）→ **直接删除该期转录 JSON 与库内残留 → 重转录**；
     **音频损坏 → 先重新下载、再转录**（勿拿损坏源反复转）。⚠️ 本条取代 §四 挂账「幻觉挂死 5 期勿再重转」旧处置：
     那 5 期按新规改为一轮重转录尝试（音频重新下载后转），若仍幻觉则回挂账。
   - **加强去重**：转录/入库前按 vid 去重（DB 已有 pass 级 transcripts 的期跳过、同 vid 多 JSON 件取最新）；
     curated 清单与库已有重复期排除（已知 6 期）；音频文件按 `youtube_<vid>.mp3` 键与 DB 对账，防重复下载与孤儿文件。

## 十、下载任务单独拆分（2026-10-04）——🟢 已收口

下载线独立任务书：**`script/senseaudio_20260929/yt_subs/_DOWNLOAD_TASKS.md`**（终态与全部教训在内）。
三批＝**D1** curated 补漏（🟢 4,197/4,197 到手）→ **D2** 损坏/幻觉期音频重下 14 期
（🟢 14/14 到手，含修正残 id 的 9hOY08UOD20）→ **D3** 探索候选字幕滚动 69 期（低优先，未启动）。
关键机制＝**cookies 管线**：`--cookies _tmp/yt_cookies.txt`（Chrome 导出 JSON→Netscape）＋
`--js-runtimes node`＋`--remote-components ejs:github`＋bgutil-ytdlp-pot-provider 2.0.1＋
`-f "b[height<=360][protocol~=m3u8]/b[height<=360]/b"`（HLS 优先、自动选原声轨）＋
**每件 ffmpeg 解码探针**（本网络通道损坏率高，探针不过即删件重下）。
并发 64 路；子代理承接；独立 ledger；与转录/入库/入大纲流水线并行分记。

## 十一、质量控制（QC）环节（2026-10-04 主理人指令，独立成环节）

> 原则：**每一项 QC 不过＝该件按"重下载→重转"回炉，绝不带病入库/入大纲。**
> 产物落 `_tmp/senseaudio_out/tb2/qc/`（每件一行 JSON：vid、六项结果、时间、处置）。

**A. 音频层（下载线执行）**
1. **解码完整**：`ffmpeg -v error -i <mp3> -f null -` rc==0（已内联进 14/16 脚本；全库审计 `18_audit_mp3.py`）。
2. **时长核对**：mp3 实测时长 vs DB `duration_seconds_db`，偏差 >5% 报警（防截断/防下错集）。
3. 不过 → 删件 → `16_redownload_list.py` 重下 → 复验（连续 3 轮不过回挂账并记录于 §四）。

**B. 转录层（复核线执行，逐字复核之外的三道专项）**
4. **防幻觉**：提示词泄漏话术／subscribe、transcribe 类残留／模型自述（"我作为AI"）／成段词拼贴／
   臆造正文——**发现即删该期 JSON 与库内残留 → 重下音频（若音频层不过）→ 重转**（§九.9）。
5. **防顺序错误**：段落时间戳**单调递增**（零回归）；`usage_seconds ≈ audio_seconds`（比例 0.9–1.1）；
   ledger 条数==JSON 件数且**无重复 vid**；同批分片互斥（15_parallel 分片不交叠）。
6. **防截断**：末段结束时间距音频总长缺口 >60s 报警；`full_text` 长度/音频时长比异常（过短 <200 字或
   单位分钟字数异常低）报警；对照 `audio_seconds` 全量核账（§二.3 入库对账同口径）。

**C. 执行时点**：下载收口（A①②）→ 批判复核（B4-6）→ 入库前 QC 全绿才跑 `03_ingest.py` →
入库后行数对账（§九.1）→ 入大纲后锚点 grep 对账。

## 十二、交接包（2026-10-04 17:10 收尾快照）

- **状态一句话**：下载线 🟢 全收口（curated 4,197/4,197 全验＋D2 14/14；审计 4,197 件全绿、
  310 冗余 mp4 已清释放 23.08 GB）；复核线 🟢 **54/54 落定（53 pass／1 fail）**；
  D3 字幕本轮 0/69（bgutil 15s 探测超时，修法见 §三.3）；转录线停在 54/3,631（survey.json 待重建、无进程）。
- **fail 处置**：`BOPeeLhZOsY` 空正文（14.8s 音频无产出）→ 按 §十一 回炉：重下音频→重转；
  其余 53 件 pass（QC 无 suspect），待转录线接续入库。
- **接手第一步**：按 §九.8「继续」定则实况复核（进程清单、`tb2/reviews/` 件数、盘点）→
  按 §七 顺序执行（复核收尾 → 审计/清理已毕 → 重建 survey → 150 路转录）。
- **在途清单**：`tb2/reviews/`（**54 件全落**：53 pass／1 fail）、`tb2/json/` 54 件、`tb2/ledger.jsonl` 54 条、
  `tb2/mp3_audit.jsonl`（4,197 行终态）、`_DOWNLOAD_TASKS.md`（D1/D2 🟢、D3 ⚠️）。
- **密钥/凭证**：key 池 22 把（备份 `bak-20261004-preGL`）；`_tmp/yt_cookies.txt` 含账号会话勿外传。
- **本会话权限**：只负责**下载＋复核**两线；转录/入库/入大纲不归本会话（§九.4）。

> ⏩ 本包为 17:10 快照；**17:20–18:00 接手复核与重启实录见 §十三**（此后状态以 §十三 为准）。

## 十三、接手复核与重启实录（2026-10-04 17:20–18:00）

**复核对账（全绿）**：复核件 **54/54**（53 pass／1 fail，最新 17:12；磁盘实况与 §十二 一致——「48/54、余 6 在途」
为陈旧数字，记忆卡已订正）；`json/` 54＝`ledger.jsonl` 54；`mp3_audit.jsonl` 4,197 行且与 `curated_final.txt`
**4,197 逐件覆盖一致**（无缺口、无多出）；curated 在盘 mp3 **4,197/4,197（缺 0）**；mp4＝0（310 已清）；
DB 三数（episodes 1,191／segments 1,502,748／quality_fail 54）逐项复合；接手时无转录/下载 worker 在跑。
**订正与清零**：① `download_pending_audio.txt` 残留 4 行（末 4 期）→ 逐件 ffmpeg 复验 4/4 rc=0 后归零；
② `mp3_audit_bad.txt` 残留 `5zmsPhLNhAM` → 复验 rc=0（审计在其下载完成前采样的 "missing" 陈旧行），归零；
③ §五 survey 行订正为已重建（三步链）。
**清理**：tb2/pcm 6.0G 清 0（§九.3 批收口纪律）；全量 PCM 峰值算术≈4.2k 期×p50 36MB≈150GB+（p90 口径 300GB+）
＞磁盘余量，已立回收器 **`script/senseaudio_20260929/tb2/_pcm_gc.py`**（默认干跑；`--apply` 删已完成期 PCM、
不清未转期）——长跑前/批收口随手跑。
**BOPee 回炉（已尽，待裁）**：17:40 重下（433,001B）→ 17:46 `02_transcribe.py --force` 重转 → 仍空正文；
确证＝EuroBSDCon 15 秒无语音宣传片（字幕轨 219B 近空为佐证），**非故障**。建议标 non-speech／弃，待主理人裁。
**D3 字幕（已闭环执行）**：09_subs 补 flags＋WORKERS 8 → 探针 2/2 全通 → 17:48–17:55 批跑 **ok=1/fail=68**；
唯一实取 `Y5cx9hEhxfE.en.vtt`（127,759B）——旧管线假性失败件，**须接 `03_ingest_subs.py` 入库**；
68 无字幕者走音频链替代。
**转录重启（在跑，含一次回退）**：survey 三步链重建（pending 4,201）→ 17:50 起 32 路 → **服务侧 1011 风暴
（前 17 分钟仅成 2 期）→ 18:20 全量 taskkill → 18:22 起 16 路（加 2.5s 错峰）**；重启后稳定产出（18:40 前后
json 107／ledger 108，重启后 +53；偶发 1011/退避自愈，弃期自动重排）。全量实测数字与「150 路双约束」见 §三.1。
**下一手**：① 转录滚动批 ~20 期 → 逐字复核＋§十一 QC → `03_ingest.py` 入库（候选/curated 行 `episode_id=vid`
的补注册纪律见 §六）；② `_pcm_gc.py --apply` 周期回收；③ BOPee 裁处；④ 并发上探（20–24 路，非高峰）与
150 路前置（流式 PCM／加内存＋服务方并发上限确认）待裁；
⑤ `Y5cx9hEhxfE` 字幕接 `03_ingest_subs.py` 入库。
