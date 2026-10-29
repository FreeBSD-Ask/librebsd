# Task 3A.6 交接书：76 个按卷任务组（ZCode／glm-5.3-flash，x 会话并行）

> **性质**：交接书，不是新规则。执行者须以 §0.1 的真值优先级为准；本文只把已有规则、注册表与 V01 实测经验串成可执行流程。
> **适用**：ZCode 的 glm-5.3-flash，x 个会话并行；每会话按 §5 认领卷组，按 §4 逐卷作业，按 §6 过检查点。
> **签署权**：卷级批准仍属 ykla；任何会话不得自批、不得写 `approved/`。

## 〇、先读三件与占位符

### 0.1 真值优先级（冲突时以此裁决）

1. `00-编纂规则与格式规范/01-规则/小节建制与题名规则.md`（阈值、禁令、批准单位）
2. 仓库根 `AGENTS.md`（项目布局、红线与每批门禁）
3. `05-卷册大纲/映射/parallel/title/README.md`（并行协议、写者边界）
4. `05-卷册大纲/映射/parallel/title/taskgroups.tsv`（每卷数值的唯一机器可读真值）
5. `05-卷册大纲/映射/parallel/title/V{NN}/task.md`（该卷任务卡）
6. 本文（流程编排；与上五件冲突时以上五件为准）

### 0.2 x 占位符（共六处，按上下文填入）

| 编号 | 出现处 | 含义 | 本次由 ykla 填 |
| ---- | ------ | ---- | -------------- |
| ① | §5.1 首句 | 并行会话总数 | x |
| ② | §5.1 分工表 | 每会话每轮认领的组数 | x |
| ③ | §5.1 分工表 | 总轮数（75 组 ÷ ① ÷ ② 向上取整） | x |
| ④ | §5.2、附录 A | 会话标识（如 `s1`…`sx`） | x |
| ⑤ | §6.5 | 每累计 x 卷做一次里程碑汇报 | x |
| ⑥ | 附录 A | 该会话本轮起止组号（`TG-V{NN}`–`TG-V{NN}`） | x |

其余数字（76 卷、544 章、3,951 节、15,206 件、168,225,093 B、V01 363 条、余 75 组）是**事实值**，不要改。

## 一、前因后果

### 1.1 为什么要重制小节层

旧 `05-卷册大纲/` 树的 15,206 个“小节”实为史料颗粒：题面不合格率 68.4%、题指纹命中率 6.4%，TF 修补 60 批未解决。根因有两条：

- **无题名门禁**：题名合规只靠人工与提示词，写坏无人拦。
- **由史料反推结构**：先有块再起题，题名只能描述块，无法构成论证骨架。

### 1.2 处置零与四条线

2026-10-29 起重制，四条线分头推进（均已完成或进行中）：

1. **置零线**（已完成）：`mapping.tsv` 37,484 行 status 复位、`layout.tsv` 清零、15,206 个 `.md` 清空并补 3,951 个 `.gitkeep`，打 tag `outline-zero-20261029`。
2. **旧树线**（已完成）：`旧大纲-20261023/` 37,484 子节全在盘，只作语料、不回迁。
3. **标题线**（本任务）：先设计全卷标题，逐卷批准，**标题未批不得进内容批**。
4. **结构线**（未开）：OUTLINE 第四级（小节行）、装配、页面与门禁扩展，属 Task 5。

### 1.3 V01 样板已批（照此口径）

- `映射/title-design/V01.tsv`：10 章 61 节 **363 条**，`status=final`。
- `映射/title-evidence/V01.tsv`：**897 行**四源证据；`exceptions/V01.tsv`：**232 条**（1 条拆节提案＋231 条 `corpus_gap`）。
- 指纹 `ledger_sha256=52d7b522…`；`approved/V01.title.ok` 与 `approvals.tsv` 已写；tag `outline-v01-titles-approved-20261029`。
- 实测教训：V01 有 34 个节无史料（占 56%），其中 231 条标题以 `corpus_gap` 登记；**不许拿“史料”充数**。

### 1.4 3A.6 的范围

全 3,951 节标题铺开（含 3,309 个无史料节）＝**余 75 卷**（V01 已批）。本任务已拆为 76 个按卷任务组：

