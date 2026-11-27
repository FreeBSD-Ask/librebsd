# Data Model: 05 大纲落地生产执行

**Date**: 2026-10-24 | 来源：任务书 §2.2/§3.2/§4.2 与 spec FR-001…FR-015

## 实体一：mapping.tsv（核心台账，16 列，制表符分隔，UTF-8 无 BOM，表头行＋37,484 数据行）

| 列 | 类型 | 规则 |
| -- | ---- | ---- |
| source_id | `S-%06d` | 按 **relpath 全串数值感知自然序**（数字段按整数值比较，`001.2`＜`001.10`；dry-run F3 规范化，10-23 sim 的纯字典序作废）稳定分配；**一经分配冻结**——mapping.tsv 在盘后再生只复用、禁重排 |
| source_relpath | 路径 | 相对仓库根；与 inventory.tsv 一致 |
| source_sha256_pre | hex64 | B1 改名前内容哈希（2.1b 后以此锁定“迁移前真值”） |
| source_sha256 | hex64 | 当前内容哈希（须与 pre 相等——NFR-003 只改名不改内容） |
| source_title | 文本 | 旧树 H1 题面（B1 标准化后形态） |
| source_section_path | 文本 | 旧卷／章／节路径串 |
| status | 枚举 | **八状态机**（见下） |
| method | 枚举 | 判定方法标记（THREE_PASS／PILOT 等） |
| confidence | 枚举 | HIGH／MED／LOW／PILOT |
| review_a / review_b / review_c | 文本 | 三趟判定记录（target_id＋理由＋策略标记）；CONFIRMED 必全填 |
| target_id | `C-%04d` 或空 | 与 targets.tsv 一致；UNMAPPED 等状态可空 |
| order | 整数或空 | 目标节内语义序（Task 7 填，本 feature 留空） |
| review_state | 枚举 | none／judging／merged／duplicate／adjudicated |
| note | 文本 | DUPLICATE 记代表件 source_id；UNMAPPED 记理由 |

**状态机（守恒不变量：八状态计数之和恒==37,484）**

```text
PENDING ──三趟判定+合并──┬─> CONFIRMED（三 target_id 全同，review_a/b/c 非空）
                         ├─> DISPUTED（任一不同；disputes.tsv 必有行）
                         ├─> UNMAPPED（三趟一致判“无落点”；note 必有理由）
                         └─> TARGET_LOST（目标节已裁撤）
PENDING ──SHA 分组───────> DUPLICATE（同哈希组非代表件；note 记代表件）
CONFIRMED/DISPUTED ─拆并> REMAP（登记后继 target_id，须非空且 active）
（DISCARDED＝裁决弃用，仅 ykla 裁决可入）
```

**验证规则**：行数==37,484；列数==16；`status` 越界值即停批；生成器二跑 diff==0。

## 实体二：title-standardization.tsv（6 列）

`relpath／old_name／new_name／change_type／sha256_before／sha256_after`。行集＝2.1b 改名件（预期 6,291：**6,118 纯反引号剥离＋173 模板名→具体 H1 名**，dry-run F2 实测）＋2.4a 补录行（change_type=outline_title_fullwidth，relpath 记 `outline.txt#L<行号>`，**168 行**——dry-run dr03 实测，替换“约 160”估计）。**派生规则（dry-run F1 规范化）**：新名＝保留现名 `编号-` 前缀＋标准化 H1 题面段＋`.md`，连字符约定不变。硬断言：非补录行 `sha256_before == sha256_after`；同目录碰撞 0；派生路径 >260 为 0（实测最长 184）。

## 实体三：title-review.tsv（语义建议，只出不改）

`relpath／current_title／suggested_title／risk(高/中/低)／reason／category(杂质名/截断短名)`。行数==21,031（7,527＋13,504）。生成期间文件名零变更。

## 实体四：path-overlong.tsv

`relpath／abs_path／length／verdict(裁决状态)`。四类扫描（>260／保留名／尾点尾空格／大小写冲突）命中全入；未裁决行对应文件不得迁移。

## 实体五：review/ 三判族

- `review/packs/<旧卷>.tsv`：24 件；列＝source_id／source_relpath／source_title／摘要标记／特殊结构。
- `review/judgments/<卷>-<子批>-{A,B,C}.tsv`：列＝source_id／target_id／reason／strategy(A|B|C)／pass_id。**三文件互无交叉引用**（NFR/契约）；strategy 与 pass_id 由脚本侧校验。
- `review/merge/<卷>-<子批>.tsv`：合并器输出（含三趟对照与最终状态）。

## 实体六：disputes.tsv

`source_id／pass_a／pass_b／pass_c／diff_summary／subtype／resolution(待裁决/维持/改判)／resolved_by`。与 mapping `DISPUTED` 行**一一对应**（双向可追溯）。**subtype（dry-run F5 新增）**：`adjacent`（同章或邻章 2:1 分裂——先导 7 例中 6 例属此型，裁决优先队列）／`empty-vs-value`（题面空趟 vs 内容趟）／`generic`（其余）。

## 实体七：checkpoints/*.json

`{task, batch, volume, sub_batch, source_id_range:[lo,hi], status_counts:{...}, input_sha256, lines, generated_at}`。续跑判据：已处理区间跳过；重跑不改变已 CONFIRMED 行。

## 实体八：mapping.duckdb（只读派生）

由 mapping.tsv 重建的统计视图（覆盖率／状态分布／目标节分布／重复统计）；**只读**——若需生产库形态，另走写库门禁（claimdb_guard＋rotate＋两处登记＋schema_meta，spec FR-007 分支）。

## 实体关系

```text
inventory.tsv ──1:1(子节)──> mapping.tsv ──N:1--> targets.tsv (target_id)
mapping.tsv ──1:N(三趟)--> judgments ──合并--> merge ──1:1(DISPUTED)--> disputes.tsv
title-standardization.tsv ──relpath──> inventory.tsv（改名前后同件）
```
