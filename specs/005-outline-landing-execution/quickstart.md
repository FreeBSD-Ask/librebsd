# Quickstart: 端到端验证指南（05 大纲落地生产执行）

**用途**: 每里程碑收口时按本指南跑断言族，全部命中即功能端到端成立。命令均在仓库根、Git Bash 下执行；Python＝`C:/Python314/python.exe`。

## 前置

- 工作树干净（`git status --porcelain` 仅预期面）；常备四件 PASS（口径同步／长线状态／元门禁／旁路备份）。
- 输入三源在位：`映射/inventory.tsv`（37,487 行）、`映射/targets.tsv`（4,304 行）、`目录/data/outline.txt`（75/523/3,705）。

## M1（Task 2 收尾）验证

```text
1. wc -l 映射/title-standardization.tsv   → 6,291＋168＋1（表头）＝6,460
2. 非补录行逐行断言 sha256_before==sha256_after（脚本）；新名保留“编号-”前缀连字符约定（DR-F1）
3. 旧树复扫六类机械违规计数 == 0（直角引号/不可见/CRLF/加粗空格/锚/重复锚 + 反引号文件名）
4. wc -l 映射/title-review.tsv == 21,032（表头＋21,031）；期间 git log 无语义改名提交
5. audit_keyword_index.py 与 audit_mirror_ingest.py 输出 PASS；映射/README.md 含冻结声明
```

## M2（Task 4）验证

```text
1. mapping.tsv：数据行==37,484；表头制表符切分==16 列；status 全 PENDING
2. target-catalog.md 与 targets.tsv 三元组逐项相等（75/523/3,705）
3. review/packs/ 文件数==24
4. 生成器二跑 diff==0（幂等）
5. _longline_status.py --check → 18 线一致；landing05 进度串含逐状态计数（不再是“未生成”）
6. 大文件提交带 APPROVED-BIGFILE:（git log -1 --format=%B 查证）
```

## M3–M4（Task 5 三判与全量）验证

```text
1. 任取已完成子批：judgments/ 下 A/B/C 三文件存在；三文件 source_id 集合相等；
   strategy 列分别恒为 A/B/C；文件内无他趟引用（grep 交叉引用为 0）
2. 守恒：八状态和==37,484（mapping.duckdb 或直数）
3. CONFIRMED 抽查：review_a/b/c 非空且三 target_id 全同；随机 30 条主题交集 0 违例
4. DISPUTED 与 disputes.tsv 行数相等（双向）
5. 任一 checkpoint 续跑演练：已处理区间输出不变
6. 先导子批分歧率实测值已落台账；>50% 时存在停盘记录
```

## M5（复核与收口）验证

```text
1. 任务复核台账.md ≥3 轮记录（卷级/全批/复验），每轮含轮次号与结论
2. 收口行含 ykla 签收标记（人工确认）
3. audit_outline_landing.py --check＋--selftest、audit_task_lifecycle.py、
   audit_gate_registry.py、audit_sidecar_backup.py 全 PASS
4. .trae spec 勾选面与生产状态一致；changelog 已记终态
5. landing05 进度串：PENDING==0
```

## 预期产物清单（收口时点）

`映射/`：mapping.tsv、target-catalog.md、title-standardization.tsv、title-review.tsv、path-overlong.tsv、review/packs×24、review/judgments/*、review/merge/*、disputes.tsv；`script/_landing_production_20261023/checkpoints/`：t2b1/t4/t5-* 族；复核与审计台账行；changelog 终态行。
