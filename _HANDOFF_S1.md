# 交接书 S1 —— 释疑闭环·大纲改写·文献库重释·视觉重 OCR 战役

> 交接时点：2026-09-25。本书记录本轮全部已完成成果、资产、断点与纪律。下一会话读此书即可无损接续。
> 相关记忆文件：`doubts-closure-and-google-channel-20260924`（已同步）。

## 〇、主理人指令链（全部有效，按时间序）

1. doubts 库 open/unresolvable（139 条）三通道（本地 DB＋大纲＋联网）批量结案后入库入大纲；需要而无法检索的书目/论文列出；不请求关闭，实在无法查询的继续维持；遵守学术规范。
2. 05-卷册大纲中「谷歌/必应无法搜索」类字样逐个闭环，不计成本。
3. **先解决数据库问题，再解决大纲问题。**
4. 大纲直接原地修改。
5. 子代理上限 4 路（**实际实测并发=2 路**，见 §四.1）。
6. WebSearch 不能用谷歌：自行修复或装本地 MCP，或直接无头浏览器/fetch（已解决：本机内置浏览器＋Google 10 区域域名轮换）。
7. 尝试从本地数据库《UNIX 传奇》释疑；**英文原版在库，交叉比较；不使用中文译本**。
8. 重新释读参考文献数据库，逐个复核提取有价值信息；**同时存在译本的不采纳译本**；修正增补大纲和错误；不计成本。
9. PDF OCR 条目：**无论现有质量如何，全部 303 件（7129 页）必须由 GLM 直接视觉识别重新 OCR、全量逐页转录，不得按质量筛选跳过**（不使用本地模型）；乱码件（27 件 612 页）另加逐个全量；源文件有问题的重新下载（子代理任务）。
10. **不使用子代理，继续 OCR；顺序进行。**（当前有效模式：主代理直接读图转录）

## 一、已完成成果（全部已落盘）

### A. doubts 库（04-现代研究文献/06-存疑数据库/doubts_standalone.duckdb）
- 596 项主台账（大纲标记 458＋open/unresolvable 139，交集 1）：`_tmp/master_items.json`。
- Google 全量复检 **1014 条查询**（本机浏览器 10 区域域名轮换，0 CAPTCHA 残留）：`_tmp/gsearch/results.jsonl`。
- 三通道取证 B1–B4（每条本地库＋DDG＋学术 API＋逐字引文）：`_tmp/research/B*.jsonl`。
- 逐项判定 J1–J8（596 项全覆盖）：`_tmp/judge/J*.jsonl`。
- **DB 写回**：139 条（resolved 49／维持 84／unresolvable 6）＋doubt_review_log 审计行；终态 **resolved 2404 / open 69 / unresolvable 23**（原 2357/84/55）。写回脚本 `_tmp/writeback_db.py`/`writeback_db2.py`；写前整库备份 `_backup/doubts_standalone.20260924_pre_close.duckdb`。
- **抽验纠错 2 处**（子代理误核对象）：1692（真对象 Hafner & Lyon 1996，非 Salus）→ open；1694（DDN/DISA 档案实地查阅）→ unresolvable。
- 抽验通过样例：Apache 八人名单、BSTJ 57(6) McIlroy 前言（archive.org 逐字）、Honeywell v. Sperry Rand 180 U.S.P.Q. 673、NetBSD 1994-12-23 Adam Glass 公告。

### B. 05-卷册大纲
- **458 处「谷歌/必应通道故障」注记行原地改写**（108 文件）：全部替换为当日真实 Google 结果（命中/仅泛结果/负结果三式）；后验=旧措辞零残留、逐文件行数守恒、新标记恰 458。改写器 `_tmp/rewrite_outline.py`（括号深度感知分句；引擎正则禁裸 "Google"）。备份 `_tmp/backup_outline`（108 件）＋`_tmp/backup_outline2`。
- **正文改订 4 处**（均有独立实测/一手证据）：
  - 1643：45.18 Evans Hall→Sproul 距离实测 **457 m**（Nominatim 坐标球面计算，原「300-400 米」偏低）。
  - 1690：195.3 OpenBSD Foundation 时序（最早可考 1999-10 本地 raw mbox；成立公告 2007-07-25 undeadly；「2003 年发起」无原始存档）。
  - 126：58.6 Apache 创始八人名单补全（Hartill/Robinson/Terbush/Thau/Wilson）＋概述勘误登记结案。
  - 1521：驱逐事件订正为 **1994-12**（Adam Glass 1994-12-23 公告逐字）——347 章概述/347.2/347.4 三处。
