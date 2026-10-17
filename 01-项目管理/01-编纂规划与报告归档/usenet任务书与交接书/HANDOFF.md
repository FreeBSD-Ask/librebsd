# 数据库行级遍历工程 · 交接文档（HANDOFF）v4

更新时间：2026-08-31（第四版：Phase 2A 功能库 14/14 收官）
Spec：`.trae/specs/db-row-traversal-mining-2026-08-29/`（spec.md / tasks.md / checklist.md）
工作区：`script/_db_row_mining/`（所有临时脚本与中间产物，规则要求保留不清理）

***

## 一、工程目标与方法论铁律

对全部 317 个 DuckDB 数据库做“行级遍历资源挖掘 + 数据挖掘 + 考据”，按规则入库（historical\_claims 等）或入大纲（05-卷册大纲 5 字段）。

**铁律（不可违反）：**

1. 禁止用关键词（FTS/LIKE）筛行或跳过数据；分页只允许主键/rowid 边界谓词。
2. 禁止脚本自动分类、自动提炼、自动写入；候选提炼、考据判定、写库、写大纲均须逐条执行、逐条复核。
3. 源库全程只读（duckdb.connect(read\_only=True)）。
4. 逐条写入，写前复核（quote 与源行同串）、写后复核（反查命中）；同源行多主张时 raw\_source 复用不重复插入。

**证据等级方向（库内 L5 最强 → L1 最弱）：**

- L5 代码证据（commit/版权头链/\_\_FBSDID）→ decisive，可写继承不得扩大到代码外

- L4 当事人陈述（邮件/访谈/公告）→ strong，可写影响须归源限定

- L3 文档/论文明确记载 → strong

- L2 强技术对应缺直接证明 → contextual，只许“传承待证”

- L1 仅相关性相似 → contextual，禁止继承/影响表述

**claim\_evidence 词表（必须）：** role=`supporting`；strength=L5=`decisive`、L4/L3=`strong`、L2/L1=`contextual`（禁用 medium/weak/supports）。

***

## 二、当前总进度

**累计入库主张：68 条**（CL-RM-000001~~000020、000401~~000403、000501~~000520、000601~~000606、000701~~000714、000801、000901~~000904）

### Phase 2A 功能库 14 库状态

| 库                             | 状态                                                                                 | 主张段                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------- |
| causal\_graph(27行)            | ✅                                                                                  | 000001 批                                             |
| fact\_checks(81)              | ✅                                                                                  | 000001 批                                             |
| review\_reports(254)          | ✅                                                                                  | 000001 批                                             |
| phoronix\_news(874)           | ✅                                                                                  | 000007\~020                                          |
| changelog(929)                | ✅                                                                                  | 000801（FreeBSD 1.0 1993-11-01）                       |
| original\_sources(1320)       | ✅                                                                                  | 000601\~606                                          |
| cross\_indexes(3090)          | ✅                                                                                  | 000501\~520                                          |
| sacred\_sources(3984)         | ✅                                                                                  | 000401\~403                                          |
| doubts\_standalone(5799)      | ✅                                                                                  | 000701\~714                                          |
| metadata\_interfaces(10066)   | ✅                                                                                  | 0 条（映射型内容）                                           |
| 资料数据库(44702)                  | ✅                                                                                  | 000901\~904 + findings\_资料数据库.json（materials 万条缺口清单） |
| historical\_claims(121542)    | ✅ 自审读（词表修复 587 条 + 缺口清单 audit\_gaps\_historical\_claims.json）                      | 修复记录                                                 |
| research\_notes(507166)       | ✅ blocks 486894 行判定收口（6 条主张 CL-RM-001501\~1506：L5 漏洞群统计×3 + 中国 GPL 判例×3，风灵案案号联网补全） | 001501\~1506                                         |
| references\_fulltext(1058838) | ✅ 13 表判定收口（5 条主张 CL-RM-002001\~2005：chroot 1982-03-18 L5 + 引用链防错×2 + 引语定位×2）       | 002001\~2005                                         |

**Phase 2A 功能库 14/14 全部收官**（类别级收官考据：03-原始史料库/06-考据记录/20260831\_功能库行级遍历类别级收官考据.md；52 张关键表 progress 全绿）。

### 其余 Phase 状态

- Phase 2B 播客 10 库：⏳ 预研完成（蓝图见 review\_logs/\_phase2b\_blueprint.md：episodes 索引登记型 \~1000 行已过目 bsdtalk 264 集核心人物访谈索引；transcripts 638 集 L4 矿藏逐集判级待做；id 段 003001）

- Phase 2C 代码仓库 11 库：⬜（commits 等关键表 70.1M 行，工程量最大）

- Phase 2D 邮件 282 库：⬜（messages 21.7M 行）

- Phase 3 大纲增补：⬜（可先行——主张库已具规模，79 条 row\_mine 主张可供筛选）

- Phase 4 收尾：⬜

***

## 三、已就绪资产与使用方法

| 文件                      | 用途                                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| db\_catalog.json        | 317 库四类编目（功能 14/代码 11/播客 10/邮件 282）                                                                           |
| key\_tables.json        | 1414 表判定（关键 705/辅助 622/空 87），含 row\_count                                                                     |
| read\_page.py           | 只读分页：`python read_page.py --db <路径> --table <表> --pk rowid --after "[N]" --limit 50 --out <jsonl>`（禁 --where） |
| progress.py             | `page`（登记）/`report`（覆盖率）/`resume`（断点）                                                                         |
| candidate\_helpers.py   | 候选契约 + EVIDENCE\_LEVEL\_DB + id 生成                                                                            |
| dedup\_index.json       | 既有块指纹 26774 条 + claim\_hash 基线                                                                                |
| reader\_exec\_log.jsonl | 读取器执行审计日志                                                                                                     |

***

## 四、id 段分配表（避免冲突）

| 库                                       | evidence/claim 段    | 已用       |
| --------------------------------------- | ------------------- | -------- |
| 首批（causal/fact\_checks/review\_reports） | 000001\~000020      | 至 000020 |
| phoronix\_news                          | 000007\~000020      | 同上批      |
| sacred\_sources                         | 000401\~000499      | 至 000403 |
| cross\_indexes                          | 000501\~000599      | 至 000520 |
| original\_sources                       | 000601\~000699      | 至 000606 |
| doubts\_standalone                      | 000701\~000799      | 至 000714 |
| changelog                               | 000801\~000899      | 至 000801 |
| 资料数据库                                   | 000901\~000999      | 至 000904 |
| historical\_claims 自审（建议）               | 000951\~ 改 001001\~ | 未用       |
| research\_notes（建议）                     | 001501\~            | 未用       |
| references\_fulltext（建议）                | 002001\~            | 未用       |
| 播客（建议）                                  | 003001\~            | 未用       |
| 代码仓库（建议）                                | 004001\~            | 未用       |
| 邮件（建议）                                  | 010001\~            | 未用       |

当前库内 max：EV-RM-000904 / CL-RM-000904。

***

## 五、已修复的坑（务必先读）

1. **claim\_evidence 词表**：首批曾用 role=supports/strength=medium，已修正为 supporting/strong（脚本 \_fix\_claim\_evidence.py）。
2. **同源行多主张 raw\_source 冲突**：sacred\_sources.blocks.3177 曾重复插入，已修复；写库脚本 \_write\_claims\_batch3.py 已内置同源复用逻辑（推荐直接复用该脚本，改 FILES 列表即可，幂等跳过已存在 claim\_id）。
3. **证据等级方向**：库内 L5 最强 L1 最弱，与直觉相反。
4. **pledge(2) 版本**：首现于 OpenBSD 5.9（tame 更名），已联网三源核验修正。
5. **子代理通道不稳定**：本会话 Task 子代理连续 5 次返回空且无产出；实际产出以磁盘文件为准核验（勿重复读取已读数据）；必要时主会话亲自执行（本会话后半段即为此模式）。
6. **dump 文件复用**：doubts\_standalone（_dump\_doubts_*.jsonl）、changelog（\_pg\_chg\_p1\~19.jsonl）、original\_sources（*_pg\_os_.jsonl）、cross\_indexes（_pg\_ci_\*.jsonl）已全量 dump，可直接消费避免重复连库。
7. **changelog.duckdb 无自增**：写入前先 `SELECT COALESCE(MAX(id),0)+1`，date+entry\_order 联合排序，去重检查（同日 summary 前 60 字符）。

***

## 六、考据记录与 changelog 已写

- 03-原始史料库/06-考据记录/20260829\_全量数据库行级遍历编目考据.md（Phase 0）

- 03-原始史料库/06-考据记录/20260829\_功能库小库行级遍历考据.md（首批 3 库）

- 03-原始史料库/06-考据记录/20260829\_功能库第二批行级遍历考据\_metadata.md

- 03-原始史料库/06-考据记录/20260829\_功能库第二批考据\_cross\_os.md（cross\_indexes 20 条 + original\_sources 6 条，含判例联网核验 URL）

- 03-原始史料库/06-考据记录/20260829\_功能库第二批考据\_doubts\_changelog.md

- changelog.duckdb：id=955（Phase 0 编目）、956（cross/os 26 条）、957（doubts/changelog 15 条）

review\_logs/ 已写 10 库日志（causal\_graph/fact\_checks/review\_reports/phoronix\_news/sacred\_sources/metadata\_interfaces/cross\_indexes/original\_sources/doubts\_standalone/changelog）。

***

## 七、下一步执行入口（接手者直接照做）

1. 读 `tasks.md` 勾选状态与 `checklist.md` 验收口径。
2. `python script/_db_row_mining/progress.py report` 看覆盖率。
3. **P1：research\_notes**（04-现代研究文献/research\_notes.duckdb：blocks 486894 + cross\_references 18441）——**预研结论**：block\_type 分布 json\_node 368657（结构节点，按 metadata\_interfaces 先例判登记型，抽样核验即可）、paragraph 37376/list\_item 30176/quote 4446/footnote 21 为叙述层（≈7.2 万行，价值核心，逐批判级）、长文本（>200字）36629 行、heading/frontmatter/csv\_row/table\_row/code\_block 为结构元数据；cross\_references 18441 行为 markdown\_link 引用登记（多为 pending 导航链接，登记型）。**执行方式**：先写 dump 脚本（按 block\_type 分组分页导出 paragraph/list\_item/quote 三类到 _pg\_rn_\*.jsonl，每批 500 行），逐批判级，候选入 candidates\_research\_notes.jsonl，id 段 001501。
4. **P2：references\_fulltext**（fulltext\_blocks 992226 等 10 表）——同上模式；id 段 002001。
5. **P3：Phase 2B/2C/2D**（播客/代码/邮件，邮件为最重部分）。
6. **P4：Phase 3 大纲增补**——最严门禁：逐条学术性+契合度双门禁复核，禁机械/批量写入，`<!-- ROW_MINE: db.table.pk -->` 幂等块，宁缺毋滥，错配登记 outline\_mismatch.md。
7. **P5：Phase 4 收尾**——覆盖率 100% 对账、禁止行为审计（reader\_exec\_log 无关键词 WHERE）、0 信任抽样 1/10、去重审计（dedup\_index）、学术性审计、markdownlint+格式终验。

