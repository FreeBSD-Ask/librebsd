# 任务书 · dragonfly_mail Phase R.2 续批（eB/gB/qB 53 条大纲回写）

> 生成时间：2026-09-13 05:40（主代理交接）。用途：供其他 AI（或下一次会话）接手执行本批大纲回写。
> 权威台账：`script/_db_row_mining/_tiering_assets/mail2d_lib_tiering.json`；流水线通则：`script/_db_row_mining/RUNBOOK_BATCH.md`。
> 姊妹文档：`_df_r2_brief.md`（R.2 首批任务书，格式与流程的原始出处）、`OUTLINE_WRITE_PROTOCOL.md`（双门禁入纲规程）。

---

## 一、任务定义

**目标**：把已落库、尚未入纲的 dragonfly_mail 候选 **53 条**（anchor `df_eB` / `df_gB` / `df_qB`，claim_id `CL-RM-016595`~`CL-RM-016647`），按“主题＋时间”双门禁逐条写入 **第 11 卷-dragonflybsd的历史** 对应子节文件末尾，形成 `ROW_MINE` 三段式幂等块；不适配者登记 mismatch 表。

**性质**：不新增史料、不改动任何既有内容、不上网、只做“库 → 大纲”的搬运与学术消化。

**上游状态**（2026-09-13 05:40 实测）：
- ① 落库已完成：53 条四表齐备（`claim`/`claim_evidence`/`evidence`/`raw_source`），`anchor='df_eB'/'df_gB'/'df_qB'`；`evidence_level='L4'`、`claim_type='FACT'`、`wording_gate='attribution_allowed'`。
- ② 回写未开始：`05-卷册大纲/第11卷-dragonflybsd的历史/` 下 **无** 任何 `CL-RM-016595`~`016647` 或对应 pk 的 `ROW_MINE` 锚点（已 grep 验证，0 命中）。
- ③ 姊妹批次参照：R.1 落库 624 条（`_df_candidates_index.jsonl`），R.2 首批已回写 76 块至 13 章 24 子节（2026-09-10，changelog 见该日 entries），本批为 R.2 第二批。

---

## 二、输入数据

| 项 | 值 |
| --- | --- |
| 主库（只读） | `04-现代研究文献/historical_claims.duckdb` |
| 源库（只读） | `03-原始史料库/11-邮件列表史料/04-dragonfly/duckdb/dragonfly_mail.duckdb` |
| 锚点分组 | `df_eB`×14（2013）／`df_gB`×15（2014）／`df_qB`×24（2008-2021） |
| 号段 | `CL-RM-016595` ~ `CL-RM-016647`（53 条，非严格连续，见清单） |
| 证据等级 | **L4**（当事人自述，过程性证据） |
| 源标识 | `SRC-rowmine:dragonfly_mail.messages.<pk>` |
| **清单（已导出）** | `script/_db_row_mining/_tmp_eBgBqB_claims.json`（53 条：anchor/pk/date/claim_id/text） |

取数 SQL（复核用）：

```sql
SELECT e.anchor, e.source_id, e.event_date, c.claim_id, c.claim_text
FROM claim c JOIN claim_evidence ce ON ce.claim_id = c.claim_id
JOIN evidence e ON e.evidence_id = ce.evidence_id
WHERE e.anchor IN ('df_eB','df_gB','df_qB')
ORDER BY e.anchor, e.event_date;
```

---

## 三、目标卷章目（第 11 卷，214-236 章；契合度判定的唯一依据）

