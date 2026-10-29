# 20260816_邮件库message_id补齐

## 查证来源

- `03-原始史料库/11-邮件列表史料/03-openbsd/openbsd_mail.db` messages 表（no-id 记录）
- 磁盘 mbox 源文件：`raw/mbox/openbsd-*/YYYY-MM.mbox`（月度，含 `X-MARC-Message` 头）与 `raw/marc/openbsd-*/<m_id>.mbox`（逐封/线程）
- marc.info 月度索引页（`https://marc.info/?l=<list>&r=N&w=4&b=YYYYMM`，联网）
- 前序成果：`20260815_邮件库数据核验.md`（47,975 补齐 + 10,809 去重，剩余 512 待回源）

## 交叉验证方法

- 字节级匹配：重读磁盘 mbox 分片，`sha256(raw)` 与库内 `msg_hash` 精确比对（最强，字节级）
- 时区归一化匹配：库内 `date`（多为 +08:00 本地）与 mbox `Date`（+00:00 UTC）实为同一时刻，转换为 UTC 时间戳后比对
- 联网索引匹配：抓取 marc.info 月度索引，`规范化 subject（去 [tag]/Re:/Fwd: 前缀 + 折叠空白 + MIME 解码）+ UTC 日期` 唯一命中
- 批内冲突检测：同一 list 内多条 no-id 映射到同一 `marc:<m_id>` 判为重复采集，保留最小 id，删除其余

## 存疑判定依据

### 1. 本日回填与去重成果（2026-08-16）

- 回填 406 条（no-id → `marc:<m_id>`）：sha256 字节级 394 + 时区归一化 5 + 联网索引 6 + ppc Onyx 1
- 去重 46 条（重复采集删除）：批内冲突 9 + 时区匹配去重 36 + ppc Onyx 1
- messages 总数 154,165 → 154,119（-46），no-id 512 → 60（-452），marc 48,463 → 48,869（+406）
- integrity=ok

### 2. 剩余 60 条 no-id 无法回源（诚实保留 no-id 标记）

- misc 48 条：源月度 mbox 已删（1997-12 至 2003-08），且 subject 多为 `Re:` 回复（与根消息 subject 歧义）、`<No Subject>`、中文垃圾邮件（`欢迎光临…`、`FREE guide…`）等，联网索引无法唯一匹配
- bugs 10 条：均为 marc.info 线程回复/补丁。线程 mbox 下载（如 `140651474131660.mbox`）剥离了回复消息的 `Message-ID` 与 `X-MARC-Message` 头，仅线程根消息有 m_id，回复消息在月度索引中无独立 m_id，无法回源唯一标识
- ports 2 条：`[PATCH] Fix json_writer…`（2025-05）不在 marc.info 月度索引；`[PATCH] x11/xmobar: update to 0.51.1`（2026-07）与索引中 `xmobar update to 0.51.1 (Re:…)` subject 不一致，无法唯一匹配

### 3. 附带发现（未处理，超出本次 message_id 补齐范围）

- messages 表 `month` 字段存在系统性错误：部分记录 `month=1` 而 `date` 字段正确（如 `1999-06-13` 对应 `month=1`），系早期采集路径日期解析 bug，与 `year`/`date` 字段不一致。建议另行核查修正。

### 4. 日志留痕

- `script/_folder_db_logs/deletion_log_20260816_openbsd_mid3.jsonl`（sha256 回填 + 去重）
- `script/_folder_db_logs/deletion_log_20260816_openbsd_mid3b.jsonl`（时区归一化回填 + 去重）
- `script/_folder_db_logs/deletion_log_20260816_openbsd_mid3c.jsonl`（联网索引回填 + ppc Onyx）
- 备份：`script/_folder_db_logs/deletion_backup_20260816_openbsd_mid3/openbsd_mail.db`（本日执行前快照）
- 注：mid3.jsonl 含 11 条首次执行（因 UNIQUE 冲突回滚）遗留的日志条目，对应 UPDATE 未提交入库，DB 实际回填 394 条，日志比 DB 多 11 条孤儿记录，以 DB 为准