- **书证增补 2 处**：11.9.2（UNIX 4.0 PWB 文档集，见 §一.C）；35.4（Computerworld 1988-10-24 p.7 两篇 Unix 战争报道逐字）。

### C. 《UNIX 传奇》书证（英文原版）
- 英文原版 PDF：`04-现代研究文献/03-文献下载/05-书籍/01-pdf/20260805_Kernighan_UNIX_History_Memoir_2019_en.pdf`（197 页）；全文 `_tmp/unix_memoir_en.txt`。中译本全文 `_tmp/unix传奇_fulltext.txt`（**仅作参照，已全面弃用**）。
- 16 条 doubts 记录书证=英文逐字（2008/2009/2011/2012/2013/2015/2016/2017/2019/2020/2024/2026/2083/2086/2117/2510；另有 1956/1998 旧有）＋大纲 7.8 佐证注。全库 0 条引用中译本。
- 中译本偏差实证：中译 p.72「MIT 于 1964 年推出 CTSS」英文原版无此年代表述。
- 2013「Ken's new system」短语**英文原版亦无**（负结果双语坐实，维持 unresolvable）。

### D. 参考文献库重释疑（references_fulltext.duckdb；注意表名 "references" 必须带引号）
- 盘点：5574 种/4100 全文/3650 有块；**语言错标 43**；**编码乱码 29 件**（`_tmp/cjk_works.json` 178 种 CJK 实测；乱码筛查 PUA/兼容区>3%）。
- **译本不采纳**：#55（回忆录中译）、#7/#8（K&R 徐宝文译，#8 整本乱码）已写 reference_update_log usage_flag。
- **文件路径甄别**：922 件「问题」大半误报（84 播客在外部库、138 md 被误当 PDF、round3 文件已并入 01-pdf 但表内路径旧）；真重下清单 `_tmp/really_missing.json`（约 40 件：3 pdf＋web/判例）。
- **视觉重 OCR 战役**（状态总入口 `_tmp/REOCR_STATE.md`）：
  - 渲染：300 件 7129 页＋乱码件 27 件 612 页 → `_tmp/reocr/<ref>/pNNNN.png`；清单 `_tmp/reocr_worklist.json`/`_tmp/reocr_meta.json`/`_tmp/mojibake_worklist.json`。
  - 已写回 DB（extraction_method=`glm_vision_20260924`，旧 OCR 块删除留痕）**11 件**：UNIX4.0 手册 2817/3565/3566/3567（含 **#3566 Ritchie&Thompson 论文 UNIX 4.0 重印本**）；516-TSS 3586/3587/3588/3589/3593/3594/3598。
  - 合并脚本 `_tmp/merge_reocr.py --apply`（**仅全覆盖才替换**守卫）；批次 `_tmp/reocr_batches/`；手录单页目录 `_tmp/reocr_out/pages/`。
  - key_facts 新增 11 条（PWB/UNIX4.0×4、Computerworld×7：Archer group/Sun blasts OSF/Oracle Sequent 124tps/NIST chads/CERN-Oracle LEP/TPPC 史/AT&T-Sun SPARC）。

## 二、重磅史料发现（候选大纲增补，未入大纲）

1. **#3594《THREAD SAVE BLOCKS》**（1968-12-12，修订 1969-06-12）：516 多道系统以 **"thread"** 称用户进程；thread save block 全 78 字布局（.RP0-.RP7/.SRP0-.SRP7/.T0-.T17 等）＋sector 0 驻留切换设计。**thread 术语史关键一手证据**（卷1 或卷11 OS 结构线）。
2. **#3593《FORMAT FOR RING INTERRUPT》**（1968-09-19）：环形网 Node Modem 中断协议（Alarm 帧 Ring#/OP code/16 Ring Time Slots，4 组×16 节点；RFS 消息）——**1968 环网协议设计一手**（卷1/卷21 传播渠道线）。
3. **#5454 Computerworld 1988-10-24**（已录 p1-40）：p7「AT&T heads new Unix group」＋「Sun blasts OSF」；p31 CERN 用 Oracle 管 LEP 对撞机；p34 TPPC 史（Omri Serlin）；p35 CERN/Oracle 详述（Vaxcluster+3090/VM+Apollo/RT/VAXstation 100+ 工作站）；p37 AT&T 承诺 Sun SPARC 线、持 Olivetti 25%；p20 NIST 投票机（chads）；p9 Oracle UNIX 124tps on Sequent。

