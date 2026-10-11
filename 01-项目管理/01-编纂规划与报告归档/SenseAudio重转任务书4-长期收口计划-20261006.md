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
- **w123–w162 汇总回写（2026-10-08～10-09，详录在任务书3 §五，此处为口径回写）**：①转录——M1（50%＝2,128 期）与 55 路定案（10-07 主理人批准，任务书3 §四.4 已改写）；120/90/70 路双重约束实测不可行；**json 至 3,373（78.8%+，w159 @3,352）后 10-08 16:10 起服务端故障零增长**（w160：55/30 路两轮全败＝no close frame、0.6x 降速，服务侧容量故障非风暴，挂账观察）；②新增条目——批 23–82 收口，**累计 1,558/池（覆盖率 ~58%）**（w162 `5d4639017`），坑⑮冻结瞬态（0/20 落盘→降并发 10 组重派）、坑⑯EP+vid 空格、坑⑰批清单须程序化复制；③DB——w155 时点 **2,664 全 reviewed** 后入库暂停（转录停滞）；④cited 11/46（M1 审计口径）；⑤fail 挂账累计 22（w155）。
- **w163 复核大清账＋引用重锚 10 期（2026-10-09 23:5x～10-10 05:3x，`bb612f5ef`）**：①**复核波 85 组 674 期全判读**（禁抽查、逐篇全文通读；40 路分 3 波；pass 667／fail 16 移 failbak——本轮新 fail 6＝LyV6bKF0odQ 韩文乱码、PoHZ84DVvbk/RFJzD5ggBcg/tR_mWRdZhA4 话术注入、ZGmuZz5ETHs/esHi3z0HdRE 后半段崩坏，加历史 fail 10 期一并挂账，failbak 累计 26）；②**入库 +733**（transcripts +733/segments +111k，`03_ingest.py` 复核门禁；**坑①dash 键双向再实证＝43 期老 verdict 键带前导 `-` 与 json doc 键不匹配致静默 skip，修复 verdict 键后补入库**）；③**置位 reviewed 双路＋对账：DB 3,389 reviewed/3,397 总**（pending 8 为 cited-46 数字轨道行＝已知 artifact；json−DB 差集 27 中 25 期为数字轨道假缺经 episodes 反查闭环）；④**引用重锚 10 期**（Y0ixYwLd9Pg/nwbqBdghh6E/rGdylV-Up_E/j_TVpq8S2Io/2ON_yeNfO7Y/S0ePkpVMHu8/RDjj5g9rzx8/UfiTV9QWhM4/TzZLj9cfuug/EfNZ4jMQic4，共 309 条引用——时间戳 244 处全平衡、实质内容订正 12 处含 4.4BSD-Lite"法律上归于清白→legally unclear"方向反转、DEC VAX→PDP-11、DFS→VFS、audit 2000→2004、数条新转写推翻旧存疑注；0 条"找不到对应"；8 执行手其中共用文件三期 nwbq/S0ePkp/RDjj 单人串行防冲突）；⑤单遍索引重建＝**1,634 vid/6,234 处**（含新增条目 1,558 条目的新引用）；⑤05_audit 门禁 6 项白名单 artifact 合格、severe_repetition 3 期均为 10-07/08 旧 pass 边界件不翻案；⑥cited **21/46**（10 期本轮重锚后全链，余 25 期待转录落地）。

