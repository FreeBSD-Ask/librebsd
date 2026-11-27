# Quickstart: 验证指南（实施完成后端到端验收）

**Feature**: specs/002-dvd6-journal-db | 前置：spec.md（验收场景）、data-model.md（校验规则）、contracts/（不变量）

## 前提

- 四库已建成：`dvd6/Website/ddj/` 下 `ddj.duckdb` / `cuj.duckdb` / `sa.duckdb` / `tpj.duckdb`。
- 全文库已增量入库、大纲两层已落账。
- 只读验证一律独立进程（写连接已关）；UNC 上校验一律写脚本文件再跑（禁内联 heredoc）。

## 验收场景（每条可二值判定）

### 1. 四库存在性与期覆盖

```text
期望：ddj/ 下恰 4 个 .duckdb；每库 issues 的 (year, issue_label) 集合
      ＝磁盘实测（CUJ 1990–2006 月包 / DDJ 1988–2009 年包 / SA 1992–2006 /
      TPJ 全部 tpjNNNN 包），差集为空。
```

### 2. 抽样保真（≥12 期，每刊 ≥3 期）

```text
期望：① articles 数＝该期 articles 树实测文章目录数；
      ② 任抽 3 文 body_text 与源 HTML 转文本逐字一致；
      ③ source_files 与解压文本逐字一致；
      ④ 图片 figures 台账处置完整。
```

### 3. 二进制与路径纪律

```text
期望：全库文本列扫描 NUL/magic 头 0 命中；任何表无完整磁盘路径字段值。
```

### 4. 图片台账零悬空

```text
期望：figures 无 uncertain；transcribed ⇒ transcription_text 非空且转写来源
      为会话子代理读图（无本地模型调用记录）；base64 ⇒ base64_data 可解码。
```

### 5. 规则补齐闭合（2026-10-05 修正：替代原 references_fulltext 场景）

```text
期望：每库 refs/summaries/key_facts 与 articles 闭合（refs=articles 计数；
      summaries 无缺行；key_facts.reference_id 全部回指本库 refs，0 悬空）；
      抽样 12 篇概述与 body_text 相符且含关键词与原文摘引；幂等重跑 0 新增。
      references_fulltext.duckdb 在本件 git/库层面 0 改动（只读侦察＋备份除外）。
```

### 6. 大纲两层闭合

```text
期望：新增 卷末书目述评 bullet（- **ref <DB>-<id>**｜体例）与 key_facts
      related_chapter 全部可回指四库 refs（0 悬空）；bullet 判重重跑 0 追加；
      大纲门禁全绿。
```

### 7. 留痕可审计

```text
期望：build_log 每批有 note（处理数/跳过数/二进制命中数）；每条库内容可经
      archive_layer + issue_label + file_name 追溯到源。
```

### 8. 推送门禁（2026-10-05 修正新增）

```text
期望：C:\ddj_stage 四库推送到 dvd6/Website/ddj 后，逐库 sha256 双侧一致、
      双侧行数断言一致；推送前本地库已通过场景 1–7。
```

## 一键核验入口（实施期落成后填充实际脚本名）

```text
C:/Python314/python.exe script/_ddj_verify_all.py        # 场景 1–4、7
C:/Python314/python.exe script/_ddj_verify_rules.py      # 场景 5
C:/Python314/python.exe script/_ddj_outline_verify.py    # 场景 6
```

（脚本名为占位，实施时以 tasks.md 实际产物为准；核验脚本自身判据须独立成变量、先断言非空。）
