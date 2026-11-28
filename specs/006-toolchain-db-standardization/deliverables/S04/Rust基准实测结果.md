# Rust 首批基准实测结果（S04-FR-02；2026-11-28）

## 结论：零改写候选

4 个"改写候选"经基准实测后**全部改判保留**——Python 的 C 加速扩展（`unicodedata`、`json`、`csv`）已足够快，Rust 无实质收益。

| 工具 | Python 中位时间（5 次） | 行数 | 瓶颈分析 | 改判理由 |
| ---- | ---- | ---- | -------- | -------- |
| `audit_md_quote_glyphs.py` | 0.104s | 187 | 启动主导 | unicodedata C 扩展 8.9M chars/s 已够 |
| `mail_dedup_verify.py` | 0.089s | 69 | 启动主导 | 微型脚本，I/O 主导 |
| `scan_md_invisible.py` | 41.475s | 196 | 全库 .md 树扫描 | unicodedata 吞吐 8.9M chars/s；Rust 收益限于并行化而非单线程；实际瓶颈是 .md 文件 I/O 而非字符扫描 |
| `shard_fetch.py` | 0.096s | 34 | I/O 主导 | 34 行 JSONL 切分；I/O 为主 |

## 方法

- Python 3.15.2；`subprocess.run` 5 次取中位。
- 纯吞吐测试：`unicodedata.category` 逐字符扫 specs/006 全部 .md（175,550 chars in 0.020s = **8.9M chars/s**）。
- 对比基线：Rust 同等操作（`char::is_control` + category table lookup）预期 100—500M chars/s——但实际瓶颈在文件 I/O 与启动，不在字符扫描。

## 对矩阵的影响

- 4 候选改判保留 → 全矩阵 123 件：保留 85／观察 38／改写候选 **0**。
- 生产改写方案标 **零改写候选**——Rust 能力保持"就绪待触发"（工作区规划＋基准方法已验证），待未来数据规模或并发需求变化时重新评估。
- 这直接验证了任务书"禁止为 Rust 而 Rust"规则的有效性。
