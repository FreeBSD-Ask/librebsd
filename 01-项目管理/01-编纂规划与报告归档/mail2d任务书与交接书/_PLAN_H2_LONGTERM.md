> ⚠️ 2026-10-04 主理人令：本文件内所有“git add -f”声明一律作废——script/ 下一律不入库、保留磁盘文件，禁止 git add -f（除非主理人显式声明）。

# H2 长线计划：ports／缺陷／网络／闲聊 四库全量判读路线图

> **建立时间** 2026-09-23 20:00｜**建立依据** 主理人 2026-09-23 裁定“继续。建立长线计划，40 路子代理”
> **配套文件** `_HANDOFF_H2.md`（v4，自包含交接书）｜`_RESUME_H2.md`（断点页，每次唤醒先看它）
> **本文件定位**：跨批次路线图与已知结构约束。**断点细节一律以 `_RESUME_H2.md` 顶块为准**，
> 本文件只回答“还剩什么、按什么顺序、按什么口径、有哪些坑”。
>
> 🔴🔴 **2026-09-24 主理人四项改判（已落地，勿回退）**：
> ① **pk 对齐断言**已落 `_chk_pk_align.py`，**派读手之前必跑**（§五 第 5 步）；
> ② **dump 自带自有文本内联**——`own_ratio<0.30` 或全文 `<200` 字的封不截断
>    （fn_b171 实测命中 591/3000＝19.7%）；
> ③ **“完成”拆成两个里程碑**——M1 挖掘完成 ≠ M2 语料可信，
>    M2 只能在 M1 收尾后一次性做，预算未估且很可能大于 M1（§2.3）；
> ④ **“只登记不追补”限制已取消**，改为授权追补（§2.5）。
> 另加**既往批次复核**：对既往分 10 路判读的批次逐个过 §七 第 1–4 项（§2.4）。

---

## 〇、战线范围（硬边界）

H2 拥有 **4 个库**，与 H1／H3／H4／H5 的库清单**互不相交**。只做本文件所列库，
其余库由另外 4 份交接书负责，**越界即破坏其他会话的工作**。

上游 `03-原始史料库/11-邮件列表史料/**.duckdb` **只读**，不得修改。

---

## 一、四库台账现状（2026-09-23 20:00 实测）

> 🔴 **2026-10-17 主会话同步**：本表为 **2026-09-23 规划快照**（彼时 ports 72,000、net 45,000），
> 结构亦已变动（表中列 `freebsd-chat`，现行 H2 四库为 ports／bugs／net／**isp**）。
> **现行真值见 `_HANDOFF_H2.md` §1.3.0 首块**：ports **182,999/191,637（95.49%）**、
> bugs **153,970/192,683（79.91%）** 在途，net 73,645／isp 31,347 已 `completed`；
> **合计 441,961/489,312＝90.32%**，余 **47,351 封**；下一站 `fpo_b212` @182,999／`fbug_b194` @153,970。
> 下表数字**勿作现行依据**。

数字取自 `mail2d_read_ledger.json` 的 `items`，claim 计数取自
`04-现代研究文献/historical_claims.duckdb` 的 `claim` 表（`claim_id LIKE 'CL-RM-%'`）。

| 库 | 全库封数 | 已判读 | 在途 | **剩余** | 每批 n | **剩余批数** | CL-RM claim |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `freebsd-ports` | 191637 | 72000 | +3000（`fpo_b175`） | **116637** | 3000 | **39** | 10264 |
| `freebsd-bugs` | 192683 | 10000 | — | **182683** | 500 | **366** | 5829 |
| `freebsd-net` | 73645 | 45000 | +3000（`fn_b171`） | **25645** | 3000 | **9** | 1230 |
| `freebsd-chat` | 43869 | 43869 | — | **0** | — | **0** | **0** |
| **合计** | **501834** | **170869** | **+6000** | **324965** | — | **414** | **17323** |

- **claim 水位**：库内 `max CL-RM seq = 218093`（＝ `fbug_b190` 收官条 `CL-RM-218093`）。
  🔴 **水位一律以 register 实报的“库内 max claim seq”为准**，不要从任何文档里抄起始号。
- 🔴🔴 **`freebsd-chat` 全库 43869 封判读完毕、CL-RM 产出 0 条**——
  14 个批次（`fch_b137`–`fch_b150`）走完整个流程，产出为零。
  **这是“低史料库”的定论证据**，也是本计划把 chat 直接判为 `completed` 的依据。
  **不要回头重判 chat**——除非主理人改判史料标准。

### 1.1 `freebsd-net` 的归属澄清