## 三、断点与续作（下一会话从ここ开始）

1. **Computerworld #5454 p41** 起顺序转录（已至 p40/153，15 万字符；余为 Review/Government/专题版）。产出→`_tmp/reocr_out/pages/5454_pNNNN.txt`→并入 `_tmp/reocr_out/w1_a_me.jsonl`。
2. **516-TSS 剩 7 件**（顺序）：3590 GMAP Assembler 7pp → 3591 Graphic Display 8pp → 3592 516 Assembler 5pp → 3595 Card Reader Bootstrap 5pp → 3596 Octal Package 3pp → 3597 Node Modem Repeater 4pp → 3599 2pp。产出→`_tmp/reocr_out/pages/<ref>_pNNNN.txt`→并入 `w1_c.jsonl`→全覆盖即 `merge_reocr.py --apply`。
3. **之后按 `_tmp/reocr_worklist.json` 全件顺序推进——不再按质量筛选**：凡 worklist 内 300 件（7129 页），无论原 rapidocr 质量好坏，一律 GLM 视觉逐页重转录并全量写回；AUUGN/Usenix（1447+1294 页）与 UNIX4.0/32V 手册余件均在此队列内。
4. **乱码件 27 件 612 页**（`_tmp/mojibake_worklist.json`）同规全量。
5. 每逢重磅史料（§二 类）随手提 key_facts＋大纲增补；乱码件写回后需重跑其上 key_facts/timeline_events 溯源。
6. 3 件渲染失败另案：#2739（803 页 ZAB 市政档案，定向页处理）、#2787（CHM）、#5442（Custer 书 md 版；其 PDF 扫描=#5443 无文本层，选段处理）。
7. **完成定义**：`_tmp/reocr_worklist.json` 全部 300 件 + mojibake 27 件，全部以 `glm_vision_20260924` 写回（`select count(*) from fulltext where extraction_method='glm_vision_20260924'` ≥ 327），且每件页数与 worklist 相符。

## 四、纪律与坑（血泪清单）

1. **子代理并发实测=2 路**（第 3 路报 user concurrency limit exceeded 且可杀在途任务）；深夜图像通道曾连续 `Captcha instance timed out`——**主代理直接读图最稳**（用户已裁定不用子代理）。
2. doubts 库**全列 VARCHAR**：算术须 `cast(cast(coalesce(nullif(x,''),'0') as integer)+1 as varchar)`；写库单事务；表名 "references" 在文献库须带引号。
3. **DB 内 outline_path/line_number 陈旧**（大纲已重编号、部分目录名含字面反斜杠）——改大纲前必须按疑点关键词回现行文件定位。
4. 注记改写器三要件：括号深度感知分句；引擎正则禁裸 "Google"（Oracle v. Google 假阳）；保留引擎提及前引导文字与 DDG 分句；写后括号配平＋行数守恒后验。
5. **残句疑点（「，需实地查阅」类）子代理易核错对象**——必须回大纲看它挂在哪个文献行（1692/1694 实例）。
6. Google 通道：直连 google.com ~50 条即 CAPTCHA；解法=本机内置浏览器＋10 区域域名轮换＋限速；子代理并发峰值期勿用。
7. 学术规范：引文逐字＋URL＋回原图核对提示；降解处 `[?]`/`[unreadable]`；负结果如实记；译本一律不引。
8. 提交：本轮**未提交 git**（改动含 108 大纲文件＋DB；提交前查并行会话 mtime；pathspec 提交勿整索引）。

## 五、后验基线（续作后必须复跑）

- doubts 状态计数 = resolved 2404 / open 69 / unresolvable 23。
- 大纲：`谷歌通道故障|必应 robots|ERR_ABORTED|search_google|子代理禁用浏览器` 全库 0 残留；「谷歌本机通道」=458；被改 108 文件行数与备份一致。
- 文献库：`select count(*) from fulltext where extraction_method='glm_vision_20260924'` ≥ 11；reference_update_log 9000+ 段留痕完整。
