---
spec_id: M
title: 任务书—specs 绑定协议
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: 十六、任务书—specs 绑定协议（G12）
version: 1.0.0
status: draft
goals: [12]
owner: ykla
created: 2026-11-27
updated: 2026-11-27
binding_id: TB-20261127-BIND
---

# Binding Protocol: 任务书—specs 绑定

> 目标 12 的判据正文。定义“什么算绑定”“如何证明”“如何变更”“边界在哪”。

## 1. 定义

**绑定**＝任务书与 spec 之间的四项同时成立：

1. **路径可定位**：spec frontmatter 的 `task_book` 指向存在的任务书；`task_book_anchor` 在任务书中可定位。
2. **内容可追溯**：spec 的 `goals` 覆盖任务书 §3 追溯矩阵中的目标；任务书 §3 反指 spec。
3. **快照可复算**：`BINDING.tsv` 记录每份 spec 三件套的 sha256；任一时点可复算。
4. **状态一致**：spec 的 `version`／`status`／`binding_id` 与清单一致。

四项缺一不称绑定；只有“互相写了路径”不构成绑定。

## 2. 目录与文件

```text
specs/006-toolchain-db-standardization/
├── spec.md                 # 总 spec（M）
├── plan.md
├── research.md
├── data-model.md
├── binding.md              # 本件
├── tasks.md
├── checklist.md
├── BINDING.tsv             # 机器可读清单
├── contracts/
│   ├── tool-registry.schema.json
│   ├── binding-manifest.schema.json
│   ├── quality-scorecard.schema.json
│   └── spec-frontmatter.schema.json
└── subspecs/
    ├── S01-standards-research/
    │   ├── spec.md
    │   ├── tasks.md
    │   └── checklist.md
    ├── ...
    └── S12-ocr-audio-toolchain/
```

## 3. Frontmatter 规范

每份 spec（含总 spec）必须以下列 YAML frontmatter 开头：

```yaml
---
spec_id: S01
title: 标准与规范调研
task_book: 01-项目管理/01-编纂规划与报告归档/工具链与数据库标准化-任务书-20261127.md
task_book_anchor: s01-标准与规范调研
version: 1.0.0
status: draft
goals: [1]
owner: ykla
created: 2026-11-27
updated: 2026-11-27
binding_id: TB-20261127-S01
---
```

字段约束：

| 字段 | 约束 |
| ---- | ---- |
| `spec_id` | M／S01—S12，唯一 |
| `task_book` | 相对仓库根路径，存在 |
| `task_book_anchor` | 任务书标题的 kebab-case 形式；须能唯一定位 |
| `version` | SemVer 2.0.0 |
| `status` | draft／active／closed／superseded |
| `goals` | 整数数组，元素 ∈ 1—12 |
| `created`／`updated` | ISO 8601 日期 |
| `binding_id` | `TB-20261127-<spec_id>` |

**锚点规则**：`task_book_anchor` 取任务书小节标题原文（去掉 `## ` 前缀），逐字匹配，含中文标点与编号。例如 `五、标准基线（种子；S01 执行时全量扩展）`。校验器按 `## <anchor>` 精确查找；若标题改名，绑定即失效，必须同步更新 spec。此规则避免 kebab-case 转写歧义，代价是锚点较长。

## 4. `BINDING.tsv` 规范

- 编码：UTF-8 无 BOM、LF。
- 分隔：制表符；首行表头；字段内不得含制表符／换行。
- 顺序：M、S01—S12。
- 哈希：文件原始字节的 sha256，小写 hex。
- 更新：任何 spec 修改后重算；任务书修改后检查锚点。

表头：

```text
binding_id	spec_id	goals	spec_path	spec_sha256	tasks_sha256	checklist_sha256	task_book_path	task_book_anchor	spec_version	status	updated_at
```

## 5. 校验器规格

**名称**：`audit_task_spec_binding.py`（执行期新建，须登记门禁与规则引用）。
**调用**：`python audit_task_spec_binding.py --check`；`--selftest`；`--json`。
**退出码**：0 PASS；1 FAIL；2 环境／格式错误。

### 5.1 判据 B1—B8

