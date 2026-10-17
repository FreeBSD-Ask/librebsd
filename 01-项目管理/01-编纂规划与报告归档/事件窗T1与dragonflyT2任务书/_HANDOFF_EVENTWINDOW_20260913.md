# 接手书 · BSD 邮件遍历 2.0 事件窗线（2026-09-13 交接）

> 用途：给后续 AI 会话续接用。已跑通的模式、未完成清单、事故、准确续接入口全部在此。
> 权威自举入口：`script/_db_row_mining/RUNBOOK_BATCH.md`（每批收口时覆盖）。

## 0. 一句话结论
BSD 系 61 库 277 万封邮件史料的“事件窗遍历”模式已跑通并投产：基建（标记库/人物库/主题库/bot 过滤）100% 完成，**T1 九窗全部收官、累计 292 锚点**——六试点窗（w001 pf 引入→195.1、w002 pledge→199.1、w003 openssh→206.1、w004 netbsd2.0-smp→183.1、w005+w006 freebsd SMPng/调度器→161.8）＋放量首批三窗（w007 OpenSSH 全球采纳→207.2、w008 LibreSSL 诞生→208.1、w009 FBI 传言考据→213.2）。子代理通道已恢复（2026-09-14 六路并行实读全部成功）。下一步为 T1 放量余窗（D/A 缺参数或语料）与 T2 起步。

## 1. 已完成（可续用资产）

### 基建
- **标记库** `04-现代研究文献/rowmine_traversal.duckdb`：`msg_state(db,msg_id,state:0=bot/1=surveyed/2=body_read/3=candidate/4=claim, batch, updated_at)`、`bot_rules`(35 条)、`batch_log`、`event_window`、视图 `db_progress`。当前 292,037 行 / bot 222,959 / claim 10,811。断点续跑唯一真相源。
- **bot 过滤**：35 规则三轮重扫，合计 226,883 封出池（bugs 三库主力、GNATS 夜报 subject、FreeBSD 转义格式 from_name 族、ILIKE 大小写规避）。via-gnats 包装**未**标（内嵌真人回信须读）。
- **人物库** `linux-mail-core-figures.duckdb`：sender_stats +321,948（BSD 层 source_scope='bsd_mail'）、core_figure_stats +11,464（锚点当事人+高产）。
- **主题库** `linux-mail-keyword-hits.duckdb`：619 BSD 词、BSD 层命中 1,050,082 行；summary 722 词（Linux+BSD 合并统计）**正确可用**。
  - ⚠️ **异常**：`keyword_hits` 表现 20,556,301 行（step4 top10 稀有词明细被过度填充——v8 修复脚本 step4 对 lkml 等大库全表 regexp 每词插入、极常见短词 dora/ane/ear 命中率极高）。summary 无误；明细表臃肿。**续接者宜复核 step4 或重建筛选（每词每库设上限）**。
- **缺口矩阵** `_inventory/gap_matrix.md`：T1 零锚技术卷 52 章、T2 100、T3 47；大纲 ROW_MINE 共 11,545。
- **179.1 再分派**：21 条强建议复核完成（3 合理→303/303/13 章、2 存疑、16 假匹配——"de"撞 de-raadt 章名等三大假匹配源已甄别）；报告 `_inventory/reassign_1791_report.md`；**v2 时段错位重排脚本未跑**（见待办）。