- **w164 GLM 官方直转插曲回归＋观察器再部署（2026-10-10 深夜～10-11 00:5x）**：①主理人 10-10 令试改官方 GLM-5.3-Flash 直转、弃旧模型旧 key——实测三路全阻后 10-11 令放弃回归本管线（**代码零改动、无需回滚**）：GLM-5.3-Flash 官方模态仅 Video/Image/Text/File **无音频输入**（docs.z.ai 实查）；ZCode harness 子代理 Read mp3 拒收（binary）、mp4 只采样视频帧**不传音轨**；本地唯一官方 key（zai-coding-plan c8b59c…）对 api.z.ai 鉴权通过但 **429 余额不足**（chat/ASR 皆然）；会话 JWT（zcode-plan 网关）已过期且该网关无转写路由。备查：官方 GLM-ASR-2512 端点 `api.z.ai/api/paas/v4/audio/transcriptions`（≤30s/25MB、无时间戳、$0.0024/min）若将来启用约 860 元可转完全部剩余。②实况复核＋WS 握手探针（`_probe_ws_20261011.py`，只握手零计费）：worker 0、观察器不在位、无 _KEY_EXHAUSTED；**旧模型 session.updated 45s 超时 ×3 key、平台现役 stt id（senseaudio-asr-1.5-260319）1011 "realtime transcribe service unavailable" ×3 key**——服务端实时转写自 10-08 16:10 起持续宕机 >56h，**key 池鉴权层健康**（WS 层无一 401）；RAM 可用 3.15GB。③观察器 `_server_watch_autostart.py` 重新后台部署（30 分钟探针、恢复即自动启 30 路滚动、16 次 ≈8h 窗，超窗由下轮会话再探）。④口径对账：survey 实转池 **4,301＝任务书 4,255＋46 引用期** 精确吻合；json **3,355（78.0%）**／待转 **946**（含 failbak 挂账 26 期，盘上 52 件=json+verdict 双件）；复核裁决件 3,365、积压 0；字幕替代波（10-10 令）在盘 3,685 VTT 维持不动。

- **w165 字幕替代波收口（2026-10-11 01:0x～02:1x，主理人令「优先下载字幕＋使用 cookies 加速」）**：①895 清单（`_tmp/yt_new_list.txt`，池内未转录 871＋failbak 24 口径）终态 **871/895 落盘**（651 为前波已存＋本轮 2 分片并行 OK 219＋tv 客户端重试收回 1），**24 期确认真无英字挂账**（`yt_subs/yt_subs_fail_final.txt`；cookies＋PO Token＋node 运行时＋tv/bare 双客户端全试尽，均为 no-sub 非限流），无字幕期等转录恢复后走 ASR 补转。②cookies 管线四修（主理人 20 条 cookies 转 Netscape 落 `yt_subs/cookies.txt`，script/ 整树不入 git 不外泄；修 `--cookies` 插入位 bug——曾被 `python -m` 当模块名致整轮零请求假失败；装 **yt-dlp-ejs 0.8.0**＋脚本固化 `--js-runtimes node`——yt-dlp 2026.08 默认仅启用 deno，本机无 deno 致 n-challenge 失败格式清单为空，即「Requested format is not available」刷屏根因；**bgutil PO Token 常驻服务 v2.0.1 起 127.0.0.1:4416**）。③效果：429 计数清零（此前匿名跑频发限流），实测 ~8 期/分。④转录线并行无恙：观察器值守中服务端仍未恢复（>56h），恢复即自动 30 路。⑤盘存 `03-原始史料库/14-播客史料/youtube_subs/` 4,107 件。

- **w166 字幕排除令＋全线静默（2026-10-11 02:3x，主理人令「已有字幕的视频不要再转录，立刻结束」）**：①**排除规则固化**进 `tb2/15_parallel_transcribe.py`（`SUB_VIDS`＝`youtube_subs/` 内任一 `.en*` 件在盘的 vid 集合，构建 pending 时直接跳过）——实测**排除 882 期**，转录队列从 946 收敛至 **64 期**（＝24 真无英字＋failbak 无字期＋清单外无字期），服务端恢复后 30/55 路重启只会派这 64 期。②**全线静默**：观察器 `_server_watch_autostart.py` 与 bgutil PO Token 服务（4416）即刻 TaskStop，进程与端口复验零残留；转录保持 worker=0 等服务端恢复（>56h），恢复后按 §五 重启。③字幕波终态 871/895、24 期挂账见 w165；本批记档随 `4b6aeea6c` 后补提交。