| 章 | 主题／年份 |
| --- | --- |
| 214 | fork 公告、命名、logo、启动（2003-07） |
| 215 | Hsu 评价、外部反馈、许可证延续（2003-2004） |
| 216 | 现状、维护记录、安装器、发布工程（2003-2006） |
| 217 | 邮件列表、IRC、档案、wiki（2003-2006）【R.2 首批已写 5 块，勿重复】 |
| 218 | vkernel、userland 差异（2004-2010） |
| 219 | 1.0 发布、LWKT、SMP、1.x 演进（2003-2008） |
| 220 | 1.x 与同期 OS 比较、漏洞（2004-2008） |
| 221 | HAMMER 1.0 设计与实现（2008-2010） |
| 222 | fork 必要性批评、贡献者（2008-2010） |
| 223 | 2.x 与同期 OS 比较、漏洞（2008-2012） |
| 224 | HAMMER2 雏形、SMP 可扩展性（2011-2015） |
| 225 | 治理、Dillon 个人主导（2011-2018） |
| 226 | 3.x-4.x 技术淘汰（2012-2017） |
| 227 | 4.x 持续改进、现代化（2015-2017） |
| 228 | 4.x 架构与驱动、技术淘汰（2015-2017） |
| 229 | 4.x 漏洞与安全响应（2015-2017） |
| 230 | 5.x 现代化、HAMMER2 改进（2017-2021） |
| 231 | 6.x 现代化、持续维护（2022-2026） |
| 232 | 可持续性外部批评、贡献者（2019-2026） |
| 233 | 技术遗产：LWKT／HAMMER／vkernels |
| 234 | 激进创新哲学、社区治理、多元贡献 |
| 235 | 反批评层、再批评与合图 |
| 236 | 习俗、传言与都市传说考据 |

> ⚠️ 上表年份为章目规划区间；实务中“主题匹配”优先于“年份机械匹配”，边界条目允许落在相邻章并以裁量注留痕（先例：R.2 首批 217.1 收 2003-11 条目）。

---

## 四、初步宿主建议（**仅供参考，必须逐条实读后自行复核**）

> 铁律：`_df_r2_brief.md` §五“仅当候选与目标章主题＋时间范围同时匹配才写入”“纯个别用户环境 bug（无路线／制度意义）不写入，登记 mismatch”。
> 下表为按日期与主题的**机械预判**，执行者须读原文后判定；与预判不符者以实读为准并留痕。

### df_eB（14 条，2013 年；DragonFly 3.3-3.6 开发期）

| pk | 日期 | 主题摘要 | 预判章 | 备注 |
| --- | --- | --- | --- | --- |
| 1784 | 2013-03-10 | tuxillo 接办 dma.c 缺陷批并升级 dma 0.7 | 226 | 驱动维护 |
| 1805 | 2013-03-10 | pavalos 报 hammer cleanup 夏令时缺陷 | 226 | HAMMER 维护 |
| 1810 | 2013-04-02 | herrgard 报 ral+ndis 组合 panic | 228 | 驱动缺陷 |
| 1821 | 2013-04-08 | marino 审 world 备份补丁 | 226 | 构建工程 |
| 1834 | 2013-06-08 | josepht 报 3.5.0 AHCI panic | 226 | 内核缺陷 |
| 1849 | 2013-06-11 | marino 定位静态 TLS 空间不足（nmalloc） | 226 | 内存分配 |
| 1893 | 2013-09-18 | logan 报 IPv6 本地 DoS（OpenBSD 修堵同步） | 229 | 安全响应 |
| 1900 | 2013-09-26 | srussell 报 pf modulate 状态缺陷长尾 | 229 | 安全／pf |
| 1922 | 2013-10-20 | davshao 报 m4/gettext 构建 panic | 226 | 构建工程 |
| 1935 | 2013-10-28 | robin.carey1 分析 IBAA／urandom 初态 | 229 | 随机数／安全 |
| 1952 | 2013-11-28 | thomas.nikolajsen 报 vm_object_token 断言 panic | 226 | VM 缺陷 |
| 1953 | 2013-11-30 | t_dfbsd 报 HAMMER mirror 拷贝期 SSH 迟滞 | 226 | HAMMER／网络 |
| 1989 | 2013-12-04 | phma 卫星链路 IP 变更事务 | 226 | 网络个案 |
| 2000 | 2013-12-18 | nthery 定位 gdb 对 swapper PT_ATTACH 崩溃 | 226 | 调试器缺陷 |

### df_gB（15 条，2014 年；DragonFly 3.6-4.0）