### T1 事件窗（模式已验证，六窗槽建成）
| 窗 | anchor | 池 | 章→节 | 状态 |
|---|---|---|---|---|
| w001 | openbsd_mail_e001 | 2000 | 195→195.1 | ✅ 40 条 CL-RM-026107~026146、verify 9/9 |
| w002 | openbsd_mail_e002 | 593 | 199→199.1 | ✅ 38 条 CL-RM-025759~025796、verify 9/9 |
| w003 | openbsd_mail_e003 | 1156 | 206→206.1 | ✅ 40 条 CL-RM-033014~033053、写回 206.1（0→40）、verify 9/9 |
| w004 | tech-kern_e004 | 563 | 183→183.1 | ✅ 40 条 CL-RM-033496~033535、写回 183.1（0→40）、verify 9/9 |
| w005 | freebsd-smp_e005 | 195 | 161→161.8 | ✅ 22 条 CL-RM-033536~033557、与 w006 合并写回 161.8、verify 9/9 |
| w006 | freebsd-current_e006 | 376 | 161→161.8 | ✅ 22 条 CL-RM-033558~033579、合并写回 161.8（共 44 块）、verify 9/9 |
| w007 | openbsd_mail_e007 | 531 | 207→207.2 | ✅ **放量 B 窗**（OpenSSH 全球采纳）34 条 CL-RM-035510~035543、verify 9/9（报告 43 条，9 条与 w003 重叠已去重） |
| w008 | openbsd_mail_e008 | 152 | 208→208.1 | ✅ **放量 E 窗**（LibreSSL 诞生）45 条 CL-RM-035544~035588、verify 9/9 |
| w009 | openbsd_mail_e009 | 1167 | 213→213.2 | ✅ **放量 H 窗**（FBI 传言考据）11 条 CL-RM-035589~035599、verify 9/9（池内相关仅 11 条，未凑数） |
- **T1 九窗全部收官，累计 292 锚点**：pf 118（141.11）+ openbsd 事件窗 **208**（195.1 40 / 199.1 38 / 206.1 40 / 207.2 34 / 208.1 45 / 213.2 11）+ netbsd 40（183.1）+ freebsd 44（161.8）。