- 注册表 `taskgroups.tsv`（76 行；合计 544 章／3,957 节／15,206 件／168,225,093 B）。
- 任务卡 `V{NN}/task.md`（编号 76 张）。
- 二者由 `脚本与命令/build_title_taskgroups.py` 再生；`--check` 判漂移（当前 0）。

**本阶段只做标题**；无史料节的空骨架 `.md` 在全部 `title.ok` 齐备后统一建（收口步），本阶段不建。

## 二、任务定义

### 2.1 每卷产出（四件＋三件凭据）

| 文件 | 内容 |
| ---- | ---- |
| `映射/title-design/V{NN}.tsv` | 十列：`subsection_id`／`vol`／`chapter`／`section`／`title`／`thesis`／`order`／`source_count`／`sources`／`status` |
| `映射/title-evidence/V{NN}.tsv` | 八列：`subsection_id`／`query`／`url`／`source_type`／`tier`／`accessed`／`quote`／`conflict` |
| `映射/title-design/exceptions/V{NN}.tsv` | 五列：`subsection_id`／`kind`／`reason`／`proposal`／`status`（无例外不建） |
| `映射/title-design/V{NN}-标题呈审报告.md` | 规模、四源矩阵、缺口、例外、风险、批准请求 |
| `映射/parallel/title/V{NN}/claim` | 认领凭据（`O_CREAT` 与 `O_EXCL`，存在即让出） |
| `映射/parallel/title/V{NN}/counts.tsv` | 过程计数（只追加） |
| `映射/parallel/title/V{NN}/done.json` | 完成凭据（`titles`／`ledger_sha256`／`selftest_exit=0`） |

### 2.2 判据要点（机器下限，逐条对应第三十九件）

- **数量**：每节 2–12 条（中位 5–7）；同节字数极差 ≤14（去空格计）。
- **形态**：论题名词短语；禁日期起头；禁转述动词（宣布／指出／表示／认为／建议／询问／承认／强调／透露／提议／反驳／呼吁／质疑／回复／答复）；禁纯版本号；禁工序词（未判定／待定／杂项／空模板件）；长度 8–40。
- **字符**：中英、中数之间各一个半角空格；弯引号；句读全角；禁直角引号与 ASCII 引号；禁双空格与不可见字符；`Port` 术语按风格规范（禁“端口”误译）。
- **四源**：每条 ≥2 源（`史料`／`联网`／`目录`／`规则`）；含拉丁字母、标准号或四位年份的题 ≥3 源；**单源题不得批准**。
- **证据**：每条标题至少一行证据；`source_type` 四类、`tier` A／B／C、`accessed` 写 `YYYY-MM-DD`。
- **重复**：同节题名不重复；同卷基名“主 1＋从 ≤1”。

### 2.3 不做（越界即返工）

- 不写正文、不建小节 `.md`、不建空骨架。
- 不改 `outline.txt`／`index.html`／`targets.tsv`／`mapping.tsv`／`layout.tsv`。
- 不改他人卷台账；不写 `approvals.tsv`／`approved/`（合并者专属）。
- 不建旁路副本（`.bak`／`.pre`／`prebak`／`~`）；留痕只靠 Git。
- 不自行批准、不先斩后奏改节层；确需拆节走 P1 提案，呈 ykla 裁定。

## 三、文件地图（按阅读顺序）

| 顺序 | 文件 | 用途 | 读／写 |
| ---- | ---- | ---- | ------ |
| 1 | `00-编纂规则与格式规范/01-规则/小节建制与题名规则.md` | 阈值、J／P 判据、批准单位 | 读 |
| 2 | `05-卷册大纲/映射/title-design/风格规范.md` | 六族句式、术语、四源矩阵、台账 schema、八步 | 读 |
| 3 | `05-卷册大纲/映射/parallel/title/README.md` | 并行协议、写者边界、§七 任务组契约 | 读 |
| 4 | `05-卷册大纲/映射/parallel/title/taskgroups.tsv` | 本卷节数、件数、字节、估算区间 | 读 |
| 5 | `05-卷册大纲/映射/parallel/title/V{NN}/task.md` | 本卷任务卡 | 读 |
| 6 | `05-卷册大纲/目录/data/outline.txt` | 卷／章／节题与 `@@` 注（内容源） | 读 |
| 7 | `05-卷册大纲/映射/targets.tsv` | 节点：`level=sec` 的 `node_id` | 读 |
| 8 | `05-卷册大纲/映射/mapping.tsv` | `target_id` → `source_relpath`（旧料件） | 读 |
| 9 | `旧大纲-20261023/` | 旧料正文（块级摘要） | 读 |
| 10 | `映射/title-design/V01.tsv`、`title-evidence/V01.tsv` | 已批样板，照口径 | 读 |
| 11 | `00-…/脚本与命令/audit_title_consistency.py` | 第三十九件门禁 | 运行 |
| 12 | `00-…/脚本与命令/build_title_taskgroups.py` | 注册表／任务卡再生与 `--check` | 运行（维护者） |

