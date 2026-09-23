# 长线总账（Live）· 防会话中断唯一入口

> **读这一份就够**：本文件是**三线**（shenyue 复核 / mail2d H3 / mail2d H1）的**唯一长期入口**，
> 新会话读到本文件即可续接，无须任何先前对话记忆。
> 细节归档（SOP 全文、裁定取证、坑速查完整版）在 `_PLAN_20260921.md`，本文件只留**活数据与命令**。
> 上游分线规程：`shenyue/review/_LONGRUN_PLAN.md`（复核线）、`script/_db_row_mining/_H3_RESUME.md`（H3 断点续跑书）、
> `script/_db_row_mining/_H1_LONGTERM.md`（H1 长线档案，含 H1 全套 SOP 与宿主分派口径）。
> Linux 邮件列表价值反推线（H6）：`03-原始史料库/11-邮件列表史料/05-linux-kernel/mining/02-遍历留痕/10-价值反推排序与选封管线.md`（价值反推排序+选封管线规程+五层面去重定义）
> 目录建议书全量复核线（jianyi2）：`shenyue/_work/jianyi2/_PLAN_JIANYI2.md`（分线计划＋恢复四步＋派单模板＋坑集）
> **冲突时以台账实测值为准，永不以本文档数字为准**（本文档是台账的副本，已实测漂移 3 次，见 §七）。

---

## 〇、一句话现状（2026-09-23 09:5x 实测，本轮：**H3 b006 波次四批全部全链闭环**（commit `c92ba6840`，`fhk_b027` 187＋`fcu_b006` 471＋`fdoc_b006` 366＋`fstb_b006` 656＝**1680 块入 7 宿主 +8400 行纯新增**，claim `CL-RM-194378~196057`，L4 1107／L3 573），四批 outline 幂等二跑均 **+0**、bookkeep 三零 **PASS**、等级门禁 **PASS 182873 块头 0 错标**；**H3 四库 b001–b006 十六批全部 committed，90000/551317（16.32%）**。叙述层 D2 臆造 **69→0** 全清零。子代理负载实测：**40 路稳定上限、100 路不成立**，防死等改扫盘（`review_logs/_watch_agents.py`）。**【2026-09-23 16:50 追记 H5 三线】**：主理人裁定**并行上限 40 路**（覆盖此前 50 路，写回 `_HANDOFF_H5.md` §10.23 沿革与 §10.24）；同窗**三批全链闭环**——`h5em_b520_1` 638 块 3188 行 `04cbf395b`（CL-RM-210715~211352）、`h5pu_b522_1` 629 块 3144 行 `260a7fd76`（CL-RM-211353~211981）、`h5hw_b518_1` 370 块 1848 行 `86ffd88d0`（CL-RM-211982~212351），三批 check／bookkeep 三零／audit 全绿，claim 序号水位 **212351**；仅 `h5arm_b521_1` 在途（649/650 行，余 20 处叙述长度瑕疵），断点与命令见 `_HANDOFF_H5.md` §10.24。新坑：**插入行数≠块数×5**（em 3188＝638×5−2、pu 3144＝629×5−1、hw 1848＝370×5−2，首块复用锚点上方既有空行，勿再拿 ×5 当硬断言）

