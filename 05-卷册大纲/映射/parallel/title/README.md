# 小节标题线·按卷并行执行协议（2026-10-29 立）

> **性质**：本文件是 Task 3A“小节标题设计”按卷并行会话的**执行体制说明**，规定分片单元、三件协议、写者边界与合并者职责。
> **依据**：`小节建制与题名规则` §七（1 卷 1 批、多会话只处理不同卷、全局文件单写者）＋`.trae/specs/rebuild-outline-subsection-layer-20261029/tasks.md` Task 3A.0。
> **不设自动化**：本项目禁止定时／循环任务（2026-09-16 ykla 裁定）；并行由人在场的多会话手动推进。

## 一、分片单元

分片键＝**卷**（V01–V76）。同一卷同一时刻只允许一个会话写；不同卷可同时推进。

目录布局：

```text
05-卷册大纲/映射/parallel/title/
├── README.md            # 本文件（协议，全局唯一）
├── V01/
│   ├── claim            # 认领凭据（原子创建；存在即被占）
│   ├── done.json        # 完成凭据（含计数、台账 hash、时间）
│   └── counts.tsv       # 过程计数（节数／已拟题／例外数／自检退出码）
├── V02/
└── …
```

## 二、三件协议

### 2.1 `claim`（认领，原子排他）

- 创建方式：`O_CREAT|O_EXCL`（原子创建；已存在即失败，不得覆盖）。
- 内容三行：

```text
session=<会话标识>
vol=V01
claimed_at=<YYYY-MM-DDTHH:MM:SS>
```

- **陈旧接管**：`claimed_at` 超过 24 小时且无 `done.json` 者，可由新会话接管；接管须重写 `claim` 并在第四行追加 `superseded=<原会话>`，同时在 `counts.tsv` 记一行 `event=takeover`。

### 2.2 `done.json`（完成凭据）

```json
{
  "vol": "V01",
  "sections": 8,
  "titles": 43,
  "exceptions": 2,
  "ledger_sha256": "<title-design/V01.tsv 的 SHA-256>",
  "selftest_exit": 0,
  "finished_at": "YYYY-MM-DDTHH:MM:SS",
  "session": "<会话标识>"
}
```

判据：`titles` 与台账行数相等；`ledger_sha256` 与磁盘文件一致；`selftest_exit=0`；缺一不写 `done.json`。

### 2.3 `counts.tsv`（过程计数）

列：`at`｜`event`｜`sections_done`｜`titles_done`｜`exceptions_open`｜`note`
`event` ∈ {start, claim, takeover, draft, exception, selfcheck, done}
只追加，不覆盖。

## 三、写者边界

| 文件 | 写者 |
| ---- | ---- |
| `title-design/V{NN}.tsv` | 该卷会话（唯一） |
| `title-evidence/V{NN}.tsv` | 该卷会话（唯一） |
| `title-design/exceptions/V{NN}.tsv` | 该卷会话（唯一） |
| `parallel/title/V{NN}/` 三件 | 该卷会话（唯一） |
| `title-design/approvals.tsv` | **合并者**（全局单写者） |
| `title-design/approved/V{NN}.title.ok` | **合并者**（凭 ykla 批准后写） |
| `title-design/风格规范.md`、本文件 | 全局单写者（改前须报批） |

禁止：跨卷写他人台账；改全局文件；在他人卷目录内建文件。

## 四、合并者职责

1. 校验该卷 `done.json` 三项判据齐备（行数、hash、自检 0）。
2. 校验 `approved/V{NN}.title.ok` 的 `ledger_sha256` 与台账一致；不一致拒写并退回该卷。
3. 追加 `approvals.tsv` 一行（`kind=title`）。
4. 全局文件改动由合并者单笔提交；`commit.lock`（`映射/commit.lock`）`O_CREAT|O_EXCL` 串行化，24 小时陈旧可接管并留痕。
5. 合并者不参与该卷拟题（不得既写又批）。

## 五、批次边界