| 编号 | 判据 | 失败示例 |
| ---- | ---- | -------- |
| B1 | 每条 `spec_path`／`tasks`／`checklist` 存在 | 文件被删或改名 |
| B2 | 三件套 sha256 与清单一致 | 改了 spec 未更新清单 |
| B3 | 目标 1—12 并集覆盖完整；无重复 `binding_id`／`spec_id` | 漏了 G10 |
| B4 | 每份 spec 的 `task_book` 存在，`task_book_anchor` 可定位 | 任务书改名 |
| B5 | `BINDING.tsv` 表头完整、字段非空、哈希格式合法 | 少列 |
| B6 | 任务书内嵌摘要的 manifest 哈希与 `BINDING.tsv` 一致 | 清单更新未回填 |
| B7 | frontmatter 的 `version`／`status`／`binding_id` 与清单一致 | 双源漂移 |
| B8 | 无孤儿 spec（不在清单）与幽灵行（清单有、磁盘无） | 目录残留 |

### 5.2 自检（`--selftest`）

必须内置正反例：

- 正例：临时目录造 2 份 spec＋清单，B1—B8 全 PASS。
- 反例 1：篡改一个字节 → B2 FAIL。
- 反例 2：删除一份 spec → B1／B8 FAIL。
- 反例 3：清单漏一个目标 → B3 FAIL。
- 反例 4：任务书锚点改名 → B4 FAIL。
- 反例 5：清单版本与 frontmatter 不一致 → B7 FAIL。

自检不得触碰真实 `specs/`；在临时目录造夹具。

## 6. 变更流程

1. 改 spec → 更新 `updated`；按 SemVer 升 `version`（内容修订 patch；FR 变更 minor；范围变更 major）。
2. 重算三件套 sha256 → 更新 `BINDING.tsv` 对应行。
3. 重算 `BINDING.tsv` 全文件 sha256 → 回填任务书附录 C 的 manifest 哈希。
4. 若改任务书小节标题 → 检查所有 `task_book_anchor`；改名须同步 spec。
5. 跑 `audit_task_spec_binding.py --check`；PASS 后才算收口。
6. 变更记入 `changelog.duckdb`（若触及入库件）或批记录（若仅工作区）。

## 7. 版本与历史

- `BINDING.tsv` 是**当前快照**，不是历史。
- 历史由两层承担：任务书在 Git 中的提交历史；`changelog.duckdb` 的变更记录。
- 每次收口在任务书 §19 变更记录追加一行版本；重大变更在 `任务审计台账` 留痕。

## 8. 入库状态（已裁定）

### 8.1 现状

- 2026-11-27 ykla 令：`specs/` 不排除、进行跟踪。`.gitignore` 已由 `/specs` 改为 `!/specs/**`；`AGENTS.md` 已同步。
- `specs/001—006` 全部纳入 Git 跟踪；`.trae/specs/` 仍为工作区，不批量入库（现有 260 个目录）。
- `BINDING.tsv` 的 sha256 继续保留，用于跨会话漂移检测；Git 历史提供第二重留痕。

### 8.2 保留的防线

- B2 哈希：改 spec 未更新清单即 FAIL。
- B4 锚点：任务书改名即断链。
- B6 manifest：清单与任务书附录 C 不一致即 FAIL。
- B7 状态：frontmatter 与清单不一致即 FAIL。
- B8 孤儿／幽灵：磁盘与清单双向核对。
- 每批收口重算并更新任务书附录 C；Git 提交形成不可变点。

### 8.3 不做什么

- 不把历史 260 个 `.trae/specs` 批量入库。
- 不用 `.bak`／压缩包／旁路副本做“备份”（红线 12）。
- 不把 spec 正文复制进任务书正文（会形成双源）。

## 9. 验收

| 编号 | 判据 | 证据 |
| ---- | ---- | ---- |
| BND-01 | 任务书与 12 子 spec 全部存在 | 目录清单 |
| BND-02 | frontmatter 字段齐全 | 逐件解析 |
| BND-03 | `BINDING.tsv` 哈希全等 | 复算脚本 |
| BND-04 | 目标覆盖 100% | 清单并集 |
| BND-05 | 锚点全部可定位 | 校验器 B4 |
| BND-06 | 无孤儿／幽灵 | 校验器 B8 |
| BND-07 | 任务书附录 C 哈希一致 | 校验器 B6 |
| BND-08 | 变更流程有记录 | 任务书 §19 |

## 10. 限制

- 本协议是**工程绑定**，不是密码学签名；sha256 防意外漂移，不防恶意篡改。
- 若需更强保证，执行期可加 Git 签名提交或 Sigstore／SLSA provenance；那是另一层，不替代本协议。
- 绑定不证明 spec 内容正确；内容正确性由评审、测试与公理化承担。