`_batch_fn_b171.json` 的 `note` 字段写着“**H3 线** freebsd-net”，**这是标注笔误**。
权威归属依据：
1. `_HANDOFF_H2.md` §二 把 `freebsd-net` 列为 H2 第 3 库；
2. `_HANDOFF_H3.md` 全文**不含** `freebsd-net`；
3. `_RESUME_H2.md` 明确记 `freebsd-net` 台账状态并写“`fn_b171` 已在途，**勿重复建批**”。

🔴 **`fn_b171` 已预建**（offset 45000、n 3000、`pk_range [1482312, 1485311]`、
`queued: true`、digest 与 4 个分件已于 2026-09-21 04:39 落地，`fn_b171_candidates_p1.txt`
已有 **190 条**）。**续跑须先做覆盖双查**（claim 0／大纲 0），**不要重新 `new`＋`dump`**——
重 dump 会作废已在产的 190 条候选。

---

## 二、波次路线图

### 2.1 立即下一波（本会话续跑）

| 顺序 | 批次 | 库 | offset | 当前状态 |
| --- | --- | --- | --- | --- |
| 1 | `fpo_b175` | ports | 72000 | 12 分件已读毕；🔴 **p8 过度抽取待压缩**（244 条／97.6%，须压到 ≤45）；随后 gate→merge→check→register→body→split→叙述 |
| 2 | `fn_b171` | net | 45000 | 预建在途；p1 已 190 条，**p2/p3/p4 待补**；先覆盖双查再补派 3 路读手 |
| 3 | `fpo_b176` | ports | 75000 | 未建 |
| 4 | `fbug_b191` | bugs | 147470 | 未建（**仍在 1994–1998 高密度窗内**，见 §3.1） |

### 2.2 中长期排程（建议批序）

**ports（39 批，offset 75000 → 191637）**：
`fpo_b176`…`fpo_b214`。收率带 **8–14%**，超 20% 即过度抽取。
历史实测各批 29–86 条/批，整批均值约 17%（本波次略高于带，见 §7.3）。

**bugs（366 批，offset 147470 → 192683）**：
- **阶段一（高密度窗，28 批）**：offset 147470 → 161098，
  `pk` 约 1056183 → 1069844，1994–1998 内容密度近 100%，
  历史收率 **55–75%**（实测 b189 69.6%、b190 68%）。
- **阶段二（窗外稀疏区，338 批）**：offset 161098 → 192683。
  🔴🔴 **本区收率预计大幅下降**——按 §3.1 的年份同质结构，
  窗外批次的“窗口内行”占比趋零。**建议每 10 批复核一次实际收率**，
  连续 3 批低于 8% 时**上报主理人裁定是否继续或改判史料标准**，不要闷头空烧。

**net（9 批，offset 48000 → 73645）**：
`fn_b172`…`fn_b179`（末批 `n` 取剩余 400 或按 3000 取整后按实际截断）。
🔴 **net 的宿主是 `1391/1392/1393/1394/1405/14111/1031/1032/884`**
（来自 `fn_b171` spec），**与 H2 交接书 §二 预判的 `364/187` 不一致**——
预判是 dump 前的猜测，**以实际 spec 的宿主列为准**。
fn_b171 p1 实测收率 190/750 = **25.3%**，远高于 ports 带——
🔴 **net 的收率带须本批重新标定**，不要套用 ports 的 8–14%。

**chat**：已完成，无排程。

### 2.3 总量估计——**两个里程碑，不是同一个“完成”**

🔴🔴 **2026-09-24 主理人改判：把“完成”拆成两件独立的事，分别排预算。**
之前把 10–15 天当成“语料可信”的 ETA，是最大的认知偏差——
那个数字只是**判读游标到 100%**，不是内容可信。

| 里程碑 | 定义 | 预算 | 可否边挖边做 |
| --- | --- | --- | --- |
| **M1 挖掘完成** | 四库判读游标 100%，全部批次走完候选→叙述→大纲→提交 | 414 批 × 12–18 分钟 ≈ **83–124 机时** | 本阶段 |
| **M2 语料可信** | 全部已入库 claim 逐条回源复核完毕（正文 0 命中的断言已删／已改） | 🔴 **未估，且很可能大于 M1 本身** | ❌ **只能在 M1 收尾后一次性做** |

**为什么 M2 不能边挖边修**：回源复核的判据是“断言是否在正文 0 命中”，
而一条 claim 的正确性会随后续批次的补记而变化；且 M2 要按宿主章节重排块，
与 M1 正在写的宿主文件正面冲突。硬要并行，两边都在改同一批宿主文件。

