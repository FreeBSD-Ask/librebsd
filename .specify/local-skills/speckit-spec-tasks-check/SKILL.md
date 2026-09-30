---
name: "speckit-spec-tasks-check"
description: "一条命令出 Trae Spec 式产物（超集）：spec.md（规格）→ plan.md（实施计划）→ tasks.md（任务）→ checklist.md（验收检查点）。跳过 implement／converge，不建分支。输入＝需求描述。"
---

# speckit-spec-tasks-check：规格 → 计划 → 任务 → 检查点

一条命令落 Trae Spec 式产物，并含一个必需超集件 `plan.md`。前三个阶段**引用上游技能执行**（不复制逻辑，上游升级自动跟随）；第四阶段因语义与上游 checklist 不同，由本技能自含规则生成。

## 用户输入

```text
$ARGUMENTS
```

取本条消息正文为需求描述；`$ARGUMENTS` 显示为字面量时同理。为空则反问一次，不自行编造。

## 为什么必须有 plan.md

Spec Kit 的 `setup-tasks.ps1` 与 `check-prerequisites.ps1` 对 `plan.md` 是**硬依赖**（实测：缺失即 `ERROR: plan.md not found` 并以 exit 1 退出），`plan.md` 缺失时 tasks 段根本无法启动。故本技能把 plan 列为第四件的必需前置——它是超集件，且能为 tasks 提供结构信息（Tech Context／Project Structure）。

## 执行步骤

### 阶段一：规格（spec.md）

读取 `.zcode/skills/speckit-specify/SKILL.md` 全文，按其 Pre-Execution Checks、Outline 与 Mandatory Post-Execution Hooks **完整执行**一次，参数＝上述需求描述。产出：

- `spec.md` —— 需求规格
- `checklists/requirements.md` —— 其自带的规格质量清单（自动产物，保留）

产出后**不等待用户批准**，直接进入阶段二。唯一例外：出现 `[NEEDS CLARIFICATION]` 标记时，先把问题提给用户并等待回答再继续。

### 阶段二：计划（plan.md）

读取 `.zcode/skills/speckit-plan/SKILL.md` 全文并**完整执行**一次，输入同上 feature 目录。

- 阶段一产出 `[NEEDS CLARIFICATION]` 未解时不启动本阶段。
- 本阶段会调 `setup-plan.ps1` 生成 `plan.md` 骨架再填充；其 Research／Contracts 等附加件按上游技能自身判断产生，不额外强求。

### 阶段三：任务（tasks.md）

读取 `.zcode/skills/speckit-tasks/SKILL.md` 全文并**完整执行**一次。此时 `spec.md` 与 `plan.md` 均已就位，脚本硬依赖满足，按其正常路径执行即可。

### 阶段四：检查点（checklist.md）

在同一个 feature 目录生成 `checklist.md`，**验收检查点**语义——每项可由「通过／不通过」二值判定。生成规则：

1. **追溯**：spec.md 的每条需求与验收场景、tasks.md 的每个任务，都应有对应检查点；无对应者说明缺口，列出而不隐藏。
2. **可判定**：禁止「功能正常」「质量良好」「性能可接受」这类不可判定措辞；须写成可观察事实（含具体条件、数量、顺序、路径）。
3. **分层**：按「实现完整性 → 需求覆盖 → 边界与异常 → 既有功能未回归」四层组织。
4. **格式**：每条一行，形如 `- [ ] Check N: <可判定事实>（来源：spec FR-x／Task N）`。
5. **不勾选**：生成时一律 `[ ]`，勾选权归复核人。
6. **史料／考据类需求**：检查点须含「证据锚点可定位」（库名／主键／路径）与「原文照录未改写」类判据。

> 语义说明：本件与上游 `.zcode/skills/speckit-checklist/SKILL.md` 的产物**不同**——上游 checklist 是「需求质量的单元测试」（评判需求写得清不清楚），本件是「实现验收的检查点」（评判做没做到）。两者可并存：想要需求质量版就另跑 `/speckit-checklist`。

### 收尾报告

报告 feature 目录绝对路径 ＋ 四件清单（`spec.md`／`plan.md`／`tasks.md`／`checklist.md`）＋ 阶段三的 Completion Report 内容（任务总数、各故事任务数、可并行项、建议 MVP、格式校验）＋ `checklist.md` 条目数及其四层分布。

## 停止边界

- 产出 `specs/NNN-<slug>/` 下的四件（外加 specify 自带的 `checklists/requirements.md` 与 plan 段自行判断产生的附加件）。
- **不执行** `speckit-implement`／`speckit-converge`／`speckit-analyze`。
- **不建 git 分支**、不写业务代码、不改既有源文件。
- feature 目录已存在时先说明现状并询问续写还是新建，不静默覆盖。
