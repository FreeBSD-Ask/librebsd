# 交接文档：邮件列表史学观点逐节增补（V2）

> 任务目标：为《给我自由——一部 BSD 史》全书 19 卷的**子节 `.md` 文件**逐节增补「邮件列表史学观点」区块（`MAIL_INSIGHT`）。
> 本文件是给下一个 AI/执行者的交接说明，含进度、待办、史料库、写入规范、已验证脚本。

---

## 一、总体进度（截至交接时点）

统计口径：非「index.md / 概述.md / 00-总览.md / 卷末书目述评.md」的章内 `.md` 视为「子节文件」。

| 卷 | 主题 | 子节数 | 已写子节 | 观点条数 | 状态 |
|---|---|---|---|---|---|
| 01 | UNIX 的起源 | 155 | 121 | 208 | ✅ 完成 |
| 02 | 伯克利的岁月 | 158 | 92 | 126 | ✅ 完成 |
| 03 | 伯克利学术文化外溢 | 65 | 51 | 150 | ✅ 完成 |
| 04 | 大分裂与四大 BSD | 162 | 36 | 59 | ⚠️ 进行中（第62-69、80-87章未写） |
| 05 | FreeBSD 工程化奠基 | 194 | 0 | 0 | ❌ 未开始 |
| 06 | FreeBSD 核心技术革新 | 147 | 0 | 0 | ❌ 未开始 |
| 07 | FreeBSD 工程体系重构 | 92 | 0 | 0 | ❌ 未开始 |
| 08 | FreeBSD 范式转换 | 89 | 0 | 0 | ❌ 未开始 |
| 09 | NetBSD 的历史 | 115 | 0 | 0 | ❌ 未开始 |
| 10 | OpenBSD 的历史 | 164 | 0 | 0 | ❌ 未开始 |
| 11 | DragonFlyBSD 的历史 | 118 | 0 | 0 | ❌ 未开始 |
| 12 | macOS 的 BSD 遗产 | 96 | 0 | 0 | ❌ 未开始 |
| 13 | BSD 衍生操作系统 | 79 | 0 | 0 | ❌ 未开始 |
| 14 | 商业生态与企业案例 | 105 | 0 | 0 | ❌ 未开始 |
| 15 | 许可证哲学与法律 | 118 | 0 | 0 | ❌ 未开始 |
| 16 | 开源运动与合规治理 | 109 | 0 | 0 | ❌ 未开始 |
| 17 | 政治制度与社区治理 | 53 | 0 | 0 | ❌ 未开始 |
| 18 | 全球社区地区 BSD 史 | 241 | 0 | 0 | ❌ 未开始 |
| 19 | BSD 史编纂学 | 5 | 0 | 0 | ❌ 未开始 |
| **合计** | | **2265** | **300** | **543** | |

---

## 二、待办任务（按优先级）

### 1. 第 04 卷补完（最高优先级）
第 62-69 章、第 80-87 章尚未写入（批 A、批 C 子代理结果丢失，需重派）。