| pk | 日期 | 主题摘要 | 预判章 | 备注 |
| --- | --- | --- | --- | --- |
| 2256 | 2014-03-07 | davshao 报 i386 Atom N270 ACPI 下 DELAY 挂死 | 227 | 平台兼容 |
| 2259 | 2014-03-08 | davshao 以 kprintf 定位两处 DELAY 阻塞 | 227 | 同上续报 |
| 2269 | 2014-04-08 | shamaz 报 IPFIREWALL+IPDIVERT+natd NAT 崩溃 | 229 | 网络栈／安全 |
| 2296 | 2014-06-01 | ftigeot 报 pkg(8) 1.2.6 过旧致 RC 镜像故障 | 227 | 发布工程 |
| 2301 | 2014-06-02 | tuxillo 征询 NFS server 消失时挂载点卡死 | 227 | NFS |
| 2311 | 2014-07-10 | dillon 给 pf pass rule 失效补丁 | 229 | pf／安全 |
| 2320 | 2014-07-24 | alexh 认领 /dev/random 读取 panic | 229 | 随机数／安全 |
| 2338 | 2014-08-08 | kaz 报 pmap_remove_pv_pte 断言 | 227 | VM |
| 2344 | 2014-08-10 | sepherosa 处理 80 核 4TB 启动失败（lapic） | 227 | SMP／硬件 |
| 2386 | 2014-09-02 | guy 报 bpf_filter mem[] 有符号整型问题 | 229 | 安全相关 |
| 2442 | 2014-11-05 | i386 官方支持终止（i915 恢复提议被否） | 226 | 架构淘汰 |
| 2485 | 2014-11-05 | lhmwzy 修 pf_table.c 无 INET6 编译错误 | 229 | 编译／pf |
| 2477 | 2014-11-21 | masu 报双 dhclient 实例吃 CPU | 227 | 网络个案 |
| 2478 | 2014-11-23 | ftigeot 修 Haswell 花屏（i915 partial revert） | 228 | 驱动 |
| 2480 | 2014-11-30 | marino 移植 NetBSD 函数支持 c++11 stoi | 227 | 工具链 |

### df_qB（24 条，2008-2021；跨 HAMMER 1 → HAMMER2 与后期维护）

| pk | 日期 | 主题摘要 | 预判章 | 备注 |
| --- | --- | --- | --- | --- |
| 9612 | 2008-07-16 | Thomas Nikolajsen 发起 HAMMER 文档规划 | 221 | HAMMER 1 文档 |
| 9742 | 2008-08-09 | dillon 发布 HAMMER 状态更新（修最后两 bug） | 221 | HAMMER 1 里程碑 |
| 9743 | 2009-03-05 | billhacker 外部初评 HAMMER 生产化阻碍 | 221 | 外部批评 |
| 9745 | 2009-03-25 | corecode 宣告 HAMMER Linux 移植启动 | 233 | 技术遗产／跨项目 |
| 9747 | 2009-04-15 | Daniel Lorch 报移植里程碑（FUSE 只读挂载） | 233 | 同上 |
| 9748 | 2009-04-16 | Jeremy Reed 移植 fuse-hammer 到 NetBSD | 233 | 跨项目 |
| 9754 | 2009-05-09 | pfg 提议 SEEK_HOLE/SEEK_DATA 支持 | 221 | HAMMER 特性 |
| 9757 | 2009-06-03 | Lorch 细问 B-Tree 定位语义 | 233 | 移植技术细节 |
| 9766 | 2010-04-04 | Lorch 发布 OS X 版 hammerread/fuse-hammer | 233 | 跨平台移植 |
| 9788 | 2014-06-02 | Peter Pokryshev 问百万文件规模稳定性 | 226 | 用户场景（可 mismatch） |
| 9792 | 2014-11-19 | Rohit Menon 报备份空间不释放 | 226 | 用户个案（可 mismatch） |
| 9802 | 2014-12-22 | Rohit Menon 报 PFS 快照目录异常 | 226 | 用户个案（可 mismatch） |
| 9813 | 2016-01-28 | Kostyrko 报 HAMMER2 空间持续减少 | 230 | HAMMER2 缺陷 |
| 9820 | 2017-09-21 | Romick 报 HAMMER2 丢 PFS | 230 | HAMMER2 缺陷 |
| 9824 | 2017-12-15 | John Shannon 报主从镜像失衡 | 230 | HAMMER 镜像 |
| 9727 | 2019-02-07 | Nima Azizzadeh 报 ipfw3 check-state 失败 | 231 | 网络／维护 |
| 9834 | 2019-11-06 | Novosyolov 问 HAMMER2 去重文档与离线去重 | 230 | HAMMER2 特性 |
| 9835 | 2019-11-07 | Novosyolov 问 HAMMER2 在 HDD 长期行为 | 230 | HAMMER2 特性 |
| 9853 | 2020-03-23 | docs 转贴 2003 年包管理之辩（Craig Dooley） | 235 | 历史转贴（可 214-216） |
| 9863 | 2020-08-17 | Moritz Systems 认领 NVMM 移植 bounty | 231 | 虚拟化／跨项目 |
| 9864 | 2020-08-31 | 网友问根式（HAMMER2 内存／UFS2 引入） | 231 | 用户咨询（可 mismatch） |
| 9870 | 2021-02-11 | tuxillo 提 sys/socket.h 缺 AF_ARP | 231 | 网络栈 |
| 9873 | 2021-03-13 | dillon 批准 AF_ARP 定义 | 231 | 同上收束 |
| 9875 | 2021-06-19 | James Cook 报 wireguard 在 DragonFly 工作 | 231 | 第三方移植 |