**M2 的量级依据**：mail2d 现有 **134,328 块**，
按 tk_b144 实测——单批 4385 条回源逐封对读就修了 **400 余处**（约 9%），
其中“档案状态泄漏句”一类约 300 条。若按 9% 外推 134,328 块 ≈ **12,000 条待改**，
每条要读正文＋改写＋回写三处（`claim.claim_text`／`evidence.fact_text`／候选文件），
单条 30–60 秒量级 ≈ **100–200 机时**。**这个数还没算“跨封借串”类需要整条重建的。**

🔴 **不得用“三分之一缺陷率”宣布收官**——若 M1 收尾时未给 M2 排预算，
就是明知内容不可信而宣布完工。

**建议节奏**：每会话 2–4 批闭环（读手波＋叙述波＋提交），
按当前实测吞吐约 **每 90 分钟闭环 1 批**（含 40 路读手 15 分钟＋叙述 11 分钟＋门禁提交）。

### 2.4 既往批次复核（2026-09-24 主理人增补）

🔴 **对既往分 10 路判读的批次，逐个复核是否存在本次增补的第 1–4 项问题，逐个修改**
（不是抽检，是逐批过一遍）。第 1–4 项即 2026-09-24 增补的
① pk 对齐 ② 截断臆造 ③ 档案状态泄漏 ④ 署名与方向（含整条挂错／跨封借串）；
其中 ③ 在 §七.1 第 10 项、④ 对应 §七.1 第 1／2／3／5 项。
复核对象按入库时间倒序，先做缺陷率最高的批：

| 复核项 | 判据 | 检测手段 |
| --- | --- | --- |
| 1. pk 对齐 | digest／cands_body 与源库正文同源 | `_chk_pk_align.py <tag>`（已落地，见 §五 第 5 步） |
| 2. 截断臆造 | claim_text 断言在正文 0 命中 | 叙述手回源逐封读（结构门禁与 token 回源**均查不出**） |
| 3. 档案状态泄漏 | 描述我方存档／读解能力而非邮件本身 | 叙述手回源逐封读 |
| 4. 署名与方向 | 张冠李戴、整条挂错、取反、跨封借串 | 叙述手回源逐封读（本批已实测抓到 p5 1482977 sbruno→dim） |

🔴 **派 10 路复核读手**（非叙述手，故不受 ≤20 路限制内的叙述侧约束），
每路一份已完成批次的 candidates＋cands_body，产出“缺陷清单”而非改写：
`<tag>_review_p<K>.md`，逐条写 `pk｜claim_text 说法｜正文实际｜建议处置`。
主代理据清单外科回写，**回写只改 `claim.claim_text` 与 `evidence.fact_text`，
绝不碰 `evidence.quote`**（quote 是原文引用，改动即篡改史料）。

### 2.5 债务追补政策（2026-09-24 全局改判：**取消“只登记不增补”**）

🔴🔴 **“只登记不追补”这条限制已取消**（主理人 2026-09-24；
H4 线 `_HANDOFF_H4.md §10.6` 2026-09-23 已先行改判，本次为全局生效）。
之前保留它的理由是“回写要重跑 register，而 register 幂等键
`source_id+content_hash` 会跳过已登记条、让库内残留旧 `claim_text`”——
这个障碍已经有确定性的解法，不再是理由。

**追补标准动作（块数不变，无需 purge／re-register）**：

🔴🔴 **实测订正（2026-09-24）**：本节的 SQL 骨架**不能直接用**。
`evidence` 表**没有 `claim_id` 列**，`claim` 表也**没有 `source_id` 列**，
两表须经 `claim_evidence(id, claim_id, evidence_id, role, strength,
disposition, search_log_ref, created_at)` 关联。直接
`UPDATE evidence SET fact_text=... WHERE claim_id=...` 会报
`Binder Error: Referenced column "claim_id" not found`。
已落地的工具是 `_fix_claims.py`（本节下方），照它写不要手拼 SQL。

