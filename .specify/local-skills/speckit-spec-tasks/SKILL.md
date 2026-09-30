---
name: "speckit-spec-tasks"
description: "一步出任务：先按 speckit-specify 落规格（spec.md ＋ 需求质量清单），紧接着按 speckit-tasks 落任务清单（tasks.md），跳过 plan／implement／converge。用于「一句话需求 → 规格＋任务」两件产物的场景。输入＝需求描述。"
---

# speckit-spec-tasks：规格 → 任务（两阶段串接）

本技能是 `speckit-specify` 与 `speckit-tasks` 的**串接封装**：不复制两者逻辑，而是按序执行其原始定义，故上游升级后行为自动跟随。

## 用户输入

```text
$ARGUMENTS
```

用户在本条消息中给出的需求描述即输入（若 `$ARGUMENTS` 显示为字面量，直接取消息正文）。输入为空时反问一次需求，不要自行编造。

## 执行步骤

1. **阶段一（规格）**：读取 `.zcode/skills/speckit-specify/SKILL.md` 全文，按其 Pre-Execution Checks、Outline 与 Mandatory Post-Execution Hooks **完整执行**一次，参数＝上述需求描述。
2. **不要停顿确认**：阶段一完成并通过其规格质量校验后，**不等待用户批准**，直接进入阶段二。唯一例外：阶段一产出 `[NEEDS CLARIFICATION]` 标记时，先把问题提给用户并等待回答，再继续。
3. **阶段二（任务）**：读取 `.zcode/skills/speckit-tasks/SKILL.md` 全文，按其 Outline 与 Mandatory Post-Execution Hooks **完整执行**一次，输入＝阶段一同一个 feature 目录。
   - 该技能把 `plan.md` 列为 Required，但两阶段模式下通常没有 plan.md；此时按它自己的规定「Generate tasks based on what's available」处理——从 spec.md 的用户故事与需求直接派生任务，不臆造技术栈章节。
4. **收尾报告**：按阶段二技能规定的 Completion Report 输出（任务总数、各用户故事任务数、可并行项、建议 MVP 范围、格式校验结论），并附上 feature 目录的绝对路径。

## 停止边界（本封装的约束）

- 只产出三件：`specs/NNN-<slug>/spec.md`、`specs/NNN-<slug>/checklists/requirements.md`、`specs/NNN-<slug>/tasks.md`。
- **不执行** `speckit-plan`、`speckit-implement`、`speckit-converge`、`speckit-analyze`。
- **不建 git 分支**、不写业务代码、不修改既有源文件；需要建分支或改源时先问用户。
- 若目标 feature 目录已存在，先说明现状并询问是续写还是新建，不静默覆盖。