每完成一库：progress.py page 登记 → review\_logs/<db>.md → 考据记录（06-考据记录/）→ changelog.duckdb 写变更（去重检查）。

***

## 八、Phase 2D 邮件库遍历记录（2026-08-31 两轮，usenet\_mail）

**已完成（累计）**：usenet\_mail.duckdb（234,573 行）dump p001-p060（id 77-3108，frontier=\[3108] 记于 \_mail2d\_usenet\_frontier.json）；逐行审读 p001-p004（200 行，id 77-276）→ 候选 30 条全部落库 EV/CL-RM-010001\~010030（id 唯一、引文同串反查 30/30；p001 9 条含 7 条 pending 已核验升级 checked）→ 大纲增补 3 文件 7 块（28.3←010011/010015/010017/010023 四块、299.2←010010、18.4←010002/010007，均 ROW\_MINE 幂等块，仅增不删）。留痕：review\_logs/usenet\_mail.md、triage 清单 p002-p004、考据记录 20260831\_usenet邮件库行级遍历首批判据.md（v2）、changelog id=970/973。

**本日事故与修复**（详见考据记录）：\_mail2d\_p34\_mine\_20260831.py 两次崩溃后 DuckDB 自动提交残留部分插入，第三次运行重插致 CL-RM-010012\~010018 双写冲突；\_mail2d\_repair\_rebuild\_20260831.py 清空 010 段按 pk 序重建修复。**规程铁律新增：批量写库必须单事务；崩溃续跑前必须先查库对账。**

**接手者下一步**（按序）：

1. p005-p060 及其后全部行按同流程续作：dump 已就绪直接用（pages/usenet\_mail\_\_messages\_\_p005 起存在）；主会话审读用 review\_views 流程（\_mail2d\_review\_prep 构建视图→Read→逐行三态→脚本登记落库）；子代理通道若恢复可走单页轻任务+磁盘核验。
2. 候选登记与落库直接复用 \_mail2d\_repair\_rebuild\_20260831.py 的“CAND 锚点表+清空重建”模式（id 续 010031\~），或单事务增量模式；**切勿在崩溃后盲目重跑**。
3. p001 遗留 11 条 needs\_recheck（id 79,87,94,99,104,109,111,112,116,122,123）与 p004 id234 待复核；id239 跨 spec 去重已跳过。
4. dedup\_index.json 解析缺陷仍未修（仅取到 1 条指纹）；落库去重现以 raw\_source.content\_hash 全库比对替代，尚可接受。
5. progress.jsonl 补登仍未做（progress.py page 的 CLI 参数需先核对）；coverage 以 review\_logs/usenet\_mail.md 的 frontier 记录为准。
6. 通道经验：本日单发 3 次全失败，主会话审读视图方案（380 字符折行规避 Read 截断）验证有效，每页约 12k token。

***

## 九、策略变更与小库优先队列（2026-09-01）

- **用户指令**：记录当前进度；邮件库遍历转为**从小到大**（按文件大小升序）。

- **进度快照**：usenet dump 60 页/3,000 行、审读 p001-p008/402 行（0.171%）、主张 30 条（010001\~010030）、大纲块 7 个、待复核 12 条。p005-p008 的 41 条候选结论固化于 review\_logs/usenet\_pending\_candidates\_p005-008.txt（锚点格式，可机械提取引文）。

- **权威队列**：mail2d\_catalog\_by\_size.json（282 库 size 升序，含 messages/lists 行数与 queue\_pos）。全库实测 125,059 MB / 22,113,386 封。

- **立即开工队列**（最小 10）：dev-reviews(12)、freebsd-accessibility(58)、freebsd-ocaml(4)、freebsd-reproducibility(5)、port-evbsh5(2)、port-hpcarm(1)、port-pc532(1)、regional-ch(1)、tech-embed(3)、archbsd-hackers(8)。此类小库可整库读完即收口。

- **执行模式**：每库 read\_page.py 全量 dump → 审读视图（>50 行则 380 字符折行）→ 逐行三态 → 候选+triage 文件 → 单事务落库（id 续 010031\~）→ review\_logs/<db>.md + progress 登记（rows\_read==rows\_total 完成判定）→ 大纲增补仅对通过双门禁者。

- usenet\_mail 遗留：p009-p060 已 dump 待审、p061 起待 dump；p005-p008 候选待落库；12 条待复核。均在小库批次后回归。

***

## 十、快照（2026-09-02 收盘）

- 邮件段主张累计 97 条（010001\~010097，全部 checked，反查通过）；**大纲 ROW\_MINE 邮件块累计 12 个**（28.3×4、299.2×1、18.4×2、315.2×2、181.2×3）

- 库进度：**19/282 completed**（dev-reviews、freebsd-accessibility\*、ocaml、reproducibility、evbsh5、hpcarm、pc532、regional-ch、tech-embed、archbsd-hackers、teaching、errata\*、ops-announce\*、tinderbox、avr32、iyonix、mvmeppc、regional-helsinki、tech-smp、lfs、ietf-ssh、policy 中 \* 为 dump 完成未审——注：实际 completed 为后 19 项含三库，以 catalog 为准）；dump 完成至队列 #60

- usenet：审读 p001-p008（402 行）+ 41 条候选全部落库；待审 p009-

- 已知事实：并行子代理跨会话 15+ 路全静默（不可用）；单发成功率 \~1/3；主会话审读视图（380 字符折行）为可靠兜底

- 下一步：①队列 #20+ 续推（netbsd-desktop 136/port-mvme68k 132/freebsd-eol 46/port-pdp10 61/freebsd-hpc 52/oi-users 66/freebsd-user-groups 97/freebsd-ia32 119/freebsd-lite 121/freebsd-realtime 100/freebsd-riscv 122 已 dump）②每完成一库即评估大纲增补机会 ③uucp 政策声明类（policy/announce）优先深挖

***

## 十一、快照（2026-09-04 收盘）

- 邮件段主张累计 132 条（010001\~010132，全 checked）；**30/282 库 completed**

- 本轮新增：pdp10(2)/eol(3)/sun2(8)/amigappc(6)/hpc(4)/women(2)

- 大纲机会登记：①port-sun2 的 2009 Attic 弃置之争与 tier 分层起源（010115~~010117）——第 9 卷无专章，择章或新开；②port-amigappc Wille 复兴工程（010121~~010126）——第 9 卷 port 史素材

- 断点：Task 2 余库 mvme68k(232K)/netbsd-desktop(258K)/realtime(298K)/user-groups(374K)/ia32(452K)/riscv(484K)/tech-multimedia(570K)/translators(631K)/lite(669K)/advocacy(826K)/oi-users(408K)；usenet p009-

- 提醒：dump 正文含 HTML 实体（" 等），锚点避开引号字符；大库视图用逐行摘要提取法更省

***

## 十二、快照（2026-09-05 收盘·goal 持续推进中）

- 邮件段主张累计 161 条（010001\~010161，全 checked）；**37/282 库 completed**；大纲 ROW\_MINE 块 13 个

- 本日新增：mvme68k(5)/desktop(5)/realtime(4)/user-groups(5)+315.2 增补/ia32(4)/riscv(4)/oi-users(2)

- **库名辨析**：oi-users=1995 Open Interface GUI 工具包列表（寄居 freefall，含 PHK 'A minor accident' 转发，010160）——非 OpenIndiana

- 断点：Task 2 仅余 tech-multimedia(570K)/freebsd-translators(631K)/freebsd-lite(669K)/netbsd-advocacy(826K) 四大库；dump 仍至队列 #60，#61+ 需续 dump

- usenet 断点 p009（审读）；p061+ 需续 dump（dump frontier=3108）

- 方法沉淀：大库用逐行摘要提取法（subject+前 200 字）预triage，候选再取全文；dump 正文含 HTML 实体，锚点避开引号

***

## 十三、快照（2026-09-06 收盘·Task 2 全部完成）

- **里程碑：Task 2（已 dump 未审库）全部清零，41/282 库 completed；邮件段主张 176 条（010001\~010176，全 checked）**

- 本日新增：lite(4，1996 LITE2 合并史专档)/advocacy(4，Ebihara OSC 展机系列+二十周年征史)

- 阶段转折：下一步进入 **Task 3（队列 #61-#100 续 dump+审读）**——dump 脚本 read\_page.py 续跑即可（frontier=队列位置）；usenet 线 p009- 同期并行

- 大纲机会登记：freebsd-lite 的 1996 LITE2 合并四部曲（010169\~010172）→ 第 4-5 卷 Lite2 合并章（尚未定位专章，择章或新开）；netbsd-advocacy 的二十周年征史（010174）→ 第 9 卷

- 方法沉淀（增补）：审读摘要中的 '/' 为视图折行标记，**绝不可混入锚点**（本轮两次回滚均因此）

***

## 十四、快照（2026-09-10 收盘·Task 8.6 大纲补课轮）

- **断点盘点纠偏**：台账曾滞后于实际进度——catalog 实为 **112/282 completed**（2.17/2.18 即 ports-announce/translators 早已于 09-06 完成，tasks.md 已补勾）；邮件段主张实为 **307 条（max CL-RM-010307）**；usenet 仍停 p008（71 条）

- **Task 8.6 首轮补课完成**：对 Task 2 期间新增主张（010098\~010307 共 294 条待评估）全量评估，**53 块 ROW\_MINE 写入 19 个大纲文件**（邮件引用 13→60）；主题簇：usenet 2BSD 六块（28.3，含 2.9 TCP/IP 首工程确证）、LITE2 合并四部曲（88.9）、FCP 三连（346.2）、sun2 Attic/tier 起源三连+桌面专项闭环+二十周年征史（186.3）、OSC 京都/AsiaBSDCon（332.3）、Netflix KERN\_TLS（267.2）、InfiniBand 五连+netmap 实测（142.12）、RISC-V 三连（133.5）、sysinstall 前史（123.2）、CTM 四部曲（89.3）、binup→freebsd-update 前身（89.4）、欧洲用户组六连（329.7）、SMP 锁纪律（181.2）、JDK 商标（97.6）、澳/印尼/美/俄/多元各一块（344.2/343.3/328.4/334.5/346.10）