- **w167 字幕源全量入库＋fail 挂账大销账＋首个字幕期引用改写（2026-10-11 09:0x～09:5x，主理人令「批准继续，同步入库入大纲」＋新增令「解决 fail 挂账」）**：①观察器重启（恢复即自动 30 路；剩余 64 期队列已含 w166 字幕排除）。②**字幕入库 878 期**（`yt_subs/03b_ingest_subs_20261011.py`：episode_id＝survey 值与 3,397 条 ASR 行同键空间——现行 episodes 表已重建、871/882 无行，orphan 口径 w163 已备案，不新注册 episodes 行；model=**youtube_subs_20261011**、review_status='reviewed' 沿 youtube_subs_20261001 先例；VTT v3 解析＝自动字幕取带标记行/人工字幕全取＋[Music] 整行标记剔除＋200 字门槛；segments **+436,364**、source_info +878 带 VTT sha256 留痕；4 期已有 10-01 波行跳过，882 范围闭合零悬空）——库内 transcripts 总量 **5,450**（ASR 3,397＋subs_20261001 1,123＋subs_20261011 878＋auto 52）。③**fail 挂账 9/24 期销账**：24 期盘面中 7 期 DB 已有字幕转写行（今日 878 波 6＋10-01 波 jfe43i0rz5g）移 `failbak_resolved_subs_20261011/`（含 w163 移入的 ASR fail json 留档，manifest 两批）；余 17 件/9 期＝8 期无字幕等 ASR（Qc0QRdxVv3g、Rsk2YZPOpG0 及 _r2 变体、Y0MYPEKKF0g、sx2unUrsQhc、K2Zmq9IDXdE、xO0x5_3A1X4）＋BOPeeLhZOsY（EuroBSDCon 15 秒宣传片，字幕实测仅 1 字符「n」，无内容可转，**建议主理人裁「无内容期」关闭**）。🔴坑＝failbak 文件名双前缀（`youtube__*.json`＝w163 移入的 ASR fail json、`f_*.json.failbak`＝旧判废件），vid 剥离须先去 `youtube__` 再去 `f_`，只去后者会把 7 期已销账期误判成挂账。④**大纲同步·cited46 对账**＝21 已收口＋**1 本轮改写**＋24 无源等 ASR：ZGmuZz5ETHs（failbak 期）字幕源入库后 4 处镜像条目守恒改写（各 1 行）——存疑脚注升级（维护者原话「It's the work of Robert Maggie」（21611.0-21616.2）在案，音合原注 Nagy 仍非书面确证；「10,000 patches for Chrome」（21616.2-21618.9）逐字支持）＋订正尾补字幕源复核注（GTK2“自己的猫”21353.8-21375.0／Python 2.7 21375.0-21490.1／万补丁拒上游化 21616.2-21637.8 三段全命中，时间轴与 YouTube 字幕源一致**无需重锚**）——**cited 22/46**。numstat 4 文件各 1/1；88.5 他线在途改动 2/2 不入本提交。⑤新增条目通道：878 期字幕转写入池，候选大增，批 83 起按 ≤20 节奏续排（排除清单须 pilot map＋批 1-82 已做集合并集，坑⑫），留待下批。