> 预判统计：221×5、226×7、227×6、228×2、229×5、230×5、231×8、233×4、235×1。
> 执行者可依实读结果调整；标“可 mismatch”者为纯用户环境个案，须按 §五 规则判定。

---

## 五、写入格式（严格照 R.2 首批样式，勿自创）

在目标子节文件**末尾追加**：

```
<!-- ROW_MINE: dragonfly_mail.messages.<pk> -->
**当事人自述**（证据等级：L4，来源：`historical_claims.duckdb.claim.<claim_id>`；2026-09-12 dragonfly_mail 战线 全库行级遍历考据采纳）

<yyyy 年 m 月 d 日>，<学术消化叙述，一段一行>。引用时按 L4 纪律：以上为邮件列表当事人陈述，属过程性证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

**文献**：DragonFly BSD 邮件列表档案（dragonfly_mail.duckdb.messages.<pk>）［A］
```

**规范**：
- 日期由写回脚本统一加前缀（叙述正文内不写日期）；
- 中文弯引号“”；**禁用**“”“”与英文直引号；
- 一段一行；`historical_claims.duckdb.claim.CL-RM-*` 用行间代码包裹；
- 路径／文件名／IP 加粗；手册页 **xx(N)** 加粗；裸命令不包裹行间代码；
- 叙述须以史学判断组织（**不得**直接搬运 `claim_text`），融合该章既有语气；
- 禁出现“一刻哲学”“构造哲学”等名称；
- UTF-8 无 BOM + LF；不篡改既有五字段与既有幂等块。

---

## 六、执行工序（双门禁，参照 `_df_r2_brief.md` 与 `OUTLINE_WRITE_PROTOCOL.md`）

**门 1 · 判定与亲撰**
1. 完整 Read 每条候选的源邮件正文（`dragonfly_mail.duckdb.messages`，`local_pk=<pk>`），**禁止**仅凭 `claim_text` 判定（0 信任）；
2. 按“主题＋时间”双门禁判定目标子节；不适配者登记 mismatch（理由栏）；
3. 亲撰叙述（60-130 字，史学消化，L4 纪律收尾句）。