| 线 | 游标（台账实测） | 下一批 |
|---|---|---|
| **shenyue jianyi2**（《给我自由》目录建议书全量复核线，分线计划 `_work/jianyi2/_PLAN_JIANYI2.md`） | 阶段 A 全毕（通道锁定 4 路可用／解析 3412 条双连续／转录核对零编造／69 批派发单落盘）；**波 1 批 0001–0040（40 路）在途**（2026-09-23 19:1x 派出，产出 `shenyue/_work/jianyi2/batch_*.out.md`）；LANDED 0/69 | 波 2 批 0041–0069（29 路）**待波 1 ≥20 批 LANDED 后派**；全部落盘后 `_merge_volumes.py` 拼回 `shenyue/jianyi_by_volume2/`（00-总览＋37 卷文件）→ 终验 3412 条全覆盖 |
| **shenyue 复核** | A 类 **692/692 全闭环**（16 批）｜B 类 **550/748**（0027 已落账 seq 27）｜C 类 **0/1972** | `BATCH-0028`（B pos 551–600，O-2082 起） |
| **mail2d H2** | `freebsd-ports` **36000/191637**（fpo_b151–b162 `[(0, 36000)]` **单段连续无缝**）｜`freebsd-bugs` **3500/192683**（`[(0, 500)]` fbug_b171 ＋ `[(137970, 140970)]` b172/b173/b174/b174e/b175/b176/b177）｜`-net` **45000/73645**｜`-chat` **43869/43869 已整库闭环** | **本轮三批全链闭环 `04c9af3aa`（+5650 行＝1130×5，七宿主）**：前情 `6809bb8a2`／`cee1e72ec`／`27cfc5725`／`333434176`／`529468ce9`／`1029cb38c`／`b3f04bfb6`／`a181c7489`／`4ecb05710` 仍在册。**fpo_b160 405 块**（89.2=358／89.4=37／90.7=4／90.9=6）＋**fbug_b176 309 块**（88.1=276／88.6=5／88.7=28）＋**fpo_b161 416 块**（89.2=350／89.4=53／90.9=8／90.7=5）；三批 outline 幂等二跑均 **+0**、bookkeep **缺块／claim_id 不符／重复 全 0 PASS**、**audit PASS：引用块头 147087、错标／悬空 0**（142148 → 144258 → **146692**（b177 ＋325）→ **147087**（b162 ＋395））。**再两批闭环**：`fbug_b177` **325 块**（L4 199／L3 126，收率 65%，88.1=281／88.6=17／88.7=27）commit **`19c170ac9`**（+1625＝325×5）；`fpo_b162` **395 块**（L4 320／L3 75，收率 13.2%，89.2=309／89.4=73／90.6=8／90.7=2／90.9=3）commit **`795b58ec5`**（+1975＝395×5）；两批 outline 二跑 +0、bookkeep 三零 PASS。**本轮共 5 批 1850 块＝9250 行＝1850×5**。本轮新增缺陷与处置：① **叙述包静默死亡的包体阈值再次实证**——b160 p5 在 67 条／73 KB 两次静默死亡（第一次停在 10 行、第二次宣布「分批写」后中断），拆 **p5a 33 条／33 KB ＋ p5b 34 条／36 KB** 重派后 67 条齐；② 🔴 **叙述手把正文转义序列原样写入**——b176 p6 的 pk **1049153** 叙述含控制字符 `\x0f`／`\x1e`（正文里的 `\036FP017` 被渲染成控制字节），`_merge_narr` 用 `splitlines()` 在该处断行，该条被截成 43 字入盘并连带报 2 条「字段数 1」幻影行；**`wc -l`／`split('\n')` 自检查不出**（它们不认这些字符，Python `splitlines()` 才认），已外科重写为「反斜杠036FP017」纯文本、全 22 份分件扫描控制字符确认仅此 1 条、重跑 merge 得 **违规 0**；③ 🔴 **读手摘要里的通配符星号**——b161 p8 的 `*_DEPENDS` 触发候选合并器 **ABORT 不写盘**，已改写「子 DEPENDS 变量」；④ **字节 vs 字符**：`awk length`／`wc -m` 在 C locale 下数 UTF-8 字节（一汉字 3 字节）会系统性误判（曾致 40 余条「太短」静默入盘、读手与叙述手均报「越限 0」），摘要与叙述长度**只能用 Python `len()` 实测**。**下一批已预建**：`fbug_b177`（offset 140470／500 行，pk 1049169–1049669，1995-08/09/10，5 份 digest×100 行，宿主 881/886/887，**5 路读手在途**）＋ `fpo_b162`（offset 33000／3000 行，pk 1585798–1588835，2006 全年，12 份 digest×250 行，宿主 891/892/894/906/907/909 禁 883，**12 路读手在途**），两批 pk 端点均与前批紧贴无缝、容器行 0（已实测断言）。**再四批闭环（06:1x–06:45）**：`fbug_b177` **325 块**（收率 65%）`19c170ac9`（+1625）＋ `fpo_b162` **395 块**（收率 13.2%）`795b58ec5`（+1975）＋ `fbug_b178` **311 块**（收率 62.2%，88.1=263／88.6=12／88.7=36）`a915159b7`（+1555＝311×5）＋ `fpo_b163` **369 块**（收率 12.3%，89.2=301／894=53／90.6=1／90.7=9／90.9=5）`a01a852e0`（+1845＝369×5）——四批 outline 幂等二跑均 **+0**、bookkeep 三零全 **PASS**、**audit PASS 154379 块头、错标／悬空 0**（146692→147087→154010→**154379**），宿主文件全部纯新增零删除零裹挟（pathspec 提交）；claim 区间 b177 `CL-RM-166565–166889`、b162 `CL-RM-166890–167284`、b178 `CL-RM-170220–170530`、b163 `CL-RM-170531–170899`；**台账已回填**（`1ece4135e`）：ports 判读 **39000** `[(0,39000)]` 单段连续、bugs **4000** `[(0,500)]`＋`[(137970,141470)]`；queued 已预建 `fpo_b164`（39000–42000，全 2007，制度性辩论密度最高：Port System Re-Engineering RFC/P×71／ports freeze duration×60／Limitations of Ports System×58／Ion3 license violation×54）＋ `fbug_b179`（141470–141970，1995→1996 2.1→2.2 过渡，ATAPI CD-ROM／DOS 分区共存安装／kern-929 NCR／fixit floppy），12＋5 路读手待派。**本轮新增纪律与工具**：① 🔴 叙述手会**持续重写 TSV**——merge 前必须重新实测盘上违规数（b178 p6 由 3 条 <60 自行补至 0，中间态一度 5 条，早前快照已失效）；② 🔴 **宿主口径裁定**：894＝「构建侧」（构建工具链）、906＝「组织侧」（端口树结构与类别批评＋跨发行版对照＋许可证标注政策）、907＝ports 冻结／解封政策投票与归属之争——已固化入 b163／b164 任务书；③ 新增 `_pad_short_narr.py` 短叙述外科补齐（dry 纯读、断言命中数与行数不变、替换后全文件复检，首跑即拦下 5 条越限）；④ **b163 p7 被 `rpm exhausted` 限流零产出**，重派 340 秒即完成，印证「写盘优先＋早写早覆盖」纪律有效 |
| **mail2d H3** | 四库 **74000/551317（13.42%）**：`freebsd-hackers` **50000/201463**｜`-current` **8000**｜`-doc` **8000**｜`-stable` **8000**（四库 b002＋b003＋b004 十二批**候选阶段全部 register**；b004 内 **fhk_b025 已全链闭环至 commit**，余三批叙述在途） | **b002 波次四批全链收口（2026-09-22 03:3x–05:0x）**：`fhk_b023` 257 块入 5 宿主 `bb31a6d93`、`fdoc_b002` 441 块入 5 宿主 `cd1ac595d`、`fcu_b002` 433 块入 5 宿主 `f6b9b9a51`、`fstb_b002` 554 块入 4 宿主 `b67e08375`（**合计 1685 块**），四批 outline 幂等二跑均 **+0**、bookkeep 三零 **PASS**、等级门禁 **PASS 145813 块头 0 错标**、`mail2d_read_ledger.json` 已刷已提交。**专名门禁四判据分流定形（`_triage_propernoun.py`，主代理 solo）**：A body 命中／B `len(body)>=1395` duckdb 截断／C 归一化变体 → KEEP；D1 读手摘要有 → KEEP 但登记债务；D2 摘要也无 → 真臆造定点改写。四批 264 命中 → **22 条真臆造改写**（含 2 例张冠李戴署名：`1108645` Simon→Marc、`2576751` 删 Eric Brunner）＋**12 条判定保留**（mbox 折行切词、码点变体、词首缩写、原文拼错四类假阳）＋**D1 债务 45 条只登记不追补**。本轮新坑：🔴 **坑⑧** `_fix_narr_len.py` 首版「已应用」分支 `continue` 未先 append 静默丢行（p1 65→64、p4 64→42），已修为先 append 再 continue＋写盘前 `assert len(out)==len(lines)` 硬阻断；🔴 **坑⑨** 中文长度手估系统性偏低 5–40 字，fcu_b002 首轮 11 条 <60 全靠回正文补实词清零；🔴 **坑⑩** 叙述手在回报完成后仍重写 TSV（fcu p3 晚 2m35s、fstb p8 晚 0m50s、fhk p1/p4 晚 11m），**以 `_narr_pK` 最新 mtime 为权威、稳定 ≥2 分钟才 cp→merge**。四批 spec 实测均 **13 键宿主**（旧「fcu 15 键」与 spec 不符，作废）。明细见 `_H3_PROGRESS.md` §7.7–§7.9。**b003 波次四批已建 spec＋dump＋8 份 digest（250 行/份，2026-09-22 上午）**：`fhk_b024` offset 46000 pk 1318741–1320740／`fcu_b003` offset 4000 pk 1027445–1029462／`fdoc_b003` offset 4000 pk 1110553–1112563／`fstb_b003` offset 4000 pk 2578642–2580643——**四批 pk 区间均与前批首尾相接零重叠**（fhk_b023 止 1318740、fcu_b002 止 1027444、fdoc_b002 止 1110552、fstb_b002 止 2578641），容器行四批实测**均 0**，四批 spec 均 13 键宿主，`queued: true` 已标记（台账不计为已读）。**⚠️ 旧记「`_batch_fhk_b003.json` offset 46000 已预建」作废**：实测 `fhk_b003` offset 是 **4000**（09-19 已完成落库、claim 532 条），hackers 的下一批是 **fhk_b024**。**12 路读手在途**（四批各 p1–p3，任务书 `_READ_TASK_b003wave.md`）。**✅ b003 波次四批已于 2026-09-22 全链收口至 commit**：`fstb_b003` 642 块 8 宿主 `e845c8e54`、`fdoc_b003` 443 块 4 宿主 `e845c8e54`、`fcu_b003` 489 块 3 宿主 `e845c8e54`、`fhk_b024` 295 块 6 宿主 `6f4801552`（**合计 1869 块**），四批 outline 幂等二跑均 **+0**、bookkeep 三零 **PASS**、等级门禁 **PASS**、`mail2d_read_ledger.json` 已刷至 **66000**。**宿主题旨裁定定形**：**1067 是「时代型」宿主**（「freebsd8x 的开发者群体与虚拟化团队」，2009–2010），故 fhk_b024（2014–2015）的 1067 项外科改挂 1588（`_rehang_fhk1067.py`，只改第 2 字段故块数与 claim 序列均不变）；**1069 是「主题型」宿主**（实为「设备驱动移植／新硬件支持」，「8-x 时期」只是章标签），实测 fstb_b003（2000 年）的 1069 项是 loader/ed 卡/ECP 并口/CD-ROM 检测、fhk_b024 p4b 的 1069 项是 qemu bsd-user/KVM/i915kms/Realtek 8168G——**两类都不改挂**，fcu_b003 的 333 项 1067（2009 年）时代吻合亦不动。**本轮两处工具缺陷**：🔴 `_apply_d2.py` 首版按行 `edits[f] = cur` 覆盖，同文件只活最后一行，自报「合计 30 条」实落 1 条（18/23 条 D2 改写静默丢失），已改为按 `(tag, part)` 聚合后一次性写盘＋`assert total == len(order)`；**教训：脚本自报成功数不是权威，必须读回目标文件按 pk 复查**。🔴 `_join_halves.py` 整份覆盖 pK，会冲掉此前已施加到 pK 的改挂——**顺序必须是先 join 半份、后改挂**。**大纲块漂移**：fdoc/fcu 的 D2 改写在 `outline --write` 之后才生效，23 个已提交块仍含旧文本（「phk 联系方式已过时」「build options」），块数与锚点均未变故不走全量重建，用 `_fix_outline_blocks.py` 定点换前缀（100.18×11／98.6×3／106.7×8／106.9×1），全库 ROW_MINE 总数稳定 177515。四批 D2 共 30 命中 → **3 KEEP＋29 REWRITE**；3 条 KEEP 均为可证修正（fcu 1027678 西里尔 `Андрей Смагин`→拉丁 Andrey Smagin、fdoc 1111951 正文印 UTI V24 应为 ITU V24、fhk 1318999 正文印 nss_winbins 应为 nss_winbind）。29 条改写四因：把全名替成缩写／句柄（phk→Poul-Henning Kamp、thompsa→Andrew Thompson、Smørgrav、LOR→lock order reversals）、外推正文没有的词（NCQ、traceroute、qemu、OOM killer、pull request 623…）、事实方向反了（1029312、1112233 rc.c→rc.conf、1027532 ada0 光驱）、漏写本封实际内容（1027632 只叙述了被引的旧信、1319357 叙述的是回帖答案而非本封）。明细见 `_H3_PROGRESS.md` §7.13–§7.14。**✅ b004 波次四批已建 spec＋dump＋24 份叙述包，候选阶段全链闭环（2026-09-22 下午）**：`fhk_b025`（offset 48000）380 条／`fcu_b004`（offset 6000）526 条／`fdoc_b004`（offset 6000）292 条／`fstb_b004`（offset 6000）617 条，**合计 1816 条 register 落库 `CL-RM-177300–179114`**，四批 spec 均 **13 键宿主**、容器行实测 **0**。**✅ `fhk_b025` 已全链闭环至 commit `c2b1ef407`**：24 份叙述齐（merge **380/380、缺 0、多 0、升序 True、违规 0**，长度 71/140/avg 117.3），宿主分布 **1588=298／1069=82**、**1067 零用**（时代型纪律在 24 路叙述手中独立成立）；D2 专名门禁 6 命中 → 主代理 solo 裁定 **6 条真臆造全部改写**（含 `1321646` 证据等级标记「（L3）」泄漏进叙述正文、`1321075` 正文只有 `Hi Eric` 却写成 McCorkle、`1320918` 单位臆造 MB、`1320751` 正文只有 `Michael` 无 `Fuckner`）＋**1 条 KEEP**（`1321849` body 有 `restoring`、token `restore` 属形态学变体）→ **D2 清零**；outline **+380**（106.9 +82／158.8 +298）、幂等二跑 **+0**、bookkeep **缺块／claim_id／重复 全 0 PASS**、等级门禁 **PASS**。**🔴 新增真门禁 `_chk_narr_b004.py`（exit 码）**：`_chk_mount_narr.py` 42 行只 print **从不 exit 非零**、`_merge_narr.py` 阻断集只有「缺文件/CRLF」，两者皆 fail-open——真门禁校验缺文件/BOM/CRLF、3 字段、长度 60–140、尾标点、禁字符、**pk 集合与顺序==narrpkg**、表外宿主键、**按批禁 1067**（`NO1067 = {fdoc_b004, fstb_b004, fhk_b025}`），fcu_b004 允许 1067 故不在表内。**🔴 register 后漂移裁定：按 register 推进、不 purge 重建**——读手在 register 之后仍重写候选分件，致分件与已 register 集合漂移（fhk 0／fcu 丢 1＝`1029772`／fdoc 0／**fstb 丢 24 加新 2**＝`2582478`·`2582502`）；抽样 12 条确认所丢 pk 全在本批 digest 窗口内为真 pk、新增 2 条亦为真 pk，故**不 purge**，漂移只登记不追补。三条理由：①读手是摘要级误归属删行而非 pk 造假；②叙述写自 1400 字正文而非摘要，摘要错只致块偏薄、不致块错；③claim 617==outline 617 保持 join 干净，purge 重建须重跑 body/split/24 叙述手。**任务书宿主裁定已固化（1067 时代型 vs 主题型第一次在派单前生效，免改挂）**：`fcu_b004` 全 2009 → **1067 允许且应当**（8.x 开发团队／虚拟化／core-team）；`fdoc_b004` 2004–2005 → **1067 禁用**，主力 10018（文档协作/手册页评审/术语统一）＋986（发布文档/手册构建）＋10110（2005 个人技术）；`fstb_b004` **双峰年段**（p1–p10 2000 年→986/10110，p11–p24 2023–2024→1588，1069 主题型任何年份可选）→ **1067 全程禁用**，且逐份在任务书里写死主宿主＋「2000 年条目不得写成 6.x/8.x 语境」。**在途**：20 路叙述手（fcu p5/p9–p14、fdoc p9–p15、fstb p5/p6/p9–p13）＋ `fcu_b004` **p7 补件 11 条**（p7 只交 11/22，缺失 pk 已点名 `1030096,1030101,1030103,1030106,1030111,1030115,1030117,1030119,1030127,1030128,1030131` 重派至 `_narr_p7b.tsv`，主代理自行拼接——p7 叙述手自报「收到分件更正」而我只派过一次，属子代理幻觉指令）；三批已落盘部分 **全数通过** `_chk_narr_b004.py`（fcu p1–p4/p6/p8、fdoc p1–p8、fstb p1–p4/p7/p8）。**`rpm exhausted` 软限流 4 路**（fcu p5、fcu p3 再派、fdoc p10、fstb p10）——按主理人裁定为软信号不降级，等窗口冷却后重派。下一动作＝21 路叙述齐 → `_merge_narr` → `_chk_narr_b004 --all` → 逐份 triage → solo D2 裁定 → outline → bookkeep → 等级门禁 → pathspec commit → `_build_read_ledger` |
| **mail2d H4**（五库 459,135 封长线，**分线计划 `script/_db_row_mining/_H4_LONGTERM.md`**（2026-09-23 新建，自包含：全景表＋批号规则＋SOP 八步＋收口链两前置＋派单规程＋密度基准＋缺陷族 12 类＋门禁盲区 7 条＋坑集㉛–㊵＋验收七条）） | 五库 **94 段 459,135 封，已读 35,000（7.6%）**——全在 `tech-kern`（**81,326 封／17 段／7 段闭环／剩 46,326**，自动化 0%）；余四库 read_effective **全 0**：`openbsd_mail` 154,119（31 段，自动化未测）／`netbsd-bugs` 98,119（20 段，35.8%）／`freebsd-gnome` 66,573（14 段，53.0%）／`pkgsrc-bugs` 58,998（12 段，**98.6%** 须先建机械预筛器） | **段 7 `tk_b145` 已全链闭环 commit `0d1f27db9`**：4,304 块入 12 宿主 **+21,520 行＝4304×5**，claim `CL-RM-213002–217305`，check 越界0违规0／register COMMITTED 四表 join 4304／outline 二跑 **+0**／bookkeep 三零／audit PASS 199,767 块头 0 错标；26 条 <60 字短行回源逐封重写，4 条内容级缺陷修正（164448/164451 张冠李戴、163910/163911 正文构成判反，均在 register 前改故未污染 claim_text）。**段 8 `tk_b146` 已建批已 dump 已补 pk_range 已拆 40 份**（offset 35000、n 5000、**pk_range [164729,208118]**、17 键宿主加 1831/1841），**三年代带** A 164729–167777（3049 封 2013-11~2015-08）／B 190453–190792（340 封 2002-07 NetBSD-2.0 SMP）／C 206168–208118（1611 封 2016-01~2017-01）；分件带归属 p1–p24 全 A／p25 混／p26-p27 全 B／p28 混／p29–p40 全 C（仅 2 份混合）；**双查 PASS**（已登记 tag tk_b138–b145 对应 pk 108235–164728 与窗口零重叠；`ROW_MINE: tech-kern.messages.*` 40,690 锚中落窗 0 条）；哨兵日期 50 封、空正文 31 封。**本轮新坑**：① 🔴 **坑㉟ `tempfile.mkstemp` 的 fd 必须 `os.close(fd)`**，否则 Windows 上 `os.replace` 报 WinError 32（不是并发锁，是本进程自己占着源文件，连试 4 次全失败）；② 🔴 **`ROW_MINE` 锚点格式是 `<lib>.messages.<pk>`**，不是 `tech-kern_<pk>_<pk>`——用错模式会**误报 0 命中**（实测踩过一次）；③ 🔴 **claim 库 join 链修正**：`anchor` 在 **`evidence`** 表不在 `claim` 表，且 tech-kern 的 anchor 是**批号 tag**（`tk_b145`）非 pk 区间，故「窗口是否已登记」只能靠 spec 的 `pk_range` 比对 | 写 `_READ_TASK_tk_b146.md`（克隆 tk_b145 版改 9 处＋三年代带纪律）→ 40 路读手 → `_merge_cand.py tk_b146 40 164729 208118 --srcdb` → check；调度＝tech-kern 余 10 批打完再转 openbsd_mail，pkgsrc-bugs 排最后且必须先建机械预筛器 |
| **mail2d H1** | `freebsd-questions` **116000/472235（24.56%）**；**58 批已提交**，claim **7,333 条**＝入纲块 **7,333 块**（唯一 pk 零缺口） | `fq_b059`（offset 116000，n 2000，**尚未建批**）；上批 `fq_b058` commit `0c23df04d`（171 块入 5 宿主 +855 行，CL-RM-197952–198122，三门禁全绿、audit PASS 180776 错标 0、drift 零漂移、锚点 7333） |
| **mail2d H5**（200K 派发线，`_h5_state.json` 28 库 101 批） | **全库闭环 10 个**（x11/ipfw/desktop/cu/acpi/smp/i386/sparc64/ppc＋tech-pkg 三批＋freebsd-ppc 三批） | tech-pkg 批1 `1c3015051`（1141 条）＋批2 `b34760350`（1477 条）＋**批3 `h5tp_b528_3` `1204cc175`（152 条 CL-RM-161258–161409，1892=144／1852=8）已 committed**，+760＝152×5、幂等二跑 +0、bookkeep PASS、audit PASS 140815 块头 0 错标；**追溯订正 `4b3958771`**（叙述手 02:08 回报晚于提交，284538 由 185.2 改挂 189.2、284581 叙述删不可核断言，外科改挂 +6/−6）；🔴 **「漏读缺口」经比对判定为伪缺口，已整批 purge 回滚**：库首 1500 行（offset 0–1499，pk 270703–272459）并非未读——2026-09-11 另一会话已处理并 152 块入纲 **179.2**（commit `85a71de45` 及其前序提交）；本轮误判后建批 `h5tp_b528_0`（3 读手 374 条、register 281 条 CL-RM-162346–162626），比对发现 **93 条与 179.2 已入纲块完全重复**（同 pk，仅 claim 编号与宿主不同），继续推进会造 93 个跨章重复块并把同一时间窗拆散两章，故 `_purge_batch.py h5tp_b528_0 281 --apply` 四表全清（anchor 残留 0、库内 MAX 回落 162345），179.2 一行未动；✅ **tech-pkg 整库闭环终态＝13931 封全量、claim 2922 条＝入纲块 2922**（179.2=152／189.2=2666／185.2=48／187.6=37／188.2=19，零孤儿零重复），**直接转余下 18 库**；教训＝建批前必须先全库核对 claim 与 ROW_MINE 块的实际 pk 覆盖、不能只信本线 offset 游标；**freebsd-alpha 批1 `h5alp_b514_1` 在途（2026-09-22 上午）**：库内序 0–5999，12 路读手 **1122 候选**（L4 1016／L3 106，收率 **18.7%**——远高于 H5 其余库 3–8%；freebsd-alpha 是专门架构列表、几乎每封都是平台工程一手证言，**该密度待抽样复核是否读手过度抽取**）；`register --apply` **COMMITTED 1122**（`CL-RM-165027–166148`，跳过 source_id 0／hash 0，quote 反查 1122/1122，四表 join 1122，claim_map 1122）；body 1,194,793 B；16 叙述包已切（70–71 条／包，各 66–91 KB，缺正文 0）；**宿主 4 键 `911,981,10112,1059` 年代分挂**（≤2000→91.1／2001–2005→98.1／2006–2007→101.12／≥2008→105.9；退役主题不论日期一律归 105.9），分布 **911=345／981=621／10112=96／1059=60**，退役主题覆盖 12 条，0 源库缺行；🔴 **本库 pk 与日期完全无序**（`pk = CAST(messages.id AS BIGINT)` 是导入自增号与时间无关，窗口跨 1997–2010），故每批必建 `_gen_hostkeys_b514_1.py` 按源库日期＋退役主题确定性指派宿主、叙述手**只抄不派**（退役正则须绑 alpha 语境，裸 `has been retired` 会误伤 833326／833329）；🔴 **本轮自伤：读手派单漏写「摘要必须中文」，6 份英文摘要（60–126 字）被 check 拦**，已 SendMessage 回收改中文并写死派单必填项；🔴 **3 路读手卡死零产出**（p1 21.7／p2 21.4／p6 19.5 分钟无文件写入）→TaskStop 后 p1 改派「翻译员」（只译已判读摘要、不重读 digest）＋p2/p6 重派；p10 两次截断（签名「Let me rewrite with strictly ascending unique pks…」）→主代理 `_fix_p10.py` 接手外科修正；🔴 新增分件预检门 `review_logs/_chk_narr_parts.py`（在 merge 之前逐份比对 narrpkg＋hostkeys，把 `_merge_narr.py`「报而不拦」的越限／禁字符／尾标点／宿主错挂拦在分件层，已用 h5tp_b528_3 验证 152 行 0 违规；本次拦下 p5 831745 叙述 57 字＋复核 p10 曾缺 3 行）；**16 路叙述手 11 分钟全落盘**、预检／merge 0 违规、`fix_tail dry` 剥离 0；`outline --write` +1122、幂等二跑 +0、bookkeep PASS（缺块／claim_id／重复全 0）、等级审计 **PASS 145813 claim 块头 0 错标**、四宿主 diff 纯新增 **5610＝1122×5 零删除**、1122 个 `ROW_MINE: freebsd-alpha.` 块 1122 唯一 pk 与候选集合全等且块结构 0 异常 → **批1 已 committed `daa3a2a11`**（91.1=345／98.1=621／101.12=96／105.9=60），`_h5_resume --mark` 置 committed（1/3）；🔴🔴 **本批读手摘要严重失真：56 条（5.0%）摘要与正文张冠李戴**（p15 17／p16 11／p12 10 最重，p1/p2/p3/p6/p7/p11 为 0），四类形态＝CI 日志冒充人工讨论、`>` 引用句当发帖人原话、事实方向相反、Tinderbox 噪声；叙述全部以正文为准故**书内正确**，仅 `claim.claim_text` 残留错误文本 → 按既有裁定**只登记不追补**（§10.8 已列全 56 个 pk）；同轮实测源库噪声：body<10 字 0、<80 字 1、`tinderbox` CI 邮件 12 条（1.1%）、源库缺行 0——**低噪声率≠低错位率**；🔴 **本库 18.7% 收率仍待抽样复核是否读手过度抽取**；**整库分批实测 16,943 行＝3 批**：批2 offset 6000 n 6000 pk 836523–842550（主体 1999–2000，年份 1995×1/1998×1/1999×1487/2000×3178/2001×1333）、批3 offset 12000 n 4943 pk 842551–847506（主体 2001–2002，年份 2001×1778/2002×2686/2003×476＋畸形 `0102`/2022/2023 各 1 条须兜底归众数宿主）；⚠️ 批2/批3 与批1 性质不同（年代高度集中），但**仍不可跳过 `_gen_hostkeys`**（退役主题不论日期归 1059＋畸形日期兜底）；✅ **批2 `h5alp_b514_2` 全链已 committed `2d53346e7`（2 文件 +5330＝1066×5 零删除）、`_h5_resume` 置 committed（2/3）**：读手 12 分件 1144 候选 → 脚本统一施引文主导过滤 **−78**（420 字截断把发帖人自有文字挤出可见窗，只余 `>` 引号块）→ 回归该过滤**误删的 14 条 GNATS PR 通告**（`alpha/NNNNN:` 主题，`>` 渲染的是提交者本人请求文本，发帖人即作者，属真史料；无过滤前快照故 14 条摘要由源库正文逐条重建补回）→ 再删读手臆造 14 条 → **1066**（L4 961／L3 105，收率 17.8%）；`register --apply` COMMITTED 1066（`CL-RM-167285–168350`，quote 反查 1066/1066，四表 join 1066）；宿主 `_gen_hostkeys_b514_2.py`（年份窗 1990–2030，退役主题 0 命中）→ **911=788／981=278**，101.12 与 105.9 本批无份；body 1066 块 0 缺、16 叙述包 0 缺正文；16 分件预检 0 违规、merge 1066/1066 缺 0 多 0、`fix_tail dry` **剥离 0**（本轮叙述手全数遵守尾标点禁令）、check 0 违规、outline 幂等二跑 **+0**（91.1 refs 3571→4359／98.1 1349→1627）、bookkeep 全 0、等级审计 **PASS 148153 块头 0 错标**；🔴🔴 **批2 摘要错位率 16.4%（142 条／可回报 13 份），为批1 5.0% 的约三倍，且分布极不均**（p7 单份 **48／67＝71.6%**、p5 15／67、p11 14／66、p13 11／66、p14 10／66，而 p3 3／67、p12 2／66）——p7 那一份的典型形态是摘要人名与内容同时全错、内容实为**另一个 pk** 的邮件（839442 抄 839504、839484 抄 839468），即 digest 分段与 pk **整段串行**（同 §10.8 根因，批2 因年代集中而错位更密）；叙述一律以正文为准故**书内正确**，仅 `claim.claim_text` 残留错误文本 → 同批1 裁定**只登记不追补**（register 按 `source_id+content_hash` 幂等，改写会因同 hash 静默 SKIPPED）；**累计 `claim_text` 债务 ≈ 288+ 条**（tech-pkg 90+／alpha 批1 56／**批2 142**）；🔴 新固化 `review_logs/_filter_quote_dominant.py`，但**回验证明启发式不可自动剔除**——批2 已人工回源确认无误的 1066 条里有 **302 条（28.3%）**会被判「自有文字不足 60 字」，其中 164 条落在 0–9 字桶，故脚本只出**疑似清单** `<tag>_quote_suspect.txt`、**不写回候选**，裁决交给叙述阶段逐条回源；已建 `review_logs/_gen_hostkeys_b514_3.py`（**年份窗收紧 1990–2011**，因 freebsd-alpha 邮件列表本身 2010-11 已退役、带外年份一律判导入戳失真，众数宿主 981；带外 3 条 845584 是 spam、844464／847475 是 Volker Stolz 的 GNATS PR 实为 2002 年）；🔴 子代理被 `rpm exhausted` 限流反复打断（叙述手 p6/p10、读手 part5/6/8/9/10 各一次，产物多已落盘但需主线回源复核）；入口 `script/_db_row_mining/_HANDOFF_H5.md`（§10.1 台账＋§10.2 源数据缺陷＋§10.3 流程纪律＋§10.4 伪缺口教训＋§10.5 合并后重写纪律＋§10.6 宿主裁定＋§10.7 派发缺陷＋§10.8 摘要错位 56 条＋§10.9 分批实测＋§10.10 分件预检门＋§10.11 420 字截断引文主导过滤＋§10.12 错位率三倍教训）＋记忆 `h5-longhaul-200k-dispatch-20260921` |
| **mail2d H6** | Linux 邮件列表价值反推（九未处理库选封入库管线已建，未执行）；linux-man 实测密度 7.29% 全场第一 | 管线就绪（5 脚本+3 文档），待授权执行第一批 linux-man 入库 |

