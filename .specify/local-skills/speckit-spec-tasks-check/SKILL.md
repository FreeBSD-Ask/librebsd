---
name: "speckit-spec-tasks-check"
description: "一条命令出 Trae Spec 式产物：spec.md（规格）→ plan.md（计划）→ tasks.md（任务）→ checklist.md（验收检查点）。自动适配两种环境——装了 Spec Kit 走上游完整管道，未装则用包内自带模板直出。不跑 implement／converge，不建分支。输入＝需求描述。"
---

# speckit-spec-tasks-check：规格 → 计划 → 任务 → 检查点

一条命令产出四件。**先判环境，再选路径**；两条路径产出相同的四件，区别只在是否复用 Spec Kit 的上游技能与脚本。

## 用户输入

```text
$ARGUMENTS
```

取本条消息正文为需求描述（`$ARGUMENTS` 显示为字面量时同理）；为空则反问一次需求，不要编造。

## 步骤 0：环境探测

1. 项目根存在 `.specify/templates/`，且 `.zcode/skills/speckit-specify/SKILL.md`、`speckit-plan/SKILL.md`、`speckit-tasks/SKILL.md` 三者均在 → 走**执行步骤 A**（Spec Kit 完整模式）。
2. 否则 → 走**执行步骤 B**（无 Spec Kit 模式）。

两条路径的产出目录一致：`specs/NNN-<slug>/`。`NNN` 为三位递增序号，扫描 `specs/` 现有目录取下一个可用号；无 `specs/` 目录则新建。同一需求只建一个 feature。

## 执行步骤 A（Spec Kit 完整模式）

### A1 规格（spec.md）

读取 `.zcode/skills/speckit-specify/SKILL.md` 全文，按其 Pre-Execution Checks、Outline 与 Mandatory Post-Execution Hooks **完整执行**一次，参数＝需求描述。产出 `spec.md` 与 `checklists/requirements.md`（后者为其自动产物，保留）。

### A2 计划（plan.md）

读取 `.zcode/skills/speckit-plan/SKILL.md` 全文并**完整执行**一次。

### A3 任务（tasks.md）

读取 `.zcode/skills/speckit-tasks/SKILL.md` 全文并**完整执行**一次。

### A4 检查点（checklist.md）

按下方「检查点生成规则」生成 `checklist.md`。**不用**上游 `speckit-checklist`——其语义是「需求质量的单元测试」（评判需求写得清不清楚，且明写 `[x]` 不代表实现完成），与本件「实现验收的检查点」不同。

> 阶段 A1 产出 `[NEEDS CLARIFICATION]` 时，先把问题提给用户并等待回答再继续；其余情况**不停顿等待批准**。

## 执行步骤 B（无 Spec Kit 模式）

四件均以本技能自带 `assets/` 下的模板为骨架填充。**`assets/` 与本 SKILL.md 同目录**——ZCode 会在可用技能清单中给出本 SKILL.md 的完整路径，取其所在目录即本技能目录（全局安装时形如 `~/.zcode/skills/speckit-spec-tasks-check/assets/`，项目级安装时形如 `<项目>/.zcode/skills/speckit-spec-tasks-check/assets/`）。模板取自 GitHub Spec Kit（MIT）。

### B1 规格（spec.md）

以 `assets/spec-template.md` 为骨架填入：

- **用户故事**：按 P1／P2／P3 优先级排序，每条**可独立验收**（只实现 P1 也应是可用的最小切片）；每条含验收场景。
- **功能需求**：编号 FR-1、FR-2…，每条**可判定**（能被「是／否」验证），不写「优化」「提升」这类不可判定措辞。
- **成功判据**：可度量、与实现细节无关。
- **假设与存疑**：未定细节写进 Assumptions；影响范围的重大歧义标 `[NEEDS CLARIFICATION: 具体问题]`，最多 3 条。

### B2 计划（plan.md）

以 `assets/plan-template.md` 为骨架填写。非软件项目可据实简化技术章节，但「范围／步骤／风险／验证方式」四项须齐。

### B3 任务（tasks.md）

以 `assets/tasks-template.md` 为骨架，按下列规则填：

- 按用户故事分组，每组含「目标／独立验收判据／任务列表」；
- 每条任务形如 `- [ ] T001 [P] [US1] 描述（涉及路径）`，`[P]` 标可并行（不同载体、无依赖）；
- 结尾给**依赖图**与**并行执行示例**；
- 任务粒度＝一个执行者能独立完成并自证完成的单元。

### B4 检查点（checklist.md）

按下方「检查点生成规则」生成。

## 检查点生成规则（A4／B4 通用）

1. **追溯**：spec 的每条需求与验收场景、tasks 的每条任务都要有对应检查点；无对应者列出并说明缺口，不隐藏。
2. **可判定**：禁止「功能正常」「质量良好」「性能可接受」这类措辞；须写成可观察事实（含具体条件、数量、顺序、路径）。
3. **分层组织**：按「实现完整性 → 需求覆盖 → 边界与异常 → 既有功能未回归」四层。
4. **格式**：每条一行，形如 `- [ ] Check N: <可判定事实>（来源：spec FR-x／Task N）`。
5. **不勾选**：生成时一律 `[ ]`；勾选权归复核人——`[x]` 表示该判据经复核通过。
6. **史料／考据类需求**：须含「证据锚点可定位」（库名／主键／路径）与「原文照录未改写」类判据。

## 收尾报告

报告 feature 目录绝对路径 ＋ 四件清单（`spec.md`／`plan.md`／`tasks.md`／`checklist.md`）＋ 任务总数／各故事任务数／可并行项／建议 MVP 范围 ＋ `checklist.md` 条目数及其四层分布。

## 停止边界

- 只产出四件（模式 A 另含上游自动件如 `checklists/requirements.md`）。
- **不执行** implement／converge／analyze；**不建 git 分支**；不写业务代码、不改既有源文件。
- feature 目录已存在时先说明现状并询问续写还是新建，不静默覆盖。
