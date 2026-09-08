# 14-deepseek-cankao 战线 Spec（参考文献缺失补齐管线）

更新：2026-09-07 22:58（四轮去重 + 批1-4下载 + 逐篇审阅完成）

## 1. 任务定义

为《给我自由—一部 BSD 史》补齐大纲/目录/重构2026 HTML 中识别出的缺失参考文献：
扫描 → 去重判定 → 下载 → **逐篇审阅（无抽样）** → mulu/ 按章归类 → 回写大纲。

## 2. 当前状态（2026-09-07 22:58）

### 2.1 总账（2456 条 DKC-0001~2456）

| 状态 | 条数 | 说明 |
| :- | :-: | :- |
| downloaded | 104 | 本战线已下载并审阅（批1-4+重试+子页） |
| exists_local | 230 | 本地/库中已有 |
| not_reference | 203 | 非文献碎片（三轮逐条审阅剔除） |
| in_mail_db / in_repo_db / in_security_db / in_ref_db | 88/51/26/2 | 专题库命中 |
| tuhs_online_archive / no_download_video | 12/3 | 在线归档不下载/视频禁下载 |
| download_failed | 37 | URL 失效（多数中国媒体404） |
| **pending** | **~800** | 待逐条联网检索（见 §4） |

### 2.2 资产

- 数据库：`03-数据库/cankao_refs.duckdb`（13 表，全链路留痕）
- 文献库：`01-文献库/` 311 文件（全部已提取文本至 `02-审阅记录/fulltext/`）
- mulu：`mulu/` 171 章 545 条目（按章归类，可直接回写大纲）
- 中间数据：`script/cankao_scan/scan_results/`（download_queue.jsonl 为待下载权威队列）

## 3. 管线铁律（不变）

- 任何下载文献**必须逐篇审阅**（Read 全文摘要→判定 valid/weak/fail→落库 batchN_review 表），禁止抽样
- 视频一律不下载；TUHS.org 在线归档不重复下载
- 下载文件命名 `YYYY_作者_题名slug.pdf/md`；PDF 先行，无 PDF 存 md 快照（带 frontmatter source_url）
- 每批落盘后：文本提取 → 审阅摘要分片 → 逐篇判定 → 回写 DB → mulu 增量
- 与既有库严格去重：新下载前查 inventory_keys（11462）+ 本战线已下载 URL

## 4. 剩余 ~800 条的检索方法论（接手者按此执行）

### 4.1 组别与通道（download_queue.jsonl group 字段）

| 组 | 条数 | 通道 | 备注 |
| :- | :-: | :- | :- |
| K-需检索 | ~560 | 逐条 WebSearch | 混杂：真文献/残句/汇总引用；先按 §4.3 甄别 |
| H-媒体博客 | 76 | WebSearch→archive.org 快照 | 原文常 404，LWN/Slashdot/OsNews 有存档 |
| J-专门档案 | 42 | bitsavers/tuhs 直链 | 批4直链命中低，需手工逐条定位（如 `bitsavers.org/pdf/dec/` 目录遍历） |
| F-机构报告 | 41 | 官网+Wayback | 基金会年报多为 PDF，可 Year+site 构造 |
| D-付费库 | 35 | WebSearch 找公开副本 | USENIX 官网搜索为 JS 渲染，脚本不可用；ACM/IEEE 抓摘要页标 abstract_only |
| G-书籍 | 30 | Anna's Archive | **本机网络被阻断（SSL EOF）**，须用户环境或换镜像 |
| E-官方文档 | 12 | 官网构造 | 同批4策略 |

### 4.2 每条七步闭环（与 13-deepseek-linux 同构）

1. WebSearch `"<题名>" <作者> pdf` → 取可信直链
2. fetch（PDF 优先；404 则试 archive.org/web/2019/<url>）
3. 落盘 `01-文献库/`，登记 download_log_batchN.jsonl
4. pypdf 提取文本 → fulltext/
5. Read 审阅：身份一致？完整性？→ verdict 落 batchN_review
6. UPDATE cankao_refs（download_status/review_status/review_note）
7. mulu 增量（重跑 mulu 生成脚本按 ref_chapters）

### 4.3 K 组甄别规则（下载前先判定是否真文献）

- 残句/引语/议论（无作者无年份+题名<32 字符）→ not_reference
- "XX 邮件"（作者+年月+邮件）→ 查邮件库（mail_db_check2.py 逻辑）
- commit/tag 引用（含 8+ 位 hex）→ 查提交库
- 书籍《》（有作者/年份）→ G 通道
- 其余带完整题名 → WebSearch

### 4.4 已知阻断与对策

- Anna's Archive：本机 SSL EOF → 用户环境手动下载（规则路径 `04-现代研究文献/03-文献下载/`）或镜像
- USENIX 搜索：JS 渲染 → 用 WebSearch `site:usenix.org <题名>` 直链
- 中国媒体 404：原链失效 → Wayback 快照（`web.archive.org/web/2016/<url>`）
- GBK 乱码页：fetch 后按 `text.decode('gbk', 'replace')` 重转（retry_review 2 条待转）

## 5. 批次日志索引

| 批 | 范围 | ok/总数 | 日志 |
| :- | :- | :-: | :- |
| 1 | papers.freebsd.org 高频 57 | 86*/135 | download_log_batch1.jsonl |
| 2 | A 组带 URL | （并入） | download_log_batch2.jsonl |
| 3 | A/B/C 组净队列 135 | 86/135 | download_log_batch3.jsonl |
| 重试 | download_failed 49 | 12/49 | download_log_retry.jsonl |
| 4 | D/J/E/I 组 99 | 6/99 | download_log_batch4.jsonl |

\* 批1-2 合计 148 文件（去重后 125 保留 + 批3/4/重试/子页）。

## 6. 断点续跑清单

1. `download_queue.jsonl` 过滤 `pending` → 按 §4.1 组序逐条七步闭环
2. 每完成 50 条：重建 mulu + 更新本 spec 计数
3. 全部完成后：mulu 移交主大纲回写（26 号文流程）