**H1 真值**（`script/_db_row_mining/_H1_LONGTERM.md` 为入口，状态机 `_h1_state.json`，2026-09-23 10:10 实测）：
`freebsd-questions` 全库 **472,235** 封，共 **237 批**（÷2000，末批 b237 为 n=235），
**58 批 committed**（fq_b001–fq_b058）+ 179 批 pending；已判读 **116,000**（24.56%），
claim **7,333 条**＝入纲块 **7,333 块**（唯一 pk，零缺口，落 27 个宿主；
五宿主 92.1 **3,850**／100.16 **2,880**／100.17 **343**／92.4 **128**／92.3 **19** 小计 **7,220**＋历史落点 113）；
累计收率 **6.32%**，近 6 批均值 **8.90%**；宿主 `921,10016,10017,923,924`；密度带 **3–8%**；
下一批 offset **116000**（`fq_b059`）；锚点唯一计数 **7,333**（`ROW_MINE: freebsd-questions.messages.*`，零重复）。

**H3 四库真值**（`script/_db_row_mining/mail2d_read_ledger.json`，实测 2026-09-23 09:5x，
b006 波四批已提交 `c92ba6840`）：

| 库 | 全库 | 已判读 | 剩余 | ≈批数 | 宿主口径 |
|---|---:|---:|---:|---:|---|
| `freebsd-hackers` | 201463 | **54000**（26.80%） | 147463 | ≈74 | **13 键**（885,916,986,1058,1067,1069,1229,1588,1648,10018,10110,12413,12417） |
| `freebsd-current` | 205027 | **12000** | 193027 | ≈97 | **13 键**（实测 b002 spec 无 1016/1039/1316，旧「15 键」作废） |
| `freebsd-doc` | 72663 | **12000** | 60663 | ≈31 | **13 键**（同 hackers） |
| `freebsd-stable` | 72164 | **12000** | 60164 | ≈31 | **13 键**（同 doc） |