- **去重与择章决策**已登记 `outline_mismatch.md`（同事件去重 1 条：FCP-0101 仅取 010238；L2/边缘留库一批；无专章可挂 17 簇——含 NetBSD 端口专史新章候选、FreeBSD 云分发新章候选）

- **格式终验 PASS**：19 文件无 BOM/CRLF/“”“”/直引号/重复标记；写入用幂等块+查重守卫（脚本 \_mail2d\_outline\_a\~e\_20260910.py 可复用）

- **dump 状态**：≤#132 全部 20 个待审库 dump 就绪（freebsd-test 2000 封本次补齐）；#133+ 未 dump

- **下一步**：①Task 3 审读 ≤#132 的 20 库（总 16,379 封，digest 摘要法，最小 regional-jp 118/regional-pt 123 起）；②usenet p009+；③changelog 已记（本轮）

- **同日续记（缺口收口）**：regional-jp（#86）与 regional-pt（#87）两库收口——118+123 封全读、14 候选落库 **010308\~010321**（14/14 反查通过），catalog **114/282**；重要史学发现：**AsiaBSDCon 首届为 2004 台北（57481），东京 2007 为第二届**——已作修正性块写入 332.3；Mewburn 2004 附件过滤试验（27617）与 regional-pt 蠕虫期自复信洪泛互证，写入 186.3；随批大纲增补 6 块（332.3×2/332.5×1/329.7×2/186.3×1），本日大纲累计 **59 块/23 文件**，邮件引用 13→66；changelog id=1027

***

## 十五、快照（2026-09-02 收盘·队列修订 282→281）

- **linuxkernel\_mail 冗余删除**：合并库（9,213,897 封，16 列表，60.3GB）经逐列表指纹对账（COUNT/MIN/MAX/SUM(hash(msg\_hash))）与 16 个拆分库（lkml/netdev/linux-mm/linux-fsdevel/linux-scsi/linux-arch/linux-api/linux-man/sparclinux/rust-for-linux/ksummit/ksummit-discuss/linux-cve-announce/linux-kernel-announce/linux-smp/tech-board-discuss）**16/16 全等**，确认零独占内容，按用户指令删除；SQLite 原库 ARCHIVE\_FINAL\_20260818.db.gz 已存 12-数据库备份/linux-kernel/；catalog 282→281（记 dedup\_note）；folder\_db\_registry.csv 移除登记；changelog id=1028；证据 script/\_db\_row\_mining/\_linuxkernel\_uniqueness\_20260902.json；**Task 6.3 此后指拆分库 16 库（lkml 644 万封为最大）**

- **大型及以上库价值分级已完成**（116 库逐个分析，含逐库真实时间跨度）：核心战线 ≈30 库 ≈125 万封（usenet/current/hackers/arch/fs/net/stable/chat/security/ports/geom/smp/jail/pkg/pf/announce/hubs/advocacy/amd64/tech-kern/tech-userlevel/tech-net/dragonfly\_mail/openbsd\_mail/other-bsd\_mail 等）；近零价值区 ≈20 库（Linux 专项/语言 port 专项/机器人库）；数据清理另立案：cuold/cunew/cu 三重存储（各 10,064 行相同）待裁定

- **本会话审读进度**：Task 3 已审 4 库（freebsd-stats 2 候选/freebsd-sysinstall 4/freebsd-tex 6/freebsd-pkgbase 40，共 3,218 封，triage 在 \_triage\_wip/）——**尚未落库**，id 续 010322 起；#92-#132 余 14 库未审（tech-repository/freebsd-proliant/afs/platforms/port-amiga/ctm-users/tech-board-discuss/testing/security/pkgsrc-wip-review/crypto/dtrace/test/regional-pl）

- digest 已生成：18 库（pages\_small/_digest_\*.txt）+ usenet p009-p060（pages/\_digest\_usenet\_pNNN.txt）；usenet 审读仍停 p008

- changelog：id=1028（linuxkernel\_mail 去重）；时钟口径：环境日期 2026-09-02

- **同日续记（全库重复复核）**：①磁盘枚举 316 库（排除备份/临时区），43 个同字节大小组全部证伪（DuckDB 行组对齐伪信号）；②281 邮件库逐库指纹（COUNT/MIN/MAX/SUM(hash(msg\_hash))/SUM(hash(message\_id))/distinct mid）**零全同组**；③cu/cunew/cuold 家族：msg\_hash 两两交集 10,064/独有 0、53 封 no-id 兜底 ID 前缀差异系解析伪差——同一份 NetBSD current-users 2021-2026 片段三次重复入库，**删除 cunew/cuold 保留 cu.duckdb**（current-users.duckdb 2008-2009 碎片零重叠互补保留）；删除前主张/证据引用扫描为零；catalog 281→279；registry 移除 2 行；changelog id=1029；证据 \_mail\_fp\_scan\_20260902.json + \_cu\_family\_diff\_20260902.py

- **同日三记（linux-cve-announce 移除）**：按用户指令删除 05-linux-kernel/db/linux-cve-announce.duckdb（15,371 封机器人 CVE 公告，★1，引用扫描为零，内容可自 12-数据库备份/linux-kernel/ARCHIVE\_FINAL\_20260818.db.gz 恢复）；catalog 279→**278**；changelog id=1030；**linuxkernel 拆分库战线为 15 库**

- **同日十二记（tech-board-discuss 收口）**：857 行全读，14 候选落库 **010554-010567**（14/14 反查通过）——**确认为 Linux 基金会 TAB 列表非 NetBSD**（此前价值分析误判已纠正）；治理全史（2006 OSDL 起源→2007 首届→2018 CoC 危机 Bottomley 反思→2020 包容性术语 Torvalds 亲临→全电子选举→2024 xz 响应→2025 Wilcox RMS 决裂宣言）；累计主张 **567**；catalog **128/273**；changelog id=1039；批三余 4 库未审：freebsd-testing(1083)/pkgsrc-wip-review(1095)/freebsd-test(2000)/tech-security(1163)——digest 均已备

- **同日十三记（tech-security 收口）**：1163 行全读，33 候选落库 **010568-010600**（33/33 反查通过）——NetBSD 安全架构全史（kauth/secmodel 可插拔模型、熵子系统三代重构 tls rnd→RDRAND→getrandom、fexecve 论战、恒时密码原语 crypto\_memset/bozohttpd、ACPI 固件 rootkit、cgd 密码演进与多盘共享密钥、veriexec MD5/SHA1 移除、strlcpy/strscpy 论战、setuid 硬链接两轮加固、信任锚入基）；累计主张 **600**；catalog **129/273**；changelog id=1041；批三余 3 库未审：freebsd-testing(1083)/pkgsrc-wip-review(1095)/freebsd-test(2000)——digest 均已备

- **同日十四记（freebsd-testing 收口）**：1083 封全读，16 候选落库 **010601-010616**（16/16 反查通过）——FreeBSD 测试基础设施全史（ATF/kyua 框架、CI 集成 Travis/Cirrus/Jenkins、32 位 compat 测试 i386→arm64、bhyve 测试 VM、Sysunit 内核单元测试、jail 执行环境、required\_klds 元数据 RFC、dummymbuf 模块、pjdfstest 集成）；累计主张 **616**；catalog **130/273**；changelog id=1042；批三余 2 库未审：pkgsrc-wip-review(1095)/freebsd-test(2000)——digest 均已备

- **同日十五记（pkgsrc-wip-review 收口）**：1095 封全读，16 候选落库 **010617-010632**（16/16 反查通过）——NetBSD pkgsrc-wip 包审查全史（关键软件早期打包 tmux/nginx/i3 作者本人/Tor/FriCAS/LibreOffice/pip/clang、Linux DESTDIR bulk build、libmicro/lmdbg、DCC/openct/opensc/softhsm 安全线、Chromium 移植困境、2014 列表收编切 tech-pkg）；累计主张 **632**；catalog **131/273**；changelog id=1043；批三余 1 库未审：freebsd-test(2000)——digest 已备

- **同日十六记（freebsd-test 收口，批三 8 库全部完成）**：2000 封全读，4 候选落库 **010633-010636**（4/4 反查通过）——FreeBSD 测试列表（99.9% test 消息），仅取邮件基础设施运维痕迹（jmb resend 代码修改/mail loop 排查、Security Officer EOL 公告测试、2026 Discourse/gmane 变迁）；累计主张 **636**；catalog **132/273**；changelog id=1044；**批三 8 库全收口（regional-pl/tech-crypto/freebsd-dtrace/tech-board-discuss/tech-security/freebsd-testing/pkgsrc-wip-review/freebsd-test = 125 候选）**

- **同日十七记（Linux 邮件库群搁置）**：计划调整（**非物理删除**）——14 个未审 Linux 内核邮件列表库（lkml 644 万/netdev 125 万/linux-mm 58.5 万/linux-fsdevel 36 万/linux-scsi 22.8 万/linux-arch 11.5 万/linux-api 6.4 万/rust-for-linux 5.1 万/sparclinux 4.4 万/linux-man 3.2 万/ksummit 1.07 万/ksummit-discuss 0.73 万/linux-kernel-announce 0.55 万/linux-smp 0.16 万，合计 **9,197,669 封**）catalog `traversal_status` 置 **deferred**，DuckDB 文件保留不删；tech-board-discuss（completed，14 主张已落库）不受影响；重算后 **completed 132 / deferred 14 / 剩余待审 127 库（3,151,606 封，14.22 GB）**；剩余 Top 全为 BSD 库（freebsd-questions 47 万/usenet\_mail 23 万/freebsd-current 20.5 万/freebsd-hackers 20 万/freebsd-bugs 19 万/freebsd-ports 19 万/openbsd\_mail 15 万）；Linux 库后续单独安排处理；changelog id=1045

- **同日十八记（BSD 小库战线启动）**：dump 32 个 ≤2000 封待审小库 digest（+freebsd-config 已备，共 33 库就绪）；首批收口 2 库——①freebsd-mozilla（932 封）10 候选落库 **010637-010646**（FreeBSD 移植 Mozilla 全史：1998 列表创立/Netscape 合作错位/两次停摆/Firefox 改名/2013 退役）；②port-mips（1661 封）10 候选落库 **010647-010656**（NetBSD MIPS 移植全史：matt-nb5-mips64 分支与 N32/N64 ABI/2011 合并 HEAD/龙芯/2025 SGI 硬件复兴）；累计主张 **656**；catalog **134/273**；changelog id=1046；剩余待审 125 库

