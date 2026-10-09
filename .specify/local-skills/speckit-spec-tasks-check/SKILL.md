---
name: "speckit-spec-tasks-check"
description: "一条命令出 Spec 式产物：spec.md（规格）→ plan.md（计划）→ tasks.md（任务）→ checklist.md（验收检查点）。项目未装 Spec Kit 时先自动安装（uv tool install specify-cli ＋ specify init，WorkBuddy AI 原生落点）。不跑 implement／converge，不建分支。输入＝需求描述。"
---

# speckit-spec-tasks-check：规格 → 计划 → 任务 → 检查点

一条命令产出四件。若目标项目尚未装 Spec Kit，**本技能会先装它**，再走上游管道执行。

本版语义已适配 **WorkBuddy AI 宿主**：目标项目内的上游技能落点为 `.workbuddy-ai/skills/`，本技能自身的全局落点为 `~/.workbuddy-ai/skills/speckit-spec-tasks-check/`（用户级，装一次所有项目可用）；对既有 ZCode 项目向后兼容（见步骤 0 的多目录探测与整合冲突守卫）。

## 用户输入

```text
$ARGUMENTS
```

取本条消息正文为需求描述（`$ARGUMENTS` 显示为字面量时同理）；为空则反问一次需求，不要编造。

## 步骤 0：环境探测与自动安装

### 就绪判据

项目根存在 `.specify/templates/`，且下列**技能目录候选**中，某**同一个**候选里 `speckit-specify/SKILL.md`、`speckit-plan/SKILL.md`、`speckit-tasks/SKILL.md` 三者均在：

| 优先级 | 技能目录候选 | 来源整合 | 说明 |
| ---- | ---- | ---- | ---- |
| 1 | `.workbuddy-ai/skills/` | `generic`（`--skills`） | **WorkBuddy AI 原生落点**，首选 |
| 2 | `.zcode/skills/` | `zcode` | ZCode 落点，兼容既有项目 |

取**优先级最高的命中候选**为本次的「技能目录」（下称 `<SKILLS_DIR>`）。两候选均未命中即「未就绪」。

### 整合冲突守卫（重要）

读取 `.specify/integration.json` 的 `installed_integrations`：

- **非空**（如 `["zcode"]`）→ 项目**已装整合**，**禁止**再执行 `specify init`。此时直接复用该整合已落地的技能目录（即在 `<SKILLS_DIR>` 中取实际存在者）进入「执行步骤」，并在收尾报告写明「复用既有整合，未重装」。
- **为空或 `.specify/` 不存在** → 视为可安装。

缘由：`specify init --force` 会按新整合重写 `.specify/integration.json` 并新增技能目录；在已有整合的项目上强行改用 `generic` 会改变项目既有整合状态，属非必要破坏。

### 分流

1. **已就绪** → 直接进「执行步骤」。
2. **未就绪且无既有整合** → 执行下方「安装 Spec Kit」，成功后复核判据并进「执行步骤」。
3. **未就绪但有既有整合** → 复用既有整合的技能目录；若该整合未产出所需三件，**停止并如实报告**缺口，不得自造模板替代。
4. **安装失败** → **停止并如实报告**失败原因与手工步骤，不得用自造模板等替代方案糊过去。

### 安装 Spec Kit（WorkBuddy AI 原生落点）

先补 PATH：`export PATH="$HOME/.local/bin:$PATH"`（Windows 上即 `C:\Users\<你>\.local\bin`）。

**第一步**：确认 `specify` 命令可用，否则装它（需 uv；无 uv 时先装 uv：`pip install uv`）。

```sh
uv tool install specify-cli
```

**第二步**：在**项目根**初始化。WorkBuddy **无官方 integration**，故以 `generic` 整合 ＋ `--skills` 显式指定 WorkBuddy 原生技能落点：

```sh
specify init --here --integration generic --integration-options="--commands-dir .workbuddy-ai/skills/ --skills" --non-interactive --force --ignore-agent-tools
```

参数说明（缺一即落点不对或失败）：