四库合计已判读 **90000／551317（16.32%）**，剩余 461317 封 ≈ **231 批**（÷2000）。

🔴 **台账是 `status_source: spec-only` 口径**：游标随 `_batch_*.json` spec 预建即推进，**不等于 outline 已提交**——本次 b003 四批 spec 已标 `queued: true`，`_build_read_ledger.py` 据此**不计入** records，故建批不会虚增游标。
**四库已判读区间已全部 outline 入纲并 committed**，此刻无「已落库未入纲」的悬挂批。（旧注记「hackers 0–48000／current 0–6000／doc 0–6000／stable 0–6000」与游标「58000→66000」均为 **2026-09-22 14:5x 快照**，已被 §〇.1 取代。）

### 〇.1 增量（2026-09-22 16:3x 实测）

| 库 | 全库 | 已判读 | 已判读区间 | 已入纲闭环批次 | 在途 |
|---|---:|---:|---|---|---|
| `freebsd-hackers` | 201463 | **50000** | 0–50000 | fhk_b001–b025（25 批） | 无 |
| `freebsd-current` | 205027 | **8000** | 0–8000 | fcu_b001–b004（4 批） | 无 |
| `freebsd-doc` | 72663 | **8000** | 0–8000 | fdoc_b001–b004（4 批） | 无 |
| `freebsd-stable` | 72164 | **8000** | 0–8000 | fstb_b001–b004（4 批） | 无 |

- **`fdoc_b004` 全链闭环**（292 块／4 宿主：100.18 +223／98.6 +54／101.10 +12／106.9 +3），
  outline 幂等二跑 **+0**、bookkeep **缺块0／claim_id不符0／重复0 PASS**、等级门禁 **PASS**、
  **1067 时代型 24/24 零用**、D2 专名 **10 命中→8 改写＋2 保留**。明细见 `_H3_PROGRESS.md` §7.18。
- **🔴 台账口径订正（推翻上一行末句与第 40 行）**：`read_judged` 只取
  `_batch_*.json`（`lib`＋`offset`＋`n`）**且 `review_logs/<tag>_claim_map.json` 存在**的区间，
  `queued: true` **本身不阻断计入**——阻断条件是「queued 且 claim_map 尚不存在」。
  故 `read_judged` 随 **register** 推进，**与 outline 是否入纲无关**。
  fdoc_b004 的 2000 行早在 register（09-22 14:10）就已计入，**H3 四库真值仍是 74000/551317（13.42%）**。
  **不要把「入纲闭环」当台账推进点，否则会误报进度。**
- **🔴 pathspec 提交被并行会话卷走**：fdoc_b004 的 4 个宿主 md 进 `4c7f499a5`（信息 `……`）、
  台账进 `3d6fd0ae8`（信息 `！`）。**内容无损**（4 文件 +1460 行 = 292×5，
  292/292 pk 经全 05 卷 238 个 md 的 `ROW_MINE: freebsd-doc.messages.<pk>` 交叉核验命中），
  按既定口径不 amend，改在 `_H3_PROGRESS.md` §7.18 补勘误注。
- **✅ b004 波次四批全部全链闭环（2026-09-22 17:10）**，commit **`00867b889`**（8 文件、
  5734 行新增、0 删除）：`fcu_b004` **526 块**入 4 宿主（124.17 +262／106.9 +143／**106.7 +119**／122.9 +2）、
  `fstb_b004` **617 块**入 4 宿主（158.8 +322／98.6 +111／101.10 +98／106.9 +86，**1067 全程 0**）；
  106.9 为共享宿主（+229）。两批 outline 幂等二跑均 **+0**、bookkeep **三零 PASS**、
  等级门禁 **PASS**（大纲 3302 文件、`historical_claims` 引用块头 **164804** 全一致、错标 0）。
  **H3 四库 b001–b004 十二批全部 committed**（fhk 25 批 50000／current 4 批 8000／doc 4 批 8000／stable 4 批 8000）。
- **D2 专名门禁 b004 波全账 23 命中 → 改写 11 ＋ 保留 12**（明细见 `_H3_PROGRESS.md` §7.19）。
  本窗 5 条改写的取证要点：`1029968` SELSASKY＝FROM 邮箱 local-part 大写形（非臆造，
  但按 FROM 真名改写为 Hans Petter Selasky）；`2582275` Glen 把**被引用公告语**当成发帖人发言
  （张冠李戴）；`2582374`/`2582375` 正文是 **14.2** 却被写成 **freebsd-stable**（分支名错挂），
  且 2582375 把 Warner 的**提问**升级为断言；`2582482` 「非 root 下才能绑定」落在正文硬截断点之后不可核。
- **🔴 坑⑳ `subprocess.run` 的 `cwd` 不能给 POSIX 风格路径**：`cwd='/d/librebsd/...'` 被 Windows
  解析成 `D:\d\librebsd\...`，24 份 triage **全崩 rc=2、stdout 全空**，循环却打印 `D2 total 0`
  ——看着像「零臆造」，实际是「没跑起来」。必须 `cwd=r'D:/librebsd/...'`。
  **批量子进程的「零命中」必须先验 returncode**：静默全绿是最危险的假阴性。
- **下一动作＝建 b007 四批**：`fhk_b028` offset **54000**／`fcu_b007`·`fdoc_b007`·`fstb_b007` 均 offset **12000**
  （`_prep_batches.py`，spec 须写 `line_date: 2026-09-18`、13 键宿主，建批后校验 `hosts` 与 `pk_range` 与前批首尾相接零重叠）。
  建批前双查 `_chk_pk_coverage.py`：claim 库与大纲块的实际 pk 覆盖，不能只信本线 offset 游标。
  派发节奏按 §〇 负载实测：**每波 ≤40 路**，派发后不等同步回报，每 15 分钟跑 `review_logs/_watch_agents.py` 扫盘。

🔴 **token 配额硬停（2026-09-21 18:38–18:50 实测，本会话 5 路子代理全部 `token plan
entitlement exhausted` 失败）**：fcu_b001 读手 4 路（21–25 分钟各死一次）＋ shenyue
seg-33 评审员（37.8 分钟）。**失败发生在写盘之后**——磁盘产物完整可用，但收尾 JSON
回报全丢。**新会话开工第一件事是确认配额是否恢复**；未恢复则**只能主代理 solo**
（见 §四 止损阶梯末级），不得再派子代理（派了也是 20+ 分钟零回报）。
⚠️ 并行会话同时在跑 H1／H2／H4／shenyue 多条线，配额是**全会话池**，多线并发会互相挤爆。

**H2 四库真值**（`script/_db_row_mining/_RESUME_H2.md` 为断点入口，台账 `_db_row_mining/mail2d_read_ledger.json`）：

| 库 | 全库 | 已判读 | 剩余 | records（行序） |
|---|---:|---:|---:|---|
| `freebsd-ports` | 191637 | **39000** | **152637** | `[(0,39000)]` fpo_b151–b163 **单段连续无缝**（13 批）；queued b164（39000–42000，spec 已建待判读） |
| `freebsd-bugs` | 192683 | **4000** | **188683** | `[(0,500)]` b171 ＋ `[(137970,141470)]` b172+b173+b174+b174e+b175+b176+b177+b178（b174e 在既有区间内，并集不扩张）；queued b179（141470–141970） |
| `freebsd-net` | 73645 | 45000 | 28645 | `[(0,45000)]` fn_b156–b170；queued `[(45000,48000)]` fn_b171 |
| `freebsd-chat` | 43869 | 43869 | **0** | `[(0,43869)]` fch_b137–b150，**已整库闭环** |

⚠️ `_HANDOFF_H2.md` §二 三处数据已过期（ports/net/chat 的「已读 0」皆非）——**以本表为准**，
订正详情见 `_RESUME_H2.md` §一。freebsd-bugs 的 pk 空间年份同质，**下一批直接按 offset 140970 跳**，
勿从 0/500 线性回退（见 `_HANDOFF_H2.md` §9.6）。**下一批已预建待派读手**：
`fpo_b164`（offset 39000／3000 行，pk 1591870–1594880，全 2007，12 份 digest×250 行）
＋ `fbug_b179`（offset 141470／500 行，pk 1050177–1050680，1995→1996 2.1→2.2 过渡，5 份 digest×100 行，
5 路读手），两批 pk 端点均与前批紧贴无缝、容器行 0、pk 单调递增、跨行重复 0（已实测断言）。
主理人授权上限 **40 路**（2026-09-23 16:45 裁定，覆盖此前 20 路）。**已闭环两批（06:35–06:45）**：`fbug_b178` **311 块**（收率 62.2%，
88.1=263／88.6=12／88.7=36）commit **`a915159b7`**（+1555＝311×5）＋ `fpo_b163` **369 块**
（收率 12.3%，89.2=301／89.4=53／90.6=1／90.7=9／90.9=5）commit **`a01a852e0`**（+1845＝369×5），
两批 outline 幂等二跑 +0、bookkeep 三零 PASS、**audit PASS 154379 块头错标 0**，台账已回填
（`1ece4135e`，ports 判读 39000／bugs 4000）。**口径裁定（已固化入 b163／b164 任务书）**：
**894＝「构建侧」**（构建工具链：portupgrade／portmanager／portmaster／fetchindex／portlint／
INDEX／libtool／RCng／portsdb／portscout／tinderbox／bsd.*.mk／pkg_*），
**906＝「组织侧」**（端口树结构与类别批评 ＋ Gentoo／Portage／dpkg／rpm 对照 ＋ 许可证标注政策）——
端口类别／树结构的组织批评落 906 不落 894；ports 冻结／解封的政策投票与归属之争落 907。
**新坑（已入任务书纪律）**：叙述手会持续重写 TSV，**merge 前必须重测盘上违规数**
（b178 p6 由 3 条越限自行补至 0，中间态一度为 5 条）；新增 `_pad_short_narr.py`
外科补齐工具（dry 纯读、断言命中数与行数不变，已拦下 5 条）。
**下一批**：`fpo_b164`（offset 39000）／`fbug_b179`（offset 141470）；**建批前必查 spec 是否已被他会话预建**。

**shenyue 台账真值**（`shenyue/review/_ledger.jsonl`）：**27 行**、verify **0 fails**、
B 游标 pos **550**（O-2073，下一位 O-2082）、B 类剩余 **198 条（4 批）**。

🔴 **本会话裁定（2026-09-21 18:00）**：会话模型适配 **1M 上下文 token**（GLM-5.2 xhigh）；
**允许多个子代理**（沿用 §四 3–4 评审员／波，`run_in_background` + 8 分钟止损）。
1M 上下文下主代理可读 KB 级探针输出，但**仍不读** R 条目正文／23 MB jsonl（铁律不变）。
BATCH-0027 已由主代理建 `URL_CORPUS.md`（48 条可达入口，含 Darwin／DragonFly／tuhs／freebsd 新增），
4 评审员（seg-21..24）已派，断点 `_progress-BATCH-0027.json` status=IN_PROGRESS_4_REVIEWERS_DISPATCHED。

---

## 一、中断恢复三步法（新会话第一件事）