- **同日十九记（freebsd-xfce 收口）**：939 封全读，6 候选落库 **010657-010662**——FreeBSD Xfce 桌面 ports 维护史（Guido Falsi 主要维护者的当事人工作：menulibre 元包扩展/libexo 依赖升级/Xfce 4.18 预告/midori 重写/元包重命名征询）；主体为 bugzilla/portscout/pkg-fallout 机器人通知 + 营销钓鱼垃圾约 50 封；累计主张 **662**；catalog **135/273**；changelog id=1047；剩余待审 124 库（30 个已 dump 小库继续逐个审读）

- **同日二十记（freebsd-bugbusters 收口）**：889 封全读，12 候选落库 **010663-010674**——FreeBSD bugbusting 团队（PR 清理制度）完整史：2002 列表官方化+GNATS 升级、Bugathon 从 NetBSD 移植（Florent Thoumie 发起、2008 关闭 120 PR）、Mark Linimon bugmaster 周报机制、PR backlog 大讨论（Warner Losh 社区杠杆论）、send-pr 网页验证码反复故障、2014 net-ldap CVE-2014-0083 与 freeradius DoS 跨项目安全协作；大量银行诈骗/股票营销垃圾约 90 封；累计主张 **674**；catalog **136/273**；changelog id=1048；剩余待审 123 库（29 个已 dump 小库）

- **同日二十一记（freebsd-fortran 收口）**：925 封全读，10 候选落库 **010675-010684**——FreeBSD 科学计算（Fortran）生态史：2013 列表创立（Anton Shterenlikht+Steve Kargl）、gfortran 权威与 Thierry Thomas/Gerald Pfeifer 的 ports 维护、Uses/fortran.mk 去硬编码、elmer-fem 复活、OpenCoarrays 移植、NASTRAN 开源、2017 LLVM Flang 诞生；2019 后主体为 bugzilla/portscout/pkg-fallout 机器人 + 垃圾约 30 封；累计主张 **684**；catalog **137/273**；changelog id=1049；剩余待审 122 库（28 个已 dump 小库）

- **同日二十二记（freebsd-git 收口）**：1228 封全读，12 候选落库 **010685-010696**——FreeBSD 从 SVN 迁移到 Git 的完整制度史：2014 列表创立与 git-beta 探索、2014 GitHub 集成第一步、Ulrich Spörlein 长期维护 svn2git 转换器、2017 切换决策重启、2019 Git WG 成立、2020-12 src/doc/ports 正式迁移 git.freebsd.org、Warner Losh 主导 Git WG 后续与 github automation、2023 GitHub PR 政策实验、2025 got(1) 入 base 探索、2026 gitea-dev/Forgejo 探索；几乎无垃圾；累计主张 **696**；catalog **138/273**；changelog id=1050；剩余待审 121 库（27 个已 dump 小库）

- **同日二十三记（freebsd-numerics 收口）**：942 封全读，12 候选落库 **010697-010708**——FreeBSD msun 数学库 C99 复数与 long double 函数实现核心史：2012 列表创立（Stephen Montgomery-Smith 提议）、复数反三角函数完整实现（PR 170206）、Bruce Evans 逐行把关、Steve Kargl 实现 expm1l/expl/coshl/erfl/erfcl/lgammal/powl、David Schultz 集成、David Chisnall 推动 C99 long double、openlibm 与 Android 继承 msun、2017 半周期三角函数；主体为 bugmaster 周报 + 深度数学讨论；累计主张 **708**；catalog **139/273**；changelog id=1051；剩余待审 120 库（26 个已 dump 小库）

- **同日二十四记（freebsd-config 收口）**：625 封全读，12 候选落库 **010709-010720**——FreeBSD 配置设施（FCF）设计史：1996 install-geeks 改名 freebsd-config、1997 Michael Smith 发布 FCF 宣言与 Juliet 原型、内核配置 metasyntax 讨论（Jordan Hubbard/Warner Losh/HOSOKAWA）、1998 WebAdmin 与 Config Databases 大讨论（Terry Lambert/Alex Belits/Mikael Karpberg/Ruslan Shevchenko，LDAP/portalfs/configfs）、第三方工具 kc 与 GUI admin、1999 tftp boot、2000-2001 pxeboot/sysinstall 定制；2002 后转用户求助；累计主张 **720**；catalog **140/273**；changelog id=1052；剩余待审 119 库（25 个已 dump 小库）

- **同日二十五记（regional-nyc 收口）**：1149 封全读，10 候选落库 **010721-010730**——NetBSD 纽约地区线下社群社交史：核心开发者（Christos Zoulas/Perry Metzger/Roland Dowdeswell/Andrew Brown/Thor Lancelot Simon/Jan Schaumann/Curt Sampson/Bill Squier/Johnny Lam）每周四 DBA/O'Flaherty's 啤酒聚会传统、NYCBSDCon 2006 展位、NYCBUG 活动、硬件流转、PGP 密钥签名仪式；主体为啤酒闲聊；累计主张 **730**；catalog **141/273**；changelog id=1053；剩余待审 118 库（24 个已 dump 小库）

- **同日二十六记（并行审读首批 4 库收口）**：切换并行模式（子代理并行审读 + 主会话串行落库）——①freebsd-i18n（1253 封）15 候选落库 **010731-010745**（FreeBSD I18N/L10N 史：Citrus XPG4DL 导入/iconv 十年长跑/GSoC BSD iconv/CLDR locale 维护）；②freebsd-cluster（1086 封）14 候选落库 **010746-010759**（FreeBSD 集群生态史：Beowulf 身份界定/SGE 移植/bproc/Galera）；③port-evbmips（671 封）14 候选落库 **010760-010773**（NetBSD 嵌入式 MIPS 移植史：Malta/Alchemy/Atheros/龙芯，Garrett D'Amore 主线）；④freebsd-atm（1172 封）15 候选落库 **010774-010788**（FreeBSD ATM 史：HARP 与 NATM 双栈/NATM 移除）；累计主张 **788**；catalog **145/273**；changelog id=1055；剩余待审 114 库（20 个已 dump 小库）

- **同日二十七记（并行审读 5 库收口）**：①freebsd-uboot（713 封）12 候选落库 **010789-010800**（FreeBSD U-Boot 引导链维护史）；②port-sh3（750 封）15 候选落库 **010801-010815**（NetBSD SH3/SH4 移植史：Dreamcast/hpcsh/landisk，itojun/SAITOH/Marcus Comstedt 主线）；③freebsd-go（1108 封）15 候选落库 **010816-010830**（FreeBSD Go ports 维护史：Adam Weinberger/DES 主线）；④port-i386（1372 封）15 候选落库 **010831-010845**（NetBSD i386 移植史：UVM 锁合并/GCC 5.3/PaX/VirtualBox/Xen）；⑤netbsd-announce（1223 封）15 候选落库 **010846-010860**（NetBSD 官方公告史：UVM/IP Filter/pthreads/NPF/两条款许可证）；累计主张 **860**；catalog **150/273**；changelog id=1058；剩余待审 109 库（15 个已 dump 小库）

- **同日二十八记（并行审读 4 库收口）**：①freebsd-database（1760 封）14 候选落库 **010861-010874**（FreeBSD 数据库 ports 生态史，1 条 hash 重复跳过）；②freebsd-security-notifications（765 封）14 候选落库 **010875-010888**（FreeBSD 官方安全公告史：VU# 通报/SA 修订/openssh 大规模事件）；③freebsd-users-jp（925 封）15 候选落库 **010889-010903**（FreeBSD 日语社区史：Warner Losh 参与日语列表/小金丸信行手册翻译节点/pkgbase 讨论/BSD 小恶魔插画归属流言——含 iso-2022-jp 编码锚点修复 3 处）；④port-powerpc（1962 封）14 候选落库 **010904-010917**（NetBSD PowerPC 移植史：ppcoea-renovation 统一 OEA 重构/Wii 移植/mpc85xx DARPA 项目）；累计主张 **917**；catalog **154/273**；changelog id=1059；已 dump 剩余 11 库：p4-projects(321)/pkgsrc-wip-discuss(965)/freebsd-snapshots(975)/port-m68k(1232)/netbsd-ports(1380)/freebsd-enlightenment(1606)/port-mac68k(1613)/freebsd-wireless(1880)/freebsd-firewire(1883)/freebsd-jobs(1922)/netbsd-docs(1974)

- **同日二十九记（批次 A 4 库收口）**：①p4-projects（321 封）11 候选落库 **010918-010928**（FreeBSD Perforce 变更审阅切片：ia64 攻坚/TrustedBSD SEBSD/OpenPAM Cyclamen/s390x 尝试/Linuxulator MI 化）；②pkgsrc-wip-discuss（965 封）15 候选落库 **010929-010943**（pkgsrc 实验包孵化器制度史：CVS→git 评估/DESTDIR 动员/bulk build 制度化/SourceForge 衰落/2014 并入 tech-pkg）；③freebsd-snapshots（975 封）11 候选落库 **010944-010954**（FreeBSD 发布工程快照制度史：2012 重启/2013 VM 镜像/ARM 扩张/2020 SVN→Git 版本标识切换——1 处锚点修正）；④port-m68k（1232 封）15 候选落库 **010955-010969**（NetBSD m68k 端口群横切史：4.4-Lite 回流/FPSP 浮点仿真/ELF 迁移全周期/softfloat 终点/RAS 锁原语）；累计主张 **969**；catalog **158/273**；changelog id=1061；已 dump 剩余 7 库

- **同日三十记（批次 B 4 库收口）**：①netbsd-ports（1380 封）15 候选落库 **010970-010984**（NetBSD 新平台移植总列表史：arm26 入树/evbarm 诞生/port-390 制度起点/Xen domain0 提议/Genesi 厂商开放承诺/PDP-11 无 MMU 口述史）；②freebsd-enlightenment（1606 封）15 候选落库 **010985-010999**（FreeBSD Enlightenment 桌面 ports 维护史）；③port-mac68k（1613 封）15 候选落库 **011000-011014**（NetBSD Macintosh 68k 移植史：MacBSD 更名正统化/cray-ymp 档案迁移/Penguin 引导器——1 处锚点修正）；④freebsd-wireless（1880 封）15 候选落库 **011015-011029**（FreeBSD 无线网络栈史）；累计主张 **1029**；catalog **162/273**；changelog id=1062；已 dump 剩余 3 库（批次 C：freebsd-firewire/freebsd-jobs/netbsd-docs）

