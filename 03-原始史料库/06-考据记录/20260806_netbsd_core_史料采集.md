# 2026-08-06 NetBSD Core Team 治理史料全量采集考据记录

- 考据主题：NetBSD Core Team 官方邮件归档、治理架构文档、季度状态报告、MARC 交叉验证、历史争议文档的全量采集与归档
- 日期：2026-08-06
- 采集范围：
  1. `https://mail-index.netbsd.org/netbsd-announce/`（Core 官方声明与政策发布列表，1995-12 至 2026-08 全量）
  2. `https://mail-index.netbsd.org/tech-kern/`（核心内核讨论列表，1993-12 至 2026-08 全量）
  3. `https://www.netbsd.org/people/core.html`、`developers.html`（Core Team 治理架构）
  4. `https://www.netbsd.org/foundation/reports/`（季度状态报告 30 文件）
  5. `https://marc.info/?l=netbsd-announce`、`?l=netbsd-tech-kern`（第三方全文检索交叉验证）
  6. `https://www.openbsd.org/faq/faq1.html`、`https://www.netbsd.org/about/history.html`（历史争议文献）
- 归档位置：`03-原始史料库/11-邮件列表史料/02-netbsd/`（raw/mail-index/、raw/marc/、governance/）
- 数据库登记：`03-原始史料库/01-代码仓库史料/01-数据库本体/资料数据库.db` → materials 表（vol=9 ch171/172/185，vol=10 ch190）
- 大纲挂载：`05-卷册大纲/第09卷-netbsd的历史/` 第171章（171.1/171.3）、第172章（172.3）、第185章（185.2/185.3）

## 一、查证来源（一手/二手史料清单与获取方式）

### 来源 1：mail-index.netbsd.org（NetBSD 官方邮件归档，MHonArc）
- `netbsd-announce/`：Core 官方声明列表，1995-12 至 2026-08 共 369 个月份。老归档（<2008）为 oindex.html 简单 HTML 结构（`<B>Subject:</B>`/`<B>Date:</B>` 标签，日期格式 `MM/DD/YYYY HH:MM:SS`）；新归档（2008+）为 MHonArc v2.6.x 结构（`date1.html` 索引 + `msgNNNNN.html` 单封，含 `<!--X-Message-Id: -->`、`<!--X-Date: -->` 标准 RFC822 注释头）
- `tech-kern/`：核心内核讨论列表，1993-12 至 2026-08 全量（约 394 个月份，数万封）
- 获取方式：`script/_mail_fetch_netbsd_core.py`（urllib + ssl.CERT_NONE 规避 Windows Schannel CRL 吊销检查失败；逐月索引 → 逐封解析 → 组装标准 RFC822 mbox；新抓 mbox 日期已标准化为 RFC2822 格式，Message-ID 缺失时用 `no-id-<list>-<yyyy><mm>-<day>-<msgid>` 兜底保证唯一）
- 存档：`raw/mail-index/<list>/<YYYY-MM>.mbox`

### 来源 2：netbsd.org/people/（Core Team 治理架构官方文档）
- `core.html`：NetBSD Core Group 现任 7 名成员（Christos Zoulas、Chuck Silvers、Martin Husemann、Matthew Green、Rin Okuyama、Robert Elz、Taylor R. Campbell）+ 历任成员 22 人（含 Theo de Raadt、Jason Thorpe、Charles Hannum、Adam Glass、Chris Demetriou、Christos Zoulas 等早期核心成员）
- `developers.html`：NetBSD 开发者管理规则与 committer 名单（103KB）
- `formal.html`：旧版正式规则页，2026-08 已 404（失效网址，按考据规则标注）
- 获取方式：`script/_mail_fetch_governance.py`，存档 `governance/*.html`

### 来源 3：netbsd.org/foundation/（Foundation 治理与报告）
- `bylaws.html`：Foundation 章程全文（84KB，Article I-XIV）
- `reports/`：季度状态报告档案馆，共 30 文件（2003 年报、2004-2007 各季报 Q1-Q4、2010 年报、2025 年度大会纪要；HTML/XML/TXT 三格式）
- `press/`：Press Releases 18 条
- `policies/`：Policies 4 件
- 获取方式：`script/_mail_fetch_reports.py`，存档 `governance/reports/`

