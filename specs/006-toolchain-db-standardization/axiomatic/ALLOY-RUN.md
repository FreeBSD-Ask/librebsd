# Alloy 6.2.0 真机检回执（2026-11-28）

## 运行

```bash
# 工具：Alloy 6.2.0（org.alloytools.alloy.dist.jar，21,062,377 B）＋ Java 27（Zulu）
cd _tmp/alloy
java -jar alloy.jar exec axioms.als
```

## 结果（三连）

| 命令 | 类型 | 结果 | 含义 |
| ---- | ---- | ---- | ---- |
| `run Default` | run | **SAT**（1/1 实例，620ms，solver=sat4j） | 公理集**可满足**——模型存在（相对一致性机检） |
| `check T1_充分性` | check | **UNSAT** | 无反例——充分性断言在给定域内成立 |
| `check T2_无孤儿` | check | **UNSAT** | 无反例——无孤儿断言在给定域内成立 |

域：exactly 12 Goal / 13 Spec / 13 Binding / 39 Artifact / 4 Heading / 4 Version / 3 Kind / 4 Status。

## 回执

- `alloy-run/receipt.json`：三命令的机器可读回执（Default 含完整 SAT 实例）。
- `alloy-run/Default-solution-0.md`：SAT 实例的人读呈现。

## 与 Python 穷举证书的关系

- Python 穷举（`verify_axioms.py`）：证明**实际仓库快照**满足全部公理（实例层）。
- Alloy 本件：证明**公理集本身**在给定有穷域内可满足且两条核心断言无反例（层内一致性）。
- 两层互补：Alloy 过 ≠ 快照过；快照过 ≠ 层内一致。两者 2026-11-28 均 PASS。

## 修复记录

1. `Status` 需 abstract＋one extends（初版漏）。
2. A05 join 方向改为 `s.~of.kind & specMd`（初版 `artifacts.of.s` 方向错）。
3. 命令需显式给 `Kind`/`Status` 作用域。
4. 删除未约束死字段 `Spec.artifacts`（首跑 SAT 实例暴露其恒空）。