### pf 战线（**全库收官**）
b107-**b126** 收官：**789 条→141.11**（pf 锚点累计 20 批，L4=545/L3=244），台账 **9580/9580=100.0%**、next_offset=9580、status=已收官。**freebsd-pf 9,580 封全库遍历完毕。**
- b110（offset 1500-1999，40 条）：PF 3.7 导入 HEAD、if_bridge 移植 RFC、桥接 IP 校验和根因、pfsync 作模块的内核链接、subanchors 缺陷与 Hartmeier 的 parse.y 补丁。
- b111（offset 2000-2499，40 条）：MPSAFE 与 user/group 规则的锁序之争（kern/106805）、IPv6 有状态过滤缺陷（kern/102647，KAME 的 SUZUKI Shinsuke 接手）、pf 模块化（pf/pflog Makefile）、反向路径校验之争（verrevpath 请求 + ip_input.c 补丁）、启动期防护空洞（pf_boot）。
- b112（offset 2500-2999，40 条）：3.9 pf 导入启动、桥接校验和问题闭环（kern/93849 转 closed）、IPSEC 与 pf（IPSEC_FILTERGIF、enc0、kern/98219）、状态跟踪 off-by-one（Hartmeier 给出 OpenBSD pf.c diff 链接）、BAD state 群案、carp 配 inet6 失效。
- b113（offset 3000-3499，40 条）：**pf 4.1 导入**（HEADSUP）、7.0 移除 NET_NEEDS_GIANT/debug.mpsafenet（Watson 点名 uid/gid/jail 规则用户）、user/group 锁序补丁六周零反馈、carpdev 由 pil.sk 赞助、《The Book of PF》出版、ALTQ 大改造（Nate Lawson 测试召集）、carp 与 VRRP 的 IPPROTO_CARP 冲突、7.0 起 pf 改逐特性导入。
- b114（offset 3500-3999，40 条）：**pf 4.1 从 ALPHA 到 BETA 的实测推进**、**user/group 规则存废摊牌**（Max Laier 宣告面临被砍 → Volker 两万余字回应）、**libevent 之争**（PHK 斥其未经设计 → 作者 Provos 回应）、**分片 UDP 案收敛到 bge 驱动**（Kobayashi 报 EDNS0 → bge 作者 Pyun 介入 → Chepkov 证实）、**ng_pf 补丁**（PF 与 netgraph 互通 + 七层过滤）、**PF+dummynet 集成补丁**、半关闭连接超时值错误（对应 OpenBSD rev 1.494，kern/118154 闭环）、enc0 单向可见、pfil_local_phys、7-STABLE 自旋互斥锁 panic、动态接口 ALTQ 补丁、carpdev ALPHA 实测、7.0-BETA1 keep state 语义变更。
- **通用脚本族（b111 起，每批只写一个数据模块）**：`_pf_batch_survey.py <batch> <offset>`／`_pf_batch_candidates.py <batch>`／`_pf_batch_register.py <batch>`／`_pf_batch_mount.py <batch>`（**按 anchor 反查，勿再传 seq 段**）／`_pf_batch_outline.py <batch>`／`_pf_batch_ledger.py <batch> <lo> <hi>`；每批新写 `_pf_data_bNNN.py`（含 LEVEL/SELECTED/NARR/SUMMARY/CONTENT 五段，候选脚本内置键集·禁“”·40≤len≤220 自检）。
- **b115~b118（子代理实读 + 主代理亲撰，四批连跑）**：b115（2007-09~2008-12，40 条）上游版本节奏之争与 PR 处置群、桥接 NAT 顺序陷阱、IPv6 无条件丢分片；b116（2008 全年，40 条）**Max Laier 坦承 pf 单锁与状态表结构致 SMP 高负载瓶颈**、多路由表支持提交、IPv6 能力缺口、十天迁移 6500 行 iptables 到 pf+CARP；b117（2008-09~2009-12，40 条）**启动期防护正式处置**（Doug Barton 调 rc.d 顺序使防火墙脚本早于 netif）、版本同步路线（8.0 后与 openbsd-current 同步并处理全局锁）、上游漏洞传导核查；b118（2009-09~2010-12，40 条）**pf 版本升级实质推进**（Ermal Luçi 的 pf45_1.diff 基于 OpenBSD 4.5、Max Laier 公开催促测试、Hennessy 反馈套用受阻）、relayd 入 base 提案、Hartmeier 与 OpenBSD 的 Ryan McBride 双双介入 synproxy/超时/日志语义。
- **长回合作业法（本会话沉淀）**：一次生成后续 4 批 survey → 并行派 4 路子代理实读（每路 500 行分 3 块）→ 主代理逐批亲撰数据模块并跑通用链。子代理报告须要求“引文从缺”逐条标注（b117/b118 各 27/16 条），主代理据此只写有据可依的叙述，避免把引文块的他人文字误当作者自述。
- **b119~b122（四批连跑，长回合作业法定型）**：b119（offset 6000-6499，2010-10~2011-12，40 条）**pf 4.5 导入落地**（Bjoern Zeeb r223637 把 contrib/pf 由 OpenBSD 4.1 整体升到 4.5）→ 状态数失控与 r226530 修复、维护停滞之争（Anarcat/harold barker/pfSense/Bjoern 以 "(no) PF from OpenBSD 4.7" 定调）、Hartmeier 原作者介入释疑；b120（offset 6500-6999，2011-09~2012-12，40 条）**SMP 化 pf 与 projects/pf 合并**（Gleb Smirnoff 发布 CFT、宣告不并行维护两条线）、新版语法升级之争（Mark Martinec 指 NAT64/af-to 为真诉求）、PR kern/167057 立档（pf 4.5 已脱上游支持）、route-to panic 字节序根因链（Hartmeier）、ipfilter 钩子残留致 pf 崩溃；b121（offset 7000-7499，2012-09~2014-12，40 条）**合并后磨合期**（CFT 实测、pfctl/pfvar.h 需同步重建、Ermal 就 r240646 与 Gleb 争论）、**VIMAGE+pf 长期治理**（Craig 报 mbuf 析构崩溃 → Marko Zec 介入 → Nikos 负责 vimage 化 → PR 182964 → Matuska 补丁仅限 host 侧）、2014 末路线之争（Martin Hanson 主张移除多线程补丁 → Jim Thompson 长文辩护 → Bjoern 谈合并上游之难）、pf+dummynet 融合补丁、NAT before IPsec、IPv6 缺陷链；b122（offset 7500-7999，2014-01~2015-08，40 条）**Kristof Provost 接手 pf 维护**（计划清单、fastroute IPv6 panic 修复、scrub drop-ovl 废弃提案）、pf 前途之争（Jim Thompson 回应）、IPv6 校验和修复链（Ilya Bakulin / Ermal Luçi，修 PR 179392 & 172648）、**Nikos 的 r276747 将 projects/pf + VNET 合入 head**。
- **b119~b122 实测号段**：b119~b122 依次约 CL-RM-036**6xx**~037**0xx** 段（MAX 当日已推至 **037068**；并行会话持续占号，register 每次实测 MAX+1，勿写死区间）。
- **b123~b126（收官四批，恢复全文实读）**：b123（offset 8000-8499，2015-11~2017-08，43 条）kp 主政期缺陷清理——dup-to 复制包（PR 203715）、**pf+TSO 战役**（D3779，RootBSD 赞助）、altq 32 位带宽上限（PR 211730）、pf 分片表项不释放（PR 201519，time_second→time_uptime）、**pfil 对齐工程**（Franco Fichtner D8058 移除 fastroute/tag）、**panic 存废之辩**（Kajetan vs kp）；b124（offset 8500-8999，2017-01~2018-12，45 条）**full cone NAT 补丁折戟**（PR 219803，kp 网关开机即 panic）、UDP 的 reply-to 失效之争、VNET jail 性能疑云、**pfr_pool_get 崩溃链**、ALTQ 退场定调、enc(4) 与隧道过滤、GSoC 2017 测试工程；b125（offset 9000-9499，2018-03~2021-02，43 条）**pf 与 OpenBSD 上游分叉的正式定调**（kp 两度系统陈述可扩展性/语法/vimage 三大障碍，明言不引入第四种防火墙）、**rdr pass 状态 expire time 归零的长线追凶**（Andreas Longwitz → kp 疑溢出 → 归因 i386 cmpxchg8b → kib 驳 → 终定为 counter_u64_fetch 丢增量）、**RDR 后状态碰撞致报文丢失**（J David 建可复现仓库）、bridge 广播/组播重复计数；b126（offset 9500-9579，2021-01~2021-05，20 条，**全库末批**）**pf ioctl 的 nvlist 改造 RFC**（kp ↔ Cy Schubert，涉 struct pf_rule 双版本字段与 libpfctl）、pfctl 优化器段错误（Patrick Lamaiziere）、counters 表语义澄清、表项过度分配。
- **全文实读恢复（b123 起）**：新增 `_pf_batch_body.py <batch>`，读 `_triage_and_surveys/_freebsd-pf_<batch>_triage.txt`（pk|date|from|level|主旨）→ 抽全库正文至 `pages_large/_freebsd-pf_<batch>_body.txt`。**b110~b122 曾跳过此步（主代理仅凭 survey 的 head150 撰写），b123 起恢复 b107~b109 的全文实读，以提升当事人自述的引文保真度。**
- **b123~b126 判读流程**：一次生成 4 批 survey → 并行派 4 路子代理 triage（**明确要求剔除 bugzilla-noreply 的纯状态变更通知**，b124 剔除 282/500、b126 剔除 49/80；仅当正文含实质技术评论时才收并标 [PR转发]）→ 主代理抽全文逐封实读 → 亲撰数据模块 → 跑通用链。子代理报告须逐条标“引文从缺”（b123~b126 各 21/25/23/11 条）。
- **b123~b126 实测号段**：b123 CL-RM-037121~037163、b124 037164~037208、b125 037209~037251、b126 037335~037354（MAX 当日推至 **037354**；并行会话持续占号）。
- **141.11 现状**：文件内 ROW_MINE 块 **789 个**，与 pf claims 789 精确一致；git 暂存快照含 b107~b126 全部块。

