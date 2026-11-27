# Linux kernel coding style（现行官方文档）（新 ref）引用卡

- **性质**：kernel.org 现行 `Documentation/process/coding-style.rst` 的 HTML 版（`www.kernel.org/doc/html/latest/process/coding-style.html`）；Chrome UA curl 200、102,354 B（2026-11-27 实抓）。
- **source_url**：https://www.kernel.org/doc/html/latest/process/coding-style.html
- **quote（逐字，一处；官方页弯引号照录）**：

For symbol names and documentation, avoid introducing new usage of ‘master / slave’ (or ‘slave’ independent of ‘master’) and ‘blacklist / whitelist’.

- **考据注**：现行条文把 master/slave 与 blacklist/whitelist 成对列入，并给出替换建议表与例外（用户态 ABI／既有硬件规格）。与 v1 只列 slave／blacklist、Lutomirski 追问 whitelist 的帖链对照，可证替换范围扩大的终态。官方文档为活页，引用以 2026-11-27 抓取版为准。
- **证据等级**：项目官方文档（L3）。
- **本批落点**：V18.1.6.4／1.6.6（supp-V18-b003）
- **考据日期**：2026-11-27（supp-V18-b003；official_doc／L3）