```sh
# 0. 先取 claim_id 与源证据行（source_id 在 evidence 侧）
SELECT e.source_id, ce.claim_id, c.claim_text, e.fact_text
FROM evidence e
JOIN claim_evidence ce ON ce.evidence_id = e.evidence_id
JOIN claim c           ON c.claim_id = ce.claim_id
WHERE e.source_id = 'SRC-rowmine:<lib>.messages.<pk>';

# 1. 只改两处文本字段，quote 绝不碰
UPDATE claim   SET claim_text = '<订正后>' WHERE claim_id = 'CL-RM-NNNNNN';
UPDATE evidence SET fact_text = '<订正后>'
WHERE evidence_id IN (SELECT ce.evidence_id FROM claim_evidence ce
                      WHERE ce.claim_id = 'CL-RM-NNNNNN');
# 2. 同步候选文件，保持 candidates.txt 与库内一致
# 3. 不动 evidence.quote、不动 evidence_level（除非是等级真错，另走 audit 三改）
# 4. 不动大纲块（叙述与大纲已正确的不要动）——除非叙述也错，那要同步改块正文
```

🔴 **落地工具 `_fix_claims.py`**（`C:/Python314/python.exe _fix_claims.py
<lib> <tsv> [--apply]`，tsv 三列 `pk<TAB>类别<TAB>订正后 claim_text`）：
一次 `WHERE e.source_id=?` 取 join 三元组 → 幂等（已正确打印 `[same]` 跳过）
→ 只外科改 `claim.claim_text` 与 `evidence.fact_text` →
`duckdb.IOException` 并发写重试 6s×8。退出码 0 成功／1 未改／2 参数错／
3 tsv 格式错／4 DB 锁未获。
🔴 **坑**：不要写 `con.execute("COMMIT")`——本 build 的 duckdb 自动提交，
显式 COMMIT 抛 `TransactionContext Error: cannot commit - no transaction is
active`，而 UPDATE 其实已经落库，会让成功的追补看起来像失败；用
`CHECKPOINT` 代替。
🔴 **坑**：`claim_text` 硬上限 **80 字**（tech-kern 36706 行实测 max 恰好 80、
零条超限），所有订正后文本必须用 Python `len()` 实测 ≤80。
🔴 **坑**：`%` 在 bash 单引号 SQL 里会破坏解析器，用参数绑定
（`'...' + chr(37)`）。
🔴 **坑**：`messages.id` 是 VARCHAR，`WHERE id IN (...)` 前必须
`CAST(id AS BIGINT)`；但逐行 CAST 点查实测 >5 分钟，一律改单条 `WHERE id IN (...)`。

🔴 **等级错标不是追补、是审计**：走 `evidence_level` 三方一致改
（`claim.evidence_level`＋块头 `证据等级：L*`＋纪律尾句），见 §八 第 1 项。
🔴 **register 幂等保留旧 `claim_text` 的坑仍然有效**——每次 register 之后
必须跑一次 `claim_text` 同步（H5 线已把这条写成常驻检查）。
🔴 **候选侧缺陷仍须一律修完才入库**（`_H1_PROGRESS.md` 既有裁定：
“所有错误允许改正”），追补政策不放宽候选层门禁。

---

## 三、关键结构约束

### 3.1 `freebsd-bugs` 的 pk 空间是“年份同质大段”（最重要，直接决定批序）

实测（`_HANDOFF_H2.md` §9.6，2026-09-21）：

| pk 带 | 行数 | 1994–1998 占比 | 线性 offset 起点 |
| --- | --- | --- | --- |
| 909129–959128 | 49948 | 0.0% | 500 |
| 959129–1009128 | 49992 | 0.0% | 50448 |
| 1009129–1059128 | 49956 | 24.9% | 100440 |
| 1059129–1109128 | 42286 | 21.4% | 150396 |
| 1109129–1115358 | 1 | 0.0% | 192682 |

- **连续 pk 段年份同质**：任取 500 行样本，落点年份基本 100% 同一年。
  所以**按线性 offset 一批批往前跑时，命中率不是全库均值，而是 0% 或 100% 二值**。
- **未读的窗口内行集中在一段连续块**：`pk 1046661–1069844`，
  对应 **offset 137970–161098**（约 47 批 × 500）。
  🔴 **本波次已推进至 offset 147470**（`fbug_b190` 收官），
  **窗口内剩余 offset 147470–161098 ≈ 28 批**。
- **不要从 offset 100440 或 150396 起跑**——那两段块内外交杂。
  **按线性 offset 从当前游标递增即可**。
- **台账已读区间为两段**：`[(0,500), (137970,147470)]`——
  `fbug_b171` 读的是 offset 0–499（稀疏混合区，11.2% 收率），
  **该收率不可外推到后续批次**。

### 3.2 `freebsd-ports` 的收率带与主题带

- 收率带 **8–14%**，**超 20% 即过度抽取**（硬判据）。
- 🔴🔴 **收率是“过度抽取”的唯一客观信号**——读手无法从内容上分辨，
  只有收率能拦住（见 §7.3 本波次实证）。