### T2 DragonFly 战线（14 窗定点收编）
- **窗口池**：`_inventory/windows_df/chNNN_wNNN.txt`（14 个，主控预建，每行一个 pk；池规模 1000/64/1000/1000/448/1000/928/1000/1000/1000/1000/1000/1000/914）。源库 `03-原始史料库/11-邮件列表史料/04-dragonfly/duckdb/dragonfly_mail.duckdb`（72,062 封）。**池内 pk 与源库命中率 100%（实测 13,350 pk 全命中）**。
- **锚点方案**：`df_wNNN`（w001~w014，与池文件名对应；`_verify_batch.py` 已增补 `df→dragonfly_mail` 前缀映射，**纯新增键、不改既有行为**）。批次标签“2026-09-14 dragonfly_mail 战线”。判级与 pf 同规（L4 一手自述／L3 转引·次高·低信息量／不收纯求助·纯联络·自动转发通知），**40 满即停**。
- **T2 脚本族（新建）**：`_df_batch_survey.py <win>`（读池 → `pages_large/_dragonfly_mail_<win>_survey.txt`）／`_df_batch_candidates.py <win>`／`_df_batch_register.py <win>`（source_db=dragonfly_mail）／`_df_batch_mount.py <win>`（按 anchor 反查）／`_df_batch_outline.py <win>`（写回 214.1 三段式幂等块）／`_df_batch_ledger.py <win>`；正文抽取 `_df_batch_body.py <win>`（读 `_dragonfly_mail_<win>_triage.txt` → 全文，供主代理实读）。每窗新写 `_df_data_wNNN.py`。
- **w001 已收官（2026-09-14）**：ch214 fork 与启动，2003-08-22~2003-10-12，**40 条**（L4=38/L3=2，CL-RM-038908~038947），宿主 **214.1**（该文件内 ROW_MINE 由 4 → **44**）。verify 9/9、写回二跑 +0 幂等。史点：构建体系与发布流程跑通（dbsd.iso 156MB、corecode 每日快照）、**slab 分配器移植与 kmem_map 移除**（NO_KMEM_MAP + USE_SLAB_ALLOCATOR）、**syscall separation 长跑**（Reese 系列 1→6 部分与 linux COMPAT_43 移除四步）、安装器两阶段设计与 whomade 反向拆解构想、docs@ 列表、variant symlink 定位、Cisco CEF 式路由引擎提案、Kip Macy 的 checkpoint/restart 与 SIGCKPT/SIGCKPTEXIT。
- **台账**：dragonfly_mail claims **717**（实测）、coverage 10985/72062=15.24%、status“T2 窗口收编中”；batch_log `df_w001`（window/T2/池 1000）。**注意：`_df_batch_ledger.py` 已改为从 DB 实测 claim 数（勿用“旧值 + N”，该台账旧条目缺 claims 键）。**
- **余量**：w002~w014（13 窗，survey 已全部生成待用）。
- **锚点→章映射（由池文件名权威给定，勿凭猜）**：w001→ch214、w002→ch215、w003→ch216、w004→ch218、w005→ch219、w006→ch221、w007→ch223、w008→ch224、w009→ch225、w010→ch226、w011→ch227、w012→ch230、w013→ch233、w014→ch217。**各窗具体宿主子节文件须实读后按“主题＋时间”双门禁自定**（w001 定在 214.1）。