## 四、每卷八步作业流程

**S1 认领**。在 `parallel/title/V{NN}/` 以 `O_CREAT|O_EXCL` 建 `claim`：

```text
session=<会话标识>
vol=V{NN}
claimed_at=<YYYY-MM-DDTHH:MM:SS>
```

已存在即让出；超 24 小时无 `done.json` 可接管，须追加 `superseded=<原会话>` 并记 `event=takeover`。

**S2 读目录与注**。只读 `outline.txt` 该卷段落（卷题、每章节题、`@@` 注）；记下节题所指范围与相邻节的分工声明，避免越级。

**S3 盘料**。用 `targets.tsv` 取该卷 `level=sec` 的 `node_id`，再用 `mapping.tsv` 的 `target_id` 找件；**只做“有无与边界”判读**，不逐块读正文。无件节记 0，不臆造。

**S4 拟题**。按风格规范 §二六族句式成题；每节先列论题候选再落字。三条硬约束：

- 同节同族、同粒度；
- 相邻节中心语轮换（形成／确立／分化／分野）；
- 无史料节标题**避用拉丁字母与四位年份**（否则两源状态下必踩“专名题 ≥3 源”）。

**S5 取证**。按风格规范 §七 填 `title-evidence`：目录源引 `outline.txt` 节题；规则源引条款号；史料源引 `source_relpath` 与块摘要；联网源只写**已实测**页面（URL＋层级＋访问日＋引文），聚合站只作线索（C 级）。

**S6 例外**。单源、无法命名、建议拆节、缺史料者逐条进 `exceptions/V{NN}.tsv`；缺史料一律 `corpus_gap`，`status=open`。

**S7 自检**。在该卷台账写完后跑：

```text
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/audit_title_consistency.py" --check
```

须 **FAIL 0**。某卷不合格会让全库变红，这是可见性，不是写冲突；只在本地卷内修。

**S8 完成凭据与呈审**。写 `done.json`（`titles` 等于台账行数、`ledger_sha256` 等于台账 SHA-256、`selftest_exit=0`），写 `V{NN}-标题呈审报告.md`，交合并者汇总呈 ykla。

## 五、x 会话并行协议

### 5.1 分工

本次派 **x**（①）个会话；每会话每轮认领 **x**（②）组，共 **x**（③）轮。

| 会话 | 本轮组号 | 卷数 | 备注 |
| ---- | -------- | ---- | ---- |
| `s1`…`sx`（④） | `TG-V{NN}`–`TG-V{NN}`（⑥） | x（②） | 组号连续分配，不跨会话抢组 |
| 合并者 | 不拟题 | — | 由 ykla 指定 1 个会话兼任，或另设第 5 个只做合并 |

分配原则：先做 **wave 1**（V02–V09），再依次推进；波次只是排班提示，组间无依赖。相邻卷（题域交叉者）尽量同会话连续做，减少术语漂移。

### 5.2 认领与轮次

- 每轮开工先建 `claim`；同一卷任何时刻只 1 个写者。
- 一轮结束只做两件事：写 `done.json`、向 ykla 报“本轮完成 x 卷＋门禁结果”；**不自行进下一轮**，等派单。
- 中途放弃或会话中断：`claim` 留 24 小时，新会话按接管规则续做，不重拟已定稿题。

### 5.3 提交与合并（唯一写者）

