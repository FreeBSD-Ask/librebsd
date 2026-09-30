---
name: "speckit-spec-tasks-check"
description: "一条命令出 Trae Spec 式三件套：spec.md（规格）→ tasks.md（任务）→ checklist.md（验收检查点）。跳过 plan／implement／converge，不建分支。输入＝需求描述。"
---

# speckit-spec-tasks-check：规格 → 任务 → 检查点

一条命令落 Trae Spec 式三件套。前两件**引用上游技能执行**（不复制逻辑，上游升级自动跟随）；第三件因语义与上游不同，由本技能自含规则生成。

## 用户输入

```text
$ARGUMENTS
```

取本条消息正文为需求描述；`$ARGUMENTS` 显示为字面量时同理。为空则反问一次，不自行编造。

## 执行步骤

### 阶段一：规格（spec.md）

读取 `.zcode/skills/speckit-specify/SKILL.md` 全文，按其 Pre-Execution Checks、Outline 与 Mandatory Post-Execution Hooks **完整执行**一次。产出（在其自建目录内）：

- `spec.md` —— 需求规格
- `checklists/requirements.md` —— 其自带的规格质量清单（自动产物，保留）

### 阶段二：任务（tasks.md）

读取 `.zcode/skills/speckit-tasks/SKILL.md` 全文并**完整执行**一次，输入同上目录。

- 该技能把 `plan.md` 列为 Required，本模式下无 plan.md 时按它自己的规定「Generate tasks based on what's available」处理：从 spec.md 的用户故事与需求直接派生，不臆造技术栈。
- 阶段一产出的 `[NEEDS CLARIFICATION]` 若未解，先问用户再继续；其余情况**不停顿等待批准**。

### 阶段三：检查点（checklist.md）

在同一个 feature 目录生成 `checklist.md`，**验收检查点**语义——每项可由「通过／不通过」二值判定。生成规则：

1. **追溯**：spec.md 的每条需求与验收场景、tasks.md 的每个任务，都应有对应检查点；无对应者说明缺口，列出而不隐藏。
2. **可判定**：禁止「功能正常」「质量良好」「性能可接受」这类不可判定措辞；须写成可观察事实（含具体条件、数量、顺序、路径）。
3. **分层**：按「实现完整性 → 需求覆盖 → 边界与异常 → 既有功能未回归」四层组织。
4. **格式**：每条一行，形如 `- [ ] Check N: <可判定事实>（来源：spec FR-x／Task N）`。
5. **不勾选**：生成时一律 `[ ]`，勾选权归复核人。
6. **史料／考据类需求**：检查点须含「证据锚点可定位」（库名／主键／路径）与「原文照录未改写」类判据。

> 说明：此件与上游 `.zcode/skills/speckit-checklist/SKILL.md` 的产物**语义不同**——上游 checklist 是「需求质量的单元测试」（评判需求写得清不清楚），本件是「实现验收的检查点」（评判做没做到）。两者可并存：想要需求质量版就另跑 `/speckit-checklist`。

### 收尾报告

报告 feature 目录绝对路径 ＋ 三件套清单 ＋ 阶段二的 Completion Report 内容（任务总数、各故事任务数、可并行项、建议 MVP、格式校验）＋ `checklist.md` 条目数及其四层分布。

## 停止边界

- 只产出 `specs/NNN-<slug>/` 下的三件套（外加 specify 自带的 `checklists/requirements.md`）。
- **不执行** `speckit-plan`／`speckit-implement`／`speckit-converge`。
- **不建 git 分支**、不写业务代码、不改既有源文件。
- feature 目录已存在时先说明现状并询问续写还是新建，不静默覆盖。