### 来源 4：marc.info（第三方全文检索邮件库）
- `?l=netbsd-announce`：1998-10 至 2026-08（272 个月份）
- `?l=netbsd-tech-kern`：1998-2026
- MARC 提供标准 RFC822 单封下载（`?l=X&m=<id>&q=mbox`），含完整 Message-Id 头，用于与官方归档交叉验证
- 获取方式：`script/_mail_fetch_marc_netbsd.py`，存档 `raw/marc/<list>/<YYYY>.mbox`

### 来源 5：历史争议文献
- `openbsd.org/faq/faq1.html`：OpenBSD 官方 FAQ 简介（17.5KB）
- `netbsd.org/about/history.html`：NetBSD 官方发展史（47.6KB，含创立者名单与 BSD 谱系图）
- `netbsd.org/releases/formal.html`：正式版本历史（22KB，NetBSD 0.8 1993-04-20 起）
- 存档 `governance/history/`

## 二、交叉验证方法（多源对比路径）

1. **netbsd-announce 全量 vs MARC 抽查**：官方 mail-index 与 MARC 对 1998-2026 年月度消息量对照，验证官方归档完整性
2. **老归档（<2008）vs 新归档（2008+）格式**：老归档 MHonArc 简化 HTML（无 Message-ID），新归档 MHonArc v2.6 含标准头注释；两套结构逐月消息数对照，验证无遗漏
3. **Core Team 成员名单**：core.html 现任/历任名单 ↔ 171.3 节考据（Adam Glass 1994-12-23 通知邮件）↔ OpenBSD faq1/history 交叉验证 Theo de Raadt 离开事件
4. **Foundation 报告**：reports/ 各季度报告 ↔ 185.2 节考据记录（501(c)(3) 免税地位 2004-01-22、董事会选举）
5. **CVS-to-Mercurial 迁移存疑验证**：185.3 节标注"2019-2020 各月存档未发现迁移完成公告"，本次 netbsd-announce 全量抓取（含 2019-2020 各月 mbox）可对查证路径提供完整本地档案复核

## 三、存疑判定依据

1. **formal.html 失效**：`netbsd.org/people/formal.html` 2026-08-06 返回 404，属新版网站改版移除；按失效网址规则处理，用 `releases/formal.html` 替代（旧版本历史页面，收录于 governance/history/netbsd-formal.html）
2. **老归档日期解析缺陷修复**：旧 mbox（1994-2007）为精简拼装格式，`Date: MM/DD/YYYY HH:MM:SS` 无法被 `email.utils.parsedate_to_datetime` 解析，导致原入库 tech-kern 38192/38193 条 date 为 NULL；本次新抓取已统一标准化为 RFC2822 日期，入库脚本 `_mail_ingest_v2.py` 增加 `MM/DD/YYYY HH:MM:SS` 与 MHonArc 注释两种日期格式兼容解析
3. **MARC 覆盖起点**：MARC 的 netbsd-announce 仅从 1998-10 开始（无 1995-1997），官方 mail-index 已覆盖 1993-2026 全量；MARC 定位为交叉验证源而非主源
4. **Core Team 内部投票记录**：`<core@NetBSD.ORG>` 私有列表存档不公开，撤权决议投票记录无法从公开渠道取得（沿用 185.3 节存疑结论）

## 四、产出清单

| 产出 | 位置 | 说明 |
|------|------|------|
| netbsd-announce mbox | `raw/mail-index/netbsd-announce/` | 1995-12 至 2026-08 全量 |
| tech-kern mbox | `raw/mail-index/tech-kern/` | 1993-12 至 2026-08 全量（统一 RFC822 格式） |
| MARC mbox | `raw/marc/` | netbsd-announce 1998-2026 交叉验证 |
| 治理文档 | `governance/` | core/developers/foundation 系列 |
| 季度报告 | `governance/reports/` | 30 文件 |
| 历史文档 | `governance/history/` | faq1/history/formal |
| 邮件库 | `netbsd_mail.db` | netbsd-announce/tech-kern 消息入库 |
| 材料登记 | `资料数据库.db` → materials | 9 条 vol=9/10 治理史料 |