- `--integration generic` ＋ `--integration-options="--commands-dir .workbuddy-ai/skills/ --skills"`：三者共同构成 WorkBuddy 原生布局，产出 `.workbuddy-ai/skills/speckit-<name>/SKILL.md`（agentskills.io 规范）。已实测 specify-cli 1.0.13 可用；
- `--here` 与项目名**互斥**（同时给报 `Cannot specify both project name and --here flag`）；
- 目录非空时非交互模式必须 `--force`（否则报 `Current directory is not empty and --non-interactive was set`）；
- `--ignore-agent-tools` 跳过「检测不到 agent 可执行文件」的检查——该检查只影响自检提示，不影响功能。

**第三步**：复核就绪判据已满足，并报告装了什么（specify-cli 版本、在项目里新建了哪些路径、`.specify/integration.json` 的 `integration` 值）。

**注意**：新装的上游技能在**当前会话内不一定被注册**（技能清单于会话启动时扫描）——这不影响本技能，因为「执行步骤」是**直接读取其 SKILL.md 文件并执行**，不依赖技能注册。

## 执行步骤

以下三处对上游技能定义的读取，路径均为 `<SKILLS_DIR>`（即步骤 0 探测所得者）。

### 一、规格（spec.md）

读取 `<SKILLS_DIR>/speckit-specify/SKILL.md` 全文，按其 Pre-Execution Checks、Outline 与 Mandatory Post-Execution Hooks **完整执行**一次，参数＝需求描述。产出：

- `spec.md` —— 需求规格
- `checklists/requirements.md` —— 其自带的规格质量清单（自动产物，保留）

产出后**不等待用户批准**，直接进入下一步。唯一例外：出现 `[NEEDS CLARIFICATION]` 标记时，先把问题提给用户并等待回答再继续。

### 二、计划（plan.md）

读取 `<SKILLS_DIR>/speckit-plan/SKILL.md` 全文并**完整执行**一次。

`plan.md` **不可省**：`setup-tasks.ps1` 与 `check-prerequisites.ps1` 对它是硬依赖（实测：缺失即 `ERROR: plan.md not found` 并 exit 1），tasks 段根本无法启动。

### 三、任务（tasks.md）

读取 `<SKILLS_DIR>/speckit-tasks/SKILL.md` 全文并**完整执行**一次。此时 `spec.md` 与 `plan.md` 均已就位，脚本硬依赖满足，走其正常路径。

### 四、检查点（checklist.md）

在同一个 feature 目录生成 `checklist.md`，**验收检查点**语义——每项可由「通过／不通过」二值判定。**不用**上游 `speckit-checklist`：其语义是「需求质量的单元测试」（评判需求写得清不清楚，且明写 `[x]` 不代表实现完成），与本件不同。生成规则：

1. **追溯**：spec 的每条需求与验收场景、tasks 的每条任务都要有对应检查点；无对应者列出并说明缺口，不隐藏。
2. **可判定**：禁止「功能正常」「质量良好」「性能可接受」这类措辞；须写成可观察事实（含具体条件、数量、顺序、路径）。
3. **分层组织**：按「实现完整性 → 需求覆盖 → 边界与异常 → 既有功能未回归」四层。
4. **格式**：每条一行，形如 `- [ ] Check N: <可判定事实>（来源：spec FR-x／Task N）`。
5. **不勾选**：生成时一律 `[ ]`；勾选权归复核人——`[x]` 表示该判据经复核通过。
6. **史料／考据类需求**：须含「证据锚点可定位」（库名／主键／路径）与「原文照录未改写」类判据。

## 收尾报告

报告 feature 目录绝对路径 ＋ 四件清单（`spec.md`／`plan.md`／`tasks.md`／`checklist.md`）＋ 任务总数／各故事任务数／可并行项／建议 MVP 范围 ＋ `checklist.md` 条目数及其四层分布 ＋（若本次触发过自动安装或复用既有整合）相应摘要与 `<SKILLS_DIR>` 实际取值。

## 停止边界

- 产出 `specs/NNN-<slug>/` 下的四件（另含上游自动件如 `checklists/requirements.md`）。
- **不执行** implement／converge／analyze；**不建分支**；不写业务代码、不改既有源文件。
- feature 目录已存在时先说明现状并询问续写还是新建，不静默覆盖。
- 安装 Spec Kit 是本技能唯一的写系统动作，仅在做「未就绪且无既有整合」时执行一次。