1. **读本文档 §〇 与 §五**，定两条线的在途状态。
2. **读两条台账定真游标**（不信本文档，见 §七）：
   - H3：`C:/Python314/python.exe -c "import json;d=json.load(open('script/_db_row_mining/mail2d_read_ledger.json'));print({k:(v['read_judged'],v['queued_spec']) for k,v in d['items'].items() if k.startswith('freebsd')})"`
   - shenyue：`shenyue/review/_ledger.json`（行数、seen、next_batch_no、B/C 游标 pos）
3. **找在途 tag**：`script/_db_row_mining/_batch_*.json` 中**有 spec 但无 claim_map** 的即在途；
   shenyue 侧看 `shenyue/review/_progress-BATCH-*.json` 的 `inflight` 段。
   → 按该批的断点文件定位缺失步 → 按 §三 SOP 续跑。

**幂等续接安全**：H3 的 `outline --write` 与 shenyue 的 `_s51_merge_partial.py` 均以「已落盘块」为权威，
重复 pk / oid 会被报出而拒收。**重派同一单元只是浪费，不会污染台账。**

---

## 二、中断免疫硬规则（七条，所有会话必须遵守）

1. **磁盘即记忆**：任何工作单元状态必须落文件；上下文被压缩/终止即全丢。**每批开工第一步写断点文件**
   （H3 追加 `_H3_PROGRESS.md` 段；shenyue 写 `shenyue/review/_progress-BATCH-<NNNN>.json` 含 dispatched 计划），
   最后一步才改完成态。
2. **游标只信台账，不信文档**：H3 信 `mail2d_read_ledger.json`；shenyue 信 `_ledger.json`。
3. **单批闭环粒度**：一个 checkpoint ＝ 一批完整闭环。**在途批每线不超过 1 批**。
4. **幂等续接**（见 §一）。
5. **原子提交 + pathspec**：每批闭环立即 `git commit -- <本批文件>`；commit 前 `git update-index --refresh`
   清 racy-stat 幻影。**禁 `git add -A`**（并行会话秒级卷走暂存件）；不 commit 他人改动。
6. **子代理限时 + 主代理兜底**：见 §四。
7. **主代理只做确定性活**：合并、落库、写回、门禁、提交、台账刷新——**一律脚本，不派子代理**。
   内容活（读手判读、叙述撰写、评审）才派子代理。

**上下文预算硬约束**：主代理**不读 20 MB+ 文件**、**不读** `<tag>_forread.txt`、
**不读** `section_record.jsonl`/`_local_rounds3.jsonl`/`local_matches.jsonl`（各 ≈23 MB）、**不读** R 条目正文。
一切数字来自脚本实测输出（KB 级）。

---

## 三、单会话工作单元（一个会话安全容量 ＝ H3 一批 **或** shenyue 一批）

### 3.1 H3 一批（`freebsd-hackers`／`freebsd-current` 通用）

```
 1. 读 _H3_PROGRESS.md 对应批段 + mail2d_read_ledger.json      ← 三源交叉定 offset
 2. _prep_batches.py <tag>:<offset>:2000 --lib <库> --hosts <池>  ← spec＋dump＋拆 4 份 digest
 3. 主代理补丁：spec 补 hosts（按本批年段从 _H3_HOST_POOL.md 实测选）＋ line_date=2026-09-18
 4. 派 4 路读手（run_in_background），每份 500 行 digest_partK.txt
 5. 限时监控；8 分钟无落盘即 TaskStop＋重派；全败则主代理直读
 6. _part_profile / _audit_cand_fidelity / _audit_author_match  ← 三源取真值，勿信读手自报
 7. _merge_parts.py <tag> 4   →   _mail2d_run_batch.py register --tag <tag> --apply
 8. body --tag <tag>   →   _split_narr.py <tag> 4   →   派叙述手（每波 ≤4）   →   _merge_narr.py
 9. _chk_mount_narr.py → _audit_narr_propernoun.py（可疑条仅回原文重写）
10. outline --write（**幂等二跑须 +0**）→ bookkeep --write → 等级门禁 → commit --apply
11. _build_read_ledger.py 刷新台账 → git commit（pathspec）→ 回写 _H3_PROGRESS.md
```

**作者对位门禁命中处置（fhk_b021 实证定式）**：命中后回 duckdb 取**完整正文**判本方口吻——
digest 仅 420 字窗口且 `from` 列是**回帖人**、正文被 `>` 引用块占满，这正是漂移根因。
该行作者有自述技术判断 → 改写为其本方口吻（L4）；仅纯转发/一句客套 → **剔除**。**严禁从被引者内容硬凑。**
门禁输出须先人工分流「from 列 40 字截断假阳（如 Wojtek Puchar）vs 真漂移」，不得整批改写。

### 3.2 shenyue 一批复核

```
 1. 读 _LONGRUN_PLAN.md + _progress-BATCH-<NNNN>.json + review/_ledger.json
 2. 写 _progress-BATCH-<NNNN>.json（dispatched 计划）            ← 先登记
 3. _s50_batch_prep.py prep <cls>   →  派 3–4 评审员（每片 ≤7 oid，run_in_background）
 4. 限时监控；8 分钟无落盘即 TaskStop＋重派；全败则主代理 solo
 5. _s51_merge_partial.py merge <cls> <NNNN>
 6. _s52_audit_web_evidence.py --batch <cls> <NNNN>              ← 联网证据门禁
 7. _s25_ledger.py append <cls> <pos_lo> <pos_hi> <报告名>  →  _s25_ledger.py verify
 8. git commit（pathspec）→ 更新 _progress（完成态）
```

**联网证据门禁**：`WebSearch` 在本 provider **不可用**（Provider API kind openai-compatible 不编码
provider-native WebSearch）。**必须主代理先建 URL 语料再派评审员**：
走 Bing 两步 WebFetch（搜索页取 organic → 逐条 fetch 正文），产出 `review/.runs/BATCH-<NNNN>/URL_CORPUS.md`
（范式见 `BATCH-0025/URL_CORPUS.md`，75 行），明确标注已实测可达入口与被拦站点
（marc.info、openbsd-hack.net、ksp.kth.se 等）。**单条 12–36 次 fetch、8–18 分钟**；
DDG 有 bot 校验、archive.org 间歇离线；URL 不得含省略号。
派单必须附此语料并写明「子代理只能引用自己实测成功的 URL」，**不计成本不得减少联网**。
（B 0017–0023 六批 300 条 URL=0、0024 门禁 FAIL 30 项同源；修法是附可直取语料，不是加代理数。）

### 3.3 解释器

`C:/Python314/python.exe` 通用（duckdb 与文本脚本均可跑）。

---

## 四、子代理编排纪律（09-21 主理人授权：至多 12 路）

| 项 | 值 |
|---|---|
| 子代理/波 | **3–4 路起，上限 12 路**（09-21 主理人解除子代理限制并授权至多 12 路并发；此前上限 3–8） |
| 并发总量 | 跨线不超过 12 路；**在途批每线不超过 1 批** |
| 派发方式 | `Agent` + `run_in_background: true`（并行，返回 agentId 供止损） |
| 止损 | `TaskOutput` 限时；**8 分钟无落盘即 `TaskStop` 并匿名重派一次**（换句柄名，勿复用 agentId）；重派仍败则转主代理 solo 清单 |
| 🔴 禁用 | **`CreateWorkflow` 跑长线**：actor 无 per-ask 超时，实测评审员 7+ 分钟 0 工具调用卡死零产出，脚本无法局部止损。`shenyue/.zcode/workflows/*.dwf.ts` **废弃不执行** |
| 自报数字 | **一律不信**（BATCH-0009 各片自报 206，实测 301） |
| 429 处理 | 记「本轮降为 X 路」，不重试整波，改主代理直读。mail2d 实测 ≥4 路易触发 429（全会话池配额），扩至 12 路时须以落盘条数为准、遇 429 即降 |
| 命名避让 | shenyue 段文件用 `seg-<会话段号>`，防并行会话互相覆盖（BATCH-0024 已发生 seg-01/02 撞名事故） |

**读手/叙述手提示词必写四句**（零产出事故的唯一有效解，本线 16 路零事故实证）：
① 每次 Read 限 100–1200 行；② 每写约 20 行用 Write 增量落盘（覆盖写全文），不得写完才一次性落盘；
③ 转录与产出以行首 pk / oid 为准，禁用行号；④ 回报写出实际落盘行数、宿主/段分布、以及任何「摘要与原文不符」清单。

---

## 五、在途表（2026-09-22 02:0x）

