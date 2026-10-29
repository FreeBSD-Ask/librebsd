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