## 2. 未完成（按优先级）

1. **T1 六窗收官 —— 已完成（2026-09-14）**：
   - w003（openbsd_mail_e003）：键集修复（LEVEL/SELECTED 第 2 处 `205631`→`207345`；NARR 删 `76545`/`70139`）→ 40 条 CL-RM-033014~033053 → 206.1（0→40）、verify 9/9。写回已被并行会话收编提交为 `6a1b6cb26`。
   - w004（tech-kern_e004）：40 条 CL-RM-033496~033535 → 183.1（0→40）、verify 9/9。
   - w005+w006（freebsd-smp_e005 22 + freebsd-current_e006 22）：CL-RM-033536~033579 → 161.8（0→44）、双锚点 verify 各 9/9。
   - 记账：changelog id=1398/1399/1400；台账 openbsd_mail +40、tech-kern +40、freebsd-smp/freebsd-current 各 +22；batch_log×4；event_window 六窗全 done。
   - 脚本族：w004 复制 e003 五脚本为 `*_e004.py`；w005+w006 双锚点共用 `_register_smp.py`/`_mount_smp.py`（`e005|e006` 参数）+ 合并写回 `_outline_smp.py`（NARR 在 `_pf_narr_smp.py`，44 条）。记账 `_ledger_e003/e004/smp.py`。
   - **格式分水岭**：w004 起 NARR 不再带前导日期（依 RUNBOOK §二⑥），故 183.1/161.8 的 84 块格式正确；e001~e003 的 118 块仍带重复日期，待统一清理。