- **写手会话不提交 Git**：只把四件与三件凭据写进工作树。四人并发 `git add` 会抢 `index.lock`。
- **只有合并者提交**：按卷或按批，pathspec 限定本批文件；提交说明写明卷号、条数、证据行数、例外数、门禁结果。
- 合并者另负责：`approvals.tsv` 追加行（`kind=title`）、`approved/V{NN}.title.ok`（含 `ledger_sha256`）、里程碑 tag、长线块刷新。
- 若签名报 `No secret key`：用 `git -c gpg.program="C:/Program Files/GnuPG/bin/gpg.exe" commit …`（用本机 GnuPG，仍签名，不绕过）。
- 提交前 hook 会自动改弯引号、删零宽、CRLF→LF；commit-msg 会拦直角引号、大文件、根目录新增等，按提示修，不用 `--no-verify`。

### 5.4 冲突处理

| 情形 | 处置 |
| ---- | ---- |
| 两会话领到同卷 | 后到者 `claim` 失败即让出，改领下一组 |
| 门禁因他卷变红 | 只修本卷；他卷问题上报，不代改 |
| 台账需改题 | 改后重算 `ledger_sha256`，该卷批准作废、重批 |
| 结构需拆节 | 停手写 P1 提案，呈 ykla；未裁不得动节层 |

## 六、检查点（C0–C5）

| 检查点 | 时机 | 判据／命令 | 不过怎么办 |
| ------ | ---- | ---------- | ---------- |
| C0 开工 | 每轮开始 | `build_title_taskgroups.py --check` 漂移 0；`claim` 创建成功；§3 前 10 件已读 | 漂移则由维护者再生，不手改注册表 |
| C1 拟题中 | 每节落字后 | 条数 2–12；同节极差 ≤14；无动词起首；无日期起头 | 就地改题，不入台账 |
| C2 单卷收口 | 该卷四件写完 | `audit_title_consistency.py --check` **FAIL 0**；`done.json` 三判据齐 | 修到 0 再写 `done.json` |
| C3 合并 | 呈审后 | `title.ok` 的 `ledger_sha256` 与台账一致（H1）；`approvals.tsv` 有行（H2）；无 `draft` 残留（H3） | hash 不符即拒写，退回该卷 |
| C4 提交 | 合并者提交 | `git status` 仅本批文件；无旁路副本；说明含卷号与门禁 | 撤回暂存，重提 |
| C5 里程碑 | 每累计 **x**（⑤）卷 | 长线块 `--write-block` 后 `--check` 19 条一致；tag `outline-rollout-<卷>-<YYYYMMDD>` 逐卷打 | 差值由维护者刷新，不手改登记表 |

另三条每批必跑（不涉改动也跑）：`sync_refactor2026_baseline.py --check`、`_longline_status.py --check`、`audit_gate_registry.py`、`audit_sidecar_backup.py`。

## 七、tasks 清单

- [ ] T0 环境核对：`C:/Python314/python.exe` 可用；仓库根 `d:\librebsd`；`git status` 干净。
- [ ] T1 读毕 §3 的 1–10 件；在 `counts.tsv` 记 `event=start`。
- [ ] T2 按 §5.1 分配领取组号；每卷建 `claim`，记 `event=claim`。
- [ ] T3 逐卷 S2–S4：读目录、盘料、拟题；每节记 `event=draft`。
- [ ] T4 逐卷 S5–S6：填证据、判例外；记 `event=exception`。
- [ ] T5 逐卷 S7：跑门禁至 FAIL 0；记 `event=selfcheck`（含退出码）。
- [ ] T6 逐卷 S8：写 `done.json` 与呈审报告；记 `event=done`。
- [ ] T7 合并者：逐卷写 `title.ok` 与 `approvals.tsv` 行；打 tag；刷新长线块。
- [ ] T8 每轮收口：向 ykla 报本轮卷数、条数、证据行数、例外数、门禁结果、未决问题。

## 八、任务书与 specs 索引

| 件 | 路径 | 作用 |
| -- | ---- | ---- |
| 任务书 | `.trae/specs/rebuild-outline-subsection-layer-20261029/spec.md` | Why／What／Impact 与 SSOT |
| 任务分解 | `.trae/specs/rebuild-outline-subsection-layer-20261029/tasks.md` | Task 3A.6 条目与执行记录 |
| 检查清单 | `.trae/specs/rebuild-outline-subsection-layer-20261029/checklist.md` | 批次核对项 |
| 长线登记 | `01-项目管理/01-编纂规划与报告归档/长线任务总登记表.md` §十九（第 19 条 `title3a`） | 跨会话续跑与真值源 |
| 变更记录 | `01-项目管理/00-变更记录/changelog.duckdb` | 每批一行（合并者写） |
| 里程碑台账 | `05-卷册大纲/映射/里程碑tag台账.tsv` | tag 逐条登记 |