- **w168 批 83-85 新增条目 48 期全链收口＋fail 挂账清账（2026-10-11 09:5x～15:0x，主理人令「批准所有建议」「批准最多8路子代理滚动缺1补1立刻」）**：①**BOPeeLhZOsY 经主理人批准按无内容期关闭**（EuroBSDCon 15 秒宣传片，字幕实测 1 字符，failbak 移 resolved 留痕）——failbak 终态＝8 期全无字幕等 ASR 重转。②**新增条目批 83-85 共 48 期落盘**（`_pilot83_content_a.json` 50 期−FFS 双上传 2 留裁）：候选＝878 期字幕转写池（时长≤5880s 保〔mm:ss〕两位分钟、≤11 万字符适配子代理上下文、已做集合 1,500 vid 排除）；10 组×5 期滚动起草（🔴general-purpose 型子代理遭账户风控 "unusual activity" 全灭，改 **Explore 型**可用；账户并发上限实测 ~4 路存活、user concurrency limit 与 ECONNRESET 频发打死组 3/7/9——组 3 死前落稿本地修复后缀、组 7 SendMessage 带上下文复活回修 CJK、组 9 死前落稿自全、组 6 四派三败终成）；全过 b80 硬规则门禁（双论点连续区间拼接／〔mm:ss〕内联单调且在区间／CJK 300-900／整数端点／文献行模板）。**落盘 48 期×2 论点＋48 文献入 292.4 块（批 83=20/84=20/85=8）**，新增条目累计 **1,558→1,606**；组 10 发现 McKusick FFS 史双上传（UmTX/TMjg）与 121.1 已立目 DEEr6dT-4uQ 同演讲→剔除留裁待主理人裁；组 1 发现 svBX/xGk5 同演讲双上传→互补选段入批。🔴**工具坑三连（新立）**：①Write 工具对正则 `\\[` 双层转义→落盘脚本 VID_RE 恒空→already 失效→批 84 重复落盘批 83 的 20 期（×4），污染态又被 F4 会话共享索引提交扫入 65bcd9187——**正则一律纯字符串构造（chr()＋re.escape＋[0-9]，零反斜杠）**，落盘脚本自带幂等护栏（内容件 vid 行数断言 ×2）；②Bash heredoc/printf 同样吃反斜杠，校验器禁内联；③多会话共享索引下他线 commit 可能扫入我线 staged 件——跨会话落盘后必须以「内容件 vid 行数=2」复验而非信任 numstat。③字幕入库 878 期／cited 22/46／口径对账见 w165-w167；观察器值守中（服务端宕机持续，恢复即自动 30 路转剩余 64 期）。

- **w169 批 83-85 逐个全量质量复核＋claim 库三层入藏＋05-大纲 ROW_MINE 同步（2026-10-12，主理人令「进行全量质量复核（逐个）然后按规则入claim 库，同步按规则入05-大纲」）**：①**逐个复核**＝8 组子代理（Explore 型滚动、缺 1 补 1、并发上限 ~4 路实测）对 48 期×2 论点逐句核验（禁抽查）：事实/数字/人名/引文逐字、〔mm:ss〕落点、区间覆盖、场合相符——**9 处缺陷全部外科修复并复审 pass**（ILOt 34.7亿→3.47亿；8SUkr 去「第三块基石」无据框架＋出区间引句换原话；auio/bTWv 区间扩展覆盖 Symbian/goroutine 段；bTWv 标记 60:22→59:31；Cdyf 场合 LISA→SREcon（转写 "we're at srecon"）；nZfNeh「所有人都忘了」→第一人称；O0TQT「作者之一」→「亲历者」；3SuuA 区间+3 标记实位；5CAQ Drift 句 764-836 搬至论点 1；5zms 区间覆盖 Flash 收尾；xGk5 awk 段覆盖＋删误位标记；zOu5 区间起点 499）；修复全程双写（内容件＋大纲）并以「内容件↔大纲 96/96 逐行一致」＋机械门禁复扫 50 期 PASS 收口。②**claim 库三层入藏**（`_b83a_claim_ingest.py`，04-现代研究文献/historical_claims.duckdb）：SRC-youtube 48（content_hash=转写全文 SHA-256）＋evidence 96（EV-youtube:<vid>:<seq>，quote=论点区间转写**原文照录**，kind=podcast，confidence=0.85）＋claim **CL-15-065..160**（FACT/L1/status=supported；**措辞门禁＝据〔场合〕讲者口述归源限定**，9 处禁写词消解）＋claim_evidence 96（supporting）＋source_chapter 48（15/292/292.4/used）＋update_log；事务批断言 n1-n0==96。③**05-大纲 ROW_MINE 注入**（`_b83a_outline_inject.py`）：48 块（块头 `ROW_MINE: youtube.episodes.<ep> 批83a`＋**讲者口述抬头＋等级标注从 claim 库读真值**＋引用纪律句），WO-007 幂等（has_block＋UTF-8 无 BOM＋LF）。④**证据等级门禁**：本批 48 块**零错标**；全库 FAIL 1482 处均系 index.md 悬空引用历史债（引用号不在主库＝多库拆分旧号，非本批引入），留档待专项。⑤规则依据＝specs/003-login-claim-outline 契约（三层入藏＋outline-inject＋WO-007＋audit_evidence_level_labels）；podcast 线适配＝source_db='youtube'/source_type='podcast'/carrier='youtube_video'/source_layer=2（一手音视频档案）。