3. **T1 放量建窗**（侦察已给参数）：
   - **B/E/H 三窗已收官**（w007 OpenSSH 全球采纳→207.2、w008 LibreSSL 诞生→208.1、w009 FBI 传言考据→213.2，见 §1）；余下：
   - **D 窗未建**：接手书只给“2005-2010 六词命中 92/131/133/120/67/108 年”，**六个关键词未列出**，须回窗口蓝图《详细计划》§四取参数（D+E 原为一组）。
   - **A 窗不可建**：实测 openbsd_mail 在 1995-01~1996-12 仅 5 封、`%fork%` 命中 0，语料确实缺失（需补 marc.info current-users，或改以 1996-11 'Opening' OpenBSD 线程为锚）。
   - F/G/I+K/J 窗（**侦察失败/停止**）——参数未出。续接者按窗口蓝图《详细计划》§四自行圈定（每窗=年份+关键词组合，读池≤2000）。
   - 建窗工具已升级为 `_build_windows3.py`（总数≤CAP 取整窗／命中≥150 只取命中／否则命中+邻域），放量脚本族 `_gen_ob_candidates.py`／`_pf_narr_ob.py`／`_register_ob.py`／`_mount_ob.py`／`_outline_ob.py` 均以 `e007|e008|e009` 参数化。
4. **179.1 时段错位重排**（未跑）：把 1,646 条按 claim date 2005-2009 内外分桶；外桶（预计过半）按库×author 聚合归域，产出迁移建议报告。
5. **T2**：DragonFly 14 窗（侦察已给参数：214 fork 2003-07 精确窗/HAMMER 3,297 命中选峰值年/Dillon 断崖 2011 后勿后移）；点名库（questions/ports/doc/stable/chat/isp/arm/emulation）窗。**（freebsd-pf offset 收编已完成，见 §1，全库 100%。）**
6. **T3/T4**：其余 L1命中圈定；bugs 三库真人评论（freebsd-bugs bot 后实余约 110k，按需圈定；**T4 样本侦察未跑**）。
7. **keyword-hits 明细表复核 —— 已完成（2026-09-14）**：根因确认——v8 step4 的 regexp 退化为 match-all（15 个 Linux 列表的 dora/ane 明细行数**精确等于该库 messages 总数**、比值全 1.000），`dora`/`ane`/`ear` 三词合计 19,490,596 行 = 94.81%（相对 summary 真值膨胀 4,867×/4,970×/624×）。整改方案（含 SQL 与上限）见 `_inventory/keyword_hits_remediation.md`：先删三词+去重→994,314 行，再按 `detail_cap=2000` 重建→784,722 行。**未执行写操作，待批**。

