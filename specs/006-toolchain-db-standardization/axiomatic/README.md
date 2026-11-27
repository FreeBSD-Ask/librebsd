# axiomatic／公理化证明目录

**性质**：S05 实例层证明附件——对“任务书＋specs/006 包（48 件对象域）”做公理化一致性、相对充分性、相对完备性证明。本目录自身是**元层**，不计入对象域。

## 文件

| 文件 | 作用 |
| ---- | ---- |
| `公理化体系.md` | 形式系统、公理 A01—A18、定理 T1—T12、证明、诚实边界（主文） |
| `verify_axioms.py` | 机器验证器：穷举判定＋负向夹具自检（证明附件，非项目固定工具） |
| `certificate.json` | 机器可读证书（最新一次运行） |
| `verification_output.txt` | 人读证书（最新一次运行） |
| `traceability.tsv` | 目标→spec→公理→定理→证据 |
| `limitations.md` | 可证／不可证边界与失效条件 |
| `axioms.als` | Alloy 模型（复现件；未在本机运行） |
| `Axioms.tla` | TLA+ 模型（复现件；未在本机运行） |

## 运行

```bash
"C:/Program Files/Python315/python.exe" specs/006-toolchain-db-standardization/axiomatic/verify_axioms.py
"C:/Program Files/Python315/python.exe" specs/006-toolchain-db-standardization/axiomatic/verify_axioms.py --selftest
```

## 结论（2026-11-28 快照）

- **一致**：公理集可满足（18/18 PASS，模型存在）。
- **相对充分**：12 目标全部被覆盖，承载 spec 结构充分（T1/T8）。
- **相对完备**：对象域 48 件三向闭合，无孤儿／幽灵／盘外（T9）。
- 任一 spec／任务书改动即证书过期，须重跑并更新本 README 的结论行。