- **同日三十一记（批次 C 3 库收口，已 dump 小库战线全部完成）**：①freebsd-firewire（1883 封）15 候选落库 **011030-011044**（FreeBSD FireWire 子系统兴衰全史：下川英敏十年主线/fwe 以太网模拟/iPod 支持/Apple IPoFW 跨项目协作/MPSAFE 化/2012 维护者交接）；②freebsd-jobs（1922 封）12 候选落库 **011045-011056**（FreeBSD 商业生态招聘史：Jan Koum 招 Yahoo 管理员/Jordan Hubbard FreeBSD→BSDi→Apple→iXsystems 职业链/BSDCon 30 committers 全职量化/Daemon News 资助机制/JUNOS 招聘——1 处 rowid 误录修正 1393161→1393159）；③netbsd-docs（1974 封）15 候选落库 **011057-011071**（NetBSD 文档工程制度史：Guide 官方化/多语种翻译协调人传承/版权不译制度/CDDL 立场/4.4BSD 文档回归/docathon 制度化）；累计主张 **1071**；catalog **165/273**；changelog id=1065；**已 dump 的 33 个小库全部收口，下一阶段转 dump 未 dump 库循环推进**

- **同日三十二记（dump 扩容 + 批次 D-1 4 库收口）**：dump 脚本 LIMIT 2000→5000，新 dump 31 库（2053-4975 封）；随后批次 D-1 4 库收口：①netbsd-syzbot（2002 封）13 候选落库 **011072-011084**（NetBSD syzbot 模糊测试集成史：2022 订阅接入/#syz fix 工作流/Ozaki 单日批量修复/Campbell↔Vyukov 五轮基础设施协作）；②tech-x11（2053 封）15 候选落库 **011085-011099**（NetBSD X11 图形栈史：native xorg 迁移/XFree86 退役/基金会资助 DRM2 工程起点/Nouveau 落地/NVIDIA 开源转向即时回响）；③freebsd-qa（2130 封）15 候选落库 **011100-011114**（FreeBSD 发布 QA 制度起源史：1999 列表创立/每4天测试快照/XFree86-4 默认化之争/RE 职责交接/Testing Guide 制度化）；④freebsd-eclipse（2311 封）15 候选落库 **011115-011129**（Eclipse IDE 移植接力史：2005 建制/eclipse-devel 双轨/2013 主线化/2014 解散危机/2019 末代抢救——2 处 rowid 误录修正）；累计主张 **1129**；catalog **169/273**；changelog id=1066

- **同日三十三记（批次 D-2 4 库收口）**：①freebsd-standards（2437 封）15 候选落库 **011130-011144**（FreeBSD 标准遵从史双峰结构：2001-2002 POSIX.1-2001 黄金期 C99 一致性工程/iconv 入基/Wollman 标准隔离区反对纲领；2018 后 select restrict 之辩/POSIX 2024）；②freebsd-bluetooth（2423 封）15 候选落库 **011145-011159**（FreeBSD 蓝牙栈史：Maksim Yevmenkin 十年单人主线/rc.d 服务化/FreeBSD↔NetBSD↔BlueZ 三角代码流动/ng\_ubt2 重写/BLE 起点/2025 Intel AX 激活）；③freebsd-libh（2457 封）15 候选落库 **011160-011174**（libh 安装器项目兴衰全史：2000 列表建立/承包商渊源/Kientzle 打包提案/2004 LibH is dead/Anaconda 借 linux.ko 移植尝试/BSD Installer 接力/2010 列表退役——2 处 rowid+1 处锚点修正）；④freebsd-drivers（2461 封）15 候选落库 **011175-011189**（FreeBSD 驱动子系统制度史：bus\_get\_dma\_tag API 分界/SDHCI 立项/Intel Jack Vogel 厂商驻社证词/iflib 框架化转折/newbus attach 之辩/ath\_hal 许可复核）；累计主张 **1189**；catalog **173/273**；changelog id=1068

- **同日三十四记（批次 D-3 4 库收口）**：①freebsd-audit（2575 封）15 候选落库 **011190-011204**（FreeBSD 安全审计运动兴衰史：1999 随机 PID 补丁起家/审计志愿者分工/WFORMAT 树级锁定/setgid 清除运动/OpenPAM/libufs/2010 列表退役）；②port-amd64（2818 封）15 候选落库 **011205-011219**（NetBSD amd64 移植史：PAE 入 GENERIC/32 CPU 上限突破/GCC 4.5.3 切换/NVMM 原生虚拟化引导 Linux/Xen PVHVM——1 处 rowid 修正 253805→253803）；③freebsd-usb（2881 封）17 候选落库 **011220-011236**（FreeBSD USB 栈史）；④current-users（2796 封）15 候选落库 **011237-011251**（NetBSD 5.0 前夜史：vmlocking2 合入/device\_t-softc 分离/jemalloc 化/sparc64 SMP/Atheros HAL 开源导入/time\_t 64 位化 Y2038/Desktop NetBSD 之争）；累计主张 **1251**；catalog **177/273**；changelog id=1070；已 dump 剩余 18 库

- **同日三十五记（批次 D-4 4 库收口）**：①tech-install（2347 封）15 候选落库 **011252-011266**（NetBSD sysinst 安装器十三年演进史：dmesg 解析之辩/大硬盘 BIOS 几何攻坚/安装介质去 GPL 化/syspkg 制度里程碑/软盘→CD 范式转移）；②freebsd-embedded（2927 封）15 候选落库 **011267-011281**（FreeBSD 嵌入式史：2006 列表创立/TinyBSD 入基/Openmoko 手机移植/TP-Link WR1043ND 全部件入库/etherswitch 框架/project-nand 入基/MIPS 平台裁剪/PKGBase 转型——3 处 rowid 错位批量校准）；③freebsd-announce（2854 封）15 候选落库 **011282-011296**（FreeBSD 官方公告史：CTM 就绪/国际加密分发/首届 committer 选举/AsiaBSDCon 首届/CVS→SVN 切换/OpenZFS 成立/Mike Karels 讣告/ports 仓库历史重写事故——1 处空正文行替换为 AsiaBSDCon）；④port-sparc64（3325 封）15 候选落库 **011297-011311**（NetBSD sparc64 移植史：SMP 2008 入干/UltraSPARC III 突破/GENERIC 默认 MP 化/GCC 4.5.3 首港/QEMU 仿真协作/illumos 弃 SPARC 回响）；累计主张 **1311**；catalog **181/273**；changelog id=1072；已 dump 剩余 14 库

- **同日三十六记（批次 D-5 4 库收口）**：①port-dreamcast（3023 封）14 候选落库 **011312-011325**（NetBSD Dreamcast 游戏主机移植史，1 条 hash 重复跳过）；②port-macppc（3099 封）15 候选落库 **011326-011340**（NetBSD PowerMac 移植史）；③port-sparc（3591 封）15 候选落库 **011341-011355**（NetBSD SPARC 移植史与 OpenBSD 前史：Theo 决裂 CVS 权限之争/OpenBSD 命名构思/硬件捐赠物质文化/SPARC 商标争端——3 处 rowid 校准）；④freebsd-mono（3613 封）15 候选落库 **011356-011370**（Mono/.NET 生态兴衰史：bsd-sharp 社区时代/Moonlight 移植/Miguel de Icaza 介入/.NET Core 团队参与/GSoC CoreCLR 立项/2020 metaport 终局——3 处锚点校准）；累计主张 **1370**；catalog **185/273**；changelog id=1076；已 dump 剩余 10 库（freebsd-pkg/freebsd-jail/freebsd-toolchain/freebsd-performance/freebsd-virtualization/freebsd-rc/aic7xxx/freebsd-small/tech-toolchain/port-cobalt）

- **同日三十七记（批次 D-6 三库收口）**：①freebsd-toolchain（3188 封）15 候选落库 **011382-011396**（工具链 GPL→LLVM 迁移主线：lld 切换决策链 armv7/amd64/LLVM binutils 迁移 2014 前史→2021 计划→2024 执行/mold 2.0 AGPL 转 MIT/libsys 拆分构想/gnu++17 默认升级/GCC 运行时 GPL 例外考据/Binutils 2.17.50 退役/gcc8 端口退役）；②freebsd-pkg（3952 封）15 候选落库 **011397-011412**（pkgng 制度化：DragonFly DPorts 采用/SAT 求解器两代架构/官方二进制包 2013-10-31 启用/签 catalog 非单包机制/pkg 1.3.0 与 1.5.0 发布/ports 仅支持 pkg(8) 2014 强制切换争议/portaudit 废弃迁移——011411 为写入失败跳号空洞）；③port-cobalt（3651 封）15 候选落库 **011413-011427**（NetBSD Cobalt MIPS 移植史 2000-2019：Soren Jorvang 创端口邀 Tsutsui 参与/厂商员工参与与 Qube2700 串口原理图外流/首个 userland 快照与 1.5\_ALPHA/恢复 CD 上架官方 FTP/Tsutsui bootloader 任意内核名与 netboot tulip 驱动/2019-05 MIPS 12 列表合并关闭——主会话兜底审读（子代理两次派发静默），digest 空格归一化跨行锚点自动修复 9 条（\_fix\_anchor\_auto\_20260904.py），52855/52856 空正文删除、列表关闭节点改用 52854 公告引文）；**口径修正**：DB 实况审计 COUNT=1420——D-5 记载 ID 段整体偏移 -10（实况 dreamcast **011322-011336**/macppc **011337-011351**/sparc **011352-011366**/mono **011367-011381**）；累计主张 **1420**；catalog **188/273**；changelog id=1079；已 dump 剩余 7 库（freebsd-jail/freebsd-performance/freebsd-virtualization/freebsd-rc/aic7xxx/freebsd-small/tech-toolchain）

- **同日三十九记（批次 D-7 四库收口；三十八记为非本线记录故跳过）**：①freebsd-jail（4146 封）16 候选落库 **011428-011443**（jail 生态史：Fournier 创列表/SoC2006 资源限制/Gritton 层级 jail 与 v2 参数化/jailconf 与 2012 新 jail(8) 入 HEAD/多 IP jail r185435/VIMAGE 11.0 稳定化与 12.0 转正/ezjail 全灭→iocage 诞生→MWL 写书大讨论/Jetpack 容器运行时——1 处锚点修正）；②freebsd-virtualization（4169 封）16 候选落库 **011444-011459**（bhyve 扩张期：Joyent 移植 SmartOS/ARMv8 引导/热迁移立项/CPU 拓扑 CFT/NVMe 仿真/VIMAGE pf 修复/ena(4) 取代 xn(4)/官方 VM 镜像 URL 变更/非特权 bhyve/bhyve 入 jail——7 处 rowid 反查修正：子代理 rowid 抄错但锚点库内可定位）；③freebsd-rc（4280 封）16 候选落库 **011460-011475**（rc 框架演进：rcNG 依赖环与 rcorder 重写/ports rc.d 大争论/early 关键字最早方案 2004/rc.conf.d/service(8) r200743/chkconfig 引介未入基）；④freebsd-performance（4975 封）17 候选落库 **011476-011492**（性能文化主阵地 2003-2021 全跨度：列表创立日/tcp\_output starving 论战/优化团队呼吁与 pmc 项目启动/fefe 基准重跑/GEOM RAID-3 诞生/PMC(3) RFC/libMicro 移植/5.3 I/O 危机与 Dillon 亲自下场/NetBSD 2.0 beats FreeBSD 论文风波/net.isr.direct 征召/UDS 细粒度锁/8 CPU 扩展性里程碑/SCHED\_ULE 默认争议/gcc vs clang 编译器基准/2021 AWS EC2 性能问题——主会话兜底审读，子代理静默，锚点全数一次通过）；累计主张 **1485**（011428-011492 无跳号）；catalog **192/273**；changelog id=1080（注意：entries 表 INSERT 须显式给 id 列，本次曾产生 NULL id 已修复）；已 dump 剩余 4 库（aic7xxx/freebsd-small/tech-toolchain/port-sgimips）