## 3. 事故与教训（必须遵守）
- **keyword-hits 事故**：BSD 扫描脚本 glob 误扫 05-linux-kernel + 并发写 → 原 Linux 层明细误删；修复 v1-v7 连环错（ATTACH 参数化/事务冲突/本误判 summary 未刷新/漏 FROM/笛卡尔）；**v8（SQL 下推聚合）正确重建 summary 722 词**，但 step4 明细被过度填充 20.5M 行。→ 教训：写 index/registry 工程库前 tasklist 查 python 残留；扫描 glob 硬排除 05-linux-kernel；SUMMARY 语义要先读原构建脚本（hits=top10 稀有词明细、summary=全量）。
- **子代理余额耗尽**：8 路大派发 + 6 路后续共 14 路触发余额不足，多数 failed/stopped。→ 后续优先主代理直办（glm-1M 上下文可大段读），子代理只在确有替代价值时限量 1-2 路。**（2026-09-14 更新：通道已恢复，六路并行全部成功、均 <5 分钟——w004/w005+w006/B/E/H 正文实读 + keyword-hits 复核；任务单附完整约束并要求"未列入者报缺"，H 窗子代理如实报"相关仅 11 条"未凑数，质量可信。）**
- **写回块日期前缀重复（既有格式瑕疵，未修）**：`_outline_e0NN.py` 的 `text = f"{zh_date}，{body}"` 与 NARR 自带的前导日期叠加，产生"2003 年 9 月 18 日，2003 年 9 月 18 日，…"。**195.1/199.1/206.1 三窗共 118 块均如此**（e001/e002 已随 verify 9/9 通过而入库）。RUNBOOK §二⑥ 本意是"日期前缀由脚本加"、NARR 应以史实陈述开头。本轮为保持窗口间一致**未单独改动**；建议后续统一清理（去 NARR 前导日期或去掉脚本前缀，二选一，须三窗同时改并重跑 outline + verify）。
- **执行纪律**（续跑必守）：源库只读；已验证脚本不改、新脚本一律 Write；叙述与史学判断不外包；changelog/CL-RM 实测 MAX+1（并行会话持续占号——e001/e002 实测 25758/26106、e003 33014、e004 33496、e005/e006 33536、e007~e009 35510、pf b110 35600、pf b113 实测 35819 起，一日内 MAX 已推进逾万号）；verify 9/9；标记库四 hook（survey→1 候选→3 落库→4 batch_log）；事件窗写回后**延迟复验**防并行整文件覆写卷走（141.11/195.1/206.1 多会话热点）。
- **141.11 曾被置 assume-unchanged（已清）**：`git ls-files -v` 显示 141.11 带 `h` 标志（全库仅 2 个），导致其工作区改动（b109 的 +38 与 b110 的 +40 共 78 块）对 `git status`/`git diff` 完全不可见——**一旦有人 `git checkout` 该文件即会丢失**。本轮已 `git update-index --no-assume-unchanged` 清除并 add，暂存快照含 b109+b110 全部块（另含并行会话对同文件史观/辨析行的未提交改动，按"只 add 目标文件、不 commit"处理）。**续接者勿再对该文件设该标志。**
- **并行占号：seq 段不可假设（b113 实证）**：CL-RM 号段由并行会话持续抢占——b112 收在 35719，b113 register 实测起点却是 **35819**（中间被他人占走 99 号）。**mount 一律按 anchor 反查，勿传 seq 段**（`_pf_batch_mount.py <batch>` 已改为此实现）；register/ledger 的起始号必须实测 MAX+1，写死区间必然出错。
- **证据引文取法 —— 已整改（2026-09-14，主理人批准返工，changelog id=1441）**：
  - **旧约定（已作废）**：`_register_*.py` / `_pf_batch_register.py` 一律取 body **前 300 字符**作 evidence.quote。回复型邮件常以引述他人来信开篇，故部分 quote 实为**被引用的他人文字**。审计 pf 789 条显示 284 条（36%）受影响。
  - **新工具**：`_quote_own.py`——`own_quote(body)` 剥离前导引用块取作者本人文字。识别：归因行（`On <date>, X wrote:`、短式 `X wrote:`、两行式 `At <date>,` + `X wrote:`、各语种变体）、引用行（`>` 及 Gleb 式 `M>` 首字母前缀）、省略标记（`[...]`、纯 `---`/`===`）、bugzilla `--- Comment #N from ... ---` 头。策略：把正文切成“本人文字段”与“元信息行”，取第一个 **>=40 字且非问候语**（如 `Mark,`、`Hi,`、`Nate, good day.`）的段；无则取首个非问候语段；通篇引用则返回 None。`classify(quote)` 分 OK/ATTR/BZ/QUOTE/SUBJ/RESIDUE/EMPTY 七类。
  - **返工脚本**：`_quote_rework.py <anchor> --audit|--dry-run|--apply`（前缀→源库：pf=freebsd-pf、df=dragonfly_mail；单事务改 `evidence.quote` 并同步 `raw_source.content_hash`；**新引文须为正文子串**，否则保留原引文）。触发条件：非 OK 一律返工，**OK 但 <40 字者亦返工**（短引文多为误取问候语/署名所致——此条是第四轮才补上的关键修正）。
  - **结果**：五轮迭代收敛（280 + 117 + 9 + 38 + 0 条，另 df R.2 三锚点 6 条）。pf 最终 OK 785 / 残留 4（b108 的 1531832、1531853 与 b112 的 1533744 为**通篇引用无本人文字**，b122 的 1538808 为 **bugzilla 纯元数据**，均属“引文从缺”、保留原引文）；df_w001 与 df_eB/gB/qB 全部 OK。引文中位长度 264 字，<40 字者仅 3 条（均为本人原话本就简短）。
  - **register 已改造**：`_pf_batch_register.py` / `_df_batch_register.py` 的 `make_quote` **优先取作者本人文字，无本人文字时回退 body 前 300 字符**，后续批次自动生效。
  - **复验**：全 21 批（pf b107~b126 + df_w001）`_verify_batch` 各 9/9 PASS。
  - **余量/未决（待主理人批）**：全库扫描（56,531 条 evidence）显示除 pf_b*/df_* 外，另有 **493 个锚点、12,270 条**引文同类问题，集中在 usenet 战线（`ng40_s6~s10` 各 200-275 条非 OK、`ng_batch1_4` 647 条、`ng12/13/19/35` 各约 200 条）与 `full`（206 条）。**未擅自返工**——理由：这些锚点的 `anchor.split('_')[0]`（`ng40`、`ng12`、`full` 等）在 `_quote_rework.py` 的 MAILDB 映射中无对应源库，且 usenet dump 的正文结构（未必是邮件式引用）需先抽样验证规则适用性。**若要扩面，须先**：①抽样核验各源库正文形态；②为 `_quote_rework.py` 补 `前缀→源库` 映射；③分战线小批试跑。