## 二、模型与 API（同任务书3）

- WS 流式端点 `wss://api.senseaudio.cn/ws/v1/realtime/transcriptions`，模型 `senseaudio-asr-stream-1.5-260910`，16k mono s16le、server_vad、smart_edit off（verbatim）、15 分钟分块（BLOCK_SECONDS=900）、~8x 实时；**术语热词已撤销**；PCM 流式读取（`02_transcribe.py` seek/read 增量，RSS 44–55MB/worker）。
- **服务端全局并发上限 ≈30–40**（32/48/80/120 路实测 1011 风暴），**30 路＝上限内最优**；零星 1011 走 worker 内部 retry 自愈，风暴则降并发。
- **120 路实测定案（2026-10-07 18:0x-18:13，主理人令测试）**：120 路重启后 ~113 路起**大量 1011 "realtime transcribe service unavailable"**（新 worker 日志 18 分钟内 1,652 条、重试风暴拖慢实际吞吐），本机 **RAM load 93%、可用 1.0 GB**（15.8 GB 机；30 路时 74%/4.0 GB）；**吞吐实测 120 路＝4 期/8min（30 期/h），低于 30 路基线 ~49 期/h**。结论＝**120 路双重约束不可行（服务器 1011 拒绝＋本机内存近枯），30 路仍为最优**；已按机制回落 30 路（杀旧＋重启，RAM 回升 4.0 GB/74%）。附带：120 路期间 giceCouM3F8 ffmpeg 解码探针失败（rc=4294967294）——该期已完整 reviewed（episodes 表数字 id 319），无数据损失。
- **40–90 路阶梯实测（2026-10-07 18:24-19:18，主理人令找最优）**：每档杀旧→重启→3min 稳定→8min 测量窗（吞吐/1011 增量/RAM）：**30 路（基线）~6.5 期/8min；40 路 3/8min、1011 79、RAM 80%；55 路 8/8min、1011 125、RAM 87%→确认窗 13/8min、1011 46、RAM 91%；70 路 4/8min、1011 171、RAM 91%；90 路 1/8min、1011 344（风暴）、RAM 95%/0.6GB**。结论＝**55 路为 40-90 区间最优（确认窗 ~97 期/h ≈ 30 路 2 倍，1011 零星自愈范围无风暴）**；70 路起 1011 递增、90 路风暴＋内存枯竭。**✅ 2026-10-07 主理人批准：55 路为运行档**（任务书3 §四.4 已同步改写；风险注：RAM 可用 1.3-1.9GB 偏紧，其他应用增多时回落 30 路一条命令 `15_parallel_transcribe.py 30`）。

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
- **M4：新增条目 50%（~690/1,380）——✅ 已达成（2026-10-08 4:2x）**：批 33-37 落盘后新增条目累计 **690/1,380**（批 1-37 共 37 批；提交 `3fb4fae59`）；门禁 citation-tags+markers 全 PASS。下一手＝M2（转录 100%）＋M3（复核/入库追平）。
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