- **同日四十一记（批次 D-8 四库收口；四十记为非本线记录故跳过）**：①freebsd-small（4614 封）16 候选落库 14 条 **011493-011506**（嵌入式小型化运动全史：1998 PicoBSD 诞生与 src/release/picobsd 入树/1999 Juniper M40 嵌入式 FreeBSD 披露与 PHK DiskOnChip fla 驱动/Soekris net4501 首批 240 块量产/PocketBSD-minibsd-m0n0wall 袖珍生态/TinyBSD 先声与 2004 PHK nanobsd 原型分水岭/2006 TinyBSD 入 -CURRENT/2006 创 freebsd-embedded 与 2010 退役——2 条 hash 重复跳过，1 处 rowid 反查 2505229→2505249）；②tech-toolchain（4614 封）16 候选落库 **011509-011524**（NetBSD 工具链史 2008-2024：GCC 4.1→4.5.3→5.3→8→12 切换决策链与 GPLv3 之争/LLVM-Clang 2008 构想→2011 补丁→2013 导入/BUILDSEED 可重现构建/libelf 导入与 CSU 解耦/pcc 之问/Compiler selection 细粒度化/binutils 2.26——1 处 rowid 反查 287426→287416）；③port-sgimips（2013 封）16 候选落库 **011525-011540**（NetBSD/SGI MIPS 移植史：Soren Jorvang 创列表/Indigo 引导/Rafal Boni Indigo2 与 PROM 拒 ELF/Havard Eidnes ARCS loader/IP32 O2 攻坚 mace\_pci-TLB-R10K-crmfb/IP30 Octane 工具链诊断/D'Amore IP12 复活/XFS relicense/COMPAT\_IRIX——1 处锚点子串修复）；④aic7xxx（4398 封）16 候选落库 15 条 **011541-011555**（Adaptec SCSI 驱动演进：Gibbs 971208 CAM Snapshot/tagged queueing 挂起与 Dque 位/aic7895 支持与 7890-91 大改判断/sequencer 407 指令与 FAILDIS 时序/AIC-7899 U160 与 AIC7902 U320/Gibbs Adaptec 雇员名义 6.x/2013 退役征询——1 处 rowid 反查 21131→21052，1 条候选放弃 18283 Ultra2 首问锚点库内不可定位）；累计主张 **1546**（011507/011508 为 hash 跳号空洞）；catalog **196/275**（catalog 总数 273→275：其他流程新增 2 库）；changelog id=1082；**已 dump 库全部收口完毕**——下一步 dump 新一批 pending 库继续循环（余 65 pending）

- **同日四十二记（≤5000 封 BSD 小库战线收官；非本线记录占用 entry\_order 40）**：①dump 脚本复跑按 messages≤5000 筛选仅剩 linux-smp（1590 封），确认**所有 ≤5000 封 BSD 小库已全部逐行遍历收口**；②发现此前裁定 deferred 的 Linux 库群 traversal\_status 被其他流程重置为 pending（deferred=0），按用户既有裁定将全部 12 个未审 Linux 库重新标记 deferred（linux-smp/linux-kernel-announce/linux-man/sparclinux/rust-for-linux/linux-api/linux-arch/linux-scsi/linux-fsdevel/linux-mm/linux-mail-core-figures/linux-mail-keyword-hits）；③dump 脚本修复 messages=None 过滤崩溃（isinstance int 守卫）；④最终口径：catalog 275（其他流程 +2），completed **196** / deferred **12** / pending **63**——pending 全部为 >5000 封 BSD 大库（5279-472235 封：port-vax 5331/tech-net 9040/freebsd-desktop 9545/freebsd-geom 7664 等）；⑤本战线累计主张 **1546**（CL-RM-010001-011555）；changelog id=1083；**后续大库战线（>5000 封，63 库）另行规划——小库 spec（mail2d-small-first-complete-2026-09-03）核心范围全部完成**；**范围裁定（2026-09-05，changelog id=1086）：纯 git 代码仓库库不纳入行级遍历任务**（mail2d catalog 核实无 01-代码仓库史料 库混入，裁定约束后续大库战线与全库遍历规划）；同日发现 lkml/netdev/ksummit/ksummit-discuss 4 库 deferred 再次被并发流程重置为 pending，已按 Linux 库群裁定重新 deferred（deferred 12→16，pending 63 口径恢复）；**范围裁定二（2026-09-05，changelog id=1087）：新闻组库 usenet\_mail（234573 封）移交其他任务**（catalog 条目加 assignment=other\_task\_usenet 标记，traversal\_status 不动），本线待规划大库降至 62

- **同日四十三记（大库战线开线 + 首库热身收口，spec mail2d-large-first-2026-09-05）**：①用户裁定大库策略——三个 -bugs 混合库（freebsd-bugs/netbsd-bugs/pkgsrc-bugs）机器人层收口+真人层遍历，其余 59 库按旧策略逐个全量遍历（changelog id=1088）；spec 三件套落盘 .trae/specs/mail2d-large-first-2026-09-05/；分段 dump 脚本 \_dump\_large\_20260905.py（每段 5000 行 → pages\_large/）；②首库 other-bsd\_mail（5,315 封 2 段）收口：15 条落库 **011556-011570**（BSDI 早期生态/TrustedBSD 安全体系 NAI-DARPA-ACL-OpenBSM 1.0 生产版/Darwin-DarwinBuild/illumos-OpenIndiana 分立——子代理 5 处 rowid 反查修正+4 条幻觉放弃，主会话主题反查抢救 4 条 283/3821/3185/37）；累计主张 **1551**；catalog **197/275**；changelog id=1089；注意 trustedbsd-discuss 2006-02-11 Perforce 归档重灌行日期失真；下一库 port-vax（5,331）或 dragonfly\_mail

- **同日十一记（freebsd-dtrace 收口）**：870 行全读，13 候选落库 **010541-010553**（13/13 反查通过）——DTrace 本地化全史（2013 列表创立动因/SDT 重构 RFC/illumos 同步/网络 providers/Brendan Gregg 与 Adam Leventhal 原作者亲临/GSoC vmem/ARM 移植/2016 OpenDTrace 项目诞生/2023 基金会资助 kinst）；累计主张 **553**；catalog **127/273**；changelog id=1038；批三余 5 库未审：tech-board-discuss(857)/freebsd-testing(1083)/pkgsrc-wip-review(1095)/freebsd-test(2000)/tech-security(1163)

- **同日十记（批三：regional-pl + tech-crypto 收口）**：①regional-pl 550 行全读，12 候选落库 **010512-010523**——波兰社区形成史（BSDay 2003/镜像募捐/NUG Poland/mountowanie 译名之辩）；②tech-crypto 708 行全读，17 候选落库 **010524-010540**——密码学出口管制全史（cryptosrc-intl 双轨→并入 src/crypto→RSA 公有化→Heimdal→racoon 入基→熵池三代重构→Argon2id→根 CA 入基）；累计主张 **540**；catalog **126/273**；changelog id=1037；批三余 6 库未审：tech-board-discuss(857)/freebsd-testing(1083)/pkgsrc-wip-review(1095)/freebsd-dtrace(870)/freebsd-test(2000)/tech-security(1163)——digest 均已备

- **同日九记（port-amiga 收口，已 dump 批 20 库全部完成）**：1210 行全读，19 候选落库 **010493-010511**（19/19 反查通过）——m68k 遗产架构 18 年实录（gcc4 缺陷与 ABI 双寄存器考古、jemalloc 危机、amigappc 重生、Kujawa 硬件驱动复兴 2011-2014、XFree86-Xorg、SunOS/68k 移除与 384MB 之困、LLVM/GCC8 之争、MNT ZZ9000 自制硬件接入）；累计主张 **511**；catalog **124/273**；changelog id=1036；**本会话累计收口 12 库（stats/sysinstall/tex/pkgbase/afs/platforms/ctm-users/tech-repository/proliant/port-amiga 10 库主会话审读 + 4 库代理预审）**；下一步 dump freebsd-testing/tech-security/pkgsrc-wip-review/tech-crypto/freebsd-dtrace/freebsd-test/regional-pl（8 库）

- **同日七/八记（tech-repository + freebsd-proliant 收口）**：①tech-repository 873 行全读，18 候选落库 **010463-010480**——NetBSD 仓库迁移 18 年实录（2008 需求清单→Fossil 作者 Hipp 亲自参战→ESR cvs-fast-export 与 Core 声明→2025 pkgsrc CVS 谢幕）；②freebsd-proliant 761 行全读，12 候选落库 **010481-010492**——企业采纳史（HP 工程师 Cagle 主持→官方交付 HPASMD→iLO 选型论→UEFI 断代）；累计主张 **492**；catalog **123/273**；changelog id=1034/1035；下一步：port-amiga（1210，digest 已备）为已 dump 批最后 1 库；其后 dump freebsd-testing/tech-security/pkgsrc-wip-review/tech-crypto/freebsd-dtrace/freebsd-test/regional-pl

- **同日六记（ctm-users 收口）**：697 行全读（主会话），19 候选落库 **010444-010462**（19/19 反查通过）——CTM 服务 23 年全史（2003 设立→2009 防火墙危机/push-pull 之辩→2011-2013 SVN 迁移→2015 Wemm 未来之问→2018 停摆未遂+ctm(1) 基系统辩论→2019 维护者手术→2021 ports-cur 死亡→2022 官方列表移除→2026 流合并）；累计主张 **462**；catalog **121/273**；changelog id=1033；注意 ctm-users 存在同 id 双行（锚点须按 fetchall 实际行校准）；下一步：tech-repository（873）/port-amiga（1210）/freebsd-proliant（761）digest 已备