- **跨窗去重（放量必守）**：同一封邮件只能有一个 claim——`_register_*.py` 以 `source_id` 判重并跳过。放量窗与既有窗池重叠时必须先剔除，否则 mount 的 `len(rows)==len(levels)` 断言会失败。实例：w007（B 窗 %openssh% 1999-11~2001-12）与已收官 w003（%openssh% 1999-12~2003-12）重叠 9 个 pk（3066/38195/69921/70084/97349/97729/207196/212546/257750，均已在 206.1），剔除后 43→34。**建窗后先跑一次 register --dry-run 看"跳过 source_id"数**，非 0 即需回 `_gen_ob_candidates.py` 的 EXCLUDE 补排除并同步裁剪 NARR。
- **`_backfill_traversal.py` D 段崩溃（既有 infra bug，未修）**：`_bsd_keywords_candidates.txt` 是词表而非 pk 表，D 段为其构造空 `rows` 并调 `con.executemany(UP, [])`，DuckDB 抛 `InvalidInputException: executemany requires a non-empty list of parameter sets` → 脚本在 D 段中止（E 段与末段台账校验未跑）。**实测无实质影响**：A/B/C 三段已提交，e003 40 候选升至 state=4、e001/e002 一并补齐；全部 4,385 条候选文件 pk 均已在 state≥3，故 D/E 本为 no-op。修法（留待主理人裁量）：`upsert_many` 内加 `if not rows: return`，或 D/E 段调用前加 `if rows:`。

## 4. 续接入口（先读先跑）
- 计划/蓝图：本会话内《详细计划》§四（A-I 合并窗蓝图）；`RUNBOOK_BATCH.md` §一已记录事件窗状态。
- 台账：`script/_db_row_mining/_tiering_assets/mail2d_lib_tiering.json`（openbsd_mail 条目已注 **+208 claims**）。
- 实读报告：`_triage_and_surveys/_tech-kern_e004_readreport.txt`（w004 40）、`_smp_current_readreport.txt`（w005+w006 44）、`_openbsd_e007_readreport.txt`（B 窗 43→去重 34）、`_openbsd_e008_readreport.txt`（E 窗 45）、`_openbsd_e009_readreport.txt`（H 窗 11）；keyword-hits 整改方案 `_inventory/keyword_hits_remediation.md`。
- 脚本族（每窗模板）：
  圈窗 `_build_windows2.py`（或按侦察参数手改 WINDOWS 表）→ survey `_gen_win_survey.py <windows 文件>` → 候选 `_gen_e0NN_candidates.py` → 叙述 `_pf_narr_e0NN.py` → 落库 `_register_e0NN.py` → mount `_mount_e0NN.py` → 写回 `_outline_e0NN.py` → 验证 `_verify_batch.py`（新库前缀先补 DB_NAME 映射，如 openbsd/e1 已补）→ 记账参照 `_ledger_e001.py`。
- 侦察报告留存：各子代理回报在会话转录（A+B+H/D+E 两路完整参数在最新文本；F+G/I+K/J/DF14 窗/pf1.0 考据因余额未产出）。

## 5. 环境
Windows/Git Bash；python duckdb 只读连接连源库（03-原始史料库/11-邮件列表史料/<族>/...）；写连接只开给 04-现代研究文献（HC/traversal/changelog）与 05-linux-kernel/db/ 索引库（figures/keyword-hits，沿例可写）。LM：glm-5.3-flash 上下文 1M。