- **1 卷 1 批**：该卷 `title.ok` 落定即该卷标题批收口，打 `outline-rollout-<卷>-<YYYYMMDD>` tag（与内容批共用同一 tag 序列；标题批单独收口者记 `-t` 后缀）。
- **全量约束**：全部 76 卷 `title.ok` 齐备前，内容批不得开工（规则 §七.3）。
- **失败批**：不打 tag；`counts.tsv` 记 `event=selfcheck` 与退出码；修复后重跑，不新增 `claim`。

## 六、与内容批的接口

- 内容批（Task 8）取本卷 `title-design/V{NN}.tsv` 与 `title-evidence/V{NN}.tsv`，核对 `title.ok` 与 `ledger_sha256` 后才研读史料。
- 标题表冻结后不得增删改题；确需改者，走“新增一行＋废前行”，并重批该卷。

## 七、按卷任务组（Task 3A.6 的拆分，2026-10-29 立）

3A.6（全 3,951 节标题铺开）拆为 **76 个按卷任务组**，组间**无写依赖**，可同时交给不同会话。

### 7.1 注册表与任务卡

- 注册表：`taskgroups.tsv`（76 行，机器可读；列含组号、卷号、卷题、章节数、`mapping.tsv` 命中 0 行的节数、旧料件数与字节、标题估算区间、波次、状态、产出路径）。
- 任务卡：`V{NN}/task.md`（每卷一卡，自足交接：范围、产出、禁止、作业顺序）。
- 交接书（给外部执行体，含流程、检查点、tasks 与反例）：`ZCode交接书-3A.6.md`。
- 二者由固定脚本再生，不得手改：`python 00-编纂规则与格式规范/01-规则/脚本与命令/build_title_taskgroups.py`；`--check` 只比对不写盘（漂移 exit 1）。

口径提示：`no_corpus_sections` 指 `mapping.tsv` 命中 0 行的节，与标题层 `corpus_gap` 例外（逐题登记，V01 为 231 条）口径不同；组内拟题时以实际题数为准。

### 7.2 独立性契约（组间零写冲突）

| 资源 | 归属 | 组可否写 |
| ---- | ---- | -------- |
| `title-design/V{NN}.tsv`、`title-evidence/V{NN}.tsv`、`exceptions/V{NN}.tsv`、`V{NN}-标题呈审报告.md` | 该卷组 | 可（唯一） |
| `parallel/title/V{NN}/` 三件 | 该卷组 | 可（唯一） |
| `approvals.tsv`、`approved/V{NN}.title.ok` | 合并者 | 否 |
| `taskgroups.tsv`、`V{NN}/task.md`、本文件、风格规范 | 维护者 | 否 |
| `outline.txt`、`index.html`、树内 `.md`、`targets.tsv`、`mapping.tsv` | 结构批／镜像线 | 否 |

因此任一组开工不需等待他组；唯一共享读取是 `audit_title_consistency.py --check`（读全部 `V*.tsv`），故某组台账不合规会让全库检查变红——属**可见性**而非写冲突，修复只在本地组内完成。

### 7.3 组内完成判据（DoD）

1. 该卷全部节均有标题，每节 2–12 条，同节字数极差 ≤14。
2. `audit_title_consistency.py --check` FAIL 0。
3. `done.json` 三判据齐（行数＝titles、`ledger_sha256` 一致、`selftest_exit=0`）。
4. 呈 ykla 卷级批准；合并者写 `title.ok` 与 `approvals.tsv` 行后该组收口。
5. 无史料节逐题登记 `corpus_gap`，不写正文、不建 `.md`（空骨架属 3A.6 收口步）。

### 7.4 排班建议

- 波次（`wave`）仅提示：V02–V09 为第 1 波，其后每 8 卷一波；波内各组可任意并发。
- 建议同时开工不超过执行环境的终端上限；同一卷任何时刻只允许 1 个写者（`claim` 排他）。
- 相邻卷（同章题域交叉者）宜由同一会话连续做，以减少术语漂移；但这不是依赖，跨会话亦可。
