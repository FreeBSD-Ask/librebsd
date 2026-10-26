# 数据前置落账小结（Task 2）

- mapping 行数：37484；状态：PENDING 10127／DISPUTED 6434／UNMAPPED 20923
- 16 条章级：改判节级 13／转 UNMAPPED 1／待复核 2（后 2 条转 Task 3）
- disputes 行数：6482；7 列 100%；source_id 唯一
- DISPUTED 缺失台账：0；历史行：48（47＋S-002792）
- 459 补录：459；48 条历史行 resolution 已补

生成器：`script/_reassign_20261026/p01_apply_prereq.py`；输入 12／13／14 号件。
