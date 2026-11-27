# contracts/ — 接口契约（login 判定入藏战役）

本战役的"接口"＝三个写入契约（判定台账 JSONL、claim 库三层入藏、05-大纲注入块）。详细字段见 [../data-model.md](../data-model.md)；本目录文件按契约逐一定稿。

- [ledger-contract.md](ledger-contract.md) —— 判定台账 JSONL 行契约（断点与幂等键）
- [claim-ingest-contract.md](claim-ingest-contract.md) —— claim 库三层入藏契约（raw_source/evidence/claim/source_chapter）
- [outline-inject-contract.md](outline-inject-contract.md) —— 05-大纲 ROW_MINE 注入块契约（WO-007 幂等＋证据等级门禁）