- 宿主口径见 §4。

### 3.3 上游只读

上游 `03-原始史料库/**.duckdb` **只读**，任何写操作都会破坏其他战线的源数据。
`historical_claims.duckdb` 并发写会 `IOException`——**重试（间隔 6 秒、至多 8 次）**。

---

## 四、宿主口径速查

### 4.1 `freebsd-bugs`（宿主 `881`／`886`／`887`，位于第 88 章）

宿主文件（**提交 pathspec 用这些精确路径**）：

```
05-卷册大纲/第05卷-freebsd的工程化奠基/第88章-freebsd2x站稳脚跟/88.1-1994-1998-年-2-0.md
05-卷册大纲/第05卷-freebsd的工程化奠基/第88章-freebsd2x站稳脚跟/88.6-对-FreeBSD-2-x-的批评-技术债务与-SMP-滞后-对.md
05-卷册大纲/第05卷-freebsd的工程化奠基/第88章-freebsd2x站稳脚跟/88.7-重要贡献者与边缘者-2-x-时期被遗忘的驱动维护者-2-x.md
```

| 宿主 | 口径 |
| --- | --- |
| **881** | 兜底章——内核／二进制／安装流程／网络守护进程／**一般安全缺陷** |
| **886** | 磁盘切片／分区表／disklabel／fdisk／扇区柱面磁道／软驱制作／ATA 与内存探测（memsize）／fixit 修复盘与 **MAKEDEV** |
| **887** | **驱动探测 probe**／SCSI 卡识别／CD-ROM 光驱／声卡／外设驱动（psm 鼠标、串口卡、磁带机）／**网卡驱动识别**／引导程序（biosboot／boot.c）／**docs/* 手册页与实现不一致** |

🔴🔴 **三条高频误判**：
1. **一般网络缺陷与多播 → 881，不是 887**（887 只管驱动与手册页）。
   实测本波 `vx0 receives any and all packets`／`route -iface` 属 881。
2. **本库无“安全执行”专章**：`crontab security hole`／`rlogind not using passwords`／
   `su(1) does not call skeyaccess()` 等**安全缺陷一律落 881**。
3. **`docs/*` 只有“手册页与实现不一致”才落 887**。
   实测 `docs/2561`（www 页面文字改动）、`docs/2559`（无内容虚假 PR）
   均**不属手册页与实现不一致，落 881**——已由 p6／p7 两路叙述手独立裁定。

### 4.2 `freebsd-ports`（宿主 `891`／`892`／`894`／`906`／`907`／`909`，🔴 **禁 `883`**）

| 宿主 | 口径 |
| --- | --- |
| **891** | Jordan Hubbard 谱系——🔴 **极窄**，历史**连续 8 批零块**，确实命中谱系才写，拿不准一律落 892 |
| **892** | 兜底——具体端口构建／升级／依赖缺陷 |
| **894** | 取件与构建基础设施（pkgng、Mk、index 构建、升级工具、clang 编译 ports） |
| **906** | 端口树规范与依赖卫生 |
| **907** | 去弃置政策与执行（deprecation campaign、removed ports、KDE3 EOL、优先级与组织行为） |
| **909** | 许可证执行公告与漏洞通告适用性 |

### 4.3 `freebsd-net`（宿主 `1391/1392/1393/1394/1405/14111/1031/1032/884`）

🔴 **以 `fn_b171` spec 的宿主列为准**，不要按 H2 交接书的预判 `364/187`。
各宿主的口径界定**须由首批 dump 后的实际判读确定**，并在本文件增补。

---

## 五、每批标准链（12 步，勿跳步）

```sh
PYD=C:/Python314/python.exe                      # duckdb 脚本（管线/门禁/verify）
PY =C:/Users/ykla/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe   # 纯文本脚本
cd D:/librebsd/script/_db_row_mining

# —— 建批与画像 ——
 1. $PYD _mail2d_run_batch.py new  --db <库> --offset <起点> --n <本批> --tag <tag> --hosts <宿主>
 2. $PYD _mail2d_run_batch.py dump --tag <tag>
    🔴 2026-09-24 起 dump 自带“自有文本内联”：own_ratio<0.30 或全文<200 字的封
    在 digest 里**不截断**（阈值 `FULL_RATIO`／`FULL_MINCH` 环境变量可覆写）。
    实测 fn_b171 命中 591/3000＝19.7%，平均 2715 字——这些正是引用密／过短、
    420 字截断伤害最大的封。dump 会打印 `[full ]` 行，条数须抄进任务书。
 3. 🔴 手工补回 spec 的 pk_range（new 会清空）——否则 check 直接 SystemExit
 4. 覆盖双查：claim 0 条 / 大纲 0 块（check --pk-coverage 或双查脚本）
 5. 🔴🔴 pk 对齐断言（2026-09-24 新增，**派读手之前必跑**）：
       $PYD _chk_pk_align.py <tag>
      两层检查：L1 digest 每行按 pk 回连源库比正文 420 字；
      L2 cands_body 分块键 == 候选 pk 集且块内含该 pk 源库正文前 40 字。
      🔴 **EXIT 1 即整批拒收、重建后再派读手**——串行一旦混入，读手看到的正文
      与他记下的 pk 来自两封不同的信，产出的摘要必然张冠李戴，
      且 token 回源审计抓不出（摘要里的词往往能在别的 pk 正文里命中）。
      靠叙述手回正文时顺手报矛盾太贵（一整波 20 路重派回源），
      而且只有恰好回查的叙述手才会报，漏报是常态。

# —— 候选层（读手波）——
 6. split digest（ports/net 12×250；bugs 5×100）
    🔴🔴 _split_digest.py 只写 _part<K>.txt；读手任务书要求 _p<K>.txt——须 cp -n 补齐
 7. 写 _READ_TASK_<tag>.md → 派读手（≤40 路，同批只用一式切分）
 8. 扫盘 _watch_<tag>.py → gate：$PYD _gate_cand.py <tag>
 9. merge：$PYD _s62_merge_multi.py <tag> <N>

# —— 候选层闭环 ——
10. $PYD _mail2d_run_batch.py check     --tag <tag>          # 须 违规 0、越界 0
11. $PYD _mail2d_run_batch.py register  --tag <tag> --apply  # 先跑不带 --apply 的 dry
12. $PYD _mail2d_run_batch.py body      --tag <tag>          # 1400 字正文
13. $PYD _chk_pk_align.py <tag>         # L2 层二次确认（register 后才有 cands_body）
14. $PY  _split_narr.py <tag> <N>       # 每包 24–25 条

# —— 叙述层 ——
15. 写 _NARR_TASK_<tag>.md → 派叙述手（🔴 ≤20 路/波）
16. $PYD _verify_<tag>_narr.py          # 主代理阻断式门禁，须 EXIT 0
17. $PYD _merge_narr.py <tag> <N> <宿主> # 须显示 违规: 0

# —— 落地与提交 ——
18. $PYD _mail2d_run_batch.py outline   --tag <tag> --write  # 二跑须 +0
19. $PYD _mail2d_run_batch.py bookkeep  --tag <tag> --write  # 三零 PASS
20. cd D:/librebsd && $PYD "00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py"
21. git add -- <本批宿主文件逐个 pathspec> && git commit
    🔴 期望 added = 块数×5、deleted = 0；/script 整目录 gitignore，script/ 下须 git add -f
22. 刷新 _RESUME_H2.md（🔴 `_build_read_ledger.py` 全量重建已禁用——会回退 freebsd-bugs／elastic 游标；台账一律走外科补丁，见 _HANDOFF_H2.md §十.9）
```

---

## 六、并发与授权（主理人 2026-09-23 裁定）

- 🔴🔴 **40 路子代理随时可派，不因波次或实测 RPM 自我收缩**。
- 🔴🔴 **同批只用一式切分**（`_merge_cand` 按 `<tag>_candidates_p<K>.txt` glob，
  第二参 N 即路数；40 路须 `_split_digest <tag> 40` 且**先删旧 `_p<K>` 候选**）。
- 🔴 **叙述手单波 ≤20 路**（**作废**：2026-09-29 主理人令混流 40 路，见 _HANDOFF_H2.md 文末 §◐B）（读手波可直接 40 路）。57 路一次派实测 15+ 路
  `token plan entitlement exhausted`。
- 🔴 **子代理回报一律不信**，以盘上 `wc -l` ＋门禁实测为准（本系列已 15+ 次实证破产）。
- 🔴 **不得建 automation／cron／闲时任务**；**不得用 CreateWorkflow**（shenyue 线约束）。
- 🔴 **共享 JSON 只改自己库的条目**（读-改-写），不得整文件覆盖；
  **不 commit 他人改动**；`git add -A` 会把并行会话的改动一起卷走。
- 🔴 **不删 `.git/index.lock`**（sleep 15 重试）；**不 `--force`**；**不 amend**。
- 🔴 **产出根必须是 `D:\librebsd\script\_db_row_mining\review_logs\`**——
  仓库根 `D:\librebsd\review_logs\` 是**别的会话的目录**。
- 🔴 **重派须换更短的提示词，不要加约束**（越加约束越容易零产出）。

---

## 七、已实证缺陷族与自检判据

### 7.1 内容级缺陷族（门禁全盲，只能回源逐条对读）

1. **摘要整条主语写错**——最高频真缺陷，结构门禁完全查不出。
2. **多层引用块归属错**——`>`／`>>` 里第三方断言挂给本封 FROM。
3. **方向写反**——取反、主客体颠倒、状态词方向（`closed-open` 当关闭）。
4. **臆造专名版本**——缩写展开、CVE 编号、硬件型号、PR 号。
5. **跨 pk 搬运细节**——相邻行摘要被并入其他行（含整份错位一行）。
6. **主题行外推**——CVE／时间窗／版本号／硬件型号／PR 号只出现在主题行时即为臆造。
7. **GNATS 两坑**——`Originator` 当发件人；PR 模板“提交者 ≠ 问题作者”。
8. **自引本人旧邮件当新判断**——须按 L3 转述口径写（本波 1055820 主代理已裁定，
   p3 叙述手独立证实现正文 FROM 实为 `J Wunsch` 而非清单写的 `mark thompson`）。
9. **等级误判**——`State-Changed-Why` 属维护者自有判断应 L4；纯转述应 L3。
   本波 p2 已报 1055751 挂 L3 实为 L4，**待外科订正**。
10. **档案状态泄漏族**——叙述描述我方存档／读解能力而非邮件本身。
11. **空正文无签名**——`LENGTH(body)` 为 2/3 的空正文不得虚构签名。
12. **PR 号漏斜杠**——`conf2558`→`conf/2558`（本波 token 回源抓出 2 条）。

### 7.2 子代理自报不可信族（本波新增实证）

🔴🔴 **读手画像可整段失实**（`fbug_b190`，2026-09-23）：
读手回报的分件 pk 范围**与磁盘实读全部不符**（自称 p1 1055683–1055803，实测
p1 1055683–1055782，各 100 行连续），且**整段主题分布是编造的**——
自称本批有“PR-31427 高密度线程”“PR-31441／Intel Pro 1000 PT 驱动探测失败（76 封）”，
实测关键字扫描**对这些 PR 号段 0 命中**，真实主题是 1996 年末–1997 年 1 月的
PR-2400～2670 段。读手自报 L4/L3＝303/37 亦错（实测 292/48）。
**但 340 条候选摘要本身通过 token 回源核验**（仅 4 条标记且均可解释）。

**判据**：
- 🔴 **读手回报的画像一律要磁盘复核**（digest 分件 pk 边界 + 关键字扫描），
  不要直接抄进叙述任务书——本波 14 路叙述手因此拿到了失实的 §二 指引，
  好在“以 narrpkg 为唯一权威”的兜底条款把损害限制在指引噪声。
- 🔴 **token 回源核验能抓拉丁 token 幻觉，抓不到整条张冠李戴**——
  两者都须做，不可互相替代。
- 🔴 **14 路叙述手独立抓到 40+ 处摘要失真**，印证“回源逐条对读”不可替代。

### 7.3 收率越限族（本波新增实证）

🔴🔴 **读手过度抽取无任何内容级信号**（`fpo_b175` p8，2026-09-23）：
单分件 250 行收 **244 条（97.6%）**，242 条 L3，摘要质量全部合格、格式全对、
pk 唯一升序——**所有结构与质量检查都抓不出**。244 条里绝大多数是纯致谢、
纯同意附和、仅复述他人结论的回复，即“L3 转述”被滥用为“什么都收”。

**判据**：
- 🔴 **收率是唯一客观信号**。ports 8–14%／超 20% 硬判；bugs 窗口内 55–75%。
  **每批 gate 后必须先看收率再决定下一步**，不要等 register 后才发现。
- 🔴 **过度抽取须整件压缩重派**，不要外科手术式随机删——
  删哪条需要重读正文判断，等价于重做该分件。
- 🔴 **压缩提示词须给出硬上限条数 + 显式剔除清单 + “只删行不重写”**
  （避免二次臆造）。

### 7.4 工具与格式坑（累计）

- `%` 多占位符格式化**必须传 tuple**（传 list 抛 `not enough arguments`，
  且崩点常在 `io.open("w")` 已截断目标文件之后）→ 大文件写入须先算完再 `os.replace`。
- claim 主表叫 **`claim`**（非 `historical_claims`）。
- 中文 `len()` 只能实测不能估（连主代理自己都翻过车：估 80 实 101）。
- `wc -l` 缺末尾 LF 会少算一行 → 计数口径用
  `rstrip("\n").count("\n") + 1`。
- **块头标记是 `<!-- ROW_MINE: <lib>.messages.<pk> -->`**，不是 `ROW_MINE:`——
  `grep -c '^ROW_MINE:'` 恒为 0。
- Bash 不能写 `.py`（hook 拦截），须用 Write 工具；Bash cwd 不跨调用保持。
- 内联 `python -c` 遇反斜杠／竖线须用 `chr()` 转义；`SyntaxError: unterminated string literal`
  即改写成 `.py` 文件。
- `DuckDB messages.id` 是 VARCHAR，逐行 `CAST(id AS BIGINT)` 点查 >5 分钟，
  必须改单条 `WHERE id IN(...)`。
- **`new` 会清空 spec 的 `pk_range`**——须手工补回，否则 `check` 直接 SystemExit。
- **`register --apply` 增量重跑会覆盖 `claim_map.json`**（已加 `merge_claim_map` 修复）。
- 🔴 **`register` 幂等会保留旧 `claim_text`**——只外科 UPDATE `claim.claim_text`
  与 `evidence.fact_text`，**绝不碰 `evidence.quote`**，每次 register 后必跑。
- 🔴 **`outline` 对已存在 `ROW_MINE` 标记直接跳过**——漂移后二跑只打印 `+0`（幂等假象）
  而宿主残留旧叙述。**merge 后、outline 前**漂移：重合并再 outline 即可；
  **outline 已跑过**必须 `_reblock_<tag>.py` 式逐块删除＋重插。
- 🔴 **block 数与插入行数**：期望 `added = 块数×5`，但部分块为 4 行时会出现良性偏差——
  权威判据是按宿主的 `ROW_MINE:` 块计数，行数是辅助。
- 🔴 **`outline` 的 `[dry]` 行是同一命令内的两次执行**，不要误读为两次 `--write`。

---

## 八、当前断点（下一次唤醒的第一条命令）

**A. `fpo_b175`（在途）**——12 分件已读毕，**p8 须先压缩**（244→≤45 条），
随后：

```sh
cd D:/librebsd/script/_db_row_mining
C:/Python314/python.exe _gate_cand.py fpo_b175
C:/Python314/python.exe _s62_merge_multi.py fpo_b175 12
C:/Python314/python.exe _mail2d_run_batch.py check --tag fpo_b175
C:/Python314/python.exe _mail2d_run_batch.py register --tag fpo_b175 --apply
C:/Python314/python.exe _mail2d_run_batch.py body --tag fpo_b175
C:/Python314/python.exe _split_narr.py fpo_b175 20
# → 写 _NARR_TASK_fpo_b175.md（按本文件 §四.2 宿主口径）→ 派 ≤20 路叙述手
# → _verify_fpo_b175_narr.py → _merge_narr.py → outline → bookkeep → audit → commit
```

🔴 **写 `_NARR_TASK_fpo_b175.md` 前必须磁盘复核读手画像**（见 §7.2）——
digest 分件 pk 边界＋关键字扫描，不要抄读手回报。

**B. `fbug_b190` 一条遗留债务**：pk **1055751** 登记为 L3，
p2 叙述手回源证实正文为“维护者自行改状态＋改责任人”＝自有判断，**应为 L4**。
外科订正（不影响块数，走改挂）：

```sh
# 1. UPDATE claim.evidence_level / evidence.evidence_level WHERE claim_id=<该条>
# 2. 改宿主 88.1 中该 pk 块头抬头的等级字面
# 3. 重跑 audit_evidence_level_labels.py 须 PASS
```
🔴 **只改等级字面，绝不碰 `evidence.quote`**。

**C. `fn_b171`（预建在途）**——先覆盖双查，再补 p2/p3/p4 三路读手：

```sh
cd D:/librebsd/script/_db_row_mining
C:/Python314/python.exe _mail2d_run_batch.py check --tag fn_b171   # 或双查脚本
# pk_range [1482312,1485311]：claim 须 0 条、大纲须 0 块
# → 确认无重叠后补派 p2/p3/p4 读手（p1 已有 190 条）
```

**D. 下一波建批**（b175／b190／fn_b171 全部闭环后）：
`fpo_b176`@75000 ＋ `fbug_b191`@147470 ＋ `fn_b172`@48000。

---

**计划版本** 2026-09-23 v1（4 库 414 批路线图；含本波次两大新缺陷族：读手画像整段失实、
读手过度抽取无内容级信号）