**第 04 卷剩余章节目录**（`d:\librebsd\05-卷册大纲\第04卷-大分裂与四大bsd的诞生\`）：
- 第62章-386bsd的诞生与bill-jolitz的移植工程
- 第63章-386bsd时代的法律诉讼与反向工程先例
- 第64章-386bsd的衰落与patchkit分叉争议
- 第65章-freebsd的创建与patchkit协调人
- 第66章-freebsd10的安全基线与20迁移
- 第67章-netbsd的创建与可移植理想
- 第68章-netbsd的贡献者与de-raadt被驱逐事件
- 第69章-openbsd的起源与de-raadt被netbsd逐出
- 第80章-linux与bsd的跨阵营对话者
- 第81章-linux与bsd的命运分化比较
- 第82章-44bsd-lite的发布与法律清白基础
- 第83章-unix版权归属争议与novell卖sco
- 第84章-分裂时期的文化图景与三项目基因分化
- 第85章-分裂时期的流行文化呈现
- 第86章-分裂时期文化叙事的批评与反思
- 第87章-stallman左派黑客政治与bsd商业化分歧

### 2. 第 05-19 卷推进（按卷序）
每卷按「章」拆分，用并行子代理分批处理（每批约 6-10 章、50-100 子节为宜）。

**注意**：第 04 卷批 B（第70-79章）已写 59 条；批 A（62-69）、批 C（80-87）尚未写。交接者应**先验证磁盘实际状态**再派发（见下方验证脚本），避免重复写。

---

## 三、史料数据库清单

### 1. Usenet 库（1981 年起，最核心一手史料）
路径：`d:\librebsd\03-原始史料库\11-邮件列表史料\07-usenet\duckdb\usenet_mail.duckdb`
表：`messages(id, list_id, message_id, subject, from_name, from_email, date, year, body, ...)`、`lists(id, list_name, ...)`
JOIN：`messages.list_id = lists.id`
重点新闻组：`comp.unix.wizards`、`comp.bugs.4bsd`、`comp.org.usenix`、`comp.unix.bsd`、`comp.unix.bsd.bsdi.*`、`comp.os.386bsd.*`、`comp.sys.sun`、`unix.bsd`

### 2. FreeBSD 库（1994 年起）
路径：`d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\`（多个 `freebsd-*.duckdb`，如 freebsd-hackers、freebsd-current、freebsd-arch、freebsd-chat、freebsd-java 等）

### 3. NetBSD 库（1993 年起）
路径：`d:\librebsd\03-原始史料库\11-邮件列表史料\02-netbsd\db\`（port-*、netbsd-help、netbsd-announce 等）

### 4. OpenBSD 库（1995 年起）
路径：`d:\librebsd\03-原始史料库\11-邮件列表史料\03-openbsd\duckdb\openbsd_mail.duckdb`

### 5. 已挖掘产物
- `d:\librebsd\script\_mine_result.json`（bikeshed 词源、guru、flame war、功劳归属、daemon 命名等）
- `d:\librebsd\script\_mine_geopolitics_result.json`（Murray Hill、Lions book、USENIX 会议、DARPA/NSF 等）
- `d:\librebsd\script\_mine_fulltext.json`（重点邮件全文）

---

## 四、写入格式（V2，严格遵守）

在子节 `.md` 文件**末尾**追加（先 `Read` 全文，若已有 `<!-- MAIL_INSIGHT:` 标记则跳过该 message_id）：

```markdown
<!-- MAIL_INSIGHT: <message_id> -->
**观点**：<1-3句中文史实陈述，含具体人名、时间、事件，蒸馏为史学陈述而非邮件原文照搬>
**邮件来源**：<发件人>，<新闻组/列表名>，<日期>，Message-ID: `<id>`
**史学意义**：<1-2句论证该史料为何重要>
<!-- /MAIL_INSIGHT -->
```

### 硬性规则
1. 每子节 1-3 条；**无实质邮件史料匹配的子节跳过**，不硬凑，并在报告中登记跳过原因
2. 蒸馏为史学陈述，禁止照搬原文（英文关键词短语可保留）
3. 去重：同一 `message_id` 全项目不重复
4. **禁止删除或修改既有内容**（只做末尾追加）
5. 中文引号「」禁用，统一用“”；一段一行；UTF-8 无 BOM；LF 换行
6. 日期噪声（epoch 边界 1969-12-31、1980-01 误解析）只写可靠年份，引用前用 SQL 回查 `raw_headers` 复核
7. 优先 1981-1990 Usenet 早期邮件（当事人当时代）；后人回顾须注明「事后回顾」

---

## 五、执行方法论（子代理通用 prompt 骨架）

1. **先盘点**：用 `LS`/`Glob` 确认章目录下实际 `.md` 文件名（子节文件 vs index/概述，只写子节文件）
2. **检索**：写 Python 脚本用 `duckdb` 按子节主题关键词查各库；先 `PRAGMA` 看表结构再查
3. **蒸馏**：逐条 Read 命中邮件正文，蒸馏为史学陈述
4. **写入**：用 `SearchReplace` 或文件追加，附加到子节末尾
5. **验证**：脚本校验格式（BOM=False、CRLF=0、`<!-- /MAIL_INSIGHT -->` 闭合、中文引号规范、message_id 去重）

---

## 六、已验证/可复用脚本（位于 `d:\librebsd\script\`）

### 进度统计（直接复用）
- `_progress_all.py` — 全 19 卷进度汇总（子节/已写/观点数）
- `_verify_vols.py` — 按卷号验证：`python _verify_vols.py 4 5 6`
- `_verify_vol.py` — 单卷验证
- `_count_vols2.py` — 卷章节规模统计

### 史料库探查（直接复用）
- `explore_usenet_db.py` / `explore_usenet_schema.py` — Usenet 库 schema 与内容探查
- `probe_usenet_keywords.py` / `probe_usenet_schema.py` — 关键词命中探查
- `explore_mail_dbs_v4ch80_87.py` — 第 04 卷 80-87 章邮件库探查（已存在，可直接参考其查询逻辑）

### 写入/验证模板（可直接参考改造）
- `append_mail_insights_20260829.py` / `append_mail_insights.py` — 追加写入模板
- `_write_mail_insights_v2.py` / `write_mail_insights_v2.py` — V2 格式写入
- `verify_mail_insight_v2_20260828.py` — V2 格式校验模板
- `_verify_encoding_20260830.py` — 编码/引号/BOM/CRLF 校验

### 已用搜索脚本（可参考其 SQL 关键词逻辑，勿重复跑写）
第 01-04 卷已写入，`script/` 下大量 `mail_insight_*`、`search_usenet_*`、`usenet_*`、`batch*` 脚本为历史执行痕迹，**交接者只需参考逻辑，不要重新执行已覆盖章节的写入**。

---

## 七、风险与注意事项

1. **子代理结果偶发丢失**：本任务历史中出现多次「子代理返回 missing 但实际已写盘」或「返回 done 但实际未写盘」的情况。**每次派发后必须用 `_verify_vols.py` 回查磁盘实际状态**，不要仅凭子代理回报判断。
2. **覆盖边界**：Usenet 库始于 1981 年，1981 年前的事件（如 1977 Fabry、1978 1BSD、1956 同意令等）无一手邮件，跳过是正确做法，不要硬凑。
3. **第 04 卷 62-69 章重点关键词**：386BSD / patchkit / Jolitz / FreeBSD 创建（Nate Williams、Rod Grimes、Jordan Hubbard）/ NetBSD 创建（Demetriou、Glass、Hannum、Theo）/ OpenBSD 分叉（Theo de Raadt 被逐出 NetBSD core，1994-1995）。
4. **第 04 卷 80-87 章重点关键词**：Linux vs BSD / 4.4BSD-Lite 发布 / Novell-SCO Unix 版权 / Stallman / GPL vs BSDL。
5. **第 05-19 卷建议每卷检索关键词映射**：
   - 第05卷 FreeBSD 工程：ports、jails、kqueue、jemalloc、pf、SMP、Foundation
   - 第06卷 技术革新：ZFS、CDDL、DTrace、Capsicum、CHERI、bhyve、pkgng、clang
   - 第07卷 工程重构：安全模型、网络栈（SACK/netmap/iflib）、GPLv3、许可证纯洁化
   - 第08卷 范式转换：systemd、Rust、Git 迁移、安全公告
   - 第09卷 NetBSD：pkgsrc、port-*、嵌入式、SMP、ZFS
   - 第10卷 OpenBSD：pf、pledge、unveil、OpenSSH、LibreSSL、安全哲学
   - 第11卷 DragonFly：HAMMER、HAMMER2、LWKT、vkernels、Matt Dillon
   - 第12卷 macOS：NeXTStep、Darwin、APSL、UNIX03 认证、GCD/libdispatch、Apple Silicon
   - 第13卷 衍生 OS：TrueNAS、pfSense/OPNsense、JunOS、PlayStation、Netflix、PC-BSD/TrueOS
   - 第14卷 商业生态：基金会资助、商业用例、BSDL vs GPL
   - 第15卷 法律：BSD 许可证、GPL、加密出口管制、SCO/Unix 归属
   - 第16卷 开源合规：FSF/OSI、Apache、Common Criteria、社区治理
   - 第17卷 政治制度：daemon 词源、基金会治理、美国政治制度
   - 第18卷 全球社区：各国 BSD 社区（美/欧/中/日/韩/俄/中东/非/南美等）
   - 第19卷 编纂学：史观自反、叙事批判（此卷为史学理论，邮件史料匹配率极低，大概率大量跳过）

---

## 八、交付验收标准

每个子代理批次完成后，交接者应：
1. 跑 `python _verify_vols.py <卷号>` 确认写入数量
2. 抽查 2-3 个子节文件，确认：V2 三字段齐全、中文引号规范、无 BOM、LF、Message-ID 反引号包裹、未改动既有内容
3. 汇总「写入条数 + 跳过清单 + 关键史料发现」至最终报告
