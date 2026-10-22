# checklist.md — adr0010-outline-writer-20261022

> 每项证据须为可复跑命令＋原始输出路径；未取得证据写“阻塞／未取得”，不得勾选通过。

## A. 需求基线

- [x] A1 FR-01–FR-10／NFR-01–NFR-05 全部有验收证据（spec.md 判据列）
- [x] A2 追溯链无断链：来源 → FR／NFR → 任务 → 验收 → 证据

## B. 实现

- [x] B1 脚本落位 `00-编纂规则与格式规范/01-规则/脚本与命令/outline_writer.py`（固定脚本位）
- [x] B2 无裸 `assert` 作唯一失败出口（失败路径均 stdout 可见＋exit 2）
- [x] B3 默认 dry-run；写盘须显式 `--write`（ADR-0008 §1.3 CLI 安全默认）
- [x] B4 `--help` 不触发执行、不写盘
- [x] B5 路径断言：`--root`／`--work`／`--ledger`／各输入／各宿主均在 `--allow-root` 内
- [x] B6 启动打印 `[paths]` 生效绝对路径
- [x] B7 生产路径仅只读（duckdb `read_only=True`；不写 05-卷册大纲）

## C. 沙箱验证（ADR-0009 L0–L5）

- [x] C1 L0 生产零改动（05-卷册大纲 聚合哈希＋claim 库 size/mtime/head 前后一致）
- [x] C2 L1 读入真实（20 pk 真实 claim_map／narr；`--check-only` 生产 0 未解析）
- [x] C3 L2 写入真实（副本 +N，宿主 SHA-256 变化）
- [x] C4 L3 逐条内容回读（每块 5 行、块头四要素、摘要＝narr＋纪律串逐字节）
- [x] C5 L4 幂等二跑 +0＋第 2/3 跑 stdout 逐字节一致＋回滚还原哈希复原
- [x] C6 L5 坏件三例 exit 2、stdout 可见 `[check]`／`[abort]`、零写入
- [x] C7 验证报告落盘（命令、原始输出、判定、偏差如实记录）

## D. 登记接线

- [x] D1 registry 件次号去重（`outline_writer.py` 改 `—`；不得占用他件号）
- [x] D2 `STAGE_MAP` 补 `outline_writer.py` 合法阶段
- [x] D3 registry `selftest="--selftest"`
- [x] D4 `脚本与命令/README.md` 增行（用途＋规则引用位置）
- [x] D5 `流程规则.md` 新增小节（ADR-0010 三项＋写盘契约指针）并同步二级索引
- [x] D6 `--selftest` 判据非空（正＋负夹具）

## E. 债务与披露

- [x] E1 TD-015 状态与偿还证据更新（不满足即维持“偿还中”并写明剩余项）
- [x] E2 `index.md` 偿还进度与阻断顺序同步
- [x] E3 发现项披露：H 线 L3 抬头“当事人自述”与 `ROW_MINE块体格式规则.md` §四（L3→二手转述）差异——登记＋主理人裁定队列（不擅自改生产块）
- [x] E4 未验证项与已知限制写入收口证据

## F. 门禁（全量，缺一不可）

- [x] F1 `audit_gate_registry.py`（R1–R8 全 PASS）
- [x] F2 `audit_engineering_practice.py`（E1–E7）
- [x] F3 `audit_task_lifecycle.py`（L1–L12）
- [x] F4 `audit_markdown_lint.py`（本批改动 .md 均通过）
- [x] F5 `audit_md_quote_glyphs.py`、`audit_md_bold_spacing.py`
- [x] F6 `sync_refactor2026_baseline.py --check`、`_longline_status.py --check`（常备）
- [x] F7 `outline_writer.py --selftest`

## G. 复核与收口

- [x] G1 复核第 1 轮（主理人：批准 ADR-0010 并按规则重建——范围签收）
- [x] G2 复核第 2 轮（复核子代理：初稿独立复核，复跑命令／回读产物）
- [x] G3 复核第 3 轮（复核子代理：修复后复验）
- [x] G4 changelog 记录（prebak＋id）
- [x] G5 两台账收口回填（prebak=／已知限制=／轮替=／归档=）
- [x] G6 提交：显式 pathspec、`-F` 消息文件、`--no-gpg-sign`；提交后 `git show --numstat` 核对