**门 2 · 写回与记账**
4. 写回脚本命名 `_df_outline_eBgBqB_20260913.py`：`RECS` 元组 `(pk, claim_id, level, date, target_rel)`；**幂等**：目标文件已含 `ROW_MINE: dragonfly_mail.messages.<pk>` 即 SKIP（b027 教训：检测正则须与实际块标记形态一致）；
5. `--dry-run` 全绿 → `--apply`；
6. `supplement_log.jsonl` 追加（batch=`df_eBgBqB`、row_id=pk、claim_id、target、block=ROW_MINE、kind=当事人自述、level=L4）；
7. mismatch 登记 `_df_r2_mismatch_eBgBqB.md`。

**验收（四重反查）**
- ① 各目标文件 `ROW_MINE: dragonfly_mail.messages.*` 计数增量 = 写入数；
- ② 二跑 `--apply` 零追加（幂等复验）；
- ③ 新增段全角直角引号“”＝ 0、无 BOM／CRLF；
- ④ 跨文件 pk 唯一性：53 条（或实写数）无 pk 出现在 ≥2 文件。

**记账收口**
- changelog（`01-项目管理/00-变更记录/changelog.duckdb`，id = 实测 MAX+1）登记本批；
- 阶台账 `_tiering_assets/mail2d_lib_tiering.json`：dragonfly_mail 条目补“R.2 续批”进度注；
- 日记 `.workbuddy/memory/2026-09-1*.md` 追加；
- **git commit 仅本批目标文件**（消息样式：`R2 dragonfly_mail eBgBqB 写回：N 块（CL-RM-016595~016647，L4 当事人自述锚点 ROW_MINE）`）。

---

## 七、参考资产（模板直接可用）

| 用途 | 路径 |
| --- | --- |
| 本批候选清单（53 条） | `script/_db_row_mining/_tmp_eBgBqB_claims.json` |
| R.2 首批任务书（格式出处） | `script/_db_row_mining/_df_r2_brief.md` |
| 入纲通用规程 | `script/_db_row_mining/OUTLINE_WRITE_PROTOCOL.md` |
| 批次流水线通则（10 步） | `script/_db_row_mining/RUNBOOK_BATCH.md` |
| 写回脚本参考（mail2d R.2） | `script/_db_row_mining/_mail2d_outline_f_20260910.py` |
| 幂等工具（WO-007） | `00-编纂规则与格式规范/01-规则/脚本与命令/wo007_idempotency.py` |
| R.2 账目核对脚本 | `script/_db_row_mining/_df_r2_accounting.py` |
| R.2 changelog 脚本 | `script/_db_row_mining/_df_r2_changelog.py` |
| 章目与锚点核对 | `script/_db_row_mining/_df_chapter_map.py` |
| 落库脚本（已执行） | `script/_db_row_mining/_register_df_eBgBqB_20260911.py` |

---

## 八、红线

- 只读：`historical_claims.duckdb`、`dragonfly_mail.duckdb`、候选清单、目标章文件；
- 只写：目标章 md（**仅追加**）、`supplement_log.jsonl`（追加）、`_df_r2_mismatch_eBgBqB.md`；
- 禁止删除或修改任何既有内容；禁止改动五字段与既有 `ROW_MINE` 块；
- 禁止上网；禁止批量跳过实读（用户指令：文本审计必须逐条实际审核，不允许抽样）；
- 目标文件不存在时先 grep `05-卷册大纲` 确认节号，不强塞。

---

## 九、当前进度摘要（2026-09-13 05:40）

| 阶段 | 状态 |
| --- | --- |
| eB/gB/qB 候选淬炼与落库 | ✅ 完成（53 条，四表 join 53/53，CL-RM-016595~016647） |
| 候选清单导出 | ✅ 完成（`_tmp_eBgBqB_claims.json`） |
| 宿主预判 | ✅ 完成（本文件 §四，53 条机械预判） |
| 门 1（实读＋判定＋亲撰） | ⬜ 未开始 |
| 门 2（写回＋记账） | ⬜ 未开始 |
| 四重反查 | ⬜ 未开始 |
| 收口记账（changelog／台账／日记／commit） | ⬜ 未开始 |

**下一步**：从 §六 门 1 第 1 项开始，逐条实读 53 封源邮件（`dragonfly_mail.duckdb`，只读）。