注：`.trae/specs/` 与 `specs/` 按项目裁决**不入库**，但文件在盘可读；不要在其中新建可持续依赖。

## 九、V01 实测坑位（反例十条）

1. 题名以“研究”“分析”“介绍”“说明”起首会被 B1 判死；“分析机的结构”因前缀“分析”也不行，改“巴贝奇分析机的存储与指令结构”。
2. 年代错置：写“从分时到个人计算的过渡”属 1980 年代，放到 1969 年前夜节即失据，改“从分时到小型机的过渡”。
3. 题域重叠：命名与版本编号归“Unics／Unix”节，不要写进实现节。
4. 商标与法律约束多在 1990 年代，早于该时段的命名节不要拿它立题。
5. 无史料节写含拉丁字母的题，会把源数下限从 2 抬到 3，直接 FAIL。
6. `corpus_gap` 不是“质量差”，是“该节旧树 0 件”；不要为了好看把史料数写成非零。
7. 同节六题字数相差超过 14 会被 D3 判死；长题要缩，短题要补中心语。
8. 全卷基名重复只能“主 1＋从 ≤1”，从者题末写“（另见 X）”。
9. 直角引号、ASCII 逗号／冒号／问号在题名里一律判死；句读用全角。
10. 引文与证据里的 URL 只写实测过的；查不到就换源或降级为 C，不要编。

## 十、验收与呈审

### 10.1 单卷验收

| 项 | 判据 |
| -- | ---- |
| 覆盖 | 该卷全部 `level=sec` 节点都有标题，节数等于任务卡 |
| 数量 | 每节 2–12 条 |
| 门禁 | 第三十九件 `--check` FAIL 0 |
| 凭据 | `done.json` 三判据齐，`ledger_sha256` 与磁盘一致 |
| 例外 | 无史料题逐条 `corpus_gap`；单源题为 0 |

### 10.2 批量呈审

- 每轮结束，合并者汇总“卷号／条数／证据行数／例外数／门禁结果”成一页呈 ykla。
- ykla 可按批一次签 x 卷，但 `title.ok` 仍**逐卷一份**、`approvals.tsv` 逐卷一行。
- 全部 75 卷 `title.ok` 齐备后，才进内容批；本阶段不建空骨架、不改页面。

## 附录 A 派单模板（复制后填 x）

```text
会话标识：<x④>
本轮组号：TG-V{NN}–TG-V{NN}（x⑥ 组，共 x② 卷）
轮次：第 <n>／x③ 轮
必读：§3 第 1–10 件；本会话各卷 V{NN}/task.md
产出：各卷 V{NN}.tsv＋title-evidence/V{NN}.tsv＋exceptions（按需）＋呈审报告＋claim/counts/done.json
禁写：approvals.tsv、approved/、outline.txt、index.html、他卷文件
收口：audit_title_consistency --check FAIL 0；done.json 三判据齐；向 ykla 报本轮结果
```

## 附录 B 命令速查

```text
# 注册表与任务卡漂移
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/build_title_taskgroups.py" --check

# 第三十九件（标题一致性）
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/audit_title_consistency.py" --check

# 常备四件
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/sync_refactor2026_baseline.py" --check
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/_longline_status.py" --check
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/audit_gate_registry.py"
C:/Python314/python.exe "00-编纂规则与格式规范/01-规则/脚本与命令/audit_sidecar_backup.py"

# 合并者提交（签名失败时用本机 GnuPG）
git -c gpg.program="C:/Program Files/GnuPG/bin/gpg.exe" commit -F <说明文件>
```

## 附录 C 交接自检（合并者在派单前跑）

- [ ] `build_title_taskgroups.py --check` 漂移 0。
- [ ] `audit_title_consistency.py --check` FAIL 0（当前 V01 单卷态）。
- [ ] `git status` 干净；`_longline_status.py --check` 19 条一致。
- [ ] 本批实际组数＝76 减已批卷数（当前 75），与派单数一致。