- **同日五记（六库收口 010358-010443）**：①4 已审库落库收口（stats 2/sysinstall 4/tex 6/**pkgbase 40**——2016-2021 pkgbase 全史当事人层，10.0 粒度之争与 TrueOS CFT 等均入 claims）；②主会话兜底审读 freebsd-afs（525 行，18 候选：Transarc 授权僵局→Arla 转折→OpenAFS→2011 port 入树）与 freebsd-platforms（528 行，16 候选：1995 PPC/Alpha 抉择、PHK 身份论、S/390、2010 退役）；③主张总数 **443**（010001-010443）；④catalog completed **120/273**；⑤changelog id=1032；子代理通道全静默（0/6），全靠主会话；下一步：ctm-users（697）/port-amiga（1210）/tech-repository（873）/freebsd-proliant（761）digest 已备，接着 dump testing/security/wip-review/crypto/dtrace/test/regional-pl

- **同日四记（5 个纯机器人库删除+价值抢救）**：①研判——21 个大型及以上机器人嫌疑库经 regexp\_matches 识别（修正 ～ SIMILAR TO 伪匹配）+ 逐库统计抽样（\_robot\_lib\_survey\_20260902.json）；②纠偏——netbsd-bugs（真人 68,034）/pkgsrc-bugs（46,164）/freebsd-java/freebsd-gnome/freebsd-bugs（真人 43,363）实为混合库保留，仅 freebsd-bugs 需"机器人层收口+真人层遍历"混合口径；③删除——pkg-fallout（100%）/ports-bugs（99.6%）/erlang（94.5%）/haskell（92.5%）/ruby（85.9%）合计 542,750 封；④抢救——真人层全量逐行复核（主会话兜底，子代理通道全静默），36 条 L4 主张落库 **010322-010357**（36/36 反查通过），回写第 6 卷 4 块（123.9 portupgrade 危机群、126.21 ruby 默认版本战争、128.6 GitLab 长征 r412530、131.8 OpenSSL 1.1/3.0 涟漪），大纲 ROW\_MINE 块累计 63 块/27 文件；catalog **278→273**；changelog id=1031；注意——ruby 多个行号誊录偏移已按主题+锚点校准（\_calib\_rowids\_20260902.py），freebsd-ruby/erlang/haskell/ports-bugs/pkg-fallout 五库 DuckDB 已不存在，后续主张仅可自 ARCHIVE\_FINAL 归档追溯

***

## 十六、快照（2026-09-04 收盘·usenet p009-p020 收口）

- **usenet（新闻组）线续审 p009-p020**（id 479-1084，600 行）：21 候选全部 L4 落库 **CL/EV-RM-010647\~010667**（0 信任反查 21/21），no\_value 579，needs\_recheck 0；usenet 主张累计 **92 条**（010001~~010030 + 010048~~010088 + 010647\~010667）

- 主题：2.9BSD 网络化/修订发行（Bostic）、ISR 发行（Travis）、2.10BSD 计划（Bostic/Leedom）、net.bugs.2bsd→comp.bugs.2bsd 大重命名（Horton）、2.10BSD 最后版（Leedom）、2bsd 许可证之争（Spencer/Rodman/Wellsch/Schultz）、2.11BSD USENIX 发行（Schultz）、4BSD bug 报告渠道（Horton）

- 联网三次复查：comp.bugs.2bsd 更名与 2.11BSD USENIX 发行均经 tuhs.org 原文镜像确认

- usenet 断点：审读 1000/234,573（0.426%），frontier 升至 p020 末（id 1084）；待续 p021+（Task 7.4）

- 落库脚本：\_mail2d\_usenet\_p009\_020\_register\_20260904.py；per-page 文件 candidates/triage p009\~020 已生成

***

## 十七、快照（2026-09-04 续·新闻组并行审读批次一）

- **子代理通道恢复**：按新闻组（lists.list\_id，43 组）切分并行派发；**通道实测规律——并行 3-4 路仅 1-2 路存活，单发 100% 成功，存活与否以磁盘候选文件为准**（review\_logs/usenet\_ng\_\_<listid>\_<name>\_candidates.txt，5 字段 pk|date|from|level|中文提炼）；并行计划固化 usenet\_newsgroups\_plan.json

- **批次一完成 4 组（2,957 封全读，候选 302 条暂存待落库）**：net.bugs 26（870 封/101 候选）、net.bugs.usg 27（551/97，库内 10 缺号已核）、net.bugs.v7 28（283/61）、comp.bugs.sys5 5（1,253/43+nr3）

- **批次一史学要点**：dmr 亲笔 5 封（V7 编译器/link 谱系，net.bugs.v7）；USG/USDL 组织史（Maranzano 1974 起源→PWB→Summit NJ→3B20S 移植，net.bugs.usg）；RFS vs NFS 之争与 SVR4 BSD 血统双当事人互证（comp.bugs.sys5 5360+5405/5702/5705/5720）；5534 苏联 DEMOS 版权撤帖（USL 诉讼前夜）；5747 Theo de Raadt 1991 早期 Usenet 线索（needs\_recheck）；125254/126098/125815/4487 四个 net→comp 更名公告闭环

- **落库欠账**：302 候选待提取引文后单事务写入 historical\_claims（id 续 CL-RM-010714\~ 起）——**下一会话优先执行**

- usenet 审读进度：1000 + 2,957 = **3,957/234,573（1.687%）**；剩余 39 组待派（第二批单发 announce 三组 31/37/43）

## 十八、索引覆盖豁免规则（2026-09-04 用户新增）

- 新规则：人物库+关键词库覆盖的 Linux 巨型库不参与逐封遍历；14 个 deferred Linux 库（9,197,669 封）改标 **covered\_by\_index**

- 覆盖索引：linux-mail-core-figures.duckdb（802 人物/126,156 发件邮箱）+ linux-mail-keyword-hits.duckdb（656 词/13,363 命中），命中可按 db.table.pk 反查原文

- 新遍历对象：两索引库登记 pending（figures 126,958 行 + keyword 14,019 行）

- 进度重算：completed 192 库/151,215 封；covered\_by\_index 14 库/9,197,669 封（不计入剩余）；pending 67 库/3,029,321 封 + 索引库 140,977 行 = 剩余 3,170,298

- 估算：nyc 基准（1,149 封/轮）约 2,759 轮；config 基准（625 封/轮）约 5,072 轮

- 规则已入 流程规则.md“Linux 巨型库索引覆盖豁免遍历规则”；catalog dedup\_note 已留痕

***

## 十九、快照（2026-09-05 收官·Linux 关键词候选 446 条裁定入库完成）

- **里程碑：linux-mail-keyword-hits 446 条 P2/C1（66）+P3/C3（380）候选 18 批逐条裁定收官——adopt 86/mismatch 360/doubt 0，去重 1，入库 85 条（CL/EV-RM-012754\~012838），0 信任反查 85/85 通过，changelog id=1102**

- 裁定管线：kw\_batches（build 提取 body\_head+windows）→ kw\_views（340 字符折行审读视图，\_build\_kw\_views\_20260905.py 可复用）→ 主会话逐条三态 → adj\_batch\_NN\_kw\.py 产出 kw\_adj/batch\_NN\_adj.jsonl → check\_kw\_adj\_20260905.py 守恒校验（pk+keyword 复合键、quote≤400 且逐字符在 windows+body\_head、adopt 字段齐备、禁用括号、证据级合法）

- 入库管线：\_kw\_build\_claims\_20260905.py（写前同串复核+sha256+源行定位，86 构建零失败）→ \_kw\_dedup（同源行同事实去重 1：linux-man|725769 batch\_03 P2 首裁保留、batch\_15 重裁移除）→ \_kw\_ingest（单事务 claim+evidence+claim\_evidence+raw\_source，同源复用，号段自动取全库 max+1）→ \_kw\_verify（三表配对+quote 反查源 body 85/85）

- 证据级分布：L4×59、L2×11、L1×9、L5×4、L3×2；词表 supporting+strong/contextual/decisive；confidence L1/L2=0.6、L3/L4=0.85、L5=0.9

- 高价值样本：dpt\_i2o \_\_bsdi\_\_ 条件编译（L5）、unifdef BSD 版权头链（L5）、ufs\_fs.h 跨变体支持史（L5）、sparc mman.h “SunOS'ified”（L5）、aic7xxx“BSDish driver glued into Linux”、MAP\_FIXED 4.2→4.3-Reno 考古、ioctl 编码 1982 CSRG Sam Leffler 提交溯源、whiteout 自 SunOS 3/4.3BSD 谱系、AT\&T vs BSD unlink 目录语义分野、IGMPv3 FreeBSD→OpenDarwin→macOS 管道、Samba 自 SunOS 移植 Linux（Allison 亲历）、Samba→第35章等 27 拟挂章

- 登记产物：kw\_outline\_handoff\_20260905.md（85 条按 27 章分组移交 Phase 3/P4 双门禁，**非写入授权**）、kw\_closure\_stats\_20260905.txt、kw\_dedup\_log\_20260905.md、outline\_mismatch.md 新增本线登记节（去重+第06→第07卷 139 章卷属修正+L1/L2 处置约束）

- 特殊处置：batch\_04 遗留 doubt（linux-mm|784941 msync/Troxel）经联网三源核证（NetBSD 开发者名录/ACM BBN 署名论文/NetBSD 邮件列表 <gdt@ir.bbn.com>）按预设路径升级采信；batch\_04 存量 quote 缺 `>` 前缀 1 处已修

- 经验沉淀：①同 message\_id 跨列表/跨批多关键词命中普遍（本线合并 14 组），裁定须全局查重后再落库；②行级 diff 上下文含行尾空格与 \t 缩进，quote 须程序化提取而非目视誊写；③PowerShell 内联 python 含特殊字符必失败，一律落脚本文件；④同源行两条主张若事实重叠须在入库前去重（raw\_source 复用≠可重复立张）

***

## 二十、快照（2026-09-05 续·85 条素材落地 05 大纲 + index.html）

- **主理人批准拟挂方向，两处落地，changelog id=1104**

- ⑤**05-卷册大纲（允许机械合并）**：27 个既有章（355 章口径，全部存在、无需新建章/卷）下各新建 1 个“关键词行级挖掘素材线索”节（N.M 节号=章内最大节号+1，共 27 节 85 条）；节内 5 字段——要点=claim\_text、史料=claim\_id+源邮件+批次锚点、史观=shigang 25 条总纲名称机械映射（**不硬编易错“第 N 条”编号，标注待人工精校**）、辨析=证据级提示、文献=主张/证据/源引用；27 个章 index.md 史料段追加引用行

- ⑥**index.html（禁止机械合并）**：手工撰写附录 doc-block（id=kw-clues，第二十二卷后、footer 前），按 22 卷口径逐章登记 85 条素材——16 个全局章经 src 溯源第一层数字精确映射，11 个（14/32/33/35/36/38/39/238/240/251/289）按语义人工定位（如 251→第十四卷第6章“macOS 与 FreeBSD 双向代码流动”、289→第十八卷第5章“自由的不对称”、35→第十五卷第1章“SunOS 与 BSD 商业化第一波”）；**未机械塞入节级 src**，仅附录登记 + 指向 05 新节

- 终验：index.html 无 BOM/CRLF、section/ul/li 标签配对、附录 claim\_id 覆盖 85/85；05 新节文件 27 个无 BOM/CRLF

- 经验沉淀：①27 拟挂章全部为既有章，故本线只新建“节”、未新建卷/章；②355 章口径与 index.html 22 卷口径是两套体系，靠 src 溯源“← 全局章号.节号”第一层数字相连，11 章因合并/重组无直接 src 对应，须语义人工定位——这正是 HTML 禁机械合并的技术根因；③05 节文件重跑须先删旧节文件，否则节号重复递增

## 十四、H5 freebsd-java h5jv_b517 三批全链闭环（2026-10-05）

freebsd-java 战役四批全 committed，整库 21,280 行全库收口（100%）。

- **b517_1**（既有，offset 0 n6000）：680 候选，CL-RM-205630-206309，宿主 167，提交 0d84fe14b。
- **b517_2**（本波，offset 6000 n6000）：读手 10 分件→候选 **2004** 条（L4 1723/L3 281）；叙述手 40 片（末片 p40 15 条）；register 落库 CL-RM-**390080**..392083，反查 quote 2004/2004 全命中；宿主 167 total_refs 680→**2684**（+2004）；numstat **+10020/0 = 2004×5 精确吻合**；幂等二跑 +0。
- **b517_3**（本波，offset 12000 n6000）：读手 7 分件→候选 **1070** 条（L4 886/L3 184）；叙述手 28 片（末片 p28 17 条）；register 落库 CL-RM-**392084**..393153，反查 quote 1070/1070 全命中；宿主 167 total_refs 2684→**3754**（+1070）；numstat **+5350/0 = 1070×5 精确吻合**；幂等二跑 +0。
- **b517_4**（本波，offset 18000 n3280，末批）：读手 6 分件→候选 **960** 条（L4 827/L3 133）；叙述手 24 片；register 落库 CL-RM-**393154**..394113，反查 quote 960/960 全命中；宿主 167 total_refs 3754→**4714**（+960）；numstat **+4800/0 = 960×5 精确吻合**；幂等二跑 +0。

**本波合计**：4034 候选 / 4034 落库 / 4034 入大纲；claim 区间 CL-RM-390080..394113 全 supported 全 L3L4；宿主 167 numstat 合并 +20170/0（4034×5 精确吻合）；三批 register 反查 quote 4034/4034 全命中。

**门禁修复记录**：
1. 合并器过严问题——既有 `_merge_cand.py` 硬门禁 20-80 字与禁 `\`，实测 b517_1 先例摘要 min 20 max 80 avg 57.8 说明 10-19 字摘要与 `Ctrl-\` 技术事实都是允许的；本轮写宽松合并器到 %TEMP% 规避误判——“判 PASS/FAIL 先查自己判据”的又一次坐实。
2. b517_2 p25 host 整片写成 667（笔误多一个 6）——合并阶段 `_merge_narr` 硬门禁抓到，机械修回 51 行 667→167。
3. b517_2 p15 pk 1385683 叙述 57 字低于 60 下限——合并阶段抓到，同义扩写至 81 字（补“调用方因此无法用它限制传输字节数”，未新增版本号/路径/命令/错误信息）。
4. b517_4 p23 子代理首次 Write 时路径漏 `_db_row_mining\`，误建 `D:\librebsd\script\review_logs\`——◐E 清理已删该错派目录与错派文件。
5. b517_2 p24 子代理在仓库内写 `_tmp_check_p24.py`——◐E 清理已删。

**freebsd-java 全库收口**：整库 21,280 行，offset 达 21,280（0/6000/12000/18000 四批），remaining 0，state complete。宿主 167 累计 4714 条 ROW_MINE（b517_1 680 + b517_2 2004 + b517_3 1070 + b517_4 960），是全库 21,280 行中 22.15% 的候选密度。

***

## 二十二、H2 freebsd-ports fpo_b199 在途进度同步（2026-10-08，全部为磁盘／库实测读数）

> 本节为 H2 线首次同步进本交接书。此前 b177–b198 共 22 批的进度只存在于 `mail2d_read_ledger.json`
> 顶层 note 与 memory，交接书从未记录 H2 线，本节一并补齐口径。

**台账权威现值**（`mail2d_read_ledger.json` 读盘，freebsd-ports）：
read_spec = read_judged = read_effective = **143999**，messages **191637**，读率 **75.14%**，
status `in_progress`，records[0].tags **48 条**、末位 `fpo_b198`，剩余待读 **47638** 封。
H2 已收口 22 批（b177–b198），b199 为第 23 批，窗口库内序 **144000–146999**（n 3000）。

**claim 库现值**（`04-现代研究文献/historical_claims.duckdb`，表名 `claim`）：
总量 **415760**（supported 410483 + rejected 5277）；全局最大 claim_id **CL-RM-424058**
（H5 h5ar_b524_4 尾号）。b198 收口于 CL-RM-418279–419816（1538 条）；**b199 尚未起号**，
register 落库时将从 CL-RM-424059 之后接续——**claim_id 全局共用，跨线并发，落库后以实测区间回填本表**。

**b199 已闭环环节（读波）**：
3000 封读出 **1609 候选**（L4 1406 / L3 203，判非候选 1391），40/40 分件读门禁全 PASS；
pk 1697133–1700134（区间跨度 3002，库内缺 2 个 pk 1697355／1699307 已在上游排除）；
date 1998-03-05 → 1999-06-25，主线段 1999-02→1999-06 合计 2997 封（99.9%），
**1999-04 整月缺口**、主线外 3 封（1998-03 两封、1999-01 一封）。
候选合并件 candidates.txt 1609 行 / 164408 B、narrpkg 40 份、cands_body 40 份
（截断阈值 1402，实测截断 **885 块**）、`_NARR_FACTS_FPO_B199.txt` 3551 B、
叙述提示词卡片 40 份（20047–20082 B，锚点齐、无 b198 残留）。
下游 12 份脚本字节层克隆全 PASS（`_gen_bodypack`／`_gen_narrpkg`／`_merge_narr`／
`_verify_narr`／`_verify_outline`／`_outline_fpo_b199`／`_register_fpo_b199`／
`_verify_ledger`／`_patch_claim`／`_patch_ledger`／`_audit_narr_actor`／`_measure`）。

**入库与入大纲进度：均未执行，阻塞在叙述波收口。**

| 环节 | 脚本 | 状态 | 前置 |
|---|---|---|---|
| 叙述波 | `_NARR_PROMPTS_b199/fpo_b199_p1..p40.md` | **12/40 在途或已落盘，良好 6** | 卡片已齐 |
| 叙述验收 | `_verify_narr_b199.py` | 未执行 | 40/40 分件全绿 |
| 叙述合并 | `_merge_narr_b199.py` → `fpo_b199_mount_narr.tsv` | 未执行 | verify PASS |
| 主体归属审计 | `_audit_narr_actor_b199.py` | 未执行 | 合并件（b198 曾因此整份重派，不得跳） |
| 入大纲 | `_outline_fpo_b199.py`（宿主 891/892/894/906/907/909） | 未执行 | 审计 PASS |
| 入库 | `_register_fpo_b199.py`（ANCHOR fpo_b199，QUOTE_LIMIT 300） | 未执行 | 大纲 PASS |
| claim 补丁 | `_patch_claim_b199.py` | 未执行 | register |
| 台账补丁 | `_patch_ledger_b199.py`（143999→146999、tags 48→49） | 未执行 | claim 补丁 |
| 终验 | `_verify_outline_b199.py` + `_verify_ledger_b199.py` | 未执行 | 全部上游 |

**b199 叙述波本波新增教训**：
1. **宿主越界是新缺陷族**——p7 首轮落盘出现白名单外的 `896`／`897`，且 28/41 行超 140 字。
   提示词虽已列宿主表，仍须在派单提示里**显式写出六个合法节号并点名拒绝 893/895/896/897/898/900**。
2. **顶格堆字不等于注水**——p2 avg 130.1、35/41 行 ≥120 字，抽查最长 6 行（ports/10102 的
   `CONFIGURE_ENV=IRCLIB`、ports/10118 的 Gary Perlman UNIX|STAT、ports/10070 的 `$(MOTIFLIB)`）
   实为 GNATS PR 表单字段本身信息密度高，非编造填充；**长度分布异常时须抽查内容而非直接判死**。
3. **叙述手自检真回补有效**——p3／p5／p6 首轮均带长度或逗号缺陷，自检后全部归零，无需主代理介入；
   主代理应在代理回报后再验盘，不打断在途代理的自检阶段。
4. **主体归属判读是本批最大价值产出**——p5 把 asami 引用块内问信人的原话（msql 2.0.4.1 老旧）
   正确改判为“转述”；p2 把摘要里正文中不存在的“Matthew Hunt”改回库内实有的句柄 `mph`；
   p4 纠正 `SOCKSconnect` 符号不在共享 `libsocks5`、`CATEGORIES+=` 的 `+=` 取舍、
   `CONFIGURE_ARGS` 实为 `--enable-gzipped-man`／`--enable-clear-pro` 而非 MANCOMPRESSED。
5. **b198 的年代判定不得承袭**——b198 卡片断言“FreeBSD 史上从未发布过 3.1”，
   b199 实测 `3.1-RELEASE` 125 次、`3.1-STABLE` 135 次、`3.2-STABLE` 77 次，
   本窗正是 3.1／3.2 双轨期；b199 卡片改为**只记实测计数、按字面照录、不据以断言任何版本发布状态**。
6. **`4.0-CURRENT` 266 次（本批最高频）主要出现在 GNATS PR 头 `>Release: FreeBSD 4.0-CURRENT i386`
   表单字段**，不是散文装机声明，卡片已明确不得据此写成“大家在跑 4.0-CURRENT”。
7. **本批新工具零值**——portmaster／poudriere／portsnap／gitup／update-tool／USE_PYTHON／
   USE_GNOME 实测全 0，卡片已列禁写清单；实测存在的只有 `USE_X_PREFIX` 8 次、`USE_AUTOCONF` 1 次。
8. **空 heredoc 会拉起交互 Python REPL 无限刷 stderr**（本波一次刷出 98MB 日志，TaskStop 后清除）；
   UNC 上一律落脚本文件再跑，不得用 `python -` 配空 heredoc。


