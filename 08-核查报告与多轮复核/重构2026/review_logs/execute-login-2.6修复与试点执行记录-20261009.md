# ;login: 线 Task 2.6 修复与试点执行记录（子代理执行，2026-10-09）

> 归属：spec `converge-all-remaining-tasks` Task 4.1 之**阻塞项修复**（对应 `execute-login-title-fix-and-figures-ocr` Task 2.6）
> 执行：工程子代理（2026-10-09，报告经主会话核收）；未触碰 `outline.txt` 与 `.trae/specs/`
> 状态：**2.6 完成并验证通过；全量 2.3 未启动（前置：队列重建）**

## 一、根因与修复（均留 `.prebak-t41-20261009` 备份）

1. **根因（决定性证据）**：`sensenova-6.8-flash-lite` 官方默认**开启思考**——同一 12000 字符窗口在 `reasoning_effort=high` 下 243s、`finish_reason=length`、reasoning 53378 字符、无 content；改 `reasoning_effort:"none"` 关闭思考后 **12.0s、`finish_reason=stop`、content 2821 字符、合法 JSON**。
2. **修复（4 处）**：
   - `script/_sensenova_lib_20261005.py`：`chat()` 增 `response_format`／`reasoning_effort` 透传；解析改 `.get()`；content 缺失且仅 reasoning 时读 `finish_reason` 并抛可重试 `ReasoningOnlyError`（不再 KeyError）。
   - `script/_title_fix_engine_20261005.py`：import 由**已冻结的 glm 旧线路**改回 sensenova；`max_tokens` 6000→24000（上限 32000）；prompt 禁推理＋`json_object`。
   - `script/_sensenova_cfg_20261005.json`：`max_tokens_extract` 6000→24000。
   - 配套：`script/_t41_assert_staging_20261009.py`／`_t41_assert_db_20261009.py`（只读断言）。

## 二、试点（13 期）与断言

- 引擎：`python script/_title_fix_engine_20261005.py --issue {25,1,227,26,12,4,15,36,29,38,123,112,108} --workers 1` → **13/13 成功、0 失败**。
- 回写：`python script/_title_fix_writer_20261005.py --drain` → applied=226／skipped=4／**quarantined=0**。
- 只读断言：corrected=11／unresolved=219／issue_failed=0／quarantine=0（示例：'Feature'→'IBM Mobile FileSync' match=0.90；'The System Administrators Guild'→'…LISA Conference' match=0.91）；DB 端 11 行均 `status=corrected, needs_review=false`，articles=6604 守恒。**两项断言 PASS**。
- 429（tpm/rpm 限流）经冷却换 key 自动恢复。

## 三、遗留（交接）

1. `script/_task_queue_title_20261005.jsonl` **磁盘缺失**——全量 2.3 须先 `python script/_title_queue_build_20261005.py` 重建队列。
2. `script/_title_review_engine_20261005.py` 仍 `import _glm_line_20261006`（glm 池已余额耗尽：`HTTP 400 …已达到使用限制或余额不足`）——Task 2.4 前须同法改回 sensenova＋`reasoning_effort=none`。
3. DB 实况与任务书不符：figures=12403（任务书称 16806）；needs_review 已被历史运行部分处理——本任务未触碰，登记备核。
4. **Task 2.3 全量启动命令（待队列重建后执行）**：
   ```
   python script/_title_queue_build_20261005.py
   python script/_title_fix_writer_20261005.py --drain
   python script/_title_fix_engine_20261005.py --shard 0,1,…,39 --workers 120
   ```

*记录：WorkBuddy（核收子代理报告），2026-10-09。*