| 项 | 状态 | 句柄／产物 |
|---|---|---|
| `fhk_b021` 候选（256 条，L4 223／L3 33） | ✅ check 0 违规、越界 0 | `review_logs/fhk_b021_candidates.txt` |
| `fhk_b021` 作者对位 | ✅ 30 条命中 → **14 真缺陷已定点改写/剔除＋6 Wojtek 假阳不动** | `_fix_author_fhk_b021.py`、`review_logs/fhk_b021_fixdec_{a,b}.json` |
| `fhk_b021` register | ✅ **COMMITTED 256**，claim seq **CL-RM-153599–153854**，反查 256/256，四表 join 256 | `_batch_fhk_b021.json` 的 `claim_map` |
| `fhk_b021` body + 叙述拆件 | ✅ 正文 256/256（缺失 0），`narrpkg_p1..p4` 各 64 条 | `cands_body_p1..p4.txt`（年段 2012×216＋2013×40） |
| `fhk_b021` 叙述手 | 🔄 **4 路**（p2✅64／p4✅64 已完稿；p1 58/64 推进中；p3 重派后待首落盘） | 首派 p1/p3 卡死（p1 写 39 行后停滞 18 分钟、p3 全程 20 分钟零落盘），17:55 止损并匿名重派（p1 `agent_6415cad4`／p3 `agent_a1e1f4d1`）；产出 `mount_narr_p1..p4.tsv` |
| `fcu_b001`（offset 0，pk 246–1025423） | ⏸ 已预建待派读手（**容器行 301/2000＝15.1%，读手一律不收**；年段 2008×1645／2010×53／2018×51／2002×47／2003×20／2017×1） | `_batch_fcu_b001.json`、`review_logs/fcu_b001_container_pks.txt` |
| shenyue `BATCH-0025` | ✅ 已落账 seq 25、verify 0 fails | `shenyue/review/_ledger.json` |
| shenyue `BATCH-0026` | ✅ 已落账 seq 26、verify 0 fails（门禁残留 67 项 C28+E32 体例漏项登记 _WEB_DEBT_REGISTER.md §八，只登记不追补） | `shenyue/review/_ledger.json` |
| shenyue `BATCH-0027` | ✅ **已落账 seq 27、门禁 PASS 零残留**（B pos 501–550、O-1891→O-2073，50 块、来源池 150 行）；四片 seg-21..24 全齐（13/13/12/12，0 占位符，counts 13/13/12/12）；0026 的 C/E 体例漏项教训已写死进派单，本批一次过 | `shenyue/review/逐条建议书-B-BATCH-0027.md`（1161 行）、`_sourcebank-B-0027.jsonl`（150 行）、`_ledger.jsonl` +1 |
| shenyue `BATCH-0028` | ⏸ 未开工（B pos 551–600、O-2082 起；剩余 4 批 0028–0031，B 类尾批 0031 为 48 条） | `_a_order.json` 的 `order.B` |
| `fbug_b173`（bugs offset 138470） | ✅ **全链闭环 `cee1e72ec`**：327 块入 88.1/88.6/88.7，+1635 行恰 = 327×5，0 删除；outline 幂等二跑 +0、bookkeep 三零 PASS、等级门禁 PASS | `_RESUME_H2.md` §二「fbug_b173 全链闭环记录」 |
| `fbug_b174`（bugs offset 138970，pk 1047667–1048166） | ✅ **全链闭环 `27cfc5725`**：328 条 register COMMITTED（`CL-RM-154743`–`155070`）→ 5 叙述包 **328 行违规 0**（62–140／avg 102.7）→ 宿主 881×275／886×9／887×44 → outline 幂等二跑 +0 → bookkeep 三零 PASS → **提交 +1640 行 = 328×5**，0 删除，仅 3 宿主文件。**16 条读手增量不进本批**，另开 tag | `_NARR_TASK_fbug_b174.md`、`fbug_b174_extra_cand.txt` |
| `fpo_b156`（ports offset 15000，pk 1567555–1570595，n=3000） | ✅ **全链闭环（裹挟入 `529468ce9`）**：702 条 → check PASS（L4 518／L3 184）→ register COMMITTED 702（`CL-RM-155072`–`155773`）→ 9 叙述包 **702 行违规 0**（60–140／avg 89.0）→ 宿主 891×117／892×570／894×3／906×2／907×7／909×3 → **702×5 = 3510 行**。⚠ 提交范围归属错误已留档 | `_NARR_TASK_fpo_b156.md`、`_RESUME_H2.md`「提交裹挟说明」 |
| `fpo_b157`（ports offset **18000**，pk 1570596–1573653，n=3000） | ✅ **全链闭环（`529468ce9`）**：309 条（剔除幽灵 pk **1571399**，源库与 digest 均无）→ register COMMITTED 309（`CL-RM-156915`–`157223`，反查 309/309、四表 join 309）→ 5 叙述包 **309 行违规 0**（63–140／avg 93.0）→ 宿主 891×60／892×220／894×1／906×15／907×7／909×6 → **309×5 = 1545 行** | `review_logs/fpo_b157_cand_p*.txt`、`_check_author_mismatch3.py`、`_fix_b157_attrib_20260921.py` |
| `fbug_b174e`（bugs offset 138970，n=500，b174 pk 区间内 16 条增量） | ✅ **全链闭环 `333434176`**：16 条 register（`CL-RM-160214`–`160229`）→ 正文 16/16 → 2 叙述包 **16 行违规 0**（87–139／avg 115.9）→ 宿主 881×10／887×6（886 零命中）→ outline 88.1+10／88.7+6、幂等二跑 **+0** → bookkeep 三零 PASS → **提交 +80 行恰 = 16×5**，0 删除，仅 2 宿主文件 → audit PASS → 台账 records 不变（区间并集），read_effective 仍 2000 | `_NARR_TASK_fbug_b174e.md`、`_batch_fbug_b174e.json`、`_RESUME_H2.md` §七「b174e 增量闭环」 |
| H2 三批次等级门禁 | ✅ **`audit_evidence_level_labels.py` PASS 错标 0**（原 FAIL 3：b174 等级互串 2 条＋b156 大纲滞后 1 条，已定点修 DB＋大纲，见 `_RESUME_H2.md`） | `_fix_level_20260921_d.py`、`_verify_narrs.py` |
| H2 下一批候选 | 🟡 **`fpo_b159`（offset 24000 n 3000）已开批、12 读手在途（09-22 派）**——pk **1576714–1579742**（与 b158 端点 1576713 紧贴）、全 2005 年（03×959／05×699／06×693／11×644）、容器行 0；12 分片各 250 行约 121 KB、pk 完全不相交。🔴 **12 路全部回报前不得 merge**（b158 教训：merge 抢在 4 路读手回报前执行→候选 463 实应 449）。另 **`fbug_b175`（offset 139470 n 500）已开批待派**（pk 1048167–1048667 紧贴 b174 端点、全 1995 年 06×416／07×82、容器行 0、5 分片各 100 行约 47 KB 一次 Read 即可、任务书已写；预期收率 ≈65%）；`fn_b172`（offset **48000**，fn_b171 收口后） | `_batch_fpo_b159.json`、`_READ_TASK_fpo_b159.md`、`_READ_TASK_fbug_b175.md`、`_profile_batch.py`、`_RESUME_H2.md` §七 |
| `fpo_b157` 摘要误归因定点回改 | ✅ **9/9 已回改、回读一致、对齐复验 9/9**：`_check_author_mismatch3.py` 报 27 条「摘要首名与 digest 显示名完全不交」，逐条回 digest 全行复核＝**假阳 18＋真缺陷 9**（姓名误拼 1／姓名补全 1／转述主体错 6／主体＋内容双错 2，后者含 1571789「实谈 RPM 规格书许可，无 SIGSEGV」与 1573347「实为纯提问，Linimon 与 noip 均未出现」）。`_fix_b157_attrib_20260921.py --apply` 只改 `claim.claim_text`＋`evidence.fact_text`，**等级一律不动**：三条转述形态（1571202／1571789／1572671）拟降 L3，回正文原文后**撤回降级**——发件人各有自有动作／观察（Oliver 自述不能测 samba 并自行发问／Robin 自述已翻看 Gentoo ebuild 发现 LICENSE 声明／Oliver 自述已包安装并亲验 vchkpw 正常），符合 L4 判据；且大纲叙述句更完整且已标「转述」，故**大纲零改动**，等级三方一致。回改后全库等级门禁复跑 **PASS**（137237 块头／错标 0） | `_fix_b157_attrib_20260921.py`、`_check_author_mismatch3.py`、`_RESUME_H2.md` §七「b157 摘要误归因定点回改」 |
| `fpo_b158`（ports offset **21000**，pk 1573654–1576713，n=3000） | ✅ **全链闭环 `1029cb38c`**：候选 **448 条**（初判 463 → 对齐 449 → 撤臆造 448）→ register（`CL-RM-160230`–`161257`，含增量 49 条 `161209`–`161257`）→ 正文 448/448 → **3 条等级回改 DB L4→L3**（`160591`／`160599`／`160629`）→ 8 叙述包 **448 行违规 0** → 宿主 **891×0／892×369／894×43／906×2／907×19／909×15** → outline 89.2+1845／89.4+215／90.7+95／90.9+75／90.6+10、幂等二跑 **+0** → bookkeep 三零 PASS → **提交 +2240 行恰 = 448×5**，0 删除，仅 5 宿主文件 → audit **PASS**（140040 块头／错标 0）→ 台账 ports `read_effective 24000`、records `[(0,24000)]` **单段连续**。本批为**史料密度最高一批**：`perl symlinks in /usr/bin will be gone`×76、`New port with maintainer ports@`×50、`HEADS UP: pkg-plist strict enforcement`×41、`INDEX build failed`×34、`Why does everybody switch to dynamic plists?`×21、`bsd.sites.mk` 可覆写提案×17；噪声类 93 条占 3.1%。**891（89.1 制度初创节）零命中**——若 b159 亦零命中属正常 | `_batch_fpo_b158.json`、`_RESUME_H2.md` §七「fpo_b158 全链闭环」 |
| **b158 候选集对齐回改**（2026-09-21 23:2x） | 🔴 **缺陷**：`_s62_merge_multi.py fpo_b158 6` 于 22:44 执行时读手 p2/p3/p5 **仍在写分片**（mtime 22:51／22:47／22:45 均晚于合并时刻），抓到的是分片中途快照——落盘 **463** 行，六片最终判读并集实测 **449** 行。**差集双向**：63 行在 463 内但读手重判后撤回（摘要归因错配＋纯寒暄＋空正文，抽样 10 条回正文验证撤回有据）；49 行读手在合并后才新增判收。**处置** `_reconcile_b158_withdrawn.py --apply`：撤回 63 条**不 DELETE 改 `claim.status='rejected'`**（库内既有 3733 行 rejected，先例 fhk_b021 pk 1312976；`_mail2d_run_batch.py` 与 `audit_evidence_level_labels.py` **均不按 status 过滤**故门禁不受影响，且留档可回溯）；candidates 重建 449 行、register 补入 49 条、claim_map 裁孤儿 → 449。再撤 1 条臆造（pk 1575968）→ **448**。**须写死进流程的三条**：① 读手未全部回报前不得 merge 候选（等 completion 齐＋分片 mtime 静止）；② 读手自报数字一律不信（本轮 p5 自报 66 实 52、p7 自报 66 **文件不存在**、叙述手自报「越限 0」实测 20 条越限）；③ 不对写盘中的分片做抢救性改写（先 TaskStop＋核实 mtime 静止） | `_reconcile_b158_withdrawn.py`、`_reject_b158_noinv.py`、`_salvage_b158_narr.py`、`_split_b158_gaps.py`、`_redist_b158_narr.py`、`_RESUME_H2.md` §七「b158 候选集对齐」 |
| **register 幂等保留陈旧等级／摘要**（新坑，b158 发现） | 🔴 **`_outline_<tag>.py` 块头等级取自 `candidates.txt`（第 61–64 行）而非 claim 表**，故两者一旦不一致，audit 必 FAIL。本批首 register 时候选还是 463 的半截快照，把 3 条写成 L4；读手其后重判 L3；而 `register` 幂等键是 `source_id` + `content_hash`，**改等级不重算 hash，故二次 register 静默 SKIPPED**，DB 永远停在首次值 → audit FAIL 3 处「块头 ≠ claim.evidence_level」。**处置** `_fix_b158_levels.py --apply`：**改 DB 侧**（DB 是旧的那一边），outline **不动**（其块头与 TAIL 纪律句本就按 candidates.txt 的 L3 生成，是对的）。**教训**：读手重判发生在首 register 之后时，必须手工比对 `candidates.txt` 与 `claim.evidence_level` 并回改 DB——register 的 source_id 幂等会静默保留陈旧等级与摘要 | `_fix_b158_levels.py`、`_find_level_mismatch.py` |
| **b158 叙述禁字体检遗漏 `\` 与 `|`** | 🔴 `_merge_narr.py` 除 `「」*` 外**也禁 `|`**（b157 教训记的是「`\|` 为 candidates 分隔符故不查」，但 mount_narr 的叙述列确实要查）。本批 3 条踩中并已改写：`1574616`（`pre\|post-deinstall` → 「pre-deinstall 与 post-deinstall」）、`1575789`（`(i && j || k)` → 「加括号与不加括号的与或表达式」）、`1576445`（正则字面量 `m/\.$/` → 「将匹配尾句号的规则由 =~ 改为 !~」）；另 2 条长度越界（`1575816` 58 字、`1575968` 56 字）一并修正。**臆造条目删而非改（b157 先例第二次适用）**：pk 1575968 正文窗内只有 `Holger Kipp writes: > …` 引用块与 Kipp 自己论述，**发件人 Matthias Andree 本人立场在 digest 与 body 窗口内都不可见**，叙述手却写成「Andree 反驳 Kipp 称该单一符号链接确有必要」——逻辑自相矛盾，按先例删行不改写，`reviewed_by='b158-noinv-no-authorial-content-20260922'` | `_scan_narr_gate.py`、`_chk_two_rows.py`、`_reject_b158_noinv.py` |
| b174 等级误判 2 条回改 | ✅ **CL-RM-154885／154921 由 L3 改 L4**，回读 6/6、audit **PASS**（137802 块头／错标 0）。**上次的等级互串修复只改对了一半**——154884 改对、154885 改错。本次逐条回 digest＋摘要＋**大纲叙述句**三方比对后定性：154884 叙述含 Khera 自有动作（给 lo0 加别名绕过并 `netstat -p ip` 验证）故维持 L4；154885 是 Henrich 自有调试、154921 是 Grillo 自有经历与建议，均应为 L4。摘要文本不动 | `_fix_b174_levels_20260921.py`、`_RESUME_H2.md` §七「b174 等级误判 2 条回改」 |
| `fdoc_b001`／`fstab_b001` | ⏸ 未预建（P1，待 P0 两库推进后再派） | — |
| H3 `fhk_b021`（hackers offset 40000，pk 1312727–1314738） | ✅ **完全收口**：候选 **255 条**（原 256，剔除 1312976——from/subject/thread_refs 全空且 message_id 为合成号 `<no-id-...>`，库中 `status='rejected'`）→ 摘要对位订正 **20 改＋1 剔除**＋叙述改 **7 条** → outline **255 块入 6 宿主**（106.9 +237／124.17 +4／124.13 +2／164.8 +4／158.8 +4／106.7 +4）→ bookkeep 缺块 0／claim_id 不符 0／重复 0 → 等级门禁全库 **PASS**（3279 md／134282 抬头／0 错／0 悬空）→ commit `54119d159` → 台账 `freebsd-hackers` **42000** | `script/_db_row_mining/review_logs/fhk_b021_*`、`_fix_cand_fhk_b021_p2.py`、`_fix_narr_fhk_b021_pn.py`、`_outline_fhk_b021.py` |
| H3 `fcu_b001`（current offset 0，pk 2462–1025423，容器行 301/2000） | 🔄 **续读 3 路已派（19:20）**：p1（剩 305 行，续 `pk>6324`）／p3（剩 100 行，续 `pk>1024811`）／p4（剩 400 行，续 `pk>1025023`），**p2 已读完**；追加写勿覆盖旧行（旧 8／253／125／26 条）。⚠ p1 大部分行落在容器行清单内，候选数不会高属正常。句柄见 `_DISPATCH_20260921_1920.json` | `_READ_TASK_fcu_b001.md`（§十 断点表）、`review_logs/fcu_b001_candidates_part1..4.txt` |
| H3 `fhk_b022`（hackers offset 42000，pk 1314739–1316740） | 🔄 **已预建＋4 读手已派（19:20）**：spec `_batch_fhk_b022.json`（已补 `pk_range`／`line_date=2026-09-18`／`containers=0`）、dump 2000 行、digest 拆 4 份各 500 行、任务书 `_READ_TASK_fhk_b022.md`（含 §五.1 摘要归属铁律）。**本批全为 2013 年、容器行 0**（判据实测：0 行符合「≥3 处行首 `From `＋`From owner-`＋>20KB」；该判据已在 fcu_b001 上复算 301/301 完全吻合，可复用）。p1 1314739–1315238／p2 1315239–1315738／p3 1315739–1316240／p4 1316241–1316740 | `_DISPATCH_20260921_1920.json`、`review_logs/fhk_b022_digest_part1..4.txt` |

---

### 五之补 · 2026-09-22 02:0x 波次（本节取代上表中 H3 各行的在途描述）

| 项 | 状态 | 句柄／产物 |
|---|---|---|
| `fcu_b001`（current offset 0） | ✅ **完全收口**：565 块入 5 宿主，commit `fe4eb1aff`＋`034401026`，台账 0→2000 | `script/_db_row_mining/_H3_PROGRESS.md` |
| `fdoc_b001`（doc offset 0） | ✅ **完全收口**：297 块入 7 宿主（100.18 +283／106.9 +5／122.9 +3／124.13 +2／164.8 +2／124.17 +1／105.8 +1），outline 幂等二跑 +0、bookkeep 三零 PASS、等级门禁 PASS、commit `8e330dc09` +1485 行，台账 0→2000 | `_H3_PROGRESS.md`、`_tmpaudit/fdoc_b001_pn.txt`（0 命中） |
| `fstb_b001`（stable offset 0，pk 2876–2576641） | ✅ **完全收口（commit `c90d1af83`，7 文件 +2578 行）**：516 块入 7 宿主（100.18 +381／88.5 +56／122.9 +48／106.9 +22／124.13 +6／105.8 +2／158.8 +1）、叙述 60–140／avg 96.4／违规 0、outline 幂等二跑 +0、bookkeep 三零 PASS、等级门禁 PASS（141440 块头／0 错标）、台账 0→2000。8 半份 → 516 条（L4 501／L3 15，25.8%）、register COMMITTED 516 seq 160693、body 516/516 | `_H3_PROGRESS.md` §7.6、`_fix_pn_fstb_b001.py`、`review_logs/fstb_b001_pn_triage.md` |
| `fstb_b001` 专名门禁（判据定形） | ✅ **48 命中 → 18 命中，18 条全为假阳性，30 条真臆造清零**（27 条 `_fix_pn_fstb_b001.py` 定点改写＋3 条叙述手自清）。四条判据＋**新判据「路径拼接假阳性」**（token 正则把整条路径当一个词：`2575344` 的 `usr/compat/linux/lib/ld-linux.so.1` 正文各组件俱全只是顺序不同）见 `_H3_PROGRESS.md` §7.6 | `_tmpaudit/fstb_b001_pn_v3.txt` |
| `fhk_b022`（hackers offset 42000） | ✅ **完全收口（commit `de2f33277`，+2520 行＝504×5）**：504 块入 5 宿主（158.8 +342／122.9 +99／106.9 +46／105.8 +11／124.13 +6）、专名 41 命中分流 12 假阳／29 真臆造改写、bookkeep 三零 PASS、等级门禁 PASS、台账 42000→44000 | `_H3_PROGRESS.md` |
| 下一批 4 spec 预建 | ✅ **已按各自源库建 spec＋dump＋digest 4 份＋32 半份，四批容器行均 0**：`fhk_b023` offset 44000 pk 1316741–1318740／`fcu_b002` offset 2000 pk 1025424–1027444／`fdoc_b002` offset 2000 pk 1108539–1110552／`fstb_b002` offset 2000 pk 2576642–2578641。**四批 spec 实测均为 13 键**（旧记「fcu_b002 为 15 键」与 spec 不符，作废）。**`--lib` 一次调用只认一个值** | `_prep_batches.py`、`_split_halves_p2.py`、`_prep_next4.log` |
| `fcu_b002`（current offset 2000） | 🔄 **已落库**：8 半份 → **433 条**（L4 429／L3 4）、`check` 违规 0、register COMMITTED 433（`CL-RM-162346`–`162778`）、body 433/433、`_split_narr.py fcu_b002 6` 6 份就绪。作者对位 9 条处置（8 改写＋1 剔除）＋摘要超长 8 条定点压缩。**6 路叙述手未派** | `review_logs/fcu_b002_candidates.txt`、`fcu_b002_narrpkg_p1..p6.txt`、`_NARR_TASK_fcu_b002.md` |
| `fdoc_b002`（doc offset 2000） | 🔄 **已落库，6 路叙述手在途**：8 半份 → **441 条**（L4 397／L3 44）、违规 0、register COMMITTED 441（`CL-RM-162779`–`163219`）、body 441/441、6 份就绪。作者对位 7 条（5 改写＋2 剔除）。年段 2003×1465／2004×535，兜底宿主 **10018** | 叙述句柄 fdoc p1–p6；`_NARR_TASK_fdoc_b002.md` |
| `fhk_b023`（hackers offset 44000） | 🔄 **已落库，4 路叙述手在途**：8 半份 → **257 条**（L4 247／L3 10）、违规 0、register COMMITTED 257（`CL-RM-163220`–`163476`）、body 257/257、4 份就绪。作者对位 7 条（3 改写＋4 剔除）。年段 2013×74／2014×1926，兜底宿主 **1588** | 叙述句柄 fhk p1–p4；`_NARR_TASK_fhk_b023.md` |
| `fstb_b002`（stable offset 2000） | 🔄 **读手 7/8 落盘**（part1b 63／part2a 64／part2b 75／part3a 70／part3b 59／part4a 70／part4b 70）；**part1a 首派零产出已重派**（末句「Now I'll verify the final list…」属截断签名）。年段 2004–2005，兜底宿主 **10018** | `_READ_TASK_fstb_b002.md` 口径复用；重派句柄见会话 |
| **本轮三处新坑** | 🔴 **坑⑤** 读手在 merge 后重写自己分件 → 重缝会「丢」条目（fcu_b002 440→433 实为读手主动剔除，非丢失）；重缝前须核半份 mtime。**坑⑥** 定点改写脚本断言须在**写盘前**捕获基准量，且锚点检查须幂等（`f[2]==new` 视为已应用）。**坑⑦** `FORB` 不得含空格（中英混排摘要必有空格） | `_H3_PROGRESS.md` §7.7 |
| shenyue `BATCH-0028/0029/0030` | ⏸ **并行会话在途，勿双写**（0030 已见 `.partial-B-BATCH-0030.md`／`.skeleton-B-BATCH-0030.md`） | `shenyue/review/.runs/BATCH-00*/` |

**止损指令**：任一子代理 8 分钟无落盘即 `TaskStop` 并重派同一分件；全败则该分件转主代理直读。

---

## 六、长尾队列总账

| 序 | 战线 | 规模 | 单批 | 剩余批数 |
|---|---|---:|---|---:|
| **P0** | H3 `freebsd-hackers` | 151463 封 | 2000/批 | ≈76（**fhk_b025 已收口 committed `c2b1ef407`**，下一批 fhk_b026 offset 50000 未建） |
| **P0** | H3 `freebsd-current` | 197027 封 | 2000/批 | ≈99（fcu_b004 已 register 526 条，**叙述在途**，下一批 fcu_b005 offset 8000） |
| **P1** | H3 `freebsd-doc` | 64663 封 | 2000/批 | ≈33（fdoc_b004 已 register 292 条，**叙述在途**，下一批 fdoc_b005 offset 8000） |
| **P1** | H3 `freebsd-stable` | 64164 封 | 2000/批 | ≈32（fstb_b004 已 register 617 条，**叙述在途**，下一批 fstb_b005 offset 8000） |
| **P1** | Linux 邮件列表价值反推 | 九库 2,540,000 封（未处理） | 单批约 200-500 封判读 | 约 5-10 批（linux-man 优先，约 46 页高价值） |
| **P2** | shenyue B 类 | **198 条**（748−550） | 50/批 | **4**（0028–0031，尾批 0031 为 48 条） |
| **P2** | H2 `freebsd-bugs` | 190683 封 | 500/批 | ≈382（**须按 offset 段跳**：139470→139970→…→161000 块尾，勿线性回退，空密度区会空烧约 276 批） |
| **P2** | H2 `freebsd-ports` | 170637 封 | 3000/批 | ≈57 |
| **P3** | H2 `freebsd-net` | 28645 封 | 3000/批 | ≈10（fn_b171 已预建 queued，part1 已完稿 190 条） |
| **P3** | shenyue C 类 | 1972 条 | 50/批 | **40**（0032–0071） |
| **P4** | shenyue 联网证据债务 | 实测 **747 条**（旧估 595 作废） | — | **已裁定「只登记不追补」**，台账 `_WEB_DEBT_REGISTER.md`（`5597bb3d7`）；裁定只登记，不重派评审员 |

---

## 七、已知坑速查（勿重复踩）

| 坑 | 处置 |
|---|---|
| 🔴 文档数字漂移（**本文档亦不免**） | 已实测 4 处：①台账「记 38000」实为 40000；②`_HANDOFF_H3.md` 称 fhk_b021「15 键」实为 13 键；③`_HANDOFF_H2.md` 称「4 库/501834 封」实为 3 库/397965（`freebsd-chat` 已 completed）；④`_H3_PROGRESS.md` 记「四批全闭应 62000/11.25%」是**加数错**（48000+6000+6000+6000=66000＝11.97%），台账实测 66000。**开工前必读台账 JSON，凡文档加总数必须当场验算** |
| 🔴 digest `from` 列＝回帖人、正文被引用块占满 | 读手把内容归给被引者 → 门禁命中后回 duckdb 取**完整正文**判本方口吻；纯转发则剔除（见 §3.1） |
| Wojtek Puchar 类 from 40 字截断 → 假阳性 | 门禁输出须人工分流「截断假阳 vs 真漂移」，不得整批改写 |
| 🔴 `_merge_parts.py` 摘要 20–80 字是**阻断级校验** | 超长即中止不写盘。须**先按「改动集＝原超长集」定点压缩至 ≤80 字再 merge**，压缩保留人名与版本号，禁从专名中间截断 |
| 候选文件整表重抄 | 必引入人名笔误。一律**脚本按 pk 定点替换**，断言 `hit == len(fixes)`，不符即中止不写盘 |
| 容器行（低 id 区 ≈15%） | 逐批读 `review_logs/<tag>_container_pks.txt`，读手一律不收 |
| 读手 pk 错位 | `fhk_b007` p4 偏移 8 位／`fhk_b008` p4 偏移 1 位。以行首 pk 转录，`_audit_author_match.py` 兜底 |
| lite 池叙述手臆造专名 | `fhk_b017` p1 实测 29 条臆造。`_audit_narr_propernoun.py` 筛，主会话只回原文重写可疑条 |
| 宿主预判号不存在 | `_HANDOFF_H3.md` 的 `1661/1673` 不在宿主池；**dump 后按年段从宿主池实测选宿主** |
| `_prep_batches.py` 尾部 ValueError | `--lib`/`--hosts` 取值被当 spec 解析；spec 与 digest 已正确生成，忽略 traceback 但须事后校验 spec 的 hosts/line_date |
| `_fetch_body` 覆盖输出 | 两次调用写同一文件致第一份丢失 → 已加 `OUTNAME` 参数 |
| 台账 append 非原子 | 读两遍核对；append 后立即 verify |
| 并行会话整索引提交卷走暂存件 | pathspec 提交；commit 前 `git update-index --refresh`；racy-stat 幻影先 refresh |
| 同文件并发 Edit 静默覆盖 | 编辑同一文件必须串行 |
| shenyue 报告内嵌多余页脚 | `_s25_ledger.py` 用 `re.search` 首匹配取 `NEXT:`，中段残留页脚会致 append 被拒。落账前删净中段页脚 |
| `.gitignore` 全局 `*.py` | 新脚本默认被忽略；`script/_db_row_mining/` 整目录只提宿主 md，工作工具按 gitignored 保留 |
| 等级门禁脚本路径 | **不在工作区根**，实为 `00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py` |
| Bash 写 `.py` 被 hook 拦截 | 用 Write 工具写脚本 |
| mail2d register 覆盖 claim_map | `cmd_register` 增量重跑会把 53 缩到 15 致 check 断言崩；已加 `merge_claim_map`（四场景单测过），修法只存磁盘 |
| 🔴 **体检脚本报零不可信** | `_check_author_mismatch2.py` 的 `latin_tokens()` 用 `re.split(r"[^a-z0-9.'\-]+",s)` 配 `not t.strip(".'-")` 过滤，实测对**所有**输入返回 `[]` → 3000 行全落「无法判定」而报「0 不符」（假阴性）。改 `re.findall(r"[a-z0-9]+",s)` 后真出 27 条。**任何报零的体检脚本先对一个已知阳性样本验证** |
| 摘要名提取的 CJK 边界 | `\u3000-\uFFEF` 漏 U+FF0E（全角句点），`Peter Czanik报告…` 句点被吞进人名。须 `ord()` 逐字判（3000–30FF／4E00–9FFF／FF00–FFF0） |
| digest 显示名无右括号 | `(Oliver Lehmann` 只有左括号，`\(([^()]*)\)` 匹配不到 → `find("(")`＋`rstrip(")").strip()` |
| 回改脚本取「旧文本」须查 DB | 候选文件把摘要截到 80 字，DB 存全文（1570990 全文 78 字含「…pure virtual method called」被截）→ `got_text == old` 断言必拦 |
| 修 `claim` 只改文本时大纲安全 | **前提：等级不动**。动等级则大纲块头「证据等级：Lx」与纪律句必须同步，否则等级门禁立刻 FAIL（见 §五「块头等级错标」）。判据写进回改脚本注释留档 |
| 转述≠必然降 L3 | L4 判据是「发件人自述自有行为／经验／判断」——转发他人内容**之外**还有自己的动作即仍为 L4。三条初判拟降 L3 经回正文撤回降级（见 §五 b157 回改行） |
| 体检脚本读候选文件而非 DB | `_check_author_mismatch3.py` 修完 DB 后仍报同一批「不交」，因候选文件是 register 前历史输入不回写。验修改须回 DB 比对 |
| 🔴 **行序 offset 记账勿靠推理相邻关系** | b157 spec offset 曾被误判「18000 与 b156 的 `[15000,18000)` 重叠」而改 21000，凭空造出 18000–21000「空洞」。实测两批 digest pk 端点 b156=1567555–1570595／b157=1570596–1573653 **完全连续**，实为相邻。若照误记从 24000 开 b158 会**真跳过 3000 行未读**。判定相邻只能实测 dump 产物 pk 端点——pk 是稀疏 bigint id，`offset+n` 与 pk 区间无可推导关系（实测 pk 跨度 3023/3041/3058 对应同为 3000 行） |
| 🔴 **判等级须三方比对，叙述句优先** | 等级门禁只能证明「DB 与大纲块头一致」，**不能证明两者都对**。b174 上次等级互串修复只改对一半（154884 改对、154885 改错），因门禁 PASS 长期不被发现。判等级时**大纲叙述句优先于 digest 截断正文与摘要**——叙述句由读过完整正文的叙述手所写，能看到 digest 预览截掉的部分（154884 只看 digest 会误判纯转述 L3，叙述句里的「给 lo0 加别名绕过并 netstat 验证」才是 L4 依据） |
| 修等级须一次改三处 | `claim.evidence_level` ＋ 大纲块头「证据等级：Lx」＋ 块尾纪律句。漏改纪律句不触发等级门禁（只查块头），但会留下语义自相矛盾的块 |
| 🔴 **`_outline_<tag>.py` 块头等级取自 `candidates.txt` 而非 claim 表** | 第 61–64 行按 `pk\|LEVEL\|摘要` 读候选文件，故候选与 DB 一旦不一致 audit 必 FAIL。**register 幂等键是 `source_id` + `content_hash`，改等级不重算 hash → 二次 register 静默 SKIPPED，DB 停在首次值**。b158 因此 audit FAIL 3 处（首 register 抓的是 463 半截快照写成 L4，读手其后重判 L3）。**处置**：读手重判在首 register 之后发生时，手工比 `candidates.txt` 与 `claim.evidence_level` 并**回改 DB**（DB 是旧的一侧），outline 不动——其块头与 TAIL 本就按 candidates.txt 生成 |
| 🔴 **读手未全部回报前不得 merge 候选** | b158 的 `_s62_merge_multi.py fpo_b158 6` 在 22:44 执行时 p2/p3/p5 仍在写分片（mtime 22:51／22:47／22:45），抓到中途快照→落盘 463、最终并集 449，**63 条错配行落库、49 条好行漏收**。判定：等所有读手 completion 通知齐＋分片 `mtime` 静止后再 merge。配套两条：**读手自报数字一律不信**（p5 自报 66 实 52、p7 自报 66 文件不存在、叙述手自报「越限 0」实测 20 条越限）；**不对写盘中的分片做抢救性改写**（先 TaskStop＋核实 mtime 静止） |
| 🔴 **`_merge_narr.py` 禁字符集含 `\|`，与 candidates 分隔符同名易漏查** | 除 `「」*` 外叙述列**也禁 `\|`**（b157 教训记「`\|` 是 candidates 分隔符故不查」，但 mount_narr 叙述列确实要查）；正则字面量 `\`（如 `m/\.$/`）同样踩线。b158 三条踩中（`1574616`／`1575789`／`1576445`）须改写为散文表述。另 `_merge_narr.py` 越限只打印不拦、照样写盘（见上行），故派单后必用 `_scan_narr_gate.py` 全库扫描，勿信自报 |
| 🔴 **`_merge_narr.py` 长度/禁字符是「非阻断级」** | 越限只打印不拦，**照样写盘**。fhk_b022 p2 实测 17 条超长（142–209）全落盘，须事后按 `_fix_narr_fhk_b022_p2b.py` 定点压缩再 merge。**阻断级**只有：缺文件、CRLF。`_merge_parts.py` 同理：**摘要越限（含禁字符）与尾标点是非阻断**，缺文件／BOM／CRLF／字段数／等级非法／pk 越界／跨份重复才是阻断 |
| 🔴 **duckdb `body` 列本身被截断** | freebsd-hackers 732 封恰在 1395–1405 字符（max 1703711）、freebsd-stable 274、freebsd-doc 217、freebsd-current 748。「全文正文」并非全文。**专名门禁分流判据**：命中且能在 `body`（精确或忽略大小写）找到 → 假阳保留；只在 `from_name`/`subject` 找到 → 假阳保留；`len(body)>=1395` → **截断假阳保留**；`len(body)<1390` 且三处皆无 → **真臆造，改写** |
| 🔴 **`_prep_batches.py` 一次只认一个 `--lib`** | `LIB` 在 `enumerate` 循环里被赋值最后一次，四库同批会全建到同一个源库（`dump`／`register` 就读错库）。**每库单独调用**。位参解析 bug 已修（原 `args=[a for a in sys.argv[1:] if not a.startswith("--")]` 把 `--lib`/`--hosts` 的**值**当 spec 喂给 `split(":")` → `ValueError: not enough values to unpack`）；预建后**必查 spec 的 `lib` 字段** |
| 🔴 **中文长度必须实测，不得手估** | 手估系统性偏低 5–40 字：fhk_b022 p2 四次 precheck 连续失败（141/145/180/151 → 142/153/141 → 147/152/141 → 141），每次按 `len()` 实印值再压。**压缩纪律**：只删枝节从句，绝不删版本号／路径／宏名／人名／等级归属；宁删重复标识符也不要改错标识符（本轮曾把 `kmem_map` 误打成 `kem_mem`，即臆造专名） |
| digest 分件 500 行不稳 → 拆 250 行半份 | `fhk_b022` p1/p2/p3 三份 500 行零落盘（读完用 1,021,646 token／947 秒后停在「Let me write the output file incrementally」）。**250 行/份是稳态**：`_split_halves_p1.py`（fhk_b022/fdoc_b001/fstb_b001）、`_split_halves_p2.py`（下一批四批，按行切） |
| 叙述手「派完即失联」须以磁盘为准 | 8 路叙述手 65 分钟零落盘即算死（不是超时，是进程已不在任务注册表）。**硬判据：开工后 5 分钟内必须有一次首落盘**（写前 8–10 条），之后每 10 条覆盖写全文。句柄不存在（`TaskStop` 报 `No task found`）＝已随会话中断消亡，直接重派即可 |
| 台账是 `spec-only` 口径 | `_build_read_ledger.py` 的游标从 `_batch_*.json` spec 推进，**spec 预建即推游标**，不等于 outline 已提交。预建下一批会把「已判读」抬高，勿据此宣称覆盖率。判据是 `review_logs/<tag>_claim_map.json` 是否存在 |

---

## 八、待主理人裁定（4 项，均已实测取证，取证详见 `_PLAN_20260921.md` §五）

1. **来源池回填的诚实边界**：转写回填标记 `sourcebank_origin: backfill` 是否接受；§9.4 体例性豁免是否合法；
   B 0017–0023 真未检索条目是否须重派。**当前状态**：已按「只登记不追补」登记 `_WEB_DEBT_REGISTER.md`。
2. **权威游标纳入 git 跟踪**（2026-09-21 17:50 实测**扩大为两个洞**）：
   - (a) `shenyue/review/_ledger.json`（shenyue 权威游标）未被 git 跟踪，仅 `_ledger.jsonl` 在版本控制内；
     被并行会话误删只能从 `.jsonl` 全量重建。
   - (b) 🔴 **`.gitignore:310:/script` 使整个 `script/` 目录未被版本控制**——H3 线的交接书
     `_HANDOFF_H3.md`、断点文档 `_H3_PROGRESS.md`、叙述任务书 `_NARR_TASK_freebsd-hackers.md`
     **全部不在 git 内**（`git check-ignore` 实测确认），与 H1 线 `_HANDOFF_H1.md`／`_H1_PROGRESS.md`
     已被 `git add -f` 提升的既有做法不一致。H3 是唯一活跃主线的交接件却无历史可回溯。
   - **须裁定**：是否将上述游标与 H3 交接件 `git add -f` 纳入版本控制？建议纳入（可逆、低风险）。
   - **未擅自变更**：此为共享仓库的版本控制状态改动，且本项本就列在待裁定清单，故只登记不执行。
3. **`_s25_ledger.py` 的 `web_date` 硬编码** `"2026-09-20"`：改按批次实际联网日期传入，还是维持批次日？
4. **pk 1573347（CL-RM-157167）应否改 `status='rejected'`**：摘要误归因回改时查明本条实为 Marco van de Voort 的**两条纯提问**
   （「is it evil to leave behind .cfg.sample files?」「如何改 pkg_add 注册目录?」），不含量化或结论性陈述，
   本不该收录。是否比照 `fhk_b021` 剔除 pk 1312976 的先例改 `status='rejected'` 并从大纲移除对应块？
   **已回改摘要文本、未改 status，等裁定。**（`_fix_b157_attrib_20260921.py` 理由串已标 ⚠）
